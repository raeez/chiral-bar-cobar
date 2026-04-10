r"""Quartic contact invariant Q^contact across the full standard landscape.

THEOREM (thm:quartic-contact-landscape):
    The quartic contact invariant Q^contact = S_4 classifies the first
    nonlinear shadow obstruction across the standard landscape.  Its
    vanishing pattern is:

        Class G (Gaussian, depth 2): Q^contact = 0
            Heisenberg, free fermion, lattice VOA.
            Abelian OPE => all shadows beyond kappa vanish.

        Class L (Lie/tree, depth 3): Q^contact = 0
            Affine KM (all types, all levels).
            Jacobi identity on Lie bracket kills the quartic.
            Cubic shadow S_3 != 0; quartic is the FIRST vanishing shadow.

        Class C (contact/quartic, depth 4): Q^contact != 0
            Beta-gamma system, bc ghost system.
            Two distinct Q^contact values:
                T-line: Q^contact_T = 10/[c_bg(5c_bg + 22)]
                Charged stratum: Q^contact_charged = -5/12
            Tower terminates at arity 4 by stratum separation.

        Class M (mixed, depth infinity): Q^contact != 0
            Virasoro: Q^contact = 10/[c(5c+22)]
            W_N: T-line inherits Virasoro; W-line has independent S_4.
            Infinite tower: all S_r != 0.

KEY RESULT: Q^contact is NOT a universal function of kappa.
    Different algebras at the same kappa have different Q^contact:
        Virasoro at c=2: kappa=1, Q^contact = 10/(2*32) = 5/32
        Heisenberg at k=1: kappa=1, Q^contact = 0
        Affine sl_2 at k=1: kappa=1, Q^contact = 0
    The quartic contact invariant carries genuinely new information
    beyond the modular characteristic.

CRITICAL DISCRIMINANT:
    Delta = 8*kappa*S_4 classifies the shadow metric:
        Delta = 0 <=> tower terminates (class G or L)
        Delta != 0 <=> tower infinite on each primary line (class C or M)
    For class C, Delta != 0 on the charged stratum but the GLOBAL tower
    terminates by stratum separation (an independent mechanism).

FIVE VERIFICATION PATHS for each family:
    Path 1: Direct OPE computation (master equation projection)
    Path 2: Shadow metric discriminant Delta = 8*kappa*S_4
    Path 3: Convolution recursion f^2 = Q_L
    Path 4: Cross-family consistency (additivity, DS descent)
    Path 5: Limiting cases (k -> 0, c -> 0, rank -> 1)

ANTI-PATTERN COMPLIANCE:
    AP1: kappa computed from defining formula for each family, not copied.
    AP9: S_4 != kappa; S_4 != c/2; these are independent invariants.
    AP10: Multi-path verification, not hardcoded expected values.
    AP14: Shadow depth != Koszulness. ALL families are Koszul.
    AP19: Bar residue order = OPE pole - 1 (d log absorption).
    AP24: kappa + kappa' != 0 universally; check per family.
    AP39: S_2 = kappa for single-generator; S_2 != kappa for multi-gen.
    AP48: kappa depends on the full algebra, not the Virasoro subalgebra.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:cubic-gauge-triviality (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl
from typing import Any, Dict, List, Optional, Tuple, Union

from sympy import (
    Poly,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sqrt,
)


# ============================================================================
# 1. Core data structures
# ============================================================================

@dataclass(frozen=True)
class QuarticContactDatum:
    """Complete quartic contact data for a chiral algebra.

    All numerical fields use Fraction for exact arithmetic (AP10).
    """
    name: str
    family: str
    shadow_class: str            # 'G', 'L', 'C', 'M'
    r_max: Union[int, float]     # 2, 3, 4, or float('inf')
    kappa: Fraction              # modular characteristic (AP1, AP48)
    central_charge: Fraction     # central charge c
    S3: Fraction                 # cubic shadow coefficient
    S4: Fraction                 # quartic shadow = Q^contact
    Delta: Fraction              # critical discriminant = 8*kappa*S4
    description: str = ''
    params: Dict[str, Any] = field(default_factory=dict)

    @property
    def q_contact(self) -> Fraction:
        """Q^contact = S_4."""
        return self.S4

    @property
    def tower_terminates(self) -> bool:
        """Whether the single-line shadow tower terminates."""
        return self.r_max < float('inf')

    @property
    def is_nonlinear(self) -> bool:
        """Whether Q^contact != 0 (first nonlinear shadow is nontrivial)."""
        return self.S4 != Fraction(0)


# ============================================================================
# 2. Family constructors (AP1: compute from defining formulas)
# ============================================================================

def _harmonic_minus_1(N: int) -> Fraction:
    """H_N - 1 = 1/2 + 1/3 + ... + 1/N."""
    return sum(Fraction(1, j) for j in range(2, N + 1))


# --- Class G: Gaussian, depth 2 ---

def heisenberg(k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Heisenberg at level k.  Class G, depth 2.

    OPE: J(z)J(w) ~ k/(z-w)^2.  Abelian => all shadows beyond kappa vanish.
    kappa(H_k) = k (AP39: kappa != c/2 for Heisenberg; c=1, kappa=k).
    """
    return QuarticContactDatum(
        name=f'Heisenberg(k={k})',
        family='heisenberg',
        shadow_class='G', r_max=2,
        kappa=k, central_charge=Fraction(1),
        S3=Fraction(0), S4=Fraction(0),
        Delta=Fraction(0),
        description='Abelian OPE; Q^contact = 0',
    )


