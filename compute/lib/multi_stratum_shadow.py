"""Charge-graded master equation recursion for multi-stratum shadow obstruction towers.

Implements the shadow obstruction tower on a charge lattice Lambda.
For a system with charge sectors q in Lambda and shadow data S_r^(q),
the recursion is:

    S_r^(q) = -(P / (2r)) * sum_{j+k=r+2, 3<=j<=k} c_{jk} * jk
              * sum_{q1+q2=q} S_j^(q1) * S_k^(q2)

where:
  - P = 2/kappa  (inverse Hessian propagator)
  - c_{jk} = 1 for j < k, 1/2 for j = k  (MC symmetry factor)
  - The sum is over charge decompositions q = q1 + q2

A charge sector Def^(q) is AVAILABLE if dim Def^(q) > 0.  The tower
terminates (at a given arity r and charge q) when all contributions
from available sectors vanish.

The four shadow depth classes persist in the multi-stratum setting:
  G (Gaussian):    r_max = 2, e.g. Heisenberg (alpha=0, Q=0)
  L (Lie/tree):    r_max = 3, e.g. affine on neutral sector only
  C (contact):     r_max = 4, e.g. beta-gamma quartic on charged sector
  M (mixed):       r_max = infinity, cubic pump feeds quartic => infinite

Ground truth:
  - thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  - prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
  - thm:nms-all-arity-master-equation (nonlinear_modular_shadows.tex)
  - virasoro_shadow_tower.py (single-sector reference implementation)

All arithmetic is exact (sympy.Rational). Never floating point.
"""

from __future__ import annotations

from itertools import product as iterproduct
from typing import Dict, List, Optional, Tuple

from sympy import Rational, Symbol, simplify, factor, S, symbols


# =========================================================================
# Charge lattice utilities
# =========================================================================

def _charge_decompositions(
    q: tuple, available: set
) -> List[Tuple[tuple, tuple]]:
    """Find all decompositions q = q1 + q2 with q1, q2 in available charges.

    Args:
        q: target charge vector (tuple of ints).
        available: set of available charge vectors (tuples of ints).

    Returns:
        List of (q1, q2) pairs with q1 + q2 = q componentwise,
        both q1 and q2 in available.
    """
    decomps = []
    for q1 in available:
        q2 = tuple(qi - q1i for qi, q1i in zip(q, q1))
        if q2 in available:
            decomps.append((q1, q2))
    return decomps


def _available_charges_two_sector() -> set:
    """Available charges for the two-sector system.

    Sectors: q=0 (neutral, carries kappa and alpha)
             q=1 (charged, carries quartic Q).
    Charge 2 is NOT available (rank-1 rigidity).
    """
    return {(0,), (1,)}


def _available_charges_rank_n(rank: int) -> set:
    """Available charges for rank-n abelian system.

    All q with |q|_infty <= 1, i.e. each component is 0 or 1.
    """
    return set(iterproduct(range(2), repeat=rank))


# =========================================================================
# Two-sector tower
# =========================================================================

def compute_two_sector_tower(
    kappa=None, alpha=None, Q=None, max_arity: int = 12
) -> Dict[Tuple[int, tuple], object]:
    """Compute the charge-graded shadow obstruction tower for a two-sector system.

    Two sectors:
      q=(0,): neutral sector, carries curvature kappa and cubic alpha
      q=(1,): charged sector, carries quartic contact Q

    The initial data:
      S_2^{(0,)} = kappa        (curvature on neutral)
      S_3^{(0,)} = alpha        (cubic shadow on neutral)
      S_4^{(1,)} = Q            (quartic contact on charged)

    The propagator P = 2/kappa.

    The recursion generates all higher shadows.  Charge 2 is NOT available
    (rank-1 rigidity), so only q in {(0,), (1,)} contribute.

    Args:
        kappa: curvature parameter.  None for symbolic Symbol('kappa').
        alpha: cubic shadow coefficient.  None for symbolic Symbol('alpha').
        Q: quartic contact coefficient.  None for symbolic Symbol('Q').
        max_arity: maximum arity to compute (default 12).

    Returns:
        dict mapping (r, q) -> S_r^(q) for all computed (r, q).
        Only nonzero entries are included.
    """
    if kappa is None:
        kappa = Symbol('kappa')
    if alpha is None:
        alpha = Symbol('alpha')
    if Q is None:
        Q = Symbol('Q')

    P = Rational(2) / kappa
    available = _available_charges_two_sector()

    # Initial data (only include if within max_arity)
    tower = {}
    tower[(2, (0,))] = kappa
    if alpha != 0 and max_arity >= 3:
        tower[(3, (0,))] = alpha
    if Q != 0 and max_arity >= 4:
        tower[(4, (1,))] = Q

    # Recursive computation for arities 5 through max_arity.
    # Arities 2, 3, 4 are initial data from the OPE structure;
    # the master equation recursion propagates from arity 5 onward.
    for r in range(5, max_arity + 1):
        for q in sorted(available):
            if (r, q) in tower:
                continue  # already set as initial data

            # Compute obstruction sum
            obstruction = S.Zero
            for j in range(3, r + 1):
                k = r + 2 - j
                if k < 3:
                    continue
                if j > k:
                    continue  # avoid double counting

                # Symmetry factor
                c_jk = Rational(1, 2) if j == k else Rational(1)

                # Sum over charge decompositions
                for q1, q2 in _charge_decompositions(q, available):
                    Sj = tower.get((j, q1), S.Zero)
                    Sk = tower.get((k, q2), S.Zero)
                    if Sj == 0 or Sk == 0:
                        continue

                    contrib = c_jk * j * k * Sj * Sk

                    # For j != k with ordered pairs, we also need (k, q2) * (j, q1)
                    # which comes from the decomposition (q2, q1) in the charge sum.
                    # But _charge_decompositions already gives all (q1, q2) pairs,
                    # so the (q2, q1) contribution with (k, j) is handled by
                    # the c_jk = 1 factor (accounting for both orderings of j, k).
                    obstruction += contrib

            if obstruction == 0:
                continue

            obstruction = simplify(obstruction)
            if obstruction == 0:
                continue

            S_r_q = simplify(-P / (2 * r) * obstruction)
            S_r_q = factor(S_r_q)
            tower[(r, q)] = S_r_q

    return tower


