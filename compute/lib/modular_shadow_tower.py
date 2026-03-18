"""
Modular shadow tower: higher-arity propagation and genus loop operator.

Implements the all-arity master equation, quintic obstruction, genus loop
operator Lambda_P, and the genus-1 Hessian correction for model families.

Ground truth:
  - nonlinear_modular_shadows.tex, Theorems thm:nms-all-arity-master-equation,
    thm:nms-virasoro-quintic-forced, thm:nms-finite-termination,
    thm:nms-nonseparating-clutching-law, thm:nms-genus-loop-model-families
  - virasoro_quartic_contact.py (Q^contact_Vir = 10/[c(5c+22)])

The key new results:
  1. All-arity master equation: nabla_H(Sh_r) + o^(r) = 0
  2. Quintic obstruction: o^(5) = {C, Q}_H
  3. Genus loop operator: Lambda_P(alpha) contracts two legs with propagator
  4. Genus-1 Hessian correction: delta H^(1) = Lambda_P(Q^(0))
  5. Virasoro loop ratio: rho^(1) = 240/[c^3(5c+22)]
"""

from sympy import (
    Symbol, Rational, simplify, factor, expand,
    binomial, oo, limit, sqrt, symbols
)


c = Symbol('c')


# =============================================================================
# Shadow tower data for model families
# =============================================================================

def virasoro_hessian():
    """H_Vir = (c/2) x^2 on the primary line."""
    return c / 2


def virasoro_cubic():
    """C_Vir = 2 x^3 (gravitational cubic, from T_(1)T = 2T)."""
    return Rational(2)


def virasoro_quartic_contact():
    """Q^contact_Vir = 10/[c(5c+22)] (extracted in MC4)."""
    return Rational(10) / (c * (5 * c + 22))


def virasoro_propagator():
    """P_Vir = H^{-1} = 2/c on the one-generator primary line."""
    return Rational(2) / c


# =============================================================================
# Genus loop operator
# =============================================================================

def genus_loop_1d(alpha_coeff, rank, propagator):
    """
    Genus loop operator Lambda_P on a one-dimensional symmetric space.

    For a rank-r symmetric tensor alpha = alpha_coeff * x^r on a 1d space,
    Lambda_P(alpha) = C(r,2) * P * alpha_coeff * x^{r-2},
    where C(r,2) = r*(r-1)/2 counts the ways to choose 2 of r symmetric legs
    to contract with the propagator P.

    Returns the coefficient of x^{r-2}.
    """
    return binomial(rank, 2) * propagator * alpha_coeff


def genus_loop_cubic_virasoro():
    """
    Lambda_P(C_Vir) on the one-generator primary line.

    C_Vir = 2 x^3, P = 2/c.
    Lambda_P(2 x^3) = C(3,2) * (2/c) * 2 * x = 3 * (2/c) * 2 * x = 12/c * x.

    Returns the coefficient of x.
    """
    C_coeff = virasoro_cubic()
    P = virasoro_propagator()
    return genus_loop_1d(C_coeff, 3, P)


def genus_loop_quartic_virasoro():
    """
    Lambda_P(Q^contact_Vir) = delta H^(1)_Vir on the primary line.

    Q = Q_0 x^4 with Q_0 = 10/[c(5c+22)], P = 2/c.
    Lambda_P(Q_0 x^4) = C(4,2) * (2/c) * Q_0 * x^2
                       = 6 * (2/c) * 10/[c(5c+22)] * x^2
                       = 120/[c^2(5c+22)] * x^2.

    Returns the coefficient of x^2 (the genus-1 Hessian correction coefficient).
    """
    Q_coeff = virasoro_quartic_contact()
    P = virasoro_propagator()
    return genus_loop_1d(Q_coeff, 4, P)


def virasoro_genus1_hessian_correction():
    """
    The genus-1 Hessian correction delta H^(1)_Vir = 120/[c^2(5c+22)].

    This is the coefficient of x^2 in Lambda_P(Q^contact x^4).
    """
    return genus_loop_quartic_virasoro()


def virasoro_loop_ratio():
    """
    The genus-1 loop ratio rho^(1) = delta H^(1) / H^(0).

    rho^(1) = [120/(c^2(5c+22))] / [c/2] = 240/[c^3(5c+22)].

    Wait -- let me recompute. H = (c/2) x^2, so H_coeff = c/2.
    delta H = [120/(c^2(5c+22))] x^2, so delta_H_coeff = 120/(c^2(5c+22)).
    rho = delta_H_coeff / H_coeff = 120/(c^2(5c+22)) / (c/2) = 240/(c^3(5c+22)).
    """
    dH = virasoro_genus1_hessian_correction()
    H = virasoro_hessian()
    return simplify(dH / H)


# =============================================================================
# Quintic obstruction
# =============================================================================

def sewing_product_1d(alpha_coeff, alpha_rank, beta_coeff, beta_rank, propagator):
    """
    Single-edge sewing product {alpha, beta}_H on a 1d symmetric space.

    alpha = alpha_coeff * x^p, beta = beta_coeff * x^q.
    {alpha, beta}_H = (combinatorial factor) * P * alpha_coeff * beta_coeff * x^{p+q-2}.

    On a 1d space, the sewing contracts one leg from each tensor with P.
    The number of ways to choose 1 leg from alpha (p choices) times
    1 leg from beta (q choices) gives p*q. But by symmetry of the
    resulting tensor, the effective combinatorial factor for the
    symmetrized product is p * q.

    Returns the coefficient of x^{p+q-2}.
    """
    return alpha_rank * beta_rank * propagator * alpha_coeff * beta_coeff


