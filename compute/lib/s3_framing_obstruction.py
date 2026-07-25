r"""Typed primary-framing data for Calabi--Yau threefold examples.

The module computes four mathematically distinct layers.

1. Hodge and HKR dimensions are exact finite calculations.
2. A chosen symplectic structure-group model has primary test-sphere
   group

       pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0.

   This calculation supplies one topological input to a framing problem.
3. The Euler scalar chi(X)/24 is recorded as a scalar shadow.
4. A categorical framing, a represented BV obstruction cochain, its
   trivialization, and a three-dimensional framing-anomaly comparison
   are separate construction data.

The last layer remains ``None`` until the caller supplies represented
chain data and the corresponding comparison maps.  In particular, a
rational Euler scalar occupies Q, whereas a BV obstruction occupies the
cohomology of a deformation complex; the two acquire a relation through
an explicit scalar-projection theorem.

The function names retain the historical API.  Their return values use
the object separation above.  The module therefore supports numerical
Hodge checks and explicit construction-state transitions while leaving
the CY3-to-chiral functor as a conditional construction problem.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple


# =========================================================================
# Section 1: Homotopy groups of classifying spaces
# =========================================================================

def pi_k_BO(k: int, n: int) -> str:
    r"""Return the low-degree homotopy group ``pi_k(BO(n))``.

    The loop equivalence ``Omega BO(n) ~= O(n)`` gives
    ``pi_k BO(n) = pi_{k-1} O(n)`` for positive ``k``.  The explicit
    unstable values through degree four are included; higher values are
    returned in the stable range.
    """
    if n < 1:
        return "trivial"

    if k == 0:
        return "0"
    elif k == 1:
        return "Z/2" if n >= 1 else "0"
    elif k == 2:
        if n == 1:
            return "0"
        if n == 2:
            return "Z"
        return "Z/2"
    elif k == 3:
        return "0"
    elif k == 4:
        if n <= 2:
            return "0"
        if n == 3:
            return "Z"
        if n == 4:
            return "Z+Z"
        return "Z"
    elif k <= 8 and n >= k + 2:
        # pi_k(BO) = pi_{k-1}(O), with stable O-pattern
        stable_o = ["Z/2", "Z/2", "0", "Z", "0", "0", "0", "Z"]
        return stable_o[(k - 1) % 8]
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

    In degree three this gives ``pi_3(BGL(C)) = 0``, the complex-linear
    primary test-sphere input used below.
    """
    return pi_k_BU(k)


# =========================================================================
# Section 2: CY3 Hodge data and structure groups
# =========================================================================

class CY3HodgeData(NamedTuple):
    """Hodge data for a CY threefold, with an optional HKR vector.

    The default Hochschild vector applies to strict Calabi--Yau
    threefolds with H^1(O_X)=H^2(O_X)=0.  Products such as K3 x E
    carry additional holomorphic forms; their HKR vector is supplied
    explicitly and controls the total dimension.
    """
    h11: int   # h^{1,1}
    h21: int   # h^{2,1}
    name: str = ""
    hh_vector_override: Tuple[int, ...] = ()

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
        """Total dimension of Hochschild (co)homology."""

        return sum(self.hh_cohomology_vector)

    @property
    def hh_cohomology_vector(self) -> Tuple[int, ...]:
        """Return the degree-zero-through-six HKR dimensions.

        For a strict CY3 the HKR decomposition gives
        (1, 0, h21, 2+2*h11, h21, 0, 1).  An explicit product vector
        takes precedence.
        """

        if self.hh_vector_override:
            return self.hh_vector_override
        return (1, 0, self.h21, 2 + 2 * self.h11, self.h21, 0, 1)

    @property
    def symplectic_rank(self) -> int:
        """Rank of the symplectic Gauss--Manin local system ``H^3(X)``."""

        return self.h3

    @property
    def euler_scalar(self) -> Fraction:
        """Return the rational Euler scalar ``chi(X)/24``."""

        return Fraction(self.euler, 24)

    @property
    def kappa_bcov(self) -> Fraction:
        """Historical API alias for :attr:`euler_scalar`."""

        return self.euler_scalar


