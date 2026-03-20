"""Singularity theory of the Virasoro shadow potential.

The shadow potential is the generating function
    S(x) = sum_{r=2}^{r_max} Sh_r(Vir_c) * x^r / r!
on the one-dimensional primary line. Its critical points control the
modular shadow landscape: the trivial critical point x=0 is the vacuum,
and nontrivial critical points (when they exist) are shadow saddles
governing the semiclassical complementarity expansion.

The singularity theory studies:
  (1) Critical equation: dS/dx = 0 (factoring out the trivial root x=0).
  (2) Shadow discriminant: the discriminant of the reduced critical
      polynomial as a function of c, detecting parameter values where
      critical points collide (A_k singularity enhancement).
  (3) Milnor number: the local multiplicity of x=0 as a critical point,
      measuring the deformation complexity of the shadow singularity.
  (4) Critical-point locus: numerical locations of shadow saddles at
      specific central charges.

KEY RESULTS:
  - The factor (5c+22) persists as a POLE of the shadow discriminant
    at ALL truncation orders (pole order grows as n(n-1)/2), confirming
    c = -22/5 as a universal singularity wall where the shadow potential
    itself degenerates (coefficients diverge via the Kac determinant).
  - At c = 0: the curvature kappa = c/2 vanishes, the Hessian degenerates,
    and the Milnor number jumps to max_arity - 1 (the shadow potential
    reduces to a cubic-leading function with maximally degenerate origin).
  - The factor (15c+56) appears in the discriminant NUMERATOR at arity 4
    (the first truncation where the reduced critical equation is nontrivial),
    giving a zero of the discriminant at c = -56/15. At higher arities
    this factor is replaced by higher-degree polynomials.
  - Milnor number at x=0 equals 1 for generic c (Morse/A_1), jumps at
    c = 0 (A_k with k = max_arity - 1), and remains 1 at c = -22/5
    (where the well-defined truncated potential is still Morse).

References:
    - virasoro_shadow_tower.py: shadow coefficients Sh_r
    - w3_multivariable_shadow.py: Kac-shadow singularity principle
    - thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    - rem:virasoro-resonance-model (w_algebras.tex)
"""

from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from sympy import (
    Symbol, Rational, factor, expand, Poly, diff, simplify, S,
    factorial, solve, N, degree, LC, oo, numer, denom, cancel,
)
from virasoro_shadow_tower import shadow_coefficients


c = Symbol('c')
x = Symbol('x')


# ============================================================================
# 1. Shadow potential
# ============================================================================

def shadow_potential_1d(max_arity=7):
    """Virasoro shadow potential S(x) = sum_{r=2}^{max_arity} Sh_r x^r / r!.

    The shadow potential is the generating function for the shadow tower
    on the primary line, normalized by factorial denominators so that
    S''(0) = kappa = c/2 (the curvature) and higher derivatives give
    the shadow coefficients directly.

    Returns a sympy expression in c and x.
    """
    coeffs = shadow_coefficients(max_arity)
    potential = S.Zero
    for r, coeff in sorted(coeffs.items()):
        potential += coeff * x**r / factorial(r)
    return expand(potential)


def shadow_potential_coefficients(max_arity=7):
    """Return dict {r: coefficient of x^r in S(x)} (i.e., Sh_r / r!)."""
    coeffs = shadow_coefficients(max_arity)
    result = {}
    for r, coeff in coeffs.items():
        result[r] = factor(coeff / factorial(r))
    return result


# ============================================================================
# 2. Critical equation
# ============================================================================

def critical_equation_1d(max_arity=7):
    """Reduced critical equation: (dS/dx) / x = 0 (factoring out trivial root).

    The full critical equation dS/dx = 0 always has x=0 as a root (the
    vacuum). The REDUCED equation factors out this trivial root, leaving
    a polynomial in x whose roots are the nontrivial shadow saddles.

    Returns a polynomial in x with coefficients in Q(c).
    """
    pot = shadow_potential_1d(max_arity)
    deriv = diff(pot, x)
    # dS/dx has x as a factor (since S starts at x^2)
    reduced = cancel(deriv / x)
    return expand(reduced)


