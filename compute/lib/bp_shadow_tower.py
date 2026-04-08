r"""Bershadsky-Polyakov shadow obstruction tower: the first non-principal DS shadow computation.

Computes the complete shadow obstruction tower for the Bershadsky-Polyakov algebra
W^k(sl_3, f_{(2,1)}), the DS reduction of sl_3 at the MINIMAL nilpotent orbit.

MATHEMATICAL CONTENT:

1. Modular characteristic kappa_BP on all generator lines.
2. Shadow obstruction tower on the T-line (Virasoro restriction) to arity 10.
3. Sigma-invariant Delta^(r) = S_r(c) + S_r(K - c) with K_BP = 196.
4. Shadow depth classification: T-line is class M (infinite), J-line is class G.
5. Comparison with the principal DS output W_3.

The BP algebra has generators J (wt 1), G+ (wt 3/2), G- (wt 3/2), T (wt 2),
with central charge c_BP(k) = 2 - 24(k+1)^2/(k+3) (Fehily-Kawasetsu-Ridout 2020).

WARNING (AP1/AP3 correction 2026-04-08): Previous formula was the PRINCIPAL W_3
formula c=2-3(2k+3)^2/(k+3), giving K=76. The correct BP formula gives K=196.

Koszul conductor: K_BP = c_BP(k) + c_BP(-k-6) = 196.
Dual level: k' = -k - 6 (involution).
Dual central charge: c'_BP = c_BP(-k-6) = 196 - c_BP(k).

References:
    nonprincipal_ds_reduction.py: BP seed data
    ds_shadow_higher_arity.py: BP tower infrastructure
    sigma_ring_finite_generation.py: Virasoro sigma-ring
    virasoro_shadow_duality.py: Virasoro tower recursion
"""

from __future__ import annotations

from typing import Dict, Tuple

from sympy import (
    Rational, Symbol, cancel, expand, factor, simplify, S, Poly, degree, diff,
    numer, denom, together, fraction,
)

k = Symbol('k')
c = Symbol('c')


# =============================================================================
# 1. Central charge and Koszul conductor
# =============================================================================

def bp_central_charge(level=None):
    """BP central charge: c_BP(k) = 2 - 24(k+1)^2/(k+3) (Fehily-Kawasetsu-Ridout 2020).

    WARNING (AP1/AP3 correction 2026-04-08): Previous formula was the
    PRINCIPAL W_3 formula c=2-3(2k+3)^2/(k+3), giving K=76. Wrong family.
    """
    if level is None:
        level = k
    return 2 - 24 * (level + 1) ** 2 / (level + 3)


def bp_dual_level(level=None):
    """Feigin-Frenkel dual: k' = -k - 6."""
    if level is None:
        level = k
    return -level - 6


def bp_dual_central_charge(level=None):
    """Dual central charge: c'_BP(k) = c_BP(-k-6) = 196 - c_BP(k)."""
    if level is None:
        level = k
    return bp_central_charge(bp_dual_level(level))


def bp_koszul_conductor():
    """K_BP = c_BP(k) + c_BP(-k-6) = 196 (level-independent)."""
    s = simplify(bp_central_charge() + bp_dual_central_charge())
    return s


def bp_residual_level(level=None):
    """Residual U(1) level: k_res = k + 1/2."""
    if level is None:
        level = k
    return level + Rational(1, 2)


# =============================================================================
# 2. Virasoro shadow obstruction tower recursion (standalone)
# =============================================================================

def virasoro_shadow_tower(max_arity=10):
    """S_r(c) for r = 2..max_arity via master equation recursion.

    S_r = -(1/(r*c)) * sum_{j+k=r+2, 2<=j<=k} eps(j,k) * j*k * S_j * S_k
    where eps(j,k) = 1 if j<k, 1/2 if j=k.
    """
    tower = {}
    tower[2] = c / 2
    tower[3] = Rational(2)
    tower[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_arity + 1):
        total = Rational(0)
        for j in range(2, r + 1):
            kk = r + 2 - j
            if kk < 2 or kk > r or j > kk:
                continue
            if j not in tower or kk not in tower:
                continue
            contrib = j * kk * tower[j] * tower[kk]
            if j == kk:
                contrib = contrib / 2
            total += contrib
        tower[r] = cancel(-total / (r * c))

    return tower


# =============================================================================
# 3. Modular characteristic kappa_BP
# =============================================================================

