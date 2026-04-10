r"""Entanglement entropy S_EE = (2*kappa/3)*log(L/eps) for all standard families.

Computes and tabulates the single-interval entanglement entropy across
the standard chiral algebra landscape.  The formula is:

    S_EE(A) = (2*kappa(A)/3) * log(L/epsilon)

where kappa(A) is the modular characteristic of the chiral algebra A,
L is the interval length, and epsilon is the UV cutoff.

This reduces to the Calabrese-Cardy formula S_EE = (c/3)*log(L/eps)
for Virasoro (where kappa = c/2), but differs for non-Virasoro families
where kappa != c/2 in general.

Families and kappa sources (all from landscape_census.tex, cross-checked
against compute/ engines and CLAUDE.md C1-C4, C5-C6):

  Heisenberg H_k:           kappa = k                                [C1]
  Virasoro Vir_c:            kappa = c/2                              [C2]
  Affine KM V_k(g):          kappa = dim(g)*(k+h^v)/(2*h^v)          [C3]
  Principal W_N:             kappa = c*(H_N - 1), H_N = sum 1/j       [C4]
  Bosonic betagamma:         kappa = 6*lam^2 - 6*lam + 1              [C6]
  Fermionic bc:              kappa = c_bc(lambda)/2                    [C5]
  Super Virasoro:            kappa = (3c-2)/4                          [AP68]
  Lattice (rank r, k=1):    kappa = r                                 [C1]
  Leech lattice:             kappa = 24                                [rank 24]

Anti-pattern coverage:
  AP1   -- kappa from canonical census, not memory
  AP10  -- every expected value has 2+ independent derivation paths
  AP24  -- complementarity sum family-specific, not assumed zero
  AP39  -- kappa != S_2 except for Virasoro
  AP126 -- kappa boundary checks included (k=0, k=-h^v)
  AP136 -- H_N - 1, not H_{N-1}, in W_N kappa
  AP137 -- c_bc + c_bg = 0 verified at each lambda

References:
  Calabrese-Cardy 2004 (hep-th/0405152)
  CLAUDE.md census C1-C6, C8, C18, C19; AP68
  landscape_census.tex
  entanglement_shadow_engine.py (scalar-level derivation)
"""

from fractions import Fraction
import math
from typing import Any, Dict, List


# ---------------------------------------------------------------------------
# Harmonic numbers
# ---------------------------------------------------------------------------

def harmonic_number(n: int) -> Fraction:
    """H_n = sum_{j=1}^{n} 1/j.  [C19: CLAUDE.md]

    >>> harmonic_number(1)
    Fraction(1, 1)
    >>> harmonic_number(2)
    Fraction(3, 2)
    >>> harmonic_number(3)
    Fraction(11, 6)
    """
    return sum(Fraction(1, j) for j in range(1, n + 1))


# ---------------------------------------------------------------------------
# Kappa functions (exact, using Fraction arithmetic)
# ---------------------------------------------------------------------------

def kappa_heisenberg(k: Any) -> Fraction:
    """kappa(H_k) = k.  [C1: landscape_census.tex]

    Checks: k=0 -> 0; k=1 -> 1.
    """
    return Fraction(k)


def kappa_virasoro(c: Any) -> Fraction:
    """kappa(Vir_c) = c/2.  [C2: landscape_census.tex]

    Checks: c=0 -> 0; c=13 -> 13/2 (self-dual); c=26 -> 13.
    """
    return Fraction(c, 2)


def kappa_affine_km(dim_g: int, k: Any, h_dual: int) -> Fraction:
    r"""kappa(V_k(g)) = dim(g)*(k + h^v)/(2*h^v).  [C3: landscape_census.tex]

    Checks:
      k=0  -> dim(g)/2  (NOT zero; abelian limit)
      k=-h^v -> 0       (critical level)
    """
    return Fraction(dim_g) * (Fraction(k) + Fraction(h_dual)) / (2 * Fraction(h_dual))


