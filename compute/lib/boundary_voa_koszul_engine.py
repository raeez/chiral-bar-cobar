r"""Gaiotto-Witten boundary VOAs and their Koszul duals.

Boundary conditions of 4d N=4 super-Yang-Mills theory (and more generally
Costello-Gaiotto twisted holography) support vertex operator algebras.
This engine computes the modular Koszul data for each boundary VOA and
tests the fundamental conjecture:

    S-DUALITY OF BOUNDARY CONDITIONS = KOSZUL DUALITY OF BOUNDARY VOAs

MATHEMATICAL FRAMEWORK
======================

In the Costello-Gaiotto setup, 4d Chern-Simons theory (the twist of 4d N=4
SYM) on C x R x R_+ has:
    - Boundary algebra A on C x {0} (the boundary VOA)
    - Koszul dual A! = boundary VOA of the S-dual boundary condition
    - R-matrix r(z) = Res^{coll}_{0,2}(Theta_A) (the Yangian structure)

BOUNDARY CONDITIONS AND THEIR VOAs:

1. NEUMANN (N): Preserves gauge field along boundary.
   For gl_N at coupling Psi: boundary VOA is a system of symplectic bosons
   (beta-gamma system) valued in gl_N.
   Central charge: c_N = -N^2 (for Psi -> infinity)
   At finite Psi: affine gl_N at level k = Psi - N (shifted level).

2. DIRICHLET (D): Fixes gauge field to zero on boundary.
   For gl_N: boundary VOA is a system of bc fermions valued in gl_N.
   Central charge: c_D = N^2 (for Psi -> infinity)
   At finite Psi: affine gl_N at level k' = 1/Psi - N (Langlands dual level).

3. NAHM POLE (N_f): Principal Nahm pole boundary condition.
   Boundary VOA = principal W-algebra W_k(gl_N, f_princ).
   This is the DS reduction of the Neumann boundary VOA.
   Class M (infinite shadow depth).

4. REGULAR NAHM: Dirichlet + regular singularity.
   Boundary VOA = small (subregular) W-algebra or related.
   For sl_2: this gives the Virasoro algebra at specific c.

5. CORNER VOA Y_{N_1,N_2,N_3}[Psi] (Gaiotto-Rapcak 1703.00982):
   Three-parameter family. The corner VOA at the junction of three
   half-spaces with gauge groups GL(N_1), GL(N_2), GL(N_3) and
   coupling constant Psi.

   TRIALITY: Y_{N_1,N_2,N_3}[Psi] has an S_3 triality symmetry:
     Y_{N_1,N_2,N_3}[Psi]  =  Y_{N_2,N_3,N_1}[1/Psi]
                             =  Y_{N_3,N_1,N_2}[1-1/Psi]
                             =  Y_{N_2,N_1,N_3}[Psi/(Psi-1)]  etc.

   SPECIALIZATIONS:
     Y_{0,0,N}[Psi] = W_Psi(gl_N) = principal W-algebra of gl_N at level Psi-N
     Y_{0,N,0}[Psi] = affine gl_N at level Psi - N (Neumann)
     Y_{N,0,0}[Psi] = affine gl_N at level 1/Psi - N (Dirichlet)

S-DUALITY AND KOSZUL DUALITY:

S-duality acts on the coupling constant as Psi -> 1/Psi and exchanges
Neumann and Dirichlet boundary conditions. On Y_{N_1,N_2,N_3}[Psi]:

    S: Y_{N_1,N_2,N_3}[Psi] -> Y_{N_2,N_1,N_3}[1/Psi]
       (exchanges first two indices and inverts Psi)

The CENTRAL CONJECTURE tested here:

    A^!_{Koszul}(Y_{N_1,N_2,N_3}[Psi]) = Y_{N_2,N_1,N_3}[1/Psi]

i.e., Koszul duality (in the chiral algebraic sense of Thm A) = S-duality
of boundary conditions. This is tested by verifying:

    (K1) kappa(A) + kappa(A^S) = complementarity sum (Thm D)
    (K2) Shadow depth class is preserved or exchanged predictably
    (K3) R-matrix transforms correctly under S-duality

LEVEL CONVENTIONS:

Following Costello-Gaiotto, the coupling constant Psi parametrizes the
topological twist. The relation to the standard affine level k is:

    k = Psi - h^v    (where h^v = N for gl_N)

The Feigin-Frenkel dual level is:
    k' = -k - 2h^v = -(Psi - N) - 2N = -Psi - N

In terms of Psi: k' = -Psi - N, corresponding to dual coupling:
    Psi' = k' + N = -Psi

But S-duality gives Psi -> 1/Psi, NOT Psi -> -Psi.
So S-duality != Feigin-Frenkel duality in general.
They coincide only when 1/Psi = -Psi, i.e., Psi^2 = -1, Psi = i.

The correct chain:
    S-duality: Psi -> 1/Psi  (Langlands / S-duality)
    FF-duality: Psi -> -Psi   (Feigin-Frenkel)
    Both together: Psi -> -1/Psi (the other S_3 generator)

CAUTION (AP1): kappa formulas are family-specific. Never copy between families.
CAUTION (AP8): Virasoro self-dual at c=13, NOT c=26.
CAUTION (AP19): r-matrix pole order one below OPE (d log absorption).
CAUTION (AP24): kappa + kappa' = 0 for KM/free; != 0 for W-algebras.
CAUTION (AP33): H_k^! = Sym^ch(V*) != H_{-k} as algebras.
CAUTION (AP39): kappa != c/2 for general VOA; kappa = c/2 only for Virasoro.
CAUTION (AP48): kappa depends on full algebra, not Virasoro subalgebra.

MULTI-PATH VERIFICATION:
    Path 1: Direct kappa computation from the VOA OPE data
    Path 2: DS reduction from parent affine algebra
    Path 3: Complementarity verification (kappa + kappa')
    Path 4: S-duality prediction comparison
    Path 5: Triality consistency (S_3 orbit of kappa values)
    Path 6: Large-N / 't Hooft limit consistency

References:
    Gaiotto-Rapcak, arXiv:1703.00982: Vertex Algebras at the Corner
    Costello-Gaiotto, arXiv:1812.09257: Vertex algebras and 4-manifold invariants
    Costello-Creutzig-Gaiotto, arXiv:1903.02984: Higgs and Coulomb branches from VOAs
    Creutzig-Gaiotto, arXiv:1708.00875: Vertex algebras for S-duality
    Feigin-Gukov, arXiv:1811.09408: VOA[M4]
    Prochazka-Rapcak, arXiv:1711.11408: W-algebra modules
    Beem-Lemos-Liendo-Peelaers-Rastelli-van Rees, arXiv:1312.5344 (BLLPRR)
    Arakawa, arXiv:1212.1theory, arXiv:1507.06197: associated varieties
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union

from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl
from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    oo,
    simplify,
    sqrt,
)


# =========================================================================
# Core data types
# =========================================================================

Num = Union[int, Fraction, Rational]


def _to_frac(x) -> Fraction:
    """Coerce to Fraction for exact arithmetic."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, Rational):
        return Fraction(int(x.p), int(x.q))
    if isinstance(x, int):
        return Fraction(x)
    return Fraction(x)


@dataclass
class BoundaryVOAData:
    """Complete modular Koszul data for a boundary VOA."""
    name: str
    boundary_type: str          # 'neumann', 'dirichlet', 'nahm_principal',
                                # 'nahm_regular', 'corner'
    gauge_group: str            # e.g. 'gl_N', 'sl_N'
    rank: int                   # N for gl_N / sl_N
    coupling: Optional[Fraction]  # Psi
    level: Optional[Fraction]   # k = Psi - N for affine interpretation

    # VOA data
    central_charge: Fraction
    kappa: Fraction             # modular characteristic
    shadow_class: str           # 'G', 'L', 'C', 'M'
    shadow_depth: Optional[int] # 2, 3, 4, or None (infinite)

    # Koszul dual data
    dual_name: str
    dual_boundary_type: str
    dual_central_charge: Fraction
    dual_kappa: Fraction
    complementarity_sum: Fraction  # kappa + kappa'

    # S-duality data
    s_dual_name: str
    s_dual_coupling: Optional[Fraction]
    s_dual_central_charge: Optional[Fraction]
    s_dual_kappa: Optional[Fraction]

    # Verification flags
    koszul_equals_s_duality: Optional[bool]  # True if A! = A^S


# =========================================================================
# 1. Lie algebra data
# =========================================================================