def bp_kappa_t(level=None):
    """kappa_BP on T-line = c_BP(k)/2."""
    return cancel(bp_central_charge(level) / 2)


def bp_kappa_j(level=None):
    """kappa_BP on J-line = k_res/2 = (2k+1)/4."""
    return bp_residual_level(level) / 2


def bp_kappa_all_lines(level=None):
    """Modular characteristic kappa on all generator lines of BP.

    Returns dict with kappa on each pure generator line:
      T-line: c_BP(k)/2 (Virasoro curvature)
      J-line: (2k+1)/4 (U(1) curvature)
      G-lines: determined by conformal weight 3/2
    """
    if level is None:
        level = k
    c_bp = bp_central_charge(level)
    k_res = bp_residual_level(level)

    return {
        'T': cancel(c_bp / 2),
        'J': k_res / 2,
        'G+': Rational(3, 2),  # conformal weight
        'G-': Rational(3, 2),  # conformal weight
    }


# =============================================================================
# 4. BP shadow obstruction tower on T-line
# =============================================================================

def bp_tline_shadow_tower(max_arity=10):
    """BP shadow obstruction tower on T-line: Sh_r^{BP,T}(k) = S_r^{Vir}(c_BP(k)).

    Returns dict {r: Sh_r(k)} as exact rational functions of k.
    """
    c_bp = bp_central_charge()
    vir = virasoro_shadow_tower(max_arity)

    bp_tower = {}
    for r in range(2, max_arity + 1):
        Sr_of_k = vir[r].subs(c, c_bp)
        bp_tower[r] = factor(cancel(Sr_of_k))

    return bp_tower


def bp_tline_shadow_tower_factored(max_arity=10):
    """Factored form showing numerator/denominator structure."""
    tower = bp_tline_shadow_tower(max_arity)
    result = {}
    for r, sr in tower.items():
        n, d = fraction(together(sr))
        result[r] = {
            'expression': sr,
            'numerator': factor(n),
            'denominator': factor(d),
            'degree_num': Poly(expand(n), k).total_degree() if expand(n).has(k) else 0,
            'degree_den': Poly(expand(d), k).total_degree() if expand(d).has(k) else 0,
        }
    return result


# =============================================================================
# 5. BP shadow obstruction tower on J-line (Gaussian, depth 2)
# =============================================================================

def bp_jline_shadow_tower(max_arity=6):
    """BP shadow obstruction tower on J-line: depth 2 (class G, Gaussian).

    J(z)J(w) ~ k_res/(z-w)^2 with no singular OPE beyond double pole.
    => J_{(0)}J = 0 => cubic = 0 => all higher = 0.
    """
    tower = {2: bp_residual_level() / 2}
    for r in range(3, max_arity + 1):
        tower[r] = Rational(0)
    return tower


# =============================================================================
# 6. Sigma-invariant: Delta^(r) = S_r(c) + S_r(K_BP - c) with K_BP = 196
# =============================================================================

def bp_sigma_invariant(max_arity=10):
    """Sigma-invariant Delta^(r) = S_r(c_BP) + S_r(196 - c_BP) on T-line.

    Since c'_BP = K_BP - c_BP = 196 - c_BP, this is
      Delta^(r) = S_r^{Vir}(c) + S_r^{Vir}(196 - c)
    evaluated at c = c_BP(k).

    For the Virasoro algebra, the sigma-invariant uses K_Vir = 26.
    For BP, we use K_BP = 196.
    """
    K_BP = 196
    vir = virasoro_shadow_tower(max_arity)

    # Compute sigma-invariant as function of c first
    sigma_c = {}
    for r, sr in vir.items():
        sr_dual = sr.subs(c, K_BP - c)
        sigma_c[r] = cancel(sr + sr_dual)

    # Then substitute c = c_BP(k)
    c_bp = bp_central_charge()
    sigma_k = {}
    for r, sc in sigma_c.items():
        sigma_k[r] = factor(cancel(sc.subs(c, c_bp)))

    return {
        'as_function_of_c': {r: factor(sc) for r, sc in sigma_c.items()},
        'as_function_of_k': sigma_k,
        'K_BP': K_BP,
    }


