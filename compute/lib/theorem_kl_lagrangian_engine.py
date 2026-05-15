r"""Knill-Laflamme scope diagnostics for the Lagrangian compute surface.

MATHEMATICAL FRAMEWORK
======================

The Knill-Laflamme (KL) conditions for quantum error correction state
that a code subspace C in a Hilbert space H admits exact error correction
against an error set {E_a} if and only if

    P_C  E_a^dag  E_b  P_C  =  C_{ab} P_C         (*)

where P_C is the projector onto C and C_{ab} is a Hermitian matrix
depending only on the errors, not on the code states.  Equivalently:

    <psi_i| E_a^dag E_b |psi_j>  =  C_{ab} delta_{ij}

for any orthonormal basis {|psi_i>} of C.

This engine checks the finite algebraic surfaces around (*) via four
independent diagnostics grounded in the monograph.  It does not promote
Verdier isotropy, finite scalar examples, shadow-slot counts, or
bar-cobar inversion to a full Hilbert-space quantum error-correcting
theorem.

PATH 1 (VERDIER ANTI-INVOLUTION):
  Theorem C provides Q_g(A) + Q_g(A^!) =
  H*(M_g_bar, Z_ch^der(A)), where Z_ch^der(A) is the bulk/derived
  centre.
  The Verdier duality sigma satisfies <sigma(v), sigma(w)>_D = -<v,w>_D.
  The eigenspaces V+ = Q_g(A), V- = Q_g(A^!) are isotropic:
  <v,w>_D = 0 for v,w in V+ (or both in V-).
  Isotropy of the code subspace C = V+ is the algebraic prerequisite
  for a symplectic code comparison.  It is not the Hilbert-space KL
  equation, because no Hermitian adjoint or physical error algebra has
  been supplied.
  On the genus-1 scalar conformal-block line, KL compression is
  automatic (any operator on a 1D space is scalar).  This does not make
  the whole genus-1 complementarity complex one-dimensional.

PATH 2 (LAGRANGIAN GEOMETRY):
  Q_g(A) is Lagrangian in the (-(3g-3))-shifted symplectic space C_g(A)
  with respect to the shifted symplectic form omega_{-(3g-3)}.
  Lagrangian = maximally isotropic + half-dimensional.
  The Verdier-isotropic condition omega(v,w) = 0 for v,w in Q_g(A)
  follows from the Lagrangian condition.  This is the algebraic
  prerequisite named in Proposition prop:hc-knill-laflamme, not the
  physical KL compression identity.

PATH 3 (SHADOW DEPTH = FORMAL SLOTS):
  The shadow obstruction tower Theta_A^{<=r} provides r-2 formal
  non-scalar MC slots in finite G/L/C windows.  These are not
  Hilbert-space redundancy channels or code-distance data until a
  physical error model and recovery maps are supplied.

PATH 4 (ENTANGLEMENT WEDGE / BAR-COBAR ADJUNCTION):
  The bar-cobar adjunction B -| Omega (Theorem A) provides encoding
  into the bar coalgebra B(A) and decoding by cobar.  Koszulness
  (Theorem B: Omega(B(A)) ~ A) ensures exact reconstruction: the
  cobar inverts the bar and recovers A itself.  The intermediate
  algebra A^i is H^*(B(A)); the Koszul dual A^! is obtained from
  A^i by Verdier/linear duality under finite-type or completed
  hypotheses.
  This is exact algebraic boundary recovery.  It is not construction of
  a physical bulk theory and not a KL recovery theorem by itself.

CONVENTIONS (from CLAUDE.md anti-patterns):
  AP19: r-matrix has poles one order below the OPE
  AP20: kappa(A) is intrinsic to A, not the physical system
  AP24: kappa + kappa' = 13 for Virasoro
  AP25: B(A) is a coalgebra; A^i = H^*(B(A)); A^! comes from A^i by
        Verdier/linear duality under finite-type/completed hypotheses;
        Omega(B(A)) = A is inversion; Z_ch^der(A) is bulk/derived centre
  AP31: kappa = 0 leaves Theta as separate data
  AP45: desuspension LOWERS degree: |s^{-1}v| = |v| - 1

References:
  prop:hc-knill-laflamme (holographic_codes_koszul.tex)
  thm:hc-symplectic-code (holographic_codes_koszul.tex)
  thm:hc-shadow-redundancy (holographic_codes_koszul.tex)
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  Knill-Laflamme 1997 (quant-ph/9604034)
  Almheiri-Dong-Harlow 2015 (1411.7041)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import numpy as np
from sympy import (
    Rational, Symbol, bernoulli, factorial, Matrix, eye, zeros as sym_zeros,
    simplify, sqrt, S, pi,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    kappa_wN,
    shadow_depth_class,
    entanglement_correction_depth,
    faber_pandharipande,
    von_neumann_entropy_scalar,
    STANDARD_KAPPAS,
)


# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
g_sym = Symbol('g', positive=True, integer=True)

AP25_OBJECT_CHAIN = {
    'bar_object': 'B(A) is the bar coalgebra.',
    'bar_cohomology': 'A^i = H^*(B(A)).',
    'koszul_dual': (
        'A^! is obtained from A^i by Verdier/linear duality under '
        'finite-type or completed hypotheses.'
    ),
    'inversion': 'Omega(B(A)) = A is bar-cobar inversion.',
    'derived_centre': 'Z_ch^der(A) is the bulk/derived centre.',
}

HOLOGRAPHIC_PACKAGE_ENTRIES = (
    'A',
    'A^i',
    'A^!',
    'C',
    'r(z)',
    'Theta_A',
    'nabla^hol',
)

MODULAR_KOSZUL_COMPUTE_PROJECTIONS = (
    'Fact_X(L)',
    'barB_X(L)',
    'Theta_L',
    'L_L',
    '(V_br,T_br)',
    'R4_mod(L)',
)

KERNEL_NORMALIZATIONS = {
    'affine_raw_collision': 'k*Omega_tr/z',
    'affine_kz': 'Omega/((k+h^vee)z)',
    'heisenberg': 'k/z',
    'virasoro': '(c/2)/z^3 + 2T/z',
}

KL_SCOPE_FIREWALL = {
    'verdier_isotropy': (
        'algebraic symplectic prerequisite; not the Hilbert-space KL equation'
    ),
    'scalar_line': 'one-dimensional compression; KL automatic',
    'lagrangian_projection': (
        'removes the complementary Lagrangian component; does not correct '
        'logical action inside the code'
    ),
    'shadow_depth': (
        'formal MC slot count; not a Hilbert-space code distance'
    ),
    'bar_cobar': (
        'boundary algebra quasi-isomorphism; not physical bulk equivalence'
    ),
}


def holographic_package_entries() -> Tuple[str, ...]:
    """Canonical seven entries of the holographic package H(A)."""
    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_compute_projections() -> Tuple[str, ...]:
    """Canonical six projections of the modular Koszul compute package."""
    return MODULAR_KOSZUL_COMPUTE_PROJECTIONS


def kernel_normalization_firewall() -> Dict[str, str]:
    """Return kernel normalizations whose coefficients must not be conflated."""
    return dict(KERNEL_NORMALIZATIONS)


def kl_scope_firewall() -> Dict[str, str]:
    """Return the scope boundaries enforced by this compute surface."""
    return dict(KL_SCOPE_FIREWALL)


# ===========================================================================
# 1. SYMPLECTIC FORM AND VERDIER INVOLUTION (algebraic foundations)
# ===========================================================================

def verdier_symplectic_form(n: int) -> np.ndarray:
    r"""Standard symplectic form J on C^{2n}.

    J = [[0, I_n], [-I_n, 0]]

    This is the Verdier pairing <v,w>_D = v^T J w restricted to each
    genus-g complementarity summand.  The eigenspaces of the Verdier
    involution sigma are the two Lagrangian subspaces.

    >>> J = verdier_symplectic_form(2)
    >>> J.shape
    (4, 4)
    >>> np.allclose(J + J.T, 0)  # antisymmetric
    True
    >>> np.linalg.matrix_rank(J)  # nondegenerate
    4
    """
    I_n = np.eye(n)
    Z = np.zeros((n, n))
    return np.block([[Z, I_n], [-I_n, Z]])


def verdier_involution(n: int) -> np.ndarray:
    r"""Verdier involution sigma on C^{2n}.

    sigma = [[I_n, 0], [0, -I_n]]

    This is the involution whose +1 eigenspace is Q_g(A) (the code
    subspace) and whose -1 eigenspace is Q_g(A^!) (the error space).

    The key property: <sigma(v), sigma(w)>_D = -<v,w>_D
    (anti-commutativity with respect to the symplectic form).

    >>> sigma = verdier_involution(2)
    >>> np.allclose(sigma @ sigma, np.eye(4))  # involution
    True
    """
    I_n = np.eye(n)
    Z = np.zeros((n, n))
    return np.block([[I_n, Z], [Z, -I_n]])


def verify_anti_commutativity(n: int) -> bool:
    r"""Verify <sigma(v), sigma(w)>_D = -<v,w>_D for all v, w.

    This is equivalent to sigma^T J sigma = -J where J is the
    symplectic form.

    Proof: sigma^T = sigma (symmetric), so
      sigma^T J sigma = sigma J sigma.
    With sigma = diag(I, -I) and J = [[0,I],[-I,0]]:
      sigma J sigma = [[I,0],[0,-I]] [[0,I],[-I,0]] [[I,0],[0,-I]]
                    = [[I,0],[0,-I]] [[0,-I],[-I,0]]
                    = [[0,-I],[I,0]]
                    = -J.  QED.

    >>> verify_anti_commutativity(1)
    True
    >>> verify_anti_commutativity(5)
    True
    >>> verify_anti_commutativity(50)
    True
    """
    J = verdier_symplectic_form(n)
    sigma = verdier_involution(n)
    return np.allclose(sigma.T @ J @ sigma, -J)


def lagrangian_subspaces(n: int) -> Tuple[np.ndarray, np.ndarray]:
    r"""The two complementary Lagrangian subspaces.

    V+ = span of first n standard basis vectors (code subspace, Q_g(A))
    V- = span of last n standard basis vectors (error space, Q_g(A^!))

    Both are isotropic under J, and each is n-dimensional in C^{2n},
    so both are Lagrangian (maximally isotropic).

    >>> Vp, Vm = lagrangian_subspaces(3)
    >>> Vp.shape
    (6, 3)
    >>> Vm.shape
    (6, 3)
    """
    I_2n = np.eye(2 * n)
    Vp = I_2n[:, :n]   # columns 0..n-1
    Vm = I_2n[:, n:]    # columns n..2n-1
    return Vp, Vm


def verify_isotropy(n: int) -> Dict:
    r"""Verify isotropy of both Lagrangian subspaces.

    For V+ (code): V+^T J V+ = 0  (n x n zero matrix)
    For V- (error): V-^T J V- = 0  (n x n zero matrix)
    Cross-pairing: V+^T J V- = I_n (perfect pairing, nondegenerate)

    >>> result = verify_isotropy(3)
    >>> result['code_isotropic']
    True
    >>> result['error_isotropic']
    True
    >>> result['cross_pairing_nondegenerate']
    True
    """
    J = verdier_symplectic_form(n)
    Vp, Vm = lagrangian_subspaces(n)

    iso_code = Vp.T @ J @ Vp      # should be zero
    iso_error = Vm.T @ J @ Vm      # should be zero
    cross = Vp.T @ J @ Vm          # should be I_n

    code_iso = bool(np.max(np.abs(iso_code)) < 1e-14)
    error_iso = bool(np.max(np.abs(iso_error)) < 1e-14)
    cross_nondeg = bool(np.max(np.abs(cross - np.eye(n))) < 1e-14)

    return {
        'n': n,
        'dim_total': 2 * n,
        'dim_code': n,
        'dim_error': n,
        'code_isotropic': code_iso,
        'error_isotropic': error_iso,
        'cross_pairing_nondegenerate': cross_nondeg,
        'code_rate': Fraction(1, 2),
    }


# ===========================================================================
# 2. PATH 1: VERDIER ANTI-INVOLUTION PROOF
# ===========================================================================

def path1_verdier_proof(n: int) -> Dict:
    r"""Verdier isotropy plus scalar-line KL scope.

    The proof proceeds in three steps:

    Step 1: sigma^T J sigma = -J (anti-commutativity, verified above).

    Step 2: For v, w in V+ (eigenvalue +1 of sigma):
      <v,w>_D = v^T J w = (sigma v)^T J (sigma w) = v^T (sigma^T J sigma) w
             = v^T (-J) w = -<v,w>_D
      => <v,w>_D = 0.  (Isotropy of V+.)
      Same argument for V-.

    Step 3: On the one-dimensional scalar conformal-block line (the
      kappa projection), the KL condition P_C E^dag E P_C = c(E) P_C
      is automatic: any operator restricted to a 1D space is a scalar.

    For the full complementarity complex, and in particular for
    higher-dimensional conformal-block spaces, the full KL condition
    requires the physical inner product, code projector, and error
    *-algebra.  Verdier isotropy does not supply those data.

    Multi-path verification: we test the algebraic identity
    sigma^T J sigma = -J for multiple dimensions, and verify KL
    for random errors on 1D codes.

    >>> result = path1_verdier_proof(3)
    >>> result['anti_commutativity']
    True
    >>> result['isotropy_proved']
    True
    >>> result['kl_genus_1']
    True
    """
    # Step 1
    anti_comm = verify_anti_commutativity(n)

    # Step 2
    iso = verify_isotropy(n)

    # Step 3: KL for 1D code (genus 1)
    # Any operator on a 1D space is proportional to the projector.
    # P_C E^dag E P_C = <psi| E^dag E |psi> P_C = c(E) P_C.
    kl_g1 = True
    rng = np.random.RandomState(42)
    psi = rng.randn(2) + 1j * rng.randn(2)
    psi = psi / np.linalg.norm(psi)
    P_C = np.outer(psi, psi.conj())

    kl_violations = 0
    n_tests = 50
    for _ in range(n_tests):
        E = rng.randn(2, 2) + 1j * rng.randn(2, 2)
        EdagE = E.conj().T @ E
        lhs = P_C @ EdagE @ P_C
        c_E = np.trace(lhs @ P_C) / np.trace(P_C @ P_C)
        residual = np.max(np.abs(lhs - c_E * P_C))
        if residual > 1e-10:
            kl_violations += 1
            kl_g1 = False

    return {
        'path': 'Verdier anti-involution',
        'reference': 'prop:hc-knill-laflamme (holographic_codes_koszul.tex)',
        'anti_commutativity': anti_comm,
        'isotropy_proved': iso['code_isotropic'] and iso['error_isotropic'],
        'cross_pairing': iso['cross_pairing_nondegenerate'],
        'kl_genus_1': kl_g1,
        'kl_genus_1_tests': n_tests,
        'kl_genus_1_violations': kl_violations,
        'automatic_kl_scope': 'one-dimensional scalar conformal-block line',
        'full_hilbert_kl_proved': False,
        'isotropy_is_hilbert_kl': False,
        'requires_physical_data': (
            'Hermitian inner product, code projector, and physical error *-algebra'
        ),
        'mechanism': (
            'sigma^T J sigma = -J => eigenspaces isotropic. '
            'On a genus-1 scalar conformal-block line: dim C = 1 '
            '=> KL automatic. '
            'For the full or higher-dimensional complex: physical KL '
            'requires a Hermitian inner product and error *-algebra.'
        ),
    }


# ===========================================================================
# 3. PATH 2: LAGRANGIAN GEOMETRY PROOF
# ===========================================================================

def shifted_symplectic_degree(g: int) -> int:
    r"""Shifted symplectic degree for genus g.

    The ambient complex C_g(A) carries a (-(3g-3))-shifted symplectic
    structure from the modular operad on M_g,n.

    At genus 1: shift = 0 (ordinary symplectic).
    At genus 2: shift = -3.
    At genus g: shift = -(3g-3).

    >>> shifted_symplectic_degree(1)
    0
    >>> shifted_symplectic_degree(2)
    -3
    >>> shifted_symplectic_degree(3)
    -6
    """
    return -(3 * g - 3)


def lagrangian_dimension_check(n: int) -> Dict:
    r"""Verify the Lagrangian dimension condition.

    A Lagrangian subspace L of a 2n-dimensional symplectic space
    satisfies dim L = n = (1/2) dim V.  This is the MAXIMUM
    dimension of an isotropic subspace: Lagrangian = maximally
    isotropic.

    The code rate k/n = dim(L)/dim(V) = 1/2 is the maximum
    achievable by a Lagrangian (symplectic self-dual) code.

    For comparison:
      - Stabilizer codes: rate can be 0 to 1
      - CSS codes: rate depends on the two classical codes
      - Lagrangian codes: rate = 1/2 ALWAYS

    >>> result = lagrangian_dimension_check(5)
    >>> result['rate']
    Fraction(1, 2)
    >>> result['maximally_isotropic']
    True
    """
    J = verdier_symplectic_form(n)
    Vp, _ = lagrangian_subspaces(n)

    # Check isotropy
    iso = Vp.T @ J @ Vp
    isotropic = bool(np.max(np.abs(iso)) < 1e-14)

    # Check dimension: any isotropic subspace has dim <= n
    # Lagrangian <=> isotropic AND dim = n
    dim_code = Vp.shape[1]
    dim_ambient = 2 * n
    maximally_isotropic = isotropic and (dim_code == n)

    return {
        'dim_ambient': dim_ambient,
        'dim_code': dim_code,
        'rate': Fraction(dim_code, dim_ambient),
        'isotropic': isotropic,
        'maximally_isotropic': maximally_isotropic,
        'lagrangian': maximally_isotropic,
    }


def lagrangian_projection_not_kl_counterexample() -> Dict:
    r"""Finite countermodel: symplectic projection is not KL recovery.

    This is the finite-dimensional model in
    Proposition prop:hc-projection-not-kl.  Let

      V = C e_1 + C e_2 + C f_1 + C f_2,
      C = <e_1, e_2>,  E = <f_1, f_2>,

    with the standard Verdier symplectic form pairing e_i with f_i and
    vanishing on C x C and E x E.  The operator

      T(e_1) = e_1,  T(e_2) = 2 e_2,  T(f_i) = 0

    preserves the code summand and has no leakage into E.  The
    symplectic projection along E therefore recovers the code component.
    But for the standard Hermitian form,

      P_C T^dag T P_C = diag(1, 4)

    on C, not a scalar multiple of P_C.  Thus Lagrangian projection and
    Verdier isotropy do not imply the Hilbert-space KL condition.

    >>> result = lagrangian_projection_not_kl_counterexample()
    >>> result['preserves_code_summand']
    True
    >>> result['kl_satisfied']
    False
    """
    n = 2
    J = verdier_symplectic_form(n)
    Vp, _ = lagrangian_subspaces(n)

    P_C = np.zeros((2 * n, 2 * n), dtype=float)
    P_C[:n, :n] = np.eye(n)

    error = np.diag([1.0, 2.0, 0.0, 0.0])
    compression = P_C @ error.T @ error @ P_C
    code_block = compression[:n, :n]

    scalar = np.trace(code_block) / n
    scalar_residual = np.max(np.abs(code_block - scalar * np.eye(n)))
    leakage_block = error[n:, :n]

    return {
        'reference': 'prop:hc-projection-not-kl (holographic_codes_koszul.tex)',
        'dim_ambient': 2 * n,
        'dim_code': n,
        'verdier_isotropy': bool(np.max(np.abs(Vp.T @ J @ Vp)) < 1e-14),
        'preserves_code_summand': bool(np.max(np.abs(leakage_block)) < 1e-14),
        'symplectic_projection_removes_leakage': True,
        'compression_diagonal': tuple(float(x) for x in np.diag(code_block)),
        'best_scalar': float(scalar),
        'scalar_residual': float(scalar_residual),
        'is_scalar_on_code': bool(scalar_residual < 1e-14),
        'kl_satisfied': bool(scalar_residual < 1e-14),
        'failure_mode': (
            'Logical action inside the code is non-scalar even though the '
            'operator preserves the Lagrangian summand.'
        ),
    }


def path2_lagrangian_proof(n: int, g: int = 1) -> Dict:
    r"""Lagrangian prerequisite in the shifted symplectic space.

    The proof:

    1. C_g(A) = R Gamma(M_g_bar, Z_ch^der(A)) carries a
       (-(3g-3))-shifted symplectic form omega, where Z_ch^der(A) is
       the bulk/derived centre.

    2. Q_g(A) is Lagrangian in (C_g(A), omega):
       (a) omega|_{Q_g(A)} = 0 (isotropy)
       (b) dim Q_g(A) = (1/2) dim C_g(A) (half-dimensional)

    3. The KL condition <psi_i|E^dag E|psi_j> = C_{ab} delta_{ij}
       does not follow from isotropy alone.  Isotropy says
       omega(v, w) = 0 for v,w in Q_g(A); KL is a Hermitian
       compression identity for a specified physical error algebra.

    4. The finite-window Lagrangian rate k/n = 1/2 is the maximum
       isotropic rate in this symplectic model.

    5. At genus 1, the shifted symplectic degree is 0 (ordinary
       symplectic geometry).  The Lagrangian condition reduces to
       the standard isotropy condition v^T J w = 0.

    >>> result = path2_lagrangian_proof(3, g=1)
    >>> result['lagrangian_verified']
    True
    >>> result['lagrangian_prerequisite']
    True
    >>> result['kl_from_isotropy']
    False
    >>> result['code_rate']
    Fraction(1, 2)
    """
    shift = shifted_symplectic_degree(g)
    lag = lagrangian_dimension_check(n)
    iso = verify_isotropy(n)

    return {
        'path': 'Lagrangian geometry',
        'reference': 'thm:hc-symplectic-code (holographic_codes_koszul.tex)',
        'genus': g,
        'shifted_symplectic_degree': shift,
        'lagrangian_verified': lag['lagrangian'],
        'isotropy_verified': iso['code_isotropic'] and iso['error_isotropic'],
        'half_dimensional': lag['rate'] == Fraction(1, 2),
        'cross_pairing': iso['cross_pairing_nondegenerate'],
        'lagrangian_prerequisite': lag['isotropic'],
        'kl_from_isotropy': False,
        'full_hilbert_kl_proved': False,
        'counterexample_available': True,
        'requires_physical_data': (
            'Hermitian inner product, code projector, and physical error *-algebra'
        ),
        'code_rate': lag['rate'],
        'mechanism': (
            f'Q_g(A) is Lagrangian in the {shift}-shifted symplectic space C_g(A). '
            'Lagrangian isotropy omega(v,w) = 0 is the Verdier-isotropic '
            'prerequisite. It does not imply the Hilbert-space KL '
            'compression identity. Code rate = 1/2 on finite '
            'Lagrangian windows.'
        ),
    }


# ===========================================================================
# 4. PATH 3: SHADOW DEPTH = FORMAL MC SLOTS
# ===========================================================================

SHADOW_DEPTH_TABLE = {
    'heisenberg': {'class': 'G', 'r_max': 2, 'channels': 0},
    'lattice': {'class': 'G', 'r_max': 2, 'channels': 0},
    'affine': {'class': 'L', 'r_max': 3, 'channels': 1},
    'betagamma': {'class': 'C', 'r_max': 4, 'channels': 2},
    'virasoro': {'class': 'M', 'r_max': float('inf'), 'channels': float('inf')},
}


def mc_redundancy_at_arity(r: int) -> int:
    r"""Number of formal non-scalar MC slots at arity r.

    The MC equation D Theta + (1/2)[Theta, Theta] = 0 at arity r
    expresses Theta_r in terms of lower-arity data Theta_{<r}:

      d_2(Theta_r) = - (1/2) sum_{i+j=r} [Theta_i, Theta_j] - ...

    Each such relation is one formal slot: the arity-r shadow is
    controlled by lower-arity data up to obstruction and gauge classes.
    A Hilbert-space correction channel requires a physical error model.

    Channels = r - 2  (arity 2 = kappa is the first non-trivial component).

    >>> mc_redundancy_at_arity(2)
    0
    >>> mc_redundancy_at_arity(3)
    1
    >>> mc_redundancy_at_arity(4)
    2
    >>> mc_redundancy_at_arity(10)
    8
    """
    if r < 2:
        return 0
    return r - 2


def path3_shadow_depth_proof(family: str) -> Dict:
    r"""Formal shadow-slot count from the MC obstruction tower.

    The shadow obstruction tower Theta_A^{<=r} satisfies the MC equation
    at each arity.  The MC equation at arity r determines Theta_r from
    lower-arity data, providing one formal non-scalar slot per arity
    after a gauge convention or contraction is fixed
    (thm:hc-shadow-redundancy).

    Class G (r_max=2): 0 non-scalar slots
    Class L (r_max=3): 1 non-scalar slot
    Class C (r_max=4): 2 non-scalar slots
    Class M (r_max=inf): countably many slots, convergent for rho < 1

    The scalar tower begins at arity 2.  No Hilbert-space code-distance
    formula follows from this datum alone.

    Multi-path verification: compare shadow depth from the family
    classification with the formal MC slot count.

    >>> result = path3_shadow_depth_proof('heisenberg')
    >>> result['redundancy_channels']
    0
    >>> result['arity_distance']
    2

    >>> result = path3_shadow_depth_proof('virasoro')
    >>> result['shadow_class']
    'M'
    """
    cls = shadow_depth_class(family)
    r_max = entanglement_correction_depth(family)

    if cls == 'G':
        channels = 0
    elif cls == 'L':
        channels = 1
    elif cls == 'C':
        channels = 2
    else:
        channels = -1  # infinite

    # Arity filtration distance: always 2
    arity_distance = 2

    # Verify: channels = r_max - 2 for finite classes
    if cls in ('G', 'L', 'C'):
        channels_from_rmax = r_max - 2
        consistency = (channels == channels_from_rmax)
    else:
        consistency = True  # infinite case

    return {
        'path': 'Shadow depth = formal MC slots',
        'reference': 'thm:hc-shadow-redundancy (holographic_codes_koszul.tex)',
        'family': family,
        'shadow_class': cls,
        'r_max': r_max,
        'redundancy_channels': channels,
        'formal_shadow_slots': channels,
        'arity_distance': arity_distance,
        'channels_consistent': consistency,
        'hilbert_code_distance_determined': False,
        'requires_physical_error_model': True,
        'mechanism': (
            f'MC equation at arity r controls Theta_r from Theta_{{<r}} '
            'up to obstruction and gauge classes. '
            f'Class {cls}: {channels} formal non-scalar slot(s). '
            f'The scalar tower starts at arity {arity_distance}; code '
            'distance needs a physical error model.'
        ),
    }


# ===========================================================================
# 5. PATH 4: BAR-COBAR ADJUNCTION = BOUNDARY RECOVERY
# ===========================================================================

def bar_cobar_recovery_structure(family: str, h_max: int = 6) -> Dict:
    r"""Bar-cobar adjunction as exact boundary-algebra recovery.

    Encoding: B: A -> B(A)  (bar construction into the bar coalgebra)
    Decoding: Omega: B(A) -> A  (cobar construction, the recovery map)

    Theorem B (bar-cobar inversion on Koszul locus):
      Omega(B(A)) ~ A  (quasi-isomorphism)

    This is exact algebraic boundary recovery:
      - Encoding: maps algebra A into the bar coalgebra B(A)
      - Decoding: recovers A from B(A) via the cobar functor
      - Exactness: the round-trip is a quasi-isomorphism (= exact
        recovery up to homotopy)

    It is not, by itself, a Hilbert-space QEC recovery theorem or a
    physical bulk reconstruction theorem.  Those require the physical
    BRST/derived-centre comparison and a Hilbert-space error model.

    IMPORTANT (AP25): B(A) is a coalgebra, not an algebra-level dual.
    Its bar cohomology is A^i = H^*(B(A)).  The Koszul dual A^! is
    obtained from A^i by Verdier/linear duality under finite-type or
    completed hypotheses.  Omega(B(A)) = A is inversion: it recovers
    the original algebra A, not A^!.

    The 12 Koszulness characterizations (K1-K12) are algebraic
    criteria for boundary recovery to be exact.

    >>> result = bar_cobar_recovery_structure('heisenberg')
    >>> result['exact_recovery']
    True
    >>> result['is_koszul']
    True
    """
    # All standard families are chirally Koszul
    is_koszul = True

    return {
        'path': 'Bar-cobar adjunction = boundary recovery',
        'reference': 'Theorem B (bar_cobar_adjunction_inversion.tex)',
        'family': family,
        'encoding_functor': 'B (bar construction)',
        'decoding_functor': 'Omega (cobar construction)',
        'round_trip': 'Omega(B(A)) ~ A (quasi-isomorphism)',
        'bar_object': AP25_OBJECT_CHAIN['bar_object'],
        'bar_cohomology_object': AP25_OBJECT_CHAIN['bar_cohomology'],
        'koszul_dual_source': AP25_OBJECT_CHAIN['koszul_dual'],
        'derived_centre_object': AP25_OBJECT_CHAIN['derived_centre'],
        'derived_center_object': AP25_OBJECT_CHAIN['derived_centre'],
        'ap25_object_chain': dict(AP25_OBJECT_CHAIN),
        'is_koszul': is_koszul,
        'exact_recovery': is_koszul,
        'exact_boundary_recovery': is_koszul,
        'physical_qec_recovery_proved': False,
        'physical_bulk_equivalence_proved': False,
        'requires_brst_derived_centre_comparison': True,
        'recovery_scope': 'boundary algebra quasi-isomorphism',
        'koszulness_characterizations': 12,
        'note_ap25': (
            'B(A) is a coalgebra; A^i = H^*(B(A)); A^! is obtained '
            'from A^i by Verdier/linear duality under finite-type or '
            'completed hypotheses. Omega(B(A)) = A is inversion, '
            'recovering A itself. Z_ch^der(A) is the bulk/derived centre.'
        ),
        'mechanism': (
            'Bar coalgebra = encoding. Cobar = decoding. '
            'Koszulness (Thm B) => Omega(B(A)) ~ A (exact boundary '
            'recovery). 12 Koszulness characterizations are algebraic '
            'bar-cobar criteria, not 12 physical KL equations.'
        ),
    }


def path4_barcobar_proof(family: str) -> Dict:
    r"""Boundary recovery from the bar-cobar adjunction (Theorems A + B).

    The proof:

    1. Theorem A: B -| Omega is an adjunction.
       The bar functor B: A -> B(A) maps the algebra to the bar
       coalgebra.
       The cobar functor Omega: C -> Omega(C) maps a coalgebra back.
       The unit eta: A -> Omega(B(A)) is the algebraic
       encoding-decoding map for boundary recovery.

    2. Theorem B: On the Koszul locus, eta is a quasi-isomorphism.
       This means Omega(B(A)) ~ A: the round-trip recovers the
       boundary algebra up to quasi-isomorphism.

    3. Koszulness is necessary and sufficient for boundary recovery:
       exact boundary recovery <=> bar-cobar unit is quasi-iso
       <=> A is Koszul.  The 12 Koszulness characterizations each
       provide an algebraic criterion for this boundary statement.

    4. The code subspace at genus g is Q_g(A) (one Lagrangian summand).
       The complementary summand is Q_g(A^!), where A^! is obtained
       from A^i = H^*(B(A)) by Verdier/linear duality under the
       finite-type or completed hypotheses.  Recovery proceeds by
       projecting along Q_g(A^!):
         pi_C: C_g(A) -> Q_g(A)  (Lagrangian projection).

    >>> result = path4_barcobar_proof('heisenberg')
    >>> result['exact_recovery']
    True
    >>> result['koszulness_iff_recovery']
    True
    """
    recovery = bar_cobar_recovery_structure(family)

    return {
        'path': 'Bar-cobar adjunction (Theorems A + B)',
        'reference': 'Theorems A, B (bar_cobar_adjunction_*.tex)',
        'family': family,
        'theorem_a': 'B -| Omega adjunction; B(A) is a coalgebra',
        'theorem_b': 'Omega(B(A)) ~ A on Koszul locus (inversion)',
        'exact_recovery': recovery['exact_recovery'],
        'exact_boundary_recovery': recovery['exact_boundary_recovery'],
        'physical_qec_recovery_proved': False,
        'physical_bulk_equivalence_proved': False,
        'koszulness_iff_recovery': True,
        'koszulness_iff_boundary_recovery': True,
        'recovery_map': 'pi_C: C_g(A) -> Q_g(A) (Lagrangian projection)',
        'ap25_object_chain': recovery['ap25_object_chain'],
        'mechanism': recovery['mechanism'],
    }


# ===========================================================================
# 6. EXPLICIT NUMERICAL VERIFICATION
# ===========================================================================

def explicit_kl_verification_1d(n_errors: int = 100, seed: int = 42) -> Dict:
    r"""Explicit KL verification for a 1D code in a 2D ambient space.

    For any 1D code subspace C in C^2, and any error operator E,
    the KL condition P_C E^dag E P_C = c(E) P_C holds trivially:
    any operator on a 1D space is a scalar multiple of the projector.

    We verify this numerically for n_errors random error operators.

    >>> result = explicit_kl_verification_1d(100)
    >>> result['kl_satisfied']
    True
    >>> result['max_residual'] < 1e-10
    True
    """
    rng = np.random.RandomState(seed)

    # Random unit code state
    psi = rng.randn(2) + 1j * rng.randn(2)
    psi = psi / np.linalg.norm(psi)
    P_C = np.outer(psi, psi.conj())

    max_residual = 0.0
    c_values = []

    for _ in range(n_errors):
        E = rng.randn(2, 2) + 1j * rng.randn(2, 2)
        EdagE = E.conj().T @ E
        lhs = P_C @ EdagE @ P_C
        # Extract scalar: c(E) = <psi| E^dag E |psi>
        c_E = (psi.conj() @ EdagE @ psi).real
        residual = np.max(np.abs(lhs - c_E * P_C))
        max_residual = max(max_residual, residual)
        c_values.append(c_E)

    return {
        'dim_ambient': 2,
        'dim_code': 1,
        'n_errors_tested': n_errors,
        'kl_satisfied': max_residual < 1e-10,
        'max_residual': max_residual,
        'c_values_all_nonneg': all(c >= -1e-14 for c in c_values),
        'mechanism': 'rank-1 projector: P E^dag E P = c(E) P automatic',
    }


def explicit_kl_verification_lagrangian(n: int, n_errors: int = 50,
                                         seed: int = 42) -> Dict:
    r"""Explicit KL for Lagrangian-preserving errors on n-dim code.

    For a Lagrangian code C = span(e_1, ..., e_n) in C^{2n}, an error
    E that preserves the Lagrangian decomposition has the block form
    E = [[A, 0], [0, D]].

    For such errors:
      P_C E^dag E P_C = [[A^dag A, 0], [0, 0]]

    The KL condition P_C E^dag E P_C = c(E) P_C requires
    A^dag A = c(E) I_n, i.e., A is a scalar times a unitary.

    We test with random scalar-unitary errors (the class of errors
    for which KL holds) and verify explicitly.

    >>> result = explicit_kl_verification_lagrangian(3, 50)
    >>> result['kl_satisfied']
    True
    """
    rng = np.random.RandomState(seed)

    # Projector onto code subspace (first n dimensions)
    P_C = np.zeros((2 * n, 2 * n))
    P_C[:n, :n] = np.eye(n)

    max_residual = 0.0
    n_success = 0

    for _ in range(n_errors):
        # Scalar * unitary on the code subspace
        A_rand = rng.randn(n, n) + 1j * rng.randn(n, n)
        U, _, Vh = np.linalg.svd(A_rand)
        scale = rng.exponential(1.0) + 0.1
        A_block = scale * (U @ Vh)

        # Block-diagonal error (Lagrangian-preserving)
        D_block = rng.randn(n, n) + 1j * rng.randn(n, n)
        E = np.block([[A_block, np.zeros((n, n))],
                       [np.zeros((n, n)), D_block]])

        EdagE = E.conj().T @ E
        lhs = P_C @ EdagE @ P_C
        c_E = scale ** 2
        expected = c_E * P_C
        residual = np.max(np.abs(lhs - expected))
        max_residual = max(max_residual, residual)
        if residual < 1e-8:
            n_success += 1

    return {
        'dim_ambient': 2 * n,
        'dim_code': n,
        'n_errors_tested': n_errors,
        'n_success': n_success,
        'kl_satisfied': n_success == n_errors,
        'max_residual': max_residual,
        'error_class': 'scalar-unitary on code subspace (Lagrangian-preserving)',
    }


def explicit_kl_off_diagonal(n: int, n_errors: int = 50,
                              seed: int = 42) -> Dict:
    r"""Verify the off-diagonal KL condition for multi-dimensional codes.

    The KL condition <psi_i| E_a^dag E_b |psi_j> = C_{ab} delta_{ij}
    requires the off-diagonal matrix elements to vanish:
    <psi_i| E_a^dag E_b |psi_j> = 0 for i != j.

    For scalar-unitary errors on a Lagrangian code, E^dag E = |c|^2 I_C,
    so off-diagonal entries vanish by orthonormality of the basis.

    >>> result = explicit_kl_off_diagonal(3, 30)
    >>> result['off_diag_vanish']
    True
    """
    rng = np.random.RandomState(seed)

    # Orthonormal basis for code subspace
    basis = np.eye(2 * n)[:, :n]  # n x (2n) columns -> (2n) x n

    max_off_diag = 0.0

    for _ in range(n_errors):
        # Scalar * unitary error on code block
        A_rand = rng.randn(n, n) + 1j * rng.randn(n, n)
        U, _, Vh = np.linalg.svd(A_rand)
        scale = rng.exponential(1.0) + 0.1
        A_block = scale * (U @ Vh)

        D_block = np.eye(n)
        E = np.block([[A_block, np.zeros((n, n))],
                       [np.zeros((n, n)), D_block]])

        EdagE = E.conj().T @ E

        # Compute <psi_i| EdagE |psi_j> for all i, j
        gram = basis.conj().T @ EdagE @ basis  # n x n

        # Off-diagonal entries should vanish
        off_diag = gram - np.diag(np.diag(gram))
        max_off = np.max(np.abs(off_diag))
        max_off_diag = max(max_off_diag, max_off)

        # Diagonal entries should all equal c(E) = scale^2
        diag_vals = np.diag(gram).real
        diag_spread = np.max(diag_vals) - np.min(diag_vals)
        if diag_spread > 1e-8:
            max_off_diag = max(max_off_diag, diag_spread)

    return {
        'dim_code': n,
        'n_errors_tested': n_errors,
        'max_off_diagonal': max_off_diag,
        'off_diag_vanish': max_off_diag < 1e-8,
        'kl_off_diagonal_verified': max_off_diag < 1e-8,
    }


# ===========================================================================
# 7. FOUR-PATH SYNTHESIS
# ===========================================================================

def verify_kl_four_paths(family: str = 'heisenberg', n: int = 3,
                          g: int = 1) -> Dict:
    r"""Four-path finite-scope verification around the KL boundary.

    Checks that the algebraic prerequisites, scalar-line KL, formal
    shadow slots, and bar-cobar boundary recovery are mutually
    consistent.  It deliberately does not assert the full Hilbert-space
    KL theorem.

    >>> result = verify_kl_four_paths('heisenberg', 3, 1)
    >>> result['all_paths_agree']
    True
    >>> result['num_paths']
    4
    """
    p1 = path1_verdier_proof(n)
    p2 = path2_lagrangian_proof(n, g)
    p3 = path3_shadow_depth_proof(family)
    p4 = path4_barcobar_proof(family)

    finite_scope_consistent = (
        p1['isotropy_proved'] and
        p1['kl_genus_1'] and
        p2['lagrangian_verified'] and
        p2['lagrangian_prerequisite'] and
        not p2['kl_from_isotropy'] and
        p3['channels_consistent'] and
        p4['exact_boundary_recovery']
    )

    return {
        'family': family,
        'genus': g,
        'dim_code': n,
        'path1_verdier': p1,
        'path2_lagrangian': p2,
        'path3_shadow_depth': p3,
        'path4_barcobar': p4,
        'all_paths_agree': finite_scope_consistent,
        'finite_scope_consistent': finite_scope_consistent,
        'full_hilbert_kl_proved': False,
        'physical_data_required': (
            'Hermitian inner product, code projector, physical error '
            '*-algebra, and BRST/derived-centre comparison for bulk claims'
        ),
        'num_paths': 4,
        'conclusion': (
            'Finite algebraic KL prerequisites and boundary recovery '
            'are mutually consistent; full Hilbert-space KL remains '
            'conditional on physical data'
            if finite_scope_consistent else 'DISAGREEMENT between finite-scope paths'
        ),
    }


# ===========================================================================
# 8. CROSS-FAMILY CENSUS
# ===========================================================================

def kl_family_census() -> Dict:
    r"""Finite-scope KL-boundary census across standard families.

    Checks the algebraic finite-scope data for each family.  Shadow
    depth remains a formal MC slot count, not a Hilbert-space distance.

    >>> census = kl_family_census()
    >>> all(v['all_paths_agree'] for v in census.values())
    True
    >>> all(v['code_rate'] == Fraction(1, 2) for v in census.values())
    True
    """
    families = {
        'heisenberg': {'class': 'G', 'r_max': 2},
        'affine': {'class': 'L', 'r_max': 3},
        'betagamma': {'class': 'C', 'r_max': 4},
        'virasoro': {'class': 'M', 'r_max': float('inf')},
    }

    census = {}
    for fam, expected in families.items():
        result = verify_kl_four_paths(fam, n=3, g=1)
        p3 = result['path3_shadow_depth']
        census[fam] = {
            'all_paths_agree': result['all_paths_agree'],
            'finite_scope_consistent': result['finite_scope_consistent'],
            'full_hilbert_kl_proved': False,
            'shadow_class': p3['shadow_class'],
            'redundancy_channels': p3['redundancy_channels'],
            'formal_shadow_slots': p3['formal_shadow_slots'],
            'hilbert_code_distance_determined': False,
            'arity_distance': p3['arity_distance'],
            'code_rate': Fraction(1, 2),
            'class_match': p3['shadow_class'] == expected['class'],
        }

    return census


# ===========================================================================
# 9. COMPLEMENTARITY KAPPA CONSTRAINT ON THE SCALAR/LAGRANGIAN SURFACE
# ===========================================================================

def complementarity_kl_constraint(c_val) -> Dict:
    r"""Complementarity constraint on the scalar/Lagrangian surface.

    For the Virasoro family:
      kappa(Vir_c) + kappa(Vir_{26-c}) = 13

    The scalar fraction kappa/(kappa + kappa') measures the relative
    scalar anomaly weight.  At the self-dual point c = 13 the scalar
    fraction is 1/2.

    The complementarity constraint imposes:
      - The Lagrangian windows have equal dimension
      - The combined code has rate 1/2
      - At c = 13: the code is self-dual (A = A^!)

    >>> result = complementarity_kl_constraint(Rational(13))
    >>> result['self_dual']
    True
    >>> result['code_fraction']
    1/2

    >>> result = complementarity_kl_constraint(Rational(1))
    >>> result['kappa_sum']
    13
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)
    total = kappa + kappa_dual  # = 13 always

    code_fraction = kappa / total if total != 0 else Rational(0)

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'kappa_sum': total,
        'kappa_sum_is_13': total == 13,
        'code_fraction': code_fraction,
        'scalar_fraction': code_fraction,
        'self_dual': c_val == 13,
        'code_rate': Fraction(1, 2),
        'full_hilbert_kl_proved': False,
    }


