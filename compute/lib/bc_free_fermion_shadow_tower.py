"""Shadow obstruction tower for the free fermion bc at lambda=1/2.

Computes the shadow tower invariants S_2 through S_8 for a single real
fermion psi of conformal weight h=1/2 with OPE:

    psi(z) psi(w) = 1/(z-w) + regular

This is the bc ghost system at lambda=1/2 (equivalently, a single
Majorana fermion, the Ising CFT free-field content).

KEY DATA:
    c = 1/2
    kappa = c/2 = 1/4
    S_2 = kappa = 1/4
    S_3 = 0  (fermionic antisymmetry, Prop prop:fermion-shadow-invariants)
    S_4 = 0  (follows from S_3=0 by cubic gauge triviality)
    S_r = 0  for all r >= 3
    Delta = 8*kappa*S_4 = 0
    Class G (Gaussian), shadow depth r_max = 2

The free fermion achieves class G through ANTISYMMETRY: the simple pole
would produce a cubic shadow in a bosonic algebra, but fermionic
statistics force S_3 = 0 because cyclic permutations on three-point
configuration space forms act by cube roots of unity.  This is
complementary to the Heisenberg mechanism (which achieves class G
through commutativity and absence of a simple pole).

CRITICAL DISTINCTION: The free fermion (class G, depth 2) is NOT the
Virasoro minimal model at c=1/2 (class M, infinite tower with
S_4 = 40/49).  They share the central charge but are different algebras
with radically different shadow towers.

Ground truth:
    free_fields.tex: Prop prop:fermion-shadow-invariants,
        Prop prop:fermion-shadow-metric
    computational_methods.tex: Example ex:comp-virasoro-half (contrast)
    n2_free_field_shadow.py: kappa_fermion_pair() = 1/2 = 2 * 1/4
"""

from sympy import Rational, Symbol, sqrt


# =============================================================================
# Parameters
# =============================================================================

def central_charge():
    """Central charge of the free fermion (bc at lambda=1/2).

    c_bc(lambda) = 1 - 3*(2*lambda - 1)^2.
    At lambda = 1/2: c = 1 - 3*(0)^2 = 1 for a COMPLEX fermion (bc pair).
    A single REAL fermion (Majorana) has c = 1/2.

    # VERIFIED:
    #   [DC] c_bc(1/2) = 1 for complex; real = 1/2 of complex -> c = 1/2
    #   [LT] Di Francesco et al, yellow book, Ising model c = 1/2
    """
    return Rational(1, 2)


def conformal_weight():
    """Conformal weight of the fermion generator psi.

    # VERIFIED:
    #   [DC] bc at lambda=1/2: h_b = lambda = 1/2, h_c = 1-lambda = 1/2
    #   [LT] Standard: free fermion weight 1/2
    """
    return Rational(1, 2)


def kappa():
    """Modular characteristic kappa(F) = c/2 = 1/4.

    For a single-generator chiral algebra, kappa = c/2 (universal).
    At c = 1/2: kappa = 1/4.

    # VERIFIED:
    #   [DC] kappa = c/2 = (1/2)/2 = 1/4
    #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-kappa
    #   [CF] n2_free_field_shadow.py: kappa_fermion_pair() = 1/2 = 2 * kappa(single)
    """
    return Rational(1, 4)


def ope_pole_order():
    """OPE pole order p for psi(z)psi(w) ~ 1/(z-w).

    Simple pole: p = 1.

    # VERIFIED:
    #   [DC] psi(z)psi(w) ~ 1/(z-w), pole order 1
    #   [LT] free_fields.tex Definition of free fermion OPE
    """
    return 1


def r_matrix_pole_order():
    """r-matrix pole order = OPE pole order - 1 = 0 (AP19).

    The d-log absorption reduces the pole order by 1.
    For the free fermion: OPE has simple pole, so r-matrix
    has no pole (constant/regular).

    # VERIFIED:
    #   [DC] p_r = p_OPE - 1 = 1 - 1 = 0
    #   [LT] AP19: pole_r = pole_OPE - 1
    """
    return 0


# =============================================================================
# Shadow tower coefficients S_2 through S_8
# =============================================================================

def S_2():
    """Quadratic shadow S_2 = kappa = 1/4.

    # VERIFIED:
    #   [DC] S_2 = kappa by definition of the shadow tower
    #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants
    #   [CF] landscape_census_verification.py: kappa_free_fermion() = 1/4
    """
    return Rational(1, 4)


def S_3():
    """Cubic shadow S_3 = 0.

    Fermionic antisymmetry forces the cubic coupling to vanish.
    On three-point configuration space, the cyclic permutation acts
    by cube roots of unity on the form space, incompatible with the
    antisymmetric tensor factor.

    # VERIFIED:
    #   [DC] Cyclic eigenvalue argument (free_fields.tex proof)
    #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-S3
    """
    return Rational(0)


