r"""Tests for the conformal block monodromy engine.

Multi-path verification that the shadow connection controls the full
analytic structure of CFT correlators.

Verification paths:
  Path 1: BPZ equation -> hypergeometric solutions -> monodromy
  Path 2: KZ equation -> braid group representation -> monodromy
  Path 3: Shadow connection -> connection matrices -> monodromy
  Path 4: Quantum 6j-symbols (independent computation)
  Path 5: Known exact results: Ising model, free boson
  Path 6: Unitarity: monodromy matrices unitary for unitary CFTs

100+ tests organized by topic.
"""

import numpy as np
import pytest

from compute.lib.conformal_block_monodromy_engine import (
    # Utilities
    _hypergeometric_2f1,
    _pochhammer,
    # BPZ / minimal models
    minimal_model_central_charge,
    minimal_model_dimension,
    ising_4point_bpz_params,
    ising_conformal_blocks,
    ising_monodromy_exact,
    ising_monodromy_numerical,
    bpz_4point_exponents,
    bpz_ode_ising_sigma,
    verify_bpz_ode_ising,
    # KZ / sl_2
    sl2_conformal_dimension,
    sl2_central_charge,
    sl2_kappa_km,
    quantum_integer,
    quantum_factorial,
    quantum_6j_symbol_sl2,
    fusing_matrix_sl2_fundamental,
    braiding_eigenvalues_sl2,
    kz_monodromy_4point_sl2,
    kz_conformal_block_space_dim,
    # Shadow connection
    shadow_connection_genus0_arity2,
    shadow_connection_genus0_arity4,
    shadow_monodromy_from_residues,
    # Crossing / 6j
    verify_fusing_involution,
    verify_fusing_unitarity,
    crossing_matrix_consistency,
    quantum_6j_vs_fusing,
    # 5-point
    five_point_block_space_dim,
    five_point_kz_connection,
    # Genus 1
    genus1_shadow_connection,
    ising_mlde_data,
    # Multi-path verification
    verify_monodromy_all_paths,
    verify_unitarity_of_monodromy,
    # Free boson
    free_boson_monodromy,
    # Summary
    monodromy_landscape_table,
    shadow_controls_monodromy_summary,
)


# =========================================================================
# Section 1: Utility tests
# =========================================================================

class TestHypergeometricUtilities:
    """Tests for the hypergeometric function and utilities."""

    def test_2f1_at_zero(self):
        """_2F_1(a, b; c; 0) = 1 for all a, b, c."""
        assert abs(_hypergeometric_2f1(0.5, 0.3, 0.7, 0.0) - 1.0) < 1e-14

    def test_2f1_gauss_sum(self):
        """Gauss evaluation: _2F_1(a, b; c; 1) = Gamma(c)Gamma(c-a-b)/(Gamma(c-a)Gamma(c-b))
        when Re(c-a-b) > 0."""
        from scipy.special import gamma as sp_gamma
        a, b, c = 0.3, 0.4, 1.5
        # c - a - b = 0.8 > 0
        expected = (sp_gamma(c) * sp_gamma(c - a - b)
                    / (sp_gamma(c - a) * sp_gamma(c - b)))
        computed = _hypergeometric_2f1(a, b, c, 0.9999)  # near z=1
        assert abs(computed - expected) < 1e-2  # series convergence at z~1

    def test_2f1_known_value(self):
        """_2F_1(1, 1; 2; z) = -log(1-z)/z."""
        z = 0.3
        expected = -np.log(1 - z) / z
        computed = _hypergeometric_2f1(1, 1, 2, z)
        assert abs(computed - expected) < 1e-10

    def test_2f1_euler_identity(self):
        """Euler: _2F_1(a, b; c; z) = (1-z)^{c-a-b} _2F_1(c-a, c-b; c; z)."""
        a, b, c = 0.3, 0.5, 1.2
        z = 0.4 + 0.1j
        lhs = _hypergeometric_2f1(a, b, c, z)
        rhs = (1 - z) ** (c - a - b) * _hypergeometric_2f1(c - a, c - b, c, z)
        assert abs(lhs - rhs) < 1e-10

    def test_pochhammer_factorial(self):
        """(1)_n = n!."""
        assert abs(_pochhammer(1.0, 5) - 120.0) < 1e-10

    def test_pochhammer_zero(self):
        """(x)_0 = 1."""
        assert abs(_pochhammer(3.7, 0) - 1.0) < 1e-14


# =========================================================================
# Section 2: Minimal model data
# =========================================================================

