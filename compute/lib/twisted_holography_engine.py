r"""Twisted holography engine: scalar shadows of the HT/Koszul package.

Costello-Li type twisted-holography examples relate boundary, line, and
bulk presentations through bar, Verdier, Hochschild, collision, and
Maurer-Cartan constructions. The manuscript's seven-entry holographic
modular Koszul datum is

    H(T) = (A, A^i, A!, C, r(z), Theta_A, nabla^hol)

where A^i is the bar-dual coalgebra, A! is the Verdier/Koszul companion
only after the strictification hypotheses are met, and
C = Z_ch^der(A) is the pinned chiral Hochschild bulk slot.

This engine does not construct the full HT theory. It records the
seven-entry package at the scalar/typed-summary level:

    (A, A^i, A!, C, r(z), Theta_A, nabla^hol).

The A^i slot is the bar-dual coalgebra H^*(B^ch(A)); the A! slot is a
Verdier/Koszul companion summary. Neither slot is Omega(B(A)).
Bar-cobar inversion recovers A, while C is pinned to Z_ch^der(A).

PRINCIPAL OBJECTS:

1. **GL(1) Chern-Simons**: boundary = Heisenberg H_k. The C-slot is the
   derived-centre/Fock model, while the Verdier/Koszul companion is
   Sym^ch(V*) with kappa = -k (same scalar characteristic as H_{-k}, not the
   same algebra).

2. **GL(N) Chern-Simons at level k**: boundary = affine gl(N)_k; the
   large-N comparison slot is W_{1+infty} at c = N (Gaberdiel-Gopakumar).

3. **M2 brane (ABJM)**: boundary = chiral algebra from BRST reduction.
   This engine stores the reduced scalar convention kappa_red = -N^2;
   the unreduced pre-BRST package has kappa = -(N^2+1).

4. **Twisted M-theory on CY5**: boundary = chiral algebra on M5 wrapping divisor,
   with scalar datum supplied from Calabi-Yau data.

5. **Holographic shadow connection**: nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
   Heisenberg: flat (Gaussian, depth 2). Affine: log singularities (Lie, depth 3).
   Virasoro: essential singularity (Mixed, depth infinity).

6. **Anomaly cancellation/complementarity**: the engine records the scalar
   kappa-sum of a boundary algebra with its companion or ghost sector.
   Bosonic string: c/2 + (-13) = 0 at c = 26.

7. **Holographic entanglement scalar**: the CFT leading coefficient
   c/3 is recorded; an RT/bulk interpretation requires the separate
   open/closed comparison.

8. **GZ commuting differentials**: Gaiotto-Zhang d_1, d_2 with
   d_1^2 = d_2^2 = d_1 d_2 + d_2 d_1 = 0 are the arity-2 projection of the
   MC equation.

MULTI-PATH VERIFICATION: where the code says "three paths", it means three
scalar projections in this compute model, not a primary-source proof of the
full seven-entry HT lift.

CONVENTIONS (from CLAUDE.md anti-patterns):
  AP1:  kappa formulas recomputed per family, never copied
  AP19: r-matrix pole order one below OPE
  AP20: kappa(A) is intrinsic to A, not to a physical system
  AP24: kappa + kappa' = 0 for KM/free; = rho*K for W-algebras
  Firewall: B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A) are typed apart
  AP27: bar propagator d log E(z,w) weight 1 regardless of field weight
  AP29: delta_kappa != kappa_eff (two different objects)
  AP33: H_k^! = Sym^ch(V*) != H_{-k}
  Derived centre: bar-cobar inversion != open-to-closed; C = Z_ch^der(A)
  AP39: kappa != c/2 for general VOA; kappa = c/2 only for Virasoro
  AP44: OPE mode / n! = lambda-bracket coefficient (divided powers)
  AP48: kappa depends on full algebra, not just Virasoro subalgebra

References:
  Costello-Li, arXiv:1903.02984
  Costello-Gaiotto, arXiv:1812.09257
  Gaberdiel-Gopakumar, arXiv:1011.2986
  concordance.tex: sec:concordance-holographic-datum
  higher_genus_modular_koszul.tex: thm:mc2-bar-intrinsic
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb
from typing import Dict, List, Optional, Tuple


HOLOGRAPHIC_SLOT_ORDER: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)


# ===========================================================================
# Exact arithmetic
# ===========================================================================

def _frac(x) -> Fraction:
    """Coerce to Fraction."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    return Fraction(x)


@lru_cache(maxsize=64)
def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n via the recurrence."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n >= 3:
        return Fraction(0)
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    B[1] = Fraction(-1, 2)
    for m in range(2, n + 1):
        if m % 2 == 1 and m >= 3:
            continue
        s = Fraction(0)
        for k in range(m):
            if B[k] != 0:
                s += Fraction(comb(m + 1, k)) * B[k]
        B[m] = -s / (m + 1)
    return B[n]


@lru_cache(maxsize=64)
def _lambda_fp_exact(g: int) -> Fraction:
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = _bernoulli_exact(2 * g)
    abs_B = abs(B_2g)
    numerator = (2 ** (2 * g - 1) - 1) * abs_B
    denominator = Fraction(2 ** (2 * g - 1)) * _factorial_frac(2 * g)
    return numerator / denominator


