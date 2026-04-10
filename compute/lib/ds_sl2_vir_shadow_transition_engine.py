r"""DS sl_2 -> Vir shadow transition engine: S_2, S_3, S_4, Delta tracking.

Tracks the shadow invariants S_2, S_3, S_4, and the discriminant
Delta = 8*kappa*S_4 through the principal Drinfeld-Sokolov reduction
V_k(sl_2) -> Vir_c, verifying the class L -> class M transition.

The structural content: V_k(sl_2) is class L (shadow depth 3, S_4 = 0)
while its DS image Vir_c is class M (shadow depth infinity, S_4 != 0).
The BRST ghost coupling creates the quartic seed S_4 = 10/(c(5c+22))
from zero inputs, which then cascades to all higher arities.

FORMULAS (all from landscape_census.tex and ds_shadow_cascade_engine.py):

  V_k(sl_2):
    dim(sl_2) = 3, h^v = 2
    c_Sug(k) = 3k/(k+2)                          [Sugawara]
    kappa(k) = 3(k+2)/4                           [C3: dim(g)(k+h^v)/(2h^v)]
    alpha = 1                                      [Killing cubic = Lie bracket]
    S_4 = 0                                        [Jacobi kills quartic for KM]
    Delta = 0                                      [class L]

  DS map: c(k) = 1 - 6(k+1)^2/(k+2)              [Fateev-Lukyanov N=2]

  Vir_c:
    kappa(c) = c/2                                 [C2]
    alpha = 2                                      [Virasoro cubic shadow]
    S_4(c) = 10/(c(5c+22))                         [quartic contact invariant]
    S_5(c) = -48/(c^2(5c+22))                      [quintic, from cascade]
    Delta(c) = 8*(c/2)*S_4 = 40/(5c+22)           [C30: Delta = 8*kappa*S_4]

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:ds-central-charge-additivity (higher_genus_modular_koszul.tex)
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    landscape_census.tex: kappa formulas C1-C4, r-matrix C9-C11
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union


# ============================================================================
# 1. Central charge formulas
# ============================================================================

def c_sugawara_sl2(k: Fraction) -> Fraction:
    r"""Sugawara central charge for V_k(sl_2).

    c = k * dim(sl_2) / (k + h^v) = 3k/(k+2).

    Checks: k=1 -> 1; k=0 -> 0; k=-2 -> critical (undefined).
    """
    k = Fraction(k)
    denom = k + 2
    if denom == 0:
        raise ValueError("Critical level k=-2: Sugawara undefined")
    return 3 * k / denom


def c_ds_sl2_to_vir(k: Fraction) -> Fraction:
    r"""Central charge of Vir from DS reduction of V_k(sl_2).

    Fateev-Lukyanov formula (N=2):
      c(k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
           = 1 - 6(k+1)^2/(k+2)

    Source: wn_central_charge_canonical.py (canonical single source of truth).

    Checks:
      k=1 -> 1 - 6*4/3 = 1 - 8 = -7.
      k=0 -> 1 - 6/2 = 1 - 3 = -2.
      k=-1 -> 1 - 0 = 1.
      Complementarity: c(k) + c(-k-4) = 26.
    """
    k = Fraction(k)
    denom = k + 2
    if denom == 0:
        raise ValueError("Critical level k=-2: DS undefined")
    return Fraction(1) - 6 * (k + 1) ** 2 / denom


# ============================================================================
# 2. Kappa formulas
# ============================================================================

def kappa_km_sl2(k: Fraction) -> Fraction:
    r"""Modular characteristic kappa for V_k(sl_2).

    kappa = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4.

    Source: landscape_census.tex, C3.
    Checks: k=0 -> 3/2; k=-2 -> 0 (critical); k=1 -> 9/4.
    """
    k = Fraction(k)
    return Fraction(3) * (k + 2) / Fraction(4)


def kappa_vir(c: Fraction) -> Fraction:
    r"""Modular characteristic kappa for Vir_c.

    kappa = c/2.

    Source: landscape_census.tex, C2.
    Checks: c=0 -> 0; c=13 -> 13/2 (self-dual); c=26 -> 13.
    """
    c = Fraction(c)
    return c / 2


# ============================================================================
# 3. Shadow invariants for V_k(sl_2) -- class L
# ============================================================================

def s2_km(k: Fraction) -> Fraction:
    r"""S_2 for V_k(sl_2). S_2 = kappa = 3(k+2)/4.

    The quadratic shadow invariant equals kappa for all families.
    """
    return kappa_km_sl2(k)


def s3_km(k: Fraction) -> Fraction:
    r"""S_3 (alpha) for V_k(sl_2). alpha = 1.

    The cubic shadow invariant for affine Kac-Moody algebras equals 1,
    arising from the Killing form structure constants (universal for all
    simple Lie algebras, independent of rank and level).
    """
    return Fraction(1)


def s4_km(k: Fraction) -> Fraction:
    r"""S_4 for V_k(sl_2). S_4 = 0.

    The quartic shadow vanishes for ALL affine Kac-Moody algebras:
    the graded Jacobi identity on the Lie bracket kills the quartic
    contact invariant. This is the defining property of class L.
    """
    return Fraction(0)


def delta_km(k: Fraction) -> Fraction:
    r"""Discriminant Delta for V_k(sl_2).

    Delta = 8 * kappa * S_4 = 0  (since S_4 = 0).

    Delta = 0 is the defining condition for the shadow tower to terminate
    (classes G and L). Source: C30.
    """
    return 8 * kappa_km_sl2(k) * s4_km(k)


# ============================================================================
# 4. Shadow invariants for Vir_c -- class M
# ============================================================================

def s2_vir(c: Fraction) -> Fraction:
    r"""S_2 for Vir_c. S_2 = kappa = c/2."""
    return kappa_vir(c)


def s3_vir(c: Fraction) -> Fraction:
    r"""S_3 (alpha) for Vir_c. alpha = 2.

    The cubic shadow invariant for Virasoro equals 2, arising from the
    T(z)T(w) OPE structure: the cubic pole coefficient 2T(w) determines
    alpha = 2. Universal (independent of c).
    """
    return Fraction(2)


def s4_vir(c: Fraction) -> Fraction:
    r"""S_4 for Vir_c. S_4 = 10 / (c * (5c + 22)).

    Source: ds_shadow_cascade_engine.py, WN_shadow_data_T_line (N=2 case).
    Also: rem:virasoro-resonance-model, w_algebras_deep.tex.

    Checks:
      c=1 -> 10/27.
      c=13 -> 10/1131.
      c=1/2 -> 40/49.
    Singular at c=0 and c=-22/5.
    """
    c = Fraction(c)
    if c == 0:
        raise ValueError("S_4 singular at c=0")
    denom = c * (5 * c + 22)
    if denom == 0:
        raise ValueError(f"S_4 singular: 5c+22=0 at c={c}")
    return Fraction(10) / denom


def s5_vir(c: Fraction) -> Fraction:
    r"""S_5 for Vir_c. S_5 = -48 / (c^2 * (5c + 22)).

    Source: ds_shadow_cascade_engine.py, cascade_verification (N=2 cross-check).

    Checks:
      c=1 -> -48/27 = -16/9.
      c=13 -> -48/(169*87) = -16/4901.
    """
    c = Fraction(c)
    if c == 0:
        raise ValueError("S_5 singular at c=0")
    denom = c ** 2 * (5 * c + 22)
    if denom == 0:
        raise ValueError(f"S_5 singular at c={c}")
    return Fraction(-48) / denom


def delta_vir(c: Fraction) -> Fraction:
    r"""Discriminant Delta for Vir_c.

    Delta = 8 * kappa * S_4 = 8 * (c/2) * 10/(c(5c+22)) = 40/(5c+22).

    Source: C30 (Delta = 8*kappa*S_4, LINEAR in kappa).

    Checks:
      c=1 -> 40/27.
      c=13 -> 40/87.
      c=1/2 -> 80/49.
    Delta != 0 for generic c: class M (infinite shadow tower).
    Delta = 0 only at c = -22/5 (singular, not in standard landscape).
    """
    c = Fraction(c)
    denom = 5 * c + 22
    if denom == 0:
        raise ValueError(f"Delta singular at c={c}")
    return Fraction(40) / denom


# ============================================================================
# 5. Shadow profile: unified interface
# ============================================================================

def shadow_profile_km(k: Fraction) -> Dict[str, Any]:
    r"""Complete shadow profile for V_k(sl_2) at level k.

    Returns dict with S_2, S_3, S_4, Delta, shadow_class, depth.
    """
    k = Fraction(k)
    return {
        'family': 'V_k(sl_2)',
        'parameter': k,
        'c': c_sugawara_sl2(k),
        'kappa': kappa_km_sl2(k),
        'S_2': s2_km(k),
        'S_3': s3_km(k),
        'S_4': s4_km(k),
        'Delta': delta_km(k),
        'shadow_class': 'L',
        'shadow_depth': 3,
        'r_matrix_pole': 1,
    }


def shadow_profile_vir(c: Fraction) -> Dict[str, Any]:
    r"""Complete shadow profile for Vir_c.

    Returns dict with S_2, S_3, S_4, S_5, Delta, shadow_class, depth.
    """
    c = Fraction(c)
    return {
        'family': 'Vir_c',
        'parameter': c,
        'c': c,
        'kappa': kappa_vir(c),
        'S_2': s2_vir(c),
        'S_3': s3_vir(c),
        'S_4': s4_vir(c),
        'S_5': s5_vir(c),
        'Delta': delta_vir(c),
        'shadow_class': 'M',
        'shadow_depth': None,  # infinity
        'r_matrix_pole': 3,
    }


# ============================================================================
# 6. DS transition analysis
# ============================================================================

def verify_class_transition(k: Fraction) -> Dict[str, Any]:
    r"""Verify class L -> M transition under DS(sl_2) at level k.

    Computes shadow profiles for both V_k(sl_2) (source, class L) and
    Vir_{c(k)} (target, class M), and returns a diagnostic comparison.
    """
    k = Fraction(k)

    # Source: V_k(sl_2)
    src = shadow_profile_km(k)

    # DS map
    c_target = c_ds_sl2_to_vir(k)

    # Target: Vir_c
    tgt = shadow_profile_vir(c_target)

    # Transition diagnostics
    return {
        'k': k,
        'c_source': src['c'],
        'c_target': c_target,
        'source': src,
        'target': tgt,
        # Class transition
        'class_source': src['shadow_class'],
        'class_target': tgt['shadow_class'],
        'class_transition': f"{src['shadow_class']} -> {tgt['shadow_class']}",
        'depth_increase': True,  # L(3) -> M(inf)
        # Key invariant changes
        'S_4_created': src['S_4'] == 0 and tgt['S_4'] != 0,
        'Delta_created': src['Delta'] == 0 and tgt['Delta'] != 0,
        'alpha_change': (src['S_3'], tgt['S_3']),
        # r-matrix pole change
        'pole_increase': (src['r_matrix_pole'], tgt['r_matrix_pole']),
    }


def transition_table(k_values: Optional[List[Fraction]] = None) -> List[Dict]:
    r"""Generate a transition comparison table across multiple levels.

    For each level k, shows the source (KM) and target (Vir) shadow profiles
    side by side, highlighting the L -> M transition.
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 3, 5, 10, 20, 50, 100]]

    rows = []
    for kv in k_values:
        trans = verify_class_transition(kv)
        rows.append({
            'k': kv,
            'c_Sug': trans['c_source'],
            'c_DS': trans['c_target'],
            'kappa_KM': trans['source']['kappa'],
            'kappa_Vir': trans['target']['kappa'],
            'S3_KM': trans['source']['S_3'],
            'S3_Vir': trans['target']['S_3'],
            'S4_KM': trans['source']['S_4'],
            'S4_Vir': trans['target']['S_4'],
            'Delta_KM': trans['source']['Delta'],
            'Delta_Vir': trans['target']['Delta'],
            'class_KM': trans['source']['shadow_class'],
            'class_Vir': trans['target']['shadow_class'],
        })
    return rows


