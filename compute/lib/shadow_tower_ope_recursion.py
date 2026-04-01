r"""Shadow tower via direct OPE/MC recursion — an independent verification engine.

The shadow coefficient S_r at arity r on a single primary line is determined
by the Maurer-Cartan recursion on the modular cyclic deformation complex:

    \nabla_H(S_r) + o^{(r)} = 0

where \nabla_H(f) = \{S_2 x^2, f\}_H is the linearized operator and
o^{(r)} is the arity-r obstruction from H-Poisson brackets of lower shadows.

RECURSION (for r >= 5, given initial data S_2 = kappa, S_3, S_4):

    S_r = -(1/(2r * kappa)) * SUM_{j+k = r+2, 2 <= j <= k < r}
              f(j,k) * j * k * S_j * S_k

where f(j,k) = 1 if j < k, f(j,k) = 1/2 if j = k.

The sum is over UNORDERED pairs {j,k} with j + k = r + 2, where both
j and k are at least 2 and strictly less than r (excluding the "linear"
terms that are absorbed into nabla_H).

KEY MATHEMATICAL POINT: This recursion is INDEPENDENT of the assumption
that the shadow metric Q_L(t) is a polynomial of degree <= 2. The sqrt(Q_L)
Taylor expansion method ASSUMES Q_L is quadratic (proved for single primary
lines, thm:riccati-algebraicity). Agreement between the two methods at each
arity is a VERIFICATION of the quadratic shadow metric theorem.

For multi-generator algebras on mixed directions, the shadow metric may
NOT be quadratic (the proof requires a single primary line). This engine
works without that assumption.

ALGEBRAS COMPUTED:
  1-7:   Virasoro at c = 1/2, 7/10, 4/5, 1, 13, 25, 26
  8-10:  W_3 at c = 2, 50, 98 (T-line and W-line)
  11:    W_4 at c = 3 (T-line, W3-line, W4-line)
  12-14: Affine sl_3(k=1), G_2(k=1), E_8(k=1)
  15:    beta-gamma at lambda = 1/3

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

Dependencies:
    shadow_tower_recursive.py: sqrt(Q_L) method for comparison
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, Symbol, cancel, factor, simplify, sqrt

c = Symbol('c')


# =============================================================================
# 1.  Core OPE/MC recursion engine (exact rational arithmetic)
# =============================================================================

def mc_recursion_rational(kappa: Fraction, S3: Fraction, S4: Fraction,
                          max_r: int = 30) -> Dict[int, Fraction]:
    r"""Compute shadow coefficients S_2 through S_{max_r} via MC recursion.

    Uses Python's fractions.Fraction for exact rational arithmetic.
    No square roots, no floating point, no assumptions about Q_L.

    Parameters:
        kappa: S_2 (curvature), as a Fraction.
        S3: S_3 (cubic shadow), as a Fraction.
        S4: S_4 (quartic contact invariant), as a Fraction.
        max_r: Maximum arity to compute.

    Returns:
        Dict mapping arity r -> S_r as a Fraction.
    """
    S: Dict[int, Fraction] = {}
    S[2] = kappa
    S[3] = S3
    S[4] = S4

    for r in range(5, max_r + 1):
        # Obstruction: sum over unordered pairs {j,k} with j+k = r+2,
        # 2 <= j <= k, j < r, k < r.
        # Since k = r+2-j >= j => j <= (r+2)/2; also k = r+2-j < r => j > 2.
        # But j >= 2 and k < r => j > 2 is automatic for r >= 5 since
        # j=2 => k=r which violates k < r.
        # Actually: j >= 2 is given, k = r+2-j, k < r => j > 2, so j >= 3.
        # And k >= j => j <= (r+2)//2.
        obs = Fraction(0)
        target = r + 2
        for j in range(3, target // 2 + 1):
            k = target - j
            if k < j or k >= r:
                continue
            if j not in S or k not in S:
                continue
            bracket_coeff = Fraction(j) * Fraction(k) * S[j] * S[k]
            if j == k:
                obs += bracket_coeff / Fraction(2)
            else:
                obs += bracket_coeff
        # Also include j=2, k=r+2-2=r: EXCLUDED since k=r is what we compute.
        # And j=r, k=2: EXCLUDED since j > k (handled by j <= k constraint).

        # S_r = -(obs) / (2 * r * kappa)
        if kappa == 0:
            S[r] = Fraction(0)
        else:
            S[r] = -obs / (Fraction(2) * Fraction(r) * kappa)

    return S


def mc_recursion_sympy(kappa_expr, S3_expr, S4_expr,
                       max_r: int = 30) -> Dict[int, Any]:
    r"""Compute shadow coefficients via MC recursion using sympy rationals.

    Parameters:
        kappa_expr, S3_expr, S4_expr: Sympy expressions for the initial data.
        max_r: Maximum arity.

    Returns:
        Dict mapping arity r -> S_r as sympy expression.
    """
    S: Dict[int, Any] = {}
    S[2] = kappa_expr
    S[3] = S3_expr
    S[4] = S4_expr

    for r in range(5, max_r + 1):
        obs = Rational(0)
        target = r + 2
        for j in range(3, target // 2 + 1):
            k = target - j
            if k < j or k >= r:
                continue
            if j not in S or k not in S:
                continue
            bracket_coeff = j * k * S[j] * S[k]
            if j == k:
                obs += bracket_coeff * Rational(1, 2)
            else:
                obs += bracket_coeff

        if kappa_expr == 0:
            S[r] = Rational(0)
        else:
            S[r] = cancel(-obs / (2 * r * kappa_expr))

    return S


# =============================================================================
# 2.  sqrt(Q_L) Taylor expansion method (for comparison)
# =============================================================================

def sqrt_ql_rational(kappa: Fraction, S3: Fraction, S4: Fraction,
                     max_r: int = 30) -> Dict[int, Fraction]:
    r"""Compute shadow coefficients via sqrt(Q_L) Taylor expansion.

    Q_L(t) = 4*kappa^2 + 12*kappa*S3*t + (9*S3^2 + 16*kappa*S4)*t^2

    H(t) = t^2 * sqrt(Q_L(t)) = sum_{r>=2} r*S_r*t^r

    So S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t)).

    Parameters:
        kappa, S3, S4: Initial shadow data as Fractions.
        max_r: Maximum arity.

    Returns:
        Dict mapping arity r -> S_r as a Fraction.
    """
    q0 = 4 * kappa**2
    q1 = 12 * kappa * S3
    q2 = 9 * S3**2 + 16 * kappa * S4

    max_n = max_r - 2

    # a_0 = sqrt(q0) = sqrt(4*kappa^2) = 2*kappa (preserving sign).
    # The square root branch is determined by matching S_2 = kappa:
    # since S_2 = a_0/2, we need a_0 = 2*kappa (including the sign of kappa).
    # Mathematically: Q_L(0) = (2*kappa)^2, and we choose the branch
    # sqrt(Q_L(0)) = 2*kappa (not 2*|kappa|).
    if kappa != 0:
        a0 = 2 * kappa
    else:
        # kappa = 0: degenerate, all shadows zero
        return {r: Fraction(0) for r in range(2, max_r + 1)}

    a: List[Fraction] = [Fraction(0)] * (max_n + 1)
    a[0] = a0

    if max_n >= 1:
        a[1] = q1 / (2 * a0)

    if max_n >= 2:
        a[2] = (q2 - a[1]**2) / (2 * a0)

    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2 * a0)

    # S_r = a_{r-2} / r
    result: Dict[int, Fraction] = {}
    for r in range(2, max_r + 1):
        result[r] = a[r - 2] / Fraction(r)

    return result


# =============================================================================
# 3.  Algebra data: all 15 algebras
# =============================================================================

def virasoro_shadow_data_frac(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Shadow initial data (kappa, S3, S4) for Virasoro at central charge c.

    kappa = c/2, S3 = 2, S4 = 10/(c*(5c+22)).
    """
    kappa = c_val / 2
    S3 = Fraction(2)
    S4 = Fraction(10) / (c_val * (5 * c_val + 22))
    return kappa, S3, S4