# ===========================================================================
# 10. SYMPY-BASED ALGEBRAIC VERIFICATION
# ===========================================================================

def sympy_verdier_isotropy(n: int) -> Dict:
    r"""Algebraic (exact) verification of Verdier isotropy.

    Using SymPy's Matrix class for exact computation (no floating point).

    The identity sigma^T J sigma = -J is verified EXACTLY.

    >>> result = sympy_verdier_isotropy(3)
    >>> result['anti_commutativity_exact']
    True
    >>> result['code_isotropy_exact']
    True
    """
    I_n = eye(n)
    Z_n = sym_zeros(n)

    J = Matrix([[Z_n, I_n], [-I_n, Z_n]])
    sigma = Matrix([[I_n, Z_n], [Z_n, -I_n]])

    # Anti-commutativity: sigma^T J sigma = -J
    product = sigma.T * J * sigma
    anti_comm = (product + J == sym_zeros(2 * n))

    # Code subspace basis: first n columns of I_{2n}
    Vp = eye(2 * n)[:, :n]

    # Isotropy: Vp^T J Vp = 0
    code_iso_matrix = Vp.T * J * Vp
    code_iso = (code_iso_matrix == sym_zeros(n))

    # Error subspace basis: last n columns
    Vm = eye(2 * n)[:, n:]
    error_iso_matrix = Vm.T * J * Vm
    error_iso = (error_iso_matrix == sym_zeros(n))

    # Cross-pairing: Vp^T J Vm = I_n
    cross = Vp.T * J * Vm
    cross_is_identity = (cross == I_n)

    return {
        'n': n,
        'anti_commutativity_exact': bool(anti_comm),
        'code_isotropy_exact': bool(code_iso),
        'error_isotropy_exact': bool(error_iso),
        'cross_pairing_exact': bool(cross_is_identity),
    }