# ============================================================================
# 7. Shadow tower computation (convolution recursion)
# ============================================================================

def shadow_tower(kappa_val: Fraction, alpha_val: Fraction,
                 S4_val: Fraction, max_arity: int = 8) -> Dict[int, Fraction]:
    r"""Compute S_2, ..., S_{max_arity} from the shadow metric Q_L.

    Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S_4)*t^2

    S_r = a_{r-2} / r  where  a_n = [t^n] sqrt(Q_L(t)).

    Convolution recursion:
      a_0 = 2*kappa  (signed)
      a_1 = q_1 / (2*a_0)
      a_n = (q_n - sum_{j=1}^{n-1} a_j*a_{n-j}) / (2*a_0)  for n >= 2
    where q_n = 0 for n >= 3 (Q_L is quadratic).

    Source: ds_shadow_cascade_engine.py, shadow_tower_exact.
    """
    kappa_val = Fraction(kappa_val)
    alpha_val = Fraction(alpha_val)
    S4_val = Fraction(S4_val)

    if kappa_val == 0:
        return {r: Fraction(0) for r in range(2, max_arity + 1)}

    q0 = 4 * kappa_val ** 2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val ** 2 + 16 * kappa_val * S4_val

    # a_0 = 2*kappa (signed)
    a0 = 2 * kappa_val
    coeffs = [a0]

    if max_arity >= 3:
        a1 = q1 / (2 * a0)
        coeffs.append(a1)

    if max_arity >= 4:
        a2 = (q2 - a1 ** 2) / (2 * a0)
        coeffs.append(a2)

    for n in range(3, max_arity - 1):
        # q_n = 0 for n >= 3
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv_sum / (2 * a0))

    tower = {}
    for i, a_n in enumerate(coeffs):
        r = i + 2
        tower[r] = a_n / r

    return tower