def quintic_obstruction_virasoro():
    """
    o^(5)_Vir = {C_Vir, Q^contact_Vir}_H.

    C = 2 x^3 (rank 3), Q = Q_0 x^4 (rank 4), P = 2/c.
    {C, Q} = 3 * 4 * (2/c) * 2 * Q_0 * x^5
           = 24 * (2/c) * 10/[c(5c+22)] * x^5
           = 480/[c^2(5c+22)] * x^5.

    Returns the coefficient of x^5.
    """
    C_coeff = virasoro_cubic()
    Q_coeff = virasoro_quartic_contact()
    P = virasoro_propagator()
    return sewing_product_1d(C_coeff, 3, Q_coeff, 4, P)


def quintic_obstruction_heisenberg():
    """o^(5)_H = 0 (both C and Q vanish)."""
    return Rational(0)


def quintic_obstruction_affine():
    """o^(5)_aff = 0 (Q_aff = 0 in minimal gauge)."""
    return Rational(0)


def quintic_obstruction_betagamma():
    """o^(5)_bg = 0 (C_bg = 0 on weight/contact slice)."""
    return Rational(0)


# =============================================================================
# Finite termination analysis
# =============================================================================

def shadow_termination_arity():
    """
    Returns the termination arity for each model family.

    Heisenberg: terminates at arity 2 (Gaussian, Sh_r = 0 for r >= 3)
    Affine sl2: terminates at arity 3 (Lie/tree, Sh_r = 0 for r >= 4)
    Beta-gamma: terminates at arity 4 (contact, on weight line)
    Virasoro: INFINITE (quintic forced, then induction)

    Returns dict mapping family name to termination arity (None = infinite).
    """
    return {
        'heisenberg': 2,
        'affine_sl2': 3,
        'betagamma': 4,
        'virasoro': None,  # infinite tower
    }


# =============================================================================
# Genus loop for general W_N
# =============================================================================

def w3_genus1_hessian_correction():
    """
    For W_3 with generators T (weight 2) and W (weight 3):
    H = (c/2) t^2 + (c/3) w^2 (diagonal Hessian).
    Propagator: P_t = 2/c, P_w = 3/c (diagonal).

    The quartic contact sector has contributions from the weight-4
    channel (Lambda) and weight-6 channel. The genus-1 correction
    involves tracing Q over two legs with the propagator.

    Returns the (t^2, w^2) coefficients of the correction (symbolic).
    """
    # Weight-4 contact: Q^{(4)} proportional to 16/(22+5c)
    # On the t-line: Lambda_P(Q^{(4)} t^4) uses P_t = 2/c
    Q4_coeff = Rational(16) / (22 + 5*c)
    P_t = Rational(2) / c
    dH_tt = binomial(4, 2) * P_t * Q4_coeff

    return {
        'delta_H_tt': simplify(dH_tt),
        'delta_H_ww': Symbol('delta_H_ww_W3'),  # requires full W3 OPE data
    }


# =============================================================================
# Verification and display
# =============================================================================

def verify_all():
    """Run all symbolic verifications."""
    print("=" * 70)
    print("MODULAR SHADOW TOWER: Higher-arity propagation & genus loop")
    print("=" * 70)

    # Quintic obstruction
    print("\n--- Quintic obstruction o^(5) ---")
    o5_vir = quintic_obstruction_virasoro()
    print(f"  Virasoro:    o^(5) = {factor(o5_vir)} * x^5")
    print(f"  Heisenberg:  o^(5) = {quintic_obstruction_heisenberg()}")
    print(f"  Affine sl2:  o^(5) = {quintic_obstruction_affine()}")
    print(f"  Beta-gamma:  o^(5) = {quintic_obstruction_betagamma()}")

    # Genus loop
    print("\n--- Genus loop operator Lambda_P ---")
    lc = genus_loop_cubic_virasoro()
    print(f"  Lambda_P(C_Vir) = {simplify(lc)} * x")
    lq = genus_loop_quartic_virasoro()
    print(f"  Lambda_P(Q_Vir) = delta H^(1) = {factor(lq)} * x^2")

    # Loop ratio
    print("\n--- Genus-1 loop ratio rho^(1) ---")
    rho = virasoro_loop_ratio()
    print(f"  rho^(1)_Vir = {factor(rho)}")

    # Finite termination
    print("\n--- Shadow tower termination ---")
    terms = shadow_termination_arity()
    for family, arity in terms.items():
        label = str(arity) if arity is not None else "INFINITE"
        print(f"  {family:15s}: terminates at arity {label}")

    # Numerical evaluations
    print("\n--- Numerical evaluations (Virasoro) ---")
    test_values = [1, Rational(1, 2), 13, 25, 26, -Rational(22, 5)]
    for cv in test_values:
        dH_val = lq.subs(c, cv)
        rho_val = rho.subs(c, cv)
        if dH_val.is_finite and rho_val.is_finite:
            print(f"  c = {str(cv):8s}: delta H^(1) coeff = {dH_val}, "
                  f"rho^(1) = {rho_val}")
        else:
            print(f"  c = {str(cv):8s}: SINGULAR")

    print("\n--- Verification complete ---")


if __name__ == '__main__':
    verify_all()
