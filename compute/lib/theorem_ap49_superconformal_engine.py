r"""AP49 cross-volume superconformal family verification engine.

Systematic check of ALL superconformal families across both volumes.

FAMILIES CHECKED:
  N=0  Virasoro:     kappa = c/2,         c -> 26-c,    comp sum = 13
  N=1  SVir:         kappa = (3c-2)/4,    c -> 15-c,    comp sum = 41/4
  N=2  SCA:          kappa = (6-c)/(2(3-c)) = (k+4)/4,  c -> 6-c,  comp sum = 1
  N=4  small SCA:    kappa = c/3 = 2k,    c -> -c-24,   comp sum = -8
  BP   (W(sl3,fmin)):kappa = c/6,         k -> -k-6,    comp sum = 98/3 (FKR conv)

FINDINGS:
  F1 (SERIOUS): subregular_hook_frontier.tex prop:bp-complementarity-constant
     claims K_BP = 76 using WRONG formula c = 2 - 3(2k+3)^2/(k+3).
     Correct: K_BP = 196 using c = 2 - 24(k+1)^2/(k+3) (FKR convention).
     The computation comp:bp-kappa-three-paths in the SAME FILE correctly says K=196.
     INTRA-FILE CONTRADICTION (AP7 + AP3).

  F2 (MODERATE): standalone/bp_self_duality.tex line 328 claims
     anomaly ratio rho = 17/12 using UNSIGNED formula sum 1/(2h_i).
     Correct: varrho = 1/6 using SIGNED formula sum (-1)^{p_i}/h_i.
     The standalone uses kappa_T = c/2 (T-line projection) throughout,
     so rho = 17/12 is dead code, but the formula is wrong.

  F3 (OK): w_algebras_deep.tex uses rescaled c = (k-15)/(k+3), giving
     K_BP = 2 and comp sum = 1/3.  Internally consistent in that convention.

  F4-F7 (OK): N=2 SCA fix verified in Vol II, N=4 fix verified,
     N=1 SVir consistent across all locations, N=2 superstring (c->9-c)
     correctly distinguished from N=2 SCA (c->6-c).

References:
  Vol I: w_algebras_deep.tex, w_algebras.tex, thqg_preface_supplement.tex,
         subregular_hook_frontier.tex, standalone/bp_self_duality.tex
  Vol II: examples-worked.tex
  Prior engines: theorem_sca_kappa_fix_engine.py, superconformal_shadow_engine.py
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Optional, Tuple


# ============================================================================
# 1. N=0 Virasoro (baseline)
# ============================================================================

def kappa_vir(c: Fraction) -> Fraction:
    """kappa(Vir_c) = c/2."""
    return c / 2


def vir_koszul_dual_c(c: Fraction) -> Fraction:
    """Virasoro Koszul involution: c -> 26 - c."""
    return 26 - c


def vir_comp_sum(c: Fraction) -> Fraction:
    """kappa(c) + kappa(26-c) = 13."""
    return kappa_vir(c) + kappa_vir(vir_koszul_dual_c(c))


# ============================================================================
# 2. N=1 super-Virasoro (SVir)
# ============================================================================

def kappa_svir(c: Fraction) -> Fraction:
    """kappa(SVir_c) = (3c - 2)/4.

    Decomposition: kappa_bos = c/2 (Virasoro subalgebra)
                   kappa_ferm = (c-2)/4 (super-Mumford correction)
    Total: c/2 + (c-2)/4 = (2c + c - 2)/4 = (3c-2)/4.

    Vanishes at c = 2/3 (analogous to kappa(Vir_0) = 0 at c=0).
    """
    return (3 * c - 2) / 4


def svir_koszul_dual_c(c: Fraction) -> Fraction:
    """N=1 Koszul involution: c -> 15 - c.

    The N=1 superstring critical dimension is c = 15.
    """
    return 15 - c


def svir_comp_sum(c: Fraction) -> Fraction:
    """kappa(SVir_c) + kappa(SVir_{15-c}) = 41/4.

    Proof: (3c-2)/4 + (3(15-c)-2)/4 = (3c-2+43-3c)/4 = 41/4.
    """
    return kappa_svir(c) + kappa_svir(svir_koszul_dual_c(c))


def svir_kappa_decomposition(c: Fraction) -> Dict[str, Fraction]:
    """Decompose kappa(SVir) into bosonic and fermionic parts.

    kappa_bos = c/2 (from the Virasoro subalgebra T)
    kappa_ferm = (c-2)/4 (from the supercurrent G, weight 3/2)
    """
    kappa_bos = c / 2
    kappa_ferm = (c - 2) / 4
    total = kappa_bos + kappa_ferm
    return {
        'kappa_bos': kappa_bos,
        'kappa_ferm': kappa_ferm,
        'total': total,
        'matches_formula': total == kappa_svir(c),
    }


# ============================================================================
# 3. N=2 SCA (from theorem_sca_kappa_fix_engine.py, verified)
# ============================================================================

def n2_central_charge(k: Fraction) -> Fraction:
    """c(N=2 SCA) = 3k/(k+2)."""
    return 3 * k / (k + 2)


def n2_level_from_c(c: Fraction) -> Fraction:
    """k = 2c/(3-c).  Pole at c=3 (free-field limit)."""
    if c == 3:
        raise ValueError("c = 3: free-field limit")
    return 2 * c / (3 - c)


def kappa_n2_from_c(c: Fraction) -> Fraction:
    """kappa(N=2 SCA) = (6-c)/(2(3-c)).

    AP48/AP49: NOT c/2.  The coset subtraction reduces kappa.
    """
    if c == 3:
        raise ValueError("c = 3: pole")
    return (6 - c) / (2 * (3 - c))


def kappa_n2_from_level(k: Fraction) -> Fraction:
    """kappa(N=2 SCA) = (k+4)/4."""
    return (k + 4) / 4


def n2_koszul_dual_c(c: Fraction) -> Fraction:
    """N=2 SCA Koszul involution: c -> 6 - c."""
    return 6 - c


def n2_comp_sum(c: Fraction) -> Fraction:
    """kappa(c) + kappa(6-c) = 1."""
    return kappa_n2_from_c(c) + kappa_n2_from_c(n2_koszul_dual_c(c))


def n2_coset_decomposition(k: Fraction) -> Dict[str, Fraction]:
    """Kazama-Suzuki coset decomposition of kappa(N=2).

    kappa = kappa(sl(2)_k) + kappa(fermion) - kappa(U(1))
          = 3(k+2)/4 + 1/2 - (k/2 + 1) = (k+4)/4.
    """
    kappa_sl2 = Fraction(3) * (k + 2) / 4
    kappa_fermion = Fraction(1, 2)
    kappa_u1 = k / 2 + 1
    total = kappa_sl2 + kappa_fermion - kappa_u1
    return {
        'kappa_sl2': kappa_sl2,
        'kappa_fermion': kappa_fermion,
        'kappa_u1': kappa_u1,
        'total': total,
        'matches_formula': total == kappa_n2_from_level(k),
    }


# ============================================================================
# 4. N=4 small SCA (from theorem_sca_kappa_fix_engine.py, verified)
# ============================================================================

def n4_central_charge(k: Fraction) -> Fraction:
    """c(N=4 small SCA) = 6k."""
    return 6 * k


def kappa_n4_from_level(k: Fraction) -> Fraction:
    """kappa(N=4 small SCA) = 2k.

    5-path verified.  AP48: NOT c/2 = 3k.
    """
    return 2 * k


def kappa_n4_from_c(c: Fraction) -> Fraction:
    """kappa(N=4 small SCA) = c/3."""
    return c / 3


def n4_koszul_dual_c(c: Fraction) -> Fraction:
    """N=4 small SCA Koszul involution: c -> -c - 24.

    FF involution on su(2) R-symmetry: k -> -k-4 (h^v = 2).
    Via c = 6k: c' = 6(-k-4) = -c - 24.
    Self-dual point: c = -12.
    """
    return -c - 24


def n4_comp_sum_ff(c: Fraction) -> Fraction:
    """kappa(c) + kappa(-c-24) = -8 (FF involution)."""
    return kappa_n4_from_c(c) + kappa_n4_from_c(n4_koszul_dual_c(c))


def n4_comp_sum_cy(k: Fraction) -> Fraction:
    """kappa(k) + kappa(-k) = 0 (CY sigma-model duality).

    This is a DIFFERENT duality from FF: k -> -k (not k -> -k-4).
    Applies only to the geometric realization (K3 sigma model).
    """
    return kappa_n4_from_level(k) + kappa_n4_from_level(-k)


# ============================================================================
# 5. Bershadsky-Polyakov W(sl_3, f_min)
# ============================================================================

def bp_central_charge(k: Fraction) -> Fraction:
    """BP central charge in the FKR (Fehily-Kawasetsu-Ridout) convention.

    c(k) = 2 - 24(k+1)^2/(k+3).

    This is the authoritative convention used in the monograph's main
    computation (comp:bp-kappa-three-paths) and the standalone paper.

    Pole at k = -3 (critical level of sl_3).
    Collapsing level k = -1 gives c = 2 = dim(g_0^f).
    """
    if k == -3:
        raise ValueError("k = -3: critical level (pole)")
    return Fraction(2) - Fraction(24) * (k + 1) ** 2 / (k + 3)


def bp_varrho() -> Fraction:
    """Anomaly ratio of BP = 1/6.

    Generators: J (h=1, bos), G+ (h=3/2, ferm), G- (h=3/2, ferm), T (h=2, bos).
    varrho = sum_i (-1)^{p_i} / h_i
           = 1/1 - 1/(3/2) - 1/(3/2) + 1/2
           = 1 - 2/3 - 2/3 + 1/2
           = 1/6.

    CAUTION (F2): The standalone paper (bp_self_duality.tex line 328) uses
    the UNSIGNED formula sum 1/(2h_i) = 1/2 + 1/3 + 1/3 + 1/4 = 17/12.
    This is WRONG for the anomaly ratio.  The correct signed formula gives 1/6.
    The standalone uses kappa_T = c/2 (T-line projection) throughout, so the
    wrong rho value is never used for kappa.  But the formula is incorrect.
    """
    return Fraction(1, 6)


def bp_varrho_unsigned() -> Fraction:
    """WRONG unsigned anomaly ratio = 17/12.

    This is the value in standalone/bp_self_duality.tex line 328.
    It uses sum 1/(2h_i) instead of the correct signed formula.
    Preserved here for testing that we detect this error.
    """
    return Fraction(17, 12)


def kappa_bp(k: Fraction) -> Fraction:
    """kappa(BP_k) = varrho * c = c(k)/6.

    The full modular characteristic of the BP algebra.
    NOT c/2 (which is kappa_T, the T-line Virasoro projection).
    """
    return bp_varrho() * bp_central_charge(k)


def kappa_bp_t_line(k: Fraction) -> Fraction:
    """kappa_T(BP_k) = c(k)/2.

    The T-line shadow projection: the modular characteristic restricted
    to the Virasoro subalgebra (T generator only).  This is what the
    standalone paper computes.  It equals the Virasoro kappa at the
    same central charge.
    """
    return bp_central_charge(k) / 2


def bp_ff_dual_level(k: Fraction) -> Fraction:
    """FF dual level for BP: k' = -k - 6 (since h^v(sl_3) = 3)."""
    return -k - 6