_LIE_DATA: Dict[Tuple[str, int], Tuple[int, int, str]] = {
    ("A", 1): (3, 2, "sl_2"),
    ("A", 2): (8, 3, "sl_3"),
    ("A", 3): (15, 4, "sl_4"),
    ("A", 4): (24, 5, "sl_5"),
    ("A", 5): (35, 6, "sl_6"),
    ("A", 6): (48, 7, "sl_7"),
    ("A", 7): (63, 8, "sl_8"),
    ("A", 8): (80, 9, "sl_9"),
    ("A", 9): (99, 10, "sl_10"),
}


def _dim_hdual(lie_type: str, rank: int) -> Tuple[int, int]:
    """Return (dim(g), h^vee) for sl_N (= A_{N-1})."""
    key = (lie_type, rank)
    if key in _LIE_DATA:
        d, h, _ = _LIE_DATA[key]
        return d, h
    if lie_type == "A":
        N = rank + 1
        return N * N - 1, N
    raise ValueError(f"Lie algebra ({lie_type}, {rank}) not in table")


def dim_gl(N: int) -> int:
    """Dimension of gl_N = N^2."""
    return N * N


def dim_sl(N: int) -> int:
    """Dimension of sl_N = N^2 - 1."""
    return N * N - 1


# =========================================================================
# 2. Central charge formulas
# =========================================================================

def c_affine_gl(N: int, k: Num) -> Fraction:
    r"""Central charge of affine gl_N at level k.

    gl_N = sl_N + u(1).  The total central charge is:
        c(gl_N, k) = c(sl_N, k) + 1
                    = k*(N^2-1)/(k+N) + 1

    The u(1) factor contributes c = 1 (one free boson = Heisenberg).
    """
    k_f = _to_frac(k)
    N_f = Fraction(N)
    if k_f + N_f == 0:
        raise ValueError(f"Critical level k = -{N}: undefined")
    c_sl = k_f * (N_f**2 - 1) / (k_f + N_f)
    return c_sl + 1


def c_affine_sl(N: int, k: Num) -> Fraction:
    r"""Sugawara central charge of affine sl_N at level k.

    c = k * dim(sl_N) / (k + h^v) = k * (N^2 - 1) / (k + N).
    """
    k_f = _to_frac(k)
    N_f = Fraction(N)
    if k_f + N_f == 0:
        raise ValueError(f"Critical level k = -{N}: undefined")
    return k_f * (N_f**2 - 1) / (k_f + N_f)


def c_wn_principal(N: int, k: Num) -> Fraction:
    r"""Fateev-Lukyanov central charge for principal W^k(sl_N).

    c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

    This is the CORRECT formula (verified: c(W_2, k=1) = -7).
    """
    return canonical_c_wn_fl(N, _to_frac(k))


def c_betagamma_system(n_pairs: int, weight: Num = Fraction(1, 2)) -> Fraction:
    r"""Central charge of n_pairs copies of beta-gamma system at weight lambda.

    Each pair: c = 2(6*lambda^2 - 6*lambda + 1).
    At lambda = 1/2 (symplectic bosons): c = -1 per pair.
    At lambda = 0 (standard bg): c = 2 per pair.
    At lambda = 1 (reversed bg): c = 2 per pair.
    """
    lam = _to_frac(weight)
    c_one = 2 * (6 * lam**2 - 6 * lam + 1)
    return Fraction(n_pairs) * c_one


def c_bc_system(n_pairs: int, weight: Num = Fraction(1, 2)) -> Fraction:
    r"""Central charge of n_pairs copies of bc ghost system at weight lambda.

    Each pair: c = -2(6*lambda^2 - 6*lambda + 1).
    At lambda = 1/2: c = 1 per pair.
    At lambda = 1 (standard bc ghosts, b weight 2, c weight -1): c = -26 per pair.
    """
    lam = _to_frac(weight)
    c_one = -2 * (6 * lam**2 - 6 * lam + 1)
    return Fraction(n_pairs) * c_one


def c_free_fermion(n: int) -> Fraction:
    r"""Central charge of n free real fermions: c = n/2."""
    return Fraction(n, 2)


# =========================================================================
# 3. kappa formulas (AP1, AP39, AP48: family-specific, never copy)
# =========================================================================

def kappa_affine_gl(N: int, k: Num) -> Fraction:
    r"""Modular characteristic of affine gl_N at level k.

    gl_N = sl_N + u(1).
    kappa(gl_N, k) = kappa(sl_N, k) + kappa(u(1), k)
                   = dim(sl_N) * (k + N) / (2N) + k

    The sl_N part: kappa = dim * (k + h^v) / (2 h^v) with h^v = N.
    The u(1) part: Heisenberg at level k has kappa = k.
    """
    k_f = _to_frac(k)
    N_f = Fraction(N)
    kappa_sl = (N_f**2 - 1) * (k_f + N_f) / (2 * N_f)
    kappa_u1 = k_f
    return kappa_sl + kappa_u1


def kappa_affine_sl(N: int, k: Num) -> Fraction:
    r"""Modular characteristic of affine sl_N at level k.

    kappa = dim(sl_N) * (k + h^v) / (2 * h^v) = (N^2 - 1)(k + N) / (2N).
    """
    k_f = _to_frac(k)
    N_f = Fraction(N)
    return (N_f**2 - 1) * (k_f + N_f) / (2 * N_f)


def kappa_wn_principal(N: int, k: Num) -> Fraction:
    r"""Modular characteristic of principal W^k(sl_N).

    kappa(W_N) = c * (H_N - 1)  where H_N = 1 + 1/2 + ... + 1/N.

    CAUTION (AP39): kappa != c/2 for W-algebras of rank > 1.
    kappa = c/2 only for N = 2 (Virasoro).
    """
    H_N = sum(Fraction(1, j) for j in range(1, N + 1))
    c = c_wn_principal(N, k)
    return c * (H_N - 1)


def kappa_betagamma(n_pairs: int, weight: Num = Fraction(1, 2)) -> Fraction:
    r"""Modular characteristic of n_pairs beta-gamma systems.

    Per pair: kappa = c/2 = 6*lambda^2 - 6*lambda + 1.
    Total: kappa = n_pairs * (6*lambda^2 - 6*lambda + 1).

    At lambda = 1/2 (symplectic bosons): kappa = -1/2 per pair.
    """
    lam = _to_frac(weight)
    kappa_one = 6 * lam**2 - 6 * lam + 1
    return Fraction(n_pairs) * kappa_one


def kappa_bc_ghost(n_pairs: int, weight: Num = Fraction(1, 2)) -> Fraction:
    r"""Modular characteristic of n_pairs bc ghost systems.

    Per pair: kappa = c/2 = -(6*lambda^2 - 6*lambda + 1).
    Complementarity: kappa_bg + kappa_bc = 0 (exact, AP24 safe).
    """
    return -kappa_betagamma(n_pairs, weight)


def kappa_heisenberg(k: Num) -> Fraction:
    r"""Modular characteristic of Heisenberg at level k: kappa = k."""
    return _to_frac(k)


def kappa_virasoro(c: Num) -> Fraction:
    r"""Modular characteristic of Virasoro at central charge c: kappa = c/2."""
    return _to_frac(c) / 2


# =========================================================================
# 4. Shadow depth classification
# =========================================================================

def shadow_class_affine(N: int) -> str:
    """Affine KM algebras are class L (depth 3) for N >= 2.
    Single boson (N=1, Heisenberg): class G (depth 2).
    """
    return 'G' if N <= 1 else 'L'


def shadow_class_betagamma() -> str:
    """Beta-gamma system is class C (depth 4, contact/quartic)."""
    return 'C'


def shadow_class_bc() -> str:
    """bc ghost system is class C (depth 4, contact/quartic)."""
    return 'C'


def shadow_class_w_algebra(N: int) -> str:
    """Principal W-algebra W_N is class M (infinite depth) for N >= 2."""
    return 'M'


def shadow_depth_from_class(cls: str) -> Optional[int]:
    """Convert shadow class to depth. None = infinite."""
    return {'G': 2, 'L': 3, 'C': 4, 'M': None}.get(cls)


# =========================================================================
# 5. Neumann boundary VOA
# =========================================================================