def sympy_kl_scalar_automatic(dim: int = 1) -> Dict:
    r"""Algebraic proof that KL is automatic for 1D code.

    For a 1D code subspace C = span(|psi>), the projector
    P_C = |psi><psi|.  For any operator M:

      P_C M P_C = |psi><psi| M |psi><psi|
               = <psi|M|psi> |psi><psi|
               = c(M) P_C

    where c(M) = <psi|M|psi>.  This is EXACTLY the KL condition
    with the scalar c(E^dag E) = <psi|E^dag E|psi>.

    >>> result = sympy_kl_scalar_automatic()
    >>> result['kl_automatic']
    True
    """
    # Symbolic: |psi> = (a, b)^T, arbitrary
    from sympy import symbols, conjugate
    a, b = symbols('a b')
    m11, m12, m21, m22 = symbols('m11 m12 m21 m22')

    psi = Matrix([a, b])
    M = Matrix([[m11, m12], [m21, m22]])

    # P_C = |psi><psi^*|
    # P_C M P_C = |psi> <psi^*| M |psi> <psi^*|
    #           = (<psi^*|M|psi>) |psi><psi^*|
    #           = c(M) P_C

    # <psi^*|M|psi> is a scalar
    psi_dag = Matrix([conjugate(a), conjugate(b)]).T
    scalar = psi_dag * M * psi  # 1x1 matrix
    # c(M) = scalar[0, 0]

    # This is always a scalar, regardless of M.
    # The proof is purely algebraic: rank-1 projector * anything * rank-1 projector
    # = scalar * rank-1 projector.

    return {
        'dim_code': 1,
        'kl_automatic': True,
        'proof': (
            'For dim C = 1: P_C M P_C = <psi|M|psi> P_C for all M. '
            'This is the KL condition with c(E^dag E) = <psi|E^dag E|psi>.'
        ),
        'scalar_expression': str(scalar),
    }


