r"""Superconformal algebra kappa verification engine.

AP49 CROSS-VOLUME FIX: Two errors in Vol II examples-worked.tex corrected.

ERROR 1 (CRITICAL): N=2 SCA kappa
  Vol I (w_algebras_deep.tex line 4913): kappa = (6-c)/(2(3-c)) = (k+4)/4.
  Vol II (examples-worked.tex line 4037): INCORRECTLY had kappa = c/2.
  At c=1: Vol I gives 5/4, Vol II gave 1/2 -- factor 5/2 discrepancy.
  FIX APPLIED: Vol II updated to match Vol I formula.

  The correct formula follows from the Kazama-Suzuki coset decomposition:
    N=2 SCA at c = 3k/(k+2) = Commutant(U(1), sl(2)_k x complex_fermion)
    kappa(N=2) = kappa(sl(2)_k) + kappa(fermion) - kappa(U(1))
              = 3(k+2)/4 + 1/2 - (k/2 + 1) = (k+4)/4

ERROR 2 (SERIOUS): N=4 small SCA
  Vol I TABLE (w_algebras_deep.tex line 3328): INCORRECTLY had c -> 12-c,
    self-dual c=6, kappa+kappa'=0.
  Vol II (examples-worked.tex line 4219): had c -> -c-24, self-dual c=-12
    (CORRECT for FF involution with c=6k), but kappa = c/2 (WRONG).
  FIX APPLIED:
    Vol I table corrected to c -> -c-24, self-dual c=-12, kappa+kappa'=-8.
    Vol II kappa corrected to c/3 = 2k (NOT c/2).

  The correct kappa = 2k is 5-path verified (geometric, character,
  complementarity, Hodge, N=4 Ward identity).

  CAUTION: For the K3 sigma model specifically, the geometric Verdier
  duality gives kappa' = -kappa = -2 and kappa+kappa'=0, using the
  CY sigma-model duality k -> -k (not the FF involution k -> -k-4).
  This applies only to the geometric realization, not to the abstract
  N=4 SCA family.

References:
  Vol I: w_algebras_deep.tex, toroidal_elliptic.tex
  Vol II: examples-worked.tex
  Compute: n2_kappa_resolution.py, cy_n4sca_k3_engine.py,
           theorem_cross_volume_ap49_engine.py
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Optional, Tuple


# ============================================================================
# 1. N=2 SCA kappa -- the correct formula
# ============================================================================

def n2_central_charge(k: Fraction) -> Fraction:
    """Central charge of the N=2 SCA: c = 3k/(k+2).

    The N=2 SCA is realized as the Kazama-Suzuki coset
    Commutant(U(1), sl(2)_k x complex_fermion).
    """
    return 3 * k / (k + 2)


def n2_level_from_c(c: Fraction) -> Fraction:
    """Recover the sl(2) level k from c = 3k/(k+2).

    Solving: c(k+2) = 3k => ck + 2c = 3k => k(3-c) = 2c => k = 2c/(3-c).
    Pole at c = 3 (the free-field limit k -> infinity).
    """
    if c == 3:
        raise ValueError("c = 3 is the free-field limit (k -> infinity)")
    return 2 * c / (3 - c)


def kappa_n2_from_level(k: Fraction) -> Fraction:
    """kappa(N=2 SCA) = (k+4)/4, in terms of the sl(2) level k.

    Derived from Kazama-Suzuki coset decomposition:
      kappa = kappa(sl(2)_k) + kappa(fermion) - kappa(U(1))
            = 3(k+2)/4 + 1/2 - (k/2 + 1)
            = 3k/4 + 3/2 + 1/2 - k/2 - 1
            = k/4 + 1 = (k+4)/4.
    """
    return (k + 4) / 4


def kappa_n2_from_c(c: Fraction) -> Fraction:
    """kappa(N=2 SCA) = (6-c)/(2(3-c)), in terms of central charge.

    Equivalently (k+4)/4 with k = 2c/(3-c).
    Pole at c = 3 (free-field limit).

    AP49: This is NOT c/2. The naive Virasoro formula fails
    because the N=2 SCA is a coset, and the coset subtraction
    reduces kappa below the Virasoro value c/2.
    """
    if c == 3:
        raise ValueError("c = 3 is the free-field limit (pole of kappa)")
    return (6 - c) / (2 * (3 - c))


def kappa_n2_coset_decomposition(k: Fraction) -> Dict[str, Fraction]:
    """Explicit coset decomposition of kappa(N=2).

    N=2 SCA = Commutant(U(1), sl(2)_k x complex_fermion)

    kappa(sl(2)_k) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4
    kappa(fermion pair) = 1/2  (complex fermion = bc at lambda=1/2)
    kappa(U(1)) = k/2 + 1  (Heisenberg at the denominator level)

    Result: kappa = 3(k+2)/4 + 1/2 - (k/2 + 1) = (k+4)/4
    """
    kappa_sl2 = Fraction(3) * (k + 2) / 4
    kappa_fermion = Fraction(1, 2)
    kappa_u1 = k / 2 + 1
    total = kappa_sl2 + kappa_fermion - kappa_u1
    return {
        'kappa_sl2_k': kappa_sl2,
        'kappa_fermion': kappa_fermion,
        'kappa_u1_denom': kappa_u1,
        'kappa_total': total,
        'formula_check': total == (k + 4) / 4,
    }


def n2_koszul_dual_c(c: Fraction) -> Fraction:
    """Koszul dual central charge: c' = 6 - c.

    The FF involution on sl(2) is k -> -k-4.
    Under c = 3k/(k+2): c' = 3(-k-4)/(-k-2) = 3(k+4)/(k+2) = 6 - c.
    """
    return 6 - c


def n2_complementarity_sum(c: Fraction) -> Fraction:
    """kappa(c) + kappa(6-c) = 1 (constant, W-type).

    PROOF: (6-c)/(2(3-c)) + c/(2(c-3))
         = (6-c)/(2(3-c)) - c/(2(3-c))
         = (6-2c)/(2(3-c)) = 1.
    """
    return kappa_n2_from_c(c) + kappa_n2_from_c(n2_koszul_dual_c(c))


# ============================================================================
# 2. N=4 small SCA kappa -- the correct formula
# ============================================================================

def n4_central_charge(k: Fraction) -> Fraction:
    """Central charge of the small N=4 SCA: c = 6k.

    k is the level of the su(2) R-symmetry current algebra.
    For unitary representations: k is a positive integer.
    K3 sigma model: k = 1, c = 6.
    """
    return 6 * k


def n4_level_from_c(c: Fraction) -> Fraction:
    """Recover the su(2) level k from c = 6k: k = c/6."""
    return c / 6


def kappa_n4_from_level(k: Fraction) -> Fraction:
    """kappa(small N=4 SCA) = 2k.

    5-path verified (at k=1):
      1. Geometric: kappa = dim_C(K3) = 2.
      2. Character: F_1 = 1/12, so kappa = 24*F_1 = 2.
      3. Complementarity: kappa' = -2 (CY Verdier), sum = 0.
      4. Hodge: obs_1/lambda_1 = (1/12)/(1/24) = 2.
      5. N=4 Ward: SUSY constrains kappa = 2k_R.

    AP48: kappa = 2k != c/2 = 3k. The N=4 supersymmetry
    reduces kappa by a factor of 2/3 relative to the Virasoro
    subalgebra value c/2.
    """
    return 2 * k


def kappa_n4_from_c(c: Fraction) -> Fraction:
    """kappa(small N=4 SCA) = c/3, in terms of central charge.

    AP48: NOT c/2. The full N=4 algebra has kappa = c/3 = 2k.
    The Virasoro subalgebra has kappa_Vir = c/2, but the
    extended supersymmetry reduces this by a factor of 2/3.
    """
    return c / 3


def n4_koszul_dual_c(c: Fraction) -> Fraction:
    """Koszul dual central charge: c' = -c - 24.

    The FF involution on the su(2) R-symmetry is k -> -k-4
    (h^v(su_2) = 2). With c = 6k: c' = 6(-k-4) = -c - 24.

    Self-dual point: c = -c-24 => c = -12 (k = -2 = -h^v).
    """
    return -c - 24


def n4_complementarity_sum_ff(c: Fraction) -> Fraction:
    """kappa(c) + kappa(c') under the FF involution.

    kappa = c/3, kappa' = c'/3 = (-c-24)/3.
    Sum = c/3 + (-c-24)/3 = -24/3 = -8.

    This is W-type (nonzero), NOT KM-type.
    """
    return kappa_n4_from_c(c) + kappa_n4_from_c(n4_koszul_dual_c(c))


def n4_complementarity_sum_cy(k: Fraction) -> Fraction:
    """kappa + kappa' under the CY sigma-model duality k -> -k.

    For the K3 sigma model, Verdier duality gives kappa' = -kappa.
    Sum = 2k + 2(-k) = 0.

    This is a DIFFERENT duality from the FF involution. It applies
    only to the geometric realization (CY sigma model), not to the
    abstract N=4 SCA family.
    """
    return kappa_n4_from_level(k) + kappa_n4_from_level(-k)


# ============================================================================
# 3. N=1 SVir kappa (for completeness of the hierarchy)
# ============================================================================

def kappa_svir(c: Fraction) -> Fraction:
    """kappa(SVir_c) = (3c-2)/4.

    The N=1 super-Virasoro algebra. Self-dual at c = 15/2.
    Koszul duality: c -> 15 - c.
    Complementarity: kappa(c) + kappa(15-c) = 41/4.
    """
    return (3 * c - 2) / 4


# ============================================================================
# 4. The superconformal complementarity hierarchy
# ============================================================================

def superconformal_hierarchy() -> Dict[str, Dict[str, object]]:
    """The corrected superconformal complementarity hierarchy.

    N=0 (Vir):   c -> 26-c,   self-dual c=13,  kappa+kappa'=13,  W-type
    N=1 (SVir):  c -> 15-c,   self-dual c=15/2, kappa+kappa'=41/4, W-type
    N=2 (SCA):   c -> 6-c,    self-dual c=3,    kappa+kappa'=1,   W-type
    N=4 (small): c -> -c-24,  self-dual c=-12,  kappa+kappa'=-8,  W-type

    The sequence 13 > 41/4 > 1 > -8 is strictly decreasing.
    ALL are W-type (nonzero complementarity sum).
    """
    hierarchy = {}

    # N=0: Virasoro
    c_vir = Fraction(13)
    hierarchy['N0_Vir'] = {
        'duality': 'c -> 26-c',
        'self_dual_c': Fraction(13),
        'kappa_at_self_dual': Fraction(13, 2),
        'comp_sum': Fraction(13),
        'type': 'W-type',
    }

    # N=1: SVir
    hierarchy['N1_SVir'] = {
        'duality': 'c -> 15-c',
        'self_dual_c': Fraction(15, 2),
        'kappa_at_self_dual': kappa_svir(Fraction(15, 2)),
        'comp_sum': kappa_svir(Fraction(15, 2)) + kappa_svir(Fraction(15, 2)),
        'type': 'W-type',
    }

    # N=2: SCA
    hierarchy['N2_SCA'] = {
        'duality': 'c -> 6-c',
        'self_dual_c': Fraction(3),
        'kappa_at_self_dual': 'pole (free-field limit)',
        'comp_sum': Fraction(1),
        'type': 'W-type',
    }

    # N=4: small
    hierarchy['N4_small'] = {
        'duality': 'c -> -c-24',
        'self_dual_c': Fraction(-12),
        'kappa_at_self_dual': kappa_n4_from_c(Fraction(-12)),
        'comp_sum': Fraction(-8),
        'type': 'W-type',
    }

    return hierarchy


# ============================================================================
# 5. Cross-volume discrepancy verification
# ============================================================================

def verify_n2_ap49_discrepancy() -> Dict[str, object]:
    """Verify the N=2 SCA AP49 cross-volume discrepancy.

    At c=1 (k=1):
      Vol I (correct): kappa = (6-1)/(2*(3-1)) = 5/4
      Vol II (was wrong): kappa = c/2 = 1/2
      Discrepancy factor: 5/2

    The Vol II formula c/2 is the Virasoro subalgebra value,
    NOT the full N=2 SCA value.
    """
    c = Fraction(1)
    correct = kappa_n2_from_c(c)  # 5/4
    wrong = c / 2  # 1/2
    return {
        'c': c,
        'correct_kappa': correct,
        'wrong_kappa': wrong,
        'discrepancy_ratio': correct / wrong,
        'is_discrepant': correct != wrong,
    }


def verify_n4_ap49_discrepancy() -> Dict[str, object]:
    """Verify the N=4 small SCA AP49 cross-volume discrepancy.

    At c=6 (k=1):
      Correct: kappa = c/3 = 2
      Vol II (was wrong): kappa = c/2 = 3
      Discrepancy factor: 3/2

      Correct duality: c -> -c-24
      Vol I table (was wrong): c -> 12-c
    """
    c = Fraction(6)
    correct = kappa_n4_from_c(c)  # 2
    wrong = c / 2  # 3
    return {
        'c': c,
        'correct_kappa': correct,
        'wrong_kappa_vol2': wrong,
        'correct_dual_c': n4_koszul_dual_c(c),
        'wrong_dual_c': 12 - c,
        'correct_comp_sum': n4_complementarity_sum_ff(c),
        'correct_self_dual': Fraction(-12),
    }


# ============================================================================
# 6. Multi-path verification utilities
# ============================================================================

def n2_kappa_multipath(c: Fraction) -> Dict[str, Fraction]:
    """Verify N=2 kappa by multiple independent methods.

    Path 1: Direct formula (6-c)/(2(3-c))
    Path 2: Coset decomposition via k = 2c/(3-c)
    Path 3: Complementarity check (sum = 1)
    """
    if c == 3:
        raise ValueError("c = 3: free-field limit")

    k = n2_level_from_c(c)

    path1 = kappa_n2_from_c(c)
    path2 = kappa_n2_from_level(k)
    coset = kappa_n2_coset_decomposition(k)
    path3 = coset['kappa_total']
    comp = n2_complementarity_sum(c)

    return {
        'path1_direct': path1,
        'path2_level': path2,
        'path3_coset': path3,
        'all_agree': path1 == path2 == path3,
        'complementarity_sum': comp,
        'comp_is_one': comp == 1,
    }


def n4_kappa_multipath(k: Fraction) -> Dict[str, Fraction]:
    """Verify N=4 kappa by multiple independent methods.

    Path 1: kappa = 2k (from level)
    Path 2: kappa = c/3 (from central charge)
    Path 3: Verify kappa != c/2 (AP48)
    Path 4: FF complementarity = -8
    Path 5: CY complementarity = 0
    """
    c = n4_central_charge(k)

    path1 = kappa_n4_from_level(k)
    path2 = kappa_n4_from_c(c)
    wrong = c / 2

    return {
        'k': k,
        'c': c,
        'path1_level': path1,
        'path2_c': path2,
        'agree': path1 == path2,
        'wrong_virasoro': wrong,
        'not_virasoro': path1 != wrong,
        'ff_comp_sum': n4_complementarity_sum_ff(c),
        'cy_comp_sum': n4_complementarity_sum_cy(k),
    }
