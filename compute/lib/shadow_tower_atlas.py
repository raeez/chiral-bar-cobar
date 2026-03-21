"""Shadow tower atlas: explicit closed-form computations for all standard families.

Computes the shadow Postnikov tower Sh_r for:
  1. Virasoro (class M, depth ∞): 32 entries on the primary line
  2. W3 (class M, depth ∞): W-line (even arities), T-line = Virasoro
  3. W_N for N=4,5,6: T-line = Virasoro, with W_N-specific sigma-invariants
  4. Affine KM V_k(sl_N) (class L, depth 3): terminates at arity 3
  5. Lattice VOAs (class G, depth 2): terminates at arity 2
  6. Beta-gamma (class C, depth 4): terminates at arity 4

Each entry is an explicit closed-form rational function of the level parameter.

FINITE GENERATION: For each family, the shadow tower is determined by
at most 3 independent inputs (kappa, C, Q). All higher arities follow
from the master equation recursion.

SIGMA-INVARIANT: For each family with Koszul conductor K_g,
Delta^(r) = S_r(c) + S_r(K_g - c) on the T-line.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Optional, Tuple

from sympy import Symbol, Rational, simplify, factor, S as Sym


c = Symbol('c')
k = Symbol('k')


# ===========================================================================
# 1. VIRASORO (class M, depth infinity)
# ===========================================================================

def virasoro_tower(max_r: int = 32) -> Dict[int, object]:
    """Virasoro shadow tower S_r on the primary line, r = 2, ..., max_r.

    S_r has denominator c^{r-3} (5c+22)^{floor((r-2)/2)} for r >= 4.
    Three inputs: S_2 = c/2, S_3 = 2, S_4 = 10/(c(5c+22)).
    Master equation determines r >= 5.
    """
    P = Rational(2) / c
    S: Dict[int, object] = {}
    S[2] = c / 2
    S[3] = Rational(2)
    S[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_r + 1):
        o_r = Rational(0)
        for j in range(2, r):
            kk = r + 2 - j
            if kk < 2 or kk >= r or kk not in S:
                continue
            if j > kk:
                continue
            coeff = j * kk * S[j] * S[kk] * P
            if j == kk:
                o_r += Rational(1, 2) * coeff
            else:
                o_r += coeff
        S[r] = factor(simplify(-o_r / (2 * r)))
    return S


# ===========================================================================
# 2. W3 ON THE W-LINE (class M, even arities only)
# ===========================================================================

def w3_wline_tower(max_r: int = 32) -> Dict[int, object]:
    """W3 shadow tower on the W-line (x_T = 0), even arities only.

    Propagator P_WW = 3/c. Sh_3 = 0 by Z_2 parity.
    Input: Sh_4|_W = 2560/(c(5c+22)^3) x_W^4.
    All odd-arity shadows vanish.
    """
    P_W = Rational(3) / c
    S: Dict[int, object] = {}

    # Even-arity inputs
    S[2] = c / 3  # kappa_W = c/3
    S[4] = Rational(2560) / (c * (5 * c + 22) ** 3)

    # Odd arities are zero
    S[3] = Rational(0)

    for r in range(5, max_r + 1):
        if r % 2 == 1:
            S[r] = Rational(0)
            continue
        o_r = Rational(0)
        for j in range(2, r):
            kk = r + 2 - j
            if kk < 2 or kk >= r or kk not in S:
                continue
            if j > kk:
                continue
            if S[j] == 0 or S[kk] == 0:
                continue
            coeff = j * kk * S[j] * S[kk] * P_W
            if j == kk:
                o_r += Rational(1, 2) * coeff
            else:
                o_r += coeff
        S[r] = factor(simplify(-o_r / (2 * r)))

    return S


# ===========================================================================
# 3. W_N T-LINE SIGMA-INVARIANTS
# ===========================================================================

# Koszul conductors: K_N = 2(N-1)(2N^2+2N+1) for type A
KOSZUL_CONDUCTORS = {
    2: 26,    # Virasoro
    3: 100,   # W3
    4: 246,   # W4
    5: 488,   # W5
    6: 850,   # W6
}


def tline_sigma_invariant(N: int, max_r: int = 32) -> Dict[int, object]:
    """T-line sigma-invariant Delta^(r) = S_r(c) + S_r(K_N - c) for W_N.

    On the T-line, S_r = Virasoro shadow coefficients.
    """
    K_N = KOSZUL_CONDUCTORS[N]
    S_vir = virasoro_tower(max_r)
    Delta: Dict[int, object] = {}
    for r, Sr in S_vir.items():
        Sr_dual = Sr.subs(c, K_N - c)
        Delta[r] = factor(simplify(Sr + Sr_dual))
    return Delta


def tline_level_independence(N: int, max_r: int = 32) -> Dict[int, bool]:
    """Check which arities are level-independent for W_N on the T-line."""
    Delta = tline_sigma_invariant(N, max_r)
    from sympy import diff
    result = {}
    for r, d in Delta.items():
        result[r] = simplify(diff(d, c)) == 0
    return result


# ===========================================================================
# 4. AFFINE KAC-MOODY (class L, depth 3)
# ===========================================================================

def affine_sl2_tower() -> Dict[int, object]:
    """Shadow tower for V_k(sl_2). Terminates at arity 3.

    kappa = 3(k+2)/4, cubic from Lie bracket, quartic = 0 (Jacobi).
    dim(sl_2) = 3, h^v = 2.
    """
    # On the primary line (single generator J):
    # Sh_2 = kappa * x^2 where kappa = 3(k+2)/4
    # Sh_3 = C * x^3 where C = structure-constant contribution
    # Sh_r = 0 for r >= 4 (the Jacobi identity kills the quartic obstruction)
    kap = Rational(3) * (k + 2) / 4
    return {
        2: kap,
        3: Rational(1),  # normalized cubic (Killing 3-cocycle)
        4: Rational(0),
        5: Rational(0),
        "depth": 3,
        "class": "L",
        "reason": "Jacobi identity: {C, C}_H = 0 on sl_2 by associativity",
    }


def affine_slN_tower(N: int) -> Dict[int, object]:
    """Shadow tower for V_k(sl_N). Terminates at arity 3.

    kappa = (N^2-1)(k+N)/(2N).
    For ALL simple Lie algebras: shadow depth = 3 (class L).
    The quartic obstruction o^(4) = 1/2{C,C}_H vanishes by the Jacobi identity.
    """
    dim_g = N * N - 1
    h_v = N
    kap = Rational(dim_g) * (k + h_v) / (2 * h_v)
    return {
        2: kap,
        3: "nonzero (Killing 3-cocycle)",
        4: Rational(0),
        "depth": 3,
        "class": "L",
        "reason": "Jacobi identity kills quartic for all semisimple g",
    }


# ===========================================================================
# 5. LATTICE VOAs (class G, depth 2)
# ===========================================================================

def lattice_tower(rank: int) -> Dict[int, object]:
    """Shadow tower for lattice VOA V_Lambda of rank r. Terminates at arity 2.

    kappa = rank (independent of the lattice cocycle).
    All shadows at arity >= 3 vanish: the OPE is abelian (no cubic interaction).
    """
    return {
        2: Rational(rank),
        3: Rational(0),
        4: Rational(0),
        "depth": 2,
        "class": "G",
        "reason": "Abelian OPE: no cubic or higher interactions",
    }


LATTICE_EXAMPLES = {
    "V_Z": {"rank": 1, "lattice": "Z"},
    "V_{Z^2}": {"rank": 2, "lattice": "Z^2"},
    "V_{A_2}": {"rank": 2, "lattice": "A_2 root lattice"},
    "V_{E_8}": {"rank": 8, "lattice": "E_8 root lattice"},
    "V_{Leech}": {"rank": 24, "lattice": "Leech lattice"},
}


# ===========================================================================
# 6. BETA-GAMMA (class C, depth 4)
# ===========================================================================

def betagamma_tower() -> Dict[int, object]:
    """Shadow tower for beta-gamma system. Terminates at arity 4.

    c = -2, kappa = -1.
    Cubic: nonzero (contact cubic from the beta-gamma OPE).
    Quartic: Q^contact = 10/(c(5c+22)) = 10/((-2)(12)) = -5/12.
    Quintic: 0 (terminates).
    """
    c_val = Rational(-2)
    kap = c_val / 2  # = -1
    Q = Rational(10) / (c_val * (5 * c_val + 22))  # = 10/(-2*12) = -5/12
    return {
        2: kap,  # = -1
        3: "nonzero (contact cubic)",
        4: Q,  # = -5/12
        5: Rational(0),
        6: Rational(0),
        "depth": 4,
        "class": "C",
        "reason": "Terminates at arity 4 by rank-one abelian rigidity",
    }


# ===========================================================================
# SUMMARY TABLE
# ===========================================================================

def shadow_depth_table() -> Dict[str, Dict[str, object]]:
    """Complete shadow depth classification for the standard landscape."""
    return {
        "Heisenberg": {"depth": 2, "class": "G", "kappa": "rank/2", "terminates": True},
        "Lattice V_Lambda": {"depth": 2, "class": "G", "kappa": "rank(Lambda)", "terminates": True},
        "Affine V_k(g)": {"depth": 3, "class": "L", "kappa": "d(k+h^v)/(2h^v)", "terminates": True},
        "Beta-gamma": {"depth": 4, "class": "C", "kappa": "-1", "terminates": True},
        "Virasoro": {"depth": "inf", "class": "M", "kappa": "c/2", "terminates": False},
        "W_3": {"depth": "inf", "class": "M", "kappa": "5c/6", "terminates": False},
        "W_N (N>=3)": {"depth": "inf", "class": "M", "kappa": "c*(H_N-1)", "terminates": False},
    }
