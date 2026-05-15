"""Finite-window Coxeter-anomaly diagnostics for shadow obstruction data.

Tests two claims from raeeznotes95 against the established shadow obstruction tower:

CLAIM A (Coxeter anomaly): Shadow obstruction tower anomaly coefficients at arity n
carry a natural S_n sign-representation structure when lifted to multi-mode
variables m_1,...,m_n on the hyperplane sum(m_i) = 0. Specifically, the
sewing amplitude at arity n should be divisible by the Vandermonde
Delta_n = prod_{i<j}(m_i - m_j).

CLAIM B (Chevalley-shadow correlation): The Chevalley quotient geometry
Spec C[H_n]^{S_n} transitions from modular-curve type (n<=4) to cameral
type (n>=5), correlating with the G/L/C/M shadow depth classification.

METHOD: compare finite-window toy lifts against exact local invariants.  The
module records diagnostics only; it does not identify finite reflection-group
tests with full anomaly classes.

Ground truth:
  - virasoro_shadow_tower.py: Sh_r coefficients on primary line
  - chapters/examples/w_algebras_deep.tex: level-4 Lambda norm
  - chapters/examples/w_algebras.tex: Coxeter anomaly is the missing
    composite-operator quartic contact, not an S_n sign representation
"""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial

from sympy import (
    Matrix,
    Poly,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    fraction,
    simplify,
    symbols,
)

__test__ = False


# =========================================================================
# 1. S_n action utilities
# =========================================================================