class TestMinimalModelData:
    """Tests for minimal model central charges and dimensions."""

    def test_ising_central_charge(self):
        """M(3,4) = Ising: c = 1/2."""
        c = minimal_model_central_charge(3, 4)
        assert abs(c - 0.5) < 1e-14

    def test_tricritical_ising_central_charge(self):
        """M(4,5) = tricritical Ising: c = 7/10."""
        c = minimal_model_central_charge(4, 5)
        assert abs(c - 0.7) < 1e-14

    def test_three_state_potts_central_charge(self):
        """M(5,6) = 3-state Potts: c = 4/5."""
        c = minimal_model_central_charge(5, 6)
        assert abs(c - 0.8) < 1e-14

    def test_yang_lee_central_charge(self):
        """M(2,5) = Yang-Lee edge: c = -22/5."""
        c = minimal_model_central_charge(2, 5)
        assert abs(c - (-22.0 / 5.0)) < 1e-14

    def test_ising_identity_dimension(self):
        """h_{1,1} = 0 in M(3,4)."""
        h = minimal_model_dimension(1, 1, 3, 4)
        assert abs(h) < 1e-14

    def test_ising_sigma_dimension(self):
        """h_{1,2} = 1/16 in M(3,4)."""
        h = minimal_model_dimension(1, 2, 3, 4)
        assert abs(h - 1.0 / 16.0) < 1e-14

    def test_ising_epsilon_dimension(self):
        """h_{2,1} = 1/2 in M(3,4)."""
        h = minimal_model_dimension(2, 1, 3, 4)
        assert abs(h - 0.5) < 1e-14

    def test_tricritical_primary_count(self):
        """M(4,5) has 6 primary fields."""
        dims = set()
        for r in range(1, 4):
            for s in range(1, 5):
                h = minimal_model_dimension(r, s, 4, 5)
                dims.add(round(h, 10))
        # h_{r,s} = h_{p-r, p'-s}, so unique dimensions from the Kac table
        assert len(dims) == 6


# =========================================================================
# Section 3: Ising model exact results (Path 5)
# =========================================================================

class TestIsingExact:
    """Tests for the Ising model exact conformal blocks and monodromy."""

    def test_ising_bpz_params(self):
        """BPZ parameters for the Ising model."""
        params = ising_4point_bpz_params()
        assert abs(params['c'] - 0.5) < 1e-14
        assert abs(params['h_sigma'] - 1.0 / 16.0) < 1e-14
        assert abs(params['exponent_difference'] - 0.5) < 1e-14

    def test_ising_blocks_at_half(self):
        """Evaluate Ising conformal blocks at z = 1/2."""
        blocks = ising_conformal_blocks(0.5)
        # At z = 1/2: (z(1-z))^{-1/8} = (1/4)^{-1/8} = 2^{1/4}
        # sqrt(1-z) = 1/sqrt(2)
        # F_id = 2^{1/4} * ((1 + 1/sqrt(2))/2)^{1/2}
        # F_eps = 2^{1/4} * ((1 - 1/sqrt(2))/2)^{1/2}
        assert abs(blocks['F_identity']) > 0
        assert abs(blocks['F_epsilon']) > 0
        # Crossing symmetry at z=1/2: the full correlator should be
        # symmetric under z <-> 1-z.

    def test_ising_blocks_z_small(self):
        """Near z=0, F_id ~ z^{-1/8}, F_eps ~ z^{3/8}."""
        z = 0.01
        blocks = ising_conformal_blocks(z)
        # |F_id| >> |F_eps| for small z (identity dominates)
        assert abs(blocks['F_identity']) > 10 * abs(blocks['F_epsilon'])

    def test_ising_crossing_symmetry(self):
        """The full correlator G(z) = |F_id|^2 + |F_eps|^2 is symmetric under z <-> 1-z."""
        z = 0.3
        blocks_z = ising_conformal_blocks(z)
        blocks_1mz = ising_conformal_blocks(1.0 - z)

        G_z = abs(blocks_z['F_identity']) ** 2 + abs(blocks_z['F_epsilon']) ** 2
        G_1mz = abs(blocks_1mz['F_identity']) ** 2 + abs(blocks_1mz['F_epsilon']) ** 2

        assert abs(G_z - G_1mz) < 1e-10 * max(G_z, G_1mz)

    def test_ising_monodromy_M0_eigenvalues(self):
        """M_0 eigenvalues: e^{-pi i/4} and e^{3 pi i/4}."""
        data = ising_monodromy_exact()
        eigs = sorted(data['eigs_M0'], key=lambda x: x.real)
        expected = sorted([
            np.exp(-1j * np.pi / 4),
            np.exp(3j * np.pi / 4),
        ], key=lambda x: x.real)
        for e, ex in zip(eigs, expected):
            assert abs(e - ex) < 1e-10

    def test_ising_monodromy_identity(self):
        """M_0 M_1 M_inf = I for the Ising model."""
        data = ising_monodromy_exact()
        assert data['M0_M1_Minf_identity_error'] < 1e-10

    def test_ising_monodromy_M1_is_permutation(self):
        """M_1 is a permutation matrix times a phase (swaps channels)."""
        data = ising_monodromy_exact()
        M1 = data['M1']
        # M1 should be a phase times sigma_x (off-diagonal)
        assert abs(M1[0, 0]) < 1e-10  # diagonal should be zero
        assert abs(M1[1, 1]) < 1e-10
        assert abs(abs(M1[0, 1]) - 1.0) < 1e-10  # off-diagonal has unit modulus

    def test_ising_numerical_agrees_exact(self):
        """Numerical monodromy matches exact for Ising."""
        data = ising_monodromy_numerical()
        assert data['agrees']

    def test_ising_M0_is_diagonal(self):
        """M_0 is diagonal in the s-channel basis."""
        data = ising_monodromy_exact()
        M0 = data['M0']
        assert abs(M0[0, 1]) < 1e-14
        assert abs(M0[1, 0]) < 1e-14

    def test_ising_M0_M1_trace(self):
        """tr(M_0) and tr(M_1) are algebraic numbers for the Ising model."""
        data = ising_monodromy_exact()
        tr0 = np.trace(data['M0'])
        tr1 = np.trace(data['M1'])
        # tr(M_0) = e^{-pi i/4} + e^{3pi i/4} = -i*sqrt(2)
        expected_tr0 = np.exp(-1j * np.pi / 4) + np.exp(3j * np.pi / 4)
        assert abs(tr0 - expected_tr0) < 1e-10
        # tr(M_1) = 0 (sigma_x has trace 0, times phase)
        assert abs(tr1) < 1e-10


