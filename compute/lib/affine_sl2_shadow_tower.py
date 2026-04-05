"""
Shadow obstruction tower for affine sl_2 (Kac-Moody family).

Computes the modular shadow hierarchy for the affine sl_2 chiral algebra
at level k, extending the shadow dictionary from Virasoro (infinite tower)
to the first affine case (finite tower, terminates at arity 3).

KEY RESULTS:
  - H_aff = (k/2) h^2 + (k/2) e_ef^2 (Hessian on Cartan + root deformation)
  - C_aff(x,y,z) = kappa(x, [y,z]) (Lie cubic, from the structure constants)
  - Q^contact_aff = 0 (the Jacobiator vanishes for Lie algebras)
  - o^(4)_aff = 0 (quartic obstruction = 0 by Jacobi identity)
  - Shadow obstruction tower TERMINATES at arity 3 (Thm thm:nms-finite-termination)
  - Boundary quartic: xi*Q_aff = C_aff *_P C_aff (non-zero!)
  - Genus loop: Lambda_P(C_aff) gives genus-1 Hessian correction

The affine sl_2 algebra has generators {e, f, h, K} with OPE:
  h(z) h(w) ~ 2k/(z-w)^2
  h(z) e(w) ~ 2e(w)/(z-w)
  h(z) f(w) ~ -2f(w)/(z-w)
  e(z) f(w) ~ k/(z-w)^2 + h(w)/(z-w)

At generic level k != -2 (non-critical), the Killing form is:
  kappa(h,h) = 2k, kappa(e,f) = kappa(f,e) = k.

Ground truth:
  - nonlinear_modular_shadows.tex: Thm thm:nms-affine-cubic-normal-form,
    Cor cor:nms-affine-boundary-tree, Thm thm:nms-finite-termination
  - kac_moody.tex: OPE data and DS reduction
"""

from sympy import (
    Symbol, Rational, simplify, factor, expand,
    binomial, Matrix, symbols, sqrt, cancel
)


k = Symbol('k')
c_km = Symbol('c')  # central charge c = 3k/(k+2) for sl_2


# =============================================================================
# Affine sl_2 shadow data (on the Cartan deformation line)
# =============================================================================

def affine_level():
    """The level parameter k for affine sl_2."""
    return k


def affine_central_charge():
    """Central charge of affine sl_2 at level k via Sugawara:
    c = k * dim(g) / (k + h^v) = 3k/(k+2) for sl_2 (h^v = 2, dim = 3)."""
    return 3 * k / (k + 2)


def affine_dual_coxeter():
    """Dual Coxeter number h^v = 2 for sl_2."""
    return 2


def affine_dim():
    """Dimension of sl_2 = 3."""
    return 3


# =============================================================================
# Hessian (quadratic shadow) on the Cartan line
# =============================================================================

def affine_hessian_cartan():
    """H_aff on the Cartan (h-direction) deformation line.

    The h-h OPE double pole: <h|h> = 2k.
    So H_cartan = k (the coefficient of h^2/2 in the Hessian form,
    or equivalently k * x^2 where x parametrizes the h-direction).

    Note: the full Hessian on sl_2 = span{e,f,h} is the Killing form:
      kappa = 2k * (diagonal on Cartan) + k * (off-diagonal on e,f)
    restricted to the deformation-relevant directions.

    For the one-dimensional h-line: H_h = 2k * x^2 / 2 = k * x^2.
    """
    return k


def affine_propagator_cartan():
    """P_h = H_h^{-1} = 1/k on the Cartan line."""
    return Rational(1) / k


# =============================================================================
# Cubic shadow (the Lie bracket)
# =============================================================================

def affine_cubic_structure_constant():
    """The cubic shadow coefficient on the h-line.

    The cubic shadow C(x,y,z) = kappa(x, [y,z]) for the Lie bracket.
    On the h-line (h is the Cartan generator):
      [h, h] = 0 (Cartan is abelian)
    So C_h(h,h,h) = kappa(h, [h,h]) = 0.

    The cubic vanishes on the Cartan line! This is because the
    Cartan subalgebra is abelian.

    On the FULL algebra (using e, f, h):
      [e, f] = h, [h, e] = 2e, [h, f] = -2f
      kappa(h, [e,f]) = kappa(h, h) = 2k
    So the cubic is nonzero on the full 3-dimensional space but
    VANISHES on the 1-dimensional Cartan line.
    """
    return Rational(0)


def affine_cubic_full():
    """The cubic shadow on the full sl_2 = span{h, e, f}.

    Structure constants f^{abc} in the basis {h, e, f}:
      [e, f] = h      -> f^{ef}_h = 1, f^{fe}_h = -1
      [h, e] = 2e     -> f^{he}_e = 2, f^{eh}_e = -2
      [h, f] = -2f    -> f^{hf}_f = -2, f^{fh}_f = 2

    The cubic shadow:
      C(x,y,z) = kappa(x, [y,z]) = sum_{a,b,c} kappa_{ac} f^{bc}_d x_a y_b z_c

    For the off-diagonal channel (e-f mixing):
      C(h, e, f) = kappa(h, [e,f]) = kappa(h, h) = 2k

    Returns a dict of nonzero cubic components.
    """
    return {
        ('h', 'e', 'f'): 2 * k,
        ('h', 'f', 'e'): -2 * k,
        ('e', 'h', 'f'): -2 * k,
        ('f', 'h', 'e'): 2 * k,
        ('e', 'f', 'h'): 2 * k,
        ('f', 'e', 'h'): -2 * k,
    }


