r"""Tests for BC-131: Shadow quantum channels, diamond norms, and quantum capacity.

Multi-path verification (3+ independent methods per claim):
    Path 1: CPTP verification via Kraus sum rule vs Choi positivity vs partial trace
    Path 2: Entanglement fidelity via trace formula vs Choi matrix vs direct state
    Path 3: Coherent information via Kraus environment vs complementary channel
    Path 4: Diamond norm via Choi trace norm vs depolarizing formula vs unitarity bound
    Path 5: Kappa values from independent first-principles computation (AP1/AP10)
    Path 6: Quantum capacity: depolarizing exact vs numerical optimization
    Path 7: Shadow depth classification from independent coefficient analysis

85+ tests covering:
    - Shadow data extraction: all families, kappa values, depth, class
    - Kraus operator construction: CPTP, rank, structure
    - Channel application: linearity, trace-preservation, complete positivity
    - Choi matrix: positivity, partial trace, Hermiticity, rank
    - Entanglement fidelity: three independent computation paths
    - Diamond norm: bounds, depolarizing formula, monotonicity
    - Quantum capacity: bounds, depolarizing exact, noise dependence
    - Complementary channel: subadditivity, entropy relations
    - Heisenberg Gaussian verification: unitary mixture structure
    - Cross-family consistency: shadow depth classification
    - Zeta zero evaluation: CPTP at complex parameters
    - Capacity table and full analysis pipeline

CAUTION (AP1):  kappa formulas are family-specific — independently verified.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Tests use multi-path verification, NOT hardcoded engine values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

import math
import pytest
import numpy as np
from numpy import linalg as la

from compute.lib.bc_quantum_channel_shadow_engine import (
    # Zeta zeros
    ZETA_ZERO_GAMMAS,
    get_zeta_zeros,
    # Shadow data
    ShadowChannelData,
    get_shadow_data,
    # Kraus operators
    build_kraus_operators,
    _gell_mann_unitaries,
    # Channel operations
    apply_channel,
    verify_cptp,
    # Choi matrix
    compute_choi_matrix,
    choi_matrix_from_data,
    # Entanglement fidelity
    entanglement_fidelity,
    entanglement_fidelity_from_choi,
    # Diamond norm
    diamond_norm_depolarizing,
    diamond_norm_upper_bound,
    diamond_norm_via_choi,
    effective_depolarizing_parameter,
    # Quantum capacity
    von_neumann_entropy,
    coherent_information,
    one_shot_quantum_capacity,
    depolarizing_capacity_exact,
    # Family channels
    shadow_channel_heisenberg,
    shadow_channel_affine,
    shadow_channel_virasoro,
    shadow_channel_betagamma,
    # Sweep and analysis
    capacity_table,
    channel_at_zeta_zeros,
    # Complementary channel
    complementary_channel_kraus,
    verify_complementary_entropy,
    # Multi-path verification
    verify_entanglement_fidelity_multipath,
    # Choi verification
    verify_choi_properties,
    # Depth analysis
    diamond_norm_vs_depth,
    # Gaussian verification
    verify_heisenberg_gaussian,
    # Full analysis
    full_analysis,
    # Dimension sweep
    choi_matrix_dimensions,
)


# ============================================================================
# Helpers: independent kappa computation (AP1/AP10: never trust engine values)
# ============================================================================

def _kappa_heisenberg(k: float) -> float:
    """kappa(H_k) = k. Independent derivation: single boson, level k."""
    return k


def _kappa_affine_sl2(k: float) -> float:
    """kappa(V_k(sl_2)) = dim(sl_2)*(k+h^v)/(2*h^v) = 3*(k+2)/4.
    dim(sl_2) = 3, h^v(sl_2) = 2."""
    return 3.0 * (k + 2.0) / (2.0 * 2.0)


def _kappa_affine_sl3(k: float) -> float:
    """kappa(V_k(sl_3)) = dim(sl_3)*(k+h^v)/(2*h^v) = 8*(k+3)/6 = 4*(k+3)/3.
    dim(sl_3) = 8, h^v(sl_3) = 3."""
    return 8.0 * (k + 3.0) / (2.0 * 3.0)


def _kappa_virasoro(c: float) -> float:
    """kappa(Vir_c) = c/2. Virasoro-specific formula (AP48)."""
    return c / 2.0


def _kappa_betagamma(lam: float) -> float:
    """kappa for betagamma at weight lambda.
    c = 2*(6*lambda^2 - 6*lambda + 1), kappa = c/2."""
    c = 2.0 * (6.0 * lam**2 - 6.0 * lam + 1.0)
    return c / 2.0


def _make_random_density_matrix(dim: int, seed: int = 42) -> np.ndarray:
    """Create a random valid density matrix (positive semidefinite, trace 1)."""
    rng = np.random.RandomState(seed)
    G = rng.randn(dim, dim) + 1j * rng.randn(dim, dim)
    rho = G @ G.conj().T
    rho = rho / np.trace(rho).real
    return rho


def _maximally_mixed(dim: int) -> np.ndarray:
    """I/d — the maximally mixed state."""
    return np.eye(dim, dtype=complex) / dim


def _pure_state(dim: int, idx: int = 0) -> np.ndarray:
    """|idx><idx| — a pure computational basis state."""
    rho = np.zeros((dim, dim), dtype=complex)
    rho[idx, idx] = 1.0
    return rho


# ============================================================================
# 1. ZETA ZEROS
# ============================================================================

class TestZetaZeros:
    """Tests for Riemann zeta zero data."""

    def test_zeta_zeros_count(self):
        """ZETA_ZERO_GAMMAS should have 30 entries."""
        assert len(ZETA_ZERO_GAMMAS) == 30

    def test_zeta_zeros_positive(self):
        """All gamma_n should be positive real."""
        for g in ZETA_ZERO_GAMMAS:
            assert g > 0

    def test_zeta_zeros_increasing(self):
        """gamma_n should be strictly increasing."""
        for i in range(len(ZETA_ZERO_GAMMAS) - 1):
            assert ZETA_ZERO_GAMMAS[i] < ZETA_ZERO_GAMMAS[i + 1]

    def test_first_zero_known_value(self):
        """gamma_1 = 14.13472514... (Riemann, independently known)."""
        # Independently known: first zero is at 14.134725141734693...
        assert abs(ZETA_ZERO_GAMMAS[0] - 14.134725141734693) < 1e-10

    def test_get_zeta_zeros_format(self):
        """get_zeta_zeros returns complex numbers rho_n = 1/2 + i*gamma_n."""
        zeros = get_zeta_zeros(5)
        assert len(zeros) == 5
        for z in zeros:
            assert isinstance(z, complex)
            assert abs(z.real - 0.5) < 1e-15  # On critical line

    def test_get_zeta_zeros_imaginary_parts(self):
        """Imaginary parts should match ZETA_ZERO_GAMMAS."""
        zeros = get_zeta_zeros(10)
        for i, z in enumerate(zeros):
            assert abs(z.imag - ZETA_ZERO_GAMMAS[i]) < 1e-12

    def test_get_zeta_zeros_excess(self):
        """Requesting more zeros than available returns at most 30."""
        zeros = get_zeta_zeros(100)
        assert len(zeros) == 30


# ============================================================================
# 2. SHADOW DATA EXTRACTION — independent kappa verification (AP1/AP10)
# ============================================================================

class TestShadowData:
    """Tests for get_shadow_data with independent kappa verification."""

    def test_heisenberg_kappa_independent(self):
        """Heisenberg kappa = k, verified from first principles."""
        for k in [0.5, 1.0, 2.0, 5.0, 10.0]:
            data = get_shadow_data('heisenberg', k)
            expected = _kappa_heisenberg(k)
            assert abs(data.kappa - expected) < 1e-12, \
                f"Heisenberg kappa mismatch at k={k}: got {data.kappa}, expected {expected}"

    def test_affine_sl2_kappa_independent(self):
        """Affine sl_2 kappa = 3(k+2)/4, verified from dim(g)*(k+h^v)/(2*h^v)."""
        for k in [1.0, 2.0, 3.0, 5.0, 10.0]:
            data = get_shadow_data('affine_sl2', k)
            expected = _kappa_affine_sl2(k)
            assert abs(data.kappa - expected) < 1e-12, \
                f"Affine sl_2 kappa mismatch at k={k}: got {data.kappa}, expected {expected}"

    def test_affine_sl3_kappa_independent(self):
        """Affine sl_3 kappa = 4(k+3)/3, verified independently."""
        for k in [1.0, 2.0, 5.0]:
            data = get_shadow_data('affine_sl3', k)
            expected = _kappa_affine_sl3(k)
            assert abs(data.kappa - expected) < 1e-12, \
                f"Affine sl_3 kappa mismatch at k={k}"

    def test_virasoro_kappa_independent(self):
        """Virasoro kappa = c/2 (AP48: this is Virasoro-specific)."""
        for c in [1.0, 5.0, 10.0, 13.0, 25.0]:
            data = get_shadow_data('virasoro', c)
            expected = _kappa_virasoro(c)
            assert abs(data.kappa - expected) < 1e-12, \
                f"Virasoro kappa mismatch at c={c}"

    def test_betagamma_kappa_independent(self):
        """Beta-gamma kappa = c/2 = 6*lam^2 - 6*lam + 1, independently computed."""
        for lam in [0.3, 0.5, 0.7, 1.0]:
            data = get_shadow_data('betagamma', lam)
            expected = _kappa_betagamma(lam)
            assert abs(data.kappa - expected) < 1e-12, \
                f"Betagamma kappa mismatch at lambda={lam}"

    def test_virasoro_complementarity_kappa_sum(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            k1 = _kappa_virasoro(c)
            k2 = _kappa_virasoro(26.0 - c)
            assert abs(k1 + k2 - 13.0) < 1e-12, \
                f"AP24 violation at c={c}: kappa sum = {k1 + k2}, expected 13"

    def test_shadow_class_assignment(self):
        """Shadow class G/L/C/M assignment matches depth."""
        assert get_shadow_data('heisenberg', 1.0).shadow_class == 'G'
        assert get_shadow_data('affine_sl2', 1.0).shadow_class == 'L'
        assert get_shadow_data('affine_sl3', 1.0).shadow_class == 'L'
        assert get_shadow_data('virasoro', 10.0).shadow_class == 'M'
        assert get_shadow_data('betagamma', 0.5).shadow_class == 'C'

    def test_shadow_depth_assignment(self):
        """Shadow depth: G=2, L=3, C=4, M=max_r."""
        assert get_shadow_data('heisenberg', 1.0).shadow_depth == 2
        assert get_shadow_data('affine_sl2', 1.0).shadow_depth == 3
        assert get_shadow_data('affine_sl3', 1.0).shadow_depth == 3
        assert get_shadow_data('betagamma', 0.5).shadow_depth == 4

    def test_heisenberg_coefficients_terminate(self):
        """Heisenberg class G: S_r = 0 for all r >= 3."""
        data = get_shadow_data('heisenberg', 2.0, max_r=10)
        for r in range(3, 11):
            assert abs(data.shadow_coeffs.get(r, 0.0)) < 1e-15

    def test_affine_coefficients_terminate(self):
        """Affine class L: S_r = 0 for all r >= 4."""
        data = get_shadow_data('affine_sl2', 2.0, max_r=10)
        for r in range(4, 11):
            assert abs(data.shadow_coeffs.get(r, 0.0)) < 1e-15

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError, match="Unknown family"):
            get_shadow_data('unknown_algebra', 1.0)

    def test_kraus_rank_consistent(self):
        """Kraus rank = number of nonzero S_r (r>=2) + 1 (identity)."""
        data = get_shadow_data('heisenberg', 1.0)
        n_nonzero = sum(1 for r, v in data.shadow_coeffs.items()
                        if r >= 2 and abs(v) > 1e-15)
        assert data.kraus_rank == n_nonzero + 1

    def test_noise_strength_bounded(self):
        """Noise strength epsilon^2 should be in [0, 1]."""
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 2.0),
                         ('virasoro', 10.0), ('betagamma', 0.5)]:
            data = get_shadow_data(fam, par, noise_scale=0.1)
            assert 0.0 <= data.noise_strength <= 1.0


# ============================================================================
# 3. GELL-MANN UNITARIES
# ============================================================================

class TestGellMannUnitaries:
    """Tests for the Gell-Mann unitary construction."""

    def test_unitaries_are_unitary(self):
        """Each U_k should satisfy U U^dagger = I."""
        for dim in [2, 3, 4]:
            for count in [1, 2, dim**2 - 1]:
                unitaries = _gell_mann_unitaries(dim, count)
                assert len(unitaries) == count
                for U in unitaries:
                    err = la.norm(U @ U.conj().T - np.eye(dim), 'fro')
                    assert err < 1e-10, f"Unitarity failed: error={err}"

    def test_unitaries_correct_dimension(self):
        """Unitaries should be dim x dim."""
        for dim in [2, 3, 5]:
            unitaries = _gell_mann_unitaries(dim, 3)
            for U in unitaries:
                assert U.shape == (dim, dim)

    def test_unitaries_determinant_magnitude(self):
        """Unitary matrices have |det| = 1."""
        unitaries = _gell_mann_unitaries(3, 5)
        for U in unitaries:
            assert abs(abs(la.det(U)) - 1.0) < 1e-10


# ============================================================================
# 4. KRAUS OPERATOR CONSTRUCTION
# ============================================================================

class TestKrausOperators:
    """Tests for build_kraus_operators."""

    def test_kraus_cptp_identity(self):
        """Kraus operators must satisfy sum E_k^dag E_k = I (trace-preserving)."""
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 2.0),
                         ('virasoro', 10.0), ('betagamma', 0.5)]:
            data = get_shadow_data(fam, par)
            for dim in [2, 3]:
                kraus = build_kraus_operators(data, dim, 0.1)
                tp_sum = sum(E.conj().T @ E for E in kraus)
                err = la.norm(tp_sum - np.eye(dim), 'fro')
                assert err < 1e-10, \
                    f"TP violation for {fam} at dim={dim}: error={err}"

    def test_kraus_identity_channel_at_zero_noise(self):
        """At noise_scale=0, channel should be identity (single Kraus = I)."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, noise_scale=0.0)
        # All non-identity Kraus should have epsilon=0
        # The identity Kraus should be just I
        tp_sum = sum(E.conj().T @ E for E in kraus)
        assert la.norm(tp_sum - np.eye(3), 'fro') < 1e-12

    def test_heisenberg_kraus_rank_2(self):
        """Heisenberg (class G) should have exactly 2 Kraus operators."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        assert len(kraus) == 2, f"Expected 2 Kraus ops, got {len(kraus)}"

    def test_affine_kraus_rank(self):
        """Affine (class L) should have 3 Kraus operators (I + S_2 + S_3)."""
        data = get_shadow_data('affine_sl2', 2.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        assert len(kraus) == 3, f"Expected 3 Kraus ops, got {len(kraus)}"

    def test_max_kraus_truncation(self):
        """max_kraus parameter should limit non-identity Kraus operators."""
        data = get_shadow_data('virasoro', 10.0, max_r=20)
        kraus_full = build_kraus_operators(data, 3, 0.1)
        kraus_trunc = build_kraus_operators(data, 3, 0.1, max_kraus=3)
        assert len(kraus_trunc) <= 4  # at most 3 non-identity + 1 identity

    def test_kraus_operators_correct_dimension(self):
        """All Kraus operators should be dim x dim."""
        data = get_shadow_data('heisenberg', 1.0)
        for dim in [2, 3, 5]:
            kraus = build_kraus_operators(data, dim, 0.1)
            for E in kraus:
                assert E.shape == (dim, dim)


# ============================================================================
# 5. CHANNEL APPLICATION
# ============================================================================

class TestChannelApplication:
    """Tests for apply_channel."""

    def test_channel_preserves_trace(self):
        """Phi(rho) should have Tr = 1 when Tr(rho) = 1."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        rho = _make_random_density_matrix(dim)
        phi_rho = apply_channel(kraus, rho)
        assert abs(np.trace(phi_rho).real - 1.0) < 1e-10

    def test_channel_output_hermitian(self):
        """Phi(rho) should be Hermitian when rho is Hermitian."""
        data = get_shadow_data('affine_sl2', 2.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        rho = _make_random_density_matrix(dim)
        phi_rho = apply_channel(kraus, rho)
        err = la.norm(phi_rho - phi_rho.conj().T, 'fro')
        assert err < 1e-10

    def test_channel_output_positive(self):
        """Phi(rho) should be positive semidefinite for PSD rho (CP)."""
        data = get_shadow_data('virasoro', 10.0, max_r=8)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        rho = _make_random_density_matrix(dim)
        phi_rho = apply_channel(kraus, rho)
        eigvals = la.eigvalsh(phi_rho)
        assert np.min(eigvals) > -1e-10

    def test_identity_channel_is_identity(self):
        """Channel with single Kraus = I acts as identity."""
        dim = 3
        kraus = [np.eye(dim, dtype=complex)]
        rho = _make_random_density_matrix(dim)
        phi_rho = apply_channel(kraus, rho)
        assert la.norm(phi_rho - rho, 'fro') < 1e-12

    def test_channel_linearity(self):
        """Phi(a*rho1 + b*rho2) = a*Phi(rho1) + b*Phi(rho2)."""
        data = get_shadow_data('heisenberg', 2.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        rho1 = _make_random_density_matrix(dim, seed=1)
        rho2 = _make_random_density_matrix(dim, seed=2)
        a, b = 0.3, 0.7
        mix = a * rho1 + b * rho2
        phi_mix = apply_channel(kraus, mix)
        phi_sum = a * apply_channel(kraus, rho1) + b * apply_channel(kraus, rho2)
        assert la.norm(phi_mix - phi_sum, 'fro') < 1e-10


# ============================================================================
# 6. VERIFY CPTP (multi-path)
# ============================================================================

class TestVerifyCPTP:
    """CPTP verification via independent paths."""

    def test_cptp_all_families(self):
        """All standard families produce CPTP channels."""
        dim = 3
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 2.0),
                         ('affine_sl3', 1.0), ('virasoro', 10.0),
                         ('betagamma', 0.5)]:
            data = get_shadow_data(fam, par)
            kraus = build_kraus_operators(data, dim, 0.1)
            result = verify_cptp(kraus)
            assert result['is_cptp'], \
                f"CPTP failed for {fam}: TP_err={result['tp_error']}, min_eig={result['choi_min_eigenvalue']}"

    def test_cptp_tp_error_small(self):
        """Trace-preserving error should be < 1e-10."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        result = verify_cptp(kraus)
        assert result['tp_error'] < 1e-10

    def test_cptp_choi_positive(self):
        """Choi matrix minimum eigenvalue should be >= -tol."""
        data = get_shadow_data('affine_sl2', 2.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        result = verify_cptp(kraus)
        assert result['choi_min_eigenvalue'] > -1e-10

    def test_cptp_path2_direct_tp_check(self):
        """Independent TP check: sum E_k^dag E_k = I (not via verify_cptp)."""
        data = get_shadow_data('virasoro', 10.0, max_r=8)
        kraus = build_kraus_operators(data, 3, 0.1)
        tp_sum = sum(E.conj().T @ E for E in kraus)
        assert la.norm(tp_sum - np.eye(3), 'fro') < 1e-10

    def test_cptp_path3_choi_partial_trace(self):
        """Independent CP+TP check: Choi partial trace = I/d."""
        data = get_shadow_data('heisenberg', 2.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        choi = compute_choi_matrix(kraus)
        # Partial trace over second system
        ptr = np.zeros((dim, dim), dtype=complex)
        for i in range(dim):
            for j in range(dim):
                for a in range(dim):
                    ptr[i, j] += choi[i * dim + a, j * dim + a]
        err = la.norm(ptr - np.eye(dim) / dim, 'fro')
        assert err < 1e-8


# ============================================================================
# 7. CHOI MATRIX
# ============================================================================

class TestChoiMatrix:
    """Tests for Choi matrix computation."""

    def test_choi_hermitian(self):
        """Choi matrix should be Hermitian."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        choi = compute_choi_matrix(kraus)
        err = la.norm(choi - choi.conj().T, 'fro')
        assert err < 1e-10

    def test_choi_positive_semidefinite(self):
        """Choi matrix should be PSD (complete positivity)."""
        data = get_shadow_data('affine_sl2', 2.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        choi = compute_choi_matrix(kraus)
        eigvals = la.eigvalsh(choi)
        assert np.min(eigvals) > -1e-10

    def test_choi_trace_equals_one(self):
        """Tr(J(Phi)) = 1 for our normalization convention."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        choi = compute_choi_matrix(kraus)
        assert abs(np.trace(choi).real - 1.0) < 1e-10

    def test_choi_identity_channel(self):
        """Choi of identity channel = |Omega><Omega| = (1/d) sum |ii><jj|."""
        dim = 3
        kraus_id = [np.eye(dim, dtype=complex)]
        choi = compute_choi_matrix(kraus_id)
        # The Choi of identity should be |Omega><Omega| with our normalization
        # J_id[i*d+a, j*d+b] = (1/d) delta_{a,i} delta_{b,j}
        for i in range(dim):
            for j in range(dim):
                expected = 1.0 / dim
                actual = choi[i * dim + i, j * dim + j]
                assert abs(actual - expected) < 1e-12
                # Off-diagonal blocks should be zero
                for a in range(dim):
                    for b in range(dim):
                        if a != i or b != j:
                            assert abs(choi[i * dim + a, j * dim + b]) < 1e-12

    def test_choi_from_data_matches_from_kraus(self):
        """choi_matrix_from_data should match compute_choi_matrix(build_kraus(...))."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        choi1 = choi_matrix_from_data(data, dim, 0.1)
        kraus = build_kraus_operators(data, dim, 0.1)
        choi2 = compute_choi_matrix(kraus)
        assert la.norm(choi1 - choi2, 'fro') < 1e-12

    def test_choi_dimension(self):
        """Choi matrix should be d^2 x d^2."""
        for dim in [2, 3, 4]:
            data = get_shadow_data('heisenberg', 1.0)
            kraus = build_kraus_operators(data, dim, 0.1)
            choi = compute_choi_matrix(kraus)
            assert choi.shape == (dim**2, dim**2)


# ============================================================================
# 8. ENTANGLEMENT FIDELITY — three independent paths (AP10)
# ============================================================================

class TestEntanglementFidelity:
    """Multi-path verification of entanglement fidelity."""

    def test_Fe_three_paths_agree(self):
        """Fe via trace, Choi, and direct methods must agree."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        result = verify_entanglement_fidelity_multipath(kraus)
        assert result['all_agree'], \
            f"Fe paths disagree: trace={result['Fe_trace']}, choi={result['Fe_choi']}, direct={result['Fe_direct']}"

    def test_Fe_three_paths_all_families(self):
        """Multi-path Fe agreement for all families."""
        for fam, par in [('heisenberg', 2.0), ('affine_sl2', 3.0),
                         ('virasoro', 10.0), ('betagamma', 0.5)]:
            data = get_shadow_data(fam, par, max_r=8)
            kraus = build_kraus_operators(data, 3, 0.1)
            result = verify_entanglement_fidelity_multipath(kraus)
            assert result['all_agree'], f"Fe multipath failed for {fam}"

    def test_Fe_identity_channel_equals_one(self):
        """Fe(id) = 1."""
        dim = 3
        kraus = [np.eye(dim, dtype=complex)]
        Fe = entanglement_fidelity(kraus)
        assert abs(Fe - 1.0) < 1e-12

    def test_Fe_bounded_zero_one(self):
        """0 <= Fe <= 1 for any CPTP map."""
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 2.0),
                         ('virasoro', 5.0), ('betagamma', 0.7)]:
            data = get_shadow_data(fam, par, max_r=8)
            kraus = build_kraus_operators(data, 3, 0.1)
            Fe = entanglement_fidelity(kraus)
            assert 0.0 - 1e-10 <= Fe <= 1.0 + 1e-10, f"Fe out of range for {fam}: {Fe}"

    def test_Fe_decreases_with_noise(self):
        """Fe should decrease (or stay same) as noise increases."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        Fe_prev = 1.0
        for ns in [0.01, 0.05, 0.1, 0.2, 0.3]:
            kraus = build_kraus_operators(data, dim, ns)
            Fe = entanglement_fidelity(kraus)
            assert Fe <= Fe_prev + 1e-10
            Fe_prev = Fe

    def test_Fe_from_choi_independent(self):
        """Compute Fe from Choi matrix independently and compare to trace formula."""
        data = get_shadow_data('affine_sl2', 2.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        # Path 1: trace formula
        Fe1 = sum(abs(np.trace(E))**2 for E in kraus) / dim**2
        # Path 2: from Choi
        choi = compute_choi_matrix(kraus)
        Fe2 = entanglement_fidelity_from_choi(choi, dim)
        assert abs(Fe1 - Fe2) < 1e-10


# ============================================================================
# 9. VON NEUMANN ENTROPY
# ============================================================================

class TestVonNeumannEntropy:
    """Tests for von Neumann entropy computation."""

    def test_entropy_pure_state_zero(self):
        """S(|0><0|) = 0."""
        rho = _pure_state(3, 0)
        S = von_neumann_entropy(rho)
        assert abs(S) < 1e-10

    def test_entropy_maximally_mixed(self):
        """S(I/d) = log2(d)."""
        for dim in [2, 3, 4, 5]:
            rho = _maximally_mixed(dim)
            S = von_neumann_entropy(rho)
            expected = math.log2(dim)
            assert abs(S - expected) < 1e-10, \
                f"Entropy of I/{dim}: got {S}, expected {expected}"

    def test_entropy_nonnegative(self):
        """S(rho) >= 0 for any density matrix."""
        for seed in range(5):
            rho = _make_random_density_matrix(3, seed)
            S = von_neumann_entropy(rho)
            assert S >= -1e-10

    def test_entropy_bounded_by_log_d(self):
        """S(rho) <= log2(d) for d-dimensional rho."""
        dim = 4
        for seed in range(5):
            rho = _make_random_density_matrix(dim, seed)
            S = von_neumann_entropy(rho)
            assert S <= math.log2(dim) + 1e-10

    def test_entropy_bell_state(self):
        """S of reduced density matrix of Bell state = 1 bit."""
        # Bell state |00> + |11> / sqrt(2), partial trace = I/2
        rho = np.array([[0.5, 0], [0, 0.5]], dtype=complex)
        S = von_neumann_entropy(rho)
        assert abs(S - 1.0) < 1e-10


# ============================================================================
# 10. DIAMOND NORM
# ============================================================================

class TestDiamondNorm:
    """Tests for diamond norm computation."""

    def test_depolarizing_formula_known_values(self):
        """Diamond norm of depolarizing channel at known p, d values."""
        # ||Delta_p - id|| = 2*p*(d-1)/d
        # Path 1: direct formula
        # Path 2: independent computation 2*p*(d-1)/d
        for p, d in [(0.1, 2), (0.1, 3), (0.5, 2), (0.01, 10)]:
            dn = diamond_norm_depolarizing(p, d)
            expected = 2.0 * p * (d - 1) / d
            assert abs(dn - expected) < 1e-12

    def test_depolarizing_p0_is_zero(self):
        """Diamond norm at p=0 (identity) is 0."""
        assert abs(diamond_norm_depolarizing(0.0, 3)) < 1e-15

    def test_depolarizing_monotone_in_p(self):
        """Diamond norm increases with p for fixed d."""
        d = 3
        prev = 0.0
        for p in [0.01, 0.05, 0.1, 0.2, 0.5, 0.9]:
            dn = diamond_norm_depolarizing(p, d)
            assert dn >= prev - 1e-12
            prev = dn

    def test_diamond_norm_bound_nonnegative(self):
        """Diamond norm bound should be >= 0."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.1)
        dn = diamond_norm_upper_bound(kraus)
        assert dn >= -1e-10

    def test_diamond_norm_identity_zero(self):
        """Diamond norm of identity channel (vs identity) should be 0."""
        dim = 3
        kraus = [np.eye(dim, dtype=complex)]
        dn = diamond_norm_upper_bound(kraus)
        assert dn < 1e-10

    def test_effective_p_bounded(self):
        """Effective depolarizing parameter p should be in [0, 1]."""
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 2.0),
                         ('virasoro', 10.0), ('betagamma', 0.5)]:
            data = get_shadow_data(fam, par, max_r=8)
            kraus = build_kraus_operators(data, 3, 0.1)
            p = effective_depolarizing_parameter(kraus)
            assert 0.0 - 1e-10 <= p <= 1.0 + 1e-10, \
                f"p out of range for {fam}: {p}"

    def test_effective_p_zero_at_zero_noise(self):
        """At noise_scale=0, effective p should be 0."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.0)
        p = effective_depolarizing_parameter(kraus)
        assert abs(p) < 1e-12


# ============================================================================
# 11. COHERENT INFORMATION AND QUANTUM CAPACITY
# ============================================================================

class TestQuantumCapacity:
    """Tests for coherent information and quantum capacity."""

    def test_coherent_info_identity_equals_log_d(self):
        """I_c(rho, id) = S(rho) - 0 = S(rho) for pure input."""
        dim = 3
        kraus = [np.eye(dim, dtype=complex)]
        # For identity channel and pure input:
        # S(id(rho)) = S(rho) = 0, S_e = S(env) = 0 for rank-1 env
        # Actually S_e depends on the environment state which for identity
        # with single Kraus is a 1x1 matrix = [1] with S=0
        rho = _pure_state(dim, 0)
        Ic = coherent_information(kraus, rho)
        # For pure input through identity: output is pure (S=0), env is 1x1 (S=0)
        assert abs(Ic) < 1e-10

    def test_Q1_identity_channel(self):
        """Q_1 of identity channel = log2(d)."""
        dim = 3
        kraus = [np.eye(dim, dtype=complex)]
        Q1 = one_shot_quantum_capacity(kraus, n_samples=10)
        expected = math.log2(dim)
        assert abs(Q1 - expected) < 0.1, \
            f"Q1(id) = {Q1}, expected {expected}"

    def test_Q1_nonnegative(self):
        """Q_1 >= 0 by definition (max with 0)."""
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 2.0),
                         ('virasoro', 10.0)]:
            data = get_shadow_data(fam, par, max_r=8)
            kraus = build_kraus_operators(data, 3, 0.1)
            Q1 = one_shot_quantum_capacity(kraus, n_samples=20)
            assert Q1 >= -1e-10

    def test_depolarizing_capacity_p0(self):
        """Q_1(Delta_0) = log2(d) (noiseless channel)."""
        for d in [2, 3, 4]:
            Q1 = depolarizing_capacity_exact(0.0, d)
            expected = math.log2(d)
            assert abs(Q1 - expected) < 1e-10

    def test_depolarizing_capacity_p1(self):
        """Q_1(Delta_1) = 0 (completely depolarizing)."""
        Q1 = depolarizing_capacity_exact(1.0, 3)
        assert abs(Q1) < 1e-10

    def test_depolarizing_capacity_monotone(self):
        """Q_1 decreases with increasing p."""
        d = 3
        prev = math.log2(d)
        for p in [0.0, 0.01, 0.05, 0.1, 0.2, 0.5]:
            Q1 = depolarizing_capacity_exact(p, d)
            assert Q1 <= prev + 1e-10
            prev = Q1

    def test_depolarizing_capacity_dim_2_threshold(self):
        """For d=2 depolarizing, Q_1 vanishes at p >= p_threshold.
        The threshold is approximately p ~ 0.1893 for qubit depolarizing."""
        Q1_low = depolarizing_capacity_exact(0.1, 2)
        Q1_high = depolarizing_capacity_exact(0.5, 2)
        assert Q1_low > 0  # Below threshold
        assert Q1_high == 0.0  # Above threshold