# ===========================================================================
# 11. ENTANGLEMENT WEDGE INTERPRETATION
# ===========================================================================

def entanglement_wedge_from_bar(family: str, c_val=None) -> Dict:
    r"""Scalar entropy coefficient and bar-cobar boundary recovery.

    The bar complex B(A) is the factorization coalgebra encoding A.
    A physical entanglement wedge requires additional open/closed
    realization data: a BRST bulk, a comparison map to the chiral
    derived centre, and a physical Hilbert-space reconstruction theorem.

    For a chirally Koszul algebra, Omega(B(A)) ~ A is exact recovery
    of the boundary algebra.  It does not by itself prove a maximal
    physical entanglement wedge.

    The area term Area/(4G_N) in the RT formula is:
      Area/(4G_N) = (2 kappa / 3) log(L/epsilon)

    where kappa = c/2 for Virasoro.

    >>> result = entanglement_wedge_from_bar('virasoro', Rational(26))
    >>> result['rt_coefficient']
    26/3
    """
    if c_val is not None:
        c_val = Rational(c_val)
        kappa = kappa_virasoro(c_val)
    else:
        kappa = STANDARD_KAPPAS.get(family.lower() + '_1', Rational(1))

    rt_coeff = Rational(2) * kappa / 3

    return {
        'family': family,
        'kappa': kappa,
        'rt_coefficient': rt_coeff,
        'scalar_entropy_coefficient': rt_coeff,
        'wedge_maximal': False,
        'physical_entanglement_wedge_proved': False,
        'bar_cobar_boundary_recovery': True,
        'exact_reconstruction': False,
        'requires_brst_derived_centre_comparison': True,
        'bar_object': AP25_OBJECT_CHAIN['bar_object'],
        'bulk_derived_centre': AP25_OBJECT_CHAIN['derived_centre'],
        'bulk_derived_center': AP25_OBJECT_CHAIN['derived_centre'],
        'mechanism': (
            'Bar coalgebra = support of B(A) restricted to region. '
            'Bulk datum = Z_ch^der(A), the chiral derived centre. '
            'Cobar = boundary-algebra reconstruction. Physical '
            'entanglement-wedge and RT claims require an additional '
            'BRST/derived-centre comparison and gravitational input.'
        ),
    }


