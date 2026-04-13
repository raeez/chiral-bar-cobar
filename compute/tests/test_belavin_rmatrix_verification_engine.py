r"""Tests for the Belavin elliptic r-matrix verification engine.

Three verification programmes with 30+ tests:

Programme 1 -- DEGENERATION (6 tests):
    tau -> i*infinity recovers the trigonometric r-matrix (XXZ).
    The further limit z -> 0 recovers the rational r-matrix Omega/z.
    Verified component-by-component via individual weight functions.

Programme 2 -- CYBE (7 tests):
    Classical Yang-Baxter equation at tau = i (square lattice),
    general tau, pure imaginary tau, and multiple spectral parameter
    configurations.  All at machine precision (~1e-8 relative).

Programme 3 -- CASIMIR EIGENVALUES (4 tests):
    Omega on Sym^2(C^2) = V_1: eigenvalue +1/2.
    Omega on wedge^2(C^2) = V_0: eigenvalue -3/2.
    Verified via direct 4x4 matrix computation and representation theory.

Supporting verifications (13+ tests):
    Jacobi triple product, theta oddness, quasi-periodicity,
    weight function residues, XYZ anisotropy, skew-symmetry,
    pole structure, AP126/AP141 k=0 vanishing, sl_2 commutation
    relations, Omega = Pauli sum, Casimir element eigenvalue,
    square lattice symmetry, level linearity.

Ground truth:
    - Belavin (1981), Belavin-Drinfeld (1982), Sklyanin (1982)
    - Bernard (1988), Felder (1994)
    - AP19: bar kernel absorbs a pole
    - AP126: level prefix mandatory; k=0 => r=0
    - C9: affine KM r-matrix conventions
    - kappa(sl_2, k) = 3(k+2)/4
"""

import pytest
import numpy as np

import importlib.util
import os

# Load module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'belavin_rmatrix_verification_engine',
    os.path.join(_lib_dir, 'belavin_rmatrix_verification_engine.py'),
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# Standard tau values for tests
TAU_SQUARE = 1j               # Square lattice (Z_4 symmetry)
TAU_GENERAL = 0.3 + 0.8j      # Generic tau with Re(tau) != 0
TAU_PURE = 1.5j               # Pure imaginary, non-square


# ============================================================
# Programme 1: DEGENERATION (elliptic -> trigonometric -> rational)
# ============================================================

class TestDegenerationToTrigonometric:
    """Verify elliptic r-matrix -> trigonometric as Im(tau) -> infinity."""

    def test_convergence_to_trigonometric(self):
        """At generic z, r^ell -> r^trig with exponential convergence in Im(tau).

        # VERIFIED:
        # [DC] Direct numerical computation of theta function series
        # [LT] Theta function asymptotics: theta_3,4(z|tau) -> 1 + O(q)
        """
        result = _mod.verify_degeneration_to_trigonometric(0.2 + 0.1j)
        assert result['passed'], (
            f"Degeneration to trigonometric failed: final error = {result['final_error']:.2e}"
        )

    def test_monotone_convergence(self):
        """Error decreases monotonically as Im(tau) increases."""
        result = _mod.verify_degeneration_to_trigonometric(0.15 + 0.08j)
        assert result['monotone_decreasing'], (
            f"Non-monotone convergence: errors = {result['errors']}"
        )

    def test_degeneration_to_rational(self):
        """Double limit (Im(tau) -> inf, z -> 0) gives Omega/z.

        # VERIFIED:
        # [DC] z * r^ell(z) -> Omega at small z with O(|z|^2) convergence
        # [LT] pi*cot(pi*z) = 1/z + O(z^2), pi/sin(pi*z) = 1/z + O(z^2)
        """
        result = _mod.verify_degeneration_to_rational()
        assert result['passed'], (
            f"Degeneration to rational failed: final error = {result['final_error']:.2e}"
        )

    def test_convergence_rate_quadratic(self):
        """Convergence rate z*r -> Omega is quadratic in |z|."""
        result = _mod.verify_degeneration_to_rational()
        exponents = result['convergence_exponents']
        # All exponents should be close to 2 (O(|z|^2) convergence)
        for exp in exponents:
            assert 1.5 < exp < 2.5, f"Convergence exponent {exp:.2f} not near 2"

    def test_componentwise_degeneration(self):
        """Each w_a -> 1/z at small z and large Im(tau)."""
        result = _mod.verify_degeneration_componentwise(
            0.005 + 0.003j, tau_im=50.0)
        assert result['all_passed'], (
            f"Componentwise degeneration failed: {result['channel_errors']}"
        )

    def test_trigonometric_limit_different_z(self):
        """Trigonometric degeneration holds at different spectral parameters."""
        for z in [0.1 + 0.3j, 0.4 + 0.05j, -0.2 + 0.15j]:
            result = _mod.verify_degeneration_to_trigonometric(z)
            assert result['passed'], (
                f"Trigonometric degeneration failed at z={z}: "
                f"final error = {result['final_error']:.2e}"
            )