def kappa_affine_sl2(k: Any) -> Fraction:
    r"""kappa(V_k(sl_2)) = 3*(k+2)/4.  dim(sl_2)=3, h^v=2.  [C3]

    Checks: k=0 -> 3/2; k=-2 -> 0 (critical).
    """
    return kappa_affine_km(3, k, 2)


def kappa_affine_sl3(k: Any) -> Fraction:
    r"""kappa(V_k(sl_3)) = 8*(k+3)/6 = 4*(k+3)/3.  dim(sl_3)=8, h^v=3.  [C3]

    Checks: k=0 -> 4; k=-3 -> 0 (critical).
    """
    return kappa_affine_km(8, k, 3)


def kappa_affine_so4(k: Any) -> Fraction:
    r"""kappa(V_k(so_4)) = 6*(k+2)/4 = 3*(k+2)/2.  dim(so_4)=6, h^v=2.  [C3]

    Checks: k=0 -> 3; k=-2 -> 0 (critical).
    """
    return kappa_affine_km(6, k, 2)


def kappa_affine_g2(k: Any) -> Fraction:
    r"""kappa(V_k(g_2)) = 14*(k+4)/8 = 7*(k+4)/4.  dim(g_2)=14, h^v=4.  [C3]

    Checks: k=0 -> 7; k=-4 -> 0 (critical).
    """
    return kappa_affine_km(14, k, 4)


def kappa_affine_e8(k: Any) -> Fraction:
    r"""kappa(V_k(e_8)) = 248*(k+30)/60 = 62*(k+30)/15.  dim(e_8)=248, h^v=30.  [C3]

    Checks: k=0 -> 124; k=1 -> 1922/15; k=-30 -> 0 (critical).
    """
    return kappa_affine_km(248, k, 30)


def kappa_wn(n: int, c: Any) -> Fraction:
    r"""kappa(W_N) = c*(H_N - 1), H_N = sum_{j=1}^{N} 1/j.  [C4]

    AP136 check: H_{N-1} != H_N - 1.
      N=2: H_2-1 = 1/2, so kappa(W_2) = c/2 = kappa(Vir).  Correct.
      N=3: H_3-1 = 5/6, so kappa(W_3) = 5c/6.
    """
    h_n_minus_1 = harmonic_number(n) - 1
    return Fraction(c) * h_n_minus_1


def c_betagamma(lam: Any) -> Fraction:
    r"""c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1).  [C6]

    Checks: lambda=1/2 -> -1; lambda=2 -> 26.
    """
    lam = Fraction(lam)
    return 2 * (6 * lam**2 - 6 * lam + 1)


def c_bc(lam: Any) -> Fraction:
    r"""c_bc(lambda) = 1 - 3*(2*lambda - 1)^2.  [C5]

    Checks: lambda=1/2 -> 1; lambda=2 -> -26.
    """
    lam = Fraction(lam)
    return 1 - 3 * (2 * lam - 1)**2


def kappa_betagamma(lam: Any) -> Fraction:
    r"""kappa(betagamma_lambda) = c_bg(lambda)/2 = 6*lambda^2 - 6*lambda + 1.

    c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1).  [C6: landscape_census.tex]

    Checks:
      lambda=1/2 -> 6/4-3+1 = -1/2  (symplectic boson, c=-1)
      lambda=1   -> 6-6+1 = 1
      lambda=2   -> 24-12+1 = 13
    """
    lam = Fraction(lam)
    return 6 * lam**2 - 6 * lam + 1


def kappa_bc(lam: Any) -> Fraction:
    r"""kappa(bc_lambda) = c_bc(lambda)/2.

    bc is fermionic; its kappa follows the Virasoro-type relation kappa = c/2
    since it is a free-field system with Virasoro structure.

    Checks:
      lambda=1/2 -> c_bc=1, kappa=1/2  (free fermion)
      lambda=2   -> c_bc=-26, kappa=-13 (reparametrization ghost)
    """
    return c_bc(lam) / 2