# Standard CY3 examples
QUINTIC = CY3HodgeData(h11=1, h21=101, name="quintic")
K3_TIMES_E = CY3HodgeData(
    h11=21,
    h21=21,
    name="K3xE",
    hh_vector_override=(1, 2, 23, 44, 23, 2, 1),
)
MIRROR_QUINTIC = CY3HodgeData(h11=101, h21=1, name="mirror_quintic")


class ConifoldData(NamedTuple):
    """Local chart inputs for the resolved conifold."""
    name: str = "resolved_conifold"
    chi_compact: int = 2
    kappa: Fraction = Fraction(1)


class C3Data(NamedTuple):
    """Local chart inputs for affine three-space."""
    name: str = "C^3"
    chi: int = 1  # ordinary Euler characteristic of the affine variety
    kappa: Fraction = Fraction(0)  # supplied chart scalar


# =========================================================================
# Section 3: S^d-framing obstruction computation
# =========================================================================

@dataclass(frozen=True)
class RepresentedBVClass:
    """A finite-window cocycle in a named deformation complex.

    ``incoming_differential`` and ``outgoing_differential`` are the two
    adjacent matrices.  The constructor checks their composite.  A
    supplied ``scalar_functional`` annihilates the incoming image, hence
    descends to cohomology.  The cocycle equation and scalar projection
    are therefore computed from compatible chain data.
    """

    complex_name: str
    degree: int
    basis: Tuple[str, ...]
    coefficients: Tuple[Fraction, ...]
    incoming_basis: Tuple[str, ...]
    incoming_differential: Tuple[Tuple[Fraction, ...], ...]
    outgoing_differential: Tuple[Tuple[Fraction, ...], ...]
    scalar_functional: Optional[Tuple[Fraction, ...]] = None

    def __post_init__(self) -> None:
        if len(self.basis) != len(self.coefficients):
            raise ValueError("basis and coefficient vectors must have equal length")
        if len(self.incoming_differential) != len(self.basis):
            raise ValueError("the incoming differential must have one row per basis element")
        if any(len(row) != len(self.incoming_basis) for row in self.incoming_differential):
            raise ValueError("each incoming row must act on the incoming basis")
        if any(len(row) != len(self.coefficients) for row in self.outgoing_differential):
            raise ValueError("each differential row must act on the coefficient vector")
        if self.scalar_functional is not None and len(self.scalar_functional) != len(
            self.coefficients
        ):
            raise ValueError("the scalar functional must act on the coefficient vector")
        for outgoing_row in self.outgoing_differential:
            for incoming_column in range(len(self.incoming_basis)):
                composite_entry = sum(
                    outgoing_row[index]
                    * self.incoming_differential[index][incoming_column]
                    for index in range(len(self.basis))
                )
                if composite_entry != 0:
                    raise ValueError("adjacent differentials must satisfy d^2=0")
        if self.scalar_functional is not None:
            for incoming_column in range(len(self.incoming_basis)):
                boundary_value = sum(
                    self.scalar_functional[index]
                    * self.incoming_differential[index][incoming_column]
                    for index in range(len(self.basis))
                )
                if boundary_value != 0:
                    raise ValueError(
                        "the scalar functional must annihilate incoming boundaries"
                    )

    @property
    def boundary(self) -> Tuple[Fraction, ...]:
        """Apply the outgoing differential to the represented cochain."""

        return tuple(
            sum(entry * coefficient for entry, coefficient in zip(row, self.coefficients))
            for row in self.outgoing_differential
        )

    @property
    def is_cocycle(self) -> bool:
        """Check the finite-window cocycle equation."""

        return all(entry == 0 for entry in self.boundary)

    @property
    def scalar_projection(self) -> Optional[Fraction]:
        """Evaluate the represented scalar functional when supplied."""

        if self.scalar_functional is None:
            return None
        return sum(
            entry * coefficient
            for entry, coefficient in zip(self.scalar_functional, self.coefficients)
        )