# ============================================================
# Programme 2: CYBE
# ============================================================

class TestClassicalYangBaxterEquation:
    """Verify the classical Yang-Baxter equation for the Belavin r-matrix."""

    def test_cybe_square_lattice(self):
        """CYBE at tau = i (the square lattice).

        # VERIFIED:
        # [DC] Direct 8x8 matrix computation, residual < 1e-8
        # [LT] Belavin (1981), Thm 1: r^ell satisfies CYBE for all tau in H
        """
        result = _mod.verify_cybe(
            0.1 + 0.2j, 0.3 + 0.1j, -0.15 + 0.25j, tau=TAU_SQUARE)
        assert result['passed'], (
            f"CYBE at tau=i failed: relative = {result['relative']:.2e}"
        )

    def test_cybe_general_tau(self):
        """CYBE at a generic tau with non-zero real part."""
        result = _mod.verify_cybe(
            0.1 + 0.2j, 0.3 + 0.1j, -0.15 + 0.25j, tau=TAU_GENERAL)
        assert result['passed'], (
            f"CYBE at tau={TAU_GENERAL} failed: relative = {result['relative']:.2e}"
        )

    def test_cybe_pure_imaginary_tau(self):
        """CYBE at pure imaginary tau (rectangular lattice)."""
        result = _mod.verify_cybe(
            0.1 + 0.2j, 0.3 + 0.1j, -0.15 + 0.25j, tau=TAU_PURE)
        assert result['passed'], (
            f"CYBE at tau={TAU_PURE} failed: relative = {result['relative']:.2e}"
        )

    def test_cybe_large_imaginary_tau(self):
        """CYBE at large Im(tau) (near trigonometric limit)."""
        result = _mod.verify_cybe(
            0.1 + 0.2j, 0.3 + 0.1j, -0.15 + 0.25j, tau=5j)
        assert result['passed'], (
            f"CYBE at tau=5i failed: relative = {result['relative']:.2e}"
        )

    def test_cybe_different_spectral_params_1(self):
        """CYBE with a different set of spectral parameters."""
        result = _mod.verify_cybe(
            0.05 + 0.1j, 0.2 + 0.05j, -0.1 + 0.15j, tau=TAU_SQUARE)
        assert result['passed'], (
            f"CYBE (params 2) failed: relative = {result['relative']:.2e}"
        )

    def test_cybe_different_spectral_params_2(self):
        """CYBE with yet another set of spectral parameters."""
        result = _mod.verify_cybe(
            0.3 + 0.4j, 0.1 + 0.2j, 0.2 + 0.3j, tau=TAU_SQUARE)
        assert result['passed'], (
            f"CYBE (params 3) failed: relative = {result['relative']:.2e}"
        )

    def test_cybe_with_level(self):
        """CYBE holds at level k != 1 (linearity: [kr, kr] = k^2 [...] = 0).

        # VERIFIED:
        # [DC] CYBE is homogeneous degree 2 in r, so scaling by k preserves it
        # [SY] Linearity of the commutator bracket
        """
        result = _mod.verify_cybe(
            0.1 + 0.2j, 0.3 + 0.1j, -0.15 + 0.25j,
            tau=TAU_SQUARE, k=3.5)
        assert result['passed'], (
            f"CYBE at k=3.5 failed: relative = {result['relative']:.2e}"
        )


# ============================================================
# Programme 3: CASIMIR EIGENVALUES
# ============================================================