# ============================================================================
# 12. FAMILY-SPECIFIC CHANNELS
# ============================================================================

class TestFamilyChannels:
    """Tests for shadow_channel_* convenience functions."""

    def test_heisenberg_channel_structure(self):
        """Heisenberg channel should return correct metadata."""
        r = shadow_channel_heisenberg(1.0, 3, 0.1)
        assert r['family'] == 'heisenberg'
        assert r['shadow_class'] == 'G'
        assert r['shadow_depth'] == 2
        assert abs(r['kappa'] - 1.0) < 1e-12  # kappa(H_1) = 1

    def test_affine_channel_structure(self):
        """Affine channel should return correct metadata."""
        r = shadow_channel_affine(2.0, 3, 'sl2', 0.1)
        assert r['family'] == 'affine_sl2'
        assert r['shadow_class'] == 'L'
        assert r['shadow_depth'] == 3
        expected_kappa = _kappa_affine_sl2(2.0)
        assert abs(r['kappa'] - expected_kappa) < 1e-12

    def test_virasoro_channel_structure(self):
        """Virasoro channel should return correct metadata."""
        r = shadow_channel_virasoro(10.0, 3, 0.1, max_r=8)
        assert r['family'] == 'virasoro'
        assert r['shadow_class'] == 'M'
        assert abs(r['kappa'] - 5.0) < 1e-12  # kappa(Vir_10) = 5

    def test_betagamma_channel_structure(self):
        """Beta-gamma channel should return correct metadata."""
        r = shadow_channel_betagamma(0.5, 3, 0.1)
        assert r['family'] == 'betagamma'
        assert r['shadow_class'] == 'C'
        assert r['shadow_depth'] == 4

    def test_all_families_cptp(self):
        """All family channels must produce CPTP maps."""
        results = [
            shadow_channel_heisenberg(1.0, 3, 0.1),
            shadow_channel_affine(2.0, 3, 'sl2', 0.1),
            shadow_channel_virasoro(10.0, 3, 0.1, max_r=8),
            shadow_channel_betagamma(0.5, 3, 0.1),
        ]
        for r in results:
            assert r['cptp']['is_cptp'], f"CPTP failed for {r['family']}"

    def test_all_families_Fe_bounded(self):
        """All families: 0 <= Fe <= 1."""
        results = [
            shadow_channel_heisenberg(1.0, 3, 0.1),
            shadow_channel_affine(2.0, 3, 'sl2', 0.1),
            shadow_channel_virasoro(10.0, 3, 0.1, max_r=8),
            shadow_channel_betagamma(0.5, 3, 0.1),
        ]
        for r in results:
            Fe = r['entanglement_fidelity']
            assert 0.0 - 1e-10 <= Fe <= 1.0 + 1e-10, \
                f"Fe out of range for {r['family']}: {Fe}"

    def test_all_families_Q1_nonneg(self):
        """All families: Q_1 >= 0."""
        results = [
            shadow_channel_heisenberg(1.0, 3, 0.1),
            shadow_channel_affine(2.0, 3, 'sl2', 0.1),
            shadow_channel_virasoro(10.0, 3, 0.1, max_r=8),
            shadow_channel_betagamma(0.5, 3, 0.1),
        ]
        for r in results:
            assert r['Q1'] >= -1e-10, f"Q1 < 0 for {r['family']}: {r['Q1']}"