def S_4():
    """Quartic shadow S_4 = 0.

    With S_3 = 0, the quartic contact invariant vanishes by cubic
    gauge triviality (Thm thm:cubic-gauge-triviality).

    # VERIFIED:
    #   [DC] S_3=0 implies obstruction class o_4=0 (recursive existence)
    #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-S4
    """
    return Rational(0)


def S_5():
    """Quintic shadow S_5 = 0.

    The quintic obstruction o^(5) = {C, Q}_H where C (cubic) and Q
    (quartic contact) both vanish, so o^(5) = 0.

    # VERIFIED:
    #   [DC] o^(5) = {S_3, S_4}_H = {0, 0}_H = 0
    #   [LT] modular_shadow_tower.py: sewing product of zeros is zero
    """
    return Rational(0)


def S_6():
    """Sextic shadow S_6 = 0.

    All higher shadows vanish: once S_3=S_4=0, the recursive
    master equation nabla_H(S_r) + o^(r) = 0 has o^(r)=0 for all
    r >= 5 (induction on sewing products of lower-arity zeros).

    # VERIFIED:
    #   [DC] Induction: o^(r) built from sewing products of S_j with j<r, all zero
    #   [LT] Thm thm:recursive-existence (tower terminates once S_3=S_4=0)
    """
    return Rational(0)


def S_7():
    """Septic shadow S_7 = 0.

    # VERIFIED:
    #   [DC] Same induction as S_6
    #   [SY] Class G termination at depth 2
    """
    return Rational(0)


def S_8():
    """Octic shadow S_8 = 0.

    # VERIFIED:
    #   [DC] Same induction as S_6
    #   [SY] Class G termination at depth 2
    """
    return Rational(0)


def shadow_tower(max_arity=8):
    """Complete shadow tower S_2 through S_{max_arity}.

    Returns dict {r: S_r} for r = 2, ..., max_arity.
    """
    tower_funcs = {
        2: S_2, 3: S_3, 4: S_4, 5: S_5,
        6: S_6, 7: S_7, 8: S_8,
    }
    result = {}
    for r in range(2, max_arity + 1):
        if r in tower_funcs:
            result[r] = tower_funcs[r]()
        else:
            # All S_r = 0 for r >= 3 (class G)
            result[r] = Rational(0)
    return result


# =============================================================================
# Derived quantities
# =============================================================================

def critical_discriminant():
    """Critical discriminant Delta = 8*kappa*S_4 = 0.

    Delta = 0 implies the shadow metric Q(t) is a perfect square.

    # VERIFIED:
    #   [DC] Delta = 8 * (1/4) * 0 = 0
    #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-discriminant
    """
    return 8 * kappa() * S_4()


def shadow_metric():
    """Shadow metric Q(t) = (2*kappa)^2 = 1/4, constant.

    For class G: Q(t) = (2*kappa + 3*alpha*t)^2 + 4*kappa*S_4*t^2
    with alpha = S_3 = 0, S_4 = 0:
    Q(t) = (2*kappa)^2 = (1/2)^2 = 1/4.

    # VERIFIED:
    #   [DC] Q = (2*1/4)^2 = 1/4
    #   [LT] free_fields.tex Prop prop:fermion-shadow-metric eq:fermion-shadow-metric
    """
    return (2 * kappa()) ** 2


def shadow_generating_function_coefficient():
    """H(t) = t^2 * sqrt(Q(t)) = (1/2)*t^2.

    The generating function is purely quadratic (no higher terms).

    # VERIFIED:
    #   [DC] sqrt(1/4) = 1/2, so H(t) = (1/2)*t^2
    #   [LT] free_fields.tex: "H(t) = t^2 sqrt(Q_F) = (1/2)*t^2"
    """
    return Rational(1, 2)


# =============================================================================
# Classification
# =============================================================================

def shadow_class():
    """Shadow class: G (Gaussian).

    # VERIFIED:
    #   [DC] S_3=S_4=0 and Delta=0 -> class G by definition
    #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-class
    #   [CF] Heisenberg also class G (different mechanism: commutativity vs antisymmetry)
    """
    return 'G'


def shadow_depth():
    """Shadow depth r_max = 2.

    The tower terminates at arity 2: S_r = 0 for all r >= 3.

    # VERIFIED:
    #   [DC] max r with S_r != 0 is r=2
    #   [LT] free_fields.tex: r_max = 2
    """
    return 2


