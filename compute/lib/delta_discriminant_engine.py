r"""delta_discriminant_engine.py -- Delta = 8*kappa*S_4 for the standard landscape.

Computes the critical discriminant Delta = 8*kappa*S_4 that classifies shadow
tower depth for each standard family of chirally Koszul algebras.

The shadow tower classification (thm:single-line-dichotomy):

    Delta = 0   <=>  tower terminates  <=>  class G or L
    Delta != 0  <=>  tower infinite    <=>  class M (or class C on charged stratum)

The discriminant is LINEAR in kappa (NOT quadratic, AP21):

    Delta = 8 * kappa * S_4

where kappa is the modular characteristic and S_4 is the quartic shadow
coefficient on the primary line.

FAMILIES AND THEIR DELTA:

Class G (Gaussian, r_max = 2):
  - Heisenberg_k: kappa = k, S_4 = 0, Delta = 0
  - Lattice VOA rank r: kappa = r, S_4 = 0, Delta = 0
  - Free fermion: kappa = 1/4, S_4 = 0, Delta = 0

Class L (Lie, r_max = 3):
  - Affine KM g-hat_k: kappa = dim(g)(k+h^v)/(2h^v), S_4 = 0, Delta = 0
  - S_4 = 0 by Jacobi identity (the quartic is killed by the Lie bracket)

Class C (contact, r_max = 4):
  - betagamma_lambda: on the NEUTRAL primary line, S_4 = 0, Delta = 0
  - But the quartic contact invariant is NONZERO on a charged stratum
  - So the system is class C globally (d_alg = 2) despite Delta = 0 on neutral line

Class M (mixed, r_max = infinity):
  - Virasoro_c: kappa = c/2, S_4 = 10/[c(5c+22)], Delta = 40/(5c+22)
  - W_3 T-line: identical to Virasoro
  - W_3 W-line: kappa = c/3, S_4 = 2560/[c(5c+22)^3], Delta = 20480/[3(5c+22)^3]
  - W_N (N >= 2): all class M

CANONICAL FORMULAS (from landscape_census.tex + C3, C4):
  kappa(Heis_k) = k                           (C1)
  kappa(Vir_c) = c/2                          (C2)
  kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)       (C3)
  kappa(W_N) = c*(H_N - 1)                    (C4)
  kappa(betagamma_lam) = 6*lam^2 - 6*lam + 1 (C6 complement)

S_4(Vir_c) = 10/[c(5c+22)]                   (C30: Delta = 8*kappa*S_4)
  At kappa != 0: Delta = 0 iff S_4 = 0.

Manuscript references:
  thm:single-line-dichotomy, eq:discriminant-def,
  thm:shadow-connection, def:shadow-metric,
  thm:shadow-archetype-classification (G/L/C/M).
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# 1. Core formula: Delta = 8 * kappa * S_4
# ============================================================================

def delta_discriminant(kappa: Fraction, S4: Fraction) -> Fraction:
    r"""Critical discriminant Delta = 8*kappa*S_4.

    LINEAR in kappa (C30, AP21: NOT quadratic).

    Parameters
    ----------
    kappa : modular characteristic of the algebra
    S4 : quartic shadow coefficient on the primary line

    Returns
    -------
    Delta = 8 * kappa * S_4
    """
    return Fraction(8) * kappa * S4


# ============================================================================
# 2. Family-specific kappa formulas
# ============================================================================

def kappa_heisenberg(k: Fraction) -> Fraction:
    """kappa(H_k) = k.
    # VERIFIED [DC] av(r(z)) = av(k/z) = k
    # VERIFIED [LT] C1 census
    """
    return Fraction(k)


def kappa_virasoro(c: Fraction) -> Fraction:
    """kappa(Vir_c) = c/2.
    # VERIFIED [LC] c=0 -> 0; c=13 -> 13/2 self-dual
    # VERIFIED [LT] C2 census
    """
    return Fraction(c) / 2


def kappa_affine_km(dim_g: int, h_dual: int, k: Fraction) -> Fraction:
    """kappa(V_k(g)) = dim(g)*(k+h^v)/(2*h^v).
    # VERIFIED [LC] k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical)
    # VERIFIED [LT] C3 census
    """
    return Fraction(dim_g) * (Fraction(k) + h_dual) / (2 * h_dual)


def kappa_w_n(N: int, c: Fraction) -> Fraction:
    """kappa(W_N) = c*(H_N - 1) where H_N = sum_{j=1}^N 1/j.
    # VERIFIED [LC] N=2 -> c*(3/2-1) = c/2 = kappa_Vir (W_2 = Vir)
    # VERIFIED [LT] C4 census; AP136: NOT c*H_{N-1}
    """
    H_N = sum(Fraction(1, j) for j in range(1, N + 1))
    return Fraction(c) * (H_N - 1)


def kappa_betagamma(lam: Fraction) -> Fraction:
    """kappa(betagamma_lam) = 6*lam^2 - 6*lam + 1.
    # VERIFIED [LC] lam=1/2 -> -1/2; lam=1 -> 1
    # VERIFIED [LT] complementarity c_bg + c_bc = 0; kappa = c_bg/2
    """
    lam = Fraction(lam)
    return 6 * lam ** 2 - 6 * lam + 1


def kappa_lattice(rank: int) -> Fraction:
    """kappa(lattice VOA, rank r) = r.
    Even unimodular lattice: kappa = rank (= c for rank-c lattice).
    """
    return Fraction(rank)


def kappa_free_fermion() -> Fraction:
    """kappa(free fermion) = 1/4 = c/2 where c = 1/2.
    bc at lambda = 1/2: c_bc(1/2) = 1 - 3*(2*1/2-1)^2 = 1.
    But kappa = c/2 = 1/2 for the SINGLE Dirac fermion.
    Actually: free fermion at lambda=1/2 has c=1/2 (single real fermion),
    kappa = c/2 = 1/4.
    """
    return Fraction(1, 4)


# ============================================================================
# 3. Family-specific S_4 formulas
# ============================================================================

def S4_heisenberg() -> Fraction:
    """S_4(Heisenberg) = 0. Abelian OPE: no quartic shadow."""
    return Fraction(0)


def S4_lattice() -> Fraction:
    """S_4(lattice VOA) = 0. Free-field, abelian bar complex."""
    return Fraction(0)


def S4_free_fermion() -> Fraction:
    """S_4(free fermion) = 0. Single generator, class G."""
    return Fraction(0)


def S4_affine_km() -> Fraction:
    """S_4(affine KM) = 0 for all simple g at all levels.
    The Jacobi identity kills the quartic shadow: the Lie bracket
    on the bar complex terminates at cubic (class L).
    """
    return Fraction(0)


def S4_virasoro(c: Fraction) -> Fraction:
    """S_4(Vir_c) = 10/[c(5c+22)].
    The quartic contact invariant from the Virasoro OPE.
    Poles at c = 0 and c = -22/5.
    # VERIFIED [DC] from T_{(4)}T OPE coefficient
    # VERIFIED [LT] AP129: NOT -(5c+22)/(10c) (reciprocal error)
    """
    c = Fraction(c)
    return Fraction(10) / (c * (5 * c + 22))


def S4_w3_T_line(c: Fraction) -> Fraction:
    """S_4 on W_3 T-line = S_4(Vir_c). The T-line is the Virasoro subsector."""
    return S4_virasoro(c)


def S4_w3_W_line(c: Fraction) -> Fraction:
    """S_4 on W_3 W-line = 2560/[c(5c+22)^3].
    The W-line has alpha = 0 (Z_2 parity) and higher S_4.
    """
    c = Fraction(c)
    return Fraction(2560) / (c * (5 * c + 22) ** 3)


def S4_betagamma_neutral_line() -> Fraction:
    """S_4 on betagamma neutral primary line = 0.
    The quartic contact is nonzero on a charged stratum (class C),
    but vanishes on the neutral weight-changing line.
    """
    return Fraction(0)


# ============================================================================
# 4. Delta for each family
# ============================================================================

def delta_heisenberg(k: Fraction) -> Fraction:
    """Delta(H_k) = 0. Class G."""
    return delta_discriminant(kappa_heisenberg(k), S4_heisenberg())


def delta_lattice(rank: int) -> Fraction:
    """Delta(lattice, rank r) = 0. Class G."""
    return delta_discriminant(kappa_lattice(rank), S4_lattice())


def delta_free_fermion() -> Fraction:
    """Delta(free fermion) = 0. Class G."""
    return delta_discriminant(kappa_free_fermion(), S4_free_fermion())


def delta_affine_km(dim_g: int, h_dual: int, k: Fraction) -> Fraction:
    """Delta(V_k(g)) = 0. Class L."""
    return delta_discriminant(kappa_affine_km(dim_g, h_dual, k), S4_affine_km())


def delta_virasoro(c: Fraction) -> Fraction:
    """Delta(Vir_c) = 40/(5c+22).
    Derivation: 8*(c/2)*10/[c(5c+22)] = 40/(5c+22).
    The c in kappa cancels the 1/c pole in S_4.
    # VERIFIED [DC] 8*(c/2)*10/[c(5c+22)] = 40/(5c+22)
    # VERIFIED [LC] c -> inf: Delta -> 0 (semiclassical)
    """
    c = Fraction(c)
    return Fraction(40) / (5 * c + 22)


def delta_w3_T_line(c: Fraction) -> Fraction:
    """Delta on W_3 T-line = 40/(5c+22) (same as Virasoro)."""
    return delta_virasoro(c)


def delta_w3_W_line(c: Fraction) -> Fraction:
    """Delta on W_3 W-line = 20480/[3(5c+22)^3].
    Derivation: 8*(c/3)*2560/[c(5c+22)^3] = 20480/[3(5c+22)^3].
    """
    c = Fraction(c)
    return Fraction(20480) / (3 * (5 * c + 22) ** 3)


def delta_betagamma_neutral(lam: Fraction) -> Fraction:
    """Delta(betagamma) on neutral line = 0.
    Class C globally (quartic on charged stratum), but Delta = 0 on neutral.
    """
    return delta_discriminant(kappa_betagamma(lam), S4_betagamma_neutral_line())


# ============================================================================
# 5. Shadow class determination
# ============================================================================

def classify_from_delta(kappa: Fraction, alpha: Fraction,
                        S4: Fraction) -> str:
    """Determine shadow class from single-line data.

    G: Delta = 0, alpha = 0   (Heisenberg, lattice, free fermion)
    L: Delta = 0, alpha != 0  (affine KM)
    M: Delta != 0, alpha != 0 (Virasoro, W_N)
    even_cascade: Delta != 0, alpha = 0 (W_3 W-line: even only)

    Class C is NOT detectable from single-line data alone (requires
    stratum separation analysis).
    """
    Delta = delta_discriminant(kappa, S4)
    if Delta == 0:
        return 'G' if alpha == 0 else 'L'
    else:
        return 'even_cascade' if alpha == 0 else 'M'


# ============================================================================
# 6. Discriminant complementarity (Virasoro)
# ============================================================================

def virasoro_discriminant_complementarity(c: Fraction) -> Dict[str, Any]:
    """Delta(Vir_c) + Delta(Vir_{26-c}) = 6960/[(5c+22)(152-5c)].

    The universal numerator 6960 = 40 * 174 = 2^4 * 3 * 5 * 29.
    At self-dual c=13: both Delta equal 40/87, sum = 80/87.
    """
    c = Fraction(c)
    D = delta_virasoro(c)
    D_dual = delta_virasoro(Fraction(26) - c)
    total = D + D_dual
    predicted = Fraction(6960) / ((5 * c + 22) * (152 - 5 * c))
    return {
        'c': c,
        'c_dual': Fraction(26) - c,
        'Delta': D,
        'Delta_dual': D_dual,
        'sum': total,
        'predicted': predicted,
        'match': total == predicted,
    }


# ============================================================================
# 7. Full landscape discriminant atlas
# ============================================================================

def full_discriminant_landscape() -> Dict[str, Dict[str, Any]]:
    """Discriminant atlas for the full standard landscape.

    Returns a dict mapping family labels to their shadow data:
    {kappa, S4, Delta, alpha, shadow_class, finite_tower}.
    """
    landscape = {}

    # Class G
    for k_val in [1, 2, 5]:
        k = Fraction(k_val)
        landscape[f'Heisenberg_k{k_val}'] = {
            'kappa': kappa_heisenberg(k),
            'S4': S4_heisenberg(),
            'Delta': delta_heisenberg(k),
            'alpha': Fraction(0),
            'shadow_class': 'G',
            'finite_tower': True,
        }

    for r in [8, 16, 24]:
        landscape[f'Lattice_r{r}'] = {
            'kappa': kappa_lattice(r),
            'S4': S4_lattice(),
            'Delta': delta_lattice(r),
            'alpha': Fraction(0),
            'shadow_class': 'G',
            'finite_tower': True,
        }

    landscape['FreeFermion'] = {
        'kappa': kappa_free_fermion(),
        'S4': S4_free_fermion(),
        'Delta': delta_free_fermion(),
        'alpha': Fraction(0),
        'shadow_class': 'G',
        'finite_tower': True,
    }

    # Class L: affine KM
    km_families = [
        ('sl2', 3, 2), ('sl3', 8, 3), ('sl4', 15, 4),
        ('so5', 10, 3), ('g2', 14, 4), ('e8', 248, 30),
    ]
    for name, dim_g, h_dual in km_families:
        for k_val in [1, 2]:
            k = Fraction(k_val)
            landscape[f'Affine_{name}_k{k_val}'] = {
                'kappa': kappa_affine_km(dim_g, h_dual, k),
                'S4': S4_affine_km(),
                'Delta': delta_affine_km(dim_g, h_dual, k),
                'alpha': Fraction(1),  # nonzero Lie bracket cubic
                'shadow_class': 'L',
                'finite_tower': True,
            }

    # Class C: betagamma
    for lam_val in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
        landscape[f'BetaGamma_lam{lam_val}'] = {
            'kappa': kappa_betagamma(lam_val),
            'S4': S4_betagamma_neutral_line(),
            'Delta': delta_betagamma_neutral(lam_val),
            'alpha': Fraction(0),
            'shadow_class': 'C',
            'finite_tower': True,  # on neutral line
            'note': 'Quartic nonzero on charged stratum (class C globally)',
        }

    # Class M: Virasoro
    for c_val in [1, 2, 5, 13, 25, 26]:
        c = Fraction(c_val)
        landscape[f'Virasoro_c{c_val}'] = {
            'kappa': kappa_virasoro(c),
            'S4': S4_virasoro(c),
            'Delta': delta_virasoro(c),
            'alpha': Fraction(2),
            'shadow_class': 'M',
            'finite_tower': False,
        }

    # Class M: W_3 T-line
    for c_val in [2, 13]:
        c = Fraction(c_val)
        landscape[f'W3_T_c{c_val}'] = {
            'kappa': kappa_virasoro(c),
            'S4': S4_w3_T_line(c),
            'Delta': delta_w3_T_line(c),
            'alpha': Fraction(2),
            'shadow_class': 'M',
            'finite_tower': False,
        }

    # Class M: W_3 W-line
    for c_val in [2, 13]:
        c = Fraction(c_val)
        landscape[f'W3_W_c{c_val}'] = {
            'kappa': kappa_w_n(3, c) - kappa_virasoro(c),  # kappa_W = c/3
            'S4': S4_w3_W_line(c),
            'Delta': delta_w3_W_line(c),
            'alpha': Fraction(0),
            'shadow_class': 'even_cascade',
            'finite_tower': False,
        }

    return landscape


# ============================================================================
# 8. Consistency checks
# ============================================================================

def verify_delta_linearity_in_kappa(S4: Fraction,
                                     kappa_values: List[Fraction]
                                     ) -> bool:
    """Delta is LINEAR in kappa at fixed S_4. NOT quadratic (AP21)."""
    if len(kappa_values) < 2:
        return True
    base = delta_discriminant(kappa_values[0], S4)
    for kv in kappa_values[1:]:
        ratio = delta_discriminant(kv, S4) / base if base != 0 else None
        expected_ratio = kv / kappa_values[0]
        if ratio is not None and ratio != expected_ratio:
            return False
    return True


def verify_virasoro_c_cancellation() -> Dict[str, Any]:
    """The c in kappa(Vir) cancels the 1/c in S_4(Vir).

    Delta(Vir_c) = 8*(c/2)*10/[c(5c+22)] = 40/(5c+22).
    The result is FINITE at c = 0 (Delta(0) = 40/22 = 20/11),
    even though kappa -> 0 and S_4 -> infinity separately.
    """
    c_values = [Fraction(1), Fraction(2), Fraction(5), Fraction(13)]
    results = {}
    for c in c_values:
        kappa = kappa_virasoro(c)
        s4 = S4_virasoro(c)
        delta_from_product = delta_discriminant(kappa, s4)
        delta_closed = delta_virasoro(c)
        results[str(c)] = {
            'kappa': kappa,
            'S4': s4,
            'delta_product': delta_from_product,
            'delta_closed': delta_closed,
            'match': delta_from_product == delta_closed,
        }
    return results


if __name__ == '__main__':
    print("=" * 70)
    print("DELTA DISCRIMINANT ENGINE: Delta = 8*kappa*S_4")
    print("=" * 70)

    landscape = full_discriminant_landscape()
    print(f"\n{'Family':<30s} {'kappa':>10s} {'S4':>14s} {'Delta':>14s} {'Class':>6s} {'Finite':>6s}")
    print("-" * 80)
    for name, data in sorted(landscape.items()):
        k_str = str(data['kappa'])[:10]
        s_str = str(data['S4'])[:14]
        d_str = str(data['Delta'])[:14]
        print(f"{name:<30s} {k_str:>10s} {s_str:>14s} {d_str:>14s} "
              f"{data['shadow_class']:>6s} {'Y' if data['finite_tower'] else 'N':>6s}")

    print("\nVirasoro complementarity:")
    for c_val in [1, 2, 5, 13, 25]:
        comp = virasoro_discriminant_complementarity(Fraction(c_val))
        print(f"  c={c_val}: Delta={comp['Delta']}, Delta_dual={comp['Delta_dual']}, "
              f"sum={comp['sum']}, match={comp['match']}")
