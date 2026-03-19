"""Virasoro shadow tower duality analysis — Vir_c^! = Vir_{26-c}.

Computes the shadow tower S_r(c) for the Virasoro algebra to high arity
using the master equation recursion, then analyzes:

1. Complementarity sums D_r(c) = S_r(c) + S_r(26-c)
2. Duality ratios R_r(c) = S_r(c) / S_r(26-c)
3. Self-dual values S_r(13)
4. Factorization of S_r(c) over Q(c)
5. Pole structure and degree growth
6. Ratio S_{r+1}/S_r stability
7. Shadow generating function and ODE structure

The recursion (from the master equation on a single primary line):

    S_r = -(1/(2r * kappa)) * sum_{j+k=r+2, 3<=j<=k} eps(j,k) * 2jk * S_j * S_k

where kappa = c/2 (Virasoro curvature), eps(j,k) = 1 if j<k, 1/2 if j=k.

Initial data: S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)].

References:
    - thm:virasoro-koszul-duality (chiral_koszul_pairs.tex)
    - cor:virasoro-quintic-shadow-explicit (w_algebras.tex)
    - thm:complementarity-scalar (higher_genus_complementarity.tex)
"""

from __future__ import annotations

from sympy import (
    Rational, Symbol, cancel, degree, denom, factor, numer,
    oo, Poly, simplify, solve, S, together, fraction, lcm,
)
from functools import lru_cache


c = Symbol('c')


# ═══════════════════════════════════════════════════════════════════════
# Core recursion
# ═══════════════════════════════════════════════════════════════════════

def virasoro_shadow_tower(max_arity=20):
    """Compute S_r(c) for r = 2, ..., max_arity using exact sympy arithmetic.

    Returns dict {r: S_r} where S_r is a rational function in c.

    The recursion (derived from nabla_H(Sh_r) + o^(r) = 0):
        S_r = -(1/(r*c)) * sum_{j+k=r+2, 2<=j<=k} eps(j,k) * jk * S_j * S_k

    where eps(j,k) = 1 if j<k, 1/2 if j=k, and P = 2/c is the propagator.

    NOTE: The sum runs over j,k >= 2 with j+k = r+2. The j=2 terms
    contribute the "Hessian propagation" while j>=3 terms are the
    obstruction sources.
    """
    S = {}
    S[2] = c / 2               # kappa
    S[3] = Rational(2)          # cubic shadow (constant!)
    S[4] = Rational(10) / (c * (5 * c + 22))  # quartic contact

    for r in range(5, max_arity + 1):
        total = Rational(0)
        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k > r or j > k:
                continue
            if j not in S or k not in S:
                continue
            contrib = j * k * S[j] * S[k]
            if j == k:
                contrib = contrib / 2
            total += contrib
        S[r] = cancel(-total / (r * c))

    return S


def virasoro_shadow_factored(max_arity=20):
    """Return S_r(c) in factored form."""
    tower = virasoro_shadow_tower(max_arity)
    return {r: factor(s) for r, s in tower.items()}


# ═══════════════════════════════════════════════════════════════════════
# Duality analysis: Vir_c^! = Vir_{26-c}
# ═══════════════════════════════════════════════════════════════════════

def complementarity_sum(max_arity=15):
    """D_r(c) = S_r(c) + S_r(26-c) for each r.

    At r=2: D_2 = c/2 + (26-c)/2 = 13. (Theorem C scalar level.)
    """
    tower = virasoro_shadow_tower(max_arity)
    D = {}
    for r, sr in tower.items():
        sr_dual = sr.subs(c, 26 - c)
        D[r] = cancel(sr + sr_dual)
    return D


def duality_ratio(max_arity=15):
    """R_r(c) = S_r(c) / S_r(26-c) for each r."""
    tower = virasoro_shadow_tower(max_arity)
    R = {}
    for r, sr in tower.items():
        sr_dual = sr.subs(c, 26 - c)
        R[r] = factor(cancel(sr / sr_dual))
    return R


def self_dual_values(max_arity=20):
    """S_r(13) — values at the self-dual point c=13."""
    tower = virasoro_shadow_tower(max_arity)
    return {r: sr.subs(c, 13) for r, sr in tower.items()}


# ═══════════════════════════════════════════════════════════════════════
# Factorization and pole analysis
# ═══════════════════════════════════════════════════════════════════════

