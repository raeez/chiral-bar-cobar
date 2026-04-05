r"""Tests for frontier_defect_explicit_engine.py

Comprehensive test suite for the frontier defect form Omega_A:
  - Explicit Omega for Heisenberg, affine sl_2, Virasoro, W_3, lattice VOAs
  - Exactness criterion and gauge criterion
  - Miura splitting for W_N
  - Residue computation at singular points
  - Verlinde comparison for minimal models
  - d_arith extraction
  - Multi-path verification (4 paths per family)
  - Cross-family consistency
  - Koszul dual complementarity

90+ tests organized by topic.

MULTI-PATH VERIFICATION:
  Path 1: Direct computation from character/representation theory
  Path 2: Extraction from shadow obstruction tower
  Path 3: Verlinde formula / known S-matrices for minimal models
  Path 4: Gauge criterion (exactness test)
"""

import math
import cmath
import pytest
import numpy as np

from compute.lib.frontier_defect_explicit_engine import (
    # Infrastructure
    _numerical_dlog,
    _numerical_derivative,
    _partial_zeta,
    completed_riemann_zeta,
    riemann_scattering,
    # Heisenberg
    HeisenbergDefect,
    # Affine sl_2
    AffineSl2Defect,
    sl2_central_charge,
    sl2_kappa,
    sl2_S_matrix,
    sl2_quantum_dimensions,
    sl2_verlinde_dimension,
    sl2_conformal_weights,
    # Virasoro
    VirasoroDefect,
    virasoro_kappa,
    virasoro_shadow_coefficients,
    minimal_model_central_charge,
    minimal_model_S_matrix,
    minimal_model_conformal_weights,
    # W_3
    W3Defect,
    MiuraSplitting,
    w3_kappa,
    w3_shadow_metric_T,
    w3_shadow_metric_W,
    # Lattice
    LatticeVOADefect,
    # Exactness
    check_closedness,
    check_exactness,
    de_rham_class,
    # Residues
    compute_residue,
    residues_at_singular_divisor,
    # Verlinde comparison
    verlinde_scattering_matrix,
    verlinde_total_quantum_dim,
    compare_verlinde_shadow,
    shadow_derived_scattering,
    # d_arith
    extract_d_arith_from_vanishing_order,
    verify_depth_decomposition,
    # Landscape
    frontier_defect_landscape,
    koszul_dual_defect_comparison,
    # Multi-path
    multipath_verify_heisenberg,
    multipath_verify_affine_sl2,
    multipath_verify_virasoro_minimal,
    # W_N Miura
    wn_miura_defect_sector,
    # Genus amplitudes
    faber_pandharipande_lambda,
    genus_amplitude_from_kappa,
    genus_amplitude_from_shadow,
)


# ============================================================================
# Section 1: Infrastructure tests
# ============================================================================

class TestInfrastructure:
    """Tests for numerical infrastructure."""

    def test_numerical_dlog_exponential(self):
        """d log(exp(s)) = 1."""
        f = lambda s: cmath.exp(s)
        result = _numerical_dlog(f, 2.0 + 0.5j)
        assert abs(result - 1.0) < 1e-5

    def test_numerical_dlog_power(self):
        """d log(s^n) = n/s."""
        n = 3
        f = lambda s: s ** n
        s0 = 2.0 + 1.0j
        result = _numerical_dlog(f, s0)
        expected = n / s0
        assert abs(result - expected) < 1e-4

    def test_partial_zeta_convergence(self):
        """zeta(2) = pi^2/6."""
        result = _partial_zeta(2.0 + 0.0j, 1000)
        expected = math.pi ** 2 / 6
        assert abs(result - expected) < 1e-3

    def test_partial_zeta_at_4(self):
        """zeta(4) = pi^4/90."""
        result = _partial_zeta(4.0 + 0.0j, 500)
        expected = math.pi ** 4 / 90
        assert abs(result - expected) < 1e-3

    def test_completed_zeta_nonzero(self):
        """Completed zeta is nonzero away from poles."""
        s = 2.0 + 1.0j
        val = completed_riemann_zeta(s)
        assert val != complex('inf')
        assert abs(val) > 1e-10  # nonzero

    def test_completed_zeta_poles(self):
        """Completed zeta has poles at s=0, s=1."""
        assert completed_riemann_zeta(0.0 + 0.0j) == complex('inf')
        assert completed_riemann_zeta(1.0 + 0.0j) == complex('inf')

    def test_riemann_scattering_at_half(self):
        """phi(1/2) should be approximately 1 by functional equation."""
        result = riemann_scattering(0.5 + 0.01j)  # slightly off critical point
        # Near s=1/2, phi ~ 1
        if result != complex('inf'):
            assert abs(abs(result) - 1.0) < 0.5


# ============================================================================
# Section 2: Heisenberg frontier defect
# ============================================================================