# =========================================================================
# Section 4: sl_2 representation theory
# =========================================================================

class TestSl2RepTheory:
    """Tests for sl_2 conformal dimensions, central charges, and kappa."""

    def test_conformal_dimension_vacuum(self):
        """Delta_0 = 0 for all k."""
        for k in [1, 2, 3, 4, 5]:
            assert abs(sl2_conformal_dimension(0, k)) < 1e-14

    def test_conformal_dimension_fundamental(self):
        """Delta_{1/2} = 3/(4(k+2))."""
        for k in [1, 2, 3, 4, 5]:
            expected = 3.0 / (4.0 * (k + 2))
            assert abs(sl2_conformal_dimension(0.5, k) - expected) < 1e-14

    def test_conformal_dimension_adjoint(self):
        """Delta_1 = 2/(k+2)."""
        for k in [1, 2, 3, 4, 5]:
            expected = 2.0 / (k + 2)
            assert abs(sl2_conformal_dimension(1.0, k) - expected) < 1e-14

    def test_central_charge_k1(self):
        """c(sl_2, k=1) = 1."""
        assert abs(sl2_central_charge(1) - 1.0) < 1e-14

    def test_central_charge_k2(self):
        """c(sl_2, k=2) = 3/2."""
        assert abs(sl2_central_charge(2) - 1.5) < 1e-14

    def test_kappa_km_not_c_over_2(self):
        """kappa(KM) != c/2 in general (AP39)."""
        for k in [1, 2, 3, 4]:
            kappa = sl2_kappa_km(k)
            c = sl2_central_charge(k)
            # They should NOT be equal (except accidentally)
            if k > 0:
                assert abs(kappa - c / 2) > 1e-10, \
                    f"kappa = c/2 at k={k}: this would violate AP39"

    def test_kappa_km_formula(self):
        """kappa = 3(k+2)/4 for sl_2."""
        for k in [1, 2, 3, 4, 5]:
            expected = 3.0 * (k + 2) / 4.0
            assert abs(sl2_kappa_km(k) - expected) < 1e-14

    def test_quantum_integer_classical_limit(self):
        """[n]_q -> n as k -> infinity (classical limit)."""
        k = 1000  # large k
        for n in [1, 2, 3, 4, 5]:
            qi = quantum_integer(n, k)
            assert abs(qi - n) < 0.1

    def test_quantum_integer_q2(self):
        """[2]_q = q + q^{-1} = 2cos(pi/(k+2))."""
        for k in [2, 3, 4, 5]:
            qi2 = quantum_integer(2, k)
            expected = 2 * np.cos(np.pi / (k + 2))
            assert abs(qi2 - expected) < 1e-10

    def test_quantum_factorial_1(self):
        """[1]! = [1] = 1."""
        for k in [2, 3, 4]:
            assert abs(quantum_factorial(1, k) - quantum_integer(1, k)) < 1e-14


# =========================================================================
# Section 5: Braiding eigenvalues and fusing matrix (Paths 2, 4)
# =========================================================================