class TestCasimirEigenvalues:
    """Verify Casimir tensor eigenvalues on Sym^2 and wedge^2 of C^2."""

    def test_casimir_on_sym2(self):
        """Omega eigenvalue on Sym^2(C^2) = V_1 is +1/2.

        # VERIFIED:
        # [DC] Direct 4x4 matrix computation
        # [LT] Omega = (C_2^tot - 2*C_2(1/2))/2; C_2(1) = 4, C_2(1/2) = 3/2
        #      => (4 - 3)/2 = 1/2
        """
        result = _mod.verify_casimir_eigenvalues()
        assert result['sym2_passed'], (
            f"Casimir on Sym^2 wrong: got {result['eigenvalues_sym2']}, "
            f"expected all +1/2"
        )

    def test_casimir_on_wedge2(self):
        """Omega eigenvalue on wedge^2(C^2) = V_0 is -3/2.

        # VERIFIED:
        # [DC] Direct 4x4 matrix computation
        # [LT] Omega = (C_2^tot - 2*C_2(1/2))/2; C_2(0) = 0, C_2(1/2) = 3/2
        #      => (0 - 3)/2 = -3/2
        """
        result = _mod.verify_casimir_eigenvalues()
        assert result['wedge2_passed'], (
            f"Casimir on wedge^2 wrong: got {result['eigenvalue_wedge2']}, "
            f"expected -3/2"
        )

    def test_casimir_eigenvalues_combined(self):
        """Full eigenvalue spectrum: three copies of +1/2 and one copy of -3/2."""
        Omega = _mod.sl2_casimir_tensor()
        eigs = np.sort(np.real(np.linalg.eigvals(Omega)))
        expected = np.array([-1.5, 0.5, 0.5, 0.5])
        assert np.allclose(eigs, expected, atol=1e-12), (
            f"Eigenvalue spectrum wrong: {eigs} vs {expected}"
        )

    def test_casimir_trace(self):
        """tr(Omega) = 3*(+1/2) + 1*(-3/2) = 0.

        # VERIFIED:
        # [DC] Direct trace computation
        # [SY] Omega is traceless (sum of tensor products of traceless matrices)
        """
        Omega = _mod.sl2_casimir_tensor()
        assert abs(np.trace(Omega)) < 1e-14, (
            f"Omega not traceless: tr = {np.trace(Omega)}"
        )


# ============================================================
# Supporting: theta function identities
# ============================================================

class TestThetaFunctions:
    """Jacobi theta function identities."""

    def test_jacobi_triple_product_square(self):
        """theta_1'(0) = pi * theta_2(0) * theta_3(0) * theta_4(0) at tau = i."""
        result = _mod.verify_jacobi_triple_product(TAU_SQUARE)
        assert result['passed'], (
            f"JTP at tau=i failed: error = {result['relative_error']:.2e}"
        )

    def test_jacobi_triple_product_general(self):
        """JTP at generic tau."""
        result = _mod.verify_jacobi_triple_product(TAU_GENERAL)
        assert result['passed'], (
            f"JTP at tau={TAU_GENERAL} failed: error = {result['relative_error']:.2e}"
        )

    def test_theta1_oddness(self):
        """theta_1(-z) = -theta_1(z)."""
        result = _mod.verify_theta1_oddness(0.3 + 0.2j, TAU_SQUARE)
        assert result['passed'], (
            f"theta_1 oddness failed: error = {result['relative_error']:.2e}"
        )

    def test_theta_quasi_periodicity(self):
        """theta_1(z+1) = -theta_1(z) and theta_1(z+tau) quasi-periodic."""
        result = _mod.verify_theta_quasi_periodicity(0.3 + 0.2j, TAU_SQUARE)
        assert result['passed'], (
            f"Quasi-periodicity failed: period_1={result['period_1_error']:.2e}, "
            f"period_tau={result['period_tau_error']:.2e}"
        )


# ============================================================
# Supporting: weight functions
# ============================================================

class TestWeightFunctions:
    """Belavin weight function properties."""

    def test_all_residues_are_one(self):
        """Each w_a has residue 1 at z=0.

        # VERIFIED:
        # [DC] z * w_a(z) -> 1 as z -> 0 for a=1,2,3
        # [LT] theta_1(z) ~ theta_1'(0)*z cancels against theta_1'(0) in numerator
        """
        result = _mod.verify_weight_residues(TAU_SQUARE)
        assert result['all_passed'], (
            f"Weight residues failed: {result['channels']}"
        )

    def test_xyz_anisotropy(self):
        """The three weight functions are DISTINCT (XYZ model).

        # VERIFIED:
        # [DC] w_1, w_2, w_3 differ at generic z and tau
        # [LT] The elliptic r-matrix is the XYZ/8-vertex model (Baxter 1972)
        """
        result = _mod.verify_weight_anisotropy(TAU_GENERAL)
        assert result['passed'], "Weight functions not anisotropic at generic tau"


# ============================================================
# Supporting: r-matrix structural properties
# ============================================================