@dataclass(frozen=True)
class RepresentedNullHomotopy:
    """A finite-window cochain whose differential is the BV cocycle."""

    complex_name: str
    degree: int
    source_basis: Tuple[str, ...]
    target_basis: Tuple[str, ...]
    coefficients: Tuple[Fraction, ...]
    outgoing_differential: Tuple[Tuple[Fraction, ...], ...]

    def __post_init__(self) -> None:
        if len(self.source_basis) != len(self.coefficients):
            raise ValueError("source basis and coefficient vectors must have equal length")
        if len(self.target_basis) != len(self.outgoing_differential):
            raise ValueError("the differential must have one row per target basis element")
        if any(len(row) != len(self.coefficients) for row in self.outgoing_differential):
            raise ValueError("each differential row must act on the homotopy coefficients")

    @property
    def image(self) -> Tuple[Fraction, ...]:
        """Apply the differential to the represented homotopy."""

        return tuple(
            sum(entry * coefficient for entry, coefficient in zip(row, self.coefficients))
            for row in self.outgoing_differential
        )

    def trivializes(self, cocycle: RepresentedBVClass) -> bool:
        """Check ``d(h)=c`` with matching complex, degree, and basis."""

        return (
            self.complex_name == cocycle.complex_name
            and self.degree + 1 == cocycle.degree
            and self.source_basis == cocycle.incoming_basis
            and self.target_basis == cocycle.basis
            and self.outgoing_differential == cocycle.incoming_differential
            and self.image == cocycle.coefficients
        )


@dataclass(frozen=True)
class FramingAnomalyComparison:
    """A chosen unit-framing convention for a named three-dimensional theory."""

    theory_name: str
    unit_framing_normalization: Fraction

    def evaluate(self, scalar: Fraction) -> Fraction:
        """Apply the represented linear comparison to a scalar input."""

        return self.unit_framing_normalization * scalar


class FramingObstruction(NamedTuple):
    """Typed output of the primary structure-group calculation."""
    cy_dim: int                          # d
    name: str                            # name of the CY
    structure_group: str                 # O(n), Sp(2m), GL(n,C), etc.
    obstruction_group: str               # pi_d(BG)
    topological_obstruction: int         # integer class (0 = vanishes)
    scalar_shadow: Fraction              # Euler/modular scalar in Q
    chain_level_obstruction: str         # deformation-complex problem
    bv_obstruction_class: Optional[RepresentedBVClass]
    scalar_projection_agrees: Optional[bool]
    null_homotopy: Optional[RepresentedNullHomotopy]
    trivialization_exists: Optional[bool]
    trivialization_data: str
    framing_comparison: Optional[FramingAnomalyComparison]
    framing_anomaly: Optional[Fraction]
    bv_cocycle_supplied: bool
    trivialization_supplied: bool
    framing_anomaly_supplied: bool