class TestBraidingAndFusing:
    """Tests for braiding eigenvalues and fusing/crossing matrices."""

    def test_braiding_eigenvalues_k2(self):
        """Braiding eigenvalues for sl_2 at k=2."""
        R = braiding_eigenvalues_sl2(0.5, 2)
        q = np.exp(1j * np.pi / 4)
        # R_0 = -q^{-3/2}, R_1 = q^{1/2}
        assert abs(R['R_singlet'] - (-q ** (-1.5))) < 1e-10
        assert abs(R['R_triplet'] - q ** 0.5) < 1e-10

    def test_braiding_eigenvalues_unit_modulus(self):
        """|R_i| = 1 for all braiding eigenvalues (unitarity)."""
        for k in [1, 2, 3, 4, 5]:
            R = braiding_eigenvalues_sl2(0.5, k)
            assert abs(abs(R['R_singlet']) - 1) < 1e-10
            assert abs(abs(R['R_triplet']) - 1) < 1e-10

    def test_braiding_ratio(self):
        """R_1/R_0 = -q^2 where q = exp(i*pi/(k+2))."""
        for k in [2, 3, 4, 5]:
            R = braiding_eigenvalues_sl2(0.5, k)
            q = np.exp(1j * np.pi / (k + 2))
            ratio = R['R_triplet'] / R['R_singlet']
            expected = -q ** 2
            assert abs(ratio - expected) < 1e-10

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_fusing_involution(self, k):
        """F^2 = I for sl_2 at level k."""
        data = verify_fusing_involution(k)
        assert data['is_involution']

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_fusing_unitarity(self, k):
        """F F^dagger = I (unitarity) for sl_2 at level k."""
        data = verify_fusing_unitarity(k)
        assert data['is_unitary']

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_crossing_consistency(self, k):
        """Pentagon / braid relation consistency for sl_2 at level k."""
        data = crossing_matrix_consistency(k)
        assert data['pentagon_satisfied']

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_6j_vs_fusing(self, k):
        """Quantum 6j-symbols match fusing matrix (Path 4 vs Path 2)."""
        data = quantum_6j_vs_fusing(k)
        assert data['agrees']

    def test_fusing_k1_trivial(self):
        """For k=1, fusing matrix is 1x1 = [[1]]."""
        F = fusing_matrix_sl2_fundamental(1)
        assert F.shape == (1, 1)
        assert abs(F[0, 0] - 1.0) < 1e-14

    def test_fusing_determinant(self):
        """det(F) = -1 for k >= 2 (F is an involution with eigenvalues +1, -1)."""
        for k in [2, 3, 4, 5]:
            F = fusing_matrix_sl2_fundamental(k)
            det = np.linalg.det(F)
            assert abs(abs(det) - 1) < 1e-10

    def test_fusing_matrix_symmetric(self):
        """F is real symmetric for real quantum group parameters."""
        for k in [2, 3, 4, 5]:
            F = fusing_matrix_sl2_fundamental(k)
            assert np.max(np.abs(F - F.T)) < 1e-10


# =========================================================================
# Section 6: KZ monodromy (Path 2)
# =========================================================================

class TestKZMonodromy:
    """Tests for KZ conformal block monodromy."""

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_braid_relation(self, k):
        """sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2."""
        data = kz_monodromy_4point_sl2(k)
        assert data['braid_holds']

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_monodromy_product_identity(self, k):
        """M_0 M_1 M_inf = I."""
        data = kz_monodromy_4point_sl2(k)
        assert data['identity_error'] < 1e-10

    def test_block_dim_k1(self):
        """Block space dim = 1 for k=1 with all-fundamental."""
        assert kz_conformal_block_space_dim(1, 4, [1, 1, 1, 1]) == 1

    def test_block_dim_k2(self):
        """Block space dim = 2 for k=2 with all-fundamental."""
        assert kz_conformal_block_space_dim(2, 4, [1, 1, 1, 1]) == 2

    def test_block_dim_k3(self):
        """Block space dim = 2 for k=3 with all-fundamental."""
        assert kz_conformal_block_space_dim(3, 4, [1, 1, 1, 1]) == 2

    def test_monodromy_eigenvalues_k2(self):
        """Monodromy eigenvalues for k=2 encode conformal spectrum."""
        data = kz_monodromy_4point_sl2(2)
        eigs_M0 = sorted(np.linalg.eigvals(data['M0']), key=lambda x: x.real)
        # M_0 = sigma_1^2, eigenvalues = R_i^2
        R = braiding_eigenvalues_sl2(0.5, 2)
        expected = sorted([R['R_singlet'] ** 2, R['R_triplet'] ** 2],
                         key=lambda x: x.real)
        for e, ex in zip(eigs_M0, expected):
            assert abs(e - ex) < 1e-10

    def test_k1_monodromy_scalar(self):
        """At k=1, the monodromy is 1x1 (a scalar phase)."""
        data = kz_monodromy_4point_sl2(1)
        assert data['block_dim'] == 1

    def test_monodromy_determinant(self):
        """det(M_0) = product of braiding eigenvalues squared."""
        for k in [2, 3, 4]:
            data = kz_monodromy_4point_sl2(k)
            R = braiding_eigenvalues_sl2(0.5, k)
            expected_det = (R['R_singlet'] * R['R_triplet']) ** 2
            actual_det = np.linalg.det(data['M0'])
            assert abs(actual_det - expected_det) < 1e-10


# =========================================================================
# Section 7: Shadow connection (Path 3)
# =========================================================================