def factorization_data(max_arity=15):
    """Factor numerator and denominator of S_r(c) over Q.

    Returns dict {r: {'num': factored_num, 'den': factored_den,
                       'num_factors': [...], 'den_factors': [...]}}.
    """
    tower = virasoro_shadow_tower(max_arity)
    data = {}
    for r, sr in tower.items():
        sr_simplified = cancel(sr)
        n, d = fraction(sr_simplified)
        n_factored = factor(n)
        d_factored = factor(d)
        # Extract irreducible factors
        n_poly = Poly(n, c) if n.has(c) else None
        d_poly = Poly(d, c) if d.has(c) else None
        data[r] = {
            'num': n_factored,
            'den': d_factored,
            'num_deg': degree(n, c) if n.has(c) else 0,
            'den_deg': degree(d, c) if d.has(c) else 0,
            'expression': factor(sr_simplified),
        }
    return data


def pole_structure(max_arity=15):
    """Find poles of S_r(c) and track which are new at each arity.

    Returns dict {r: {'poles': set, 'new_poles': set, 'pole_orders': dict}}.
    """
    tower = virasoro_shadow_tower(max_arity)
    all_prev_poles = set()
    result = {}

    for r in sorted(tower.keys()):
        sr = cancel(tower[r])
        _, d = fraction(sr)
        if not d.has(c):
            result[r] = {'poles': set(), 'new_poles': set(), 'pole_orders': {}}
            continue

        poles_r = set()
        pole_orders = {}
        d_poly = Poly(d, c)
        # Find roots of denominator
        roots = solve(d, c)
        for root in roots:
            poles_r.add(root)
            # Compute multiplicity
            test_d = d
            mult = 0
            while simplify(test_d.subs(c, root)) == 0:
                test_d = cancel(test_d / (c - root))
                mult += 1
                if mult > 20:
                    break
            pole_orders[root] = mult

        new_poles = poles_r - all_prev_poles
        all_prev_poles = all_prev_poles | poles_r
        result[r] = {
            'poles': poles_r,
            'new_poles': new_poles,
            'pole_orders': pole_orders,
        }

    return result


def degree_growth(max_arity=20):
    """Track deg_c(numerator) and deg_c(denominator) of S_r(c).

    Returns dict {r: (num_deg, den_deg)}.
    """
    tower = virasoro_shadow_tower(max_arity)
    result = {}
    for r in sorted(tower.keys()):
        sr = cancel(tower[r])
        n, d = fraction(sr)
        nd = degree(n, c) if n.has(c) else 0
        dd = degree(d, c) if d.has(c) else 0
        result[r] = (nd, dd)
    return result


# ═══════════════════════════════════════════════════════════════════════
# Ratio analysis
# ═══════════════════════════════════════════════════════════════════════

def consecutive_ratios(max_arity=15):
    """S_{r+1}(c) / S_r(c) for each r. Does it stabilize?"""
    tower = virasoro_shadow_tower(max_arity)
    ratios = {}
    for r in range(2, max_arity):
        if r in tower and (r + 1) in tower and tower[r] != 0:
            ratios[r] = factor(cancel(tower[r + 1] / tower[r]))
    return ratios


# ═══════════════════════════════════════════════════════════════════════
# Denominator linear-factor analysis
# ═══════════════════════════════════════════════════════════════════════

def denominator_roots(max_arity=15):
    """Find all roots of the denominator of S_r(c).

    KEY QUESTION: does the denominator factor into LINEAR factors over Q?
    """
    tower = virasoro_shadow_tower(max_arity)
    result = {}
    for r in sorted(tower.keys()):
        sr = cancel(tower[r])
        _, d = fraction(sr)
        if not d.has(c):
            result[r] = {'roots': [], 'all_linear': True, 'den': d}
            continue
        roots = solve(d, c)
        d_poly = Poly(d, c)
        # Check if all roots are rational
        all_linear = all(root.is_rational for root in roots)
        # Check degree matches number of roots (counting multiplicity)
        result[r] = {
            'roots': sorted(roots, key=lambda x: float(x)),
            'all_linear': all_linear,
            'den_degree': d_poly.degree(),
            'num_roots': len(roots),
        }
    return result


# ═══════════════════════════════════════════════════════════════════════
# Generating function analysis
# ═══════════════════════════════════════════════════════════════════════

def shadow_generating_function_coeffs(max_arity=15):
    """G(t, c) = sum_{r>=2} S_r(c) * t^r.

    Returns the list of coefficients for analysis.
    """
    tower = virasoro_shadow_tower(max_arity)
    return [(r, tower[r]) for r in sorted(tower.keys())]