class TestRMatrixStructure:
    """Structural properties of the Belavin r-matrix."""

    def test_skew_symmetry_square_lattice(self):
        """r_{12}(z) + r_{21}(-z) = 0 at tau = i.

        # VERIFIED:
        # [DC] Direct matrix computation
        # [LT] Classical r-matrix skew-symmetry (Belavin-Drinfeld 1982)
        """
        result = _mod.verify_skew_symmetry(0.2 + 0.15j, TAU_SQUARE)
        assert result['passed'], (
            f"Skew-symmetry failed: relative = {result['relative']:.2e}"
        )

    def test_skew_symmetry_general_tau(self):
        """Skew-symmetry at generic tau."""
        result = _mod.verify_skew_symmetry(0.15 + 0.1j, TAU_GENERAL)
        assert result['passed'], (
            f"Skew-symmetry at general tau failed: relative = {result['relative']:.2e}"
        )

    def test_simple_pole_at_origin(self):
        """r(z) has a simple pole at z=0 with residue Omega."""
        result = _mod.verify_simple_pole_at_origin(TAU_SQUARE)
        assert result['all_passed'], (
            f"Pole structure failed: {result['directions']}"
        )

    def test_ap126_k_zero_vanishing(self):
        """AP126/AP141: at k=0, the level-prefixed r-matrix is identically zero.

        # VERIFIED:
        # [DC] leveled_r(z, tau, k=0) = 0 * belavin_r(z, tau) = 0
        # [SY] AP126 level prefix mandatory
        """
        result = _mod.verify_level_prefix_k_zero(TAU_SQUARE)
        assert result['passed'], (
            f"AP126 k=0 check failed: norm = {result['norm_at_k0']}"
        )

    def test_level_linearity(self):
        """r(z, tau, k) = k * r(z, tau, 1) (linearity in level)."""
        z, tau, k = 0.2 + 0.1j, TAU_SQUARE, 3.7
        r_k = _mod.leveled_r_matrix_sl2(z, tau, k)
        r_1 = _mod.leveled_r_matrix_sl2(z, tau, 1.0)
        assert np.allclose(r_k, k * r_1, atol=1e-14), (
            f"Level linearity failed: ||r_k - k*r_1|| = "
            f"{np.linalg.norm(r_k - k * r_1):.2e}"
        )

    def test_square_lattice_z4_symmetry(self):
        """At tau = i, eigenvalue magnitudes of r(z) and r(iz) match (Z_4 symmetry)."""
        result = _mod.verify_square_lattice_symmetry()
        assert result['passed'], (
            f"Square lattice symmetry failed: error = {result['relative_error']:.2e}"
        )


# ============================================================
# Supporting: sl_2 algebra
# ============================================================

class TestSl2Algebra:
    """sl_2 representation-theoretic foundations."""

    def test_commutation_relations(self):
        """[E,F]=H, [H,E]=2E, [H,F]=-2F."""
        result = _mod.verify_sl2_commutation_relations()
        assert result['all_passed'], f"sl_2 commutation failed: {result}"

    def test_omega_equals_pauli_sum(self):
        """Omega = sum sigma_a tensor sigma_a / 2 = E tensor F + F tensor E + H tensor H / 2."""
        result = _mod.verify_omega_equals_pauli_sum()
        assert result['passed'], f"Omega != Pauli sum: error = {result['error']:.2e}"

    def test_casimir_element_eigenvalue(self):
        """C_2 = EF + FE + H^2/2 has eigenvalue 3/2 on V_{1/2}.

        # VERIFIED:
        # [DC] Direct 2x2 matrix computation
        # [LT] C_2(j) with our normalization: eigenvalue j(j+1) at j=1/2
        #      gives 1/2 * 3/2 = 3/4?  No: C_2 = EF+FE+H^2/2.
        #      On |e_1>: EF|e_1>=|e_1>, FE|e_1>=0, H^2/2|e_1>=1/2|e_1>.
        #      Total: 3/2.
        """
        result = _mod.verify_casimir_element_eigenvalue()
        assert result['passed'], (
            f"C_2 eigenvalue wrong: {result['eigenvalues']}, expected {result['expected']}"
        )

    def test_permutation_squares_to_identity(self):
        """P^2 = I (the permutation operator is an involution)."""
        P = _mod.permutation_operator()
        assert np.allclose(P @ P, np.eye(4), atol=1e-14), "P^2 != I"

    def test_projector_completeness(self):
        """P_sym + P_wedge = I (Sym^2 + wedge^2 = C^2 tensor C^2)."""
        P_sym = _mod.sym2_projector()
        P_wedge = _mod.wedge2_projector()
        assert np.allclose(P_sym + P_wedge, np.eye(4), atol=1e-14), (
            "P_sym + P_wedge != I"
        )

    def test_projector_ranks(self):
        """Sym^2 has rank 3 (dim V_1), wedge^2 has rank 1 (dim V_0)."""
        P_sym = _mod.sym2_projector()
        P_wedge = _mod.wedge2_projector()
        rank_sym = int(np.round(np.real(np.trace(P_sym))))
        rank_wedge = int(np.round(np.real(np.trace(P_wedge))))
        assert rank_sym == 3, f"Sym^2 rank = {rank_sym}, expected 3"
        assert rank_wedge == 1, f"wedge^2 rank = {rank_wedge}, expected 1"


# ============================================================
# Integration test
# ============================================================

class TestFullVerification:
    """Run the complete verification suite."""

    def test_all_pass(self):
        """All 19 internal verifications pass."""
        results = _mod.run_all_verifications()
        summary = results['summary']
        assert summary['all_passed'], (
            f"Not all passed: {summary['n_passed']}/{summary['n_total']}"
        )
