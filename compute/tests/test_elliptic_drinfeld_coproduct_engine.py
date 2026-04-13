r"""Tests for the elliptic Drinfeld coproduct engine E_{tau,eta}(sl_2).

30 tests organized in seven groups:

[A] R-matrix structure (6 tests):
    Quantum YBE at tau=i and generic tau, unitarity, eight-vertex structure,
    Pauli decomposition, regularity R(0) = sn(gamma)*P, crossing symmetry.

[B] L-operator and RTT (3 tests):
    RTT at tau=i, generic tau, and with shifted evaluation parameter.

[C] Coproduct structure (6 tests):
    Standard coproduct RTT, shifted coproduct RTT, shifted z=0 reduces to
    standard, standard coassociativity, shifted coassociativity, triple
    shifted transfer matrix RTT.

[D] Quantum determinant (2 tests):
    Quantum determinant proportional to identity at two spectral parameters.

[E] Degeneration chain (4 tests):
    Elliptic -> trigonometric (d -> 0), rational limit (gamma -> 0),
    classical limit (twisted CYBE), classical Belavin CYBE.

[F] Theta function foundations (4 tests):
    Jacobi triple product, theta_1 oddness, theta cross-check, weight
    function residues.

[G] Additional structural tests (5 tests):
    YBE at generic tau, shifted coproduct RTT with complex z, regularity
    at different gamma, quantum determinant factorization, shifted RTT
    with large z.

Ground truth:
    - Baxter (1972, 1982): eight-vertex model
    - Belavin (1981), Belavin-Drinfeld (1982), Sklyanin (1982)
    - Felder (1994, 1995): elliptic quantum groups
    - Korepin-Bogoliubov-Izergin (1993): QISM, crossing symmetry
    - AP19: bar kernel absorbs a pole
    - AP126: level prefix mandatory; k=0 => r=0
    - AP141: k=0 vanishing check
"""

import pytest
import numpy as np

import importlib.util
import os

# Load module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'elliptic_drinfeld_coproduct_engine',
    os.path.join(_lib_dir, 'elliptic_drinfeld_coproduct_engine.py'),
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# Standard parameters
TAU_I = 1j           # square lattice
TAU_GEN = 0.5 + 1.2j  # generic modular parameter
GAMMA = 0.25         # crossing parameter


# ============================================================
# [A] R-matrix structure
# ============================================================

class TestRMatrixStructure:
    """Tests A1-A6: fundamental R-matrix properties."""

    def test_A1_quantum_ybe_tau_i(self):
        """Quantum YBE at tau=i for four spectral parameter pairs."""
        for z12, z13 in [(0.3, 0.7), (0.1, 0.5), (0.15, 0.4), (0.2, 0.9)]:
            result = _mod.verify_quantum_ybe(z12, z13, GAMMA, TAU_I)
            assert result['passed'], (
                f"YBE failed at z12={z12}, z13={z13}: "
                f"rel={result['relative']:.2e}")

    def test_A2_unitarity(self):
        """Unitarity R_{12}(z) R_{21}(-z) = rho(z)*I at four z values."""
        for z_val in [0.2, 0.5, 0.8, 1.1]:
            result = _mod.verify_unitarity(z_val, GAMMA, TAU_I)
            assert result['passed'], (
                f"Unitarity failed at z={z_val}: rel={result['relative']:.2e}")

    def test_A3_eight_vertex(self):
        """All four Pauli channels nonzero (eight-vertex, d != 0)."""
        result = _mod.verify_eight_vertex(0.3, GAMMA, TAU_I)
        assert result['passed'], f"|d| = {abs(result['d']):.2e} too small"

    def test_A4_pauli_decomposition(self):
        """Pauli decomposition matches eight-vertex form exactly."""
        result = _mod.verify_pauli_decomposition(0.3, GAMMA, TAU_I)
        assert result['passed'], f"Pauli err = {result['error']:.2e}"

    def test_A5_regularity(self):
        """R(0) = sn(gamma) * P (regularity at spectral origin)."""
        result = _mod.verify_regularity(GAMMA, TAU_I)
        assert result['passed'], (
            f"Regularity failed: sn(gamma)={result['sn_gamma']}, "
            f"rel={result['relative']:.2e}")

    def test_A6_crossing_symmetry(self):
        """Crossing: R^{t_2}(-z-gamma) = -(I x sigma_y) R(z) (I x sigma_y)."""
        result = _mod.verify_crossing_symmetry(0.3, GAMMA, TAU_I)
        assert result['passed'], f"Crossing rel = {result['relative']:.2e}"


# ============================================================
# [B] L-operator and RTT
# ============================================================