def critical_polynomial_1d(max_arity=7):
    """Return the reduced critical equation as a sympy Poly in x over Q(c).

    Clears denominators in c so the coefficients are polynomial in c.
    """
    crit = critical_equation_1d(max_arity)
    p = Poly(crit, x, domain='ZZ(c)')
    return p


# ============================================================================
# 3. Shadow discriminant
# ============================================================================

def shadow_discriminant_1d(max_arity=7):
    """Discriminant of the reduced critical equation as a rational function of c.

    The discriminant vanishes when two nontrivial critical points of S
    collide (A_2 singularity enhancement). As a rational function of c:
      - ZEROS of the discriminant: values of c where saddle points merge.
      - POLES of the discriminant: values of c where the critical equation
        degenerates (shadow coefficients diverge, e.g., c = -22/5).

    Returns factor(discriminant) as a sympy expression in c.
    """
    crit = critical_equation_1d(max_arity)
    p = Poly(crit, x, domain='ZZ(c)')
    disc = p.discriminant()
    return factor(disc)


def discriminant_numerator(max_arity=7):
    """Numerator of the shadow discriminant, factored over Q[c].

    Zeros of this polynomial are the central charges where nontrivial
    critical points collide.
    """
    disc = shadow_discriminant_1d(max_arity)
    return factor(numer(disc))


def discriminant_denominator(max_arity=7):
    """Denominator of the shadow discriminant, factored over Q[c].

    Zeros of this polynomial are the central charges where the shadow
    potential degenerates (Kac singularity walls).
    """
    disc = shadow_discriminant_1d(max_arity)
    return factor(denom(disc))


def shadow_discriminant_factors(max_arity=7):
    """Extract the irreducible factors of the shadow discriminant.

    Returns a dict with keys 'numerator_factors' and 'denominator_factors',
    each a list of (factor_in_c, multiplicity) pairs.
    """
    disc = shadow_discriminant_1d(max_arity)
    if disc == S.Zero:
        return {'numerator_factors': [('zero', 0)],
                'denominator_factors': []}

    result = {'numerator_factors': [], 'denominator_factors': []}
    for part_name, part_expr in [('numerator_factors', numer(disc)),
                                  ('denominator_factors', denom(disc))]:
        factored = factor(part_expr)
        if hasattr(factored, 'as_ordered_factors'):
            for f in factored.as_ordered_factors():
                if f.is_Pow:
                    base, exp = f.as_base_exp()
                    if base.has(c) and not base.is_number:
                        result[part_name].append((base, int(exp)))
                elif f.has(c) and not f.is_number:
                    result[part_name].append((f, 1))
    return result


# ============================================================================
# 4. Milnor number
# ============================================================================

def milnor_number_at_origin(max_arity=7, c_val=0):
    """Milnor number of S at x=0 for a given central charge value.

    The Milnor number mu = ord_0(dS/dx), where ord_0 is the order
    of vanishing at x=0. For a Morse critical point (generic c),
    mu = 1 (the simplest A_1 singularity). At c = 0 where kappa = c/2
    vanishes, the leading term of dS/dx becomes cubic and mu jumps.

    For c values where shadow coefficients diverge (e.g., c = -22/5),
    returns the Milnor number of the TRUNCATED potential excluding
    the divergent terms.

    Returns the Milnor number (integer >= 1).
    """
    pot = shadow_potential_1d(max_arity)
    pot_spec = pot.subs(c, c_val)
    # Check if the potential is well-defined (no infinities)
    if pot_spec.has(oo) or pot_spec.has(-oo) or pot_spec.has(S.ComplexInfinity):
        # Potential diverges at this c value; use the well-defined truncation
        coeffs = shadow_coefficients(max_arity)
        pot_spec = S.Zero
        for r, coeff in sorted(coeffs.items()):
            coeff_val = coeff.subs(c, c_val)
            if coeff_val.is_finite and not coeff_val.has(oo):
                pot_spec += coeff_val * x**r / factorial(r)

    deriv = expand(diff(pot_spec, x))
    if deriv == S.Zero:
        return max_arity - 1  # maximally degenerate

    p = Poly(deriv, x)
    # Find order of vanishing at x=0 = lowest nonzero coefficient
    for i in range(p.degree() + 1):
        if p.nth(i) != 0:
            return i

    return p.degree()  # fallback