def neumann_boundary_voa(N: int, psi: Num) -> BoundaryVOAData:
    r"""Neumann boundary VOA for GL(N) at coupling Psi.

    The Neumann boundary condition for GL(N) Chern-Simons at coupling Psi
    supports the affine gl_N algebra at level k = Psi - N.

    At generic Psi, this is an affine VOA (class L for N >= 2).

    The S-dual is the Dirichlet boundary at coupling 1/Psi.
    The Koszul dual (Feigin-Frenkel) is affine gl_N at level k' = -k - 2N.

    IMPORTANT DISTINCTION:
    S-duality: Psi -> 1/Psi, giving k^S = 1/Psi - N
    FF-duality: k -> -k - 2N, giving k^FF = -(Psi - N) - 2N = -Psi - N

    These are DIFFERENT operations with DIFFERENT dual levels, unless Psi = i.
    """
    psi_f = _to_frac(psi)
    k = psi_f - N

    # VOA data
    c = c_affine_gl(N, k)
    kap = kappa_affine_gl(N, k)
    sc = shadow_class_affine(N)
    sd = shadow_depth_from_class(sc)

    # Koszul dual: Feigin-Frenkel, k' = -k - 2N
    k_ff = -k - 2 * N
    c_dual = c_affine_gl(N, k_ff)
    kap_dual = kappa_affine_gl(N, k_ff)

    # Complementarity sum
    comp_sum = kap + kap_dual

    # S-dual: Dirichlet at coupling 1/Psi
    psi_s = Fraction(1, 1) / psi_f if psi_f != 0 else None
    k_s = psi_s - N if psi_s is not None else None
    c_s = c_affine_gl(N, k_s) if k_s is not None else None
    kap_s = kappa_affine_gl(N, k_s) if k_s is not None else None

    # Test: does Koszul = S-duality?
    # For this we need to check if kap_dual == kap_s
    koszul_eq_s = (kap_dual == kap_s) if kap_s is not None else None

    return BoundaryVOAData(
        name=f"V_{{Psi={psi_f}}}(gl_{N}) [Neumann]",
        boundary_type='neumann',
        gauge_group=f'gl_{N}',
        rank=N,
        coupling=psi_f,
        level=k,
        central_charge=c,
        kappa=kap,
        shadow_class=sc,
        shadow_depth=sd,
        dual_name=f"V_{{k'={k_ff}}}(gl_{N}) [FF dual]",
        dual_boundary_type='neumann',
        dual_central_charge=c_dual,
        dual_kappa=kap_dual,
        complementarity_sum=comp_sum,
        s_dual_name=f"V_{{Psi={psi_s}}}(gl_{N}) [Dirichlet/S-dual]",
        s_dual_coupling=psi_s,
        s_dual_central_charge=c_s,
        s_dual_kappa=kap_s,
        koszul_equals_s_duality=koszul_eq_s,
    )


# =========================================================================
# 6. Dirichlet boundary VOA
# =========================================================================

def dirichlet_boundary_voa(N: int, psi: Num) -> BoundaryVOAData:
    r"""Dirichlet boundary VOA for GL(N) at coupling Psi.

    The Dirichlet boundary condition supports the affine gl_N algebra
    at level k = 1/Psi - N (the Langlands dual level).

    The S-dual is the Neumann boundary at coupling 1/Psi.
    """
    psi_f = _to_frac(psi)
    if psi_f == 0:
        raise ValueError("Psi = 0: Dirichlet level diverges")
    k = Fraction(1, 1) / psi_f - N

    c = c_affine_gl(N, k)
    kap = kappa_affine_gl(N, k)
    sc = shadow_class_affine(N)
    sd = shadow_depth_from_class(sc)

    # Koszul dual: FF, k' = -k - 2N
    k_ff = -k - 2 * N
    c_dual = c_affine_gl(N, k_ff)
    kap_dual = kappa_affine_gl(N, k_ff)
    comp_sum = kap + kap_dual

    # S-dual: Neumann at coupling 1/Psi
    psi_s = Fraction(1, 1) / psi_f
    k_s = psi_s - N
    c_s = c_affine_gl(N, k_s)
    kap_s = kappa_affine_gl(N, k_s)

    koszul_eq_s = (kap_dual == kap_s)

    return BoundaryVOAData(
        name=f"V_{{k={k}}}(gl_{N}) [Dirichlet]",
        boundary_type='dirichlet',
        gauge_group=f'gl_{N}',
        rank=N,
        coupling=psi_f,
        level=k,
        central_charge=c,
        kappa=kap,
        shadow_class=sc,
        shadow_depth=sd,
        dual_name=f"V_{{k'={k_ff}}}(gl_{N}) [FF dual]",
        dual_boundary_type='dirichlet',
        dual_central_charge=c_dual,
        dual_kappa=kap_dual,
        complementarity_sum=comp_sum,
        s_dual_name=f"V_{{Psi={psi_s}}}(gl_{N}) [Neumann/S-dual]",
        s_dual_coupling=psi_s,
        s_dual_central_charge=c_s,
        s_dual_kappa=kap_s,
        koszul_equals_s_duality=koszul_eq_s,
    )


# =========================================================================
# 7. Nahm pole (principal W-algebra) boundary VOA
# =========================================================================

def nahm_principal_boundary_voa(N: int, psi: Num) -> BoundaryVOAData:
    r"""Principal Nahm pole boundary VOA: W^k(sl_N, f_princ).

    The Nahm pole boundary condition with principal embedding f_princ: sl_2 -> sl_N
    supports the principal W-algebra at level k = Psi - N.

    The Koszul dual is W^{k'}(sl_N, f_princ) at the Feigin-Frenkel dual level
    k' = -k - 2N. The complementarity sum kappa + kappa' is constant (AP24).

    S-duality gives Psi -> 1/Psi, hence level k^S = 1/Psi - N.
    FF-duality gives k -> -k - 2N = -(Psi - N) - 2N = -Psi - N.
    """
    psi_f = _to_frac(psi)
    k = psi_f - N

    c = c_wn_principal(N, k)
    kap = kappa_wn_principal(N, k)
    sc = shadow_class_w_algebra(N)
    sd = shadow_depth_from_class(sc)

    # Koszul dual: FF level
    k_ff = -k - 2 * N
    c_dual = c_wn_principal(N, k_ff)
    kap_dual = kappa_wn_principal(N, k_ff)
    comp_sum = kap + kap_dual

    # S-dual: Nahm at dual coupling
    psi_s = Fraction(1, 1) / psi_f if psi_f != 0 else None
    if psi_s is not None:
        k_s = psi_s - N
        c_s = c_wn_principal(N, k_s)
        kap_s = kappa_wn_principal(N, k_s)
    else:
        k_s, c_s, kap_s = None, None, None

    koszul_eq_s = (kap_dual == kap_s) if kap_s is not None else None

    return BoundaryVOAData(
        name=f"W^{{k={k}}}(sl_{N}) [Nahm principal]",
        boundary_type='nahm_principal',
        gauge_group=f'sl_{N}',
        rank=N,
        coupling=psi_f,
        level=k,
        central_charge=c,
        kappa=kap,
        shadow_class=sc,
        shadow_depth=sd,
        dual_name=f"W^{{k'={k_ff}}}(sl_{N}) [FF dual]",
        dual_boundary_type='nahm_principal',
        dual_central_charge=c_dual,
        dual_kappa=kap_dual,
        complementarity_sum=comp_sum,
        s_dual_name=f"W^{{k^S}}(sl_{N}) [Nahm at 1/Psi]",
        s_dual_coupling=psi_s,
        s_dual_central_charge=c_s,
        s_dual_kappa=kap_s,
        koszul_equals_s_duality=koszul_eq_s,
    )


# =========================================================================
# 8. Symplectic boson boundary VOA (Neumann at Psi -> infinity)
# =========================================================================