# ============================================================================
# 8. Full tower comparison
# ============================================================================

def full_tower_comparison(k: Fraction, max_arity: int = 8) -> Dict[str, Any]:
    r"""Compare full shadow towers for V_k(sl_2) and Vir_{c(k)}.

    Computes S_r for r = 2, ..., max_arity for both the source (KM)
    and target (Vir), showing the tower truncation in class L and
    infinite cascade in class M.
    """
    k = Fraction(k)

    # Source: V_k(sl_2) -- class L
    tower_km = shadow_tower(
        kappa_km_sl2(k), s3_km(k), s4_km(k), max_arity)

    # Target: Vir_c -- class M
    c_target = c_ds_sl2_to_vir(k)
    tower_vir = shadow_tower(
        kappa_vir(c_target), s3_vir(c_target), s4_vir(c_target), max_arity)

    comparison = {}
    for r in range(2, max_arity + 1):
        s_km = tower_km.get(r, Fraction(0))
        s_vir = tower_vir.get(r, Fraction(0))
        comparison[r] = {
            'S_r_KM': s_km,
            'S_r_Vir': s_vir,
            'KM_zero': s_km == 0,
            'Vir_zero': s_vir == 0,
        }

    # KM tower truncates: S_r = 0 for r >= 4
    km_truncated = all(
        comparison[r]['KM_zero'] for r in range(4, max_arity + 1))

    # Vir tower cascades: S_r != 0 for all r >= 2
    vir_infinite = all(
        not comparison[r]['Vir_zero'] for r in range(2, max_arity + 1))

    return {
        'k': k,
        'c_target': c_target,
        'tower_km': tower_km,
        'tower_vir': tower_vir,
        'comparison': comparison,
        'km_truncated_at_4': km_truncated,
        'vir_infinite_tower': vir_infinite,
    }


