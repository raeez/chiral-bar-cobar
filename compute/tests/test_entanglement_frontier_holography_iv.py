"""Independent verification for entanglement and frontier holography bottlenecks."""

from __future__ import annotations

from fractions import Fraction

import sympy as sp

from compute.lib.entanglement_entropy_engine import (
    central_charge_affine_sl2,
    central_charge_heisenberg,
    entanglement_entropy_exact,
    kappa_affine_sl2,
    kappa_heisenberg,
    shadow_entropy_prefactor,
)
from compute.lib.independent_verification import independent_verification


def _kron3(a: sp.Matrix, b: sp.Matrix, c: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(a, b, c)


def _sl2_spin_half_omega(site_i: int, site_j: int) -> sp.Matrix:
    """Exact sl2 Casimir on sites i,j of (Q^2)^{tensor 3}."""
    e = sp.Matrix([[0, 1], [0, 0]])
    f = sp.Matrix([[0, 0], [1, 0]])
    h = sp.Matrix([[1, 0], [0, -1]])
    one = sp.eye(2)
    local_terms = [(h, h, sp.Rational(1, 2)), (e, f, sp.Integer(1)), (f, e, sp.Integer(1))]
    total = sp.zeros(8)
    for left, right, coeff in local_terms:
        factors = []
        for site in range(3):
            if site == site_i:
                factors.append(left)
            elif site == site_j:
                factors.append(right)
            else:
                factors.append(one)
        total += coeff * _kron3(*factors)
    return total


@independent_verification(
    claim="thm:ent-scalar-entropy",
    derived_from=[
        "entanglement_modular_koszul.tex replica proof using the twist dimension",
        "Calabrese-Cardy import recorded as lem:ent-twist-dimension",
    ],
    verified_against=[
        "Symbolic limit of the n-sheeted two-point exponent",
        "Exact rational algebra from h_n to S_n and the n->1 coefficient",
    ],
    disjoint_rationale=(
        "The manuscript cites the CFT twist-dimension theorem and then performs "
        "the replica manipulation in prose.  This test recomputes the algebra "
        "symbolically from h_n, log Z_n, and the n->1 limit."
    ),
)
def test_ent_scalar_entropy_replica_factor_four_and_limit():
    """h_n = c/24(n-1/n) gives S_n = c/6(1+1/n) log and S_EE = c/3 log."""
    n, c, x = sp.symbols("n c x", positive=True)
    h_n = c * (n - 1 / n) / 24
    log_z_n = -4 * h_n * x
    renyi = sp.simplify(log_z_n / (1 - n))
    assert sp.simplify(renyi - c * (n + 1) * x / (6 * n)) == 0
    assert sp.simplify(sp.limit(renyi, n, 1) - c * x / 3) == 0


@independent_verification(
    claim="thm:ent-scalar-entropy",
    derived_from=[
        "Definition of S_n and S_EE in setup:ent-framework",
        "Theorem statement eq:ent-renyi-scalar and eq:ent-vn-scalar",
    ],
    verified_against=[
        "Finite density matrix trace identity for rho=diag(1/4,3/4)",
        "L'Hopital limit of log Tr(rho^n)/(1-n) to Shannon entropy",
    ],
    disjoint_rationale=(
        "The theorem proof uses CFT twist fields.  The sign of the replica "
        "definition is checked on a two-state density matrix, where no CFT "
        "or modular-Koszul input is present."
    ),
)
def test_replica_trace_limit_has_the_entropy_sign():
    """lim_{n->1} log Tr rho^n/(1-n) equals -Tr rho log rho."""
    n = sp.symbols("n", positive=True)
    p = sp.Rational(1, 4)
    q = sp.Rational(3, 4)
    renyi = sp.log(p**n + q**n) / (1 - n)
    expected = -(p * sp.log(p) + q * sp.log(q))
    assert sp.simplify(sp.limit(renyi, n, 1) - expected) == 0


@independent_verification(
    claim="thm:ent-scalar-entropy",
    derived_from=[
        "modular-characteristic formulas in the standard-landscape census",
        "legacy entanglement_entropy_engine shadow-prefactor convention",
    ],
    verified_against=[
        "Sugawara central-charge computation c(sl2,k)=k dim(g)/(k+hvee)",
        "Rank-one Heisenberg central charge and direct c/3 Calabrese-Cardy coefficient",
    ],
    disjoint_rationale=(
        "The old compute surface conflated physical entropy with the shadow "
        "2*kappa/3 readout.  This test checks two families where central charge "
        "and modular characteristic separate."
    ),
)
def test_scalar_entropy_uses_c_not_kappa_outside_virasoro_lane():
    """Heisenberg and affine sl2 separate c/3 from 2*kappa/3."""
    assert entanglement_entropy_exact(central_charge_heisenberg(2)) == Fraction(1, 3)
    assert shadow_entropy_prefactor(kappa_heisenberg(2)) == Fraction(4, 3)

    assert central_charge_affine_sl2(1) == Fraction(1)
    assert kappa_affine_sl2(1) == Fraction(9, 4)
    assert entanglement_entropy_exact(central_charge_affine_sl2(1)) == Fraction(1, 3)
    assert shadow_entropy_prefactor(kappa_affine_sl2(1)) == Fraction(3, 2)


@independent_verification(
    claim="thm:frontier-protected-bulk-antiinvolution",
    derived_from=[
        "Verdier intertwining and higher-genus inversion in the protected-transform proof",
        "involution-splitting lemma invoked in frontier_modular_holography_platonic.tex",
    ],
    verified_against=[
        "Finite symplectic vector-space model with J=[[0,I],[-I,0]]",
        "Swap matrix P checking P^2=I and P^T J P=-J exactly",
    ],
    disjoint_rationale=(
        "The theorem proof is categorical.  The test forgets categories and "
        "checks the exact matrix sign of the protected anti-involution on a "
        "split finite-dimensional Lagrangian model."
    ),
)
def test_protected_transform_is_exact_anti_symplectic_involution():
    """The protected swap squares to identity and reverses the symplectic form."""
    ident = sp.eye(2)
    zero = sp.zeros(2)
    j_form = sp.Matrix.vstack(
        sp.Matrix.hstack(zero, ident),
        sp.Matrix.hstack(-ident, zero),
    )
    swap = sp.Matrix.vstack(
        sp.Matrix.hstack(zero, ident),
        sp.Matrix.hstack(ident, zero),
    )
    assert swap * swap == sp.eye(4)
    assert swap.T * j_form * swap == -j_form


@independent_verification(
    claim="thm:frontier-protected-bulk-antiinvolution",
    derived_from=[
        "cofiber identification statement in eq:frontier-holographic-cofiber-identification",
        "protected transform theorem proof using the direct-sum decomposition C=Q(A)+Q(A!)",
    ],
    verified_against=[
        "Strict finite chain-complex quotient of block-diagonal complexes",
        "Projection chain-map identity p d_C = d_W p and kernel=image inclusion",
    ],
    disjoint_rationale=(
        "The manuscript works in the homotopy category.  This test computes a "
        "strict split cofiber in finite matrices, including the differential "
        "compatibility that fixes the sign convention."
    ),
)
def test_split_cofiber_is_second_lagrangian_chain_complex():
    """For a strict split inclusion V -> V+W, the cofiber is W without shift."""
    d_v = sp.Matrix([[0, 1], [0, 0]])
    d_w = sp.Matrix([[0, 0], [1, 0]])
    d_c = sp.diag(0, 0, 0, 0)
    d_c[:2, :2] = d_v
    d_c[2:, 2:] = d_w

    inclusion = sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
    projection = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1]])

    assert d_c * d_c == sp.zeros(4)
    assert projection * d_c == d_w * projection
    assert d_c * inclusion == inclusion * d_v
    assert inclusion.rank() == 2
    assert projection.rank() == 2
    assert projection * inclusion == sp.zeros(2)