# =========================================================================
# Rank-n abelian tower
# =========================================================================

def compute_rank_n_abelian_tower(
    kappa=None, Q_list: Optional[List] = None,
    max_arity: int = 12, rank: int = 2
) -> Dict[Tuple[int, tuple], object]:
    """Compute the charge-graded shadow obstruction tower for a rank-n abelian system.

    For rank-n abelian systems, alpha = 0 on all sectors (no cubic shadow),
    and the quartic contacts Q_i are specified per fundamental charge sector.

    Available charges: all q with each component in {0, 1}.
    The neutral sector q = (0,...,0) carries kappa only (no cubic, no quartic).
    The fundamental charge sectors e_i = (0,...,1,...,0) carry quartic Q_i.

    Args:
        kappa: curvature parameter.  None for symbolic Symbol('kappa').
        Q_list: list of quartic contact coefficients, one per rank.
            None for symbolic [Symbol('Q_1'), ..., Symbol('Q_n')].
        max_arity: maximum arity to compute (default 12).
        rank: number of abelian generators (default 2).

    Returns:
        dict mapping (r, q) -> S_r^(q) for all computed (r, q).
    """
    if kappa is None:
        kappa = Symbol('kappa')
    if Q_list is None:
        Q_list = [Symbol(f'Q_{i+1}') for i in range(rank)]

    assert len(Q_list) == rank, f"Q_list has {len(Q_list)} entries, expected {rank}"

    P = Rational(2) / kappa
    available = _available_charges_rank_n(rank)

    # Initial data
    tower = {}

    # Neutral sector: curvature only
    zero_charge = tuple(0 for _ in range(rank))
    tower[(2, zero_charge)] = kappa

    # Fundamental charge sectors: quartic contacts
    for i in range(rank):
        e_i = tuple(1 if j == i else 0 for j in range(rank))
        if Q_list[i] != 0:
            tower[(4, e_i)] = Q_list[i]

    # Recursive computation
    for r in range(5, max_arity + 1):
        for q in sorted(available):
            if (r, q) in tower:
                continue

            obstruction = S.Zero
            for j in range(3, r + 1):
                k = r + 2 - j
                if k < 3:
                    continue
                if j > k:
                    continue

                c_jk = Rational(1, 2) if j == k else Rational(1)

                for q1, q2 in _charge_decompositions(q, available):
                    Sj = tower.get((j, q1), S.Zero)
                    Sk = tower.get((k, q2), S.Zero)
                    if Sj == 0 or Sk == 0:
                        continue
                    obstruction += c_jk * j * k * Sj * Sk

            if obstruction == 0:
                continue

            obstruction = simplify(obstruction)
            if obstruction == 0:
                continue

            S_r_q = simplify(-P / (2 * r) * obstruction)
            S_r_q = factor(S_r_q)
            tower[(r, q)] = S_r_q

    return tower


# =========================================================================
# Four-class persistence verification
# =========================================================================