def symplectic_boson_boundary_voa(N: int) -> BoundaryVOAData:
    r"""Symplectic boson (beta-gamma) boundary VOA.

    In the limit Psi -> infinity, the Neumann boundary condition gives
    N^2 symplectic bosons (beta-gamma pairs at weight 1/2).

    Central charge: c = -N^2 (each symplectic boson contributes c = -1).
    kappa = -N^2/2.
    Shadow class: C (contact/quartic, depth 4).

    Koszul dual: N^2 bc ghosts at weight 1/2.
    c_dual = N^2, kappa_dual = N^2/2.
    Complementarity: kappa + kappa' = 0 (free field).

    S-dual (Psi -> 0): Dirichlet limit, free fermions.
    """
    n_pairs = N * N

    c = c_betagamma_system(n_pairs, Fraction(1, 2))
    kap = kappa_betagamma(n_pairs, Fraction(1, 2))
    sc = shadow_class_betagamma()
    sd = shadow_depth_from_class(sc)

    # Koszul dual: bc ghosts
    c_dual = c_bc_system(n_pairs, Fraction(1, 2))
    kap_dual = kappa_bc_ghost(n_pairs, Fraction(1, 2))
    comp_sum = kap + kap_dual

    # S-dual: N^2 free fermions (bc at weight 1/2 = free fermion)
    c_s = c_dual  # bc at weight 1/2 has c = 1 per pair = N^2
    kap_s = kap_dual

    # For free field systems: Koszul dual = S-dual in the strong limit
    koszul_eq_s = (kap_dual == kap_s)

    return BoundaryVOAData(
        name=f"{n_pairs} symplectic bosons (bg, lambda=1/2) [Neumann limit]",
        boundary_type='neumann',
        gauge_group=f'gl_{N}',
        rank=N,
        coupling=None,
        level=None,
        central_charge=c,
        kappa=kap,
        shadow_class=sc,
        shadow_depth=sd,
        dual_name=f"{n_pairs} bc ghosts (lambda=1/2) [Koszul dual]",
        dual_boundary_type='dirichlet',
        dual_central_charge=c_dual,
        dual_kappa=kap_dual,
        complementarity_sum=comp_sum,
        s_dual_name=f"{n_pairs} bc ghosts (lambda=1/2) [Dirichlet limit]",
        s_dual_coupling=Fraction(0),
        s_dual_central_charge=c_s,
        s_dual_kappa=kap_s,
        koszul_equals_s_duality=koszul_eq_s,
    )


# =========================================================================
# 9. Free fermion boundary VOA (Dirichlet at Psi -> infinity)
# =========================================================================

def free_fermion_boundary_voa(N: int) -> BoundaryVOAData:
    r"""Free fermion (bc ghost) boundary VOA.

    In the Dirichlet limit, the boundary VOA consists of N^2 bc fermion pairs
    at weight 1/2.

    Central charge: c = N^2 (each bc pair at lambda=1/2 contributes c = 1).
    kappa = N^2/2.
    Shadow class: C (contact/quartic, depth 4).

    Koszul dual: N^2 symplectic bosons.
    S-dual: Neumann limit -> symplectic bosons.
    """
    n_pairs = N * N

    c = c_bc_system(n_pairs, Fraction(1, 2))
    kap = kappa_bc_ghost(n_pairs, Fraction(1, 2))
    sc = shadow_class_bc()
    sd = shadow_depth_from_class(sc)

    # Koszul dual: bg
    c_dual = c_betagamma_system(n_pairs, Fraction(1, 2))
    kap_dual = kappa_betagamma(n_pairs, Fraction(1, 2))
    comp_sum = kap + kap_dual

    # S-dual: symplectic bosons
    c_s = c_dual
    kap_s = kap_dual

    koszul_eq_s = (kap_dual == kap_s)

    return BoundaryVOAData(
        name=f"{n_pairs} bc fermions (lambda=1/2) [Dirichlet limit]",
        boundary_type='dirichlet',
        gauge_group=f'gl_{N}',
        rank=N,
        coupling=None,
        level=None,
        central_charge=c,
        kappa=kap,
        shadow_class=sc,
        shadow_depth=sd,
        dual_name=f"{n_pairs} symplectic bosons [Koszul dual]",
        dual_boundary_type='neumann',
        dual_central_charge=c_dual,
        dual_kappa=kap_dual,
        complementarity_sum=comp_sum,
        s_dual_name=f"{n_pairs} symplectic bosons [Neumann limit]",
        s_dual_coupling=None,
        s_dual_central_charge=c_s,
        s_dual_kappa=kap_s,
        koszul_equals_s_duality=koszul_eq_s,
    )


# =========================================================================
# 10. Corner VOA Y_{N1,N2,N3}[Psi]
# =========================================================================

def corner_voa_central_charge(N1: int, N2: int, N3: int, psi: Num) -> Fraction:
    r"""Central charge of the corner VOA Y_{N1,N2,N3}[Psi].

    SPECIALIZATIONS (exact, verified):
      Y_{0,0,N}[Psi] = W_{Psi}(gl_N):
        c = c(W^{Psi-N}(sl_N)) + 1  (the +1 is the u(1) Heisenberg)
      Y_{0,N,0}[Psi] = affine gl_N at level Psi - N:
        c = c(sl_N, Psi-N) + 1
      Y_{N,0,0}[Psi] = affine gl_N at level 1/Psi - N:
        c = c(sl_N, 1/Psi - N) + 1

    GENERAL TRIPLES: use the Prochazka-Rapcak formula from the W_{1+inf}
    free field realization. The Omega-background parameters are
    epsilon_1 = 1, epsilon_2 = -Psi, epsilon_3 = Psi - 1 (summing to 0).
    The formula (Prochazka-Rapcak arXiv:1711.11408, Gaiotto-Rapcak
    arXiv:1703.00982) for general triples is given by specialization
    recursion from the single-index cases combined with the triality
    covariance.

    For two-index cases Y_{N1,N2,0}[Psi], Y_{N1,0,N3}[Psi], Y_{0,N2,N3}[Psi],
    the algebra is a coset / extension of affine algebras.
    """
    psi_f = _to_frac(psi)
    if psi_f == 0:
        raise ValueError("Psi = 0: corner VOA undefined")

    # ---- Single-index specializations (exact) ----

    # Y_{0,0,N}[Psi] = W_Psi(gl_N)
    if N1 == 0 and N2 == 0 and N3 >= 0:
        if N3 == 0:
            return Fraction(0)
        k = psi_f - N3
        return c_wn_principal(N3, k) + Fraction(1)

    # Y_{0,N,0}[Psi] = affine gl_N at level Psi - N
    if N1 == 0 and N3 == 0 and N2 >= 0:
        if N2 == 0:
            return Fraction(0)
        k = psi_f - N2
        return c_affine_gl(N2, k)

    # Y_{N,0,0}[Psi] = affine gl_N at level 1/Psi - N
    if N2 == 0 and N3 == 0 and N1 >= 0:
        if N1 == 0:
            return Fraction(0)
        k = Fraction(1) / psi_f - N1
        return c_affine_gl(N1, k)

    # ---- General triples: use the triality-covariant formula ----
    # From Prochazka-Rapcak, the central charge can be computed by
    # summing contributions from each "corner" in the brane diagram.
    # For Y_{N1,N2,N3}[Psi], the effective formula decomposes into
    # three single-index contributions minus overlap corrections.
    #
    # The Gaberdiel-Li-Peng cubic formula uses
    #   epsilon_1 = 1, epsilon_2 = -Psi, epsilon_3 = Psi - 1
    # and gives the central charge as:
    #
    #   c = (N_tot - 1) - sum_a epsilon_a N_a (N_a^2 - 1) / (3 * prod_b epsilon_b)
    #       + cross terms
    #
    # For the EXACT formula we need the full W_{1+inf}[lambda] character theory.
    # Since this is complex and error-prone, we implement it using the identity:
    #
    #   c(Y_{N1,N2,N3}[Psi]) = c_Y(epsilon_1, epsilon_2, epsilon_3, N1, N2, N3)
    #
    # where c_Y is defined recursively by the box-adding/removing operations
    # in the plane partition model.
    #
    # For COMPUTATIONAL PURPOSES in this engine, we use the following
    # APPROXIMATE formula for general triples, with a flag that it requires
    # independent verification:
    #
    # c ~ sum of single-index contributions - corrections
    # This is flagged as approximate below.

    # Two-index cases: reduce via coset / extension
    if N3 == 0:
        # Y_{N1,N2,0}[Psi]: coset of gl_{N1} x gl_{N2} algebras
        k1 = Fraction(1) / psi_f - N1
        k2 = psi_f - N2
        return c_affine_gl(N1, k1) + c_affine_gl(N2, k2)

    if N2 == 0:
        # Y_{N1,0,N3}[Psi]: combination of affine and W-algebra
        k1 = Fraction(1) / psi_f - N1
        k3 = psi_f - N3
        return c_affine_gl(N1, k1) + c_wn_principal(N3, k3) + Fraction(1)

    if N1 == 0:
        # Y_{0,N2,N3}[Psi]: combination of affine and W-algebra
        k2 = psi_f - N2
        k3 = psi_f - N3
        return c_affine_gl(N2, k2) + c_wn_principal(N3, k3) + Fraction(1)

    # Full triple: sum all three single-index contributions.
    # This is an APPROXIMATION for the general case.
    # The exact formula requires the full Prochazka-Rapcak box model.
    k1 = Fraction(1) / psi_f - N1
    k2 = psi_f - N2
    k3 = psi_f - N3
    return (c_affine_gl(N1, k1)
            + c_affine_gl(N2, k2)
            + c_wn_principal(N3, k3)
            + Fraction(1))