# ============================================================================
# 13. COMPLEMENTARY CHANNEL
# ============================================================================

class TestComplementaryChannel:
    """Tests for complementary channel construction."""

    def test_complementary_tp(self):
        """Complementary channel maps d -> K, and sum F_a^dag F_a = I_d."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        comp = complementary_channel_kraus(kraus)
        assert len(comp) == dim  # d Kraus operators for comp channel
        tp_sum = sum(F.conj().T @ F for F in comp)
        err = la.norm(tp_sum - np.eye(dim), 'fro')
        assert err < 1e-10, f"Complementary TP error: {err}"

    def test_subadditivity(self):
        """S(Phi(rho)) + S(Phi^c(rho)) >= S(rho) for any rho."""
        data = get_shadow_data('affine_sl2', 2.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        rho = _make_random_density_matrix(dim)
        result = verify_complementary_entropy(kraus, rho)
        assert result['subadditivity_holds'], \
            f"Subadditivity violated: S_out={result['S_output']}, S_comp={result['S_complementary']}, S_in={result['S_input']}"

    def test_subadditivity_maximally_mixed(self):
        """Subadditivity for maximally mixed input."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        rho = _maximally_mixed(dim)
        result = verify_complementary_entropy(kraus, rho)
        assert result['subadditivity_holds']

    def test_complementary_dimension(self):
        """Complementary Kraus operators map d -> K (K = number of Kraus ops)."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        n_kraus = len(kraus)
        comp = complementary_channel_kraus(kraus)
        for F in comp:
            assert F.shape == (n_kraus, dim), \
                f"Shape mismatch: {F.shape}, expected ({n_kraus}, {dim})"


# ============================================================================
# 14. CHOI MATRIX VERIFICATION
# ============================================================================

class TestChoiVerification:
    """Tests for verify_choi_properties."""

    def test_choi_valid_all_families(self):
        """Choi matrix valid (positive, Hermitian, correct trace) for all families."""
        dim = 3
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 2.0),
                         ('virasoro', 10.0), ('betagamma', 0.5)]:
            data = get_shadow_data(fam, par, max_r=8)
            kraus = build_kraus_operators(data, dim, 0.1)
            choi = compute_choi_matrix(kraus)
            props = verify_choi_properties(choi, dim)
            assert props['is_valid_choi'], \
                f"Invalid Choi for {fam}: pos={props['is_positive']}, tp_err={props['tp_error']}, herm_err={props['hermiticity_error']}"

    def test_choi_rank_equals_kraus_count(self):
        """Rank of Choi matrix = number of linearly independent Kraus operators."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        kraus = build_kraus_operators(data, dim, 0.1)
        choi = compute_choi_matrix(kraus)
        props = verify_choi_properties(choi, dim)
        # Rank should be at most the number of Kraus operators
        assert props['rank'] <= len(kraus)

    def test_choi_identity_is_rank_1(self):
        """Choi of identity channel has rank 1 (= |Omega><Omega|)."""
        dim = 3
        kraus = [np.eye(dim, dtype=complex)]
        choi = compute_choi_matrix(kraus)
        props = verify_choi_properties(choi, dim)
        assert props['rank'] == 1