def bp_koszul_conductor(k: Fraction) -> Fraction:
    """K_BP = c(k) + c(-k-6) = 196 (FKR convention).

    FINDING F1 (SERIOUS): prop:bp-complementarity-constant in
    subregular_hook_frontier.tex claims K_BP = 76 using the WRONG
    formula c = 2 - 3(2k+3)^2/(k+3).  The correct value is 196.
    This contradicts comp:bp-kappa-three-paths in the SAME FILE.
    """
    kp = bp_ff_dual_level(k)
    return bp_central_charge(k) + bp_central_charge(kp)


def bp_comp_sum(k: Fraction) -> Fraction:
    """kappa(k) + kappa(-k-6) = varrho * K = 196/6 = 98/3."""
    kp = bp_ff_dual_level(k)
    return kappa_bp(k) + kappa_bp(kp)


def bp_comp_sum_t_line(k: Fraction) -> Fraction:
    """kappa_T(k) + kappa_T(-k-6) = K/2 = 98.

    This is the T-LINE complementarity, NOT the full algebra's.
    The standalone paper computes this quantity.
    """
    kp = bp_ff_dual_level(k)
    return kappa_bp_t_line(k) + kappa_bp_t_line(kp)


def bp_wrong_central_charge(k: Fraction) -> Fraction:
    """WRONG BP central charge used in prop:bp-complementarity-constant proof.

    c = 2 - 3(2k+3)^2/(k+3).

    This is in NO consistent convention:
    - At k=-1 (collapsing level), gives c = 1/2 instead of correct c = 2.
    - Gives K = 76 instead of correct K = 196.

    Preserved here for testing that we detect this error.
    """
    if k == -3:
        raise ValueError("k = -3: pole")
    return Fraction(2) - Fraction(3) * (2 * k + 3) ** 2 / (k + 3)