# =============================================================================
# Quartic shadow and obstruction
# =============================================================================

def affine_quartic_contact():
    """Q^contact_aff = 0 on any deformation slice.

    The quartic contact vanishes because the Jacobiator:
      Jac(x,y,z,w) = kappa([x,y], [z,w]) + cyclic
    vanishes by the Jacobi identity for the Lie bracket.

    More precisely: the A-infinity operation m_3 on the Lie algebra
    is zero (the L-infinity structure of a Lie algebra has m_2 = [,]
    and m_n = 0 for n >= 3). Therefore the quartic shadow
    Q = <eta, m_3(eta,eta,eta)> = 0 for any deformation class eta.
    """
    return Rational(0)


def affine_quartic_obstruction():
    """o^(4)_aff = 0 (Jacobi identity kills the obstruction)."""
    return Rational(0)


def affine_quintic_obstruction():
    """o^(5)_aff = {C, Q}_H = 0 since Q = 0."""
    return Rational(0)


# =============================================================================
# Boundary sewing shadow (the KEY non-trivial quantity)
# =============================================================================

def affine_boundary_quartic_full():
    """The boundary quartic shadow: xi*Q_aff = C_aff *_P C_aff.

    This is the sewing product of two cubic vertices connected by
    the propagator. On the full sl_2 = {h, e, f}:

    (C *_P C)(x1, x2, x3, x4) = sum_{channels} P^{ab} C(x1, x2, a) C(b, x3, x4)

    where P^{ab} is the inverse Killing form (propagator).

    The Killing form for sl_2 at level k:
      kappa(h,h) = 2k
      kappa(e,f) = kappa(f,e) = k
    Inverse:
      P(h,h) = 1/(2k)
      P(e,f) = P(f,e) = 1/k

    For the h-h-h-h channel (all Cartan):
      (C *_P C)(h,h,h,h) = sum_a P^{aa'} C(h,h,a) C(a',h,h)
    But C(h,h,a) = kappa(h, [h,a]) and [h,h] = 0, so C(h,h,a) = 0.
    Therefore the boundary quartic vanishes on the Cartan line too.

    The non-trivial channels involve e-f mixing:
      C(h,e,f) = 2k (from above)
    So (C *_P C)(h,e,e,f) and similar mixed terms are nonzero.
    """
    # On the Cartan line: boundary quartic = 0 (Cartan is abelian)
    # On the full algebra: nonzero in off-diagonal channels
    return {
        'cartan_line': Rational(0),
        'h_e_e_f': _boundary_quartic_hef(),
        'description': 'Boundary quartic nonzero in off-diagonal e-f channels',
    }


def _boundary_quartic_hef():
    """Compute (C *_P C)(h,e,f,h) on the full sl_2.

    Channel: contract the middle index.
    (C *_P C)(h,e,f,h) = sum_{a,b} P^{ab} C(h,e,a) C(b,f,h)

    C(h,e,a): kappa(h, [e,a])
      a=h: kappa(h, [e,h]) = kappa(h, -2e) = 0
      a=e: kappa(h, [e,e]) = 0
      a=f: kappa(h, [e,f]) = kappa(h, h) = 2k

    C(b,f,h): kappa(b, [f,h])
      [f,h] = -[h,f] = 2f
      b=h: kappa(h, 2f) = 0
      b=e: kappa(e, 2f) = 2k
      b=f: kappa(f, 2f) = 0

    So only (a,b) = (f,e) contributes:
      P^{fe} * C(h,e,f) * C(e,f,h) = (1/k) * 2k * 2k = 4k
    """
    return 4 * k


# =============================================================================
# Genus loop operator for affine sl_2
# =============================================================================

def affine_genus_loop_cubic():
    """Lambda_P(C_aff) on the Cartan line.

    On the Cartan line, C_cartan = 0, so Lambda_P(C_cartan) = 0.
    The genus-1 Hessian correction from the Cartan-line cubic vanishes.

    On the full algebra, the genus loop contracts two of three
    cubic legs with the propagator:
      Lambda_P(C)(x) = sum_{a,b} P^{ab} C(x, a, b)

    For x = h:
      Lambda_P(C)(h) = P^{hh} C(h,h,h) + P^{ef} C(h,e,f) + P^{fe} C(h,f,e)
                      = (1/(2k)) * 0 + (1/k) * 2k + (1/k) * (-2k)
                      = 2 - 2 = 0

    The genus loop of the cubic ALSO vanishes on h! This is because
    the e-f contributions cancel (they come with opposite signs from
    the antisymmetric Lie bracket).
    """
    return Rational(0)