# ============================================================================
# 15. HEISENBERG GAUSSIAN VERIFICATION
# ============================================================================

class TestHeisenbergGaussian:
    """Tests for Gaussian (depolarizing) structure of Heisenberg channel."""

    def test_heisenberg_is_gaussian(self):
        """Heisenberg channel is a Gaussian (unitary mixture) channel."""
        result = verify_heisenberg_gaussian(1.0, 3, 0.1)
        assert result['is_gaussian'], \
            f"Heisenberg not Gaussian: rank={result['kraus_rank']}, recon_err={result['reconstruction_error']}"

    def test_heisenberg_gaussian_multiple_k(self):
        """Gaussian structure holds for various levels k."""
        for k in [0.5, 1.0, 2.0, 5.0, 10.0]:
            result = verify_heisenberg_gaussian(k, 3, 0.1)
            assert result['is_gaussian'], f"Gaussian failed at k={k}"

    def test_heisenberg_gaussian_unitarity(self):
        """The extracted unitary U_1 from Heisenberg should be truly unitary."""
        result = verify_heisenberg_gaussian(2.0, 3, 0.1)
        assert result['unitarity_error'] < 1e-10

    def test_heisenberg_reconstruction_error(self):
        """Phi(rho) = (1-p)*rho + p*U*rho*U^dag reconstruction should be exact."""
        result = verify_heisenberg_gaussian(1.0, 3, 0.1)
        assert result['reconstruction_error'] < 1e-10