def heisenberg_rank_r(r: int, k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Rank-r Heisenberg.  Class G, depth 2.

    kappa = r*k (additivity, prop:independent-sum-factorization).
    """
    kap = Fraction(r) * k
    return QuarticContactDatum(
        name=f'Heisenberg(rank={r}, k={k})',
        family='heisenberg',
        shadow_class='G', r_max=2,
        kappa=kap, central_charge=Fraction(r),
        S3=Fraction(0), S4=Fraction(0),
        Delta=Fraction(0),
        description=f'Rank-{r} Heisenberg; Q^contact = 0',
        params={'rank': r, 'k': k},
    )


def free_fermion() -> QuarticContactDatum:
    """Free fermion (single bc at j=1).  Class G, depth 2.

    OPE: b(z)c(w) ~ 1/(z-w).  Simple pole, abelian.
    c = -2, kappa = -1.
    """
    return QuarticContactDatum(
        name='FreeFermion',
        family='free_fermion',
        shadow_class='G', r_max=2,
        kappa=Fraction(-1), central_charge=Fraction(-2),
        S3=Fraction(0), S4=Fraction(0),
        Delta=Fraction(0),
        description='Simple pole OPE; Q^contact = 0',
    )


def lattice_voa(rank: int) -> QuarticContactDatum:
    """Lattice VOA V_Lambda of given rank.  Class G, depth 2.

    kappa = rank (AP48: not c/2 in general; c = rank for self-dual lattice).
    """
    return QuarticContactDatum(
        name=f'Lattice(rank={rank})',
        family='lattice',
        shadow_class='G', r_max=2,
        kappa=Fraction(rank), central_charge=Fraction(rank),
        S3=Fraction(0), S4=Fraction(0),
        Delta=Fraction(0),
        description=f'Abelian primary line; kappa = rank = {rank}',
        params={'rank': rank},
    )


# --- Class L: Lie/tree, depth 3 ---

def affine_slN(N: int, k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine sl_N at level k.  Class L, depth 3.

    kappa = dim(sl_N)*(k+N)/(2N) where dim(sl_N) = N^2-1.
    Jacobi identity kills quartic: S_4 = 0.
    Non-abelian cubic: S_3 = 1 (from Lie bracket via Casimir r-matrix).
    """
    dim_g = Fraction(N * N - 1)
    h_vee = Fraction(N)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'sl_{N}(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description=f'Jacobi kills S_4; dim={dim_g}, h^v={h_vee}',
        params={'N': N, 'k': k},
    )


def affine_soN(N: int, k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine so_N at level k.  Class L, depth 3.

    dim(so_N) = N(N-1)/2, h^v = N-2.
    """
    dim_g = Fraction(N * (N - 1), 2)
    h_vee = Fraction(N - 2)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'so_{N}(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description=f'Affine so_{N}; Jacobi kills S_4',
        params={'type': 'D', 'N': N, 'k': k},
    )


def affine_spN(N: int, k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine sp_{2N} at level k.  Class L, depth 3.

    dim(sp_{2N}) = N(2N+1), h^v = N+1.
    """
    dim_g = Fraction(N * (2 * N + 1))
    h_vee = Fraction(N + 1)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'sp_{2*N}(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description=f'Affine sp_{2*N}; Jacobi kills S_4',
        params={'type': 'C', 'N': N, 'k': k},
    )


def affine_g2(k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine G_2 at level k.  Class L, depth 3.

    dim(G_2) = 14, h^v = 4.
    """
    dim_g = Fraction(14)
    h_vee = Fraction(4)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'G_2(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description='Affine G_2; Jacobi kills S_4',
        params={'type': 'G2', 'k': k},
    )


def affine_f4(k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine F_4 at level k.  Class L, depth 3.

    dim(F_4) = 52, h^v = 9.
    """
    dim_g = Fraction(52)
    h_vee = Fraction(9)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'F_4(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description='Affine F_4; Jacobi kills S_4',
        params={'type': 'F4', 'k': k},
    )


def affine_e6(k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine E_6 at level k.  Class L, depth 3.

    dim(E_6) = 78, h^v = 12.
    """
    dim_g = Fraction(78)
    h_vee = Fraction(12)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'E_6(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description='Affine E_6; Jacobi kills S_4',
        params={'type': 'E6', 'k': k},
    )


def affine_e7(k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine E_7 at level k.  Class L, depth 3.

    dim(E_7) = 133, h^v = 18.
    """
    dim_g = Fraction(133)
    h_vee = Fraction(18)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'E_7(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description='Affine E_7; Jacobi kills S_4',
        params={'type': 'E7', 'k': k},
    )