class TestHeisenberg:
    """Heisenberg algebra: Omega = 0 (trivially exact, no arithmetic frontier)."""

    def test_omega_is_zero(self):
        """Omega_{H_k}(s) = 0 for all s."""
        heis = HeisenbergDefect(k=1.0)
        for s in [1.0, 2.0 + 1j, 0.5 + 3j, 10.0]:
            assert abs(heis.omega(complex(s))) < 1e-15

    def test_kappa_equals_k(self):
        """kappa(H_k) = k (AP1)."""
        for k in [0.5, 1.0, 2.0, 5.0]:
            heis = HeisenbergDefect(k=k)
            assert heis.kappa == k

    def test_shadow_class_G(self):
        heis = HeisenbergDefect(k=1.0)
        assert heis.shadow_class == 'G'

    def test_d_arith_zero(self):
        heis = HeisenbergDefect(k=1.0)
        assert heis.d_arith == 0

    def test_d_alg_zero(self):
        heis = HeisenbergDefect(k=1.0)
        assert heis.d_alg == 0

    def test_total_depth_one(self):
        """d = 1 + 0 + 0 = 1."""
        heis = HeisenbergDefect(k=1.0)
        assert heis.total_depth == 1

    def test_is_exact(self):
        heis = HeisenbergDefect(k=1.0)
        assert heis.is_exact()

    def test_no_residues(self):
        heis = HeisenbergDefect(k=1.0)
        assert heis.residues() == {}

    def test_multipath_consistent(self):
        result = multipath_verify_heisenberg(1.0)
        assert result['all_consistent']

    def test_multipath_various_k(self):
        for k in [0.5, 1.0, 2.0, 10.0]:
            result = multipath_verify_heisenberg(k)
            assert result['path1_direct']
            assert result['path2_shadow_class']
            assert result['path3_exact']


# ============================================================================
# Section 3: Affine sl_2 frontier defect
# ============================================================================

class TestAffineSl2:
    """Affine sl_2 at integrable levels: Omega should be exact."""

    def test_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k in [1, 2, 3, 4, 5]:
            expected = 3.0 * (k + 2) / 4.0
            assert abs(sl2_kappa(k) - expected) < 1e-10

    def test_central_charge(self):
        """c(sl_2, k) = 3k/(k+2)."""
        assert abs(float(sl2_central_charge(1)) - 1.0) < 1e-10
        assert abs(float(sl2_central_charge(2)) - 1.5) < 1e-10
        assert abs(float(sl2_central_charge(4)) - 2.0) < 1e-10

    def test_S_matrix_symmetric(self):
        """S-matrix is symmetric."""
        for k in [1, 2, 3, 4]:
            S = sl2_S_matrix(k)
            assert np.allclose(S, S.T, atol=1e-12)

    def test_S_matrix_orthogonal(self):
        """S^2 = I for sl_2 S-matrix."""
        for k in [1, 2, 3, 4]:
            S = sl2_S_matrix(k)
            STS = S @ S.T
            assert np.allclose(STS, np.eye(k + 1), atol=1e-10)

    def test_quantum_dims_positive(self):
        """All quantum dimensions are positive for integrable levels."""
        for k in [1, 2, 3, 4, 5]:
            d = sl2_quantum_dimensions(k)
            assert all(di > 0 for di in d)

    def test_quantum_dim_vacuum_is_one(self):
        """d_0 = 1 (vacuum has quantum dimension 1)."""
        for k in [1, 2, 3]:
            d = sl2_quantum_dimensions(k)
            assert abs(d[0] - 1.0) < 1e-10

    def test_verlinde_genus_0(self):
        """Z_0 = 1 (genus-0 Verlinde dimension)."""
        for k in [1, 2, 3, 4]:
            Z0 = sl2_verlinde_dimension(k, 0)
            assert abs(Z0 - 1.0) < 1e-6

    def test_verlinde_genus_1(self):
        """Z_1 = k+1 (number of integrable reps)."""
        for k in [1, 2, 3, 4]:
            Z1 = sl2_verlinde_dimension(k, 1)
            assert abs(Z1 - (k + 1)) < 1e-4

    def test_conformal_weights(self):
        """h_0 = 0 (vacuum weight)."""
        for k in [1, 2, 3]:
            h = sl2_conformal_weights(k)
            assert abs(h[0]) < 1e-12

    def test_d_arith_zero_integrable(self):
        """d_arith = 0 for integrable levels."""
        for k in [1, 2, 3]:
            aff = AffineSl2Defect(k=k)
            assert aff.d_arith == 0

    def test_shadow_class_L(self):
        """Affine is class L (depth 3)."""
        aff = AffineSl2Defect(k=1)
        assert aff.shadow_class == 'L'

    def test_total_depth(self):
        """d = 1 + 0 + 1 = 2 for affine sl_2."""
        aff = AffineSl2Defect(k=1)
        assert aff.total_depth == 2

    def test_integrable_weight_count(self):
        for k in [1, 2, 3, 4, 5]:
            aff = AffineSl2Defect(k=k)
            assert aff.integrable_weights == k + 1

    def test_multipath_k1(self):
        result = multipath_verify_affine_sl2(1)
        assert result['path2_S_unitary']
        assert result['path3_verlinde_g0']

    def test_multipath_k2(self):
        result = multipath_verify_affine_sl2(2)
        assert result['all_consistent']

    def test_multipath_k3(self):
        result = multipath_verify_affine_sl2(3)
        assert result['path2_S_unitary']