def s_d_framing_obstruction(d: int, name: str, **kwargs: Any) -> FramingObstruction:
    """Compute a primary classifying-space input and construction state.

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
        Typed primary and chain-construction data.
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
    """Primary connected-structure-group input in CY dimension one."""
    return FramingObstruction(
        cy_dim=1,
        name=name,
        structure_group="GL(2, C)",
        obstruction_group="pi_1(BGL(2,C)) = 0",
        topological_obstruction=0,
        scalar_shadow=Fraction(0),
        chain_level_obstruction="cyclic/framing comparison in the chosen model",
        bv_obstruction_class=None,
        scalar_projection_agrees=None,
        null_homotopy=None,
        trivialization_exists=None,
        trivialization_data="represented cyclic structure and framing comparison",
        framing_comparison=None,
        framing_anomaly=None,
        bv_cocycle_supplied=False,
        trivialization_supplied=False,
        framing_anomaly_supplied=False,
    )


def _framing_obstruction_d2(name: str, **kwargs: Any) -> FramingObstruction:
    """Primary first-Chern-class input in CY dimension two."""
    rank = kwargs.get("mukai_rank", 24)  # default K3 Mukai rank
    return FramingObstruction(
        cy_dim=2,
        name=name,
        structure_group=f"GL({rank}, C)",
        obstruction_group=f"pi_2(BGL({rank},C)) = Z (first Chern class)",
        topological_obstruction=0,
        scalar_shadow=Fraction(0),
        chain_level_obstruction="categorical framing comparison beyond c_1(TX)=0",
        bv_obstruction_class=None,
        scalar_projection_agrees=None,
        null_homotopy=None,
        trivialization_exists=None,
        trivialization_data="represented categorical framing and comparison map",
        framing_comparison=None,
        framing_anomaly=None,
        bv_cocycle_supplied=False,
        trivialization_supplied=False,
        framing_anomaly_supplied=False,
    )


def _framing_obstruction_d3(name: str, **kwargs: Any) -> FramingObstruction:
    """Compute the primary ``pi_3(BSp)`` input and construction state.

    The caller may supply ``represented_bv_class``, ``null_homotopy``,
    and a typed ``framing_comparison``.
    The default
    output records the exact scalar shadow while retaining the
    deformation-complex and anomaly lanes as open construction data.
    """
    h11 = kwargs.get("h11", 0)
    h21 = kwargs.get("h21", 0)
    chi = kwargs.get("chi", 2 * (h11 - h21))
    kappa = kwargs.get("kappa", None)
    compact = kwargs.get("compact", True)
    rigid = kwargs.get("rigid", h21 == 0 and h11 == 0)
    represented_bv_class = kwargs.get("represented_bv_class")
    null_homotopy = kwargs.get("null_homotopy")
    framing_comparison = kwargs.get("framing_comparison")

    if represented_bv_class is not None and not isinstance(
        represented_bv_class, RepresentedBVClass
    ):
        raise TypeError("represented_bv_class must be a RepresentedBVClass")
    if represented_bv_class is not None and represented_bv_class.is_cocycle is False:
        raise ValueError("the represented BV cochain must satisfy the cocycle equation")
    if null_homotopy is not None and not isinstance(
        null_homotopy, RepresentedNullHomotopy
    ):
        raise TypeError("null_homotopy must be a RepresentedNullHomotopy")
    if framing_comparison is not None and not isinstance(
        framing_comparison, FramingAnomalyComparison
    ):
        raise TypeError("framing_comparison must be a FramingAnomalyComparison")
    if null_homotopy is not None:
        if represented_bv_class is None:
            raise ValueError("a null-homotopy requires a represented BV class")
        if null_homotopy.trivializes(represented_bv_class) is False:
            raise ValueError("the supplied homotopy must satisfy d(h)=c")

    if kappa is None:
        if compact and chi != 0:
            kappa = Fraction(chi, 24)
        else:
            kappa = Fraction(0)

    framing_anomaly = chern_simons_framing_anomaly(
        kappa,
        comparison=framing_comparison,
    )
    scalar_projection = (
        represented_bv_class.scalar_projection
        if represented_bv_class is not None
        else None
    )
    scalar_projection_agrees = (
        scalar_projection == kappa if scalar_projection is not None else None
    )

    symplectic_rank = 2 * (1 + h21) if compact else 0
    rigidity_clause = "rigid local model" if rigid else "varying CY3 family"
    bv_obs = (
        f"represented cocycle in the CY3 deformation complex for the "
        f"{rigidity_clause}; Euler scalar shadow = {kappa}"
    )
    triv_data = (
        "represented holomorphic Chern--Simons functional, BV comparison "
        "map, and an explicit null-homotopy in the chosen completion"
    )

    sg = (
        f"Sp({symplectic_rank}, C)"
        if symplectic_rank > 0
        else "chosen local symplectic model"
    )

    return FramingObstruction(
        cy_dim=3,
        name=name,
        structure_group=sg,
        obstruction_group=(
            f"pi_3(B{sg}) = pi_2({sg}) = 0"
            if symplectic_rank > 0
            else "pi_3(BSp(2m)) = 0 for each supplied finite rank m >= 1"
        ),
        topological_obstruction=0,
        scalar_shadow=kappa,
        chain_level_obstruction=bv_obs,
        bv_obstruction_class=represented_bv_class,
        scalar_projection_agrees=scalar_projection_agrees,
        null_homotopy=null_homotopy,
        trivialization_exists=True if null_homotopy is not None else None,
        trivialization_data=triv_data,
        framing_comparison=framing_comparison,
        framing_anomaly=framing_anomaly,
        bv_cocycle_supplied=represented_bv_class is not None,
        trivialization_supplied=null_homotopy is not None,
        framing_anomaly_supplied=framing_anomaly is not None,
    )


# =========================================================================
# Section 4: Explicit computations for standard CY3 examples
# =========================================================================

def obstruction_c3() -> FramingObstruction:
    """Primary framing data for the local model ``C^3``.

    The skyscraper sheaf at the origin has
    Ext*(O_0, O_0) = \\Lambda*(C^3), the exterior algebra on three
    generators.  This function records the zero Euler scalar and leaves
    the represented BV comparison to the chain-level construction.
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
    """Primary framing data for the quintic threefold in ``P^4``.

    h^{1,1} = 1, h^{2,1} = 101.
    chi = 2(1 - 101) = -200.
    kappa = chi/24 = -25/3.

    The group calculation gives ``pi_3(BSp(204)) = 0``.  The scalar
    shadow is ``-25/3``.  A represented BV cocycle, its projection, and
    its null-homotopy form the separate chain-level package.
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
    """Primary framing data for ``K3 x E``.

    h^{1,1} = 21, h^{2,1} = 21.
    chi = 2(21 - 21) = 0.
    kappa = 0/24 = 0.

    The scalar shadow equals zero, while the family has 21 complex
    structure directions and Gauss--Manin rank 44.  The represented BV
    class remains an independent deformation-complex datum.
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
    """Primary framing data for the resolved-conifold chart.

    The local geometry is ``O(-1) + O(-1) -> P^1``.  The scalar value
    one is the beta--gamma chart convention supplied to this engine.
    Chain-level framing data occupy the represented comparison fields.
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
    r"""Compute stable classifying-space groups in degree ``d``.

    In the stable range (structure group rank >> d), the obstruction lives in
    pi_d(BG) for G = GL(C) (complex linear) or Sp (symplectic, for odd d).

    The returned groups are primary homotopy inputs.  A categorical
    framing additionally carries its represented comparison data.
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

    # Stable orthogonal lane: pi_d(BO) = pi_{d-1}(O).
    o_homotopy = {
        0: "Z/2", 1: "Z/2", 2: "0", 3: "Z",
        4: "0", 5: "0", 6: "0", 7: "Z",
    }
    pi_dm1_O = o_homotopy.get((d - 1) % 8, "?")
    pi_d_BO = pi_dm1_O
    vanishes_orthogonal = (pi_d_BO == "0")

    # CY condition analysis
    tangent_cy_class_resolves_primary = False
    cy_explanation = ""
    if d % 2 == 0 and vanishes_complex is False:
        if d == 2:
            tangent_cy_class_resolves_primary = True
            cy_explanation = "the tangent Calabi--Yau condition supplies c_1(TX)=0"
        elif d == 4:
            tangent_cy_class_resolves_primary = False
            cy_explanation = (
                "the degree-four primary class is c_2; its value is "
                "additional geometric input"
            )
        elif d == 6:
            tangent_cy_class_resolves_primary = False
            cy_explanation = "the degree-six primary class is additional geometric input"

    primary_input_resolved = (
        vanishes_complex or tangent_cy_class_resolves_primary
    )

    return {
        "d": d,
        "pi_d_BU": pi_d_BU,
        "pi_d_BSp": pi_d_BSp,
        "pi_d_BO": pi_d_BO,
        "vanishes_complex": vanishes_complex,
        "vanishes_symplectic": vanishes_symplectic,
        "vanishes_orthogonal": vanishes_orthogonal,
        "tangent_cy_class_resolves_primary": tangent_cy_class_resolves_primary,
        "cy_explanation": cy_explanation,
        "primary_input_resolved": primary_input_resolved,
        "categorical_framing_constructed": False,
    }