@independent_verification(
    claim="thm:frontier-protected-bulk-antiinvolution",
    derived_from=[
        "abstract claim (A!)! is equivalent to A in the protected-transform theorem",
        "Koszul-dual branch language in the theorem statement",
    ],
    verified_against=[
        "Feigin-Frenkel affine level involution k -> -k-2hvee",
        "Virasoro central-charge involution c -> 26-c",
    ],
    disjoint_rationale=(
        "The theorem uses categorical double-duality.  The test checks two "
        "standard-family parameter involutions by exact arithmetic, independent "
        "of the cofiber and Verdier proof text."
    ),
)
def test_standard_family_double_duals_return_the_parameter():
    """Two explicit Koszul-dual parameter involutions square to the identity."""
    for h_dual in (2, 3, 30):
        for k in (Fraction(-1), Fraction(0), Fraction(5, 2)):
            dual = -k - 2 * h_dual
            assert -dual - 2 * h_dual == k

    for c in (Fraction(0), Fraction(1, 2), Fraction(13), Fraction(26)):
        assert 26 - (26 - c) == c


@independent_verification(
    claim="thm:sphere-reconstruction",
    derived_from=[
        "genus-zero projection of the modular MC equation in the theorem proof",
        "statement that nabla_hol is d minus the shadow of Theta_A",
    ],
    verified_against=[
        "Arnold partial-fraction identity on Conf_3(C)",
        "Direct symbolic cancellation of eta12 eta23 plus eta23 eta31 plus eta31 eta12",
    ],
    disjoint_rationale=(
        "The manuscript derives flatness from the MC equation.  This test "
        "checks the independent configuration-space identity that makes the "
        "genus-zero connection curvature vanish."
    ),
)
def test_sphere_flatness_arnold_identity_symbolic():
    """The three-point Arnold rational coefficient cancels exactly."""
    z1, z2, z3 = sp.symbols("z1 z2 z3")
    arnold = (
        1 / ((z1 - z2) * (z2 - z3))
        + 1 / ((z2 - z3) * (z3 - z1))
        + 1 / ((z3 - z1) * (z1 - z2))
    )
    assert sp.simplify(arnold) == 0