def bp_wrong_koszul_conductor(k: Fraction) -> Fraction:
    """WRONG K_BP = 76 from the wrong formula. For testing."""
    kp = bp_ff_dual_level(k)
    return bp_wrong_central_charge(k) + bp_wrong_central_charge(kp)


# ============================================================================
# 6. The superconformal complementarity hierarchy
# ============================================================================

def superconformal_hierarchy() -> Dict[str, Dict[str, object]]:
    """The complete superconformal complementarity hierarchy.

    N=0 (Vir):   c -> 26-c,   self-dual c=13,  kappa+kappa'=13,    W-type
    N=1 (SVir):  c -> 15-c,   self-dual c=15/2, kappa+kappa'=41/4, W-type
    N=2 (SCA):   c -> 6-c,    self-dual c=3,    kappa+kappa'=1,    W-type
    N=4 (small): c -> -c-24,  self-dual c=-12,  kappa+kappa'=-8,   W-type

    The sequence 13 > 41/4 > 1 > -8 is strictly decreasing.
    ALL are W-type (nonzero complementarity sum).
    """
    return {
        'N0_Vir': {
            'kappa_fn': kappa_vir,
            'dual_c_fn': vir_koszul_dual_c,
            'self_dual_c': Fraction(13),
            'comp_sum': Fraction(13),
        },
        'N1_SVir': {
            'kappa_fn': kappa_svir,
            'dual_c_fn': svir_koszul_dual_c,
            'self_dual_c': Fraction(15, 2),
            'comp_sum': Fraction(41, 4),
        },
        'N2_SCA': {
            'kappa_fn': kappa_n2_from_c,
            'dual_c_fn': n2_koszul_dual_c,
            'self_dual_c': Fraction(3),
            'comp_sum': Fraction(1),
        },
        'N4_small': {
            'kappa_fn': kappa_n4_from_c,
            'dual_c_fn': n4_koszul_dual_c,
            'self_dual_c': Fraction(-12),
            'comp_sum': Fraction(-8),
        },
    }