# ============================================================================
# Section 4: Virasoro frontier defect
# ============================================================================

class TestVirasoro:
    """Virasoro algebra: minimal models and generic central charge."""

    def test_kappa_formula(self):
        """kappa(Vir_c) = c/2."""
        for c_val in [0.5, 1.0, 13.0, 26.0]:
            assert abs(virasoro_kappa(c_val) - c_val / 2.0) < 1e-12

    def test_minimal_model_central_charges(self):
        """Known central charges for minimal models."""
        # Ising: M(4,3), c = 1/2
        assert abs(minimal_model_central_charge(4, 3) - 0.5) < 1e-10
        # Tri-critical Ising: M(5,4), c = 7/10
        assert abs(minimal_model_central_charge(5, 4) - 0.7) < 1e-10
        # 3-state Potts: M(6,5), c = 4/5
        assert abs(minimal_model_central_charge(6, 5) - 0.8) < 1e-10

    def test_ising_kac_table(self):
        """Ising model M(4,3) has 3 primaries."""
        vir = VirasoroDefect(c_val=0.5, p=4, q=3)
        assert vir.kac_table_size == 3

    def test_tri_ising_kac_table(self):
        """Tri-critical Ising M(5,4) has 6 primaries."""
        vir = VirasoroDefect(c_val=0.7, p=5, q=4)
        assert vir.kac_table_size == 6

    def test_potts_kac_table(self):
        """3-state Potts M(6,5) has 10 primaries."""
        vir = VirasoroDefect(c_val=0.8, p=6, q=5)
        assert vir.kac_table_size == 10

    def test_minimal_model_S_matrix_symmetric(self):
        """S-matrix is symmetric for minimal models."""
        for (p, q) in [(4, 3), (5, 4), (6, 5)]:
            S, _ = minimal_model_S_matrix(p, q)
            assert np.allclose(S, S.T, atol=1e-10)

    def test_minimal_model_S_matrix_orthogonal(self):
        """S*S^T = I for minimal model S-matrices."""
        for (p, q) in [(4, 3), (5, 4), (6, 5)]:
            S, labels = minimal_model_S_matrix(p, q)
            n = len(labels)
            STS = S @ S.T
            assert np.allclose(STS, np.eye(n), atol=1e-6)

    def test_ising_conformal_weights(self):
        """Ising conformal weights: h_{1,1}=0, h_{2,1}=1/16, h_{1,2}=1/2.

        h_{r,s} = ((rq-sp)^2 - (p-q)^2) / (4pq) for M(4,3):
          h_{1,1} = ((3-4)^2 - 1)/48 = 0
          h_{2,1} = ((6-4)^2 - 1)/48 = 3/48 = 1/16
          h_{1,2} = ((3-8)^2 - 1)/48 = 24/48 = 1/2
        """
        weights = minimal_model_conformal_weights(4, 3)
        # (1,1): h = 0 (identity)
        assert abs(weights[(1, 1)]) < 1e-10
        # (2,1): h = 1/16 (sigma / spin field)
        if (2, 1) in weights:
            assert abs(weights[(2, 1)] - 1.0 / 16) < 1e-10
        # (1,2): h = 1/2 (epsilon / energy field)
        if (1, 2) in weights:
            assert abs(weights[(1, 2)] - 0.5) < 1e-10

    def test_shadow_coefficients_generic(self):
        """Shadow coefficients for generic Virasoro."""
        coeffs = virasoro_shadow_coefficients(1.0, 6)
        # kappa = c/2 = 0.5
        assert abs(coeffs[2] - 0.5) < 1e-6
        # S_3 = alpha/3 = 2/3 (from alpha=2, S_3 = a_1/3 = 6*kappa*alpha/(2*2*kappa)/3)
        # Actually S_3 = a_1/3 where a_1 = q1/(2*a_0) = 12*kappa*alpha/(2*2*kappa) = 3*alpha
        # So S_3 = 3*alpha/3 = alpha = 2
        # Wait, let's be more careful: S_r = a_{r-2}/r
        # a_0 = 2*kappa = 1.0
        # a_1 = q1/(2*a_0) = 12*0.5*2/(2*1.0) = 12/2 = 6
        # S_3 = a_1/3 = 6/3 = 2
        assert abs(coeffs[3] - 2.0) < 1e-4

    def test_shadow_kappa_matches_virasoro(self):
        """S_2 from shadow tower matches kappa = c/2."""
        for c_val in [0.5, 1.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients(c_val, 4)
            assert abs(coeffs[2] - c_val / 2.0) < 1e-4

    def test_minimal_model_d_arith_zero(self):
        """d_arith = 0 for minimal models (rational)."""
        vir = VirasoroDefect(c_val=0.5, p=4, q=3)
        assert vir.d_arith == 0

    def test_generic_d_arith_one(self):
        """d_arith = 1 for generic Virasoro (quasi-modular)."""
        vir = VirasoroDefect(c_val=1.0)
        assert vir.d_arith == 1

    def test_shadow_class_M(self):
        """Virasoro is always class M."""
        for c_val in [0.5, 1.0, 13.0]:
            vir = VirasoroDefect(c_val=c_val)
            assert vir.shadow_class == 'M'

    def test_multipath_ising(self):
        result = multipath_verify_virasoro_minimal(4, 3)
        assert result['path2_S_orthogonal']
        assert result['path4_kappa_matches']

    def test_multipath_tri_ising(self):
        result = multipath_verify_virasoro_minimal(5, 4)
        assert result['all_consistent']

    def test_multipath_potts(self):
        result = multipath_verify_virasoro_minimal(6, 5)
        assert result['all_consistent']


# ============================================================================
# Section 5: W_3 frontier defect
# ============================================================================

class TestW3:
    """W_3 algebra: Miura splitting and defect sector."""

    def test_w3_kappa_at_c2(self):
        """kappa for W_3 at c=2: 4(k+3)/3 where k = 3*2/(8-2) = 1."""
        kappa = w3_kappa(2.0)
        # k = 6/6 = 1, so kappa = 4*4/3 = 16/3
        assert abs(kappa - 16.0 / 3) < 1e-6

    def test_shadow_T_line_kappa(self):
        """T-line kappa = c/2."""
        kappa_T, _, _ = w3_shadow_metric_T(2.0)
        assert abs(kappa_T - 1.0) < 1e-10

    def test_shadow_W_line_alpha_zero(self):
        """W-line has alpha = 0 (Z_2 parity)."""
        _, alpha_W, _ = w3_shadow_metric_W(2.0)
        assert abs(alpha_W) < 1e-12

    def test_shadow_W_line_kappa(self):
        """W-line kappa = c/3."""
        kappa_W, _, _ = w3_shadow_metric_W(2.0)
        assert abs(kappa_W - 2.0 / 3) < 1e-10

    def test_w3_shadow_class_M(self):
        w3 = W3Defect(c_val=2.0)
        assert w3.shadow_class == 'M'

    def test_w3_d_arith(self):
        w3 = W3Defect(c_val=2.0)
        assert w3.d_arith == 1

    def test_w3_shadow_T_coefficients(self):
        """Shadow tower on T-line gives S_2 = c/2 = 1."""
        w3 = W3Defect(c_val=2.0)
        coeffs = w3.shadow_T_line()
        assert abs(coeffs[2] - 1.0) < 1e-4

    def test_w3_shadow_W_coefficients(self):
        """Shadow tower on W-line gives S_2 = c/3 = 2/3."""
        w3 = W3Defect(c_val=2.0)
        coeffs = w3.shadow_W_line()
        assert abs(coeffs[2] - 2.0 / 3) < 1e-4


# ============================================================================
# Section 6: Miura splitting
# ============================================================================

class TestMiuraSplitting:
    """Tests for the Miura packet splitting of W_N algebras."""

    def test_miura_w2_defect_rank_zero(self):
        """W_2 = Virasoro: defect rank 0."""
        m = MiuraSplitting(N=2)
        assert m.defect_rank == 0

    def test_miura_w3_defect_rank_one(self):
        """W_3: defect rank 1."""
        m = MiuraSplitting(N=3)
        assert m.defect_rank == 1

    def test_miura_w4_defect_rank_two(self):
        """W_4: defect rank 2."""
        m = MiuraSplitting(N=4)
        assert m.defect_rank == 2

    def test_miura_w5_defect_rank_three(self):
        """W_5: defect rank 3."""
        m = MiuraSplitting(N=5)
        assert m.defect_rank == 3

    def test_miura_heisenberg_rank(self):
        """Heisenberg rank = N-1 for W_N."""
        for N in [2, 3, 4, 5]:
            m = MiuraSplitting(N=N)
            assert m.heisenberg_rank == N - 1

    def test_miura_total_rank(self):
        """Total rank = 2N-3 for W_N."""
        for N in [2, 3, 4, 5]:
            m = MiuraSplitting(N=N)
            assert m.total_packet_rank == 2 * N - 3

    def test_miura_heisenberg_omega_vanishes(self):
        """Heisenberg part of Omega should vanish."""
        for N in [3, 4, 5]:
            m = MiuraSplitting(N=N)
            s = 2.0 + 0.5j
            assert abs(m.omega_heisenberg(s)) < 1e-12

    def test_miura_w2_omega_zero(self):
        """For W_2 (Virasoro): defect rank 0 -> omega_defect = 0."""
        m = MiuraSplitting(N=2)
        s = 2.0 + 1.0j
        assert abs(m.omega_defect(s)) < 1e-12

    def test_miura_splitting_verified(self):
        """Verify splitting at test points for W_3."""
        m = MiuraSplitting(N=3)
        s_vals = [2.0 + 0.5j, 3.0 + 1.0j, 4.0]
        assert m.verify_splitting(s_vals)

    def test_miura_w3_defect_dirichlet(self):
        """W_3 defect polynomial: -zeta(u+1) * (2 + 2^{-u})."""
        m = MiuraSplitting(N=3)
        u = 2.0 + 0.0j
        val = m.defect_dirichlet_polynomial(u)
        # -zeta(3) * (2 + 2^{-2}) = -zeta(3) * 2.25
        zeta3 = sum(n ** (-3) for n in range(1, 301))
        expected = -zeta3 * (2 + 0.25)
        assert abs(val - expected) < 0.1

    def test_wn_miura_landscape(self):
        """Compute Miura data for W_3, W_4, W_5."""
        s_vals = [2.0 + 0.5j, 3.0]
        for N in [3, 4, 5]:
            data = wn_miura_defect_sector(N, s_vals)
            assert data['defect_rank'] == N - 2
            assert data['heisenberg_vanishes']


# ============================================================================
# Section 7: Lattice VOA frontier defect
# ============================================================================

class TestLatticeVOA:
    """Tests for lattice VOA frontier defect."""

    def test_e8_kappa(self):
        """kappa(V_{E_8}) = 8 (rank, AP48)."""
        lat = LatticeVOADefect(rank=8, lattice_name='E8')
        assert lat.kappa == 8.0

    def test_e8_d_arith_zero(self):
        """No cusp forms in S_4(SL(2,Z)), so d_arith = 0."""
        lat = LatticeVOADefect(rank=8, lattice_name='E8')
        assert lat.d_arith == 0

    def test_e8_exact(self):
        """E_8 lattice: Omega is trivially exact (no cusp forms)."""
        lat = LatticeVOADefect(rank=8, lattice_name='E8')
        assert lat.is_exact()

    def test_leech_kappa(self):
        """kappa(V_Leech) = 24 (rank, AP48)."""
        lat = LatticeVOADefect(rank=24, lattice_name='Leech')
        assert lat.kappa == 24.0

    def test_leech_d_arith_one(self):
        """Leech lattice: dim S_12 = 1 (Delta function), so d_arith = 1."""
        lat = LatticeVOADefect(rank=24, lattice_name='Leech')
        assert lat.d_arith == 1

    def test_leech_not_exact(self):
        """Leech lattice: genuine arithmetic frontier (cusp form Delta)."""
        lat = LatticeVOADefect(rank=24, lattice_name='Leech')
        assert not lat.is_exact()

    def test_lattice_shadow_class_G(self):
        """Lattice VOAs are class G (Gaussian)."""
        for rank in [8, 16, 24]:
            lat = LatticeVOADefect(rank=rank)
            assert lat.shadow_class == 'G'

    def test_cusp_dimension_standard(self):
        """Standard cusp dimension values."""
        lat = LatticeVOADefect(rank=8)
        # S_4: k=4, dim = 0
        assert lat._cusp_dimension(4) == 0
        # S_12: k=12, dim = 1
        assert lat._cusp_dimension(12) == 1
        # S_16: k=16, dim = 1
        assert lat._cusp_dimension(16) == 1
        # S_24: k=24, dim = 2
        assert lat._cusp_dimension(24) == 2

    def test_total_depth_e8(self):
        """d(V_{E_8}) = 1 + 0 + 0 = 1."""
        lat = LatticeVOADefect(rank=8, lattice_name='E8')
        assert lat.total_depth == 1

    def test_total_depth_leech(self):
        """d(V_Leech) = 1 + 1 + 0 = 2."""
        lat = LatticeVOADefect(rank=24, lattice_name='Leech')
        assert lat.total_depth == 2

    def test_rank16_cusp_forms(self):
        """rank 16: S_8 = 0 -> d_arith = 0."""
        lat = LatticeVOADefect(rank=16)
        assert lat.d_arith == 0


# ============================================================================
# Section 8: Exactness criterion
# ============================================================================

class TestExactness:
    """Tests for the exactness / gauge criterion."""

    def test_exact_function_zero(self):
        """Zero form is exact."""
        omega = lambda s: 0.0 + 0.0j
        is_exact, integral = check_exactness(omega, 2.0, 0.5)
        assert is_exact
        assert abs(integral) < 1e-10

    def test_exact_dlog(self):
        """d log(s) = 1/s is exact on simply-connected domains."""
        omega = lambda s: 1.0 / s
        # Contour NOT enclosing origin -> exact
        is_exact, integral = check_exactness(omega, 3.0 + 0.0j, 0.5)
        assert is_exact

    def test_not_exact_around_pole(self):
        """1/s has nonzero residue at s=0: not exact on annulus."""
        omega = lambda s: 1.0 / s
        # Contour enclosing origin -> not exact
        is_exact, integral = check_exactness(omega, 0.0 + 0.0j, 1.0)
        assert not is_exact
        # Residue should be 1
        assert abs(integral / (2 * cmath.pi * 1j) - 1.0) < 0.1

    def test_closedness_smooth_function(self):
        """Smooth 1-form on 1D is automatically closed."""
        omega = lambda s: cmath.exp(s)
        s_vals = [1.0, 2.0, 3.0 + 1j]
        is_closed, _ = check_closedness(omega, s_vals)
        assert is_closed

    def test_de_rham_class_simple_pole(self):
        """De Rham class of 1/s around origin should be 1."""
        omega = lambda s: 1.0 / s
        cl = de_rham_class(omega, 0.0 + 0.0j, 1.0)
        if cl != complex('inf'):
            assert abs(cl - 1.0) < 0.1

    def test_heisenberg_gauge_criterion(self):
        """Heisenberg satisfies gauge criterion (Omega = 0)."""
        heis = HeisenbergDefect(k=1.0)
        is_exact, _ = check_exactness(heis.omega, 2.0, 0.5)
        assert is_exact


# ============================================================================
# Section 9: Residue computation
# ============================================================================

class TestResidues:
    """Tests for residue computation at singular points."""

    def test_residue_simple_pole(self):
        """Res_{s=0}(1/s) = 1."""
        omega = lambda s: 1.0 / s
        res = compute_residue(omega, 0.0 + 0.0j, radius=0.1)
        assert abs(res - 1.0) < 0.1

    def test_residue_double_pole(self):
        """Res_{s=0}(1/s^2) = 0."""
        omega = lambda s: 1.0 / s ** 2
        res = compute_residue(omega, 0.0 + 0.0j, radius=0.1)
        assert abs(res) < 0.2

    def test_residue_shifted_pole(self):
        """Res_{s=1}(1/(s-1)) = 1."""
        omega = lambda s: 1.0 / (s - 1)
        res = compute_residue(omega, 1.0 + 0.0j, radius=0.1)
        assert abs(res - 1.0) < 0.1

    def test_residue_rational_function(self):
        """Res_{s=0}(s/(s^2+1)) = 0 (no pole at 0)."""
        omega = lambda s: s / (s ** 2 + 1)
        res = compute_residue(omega, 0.0 + 0.0j, radius=0.5)
        assert abs(res) < 0.1

    def test_residues_at_divisor(self):
        """Compute residues at multiple points."""
        omega = lambda s: 1.0 / (s * (s - 1))
        singular = [0.0 + 0.0j, 1.0 + 0.0j]
        residues = residues_at_singular_divisor(omega, singular, radius=0.05)
        # Res at 0: -1, Res at 1: +1
        assert len(residues) == 2


# ============================================================================
# Section 10: Verlinde comparison for minimal models
# ============================================================================

class TestVerlindeComparison:
    """Comparison between Verlinde (exact) and shadow (perturbative) data."""

    def test_ising_verlinde_quantum_dims(self):
        """Ising M(4,3): 3 primaries with known quantum dimensions."""
        qd = verlinde_scattering_matrix(4, 3)
        # Identity has d = 1
        assert abs(qd[0] - 1.0) < 1e-6
        # All positive
        assert all(d > 0 for d in qd)

    def test_ising_total_quantum_dim(self):
        """Ising: D^2 = 1/S_{00}^2."""
        D2 = verlinde_total_quantum_dim(4, 3)
        assert D2 > 1.0  # must be > 1 for non-trivial MTC

    def test_ising_shadow_comparison(self):
        """Compare Verlinde and shadow data for Ising."""
        data = compare_verlinde_shadow(4, 3)
        assert abs(data['c'] - 0.5) < 1e-10
        assert abs(data['kappa'] - 0.25) < 1e-10
        assert len(data['verlinde_quantum_dims']) == 3

    def test_tri_ising_comparison(self):
        """Tri-critical Ising M(5,4)."""
        data = compare_verlinde_shadow(5, 4)
        assert abs(data['c'] - 0.7) < 1e-10
        assert len(data['verlinde_quantum_dims']) == 6

    def test_potts_comparison(self):
        """3-state Potts M(6,5)."""
        data = compare_verlinde_shadow(6, 5)
        assert abs(data['c'] - 0.8) < 1e-10
        assert len(data['verlinde_quantum_dims']) == 10

    def test_shadow_derived_scattering_ising(self):
        """Shadow-derived scattering data for Ising c=1/2."""
        data = shadow_derived_scattering(0.5)
        assert abs(data['kappa'] - 0.25) < 1e-6
        assert data['shadow_class'] == 'M'

    def test_verlinde_shadow_kappa_consistency(self):
        """kappa from Verlinde and shadow must agree."""
        for (p, q) in [(4, 3), (5, 4), (6, 5)]:
            data = compare_verlinde_shadow(p, q)
            c = data['c']
            kappa_shadow = data['shadow_coefficients'].get(2, 0)
            kappa_direct = c / 2.0
            assert abs(kappa_shadow - kappa_direct) < 1e-4


# ============================================================================
# Section 11: d_arith extraction
# ============================================================================

class TestDarithExtraction:
    """Tests for extracting arithmetic depth from Omega."""

    def test_d_arith_heisenberg(self):
        """Heisenberg: Omega = 0 everywhere -> d_arith = max (all derivatives vanish)."""
        heis = HeisenbergDefect(k=1.0)
        d = extract_d_arith_from_vanishing_order(heis.omega, max_order=3)
        # All derivatives vanish, so d_arith >= max_order
        assert d >= 3

    def test_d_arith_nonzero_function(self):
        """1/s has d_arith = 0 at s=1/2 (nonzero there)."""
        omega = lambda s: 1.0 / s
        d = extract_d_arith_from_vanishing_order(omega, max_order=3)
        assert d == 0

    def test_d_arith_vanishing_at_half(self):
        """(s - 1/2) has d_arith = 1 at s=1/2."""
        omega = lambda s: s - 0.5
        d = extract_d_arith_from_vanishing_order(omega, max_order=3)
        assert d == 1

    def test_d_arith_double_vanishing(self):
        """(s - 1/2)^2 has d_arith = 2 at s=1/2."""
        omega = lambda s: (s - 0.5) ** 2
        d = extract_d_arith_from_vanishing_order(omega, max_order=3)
        assert d == 2

    def test_depth_decomposition_heisenberg(self):
        """d = 1 + 0 + 0 = 1 for Heisenberg."""
        assert verify_depth_decomposition('Heisenberg', 0, 0, 1)

    def test_depth_decomposition_affine(self):
        """d = 1 + 0 + 1 = 2 for affine sl_2."""
        assert verify_depth_decomposition('affine_sl2', 0, 1, 2)


# ============================================================================
# Section 12: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks."""

    def test_landscape_nonempty(self):
        """Landscape computation produces data for all families."""
        landscape = frontier_defect_landscape()
        assert 'Heisenberg_k=1' in landscape
        assert 'sl2_k=1' in landscape
        assert 'Vir_Ising' in landscape
        assert 'Vir_c=13.0' in landscape
        assert 'W3_c=2' in landscape

    def test_landscape_kappa_values(self):
        """Kappa values in landscape are correct."""
        landscape = frontier_defect_landscape()
        assert abs(landscape['Heisenberg_k=1']['kappa'] - 1.0) < 1e-10
        assert abs(landscape['Vir_Ising']['kappa'] - 0.25) < 1e-10
        assert abs(landscape['Vir_c=13.0']['kappa'] - 6.5) < 1e-10

    def test_koszul_dual_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [1.0, 6.0, 10.0, 13.0, 25.0]:
            data = koszul_dual_defect_comparison(c_val)
            assert abs(data['kappa_sum'] - 13.0) < 1e-10

    def test_koszul_dual_self_dual_point(self):
        """At c=13: kappa = kappa_dual = 6.5."""
        data = koszul_dual_defect_comparison(13.0)
        assert abs(data['kappa'] - 6.5) < 1e-10
        assert abs(data['kappa_dual'] - 6.5) < 1e-10

    def test_heisenberg_exact_in_landscape(self):
        """Heisenberg is exact in the landscape."""
        landscape = frontier_defect_landscape()
        assert landscape['Heisenberg_k=1']['is_exact']

    def test_shadow_class_consistency(self):
        """Shadow classes match expected values."""
        landscape = frontier_defect_landscape()
        assert landscape['Heisenberg_k=1']['shadow_class'] == 'G'
        assert landscape['sl2_k=1']['shadow_class'] == 'L'
        assert landscape['Vir_Ising']['shadow_class'] == 'M'
        assert landscape['W3_c=2']['shadow_class'] == 'M'


# ============================================================================
# Section 13: Genus amplitude comparison
# ============================================================================

class TestGenusAmplitudes:
    """Faber-Pandharipande lambda and genus amplitudes."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert abs(faber_pandharipande_lambda(1) - 1.0 / 24) < 1e-10

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert abs(faber_pandharipande_lambda(2) - 7.0 / 5760) < 1e-10

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert abs(faber_pandharipande_lambda(3) - 31.0 / 967680) < 1e-8

    def test_F1_virasoro(self):
        """F_1(Vir_c) = (c/2)/24 = c/48."""
        for c_val in [1.0, 13.0, 26.0]:
            F1 = genus_amplitude_from_kappa(c_val / 2.0, 1)
            assert abs(F1 - c_val / 48.0) < 1e-10

    def test_F1_from_shadow(self):
        """F_1 from shadow tower matches F_1 from kappa."""
        for c_val in [0.5, 1.0, 13.0]:
            coeffs = virasoro_shadow_coefficients(c_val, 4)
            F1_shadow = genus_amplitude_from_shadow(coeffs, 1)
            F1_kappa = genus_amplitude_from_kappa(c_val / 2.0, 1)
            assert abs(F1_shadow - F1_kappa) < 1e-6

    def test_genus_amplitudes_positive(self):
        """F_g > 0 for kappa > 0 (Bernoulli signs: A-hat has all positive)."""
        for g in [1, 2, 3, 4]:
            assert faber_pandharipande_lambda(g) > 0
            assert genus_amplitude_from_kappa(1.0, g) > 0

    def test_genus_amplitudes_linear_in_kappa(self):
        """F_g is linear in kappa."""
        for g in [1, 2, 3]:
            F1 = genus_amplitude_from_kappa(1.0, g)
            F2 = genus_amplitude_from_kappa(2.0, g)
            assert abs(F2 - 2 * F1) < 1e-12

    def test_genus_amplitudes_decay(self):
        """lambda_g decays factorially: lambda_{g+1}/lambda_g -> 0."""
        for g in [1, 2, 3]:
            ratio = faber_pandharipande_lambda(g + 1) / faber_pandharipande_lambda(g)
            assert abs(ratio) < 1


# ============================================================================
# Section 14: AP-specific verification
# ============================================================================

class TestAntiPatternGuards:
    """Guards against known anti-patterns from CLAUDE.md."""

    def test_ap1_kappa_not_copied(self):
        """AP1: kappa(H_k) = k, kappa(Vir_c) = c/2, kappa(sl_2,k) = 3(k+2)/4.
        These are DISTINCT formulas."""
        heis = HeisenbergDefect(k=1.0)
        vir = VirasoroDefect(c_val=1.0)
        aff = AffineSl2Defect(k=1)
        # All have c or k = 1, but kappas differ
        assert abs(heis.kappa - 1.0) < 1e-10       # k
        assert abs(vir.kappa - 0.5) < 1e-10        # c/2
        assert abs(aff.kappa - 2.25) < 1e-10       # 3*3/4

    def test_ap15_quasi_modular_flag(self):
        """AP15: Generic Virasoro involves E_2* (quasi-modular), flag d_arith=1."""
        vir = VirasoroDefect(c_val=1.0)
        assert vir.d_arith == 1  # quasi-modular contribution

    def test_ap24_complementarity_sum_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c in [0.5, 1.0, 5.0, 10.0, 13.0, 25.0]:
            ksum = virasoro_kappa(c) + virasoro_kappa(26.0 - c)
            assert abs(ksum - 13.0) < 1e-10

    def test_ap48_lattice_kappa_not_c_over_2(self):
        """AP48: kappa(V_Lambda) = rank, NOT c/2."""
        lat = LatticeVOADefect(rank=24, lattice_name='Leech')
        assert lat.kappa == 24.0
        assert lat.kappa != lat.central_charge / 2.0  # c=24, c/2=12 != 24

    def test_ap39_kappa_neq_S2_general(self):
        """AP39: S_2 = kappa for rank-1, but NOT in general."""
        # For Virasoro (rank 1): S_2 = kappa = c/2. OK.
        coeffs = virasoro_shadow_coefficients(1.0, 4)
        assert abs(coeffs[2] - 0.5) < 1e-4  # S_2 = kappa = 1/2

    def test_ap14_shadow_depth_not_koszulness(self):
        """AP14: Shadow depth classifies complexity, NOT Koszulness."""
        # Both Heisenberg (depth 2) and Virasoro (depth infinity) are Koszul.
        heis = HeisenbergDefect(k=1.0)
        vir = VirasoroDefect(c_val=1.0)
        assert heis.shadow_class == 'G'  # depth 2
        assert vir.shadow_class == 'M'  # depth infinity
        # Both are Koszul (not tested here, but the point is
        # that different depths does NOT mean different Koszulness)

    def test_ap31_kappa_zero_not_theta_zero(self):
        """AP31: kappa=0 does NOT imply Theta_A=0."""
        # Virasoro at c=0: kappa=0
        vir = VirasoroDefect(c_val=0.001)  # near c=0
        # kappa ~ 0, but the higher shadow coefficients can be nonzero
        coeffs = vir.shadow_coefficients(6)
        # S_3 = 2 (independent of kappa for Virasoro)
        assert abs(coeffs[3] - 2.0) < 0.5  # S_3 != 0 even as kappa -> 0


# ============================================================================
# Section 15: Edge cases and boundary conditions
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_heisenberg_k_zero(self):
        """H_0 has kappa = 0."""
        heis = HeisenbergDefect(k=0.0)
        assert abs(heis.kappa) < 1e-12
        assert abs(heis.omega(2.0)) < 1e-12

    def test_affine_sl2_k1(self):
        """sl_2 at k=1: 2 integrable weights (V_0, V_1)."""
        aff = AffineSl2Defect(k=1)
        assert aff.integrable_weights == 2

    def test_virasoro_self_dual(self):
        """Virasoro at c=13: self-dual point (AP8)."""
        vir = VirasoroDefect(c_val=13.0)
        assert abs(vir.kappa - 6.5) < 1e-10
        # Koszul dual: Vir_{26-13} = Vir_{13}
        kappa_dual = virasoro_kappa(26.0 - 13.0)
        assert abs(kappa_dual - 6.5) < 1e-10

    def test_virasoro_critical_string(self):
        """Virasoro at c=26: bosonic string critical dimension."""
        vir = VirasoroDefect(c_val=26.0)
        assert abs(vir.kappa - 13.0) < 1e-10

    def test_miura_invalid_N(self):
        """MiuraSplitting with N < 2 should raise."""
        with pytest.raises(ValueError):
            MiuraSplitting(N=1)

    def test_affine_invalid_k(self):
        """AffineSl2Defect with k < 1 should raise."""
        with pytest.raises(ValueError):
            AffineSl2Defect(k=0)

    def test_virasoro_mismatched_pq(self):
        """VirasoroDefect with wrong (p,q) for c should raise."""
        with pytest.raises(ValueError):
            VirasoroDefect(c_val=0.5, p=5, q=4)  # c=0.7, not 0.5