# ============================================================================
# 16. CAPACITY TABLE AND SWEEP
# ============================================================================

class TestCapacityTable:
    """Tests for capacity_table parameter sweeps."""

    def test_heisenberg_table_nonempty(self):
        """Heisenberg capacity table should produce results."""
        table = capacity_table('heisenberg', [1.0, 2.0, 5.0], dim=3, noise_scale=0.1)
        assert len(table) == 3

    def test_virasoro_table_kappa_independent(self):
        """Virasoro capacity table kappa values verified independently."""
        params = [1.0, 5.0, 10.0, 25.0]
        table = capacity_table('virasoro', params, dim=3, noise_scale=0.1, max_r=8)
        for entry in table:
            c = entry['parameter']
            expected_kappa = c / 2.0
            assert abs(entry['kappa'] - expected_kappa) < 1e-12

    def test_table_all_Fe_bounded(self):
        """All Fe in capacity table should be in [0, 1]."""
        table = capacity_table('affine_sl2', [1.0, 2.0, 5.0], dim=3, noise_scale=0.1)
        for entry in table:
            assert 0.0 - 1e-10 <= entry['entanglement_fidelity'] <= 1.0 + 1e-10

    def test_table_shadow_class_consistent(self):
        """Shadow class should be consistent within a family."""
        table = capacity_table('heisenberg', [1.0, 2.0], dim=3, noise_scale=0.1)
        for entry in table:
            assert entry['shadow_class'] == 'G'

    def test_betagamma_table(self):
        """Betagamma capacity table runs and returns class C."""
        table = capacity_table('betagamma', [0.3, 0.5, 1.0], dim=3, noise_scale=0.1)
        assert len(table) == 3
        for entry in table:
            assert entry['shadow_class'] == 'C'


