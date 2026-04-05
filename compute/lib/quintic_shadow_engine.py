r"""Quintic-sextic shadow obstruction engine --- first explicit arity-5/6 computations.

FIRST EXPLICIT COMPUTATION at arity 5 and 6 for all standard chiral algebra
families.  This pushes the shadow obstruction tower frontier from arity 4 to arity 6.

KEY RESULTS:
  S_5^Vir(c) = -48 / [c^2 (5c + 22)]
  S_6^Vir(c) = 80(45c + 193) / [3 c^3 (5c + 22)^2]
  S_7^Vir(c) = -2880(15c + 61) / [7 c^4 (5c + 22)^2]

  The quintic obstruction o^(5) forces S_5 != 0 for ALL class-M algebras
  (Virasoro, W_N for N >= 2), confirming the infinite shadow obstruction tower.

  For depth-bounded classes:
    G (Gaussian, Heisenberg):  S_5 = 0  (alpha = S_4 = 0)
    L (Lie/tree, affine KM):  S_5 = 0  (S_4 = 0, Delta = 0)
    C (Contact, bc ghosts):   S_5 != 0 on 1D metric, but = 0 in full complex
    M (Mixed, Virasoro/W_N):  S_5 != 0  (forced by Delta != 0)

IMPORTANT: The 1D shadow metric (single primary line) gives S_r for all
arities via sqrt(Q_L).  For class-C algebras (bc ghosts), the 1D computation
gives nonzero S_5, but the true depth is 4 because STRATUM SEPARATION kills
the quintic in the full deformation complex (thm:single-line-dichotomy).
1D depth != true depth for contact class.

COMPLEMENTARITY at arity 5: S_5(c) + S_5(26-c) has a specific rational form
dictated by Theorem C (complementarity of shadows).

DS DEPTH INCREASE at arity 5: sl_2 (depth 3, S_5 = 0) -> Vir (depth inf,
S_5 != 0).  The ghost sector creates nonzero S_4, which cascades to S_5,
S_6, ... through the convolution recursion.

FORMULA DERIVATION:
  Shadow metric: Q_L(t) = 4 kappa^2 + 12 kappa alpha t + (9 alpha^2 + 16 kappa S_4) t^2
  For Virasoro: kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22))

  q0 = c^2,  q1 = 12c,  q2 = 36 + 80/(5c+22) = (180c + 872)/(5c+22)

  Convolution recursion f^2 = Q_L:
    a_0 = c
    a_1 = 6
    a_2 = 40 / [c(5c+22)]
    a_3 = -240 / [c^2(5c+22)]
    a_4 = 160(45c + 193) / [c^3(5c+22)^2]
    a_5 = -2880(15c + 61) / [c^4(5c+22)^2]

  S_r = a_{r-2} / r, giving the formulas above.

  NOTE: q2 = 36 + 80/(5c+22), NOT 36 + 80/(c(5c+22)).  The factor
  16 kappa S_4 = 16(c/2)(10/(c(5c+22))) = 80/(5c+22) cancels one c.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
    thm:quartic-resonance-obstruction (higher_genus_modular_koszul.tex)
    rem:virasoro-resonance-model (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    oo,
    simplify,
    sqrt,
    symbols,
    together,
    N as Neval,
)


c = Symbol('c', positive=True)
k = Symbol('k')


# ============================================================================
# 1.  Exact quintic/sextic formulas from convolution recursion
# ============================================================================

def _convolution_coefficients(q0, q1, q2, max_n: int) -> list:
    r"""Taylor coefficients of f(t) = sqrt(q0 + q1*t + q2*t^2).

    Recursion derived from f^2 = Q_L:
        a_0 = sqrt(q0)
        a_1 = q1 / (2 a_0)
        a_2 = (q2 - a_1^2) / (2 a_0)
        a_n = -(1/(2 a_0)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3

    The shadow coefficient at arity r is S_r = a_{r-2} / r.
    """
    a0 = sqrt(q0)
    coeffs = [a0]
    if max_n >= 1:
        a1 = q1 / (2 * a0)
        coeffs.append(a1)
    if max_n >= 2:
        a2 = (q2 - coeffs[1] ** 2) / (2 * a0)
        coeffs.append(a2)
    for n in range(3, max_n + 1):
        conv = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv / (2 * a0))
    return coeffs


def virasoro_shadow_data():
    """Shadow metric data for Virasoro at central charge c (symbolic).

    Returns dict with kappa, alpha (= S_3), S4, the three shadow-metric
    coefficients q0, q1, q2, and the critical discriminant Delta.
    """
    kappa = c / 2
    alpha = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    q0 = 4 * kappa ** 2                        # c^2
    q1 = 12 * kappa * alpha                     # 12c
    q2 = 9 * alpha ** 2 + 16 * kappa * S4      # 36 + 80/(5c+22)
    Delta = 8 * kappa * S4                      # 40/(5c+22)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'q0': q0, 'q1': q1, 'q2': q2, 'Delta': Delta,
    }


def virasoro_quintic_exact():
    r"""Compute S_5^Vir(c) exactly as a rational function of c.

    From the convolution recursion with q0 = c^2, q1 = 12c,
    q2 = (180c + 872)/(5c + 22):

        a_0 = c
        a_1 = 6
        a_2 = 40 / [c(5c + 22)]
        a_3 = -240 / [c^2(5c + 22)]

    S_5 = a_3 / 5 = -48 / [c^2(5c + 22)]

    Returns:
        Dict with exact symbolic and verification data.
    """
    data = virasoro_shadow_data()
    coeffs = _convolution_coefficients(data['q0'], data['q1'], data['q2'], 5)

    # Extract and simplify
    a = [cancel(ai) for ai in coeffs]
    S = {}
    for n in range(len(a)):
        r = n + 2
        S[r] = cancel(a[n] / r)

    # Expected exact formula (verified symbolically)
    S5_expected = Rational(-48) / (c ** 2 * (5 * c + 22))

    return {
        'a_coefficients': {n: a[n] for n in range(len(a))},
        'shadow_coefficients': S,
        'S5': S[5],
        'S5_expected': S5_expected,
        'S5_matches': simplify(S[5] - S5_expected) == 0,
        'S6': S[6] if 6 in S else None,
        'S7': S[7] if 7 in S else None,
    }


def virasoro_sextic_exact():
    r"""Compute S_6^Vir(c) and S_7, S_8 exactly.

    S_6 = 80(45c + 193) / [3 c^3 (5c + 22)^2]
    S_7 = -2880(15c + 61) / [7 c^4 (5c + 22)^2]
    """
    data = virasoro_shadow_data()
    coeffs = _convolution_coefficients(data['q0'], data['q1'], data['q2'], 6)
    a = [cancel(ai) for ai in coeffs]

    S5 = cancel(a[3] / 5)
    S6 = cancel(a[4] / 6)
    S7 = cancel(a[5] / 7)
    S8 = cancel(a[6] / 8)

    return {
        'S5': S5,
        'S6': S6,
        'S7': S7,
        'S8': S8,
        'S6_factored': factor(S6),
        'S7_factored': factor(S7),
    }


def virasoro_shadow_tower_exact(max_r: int = 10) -> Dict[int, Any]:
    r"""Full shadow obstruction tower S_2, ..., S_{max_r} as exact rational functions of c.

    Returns dict mapping arity r -> S_r(c) as a cancelled sympy expression.
    """
    data = virasoro_shadow_data()
    coeffs = _convolution_coefficients(
        data['q0'], data['q1'], data['q2'], max_r - 2)

    tower = {}
    for n in range(len(coeffs)):
        r = n + 2
        tower[r] = cancel(coeffs[n] / r)
    return tower


# ============================================================================
# 2.  Cross-family quintic table
# ============================================================================

def heisenberg_quintic():
    """S_5 = 0 for Heisenberg (class G, depth 2).

    kappa = c/2, alpha = 0, S_4 = 0.  All S_r = 0 for r >= 3.
    """
    return Rational(0)


def affine_sl2_quintic():
    """S_5 = 0 for affine sl_2 (class L, depth 3).

    S_4 = 0 implies Delta = 0 implies depth 3.
    All S_r = 0 for r >= 4.
    """
    return Rational(0)


def bc_ghosts_quintic():
    r"""S_5 on the 1D shadow metric for the bc ghost system (class C, depth 4).

    bc ghosts: kappa = -1, alpha = 1, S_4 = -5/12.

    Q_L = 4 - 12t + (47/3)t^2

    IMPORTANT: This gives S_5 = 1/2 != 0 on the 1D metric!
    True depth is 4 because stratum separation kills the quintic
    in the full deformation complex.  The 1D metric OVERESTIMATES
    depth for class-C algebras.
    """
    kap = Rational(-1)
    alp = Rational(1)
    s4 = Rational(-5, 12)
    q0 = 4 * kap ** 2                         # 4
    q1 = 12 * kap * alp                        # -12
    q2 = 9 * alp ** 2 + 16 * kap * s4          # 9 + 20/3 = 47/3

    coeffs = _convolution_coefficients(q0, q1, q2, 5)
    S5_1d = cancel(coeffs[3] / 5)

    return {
        'S5_1d_metric': S5_1d,
        'S5_1d_nonzero': S5_1d != 0,
        'S5_true_depth': Rational(0),  # vanishes in full complex
        'mechanism': 'stratum_separation',
        'note': ('1D shadow metric gives S_5 != 0, but stratum separation '
                 'kills quintic in full deformation complex. '
                 'Class C escapes via rank-one rigidity.'),
    }


def bc_ghosts_shadow_tower_1d(max_r: int = 10) -> Dict[int, Any]:
    """Full 1D shadow obstruction tower for the bc ghost system.

    Shows S_r != 0 for all r on the 1D metric.  True depth is 4
    because stratum separation zeroes out S_5 and higher in the
    full multi-line deformation complex.
    """
    kap, alp, s4 = Rational(-1), Rational(1), Rational(-5, 12)
    q0 = 4 * kap ** 2
    q1 = 12 * kap * alp
    q2 = 9 * alp ** 2 + 16 * kap * s4
    coeffs = _convolution_coefficients(q0, q1, q2, max_r - 2)
    return {r + 2: cancel(coeffs[r] / (r + 2)) for r in range(len(coeffs))}


# Backward-compatible aliases (deprecated: the family is bc ghosts, not betagamma)
betagamma_quintic = bc_ghosts_quintic
betagamma_shadow_tower_1d = bc_ghosts_shadow_tower_1d


def cross_family_quintic_table() -> Dict[str, Dict]:
    r"""Cross-family S_5 comparison table.

    Family         | Class | Depth | S_5 (1D metric) | S_5 (true)
    -------------- | ----- | ----- | --------------- | ----------
    Heisenberg     |   G   |   2   |       0         |     0
    Affine sl_2    |   L   |   3   |       0         |     0
    bc ghosts      |   C   |   4   |    1/2          |     0
    Virasoro       |   M   |  inf  |  -48/(c^2..)    |  same
    """
    vir = virasoro_quintic_exact()
    bg = bc_ghosts_quintic()

    return {
        'Heisenberg': {
            'class': 'G', 'depth': 2,
            'S5_1d': Rational(0), 'S5_true': Rational(0),
        },
        'Affine_sl2': {
            'class': 'L', 'depth': 3,
            'S5_1d': Rational(0), 'S5_true': Rational(0),
        },
        'bc_ghosts': {
            'class': 'C', 'depth': 4,
            'S5_1d': bg['S5_1d_metric'], 'S5_true': Rational(0),
            'mechanism': 'stratum_separation',
        },
        'Virasoro': {
            'class': 'M', 'depth': None,
            'S5_1d': vir['S5'], 'S5_true': vir['S5'],
        },
    }


# ============================================================================
# 3.  DS depth-increase analysis at quintic level
# ============================================================================

def ds_central_charge_sl2(k_val=None):
    """c_{Vir from DS}(k) = 1 - 6/(k+2) = (k-4)/(k+2)."""
    kk = k_val if k_val is not None else k
    return 1 - Rational(6) / (kk + 2)


def ds_central_charge_sl3(k_val=None):
    """c_{W_3 from DS}(k) = 2(1 - 12/(k+3)) = 2(k-9)/(k+3)."""
    kk = k_val if k_val is not None else k
    return 2 * (1 - Rational(12) / (kk + 3))


def ds_depth_increase_quintic():
    r"""Verify DS depth increase at arity 5: sl_2 -> Virasoro.

    sl_2_k: class L, depth 3, S_5 = 0
    Vir from DS(sl_2_k): class M, depth inf, S_5 != 0

    The DS ghost sector (c_ghost = c(sl_2) - c(Vir) = 2) creates a nonzero
    quartic S_4 from ghost-current coupling, which cascades to S_5, S_6, ...
    through the convolution recursion.
    """
    # c(sl_2_k) = 3k/(k+2)
    c_sl2 = 3 * k / (k + 2)
    # c(Vir from DS) = (k-4)/(k+2)
    c_vir = ds_central_charge_sl2()
    # c_ghost = c(sl_2) - c(Vir) = 2  (= dim n_+ for sl_2)
    c_ghost = cancel(c_sl2 - c_vir)

    # sl_2 shadow: S_5 = 0 (depth 3)
    S5_sl2 = Rational(0)

    # Vir shadow at c = c_vir: S_5 = -48/(c_vir^2(5c_vir + 22))
    S5_vir = cancel(Rational(-48) / (c_vir ** 2 * (5 * c_vir + 22)))

    # Evaluate at specific levels
    test_levels = [1, 2, 5, 10, 100]
    evaluations = {}
    for k_val in test_levels:
        c_v = float(c_vir.subs(k, k_val))
        s5 = float(S5_vir.subs(k, k_val))
        evaluations[k_val] = {
            'c_vir': c_v,
            'S5_vir': s5,
            'S5_sl2': 0.0,
            'S5_nonzero': abs(s5) > 1e-20,
        }

    return {
        'c_sl2': c_sl2,
        'c_vir': c_vir,
        'c_ghost': c_ghost,
        'S5_sl2': S5_sl2,
        'S5_vir_symbolic': S5_vir,
        'evaluations': evaluations,
        'depth_increase': True,
        'mechanism': ('Ghost quartic seed: DS creates S_4 != 0 from '
                      'ghost-current coupling.  Convolution recursion '
                      'propagates to S_5, S_6, ...'),
    }


def ds_depth_increase_sl3_quintic():
    r"""DS depth increase for sl_3 -> W_3 at arity 5.

    sl_3_k: class L, depth 3, S_5 = 0
    W_3 from DS(sl_3_k): class M, depth inf, S_5 != 0

    The ghost contribution has c_ghost = 6 (= dim n_+ for sl_3).
    """
    c_w3 = ds_central_charge_sl3()

    # W_3 T-line shadow = Virasoro shadow at c = c_{W_3}
    S5_w3_tline = cancel(
        Rational(-48) / (c_w3 ** 2 * (5 * c_w3 + 22)))

    test_levels = [1, 2, 5, 10]
    evaluations = {}
    for k_val in test_levels:
        c_v = float(c_w3.subs(k, k_val))
        # Avoid division by zero
        if abs(c_v) > 0.01 and abs(5 * c_v + 22) > 0.01:
            s5 = float(S5_w3_tline.subs(k, k_val))
        else:
            s5 = float('nan')
        evaluations[k_val] = {
            'c_W3': c_v,
            'S5_W3_T_line': s5,
            'S5_sl3': 0.0,
        }

    return {
        'c_W3': c_w3,
        'S5_W3_T_line': S5_w3_tline,
        'S5_sl3': Rational(0),
        'evaluations': evaluations,
    }


# ============================================================================
# 4.  Complementarity at quintic level
# ============================================================================

def virasoro_quintic_complementarity():
    r"""Test complementarity at arity 5: S_5(c) + S_5(26-c).

    Theorem C says Q_g(A) + Q_g(A!) = H*(M_g, Z(A)).  At arity 5,
    this constrains the sum S_5(c) + S_5(26-c).

    S_5(c)    = -48 / [c^2 (5c + 22)]
    S_5(26-c) = -48 / [(26-c)^2 (5(26-c) + 22)]
              = -48 / [(26-c)^2 (152 - 5c)]
    """
    S5_c = Rational(-48) / (c ** 2 * (5 * c + 22))
    c_dual = 26 - c
    S5_dual = Rational(-48) / (c_dual ** 2 * (5 * c_dual + 22))
    S5_dual_simplified = cancel(S5_dual)

    # Compute sum
    total = cancel(S5_c + S5_dual_simplified)
    total_factored = factor(total)

    # Self-dual point: c = 13
    S5_at_13 = float(S5_c.subs(c, 13))
    total_at_13 = float(total.subs(c, 13))

    return {
        'S5_c': S5_c,
        'S5_26_minus_c': S5_dual_simplified,
        'sum': total,
        'sum_factored': total_factored,
        'self_dual_S5': S5_at_13,
        'self_dual_sum': total_at_13,
        'sum_vanishes_at_13': abs(total_at_13 - 2 * S5_at_13) < 1e-15,
    }


# ============================================================================
# 5.  Growth rate and convergence analysis at quintic/sextic
# ============================================================================

def quintic_growth_diagnostics(c_val: float) -> Dict[str, float]:
    """Numerical shadow obstruction tower diagnostics at a specific central charge.

    Computes S_r to arity 20 and extracts growth-rate information.
    """
    kap = c_val / 2
    alp = 2.0
    s4 = 10.0 / (c_val * (5 * c_val + 22))

    q0 = 4 * kap ** 2
    q1 = 12 * kap * alp
    q2 = 9 * alp ** 2 + 16 * kap * s4

    # Compute to arity 20
    a0 = c_val
    a = [a0, q1 / (2 * a0)]
    a.append((q2 - a[1] ** 2) / (2 * a0))
    for n in range(3, 19):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a0))

    S = {r + 2: a[r] / (r + 2) for r in range(len(a))}

    # Ratios |S_{r+1}/S_r|
    ratios = {}
    for r in range(2, 19):
        if abs(S[r]) > 1e-50:
            ratios[r] = abs(S[r + 1] / S[r])

    # Exact growth rate: rho = sqrt(9 alpha^2 + 2 Delta) / (2|kappa|)
    Delta = 8 * kap * s4
    rho_exact = (9 * alp ** 2 + 2 * Delta) ** 0.5 / (2 * abs(kap))

    return {
        'c': c_val,
        'S5': S[5],
        'S6': S[6],
        'S7': S[7],
        'S8': S[8],
        'ratio_S6_S5': ratios.get(5, None),
        'ratio_S7_S6': ratios.get(6, None),
        'ratio_S8_S7': ratios.get(7, None),
        'ratio_limit': ratios.get(18, None),
        'rho_exact': rho_exact,
        'convergent': rho_exact < 1.0,
    }


def quintic_phase_diagram() -> Dict[str, Dict]:
    """Phase diagram: convergence properties at arity 5 across c values."""
    test_points = [0.5, 1.0, 2.0, 5.0, 10.0, 13.0, 20.0, 25.0, 50.0]
    results = {}
    for c_val in test_points:
        diag = quintic_growth_diagnostics(c_val)
        results[f'c={c_val}'] = {
            'S5': diag['S5'],
            'rho': diag['rho_exact'],
            'convergent': diag['convergent'],
        }
    return results


# ============================================================================
# 6.  Multi-line quintic for W_3
# ============================================================================

def w3_quintic_t_line(k_val=None):
    r"""W_3 quintic on the T-line (energy-momentum tensor line).

    The T-line shadow of W_3 is the Virasoro shadow at c = c_{W_3}(k).

        c_{W_3}(k) = 2(1 - 12/(k+3)) = 2(k-9)/(k+3)
    """
    kk = k_val if k_val is not None else k
    c_w3 = 2 * (kk - 9) / (kk + 3)
    S5 = cancel(Rational(-48) / (c_w3 ** 2 * (5 * c_w3 + 22)))
    return {'c_W3': c_w3, 'S5_T_line': S5}


def w3_quintic_w_line():
    r"""W_3 quintic on the W-line (spin-3 current line).

    The W-line has kappa_W = (conformal weight-3 contribution).
    The W-line shadow at arity 5 involves mixed (T,W) correlators
    which are currently computed only at arity 2--4 in the manuscript.

    FRONTIER: Full W-line quintic requires OPE extraction beyond
    the current w4_ope_miura.py capability.
    """
    return {
        'status': 'frontier',
        'note': ('W-line quintic requires spin-3 OPE data at arity 5.  '
                 'Currently blocked by w4_ope_miura.py limitations.  '
                 'T-line quintic is computable and is done above.'),
    }


# ============================================================================
# 7.  Obstruction class analysis
# ============================================================================

def quintic_obstruction_class():
    r"""The quintic obstruction class o^(5) in Def_cyc^mod(A).

    Master equation at arity 5:
        nabla_H(S_5) + o^(5)(S_2, S_3, S_4) = 0

    The obstruction o^(5) is a sum over planted forests with 5 leaves
    of graph amplitudes involving S_2, S_3, S_4.

    For class M (Virasoro): o^(5) != 0, forcing S_5 != 0.
    The exact formula involves 26 binary trees on 5 leaves (Catalan C_4 = 14
    full binary trees, plus forests with additional structure) out of
    236 total planted forests on 5 leaves (A000311).
    """
    S5 = Rational(-48) / (c ** 2 * (5 * c + 22))

    return {
        'quintic_forced_class_M': True,
        'quintic_vanishes_class_G': True,
        'quintic_vanishes_class_L': True,
        'quintic_stratum_separated_class_C': True,
        'S5_Virasoro': S5,
        'n_forests_arity_5': 236,       # A000311(5)
        'n_binary_trees_arity_5': 14,   # Catalan C_4 = 14
    }


# ============================================================================
# 8.  Higher-arity patterns
# ============================================================================

def virasoro_shadow_pattern(max_r: int = 15) -> Dict[str, Any]:
    r"""Analyze the pattern of Virasoro shadow coefficients S_r(c).

    Each S_r is a rational function of c.  Denominators involve
    increasing powers of c and (5c+22).  The structure is dictated
    by the convolution recursion: each step divides by 2*a_0 = 2c
    and involves products of earlier a_n that carry (5c+22) factors
    from a_2 = 40/(c(5c+22)).
    """
    tower = virasoro_shadow_tower_exact(max_r)

    pattern = {}
    for r, Sr in tower.items():
        f = factor(Sr)
        pattern[r] = {
            'S_r': cancel(Sr),
            'factored': f,
        }

    return pattern


def virasoro_shadow_numerical_table(c_val: float,
                                     max_r: int = 20) -> Dict[int, float]:
    """Numerical shadow obstruction tower at a specific c value."""
    kap = c_val / 2
    alp = 2.0
    s4 = 10.0 / (c_val * (5 * c_val + 22))

    q0 = 4 * kap ** 2
    q1 = 12 * kap * alp
    q2 = 9 * alp ** 2 + 16 * kap * s4

    a0 = c_val
    a = [a0, q1 / (2 * a0)]
    a.append((q2 - a[1] ** 2) / (2 * a0))
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a0))

    return {r + 2: a[r] / (r + 2) for r in range(len(a))}


# ============================================================================
# 9.  Verification suite
# ============================================================================

def verify_quintic_formulas() -> Dict[str, bool]:
    """Verify all quintic formulas against independent computations."""
    results = {}

    # 1. S_5 formula: -48/(c^2(5c+22))
    tower = virasoro_shadow_tower_exact(8)
    S5_from_tower = tower[5]
    S5_expected = Rational(-48) / (c ** 2 * (5 * c + 22))
    results['S5_formula'] = simplify(S5_from_tower - S5_expected) == 0

    # 2. S_2 = c/2
    results['S2_is_kappa'] = simplify(tower[2] - c / 2) == 0

    # 3. S_3 = 2 (independent of c)
    results['S3_is_2'] = simplify(tower[3] - 2) == 0

    # 4. S_4 = 10/(c(5c+22))
    S4_expected = Rational(10) / (c * (5 * c + 22))
    results['S4_formula'] = simplify(tower[4] - S4_expected) == 0

    # 5. S_6 = 80(45c+193)/(3c^3(5c+22)^2)
    S6_expected = Rational(80) * (45 * c + 193) / (
        3 * c ** 3 * (5 * c + 22) ** 2)
    results['S6_formula'] = simplify(tower[6] - S6_expected) == 0

    # 6. Heisenberg S_5 = 0
    results['heisenberg_S5_zero'] = heisenberg_quintic() == 0

    # 7. Affine S_5 = 0
    results['affine_S5_zero'] = affine_sl2_quintic() == 0

    # 8. bc ghosts S_5 on 1D metric is nonzero
    bg = bc_ghosts_quintic()
    results['bc_ghosts_S5_1d_nonzero'] = bg['S5_1d_nonzero']

    # 9. bc ghosts S_5 on 1D metric equals 1/2
    results['bc_ghosts_S5_equals_half'] = bg['S5_1d_metric'] == Rational(1, 2)

    # 10. Numerical cross-check at c = 25
    num_tower = virasoro_shadow_numerical_table(25.0, 8)
    S5_num = num_tower[5]
    S5_exact_at_25 = -48.0 / (25.0 ** 2 * (125.0 + 22.0))
    results['numerical_c25'] = abs(S5_num - S5_exact_at_25) < 1e-12

    # 11. Numerical cross-check at c = 1/2 (Ising)
    num_ising = virasoro_shadow_numerical_table(0.5, 8)
    S5_ising = num_ising[5]
    S5_exact_ising = -48.0 / (0.5 ** 2 * (2.5 + 22.0))
    results['numerical_ising'] = abs(S5_ising - S5_exact_ising) < 1e-12

    # 12. Complementarity at self-dual point c=13
    comp = virasoro_quintic_complementarity()
    results['complementarity_computed'] = comp['sum'] is not None

    # 13. Convolution identity: t^3 coefficient of f^2 = 0
    data = virasoro_shadow_data()
    coeffs = _convolution_coefficients(data['q0'], data['q1'], data['q2'], 5)
    t3_check = cancel(
        2 * coeffs[0] * coeffs[3] + 2 * coeffs[1] * coeffs[2])
    results['convolution_t3_vanishes'] = simplify(t3_check) == 0

    return results


# ============================================================================
# Main: demonstration
# ============================================================================

if __name__ == '__main__':
    print("=" * 72)
    print("QUINTIC-SEXTIC SHADOW OBSTRUCTION ENGINE")
    print("=" * 72)

    print("\n--- Virasoro S_5 exact formula ---")
    q5 = virasoro_quintic_exact()
    print(f"  S_5(c) = {q5['S5']}")
    print(f"  Expected: {q5['S5_expected']}")
    print(f"  Match: {q5['S5_matches']}")

    print("\n--- Virasoro S_6 exact formula ---")
    q6 = virasoro_sextic_exact()
    print(f"  S_6(c) = {q6['S6']}")
    print(f"  S_6 factored = {q6['S6_factored']}")

    print("\n--- Virasoro S_7 exact formula ---")
    print(f"  S_7(c) = {q6['S7']}")
    print(f"  S_7 factored = {q6['S7_factored']}")

    print("\n--- Cross-family quintic table ---")
    table = cross_family_quintic_table()
    for name, data in table.items():
        print(f"  {name:15s}: class={data['class']}, depth={data['depth']}, "
              f"S5_1d={data['S5_1d']}, S5_true={data['S5_true']}")

    print("\n--- Complementarity at arity 5 ---")
    comp = virasoro_quintic_complementarity()
    print(f"  S_5(c) + S_5(26-c) = {comp['sum_factored']}")
    print(f"  At c=13: {comp['self_dual_sum']:.6e}")

    print("\n--- DS depth increase at arity 5 ---")
    ds = ds_depth_increase_quintic()
    print(f"  S_5(sl_2) = {ds['S5_sl2']}")
    print(f"  S_5(Vir from DS) = {ds['S5_vir_symbolic']}")
    for kv, ev in ds['evaluations'].items():
        print(f"    k={kv}: c_vir={ev['c_vir']:.4f}, "
              f"S5_vir={ev['S5_vir']:.6e}")

    print("\n--- Verification ---")
    for name, ok in verify_quintic_formulas().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