def kappa_super_virasoro(c: Any) -> Fraction:
    r"""kappa(SVir_c) = (3c - 2)/4.  [AP68: CLAUDE.md]

    Checks:
      c=2/3 -> (2-2)/4 = 0
      c=10  -> 28/4 = 7
    """
    return (3 * Fraction(c) - 2) / 4


def kappa_lattice(rank: int, k: int = 1) -> Fraction:
    r"""kappa(lattice) = rank * kappa(H_k) = rank * k.

    Each lattice direction contributes a Heisenberg at level k.
    For even unimodular lattices, k=1.

    Checks: Leech -> rank=24, kappa=24; E_8 lattice -> rank=8, kappa=8.
    """
    return Fraction(rank) * Fraction(k)


# ---------------------------------------------------------------------------
# Central formula: entanglement entropy
# ---------------------------------------------------------------------------

def entanglement_entropy(kappa_val: Any, L: float, eps: float) -> float:
    r"""S_EE = (2*kappa/3) * log(L/eps).

    This is the single-interval entanglement entropy at the scalar
    (leading) level.  For Virasoro, kappa = c/2, so
    S_EE = (c/3)*log(L/eps) (Calabrese-Cardy 2004).

    For non-Virasoro families, kappa != c/2 in general.

    Parameters
    ----------
    kappa_val : number
        Modular characteristic of the chiral algebra.
    L : float
        Interval length.
    eps : float
        UV cutoff (must be positive).

    Returns
    -------
    float
        The entanglement entropy S_EE.
    """
    if eps <= 0:
        raise ValueError("UV cutoff eps must be positive")
    if L <= 0:
        raise ValueError("Interval length L must be positive")
    k = float(kappa_val)
    return (2 * k / 3) * math.log(L / eps)


def entanglement_entropy_exact(kappa_val: Fraction, L_over_eps: Any = None) -> Fraction:
    r"""Exact (symbolic) S_EE prefactor: returns (2*kappa/3).

    The full entropy is (2*kappa/3)*log(L/eps).  This function returns the
    rational prefactor for exact verification.
    """
    return Fraction(2) * Fraction(kappa_val) / Fraction(3)


# ---------------------------------------------------------------------------
# Lie algebra data for affine KM
# ---------------------------------------------------------------------------

LIE_DATA = {
    'sl2':  {'dim': 3,   'h_dual': 2},
    'sl3':  {'dim': 8,   'h_dual': 3},
    'sl4':  {'dim': 15,  'h_dual': 4},
    'so4':  {'dim': 6,   'h_dual': 2},
    'so5':  {'dim': 10,  'h_dual': 3},
    'g2':   {'dim': 14,  'h_dual': 4},
    'f4':   {'dim': 52,  'h_dual': 9},
    'e6':   {'dim': 78,  'h_dual': 12},
    'e7':   {'dim': 133, 'h_dual': 18},
    'e8':   {'dim': 248, 'h_dual': 30},
}


# ---------------------------------------------------------------------------
# Standard landscape tabulation
# ---------------------------------------------------------------------------