# =========================================================================
# Section 6: Framing anomaly and Chern-Simons invariant
# =========================================================================

def chern_simons_framing_anomaly(
    kappa: Fraction,
    *,
    comparison: Optional[FramingAnomalyComparison] = None,
) -> Optional[Fraction]:
    r"""Return the anomaly value after a supplied scalar comparison.

    ``kappa`` is an Euler/modular scalar.  A three-dimensional TFT, its
    gravitational Chern--Simons comparison, and the value assigned to a
    unit framing shift determine the anomaly coefficient.
    """

    if comparison is None:
        return None
    return comparison.evaluate(kappa)


def framing_anomaly_phase(
    kappa: Fraction,
    *,
    comparison: Optional[FramingAnomalyComparison] = None,
) -> Optional[complex]:
    """Evaluate ``exp(2*pi*i*kappa)`` on the compared anomaly lane."""

    anomaly = chern_simons_framing_anomaly(
        kappa,
        comparison=comparison,
    )
    if anomaly is None:
        return None
    angle = 2 * math.pi * float(anomaly)
    return complex(math.cos(angle), math.sin(angle))


def framing_anomaly_order(
    kappa: Fraction,
    *,
    comparison: Optional[FramingAnomalyComparison] = None,
) -> Optional[int]:
    """Return the order of the compared phase in ``U(1)``."""

    anomaly = chern_simons_framing_anomaly(
        kappa,
        comparison=comparison,
    )
    return anomaly.denominator if anomaly is not None else None