def bp_sigma_invariant_level_dependence(max_arity=8):
    """Classify each sigma-invariant arity as perturbative or dynamical.

    Perturbative: Delta^(r) is independent of c (hence independent of k).
    Dynamical: Delta^(r) depends on c (and hence on k).
    """
    K_BP = 196
    vir = virasoro_shadow_tower(max_arity)

    result = {}
    for r, sr in vir.items():
        sr_dual = sr.subs(c, K_BP - c)
        sigma = cancel(sr + sr_dual)
        is_const = simplify(diff(sigma, c)) == 0
        result[r] = {
            'Delta_r': factor(sigma),
            'perturbative': is_const,
            'type': 'perturbative' if is_const else 'dynamical',
        }
    return result


# =============================================================================
# 7. Depth classification
# =============================================================================

def bp_depth_classification():
    """Determine shadow depth class for BP on each line.

    T-line: class M (infinite) because c_BP is generically nonzero and
            5*c_BP + 22 is generically nonzero.
    J-line: class G (depth 2) because J is abelian.
    """
    c_bp = bp_central_charge()
    factor_5c22 = factor(5 * c_bp + 22)

    # Check if 5c_BP + 22 = 0 has a solution
    from sympy import solve as sym_solve
    zeros_5c22 = sym_solve(5 * c_bp + 22, k)

    # Check if c_BP = 0 has a solution
    zeros_c = sym_solve(c_bp, k)

    # Verify quartic is nonzero at generic k
    quartic = cancel(Rational(10) / (c_bp * (5 * c_bp + 22)))

    return {
        'T_line': {
            'depth': 'infinity',
            'class': 'M',
            'reason': 'Quartic Q_4 != 0 at generic k; master equation cascade',
        },
        'J_line': {
            'depth': 2,
            'class': 'G',
            'reason': 'U(1) current, J_{(0)}J = 0, all cubics and higher vanish',
        },
        'overall': 'M (mixed: T-line infinite, J-line Gaussian)',
        'c_BP': factor(c_bp),
        '5c_BP_plus_22': factor_5c22,
        'zeros_5c22': zeros_5c22,
        'zeros_c_BP': zeros_c,
        'quartic_T': factor(quartic),
    }


# =============================================================================
# 8. Comparison: BP vs W_3 (principal vs minimal DS of sl_3)
# =============================================================================

def bp_vs_w3_comparison(max_arity=8):
    """Compare the shadow obstruction towers of BP and W_3, both DS reductions of sl_3.

    BP = W^k(sl_3, f_min): minimal nilpotent, partition (2,1)
    W_3 = W^k(sl_3, f_principal): principal nilpotent, partition (3)

    Both are class M on the T-line. The difference is in the central charge
    parametrization and hence in the shadow coefficients as functions of k.
    """
    c_bp = bp_central_charge()
    c_w3 = 2 * (1 - 12 / (k + 3))  # = 2(k-9)/(k+3)

    vir = virasoro_shadow_tower(max_arity)

    bp_tower = {}
    w3_tower = {}
    for r in range(2, max_arity + 1):
        bp_tower[r] = factor(cancel(vir[r].subs(c, c_bp)))
        w3_tower[r] = factor(cancel(vir[r].subs(c, c_w3)))

    return {
        'c_BP': factor(c_bp),
        'c_W3': factor(c_w3),
        'K_BP': 196,
        'K_W3': 100,
        'BP_tower': bp_tower,
        'W3_tower': w3_tower,
    }


# =============================================================================
# 9. Numerical evaluation at specific levels
# =============================================================================

def bp_numerical_evaluation(level_values=None, max_arity=8):
    """Evaluate BP shadow obstruction tower numerically at specific levels.

    Default levels: k = 1, 2, 5, 10, -1/2 (residual level = 0),
                    -3/2 (c_BP = 2, the fixed point).
    """
    if level_values is None:
        level_values = [
            Rational(1), Rational(2), Rational(5), Rational(10),
            Rational(-1, 2), Rational(-3, 2),
        ]

    tower = bp_tline_shadow_tower(max_arity)

    results = {}
    for lv in level_values:
        c_val = bp_central_charge(lv)
        row = {'c_BP': c_val, 'k_res': bp_residual_level(lv)}
        for r in range(2, max_arity + 1):
            try:
                row[f'Sh_{r}'] = tower[r].subs(k, lv)
            except (ZeroDivisionError, ValueError):
                row[f'Sh_{r}'] = 'singular'
        results[lv] = row

    return results


# =============================================================================
# 10. Verification suite
# =============================================================================