class TestRTTRelation:
    """Tests B7-B9: RTT relation for the L-operator."""

    def test_B7_rtt_tau_i(self):
        """RTT at tau=i for three (u,v) pairs."""
        for u, v in [(0.3, 0.7), (0.1, 0.5), (0.2, 0.8)]:
            result = _mod.verify_rtt(u, v, GAMMA, TAU_I)
            assert result['passed'], (
                f"RTT failed at u={u}, v={v}: rel={result['relative']:.2e}")

    def test_B8_rtt_generic_tau(self):
        """RTT at generic tau = 0.5 + 1.2i."""
        result = _mod.verify_rtt(0.3, 0.6, GAMMA, TAU_GEN)
        assert result['passed'], f"RTT rel = {result['relative']:.2e}"

    def test_B9_rtt_shifted_eval(self):
        """RTT with nonzero evaluation shift w=0.4."""
        result = _mod.verify_rtt(0.25, 0.6, GAMMA, TAU_I, w=0.4)
        assert result['passed'], f"RTT rel = {result['relative']:.2e}"


# ============================================================
# [C] Coproduct structure
# ============================================================

class TestCoproductStructure:
    """Tests C10-C15: coproduct, shifted coproduct, coassociativity."""

    def test_C10_standard_coproduct_rtt(self):
        """Standard coproduct (z=0) satisfies RTT in tensor product."""
        result = _mod.verify_shifted_coproduct_rtt(0.3, 0.6, 0.0, GAMMA, TAU_I)
        assert result['passed'], f"Coprod RTT rel = {result['relative']:.2e}"

    def test_C11_shifted_coproduct_rtt(self):
        """Shifted coproduct Delta_z at z=0.25 satisfies RTT."""
        # VERIFIED: [DC] direct 16x16 matrix computation
        # [LT] Felder (1995) Prop 3.1: evaluation representations
        result = _mod.verify_shifted_coproduct_rtt(
            0.3, 0.6, 0.25, GAMMA, TAU_I)
        assert result['passed'], f"Shifted RTT rel = {result['relative']:.2e}"

    def test_C12_shifted_z0_is_standard(self):
        """Delta_{z=0}(L(u)) = Delta(L(u)) (shifted reduces to standard)."""
        result = _mod.verify_shifted_at_z0(0.3, GAMMA, TAU_I)
        assert result['passed'], f"z=0 rel = {result['relative']:.2e}"

    def test_C13_standard_coassociativity(self):
        """(Delta x id) o Delta = (id x Delta) o Delta."""
        result = _mod.verify_coassociativity(0.3, GAMMA, TAU_I)
        assert result['passed']

    def test_C14_shifted_coassociativity(self):
        """Shifted coproducts compose: evals at (0, z1, z1+z2)."""
        result = _mod.verify_shifted_coassociativity(
            0.3, 0.15, 0.2, GAMMA, TAU_I)
        assert result['passed']

    def test_C15_triple_shifted_rtt(self):
        """Triple shifted transfer matrix L(u;0)*L(u;z1)*L(u;z1+z2) satisfies RTT.

        This is the nontrivial content of shifted coassociativity: the
        iterated coproduct defines a valid algebra homomorphism.
        """
        # VERIFIED: [DC] 32x32 matrix computation (2^5 space)
        # [LT] Faddeev (Les Houches 1996): transfer matrix RTT
        result = _mod.verify_shifted_triple_rtt(
            0.3, 0.6, 0.15, 0.2, GAMMA, TAU_I)
        assert result['passed'], f"Triple RTT rel = {result['relative']:.2e}"


# ============================================================
# [D] Quantum determinant
# ============================================================

class TestQuantumDeterminant:
    """Tests D16-D17: quantum determinant is scalar."""

    def test_D16_qdet_scalar(self):
        """qdet L(u) proportional to identity at u=0.3."""
        result = _mod.verify_quantum_determinant_scalar(0.3, GAMMA, TAU_I)
        assert result['passed'], "qdet not scalar"

    def test_D17_qdet_scalar_u2(self):
        """qdet L(u) proportional to identity at u=0.7."""
        result = _mod.verify_quantum_determinant_scalar(0.7, GAMMA, TAU_I)
        assert result['passed'], "qdet not scalar at u=0.7"


# ============================================================
# [E] Degeneration chain
# ============================================================

class TestDegenerationChain:
    """Tests E18-E21: elliptic -> trigonometric -> rational, classical limit."""

    def test_E18_trigonometric_limit(self):
        """d-weight -> 0 as Im(tau) -> infinity (six-vertex limit)."""
        result = _mod.verify_trigonometric_limit(0.3, GAMMA)
        assert result['passed'], (
            f"Trig limit: final |d| = {result['final_d']:.2e}")

    def test_E19_rational_limit(self):
        """R(gamma*z, gamma)/sn(gamma) -> z*I + P as gamma -> 0."""
        # VERIFIED: [DC] direct numerical evaluation
        # [LT] Faddeev (1996): Yang R-matrix u*I + c*P
        result = _mod.verify_rational_limit(0.5)
        assert result['passed'], (
            f"Rational limit: final err = {result['final_error']:.2e}")

    def test_E20_classical_limit_cybe(self):
        """Quasi-classical r_qc satisfies twisted CYBE, error O(gamma)."""
        result = _mod.verify_classical_limit(tau=TAU_I)
        assert result['passed'], (
            f"Classical limit: errors = {result['errors']}")

    def test_E21_classical_belavin_cybe(self):
        """Classical Belavin r-matrix (weight functions) satisfies CYBE."""
        z1, z2, z3 = 0.1 + 0.05j, 0.3 + 0.1j, 0.5 + 0.2j
        r12 = _mod._embed_12(_mod.classical_r_matrix(z1 - z2, TAU_I))
        r13 = _mod._embed_13(_mod.classical_r_matrix(z1 - z3, TAU_I))
        r23 = _mod._embed_23(_mod.classical_r_matrix(z2 - z3, TAU_I))
        cybe = (r12 @ r13 - r13 @ r12
                + r12 @ r23 - r23 @ r12
                + r13 @ r23 - r23 @ r13)
        err = np.linalg.norm(cybe) / max(np.linalg.norm(r12), 1.0)
        assert err < 1e-7, f"CYBE rel = {err:.2e}"