@independent_verification(
    claim="thm:sphere-reconstruction",
    derived_from=[
        "shadow/KZ comparison invoked by thm:sphere-reconstruction(iii)",
        "frontier theorem proof via conformal-block Ward identities",
    ],
    verified_against=[
        "Exact spin-half sl2 tensor matrices on (Q^2)^{tensor 3}",
        "Infinitesimal braid relations for Omega_12, Omega_13, Omega_23",
    ],
    disjoint_rationale=(
        "The theorem routes the affine comparison through the shadow connection. "
        "This test computes the finite KZ Casimir matrices directly and verifies "
        "the algebraic flatness relations."
    ),
)
def test_sphere_reconstruction_kz_infinitesimal_braid_relation():
    """The KZ curvature vanishes by exact infinitesimal braid relations."""
    omega12 = _sl2_spin_half_omega(0, 1)
    omega13 = _sl2_spin_half_omega(0, 2)
    omega23 = _sl2_spin_half_omega(1, 2)

    assert omega12 * (omega13 + omega23) - (omega13 + omega23) * omega12 == sp.zeros(8)
    assert (omega12 + omega13) * omega23 - omega23 * (omega12 + omega13) == sp.zeros(8)


@independent_verification(
    claim="thm:sphere-reconstruction",
    derived_from=[
        "horizontal-section clause for genus-zero correlators in thm:sphere-reconstruction",
        "Heisenberg comparison surface in the shadow-connection chapter",
    ],
    verified_against=[
        "Direct derivative of the abelian three-point product of powers",
        "Charge-diagonal dlog connection coefficient computed from first principles",
    ],
    disjoint_rationale=(
        "The theorem cites Ward identities.  The test verifies a concrete "
        "sphere correlator on the abelian comparison surface by differentiating "
        "the product formula itself."
    ),
)
def test_sphere_reconstruction_heisenberg_horizontal_section():
    """The Heisenberg product correlator is horizontal for the dlog connection."""
    z1, z2, z3, kappa = sp.symbols("z1 z2 z3 kappa")
    charges = (sp.Integer(1), sp.Integer(-1), sp.Integer(0))
    points = (z1, z2, z3)
    log_f = sp.Integer(0)
    for i in range(3):
        for j in range(i + 1, 3):
            log_f += kappa * charges[i] * charges[j] * sp.log(points[i] - points[j])

    for i, z_i in enumerate(points):
        dlog = sp.diff(log_f, z_i)
        connection_coeff = sum(
            kappa * charges[i] * charges[j] / (points[i] - points[j])
            for j in range(3)
            if j != i
        )
        assert sp.simplify(dlog - connection_coeff) == 0