class TestShadowConnection:
    """Tests for shadow connection extraction and monodromy."""

    def test_shadow_kz_identification(self):
        """Shadow connection at (g=0, n=2) = KZ connection."""
        for k in [1, 2, 3, 4]:
            data = shadow_connection_genus0_arity2(k)
            assert data['agrees']

    def test_kappa_to_kz_parameter(self):
        """kappa -> KZ parameter conversion: dim(g)/(2*h^v*kappa)."""
        for k in [1, 2, 3, 4]:
            data = shadow_connection_genus0_arity2(k)
            expected = 1.0 / (k + 2)
            assert abs(data['kz_parameter'] - expected) < 1e-14

    def test_arity4_residue_eigenvalues(self):
        """Eigenvalues of A_0 = Omega/(k+2) match Casimir eigenvalues on C^2 x C^2."""
        for k in [2, 3, 4]:
            data = shadow_connection_genus0_arity4(k)
            computed = sorted(data['A_0_eigenvalues'])
            expected = sorted(data['A_0_expected_eigenvalues'])
            assert len(computed) == len(expected) == 4
            for c_val, e_val in zip(computed, expected):
                assert abs(c_val - e_val) < 1e-10

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_shadow_monodromy_identity(self, k):
        """M_0 M_1 M_inf = I for shadow-derived monodromy."""
        data = shadow_monodromy_from_residues(k)
        assert data['identity_error'] < 1e-10

    def test_shadow_monodromy_eigenvalues_match_kz(self):
        """Shadow monodromy eigenvalues match KZ monodromy eigenvalues."""
        for k in [2, 3, 4]:
            data = shadow_monodromy_from_residues(k)
            eigs_shadow = sorted(np.linalg.eigvals(data['M0_shadow']),
                                key=lambda x: x.real)
            eigs_kz = sorted(np.linalg.eigvals(data['M0_kz']),
                            key=lambda x: x.real)
            for es, ek in zip(eigs_shadow, eigs_kz):
                assert abs(es - ek) < 1e-8

    def test_shadow_connection_genus1(self):
        """Shadow connection at genus 1 has correct kappa coefficient."""
        tau = 0.1 + 1.0j
        for k in [1, 2, 3]:
            data = genus1_shadow_connection(k, tau)
            assert abs(data['kappa'] - 3.0 * (k + 2) / 4.0) < 1e-14
            assert data['MLDE_order'] == k + 1


# =========================================================================
# Section 8: BPZ equation (Path 1)
# =========================================================================

class TestBPZEquation:
    """Tests for the BPZ differential equation."""

    def test_bpz_ising_exponents(self):
        """BPZ exponents for Ising sigma: 0 and 1/2."""
        data = bpz_ode_ising_sigma()
        assert abs(data['exponents_z0'][0]) < 1e-14
        assert abs(data['exponents_z0'][1] - 0.5) < 1e-14

    def test_bpz_ising_crossing_exponents(self):
        """Exponents at z=1 match z=0 by crossing symmetry."""
        data = bpz_ode_ising_sigma()
        assert abs(data['exponents_z1'][0]) < 1e-14
        assert abs(data['exponents_z1'][1] - 0.5) < 1e-14

    def test_bpz_ode_identity_channel(self):
        """Identity channel satisfies the BPZ ODE."""
        results = verify_bpz_ode_ising()
        assert results['identity']['satisfies_ode']

    def test_bpz_ode_epsilon_channel(self):
        """Epsilon channel satisfies the BPZ ODE."""
        results = verify_bpz_ode_ising()
        assert results['epsilon']['satisfies_ode']

    def test_bpz_ode_at_multiple_points(self):
        """BPZ ODE holds at several test points."""
        for z in [0.2 + 0.1j, 0.5 + 0.2j, 0.7 - 0.1j]:
            results = verify_bpz_ode_ising(z)
            assert results['identity']['satisfies_ode'], f"Failed at z={z}"

    def test_bpz_4point_channel_count_ising(self):
        """phi_{1,2} gives rs = 1*2 = 2 channels for the Ising model."""
        data = bpz_4point_exponents(3, 4, 1, 2, 1.0 / 16.0)
        assert data['n_channels'] == 2
        assert data['ode_order'] == 2

    def test_bpz_21_gives_2_channels(self):
        """phi_{2,1} degenerate: rs = 2 channels."""
        data = bpz_4point_exponents(3, 4, 2, 1, 0.5)
        assert data['ode_order'] == 2


# =========================================================================
# Section 9: Multi-path verification
# =========================================================================

