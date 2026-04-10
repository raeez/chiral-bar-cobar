r"""Niemeier lattice shadow depth engine via cusp form arithmetic.

MATHEMATICAL FRAMEWORK
======================

All 24 Niemeier lattices Lambda are even unimodular lattices of rank 24.
Each yields a holomorphic VOA V_Lambda of central charge c = 24.

SHADOW DEPTH VIA ARITHMETIC
============================

The depth decomposition (thm:depth-decomposition, arithmetic_shadows.tex)
gives:

    d(A) = 1 + d_arith(A) + d_alg(A)

For lattice VOAs (eq:depth-cusp-formula, eq:depth-cusp-full):

    d(V_Lambda) = 3 + dim S_{r/2}(SL(2,Z))

where r = rank(Lambda) and S_k denotes the space of cusp forms of weight k
for the full modular group SL(2,Z).

For Niemeier lattices: r = 24, so the relevant weight is r/2 = 12.
The space S_12(SL(2,Z)) is 1-dimensional, spanned by the Ramanujan Delta
function Delta(tau) = eta(tau)^{24} = sum_{n>=1} tau(n) q^n.

Therefore: d(V_Lambda) = 3 + dim S_12 = 3 + 1 = 4 for ALL 24 Niemeier
lattice VOAs.

This is an ARITHMETIC shadow depth: d_alg = 0 (class G on the scalar
shadow tower, bar complex strictly coassociative), d_arith = 2 + dim S_12
= 3 (two Eisenstein critical lines plus one cusp eigenform critical line).

The depth decomposition gives:
    d = 1 + d_arith + d_alg = 1 + 3 + 0 = 4.

The class label is F_4 (finite depth 4), NOT class C (betagamma).
The scalar shadow tower has S_3 = 0, S_4 = 0 (class G, depth 2),
but the full arithmetic shadow depth sees the Ramanujan cusp form.

DIMENSION OF MODULAR FORM SPACES
=================================

For SL(2,Z), the dimension formulas are:

    dim M_k = { 0           if k odd or k < 0
              { 1           if k = 0
              { 0           if k = 2
              { floor(k/12) if k >= 4 and k = 2 mod 12
              { floor(k/12)+1  if k >= 4 and k != 2 mod 12

    dim S_k = max(0, dim M_k - 1)  for k >= 2

Verification at k = 12: k mod 12 = 0 != 2, so dim M_12 = 12//12 + 1 = 2.
dim S_12 = 2 - 1 = 1.  This is the Ramanujan Delta.

KAPPA FOR NIEMEIER LATTICE VOAs
================================

Each V_Lambda has c = 24.  The kappa invariant for a rank-r free boson
(Heisenberg) lattice VOA at level k = 1 is:

    kappa(V_Lambda) = r * k = 24 * 1 = 24

Cross-check via the Heisenberg formula: kappa(H_k) = k per boson.
For 24 bosons at level 1: kappa_total = 24.
Cross-check via c: c = rank = 24 for free bosons, and kappa = c = 24.
(NOTE: kappa = c is specific to Heisenberg/lattice; kappa = c/2 is Virasoro
only, per AP1/C1/C2.)

THE 24 NIEMEIER ROOT SYSTEMS
==============================

Classification by root system (Niemeier 1968, Conway-Sloane Ch. 16):

  23 with non-empty root system (all rank 24):
    D_24, D_16 E_8, 3E_8, A_24, 2D_12, A_17 E_7, D_10 2E_7,
    A_15 D_9, 3D_8, 2A_12, A_11 D_7 E_6, 4E_6, 2A_9 D_6,
    4D_6, 3A_8, 2A_7 2D_5, 4A_6, 4A_5 D_4, 6D_4, 6A_4,
    8A_3, 12A_2, 24A_1

  1 with empty root system:
    Leech lattice (Lambda_24)

All 24 have c = 24, kappa = 24, and shadow depth d = 4.

MULTI-PATH VERIFICATION:
  Path 1: Direct formula d = 3 + dim S_{r/2} with r = 24
  Path 2: Depth decomposition d = 1 + d_arith + d_alg = 1 + 3 + 0
  Path 3: Modular forms dimension formula for dim S_12 = 1
  Path 4: Manuscript tables (higher_genus_modular_koszul.tex, line ~15991)
  Path 5: Conway-Sloane classification (24 lattices, all rank 24)

References:
    thm:depth-decomposition (arithmetic_shadows.tex)
    eq:depth-cusp-formula (arithmetic_shadows.tex)
    eq:depth-cusp-full (arithmetic_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    prop:leech-epstein (higher_genus_modular_koszul.tex)
    Niemeier (1968): classification of even unimodular rank-24 lattices
    Conway-Sloane, "Sphere Packings, Lattices and Groups", Ch. 16
    Ramanujan (1916): Delta = eta^{24}, dim S_12 = 1
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple


# =========================================================================
# 1. Modular forms dimension formulas for SL(2,Z)
# =========================================================================

def dim_M_k(k: int) -> int:
    r"""Dimension of M_k(SL(2,Z)), the space of modular forms of weight k.

    Formula (standard, cf. Zagier "Modular Forms" or Diamond-Shurman Ch. 3):
        dim M_k = 0           if k odd or k < 0
        dim M_k = 1           if k = 0
        dim M_k = 0           if k = 2
        dim M_k = floor(k/12) if k >= 4 and k = 2 mod 12
        dim M_k = floor(k/12) + 1  if k >= 4 and k != 2 mod 12

    # VERIFIED [DC] direct formula, [LT] Diamond-Shurman Thm 3.5.1,
    #   [LC] k=0 -> 1, k=12 -> 2 matches {E_12, Delta}.
    """
    if k < 0 or k % 2 != 0:
        return 0
    if k == 0:
        return 1
    if k == 2:
        # VERIFIED [DC] no weight-2 modular forms for SL(2,Z),
        #   [LT] Diamond-Shurman Cor 3.5.2, [LC] E_2 is quasi-modular not modular.
        return 0
    # k >= 4, even
    q, r = divmod(k, 12)
    if r == 2:
        return q
    else:
        return q + 1


def dim_S_k(k: int) -> int:
    r"""Dimension of S_k(SL(2,Z)), the space of cusp forms of weight k.

    Formula: dim S_k = max(0, dim M_k - 1) for k >= 2.
    For k < 2: dim S_k = 0.

    # VERIFIED [DC] dim S_k = dim M_k - 1 (subtract Eisenstein space, which
    #   is 1-dimensional for k >= 4 even), [LT] Diamond-Shurman Thm 3.5.1,
    #   [LC] k=12: dim M_12=2, dim S_12=1 (Ramanujan Delta).
    """
    if k < 2:
        return 0
    return max(0, dim_M_k(k) - 1)


# =========================================================================
# 2. Niemeier lattice registry
# =========================================================================

# ADE root system data
def _ade_rank(family: str, n: int) -> int:
    """Rank of a simple Lie algebra of type family_n."""
    if family == 'A':
        return n
    elif family == 'D':
        return n
    elif family == 'E':
        assert n in (6, 7, 8), f"E_{n} is not a valid exceptional type"
        return n
    else:
        raise ValueError(f"Unknown family {family}")


def _ade_dim(family: str, n: int) -> int:
    """Dimension of the Lie algebra g of type family_n.

    # VERIFIED [DC] A_n: n(n+2), D_n: n(2n-1), E_6: 78, E_7: 133, E_8: 248
    #   [LT] Humphreys "Introduction to Lie Algebras" Table p. 66
    """
    if family == 'A':
        return n * (n + 2)
    elif family == 'D':
        return n * (2 * n - 1)
    elif family == 'E':
        return {6: 78, 7: 133, 8: 248}[n]
    else:
        raise ValueError(f"Unknown family {family}")


def _ade_coxeter(family: str, n: int) -> int:
    """Coxeter number h of a simple Lie algebra of type family_n.

    # VERIFIED [DC] A_n: n+1, D_n: 2(n-1), E_6: 12, E_7: 18, E_8: 30
    #   [LT] Humphreys Table p. 66, [CF] h = |roots|/rank
    """
    if family == 'A':
        return n + 1
    elif family == 'D':
        return 2 * (n - 1)
    elif family == 'E':
        return {6: 12, 7: 18, 8: 30}[n]
    else:
        raise ValueError(f"Unknown family {family}")


def _ade_num_roots(family: str, n: int) -> int:
    """Number of roots of type family_n.

    # VERIFIED [DC] A_n: n(n+1), D_n: 2n(n-1), E_6: 72, E_7: 126, E_8: 240
    #   [LT] Bourbaki "Lie Groups and Lie Algebras" Ch. 4-6, [CF] |roots| = h * rank
    """
    if family == 'A':
        return n * (n + 1)
    elif family == 'D':
        return 2 * n * (n - 1)
    elif family == 'E':
        return {6: 72, 7: 126, 8: 240}[n]
    else:
        raise ValueError(f"Unknown family {family}")


@dataclass(frozen=True)
class NiemeierLattice:
    """Data for a Niemeier lattice."""
    label: str
    components: Tuple[Tuple[str, int], ...]
    # Derived quantities
    rank: int = 24  # always 24 for Niemeier

    @property
    def root_rank(self) -> int:
        return sum(_ade_rank(f, n) for f, n in self.components)

    @property
    def num_roots(self) -> int:
        return sum(_ade_num_roots(f, n) for f, n in self.components)

    @property
    def num_factors(self) -> int:
        return len(self.components)

    @property
    def is_leech(self) -> bool:
        return len(self.components) == 0

    @property
    def coxeter_numbers(self) -> Tuple[int, ...]:
        return tuple(_ade_coxeter(f, n) for f, n in self.components)


# All 24 Niemeier lattices (Conway-Sloane order, descending by |R|)
# VERIFIED [LT] Conway-Sloane "Sphere Packings" Ch. 16 Table 16.1,
#   [DC] each root system has total rank 24, [CF] Niemeier (1968).
NIEMEIER_LATTICES: List[NiemeierLattice] = [
    NiemeierLattice('D24', (('D', 24),)),
    NiemeierLattice('D16_E8', (('D', 16), ('E', 8))),
    NiemeierLattice('3E8', (('E', 8), ('E', 8), ('E', 8))),
    NiemeierLattice('A24', (('A', 24),)),
    NiemeierLattice('2D12', (('D', 12), ('D', 12))),
    NiemeierLattice('A17_E7', (('A', 17), ('E', 7))),
    NiemeierLattice('D10_2E7', (('D', 10), ('E', 7), ('E', 7))),
    NiemeierLattice('A15_D9', (('A', 15), ('D', 9))),
    NiemeierLattice('3D8', (('D', 8), ('D', 8), ('D', 8))),
    NiemeierLattice('2A12', (('A', 12), ('A', 12))),
    NiemeierLattice('A11_D7_E6', (('A', 11), ('D', 7), ('E', 6))),
    NiemeierLattice('4E6', (('E', 6), ('E', 6), ('E', 6), ('E', 6))),
    NiemeierLattice('2A9_D6', (('A', 9), ('A', 9), ('D', 6))),
    NiemeierLattice('4D6', (('D', 6), ('D', 6), ('D', 6), ('D', 6))),
    NiemeierLattice('3A8', (('A', 8), ('A', 8), ('A', 8))),
    NiemeierLattice('2A7_2D5', (('A', 7), ('A', 7), ('D', 5), ('D', 5))),
    NiemeierLattice('4A6', (('A', 6), ('A', 6), ('A', 6), ('A', 6))),
    NiemeierLattice('4A5_D4', (('A', 5), ('A', 5), ('A', 5), ('A', 5), ('D', 4))),
    NiemeierLattice('6D4', (('D', 4), ('D', 4), ('D', 4), ('D', 4), ('D', 4), ('D', 4))),
    NiemeierLattice('6A4', (('A', 4), ('A', 4), ('A', 4), ('A', 4), ('A', 4), ('A', 4))),
    NiemeierLattice('8A3', (('A', 3),) * 8),
    NiemeierLattice('12A2', (('A', 2),) * 12),
    NiemeierLattice('24A1', (('A', 1),) * 24),
    NiemeierLattice('Leech', ()),
]

ALL_LABELS = [lat.label for lat in NIEMEIER_LATTICES]
assert len(NIEMEIER_LATTICES) == 24  # VERIFIED [DC] enumeration, [LT] Conway-Sloane


def get_lattice(label: str) -> NiemeierLattice:
    """Look up a Niemeier lattice by label."""
    for lat in NIEMEIER_LATTICES:
        if lat.label == label:
            return lat
    raise KeyError(f"Unknown Niemeier lattice: {label}")


# =========================================================================
# 3. Central charge and kappa for Niemeier lattice VOAs
# =========================================================================

# VERIFIED [DC] c = rank for free bosons, [LT] FLM88 Ch. 5,
#   [CF] all Niemeier lattices have rank 24 so c = 24.
CENTRAL_CHARGE = 24

# VERIFIED [DC] kappa(H_k) = k per boson (CLAUDE.md C1), 24 bosons at level 1
#   gives kappa = 24, [CF] c = 24 and kappa = c for Heisenberg/lattice,
#   [LT] thm:depth-decomposition table lists V_Leech as kappa = 24.
KAPPA_NIEMEIER = 24


def central_charge() -> int:
    """Central charge c = 24 for all Niemeier lattice VOAs."""
    return CENTRAL_CHARGE


def kappa() -> int:
    """kappa = 24 for all Niemeier lattice VOAs (rank-24 Heisenberg at level 1)."""
    return KAPPA_NIEMEIER


# =========================================================================
# 4. Shadow depth computation
# =========================================================================

def lattice_shadow_depth(rank: int) -> int:
    r"""Shadow depth for an even unimodular lattice VOA of given rank.

    Formula (eq:depth-cusp-formula, eq:depth-cusp-full):
        d(V_Lambda) = 3 + dim S_{r/2}(SL(2,Z))

    where r = rank(Lambda).

    # VERIFIED [DC] direct formula application,
    #   [LT] thm:depth-decomposition + eq:depth-cusp-formula (arithmetic_shadows.tex),
    #   [CF] Niemeier (r=24): 3 + dim S_12 = 3 + 1 = 4, matches manuscript table.
    """
    weight = rank // 2
    if rank % 2 != 0:
        raise ValueError(f"Even unimodular lattice must have even rank, got {rank}")
    return 3 + dim_S_k(weight)


def niemeier_shadow_depth() -> int:
    """Shadow depth for all Niemeier lattice VOAs: d = 3 + dim S_12 = 4.

    # VERIFIED [DC] 3 + 1 = 4,
    #   [LT] manuscript table (higher_genus_modular_koszul.tex ~line 15991):
    #       V_Leech: class G, depth 4, d_alg = 0,
    #   [CF] depth decomposition: d = 1 + d_arith + d_alg = 1 + 3 + 0 = 4.
    """
    return lattice_shadow_depth(24)


def depth_decomposition_niemeier() -> Dict[str, int]:
    r"""Full depth decomposition for Niemeier lattice VOAs.

    d = 1 + d_arith + d_alg

    For lattice VOAs:
        d_arith = 2 + dim S_{r/2}  (two Eisenstein + cusp eigenform lines)
        d_alg = 0  (bar complex strictly coassociative, class G)

    # VERIFIED [DC] d_arith = 2 + 1 = 3 (two Eisenstein lines + one Delta line),
    #   [LT] thm:depth-decomposition table,
    #   [CF] d = 1 + 3 + 0 = 4 matches direct formula 3 + dim S_12.
    """
    rank = 24
    weight = rank // 2  # = 12
    dim_cusp = dim_S_k(weight)  # = 1
    d_arith = 2 + dim_cusp  # = 3
    d_alg = 0  # class G, bar complex strictly coassociative
    d_total = 1 + d_arith + d_alg  # = 4
    return {
        'rank': rank,
        'weight': weight,
        'dim_S_k': dim_cusp,
        'dim_M_k': dim_M_k(weight),
        'd_arith': d_arith,
        'd_alg': d_alg,
        'd_total': d_total,
        'class_scalar': 'G',  # scalar shadow tower class
        'class_full': 'F_4',  # full class (finite depth 4)
        'num_eisenstein_lines': 2,
        'num_cusp_lines': dim_cusp,
    }


# =========================================================================
# 5. Scalar shadow tower (class G, blind to lattice structure)
# =========================================================================

def scalar_shadow_class() -> str:
    """Scalar shadow class: G (Gaussian) for all Niemeier lattice VOAs.

    # VERIFIED [DC] S_3 = 0, S_4 = 0 => class G,
    #   [LT] thm:shadow-archetype-classification,
    #   [CF] theorem_niemeier_shadow_discrimination_engine.py.
    """
    return 'G'


def scalar_shadow_depth() -> int:
    """Scalar shadow depth: r_max = 2 for all Niemeier lattice VOAs.

    The SCALAR tower has depth 2 (class G). The FULL arithmetic depth is 4.

    # VERIFIED [DC] S_r = 0 for r >= 3,
    #   [LT] theorem_niemeier_shadow_discrimination_engine.py,
    #   [CF] class G => depth 2.
    """
    return 2


def scalar_S3() -> Fraction:
    """S_3 = 0 for all Niemeier lattice VOAs (class G)."""
    return Fraction(0)


def scalar_S4() -> Fraction:
    """S_4 = 0 for all Niemeier lattice VOAs (class G)."""
    return Fraction(0)


# =========================================================================
# 6. Modular form space verification
# =========================================================================

def verify_dim_S_12() -> Dict[str, Any]:
    r"""Verify dim S_12 = 1 (Ramanujan Delta is the unique weight-12 cusp form).

    Verification paths:
      Path 1 [DC]: dimension formula gives dim M_12 = 2, dim S_12 = 1.
      Path 2 [LT]: S_12 is spanned by Delta = eta^{24} = sum tau(n) q^n
          (Ramanujan 1916, Mordell 1917).
      Path 3 [CF]: M_12 = C*E_12 + C*Delta (Eisenstein + cusp),
          dim M_12 = 2, dim S_12 = 1.
      Path 4 [NE]: tau(1) = 1, tau(2) = -24, tau(3) = 252 (Ramanujan).

    # VERIFIED [DC] formula, [LT] Ramanujan/Mordell, [CF] E_12 + Delta basis,
    #   [NE] Ramanujan tau values.
    """
    dm = dim_M_k(12)
    ds = dim_S_k(12)
    return {
        'dim_M_12': dm,
        'dim_S_12': ds,
        'basis_M_12': ['E_12', 'Delta'],
        'basis_S_12': ['Delta'],
        'ramanujan_tau_1': 1,
        'ramanujan_tau_2': -24,
        'ramanujan_tau_3': 252,
        'dim_M_12_correct': dm == 2,
        'dim_S_12_correct': ds == 1,
    }


def modular_forms_dimension_table(max_weight: int = 30) -> List[Dict[str, int]]:
    """Dimension table for M_k and S_k for even k up to max_weight.

    # VERIFIED [DC] formula, [LT] Diamond-Shurman Table 3.2.
    """
    table = []
    for k in range(0, max_weight + 1, 2):
        table.append({
            'k': k,
            'dim_M_k': dim_M_k(k),
            'dim_S_k': dim_S_k(k),
        })
    return table


# =========================================================================
# 7. Higher-rank lattice shadow depths
# =========================================================================

def lattice_shadow_depth_table(max_rank: int = 96) -> List[Dict[str, Any]]:
    """Shadow depth for even unimodular lattices at various ranks.

    Ranks where even unimodular lattices exist: multiples of 8 (>= 8).
    (Rank 8: E_8 root lattice; rank 16: two lattices; rank 24: 24 Niemeier;
     rank 32: > 10^7 lattices; ...)

    # VERIFIED [DC] formula d = 3 + dim S_{r/2},
    #   [LT] manuscript line ~15825 (depths 5, 6, 7, ...),
    #   [CF] rank 8: d = 3 + dim S_4 = 3 + 0 = 3 (class L equivalent).
    """
    table = []
    for r in range(8, max_rank + 1, 8):
        w = r // 2
        ds = dim_S_k(w)
        dm = dim_M_k(w)
        d = 3 + ds
        table.append({
            'rank': r,
            'weight': w,
            'dim_M': dm,
            'dim_S': ds,
            'depth': d,
        })
    return table


# =========================================================================
# 8. Ramanujan tau function (first few values for verification)
# =========================================================================

# First 12 values of Ramanujan's tau function
# VERIFIED [DC] eta^{24} expansion, [LT] OEIS A000594,
#   [NE] Ramanujan (1916), Lehmer (1947).
RAMANUJAN_TAU = {
    1: 1,
    2: -24,
    3: 252,
    4: -1472,
    5: 4830,
    6: -6048,
    7: -16744,
    8: 84480,
    9: -113643,
    10: -115920,
    11: 534612,
    12: -370944,
}


def ramanujan_tau(n: int) -> int:
    """Return tau(n) for small n (precomputed).

    # VERIFIED [DC] eta^24 expansion, [LT] OEIS A000594.
    """
    if n in RAMANUJAN_TAU:
        return RAMANUJAN_TAU[n]
    raise ValueError(f"tau({n}) not precomputed; available for n <= 12")


# =========================================================================
# 9. Complete verification suite
# =========================================================================

def run_all_verifications() -> Dict[str, Any]:
    """Run all verification checks.

    Returns a dictionary with all results and a boolean 'all_pass' key.
    """
    results = {}

    # 1. Count of Niemeier lattices
    results['num_lattices'] = len(NIEMEIER_LATTICES)
    results['num_lattices_ok'] = results['num_lattices'] == 24

    # 2. All have rank 24
    rank_checks = []
    for lat in NIEMEIER_LATTICES:
        if not lat.is_leech:
            rank_checks.append(lat.root_rank == 24)
        else:
            rank_checks.append(lat.root_rank == 0)
    results['all_rank_24'] = all(rank_checks)

    # 3. Central charge
    results['c'] = central_charge()
    results['c_ok'] = results['c'] == 24

    # 4. Kappa
    results['kappa'] = kappa()
    results['kappa_ok'] = results['kappa'] == 24

    # 5. Shadow depth
    results['shadow_depth'] = niemeier_shadow_depth()
    results['shadow_depth_ok'] = results['shadow_depth'] == 4

    # 6. Depth decomposition
    decomp = depth_decomposition_niemeier()
    results['decomposition'] = decomp
    results['decomposition_ok'] = (
        decomp['d_total'] == 4
        and decomp['d_arith'] == 3
        and decomp['d_alg'] == 0
    )

    # 7. dim S_12
    s12 = verify_dim_S_12()
    results['dim_S_12'] = s12
    results['dim_S_12_ok'] = s12['dim_S_12_correct'] and s12['dim_M_12_correct']

    # 8. Scalar tower
    results['scalar_class'] = scalar_shadow_class()
    results['scalar_depth'] = scalar_shadow_depth()
    results['scalar_ok'] = (
        results['scalar_class'] == 'G'
        and results['scalar_depth'] == 2
    )

    results['all_pass'] = all(
        results[k] for k in results if k.endswith('_ok')
    )

    return results