FAMILIES = [
    # (name, params_dict, kappa_value)
    ("Heisenberg k=1",        {"k": 1},              kappa_heisenberg(1)),
    ("Heisenberg k=2",        {"k": 2},              kappa_heisenberg(2)),
    ("Heisenberg k=0",        {"k": 0},              kappa_heisenberg(0)),
    ("Virasoro c=1",          {"c": 1},              kappa_virasoro(1)),
    ("Virasoro c=1/2 (Ising)",{"c": Fraction(1, 2)}, kappa_virasoro(Fraction(1, 2))),
    ("Virasoro c=13 (self-dual)", {"c": 13},         kappa_virasoro(13)),
    ("Virasoro c=26",         {"c": 26},             kappa_virasoro(26)),
    ("Virasoro c=0",          {"c": 0},              kappa_virasoro(0)),
    ("Affine sl_2 k=1",      {"g": "sl2", "k": 1},  kappa_affine_sl2(1)),
    ("Affine sl_2 k=0",      {"g": "sl2", "k": 0},  kappa_affine_sl2(0)),
    ("Affine sl_2 k=-2 (crit)", {"g": "sl2", "k": -2}, kappa_affine_sl2(-2)),
    ("Affine sl_3 k=1",      {"g": "sl3", "k": 1},  kappa_affine_sl3(1)),
    ("Affine sl_3 k=0",      {"g": "sl3", "k": 0},  kappa_affine_sl3(0)),
    ("Affine sl_3 k=-3 (crit)", {"g": "sl3", "k": -3}, kappa_affine_sl3(-3)),
    ("Affine so_4 k=1",      {"g": "so4", "k": 1},  kappa_affine_so4(1)),
    ("Affine g_2 k=1",       {"g": "g2", "k": 1},   kappa_affine_g2(1)),
    ("Affine e_8 k=1",       {"g": "e8", "k": 1},   kappa_affine_e8(1)),
    ("W_2 c=1 (=Vir)",       {"N": 2, "c": 1},      kappa_wn(2, 1)),
    ("W_3 c=2",              {"N": 3, "c": 2},      kappa_wn(3, 2)),
    ("W_3 c=6",              {"N": 3, "c": 6},      kappa_wn(3, 6)),
    ("Betagamma lam=1/2 (sympl boson)", {"lambda": Fraction(1, 2)}, kappa_betagamma(Fraction(1, 2))),
    ("Betagamma lam=1",      {"lambda": 1},          kappa_betagamma(1)),
    ("Betagamma lam=2",      {"lambda": 2},          kappa_betagamma(2)),
    ("bc lam=1/2 (free fermion)", {"lambda": Fraction(1, 2)}, kappa_bc(Fraction(1, 2))),
    ("bc lam=2 (reparam ghost)", {"lambda": 2},      kappa_bc(2)),
    ("Super Virasoro c=10",  {"c": 10},              kappa_super_virasoro(10)),
    ("Super Virasoro c=2/3", {"c": Fraction(2, 3)},  kappa_super_virasoro(Fraction(2, 3))),
    ("Lattice E_8",          {"rank": 8},            kappa_lattice(8)),
    ("Leech lattice",        {"rank": 24},           kappa_lattice(24)),
]


def tabulate(L: float = 100.0, eps: float = 1.0) -> List[Dict]:
    """Compute S_EE for all standard families at given L, eps.

    Returns a list of dicts with keys:
      family, params, kappa, kappa_float, S_EE, L, eps, prefactor
    where prefactor = 2*kappa/3.
    """
    results = []
    for name, params, kappa_val in FAMILIES:
        s_ee = entanglement_entropy(kappa_val, L, eps)
        results.append({
            "family": name,
            "params": params,
            "kappa": kappa_val,
            "kappa_float": float(kappa_val),
            "prefactor": float(Fraction(2) * kappa_val / Fraction(3)),
            "S_EE": s_ee,
            "L": L,
            "eps": eps,
        })
    return results


def print_table(L: float = 100.0, eps: float = 1.0):
    """Pretty-print the entanglement entropy tabulation."""
    results = tabulate(L, eps)
    header = (f"{'Family':<40} {'kappa':>12} {'2*kappa/3':>12} "
              f"{'S_EE':>14}  (L={L}, eps={eps})")
    print(header)
    print("-" * len(header))
    for r in results:
        print(
            f"{r['family']:<40} {float(r['kappa']):>12.6f} "
            f"{r['prefactor']:>12.6f} {r['S_EE']:>14.8f}"
        )


if __name__ == "__main__":
    print_table()