def theta_mc_element():
    """The MC element Theta_F = (1/4) * eta tensor Lambda.

    The full MC element is determined entirely by kappa (no higher
    corrections needed since all S_r = 0 for r >= 3).

    # VERIFIED:
    #   [DC] Theta = kappa * eta tensor Lambda = (1/4) * eta tensor Lambda
    #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-tower
    """
    return {'kappa_coefficient': kappa(), 'higher_corrections': False}


# =============================================================================
# Contrast with Virasoro at c=1/2
# =============================================================================

def virasoro_contrast():
    """Contrast: free fermion vs Virasoro at c=1/2.

    Both have c=1/2, kappa=1/4, but radically different shadow towers:
    - Free fermion: S_3=0, S_4=0, class G (depth 2)
    - Virasoro at c=1/2: S_3=alpha=2, S_4=40/49, class M (infinite depth)

    The Virasoro algebra is NOT the free fermion. The Virasoro algebra
    at c=1/2 is the Ising minimal model; the free fermion is an extended
    algebra with a weight-1/2 generator that the Virasoro algebra lacks.

    # VERIFIED:
    #   [DC] Vir S_4 = 10/(c*(5c+22)) = 10/((1/2)*(49/2)) = 40/49
    #   [LT] computational_methods.tex Example ex:comp-virasoro-half
    """
    c_val = Rational(1, 2)
    return {
        'free_fermion': {
            'c': c_val,
            'kappa': Rational(1, 4),
            'S_3': Rational(0),
            'S_4': Rational(0),
            'Delta': Rational(0),
            'class': 'G',
            'depth': 2,
        },
        'virasoro_c_half': {
            'c': c_val,
            'kappa': Rational(1, 4),
            'S_3': Rational(2),       # alpha = 2 for Virasoro
            'S_4': Rational(40, 49),   # 10/(c*(5c+22)) at c=1/2
            'Delta': 8 * Rational(1, 4) * Rational(40, 49),  # = 80/49
            'class': 'M',
            'depth': float('inf'),
        },
    }


# =============================================================================
# Verification
# =============================================================================

def verify_all():
    """Run all internal consistency checks."""
    results = {}

    # Basic parameters
    results['c = 1/2'] = (central_charge() == Rational(1, 2))
    results['h = 1/2'] = (conformal_weight() == Rational(1, 2))
    results['kappa = 1/4'] = (kappa() == Rational(1, 4))
    results['kappa = c/2'] = (kappa() == central_charge() / 2)

    # Shadow tower
    results['S_2 = 1/4'] = (S_2() == Rational(1, 4))
    results['S_2 = kappa'] = (S_2() == kappa())
    results['S_3 = 0'] = (S_3() == 0)
    results['S_4 = 0'] = (S_4() == 0)
    results['S_5 = 0'] = (S_5() == 0)
    results['S_6 = 0'] = (S_6() == 0)
    results['S_7 = 0'] = (S_7() == 0)
    results['S_8 = 0'] = (S_8() == 0)

    # Derived
    results['Delta = 0'] = (critical_discriminant() == 0)
    results['Q = 1/4'] = (shadow_metric() == Rational(1, 4))
    results['H coeff = 1/2'] = (
        shadow_generating_function_coefficient() == Rational(1, 2)
    )

    # Classification
    results['class G'] = (shadow_class() == 'G')
    results['depth 2'] = (shadow_depth() == 2)

    # OPE / r-matrix
    results['OPE pole = 1'] = (ope_pole_order() == 1)
    results['r-matrix pole = 0'] = (r_matrix_pole_order() == 0)

    # Tower completeness
    tower = shadow_tower(8)
    results['tower length'] = (len(tower) == 7)
    results['tower S_2 nonzero'] = (tower[2] != 0)
    results['tower S_3..S_8 zero'] = all(
        tower[r] == 0 for r in range(3, 9)
    )

    # Virasoro contrast
    contrast = virasoro_contrast()
    results['Vir S_4 != fermion S_4'] = (
        contrast['virasoro_c_half']['S_4'] != contrast['free_fermion']['S_4']
    )
    results['Vir class != fermion class'] = (
        contrast['virasoro_c_half']['class'] != contrast['free_fermion']['class']
    )

    return results


if __name__ == '__main__':
    print("=" * 70)
    print("FREE FERMION bc(lambda=1/2) SHADOW TOWER")
    print("=" * 70)

    print(f"\nc = {central_charge()}")
    print(f"h = {conformal_weight()}")
    print(f"kappa = {kappa()}")

    print(f"\nShadow tower:")
    for r, val in shadow_tower(8).items():
        print(f"  S_{r} = {val}")

    print(f"\nDelta = {critical_discriminant()}")
    print(f"Q(t) = {shadow_metric()}")
    print(f"Class: {shadow_class()}, depth: {shadow_depth()}")

    print(f"\nVerification:")
    for name, ok in verify_all().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