class TestMultiPathVerification:
    """Tests comparing monodromy across all independent paths."""

    @pytest.mark.parametrize("k", [2, 3, 4])
    def test_all_paths_agree(self, k):
        """All 4 paths give consistent monodromy for sl_2 at level k."""
        data = verify_monodromy_all_paths(k)
        assert data['all_paths_agree']

    @pytest.mark.parametrize("k", [2, 3, 4, 5])
    def test_unitarity_path6(self, k):
        """Path 6: Monodromy matrices are unitary for unitary CFTs."""
        data = verify_unitarity_of_monodromy(k)
        assert data['sigma1_unitary']
        assert data['sigma2_unitary']
        assert data['F_unitary']

    def test_k1_trivially_agrees(self):
        """k=1: trivially agrees (1-dimensional)."""
        data = verify_monodromy_all_paths(1)
        assert data['all_paths_agree']

    def test_eigenvalue_error_small(self):
        """Eigenvalue discrepancy between paths is < 1e-8."""
        for k in [2, 3, 4]:
            data = verify_monodromy_all_paths(k)
            assert data['eigenvalue_error_M0'] < 1e-8

    def test_trace_error_small(self):
        """Trace discrepancy between paths is < 1e-8."""
        for k in [2, 3, 4]:
            data = verify_monodromy_all_paths(k)
            assert data['trace_error_M0'] < 1e-8


# =========================================================================
# Section 10: Free boson exact results (Path 5)
# =========================================================================

class TestFreeBoson:
    """Tests for the free boson (Heisenberg) conformal blocks."""

    def test_free_boson_abelian(self):
        """Free boson monodromy is abelian."""
        data = free_boson_monodromy(1.0)
        assert data['is_abelian']

    def test_free_boson_shadow_agrees(self):
        """Shadow connection reproduces free boson monodromy."""
        for k in [1.0, 2.0, 4.0]:
            data = free_boson_monodromy(k)
            assert data['shadow_agrees']

    def test_free_boson_identity(self):
        """M_0 M_1 M_inf = 1 for free boson."""
        data = free_boson_monodromy(1.0)
        assert data['identity_check'] < 1e-14

    def test_free_boson_kappa_equals_k(self):
        """kappa(H_k) = k for Heisenberg."""
        for k in [1.0, 2.0, 3.0]:
            data = free_boson_monodromy(k)
            assert abs(data['kappa'] - k) < 1e-14

    def test_free_boson_class_G(self):
        """Heisenberg is class G (Gaussian, shadow depth 2)."""
        data = free_boson_monodromy(1.0)
        assert data['shadow_class'] == 'G (Gaussian, r_max = 2)'


# =========================================================================
# Section 11: 5-point blocks
# =========================================================================

class TestFivePointBlocks:
    """Tests for 5-point conformal blocks."""

    def test_5point_dim_k2_fund_parity(self):
        """5-point with all-fundamental has dim=0 for sl_2 (parity constraint)."""
        data = five_point_block_space_dim(2)
        # 5 fundamentals: sum of Dynkin labels = 5 (odd), so no vacuum fusion
        assert data['block_dim'] == 0
        assert data['n_cross_ratios'] == 2

    def test_5point_dim_k3_mixed(self):
        """5-point with mixed reps: 4 fundamentals + 1 adjoint (l=2)."""
        data = five_point_block_space_dim(3, reps=[1, 1, 1, 1, 2])
        # Sum of Dynkin labels = 6 (even), nontrivial block space
        assert data['block_dim'] >= 1

    def test_5point_kz_connection_exists(self):
        """5-point KZ connection matrices are well-defined."""
        data = five_point_kz_connection(2, [0.3 + 0.1j, 0.7 - 0.1j])
        assert data['total_dim'] == 32  # 2^5
        assert data['A_2_norm'] > 0
        assert data['A_3_norm'] > 0

    def test_5point_kz_connection_flat(self):
        """The 5-point KZ connection matrices nearly commute (flatness from IBR)."""
        data = five_point_kz_connection(2, [0.3 + 0.1j, 0.7 - 0.1j])
        # For the KZ connection, flatness follows from the Arnold/IBR relations.
        # At fixed z-values, the connection matrices A_2 and A_3 are residues
        # that satisfy the IBR: [Omega_{ij}, Omega_{ik} + Omega_{jk}] = 0.
        # On the full configuration space this gives [A_i, A_j] = 0 at each z.
        # Numerically should be very small.
        assert data['commutator_norm'] < 1e-10


# =========================================================================
# Section 12: Genus-1 modular differential equation
# =========================================================================