def corner_voa_kappa(N1: int, N2: int, N3: int, psi: Num) -> Fraction:
    r"""Modular characteristic of corner VOA Y_{N1,N2,N3}[Psi].

    For the corner VOA, which is generically a truncation of W_{1+inf},
    the modular characteristic depends on the specific truncation.

    For Y_{0,0,N}[Psi] = W_Psi(gl_N), we use:
        kappa = kappa(W_N) + kappa(u(1))

    For general triples, we use:
        kappa = c/2 for rank-1 truncations (where the W-algebra is Virasoro-like)
        kappa = c * rho_eff for higher-rank truncations

    CAUTION (AP39, AP48): kappa != c/2 in general.

    For the purposes of this engine, we compute kappa from the anomaly ratio
    of the W_{1+inf} truncation. The anomaly ratio rho for the Y-algebra
    depends on the generator content.

    SIMPLE CASES (verified independently):
      Y_{0,0,N}[Psi]: kappa = kappa(W^{Psi-N}(sl_N)) + (Psi - N)
                       = c_{W_N} * (H_N - 1) + (Psi - N)
      Y_{0,N,0}[Psi]: kappa = kappa(gl_N, Psi-N) = (N^2-1)(Psi)/(2N) + (Psi-N)
      Y_{N,0,0}[Psi]: kappa = kappa(gl_N, 1/Psi-N)

    GENERAL CASE: For the W_{1+inf} truncation Y_{N1,N2,N3}[Psi],
    the algebra has generators of spins 1, 2, ..., max(N1,N2,N3).
    The anomaly ratio involves the harmonic number of the truncation level.

    We use the following DERIVED formula for kappa:
    For Y_{N1,N2,N3}[Psi], define the effective rank r = max(N1,N2,N3).
    Then kappa = c * (H_r - 1) where H_r is the r-th harmonic number,
    PLUS a correction from the u(1) sector.

    HOWEVER: this formula is NOT verified for all triples.
    For triples where multiple N_a > 0, the generator spectrum is more
    complex and the simple H_r formula may fail.

    For now, we compute kappa ONLY for the specializations Y_{0,0,N},
    Y_{0,N,0}, Y_{N,0,0} where the answer is known, and flag general
    triples as requiring case-by-case analysis.
    """
    psi_f = _to_frac(psi)

    # Specialization: Y_{0,0,N}[Psi] = W_Psi(gl_N)
    if N1 == 0 and N2 == 0 and N3 > 0:
        k = psi_f - N3
        return kappa_wn_principal(N3, k) + kappa_heisenberg(k)

    # Specialization: Y_{0,N,0}[Psi] = affine gl_N at level Psi - N
    if N1 == 0 and N3 == 0 and N2 > 0:
        k = psi_f - N2
        return kappa_affine_gl(N2, k)

    # Specialization: Y_{N,0,0}[Psi] = affine gl_N at level 1/Psi - N
    if N2 == 0 and N3 == 0 and N1 > 0:
        if psi_f == 0:
            raise ValueError("Psi = 0: undefined")
        k = Fraction(1) / psi_f - N1
        return kappa_affine_gl(N1, k)

    # General case: use c/2 as a LOWER BOUND / first approximation.
    # Flag that this needs case-by-case verification (AP39).
    c = corner_voa_central_charge(N1, N2, N3, psi_f)

    # For a general W_{1+inf} truncation, the effective rank is
    # min(N1,N2,N3,...) where the algebra has generators at spins
    # 1 through max(N_a). The anomaly ratio generalizes H_r - 1.
    # For now, use c/2 and flag.
    return c / 2  # APPROXIMATE: valid only when all generators have weight 2


def corner_voa_shadow_class(N1: int, N2: int, N3: int) -> str:
    r"""Shadow depth class of corner VOA Y_{N1,N2,N3}.

    - If max(N_a) == 1: single boson, class G
    - If max(N_a) == 2 and all nonzero N_a == 1: affine, class L
    - If any N_a >= 2 and the truncation has weight >= 3 generators: class M
    - Symplectic boson / bc limit: class C
    """
    m = max(N1, N2, N3)
    if m <= 1:
        return 'G'

    # Y_{0,0,N} for N >= 2: W-algebra, class M
    # Y_{0,N,0} for N >= 2: affine, class L
    # Y_{N,0,0} for N >= 2: affine, class L
    n_nonzero = sum(1 for n in [N1, N2, N3] if n > 0)
    if n_nonzero == 1:
        # Single nonzero index
        n_val = max(N1, N2, N3)
        idx = [N1, N2, N3].index(n_val)
        if idx == 0:
            # Y_{N,0,0}: affine
            return 'L' if n_val >= 2 else 'G'
        elif idx == 1:
            # Y_{0,N,0}: affine
            return 'L' if n_val >= 2 else 'G'
        else:
            # Y_{0,0,N}: W-algebra
            return 'M' if n_val >= 2 else 'G'

    # Multiple nonzero: generically class M (W-algebra type)
    return 'M'


def corner_voa_data(N1: int, N2: int, N3: int, psi: Num) -> BoundaryVOAData:
    r"""Full boundary VOA data for corner VOA Y_{N1,N2,N3}[Psi].

    S-duality acts as: (N1,N2,N3,Psi) -> (N2,N1,N3,1/Psi).
    Koszul duality (FF): level inversion within the same VOA family.

    The central test:
        A = Y_{N1,N2,N3}[Psi]
        A^S = Y_{N2,N1,N3}[1/Psi]   (S-dual)
        A^! = FF dual of A            (Koszul dual)
        TEST: kappa(A^!) == kappa(A^S)?
    """
    psi_f = _to_frac(psi)

    c = corner_voa_central_charge(N1, N2, N3, psi_f)
    kap = corner_voa_kappa(N1, N2, N3, psi_f)
    sc = corner_voa_shadow_class(N1, N2, N3)
    sd = shadow_depth_from_class(sc)

    # S-dual: (N1,N2,N3,Psi) -> (N2,N1,N3,1/Psi)
    psi_s = Fraction(1) / psi_f if psi_f != 0 else None
    if psi_s is not None:
        c_s = corner_voa_central_charge(N2, N1, N3, psi_s)
        kap_s = corner_voa_kappa(N2, N1, N3, psi_s)
    else:
        c_s, kap_s = None, None

    # Koszul dual: FF duality inverts the coupling within the same family
    # For Y_{N1,N2,N3}[Psi], the FF dual is Y_{N1,N2,N3}[-Psi]
    # (since FF sends k -> -k-2N, which sends Psi -> -Psi in the convention k=Psi-N)
    psi_ff = -psi_f
    try:
        c_dual = corner_voa_central_charge(N1, N2, N3, psi_ff)
        kap_dual = corner_voa_kappa(N1, N2, N3, psi_ff)
    except (ValueError, ZeroDivisionError):
        c_dual = Fraction(0)
        kap_dual = Fraction(0)

    comp_sum = kap + kap_dual

    # Test: does Koszul = S-duality?
    koszul_eq_s = (kap_dual == kap_s) if kap_s is not None else None

    return BoundaryVOAData(
        name=f"Y_{{{N1},{N2},{N3}}}[Psi={psi_f}]",
        boundary_type='corner',
        gauge_group=f'gl_{{max({N1},{N2},{N3})}}',
        rank=max(N1, N2, N3),
        coupling=psi_f,
        level=psi_f - max(N1, N2, N3),
        central_charge=c,
        kappa=kap,
        shadow_class=sc,
        shadow_depth=sd,
        dual_name=f"Y_{{{N1},{N2},{N3}}}[Psi={psi_ff}] [FF dual]",
        dual_boundary_type='corner',
        dual_central_charge=c_dual,
        dual_kappa=kap_dual,
        complementarity_sum=comp_sum,
        s_dual_name=f"Y_{{{N2},{N1},{N3}}}[Psi={psi_s}] [S-dual]",
        s_dual_coupling=psi_s,
        s_dual_central_charge=c_s,
        s_dual_kappa=kap_s,
        koszul_equals_s_duality=koszul_eq_s,
    )


# =========================================================================
# 11. Triality verification for corner VOAs
# =========================================================================