def hierarchy_comp_sums_decreasing() -> bool:
    """Verify the comp sums form a strictly decreasing sequence."""
    sums = [Fraction(13), Fraction(41, 4), Fraction(1), Fraction(-8)]
    return all(sums[i] > sums[i + 1] for i in range(len(sums) - 1))


# ============================================================================
# 7. Cross-volume consistency checks
# ============================================================================

def check_n2_cross_volume() -> Dict[str, object]:
    """Verify N=2 SCA kappa is consistent across volumes.

    Vol I (w_algebras_deep.tex): kappa = (6-c)/(2(3-c)) = (k+4)/4
    Vol II (examples-worked.tex): same formula (FIXED from prior c/2 error)

    At c=1 (k=1): kappa = 5/4 (NOT 1/2 = c/2).
    """
    c = Fraction(1)
    k = n2_level_from_c(c)
    kappa_from_c = kappa_n2_from_c(c)
    kappa_from_k = kappa_n2_from_level(k)
    coset = n2_coset_decomposition(k)
    wrong_virasoro = c / 2
    return {
        'c': c,
        'k': k,
        'kappa_from_c': kappa_from_c,
        'kappa_from_k': kappa_from_k,
        'kappa_coset': coset['total'],
        'all_agree': kappa_from_c == kappa_from_k == coset['total'],
        'wrong_virasoro_value': wrong_virasoro,
        'correctly_differs_from_virasoro': kappa_from_c != wrong_virasoro,
    }


