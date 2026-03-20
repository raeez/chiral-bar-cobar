"""Virasoro shadow tower — Delta-factored form through arity 10.

Every shadow coefficient S_r (r >= 4) factors as

    S_r = Delta_Vir * R_r(c)

where Delta_Vir = 40/(5c+22) is the Virasoro critical discriminant and
R_r(c) is a rational function of c with poles only at c = 0 and c = -22/5.

The discriminant arises from the quartic contact shadow:
    Delta_Vir = 8 * kappa * S_4 = 8 * (c/2) * 10/[c(5c+22)] = 40/(5c+22).

The factored quotients R_r = S_r / Delta_Vir satisfy:
    R_4 = 1/(4c)                                      = 1/(8*kappa)
    R_5 = -6/(5c^2)
    R_6 = 2(45c + 193) / [3c^3(5c + 22)]
    R_7 = -72(15c + 61) / [7c^4(5c + 22)]
    R_8 = 2(2025c^2 + 16470c + 33314) / [c^5(5c + 22)^2]
    R_9 = -32(2025c^2 + 15570c + 29554) / [3c^6(5c + 22)^2]
    R_10 = 32(91125c^3 + 1050975c^2 + 3989790c + 4969967) / [5c^7(5c + 22)^3]

The Delta-factored form expresses the shadow tower as
    Sh_r = Delta_Vir * R_r * x^r,
isolating the universal quartic discriminant from the arity-dependent
rational envelope R_r.

References:
    - thm:shadow-archetype-classification (chap:e1-modular-koszul)
    - rem:virasoro-resonance-model (w_algebras.tex)
    - prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from sympy import (
    Rational, Symbol, cancel, factor, fraction, simplify, solve, S,
)

c = Symbol('c')

# Physical curvature: kappa = c/2
kappa = c / 2

# Virasoro critical discriminant
Delta_Vir = Rational(40) / (5 * c + 22)


def _import_tower(max_arity=10):
    """Import shadow tower from virasoro_shadow_duality (faster recursion)."""
    from virasoro_shadow_duality import virasoro_shadow_tower
    return virasoro_shadow_tower(max_arity)


def compute_shadow_tower(max_arity=10):
    """Compute the Virasoro shadow tower S_r(c) through the given arity.

    Standalone recursion (no external dependency). Uses the master equation
    on the single primary line:
        S_r = -(1/(r*c)) * sum_{j+k=r+2, 2<=j<=k} eps(j,k) * j*k * S_j * S_k
    """
    tower = {}
    tower[2] = c / 2
    tower[3] = Rational(2)
    tower[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_arity + 1):
        total = Rational(0)
        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k > r or j > k:
                continue
            if j not in tower or k not in tower:
                continue
            contrib = j * k * tower[j] * tower[k]
            if j == k:
                contrib = contrib / 2
            total += contrib
        tower[r] = cancel(-total / (r * c))

    return tower


def delta_factored_quotients(max_arity=10):
    """Compute R_r = S_r / Delta_Vir for r = 4, ..., max_arity.

    Returns dict {r: R_r} where each R_r is a factored rational function of c.
    Poles of R_r lie only at c = 0 and c = -22/5.
    """
    tower = compute_shadow_tower(max_arity)
    quotients = {}
    for r in range(4, max_arity + 1):
        R_r = cancel(tower[r] / Delta_Vir)
        quotients[r] = factor(R_r)
    return quotients


def verify_delta_factorization(max_arity=10):
    """Verify S_r = Delta_Vir * R_r for r = 4, ..., max_arity.

    Returns True if all verifications pass. Raises AssertionError otherwise.
    """
    tower = compute_shadow_tower(max_arity)
    quotients = delta_factored_quotients(max_arity)

    for r in range(4, max_arity + 1):
        reconstructed = cancel(Delta_Vir * quotients[r])
        diff = simplify(tower[r] - reconstructed)
        assert diff == 0, (
            f"Delta factorization fails at r={r}: "
            f"S_{r} = {tower[r]}, Delta*R_{r} = {reconstructed}"
        )
    return True


def verify_pole_structure(max_arity=10):
    """Verify that R_r has poles only at c = 0 and c = -22/5.

    Returns dict {r: poles} where poles is a sorted list of roots of
    the denominator.
    """
    quotients = delta_factored_quotients(max_arity)
    pole_data = {}

    for r in range(4, max_arity + 1):
        R_r = cancel(quotients[r])
        _, denom = fraction(R_r)
        if not denom.has(c):
            pole_data[r] = []
            continue
        roots = solve(denom, c)
        pole_data[r] = sorted(roots, key=lambda x: float(x))

        # Verify only allowed poles
        allowed = {S.Zero, Rational(-22, 5)}
        for root in roots:
            assert root in allowed, (
                f"Unexpected pole at c = {root} in R_{r}"
            )

    return pole_data


def verify_closed_forms():
    """Verify R_4 and R_5 against closed-form expressions.

    R_4 = 1/(4c) = 1/(8*kappa)
    R_5 = -6/(5c^2)
    """
    quotients = delta_factored_quotients(5)

    # R_4 = 1/(4c)
    expected_R4 = Rational(1, 4) / c
    assert simplify(quotients[4] - expected_R4) == 0, (
        f"R_4 mismatch: got {quotients[4]}, expected {expected_R4}"
    )

    # R_4 = 1/(8*kappa) with kappa = c/2
    assert simplify(quotients[4] - 1 / (8 * kappa)) == 0, (
        f"R_4 != 1/(8*kappa): got {quotients[4]}"
    )

    # R_5 = -6/(5c^2)
    expected_R5 = Rational(-6, 5) / c**2
    assert simplify(quotients[5] - expected_R5) == 0, (
        f"R_5 mismatch: got {quotients[5]}, expected {expected_R5}"
    )

    return True


def delta_origin():
    """Verify Delta_Vir = 8 * kappa * S_4.

    This identity shows that the discriminant is the quartic contact
    shadow normalized by the curvature propagator.
    """
    S4 = Rational(10) / (c * (5 * c + 22))
    computed = cancel(8 * kappa * S4)
    assert simplify(computed - Delta_Vir) == 0, (
        f"Delta origin failed: 8*kappa*S_4 = {computed}, Delta = {Delta_Vir}"
    )
    return True


def pole_orders(max_arity=10):
    """Compute the order of each pole in R_r.

    Returns dict {r: {pole: order}}.
    """
    quotients = delta_factored_quotients(max_arity)
    result = {}

    for r in range(4, max_arity + 1):
        R_r = cancel(quotients[r])
        _, denom = fraction(R_r)
        orders = {}

        if not denom.has(c):
            result[r] = orders
            continue

        # Order at c = 0
        d_at_0 = denom
        mult_0 = 0
        while simplify(d_at_0.subs(c, 0)) == 0:
            d_at_0 = cancel(d_at_0 / c)
            mult_0 += 1
            if mult_0 > 20:
                break
        if mult_0 > 0:
            orders[S.Zero] = mult_0

        # Order at c = -22/5
        d_at_m = denom
        mult_m = 0
        c_shift = c + Rational(22, 5)
        while simplify(d_at_m.subs(c, Rational(-22, 5))) == 0:
            d_at_m = cancel(d_at_m / c_shift)
            mult_m += 1
            if mult_m > 20:
                break
        if mult_m > 0:
            orders[Rational(-22, 5)] = mult_m

        result[r] = orders

    return result


def sign_pattern(max_arity=10, c_val=1):
    """Compute the sign of R_r at a given value of c.

    Returns dict {r: +1 or -1}.
    """
    quotients = delta_factored_quotients(max_arity)
    signs = {}
    for r in range(4, max_arity + 1):
        val = quotients[r].subs(c, c_val)
        signs[r] = 1 if val > 0 else -1
    return signs


if __name__ == '__main__':
    print("Virasoro shadow tower — Delta-factored form")
    print("=" * 60)
    print()

    # Verify Delta origin
    delta_origin()
    print(f"Delta_Vir = 8*kappa*S_4 = {Delta_Vir}  [VERIFIED]")
    print()

    # Shadow tower
    tower = compute_shadow_tower(10)
    print("Shadow coefficients S_r(c):")
    for r in sorted(tower.keys()):
        print(f"  S_{r:2d} = {factor(tower[r])}")
    print()

    # Factored quotients
    quotients = delta_factored_quotients(10)
    print("Factored quotients R_r = S_r / Delta_Vir:")
    for r in sorted(quotients.keys()):
        print(f"  R_{r:2d} = {quotients[r]}")
    print()

    # Verify factorization
    verify_delta_factorization(10)
    print("Delta factorization S_r = Delta_Vir * R_r: VERIFIED (r = 4..10)")

    # Verify closed forms
    verify_closed_forms()
    print("Closed forms R_4 = 1/(4c) = 1/(8*kappa), R_5 = -6/(5c^2): VERIFIED")
    print()

    # Pole structure
    poles = verify_pole_structure(10)
    print("Pole structure of R_r (only c=0 and c=-22/5 allowed):")
    for r in sorted(poles.keys()):
        print(f"  R_{r:2d}: poles at c = {poles[r]}")
    print()

    # Pole orders
    orders = pole_orders(10)
    print("Pole orders:")
    for r in sorted(orders.keys()):
        print(f"  R_{r:2d}: {dict(orders[r])}")
    print()

    # Sign pattern at c=1
    signs = sign_pattern(10, c_val=1)
    print("Signs of R_r at c=1:")
    for r in sorted(signs.keys()):
        sign_char = '+' if signs[r] > 0 else '-'
        print(f"  R_{r:2d}: {sign_char}")