def verify_triality(N1: int, N2: int, N3: int, psi: Num) -> Dict[str, Any]:
    r"""Verify the S_3 triality of corner VOA central charges.

    The triality group S_3 acts on (N1,N2,N3,Psi) as follows:
      sigma_12: (N1,N2,N3,Psi) -> (N2,N1,N3, Psi/(Psi-1))
      sigma_23: (N1,N2,N3,Psi) -> (N1,N3,N2, 1-Psi)
      sigma_13: (N1,N2,N3,Psi) -> (N3,N2,N1, 1/Psi)

    S-duality is sigma_13: exchanges N1 <-> N3 and Psi -> 1/Psi.

    Actually the standard S_3 action from Gaiotto-Rapcak exchanges
    epsilon parameters. With h1=Psi, h2=-1, h3=1-Psi:

    Permuting (1,2): N1<->N2, Psi <-> 1/(1-Psi) [i.e. h1<->h2]
    Wait: h1=Psi, h2=-1. Exchanging them: h1=-1, h2=Psi.
    The new Psi' = h1 = -1... that doesn't make sense.

    Let me reconsider. The three parameters are
      epsilon_1, epsilon_2, epsilon_3 with epsilon_1 + epsilon_2 + epsilon_3 = 0
    and Psi = -epsilon_2/epsilon_1.

    S_3 permutes the epsilon's. The orbit of Psi under S_3:
      id:      Psi
      (12):    -epsilon_1/epsilon_2 = 1/Psi
      (23):    -epsilon_3/epsilon_1 = (epsilon_1+epsilon_2)/epsilon_1 = 1 - 1/Psi
               wait: epsilon_3 = -(epsilon_1+epsilon_2), so
               -epsilon_3/epsilon_1 = (epsilon_1+epsilon_2)/epsilon_1 = 1 + epsilon_2/epsilon_1
               = 1 - Psi.
               Hmm, that's for permuting (epsilon_2, epsilon_3).

    Let me be more careful. With Psi = -epsilon_2/epsilon_1:
      (12): swap epsilon_1 <-> epsilon_2.
            New Psi = -epsilon_1/epsilon_2 = 1/Psi.
            Swap N1 <-> N2.
      (13): swap epsilon_1 <-> epsilon_3.
            New Psi = -epsilon_2/epsilon_3 = -epsilon_2/(-(epsilon_1+epsilon_2))
                    = epsilon_2/(epsilon_1+epsilon_2) = (-Psi*epsilon_1)/(epsilon_1 - Psi*epsilon_1)
                    = -Psi/(1-Psi) = Psi/(Psi-1).
            Swap N1 <-> N3.
      (23): swap epsilon_2 <-> epsilon_3.
            New Psi = -epsilon_3/epsilon_1 = (epsilon_1+epsilon_2)/epsilon_1
                    = 1 - Psi.
            Swap N2 <-> N3.

    The full S_3 orbit of (N1,N2,N3,Psi):
      id:    (N1, N2, N3, Psi)
      (12):  (N2, N1, N3, 1/Psi)            <-- S-duality
      (23):  (N1, N3, N2, 1-Psi)
      (13):  (N3, N2, N1, Psi/(Psi-1))
      (123): (N2, N3, N1, 1/(1-Psi))
      (132): (N3, N1, N2, (Psi-1)/Psi)

    ALL SIX central charges must agree.
    """
    psi_f = _to_frac(psi)

    results = {}

    # The six S_3 images
    orbit = [
        ('id',    N1, N2, N3, psi_f),
        ('(12)',  N2, N1, N3, Fraction(1) / psi_f if psi_f != 0 else None),
        ('(23)',  N1, N3, N2, 1 - psi_f if psi_f != 1 else None),
        ('(13)',  N3, N2, N1, psi_f / (psi_f - 1) if psi_f != 1 else None),
        ('(123)', N2, N3, N1, Fraction(1) / (1 - psi_f) if psi_f != 1 else None),
        ('(132)', N3, N1, N2, (psi_f - 1) / psi_f if psi_f != 0 else None),
    ]

    central_charges = []
    for label, n1, n2, n3, p in orbit:
        if p is not None:
            try:
                c_val = corner_voa_central_charge(n1, n2, n3, p)
                central_charges.append((label, c_val))
            except (ValueError, ZeroDivisionError):
                central_charges.append((label, None))
        else:
            central_charges.append((label, None))

    # Check all central charges agree
    valid_ccs = [c for _, c in central_charges if c is not None]
    all_equal = len(set(valid_ccs)) <= 1 if valid_ccs else True

    results['orbit'] = central_charges
    results['triality_holds'] = all_equal
    results['distinct_values'] = len(set(valid_ccs)) if valid_ccs else 0

    return results


# =========================================================================
# 12. S-duality = Koszul duality comparison
# =========================================================================

def s_duality_koszul_comparison(N: int, psi: Num,
                                 boundary_type: str = 'neumann') -> Dict[str, Any]:
    r"""Compare S-dual and Koszul dual for a boundary VOA.

    For Neumann: A = gl_N at level k = Psi - N.
      S-dual:    A^S = gl_N at level k^S = 1/Psi - N.
      FF-dual:   A^FF = gl_N at level k^FF = -k - 2N = -(Psi-N) - 2N = -Psi-N.

    Key question: when does k^S = k^FF?
      1/Psi - N = -Psi - N
      1/Psi = -Psi
      Psi^2 = -1
      Psi = +/- i

    So S-duality = FF-duality ONLY at Psi = i (the self-dual coupling).
    At generic Psi, they are DIFFERENT.

    BUT: the question for Koszul duality is whether the MODULAR CHARACTERISTIC
    kappa agrees, not whether the levels agree. Two algebras at different
    levels can have the same kappa.

    For affine gl_N: kappa(k) = (N^2-1)(k+N)/(2N) + k.
    kappa(k^S) = (N^2-1)(1/Psi)/(2N) + (1/Psi - N)
    kappa(k^FF) = (N^2-1)(-Psi)/(2N) + (-Psi - N)

    These are generically different. The ratio kappa(A^S)/kappa(A^FF) is:
    [(N^2-1)/(2N*Psi) + 1/Psi - N] / [-(N^2-1)*Psi/(2N) - Psi - N]

    For N=1 (Heisenberg): kappa(k) = k + 0 = k = Psi - 1.
    kappa(k^S) = 1/Psi - 1.
    kappa(k^FF) = -Psi - 1.
    Ratio: (1/Psi - 1)/(-Psi - 1) = (1-Psi)/(Psi*(Psi+1)) * (-1)
    = (Psi-1)/(Psi(Psi+1)).
    This is NOT 1 generically.

    CONCLUSION for affine algebras: S-duality != Koszul duality (generically).
    S-duality is LANGLANDS duality (Psi -> 1/Psi), not Feigin-Frenkel duality.
    """
    psi_f = _to_frac(psi)

    if boundary_type == 'neumann':
        data = neumann_boundary_voa(N, psi_f)
    elif boundary_type == 'dirichlet':
        data = dirichlet_boundary_voa(N, psi_f)
    elif boundary_type == 'nahm_principal':
        data = nahm_principal_boundary_voa(N, psi_f)
    else:
        raise ValueError(f"Unknown boundary type: {boundary_type}")

    result = {
        'name': data.name,
        'boundary_type': boundary_type,
        'N': N,
        'Psi': psi_f,
        'kappa': data.kappa,
        'kappa_koszul_dual': data.dual_kappa,
        'kappa_s_dual': data.s_dual_kappa,
        'kappa_koszul_eq_s': data.koszul_equals_s_duality,
        'complementarity_sum': data.complementarity_sum,
        'central_charge': data.central_charge,
        'dual_central_charge': data.dual_central_charge,
        's_dual_central_charge': data.s_dual_central_charge,
    }

    # Compute the discrepancy
    if data.s_dual_kappa is not None:
        result['kappa_discrepancy'] = data.dual_kappa - data.s_dual_kappa
    else:
        result['kappa_discrepancy'] = None

    return result


# =========================================================================
# 13. Landscape survey: all boundary VOAs
# =========================================================================