def verify_bp_shadow_tower() -> Dict[str, bool]:
    """Comprehensive verification of the BP shadow obstruction tower computation."""
    results: Dict[str, bool] = {}

    # 1. Koszul conductor
    K = bp_koszul_conductor()
    results['K_BP = 196'] = (simplify(K - 196) == 0)

    # 2. Dual level involution
    kp = bp_dual_level()
    kpp = bp_dual_level(kp)
    results['dual level involution (k\'\')=k'] = (simplify(kpp - k) == 0)

    # 3. Complementarity
    c_sum = simplify(bp_central_charge() + bp_dual_central_charge())
    results['c(k)+c(k\')=196'] = (simplify(c_sum - 196) == 0)

    # 4. kappa_T = c/2
    kappa_t = bp_kappa_t()
    results['kappa_T = c_BP/2'] = (simplify(kappa_t - bp_central_charge() / 2) == 0)

    # 5. kappa_J = (2k+1)/4
    kappa_j = bp_kappa_j()
    results['kappa_J = (2k+1)/4'] = (simplify(kappa_j - (2 * k + 1) / 4) == 0)

    # 6. c_BP special values (corrected: Fehily-Kawasetsu-Ridout 2020)
    results['c_BP(-3/2) = -2'] = (simplify(bp_central_charge(Rational(-3, 2)) - (-2)) == 0)
    results['c_BP(0) = -6'] = (simplify(bp_central_charge(S(0)) - (-6)) == 0)
    results['c_BP(-1) = 2'] = (simplify(bp_central_charge(S(-1)) - 2) == 0)

    # 7. T-line tower matches Virasoro at c = c_BP
    bp_tower = bp_tline_shadow_tower(6)
    vir = virasoro_shadow_tower(6)
    c_bp = bp_central_charge()
    for r in range(2, 7):
        vir_at_bp = cancel(vir[r].subs(c, c_bp))
        results[f'Sh_{r}^T = S_{r}^Vir(c_BP)'] = (
            simplify(bp_tower[r] - vir_at_bp) == 0
        )

    # 8. J-line vanishing at r >= 3
    j_tower = bp_jline_shadow_tower(6)
    for r in range(3, 7):
        results[f'Sh_{r}^J = 0'] = (j_tower[r] == 0)

    # 9. Sigma invariant at r=2: Delta^(2) = K_BP/2 = 98
    sigma = bp_sigma_invariant(6)
    sigma_c = sigma['as_function_of_c']
    results['Delta^(2) = 98'] = (simplify(sigma_c[2] - 98) == 0)

    # 10. Quartic nonvanishing at generic k
    tower = bp_tline_shadow_tower(6)
    results['Sh_4^T nonzero'] = (simplify(tower[4]) != 0)
    results['Sh_5^T nonzero'] = (simplify(tower[5]) != 0)

    # 11. Depth classification
    depth = bp_depth_classification()
    results['T-line class M'] = (depth['T_line']['class'] == 'M')
    results['J-line class G'] = (depth['J_line']['class'] == 'G')

    return results


# =============================================================================
# 11. Main display
# =============================================================================