# ============================================================================
# 9. Complementarity check
# ============================================================================

def ds_complementarity(k: Fraction) -> Dict[str, Any]:
    r"""Verify Feigin-Frenkel complementarity: c(k) + c(-k-4) = 26.

    For Virasoro (N=2): the dual level is k' = -k - 2N = -k - 4.
    The Koszul conductor K = c + c' = 26 (= 2(N-1) + 4N(N^2-1) at N=2).
    kappa + kappa' = 13 (Virasoro self-dual point).
    """
    k = Fraction(k)
    k_dual = -k - 4
    c_k = c_ds_sl2_to_vir(k)
    c_k_dual = c_ds_sl2_to_vir(k_dual)

    return {
        'k': k,
        'k_dual': k_dual,
        'c': c_k,
        'c_dual': c_k_dual,
        'c_sum': c_k + c_k_dual,
        'c_sum_is_26': c_k + c_k_dual == 26,
        'kappa': kappa_vir(c_k),
        'kappa_dual': kappa_vir(c_k_dual),
        'kappa_sum': kappa_vir(c_k) + kappa_vir(c_k_dual),
        'kappa_sum_is_13': kappa_vir(c_k) + kappa_vir(c_k_dual) == 13,
    }


# ============================================================================
# 10. Verification
# ============================================================================