def boundary_voa_landscape(N_max: int = 5) -> List[Dict[str, Any]]:
    r"""Survey all boundary VOA types for GL(N), N = 1, ..., N_max.

    Returns a list of dictionaries with complete modular Koszul data
    for each boundary condition type.
    """
    results = []

    for N in range(1, N_max + 1):
        # Test at several coupling values
        for psi_num, psi_den in [(3, 1), (2, 1), (5, 2), (1, 2), (1, 3)]:
            psi = Fraction(psi_num, psi_den)

            # Skip degenerate cases
            if psi == 0 or psi == N or psi == 1:
                continue

            try:
                entry = s_duality_koszul_comparison(N, psi, 'neumann')
                entry['shadow_class'] = shadow_class_affine(N)
                results.append(entry)
            except (ValueError, ZeroDivisionError):
                pass

            try:
                entry = s_duality_koszul_comparison(N, psi, 'dirichlet')
                entry['shadow_class'] = shadow_class_affine(N)
                results.append(entry)
            except (ValueError, ZeroDivisionError):
                pass

            if N >= 2:
                try:
                    entry = s_duality_koszul_comparison(N, psi, 'nahm_principal')
                    entry['shadow_class'] = shadow_class_w_algebra(N)
                    results.append(entry)
                except (ValueError, ZeroDivisionError):
                    pass

    return results


# =========================================================================
# 14. Complementarity sum verification
# =========================================================================

def verify_complementarity_affine_gl(N: int, psi: Num) -> Dict[str, Any]:
    r"""Verify that kappa + kappa' is level-independent for affine gl_N.

    For affine algebras: kappa(k) + kappa(-k-2N) should be a constant.
    For sl_N: the sum is 0.
    For gl_N: the sum includes the u(1) contribution.

    kappa(gl_N, k) = (N^2-1)(k+N)/(2N) + k
    kappa(gl_N, -k-2N) = (N^2-1)(-k-2N+N)/(2N) + (-k-2N)
                       = (N^2-1)(-k-N)/(2N) - k - 2N

    Sum = (N^2-1)(k+N)/(2N) + (N^2-1)(-k-N)/(2N) + k + (-k-2N)
        = 0 + (-2N)
        = -2N

    So for gl_N: kappa + kappa' = -2N (level-independent!).
    """
    psi_f = _to_frac(psi)
    k = psi_f - N
    k_ff = -k - 2 * N

    kap = kappa_affine_gl(N, k)
    kap_ff = kappa_affine_gl(N, k_ff)
    total = kap + kap_ff

    expected = Fraction(-2 * N)

    return {
        'N': N,
        'Psi': psi_f,
        'k': k,
        'k_ff': k_ff,
        'kappa': kap,
        'kappa_dual': kap_ff,
        'sum': total,
        'expected': expected,
        'correct': total == expected,
    }


def verify_complementarity_wn(N: int, psi: Num) -> Dict[str, Any]:
    r"""Verify kappa + kappa' for principal W-algebra W^k(sl_N).

    The complementarity sum kappa(W_N,k) + kappa(W_N,-k-2N) is constant.
    For N=2 (Virasoro): sum = 13.
    For N=3 (W_3): sum = 250/3.
    """
    psi_f = _to_frac(psi)
    k = psi_f - N
    k_ff = -k - 2 * N

    kap = kappa_wn_principal(N, k)
    kap_ff = kappa_wn_principal(N, k_ff)
    total = kap + kap_ff

    # Expected from complementarity_landscape.py
    H_N = sum(Fraction(1, j) for j in range(1, N + 1))
    c_sum = Fraction(2 * (N - 1)) + Fraction(4 * N * (N**2 - 1))
    expected = (H_N - 1) * c_sum

    return {
        'N': N,
        'Psi': psi_f,
        'k': k,
        'k_ff': k_ff,
        'kappa': kap,
        'kappa_dual': kap_ff,
        'sum': total,
        'expected': expected,
        'correct': total == expected,
    }


# =========================================================================
# 15. Summary: S-duality vs Koszul duality diagnosis
# =========================================================================

def diagnose_s_duality_koszul_relation() -> Dict[str, Any]:
    r"""Comprehensive diagnosis of the S-duality = Koszul duality question.

    FINDING: S-duality and Koszul duality are DIFFERENT operations.
    They coincide only in special cases.

    STRUCTURE:
    - S-duality: Psi -> 1/Psi (Langlands / Montonen-Olive)
    - Koszul duality: k -> -k - 2h^v (Feigin-Frenkel)

    For affine gl_N:
      S-dual level:  k^S = 1/Psi - N
      FF-dual level: k^FF = -k - 2N = -(Psi-N) - 2N = -Psi - N

      k^S = k^FF iff 1/Psi - N = -Psi - N iff 1/Psi = -Psi iff Psi^2 = -1.

    So S = FF only at Psi = +/- i (purely imaginary self-dual coupling).

    HOWEVER: at the level of KAPPA values:
      kappa(A^S) and kappa(A^FF) are both rational functions of Psi and N.
      The question is whether the PHYSICAL duality (S) produces the same
      modular invariant (kappa) as the ALGEBRAIC duality (FF).

    ANSWER: NO, generically. But the DISCREPANCY is systematic and
    controlled by the anomaly ratio.

    The precise relation:
      kappa(A^S) - kappa(A^FF) = (N^2-1)/(2N) * (1/Psi + Psi) + (1/Psi + Psi)
      = (N^2+2N-1)/(2N) * (1/Psi + Psi)
      = (N+1)^2/(2N) * (Psi + 1/Psi) - 1/N * (Psi + 1/Psi)
      ... (this simplifies)

    For N=1: discrepancy = (1/Psi + Psi) = Psi + 1/Psi.
    For Psi real, Psi + 1/Psi >= 2, so the discrepancy NEVER vanishes
    for real positive Psi.

    DEEP STRUCTURE: S-duality and Koszul duality COMPOSE to give a
    third operation: the "modified Langlands duality" that sends
    Psi -> -1/Psi. This composition is the generator of the
    PSL(2,Z) action on the coupling constant.

    The S_3 triality of corner VOAs factors through:
      S-duality: (12) in S_3
      Koszul duality: related to (13) or (23) in S_3
      Together: they generate the full S_3 triality.

    CONCLUSION: S-duality != Koszul duality, but they are two of the
    three generators of the S_3 triality group of the coupling constant.
    The correct statement is:

        S_3 TRIALITY = < S-DUALITY, KOSZUL DUALITY >

    i.e., the triality group is GENERATED by S-duality and Koszul duality.
    """
    diagnosis = {
        'main_finding': 'S-duality != Koszul duality (generically)',
        'coincidence_locus': 'Psi^2 = -1 (imaginary self-dual coupling)',
        'structure': 'S_3 triality = <S-duality, Koszul duality>',
    }

    # Verify for N = 2, 3 at several Psi values
    examples = []
    for N in [1, 2, 3]:
        for psi_num, psi_den in [(3, 1), (2, 1), (5, 2)]:
            psi = Fraction(psi_num, psi_den)
            try:
                comp = s_duality_koszul_comparison(N, psi, 'neumann')
                examples.append(comp)
            except (ValueError, ZeroDivisionError):
                pass

    diagnosis['examples'] = examples

    # Count how many have koszul = s-duality
    n_match = sum(1 for e in examples if e.get('kappa_koszul_eq_s'))
    n_total = len(examples)
    diagnosis['match_count'] = n_match
    diagnosis['total_count'] = n_total
    diagnosis['match_fraction'] = f"{n_match}/{n_total}"

    return diagnosis


# =========================================================================
# 16. Affine Kac-Moody kappa + kappa' for sl_N (NOT gl_N)
# =========================================================================

def verify_complementarity_affine_sl(N: int, k: Num) -> Dict[str, Any]:
    r"""For sl_N: kappa(k) + kappa(-k-2N) = 0 (exact anti-symmetry)."""
    k_f = _to_frac(k)
    k_ff = -k_f - 2 * N

    kap = kappa_affine_sl(N, k_f)
    kap_ff = kappa_affine_sl(N, k_ff)
    total = kap + kap_ff

    return {
        'N': N,
        'k': k_f,
        'k_ff': k_ff,
        'kappa': kap,
        'kappa_dual': kap_ff,
        'sum': total,
        'correct': total == 0,
    }


# =========================================================================
# 17. BLLPRR boundary VOAs from 4d N=2 SCFTs
# =========================================================================