# =========================================================================
# Section 7: Pontryagin class computation
# =========================================================================

def cy3_characteristic_class_inputs(h11: int, h21: int) -> Dict[str, Any]:
    r"""Separate Hodge-number data from characteristic-class input.

    The Gauss--Manin local system ``R^3 pi_* Z`` has symplectic rank
    ``2+2*h21`` and a flat connection on the smooth base.  The tangent
    bundle of complex-structure moduli and its Weil--Petersson
    connection form a different object.  Hodge numbers determine the
    ranks below; a representative of ``p_1(T M_cs)`` requires geometric
    curvature data beyond these two integers.
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
        "gauss_manin_connection": "flat on the smooth locus",
        "tangent_connection": "Weil--Petersson/Chern connection on T M_cs",
        "p1_representative": None,
        "p1_interpretation": (
            f"p_1(T_{{M_cs}}) lies in H^4(M_cs); h^{{2,1}} = {h21} "
            "determines the tangent rank"
        ),
        "cs_transgression": None,
        "cs_interpretation": (
            "a Chern--Simons transgression requires a represented "
            "degree-four characteristic form and a reference connection"
        ),
        "kappa": kappa,
        "chi": chi,
    }


def first_pontryagin_class_cy3(h11: int, h21: int) -> Dict[str, Any]:
    """Historical API alias for :func:`cy3_characteristic_class_inputs`."""

    return cy3_characteristic_class_inputs(h11, h21)


# =========================================================================
# Section 8: The BV compatibility analysis
# =========================================================================

class BVObstruction(NamedTuple):
    """Construction state of the BV comparison problem."""
    name: str
    scalar_shadow: Fraction
    bv_class: Optional[RepresentedBVClass]
    scalar_projection_agrees: Optional[bool]
    null_homotopy: Optional[RepresentedNullHomotopy]
    bcov_anomaly: Optional[Fraction]
    trivialization_method: str
    trivialization_cost: str
    is_trivializable: Optional[bool]
    relation_to_framing_anomaly: str
    bv_cocycle_supplied: bool
    bcov_comparison_supplied: bool
    trivialization_supplied: bool


def bv_obstruction_cy3(
    name: str,
    kappa: Fraction,
    h21: int = 0,
    rigid: bool = False,
    *,
    represented_bv_class: Optional[RepresentedBVClass] = None,
    null_homotopy: Optional[RepresentedNullHomotopy] = None,
) -> BVObstruction:
    """Assemble explicitly supplied BV, BCOV, and trivialization data."""

    if represented_bv_class is not None and not isinstance(
        represented_bv_class, RepresentedBVClass
    ):
        raise TypeError("represented_bv_class must be a RepresentedBVClass")
    if represented_bv_class is not None and represented_bv_class.is_cocycle is False:
        raise ValueError("the represented BV cochain must satisfy the cocycle equation")
    if null_homotopy is not None and not isinstance(
        null_homotopy, RepresentedNullHomotopy
    ):
        raise TypeError("null_homotopy must be a RepresentedNullHomotopy")
    if null_homotopy is not None:
        if represented_bv_class is None:
            raise ValueError("a null-homotopy requires a represented BV class")
        if null_homotopy.trivializes(represented_bv_class) is False:
            raise ValueError("the supplied homotopy must satisfy d(h)=c")

    family_lane = "rigid local model" if rigid or h21 == 0 else f"{h21}-parameter family"
    scalar_projection = (
        represented_bv_class.scalar_projection
        if represented_bv_class is not None
        else None
    )
    return BVObstruction(
        name=name,
        scalar_shadow=kappa,
        bv_class=represented_bv_class,
        scalar_projection_agrees=(
            scalar_projection == kappa if scalar_projection is not None else None
        ),
        null_homotopy=null_homotopy,
        bcov_anomaly=scalar_projection,
        trivialization_method=(
            "represented holomorphic Chern--Simons functional together "
            "with a BV comparison and explicit null-homotopy"
        ),
        trivialization_cost=(
            f"chain maps in the chosen completion for the {family_lane}"
        ),
        is_trivializable=True if null_homotopy is not None else None,
        relation_to_framing_anomaly=(
            "a represented projection theorem relates the BV class, the "
            f"BCOV scalar, and the Euler shadow {kappa}"
        ),
        bv_cocycle_supplied=represented_bv_class is not None,
        bcov_comparison_supplied=scalar_projection is not None,
        trivialization_supplied=null_homotopy is not None,
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
    """Compare exact Hodge and Euler-scalar data for a mirror pair.

    For a mirror pair (X, X_mirror):
      h^{1,1}(X) = h^{2,1}(X_mirror), h^{2,1}(X) = h^{1,1}(X_mirror).
      chi(X) = -chi(X_mirror).
      kappa(X) = -kappa(X_mirror).

    The sign exchange concerns the scalar ``chi/24`` lane.  Represented
    BV and framing-anomaly comparisons remain separate inputs.
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
        "scalar_shadow_A": kappa_A,
        "scalar_shadow_B": kappa_B,
        "scalar_shadow_sum": kappa_A + kappa_B,
        "bv_obstruction_A": None,
        "bv_obstruction_B": None,
        "framing_anomaly_sum": None,
    }