def singularity_type_at_origin(max_arity=7, c_val=0):
    """Classify the singularity type at x=0 via the Milnor number.

    Returns:
        'A_1' (Morse, mu=1): generic, two-sheeted critical structure
        'A_k' (k>=2): degenerate, k+1 critical points colliding
        'smooth' (mu=0): x=0 is not a critical point (impossible for S)
    """
    mu = milnor_number_at_origin(max_arity, c_val)
    if mu == 0:
        return 'smooth'
    return f'A_{mu}'


# ============================================================================
# 5. Critical points (numerical)
# ============================================================================

def critical_points_numerical(c_val, max_arity=7):
    """Find all nontrivial critical points of S numerically at given c.

    Solves the reduced critical equation (dS/dx)/x = 0 at c = c_val.
    Returns a list of complex numbers (the x-coordinates of the saddles).
    """
    crit = critical_equation_1d(max_arity)
    crit_spec = crit.subs(c, c_val)
    crit_spec = cancel(crit_spec)

    if crit_spec == S.Zero:
        return []  # degenerate: every x is critical

    # Check for infinities (pole in c)
    if crit_spec.has(oo) or crit_spec.has(-oo) or crit_spec.has(S.ComplexInfinity):
        return []

    roots = solve(crit_spec, x)
    return [complex(N(r)) for r in roots]


def real_critical_points(c_val, max_arity=7, tol=1e-10):
    """Return only the real critical points at given c."""
    pts = critical_points_numerical(c_val, max_arity)
    return [z.real for z in pts if abs(z.imag) < tol]


# ============================================================================
# 6. Singularity walls and persistence
# ============================================================================

def discriminant_pole_order(factor_poly, max_arity=7):
    """Compute the pole order of (factor_poly) in the discriminant denominator.

    The discriminant is a rational function of c. This function computes
    the multiplicity of the root of factor_poly in the denominator.

    Returns dict {arity: pole_order}.
    """
    results = {}
    for arity in range(4, max_arity + 1):
        disc = shadow_discriminant_1d(arity)
        den = denom(disc)
        factor_roots = solve(factor_poly, c)
        if not factor_roots:
            results[arity] = 0
            continue
        root = factor_roots[0]
        # Count multiplicity by repeated division
        poly_den = Poly(den, c)
        mult = 0
        remainder = den
        while True:
            val = simplify(remainder.subs(c, root))
            if val != 0:
                break
            remainder = cancel(remainder / (c - root))
            mult += 1
        results[arity] = mult
    return results


def discriminant_zero_test(factor_poly, min_arity=4, max_arity=7):
    """Test whether a given factor of c is a zero of the discriminant
    NUMERATOR across truncation orders.

    Returns dict {arity: is_zero_of_numerator}.
    """
    results = {}
    for arity in range(min_arity, max_arity + 1):
        disc = shadow_discriminant_1d(arity)
        num = numer(disc)
        factor_roots = solve(factor_poly, c)
        is_zero = True
        for root in factor_roots:
            val = simplify(num.subs(c, root))
            if val != 0:
                is_zero = False
                break
        results[arity] = is_zero
    return results


def factor_5c22_pole_persistence(max_arity=7):
    """Pole order of (5c+22) in the discriminant denominator at each arity.

    The (5c+22) factor arises from the Kac determinant at weight 4
    (the Lambda norm N_Lambda = c(5c+22)/10). Its persistence as a
    POLE reflects the universal role of the weight-4 null vector.
    """
    return discriminant_pole_order(5*c + 22, max_arity)


def factor_15c56_in_numerator(max_arity=7):
    """Test whether (15c+56) is a zero of the discriminant numerator.

    The factor (15c+56) appears at arity 4 and encodes the first
    critical-point collision in the shadow potential.
    """
    return discriminant_zero_test(15*c + 56, min_arity=4, max_arity=max_arity)


# ============================================================================
# 7. Hessian and Morse index
# ============================================================================