def verify_four_class_persistence(max_arity: int = 10) -> Dict[str, dict]:
    """Verify that the four shadow depth classes persist in the two-sector setting.

    The four cases for the two-sector system (q=0 neutral, q=1 charged):
      G: alpha=0, Q=0  =>  r_max = 2 on neutral, 0 on charged  (class G)
      L: alpha!=0, Q=0 =>  r_max = 3 on neutral, 0 on charged  (class L)
      C: alpha=0, Q!=0 =>  r_max = 2 on neutral, 4 on charged  (class C)
      M: alpha!=0, Q!=0 => r_max = 3 on neutral, infinity on charged (class M)
         The cubic pump feeds the charged sector indefinitely via
         S_3^{(0)} * S_{r-1}^{(1)} => S_r^{(1)}.  The neutral sector
         stays at arity 3 because charge conservation (no charge -1
         available) blocks backflow.

    Returns:
        dict with keys 'G', 'L', 'C', 'M', each mapping to a dict with:
          'tower': the computed tower
          'max_r_neutral': highest nonzero arity on q=(0,)
          'max_r_charged': highest nonzero arity on q=(1,)
          'class_correct': bool
    """
    kappa_sym = Symbol('kappa')
    alpha_sym = Symbol('alpha')
    Q_sym = Symbol('Q')

    results = {}

    # Class G: alpha=0, Q=0
    tower_G = compute_two_sector_tower(
        kappa=kappa_sym, alpha=S.Zero, Q=S.Zero, max_arity=max_arity
    )
    max_r_n_G = max(
        (r for (r, q) in tower_G if q == (0,)), default=0
    )
    max_r_c_G = max(
        (r for (r, q) in tower_G if q == (1,)), default=0
    )
    results['G'] = {
        'tower': tower_G,
        'max_r_neutral': max_r_n_G,
        'max_r_charged': max_r_c_G,
        'class_correct': max_r_n_G == 2 and max_r_c_G == 0,
    }

    # Class L: alpha!=0, Q=0
    tower_L = compute_two_sector_tower(
        kappa=kappa_sym, alpha=alpha_sym, Q=S.Zero, max_arity=max_arity
    )
    max_r_n_L = max(
        (r for (r, q) in tower_L if q == (0,)), default=0
    )
    max_r_c_L = max(
        (r for (r, q) in tower_L if q == (1,)), default=0
    )
    results['L'] = {
        'tower': tower_L,
        'max_r_neutral': max_r_n_L,
        'max_r_charged': max_r_c_L,
        'class_correct': max_r_n_L == 3 and max_r_c_L == 0,
    }

    # Class C: alpha=0, Q!=0
    tower_C = compute_two_sector_tower(
        kappa=kappa_sym, alpha=S.Zero, Q=Q_sym, max_arity=max_arity
    )
    max_r_n_C = max(
        (r for (r, q) in tower_C if q == (0,)), default=0
    )
    max_r_c_C = max(
        (r for (r, q) in tower_C if q == (1,)), default=0
    )
    results['C'] = {
        'tower': tower_C,
        'max_r_neutral': max_r_n_C,
        'max_r_charged': max_r_c_C,
        'class_correct': max_r_n_C == 2 and max_r_c_C == 4,
    }

    # Class M: alpha!=0, Q!=0
    tower_M = compute_two_sector_tower(
        kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=max_arity
    )
    max_r_n_M = max(
        (r for (r, q) in tower_M if q == (0,)), default=0
    )
    max_r_c_M = max(
        (r for (r, q) in tower_M if q == (1,)), default=0
    )
    # For class M, the cubic pump feeds the charged sector indefinitely:
    # the sewing S_3^{(0,)} * S_{r-1}^{(1,)} => S_r^{(1,)} at each step.
    # The charged sector reaches max_arity; the neutral stays at arity 3
    # because charge conservation (no charge -1 available) prevents
    # backflow from charged to neutral.
    results['M'] = {
        'tower': tower_M,
        'max_r_neutral': max_r_n_M,
        'max_r_charged': max_r_c_M,
        'class_correct': max_r_n_M == 3 and max_r_c_M >= max_arity,
    }

    return results


# =========================================================================
# Convenience extractors
# =========================================================================

def tower_by_charge(
    tower: Dict[Tuple[int, tuple], object], q: tuple
) -> Dict[int, object]:
    """Extract the sub-tower for a single charge sector."""
    return {r: val for (r, qq), val in tower.items() if qq == q}


def shadow_depth(
    tower: Dict[Tuple[int, tuple], object], q: tuple
) -> int:
    """Return the maximum arity with nonzero shadow in charge sector q."""
    arities = [r for (r, qq) in tower if qq == q]
    return max(arities) if arities else 0


def single_sector_recovery(
    tower: Dict[Tuple[int, tuple], object]
) -> Dict[int, object]:
    """For a one-sector system (charge lattice = {0}), recover the
    standard tower dict {r: S_r}."""
    zero_q = None
    for (r, q) in tower:
        zero_q = q
        break
    if zero_q is None:
        return {}
    return tower_by_charge(tower, zero_q)


if __name__ == '__main__':
    print("Multi-stratum shadow obstruction tower: four-class persistence check")
    print("=" * 60)

    results = verify_four_class_persistence(max_arity=8)
    for cls_name in ('G', 'L', 'C', 'M'):
        res = results[cls_name]
        status = "PASS" if res['class_correct'] else "FAIL"
        print(f"  Class {cls_name}: neutral r_max={res['max_r_neutral']}, "
              f"charged r_max={res['max_r_charged']} [{status}]")