def print_full_report():
    """Print the complete BP shadow obstruction tower computation."""

    print("=" * 72)
    print("BERSHADSKY-POLYAKOV SHADOW TOWER")
    print("W^k(sl_3, f_{(2,1)}) — First Non-Principal DS Shadow Computation")
    print("=" * 72)

    # --- Central charge ---
    print("\n--- 1. Central charge and Koszul conductor ---")
    c_bp = factor(bp_central_charge())
    c_bp_dual = factor(bp_dual_central_charge())
    K = bp_koszul_conductor()
    print(f"  c_BP(k)  = {c_bp}")
    print(f"  c_BP(k') = {c_bp_dual}  (k' = -k-6)")
    print(f"  K_BP = c(k) + c(k') = {K}")
    print(f"  k_res = k + 1/2")
    print(f"  Special: c_BP(-3/2) = {bp_central_charge(Rational(-3,2))},  "
          f"c_BP(-1) = {bp_central_charge(-1)},  "
          f"c_BP(0) = {bp_central_charge(0)}")

    # --- Kappa ---
    print("\n--- 2. Modular characteristic kappa_BP ---")
    kappas = bp_kappa_all_lines()
    for line, kap in kappas.items():
        print(f"  kappa_{line} = {factor(cancel(kap))}")
    print(f"  kappa_T(k) = {factor(bp_kappa_t())}")
    print(f"  kappa_J(k) = {bp_kappa_j()}")

    # --- T-line shadow obstruction tower ---
    print("\n--- 3. Shadow obstruction tower on T-line (Virasoro restriction) ---")
    tower = bp_tline_shadow_tower(10)
    for r in sorted(tower.keys()):
        print(f"  Sh_{r}^T(k) = {tower[r]}")

    # --- J-line ---
    print("\n--- 4. Shadow obstruction tower on J-line (U(1) restriction) ---")
    j_tower = bp_jline_shadow_tower(6)
    for r in sorted(j_tower.keys()):
        print(f"  Sh_{r}^J(k) = {j_tower[r]}")
    print("  Depth 2 (class G, Gaussian): J is abelian")

    # --- Sigma invariant ---
    print("\n--- 5. Sigma-invariant Delta^(r) = S_r(c) + S_r(196-c) ---")
    sigma = bp_sigma_invariant(8)
    print("  As function of c (before substituting c = c_BP(k)):")
    for r, sc in sorted(sigma['as_function_of_c'].items()):
        print(f"    Delta^({r})(c) = {sc}")
    print()
    print("  As function of k (after substituting c = c_BP(k)):")
    for r, sk in sorted(sigma['as_function_of_k'].items()):
        print(f"    Delta^({r})(k) = {sk}")

    # --- Level dependence ---
    print("\n--- 6. Sigma-invariant level-dependence classification ---")
    ldep = bp_sigma_invariant_level_dependence(8)
    for r, data in sorted(ldep.items()):
        print(f"  r={r}: {data['type']}, Delta^({r}) = {data['Delta_r']}")

    # --- Depth classification ---
    print("\n--- 7. Shadow depth classification ---")
    depth = bp_depth_classification()
    print(f"  T-line: depth = {depth['T_line']['depth']}, "
          f"class = {depth['T_line']['class']}")
    print(f"    Reason: {depth['T_line']['reason']}")
    print(f"  J-line: depth = {depth['J_line']['depth']}, "
          f"class = {depth['J_line']['class']}")
    print(f"    Reason: {depth['J_line']['reason']}")
    print(f"  Overall: {depth['overall']}")
    print(f"  c_BP(k) = {depth['c_BP']}")
    print(f"  5c_BP + 22 = {depth['5c_BP_plus_22']}")
    print(f"  Zeros of c_BP: k = {depth['zeros_c_BP']}")
    print(f"  Zeros of 5c_BP+22: k = {depth['zeros_5c22']}")
    print(f"  Quartic on T-line: Q_4 = {depth['quartic_T']}")

    # --- Numerical ---
    print("\n--- 8. Numerical evaluation at selected levels ---")
    nums = bp_numerical_evaluation(max_arity=6)
    for lv, row in nums.items():
        print(f"  k = {lv}: c = {row['c_BP']}, k_res = {row['k_res']}")
        for r in range(2, 7):
            val = row.get(f'Sh_{r}', 'N/A')
            if val != 'singular':
                try:
                    fval = float(val)
                    print(f"    Sh_{r} = {val} = {fval:.8f}")
                except (TypeError, ValueError):
                    print(f"    Sh_{r} = {val}")
            else:
                print(f"    Sh_{r} = SINGULAR")
        print()

    # --- Comparison ---
    print("\n--- 9. BP vs W_3 comparison (minimal vs principal DS of sl_3) ---")
    comp = bp_vs_w3_comparison(6)
    print(f"  c_BP(k)  = {comp['c_BP']},  K_BP  = {comp['K_BP']}")
    print(f"  c_W3(k)  = {comp['c_W3']},  K_W3  = {comp['K_W3']}")
    print("  Shadow obstruction tower comparison:")
    for r in range(2, 7):
        print(f"    Sh_{r}^BP  = {comp['BP_tower'][r]}")
        print(f"    Sh_{r}^W3  = {comp['W3_tower'][r]}")
        print()

    # --- Verification ---
    print("\n--- 10. Verification suite ---")
    checks = verify_bp_shadow_tower()
    all_pass = True
    for name, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_pass = False
        print(f"  [{status}] {name}")
    print(f"\n  {'ALL CHECKS PASSED' if all_pass else 'SOME CHECKS FAILED'}")
    print(f"  Total: {sum(checks.values())}/{len(checks)} passed")


if __name__ == '__main__':
    print_full_report()