def shadow_gf_at_c(c_val, max_arity=20):
    """Numerical coefficients of G(t, c_val) = sum S_r(c_val) t^r."""
    tower = virasoro_shadow_tower(max_arity)
    return {r: float(sr.subs(c, c_val)) for r, sr in tower.items()}


# ═══════════════════════════════════════════════════════════════════════
# Complementarity sum analysis
# ═══════════════════════════════════════════════════════════════════════

def complementarity_analysis(max_arity=15):
    """Detailed analysis of D_r(c) = S_r(c) + S_r(26-c).

    Questions:
    - Is D_r a polynomial in c? (True for r=2: D_2 = 13.)
    - Is D_r identically zero for some r?
    - What is the structure?
    """
    D = complementarity_sum(max_arity)
    result = {}
    for r, dr in D.items():
        dr_simplified = cancel(dr)
        n, d = fraction(dr_simplified)
        is_polynomial = not d.has(c)
        is_zero = simplify(dr) == 0
        # Check symmetry: D_r(c) = D_r(26-c)?
        is_self_dual_symmetric = simplify(dr - dr.subs(c, 26 - c)) == 0
        result[r] = {
            'value': factor(dr_simplified),
            'is_polynomial': is_polynomial,
            'is_zero': is_zero,
            'is_symmetric_under_c_to_26mc': is_self_dual_symmetric,
        }
    return result


# ═══════════════════════════════════════════════════════════════════════
# Main driver
# ═══════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 15

    print(f"Virasoro shadow tower duality analysis (arities 2..{N})")
    print("=" * 70)

    # 1. Shadow tower
    print("\n1. SHADOW TOWER S_r(c):")
    tower = virasoro_shadow_factored(N)
    for r in sorted(tower.keys()):
        print(f"   S_{r:2d}(c) = {tower[r]}")

    # 2. Complementarity sums
    print("\n2. COMPLEMENTARITY SUMS D_r(c) = S_r(c) + S_r(26-c):")
    analysis = complementarity_analysis(N)
    for r in sorted(analysis.keys()):
        a = analysis[r]
        flags = []
        if a['is_zero']:
            flags.append("ZERO")
        if a['is_polynomial']:
            flags.append("polynomial")
        if a['is_symmetric_under_c_to_26mc']:
            flags.append("symmetric")
        print(f"   D_{r:2d}(c) = {a['value']}  [{', '.join(flags)}]")

    # 3. Duality ratios
    print("\n3. DUALITY RATIOS R_r(c) = S_r(c) / S_r(26-c):")
    R = duality_ratio(N)
    for r in sorted(R.keys()):
        print(f"   R_{r:2d}(c) = {R[r]}")

    # 4. Self-dual values
    print("\n4. SELF-DUAL VALUES S_r(13):")
    vals = self_dual_values(N)
    for r in sorted(vals.keys()):
        print(f"   S_{r:2d}(13) = {vals[r]}")

    # 5. Degree growth
    print("\n5. DEGREE GROWTH (num_deg, den_deg):")
    dg = degree_growth(N)
    for r in sorted(dg.keys()):
        nd, dd = dg[r]
        print(f"   r={r:2d}: num_deg={nd}, den_deg={dd}, total_deg={nd+dd}")

    # 6. Denominator roots
    print("\n6. DENOMINATOR ROOTS (linear factor question):")
    dr = denominator_roots(N)
    for r in sorted(dr.keys()):
        info = dr[r]
        linear_flag = "ALL LINEAR" if info['all_linear'] else "NON-LINEAR"
        print(f"   r={r:2d}: roots={info['roots']}  [{linear_flag}]")

    # 7. Pole structure
    print("\n7. NEW POLES AT EACH ARITY:")
    ps = pole_structure(N)
    for r in sorted(ps.keys()):
        info = ps[r]
        if info['new_poles']:
            print(f"   r={r:2d}: new poles = {info['new_poles']}, orders = {info['pole_orders']}")

    # 8. Consecutive ratios
    print("\n8. CONSECUTIVE RATIOS S_{r+1}/S_r:")
    ratios = consecutive_ratios(N)
    for r in sorted(ratios.keys()):
        print(f"   S_{r+1:2d}/S_{r:2d} = {ratios[r]}")

    # 9. Numerical generating function at self-dual point
    print("\n9. NUMERICAL G(t, c=13): coefficients S_r(13):")
    gf = shadow_gf_at_c(13, N)
    for r in sorted(gf.keys()):
        print(f"   r={r:2d}: S_r(13) = {gf[r]:.10e}")