def check_n4_cross_volume() -> Dict[str, object]:
    """Verify N=4 small SCA kappa is consistent across volumes.

    At c=6 (k=1): kappa = 2 (NOT 3 = c/2).
    Duality: c -> -c-24 (NOT c -> 12-c).
    """
    k = Fraction(1)
    c = n4_central_charge(k)
    kappa_from_k = kappa_n4_from_level(k)
    kappa_from_c = kappa_n4_from_c(c)
    wrong = c / 2
    return {
        'c': c,
        'k': k,
        'kappa_from_k': kappa_from_k,
        'kappa_from_c': kappa_from_c,
        'agree': kappa_from_k == kappa_from_c,
        'wrong_virasoro': wrong,
        'correctly_differs': kappa_from_k != wrong,
        'correct_dual_c': n4_koszul_dual_c(c),
        'wrong_dual_c': 12 - c,
        'duality_correct': n4_koszul_dual_c(c) == Fraction(-30),
    }


def check_bp_intra_file_contradiction() -> Dict[str, object]:
    """Detect the intra-file contradiction in subregular_hook_frontier.tex.

    comp:bp-kappa-three-paths (line ~941) says K_BP = 196.
    prop:bp-complementarity-constant (line ~961) says K_BP = 76.
    Both are in the SAME FILE.

    Root cause: the proof of prop uses the WRONG formula
    c = 2 - 3(2k+3)^2/(k+3) instead of c = 2 - 24(k+1)^2/(k+3).
    """
    results = {}
    for k_val in [0, 1, 2, 5, -1, -2]:
        k = Fraction(k_val)
        K_correct = bp_koszul_conductor(k)
        K_wrong = bp_wrong_koszul_conductor(k)
        results[f'k={k_val}'] = {
            'K_correct': K_correct,
            'K_wrong': K_wrong,
            'correct_is_196': K_correct == 196,
            'wrong_is_76': K_wrong == 76,
        }
    return results


def check_bp_collapsing_level() -> Dict[str, object]:
    """At the collapsing level k=-1, c should equal dim(g_0^f) = 2.

    The wrong formula gives c = 1/2 instead.
    """
    k = Fraction(-1)
    c_correct = bp_central_charge(k)
    c_wrong = bp_wrong_central_charge(k)
    return {
        'k': k,
        'c_correct': c_correct,
        'c_wrong': c_wrong,
        'correct_is_2': c_correct == 2,
        'wrong_is_half': c_wrong == Fraction(1, 2),
    }