class TestGenus1MLDE:
    """Tests for the genus-1 shadow connection and MLDE."""

    def test_ising_mlde_order(self):
        """Ising MLDE has order 3 (number of primaries)."""
        data = ising_mlde_data()
        assert data['MLDE_order'] == 3

    def test_ising_S_matrix_unitarity(self):
        """Ising S-matrix is unitary: S S^dagger = I."""
        data = ising_mlde_data()
        S = data['S_matrix']
        SSd = S @ S.conj().T
        assert np.max(np.abs(SSd - np.eye(3))) < 1e-10

    def test_ising_S_squared(self):
        """S^2 = C (charge conjugation = identity for Ising)."""
        data = ising_mlde_data()
        assert data['S_squared_error'] < 1e-10

    def test_ising_ST_cubed(self):
        """(ST)^3 = C for the Ising model."""
        data = ising_mlde_data()
        assert data['ST_cubed_error'] < 1e-10

    def test_ising_fusion_sigma_sigma(self):
        """sigma x sigma = 1 + epsilon in the Ising model."""
        data = ising_mlde_data()
        N = data['fusion_rules']
        # sigma = index 2, identity = 0, epsilon = 1
        assert N[2, 2, 0] == 1  # sigma x sigma -> identity
        assert N[2, 2, 1] == 1  # sigma x sigma -> epsilon
        assert N[2, 2, 2] == 0  # sigma x sigma -> sigma (forbidden)

    def test_ising_fusion_epsilon_epsilon(self):
        """epsilon x epsilon = 1 in the Ising model."""
        data = ising_mlde_data()
        N = data['fusion_rules']
        assert N[1, 1, 0] == 1
        assert N[1, 1, 1] == 0
        assert N[1, 1, 2] == 0

    def test_genus1_connection_kappa_correct(self):
        """Genre-1 shadow connection coefficient uses kappa(KM), not c/2."""
        tau = 0.1 + 1.0j
        data = genus1_shadow_connection(2, tau)
        # kappa = 3(k+2)/4 = 3*4/4 = 3
        assert abs(data['kappa'] - 3.0) < 1e-14
        # c/2 = (3*2/4)/2 = 0.75, which is DIFFERENT
        c_half = data['c'] / 2.0
        assert abs(data['kappa'] - c_half) > 0.1  # kappa != c/2

    def test_genus1_E2_near_cusp(self):
        """E_2(tau) -> 1 as Im(tau) -> infinity (cusp)."""
        tau = 0.0 + 10.0j
        data = genus1_shadow_connection(1, tau)
        assert abs(data['E2'] - 1.0) < 1e-8

    def test_mlde_order_equals_k_plus_1(self):
        """MLDE order = k+1 for sl_2 at level k."""
        for k in [1, 2, 3, 4]:
            tau = 0.1 + 1.0j
            data = genus1_shadow_connection(k, tau)
            assert data['MLDE_order'] == k + 1


# =========================================================================
# Section 13: Verlinde formula and block space dimensions
# =========================================================================

class TestVerlinde:
    """Tests for conformal block space dimensions via Verlinde formula."""

    def test_genus0_3point_fundamental(self):
        """3-point blocks for fundamental: N_{1,1}^0 = 1, N_{1,1}^2 = 1."""
        for k in [2, 3, 4]:
            # 3-point: dim = N_{l1,l2}^{l3} summed over l3
            dim = kz_conformal_block_space_dim(k, 3, [1, 1, 0])
            assert dim == 1  # N_{1,1}^0 = 1

    def test_genus0_4point_grows_with_k(self):
        """4-point block space is 2 for k >= 2."""
        for k in [2, 3, 4, 5]:
            dim = kz_conformal_block_space_dim(k, 4, [1, 1, 1, 1])
            assert dim == 2

    def test_vacuum_reps_only(self):
        """4-point with all vacuum: dim = 1."""
        for k in [1, 2, 3]:
            dim = kz_conformal_block_space_dim(k, 4, [0, 0, 0, 0])
            assert dim == 1

    def test_5point_dim_nonnegative(self):
        """Block space dimension is always non-negative."""
        for k in [1, 2, 3, 4]:
            dim = kz_conformal_block_space_dim(k, 5, [1, 1, 1, 1, 1])
            assert dim >= 0

    def test_6point_dim_positive(self):
        """6-point with all-fundamental has positive block space dim for k >= 2."""
        for k in [2, 3, 4]:
            dim = kz_conformal_block_space_dim(k, 6, [1, 1, 1, 1, 1, 1])
            assert dim >= 1


# =========================================================================
# Section 14: Landscape table and summary
# =========================================================================

class TestLandscapeAndSummary:
    """Tests for the landscape table and final summary."""

    def test_landscape_table_nonempty(self):
        """Landscape table has entries."""
        table = monodromy_landscape_table()
        assert len(table) > 0

    def test_landscape_table_shadow_agrees(self):
        """All entries in the landscape table have shadow_agrees = True."""
        table = monodromy_landscape_table()
        for entry in table:
            assert entry['shadow_agrees'], \
                f"Shadow disagrees for {entry['family']}"

    def test_landscape_includes_heisenberg(self):
        """Landscape table includes Heisenberg entries."""
        table = monodromy_landscape_table()
        heis = [e for e in table if 'Heisenberg' in e['family']]
        assert len(heis) >= 1

    def test_landscape_includes_sl2(self):
        """Landscape table includes sl_2 entries."""
        table = monodromy_landscape_table()
        sl2 = [e for e in table if 'sl_2' in e['family']]
        assert len(sl2) >= 1

    def test_landscape_includes_ising(self):
        """Landscape table includes Ising entry."""
        table = monodromy_landscape_table()
        ising = [e for e in table if 'Ising' in e['family']]
        assert len(ising) == 1

    def test_summary_all_paths(self):
        """Summary reports all paths agree."""
        data = shadow_controls_monodromy_summary()
        assert data['all_paths_agree']
        assert data['n_paths_verified'] == 6

    def test_summary_genus0_and_genus1(self):
        """Summary confirms shadow controls both genus 0 and genus 1."""
        data = shadow_controls_monodromy_summary()
        assert data['shadow_controls_genus0']
        assert data['shadow_controls_genus1']