def affine_genus1_hessian_correction():
    """delta H^(1)_aff on the Cartan line.

    delta H^(1) = Lambda_P(Q^(0)) = Lambda_P(0) = 0.

    Plus the boundary contribution:
    delta H^(1)_boundary = Lambda_P(xi*Q) on the h-h sector.
    But xi*Q on h-h-h-h = 0 (computed above).

    So delta H^(1)_aff = 0 on the Cartan line.

    This is consistent with the known result: for affine algebras,
    the genus-1 curvature correction is kappa(A) * omega_1 (universal),
    with no additional shadow corrections beyond the Hessian level.
    The affine shadow obstruction tower TERMINATES at arity 3.
    """
    return Rational(0)


def affine_loop_ratio():
    """rho^(1)_aff = delta H^(1) / H = 0/k = 0 on the Cartan line.

    Contrast with Virasoro: rho^(1)_Vir = 240/[c^3(5c+22)] != 0.
    The affine loop ratio vanishes because the shadow obstruction tower terminates.
    """
    return Rational(0)


# =============================================================================
# Shadow obstruction tower summary
# =============================================================================

def affine_shadow_tower():
    """Complete shadow obstruction tower for affine sl_2 on the Cartan line.

    Returns the tower as a dict of (arity, coefficient) pairs.

    The tower:
      arity 2: H = k (Hessian, from Killing form)
      arity 3: C = 0 (cubic vanishes on Cartan; nonzero on full sl_2)
      arity >= 4: 0 (terminates)

    For the FULL algebra (3-dimensional):
      arity 2: H = diag(2k, k, k) on {h, e, f} basis
      arity 3: C(x,y,z) = kappa(x, [y,z]) (nonzero)
      arity >= 4: Q^contact = 0, boundary quartic nonzero in off-diagonal
    """
    return {
        'arity_2_cartan': affine_hessian_cartan(),
        'arity_3_cartan': affine_cubic_structure_constant(),
        'arity_4_cartan': affine_quartic_contact(),
        'termination': 3,
        'genus_1_correction_cartan': affine_genus1_hessian_correction(),
        'loop_ratio_cartan': affine_loop_ratio(),
        'cubic_full_sl2': affine_cubic_full(),
        'boundary_quartic_full': affine_boundary_quartic_full(),
    }


# =============================================================================
# Comparison table: Virasoro vs Affine
# =============================================================================

def comparison_table():
    """Shadow obstruction tower comparison: Virasoro vs Affine sl_2.

    Returns a dict summarizing the structural difference.
    """
    from compute.lib.modular_shadow_tower import (
        virasoro_hessian, virasoro_cubic, virasoro_quartic_contact,
        quintic_obstruction_virasoro, virasoro_genus1_hessian_correction,
        virasoro_loop_ratio
    )

    return {
        'virasoro': {
            'H': virasoro_hessian(),
            'C': virasoro_cubic(),
            'Q': virasoro_quartic_contact(),
            'o5': quintic_obstruction_virasoro(),
            'dH1': virasoro_genus1_hessian_correction(),
            'rho1': virasoro_loop_ratio(),
            'terminates': False,
        },
        'affine_sl2': {
            'H': affine_hessian_cartan(),
            'C': affine_cubic_structure_constant(),
            'Q': affine_quartic_contact(),
            'o5': affine_quintic_obstruction(),
            'dH1': affine_genus1_hessian_correction(),
            'rho1': affine_loop_ratio(),
            'terminates': True,
            'termination_arity': 3,
        },
    }


# =============================================================================
# Verification
# =============================================================================

def verify_all():
    """Run all affine sl_2 shadow verifications."""
    print("=" * 70)
    print("AFFINE sl_2 SHADOW TOWER")
    print("=" * 70)

    print(f"\nHessian (Cartan line): H = {affine_hessian_cartan()} * x^2")
    print(f"Propagator (Cartan): P = {affine_propagator_cartan()}")
    print(f"Cubic (Cartan): C = {affine_cubic_structure_constant()}")
    print(f"Quartic contact: Q = {affine_quartic_contact()}")
    print(f"Quartic obstruction: o^(4) = {affine_quartic_obstruction()}")
    print(f"Quintic obstruction: o^(5) = {affine_quintic_obstruction()}")
    print(f"Genus-1 correction (Cartan): delta H^(1) = {affine_genus1_hessian_correction()}")
    print(f"Loop ratio (Cartan): rho^(1) = {affine_loop_ratio()}")

    print(f"\nBoundary quartic (h,e,f,h channel): {_boundary_quartic_hef()}")
    print(f"Genus loop of cubic (h direction): {affine_genus_loop_cubic()}")

    print(f"\nShadow obstruction tower terminates at arity: {shadow_termination_arity_affine()}")
    print(f"Central charge: c = {affine_central_charge()}")
    print(f"  At k=1: c = {affine_central_charge().subs(k, 1)}")
    print(f"  At k=2: c = {affine_central_charge().subs(k, 2)}")


def shadow_termination_arity_affine():
    """Affine sl_2 shadow obstruction tower terminates at arity 3."""
    return 3


if __name__ == '__main__':
    verify_all()
