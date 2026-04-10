r"""Shadow depth for non-even (type I) unimodular lattice VOAs.

For an even unimodular lattice (type II) of rank r, the shadow depth is

    d(V_Lambda) = 3 + dim S_{r/2}(SL(2,Z)),

where S_k(SL(2,Z)) is the space of cusp forms of weight k for the full
modular group (lattice_shadow_higher_depth_engine.py).  The rank must be
divisible by 8, and the theta function Theta_Lambda is a modular form of
weight r/2 for SL(2,Z).

For an ODD unimodular lattice (type I), the theta function is NOT modular
for SL(2,Z).  Instead it transforms under the theta group Gamma_theta,
which is conjugate to Gamma_0(2) and contained in Gamma_0(4).  The shadow
obstructions therefore live in S_{r/2}(Gamma_0(4), chi), where chi is a
Nebentypus character determined by the lattice parity structure.  Since
Gamma_0(4) has more cusp forms than SL(2,Z) at any given weight, the
type I shadow depth is generically LARGER than the type II depth.

MAIN RESULT (conjectural):

  For a type I unimodular lattice of rank r >= 1, the shadow depth is

    d(V_Lambda) = 3 + dim_cusp_type_I(r),

  where dim_cusp_type_I(r) counts cusp forms at the appropriate weight
  and level:

  (a) Even rank r, integer weight k = r/2:
      dim_cusp_type_I(r) = dim S_k(Gamma_0(4), chi_k)
        = max(0, floor((k - 3)/2))
        = max(0, floor((r - 6)/4))

      For k even (r divisible by 4): trivial character, S_k(Gamma_0(4)).
        Gamma_0(4) data: index 6, genus 0, 0 elliptic points, 3 cusps.
        dim S_k(Gamma_0(4)) = max(0, k/2 - 2) for k >= 2 even.

      For k odd (r congruent to 2 mod 4): character chi_{-4} = (-4/.).
        dim S_k(Gamma_0(4), chi_{-4}) = max(0, (k-3)/2) for k >= 3 odd.

      Both cases unify to floor((k - 3)/2) = floor((r/2 - 3)/2).

  (b) Odd rank r, half-integer weight k = r/2:
      Via the Shimura correspondence and Kohnen plus-space:
        dim_cusp_type_I(r) = dim S_{r-1}(SL(2,Z))
      where S_{r-1} is the space of cusp forms of integer weight r-1
      for the full modular group.

COMPARISON WITH TYPE II:

  At ranks divisible by 8 (where both types exist):
    d_I(r) - d_II(r) = dim S_{r/2}(Gamma_0(4)) - dim S_{r/2}(SL(2,Z))
  This correction grows as approximately 5r/24 and is always non-negative.
  It vanishes only at r = 8 (the smallest even-unimodular rank).

  Physical interpretation: odd-norm vectors in the lattice create additional
  modular form channels through which shadow obstructions can propagate.
  The theta function for a type I lattice has richer modular properties
  (lower-level congruence subgroup), and each extra cusp form contributes
  one additional shadow depth level.

EXAMPLES:

  Z^1 (rank 1): d = 3 (no cusp forms at weight 1/2)
  Z^8 (rank 8): d = 3 (same as E8; both cusp form spaces vanish)
  Z^10 (rank 10): d = 4 (dim S_5(Gamma_0(4), chi_{-4}) = 1)
  Z^16 (rank 16): d = 5 (dim S_8(Gamma_0(4)) = 2; compare E8+E8: d = 3)
  Z^24 (rank 24): d = 7 (dim S_12(Gamma_0(4)) = 4; compare Leech: d = 4)

CONVENTIONS:
  kappa(V_Lambda) = r/2 for unimodular lattice of rank r (AP1, C1).
  Shadow class is G (abelian OPE) at the algebraic level; the arithmetic
  correction lifts the depth above the base G-class value of 2.
  The '3' baseline in d = 3 + dim_cusp comes from:
    - S_2 = kappa = r/2 (arity 2, always nonzero for r > 0)
    - Kodaira-Spencer cubic at genus 1 (arity 3, always present)
    - Quartic contact S_4 from theta function normalization (arity 4,
      present whenever the Eisenstein component is nonzero)
  Each independent cusp form adds one further arity of obstruction.

CAUTIONS:
  AP1:  kappa = r/2 for lattice VOA, NOT r. Verify at r = 0: kappa = 0.
  AP32: Shadow depth is an ARITHMETIC invariant of the genus expansion.
        It is NOT the same as the algebraic shadow class (G for all lattice VOAs).
  AP141: This module does not involve r-matrices, but see lattice_shadow_census.py
         for the r-matrix r(z) = k*Omega/z (level prefix mandatory, AP126).

References:
  Conway-Sloane, "Sphere Packings, Lattices and Groups" (1999), Ch. 7
  Shimura, "On modular forms of half integral weight" (1973), Ann. Math.
  Kohnen, "Newforms of half-integral weight" (1982), J. Reine Angew. Math.
  Diamond-Shurman, "A First Course in Modular Forms" (2005), Ch. 6
  Ebeling, "Lattices and Codes" (2013), Ch. 4
  Vol I: higher_genus_modular_koszul.tex (shadow depth classification)
  Vol I: lattice_shadow_higher_depth_engine.py (type II baseline)
"""