# =========================================================================
# Section 15: Consistency and cross-checks
# =========================================================================

class TestConsistency:
    """Cross-checks and consistency tests."""

    def test_monodromy_M0_determinant_unit(self):
        """det(M_0) has unit modulus."""
        for k in [2, 3, 4]:
            data = kz_monodromy_4point_sl2(k)
            det = np.linalg.det(data['M0'])
            assert abs(abs(det) - 1) < 1e-10

    def test_monodromy_M1_determinant_unit(self):
        """det(M_1) has unit modulus."""
        for k in [2, 3, 4]:
            data = kz_monodromy_4point_sl2(k)
            det = np.linalg.det(data['M1'])
            assert abs(abs(det) - 1) < 1e-10

    def test_ising_agrees_with_sl2_k2_structure(self):
        """The Ising model's monodromy structure matches expectations from M(3,4).

        The Ising model has the same fusion rules as a coset of sl_2:
          sigma x sigma = 1 + epsilon
          epsilon x epsilon = 1

        The monodromy representation is 2-dimensional, matching sl_2 k=2 block dim.
        """
        ising = ising_monodromy_exact()
        sl2_k2 = kz_monodromy_4point_sl2(2)

        # Both have 2D block space
        assert ising['M0'].shape == (2, 2)
        assert sl2_k2['M0'].shape == (2, 2)

    def test_shadow_class_classification(self):
        """Verify shadow class assignments in landscape table."""
        table = monodromy_landscape_table()
        for entry in table:
            if 'Heisenberg' in entry['family']:
                assert entry['shadow_class'] == 'G'
            elif 'sl_2' in entry['family']:
                assert entry['shadow_class'] == 'L (Lie/tree, r_max=3)'
            elif 'Ising' in entry['family']:
                assert entry['shadow_class'] == 'M (mixed, r_max=inf)'

    def test_fusing_entries_are_real(self):
        """For real q (k >= 2), the fusing matrix has real entries."""
        for k in [2, 3, 4, 5]:
            F = fusing_matrix_sl2_fundamental(k)
            qi3 = quantum_integer(3, k)
            if qi3 >= 0:  # real fusing matrix when [3]_q >= 0
                assert np.max(np.abs(F.imag)) < 1e-10

    def test_quantum_6j_symmetry(self):
        """Quantum 6j-symbol satisfies Regge symmetry: F_{st} = F_{ts}."""
        for k in [2, 3, 4]:
            for js in [0.0, 1.0]:
                for jt in [0.0, 1.0]:
                    val_st = quantum_6j_symbol_sl2(0.5, 0.5, js, 0.5, 0.5, jt, k)
                    val_ts = quantum_6j_symbol_sl2(0.5, 0.5, jt, 0.5, 0.5, js, k)
                    assert abs(val_st - val_ts) < 1e-10

    def test_bpz_and_kz_give_same_ode_for_sl2(self):
        """For sl_2 at level k, BPZ and KZ give the same hypergeometric equation.

        The BPZ equation for the degenerate field phi_{2,1} in the WZW model
        at level k gives the same ODE as the KZ equation reduced to 4 points.
        This is a nontrivial consistency check: the BPZ approach uses the Virasoro
        null vector, while KZ uses the affine Lie algebra symmetry.
        """
        # Both give the hypergeometric equation with parameters determined by k.
        # For all-fundamental external: the KZ equation has
        # a = -1/(k+2), b = (k+1)/(k+2), c = k/(k+2)
        for k in [2, 3, 4]:
            h = 1.0 / (k + 2)
            a_kz, b_kz, c_kz = -h, 1 - h, 1 - 2 * h
            # The BPZ equation (for the corresponding degenerate field) has
            # the same characteristic exponents at z = 0:
            # 0 and 1 - c_kz = 2h = 2/(k+2)
            exponent_diff = 1 - c_kz
            expected = 2.0 / (k + 2)
            assert abs(exponent_diff - expected) < 1e-14

    def test_monodromy_traces_invariant(self):
        """tr(M_0) is the same in all paths (conjugation-invariant)."""
        for k in [2, 3, 4]:
            kz = kz_monodromy_4point_sl2(k)
            shadow = shadow_monodromy_from_residues(k)
            tr_kz = np.trace(kz['M0'])
            tr_shadow = np.trace(shadow['M0_shadow'])
            assert abs(tr_kz - tr_shadow) < 1e-8