# ============================================================
# [F] Theta function foundations
# ============================================================

class TestThetaFunctions:
    """Tests F22-F25: theta function identities and weight residues."""

    def test_F22_jacobi_triple_product(self):
        """theta_1'(0) = pi * theta_2(0) * theta_3(0) * theta_4(0)."""
        result = _mod.verify_theta_triple_product(TAU_I)
        assert result['passed'], f"err = {result['relative_error']:.2e}"

    def test_F23_theta1_oddness(self):
        """theta_1(-z) = -theta_1(z)."""
        result = _mod.verify_theta1_oddness(0.3 + 0.2j, TAU_I)
        assert result['passed'], f"err = {result['relative_error']:.2e}"

    def test_F24_theta_cross_check(self):
        """theta_4(0|tau) = theta_3(0|tau+1) at tau=i."""
        th4 = _mod.theta4(0, 1j)
        th3_shift = _mod.theta3(0, 1 + 1j)
        err = abs(th4 - th3_shift) / max(abs(th4), 1e-10)
        assert err < 1e-10, f"Theta cross-check err = {err:.2e}"

    def test_F25_weight_function_residue(self):
        """w_a(z) ~ 1/z at z -> 0, so z*w_a(z) -> 1."""
        z_small = 1e-6
        for a in range(1, 4):
            w = _mod.belavin_weight_function(z_small, TAU_I, a)
            res = abs(z_small * w - 1.0)
            assert res < 1e-4, (
                f"Residue error for w_{a}: |z*w-1| = {res:.2e}")


# ============================================================
# [G] Additional structural tests
# ============================================================

class TestAdditionalStructural:
    """Tests G26-G30: robustness and additional verifications."""

    def test_G26_ybe_generic_tau(self):
        """Quantum YBE at generic tau = 0.3 + 0.8i."""
        tau3 = 0.3 + 0.8j
        result = _mod.verify_quantum_ybe(0.2, 0.6, GAMMA, tau3)
        assert result['passed'], f"YBE rel = {result['relative']:.2e}"

    def test_G27_shifted_rtt_complex_z(self):
        """Shifted coproduct RTT with complex shift z = 0.1 + 0.15i."""
        result = _mod.verify_shifted_coproduct_rtt(
            0.25, 0.55, 0.1 + 0.15j, GAMMA, TAU_I)
        assert result['passed'], f"Shifted RTT rel = {result['relative']:.2e}"

    def test_G28_regularity_different_gamma(self):
        """Regularity R(0) = sn(gamma)*P at gamma=0.15."""
        result = _mod.verify_regularity(0.15, TAU_I)
        assert result['passed'], f"Regularity rel = {result['relative']:.2e}"

    def test_G29_qdet_factorization(self):
        """Quantum determinant nonzero at generic parameters."""
        qd1 = _mod.quantum_determinant(0.3, GAMMA, TAU_I, w=0.0)
        qd2 = _mod.quantum_determinant(0.3, GAMMA, TAU_I, w=0.25)
        s1 = np.trace(qd1) / 2.0
        s2 = np.trace(qd2) / 2.0
        assert abs(s1 * s2) > 1e-10, (
            f"qdet product vanishes: s1={s1:.6f}, s2={s2:.6f}")

    def test_G30_shifted_rtt_large_z(self):
        """Shifted coproduct RTT stable at large shift z=0.7."""
        result = _mod.verify_shifted_coproduct_rtt(
            0.2, 0.5, 0.7, GAMMA, TAU_I)
        assert result['passed'], f"Large z RTT rel = {result['relative']:.2e}"


# ============================================================
# Integration test: run_all_tests
# ============================================================

class TestIntegration:
    """Run the engine's built-in test suite."""

    def test_run_all_tests(self):
        """All 30 tests in run_all_tests pass."""
        results = _mod.run_all_tests(verbose=False)
        failed = [name for name, passed in results.items() if not passed]
        assert not failed, f"Failed tests: {failed}"
        assert len(results) >= 30, (
            f"Expected 30+ tests, got {len(results)}")