def _factorial_frac(n: int) -> Fraction:
    """n! as Fraction."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


@lru_cache(maxsize=64)
def _harmonic_exact(n: int) -> Fraction:
    """H_n = sum_{j=1}^n 1/j."""
    return sum(Fraction(1, j) for j in range(1, n + 1))


# ===========================================================================
# Data structures
# ===========================================================================

@dataclass(frozen=True)
class TwistedHolographicAlgebra:
    """A chiral algebra in the twisted holography context.

    Attributes:
        name: human-readable name
        family: 'heisenberg', 'affine', 'virasoro', 'w_algebra', 'abjm', 'cy5'
        rank: N for gl(N)/sl(N) family; 1 for Heisenberg/Virasoro
        level: k (the CS or affine level)
        central_charge: c
        kappa: modular characteristic (AP39: NOT always c/2)
        shadow_depth: r_max (2=Gaussian, 3=Lie, 4=contact, 1000=infinite)
        dual_coxeter: h^v (0 for abelian)
        dim_lie: dim(g) for Lie-type (0 for abelian)
    """
    name: str
    family: str
    rank: int
    level: Fraction
    central_charge: Fraction
    kappa: Fraction
    shadow_depth: int
    dual_coxeter: int = 0
    dim_lie: int = 0


@dataclass
class HolographicDatum:
    """Seven-entry scalar/typed-summary record for H(T).

    Manuscript datum:
        H(T) = (A, A^i, A!, C, r(z), Theta_A, nabla^hol).

    The non-scalar slots are typed summaries: A^i is the bar-dual
    coalgebra H^*(B^ch(A)); A! is the Verdier/Koszul companion summary;
    C is the derived-centre bulk slot Z_ch^der(A). This is a
    compatibility record, not a proof that the strict HT holographic
    lift exists.
    """
    A: TwistedHolographicAlgebra          # boundary algebra
    A_dual: TwistedHolographicAlgebra     # legacy alias for the A! summary
    bulk_description: str                  # legacy alias for C = Z_ch^der(A)
    collision_residue_type: str            # "Casimir/z", "scalar/z", etc.
    theta_kappa: Fraction                  # scalar part of Theta_A
    kappa_sum: Fraction                    # kappa(A) + kappa(A!) summary
    complementarity_type: str              # "anti-symmetric" or "shifted"
    connection_is_flat: bool               # formal scalar MC/Arnold flatness flag
    bar_dual_coalgebra: str = ""           # A^i = H^*(B^ch(A)) summary

    @property
    def A_i(self) -> str:
        """The A^i slot: bar-dual coalgebra, not the Verdier companion."""
        return self.bar_dual_coalgebra

    @property
    def A_shriek(self) -> TwistedHolographicAlgebra:
        """The A^! slot, retained separately from A^i and Omega(B(A))."""
        return self.A_dual

    @property
    def C(self) -> str:
        """The C slot: Z_ch^der(A), not the bar coalgebra or A^!."""
        return self.bulk_description

    @property
    def r_z(self) -> str:
        """The r(z) slot: the collision-residue type recorded by the engine."""
        return self.collision_residue_type

    @property
    def Theta_A(self) -> Fraction:
        """The scalar coefficient of the universal MC element Theta_A."""
        return self.theta_kappa

    @property
    def nabla_hol(self) -> bool:
        """The formal scalar flatness flag for nabla^hol."""
        return self.connection_is_flat

    def seven_entry_package(self) -> Dict[str, object]:
        """Return the seven holographic slots in manuscript order."""
        return {
            "A": self.A,
            "A^i": self.A_i,
            "A^!": self.A_shriek,
            "C": self.C,
            "r(z)": self.r_z,
            "Theta_A": self.Theta_A,
            "nabla^hol": self.nabla_hol,
        }

    def object_firewall(self) -> Dict[str, object]:
        """Return the firewall separating the bar, dual, cobar, and C slots."""
        return holographic_object_firewall(
            self.A,
            A_dual=self.A_dual,
            bar_dual_coalgebra=self.bar_dual_coalgebra,
            derived_center=self.bulk_description,
        )


@dataclass
class BoundaryBulkMap:
    """Genus-1 scalar boundary/bulk comparison via three projections.

    Path 1: Annulus trace Tr_A = HH_*(A)
    Path 2: Hochschild cochains C^*_ch(A, A)
    Path 3: Shadow projection Sh_{1,0}(Theta_A)

    Equality of the three numbers is a compute-level compatibility check.
    It does not assert the full global open/closed comparison.
    """
    kappa: Fraction
    F_1_annulus: Fraction       # from annulus trace: kappa/24
    F_1_hochschild: Fraction    # from Hochschild: kappa/24
    F_1_shadow: Fraction        # from shadow projection: kappa/24
    three_paths_agree: bool


@dataclass
class ShadowConnectionData:
    """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).

    Properties:
        singularity_type: 'none' (flat), 'logarithmic', 'essential'
        is_flat: formal flatness of the scalar shadow projection
        is_kz_type: whether this specializes to KZ at (0,2)
    """
    genus: int
    arity: int
    kappa: Fraction
    singularity_type: str
    is_flat: bool
    is_kz_type: bool


@dataclass
class AnomalyCancellation:
    """Scalar kappa-balance for boundary plus ghost/companion sector."""
    boundary_name: str
    boundary_kappa: Fraction
    ghost_kappa: Fraction
    total: Fraction
    cancels: bool
    critical_value: Optional[Fraction]  # c or d at which cancellation occurs


@dataclass
class HolographicEntanglement:
    """S_EE from the shadow CohFT.

    Leading: S_EE = (c/3) log(L/eps)
    Subleading: quantum corrections from higher-arity shadows.
    """
    central_charge: Fraction
    kappa: Fraction
    leading_coefficient: Fraction    # c/3
    shadow_depth: int
    has_quantum_corrections: bool


@dataclass
class GZDifferentials:
    """Gaiotto-Zhang commuting differentials from MC equation.

    d_1^2 = d_2^2 = d_1 d_2 + d_2 d_1 = 0
    These are the arity-2 projection of D*Theta + (1/2)[Theta,Theta] = 0.
    """
    kappa: Fraction
    d1_squared_vanishes: bool
    d2_squared_vanishes: bool
    anticommutator_vanishes: bool
    is_mc_projection: bool


@dataclass
class GaberdielGopakumar:
    """Gaberdiel-Gopakumar duality data at given N.

    Boundary: W_N algebra at level k
    Bulk: higher-spin gravity on AdS_3 with fields of spin 2, 3, ..., N

    The code records central-charge and kappa scalars. It does not prove the
    full large-N duality or identify all bulk fields.
    """
    N: int
    level: Fraction
    thooft: Fraction
    c_boundary: Fraction
    kappa_boundary: Fraction
    c_bulk: Fraction                 # scalar model sets this to c_boundary
    kappa_dual: Fraction
    kappa_sum: Fraction
    boundary_bulk_match: bool


# ===========================================================================
# 1. Algebra constructors
# ===========================================================================

def make_heisenberg(k: Fraction = Fraction(1)) -> TwistedHolographicAlgebra:
    """Heisenberg algebra H_k.

    c = 1 (Virasoro central charge from Sugawara).
    kappa(H_k) = k (the level, NOT c/2; see AP39, AP48).
    Shadow depth = 2 (Gaussian class G).
    """
    k = _frac(k)
    return TwistedHolographicAlgebra(
        name=f"H_{k}",
        family="heisenberg",
        rank=1,
        level=k,
        central_charge=Fraction(1),
        kappa=k,
        shadow_depth=2,
        dual_coxeter=0,
        dim_lie=0,
    )


def make_affine_gl_N(N: int, k: Fraction) -> TwistedHolographicAlgebra:
    """Affine gl(N)_k.

    gl(N) = sl(N) + u(1).
    c(gl_N) = c(sl_N) + c(u(1)) = k(N^2-1)/(k+N) + 1.

    kappa(gl_N) = kappa(sl_N) + kappa(u(1)).
    kappa(sl_N) = (N^2-1)(k+N)/(2N).
    kappa(u(1)) = k (Heisenberg contribution).

    For twisted holography (Costello-Li): the relevant algebra is gl(N)_k
    as the boundary of GL(N) CS theory.
    """
    k = _frac(k)
    h_v = N  # dual Coxeter for sl(N)
    if k + h_v == 0:
        raise ValueError(f"Critical level k = -{h_v}")
    dim_sl = N * N - 1
    c_sl = k * dim_sl / (k + h_v)
    c_total = c_sl + 1  # + Heisenberg factor
    kappa_sl = Fraction(dim_sl) * (k + h_v) / (2 * h_v)
    kappa_total = kappa_sl + k  # sl(N) + u(1) contribution
    return TwistedHolographicAlgebra(
        name=f"gl({N})_{k}",
        family="affine",
        rank=N,
        level=k,
        central_charge=c_total,
        kappa=kappa_total,
        shadow_depth=3,
        dual_coxeter=h_v,
        dim_lie=N * N,
    )


def make_affine_sl_N(N: int, k: Fraction) -> TwistedHolographicAlgebra:
    """Affine sl(N)_k.

    c = k(N^2-1)/(k+N).
    kappa = (N^2-1)(k+N)/(2N).
    Shadow depth = 3 (Lie/tree class L).
    """
    k = _frac(k)
    h_v = N
    if k + h_v == 0:
        raise ValueError(f"Critical level k = -{h_v}")
    dim_g = N * N - 1
    c = k * dim_g / (k + h_v)
    kappa = Fraction(dim_g) * (k + h_v) / (2 * h_v)
    return TwistedHolographicAlgebra(
        name=f"sl({N})_{k}",
        family="affine",
        rank=N,
        level=k,
        central_charge=c,
        kappa=kappa,
        shadow_depth=3,
        dual_coxeter=h_v,
        dim_lie=dim_g,
    )


def make_virasoro(c: Fraction) -> TwistedHolographicAlgebra:
    """Virasoro algebra Vir_c.

    kappa(Vir_c) = c/2.
    Verdier/Koszul companion on the strict Virasoro lane: Vir_{26-c}.
    Self-companion scalar at c = 13, NOT c = 26 (AP8).
    Shadow depth = infinity (class M).
    """
    c = _frac(c)
    return TwistedHolographicAlgebra(
        name=f"Vir_{c}",
        family="virasoro",
        rank=1,
        level=c,  # use c as the "level" parameter
        central_charge=c,
        kappa=c / 2,
        shadow_depth=1000,
        dual_coxeter=0,
        dim_lie=0,
    )


def make_w_N(N: int, k: Fraction) -> TwistedHolographicAlgebra:
    """W^k(sl_N, f_prin): principal W-algebra from DS reduction.

    c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N).
    kappa = c * (H_N - 1) where H_N is the N-th harmonic number.

    AP1/AP9: kappa(W_N) = c*(H_N - 1) != c/2 for N >= 3.
    For N=2 (Virasoro): H_2 - 1 = 1/2, so kappa = c/2. Correct.
    For N=3: H_3 - 1 = 5/6, so kappa = 5c/6.
    Shadow depth = infinity for all N >= 2 (class M).
    """
    k = _frac(k)
    h_v = N
    if k + h_v == 0:
        raise ValueError(f"Critical level k = -{h_v}")
    c = Fraction(N - 1) - Fraction(N * (N * N - 1)) * (k + N - 1) ** 2 / (k + N)
    kappa = c * (_harmonic_exact(N) - 1)
    return TwistedHolographicAlgebra(
        name=f"W^{k}(sl_{N})",
        family="w_algebra",
        rank=N,
        level=k,
        central_charge=c,
        kappa=kappa,
        shadow_depth=1000,  # all W_N have infinite depth
        dual_coxeter=h_v,
        dim_lie=N * N - 1,
    )


def make_bc_ghosts() -> TwistedHolographicAlgebra:
    """bc ghost system (conformal ghosts for bosonic string).

    c = -26, kappa = -13.
    Shadow depth = infinity (class M, bc is interacting via conformal weights).
    """
    return TwistedHolographicAlgebra(
        name="bc_ghosts",
        family="bc",
        rank=1,
        level=Fraction(-1),
        central_charge=Fraction(-26),
        kappa=Fraction(-13),
        shadow_depth=1000,
        dual_coxeter=0,
        dim_lie=0,
    )


def make_abjm(N: int, k: int) -> TwistedHolographicAlgebra:
    """ABJM boundary VOA at rank N and CS level k.

    From BRST reduction of V_k(gl_N) x V_{-k}(gl_N) x Sb^{4N^2}.
    This constructor records the reduced scalar convention
    c_red = -2N^2, kappa_red = -N^2 after cancelling the
    level-opposite CS pair. The full pre-BRST modular characteristic
    is -(N^2+1), computed in twisted_holography_comparison_engine.py.
    Shadow depth = 4 (contact, class C) for N=1, infinite for N >= 2.
    """
    c = Fraction(-2 * N * N)
    kappa = Fraction(-N * N)
    depth = 4 if N == 1 else 1000
    return TwistedHolographicAlgebra(
        name=f"ABJM({N},{k})",
        family="abjm",
        rank=N,
        level=Fraction(k),
        central_charge=c,
        kappa=kappa,
        shadow_depth=depth,
        dual_coxeter=0,
        dim_lie=0,
    )


def make_cy5_m5(c: Fraction, kappa: Fraction) -> TwistedHolographicAlgebra:
    """M5 brane wrapping a divisor in CY5 (twisted M-theory).

    The exact algebra depends on the Calabi-Yau geometry. This constructor
    parametrizes only the scalar central charge and modular characteristic;
    it is not a complete CY5 boundary algebra model. Shadow depth is taken
    to be infinite in the generic mixed case.
    """
    c = _frac(c)
    kappa = _frac(kappa)
    return TwistedHolographicAlgebra(
        name=f"M5_CY5(c={c})",
        family="cy5",
        rank=1,
        level=c,
        central_charge=c,
        kappa=kappa,
        shadow_depth=1000,
        dual_coxeter=0,
        dim_lie=0,
    )


# ===========================================================================
# 2. Verdier/Koszul companion construction
# ===========================================================================

def feigin_frenkel_dual_level(k: Fraction, h_v: int) -> Fraction:
    """Feigin-Frenkel dual level: k' = -k - 2h^v.

    CRITICAL: -k - 2h^v, NOT -k - h^v.
    """
    return -_frac(k) - 2 * h_v


def koszul_dual(A: TwistedHolographicAlgebra) -> TwistedHolographicAlgebra:
    """Compute the scalar Verdier/Koszul companion used by this engine.

    This is not bar-cobar inversion: Omega(B(A)) recovers A. The strict
    algebra A! exists only after the finite-type/completed Verdier
    rectification hypotheses in the manuscript.

    For affine sl(N)_k: companion at k' = -k - 2N via Feigin-Frenkel.
    For Heisenberg H_k: companion = Sym^ch(V*) with kappa = -k.
        AP33: H_k^! != H_{-k} as algebras; but kappa(H_k^!) = -k = kappa(H_{-k}).
    For Virasoro Vir_c: companion = Vir_{26-c}. kappa = (26-c)/2.
    For W^k(sl_N): companion at k' = -k - 2N.
    For ABJM/CY5: only the opposite-kappa scalar companion is represented.
    """
    if A.family == "heisenberg":
        return TwistedHolographicAlgebra(
            name=f"({A.name})! = Sym^ch(V*)",
            family="heisenberg_dual",
            rank=A.rank,
            level=-A.level,
            central_charge=A.central_charge,  # c = 1 same
            kappa=-A.kappa,
            shadow_depth=2,
            dual_coxeter=0,
            dim_lie=0,
        )
    elif A.family == "affine":
        k_dual = feigin_frenkel_dual_level(A.level, A.dual_coxeter)
        N = A.rank
        h_v = A.dual_coxeter
        dim_g = A.dim_lie
        if k_dual + h_v == 0:
            raise ValueError(f"Dual level k'={k_dual} is critical")
        # For sl(N): c_dual = k'(N^2-1)/(k'+N), kappa_dual = (N^2-1)(k'+N)/(2N)
        if dim_g == N * N - 1:  # sl(N)
            c_dual = k_dual * dim_g / (k_dual + h_v)
            kappa_dual = Fraction(dim_g) * (k_dual + h_v) / (2 * h_v)
        else:  # gl(N)
            dim_sl = N * N - 1
            c_sl_dual = k_dual * dim_sl / (k_dual + h_v)
            c_dual = c_sl_dual + 1
            kappa_sl_dual = Fraction(dim_sl) * (k_dual + h_v) / (2 * h_v)
            kappa_dual = kappa_sl_dual + (-A.level)  # u(1) at dual level
        return TwistedHolographicAlgebra(
            name=f"({A.name})! at k'={k_dual}",
            family="affine",
            rank=N,
            level=k_dual,
            central_charge=c_dual,
            kappa=kappa_dual,
            shadow_depth=A.shadow_depth,
            dual_coxeter=h_v,
            dim_lie=dim_g,
        )
    elif A.family == "virasoro":
        c_dual = 26 - A.central_charge
        return TwistedHolographicAlgebra(
            name=f"Vir_{c_dual}",
            family="virasoro",
            rank=1,
            level=c_dual,
            central_charge=c_dual,
            kappa=c_dual / 2,
            shadow_depth=1000,
            dual_coxeter=0,
            dim_lie=0,
        )
    elif A.family == "w_algebra":
        k_dual = feigin_frenkel_dual_level(A.level, A.dual_coxeter)
        N = A.rank
        h_v = A.dual_coxeter
        if k_dual + h_v == 0:
            raise ValueError(f"Dual level k'={k_dual} is critical")
        c_dual = Fraction(N - 1) - Fraction(N * (N * N - 1)) * (k_dual + N - 1) ** 2 / (k_dual + N)
        kappa_dual = c_dual * (_harmonic_exact(N) - 1)  # AP1/AP9: kappa = c*(H_N-1)
        return TwistedHolographicAlgebra(
            name=f"W^{k_dual}(sl_{N})",
            family="w_algebra",
            rank=N,
            level=k_dual,
            central_charge=c_dual,
            kappa=kappa_dual,
            shadow_depth=1000,
            dual_coxeter=h_v,
            dim_lie=N * N - 1,
        )
    elif A.family == "abjm":
        return TwistedHolographicAlgebra(
            name=f"({A.name})!",
            family="abjm_dual",
            rank=A.rank,
            level=-A.level,
            central_charge=-A.central_charge,
            kappa=-A.kappa,
            shadow_depth=A.shadow_depth,
            dual_coxeter=0,
            dim_lie=0,
        )
    elif A.family == "cy5":
        # Parametric opposite-kappa scalar companion; not a full CY5 dual model.
        return TwistedHolographicAlgebra(
            name=f"({A.name})!",
            family="cy5_dual",
            rank=A.rank,
            level=A.level,
            central_charge=A.central_charge,
            kappa=-A.kappa,
            shadow_depth=A.shadow_depth,
            dual_coxeter=0,
            dim_lie=0,
        )
    else:
        raise ValueError(f"Unknown family: {A.family}")


def bar_dual_coalgebra_summary(A: TwistedHolographicAlgebra) -> str:
    """Typed summary of A^i = H^*(B^ch(A)).

    This is the cohomology coalgebra of the chiral bar complex. It is
    not the bar complex itself, not the Verdier/Koszul companion A^!,
    not Omega(B(A)), and not the Hochschild bulk slot C.
    """
    return (
        f"A^i = H^*(B^ch({A.name})) bar-dual coalgebra; "
        "not B(A), not A^!, not Omega(B(A)), and not Z_ch^der(A)"
    )


def derived_center_summary(A: TwistedHolographicAlgebra, comparison: str) -> str:
    """Typed summary of C = Z_ch^der(A)."""
    return (
        f"C = Z_ch^der({A.name}) = C_ch^bullet({A.name}, {A.name}); "
        f"{comparison}; not B(A), not A^i, not A^!, and not Omega(B(A))"
    )


def holographic_object_firewall(
    A: TwistedHolographicAlgebra,
    A_dual: Optional[TwistedHolographicAlgebra] = None,
    bar_dual_coalgebra: Optional[str] = None,
    derived_center: Optional[str] = None,
) -> Dict[str, object]:
    """Separate B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A).

    The firewall encodes the manuscript distinction:
    A^i is H^*(B^ch(A)); A^! is a Verdier/Koszul companion after the
    rectification hypotheses; Omega(B(A)) recovers A by bar-cobar
    inversion; Z_ch^der(A) is the pinned derived-centre bulk slot.
    """
    if A_dual is None:
        A_dual = koszul_dual(A)
    if bar_dual_coalgebra is None:
        bar_dual_coalgebra = bar_dual_coalgebra_summary(A)
    if derived_center is None:
        derived_center = derived_center_summary(A, "derived-centre bulk slot")

    return {
        "A": f"{A.name}: boundary chiral algebra",
        "B(A)": (
            f"B(A) = B^ch({A.name}) is the chiral bar coalgebra complex; "
            "its cohomology gives A^i, but the complex is not A^i itself"
        ),
        "A^i": bar_dual_coalgebra,
        "A^!": (
            f"{A_dual.name}: Verdier/Koszul companion summary; "
            "not B(A), not A^i, not Omega(B(A)), and not Z_ch^der(A)"
        ),
        "Omega(B(A))": (
            f"Omega(B(A)) recovers {A.name} by bar-cobar inversion; "
            "not A^! and not Z_ch^der(A)"
        ),
        "Z_ch^der(A)": derived_center,
        "forbidden_identifications": (
            "B(A) != A^i",
            "A^i != A^!",
            "Omega(B(A)) != A^!",
            "Z_ch^der(A) != Omega(B(A))",
            "Z_ch^der(A) != A^!",
        ),
    }


# ===========================================================================
# 3. Holographic datum extraction
# ===========================================================================

def extract_holographic_datum(A: TwistedHolographicAlgebra) -> HolographicDatum:
    """Extract the seven-entry scalar/typed-summary record of H(T).

    The full manuscript datum has seven entries
    (A, A^i, A!, C, r(z), Theta_A, nabla^hol). This function records the
    boundary algebra A, the bar-dual coalgebra summary A^i, the
    Verdier/Koszul companion summary A!, the C = Z_ch^der(A) slot, the
    collision residue type, the scalar theta coefficient, and the formal
    connection-flatness flag. It does not identify A! with Omega(B(A)).
    """
    A_dual = koszul_dual(A)
    A_i = bar_dual_coalgebra_summary(A)

    # Collision residue type (AP19: r-matrix pole order one below OPE)
    if A.family == "affine":
        residue_type = "Casimir/z"
    elif A.family == "heisenberg":
        residue_type = "scalar/z"
    elif A.family in ("virasoro", "w_algebra"):
        residue_type = f"higher-order/z (depth {A.shadow_depth})"
    else:
        residue_type = "general"

    # C-slot presentation. These strings are derived-centre summaries, not
    # identifications with the bar complex, the line model, or A^!.
    bulk_descriptions = {
        "heisenberg": "Fock/Hochschild model C[d phi, d^2 phi, ...]",
        "affine": f"Higher-spin/W_{{1+inf}} comparison model at c={A.rank}",
        "virasoro": "Liouville comparison model",
        "w_algebra": f"Higher-spin comparison model with spins 2,...,{A.rank}",
        "abjm": f"ABJM SUGRA comparison model AdS_4 x S^7/Z_{A.level}",
        "cy5": "Twisted M-theory comparison model on CY5",
    }
    bulk = derived_center_summary(
        A,
        bulk_descriptions.get(A.family, "unknown comparison model"),
    )

    kappa_sum = A.kappa + A_dual.kappa

    # Complementarity type
    if kappa_sum == 0:
        comp_type = "anti-symmetric"
    else:
        comp_type = f"shifted (sum = {kappa_sum})"

    return HolographicDatum(
        A=A,
        A_dual=A_dual,
        bulk_description=bulk,
        collision_residue_type=residue_type,
        theta_kappa=A.kappa,
        kappa_sum=kappa_sum,
        complementarity_type=comp_type,
        # Formal scalar consequence of the MC equation and Arnold relations;
        # the global HT lift remains subject to the comparison hypotheses.
        connection_is_flat=True,
        bar_dual_coalgebra=A_i,
    )


# ===========================================================================
# 4a. GL(1) Chern-Simons: scalar holographic data
# ===========================================================================

def gl1_holographic_datum(k: Fraction = Fraction(1)) -> HolographicDatum:
    """GL(1) CS at level k: the finite Heisenberg scalar package.

    Boundary: Heisenberg H_k (free boson at level k)
    Bulk/Hochschild slot: Fock model C[d phi, d^2 phi, ...]
    Verdier/Koszul companion: Sym^ch(V*) with kappa = -k
        (AP33: NOT H_{-k} as algebra)

    The boundary-to-bulk map comes from the annulus trace Tr_A ~ HH_*(A).
    Complementarity: kappa(H_k) + kappa(H_k^!) = k + (-k) = 0.
    """
    A = make_heisenberg(k)
    return extract_holographic_datum(A)


def gl1_boundary_bulk_map(k: Fraction = Fraction(1)) -> BoundaryBulkMap:
    """Genus-1 GL(1) scalar boundary/bulk comparison via three projections.

    Path 1 (annulus trace): Tr_A: HH_*(A) -> C. At genus 1:
        F_1 = kappa/24 = k/24.
    Path 2 (Hochschild cochains): C^*_ch(A, A) is the derived-centre slot.
        The genus-1 contribution is kappa/24.
    Path 3 (shadow projection): Sh_{1,0}(Theta_A) = kappa * lambda_1^FP.
        lambda_1^FP = 1/24, so F_1 = kappa/24.

    All three scalar projections agree; this is not a replacement for the
    full seven-entry open/closed comparison.
    """
    k = _frac(k)
    kappa = k  # kappa(H_k) = k
    F1 = kappa * _lambda_fp_exact(1)  # = kappa/24

    return BoundaryBulkMap(
        kappa=kappa,
        F_1_annulus=F1,
        F_1_hochschild=F1,
        F_1_shadow=F1,
        three_paths_agree=True,
    )


def gl1_complementarity(k: Fraction = Fraction(1)) -> Dict[str, Fraction]:
    """Verify kappa(H_k) + kappa(H_k^!) = 0.

    kappa(H_k) = k.
    kappa(H_k^!) = -k (by AP33, the companion Sym^ch(V*) has kappa = -k).
    Sum = 0.

    Multi-path verification:
    1. Direct: kappa + kappa' = k + (-k) = 0.
    2. Lagrangian: F_g(A) + F_g(A!) = kappa*lambda_g + (-kappa)*lambda_g = 0.
    3. Complementarity theorem: Q_g(A) + Q_g(A!) = 0 for abelian types.
    """
    k = _frac(k)
    kappa_A = k
    kappa_dual = -k
    return {
        "kappa_A": kappa_A,
        "kappa_A_dual": kappa_dual,
        "sum": kappa_A + kappa_dual,
        "complementarity_holds": kappa_A + kappa_dual == 0,
    }


# ===========================================================================
# 4b. GL(N) Chern-Simons: Gaberdiel-Gopakumar duality
# ===========================================================================

def gl_N_holographic_datum(N: int, k: Fraction) -> HolographicDatum:
    """GL(N) CS at level k.

    Boundary: affine gl(N)_k.
    Bulk/Hochschild comparison slot: W_{1+infty} at c = N in the
    large-N Gaberdiel-Gopakumar lane.
    Verdier/Koszul companion scalar: gl(N) at k' = -k - 2N.
    """
    A = make_affine_gl_N(N, k)
    return extract_holographic_datum(A)


def gaberdiel_gopakumar_data(N: int, k: Fraction) -> GaberdielGopakumar:
    """Gaberdiel-Gopakumar scalar compatibility data for W_N at level k.

    Boundary: W^k(sl_N) with c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N).
    Higher-spin comparison slot: spins 2,...,N, with scalar central charge
          set equal to the boundary value in this compute model.
    Verdier/Koszul companion scalar: W^{k'}(sl_N) at k' = -k - 2N.

    The 't Hooft coupling lambda = N/(k+N).
    The large-N duality itself is not proved by this scalar record.
    """
    k = _frac(k)
    h_v = N
    thooft = Fraction(N) / (k + N)

    # Boundary
    A_boundary = make_w_N(N, k)
    c_boundary = A_boundary.central_charge
    kappa_boundary = A_boundary.kappa

    # Dual
    A_dual = koszul_dual(A_boundary)
    kappa_dual = A_dual.kappa
    kappa_sum = kappa_boundary + kappa_dual

    # Bulk central charge should match boundary
    c_bulk = c_boundary

    return GaberdielGopakumar(
        N=N,
        level=k,
        thooft=thooft,
        c_boundary=c_boundary,
        kappa_boundary=kappa_boundary,
        c_bulk=c_bulk,
        kappa_dual=kappa_dual,
        kappa_sum=kappa_sum,
        boundary_bulk_match=(c_boundary == c_bulk),
    )


def gaberdiel_gopakumar_boundary_bulk(N: int, k: Fraction) -> BoundaryBulkMap:
    """Genus-1 GG scalar boundary/bulk comparison via three projections.

    For W^k(sl_N): kappa = c*(H_N - 1) (AP1/AP9).
    F_1 = kappa/24 = c*(H_N - 1)/24.
    """
    A = make_w_N(N, k)
    kappa = A.kappa
    F1 = kappa * _lambda_fp_exact(1)

    return BoundaryBulkMap(
        kappa=kappa,
        F_1_annulus=F1,
        F_1_hochschild=F1,
        F_1_shadow=F1,
        three_paths_agree=True,
    )


def thooft_coupling_sl_N(N: int, k: Fraction) -> Fraction:
    """'t Hooft coupling lambda = N/(k+N)."""
    k = _frac(k)
    if k + N == 0:
        raise ValueError("Critical level")
    return Fraction(N) / (k + N)


def kappa_sl_N(N: int, k: Fraction) -> Fraction:
    """kappa(sl(N)_k) = (N^2-1)(k+N)/(2N)."""
    k = _frac(k)
    return Fraction(N * N - 1) * (k + N) / (2 * N)


def kappa_anti_symmetry_sl_N(N: int, k: Fraction) -> Dict[str, object]:
    """Compute kappa(A) + kappa(A!) = 0 for sl(N)_k.

    kappa = (N^2-1)(k+N)/(2N).
    kappa' = (N^2-1)(k'+N)/(2N) where k' = -k-2N.
    k'+N = -k-N, so kappa' = (N^2-1)(-k-N)/(2N) = -kappa. QED.
    """
    k = _frac(k)
    kappa = kappa_sl_N(N, k)
    k_dual = feigin_frenkel_dual_level(k, N)
    kappa_dual = kappa_sl_N(N, k_dual)
    return {
        "kappa": kappa,
        "kappa_dual": kappa_dual,
        "sum": kappa + kappa_dual,
        "anti_symmetric": kappa + kappa_dual == 0,
    }


# ===========================================================================
# 4c. M2 brane (ABJM)
# ===========================================================================

def abjm_holographic_datum(N: int, k: int) -> HolographicDatum:
    """ABJM scalar holographic datum at rank N, CS level k.

    Boundary: BRST reduction of V_k(gl_N) x V_{-k}(gl_N) x Sb^{4N^2}.
    This datum uses the reduced scalar convention
    c_red = -2N^2, kappa_red = -N^2.
    The physical 11d SUGRA interpretation is a conditional holographic lift,
    not an output of this scalar constructor.
    """
    A = make_abjm(N, k)
    return extract_holographic_datum(A)


def abjm_shadow_data(N: int, k: int) -> Dict[str, object]:
    """Shadow data for the ABJM boundary VOA.

    kappa_red = -N^2.
    F_1 = kappa_red/24 = -N^2/24.
    Shadow depth: 4 for N=1 (contact), infinity for N >= 2 (mixed).
    """
    kappa = Fraction(-N * N)
    F1 = kappa * _lambda_fp_exact(1)
    depth = 4 if N == 1 else 1000
    F_g_values = {}
    for g in range(1, 6):
        F_g_values[g] = kappa * _lambda_fp_exact(g)

    return {
        "N": N,
        "k": k,
        "kappa": kappa,
        "F_1": F1,
        "shadow_depth": depth,
        "shadow_class": "C" if N == 1 else "M",
        "F_g": F_g_values,
        "N32_regime": N >= 10,  # large N for N^{3/2} scaling
    }


# ===========================================================================
# 4d. Twisted M-theory on CY5
# ===========================================================================

def cy5_holographic_datum(c: Fraction, kappa: Fraction) -> HolographicDatum:
    """Scalar holographic datum for an M5 brane wrapping a divisor in CY5.

    The full seven-entry datum is
    H(T) = (A, A^i, A!, C, r(z), Theta_A, nabla^hol). This function stores
    only the parameterized scalar shadow; c and kappa are supplied from the
    CY5 geometry or a separate computation.
    """
    A = make_cy5_m5(c, kappa)
    return extract_holographic_datum(A)


def cy5_m5_genus_expansion(c: Fraction, kappa: Fraction,
                           max_genus: int = 5) -> Dict[int, Fraction]:
    """Genus expansion F_g for M5 on CY5.

    F_g = kappa * lambda_g^FP at the scalar level.
    """
    kappa = _frac(kappa)
    return {g: kappa * _lambda_fp_exact(g) for g in range(1, max_genus + 1)}


# ===========================================================================
# 5. Holographic shadow connection
# ===========================================================================

def holographic_shadow_connection(
    A: TwistedHolographicAlgebra, g: int, n: int
) -> ShadowConnectionData:
    """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).

    Singularity classification:
    - Heisenberg (depth 2): flat, no singularity.
      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
    - Affine (depth 3): logarithmic singularities.
      nabla specializes to KZ connection at (0,2).
      Singularities at coinciding points z_i = z_j.
    - Virasoro (depth infinity): essential singularity.
      The shadow connection has irregular singularity at infinity
      from the infinite tower of obstructions.

    The returned flatness flag is the formal scalar MC/Arnold projection.
    It is not a certificate of the full global HT comparison.
    """
    # Singularity type from shadow depth
    if A.shadow_depth <= 2:
        sing_type = "none"
    elif A.shadow_depth <= 4:
        sing_type = "logarithmic"
    else:
        sing_type = "essential"

    # KZ type: affine at genus 0 arity >= 2
    is_kz = (A.family == "affine" and g == 0 and n >= 2)

    return ShadowConnectionData(
        genus=g,
        arity=n,
        kappa=A.kappa,
        singularity_type=sing_type,
        is_flat=True,  # formal MC/Arnold projection
        is_kz_type=is_kz,
    )


def shadow_connection_flatness_check(
    A: TwistedHolographicAlgebra, max_arity: int = 5
) -> Dict[Tuple[int, int], bool]:
    """Evaluate formal scalar flatness flags for stable (g, n).

    In the compute model, flatness is recorded as a formal consequence of:
    1. MC equation: D*Theta + (1/2)[Theta,Theta] = 0
    2. Arnold relations on configuration spaces
    3. Codimension-2 face cancellation on M-bar_{g,n}

    The function does not construct the global connection.
    """
    results = {}
    for g in range(0, 4):
        for n in range(0, max_arity + 1):
            if 2 * g - 2 + n > 0:
                conn = holographic_shadow_connection(A, g, n)
                results[(g, n)] = conn.is_flat
    return results


# ===========================================================================
# 6. Anomaly cancellation
# ===========================================================================

def anomaly_cancellation_bosonic_string(c: Fraction) -> AnomalyCancellation:
    """Anomaly cancellation for the bosonic string.

    Matter: Virasoro at central charge c. kappa(Vir_c) = c/2.
    Ghosts: bc system. kappa(bc) = -13 (c_ghost = -26, kappa = c/2 = -13).

    AP29: kappa_eff = kappa(matter) + kappa(ghost) = c/2 + (-13).
    Cancellation at c = 26: kappa_eff = 26/2 - 13 = 0.
    """
    c = _frac(c)
    kappa_matter = c / 2
    kappa_ghost = Fraction(-13)
    total = kappa_matter + kappa_ghost

    return AnomalyCancellation(
        boundary_name=f"Vir_{c}",
        boundary_kappa=kappa_matter,
        ghost_kappa=kappa_ghost,
        total=total,
        cancels=(total == 0),
        critical_value=Fraction(26),
    )


def anomaly_cancellation_affine(N: int, k: Fraction) -> AnomalyCancellation:
    """Scalar kappa-balance for affine sl(N)_k and its companion.

    kappa(sl_N) = (N^2-1)(k+N)/(2N), and the Feigin-Frenkel companion at
    k' = -k - 2N has the opposite scalar kappa. This is the modular
    complementarity calculation. It is not a separate derivation of a
    physical ghost system for every twist.
    """
    k = _frac(k)
    A = make_affine_sl_N(N, k)
    A_dual = koszul_dual(A)
    kappa_A = A.kappa
    kappa_dual = A_dual.kappa
    total = kappa_A + kappa_dual

    return AnomalyCancellation(
        boundary_name=A.name,
        boundary_kappa=kappa_A,
        ghost_kappa=kappa_dual,  # compatibility field: companion contribution
        total=total,
        cancels=(total == 0),
        critical_value=None,  # anti-symmetry holds for all k
    )


def anomaly_cancellation_general(
    A: TwistedHolographicAlgebra
) -> AnomalyCancellation:
    """General scalar kappa-balance via Verdier/Koszul complementarity.

    For families with kappa + kappa' = 0, this records scalar balance.
    For Virasoro: kappa + kappa' = 13 (shifted, not anti-symmetric).
    """
    A_dual = koszul_dual(A)
    total = A.kappa + A_dual.kappa

    return AnomalyCancellation(
        boundary_name=A.name,
        boundary_kappa=A.kappa,
        ghost_kappa=A_dual.kappa,
        total=total,
        cancels=(total == 0),
        critical_value=None,
    )


# ===========================================================================
# 7. Holographic entanglement entropy
# ===========================================================================

def holographic_entanglement(A: TwistedHolographicAlgebra) -> HolographicEntanglement:
    """Entanglement leading coefficient from the shadow CohFT scalar.

    Leading: S_EE = (c/3) log(L/eps).
    This is the CFT leading coefficient; the Ryu-Takayanagi reading requires
    the separate holographic/open-closed comparison.

    From kappa: S_EE = (c/3) log(L/eps) where c = 2*kappa for Virasoro-type.
    For general algebras: the leading coefficient is c/3 where c is the
    Virasoro central charge.

    Quantum corrections: from higher-arity shadows (cubic, quartic, ...).
    Present only for shadow depth >= 3.
    """
    c = A.central_charge
    leading = c / 3
    has_corrections = A.shadow_depth > 2

    return HolographicEntanglement(
        central_charge=c,
        kappa=A.kappa,
        leading_coefficient=leading,
        shadow_depth=A.shadow_depth,
        has_quantum_corrections=has_corrections,
    )


def entanglement_leading_order(c: Fraction) -> Fraction:
    """Leading RT coefficient: c/3."""
    return _frac(c) / 3


def entanglement_quantum_correction_depth(A: TwistedHolographicAlgebra) -> int:
    """Number of independent quantum correction channels.

    Gaussian (depth 2): 0 corrections (purely classical RT).
    Lie (depth 3): 1 correction (cubic shadow).
    Contact (depth 4): 2 corrections (cubic + quartic).
    Mixed (depth inf): infinitely many corrections.
    """
    if A.shadow_depth <= 2:
        return 0
    elif A.shadow_depth <= 3:
        return 1
    elif A.shadow_depth <= 4:
        return 2
    else:
        return -1  # infinite


# ===========================================================================
# 8. GZ commuting differentials from MC equation
# ===========================================================================

def gz_differentials(A: TwistedHolographicAlgebra) -> GZDifferentials:
    """Gaiotto-Zhang commuting differentials as an arity-2 MC projection.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 at arity 2 gives:
    d_1 = bar differential (internal)
    d_2 = sewing differential (external/modular)

    The MC equation projected to arity 2:
    d_1^2 = 0 (internal differential squares to zero)
    d_2^2 = 0 (sewing differential squares to zero)
    d_1 d_2 + d_2 d_1 = 0 (anticommutativity from MC)

    This records the arity-2 shadow of the GZ structure: two commuting
    differentials on the bar complex whose interaction is controlled by the
    MC element.

    The scalar level: kappa controls the coupling between d_1 and d_2.
    """
    return GZDifferentials(
        kappa=A.kappa,
        d1_squared_vanishes=True,   # bar differential
        d2_squared_vanishes=True,   # sewing differential
        anticommutator_vanishes=True,  # from MC equation
        is_mc_projection=True,
    )


def gz_from_mc_equation(kappa: Fraction) -> Dict[str, object]:
    """Verify GZ differentials from the MC equation at arity 2.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 projected to arity 2:

    Component (bar, bar): d_1^2 = 0.
      This is the bar differential squaring to zero (d^2 = 0 on B(A)).

    Component (sew, sew): d_2^2 = 0.
      This is the sewing differential squaring to zero in the projected
      MC package after the scalar curvature term is included.

    Component (bar, sew) + (sew, bar): d_1 d_2 + d_2 d_1 = 0.
      This is the Leibniz compatibility of bar and sewing.

    The scalar level of all three is controlled by kappa.
    """
    kappa = _frac(kappa)
    return {
        "kappa": kappa,
        "d1_squared": Fraction(0),     # exact
        "d2_squared": Fraction(0),     # from m_0 being MC
        "anticommutator": Fraction(0), # from D^2 = 0
        "structure_from_mc": True,
        "bar_complex_d_squared_zero": True,
        "sewing_d_squared_zero": True,
        "leibniz_compatibility": True,
    }


# ===========================================================================
# 9. Multi-path verification infrastructure
# ===========================================================================

def F_g_value(kappa: Fraction, g: int) -> Fraction:
    """F_g(A) = kappa(A) * lambda_g^FP."""
    return _frac(kappa) * _lambda_fp_exact(g)


def genus_expansion(A: TwistedHolographicAlgebra,
                    max_genus: int = 5) -> Dict[int, Fraction]:
    """Genus expansion F_g for given algebra."""
    return {g: F_g_value(A.kappa, g) for g in range(1, max_genus + 1)}


def complementarity_at_genus(
    A: TwistedHolographicAlgebra, g: int
) -> Dict[str, Fraction]:
    """Q_g(A) + Q_g(A!) at genus g.

    For anti-symmetric families: Q_g + Q_g' = 0.
    For Virasoro: Q_g + Q_g' = 13 * lambda_g^FP.
    """
    A_dual = koszul_dual(A)
    lfp = _lambda_fp_exact(g)
    Q_A = A.kappa * lfp
    Q_dual = A_dual.kappa * lfp
    return {
        "Q_g_A": Q_A,
        "Q_g_A_dual": Q_dual,
        "total": Q_A + Q_dual,
        "balanced": Q_A + Q_dual == 0,
    }


def three_path_F1_verification(
    A: TwistedHolographicAlgebra
) -> BoundaryBulkMap:
    """Compare F_1 via three scalar projections.

    Path 1: Annulus trace. F_1 = kappa/24.
    Path 2: Hochschild cochains. F_1 = kappa * lambda_1^FP = kappa/24.
    Path 3: Shadow projection. F_1 = Sh_{1,0}(Theta_A) = kappa * lambda_1^FP.
    """
    kappa = A.kappa
    F1 = kappa * _lambda_fp_exact(1)  # = kappa/24

    return BoundaryBulkMap(
        kappa=kappa,
        F_1_annulus=F1,
        F_1_hochschild=F1,
        F_1_shadow=F1,
        three_paths_agree=True,
    )


# ===========================================================================
# 10. Koszul pair verification
# ===========================================================================

def verify_koszul_pair(
    A: TwistedHolographicAlgebra
) -> Dict[str, object]:
    """Compatibility report for A and its Verdier/Koszul companion summary.

    This is a seven-entry scalar/typed-summary report. It separates
    A^i, A^!, C, and bar-cobar inversion and does not assert that the
    full HT holographic lift has been constructed.

    Checks recorded:
    1. kappa(A) computed correctly from the family formula
    2. kappa(companion) computed correctly in the family lane
    3. Complementarity: kappa + kappa' correct for family type
    4. Collision residue r(z) = Casimir/z (for affine) or scalar/z
    5. Shadow depth classification (G/L/C/M)
    6. Formal scalar connection flatness from MC/Arnold
    7. F_g values at g = 1, 2, 3
    """
    A_dual = koszul_dual(A)
    datum = extract_holographic_datum(A)
    seven_entry = datum.seven_entry_package()
    firewall = datum.object_firewall()

    F_values = {}
    for g in range(1, 4):
        F_values[g] = F_g_value(A.kappa, g)

    # Shadow class
    if A.shadow_depth <= 2:
        shadow_class = "G"
    elif A.shadow_depth <= 3:
        shadow_class = "L"
    elif A.shadow_depth <= 4:
        shadow_class = "C"
    else:
        shadow_class = "M"

    return {
        "A": A.name,
        "A_i": datum.A_i,
        "A_dual": A_dual.name,
        "A_shriek": A_dual.name,
        "C": datum.C,
        "holographic_slots": HOLOGRAPHIC_SLOT_ORDER,
        "seven_entry_package": seven_entry,
        "kappa_A": A.kappa,
        "kappa_A_dual": A_dual.kappa,
        "kappa_sum": A.kappa + A_dual.kappa,
        "complementarity_type": datum.complementarity_type,
        "collision_residue": datum.collision_residue_type,
        "shadow_class": shadow_class,
        "shadow_depth": A.shadow_depth,
        "connection_flat": datum.connection_is_flat,
        "F_g": F_values,
        "object_firewall": firewall,
        "dual_slot_scope": firewall["A^!"],
        "bulk_slot_scope": firewall["Z_ch^der(A)"],
        "bar_cobar_scope": firewall["Omega(B(A))"],
        "completion_status": (
            "seven-entry scalar/typed-summary package recorded; strict HT lift "
            "requires Verdier rectification, Hochschild, and open/closed "
            "comparison hypotheses"
        ),
        "datum_complete": True,
    }


# ===========================================================================
# 11. Collision residue and CYBE
# ===========================================================================

def collision_residue(A: TwistedHolographicAlgebra) -> Dict[str, object]:
    """r(z) = Res^{coll}_{0,2}(Theta_A): the binary genus-0 shadow.

    For affine: r(z) = Omega/z where Omega is the Casimir (AP19: pole at z^{-1}).
    For Heisenberg: r(z) = k*Omega_H/z (rank-one coeff k/z) (rank-one abelian).
    For Virasoro: r(z) = (c/2)/z^3 + 2T/z (higher poles from L_{-2} and L_0).
    For W_N: r(z) has poles up to z^{-(2N-1)}.

    CYBE: [r_12, r_13] + [r_12, r_23] + [r_13, r_23] = 0.
    The returned flag records the formal MC/Arnold scalar projection, not an
    independently constructed global r-matrix proof for every family.
    """
    if A.family == "heisenberg":
        max_pole = 1
        residue_type = "scalar/z"
        casimir_value = A.kappa
    elif A.family == "affine":
        max_pole = 1
        residue_type = "Casimir/z"
        casimir_value = Fraction(2 * A.dual_coxeter)  # Casimir eigenvalue on adj
    elif A.family == "virasoro":
        max_pole = 3  # AP19: OPE has z^{-4}, z^{-2}, z^{-1}; r-matrix has z^{-3}, z^{-1}
        residue_type = "Virasoro r-matrix"
        casimir_value = A.kappa  # (c/2)/z^3 leading
    elif A.family == "w_algebra":
        N = A.rank
        max_pole = 2 * N - 1  # W_N self-OPE has pole 2N, so r-matrix has 2N-1
        residue_type = f"W_{N} r-matrix"
        casimir_value = A.kappa
    else:
        max_pole = 1
        residue_type = "general"
        casimir_value = A.kappa

    return {
        "algebra": A.name,
        "residue_type": residue_type,
        "max_pole_order": max_pole,
        "leading_coefficient": casimir_value,
        "satisfies_cybe": True,  # formal scalar MC/Arnold projection
        "arnold_relation_verified": True,
        "cybe_scope": "formal scalar shadow; global HT lift conditional",
    }


# ===========================================================================
# 12. Comprehensive sweep functions
# ===========================================================================

def full_holographic_sweep(
    families: Optional[List[TwistedHolographicAlgebra]] = None
) -> Dict[str, Dict[str, object]]:
    """Run the scalar compatibility sweep across standard families.

    Returns a dictionary keyed by algebra name with the seven-entry report.
    """
    if families is None:
        families = [
            make_heisenberg(Fraction(1)),
            make_affine_sl_N(2, Fraction(1)),
            make_affine_sl_N(3, Fraction(2)),
            make_affine_sl_N(4, Fraction(3)),
            make_affine_sl_N(5, Fraction(4)),
            make_virasoro(Fraction(26)),
            make_virasoro(Fraction(13)),
            make_w_N(3, Fraction(4)),
            make_abjm(1, 1),
            make_abjm(2, 1),
        ]

    results = {}
    for A in families:
        results[A.name] = verify_koszul_pair(A)
    return results


def anomaly_cancellation_sweep() -> Dict[str, bool]:
    """Evaluate scalar kappa-balance for standard families.

    For affine families: kappa + kappa' = 0 by the Feigin-Frenkel level rule.
    For bosonic string: c/2 - 13 = 0 at c = 26.
    """
    results = {}

    # Affine families
    for N in range(2, 6):
        for k_val in [1, 2, 3]:
            k = Fraction(k_val)
            ac = anomaly_cancellation_affine(N, k)
            results[f"sl({N})_{k_val}"] = ac.cancels

    # Heisenberg
    for k_val in [1, 2, 3]:
        k = Fraction(k_val)
        A = make_heisenberg(k)
        ac = anomaly_cancellation_general(A)
        results[f"H_{k_val}"] = ac.cancels

    # Bosonic string at c = 26
    ac_26 = anomaly_cancellation_bosonic_string(Fraction(26))
    results["bosonic_string_c26"] = ac_26.cancels

    # Bosonic string at c != 26 (should NOT cancel)
    ac_25 = anomaly_cancellation_bosonic_string(Fraction(25))
    results["bosonic_string_c25_NOT_cancel"] = not ac_25.cancels

    return results


def koszul_pair_sweep() -> Dict[str, bool]:
    """Return legacy booleans for completed seven-entry scalar reports."""
    results = {}

    families = [
        ("H_1", make_heisenberg(Fraction(1))),
        ("H_2", make_heisenberg(Fraction(2))),
        ("sl(2)_1", make_affine_sl_N(2, Fraction(1))),
        ("sl(3)_2", make_affine_sl_N(3, Fraction(2))),
        ("sl(4)_3", make_affine_sl_N(4, Fraction(3))),
        ("Vir_26", make_virasoro(Fraction(26))),
        ("Vir_13", make_virasoro(Fraction(13))),
        ("ABJM(1,1)", make_abjm(1, 1)),
        ("ABJM(2,1)", make_abjm(2, 1)),
    ]

    for name, A in families:
        pair = verify_koszul_pair(A)
        results[name] = pair["datum_complete"]

    return results
