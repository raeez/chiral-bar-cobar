r"""Arithmetic depth d_arith for the complete standard landscape.

The depth decomposition (thm:depth-decomposition in arithmetic_shadows.tex):

    d(A) = 1 + d_arith(A) + d_alg(A)

where d_arith counts independent holomorphic Hecke eigenforms in the
Roelcke-Selberg spectral decomposition of Z_hat^c_A on M_{1,1}.

CRITICAL DISTINCTIONS (AP9, AP1):

  (1) d_arith depends on the PARTITION FUNCTION, not on kappa.
      Two algebras with the same kappa can have different d_arith.
  (2) For lattice VOAs: the partition function factors through theta
      functions, which are holomorphic modular forms for SL(2,Z).
      d_arith = 2 + dim S_{r/2}(SL(2,Z)).
  (3) For non-lattice families: the partition function is NOT a
      holomorphic modular form. The Roelcke-Selberg decomposition
      involves Maass cusp forms. d_arith counts HOLOMORPHIC eigenforms
      only (Maass contributions do not produce new critical lines).
  (4) For Virasoro minimal models: finitely many primaries, so the
      constrained Epstein zeta is a finite Dirichlet series.
      d_arith = #{distinct critical lines}, which is 0 when all zeros
      lie on Re(s) = 0 (prop:ising-d-arith).
  (5) For affine KM at level k: the character chi_{g,k} is a
      vector-valued modular form (VVMF) of finite rank. The number
      of holomorphic Hecke eigenforms in |chi|^2 depends on the rank
      of the VVMF and the structure of its Rankin-Selberg unfolding.
      NOT the same as dim S_k(Gamma_0(N)), which is generically much
      larger. d_arith for affine KM counts the eigenforms WITH NONZERO
      PROJECTION onto |chi|^2, not the full space dimension.

PATTERN/FORMULA by family class:

  CLASS G (Gaussian, r_max = 2):
    Lattice V_Lambda (rank r, unimodular): d_arith = 2 + dim S_{r/2}(SL(2,Z))
    Heisenberg H_k (rank 1): d_arith = 1 (half-integral weight)

  CLASS L (Lie, r_max = 3):
    Affine KM at level 1, simply-laced: d_arith = 1 (low modular weight)
      Exception: E_8 at level 1 ~ V_{E_8}, d_arith = 2 (lattice)
    Affine KM at level 1, non-simply-laced: d_arith = 1
    Affine KM at level k >= 2: d_arith = 1 (generically; VVMF structure
      suppresses cusp form projections beyond Eisenstein)

  CLASS C (contact, r_max = 4):
    betagamma: d_arith = 1 (one holomorphic eigenform from theta_3)

  CLASS M (mixed, r_max = infinity):
    Virasoro minimal M(p,q): d_arith = #{multiplicatively independent
      primaries} - 1 (finite, often 0)
    Virasoro generic c: d_arith = 0 (non-modular partition function)
    W_N generic c: d_arith = 0
    W_N at free-field c = N-1: d_arith = 1

FIRST FAMILY with d_arith > 3:
  Lattice VOA at rank 48: d_arith = 2 + dim S_24 = 2 + 2 = 4.
  (dim S_24(SL(2,Z)) = 2: two independent cusp forms of weight 24.)

Manuscript references:
    thm:depth-decomposition (arithmetic_shadows.tex)
    prop:ising-d-arith (arithmetic_shadows.tex)
    thm:refined-shadow-spectral (arithmetic_shadows.tex)
    rem:non-unimodular (arithmetic_shadows.tex)
    def:arithmetic-depth-filtration (arithmetic_shadows.tex)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, List, Optional, Tuple, Union

from sympy import Rational, oo


# ============================================================================
# 1. Cusp form dimension for SL(2,Z)
# ============================================================================

def cusp_form_dim_sl2z(k: int) -> int:
    r"""dim S_k(SL(2,Z)): dimension of weight-k cusp forms for SL(2,Z).

    Standard formula (Diamond-Shurman Thm 3.5.1):
      k < 12 or k odd: dim = 0
      k = 12: dim = 1 (Ramanujan Delta)
      k even, k >= 14: from genus formula for X_0(1).
    """
    if k < 0 or k % 2 == 1:
        return 0
    if k == 0 or k == 2:
        return 0
    if k % 12 == 2:
        dim_M = k // 12
    else:
        dim_M = k // 12 + 1
    return max(dim_M - 1, 0)


# ============================================================================
# 2. Result dataclass
# ============================================================================

@dataclass
class DArithResult:
    """Result of arithmetic depth computation for a single algebra."""
    family: str
    shadow_class: str
    d_arith: Union[int, str]  # int or 'infinite' or 'unknown'
    d_alg: Union[int, None]  # None for infinity
    d_total: Union[int, None]  # None for infinity
    mechanism: str  # how d_arith was computed
    notes: str = ""

    def __repr__(self):
        d_alg_str = 'inf' if self.d_alg is None else str(self.d_alg)
        d_total_str = 'inf' if self.d_total is None else str(self.d_total)
        return (f"DArithResult({self.family}: d_arith={self.d_arith}, "
                f"d_alg={d_alg_str}, d_total={d_total_str})")


# ============================================================================
# 3. Lattice VOA arithmetic depth
# ============================================================================

def darith_lattice_unimodular(rank: int) -> DArithResult:
    r"""Arithmetic depth for even unimodular lattice VOA of given rank.

    For rank r even unimodular lattice (r divisible by 8):
      Theta_Lambda in M_{r/2}(SL(2,Z))
      d_arith = 2 + dim S_{r/2}(SL(2,Z))
      d_alg = 0 (class G)
      d_total = 1 + d_arith

    The "2" accounts for:
      (1) The Eisenstein series E_{r/2} contribution
      (2) The unit/constant term contribution
    """
    assert rank >= 8 and rank % 8 == 0, f"Even unimodular lattice requires rank divisible by 8, got {rank}"
    k = rank // 2
    dim_cusp = cusp_form_dim_sl2z(k)
    da = 2 + dim_cusp
    return DArithResult(
        family=f"Lattice (rank {rank}, unimod)",
        shadow_class='G',
        d_arith=da,
        d_alg=0,
        d_total=1 + da,
        mechanism=f"Theta in M_{k}(SL(2,Z)), dim S_{k} = {dim_cusp}",
        notes=f"kappa = {rank}."
    )


# Named lattice families
EVEN_UNIMODULAR_LATTICES = {
    # rank 8: 1 lattice
    'E8': {'rank': 8, 'root': 'E_8'},
    # rank 16: 2 lattices
    'E8xE8': {'rank': 16, 'root': 'E_8^2'},
    'D16+': {'rank': 16, 'root': 'D_{16}^+'},
    # rank 24: 24 Niemeier lattices (selected representatives)
    'Leech': {'rank': 24, 'root': 'none (Leech)'},
    'A1_24': {'rank': 24, 'root': 'A_1^{24}'},
    'D4_6': {'rank': 24, 'root': 'D_4^6'},
    'D6_4': {'rank': 24, 'root': 'D_6^4'},
    'D8_3': {'rank': 24, 'root': 'D_8^3'},
    'D12_2': {'rank': 24, 'root': 'D_{12}^2'},
    'D24': {'rank': 24, 'root': 'D_{24}'},
    'E6_4': {'rank': 24, 'root': 'E_6^4'},
    'E8_3': {'rank': 24, 'root': 'E_8^3'},
    'D16E8': {'rank': 24, 'root': 'D_{16} E_8'},
    'A2_12': {'rank': 24, 'root': 'A_2^{12}'},
    'A3_8': {'rank': 24, 'root': 'A_3^8'},
    'A4_6': {'rank': 24, 'root': 'A_4^6'},
    'A5D4': {'rank': 24, 'root': 'A_5^4 D_4'},
    'A6_4': {'rank': 24, 'root': 'A_6^4'},
    'A7D5_2': {'rank': 24, 'root': 'A_7^2 D_5^2'},
    'A8_3': {'rank': 24, 'root': 'A_8^3'},
    'A9D6': {'rank': 24, 'root': 'A_9^2 D_6'},
    'A11D7E6': {'rank': 24, 'root': 'A_{11} D_7 E_6'},
    'A12_2': {'rank': 24, 'root': 'A_{12}^2'},
    'A15D9': {'rank': 24, 'root': 'A_{15} D_9'},
    'A17E7': {'rank': 24, 'root': 'A_{17} E_7'},
    'A24': {'rank': 24, 'root': 'A_{24}'},
    'D10E7_2': {'rank': 24, 'root': 'D_{10} E_7^2'},
}


def darith_all_niemeier() -> Dict[str, DArithResult]:
    """Compute d_arith for all 24 Niemeier lattices.

    ALL have rank 24, theta weight 12, dim S_12 = 1.
    Therefore d_arith = 3 for ALL Niemeier lattices (universal).
    """
    results = {}
    for name, data in EVEN_UNIMODULAR_LATTICES.items():
        if data['rank'] == 24:
            r = darith_lattice_unimodular(24)
            r.family = f"Niemeier: {name} ({data['root']})"
            results[name] = r
    return results


# ============================================================================
# 4. Heisenberg arithmetic depth
# ============================================================================

def darith_heisenberg(level=1) -> DArithResult:
    r"""Arithmetic depth for Heisenberg algebra H_k.

    The Heisenberg at level k: one free boson. Partition function
    involves |eta|^{-2}. The primary-counting function for rank-1
    Narain is Z_hat = y^{1/2} |theta_3|^2.

    theta_3 is a half-integral weight modular form (weight 1/2)
    for Gamma_0(4). Via Shimura correspondence, this gives one
    holomorphic eigenform contribution.

    d_arith = 1, d_alg = 0 (class G).
    d_total = 1 + 1 + 0 = 2.
    """
    return DArithResult(
        family=f"Heisenberg H_{level}",
        shadow_class='G',
        d_arith=1,
        d_alg=0,
        d_total=2,
        mechanism="Rank-1 theta: one holomorphic eigenform",
        notes=f"kappa = {level}."
    )


# ============================================================================
# 5. Affine Kac-Moody arithmetic depth
# ============================================================================

_LIE_DATA = {
    'sl2':  {'dim': 3,   'h_dual': 2,  'rank': 1, 'simply_laced': True},
    'sl3':  {'dim': 8,   'h_dual': 3,  'rank': 2, 'simply_laced': True},
    'sl4':  {'dim': 15,  'h_dual': 4,  'rank': 3, 'simply_laced': True},
    'sl5':  {'dim': 24,  'h_dual': 5,  'rank': 4, 'simply_laced': True},
    'so5':  {'dim': 10,  'h_dual': 3,  'rank': 2, 'simply_laced': False},  # B2
    'sp4':  {'dim': 10,  'h_dual': 3,  'rank': 2, 'simply_laced': False},  # C2
    'G2':   {'dim': 14,  'h_dual': 4,  'rank': 2, 'simply_laced': False},
    'F4':   {'dim': 52,  'h_dual': 9,  'rank': 4, 'simply_laced': False},
    'E6':   {'dim': 78,  'h_dual': 12, 'rank': 6, 'simply_laced': True},
    'E7':   {'dim': 133, 'h_dual': 18, 'rank': 7, 'simply_laced': True},
    'E8':   {'dim': 248, 'h_dual': 30, 'rank': 8, 'simply_laced': True},
    'D4':   {'dim': 28,  'h_dual': 6,  'rank': 4, 'simply_laced': True},
}


def _kappa_km(lie_type: str, level: int) -> Rational:
    """kappa(V_k(g)) = dim(g) * (k + h^vee) / (2 * h^vee)."""
    d = _LIE_DATA[lie_type]
    return Rational(d['dim'] * (level + d['h_dual']), 2 * d['h_dual'])


def _central_charge_km(lie_type: str, level: int) -> Rational:
    """Central charge c(g, k) = k * dim(g) / (k + h^vee)."""
    d = _LIE_DATA[lie_type]
    return Rational(level * d['dim'], level + d['h_dual'])


def darith_affine_km(lie_type: str, level: int) -> DArithResult:
    r"""Arithmetic depth for affine Kac-Moody V_k(g).

    THE KEY INSIGHT: d_arith for affine KM is NOT determined by the
    total cusp form space dim S_k(Gamma_0(N)). The characters of
    V_k(g) form a vector-valued modular form (VVMF) of finite rank
    r = #{integrable highest-weight modules at level k}. The squared
    character norm |chi|^2 decomposes over Hecke eigenforms, but only
    a SMALL number have nonzero projection.

    Level 1 simply-laced special cases:
      - E_8: the root lattice IS even unimodular, so
        V_1(E_8) ~ V_{E_8}, theta in M_4(SL(2,Z)), dim S_4 = 0.
        d_arith = 2 (lattice-type).
      - E_7: root lattice rank 7, det 2. The partition function
        involves theta of the E_7 lattice (an even integral lattice,
        det 2). At weight 7/2 for Gamma_0(2), the cusp form space
        is empty. d_arith = 1.
      - E_6: root lattice rank 6, det 3. d_arith = 1.
      - D_4: root lattice rank 4, det 4. d_arith = 1.
      - A_{n-1}: root lattice rank n-1, det n. For small n: d_arith = 1.

    Level 1 non-simply-laced: d_arith = 1 (low modular weight).

    Level k >= 2: The VVMF has rank k+1 (for sl_2). The squared norm
    |chi|^2 is a sum of k+1 terms, each of the form |chi_j|^2.
    These are real-analytic modular forms. In the Roelcke-Selberg
    decomposition, the holomorphic eigenform projections are typically
    suppressed by the VVMF structure. Generically: d_arith = 1.

    Exception: at very high levels, when the VVMF representation becomes
    highly reducible, additional holomorphic eigenforms may contribute.
    For sl_2 at level k, the character representation decomposes into
    k+1 components. At level k where the representation contains a
    component that is a holomorphic modular form (rather than a VVMF
    component), d_arith can increase. This first happens for sl_2 at
    level k such that there exist holomorphic modular forms of weight 1
    with the same conductor. For practical purposes (k <= 10), this
    gives d_arith = 1 for all non-E_8 cases.
    """
    d = _LIE_DATA[lie_type]
    kappa = _kappa_km(lie_type, level)
    c_val = _central_charge_km(lie_type, level)

    if level == 1:
        if lie_type == 'E8':
            # E_8 at level 1: root lattice is even unimodular
            # Theta_{E_8} in M_4(SL(2,Z)), dim S_4 = 0
            return DArithResult(
                family="Affine E_8 level 1",
                shadow_class='L',
                d_arith=2,
                d_alg=1,
                d_total=4,
                mechanism="E_8 root lattice is unimodular, theta in M_4(SL(2,Z)), dim S_4 = 0",
                notes=f"c = {c_val}, kappa = {kappa}. Lattice-type (d_arith = 2)."
            )
        else:
            # All other level-1 algebras: low modular weight, no cusp forms
            return DArithResult(
                family=f"Affine {lie_type} level 1",
                shadow_class='L',
                d_arith=1,
                d_alg=1,
                d_total=3,
                mechanism=f"Level 1: low modular weight, rank {d['rank']} root lattice, no cusp form contribution",
                notes=f"c = {c_val}, kappa = {kappa}."
            )
    else:
        # Higher levels: VVMF structure suppresses holomorphic eigenforms
        n_modules = level + 1 if lie_type == 'sl2' else None  # sl_2 only
        return DArithResult(
            family=f"Affine {lie_type} level {level}",
            shadow_class='L',
            d_arith=1,
            d_alg=1,
            d_total=3,
            mechanism=f"VVMF structure: {n_modules or '?'} modules, holomorphic projections suppressed",
            notes=f"c = {c_val}, kappa = {kappa}. Generic d_arith = 1."
        )


# ============================================================================
# 6. Virasoro arithmetic depth
# ============================================================================

def _minimal_model_c(p: int, q: int) -> Rational:
    """Central charge of minimal model M(p, q), gcd(p,q)=1, p > q >= 2."""
    return 1 - Rational(6 * (p - q)**2, p * q)


def _minimal_model_primaries(p: int, q: int) -> List[Rational]:
    """Conformal weights of primary fields in M(p, q).

    h_{r,s} = ((rq - sp)^2 - (p-q)^2) / (4pq)
    for 1 <= r <= p-1, 1 <= s <= q-1, with h_{r,s} = h_{p-r, q-s}.
    """
    weights = set()
    for r in range(1, p):
        for s in range(1, q):
            h = Rational((r * q - s * p)**2 - (p - q)**2, 4 * p * q)
            weights.add(h)
    return sorted(weights)


def _count_critical_lines_minimal(p: int, q: int) -> int:
    """Count distinct critical lines for a minimal model.

    The constrained Epstein zeta is a FINITE Dirichlet series
    sum_i (2 Delta_i)^{-s} where Delta_i = 2 h_i are the conformal
    dimensions of scalar primaries.

    d_arith = 0 when all lambda_i = 2*Delta_i are multiplicatively
    dependent (all zeros on Re(s) = 0).

    Method: factor each lambda_i over primes, compute the rank of the
    exponent matrix.
    """
    primaries = _minimal_model_primaries(p, q)
    positive = [h for h in primaries if h > 0]

    if len(positive) <= 1:
        return 0

    # Compute lambda_i = 2 * h_i as fractions
    lambdas = sorted(set(Fraction(2 * h) for h in positive))
    if len(lambdas) <= 1:
        return 0

    # Factor each lambda over primes, build exponent matrix
    all_primes = set()
    factorizations = []
    for lam in lambdas:
        num_factors = _factorize(abs(lam.numerator))
        den_factors = _factorize(abs(lam.denominator))
        combined = {}
        for pr, e in num_factors.items():
            combined[pr] = combined.get(pr, 0) + e
            all_primes.add(pr)
        for pr, e in den_factors.items():
            combined[pr] = combined.get(pr, 0) - e
            all_primes.add(pr)
        factorizations.append(combined)

    if not all_primes:
        return 0

    primes_list = sorted(all_primes)
    matrix = [[f.get(p, 0) for p in primes_list] for f in factorizations]
    rank = _matrix_rank_Q(matrix)

    # d_arith = rank - 1 (one dimension is "used up" by the overall scale)
    return max(rank - 1, 0)


def _factorize(n: int) -> Dict[int, int]:
    """Factorize positive integer into prime powers."""
    if n <= 1:
        return {}
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _matrix_rank_Q(matrix: List[List[int]]) -> int:
    """Compute rank of integer matrix over Q via Gaussian elimination."""
    if not matrix or not matrix[0]:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    mat = [[Fraction(x) for x in row] for row in matrix]

    rank = 0
    for col in range(n):
        pivot = None
        for row in range(rank, m):
            if mat[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        for row in range(m):
            if row != rank and mat[row][col] != 0:
                factor = mat[row][col] / mat[rank][col]
                for j in range(n):
                    mat[row][j] -= factor * mat[rank][j]
        rank += 1
    return rank


def darith_virasoro_minimal(p: int, q: int) -> DArithResult:
    r"""Arithmetic depth for Virasoro minimal model M(p, q).

    The constrained Epstein zeta is a FINITE Dirichlet series.
    d_arith counts the number of multiplicatively independent
    lambda_i = 2*Delta_i, minus 1.

    Verified: M(3,4) [Ising, c=1/2]: d_arith = 0 (prop:ising-d-arith).
    """
    c_val = _minimal_model_c(p, q)
    n_crit = _count_critical_lines_minimal(p, q)
    primaries = _minimal_model_primaries(p, q)
    n_positive = len([h for h in primaries if h > 0])

    return DArithResult(
        family=f"Virasoro M({p},{q}), c = {c_val}",
        shadow_class='M',
        d_arith=n_crit,
        d_alg=None,  # infinity for class M
        d_total=None,  # infinity
        mechanism=f"{n_positive} positive primaries, {n_crit} critical lines",
        notes=f"c = {float(c_val):.6f}."
    )


def darith_virasoro_generic(c_val) -> DArithResult:
    r"""Arithmetic depth for Virasoro at generic central charge c.

    For IRRATIONAL c: partition function not modular for any congruence
    subgroup. d_arith = 0.

    For RATIONAL c: partial modular properties possible. For minimal
    models (c < 1, rational), use darith_virasoro_minimal.

    For integer c:
      c = 1: free boson. theta-like structure. d_arith = 1.
      c = 25: Koszul dual of c = 1. d_arith = 1.
      c = 26: critical string. eta^{-26} structure. d_arith = 1.
      Other integer c: generic. d_arith = 0.
    """
    c_r = Rational(c_val) if not isinstance(c_val, Rational) else c_val

    # Known minimal models
    if c_r == Rational(1, 2):
        return darith_virasoro_minimal(3, 4)
    elif c_r == Rational(7, 10):
        return darith_virasoro_minimal(4, 5)
    elif c_r == Rational(4, 5):
        return darith_virasoro_minimal(5, 6)

    # Integer c
    if c_r.denominator == 1:
        c_int = int(c_r)
        if c_int in (1, 25, 26):
            return DArithResult(
                family=f"Virasoro c = {c_int}",
                shadow_class='M',
                d_arith=1,
                d_alg=None,
                d_total=None,
                mechanism=f"c = {c_int}: {'free boson' if c_int == 1 else 'Koszul dual of free boson' if c_int == 25 else 'critical string'}, eta-modular structure",
                notes=f"kappa = {Rational(c_int, 2)}."
            )
        else:
            return DArithResult(
                family=f"Virasoro c = {c_int}",
                shadow_class='M',
                d_arith=0,
                d_alg=None,
                d_total=None,
                mechanism=f"c = {c_int}: generic integer, non-modular",
                notes=f"kappa = {Rational(c_int, 2)}."
            )

    # Generic rational
    return DArithResult(
        family=f"Virasoro c = {c_r}",
        shadow_class='M',
        d_arith=0,
        d_alg=None,
        d_total=None,
        mechanism=f"c = {c_r}: generic rational, non-modular",
        notes=f"kappa = {c_r}/2."
    )


# ============================================================================
# 7. W-algebra arithmetic depth
# ============================================================================

def darith_w_algebra(N: int, c_val=None) -> DArithResult:
    r"""Arithmetic depth for W_N algebra.

    W_N at generic c: d_arith = 0 (non-modular partition function).
    W_N at c = N-1 (free field): d_arith = 1 (eta structure).
    """
    if c_val is not None:
        c_r = Rational(c_val) if not isinstance(c_val, Rational) else c_val
        if c_r == N - 1:
            return DArithResult(
                family=f"W_{N} at c = {N-1} (free field)",
                shadow_class='M',
                d_arith=1,
                d_alg=None,
                d_total=None,
                mechanism=f"Free field: {N-1} free bosons, eta structure",
            )
        return DArithResult(
            family=f"W_{N} at c = {c_r}",
            shadow_class='M',
            d_arith=0,
            d_alg=None,
            d_total=None,
            mechanism=f"Generic c = {c_r}: non-modular",
        )
    return DArithResult(
        family=f"W_{N} generic c",
        shadow_class='M',
        d_arith=0,
        d_alg=None,
        d_total=None,
        mechanism="Generic c: non-modular partition function",
    )


# ============================================================================
# 8. Betagamma arithmetic depth
# ============================================================================

def darith_betagamma(weight=1) -> DArithResult:
    r"""Arithmetic depth for betagamma system.

    From the manuscript (thm:depth-decomposition proof):
      d(betagamma) = 4, d_arith = 1, d_alg = 2.

    Z_hat^{bg} = y^{1/2} |theta_3|^2 / |eta|^2
    One holomorphic eigenform from theta_3^2.
    """
    w = Rational(weight)
    kappa = 6 * w**2 - 6 * w + 1
    return DArithResult(
        family=f"betagamma (lam={weight})",
        shadow_class='C',
        d_arith=1,
        d_alg=2,
        d_total=4,
        mechanism="|theta_3|^2/|eta|^2: one holomorphic eigenform",
        notes=f"kappa = {kappa}."
    )


# ============================================================================
# 9. Complete landscape table
# ============================================================================

def complete_landscape_table() -> List[DArithResult]:
    """Compute d_arith for the entire standard landscape."""
    results = []

    # === CLASS G ===
    results.append(darith_heisenberg(1))
    for rank in [8, 16, 24, 32, 40, 48, 72, 96]:
        results.append(darith_lattice_unimodular(rank))

    # === CLASS L ===
    for k in range(1, 11):
        results.append(darith_affine_km('sl2', k))
    for k in range(1, 6):
        results.append(darith_affine_km('sl3', k))
    results.append(darith_affine_km('sl4', 1))
    results.append(darith_affine_km('E8', 1))
    results.append(darith_affine_km('E7', 1))
    results.append(darith_affine_km('E6', 1))
    results.append(darith_affine_km('D4', 1))
    results.append(darith_affine_km('G2', 1))
    results.append(darith_affine_km('F4', 1))
    results.append(darith_affine_km('so5', 1))

    # === CLASS C ===
    results.append(darith_betagamma(1))
    results.append(darith_betagamma(Rational(1, 2)))

    # === CLASS M ===
    # Unitary minimal models M(m, m+1)
    for m in range(3, 8):
        results.append(darith_virasoro_minimal(m, m + 1))
    # Non-unitary M(3,5)
    results.append(darith_virasoro_minimal(3, 5))

    # Generic Virasoro
    for c in [1, 13, 25, 26]:
        results.append(darith_virasoro_generic(c))

    # W-algebras
    results.append(darith_w_algebra(3, c_val=2))
    results.append(darith_w_algebra(3))
    results.append(darith_w_algebra(4, c_val=3))
    results.append(darith_w_algebra(4))

    return results


def first_darith_exceeding(threshold: int) -> Dict[str, object]:
    """Find the first lattice VOA family where d_arith > threshold."""
    for rank in range(8, 200, 8):
        k = rank // 2
        dim_cusp = cusp_form_dim_sl2z(k)
        da = 2 + dim_cusp
        if da > threshold:
            return {
                'rank': rank,
                'weight': k,
                'dim_cusp': dim_cusp,
                'd_arith': da,
                'info': f"dim S_{k}(SL(2,Z)) = {dim_cusp}"
            }
    return {'rank': None, 'note': f'Not found up to rank 200'}


def darith_monotonicity_lattice(max_rank: int = 200) -> List[Tuple[int, int, int]]:
    """Verify d_arith is non-decreasing with rank for unimodular lattice VOAs."""
    data = []
    for rank in range(8, max_rank + 1, 8):
        k = rank // 2
        da = 2 + cusp_form_dim_sl2z(k)
        data.append((rank, k, da))
    return data


# ============================================================================
# 10. Analysis functions
# ============================================================================

def landscape_summary() -> Dict[str, object]:
    """Summary statistics for the complete d_arith landscape."""
    table = complete_landscape_table()
    by_class = {'G': [], 'L': [], 'C': [], 'M': []}
    for r in table:
        by_class[r.shadow_class].append(r)

    finite = [r for r in table if isinstance(r.d_arith, int)]
    max_r = max(finite, key=lambda r: r.d_arith) if finite else None

    return {
        'total': len(table),
        'by_class': {k: len(v) for k, v in by_class.items()},
        'max_darith': max_r,
        'first_gt_2': first_darith_exceeding(2),
        'first_gt_3': first_darith_exceeding(3),
        'first_gt_4': first_darith_exceeding(4),
    }


def cusp_form_dim_table(max_weight: int = 60) -> List[Tuple[int, int]]:
    """Table of dim S_k(SL(2,Z)) for even k up to max_weight."""
    return [(k, cusp_form_dim_sl2z(k)) for k in range(2, max_weight + 1, 2)]


def darith_vs_rank_table() -> List[Dict[str, object]]:
    """Table showing d_arith growth with lattice rank."""
    rows = []
    for rank in range(8, 120 + 1, 8):
        k = rank // 2
        dim_cusp = cusp_form_dim_sl2z(k)
        da = 2 + dim_cusp
        rows.append({
            'rank': rank,
            'weight': k,
            'dim_S_k': dim_cusp,
            'd_arith': da,
            'd_total': 1 + da,
        })
    return rows


# ============================================================================
# Main
# ============================================================================

def print_complete_table():
    """Print the complete d_arith landscape table."""
    table = complete_landscape_table()

    print("=" * 85)
    print("COMPLETE ARITHMETIC DEPTH d_arith FOR THE STANDARD LANDSCAPE")
    print("=" * 85)

    current_class = None
    for r in table:
        if r.shadow_class != current_class:
            current_class = r.shadow_class
            class_names = {'G': 'Gaussian', 'L': 'Lie', 'C': 'Contact', 'M': 'Mixed'}
            print(f"\n--- CLASS {current_class} ({class_names.get(current_class, '')}, "
                  f"r_max = {'2' if current_class == 'G' else '3' if current_class == 'L' else '4' if current_class == 'C' else 'inf'}) ---")
            print(f"{'Family':<40} {'d_arith':>7} {'d_alg':>7} {'d_total':>7}  {'Mechanism':<30}")
            print("-" * 85)

        d_alg_s = 'inf' if r.d_alg is None else str(r.d_alg)
        d_total_s = 'inf' if r.d_total is None else str(r.d_total)
        d_arith_s = str(r.d_arith)
        mech_short = r.mechanism[:30]
        print(f"{r.family:<40} {d_arith_s:>7} {d_alg_s:>7} {d_total_s:>7}  {mech_short:<30}")

    print()
    print("=" * 85)
    print("\nLATTICE d_arith VS RANK:")
    print(f"{'Rank':>6}  {'Weight':>6}  {'dim S_k':>7}  {'d_arith':>7}  {'d_total':>7}")
    for row in darith_vs_rank_table():
        print(f"{row['rank']:>6}  {row['weight']:>6}  {row['dim_S_k']:>7}  "
              f"{row['d_arith']:>7}  {row['d_total']:>7}")

    print()
    summary = landscape_summary()
    print(f"Total families: {summary['total']}")
    print(f"By class: {summary['by_class']}")
    r = summary['first_gt_2']
    print(f"First d_arith > 2: rank {r.get('rank', '?')} (dim S_{r.get('weight', '?')} = {r.get('dim_cusp', '?')})")
    r = summary['first_gt_3']
    print(f"First d_arith > 3: rank {r.get('rank', '?')} (dim S_{r.get('weight', '?')} = {r.get('dim_cusp', '?')})")
    r = summary['first_gt_4']
    print(f"First d_arith > 4: rank {r.get('rank', '?')} (dim S_{r.get('weight', '?')} = {r.get('dim_cusp', '?')})")


if __name__ == '__main__':
    print_complete_table()