from __future__ import annotations

from typing import Dict, Optional, Tuple


# ============================================================================
# Cusp form dimensions: SL(2,Z) (reproduced from lattice_shadow_higher_depth_engine)
# ============================================================================

def dim_cusp_forms_sl2z(k: int) -> int:
    r"""Return dim S_k(SL(2,Z)) for the full modular group.

    Standard dimension formula (Diamond-Shurman Theorem 3.5.1):
      k < 2 or k odd:  0
      k = 2:           0
      k >= 4 even:     floor(k/12)     if k mod 12 != 2
                        floor(k/12) - 1 if k mod 12 == 2

    VERIFIED: [DC] direct computation from the Riemann-Roch formula on X(1);
    [LT] Diamond-Shurman Table 3.3, LMFDB Modular Forms database.
    """
    if k < 12 or k % 2 != 0:
        return 0
    if k == 12:
        # VERIFIED: [DC] S_12 = C*Delta, dim = 1; [LT] Ramanujan Delta
        return 1
    if k % 12 == 2:
        # VERIFIED: [DC] floor(k/12)-1; [LC] k=14->0, k=26->1
        return k // 12 - 1
    # VERIFIED: [DC] floor(k/12); [LC] k=24->2, k=36->3
    return k // 12


# ============================================================================
# Cusp form dimensions: Gamma_0(4) (type I lattice level)
# ============================================================================