# ===========================================================================
# 12. GENUS-DEPENDENT CODE PARAMETERS
# ===========================================================================

def genus_dependent_code_dimension(g: int) -> Dict:
    r"""Scalar-line code dimension as a function of genus.

    At genus g, the ambient complex C_g(A) has dimension
    determined by the Euler characteristic of M_g_bar and the
    central data of A.

    At genus 1, on the scalar projection: dim C_1(A) = 2
    (1D code line + 1D complementary line).
    At genus 2: dim C_2(A) = 2 * dim Q_2(A), where
      dim Q_2(A) depends on the algebra.

    The finite-window Lagrangian rate is 1/2.

    For the scalar level (the kappa projection):
      dim Q_g^scalar(A) = 1 for all g >= 1.
    This is a 1D scalar line, not the full conformal-block complex.

    >>> result = genus_dependent_code_dimension(1)
    >>> result['dim_code_scalar']
    1
    >>> result['code_rate']
    Fraction(1, 2)
    """
    # At the scalar level, dim Q_g^scalar = 1 for all g
    dim_code_scalar = 1
    dim_ambient_scalar = 2
    rate = Fraction(1, 2)

    # Shifted symplectic degree
    shift = shifted_symplectic_degree(g)

    return {
        'genus': g,
        'shifted_symplectic_degree': shift,
        'dim_code_scalar': dim_code_scalar,
        'dim_ambient_scalar': dim_ambient_scalar,
        'code_rate': rate,
        'kl_automatic_at_scalar': True,  # dim 1 => automatic
        'full_complex_dimension_computed': False,
        'full_hilbert_kl_proved': False,
    }


def genus_tower_kl_status() -> List[Dict]:
    r"""KL status at each genus level.

    Genus 1: KL automatic on the one-dimensional scalar line.
    Genus >= 2: physical KL requires a Hilbert completion and error
                *-algebra.  Lagrangian isotropy remains algebraic.

    >>> tower = genus_tower_kl_status()
    >>> tower[0]['kl_status']
    'automatic on scalar line'
    >>> tower[1]['kl_status']
    'requires physical error model'
    """
    tower = []
    for g in range(1, 6):
        if g == 1:
            status = 'automatic on scalar line'
            reason = (
                'dim Q_1^scalar(A) = 1 => rank-1 projector gives KL '
                'on the scalar line; the full complex is not thereby one-dimensional'
            )
        else:
            status = 'requires physical error model'
            reason = (
                f'Q_{g}(A) is a Lagrangian summand in the algebraic '
                'surface; physical KL requires Hermitian structure and '
                'a specified error *-algebra.'
            )

        tower.append({
            'genus': g,
            'shifted_degree': shifted_symplectic_degree(g),
            'kl_status': status,
            'reason': reason,
            'code_rate': Fraction(1, 2),
            'full_hilbert_kl_proved': False,
        })

    return tower
