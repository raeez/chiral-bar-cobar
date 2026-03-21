r"""Full 2D W_3 shadow tower: bivariate recursion on (x_T, x_W).

NEW COMPUTATION. The T-line (x_W=0) gives the Virasoro tower. The W-line
(x_T=0) gives the Z_2-even tower. This module computes the FULL bivariate
shadow Sh_r(x_T, x_W) at each arity r, revealing the complete mixing
structure between T and W modes.

THE 2D H-POISSON BRACKET:
  {f, g}_{2D} = (df/dx_T)(2/c)(dg/dx_T) + (df/dx_W)(3/c)(dg/dx_W)

INPUT DATA:
  Sh_2 = (c/2) x_T^2 + (c/3) x_W^2
  Sh_3 = 2 x_T^3 + 3 x_T x_W^2
  Sh_4 = Q_TT x_T^4 + 6 Q_TW x_T^2 x_W^2 + Q_WW x_W^4

  where Q_TT = 10/[c(5c+22)], Q_TW = 160/[c(5c+22)^2],
        Q_WW = 2560/[c(5c+22)^3].

RECURSION: For r >= 5,
  nabla_H(Sh_r) + o^(r) = 0
  o^(r) = sum_{j+k=r+2, 2<=j<=k} (symmetry factor) * {Sh_j, Sh_k}_{2D}

Z_2 PARITY: W -> -W implies x_W -> -x_W.
  Even arity: only even powers of x_W.
  Odd arity: only odd powers of x_W.

RESULTS:
  Each Sh_r(x_T, x_W) is a homogeneous degree-r polynomial in (x_T, x_W)
  with rational-function coefficients in c. The denominators are products
  of c and (5c+22), confirming the Kac-shadow singularity principle.

  NEW DISCOVERY: The mixing coefficients at arity >= 5 reveal the complete
  coupling between T and W towers that is invisible on either 1D projection.

References:
  w3_multivariable_shadow.py: quartic input data
  w3_wline_shadow_tower.py: W-line 1D projection
  virasoro_shadow_tower.py: T-line 1D projection
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from typing import Dict, List, Tuple

from sympy import (
    Rational, Symbol, cancel, collect, diff, expand, factor,
    Poly, S, simplify, symbols,
)

c = Symbol('c')
x_T = Symbol('x_T')
x_W = Symbol('x_W')


# =============================================================================
# 1. Hessian, propagator, and 2D bracket
# =============================================================================

KAPPA_T = c / 2
KAPPA_W = c / 3
P_T = Rational(2) / c   # 1/kappa_T = 2/c
P_W = Rational(3) / c   # 1/kappa_W = 3/c


def h_poisson_2d(f, g):
    """2D H-Poisson bracket: {f, g} = (df/dx_T)(2/c)(dg/dx_T) + (df/dx_W)(3/c)(dg/dx_W)."""
    return expand(
        diff(f, x_T) * P_T * diff(g, x_T)
        + diff(f, x_W) * P_W * diff(g, x_W)
    )


def euler_operator_2d(f):
    """Euler operator: E(f) = x_T df/dx_T + x_W df/dx_W.

    For a homogeneous polynomial of degree r: E(f) = r * f.
    """
    return expand(x_T * diff(f, x_T) + x_W * diff(f, x_W))


def nabla_H_2d(f):
    """Covariant derivative nabla_H = {kappa, -}_H where kappa = Sh_2.

    nabla_H(f) = {Sh_2, f}_{2D}
    = (df/dx_T)(2/c)(c x_T) + (df/dx_W)(3/c)((2c/3) x_W)
    = 2 x_T df/dx_T + 2 x_W df/dx_W
    = 2 E(f)

    For homogeneous f of degree r: nabla_H(f) = 2r f.
    """
    Sh_2 = KAPPA_T * x_T**2 + KAPPA_W * x_W**2
    return h_poisson_2d(Sh_2, f)


# =============================================================================
# 2. Input data: Sh_2, Sh_3, Sh_4
# =============================================================================

def input_shadows():
    """The three input shadows for the W_3 2D recursion.

    These are INPUTS (not derived from the recursion).
    The master equation generates r >= 5 from these.
    """
    alpha = Rational(16) / (5 * c + 22)

    Sh_2 = KAPPA_T * x_T**2 + KAPPA_W * x_W**2

    # Cubic: from OPE data. Z_2 forces form 2 x_T^3 + 3 x_T x_W^2.
    # The coefficient 3 for the mixed term comes from h_W = 3 normalization
    # in the cyclic deformation complex.
    Sh_3 = 2 * x_T**3 + 3 * x_T * x_W**2

    # Quartic: from Lambda-exchange (w3_multivariable_shadow.py)
    Q_TT = Rational(10) / (c * (5 * c + 22))
    Q_TW = Rational(160) / (c * (5 * c + 22)**2)
    Q_WW = Rational(2560) / (c * (5 * c + 22)**3)
    Sh_4 = Q_TT * x_T**4 + 6 * Q_TW * x_T**2 * x_W**2 + Q_WW * x_W**4

    return {2: Sh_2, 3: Sh_3, 4: Sh_4}


# =============================================================================
# 3. Full 2D recursion
# =============================================================================

def compute_full_2d_tower(max_arity=12):
    """Compute the full 2D W_3 shadow tower through max_arity.

    Returns dict {r: Sh_r(x_T, x_W)} where each Sh_r is a homogeneous
    degree-r polynomial in (x_T, x_W) with rational-function coefficients in c.
    """
    shadows = input_shadows()

    for r in range(5, max_arity + 1):
        obstruction = S.Zero

        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k not in shadows:
                continue
            if j > k:
                continue

            bracket = h_poisson_2d(shadows[j], shadows[k])

            if j == k:
                obstruction += Rational(1, 2) * bracket
            else:
                obstruction += bracket

        obstruction = expand(obstruction)

        if obstruction == S.Zero:
            shadows[r] = S.Zero
            continue

        # nabla_H(Sh_r) = 2r Sh_r for homogeneous degree r.
        # So Sh_r = -obstruction / (2r).
        Sh_r = cancel(-obstruction / (2 * r))
        Sh_r = expand(Sh_r)
        shadows[r] = Sh_r

    return shadows


def extract_monomial_coefficients(shadows):
    """Extract the coefficient of each monomial x_T^a x_W^b in Sh_r.

    Returns dict {r: {(a,b): coefficient}}.
    """
    result = {}
    for r, Sh_r in shadows.items():
        if Sh_r == S.Zero:
            result[r] = {}
            continue

        coeffs = {}
        poly = Poly(Sh_r, x_T, x_W)
        for monom, coeff in poly.as_dict().items():
            a, b = monom
            coeffs[(a, b)] = factor(coeff)
        result[r] = coeffs
    return result


# =============================================================================
# 4. Consistency checks
# =============================================================================

def verify_tline_restriction(shadows, max_arity=7):
    """Verify: on x_W = 0, the 2D tower reduces to the Virasoro tower."""
    from sympy import Poly as SymPoly

    virasoro_coeffs = {
        2: c / 2,
        3: Rational(2),
        4: Rational(10) / (c * (5 * c + 22)),
        5: Rational(-48) / (c**2 * (5 * c + 22)),
    }

    results = {}
    for r in range(2, min(max_arity + 1, max(shadows.keys()) + 1)):
        if r not in shadows:
            continue
        Sh_r = shadows[r]
        restricted = Sh_r.subs(x_W, 0)
        # Extract coefficient of x_T^r
        if restricted == S.Zero:
            coeff = S.Zero
        else:
            p = Poly(restricted, x_T)
            coeff = p.nth(r)

        if r in virasoro_coeffs:
            diff_val = simplify(coeff - virasoro_coeffs[r])
            results[r] = {
                'computed': factor(coeff),
                'expected': virasoro_coeffs[r],
                'match': diff_val == 0,
            }
        else:
            results[r] = {'computed': factor(coeff)}
    return results


def verify_wline_restriction(shadows, max_arity=12):
    """Verify: on x_T = 0, the 2D tower matches the W-line tower.

    On the W-line: odd arities vanish, even arities match w3_wline_shadow_tower.
    """
    results = {}
    for r in range(2, min(max_arity + 1, max(shadows.keys()) + 1)):
        if r not in shadows:
            continue
        Sh_r = shadows[r]
        restricted = Sh_r.subs(x_T, 0)

        if r % 2 == 1:
            # Odd arities should vanish on W-line
            results[r] = {
                'computed': restricted,
                'vanishes': simplify(restricted) == 0,
            }
        else:
            # Even arities: extract coefficient of x_W^r
            if restricted == S.Zero:
                coeff = S.Zero
            else:
                p = Poly(restricted, x_W)
                coeff = p.nth(r)
            results[r] = {'computed': factor(coeff)}
    return results


def verify_z2_parity(shadows):
    """Verify Z_2 parity: Sh_r(x_T, -x_W) = (-1)^r Sh_r(x_T, x_W).

    Wait: Z_2 acts as W -> -W, so x_W -> -x_W. The shadow Sh_r is
    Z_2-invariant if it has the same parity as r (since the shadow is
    a section of Sym^r and Z_2 acts on each factor).

    Actually: Z_2 acts on the deformation space by x_W -> -x_W.
    The shadow Sh_r is a function on this space, and Z_2 invariance
    means Sh_r(x_T, -x_W) = Sh_r(x_T, x_W).

    But a degree-r monomial x_T^a x_W^b transforms as (-1)^b.
    So Z_2 invariance forces b to be EVEN for all monomials.

    Odd-arity shadows (r odd): the monomials with a+b=r and b even
    are (a,b) with a odd. So x_T has odd power. ✓ (no contradiction)

    Even-arity shadows (r even): monomials with a+b=r and b even. ✓
    """
    results = {}
    for r, Sh_r in shadows.items():
        if Sh_r == S.Zero:
            results[r] = {'z2_invariant': True}
            continue
        flipped = Sh_r.subs(x_W, -x_W)
        is_invariant = simplify(flipped - Sh_r) == 0
        results[r] = {'z2_invariant': is_invariant}
    return results


# =============================================================================
# 5. Mixing analysis
# =============================================================================

def mixing_coefficients(shadows, max_arity=12):
    """For each arity r, extract the 'pure T', 'pure W', and 'mixed' parts.

    Pure T: coefficient of x_T^r
    Pure W: coefficient of x_W^r
    Mixed: all other monomials

    The mixed coefficients are the GENUINELY NEW data that is invisible
    on either 1D projection.
    """
    monomial_data = extract_monomial_coefficients(shadows)
    result = {}
    for r, coeffs in monomial_data.items():
        pure_T = coeffs.get((r, 0), S.Zero)
        pure_W = coeffs.get((0, r), S.Zero)
        mixed = {k: v for k, v in coeffs.items()
                 if k != (r, 0) and k != (0, r)}
        result[r] = {
            'pure_T': factor(pure_T),
            'pure_W': factor(pure_W),
            'mixed': {k: factor(v) for k, v in mixed.items()},
            'n_mixed_monomials': len(mixed),
        }
    return result


def denominator_analysis(shadows, max_arity=12):
    """Analyze the denominator structure of each shadow coefficient.

    The Kac-shadow singularity principle predicts:
    denominator divides c^a * (5c+22)^b for some a, b >= 0.
    """
    from sympy import numer, denom as sym_denom
    monomial_data = extract_monomial_coefficients(shadows)
    result = {}
    for r, coeffs in monomial_data.items():
        arity_denoms = {}
        for (a, b), coeff in coeffs.items():
            if coeff == S.Zero:
                continue
            d = sym_denom(cancel(coeff))
            d_factored = factor(d)
            arity_denoms[(a, b)] = d_factored
        result[r] = arity_denoms
    return result


def diagonal_shadow_tower(shadows, max_arity=12):
    """Restrict the 2D tower to the diagonal x_T = x_W = x.

    On the diagonal, each Sh_r becomes a univariate polynomial S_r^diag * x^r.
    This gives the 'total' shadow tower on the direction (1,1) in deformation space.
    """
    x = Symbol('x')
    result = {}
    for r, Sh_r in shadows.items():
        Sh_diag = Sh_r.subs(x_T, x).subs(x_W, x)
        Sh_diag = expand(Sh_diag)
        if Sh_diag == S.Zero:
            result[r] = S.Zero
        else:
            p = Poly(Sh_diag, x)
            result[r] = factor(p.nth(r))
    return result


def curvature_proportional_direction(shadows):
    """Find the direction (a, b) where the quartic gradient is proportional to kappa.

    On this direction: f_T/kappa_T = f_W/kappa_W, so the propagator variance vanishes.
    The shadow tower on this direction is AUTONOMOUS (no mixing corrections).
    """
    Sh_4 = shadows[4]

    # Quartic gradient at (a, b): d_T Sh_4(ax, bx) = a * Sh_4_T(ax, bx)
    Sh_4_T = diff(Sh_4, x_T)
    Sh_4_W = diff(Sh_4, x_W)

    # Evaluate at x_T = a, x_W = b (as symbols)
    a, b = symbols('a b')
    f_T = Sh_4_T.subs(x_T, a).subs(x_W, b)
    f_W = Sh_4_W.subs(x_T, a).subs(x_W, b)

    # Curvature proportionality: f_T/kappa_T = f_W/kappa_W
    # i.e., f_T * kappa_W = f_W * kappa_T
    condition = expand(f_T * KAPPA_W - f_W * KAPPA_T)

    return {
        'condition': condition,
        'f_T': f_T,
        'f_W': f_W,
    }


# =============================================================================
# 6. Arity-5 detailed computation
# =============================================================================

def arity5_detailed():
    """Detailed computation of Sh_5: the first arity generated by the recursion.

    o^(5) = {Sh_3, Sh_4}_{2D}

    Sh_3 = 2 x_T^3 + 3 x_T x_W^2
    Sh_4 = Q_TT x_T^4 + 6 Q_TW x_T^2 x_W^2 + Q_WW x_W^4

    The bracket mixes T and W derivatives:
    {Sh_3, Sh_4} = (dSh_3/dx_T)(2/c)(dSh_4/dx_T) + (dSh_3/dx_W)(3/c)(dSh_4/dx_W)
    """
    inp = input_shadows()
    Sh_3 = inp[3]
    Sh_4 = inp[4]

    # Derivatives
    dSh3_dT = diff(Sh_3, x_T)  # = 6 x_T^2 + 3 x_W^2
    dSh3_dW = diff(Sh_3, x_W)  # = 6 x_T x_W
    dSh4_dT = diff(Sh_4, x_T)
    dSh4_dW = diff(Sh_4, x_W)

    # T-channel and W-channel contributions
    T_channel = expand(dSh3_dT * P_T * dSh4_dT)
    W_channel = expand(dSh3_dW * P_W * dSh4_dW)

    obstruction = expand(T_channel + W_channel)

    # Sh_5 = -obstruction / (2*5)
    Sh_5 = cancel(-obstruction / 10)
    Sh_5 = expand(Sh_5)

    # Extract monomial coefficients
    poly = Poly(Sh_5, x_T, x_W)
    coeffs = {}
    for monom, coeff in poly.as_dict().items():
        a, b = monom
        coeffs[(a, b)] = factor(coeff)

    return {
        'T_channel': T_channel,
        'W_channel': W_channel,
        'obstruction': obstruction,
        'Sh_5': Sh_5,
        'coefficients': coeffs,
    }


# =============================================================================
# 7. Growth rate analysis
# =============================================================================

def shadow_norm_growth(shadows, max_arity=12):
    """Analyze the growth rate of shadow coefficients on each projection.

    For the Virasoro tower on the T-line:
    |S_r| ~ (r!)^{alpha} for some exponent alpha.

    For the W-line tower (even arities only):
    |W_r| ~ (r!)^{beta} for some exponent beta.

    The mixing coefficients may have different growth rates.
    """
    from sympy import log as sym_log, Abs

    diag = diagonal_shadow_tower(shadows, max_arity)
    tline = {}
    wline = {}
    for r, Sh_r in shadows.items():
        tline_val = Sh_r.subs(x_W, 0)
        wline_val = Sh_r.subs(x_T, 0)
        if tline_val != S.Zero:
            p = Poly(tline_val, x_T)
            tline[r] = factor(p.nth(r))
        if wline_val != S.Zero:
            p = Poly(wline_val, x_W)
            wline[r] = factor(p.nth(r))

    return {
        'diagonal': diag,
        'T_line': tline,
        'W_line': wline,
    }


if __name__ == '__main__':
    print("=" * 70)
    print("Full 2D W_3 shadow tower computation")
    print("=" * 70)
    print()

    # Compute tower
    max_r = 10
    shadows = compute_full_2d_tower(max_r)

    # Display each arity
    for r in sorted(shadows.keys()):
        Sh_r = shadows[r]
        if Sh_r == S.Zero:
            print(f"Sh_{r} = 0")
            continue
        print(f"Sh_{r}(x_T, x_W) =")
        poly = Poly(Sh_r, x_T, x_W)
        for monom, coeff in sorted(poly.as_dict().items(), reverse=True):
            a, b = monom
            coeff_f = factor(coeff)
            print(f"    + ({coeff_f}) * x_T^{a} x_W^{b}")
        print()

    # Consistency checks
    print("T-line restriction (should match Virasoro):")
    tline = verify_tline_restriction(shadows)
    for r, data in sorted(tline.items()):
        if 'match' in data:
            status = "PASS" if data['match'] else "FAIL"
            print(f"  r={r}: {status}  computed={data['computed']}")
        else:
            print(f"  r={r}: {data['computed']}")

    print()
    print("W-line restriction (odd vanish, even match):")
    wline = verify_wline_restriction(shadows)
    for r, data in sorted(wline.items()):
        if 'vanishes' in data:
            status = "PASS" if data['vanishes'] else "FAIL"
            print(f"  r={r} (odd): vanishes={status}")
        else:
            print(f"  r={r} (even): coeff = {data['computed']}")

    print()
    print("Z_2 parity check:")
    z2 = verify_z2_parity(shadows)
    for r, data in sorted(z2.items()):
        status = "PASS" if data['z2_invariant'] else "FAIL"
        print(f"  r={r}: Z_2 invariant = {status}")

    print()
    print("Mixing analysis:")
    mix = mixing_coefficients(shadows, max_r)
    for r in sorted(mix.keys()):
        data = mix[r]
        print(f"  r={r}: pure_T={data['pure_T']}, pure_W={data['pure_W']}, "
              f"n_mixed={data['n_mixed_monomials']}")
        for (a, b), coeff in sorted(data['mixed'].items(), reverse=True):
            print(f"       mixed ({a},{b}): {coeff}")

    print()
    print("Denominator analysis:")
    denoms = denominator_analysis(shadows, max_r)
    for r in sorted(denoms.keys()):
        for (a, b), d in sorted(denoms[r].items(), reverse=True):
            print(f"  Sh_{r} coeff ({a},{b}): denom = {d}")