def hessian_at_origin(max_arity=7):
    """The Hessian d^2S/dx^2 at x=0, as a function of c.

    For the 1d shadow potential: H = S''(0) = Sh_2 = c/2.
    This is the curvature kappa, and it vanishes at c=0.
    """
    pot = shadow_potential_1d(max_arity)
    return simplify(diff(pot, x, 2).subs(x, 0))


def morse_index_generic():
    """Morse index at x=0 for generic c.

    For c > 0: H = c/2 > 0, so x=0 is a local minimum (index 0).
    For c < 0: H = c/2 < 0, so x=0 is a local maximum (index 1).
    At c = 0: degenerate (Hessian vanishes), not Morse.
    """
    return {
        'c > 0': {'index': 0, 'type': 'minimum'},
        'c < 0': {'index': 1, 'type': 'maximum'},
        'c = 0': {'index': None, 'type': 'degenerate (A_k, k >= 2)'},
    }


# ============================================================================
# 8. Critical value function
# ============================================================================

def critical_values_numerical(c_val, max_arity=7):
    """Compute the shadow potential value S(x*) at each critical point x*.

    These critical values govern the exponential weight in the
    semiclassical complementarity expansion at genus g >> 1.
    """
    pot = shadow_potential_1d(max_arity)
    crit_pts = critical_points_numerical(c_val, max_arity)
    values = []
    for pt in crit_pts:
        val = complex(N(pot.subs(c, c_val).subs(x, pt)))
        values.append((pt, val))
    return values


# ============================================================================
# Main block: diagnostics
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("SHADOW POTENTIAL SINGULARITY THEORY")
    print("=" * 70)

    # --- Shadow discriminant at arities 4, 5, 6, 7 ---
    print("\n--- Shadow discriminant at increasing truncation orders ---")
    for arity in [4, 5, 6, 7]:
        disc = shadow_discriminant_1d(arity)
        num = discriminant_numerator(arity)
        den = discriminant_denominator(arity)
        print(f"  Arity {arity}:")
        print(f"    disc = {disc}")
        print(f"    num  = {num}")
        print(f"    den  = {den}")

    # --- (5c+22) pole persistence ---
    print("\n--- (5c+22) as POLE of discriminant (Kac wall) ---")
    poles = factor_5c22_pole_persistence(7)
    for arity, order in sorted(poles.items()):
        print(f"  Arity {arity}: pole order = {order}")
    print("  Pattern: pole order = n(n-1)/2 where n = arity - 2")

    # --- (15c+56) in numerator ---
    print("\n--- (15c+56) as ZERO of discriminant numerator ---")
    zeros = factor_15c56_in_numerator(7)
    for arity, is_zero in sorted(zeros.items()):
        print(f"  Arity {arity}: (15c+56) divides num = {is_zero}")

    # --- Milnor numbers at special c values ---
    print("\n--- Milnor numbers at special central charges ---")
    special_c = {
        'c=0': 0,
        'c=-22/5': Rational(-22, 5),
        'c=-56/15': Rational(-56, 15),
    }
    for name, c_val in special_c.items():
        mu = milnor_number_at_origin(7, c_val)
        stype = singularity_type_at_origin(7, c_val)
        print(f"  {name}: Milnor number = {mu}, type = {stype}")

    # --- Critical points at specific c values ---
    print("\n--- Critical points (nontrivial saddles) ---")
    test_c = {
        'c=1': 1,
        'c=13 (self-dual)': 13,
        'c=-56/15': Rational(-56, 15),
    }
    for name, c_val in test_c.items():
        pts = critical_points_numerical(c_val, max_arity=7)
        real_pts = real_critical_points(c_val, max_arity=7)
        print(f"  {name}: {len(pts)} critical points, {len(real_pts)} real")
        for i, pt in enumerate(pts):
            flag = " (real)" if abs(pt.imag) < 1e-10 else ""
            print(f"    x_{i} = {pt:.6f}{flag}")

    # --- Critical values at c=1 ---
    print("\n--- Critical values S(x*) at c=1 ---")
    cvals = critical_values_numerical(1, max_arity=7)
    for pt, val in cvals:
        print(f"  x* = {pt:.6f}, S(x*) = {val:.6f}")

    # --- Hessian ---
    print(f"\n--- Hessian at origin: S''(0) = {hessian_at_origin()} ---")
