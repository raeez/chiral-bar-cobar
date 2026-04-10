r"""lattice_shadow_depth_engine.py -- Shadow depth for unimodular lattice VOAs.

BACKGROUND
==========

A unimodular lattice Lambda of rank n gives rise to a lattice vertex algebra
V_Lambda.  The underlying Heisenberg algebra has level k = 1 per boson,
so for rank n the effective level is k = n and the central charge c = n.

CLASSIFICATION
--------------
- Type I  (odd unimodular):  exists at every rank n >= 1.  Simplest: Z^n.
  Lattice contains vectors of odd norm, so vertex operators can have
  half-integer conformal weights.
- Type II (even unimodular): exists only at ranks divisible by 8.
  All lattice vectors have even norm, so all vertex operators have
  integer conformal weights.  Simplest: E_8 at rank 8.

SHADOW DEPTH
------------
All unimodular lattice VOAs are Heisenberg-type (the OPE of the currents
J^i(z) J^j(w) ~ k delta^{ij}/(z-w)^2 is purely quadratic-pole).  Therefore:

- OPE pole order p = 2
- Shadow depth r = p = 2 (class G in the G/L/C/M classification)
- S_2 = kappa = n (rank)
- S_r = 0 for r >= 3
- Delta = 8 * kappa * S_4 = 0 (finite shadow tower)
- Koszul complementarity: kappa + kappa' = 0 (lattice/free family)

The r-matrix is r(z) = k/z = n/z (AP126: level prefix mandatory; k=0 -> r=0).

The Type I vs Type II distinction does NOT affect shadow depth (both are
class G).  It affects the SPECTRUM of vertex operators:
- Type I:  half-integer weights possible -> fermionic sectors
- Type II: integer weights only -> purely bosonic

GROUND TRUTH
============
- CLAUDE.md C1:  kappa(H_k) = k
- CLAUDE.md C10: r^Heis(z) = k/z
- CLAUDE.md C26: G (r=2, Heis)
- CLAUDE.md C30: Delta = 8*kappa*S_4, finite tower iff Delta=0
- landscape_census.tex: lattice VOAs are class G
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Optional, Tuple


# ======================================================================
# Lattice data
# ======================================================================

@dataclass(frozen=True)
class UnimodularLattice:
    """Data for a unimodular lattice.

    Parameters
    ----------
    name : str
        Human-readable name (e.g. "Z^8", "E_8", "D_16^+").
    rank : int
        Rank of the lattice.
    is_even : bool
        True for Type II (even unimodular), False for Type I (odd unimodular).
    min_norm : int
        Minimum nonzero norm of a lattice vector.
        Type I: min_norm = 1 (from unit vectors in Z^n).
        Type II: min_norm >= 2 (all norms even).
    kissing_number : Optional[int]
        Number of vectors of minimum norm, if known.
    """

    name: str
    rank: int
    is_even: bool
    min_norm: int
    kissing_number: Optional[int] = None

    @property
    def lattice_type(self) -> str:
        """Return 'Type I' (odd) or 'Type II' (even)."""
        return "Type II" if self.is_even else "Type I"

    def __post_init__(self):
        if self.rank < 1:
            raise ValueError(f"Rank must be >= 1, got {self.rank}")
        if self.is_even and self.rank % 8 != 0:
            raise ValueError(
                f"Even unimodular lattices exist only at ranks divisible by 8, "
                f"got rank {self.rank}"
            )
        if self.is_even and self.min_norm < 2:
            raise ValueError(
                f"Even unimodular lattices have min_norm >= 2, got {self.min_norm}"
            )


# ======================================================================
# Standard lattice catalog
# ======================================================================

def Zn_lattice(n: int) -> UnimodularLattice:
    """The standard cubic lattice Z^n (Type I, odd unimodular).

    Exists for all n >= 1.  Kissing number = 2n (the +/- unit vectors).
    """
    return UnimodularLattice(
        name=f"Z^{n}",
        rank=n,
        is_even=False,
        min_norm=1,
        kissing_number=2 * n,
    )


def E8_lattice() -> UnimodularLattice:
    r"""The E_8 root lattice (Type II, even unimodular, rank 8).

    The unique even unimodular lattice at rank 8.
    Kissing number = 240 (the E_8 roots).
    # VERIFIED: [LT] Conway-Sloane SPLAG Table 1.3; [DC] |roots(E_8)| = 240.
    """
    return UnimodularLattice(
        name="E_8",
        rank=8,
        is_even=True,
        min_norm=2,
        kissing_number=240,
    )


def D16_plus_lattice() -> UnimodularLattice:
    r"""The D_{16}^+ lattice (Type II, even unimodular, rank 16).

    One of the two even unimodular lattices at rank 16 (the other is E_8 x E_8).
    Kissing number = 480.
    # VERIFIED: [LT] Conway-Sloane SPLAG Ch. 16; [DC] D_n root count = 2n(n-1),
    #   D_16 roots = 480, plus glue vectors of norm 4.
    """
    return UnimodularLattice(
        name="D_{16}^+",
        rank=16,
        is_even=True,
        min_norm=2,
        kissing_number=480,
    )


def E8_x_E8_lattice() -> UnimodularLattice:
    r"""The E_8 x E_8 lattice (Type II, even unimodular, rank 16).

    Direct sum of two copies of E_8.  Kissing number = 2 * 240 = 480.
    # VERIFIED: [DC] direct sum kissing = sum of kissing numbers;
    #   [LT] Conway-Sloane SPLAG Ch. 16.
    """
    return UnimodularLattice(
        name="E_8 x E_8",
        rank=16,
        is_even=True,
        min_norm=2,
        kissing_number=480,
    )


# ======================================================================
# Lattice VOA shadow data
# ======================================================================

@dataclass(frozen=True)
class LatticeVOAShadowData:
    """Shadow depth data for the lattice VOA V_Lambda.

    All lattice VOAs are Heisenberg-type, hence class G.
    """

    lattice: UnimodularLattice

    # Central charge = rank
    # VERIFIED: [DC] c = n for n free bosons; [LT] FBZ Ch. 5.
    central_charge: int

    # kappa = rank (Heisenberg kappa at effective level k = rank)
    # VERIFIED: [DC] kappa(H_k) = k, here k = rank; [CF] matches C1 in CLAUDE.md.
    kappa: int

    # Shadow coefficients
    # VERIFIED: [DC] Heisenberg S_2 = kappa, S_r = 0 for r >= 3;
    #   [LT] shadow_eisenstein_correct_engine.py Heisenberg case.
    S2: int               # = kappa
    S4: int               # = 0 (class G)

    # Discriminant Delta = 8 * kappa * S_4
    # VERIFIED: [DC] 8 * kappa * 0 = 0; [CF] C30: Delta=0 <-> finite tower.
    Delta: int            # = 0

    # Shadow depth (class G)
    shadow_depth: int     # = 2

    # G/L/C/M classification
    shadow_class: str     # = "G"

    # r-matrix: r(z) = k/z = rank/z
    # AP126: level prefix mandatory. k=0 -> r=0. VERIFIED.
    r_matrix_level: int   # = rank

    # Koszul complementarity: kappa + kappa' = 0 for lattice/free family
    # VERIFIED: [DC] free/lattice family; [CF] C18: K=0 for KM/Heis/lattice/free.
    koszul_conductor: int  # = 0

    # Spectrum type
    has_half_integer_weights: bool  # True for Type I (odd), False for Type II (even)


def compute_shadow_data(lattice: UnimodularLattice) -> LatticeVOAShadowData:
    """Compute shadow depth data for the lattice VOA V_Lambda.

    All unimodular lattice VOAs are Heisenberg-type (class G) regardless
    of whether the lattice is Type I or Type II.

    Parameters
    ----------
    lattice : UnimodularLattice
        The unimodular lattice.

    Returns
    -------
    LatticeVOAShadowData
        Complete shadow depth data.
    """
    n = lattice.rank

    # Central charge = rank
    c = n

    # kappa = rank (Heisenberg: kappa(H_k) = k, effective level k = rank)
    # AP1: from CLAUDE.md C1, NOT from memory.
    kappa = n

    # Shadow coefficients: Heisenberg-type
    # S_2 = kappa, S_r = 0 for r >= 3
    S2 = kappa
    S4 = 0

    # Discriminant: Delta = 8 * kappa * S_4
    # CLAUDE.md C30: Delta = 8*kappa*S_4. Linear in kappa (NOT quadratic, AP21).
    Delta = 8 * kappa * S4  # = 0

    # Shadow depth and class
    shadow_depth = 2
    shadow_class = "G"

    # r-matrix level: k = rank
    # AP126: r(z) = k/z. At k=0: r=0. Verified.
    r_matrix_level = n

    # Koszul complementarity
    # CLAUDE.md C18: K = 0 for KM/Heis/lattice/free.
    koszul_conductor = 0

    # Spectrum: Type I (odd) has half-integer weights; Type II (even) does not.
    has_half_integer_weights = not lattice.is_even

    return LatticeVOAShadowData(
        lattice=lattice,
        central_charge=c,
        kappa=kappa,
        S2=S2,
        S4=S4,
        Delta=Delta,
        shadow_depth=shadow_depth,
        shadow_class=shadow_class,
        r_matrix_level=r_matrix_level,
        koszul_conductor=koszul_conductor,
        has_half_integer_weights=has_half_integer_weights,
    )


# ======================================================================
# Shadow tower truncation
# ======================================================================

def shadow_tower_terms(data: LatticeVOAShadowData, max_r: int = 10) -> Dict[int, int]:
    """Return the shadow tower coefficients S_r for r = 2, ..., max_r.

    For class G (Heisenberg-type): S_2 = kappa, S_r = 0 for r >= 3.

    Parameters
    ----------
    data : LatticeVOAShadowData
        The shadow data.
    max_r : int
        Maximum arity to compute.

    Returns
    -------
    dict
        {r: S_r} for r = 2, ..., max_r.
    """
    tower = {}
    for r in range(2, max_r + 1):
        if r == 2:
            tower[r] = data.S2
        else:
            tower[r] = 0
    return tower


# ======================================================================
# r-matrix evaluation
# ======================================================================

def r_matrix_at_z(data: LatticeVOAShadowData, z: complex) -> complex:
    r"""Evaluate the classical r-matrix r(z) = k/z for the lattice VOA.

    AP126: level prefix mandatory. r(z) = k/z with k = rank.
    AP141: k=0 -> r=0 (verified in tests).

    Parameters
    ----------
    data : LatticeVOAShadowData
        The shadow data.
    z : complex
        Evaluation point (nonzero).

    Returns
    -------
    complex
        r(z) = k/z.
    """
    if z == 0:
        raise ValueError("r-matrix has a simple pole at z=0")
    k = data.r_matrix_level
    return k / z


# ======================================================================
# Genus-1 free energy
# ======================================================================

def genus1_free_energy(data: LatticeVOAShadowData) -> Fraction:
    r"""Compute the genus-1 free energy F_1 = kappa/24.

    VERIFIED: [DC] F_1 = kappa/24 for Heisenberg-type;
              [CF] CLAUDE.md: F_1 = kappa/24 sanity check.

    Parameters
    ----------
    data : LatticeVOAShadowData
        The shadow data.

    Returns
    -------
    Fraction
        F_1 = kappa/24.
    """
    return Fraction(data.kappa, 24)


# ======================================================================
# Comparison engine
# ======================================================================

@dataclass(frozen=True)
class LatticeComparison:
    """Side-by-side comparison of two lattice VOA shadow data."""

    lattice_a: LatticeVOAShadowData
    lattice_b: LatticeVOAShadowData

    @property
    def same_shadow_class(self) -> bool:
        return self.lattice_a.shadow_class == self.lattice_b.shadow_class

    @property
    def same_shadow_depth(self) -> bool:
        return self.lattice_a.shadow_depth == self.lattice_b.shadow_depth

    @property
    def kappa_ratio(self) -> Fraction:
        """Ratio kappa_a / kappa_b."""
        if self.lattice_b.kappa == 0:
            raise ValueError("Cannot compute ratio: kappa_b = 0")
        return Fraction(self.lattice_a.kappa, self.lattice_b.kappa)

    @property
    def central_charge_difference(self) -> int:
        return self.lattice_a.central_charge - self.lattice_b.central_charge

    @property
    def both_finite_tower(self) -> bool:
        return self.lattice_a.Delta == 0 and self.lattice_b.Delta == 0

    @property
    def spectrum_difference(self) -> str:
        """Describe the spectral difference."""
        a_half = self.lattice_a.has_half_integer_weights
        b_half = self.lattice_b.has_half_integer_weights
        if a_half and not b_half:
            return "A has half-integer weights (Type I); B is purely bosonic (Type II)"
        elif not a_half and b_half:
            return "A is purely bosonic (Type II); B has half-integer weights (Type I)"
        elif a_half and b_half:
            return "Both have half-integer weights (both Type I)"
        else:
            return "Both purely bosonic (both Type II)"


def compare_lattices(
    lattice_a: UnimodularLattice,
    lattice_b: UnimodularLattice,
) -> LatticeComparison:
    """Compare shadow depth data for two unimodular lattice VOAs.

    Parameters
    ----------
    lattice_a, lattice_b : UnimodularLattice
        The two lattices to compare.

    Returns
    -------
    LatticeComparison
        Side-by-side comparison data.
    """
    data_a = compute_shadow_data(lattice_a)
    data_b = compute_shadow_data(lattice_b)
    return LatticeComparison(lattice_a=data_a, lattice_b=data_b)


# ======================================================================
# Batch analysis
# ======================================================================

def analyze_Zn_family(max_rank: int = 24) -> List[LatticeVOAShadowData]:
    """Compute shadow data for Z^1, Z^2, ..., Z^{max_rank}.

    Parameters
    ----------
    max_rank : int
        Maximum rank to analyze.

    Returns
    -------
    list of LatticeVOAShadowData
        Shadow data for each Z^n lattice.
    """
    results = []
    for n in range(1, max_rank + 1):
        lattice = Zn_lattice(n)
        results.append(compute_shadow_data(lattice))
    return results


def analyze_even_unimodular_rank8_16() -> List[LatticeVOAShadowData]:
    """Compute shadow data for the even unimodular lattices at ranks 8 and 16.

    Rank 8:  E_8 (unique).
    Rank 16: E_8 x E_8 and D_{16}^+ (two lattices, same shadow data).

    Returns
    -------
    list of LatticeVOAShadowData
    """
    return [
        compute_shadow_data(E8_lattice()),
        compute_shadow_data(E8_x_E8_lattice()),
        compute_shadow_data(D16_plus_lattice()),
    ]