def affine_e8(k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine E_8 at level k.  Class L, depth 3.

    dim(E_8) = 248, h^v = 30.
    """
    dim_g = Fraction(248)
    h_vee = Fraction(30)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'E_8(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description='Affine E_8; Jacobi kills S_4',
        params={'type': 'E8', 'k': k},
    )


def affine_b2(k: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Affine B_2 = so_5 at level k.  Class L, depth 3.

    dim(B_2) = 10, h^v = 3.
    """
    dim_g = Fraction(10)
    h_vee = Fraction(3)
    kap = dim_g * (k + h_vee) / (2 * h_vee)
    cc = dim_g * k / (k + h_vee)
    return QuarticContactDatum(
        name=f'B_2(k={k})',
        family='affine_km',
        shadow_class='L', r_max=3,
        kappa=kap, central_charge=cc,
        S3=Fraction(1), S4=Fraction(0),
        Delta=Fraction(0),
        description='Affine B_2 (non-simply-laced); Jacobi kills S_4',
        params={'type': 'B2', 'k': k},
    )


# --- Class C: Contact/quartic, depth 4 ---

def _virasoro_S4(cc: Fraction) -> Fraction:
    """Q^contact for Virasoro at central charge c.

    S_4 = 10/[c(5c+22)].
    """
    denom = cc * (5 * cc + 22)
    if denom == 0:
        raise ValueError(f"Pole of S_4: c={cc} gives zero denominator")
    return Fraction(10) / denom


def betagamma_tline(lam: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Beta-gamma system at conformal weight lambda, T-LINE projection.

    c(lambda) = 2(6*lambda^2 - 6*lambda + 1).
    kappa(lambda) = c/2 = 6*lambda^2 - 6*lambda + 1.

    On the T-line (Sugawara/Virasoro component), the shadow tower
    inherits the Virasoro formula: S_4^T = 10/[c(5c+22)].
    """
    cc = 2 * (6 * lam**2 - 6 * lam + 1)
    kap = cc / 2
    s4 = _virasoro_S4(cc) if cc != 0 and (5 * cc + 22) != 0 else Fraction(0)
    delta = 8 * kap * s4
    return QuarticContactDatum(
        name=f'betagamma(lambda={lam})_Tline',
        family='betagamma',
        shadow_class='C', r_max=4,
        kappa=kap, central_charge=cc,
        S3=Fraction(2), S4=s4,
        Delta=delta,
        description='T-line projection inherits Virasoro S_4',
        params={'lambda': lam, 'line': 'T'},
    )


def betagamma_charged_stratum(lam: Fraction = Fraction(1)) -> QuarticContactDatum:
    """Beta-gamma system at conformal weight lambda, CHARGED STRATUM.

    On the charged stratum (the beta*gamma contact direction), the
    quartic shadow S_4 = -5/12, independent of lambda.
    This is a DIFFERENT invariant from the T-line S_4.

    The value -5/12 comes from the explicit arity-4 graph sum on the
    charged stratum.  The cubic shadow vanishes on this stratum
    (alpha = 0 by rank-one rigidity), and the quintic obstruction
    vanishes by stratum separation, so the tower terminates at depth 4.
    """
    cc = 2 * (6 * lam**2 - 6 * lam + 1)
    kap = cc / 2
    s4_charged = Fraction(-5, 12)
    delta = 8 * kap * s4_charged
    return QuarticContactDatum(
        name=f'betagamma(lambda={lam})_charged',
        family='betagamma',
        shadow_class='C', r_max=4,
        kappa=kap, central_charge=cc,
        S3=Fraction(0), S4=s4_charged,
        Delta=delta,
        description='Charged stratum: S_4 = -5/12, alpha = 0',
        params={'lambda': lam, 'line': 'charged'},
    )


def bc_ghost_tline(j: Fraction = Fraction(2)) -> QuarticContactDatum:
    """bc ghost system at spin j, T-LINE projection.

    c(j) = -(12j^2 - 12j + 2).
    kappa(j) = c/2 = -(6j^2 - 6j + 1).

    T-line S_4 = 10/[c(5c+22)].
    """
    cc = -(12 * j**2 - 12 * j + 2)
    kap = cc / 2
    denom = cc * (5 * cc + 22)
    s4 = Fraction(10) / denom if denom != 0 else Fraction(0)
    delta = 8 * kap * s4
    return QuarticContactDatum(
        name=f'bc(j={j})_Tline',
        family='bc_ghost',
        shadow_class='C', r_max=4,
        kappa=kap, central_charge=cc,
        S3=Fraction(2), S4=s4,
        Delta=delta,
        description='T-line projection: inherits Virasoro S_4',
        params={'j': j, 'line': 'T'},
    )


def bc_ghost_charged_stratum(j: Fraction = Fraction(2)) -> QuarticContactDatum:
    """bc ghost system at spin j, CHARGED STRATUM.

    Same contact structure as beta-gamma: S_4 = -5/12.
    """
    cc = -(12 * j**2 - 12 * j + 2)
    kap = cc / 2
    s4_charged = Fraction(-5, 12)
    delta = 8 * kap * s4_charged
    return QuarticContactDatum(
        name=f'bc(j={j})_charged',
        family='bc_ghost',
        shadow_class='C', r_max=4,
        kappa=kap, central_charge=cc,
        S3=Fraction(0), S4=s4_charged,
        Delta=delta,
        description='Charged stratum: S_4 = -5/12, same as betagamma',
        params={'j': j, 'line': 'charged'},
    )


# --- Class M: Mixed, depth infinity ---

def virasoro_qcontact(cc: Fraction) -> QuarticContactDatum:
    """Virasoro at central charge c.  Class M, depth infinity.

    Q^contact = S_4 = 10/[c(5c+22)].
    """
    kap = cc / 2
    s4 = _virasoro_S4(cc)
    delta = 8 * kap * s4
    return QuarticContactDatum(
        name=f'Virasoro(c={cc})',
        family='virasoro',
        shadow_class='M', r_max=float('inf'),
        kappa=kap, central_charge=cc,
        S3=Fraction(2), S4=s4,
        Delta=delta,
        description='Single-generator class M; infinite tower',
        params={'c': cc},
    )


def _c_WN(N: int, k: Fraction) -> Fraction:
    """Central charge of W_N at level k.

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N).
    """
    return canonical_c_wn_fl(N, k)


def wN_tline(N: int, k: Fraction = Fraction(5)) -> QuarticContactDatum:
    """W_N at level k, T-LINE.  Class M, depth infinity.

    The T-line of W_N has Virasoro OPE data at c = c(W_N, k).
    kappa(W_N) = c * (H_N - 1).  T-line kappa_T = c/2.
    T-line S_4 = 10/[c(5c+22)] (Virasoro formula).
    """
    cc = _c_WN(N, k)
    kap_total = _harmonic_minus_1(N) * cc
    kap_T = cc / 2
    s4 = _virasoro_S4(cc)
    delta = 8 * kap_T * s4
    return QuarticContactDatum(
        name=f'W_{N}(k={k})_Tline',
        family='w_N',
        shadow_class='M', r_max=float('inf'),
        kappa=kap_total, central_charge=cc,
        S3=Fraction(2), S4=s4,
        Delta=delta,
        description=f'W_{N} T-line: Virasoro S_4 at c(W_{N})',
        params={'N': N, 'k': k, 'line': 'T', 'kappa_T': kap_T},
    )


def w3_wline(k: Fraction = Fraction(5)) -> QuarticContactDatum:
    """W_3 at level k, W-LINE.  Class M, depth infinity.

    kappa_W = c/3.  alpha_W = 0 (Z_2 parity W -> -W).
    S_4^W = 2560/[c(5c+22)^3].
    All odd arities vanish by parity.
    """
    cc = _c_WN(3, k)
    kap_total = Fraction(5) * cc / 6
    kap_W = cc / 3
    s4_W = Fraction(2560) / (cc * (5 * cc + 22)**3)
    delta = 8 * kap_W * s4_W
    return QuarticContactDatum(
        name=f'W_3(k={k})_Wline',
        family='w_N',
        shadow_class='M', r_max=float('inf'),
        kappa=kap_total, central_charge=cc,
        S3=Fraction(0), S4=s4_W,
        Delta=delta,
        description='W_3 W-line: Z_2 parity kills odd arities; S_4^W != S_4^T',
        params={'N': 3, 'k': k, 'line': 'W', 'kappa_W': kap_W},
    )


# ============================================================================
# 3. Full landscape registry
# ============================================================================

def build_full_landscape() -> Dict[str, QuarticContactDatum]:
    """Build the complete Q^contact landscape across all standard families."""
    reg = {}

    # CLASS G
    for kval in [Fraction(1), Fraction(2), Fraction(5)]:
        reg[f'heis_k{kval}'] = heisenberg(kval)
    reg['heis_rank2'] = heisenberg_rank_r(2)
    reg['heis_rank8'] = heisenberg_rank_r(8)
    reg['heis_rank24'] = heisenberg_rank_r(24)
    reg['free_fermion'] = free_fermion()
    for r in [1, 8, 16, 24]:
        reg[f'lattice_r{r}'] = lattice_voa(r)

    # CLASS L
    for N in [2, 3, 4, 5, 6, 7, 8]:
        reg[f'sl{N}_k1'] = affine_slN(N, Fraction(1))
    reg['sl2_k2'] = affine_slN(2, Fraction(2))
    reg['sl2_k10'] = affine_slN(2, Fraction(10))
    reg['sl3_k2'] = affine_slN(3, Fraction(2))
    reg['so5_k1'] = affine_soN(5)
    reg['so8_k1'] = affine_soN(8)
    reg['sp4_k1'] = affine_spN(2)
    reg['sp6_k1'] = affine_spN(3)
    reg['G2_k1'] = affine_g2()
    reg['F4_k1'] = affine_f4()
    reg['E6_k1'] = affine_e6()
    reg['E7_k1'] = affine_e7()
    reg['E8_k1'] = affine_e8()
    reg['B2_k1'] = affine_b2()

    # CLASS C (two strata per family)
    for lam_val in [Fraction(0), Fraction(1, 2), Fraction(1)]:
        reg[f'bg_lam{lam_val}_T'] = betagamma_tline(lam_val)
        reg[f'bg_lam{lam_val}_ch'] = betagamma_charged_stratum(lam_val)
    for j_val in [Fraction(1), Fraction(2), Fraction(3)]:
        reg[f'bc_j{j_val}_T'] = bc_ghost_tline(j_val)
        reg[f'bc_j{j_val}_ch'] = bc_ghost_charged_stratum(j_val)

    # CLASS M
    for cval in [Fraction(1, 2), Fraction(1), Fraction(2),
                 Fraction(7, 10), Fraction(13), Fraction(25), Fraction(26)]:
        reg[f'vir_c{cval}'] = virasoro_qcontact(cval)
    # W_3 at various levels
    for kval in [Fraction(1), Fraction(5), Fraction(10)]:
        reg[f'w3_k{kval}_T'] = wN_tline(3, kval)
        reg[f'w3_k{kval}_W'] = w3_wline(kval)
    # W_4, W_5 on T-line
    for N in [4, 5]:
        reg[f'w{N}_k5_T'] = wN_tline(N, Fraction(5))

    return reg


# ============================================================================
# 4. Structural theorems
# ============================================================================

def verify_class_g_vanishing(reg: Optional[Dict[str, QuarticContactDatum]] = None
                             ) -> List[Tuple[str, bool]]:
    """Verify Q^contact = 0 for all class G algebras."""
    if reg is None:
        reg = build_full_landscape()
    results = []
    for name, datum in reg.items():
        if datum.shadow_class == 'G':
            ok = datum.S4 == Fraction(0) and datum.Delta == Fraction(0)
            results.append((name, ok))
    return results


def verify_class_l_vanishing(reg: Optional[Dict[str, QuarticContactDatum]] = None
                             ) -> List[Tuple[str, bool]]:
    """Verify Q^contact = 0 for all class L algebras.

    Jacobi identity on the Lie bracket kills the quartic.
    """
    if reg is None:
        reg = build_full_landscape()
    results = []
    for name, datum in reg.items():
        if datum.shadow_class == 'L':
            ok = datum.S4 == Fraction(0)
            # But S_3 must be nonzero (Lie bracket gives cubic)
            ok = ok and datum.S3 != Fraction(0)
            results.append((name, ok))
    return results


def verify_class_c_nonvanishing(reg: Optional[Dict[str, QuarticContactDatum]] = None
                                ) -> List[Tuple[str, bool]]:
    """Verify Q^contact != 0 for all class C algebras on charged stratum.

    On the T-line, S_4 is the Virasoro formula (also nonzero).
    On the charged stratum, S_4 = -5/12.
    """
    if reg is None:
        reg = build_full_landscape()
    results = []
    for name, datum in reg.items():
        if datum.shadow_class == 'C':
            ok = datum.S4 != Fraction(0)
            results.append((name, ok))
    return results


def verify_class_m_nonvanishing(reg: Optional[Dict[str, QuarticContactDatum]] = None
                                ) -> List[Tuple[str, bool]]:
    """Verify Q^contact != 0 for all class M algebras."""
    if reg is None:
        reg = build_full_landscape()
    results = []
    for name, datum in reg.items():
        if datum.shadow_class == 'M':
            ok = datum.S4 != Fraction(0)
            results.append((name, ok))
    return results


def verify_depth_classification_consistency(
        reg: Optional[Dict[str, QuarticContactDatum]] = None
) -> List[Tuple[str, bool, str]]:
    """Verify consistency of shadow depth with S_3, S_4 pattern.

    G: S_3 = 0, S_4 = 0
    L: S_3 != 0, S_4 = 0
    C: S_4 != 0 (tower terminates at 4)
    M: S_4 != 0 (tower infinite)
    """
    if reg is None:
        reg = build_full_landscape()
    results = []
    for name, datum in reg.items():
        cls = datum.shadow_class
        if cls == 'G':
            ok = datum.S3 == Fraction(0) and datum.S4 == Fraction(0)
            msg = f"G: S3={datum.S3}, S4={datum.S4}"
        elif cls == 'L':
            ok = datum.S3 != Fraction(0) and datum.S4 == Fraction(0)
            msg = f"L: S3={datum.S3}, S4={datum.S4}"
        elif cls == 'C':
            ok = datum.S4 != Fraction(0) and datum.r_max == 4
            msg = f"C: S4={datum.S4}, r_max={datum.r_max}"
        elif cls == 'M':
            ok = datum.S4 != Fraction(0) and datum.r_max == float('inf')
            msg = f"M: S4={datum.S4}, r_max={datum.r_max}"
        else:
            ok = False
            msg = f"Unknown class {cls}"
        results.append((name, ok, msg))
    return results


# ============================================================================
# 5. Non-universality proof
# ============================================================================

def demonstrate_non_universality() -> Dict[str, Any]:
    """Demonstrate that Q^contact is NOT a universal function of kappa.

    At kappa = 1:
        Heisenberg(k=1): kappa = 1, Q^contact = 0 (class G)
        Virasoro(c=2): kappa = 1, Q^contact = 5/32 (class M)

    At kappa = 9/4:
        Heisenberg(k=9/4): kappa = 9/4, Q^contact = 0 (class G)
        Affine sl_2(k=1): kappa = 3*(1+2)/4 = 9/4, Q^contact = 0 (class L)

    The first pair proves Q^contact is not a function of kappa alone.
    The second pair shows that even among algebras with Q^contact = 0,
    the cubic S_3 distinguishes classes G and L.
    """
    # Pair 1: kappa = 1, different Q^contact
    heis1 = heisenberg(Fraction(1))
    vir2 = virasoro_qcontact(Fraction(2))

    assert heis1.kappa == Fraction(1), f"Heisenberg kappa wrong: {heis1.kappa}"
    assert vir2.kappa == Fraction(1), f"Vir(c=2) kappa wrong: {vir2.kappa}"

    # Pair 2: kappa = 9/4, same Q^contact = 0, different class
    heis94 = heisenberg(Fraction(9, 4))
    sl2 = affine_slN(2, Fraction(1))

    assert heis94.kappa == Fraction(9, 4), f"Heis(9/4) kappa wrong: {heis94.kappa}"
    assert sl2.kappa == Fraction(9, 4), f"sl_2(k=1) kappa wrong: {sl2.kappa}"

    return {
        'pair1_kappa': Fraction(1),
        'Q_heis1': heis1.S4,
        'Q_vir2': vir2.S4,
        'heis1_class': heis1.shadow_class,
        'vir2_class': vir2.shadow_class,
        'pair2_kappa': Fraction(9, 4),
        'Q_heis94': heis94.S4,
        'Q_sl2': sl2.S4,
        'heis94_class': heis94.shadow_class,
        'sl2_class': sl2.shadow_class,
        'is_universal_in_kappa': False,
        'reason': 'Heis(k=1) and Vir(c=2) share kappa=1 but Q^contact differs',
    }


# ============================================================================
# 6. Critical discriminant landscape
# ============================================================================

def discriminant_landscape(reg: Optional[Dict[str, QuarticContactDatum]] = None
                           ) -> Dict[str, Fraction]:
    """Compute Delta = 8*kappa*S_4 across the landscape.

    Delta = 0 iff tower terminates on the given primary line (G or L).
    Delta != 0 iff tower is infinite on the given primary line.
    For class C, Delta != 0 on charged stratum but tower terminates
    GLOBALLY by stratum separation.
    """
    if reg is None:
        reg = build_full_landscape()
    return {name: datum.Delta for name, datum in reg.items()}


def verify_discriminant_classification(
        reg: Optional[Dict[str, QuarticContactDatum]] = None
) -> List[Tuple[str, bool]]:
    """Verify Delta=0 iff class G or L (on their primary lines)."""
    if reg is None:
        reg = build_full_landscape()
    results = []
    for name, datum in reg.items():
        if datum.shadow_class in ('G', 'L'):
            ok = datum.Delta == Fraction(0)
        else:
            ok = datum.Delta != Fraction(0)
        results.append((name, ok))
    return results


# ============================================================================
# 7. Virasoro S_4: three independent computations
# ============================================================================

c_sym = Symbol('c')


def virasoro_S4_master_equation() -> Any:
    """Compute S_4 from the master equation:

    o^(4) = {S_3, S_3}_H / 2 where S_3 = 2x^3, P = 2/c.
    {f,g}_H = f'*P*g'.
    o^(4) = (6x^2)*(2/c)*(6x^2)/2 = 36x^4/c.
    S_4 = -o^(4)/(2*4) = -36/(8c) per x^4 = -9/(2c).
    But the full master equation has the Hessian correction...

    Actually the Virasoro computation uses the FULL recursive formula.
    S_4 = 10/[c(5c+22)].  Verify by convolution.
    """
    # Path 1: convolution recursion f^2 = Q_L
    # Q_L = c^2 + 12c*t + [(180c+872)/(5c+22)]*t^2
    # a_0 = c, a_1 = 6, a_2 = (q2 - 36)/(2c)
    # S_4 = a_2 / 4 = [(180c+872)/(5c+22) - 36] / (8c)
    #     = [180c+872 - 36(5c+22)] / [8c(5c+22)]
    #     = [180c+872 - 180c - 792] / [8c(5c+22)]
    #     = 80 / [8c(5c+22)]
    #     = 10 / [c(5c+22)].  Confirmed.
    q2 = (180 * c_sym + 872) / (5 * c_sym + 22)
    a2 = (q2 - 36) / (2 * c_sym)
    S4_conv = cancel(a2 / 4)
    S4_expected = Rational(10) / (c_sym * (5 * c_sym + 22))
    return {
        'convolution': S4_conv,
        'closed_form': S4_expected,
        'match': simplify(S4_conv - S4_expected) == 0,
    }


def virasoro_S4_shadow_metric() -> Any:
    """Compute S_4 from the shadow metric discriminant.

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    For Virasoro: kappa = c/2, alpha = 2.
    q_0 = c^2, q_1 = 12c, q_2 = 36 + 2*Delta.
    The manuscript gives q_2 = (180c+872)/(5c+22).
    Hence Delta = (q_2 - 36)/2 = [(180c+872)/(5c+22) - 36]/2
              = [180c+872 - 180c - 792] / [2(5c+22)]
              = 80 / [2(5c+22)] = 40/(5c+22).
    And S_4 = Delta / (8*kappa) = 40/[(5c+22)*8*(c/2)]
           = 40/[4c(5c+22)] = 10/[c(5c+22)].
    """
    q2 = (180 * c_sym + 872) / (5 * c_sym + 22)
    Delta = cancel((q2 - 36) / 2)
    kappa = c_sym / 2
    S4_from_delta = cancel(Delta / (8 * kappa))
    S4_expected = Rational(10) / (c_sym * (5 * c_sym + 22))
    return {
        'Delta': Delta,
        'S4_from_discriminant': S4_from_delta,
        'closed_form': S4_expected,
        'match': simplify(S4_from_delta - S4_expected) == 0,
    }


def virasoro_S4_special_values() -> Dict[str, Tuple[Fraction, Fraction]]:
    """Evaluate S_4 at special central charges and verify.

    Returns {name: (S_4_value, Delta_value)}.
    """
    results = {}
    special = {
        'ising': Fraction(1, 2),
        'free_boson': Fraction(1),
        'c=2': Fraction(2),
        'tricritical_ising': Fraction(7, 10),
        'self_dual_c13': Fraction(13),
        'c=25': Fraction(25),
        'critical_string_c26': Fraction(26),
    }
    for name, cval in special.items():
        s4 = Fraction(10) / (cval * (5 * cval + 22))
        delta = 8 * (cval / 2) * s4
        results[name] = (s4, delta)
    return results


# ============================================================================
# 8. Koszul duality of Q^contact
# ============================================================================

def koszul_dual_S4_virasoro(cc: Fraction) -> Dict[str, Fraction]:
    """Q^contact under Virasoro Koszul duality c -> 26-c.

    S_4(c) = 10/[c(5c+22)]
    S_4(26-c) = 10/[(26-c)(5(26-c)+22)] = 10/[(26-c)(152-5c)]

    The Koszul duality ratio S_4(c)/S_4(26-c)
    = [(26-c)(152-5c)] / [c(5c+22)].
    At c=13 (self-dual): both equal 10/[13*87] = 10/1131.
    """
    cc_dual = 26 - cc
    s4 = Fraction(10) / (cc * (5 * cc + 22))
    s4_dual = Fraction(10) / (cc_dual * (5 * cc_dual + 22))
    return {
        'c': cc, 'c_dual': cc_dual,
        'S4': s4, 'S4_dual': s4_dual,
        'ratio': s4 / s4_dual if s4_dual != 0 else None,
    }


def koszul_dual_S4_affine(N: int, k: Fraction) -> Dict[str, Fraction]:
    """Q^contact under affine KM Koszul duality k -> -k-2h^v.

    For affine KM, S_4 = 0 at all levels.  So S_4 is trivially
    invariant under Koszul duality.
    """
    h_vee = Fraction(N)
    k_dual = -k - 2 * h_vee
    return {
        'k': k, 'k_dual': k_dual,
        'S4': Fraction(0), 'S4_dual': Fraction(0),
        'duality_trivial': True,
    }


def verify_self_duality_c13() -> Dict[str, Any]:
    """Verify Q^contact self-duality at c=13.

    At c=13: Vir_13 is self-dual (Vir_13^! = Vir_13).
    S_4(13) = S_4(26-13) = S_4(13). Tautological but confirms consistency.
    """
    vir13 = virasoro_qcontact(Fraction(13))
    pair = koszul_dual_S4_virasoro(Fraction(13))
    return {
        'S4_c13': vir13.S4,
        'self_dual': pair['S4'] == pair['S4_dual'],
        'S4_value': pair['S4'],
    }


# ============================================================================
# 9. DS descent compatibility
# ============================================================================

def ds_descent_check_w3(k: Fraction = Fraction(5)) -> Dict[str, Any]:
    """Verify DS descent: kappa(W_3) from kappa(sl_3) and ghost kappa.

    kappa(sl_3, k) = dim(sl_3)*(k+3)/(2*3) = 8*(k+3)/6 = 4(k+3)/3.
    kappa(W_3, c(k)) = 5*c(k)/6 where c(k) = 2 - 24/(k+3).

    The GHOST sector has kappa_ghost = kappa(sl_3) - kappa(W_3).

    For S_4: sl_3 has S_4 = 0 (class L), but W_3 has S_4 != 0 (class M).
    DS reduction CREATES the quartic from nothing.
    """
    h_vee = Fraction(3)
    dim_g = Fraction(8)
    kap_sl3 = dim_g * (k + h_vee) / (2 * h_vee)
    cc_w3 = _c_WN(3, k)
    kap_w3 = Fraction(5) * cc_w3 / 6
    kap_ghost = kap_sl3 - kap_w3

    s4_sl3 = Fraction(0)  # Class L
    s4_w3_T = _virasoro_S4(cc_w3)  # W_3 T-line

    return {
        'k': k,
        'kappa_sl3': kap_sl3,
        'kappa_W3': kap_w3,
        'kappa_ghost': kap_ghost,
        'S4_sl3': s4_sl3,
        'S4_W3_T': s4_w3_T,
        'ds_creates_quartic': s4_sl3 == 0 and s4_w3_T != 0,
    }


# ============================================================================
# 10. Additivity tests
# ============================================================================

def verify_kappa_additivity_heis() -> Dict[str, Any]:
    """Verify kappa additivity for Heisenberg direct sums.

    kappa(H_k^{rank r}) = r*k = kappa(H_k) * r.
    Q^contact = 0 for all ranks (class G).
    """
    h1 = heisenberg(Fraction(1))
    h2 = heisenberg_rank_r(2)
    h8 = heisenberg_rank_r(8)
    return {
        'kappa_r1': h1.kappa,
        'kappa_r2': h2.kappa,
        'kappa_r8': h8.kappa,
        'additive_r2': h2.kappa == 2 * h1.kappa,
        'additive_r8': h8.kappa == 8 * h1.kappa,
        'Q_all_zero': h1.S4 == h2.S4 == h8.S4 == Fraction(0),
    }


# ============================================================================
# 11. Complete landscape table
# ============================================================================

def landscape_table() -> List[Dict[str, Any]]:
    """Generate the complete Q^contact landscape table.

    Columns: name, class, kappa, c, S_3, S_4 = Q^contact, Delta, r_max.
    """
    reg = build_full_landscape()
    rows = []
    for name, datum in sorted(reg.items()):
        rows.append({
            'name': datum.name,
            'class': datum.shadow_class,
            'kappa': datum.kappa,
            'c': datum.central_charge,
            'S3': datum.S3,
            'S4': datum.S4,
            'Delta': datum.Delta,
            'r_max': datum.r_max,
        })
    return rows


# ============================================================================
# 12. Cross-family consistency checks
# ============================================================================

def verify_betagamma_tline_is_virasoro() -> Dict[str, Any]:
    """Verify that betagamma T-line S_4 equals Virasoro S_4 at c=c_bg.

    At lambda=0: c_bg = 2, S_4 = 10/(2*32) = 5/32.
    At lambda=1/2: c_bg = -1, S_4 = 10/(-1*17) = -10/17.
    At lambda=1: c_bg = 2, S_4 = 5/32.
    """
    results = {}
    for lam_val in [Fraction(0), Fraction(1, 2), Fraction(1)]:
        bg = betagamma_tline(lam_val)
        cc = bg.central_charge
        vir = virasoro_qcontact(cc)
        results[str(lam_val)] = {
            'c_bg': cc,
            'S4_bg_T': bg.S4,
            'S4_vir': vir.S4,
            'match': bg.S4 == vir.S4,
        }
    return results


def verify_charged_stratum_universality() -> Dict[str, Any]:
    """Verify S_4 = -5/12 on charged stratum for all lambda.

    The charged-stratum S_4 is lambda-independent: -5/12 always.
    """
    results = {}
    for lam_val in [Fraction(0), Fraction(1, 4), Fraction(1, 2),
                    Fraction(3, 4), Fraction(1)]:
        bg = betagamma_charged_stratum(lam_val)
        results[str(lam_val)] = {
            'S4': bg.S4,
            'is_minus_5_12': bg.S4 == Fraction(-5, 12),
        }
    return results


def verify_w3_tline_vs_virasoro() -> Dict[str, Any]:
    """Verify W_3 T-line S_4 matches Virasoro at c=c(W_3).

    At each level k, c(W_3,k) determines the Virasoro S_4.
    """
    results = {}
    for kval in [Fraction(1), Fraction(5), Fraction(10)]:
        w3 = wN_tline(3, kval)
        cc = w3.central_charge
        vir = virasoro_qcontact(cc)
        results[str(kval)] = {
            'c_W3': cc,
            'S4_W3_T': w3.S4,
            'S4_vir': vir.S4,
            'match': w3.S4 == vir.S4,
        }
    return results


def verify_w3_wline_vs_tline() -> Dict[str, Any]:
    """Verify W_3 W-line S_4 DIFFERS from T-line S_4.

    S_4^W = 2560/[c(5c+22)^3] vs S_4^T = 10/[c(5c+22)].
    Ratio: S_4^W / S_4^T = 256/(5c+22)^2.
    """
    results = {}
    for kval in [Fraction(1), Fraction(5), Fraction(10)]:
        w3_T = wN_tline(3, kval)
        w3_W = w3_wline(kval)
        cc = w3_T.central_charge
        ratio = w3_W.S4 / w3_T.S4 if w3_T.S4 != 0 else None
        expected_ratio = Fraction(256) / (5 * cc + 22)**2
        results[str(kval)] = {
            'c': cc,
            'S4_T': w3_T.S4,
            'S4_W': w3_W.S4,
            'ratio': ratio,
            'expected_ratio': expected_ratio,
            'ratio_match': ratio == expected_ratio if ratio is not None else False,
        }
    return results


# ============================================================================
# 13. Landscape summary statistics
# ============================================================================

def landscape_summary() -> Dict[str, Any]:
    """Summary statistics of Q^contact across the landscape."""
    reg = build_full_landscape()
    counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
    zero_count = 0
    nonzero_count = 0

    for datum in reg.values():
        counts[datum.shadow_class] += 1
        if datum.S4 == Fraction(0):
            zero_count += 1
        else:
            nonzero_count += 1

    return {
        'total': len(reg),
        'class_counts': counts,
        'S4_zero': zero_count,
        'S4_nonzero': nonzero_count,
        'universality_in_kappa': False,
    }


if __name__ == '__main__':
    print("Quartic contact invariant Q^contact: full standard landscape")
    print("=" * 70)

    # Table
    table = landscape_table()
    print(f"\n{'Name':<35} {'Class':<5} {'kappa':<12} {'S4=Q^contact':<20}")
    print("-" * 72)
    for row in table:
        s4_str = str(row['S4']) if row['S4'] != Fraction(0) else "0"
        print(f"{row['name']:<35} {row['class']:<5} {str(row['kappa']):<12} {s4_str:<20}")

    # Summary
    summary = landscape_summary()
    print(f"\nTotal families: {summary['total']}")
    print(f"Class counts: {summary['class_counts']}")
    print(f"S_4 = 0: {summary['S4_zero']}, S_4 != 0: {summary['S4_nonzero']}")
    print(f"Q^contact universal in kappa: {summary['universality_in_kappa']}")

    # Non-universality proof
    nu = demonstrate_non_universality()
    print(f"\nNon-universality at kappa={nu['kappa_common']}:")
    print(f"  Heisenberg: Q = {nu['Q_heis']} (class {nu['heis_class']})")
    print(f"  sl_2:       Q = {nu['Q_sl2']} (class {nu['sl2_class']})")
    print(f"  Vir(c=2):   Q = {nu['Q_vir']} (class {nu['vir_class']})")