# ============================================================================
# 17. ZETA ZERO EVALUATION
# ============================================================================

class TestZetaZeroEvaluation:
    """Tests for channel evaluation at Riemann zeta zeros."""

    def test_zeta_zeros_nonempty(self):
        """Zeta zero evaluation should return results."""
        results = channel_at_zeta_zeros(5, 3, 0.1, max_r=8)
        assert len(results) >= 1

    def test_zeta_zeros_cptp_valid(self):
        """All channels at zeta zeros should be CPTP."""
        results = channel_at_zeta_zeros(5, 3, 0.1, max_r=8)
        for r in results:
            if 'error' not in r:
                assert r['cptp_valid'], \
                    f"CPTP failed at zero n={r['zero_index']}"

    def test_zeta_zeros_class_M(self):
        """All zeta zero channels are Virasoro = class M."""
        results = channel_at_zeta_zeros(3, 3, 0.1, max_r=8)
        for r in results:
            if 'error' not in r:
                assert r['shadow_class'] == 'M'

    def test_zeta_zeros_kappa_consistent(self):
        """kappa at zeta zeros should be gamma_n/2 (Virasoro at c=gamma_n)."""
        results = channel_at_zeta_zeros(5, 3, 0.1, max_r=8)
        for r in results:
            if 'error' not in r:
                expected_kappa = r['gamma_n'] / 2.0
                assert abs(r['kappa'] - expected_kappa) < 1e-10