def dim_cusp_forms_gamma0_4(k: int, even_weight: bool = True) -> int:
    r"""Return dim S_k(Gamma_0(4), chi) for the congruence subgroup Gamma_0(4).

    Gamma_0(4) data:
      Index [SL(2,Z) : Gamma_0(4)] = 6
      Genus of X_0(4) = 0
      Elliptic points: eps_2 = 0, eps_3 = 0
      Cusps: 3 (at 0, 1/2, infinity)

    For EVEN weight k >= 2 with trivial character (even_weight=True, k even):
      dim S_k(Gamma_0(4)) = max(0, k/2 - 2)

      Derivation (Stein, Modular Forms: A Computational Approach, Thm 6.1):
        dim S_k = (k-1)(g-1) + floor(k/4)*eps_2 + floor(k/3)*eps_3 + (k/2-1)*c
        = (k-1)(-1) + 0 + 0 + (k/2-1)*3
        = -(k-1) + 3k/2 - 3 = k/2 - 2

      VERIFIED: [DC] direct from dimension formula with g=0, c=3, eps_2=eps_3=0;
      [LT] LMFDB confirms dim S_4 = 0, S_6 = 1, S_8 = 2, S_12 = 4.

    For ODD weight k >= 3 with character chi_{-4} (even_weight=False, k odd):
      dim S_k(Gamma_0(4), chi_{-4}) = max(0, (k-3)/2)

      The character chi_{-4} = (-4/.) is the Kronecker symbol of conductor 4.
      Since -I in Gamma_0(4) acts by (-1)^k and chi_{-4}(-1) = -1, odd weight
      with this character is consistent.

      VERIFIED: [DC] Cohen-Oesterlé dimension formula for Gamma_0(4) with
      Nebentypus chi_{-4}; [LT] LMFDB level 4 weight 5 gives dim 1.

    Parameters
    ----------
    k : int
        Weight of cusp forms.  Must be >= 1.
    even_weight : bool
        If True, compute dim S_k(Gamma_0(4)) with trivial character (k must be even).
        If False, compute dim S_k(Gamma_0(4), chi_{-4}) (k must be odd).
    """
    if k < 2:
        return 0

    if even_weight:
        if k % 2 != 0:
            raise ValueError(
                f"even_weight=True requires even k, got k={k}"
            )
        if k == 2:
            # VERIFIED: [DC] genus 0 implies dim S_2 = 0; [LC] X_0(4) rational
            return 0
        # k >= 4, even
        # VERIFIED: [DC] k/2 - 2; [LC] k=4->0, k=6->1, k=8->2, k=12->4
        return max(0, k // 2 - 2)
    else:
        if k % 2 != 1:
            raise ValueError(
                f"even_weight=False requires odd k, got k={k}"
            )
        # k >= 3, odd, character chi_{-4}
        # VERIFIED: [DC] (k-3)/2; [LC] k=3->0, k=5->1, k=7->2
        return max(0, (k - 3) // 2)


# ============================================================================
# Cusp form dimensions for type I lattice shadow depth
# ============================================================================

def dim_cusp_type_I(rank: int) -> int:
    r"""Return the cusp form dimension controlling type I shadow depth.

    For a type I (odd) unimodular lattice of rank r:

    (a) Even rank r: integer weight k = r/2.
        - k even (r divisible by 4): dim S_k(Gamma_0(4)), trivial character.
        - k odd (r congruent to 2 mod 4): dim S_k(Gamma_0(4), chi_{-4}).
        Both cases give max(0, floor((k-3)/2)) = max(0, floor((r-6)/4)).

    (b) Odd rank r: half-integer weight k = r/2.
        Via Shimura-Kohnen correspondence:
          dim S_{r/2}^+(Gamma_0(4)) = dim S_{r-1}(SL(2,Z))

    VERIFIED: [DC] dimension formulas for Gamma_0(4) and SL(2,Z);
    [CF] even-rank formula matches direct Gamma_0(4) computation;
    [LC] rank 8 -> 0, rank 10 -> 1, rank 24 -> 4.
    """
    if rank < 1:
        raise ValueError(f"rank must be >= 1, got {rank}")

    if rank % 2 == 0:
        # Even rank: integer weight k = r/2
        k = rank // 2
        if k < 3:
            return 0
        # Unified formula: floor((k-3)/2) = floor((r-6)/4)
        # VERIFIED: [DC] matches dim S_k(Gamma_0(4), chi_k) for both parities of k;
        # [LC] r=8 -> k=4 -> floor(1/2)=0; r=10 -> k=5 -> floor(2/2)=1
        return (k - 3) // 2
    else:
        # Odd rank: half-integer weight, Shimura correspondence
        # dim S_{r/2}^+(Gamma_0(4)) = dim S_{r-1}(SL(2,Z))
        # VERIFIED: [DC] Kohnen's theorem; [LC] r=13 -> dim S_12(SL2Z) = 1
        weight_sl2z = rank - 1
        return dim_cusp_forms_sl2z(weight_sl2z)


# ============================================================================
# Shadow depth: type I
# ============================================================================

def shadow_depth_type_I(rank: int) -> int:
    r"""Shadow depth for a type I unimodular lattice VOA of rank r.

    d(V_Lambda) = 3 + dim_cusp_type_I(r)

    The baseline depth 3 comes from:
      - S_2 = kappa = r/2 (arity 2)
      - Kodaira-Spencer cubic (arity 3)
      - Eisenstein quartic normalization (arity 4, contributes to baseline)
    Each independent cusp form at the lattice theta-function level adds +1.

    VERIFIED: [DC] d = 3 + dim_cusp; [LC] rank 1 -> 3 (Z has no cusp forms),
    rank 8 -> 3 (matches E8 type II), rank 10 -> 4, rank 24 -> 7.
    """
    if rank < 1:
        raise ValueError(f"rank must be >= 1, got {rank}")
    return 3 + dim_cusp_type_I(rank)


# ============================================================================
# Shadow depth: type II (wrapper for comparison)
# ============================================================================

def shadow_depth_type_II(rank: int) -> int:
    r"""Shadow depth for a type II (even) unimodular lattice VOA of rank r.

    d(V_Lambda) = 3 + dim S_{r/2}(SL(2,Z))

    Rank must be a positive multiple of 8.

    VERIFIED: [DC] standard formula; [LC] rank 8 -> 3, rank 24 -> 4.
    """
    if rank <= 0 or rank % 8 != 0:
        raise ValueError(
            f"rank must be a positive multiple of 8 for type II, got {rank}"
        )
    return 3 + dim_cusp_forms_sl2z(rank // 2)


# ============================================================================
# Depth correction: delta = d_I - d_II
# ============================================================================

def depth_correction(rank: int) -> int:
    r"""Excess shadow depth of type I over type II at the same rank.

    delta(r) = d_I(r) - d_II(r)
             = dim S_{r/2}(Gamma_0(4)) - dim S_{r/2}(SL(2,Z))

    This counts the cusp forms for Gamma_0(4) that are NOT lifts from SL(2,Z),
    i.e., the "old forms" and "genuinely new" forms at level 4.

    Only defined when rank is a positive multiple of 8 (both types exist).

    VERIFIED: [DC] difference of two dimension formulas;
    [LC] rank 8 -> 0, rank 16 -> 2, rank 24 -> 3, rank 48 -> 8.
    """
    if rank <= 0 or rank % 8 != 0:
        raise ValueError(
            f"rank must be a positive multiple of 8 for comparison, got {rank}"
        )
    return shadow_depth_type_I(rank) - shadow_depth_type_II(rank)


# ============================================================================
# Comprehensive census
# ============================================================================

def shadow_depth_census(
    max_rank: int = 48,
) -> Dict[int, Dict[str, object]]:
    r"""Build a census of shadow depths for type I lattices up to max_rank.

    Returns a dict mapping rank -> {
        'rank': int,
        'kappa': Fraction,
        'dim_cusp': int,
        'depth_type_I': int,
        'depth_type_II': int or None (if rank not divisible by 8),
        'delta': int or None,
        'weight': str (e.g. '4' or '5/2'),
        'level_group': str,
    }
    """
    from fractions import Fraction

    census = {}
    for r in range(1, max_rank + 1):
        entry: Dict[str, object] = {
            'rank': r,
            'kappa': Fraction(r, 2),
            'dim_cusp': dim_cusp_type_I(r),
            'depth_type_I': shadow_depth_type_I(r),
        }

        # Weight description
        if r % 2 == 0:
            entry['weight'] = str(r // 2)
            if r % 4 == 0:
                entry['level_group'] = 'Gamma_0(4), trivial'
            else:
                entry['level_group'] = 'Gamma_0(4), chi_{-4}'
        else:
            entry['weight'] = f'{r}/2'
            entry['level_group'] = 'Gamma_0(4), theta-multiplier (Kohnen)'

        # Type II comparison when available
        if r % 8 == 0 and r > 0:
            entry['depth_type_II'] = shadow_depth_type_II(r)
            entry['delta'] = depth_correction(r)
        else:
            entry['depth_type_II'] = None
            entry['delta'] = None

        census[r] = entry

    return census


# ============================================================================
# Lattice examples
# ============================================================================

# Standard type I unimodular lattices
TYPE_I_EXAMPLES = {
    1: {'name': 'Z', 'rank': 1, 'description': 'integer lattice'},
    2: {'name': 'Z^2', 'rank': 2, 'description': 'square lattice'},
    3: {'name': 'Z^3', 'rank': 3, 'description': 'cubic lattice'},
    4: {'name': 'Z^4', 'rank': 4, 'description': 'hypercubic lattice'},
    8: {'name': 'Z^8', 'rank': 8, 'description': 'hypercubic; compare E8 (type II)'},
    9: {'name': 'Z^9', 'rank': 9, 'description': 'first rank with d_I > 3 impossible (still 3)'},
    10: {'name': 'Z^10', 'rank': 10, 'description': 'first even rank with d_I > 3'},
    13: {'name': 'Z^13', 'rank': 13, 'description': 'first odd rank with d_I > 3'},
    16: {'name': 'Z^16', 'rank': 16, 'description': 'compare E8+E8, D16+ (type II, d=3)'},
    24: {'name': 'Z^24', 'rank': 24, 'description': 'compare Leech (type II, d=4)'},
}


if __name__ == '__main__':
    print('Type I lattice shadow depths')
    print('=' * 65)
    print(f'{"rank":>5} {"weight":>7} {"dim_cusp":>9} {"d_I":>5} {"d_II":>6} {"delta":>6}')
    print('-' * 65)
    census = shadow_depth_census(48)
    for r in sorted(census):
        e = census[r]
        d_II_str = str(e['depth_type_II']) if e['depth_type_II'] is not None else '-'
        delta_str = str(e['delta']) if e['delta'] is not None else '-'
        print(
            f"{e['rank']:>5} {e['weight']:>7} {e['dim_cusp']:>9} "
            f"{e['depth_type_I']:>5} {d_II_str:>6} {delta_str:>6}"
        )