def check_bp_anomaly_ratio() -> Dict[str, object]:
    """Verify the signed anomaly ratio = 1/6, detecting the wrong 17/12.

    Generators: J (h=1, bos, p=0), G+ (h=3/2, ferm, p=1),
                G- (h=3/2, ferm, p=1), T (h=2, bos, p=0).
    """
    generators = [
        ('J', Fraction(1), 0),     # (name, weight, parity)
        ('G+', Fraction(3, 2), 1),
        ('G-', Fraction(3, 2), 1),
        ('T', Fraction(2), 0),
    ]
    signed_sum = sum((-1) ** p / h for _, h, p in generators)
    unsigned_sum = sum(Fraction(1) / (2 * h) for _, h, _ in generators)
    return {
        'signed_varrho': signed_sum,
        'unsigned_rho': unsigned_sum,
        'signed_is_1_6': signed_sum == Fraction(1, 6),
        'unsigned_is_17_12': unsigned_sum == Fraction(17, 12),
        'they_differ': signed_sum != unsigned_sum,
    }


# ============================================================================
# 8. AP48 verification: kappa != c/2 for non-Virasoro families
# ============================================================================

def ap48_kappa_not_c_over_2() -> Dict[str, Dict[str, object]]:
    """Verify kappa != c/2 for all non-Virasoro superconformal families.

    For EACH family, check that the correct kappa differs from c/2.
    The only family where kappa = c/2 is Virasoro itself (AP48).
    """
    results = {}

    # N=1 SVir at c=15/2 (self-dual)
    c = Fraction(15, 2)
    results['SVir_c=15/2'] = {
        'kappa': kappa_svir(c),
        'c_over_2': c / 2,
        'differs': kappa_svir(c) != c / 2,
    }

    # N=2 SCA at c=1
    c = Fraction(1)
    results['N2_c=1'] = {
        'kappa': kappa_n2_from_c(c),
        'c_over_2': c / 2,
        'differs': kappa_n2_from_c(c) != c / 2,
    }

    # N=4 small at c=6
    c = Fraction(6)
    results['N4_c=6'] = {
        'kappa': kappa_n4_from_c(c),
        'c_over_2': c / 2,
        'differs': kappa_n4_from_c(c) != c / 2,
    }

    # BP at k=1
    k = Fraction(1)
    c = bp_central_charge(k)
    results['BP_k=1'] = {
        'kappa': kappa_bp(k),
        'c_over_2': c / 2,
        'differs': kappa_bp(k) != c / 2,
    }

    return results


# ============================================================================
# 9. Multi-path kappa verification for each family
# ============================================================================

def multipath_svir(c: Fraction) -> Dict[str, object]:
    """Multi-path verification of N=1 SVir kappa.

    Path 1: Direct formula (3c-2)/4
    Path 2: Decomposition kappa_bos + kappa_ferm
    Path 3: Complementarity check (sum = 41/4)
    """
    path1 = kappa_svir(c)
    decomp = svir_kappa_decomposition(c)
    path2 = decomp['total']
    comp = svir_comp_sum(c)
    return {
        'path1_formula': path1,
        'path2_decomposition': path2,
        'paths_agree': path1 == path2,
        'comp_sum': comp,
        'comp_is_41_4': comp == Fraction(41, 4),
    }


def multipath_bp(k: Fraction) -> Dict[str, object]:
    """Multi-path verification of BP kappa.

    Path 1: kappa = varrho * c = c/6
    Path 2: Verify K = 196 (level-independent)
    Path 3: Complementarity sum = 98/3
    Path 4: At k=-1 (collapsing level), c = 2
    """
    path1 = kappa_bp(k)
    path2_K = bp_koszul_conductor(k)
    path3_comp = bp_comp_sum(k)
    return {
        'kappa': path1,
        'kappa_equals_c_6': path1 == bp_central_charge(k) / 6,
        'K': path2_K,
        'K_is_196': path2_K == 196,
        'comp_sum': path3_comp,
        'comp_is_98_3': path3_comp == Fraction(98, 3),
    }