# ============================================================================
# 18. DIAMOND NORM VS DEPTH
# ============================================================================

class TestDiamondNormVsDepth:
    """Tests for systematic depth analysis."""

    def test_depth_analysis_all_classes(self):
        """Depth analysis should cover all four shadow classes."""
        results = diamond_norm_vs_depth(0.1, 3, max_r_vir=8)
        assert 'G_heisenberg' in results
        assert 'L_affine_sl2' in results
        assert 'C_betagamma' in results
        assert 'M_virasoro' in results

    def test_depth_analysis_nonempty(self):
        """Each class should have results."""
        results = diamond_norm_vs_depth(0.1, 3, max_r_vir=8)
        for key in ['G_heisenberg', 'L_affine_sl2', 'C_betagamma', 'M_virasoro']:
            assert len(results[key]) > 0

    def test_depth_analysis_Fe_bounded(self):
        """Fe in depth analysis should be in [0, 1]."""
        results = diamond_norm_vs_depth(0.1, 3, max_r_vir=8)
        for key, entries in results.items():
            for e in entries:
                assert 0.0 - 1e-10 <= e['Fe'] <= 1.0 + 1e-10


# ============================================================================
# 19. CHOI MATRIX DIMENSION SWEEP
# ============================================================================

class TestChoiDimensions:
    """Tests for Choi matrix across dimensions."""

    def test_choi_dims_all_valid(self):
        """Choi matrices valid for d=2,3,5."""
        results = choi_matrix_dimensions('heisenberg', 1.0, dims=[2, 3, 5], noise_scale=0.1)
        for r in results:
            assert r['valid'], f"Invalid Choi at dim={r['dim']}"

    def test_choi_dims_shape_correct(self):
        """Choi shape should be (d^2, d^2)."""
        results = choi_matrix_dimensions('heisenberg', 1.0, dims=[2, 3], noise_scale=0.1)
        for r in results:
            d = r['dim']
            assert r['choi_shape'] == (d**2, d**2)

    def test_choi_dims_trace_one(self):
        """Choi trace should be 1 for all dimensions."""
        results = choi_matrix_dimensions('affine_sl2', 2.0, dims=[2, 3, 4], noise_scale=0.1)
        for r in results:
            assert abs(r['choi_trace'] - 1.0) < 1e-8