# =========================================================================
# Section 10: Summary and the d=3 functor existence
# =========================================================================

def d3_functor_existence_analysis() -> Dict[str, Any]:
    r"""Separate the primary group calculation from the two-stage functor.

    The canonical architecture is

        Phi_3^(Sigma_2,C) = Sp^ch_(Sigma_2,C) o Phi_3^FA.

    The factorization-algebra stage and the chiral specialization stage
    carry independent construction data.

    1. The topological obstruction group vanishes in the stated stable
       complex/symplectic model.
       Reason: pi_3(BGL(C)) = 0 (Bott periodicity for unitary groups).
       Alternative: pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0 (all m >= 1).

    2. A represented chain-level BV class is a separate datum in a
       named deformation complex.  Its scalar projection requires a
       comparison map.

    3. The first stage requires a functorial factorization-algebra and BV
       construction.  The second requires the specialization kernel,
       descent, and comparison with the target chiral algebra.
    """
    examples = {
        "C^3": obstruction_c3(),
        "quintic": obstruction_quintic(),
        "mirror_quintic": obstruction_mirror_quintic(),
        "K3xE": obstruction_k3_times_e(),
        "conifold": obstruction_conifold(),
    }

    return {
        "primary_test_sphere_group_zero": True,
        "reason": (
            "pi_3(BGL(n,C)) = pi_2(GL(n,C)) = pi_2(U(n)) = 0 "
            "for all n >= 1 (Bott periodicity)"
        ),
        "alternative_reason": (
            "For CY3 with antisymmetric pairing: structure group Sp(2m), "
            "pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0 for all m >= 1"
        ),
        "chain_level_obstruction": (
            "represented BV cocycle, scalar projection, and explicit "
            "null-homotopy in a chosen completed deformation complex"
        ),
        "factorization_stage": "Phi_3^FA",
        "specialization_stage": "Sp^ch_(Sigma_2,C)",
        "composite_functor": "Sp^ch_(Sigma_2,C) o Phi_3^FA",
        "factorization_stage_status": "conditional construction problem",
        "specialization_stage_status": "conditional construction problem",
        "composite_functor_status": "conditional construction problem",
        "factorization_stage_constructed": False,
        "specialization_stage_constructed": False,
        "chain_level_framing_constructed": False,
        "d3_functor_construction_requires": (
            "Phi_3^FA: represented factorization algebra, holomorphic "
            "Chern--Simons functional, BV quantization, functorial framing; "
            "Sp^ch_(Sigma_2,C): specialization kernel, descent, target comparison"
        ),
        "examples": {
            name: {
                "topological_obstruction": obs.topological_obstruction,
                "scalar_shadow": obs.scalar_shadow,
                "bv_class": obs.bv_obstruction_class,
                "scalar_projection_agrees": obs.scalar_projection_agrees,
                "framing_comparison": obs.framing_comparison,
                "framing_anomaly": obs.framing_anomaly,
                "trivialization_exists": obs.trivialization_exists,
                "bv_cocycle_supplied": obs.bv_cocycle_supplied,
                "trivialization_supplied": obs.trivialization_supplied,
                "framing_anomaly_supplied": obs.framing_anomaly_supplied,
            }
            for name, obs in examples.items()
        },
    }