def permutation_sign(perm: list) -> int:
    """Sign of a permutation given as a list."""
    n = len(perm)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        j = i
        cycle_len = 0
        while not visited[j]:
            visited[j] = True
            j = perm[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign *= -1
    return sign


def apply_permutation(f, modes, perm):
    """Apply permutation to mode variables in expression f."""
    n = len(modes)
    # Use dummy variables to avoid collision
    dummies = [Symbol(f'__perm_{i}__') for i in range(n)]
    result = f
    for i in range(n):
        result = result.subs(modes[i], dummies[i])
    for i in range(n):
        result = result.subs(dummies[i], modes[perm[i]])
    return expand(result)


def symmetrize(f, modes):
    """Project to trivial S_n representation."""
    n = len(modes)
    total = sum(apply_permutation(f, modes, list(p))
                for p in permutations(range(n)))
    return expand(total) / factorial(n)


def antisymmetrize(f, modes):
    """Project to sign S_n representation."""
    n = len(modes)
    total = sum(permutation_sign(list(p)) * apply_permutation(f, modes, list(p))
                for p in permutations(range(n)))
    return expand(total) / factorial(n)


def _swap_vars(f, a, b):
    """Swap variables a and b in expression f using a dummy."""
    d = Symbol('__swap__')
    return expand(f.subs(a, d).subs(b, a).subs(d, b))


def is_symmetric(f, modes) -> bool:
    """Check full S_n symmetry via adjacent transpositions."""
    for i in range(len(modes) - 1):
        swapped = _swap_vars(f, modes[i], modes[i + 1])
        if simplify(swapped - f) != 0:
            return False
    return True


def is_anti_invariant(f, modes) -> bool:
    """Check sign representation via adjacent transpositions."""
    for i in range(len(modes) - 1):
        swapped = _swap_vars(f, modes[i], modes[i + 1])
        if simplify(swapped + f) != 0:
            return False
    return True


def vandermonde(modes):
    """Delta_n = prod_{i<j}(m_i - m_j)."""
    n = len(modes)
    result = 1
    for i in range(n):
        for j in range(i + 1, n):
            result *= (modes[i] - modes[j])
    return expand(result)


def _mode_polynomial_numerator(f, modes):
    """Clear non-mode denominators and return the numerator in mode variables."""
    numerator, denominator = fraction(cancel(f))
    if Poly(denominator, *modes, domain='EX').total_degree() != 0:
        raise ValueError("mode-dependent denominator is not a polynomial diagnostic")
    return expand(numerator)


def polynomial_divides(f, divisor, modes) -> bool:
    """Return whether ``divisor`` divides ``f`` after clearing scalar denominators."""
    if simplify(divisor) == 0:
        raise ValueError("zero divisor")
    numerator = _mode_polynomial_numerator(f, modes)
    remainder = Poly(numerator, *modes, domain='EX').rem(
        Poly(divisor, *modes, domain='EX')
    )
    return simplify(remainder.as_expr()) == 0


def total_mode_degree(f, modes) -> int:
    """Total degree after clearing denominators independent of the mode variables."""
    numerator = _mode_polynomial_numerator(f, modes)
    return Poly(numerator, *modes, domain='EX').total_degree()


# =========================================================================
# 2. Multi-mode shadow amplitudes
# =========================================================================

def shadow_arity2(m1, m2, kappa):
    """Arity-2: kappa * m1 * m2 (symmetric bilinear)."""
    return kappa * m1 * m2


def shadow_arity3(m1, m2, m3, C_coeff=2):
    """Arity-3: C * m1 * m2 * m3 (symmetric trilinear).

    From Virasoro Sugawara cubic: C_Vir = 2.
    """
    return C_coeff * m1 * m2 * m3


def sewing_arity4_contact(m1, m2, m3, m4, C_coeff, P):
    """DEPRECATED: Raw sewing of two cubics (DEGREE 6, not the physical quartic).

    WARNING: This function computes C(m_a,m_b,k)*P*C(k,m_c,m_d) which gives
    a degree-6 polynomial in the mode variables. The physical quartic shadow
    Sh_4 has degree 4 and comes from the Lambda-exchange mechanism (quasi-primary
    intermediate states), NOT from direct sewing of cubics. See
    w3_multivariable_shadow.py for the correct computation.

    This function is retained only as an attack surface. It is not fully
    symmetric, is not anti-invariant, has zero sign projection, and is not
    Vandermonde-divisible. Hence it supports no sign-representation claim.

    Q(m1,m2,m3,m4) = sum over (2,2)-partitions of
        P * C(m_a, m_b, k) * C(k, m_c, m_d)
    where k = m_a + m_b (mode conservation at left vertex).

    C(a,b,c) = C_coeff * a * b * c (symmetric trilinear).
    """
    modes = [m1, m2, m3, m4]
    # All (2,2)-partitions of {0,1,2,3}
    partitions = [
        ((0, 1), (2, 3)),
        ((0, 2), (1, 3)),
        ((0, 3), (1, 2)),
    ]

    total = 0
    for (a, b), (c, d) in partitions:
        k = modes[a] + modes[b]  # internal mode
        left = C_coeff * modes[a] * modes[b] * k
        right = C_coeff * k * modes[c] * modes[d]
        total += P * left * right

    return expand(total)


def sewing_arity5(m1, m2, m3, m4, m5, C_coeff, Q_on_line, P):
    """Arity-5 amplitude from sewing cubic with quartic.

    o^(5) = {C, Q}_H where:
    - C is the arity-3 cubic (symmetric trilinear)
    - Q is the arity-4 quartic (symmetric quadrilinear on primary line)

    For multi-mode: we sew one leg from C with one leg from Q.
    This gives a (3+4-2)=5 mode amplitude.

    Actually on the 1d line: {Sh_3, Sh_4}_H has degree 3+4-2=5.
    In multi-mode: we choose 1 leg from the cubic and 1 from the quartic
    to contract with propagator P. The remaining 2+3=5 legs carry modes.
    """
    modes = [m1, m2, m3, m4, m5]
    total = 0

    # Choose which 2 of the 5 modes go to the cubic (other 3 to quartic)
    # But the cubic has 3 legs total: 2 external + 1 internal
    # And the quartic has 4 legs total: 3 external + 1 internal

    # All ways to partition {0,...,4} into (subset of 2 for cubic) and (subset of 3 for quartic)
    for cubic_pair in combinations(range(5), 2):
        quartic_triple = [i for i in range(5) if i not in cubic_pair]
        a, b = cubic_pair
        c, d, e = quartic_triple

        k = modes[a] + modes[b]  # internal mode from cubic side
        left = C_coeff * modes[a] * modes[b] * k
        # Quartic on primary line: Q_coeff * m_c * m_d * m_e * k
        # But multi-mode quartic from sewing is more complex.
        # On the PRIMARY LINE the quartic is Q_on_line * x^4 = symmetric.
        # In multi-mode: Q(m_c, m_d, m_e, k) = Q_on_line * m_c * m_d * m_e * k
        right = Q_on_line * modes[c] * modes[d] * modes[e] * k
        total += P * left * right

    return expand(total)


# =========================================================================
# 3. Core tests
# =========================================================================

def test_claim_A_arity2():
    """Test: is the arity-2 shadow symmetric or anti-invariant?"""
    m1, m2 = symbols('m1 m2')
    c = Symbol('c')
    sh2 = shadow_arity2(m1, m2, c / 2)
    return {
        'amplitude': sh2,
        'is_symmetric': is_symmetric(sh2, [m1, m2]),
        'is_anti_invariant': is_anti_invariant(sh2, [m1, m2]),
        'verdict': 'SYMMETRIC (trivial S_2 rep)',
    }


def test_claim_A_arity3():
    """Test: is the arity-3 shadow symmetric or anti-invariant?"""
    m1, m2, m3 = symbols('m1 m2 m3')
    sh3 = shadow_arity3(m1, m2, m3)
    return {
        'amplitude': sh3,
        'is_symmetric': is_symmetric(sh3, [m1, m2, m3]),
        'is_anti_invariant': is_anti_invariant(sh3, [m1, m2, m3]),
        'verdict': 'SYMMETRIC (trivial S_3 rep)',
    }


def test_claim_A_arity4():
    """Finite-window sign test for the raw degree-6 arity-4 toy lift.

    This is not the physical quartic shadow.  The physical Virasoro quartic
    comes from the weight-4 quasi-primary Lambda exchange and has degree 4.
    The raw lift is tested only to prevent a false sign/Vandermonde claim.
    """
    m1, m2, m3, m4 = symbols('m1 m2 m3 m4')
    c = Symbol('c')

    C_coeff = 2  # Virasoro cubic
    P = Rational(2) / c  # inverse Hessian

    amp = sewing_arity4_contact(m1, m2, m3, m4, C_coeff, P)
    modes = [m1, m2, m3, m4]
    delta = vandermonde(modes)

    sym = is_symmetric(amp, modes)
    anti = is_anti_invariant(amp, modes)

    sym_part = symmetrize(amp, modes)
    anti_part = antisymmetrize(amp, modes)
    anti_part_vanishes = simplify(anti_part) == 0

    return {
        'amplitude': amp,
        'amplitude_degree': total_mode_degree(amp, modes),
        'physical_quartic_degree': 4,
        'is_fully_symmetric': sym,
        'is_anti_invariant': anti,
        'symmetric_projection': sym_part,
        'antisymmetric_projection': anti_part,
        'anti_part_vanishes': anti_part_vanishes,
        'vandermonde_degree': total_mode_degree(delta, modes),
        'is_vandermonde_divisible': polynomial_divides(amp, delta, modes),
        'scope': 'raw_degree_6_toy_lift_not_physical_quartic',
        'full_anomaly_class_inferred': False,
        'verdict': (
            'NO SIGN COMPONENT -> Claim A unsupported at arity 4'
            if anti_part_vanishes else
            'SIGN COMPONENT PRESENT -> inspect before using'
        ),
    }


def test_claim_A_arity4_on_constraint():
    """Raw arity-4 lift on the hyperplane m1+m2+m3+m4 = 0."""
    m1, m2, m3 = symbols('m1 m2 m3')
    c = Symbol('c')
    m4 = -(m1 + m2 + m3)

    C_coeff = 2
    P = Rational(2) / c

    amp = sewing_arity4_contact(m1, m2, m3, m4, C_coeff, P)
    amp = expand(amp)

    # Evaluate on the primary line: m1=m2=m3=t, m4=-3t
    t = Symbol('t')
    amp_line = amp.subs([(m1, t), (m2, t), (m3, t)])
    amp_line = expand(amp_line)

    return {
        'constrained_amplitude': amp,
        'on_primary_line': amp_line,
        'constrained_degree': total_mode_degree(amp, [m1, m2, m3]),
        'line_degree': Poly(_mode_polynomial_numerator(amp_line, [t]), t).total_degree(),
        'physical_quartic_degree': 4,
        'matches_physical_quartic_degree': False,
        'scope': 'constraint_restriction_of_raw_degree_6_toy_lift',
        'full_anomaly_class_inferred': False,
    }


def test_claim_A_arity5():
    """Test S_5 structure of the arity-5 quintic amplitude."""
    m1, m2, m3, m4, m5 = symbols('m1 m2 m3 m4 m5')
    c = Symbol('c')

    C_coeff = 2
    Q_on_line = Rational(10) / (c * (5 * c + 22))
    P = Rational(2) / c

    amp = sewing_arity5(m1, m2, m3, m4, m5, C_coeff, Q_on_line, P)
    modes = [m1, m2, m3, m4, m5]
    delta = vandermonde(modes)

    sym = is_symmetric(amp, modes)
    anti_part = antisymmetrize(amp, modes)

    return {
        'amplitude': amp,
        'amplitude_degree': total_mode_degree(amp, modes) if amp != 0 else 0,
        'physical_quintic_degree': 5,
        'is_symmetric': sym,
        'antisymmetric_projection': anti_part,
        'anti_part_vanishes': simplify(anti_part) == 0,
        'vandermonde_degree': total_mode_degree(delta, modes),
        'is_vandermonde_divisible': polynomial_divides(amp, delta, modes),
        'scope': 'toy_degree_7_cubic_quartic_lift_not_full_arity5_construction',
        'full_anomaly_class_inferred': False,
        'verdict': (
            'SYMMETRIC finite-window toy -> no sign rep at arity 5'
            if sym else
            'NOT SYMMETRIC -> check representation decomposition'
        ),
    }


# =========================================================================
# 4. Claim B: Chevalley-shadow correlation
# =========================================================================

def chevalley_A2_discriminant_packet():
    """Exact A2 Chevalley discriminant on H_3 = {m1+m2+m3=0}.

    For roots m_i with sum zero, Delta_3^2 equals the cubic discriminant
    p2^3/2 - 3 p3^2, where p_j = sum_i m_i^j.  This is a finite
    reflection-group identity only; it is not a shadow anomaly theorem.
    """
    m1, m2, m3 = symbols('m1 m2 m3')
    constrained_m3 = -(m1 + m2)

    delta_sq = expand(vandermonde([m1, m2, m3])**2)
    delta_sq_H3 = expand(delta_sq.subs(m3, constrained_m3))
    p2 = expand(m1**2 + m2**2 + constrained_m3**2)
    p3 = expand(m1**3 + m2**3 + constrained_m3**3)
    rhs = expand(p2**3 / 2 - 3 * p3**2)

    return {
        'A2_vandermonde_squared_on_H3': factor(delta_sq_H3),
        'p2': p2,
        'p3': p3,
        'discriminant_in_power_sums': factor(rhs),
        'identity_holds': simplify(delta_sq_H3 - rhs) == 0,
        'scope': 'finite_A2_Chevalley_discriminant_only',
        'full_anomaly_class_inferred': False,
    }


def test_claim_B():
    """Finite type-A invariant-dimension diagnostic for Claim B.

    The raeeznotes95 claim: A_4 (n=5) marks the transition to cameral geometry.

    The supported content here is only dimensional:
    Shadow depth n means the n-point function terminates.
    A_{n-1} has rank n-1. The quotient P(2,...,n) has dimension n-1.
    The transition at A_4 is just: dimension >= 4 means not a surface.

    The NON-TAUTOLOGICAL question: WHY does the shadow obstruction tower terminate
    at specific arities for specific families? Answer: A-infinity formality
    (prop:shadow-formality-low-arity), not Chevalley geometry.
    """
    a2 = chevalley_A2_discriminant_packet()

    return {
        'A2_vandermonde_sq': a2['A2_vandermonde_squared_on_H3'],
        'A2_p2': a2['p2'],
        'A2_p3': a2['p3'],
        'A2_identity_holds': a2['identity_holds'],
        'chevalley_degrees_by_arity': {n: tuple(range(2, n + 1)) for n in range(2, 6)},
        'correlation_tautological': True,
        'genuine_content': 'A-infinity formality depth, not Chevalley geometry',
        'scope': 'finite_reflection_group_dimension_diagnostic_only',
        'full_anomaly_class_inferred': False,
    }


# =========================================================================
# 5. The GENUINE insight from raeeznotes95 (if any)
# =========================================================================

def virasoro_level4_finite_window_packet():
    """Exact Virasoro level-4 packet from the local Lambda computation.

    Local source: chapters/examples/w_algebras_deep.tex computes
    det G = c^2(5c+22)/2 and
    <Lambda|Lambda> = c(5c+22)/10.  The quartic shadow coefficient is
    S_4 = 10/[c(5c+22)], so S_4 * <Lambda|Lambda> = 1.
    """
    c = Symbol('c')
    gram = Matrix([
        [5 * c, 3 * c],
        [3 * c, Rational(1, 2) * c * (c + 8)],
    ])
    det_gram = factor(gram.det())
    lambda_norm = c * (5 * c + 22) / 10
    s4 = Rational(10) / (c * (5 * c + 22))
    s4_denominator = c * (5 * c + 22)
    shared_factor = 5 * c + 22

    return {
        'level4_gram': gram,
        'vacuum_level4_gram_det': det_gram,
        'lambda_norm': lambda_norm,
        'S4': s4,
        'S4_denominator': s4_denominator,
        'S4_times_lambda_norm': cancel(s4 * lambda_norm),
        'shared_factor': shared_factor,
        'shared_denominator': s4_denominator,
        'det_over_shared_factor': cancel(det_gram / shared_factor),
        'det_over_S4_denominator': cancel(det_gram / s4_denominator),
        'kac_shadow_connection_status': 'finite-window shared-factor check',
        'scope': 'Virasoro_rank_one_level4_Lambda_window',
        'full_anomaly_class_inferred': False,
    }


def identify_genuine_insight():
    """What raeeznotes95 gets right vs wrong.

    WRONG (Claim A): the tested finite-window shadow amplitudes live in
    the S_n sign representation.  They do not.  The rank-one Virasoro
    primary-line data are symmetric scalars; the raw arity-4 lift is not
    physical and has zero sign projection.

    WRONG (Claim B): The Chevalley-shadow correlation is structural.
    It is only a finite rank/dimension diagnostic here.

    PARTIALLY RIGHT: the Vandermonde appears as the Jacobian of the
    Chevalley quotient map H_n -> H_n/S_n.  This module verifies the
    finite A2 discriminant identity, not a sewing-amplitude theorem.

    GENUINE FINITE-WINDOW CONTENT: the Virasoro level-4 Gram determinant,
    the Lambda norm, and the quartic shadow denominator share the factor
    c(5c+22).  That is a Kac-shadow singularity check in one exact window,
    not a proof that finite reflection-group discriminants classify the full
    anomaly package.
    """
    level4 = virasoro_level4_finite_window_packet()
    a2 = chevalley_A2_discriminant_packet()

    return {
        'claim_A': 'REFUTED in tested windows: no sign-representation component',
        'claim_B': 'DIMENSIONAL finite-reflection diagnostic, not structural cause',
        'genuine_connection': (
            'Finite-window Kac-shadow singularity: det G_4 = c^2(5c+22)/2, '
            '<Lambda|Lambda> = c(5c+22)/10, and S4 = 10/[c(5c+22)]. '
            'This is the Lambda-exchange/BPZ singular-vector window, not '
            'Chevalley geometry.'
        ),
        'open_question': (
            'Whether higher Kac determinants factor through type-A '
            'Chevalley discriminants in natural spectral variables remains '
            'open in this module.'
        ),
        'kac_level4': level4['vacuum_level4_gram_det'],
        'Q_denominator': level4['S4_denominator'],
        'shared_factor': level4['shared_factor'],
        'shared_denominator': level4['shared_denominator'],
        'lambda_norm': level4['lambda_norm'],
        'S4_times_lambda_norm': level4['S4_times_lambda_norm'],
        'A2_discriminant_identity_holds': a2['identity_holds'],
        'kac_shadow_connection_status': level4['kac_shadow_connection_status'],
        'scope': 'finite_window_diagnostics_only',
        'full_anomaly_class_inferred': False,
    }


for _diagnostic in (
    test_claim_A_arity2,
    test_claim_A_arity3,
    test_claim_A_arity4,
    test_claim_A_arity4_on_constraint,
    test_claim_A_arity5,
    test_claim_B,
):
    _diagnostic.__test__ = False
del _diagnostic


if __name__ == '__main__':
    print("=" * 70)
    print("COXETER ANOMALY SPECIES: Testing raeeznotes95 claims")
    print("=" * 70)

    print("\n--- Claim A: S_n structure ---")
    r2 = test_claim_A_arity2()
    print(f"  Arity 2: {r2['verdict']}")

    r3 = test_claim_A_arity3()
    print(f"  Arity 3: {r3['verdict']}")

    r4 = test_claim_A_arity4()
    print(f"  Arity 4: {r4['verdict']}")
    print(f"    Amplitude: {r4['amplitude']}")
    print(f"    Anti-sym projection: {r4['antisymmetric_projection']}")
    print(f"    Anti-sym vanishes: {r4['anti_part_vanishes']}")

    print("\n--- Claim B: Chevalley-shadow ---")
    rB = test_claim_B()
    print(f"  Tautological: {rB['correlation_tautological']}")
    print(f"  Genuine content: {rB['genuine_content']}")

    print("\n--- Genuine insight ---")
    genuine = identify_genuine_insight()
    print(f"  Claim A: {genuine['claim_A']}")
    print(f"  Claim B: {genuine['claim_B']}")
    print(f"  Genuine: {genuine['genuine_connection']}")
    print(f"  Open: {genuine['open_question']}")