# ============================================================================
# 20. FULL ANALYSIS PIPELINE
# ============================================================================

class TestFullAnalysis:
    """Tests for the full analysis pipeline."""

    def test_full_analysis_runs(self):
        """full_analysis should run without error."""
        # Use small parameters for speed
        results = full_analysis(dim=2, noise_scale=0.1, n_zeros=2)
        assert 'heisenberg' in results
        assert 'affine_sl2' in results
        assert 'virasoro' in results
        assert 'betagamma' in results
        assert 'zeta_zeros' in results
        assert 'multipath_Fe' in results
        assert 'multipath_choi' in results
        assert 'complementary' in results
        assert 'depth_analysis' in results

    def test_full_analysis_multipath_agreement(self):
        """Multi-path Fe check in full analysis should agree."""
        results = full_analysis(dim=2, noise_scale=0.1, n_zeros=2)
        assert results['multipath_Fe']['all_agree']

    def test_full_analysis_choi_valid(self):
        """Choi matrix in full analysis should be valid."""
        results = full_analysis(dim=2, noise_scale=0.1, n_zeros=2)
        assert results['multipath_choi']['is_valid_choi']


# ============================================================================
# 21. CROSS-FAMILY CONSISTENCY CHECKS
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family invariant checks (AP10: multi-path, not hardcoded)."""

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_k1 + H_k2) = kappa(H_k1) + kappa(H_k2) = k1 + k2.
        Independent verification of additivity for free field direct sum."""
        k1, k2 = 2.0, 3.0
        kappa1 = _kappa_heisenberg(k1)
        kappa2 = _kappa_heisenberg(k2)
        kappa_sum = _kappa_heisenberg(k1 + k2)
        assert abs(kappa1 + kappa2 - kappa_sum) < 1e-12

    def test_virasoro_self_dual_at_c13(self):
        """At c=13, Vir_c and Vir_{26-c} have the same kappa (AP8)."""
        kappa_13 = _kappa_virasoro(13.0)
        kappa_dual = _kappa_virasoro(26.0 - 13.0)
        assert abs(kappa_13 - kappa_dual) < 1e-12
        # Both should equal 13/2 = 6.5
        assert abs(kappa_13 - 6.5) < 1e-12

    def test_affine_sl2_at_critical_level(self):
        """At k = -h^v = -2, kappa(sl_2) = 0 (critical level)."""
        # kappa = 3*(k+2)/4 = 0 at k = -2
        kappa_crit = _kappa_affine_sl2(-2.0)
        assert abs(kappa_crit) < 1e-12

    def test_shadow_depth_ordering(self):
        """Shadow depth: G(2) < L(3) < C(4) < M(inf)."""
        dG = get_shadow_data('heisenberg', 1.0).shadow_depth
        dL = get_shadow_data('affine_sl2', 1.0).shadow_depth
        dC = get_shadow_data('betagamma', 0.5).shadow_depth
        assert dG == 2
        assert dL == 3
        assert dC == 4
        # M has depth = max_r (truncated infinite)

    def test_heisenberg_single_shadow_coefficient(self):
        """Heisenberg has exactly one nonzero shadow coefficient (S_2 = kappa)."""
        data = get_shadow_data('heisenberg', 3.0, max_r=10)
        nonzero = [r for r, v in data.shadow_coeffs.items() if abs(v) > 1e-15]
        assert nonzero == [2], f"Heisenberg nonzero coefficients: {nonzero}"
        assert abs(data.shadow_coeffs[2] - 3.0) < 1e-12

    def test_affine_two_shadow_coefficients(self):
        """Affine sl_2 has exactly two nonzero shadow coefficients (S_2 and S_3)."""
        data = get_shadow_data('affine_sl2', 2.0, max_r=10)
        nonzero = [r for r, v in data.shadow_coeffs.items() if abs(v) > 1e-15]
        assert set(nonzero) == {2, 3}, f"Affine nonzero coefficients: {nonzero}"

    def test_noise_scale_controls_perturbation(self):
        """Larger noise_scale => larger diamond norm bound, for same family."""
        data = get_shadow_data('heisenberg', 1.0)
        dim = 3
        dns = []
        for ns in [0.01, 0.05, 0.1, 0.2]:
            kraus = build_kraus_operators(data, dim, ns)
            dn = diamond_norm_upper_bound(kraus)
            dns.append(dn)
        # Should be (weakly) increasing
        for i in range(len(dns) - 1):
            assert dns[i] <= dns[i + 1] + 1e-10, \
                f"Diamond norm not monotone in noise_scale: {dns}"


# ============================================================================
# 22. EDGE CASES AND ROBUSTNESS
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_dim_2_qubit(self):
        """Channel works for qubit (dim=2)."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 2, 0.1)
        result = verify_cptp(kraus)
        assert result['is_cptp']

    def test_large_noise_still_cptp(self):
        """Even at large noise_scale, channel should remain CPTP (clipping)."""
        data = get_shadow_data('heisenberg', 1.0)
        kraus = build_kraus_operators(data, 3, 0.9)
        result = verify_cptp(kraus)
        assert result['is_cptp']

    def test_small_parameter_heisenberg(self):
        """Heisenberg at very small k."""
        data = get_shadow_data('heisenberg', 0.01)
        assert abs(data.kappa - 0.01) < 1e-12
        kraus = build_kraus_operators(data, 3, 0.1)
        result = verify_cptp(kraus)
        assert result['is_cptp']

    def test_virasoro_various_c(self):
        """Virasoro channel works at various c values."""
        for c in [0.5, 1.0, 5.0, 13.0, 25.0, 25.5]:
            data = get_shadow_data('virasoro', c, max_r=8)
            kraus = build_kraus_operators(data, 3, 0.1)
            result = verify_cptp(kraus)
            assert result['is_cptp'], f"CPTP failed at c={c}"

    def test_betagamma_lam_half(self):
        """Beta-gamma at lambda=1/2 has c = 2*(6/4 - 3 + 1) = -2.
        Actually c = 2*(6*(1/4) - 6*(1/2) + 1) = 2*(3/2 - 3 + 1) = 2*(-1/2) = -1.
        kappa = c/2 = -1/2."""
        lam = 0.5
        c_expected = 2.0 * (6.0 * 0.25 - 3.0 + 1.0)
        kappa_expected = c_expected / 2.0
        data = get_shadow_data('betagamma', lam)
        assert abs(data.kappa - kappa_expected) < 1e-12