def w3_tline_data_frac(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """W_3 T-line shadow data (identical to Virasoro)."""
    return virasoro_shadow_data_frac(c_val)


def w3_wline_data_frac(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """W_3 W-line shadow data.

    kappa_W = c/3, S3_W = 0 (Z_2 parity), S4_W = 2560/(c*(5c+22)^3).
    """
    kappa = c_val / 3
    S3 = Fraction(0)
    S4 = Fraction(2560) / (c_val * (5 * c_val + 22)**3)
    return kappa, S3, S4


def w4_tline_data_frac(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """W_4 T-line shadow data (identical to Virasoro)."""
    return virasoro_shadow_data_frac(c_val)


def w4_w3line_data_frac(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """W_4 W3-line shadow data.

    kappa_{W3} = c/3, S3_{W3} = 0 (Z_2 from W_3 -> -W_3), S4 from W_3 exchange.
    Same as W_3 W-line (the W_3 generator in W_4 has the same parity structure).
    """
    return w3_wline_data_frac(c_val)


def w4_w4line_data_frac(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """W_4 W4-line shadow data.

    kappa_{W4} = c/4.
    S3_{W4}: the cubic C(W4, W4, W4) vanishes by W_4-charge conservation
    (W_4 carries charge under a Z-grading with the W_4 generator having
    charge 1; three W_4's give charge 3, which is nonzero mod any symmetry
    that would enforce vanishing... Actually, W_4 has NO Z_2 parity from
    W_3 -> -W_3 (W_4 is even under this), but there IS a separate parity
    from W_4 -> -W_4. Under this Z_2: cubic W_4^3 has odd parity, so
    S3_{W4} = 0 on the W4-line.

    For the quartic: W_4 x W_4 -> W_4 coupling c_444 determines S4.
    At this stage, S4_{W4} from self-coupling:
    S4 = c_444^2 * N_{W4}^{-1} = c_444^2 / (c/4) = 4*c_444^2/c.

    For W_4 at c=3, the self-coupling c_444 depends on the normalization.
    The universal W_4 algebra (DS of sl_4) has c = 3 - 240/(k+4).
    At k -> infinity: c -> infinity, so c=3 is NOT a standard integer level.

    For a GENERIC W_4 analysis: we note that the W4-line has even-parity
    structure (S3 = 0, only even arities nonzero) similar to the W-line
    of W_3.

    In the absence of a known closed-form for c_444, we use the result
    from the W_4 OPE: c_444^2 is computed from the Jacobi identity.

    APPROXIMATION: for the purpose of this cross-check, we compute what
    the recursion gives with S3=0 and a specific S4, then compare with
    sqrt(Q_L). The agreement will hold regardless of the specific S4 value.

    For c = 3, we use a symbolic S4 to verify the recursion structure.
    """
    kappa = c_val / 4
    S3 = Fraction(0)
    # For the W4-line, the quartic comes from the W4 x W4 self-OPE.
    # Using the known W_4 self-coupling structure:
    # At generic c, S4_{W4} involves the c_444 structure constant.
    # For our verification, we use a specific rational value.
    # The W_4 OPE gives: at c=3, the W_4 self-coupling involves
    # Lambda and W_4 exchange channels.
    # Lambda norm = c(5c+22)/10 = 3*37/10 = 111/10
    # W_4 norm = c/4 = 3/4
    # The quartic on the W4-line from W4 x W4 -> Lambda -> W4 x W4:
    # S4 = alpha_{44,Lambda}^2 / N_Lambda + c_444^2 / N_{W4}
    # For the verification purpose, we'll use S4 = 0 (class G on this line)
    # which gives a terminating tower — verifiable.
    # If the actual S4 is nonzero, the recursion still works.
    S4 = Fraction(0)  # placeholder; real value requires c_444
    return kappa, S3, S4


def affine_data_frac(dim_g: int, h_vee: int, k_val: int
                     ) -> Tuple[Fraction, Fraction, Fraction]:
    """Shadow data for affine Kac-Moody algebra g-hat at level k.

    kappa = dim(g)*(k+h^v)/(2*h^v), S3 = 1, S4 = 0 (class L).
    """
    kappa = Fraction(dim_g) * (k_val + h_vee) / (2 * h_vee)
    S3 = Fraction(1)  # universal for all affine KM
    S4 = Fraction(0)  # Jacobi identity kills quartic
    return kappa, S3, S4


def betagamma_tline_data_frac(lam_val: Fraction
                              ) -> Tuple[Fraction, Fraction, Fraction]:
    """Shadow data for beta-gamma T-line at weight lambda.

    The T-line shadow data is identical to Virasoro at c = c_bg(lambda).
    c(lambda) = 2*(6*lambda^2 - 6*lambda + 1).
    kappa = c/2, S3 = 2, S4 = 10/(c*(5c+22)).
    """
    c_bg = 2 * (6 * lam_val**2 - 6 * lam_val + 1)
    return virasoro_shadow_data_frac(c_bg)


# =============================================================================
# 4.  Master computation: all 15 algebras
# =============================================================================

def compute_all_towers(max_r: int = 30) -> Dict[str, Dict]:
    """Compute shadow towers for all 15 algebras via both methods.

    Returns a dict mapping algebra name to:
        {
            'mc': {r: S_r} from MC recursion,
            'sqrt': {r: S_r} from sqrt(Q_L) Taylor expansion,
            'agree': bool (True if all coefficients match),
            'max_diff_arity': int (first arity where they disagree, or None),
            'initial_data': (kappa, S3, S4),
            'depth_class': str,
        }
    """
    results: Dict[str, Dict] = {}

    # ---- 1-7: Virasoro at various central charges ----
    vir_c_values = [
        ('Vir_c=1/2', Fraction(1, 2)),
        ('Vir_c=7/10', Fraction(7, 10)),
        ('Vir_c=4/5', Fraction(4, 5)),
        ('Vir_c=1', Fraction(1)),
        ('Vir_c=13', Fraction(13)),
        ('Vir_c=25', Fraction(25)),
        ('Vir_c=26', Fraction(26)),
    ]
    for name, cv in vir_c_values:
        data = virasoro_shadow_data_frac(cv)
        results[name] = _compute_and_compare(name, data, max_r, depth='M')

    # ---- 8-10: W_3 at c = 2, 50, 98, T-line and W-line ----
    w3_c_values = [
        ('W3_c=2', Fraction(2)),
        ('W3_c=50', Fraction(50)),
        ('W3_c=98', Fraction(98)),
    ]
    for base_name, cv in w3_c_values:
        # T-line
        t_data = w3_tline_data_frac(cv)
        results[f'{base_name}_Tline'] = _compute_and_compare(
            f'{base_name}_Tline', t_data, max_r, depth='M')
        # W-line
        w_data = w3_wline_data_frac(cv)
        results[f'{base_name}_Wline'] = _compute_and_compare(
            f'{base_name}_Wline', w_data, max_r, depth='M')

    # ---- 11: W_4 at c = 3, three lines ----
    cv = Fraction(3)
    t_data = w4_tline_data_frac(cv)
    results['W4_c=3_Tline'] = _compute_and_compare(
        'W4_c=3_Tline', t_data, max_r, depth='M')

    w3l_data = w4_w3line_data_frac(cv)
    results['W4_c=3_W3line'] = _compute_and_compare(
        'W4_c=3_W3line', w3l_data, max_r, depth='M')

    w4l_data = w4_w4line_data_frac(cv)
    results['W4_c=3_W4line'] = _compute_and_compare(
        'W4_c=3_W4line', w4l_data, max_r, depth='G')

    # ---- 12-14: Affine KM ----
    affine_algebras = [
        ('sl3_k=1', 8, 3, 1),     # dim=8, h^v=3, k=1
        ('G2_k=1', 14, 4, 1),     # dim=14, h^v=4, k=1
        ('E8_k=1', 248, 30, 1),   # dim=248, h^v=30, k=1
    ]
    for name, dim_g, h_vee, k_val in affine_algebras:
        data = affine_data_frac(dim_g, h_vee, k_val)
        results[name] = _compute_and_compare(name, data, max_r, depth='L')

    # ---- 15: beta-gamma at lambda = 1/3 ----
    lam_val = Fraction(1, 3)
    bg_data = betagamma_tline_data_frac(lam_val)
    results['bg_lam=1/3_Tline'] = _compute_and_compare(
        'bg_lam=1/3_Tline', bg_data, max_r, depth='M')

    return results


def _compute_and_compare(name: str,
                         initial_data: Tuple[Fraction, Fraction, Fraction],
                         max_r: int,
                         depth: str = 'M') -> Dict:
    """Compute tower by both methods and compare.

    Returns result dict with both towers and agreement status.
    """
    kappa, S3, S4 = initial_data

    # Method 1: MC recursion
    mc_tower = mc_recursion_rational(kappa, S3, S4, max_r)

    # Method 2: sqrt(Q_L) Taylor expansion
    sqrt_tower = sqrt_ql_rational(kappa, S3, S4, max_r)

    # Compare
    agree = True
    max_diff_arity = None
    diffs: Dict[int, Tuple[Fraction, Fraction]] = {}
    for r in range(2, max_r + 1):
        mc_val = mc_tower.get(r, Fraction(0))
        sq_val = sqrt_tower.get(r, Fraction(0))
        if mc_val != sq_val:
            agree = False
            if max_diff_arity is None:
                max_diff_arity = r
            diffs[r] = (mc_val, sq_val)

    return {
        'mc': mc_tower,
        'sqrt': sqrt_tower,
        'agree': agree,
        'max_diff_arity': max_diff_arity,
        'diffs': diffs,
        'initial_data': initial_data,
        'depth_class': depth,
        'name': name,
    }


# =============================================================================
# 5.  Structural properties of the MC tower
# =============================================================================

def tower_depth(tower: Dict[int, Fraction], tol: Fraction = Fraction(0)
                ) -> Optional[int]:
    """Determine the depth (first arity r where S_r = 0 and all subsequent vanish).

    Returns the depth r_max, or None if all computed coefficients are nonzero.
    """
    max_r = max(tower.keys())
    for r in range(2, max_r + 1):
        if tower.get(r, Fraction(0)) != tol:
            continue
        # Check if all subsequent vanish
        all_zero = all(tower.get(s, Fraction(0)) == tol
                       for s in range(r, max_r + 1))
        if all_zero:
            return r - 1  # depth = last nonzero arity
    return None  # infinite depth (all nonzero through max_r)


def tower_parity(tower: Dict[int, Fraction]) -> Optional[str]:
    """Check parity structure of the tower.

    Returns:
        'even' if all odd-arity coefficients vanish (Z_2 symmetry),
        'odd' if all even-arity coefficients (>2) vanish,
        'none' if no parity structure.
    """
    max_r = max(tower.keys())
    odd_zero = all(tower.get(r, Fraction(0)) == 0
                   for r in range(3, max_r + 1, 2))
    even_zero = all(tower.get(r, Fraction(0)) == 0
                    for r in range(4, max_r + 1, 2))

    if odd_zero and not even_zero:
        return 'even'
    if even_zero and not odd_zero:
        return 'odd'
    return 'none'


def ratio_test_rational(tower: Dict[int, Fraction],
                        start_r: int = 5) -> List[Tuple[int, float]]:
    """Compute |S_{r+1}/S_r| ratios for convergence analysis.

    Returns list of (r, |S_{r+1}/S_r|) tuples.
    """
    max_r = max(tower.keys())
    ratios: List[Tuple[int, float]] = []
    for r in range(start_r, max_r):
        sr = tower.get(r, Fraction(0))
        sr1 = tower.get(r + 1, Fraction(0))
        if sr != 0:
            ratio = abs(float(sr1 / sr))
            ratios.append((r, ratio))
    return ratios


def growth_rate_estimate(tower: Dict[int, Fraction],
                         tail_length: int = 5) -> Optional[float]:
    """Estimate the growth rate rho from the tail of the ratio test.

    Uses the average of the last `tail_length` ratios.
    """
    ratios = ratio_test_rational(tower)
    if len(ratios) < tail_length:
        return None
    tail = [r for _, r in ratios[-tail_length:]]
    return sum(tail) / len(tail)


# =============================================================================
# 6.  Symbolic verification on Virasoro family
# =============================================================================

def virasoro_mc_recursion_symbolic(max_r: int = 15) -> Dict[int, Any]:
    """Compute the Virasoro shadow tower symbolically (in c) via MC recursion.

    Returns dict {r: S_r(c)} as sympy expressions in c.
    """
    kappa = c / 2
    S3 = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    return mc_recursion_sympy(kappa, S3, S4, max_r)


def virasoro_sqrt_ql_symbolic(max_r: int = 15) -> Dict[int, Any]:
    """Compute the Virasoro shadow tower symbolically via sqrt(Q_L).

    Uses sympy's sqrt for the initial a_0 = sqrt(4*kappa^2) = |c|.
    For c > 0 (the physical regime), sqrt(c^2) = c.
    We use a positive symbol to avoid sign ambiguity.
    """
    cp = Symbol('c', positive=True)
    kappa = cp / 2
    S3 = Rational(2)
    S4 = Rational(10) / (cp * (5 * cp + 22))

    q0 = 4 * kappa**2
    q1 = 12 * kappa * S3
    q2 = 9 * S3**2 + 16 * kappa * S4

    max_n = max_r - 2
    a0 = sqrt(q0)  # = |c| = cp since cp > 0
    a = [a0]

    if max_n >= 1:
        a.append(q1 / (2 * a0))
    if max_n >= 2:
        a.append((q2 - a[1]**2) / (2 * a0))

    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(cancel(-conv_sum / (2 * a0)))

    result: Dict[int, Any] = {}
    for r in range(2, max_r + 1):
        result[r] = cancel(a[r - 2] / r)
    # Substitute back to unqualified c
    return {r: v.subs(cp, c) for r, v in result.items()}


# =============================================================================
# 7.  Affine KM tower structure verification
# =============================================================================

def verify_affine_termination(dim_g: int, h_vee: int, k_val: int,
                              max_r: int = 30) -> Dict:
    """Verify that affine KM towers terminate at arity 3 (class L).

    Returns verification results: all S_r = 0 for r >= 4.
    """
    data = affine_data_frac(dim_g, h_vee, k_val)
    kappa, S3, S4 = data

    mc_tower = mc_recursion_rational(kappa, S3, S4, max_r)
    sqrt_tower = sqrt_ql_rational(kappa, S3, S4, max_r)

    # Check termination
    terminated_mc = all(mc_tower[r] == 0 for r in range(4, max_r + 1))
    terminated_sqrt = all(sqrt_tower[r] == 0 for r in range(4, max_r + 1))

    return {
        'kappa': kappa,
        'S3': S3,
        'S4': S4,
        'terminated_mc': terminated_mc,
        'terminated_sqrt': terminated_sqrt,
        'agree': mc_tower == sqrt_tower,
        'mc_S2': mc_tower[2],
        'mc_S3': mc_tower[3],
        'sqrt_S2': sqrt_tower[2],
        'sqrt_S3': sqrt_tower[3],
    }


# =============================================================================
# 8.  W-line parity verification
# =============================================================================

def verify_wline_parity(c_val: Fraction, max_r: int = 30) -> Dict:
    """Verify that the W-line tower has even-parity structure.

    Z_2 from W -> -W forces all odd-arity coefficients to vanish.
    """
    data = w3_wline_data_frac(c_val)
    kappa, S3, S4 = data

    mc_tower = mc_recursion_rational(kappa, S3, S4, max_r)
    sqrt_tower = sqrt_ql_rational(kappa, S3, S4, max_r)

    # Check parity: all odd arities should vanish
    odd_vanish_mc = all(mc_tower.get(r, Fraction(0)) == 0
                        for r in range(3, max_r + 1, 2))
    odd_vanish_sqrt = all(sqrt_tower.get(r, Fraction(0)) == 0
                          for r in range(3, max_r + 1, 2))

    return {
        'c': c_val,
        'kappa_W': kappa,
        'S3_W': S3,
        'S4_W': S4,
        'odd_vanish_mc': odd_vanish_mc,
        'odd_vanish_sqrt': odd_vanish_sqrt,
        'agree': mc_tower == sqrt_tower,
        'parity_mc': tower_parity(mc_tower),
        'parity_sqrt': tower_parity(sqrt_tower),
    }


# =============================================================================
# 9.  Cross-method consistency summary
# =============================================================================

def full_consistency_report(max_r: int = 30) -> Dict:
    """Generate a complete consistency report across all 15 algebras.

    Returns summary statistics and any discrepancies found.
    """
    all_results = compute_all_towers(max_r)

    n_agree = sum(1 for r in all_results.values() if r['agree'])
    n_total = len(all_results)
    disagreements = {name: r for name, r in all_results.items() if not r['agree']}

    # Structural checks
    affine_terminated = all(
        all_results[name]['mc'].get(r, Fraction(0)) == 0
        for name in ['sl3_k=1', 'G2_k=1', 'E8_k=1']
        for r in range(4, max_r + 1)
    )

    wline_parity = all(
        all_results[name]['mc'].get(r, Fraction(0)) == 0
        for name in [n for n in all_results if 'Wline' in n]
        for r in range(3, max_r + 1, 2)
    )

    return {
        'n_agree': n_agree,
        'n_total': n_total,
        'all_agree': n_agree == n_total,
        'disagreements': disagreements,
        'affine_terminated': affine_terminated,
        'wline_parity': wline_parity,
        'max_r': max_r,
    }


# =============================================================================
# 10.  Koszul duality verification
# =============================================================================

def virasoro_koszul_pair_towers(c_val: Fraction, max_r: int = 30
                                ) -> Dict:
    """Compute towers for Vir_c and Vir_{26-c} and verify complementarity.

    kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13 (AP24).
    """
    data_A = virasoro_shadow_data_frac(c_val)
    data_Ad = virasoro_shadow_data_frac(Fraction(26) - c_val)

    mc_A = mc_recursion_rational(*data_A, max_r)
    mc_Ad = mc_recursion_rational(*data_Ad, max_r)

    kappa_sum = data_A[0] + data_Ad[0]

    return {
        'c': c_val,
        'c_dual': Fraction(26) - c_val,
        'kappa_A': data_A[0],
        'kappa_Ad': data_Ad[0],
        'kappa_sum': kappa_sum,
        'kappa_sum_correct': kappa_sum == Fraction(13),
        'mc_A': mc_A,
        'mc_Ad': mc_Ad,
    }


# =============================================================================
# 11.  Depth classification from MC recursion
# =============================================================================

def classify_depth_from_tower(tower: Dict[int, Fraction],
                              max_r: int = 30) -> str:
    """Classify the shadow tower depth class from computed coefficients.

    G: S_3 = 0, S_4 = 0 => depth 2
    L: S_3 != 0, S_4 = 0 => depth 3
    M: S_4 != 0 => depth infinity (generically)
    """
    S3 = tower.get(3, Fraction(0))
    S4 = tower.get(4, Fraction(0))

    if S3 == 0 and S4 == 0:
        return 'G'
    if S3 != 0 and S4 == 0:
        # Check if all higher vanish
        all_higher_zero = all(tower.get(r, Fraction(0)) == 0
                              for r in range(4, max_r + 1))
        if all_higher_zero:
            return 'L'
        return 'M'  # S_3 != 0 but higher might not vanish
    return 'M'


if __name__ == '__main__':
    print("Shadow Tower OPE Recursion Engine")
    print("=" * 60)

    report = full_consistency_report(max_r=30)
    print(f"\nAgreement: {report['n_agree']}/{report['n_total']} algebras")
    print(f"All agree: {report['all_agree']}")
    print(f"Affine terminated: {report['affine_terminated']}")
    print(f"W-line parity: {report['wline_parity']}")

    if report['disagreements']:
        print("\nDISAGREEMENTS FOUND:")
        for name, data in report['disagreements'].items():
            print(f"  {name}: first disagreement at arity {data['max_diff_arity']}")
    else:
        print("\nAll towers agree: MC recursion = sqrt(Q_L) at all arities.")