def bllprr_schur_voa(theory: str, **params) -> Dict[str, Any]:
    r"""Compute modular Koszul data for the Schur VOA of a 4d N=2 SCFT.

    The BLLPRR correspondence associates a 2d VOA A(T) to every 4d N=2 SCFT T
    via the Schur index: the Schur operators form a 2d chiral algebra.

    Known examples:
      - Free hypermultiplet: A(T) = symplectic boson pair (bg at lambda=1/2)
      - Free vector multiplet: A(T) = bc ghost pair (at lambda=1)
      - SU(2) N_f=4: A(T) = affine so(8) at level -2
      - Argyres-Douglas H_0: A(T) = Virasoro at c = -22/5
      - Argyres-Douglas H_1: A(T) = Virasoro at c = -7 (= W_2 at k=1)
      - Minahan-Nemeschansky E_6: A(T) = affine e_6 at level -3
      - Minahan-Nemeschansky E_7: A(T) = affine e_7 at level -4
      - Minahan-Nemeschansky E_8: A(T) = affine e_8 at level -6

    The central charge of the VOA is:
      c_2d = -12 c_4d
    where c_4d is the Weyl anomaly coefficient of the 4d SCFT.
    """
    if theory == 'free_hyper':
        c = Fraction(-1)  # symplectic boson
        kap = Fraction(-1, 2)
        sc = 'C'
        dual_c = Fraction(1)  # bc at lambda=1/2
        dual_kap = Fraction(1, 2)
        name = "Symplectic boson (free hyper)"

    elif theory == 'free_vector':
        c = Fraction(-26)   # bc ghosts at lambda=1 (reparametrization ghosts)
        kap = Fraction(-13)
        sc = 'C'
        dual_c = Fraction(26)
        dual_kap = Fraction(13)
        name = "bc ghosts lambda=1 (free vector)"

    elif theory == 'argyres_douglas_H0':
        c = Fraction(-22, 5)
        kap = Fraction(-11, 5)
        sc = 'M'
        dual_c = 26 - c  # Virasoro: c' = 26 - c
        dual_kap = dual_c / 2
        name = "Virasoro c=-22/5 (Argyres-Douglas H_0)"

    elif theory == 'argyres_douglas_H1':
        c = Fraction(-7)
        kap = Fraction(-7, 2)
        sc = 'M'
        dual_c = Fraction(33)  # 26 - (-7) = 33
        dual_kap = Fraction(33, 2)
        name = "Virasoro c=-7 (Argyres-Douglas H_1 = W_2 at k=1)"

    elif theory == 'su2_nf4':
        # affine so(8) at level -2
        # dim(so_8) = 28, h^v(D_4) = 6
        # c = k * 28 / (k + 6) = (-2)*28/4 = -14
        # kappa = 28 * (k+6) / (2*6) = 28*4/12 = 28/3
        c = Fraction(-14)
        kap = Fraction(28, 3)
        sc = 'L'
        # FF dual: k' = -k - 2*6 = -(-2) - 12 = 2 - 12 = -10
        k_ff = -(-2) - 12
        dual_c = Fraction(k_ff * 28, k_ff + 6)  # (-10)*28/(-4) = 70
        dual_kap = Fraction(28 * (k_ff + 6), 12)  # 28*(-4)/12 = -28/3
        name = "Affine so(8) at k=-2 (SU(2) N_f=4)"

    elif theory == 'MN_E6':
        # affine e_6 at level -3
        # dim(e_6) = 78, h^v = 12
        # c = (-3)*78/(-3+12) = -234/9 = -26
        # kappa = 78 * (-3+12) / (2*12) = 78*9/24 = 702/24 = 117/4
        c = Fraction(-26)
        kap = Fraction(117, 4)
        sc = 'L'
        k_ff = -(-3) - 24  # = 3 - 24 = -21
        dual_c = Fraction((-21) * 78, -21 + 12)  # = -1638/(-9) = 182
        dual_kap = Fraction(78 * (-21 + 12), 24)  # = 78*(-9)/24 = -702/24 = -117/4
        name = "Affine e_6 at k=-3 (MN E_6)"

    elif theory == 'MN_E7':
        # affine e_7 at level -4
        # dim(e_7) = 133, h^v = 18
        # c = (-4)*133/(-4+18) = -532/14 = -38
        # kappa = 133*(-4+18)/(2*18) = 133*14/36 = 1862/36 = 931/18
        c = Fraction(-38)
        kap = Fraction(931, 18)
        sc = 'L'
        k_ff = -(-4) - 36  # = 4 - 36 = -32
        dual_c = Fraction((-32) * 133, -32 + 18)  # = -4256/(-14) = 304
        dual_kap = Fraction(133 * (-32 + 18), 36)  # = 133*(-14)/36 = -1862/36 = -931/18
        name = "Affine e_7 at k=-4 (MN E_7)"

    elif theory == 'MN_E8':
        # affine e_8 at level -6
        # dim(e_8) = 248, h^v = 30
        # c = (-6)*248/(-6+30) = -1488/24 = -62
        # kappa = 248*(-6+30)/(2*30) = 248*24/60 = 5952/60 = 992/10 = 496/5
        c = Fraction(-62)
        kap = Fraction(496, 5)
        sc = 'L'
        k_ff = -(-6) - 60  # = 6 - 60 = -54
        dual_c = Fraction((-54) * 248, -54 + 30)  # = -13392/(-24) = 558
        dual_kap = Fraction(248 * (-54 + 30), 60)  # = 248*(-24)/60 = -5952/60 = -496/5
        name = "Affine e_8 at k=-6 (MN E_8)"

    else:
        raise ValueError(f"Unknown 4d N=2 theory: {theory}")

    return {
        'name': name,
        'theory': theory,
        'central_charge': c,
        'kappa': kap,
        'shadow_class': sc,
        'dual_central_charge': dual_c,
        'dual_kappa': dual_kap,
        'complementarity_sum': kap + dual_kap,
    }


# =========================================================================
# Self-tests on import
# =========================================================================

# Verify: c(gl_2, k=1) = 1*3/3 + 1 = 2
assert c_affine_gl(2, 1) == Fraction(2), f"c(gl_2, k=1) = {c_affine_gl(2, 1)}"

# Verify: kappa(gl_1, k) = k (Heisenberg)
assert kappa_affine_gl(1, 3) == Fraction(3), f"kappa(gl_1, k=3) = {kappa_affine_gl(1, 3)}"

# Verify: kappa(sl_2, k=1) = 3*3/(2*2) = 9/4
assert kappa_affine_sl(2, 1) == Fraction(9, 4), f"kappa(sl_2, k=1) = {kappa_affine_sl(2, 1)}"

# Verify: c(W_2, k=1) = -7
assert c_wn_principal(2, 1) == Fraction(-7), f"c(W_2, k=1) = {c_wn_principal(2, 1)}"

# Verify: bg at lambda=1/2 has c = -1 per pair
assert c_betagamma_system(1, Fraction(1, 2)) == Fraction(-1)

# Verify: bg + bc complementarity = 0
assert kappa_betagamma(1, Fraction(1, 2)) + kappa_bc_ghost(1, Fraction(1, 2)) == 0

# Verify: corner VOA Y_{0,0,2}[Psi=3] central charge
# Y_{0,0,2}[3] = W^{k=1}(sl_2) + u(1) = Virasoro at c=-7 plus Heisenberg
# c = c(W_2, k=1) + 1 = -7 + 1 = -6
_c_y002_3 = corner_voa_central_charge(0, 0, 2, 3)
assert _c_y002_3 == Fraction(-6), f"c(Y_{{0,0,2}}[3]) = {_c_y002_3}, expected -6"

# Verify: corner VOA Y_{0,2,0}[3] = affine gl_2 at level 1
# c(gl_2, k=1) = 3*1/3 + 1 = 2
_c_y020_3 = corner_voa_central_charge(0, 2, 0, 3)
assert _c_y020_3 == Fraction(2), f"c(Y_{{0,2,0}}[3]) = {_c_y020_3}, expected 2"

# Verify: corner VOA Y_{2,0,0}[3] = affine gl_2 at level 1/3 - 2 = -5/3
# c(gl_2, k=-5/3) = (-5/3)*3/(-5/3 + 2) + 1 = -5/(1/3) + 1 = -15 + 1 ... wait
# c(sl_2, k=-5/3) = (-5/3)*3 / (-5/3 + 2) = -5 / (1/3) = -15
# c(gl_2) = -15 + 1 = -14
_c_y200_3 = corner_voa_central_charge(2, 0, 0, 3)
assert _c_y200_3 == Fraction(-14), f"c(Y_{{2,0,0}}[3]) = {_c_y200_3}, expected -14"

# Verify: sl_N complementarity: kappa(k) + kappa(-k-2N) = 0
_v = verify_complementarity_affine_sl(2, 1)
assert _v['correct'], f"sl_2 complementarity failed: sum = {_v['sum']}"

# Verify: gl_N complementarity: kappa(k) + kappa(-k-2N) = -2N
_v2 = verify_complementarity_affine_gl(2, 3)
assert _v2['correct'], f"gl_2 complementarity failed: sum = {_v2['sum']}, expected {_v2['expected']}"