def verify_all() -> Dict[str, bool]:
    """Run all verifications. Returns dict of test_name -> pass/fail."""
    results = {}

    # kappa boundary values
    results['kappa_km_k0'] = kappa_km_sl2(Fraction(0)) == Fraction(3, 2)
    results['kappa_km_k_crit'] = kappa_km_sl2(Fraction(-2)) == Fraction(0)

    # DS central charge checks
    results['ds_c_k1'] = c_ds_sl2_to_vir(Fraction(1)) == Fraction(-7)
    results['ds_c_k0'] = c_ds_sl2_to_vir(Fraction(0)) == Fraction(-2)
    results['ds_c_k_neg1'] = c_ds_sl2_to_vir(Fraction(-1)) == Fraction(1)

    # S_4 checks
    results['s4_vir_c1'] = s4_vir(Fraction(1)) == Fraction(10, 27)
    results['s4_km_zero'] = s4_km(Fraction(5)) == Fraction(0)

    # Delta checks
    results['delta_km_zero'] = delta_km(Fraction(5)) == Fraction(0)
    results['delta_vir_c1'] = delta_vir(Fraction(1)) == Fraction(40, 27)
    results['delta_vir_c13'] = delta_vir(Fraction(13)) == Fraction(40, 87)

    # Class transition
    for kv in [Fraction(1), Fraction(5), Fraction(10)]:
        trans = verify_class_transition(kv)
        results[f'transition_k{kv}'] = (
            trans['class_source'] == 'L' and
            trans['class_target'] == 'M' and
            trans['S_4_created'] and
            trans['Delta_created']
        )

    # Complementarity
    for kv in [Fraction(1), Fraction(5), Fraction(10)]:
        comp = ds_complementarity(kv)
        results[f'complementarity_k{kv}'] = (
            comp['c_sum_is_26'] and comp['kappa_sum_is_13']
        )

    # Tower truncation/cascade
    ftc = full_tower_comparison(Fraction(5), 8)
    results['km_tower_truncated'] = ftc['km_truncated_at_4']
    results['vir_tower_infinite'] = ftc['vir_infinite_tower']

    return results


if __name__ == '__main__':
    print("=" * 60)
    print("DS sl_2 -> Vir SHADOW TRANSITION ENGINE")
    print("=" * 60)

    print("\n--- Verification ---")
    for name, ok in verify_all().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Transition table (selected levels) ---")
    for row in transition_table():
        print(f"  k={row['k']:>4}: class {row['class_KM']} -> {row['class_Vir']}, "
              f"S4: {float(row['S4_KM']):.4f} -> {float(row['S4_Vir']):.6f}, "
              f"Delta: {float(row['Delta_KM']):.4f} -> {float(row['Delta_Vir']):.6f}")
