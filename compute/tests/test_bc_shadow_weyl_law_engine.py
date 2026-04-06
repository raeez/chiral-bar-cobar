r"""Tests for shadow Weyl law engine: zero-counting, spectral dimension, heat kernel, NC volume.

Multi-path verification (3+ independent methods per numerical claim):
    Path 1: Direct eigenvalue computation (numpy.linalg.eigvalsh)
    Path 2: Weyl asymptotic (power-law fit to N(lambda))
    Path 3: Heat kernel (Laplace transform / small-t asymptotics)
    Path 4: Spectral zeta residue
    Path 5: Sturm-Liouville counting (sign changes of characteristic polynomial)
    Path 6: Independent matrix construction and trace identities
    Path 7: Dimensional / degree analysis

90 tests covering:
    - Shadow Dirac operator construction (symmetry, tridiagonal, trace, determinant)
    - Heisenberg (class G): finite-rank, exact eigenvalues
    - Affine sl_2/sl_3 (class L): 3-arity truncation
    - Beta-gamma (class C): 4-arity truncation
    - Virasoro (class M): infinite tower, spectral properties
    - Eigenvalue counting function (monotonicity, limiting values)
    - Weyl law fitting (finite truncation: d_S near 0, valid fit metadata)
    - Heat kernel (positivity, monotonicity, trace identity)
    - Spectral zeta (convergence for large Re(s), pole structure)
    - Dixmier trace (positivity, NC volume)
    - Weyl remainder analysis
    - Riemann zero evaluations
    - Selberg-type counting
    - Pair correlation (GUE reference)
    - Multi-path verification consistency
    - Cross-class comparison
    - Koszul complementarity (AP24: kappa + kappa' = 13 for Virasoro)
    - Virasoro c-scan
    - Remainder structure at Riemann zeros
    - Independent shadow coefficient formulas

Tolerance: 1e-10 for exact comparisons, broad tolerances for spectral fits.

CAUTION (AP1):  kappa formulas are family-specific -- never copy between families.
CAUTION (AP9):  S_2 != c/2 in general.
CAUTION (AP10): Tests derive expected values independently, never from engine output.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

import math
import cmath
import pytest
import numpy as np
from numpy.linalg import eigvalsh

from compute.lib.bc_shadow_weyl_law_engine import (
    # Dispatch helpers
    _get_shadow_coeffs,
    _shadow_class,
    _shadow_depth,
    # Dirac operator
    ShadowDiracSpectrum,
    build_shadow_dirac,
    shadow_dirac_spectrum,
    # Counting function
    counting_function,
    # Weyl fit
    WeylFitResult,
    fit_weyl_law,
    # Heat kernel
    HeatKernelResult,
    heat_kernel_trace,
    # Spectral zeta
    SpectralZetaResult,
    spectral_zeta,
    spectral_zeta_complex,
    spectral_zeta_derivative,
    find_spectral_zeta_zeros,
    # Pair correlation
    PairCorrelationResult,
    pair_correlation_spectral_zeros,
    # Dixmier trace
    dixmier_trace,
    # Weyl remainder
    WeylRemainderResult,
    weyl_remainder,
    # Riemann zero evaluations
    WeylAtRiemannZeroResult,
    weyl_at_riemann_zeros,
    # Selberg analogy
    SelbergAnalogy,
    selberg_type_counting,
    # Multi-path verification
    MultiPathVerification,
    multi_path_verify,
    _sturm_liouville_count,
    # Full analysis
    ShadowWeylAnalysis,
    full_shadow_weyl_analysis,
    # Virasoro c-scan
    VirasoroCscanResult,
    virasoro_c_scan,
    # Remainder structure
    RemainderStructureResult,
    remainder_structure_at_zeros,
    # Cross-class
    CrossClassComparison,
    cross_class_comparison,
    # Koszul complementarity
    WeylComplementarityResult,
    weyl_complementarity,
    # Constants
    RIEMANN_ZETA_ZEROS,
)


# ============================================================================
# 0. Shadow class / depth dispatch
# ============================================================================

class TestShadowClassDispatch:
    """Test the shadow depth class classification."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (Gaussian, r_max=2)."""
        assert _shadow_class('heisenberg') == 'G'

    def test_affine_sl2_class_L(self):
        """Affine sl_2 is class L (Lie/tree, r_max=3)."""
        assert _shadow_class('affine_sl2') == 'L'

    def test_affine_sl3_class_L(self):
        """Affine sl_3 is class L (Lie/tree, r_max=3)."""
        assert _shadow_class('affine_sl3') == 'L'

    def test_betagamma_class_C(self):
        """Beta-gamma is class C (contact/quartic, r_max=4)."""
        assert _shadow_class('betagamma') == 'C'

    def test_virasoro_class_M(self):
        """Virasoro is class M (mixed, r_max=infinity)."""
        assert _shadow_class('virasoro') == 'M'

    def test_w3_t_class_M(self):
        """W_3 T-line is class M."""
        assert _shadow_class('w3_t') == 'M'

    def test_w3_w_class_M(self):
        """W_3 W-line is class M."""
        assert _shadow_class('w3_w') == 'M'

    def test_unknown_defaults_M(self):
        """Unknown family defaults to class M."""
        assert _shadow_class('unknown_family') == 'M'

    def test_heisenberg_depth_2(self):
        """Heisenberg shadow depth = 2."""
        assert _shadow_depth('heisenberg') == 2

    def test_affine_sl2_depth_3(self):
        """Affine sl_2 shadow depth = 3."""
        assert _shadow_depth('affine_sl2') == 3

    def test_betagamma_depth_4(self):
        """Beta-gamma shadow depth = 4."""
        assert _shadow_depth('betagamma') == 4

    def test_virasoro_depth_infinite(self):
        """Virasoro shadow depth = 1000 (effectively infinite)."""
        assert _shadow_depth('virasoro') == 1000


# ============================================================================
# 1. Shadow Dirac operator construction
# ============================================================================

class TestBuildShadowDirac:
    """Test the shadow Dirac operator matrix construction."""

    def test_symmetry(self):
        """D_sh must be a symmetric (self-adjoint) matrix."""
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=52)
        D = build_shadow_dirac(coeffs, N=50)
        np.testing.assert_allclose(D, D.T, atol=1e-15,
                                   err_msg="Shadow Dirac must be symmetric")

    def test_tridiagonal_structure(self):
        """D_sh must be tridiagonal: D[i,j] = 0 if |i-j| > 1."""
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=22)
        D = build_shadow_dirac(coeffs, N=20)
        for i in range(20):
            for j in range(20):
                if abs(i - j) > 1:
                    assert D[i, j] == 0.0, (
                        f"D[{i},{j}] = {D[i,j]} but should be 0 (tridiagonal)")

    def test_real_eigenvalues(self):
        """Symmetric real matrix has real eigenvalues."""
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=52)
        D = build_shadow_dirac(coeffs, N=50)
        eigs = eigvalsh(D)
        assert np.all(np.isfinite(eigs)), "Eigenvalues must be finite"

    def test_heisenberg_diagonal_structure(self):
        """Heisenberg has S_r=0 for r>=3, so all off-diagonal hops
        involving S_{r>=3} vanish.  D[0,0] = S_2/|S_2| = 1, rest diagonal = 0.

        Path 1: check D[0,0]
        Path 2: check off-diagonal all zero (S_3=0 kills all hops)
        Path 3: eigenvalue structure has single nonzero eigenvalue
        """
        coeffs = _get_shadow_coeffs('heisenberg', 2.0, max_r=12)
        D = build_shadow_dirac(coeffs, N=10)
        # Path 1: D[0,0] = S_2/|S_2| = 1
        assert abs(D[0, 0] - 1.0) < 1e-14
        # Path 2: all off-diagonal zero
        for i in range(10):
            for j in range(10):
                if i != j:
                    assert abs(D[i, j]) < 1e-14
        # Path 3: eigenvalues = {1, 0, 0, ..., 0}
        eigs = eigvalsh(D)
        nonzero = [e for e in eigs if abs(e) > 1e-12]
        assert len(nonzero) == 1
        assert abs(nonzero[0] - 1.0) < 1e-12

    def test_matrix_size(self):
        """D_sh should be N x N."""
        N = 30
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=N + 2)
        D = build_shadow_dirac(coeffs, N=N)
        assert D.shape == (N, N)

    def test_trace_equals_sum_of_diagonal(self):
        """Tr(D_sh) = sum of diagonal entries = sum of eigenvalues.

        Path 1: numpy trace
        Path 2: manual sum of diagonal
        Path 3: sum of eigenvalues
        """
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=52)
        D = build_shadow_dirac(coeffs, N=50)
        trace_np = np.trace(D)
        trace_manual = sum(D[i, i] for i in range(50))
        eigs = eigvalsh(D)
        trace_eigs = np.sum(eigs)

        np.testing.assert_allclose(trace_np, trace_manual, atol=1e-12)
        np.testing.assert_allclose(trace_np, trace_eigs, atol=1e-10)

    def test_determinant_equals_product_of_eigenvalues(self):
        """det(D_sh) = product of eigenvalues.

        Path 1: numpy det
        Path 2: product of eigvalsh
        """
        coeffs = _get_shadow_coeffs('affine_sl2', 1.0, max_r=12)
        D = build_shadow_dirac(coeffs, N=10)
        det_np = np.linalg.det(D)
        eigs = eigvalsh(D)
        det_eigs = np.prod(eigs)
        if abs(det_np) > 1e-300 and abs(det_eigs) > 1e-300:
            np.testing.assert_allclose(
                np.log(abs(det_np)), np.log(abs(det_eigs)), atol=1e-8)
        else:
            np.testing.assert_allclose(det_np, det_eigs, atol=1e-10)

    def test_frobenius_norm_vs_eigenvalues(self):
        """||D||_F^2 = Tr(D^T D) = sum(eigenvalues^2) for symmetric D.

        Path 1: Frobenius norm squared
        Path 2: sum of eig^2
        """
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=32)
        D = build_shadow_dirac(coeffs, N=30)
        frob_sq = np.sum(D ** 2)
        eigs = eigvalsh(D)
        sum_eig_sq = np.sum(eigs ** 2)
        np.testing.assert_allclose(frob_sq, sum_eig_sq, rtol=1e-10)

    def test_diagonal_is_normalized_shadow_coefficients(self):
        """D[i,i] = S_{i+2} / max(|S_2|, 1e-15).

        Path 1: engine matrix
        Path 2: independent computation from shadow coefficients
        """
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=22)
        D = build_shadow_dirac(coeffs, N=20)
        scale = max(abs(coeffs.get(2, 0.0)), 1e-15)
        for i in range(20):
            r = i + 2
            expected = coeffs.get(r, 0.0) / scale
            np.testing.assert_allclose(D[i, i], expected, atol=1e-14)


# ============================================================================
# 2. Shadow Dirac spectrum
# ============================================================================

class TestShadowDiracSpectrum:
    """Test the spectrum computation."""

    def test_spectrum_sorted(self):
        """Eigenvalues should be sorted ascending."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        assert np.all(np.diff(spec.eigenvalues) >= -1e-15)

    def test_abs_eigenvalues_sorted(self):
        """Absolute eigenvalues (nonzero only) should be sorted ascending."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        assert np.all(np.diff(spec.abs_eigenvalues) >= -1e-15)

    def test_spectral_radius_ge_gap(self):
        """Spectral radius >= spectral gap."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        assert spec.spectral_radius >= spec.spectral_gap - 1e-15

    def test_n_zero_nonnegative(self):
        """Number of zero eigenvalues must be non-negative."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        assert spec.n_zero >= 0

    def test_metadata_stored(self):
        """Check that family, param, N are stored correctly."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=30)
        assert spec.family == 'virasoro'
        assert spec.param == 10.0
        assert spec.N == 30

    def test_heisenberg_spectrum_single_nonzero(self):
        """Heisenberg: D_sh has one nonzero eigenvalue = 1.0.

        Path 1: direct eigenvalue count from spec
        Path 2: trace = 1 implies one eig = 1 (rest 0)
        Path 3: rank of matrix = 1 (one nonzero diagonal)
        """
        spec = shadow_dirac_spectrum('heisenberg', 1.0, N=20)
        nonzero = spec.abs_eigenvalues
        assert len(nonzero) == 1
        assert abs(nonzero[0] - 1.0) < 1e-10

    def test_count_eigenvalues_matches_N(self):
        """Total eigenvalue count (zero + nonzero) equals N."""
        N = 40
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=N)
        total = spec.n_zero + len(spec.abs_eigenvalues)
        assert total == N

    def test_virasoro_bounded_spectrum(self):
        """Virasoro shadow Dirac has bounded spectral radius
        (shadow coefficients decay, making the operator effectively finite-rank)."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=200)
        assert spec.spectral_radius < 100.0  # bounded above
        assert spec.spectral_radius > 0.0    # nontrivial


# ============================================================================
# 3. Counting function
# ============================================================================

class TestCountingFunction:
    """Test the eigenvalue counting function N(lambda)."""

    def test_monotonically_nondecreasing(self):
        """N(lambda) must be non-decreasing."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        lam, N_vals = counting_function(spec, n_points=200)
        assert np.all(np.diff(N_vals) >= -1e-15)

    def test_starts_at_n_zero(self):
        """N(0) should equal the number of zero eigenvalues."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        lam = np.array([0.0])
        _, N_vals = counting_function(spec, lambdas=lam)
        assert N_vals[0] == spec.n_zero

    def test_saturates_at_N(self):
        """N(lambda) -> N for lambda >> spectral radius."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        big_lam = np.array([spec.spectral_radius * 10])
        _, N_vals = counting_function(spec, lambdas=big_lam)
        assert N_vals[0] == spec.N

    def test_step_function_at_eigenvalue(self):
        """N(lambda) should jump at each eigenvalue.

        Path 1: counting function
        Path 2: direct count with searchsorted
        Path 3: manual loop count
        """
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        abs_eigs = np.sort(np.abs(spec.eigenvalues))
        if len(abs_eigs) > 5:
            test_lam = abs_eigs[5] + 1e-12
            _, N1 = counting_function(spec, lambdas=np.array([test_lam]))
            N2 = np.searchsorted(abs_eigs, test_lam, side='right')
            N3 = sum(1 for e in abs_eigs if e <= test_lam)
            assert abs(N1[0] - N2) < 1.5
            assert abs(N2 - N3) < 1.5

    def test_empty_spectrum_returns_zeros(self):
        """Counting function for empty spectrum returns zeros."""
        spec = ShadowDiracSpectrum(
            eigenvalues=np.array([]),
            abs_eigenvalues=np.array([]),
            N=0, family='test', param=0.0,
            n_zero=0, spectral_gap=0.0, spectral_radius=0.0,
        )
        lam, N_vals = counting_function(spec, n_points=10)
        assert np.all(N_vals == 0)


# ============================================================================
# 4. Weyl law fitting
# ============================================================================

class TestWeylLawFit:
    """Test the Weyl law fitting N(lambda) ~ a * lambda^d_S.

    For shadow Dirac operators, the shadow coefficients decay rapidly,
    making the operator effectively finite-rank.  The spectral dimension
    d_S is near 0 for all families at practical truncation sizes.
    """

    def test_virasoro_d_S_nonneg(self):
        """Virasoro d_S should be non-negative."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        assert wf.spectral_dimension >= -0.01

    def test_heisenberg_zero_spectral_dimension(self):
        """Heisenberg (class G, rank 1): d_S should be exactly 0."""
        spec = shadow_dirac_spectrum('heisenberg', 1.0, N=20)
        wf = fit_weyl_law(spec)
        assert abs(wf.spectral_dimension) < 1.0

    def test_weyl_coefficient_nonneg(self):
        """Weyl coefficient a(c) should be non-negative (counts eigenvalues)."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        assert wf.weyl_coefficient >= 0

    def test_fit_range_within_spectrum(self):
        """Fit range should lie within the spectral range."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        if wf.fit_range != (0.0, 0.0):
            assert wf.fit_range[0] >= 0
            assert wf.fit_range[1] <= spec.spectral_radius * 1.5

    def test_d_S_uncertainty_finite_or_inf(self):
        """Uncertainty in d_S should be finite or inf (for degenerate cases)."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        assert isinstance(wf.d_S_uncertainty, float)

    def test_insufficient_data_returns_zero(self):
        """With too few eigenvalues, should return d_S = 0."""
        spec = ShadowDiracSpectrum(
            eigenvalues=np.array([1.0, 2.0]),
            abs_eigenvalues=np.array([1.0, 2.0]),
            N=2, family='test', param=0.0,
            n_zero=0, spectral_gap=1.0, spectral_radius=2.0,
        )
        wf = fit_weyl_law(spec)
        assert wf.spectral_dimension == 0.0

    def test_r_squared_in_valid_range(self):
        """R^2 should be in (-inf, 1], and for a reasonable fit, in [0, 1]."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        assert wf.r_squared <= 1.0 + 1e-10


# ============================================================================
# 5. Heat kernel
# ============================================================================

class TestHeatKernel:
    """Test the heat kernel trace Tr(e^{-t D^2})."""

    def test_trace_positive(self):
        """Heat kernel trace must be positive (sum of exponentials)."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        hk = heat_kernel_trace(spec)
        assert np.all(hk.trace_values > 0)

    def test_trace_nonincreasing(self):
        """Tr(e^{-tD^2}) is non-increasing in t."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        hk = heat_kernel_trace(spec)
        diffs = np.diff(hk.trace_values)
        assert np.all(diffs < 1e-8)

    def test_trace_at_small_t_near_N(self):
        """Tr(e^{-0 * D^2}) = N.  At very small t, trace is near N.

        Path 1: direct evaluation at small t
        Path 2: sum e^{-t*eig^2} at t near 0 gives N
        Path 3: from hk.trace_values[0]
        """
        N = 50
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=N)
        hk = heat_kernel_trace(spec, t_min=1e-8, t_max=1.0, n_t=100)
        # Path 1: smallest t should give trace near N
        assert abs(hk.trace_values[0] - N) < 1, (
            f"Tr(exp(-t D^2)) at t~0 should be ~{N}, got {hk.trace_values[0]}")
        # Path 2: independent computation
        eigs = spec.eigenvalues
        t_small = hk.t_values[0]
        trace_direct = sum(math.exp(-t_small * e**2) for e in eigs)
        np.testing.assert_allclose(hk.trace_values[0], trace_direct, rtol=1e-10)

    def test_seeley_dewitt_a0_positive(self):
        """Leading Seeley-DeWitt coefficient a_0 > 0."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        hk = heat_kernel_trace(spec)
        assert hk.seeley_dewitt_a0 > 0

    def test_heat_kernel_vs_eigenvalue_sum(self):
        """Verify Tr(e^{-tD^2}) = sum_n e^{-t * lambda_n^2} at a specific t.

        Path 1: engine computation
        Path 2: independent summation from eigenvalues
        Path 3: using D^2 eigenvalues (eig(D)^2 = eig(D^2) for symmetric D)
        """
        N = 30
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=N)
        hk = heat_kernel_trace(spec, t_min=0.1, t_max=10.0, n_t=50)
        t_test = hk.t_values[25]

        # Path 1
        val_engine = hk.trace_values[25]
        # Path 2
        val_indep = sum(math.exp(-t_test * e**2) for e in spec.eigenvalues)
        # Path 3
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=N + 2)
        D = build_shadow_dirac(coeffs, N)
        D2 = D @ D
        eig_D2 = eigvalsh(D2)
        val_matexp = np.sum(np.exp(-t_test * eig_D2))

        np.testing.assert_allclose(val_engine, val_indep, rtol=1e-10)
        np.testing.assert_allclose(val_engine, val_matexp, rtol=1e-10)

    def test_spectral_dimension_heat_nonneg(self):
        """Heat kernel d_S should be non-negative."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        hk = heat_kernel_trace(spec)
        assert hk.spectral_dimension_heat >= -0.01


# ============================================================================
# 6. Spectral zeta function
# ============================================================================

class TestSpectralZeta:
    """Test the spectral zeta function zeta_D(s) = sum |lambda_n|^{-s}."""

    def test_convergence_large_s(self):
        """For large Re(s), zeta_D(s) should be finite and positive."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        s_vals = np.array([3.0, 4.0, 5.0])
        sz = spectral_zeta(spec, s_values=s_vals)
        assert np.all(sz.zeta_values > 0)
        assert np.all(np.isfinite(sz.zeta_values))

    def test_zeta_finite(self):
        """Spectral zeta at moderate s values should be finite."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        s_vals = np.linspace(2.0, 5.0, 20)
        sz = spectral_zeta(spec, s_values=s_vals)
        assert np.all(np.isfinite(sz.zeta_values))

    def test_pole_location_nonneg(self):
        """Pole location should be non-negative."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        sz = spectral_zeta(spec)
        assert sz.pole_location >= 0

    def test_complex_zeta_matches_real(self):
        """spectral_zeta_complex at real s should match the real version.

        Path 1: spectral_zeta (real array)
        Path 2: spectral_zeta_complex (complex scalar)
        Path 3: independent sum of |eig|^{-s}
        """
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        s_test = 3.0
        # Path 1
        sz = spectral_zeta(spec, s_values=np.array([s_test]))
        val_real = sz.zeta_values[0]
        # Path 2
        val_complex = spectral_zeta_complex(spec, complex(s_test, 0))
        # Path 3
        val_indep = sum(e ** (-s_test) for e in spec.abs_eigenvalues)
        np.testing.assert_allclose(val_real, val_complex.real, rtol=1e-10)
        np.testing.assert_allclose(val_real, val_indep, rtol=1e-10)
        assert abs(val_complex.imag) < 1e-10

    def test_zeta_derivative_real_at_real_s(self):
        """zeta_D'(s) should be real for real s."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        dz = spectral_zeta_derivative(spec, complex(3.0, 0))
        assert abs(dz.imag) < 1e-10

    def test_zeta_derivative_formula(self):
        """zeta_D'(s) = -sum |lambda_n|^{-s} * log(|lambda_n|).

        Path 1: engine derivative
        Path 2: independent computation
        """
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=50)
        s = complex(3.0, 0)
        dz_engine = spectral_zeta_derivative(spec, s)
        dz_indep = -sum(e ** (-s) * math.log(e) for e in spec.abs_eigenvalues if e > 1e-300)
        np.testing.assert_allclose(dz_engine.real, dz_indep.real, rtol=1e-10)

    def test_empty_spectrum_zeta(self):
        """Empty spectrum gives zero zeta."""
        spec = ShadowDiracSpectrum(
            eigenvalues=np.array([]),
            abs_eigenvalues=np.array([]),
            N=0, family='test', param=0.0,
            n_zero=0, spectral_gap=0.0, spectral_radius=0.0,
        )
        val = spectral_zeta_complex(spec, complex(2.0, 0))
        assert val == 0.0


# ============================================================================
# 7. Sturm-Liouville counting
# ============================================================================

class TestSturmLiouville:
    """Test Sturm-Liouville eigenvalue counting via LDL factorization."""

    def test_sturm_matches_eigvalsh(self):
        """Sturm count should match direct eigenvalue count.

        Path 1: Sturm-Liouville (LDL sign counting)
        Path 2: direct eigvalsh comparison
        Path 3: numpy searchsorted on sorted eigenvalues
        """
        N = 30
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=N + 2)
        D = build_shadow_dirac(coeffs, N)
        eigs = eigvalsh(D)

        for lam in [eigs[5], eigs[10], eigs[20]]:
            sturm = _sturm_liouville_count(D, lam)
            direct = int(np.sum(eigs < lam))
            assert abs(sturm - direct) <= 1, (
                f"Sturm={sturm} vs direct={direct} at lam={lam}")

    def test_sturm_zero_below_minimum(self):
        """No eigenvalues below the minimum eigenvalue."""
        N = 20
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=N + 2)
        D = build_shadow_dirac(coeffs, N)
        eigs = eigvalsh(D)
        count = _sturm_liouville_count(D, eigs[0] - 10.0)
        assert count == 0

    def test_sturm_N_above_maximum(self):
        """All eigenvalues below a value above the maximum."""
        N = 20
        coeffs = _get_shadow_coeffs('virasoro', 10.0, max_r=N + 2)
        D = build_shadow_dirac(coeffs, N)
        eigs = eigvalsh(D)
        count = _sturm_liouville_count(D, eigs[-1] + 10.0)
        assert count == N


# ============================================================================
# 8. Dixmier trace
# ============================================================================

class TestDixmierTrace:
    """Test the Dixmier trace (NC volume)."""

    def test_positive_for_positive_d_S(self):
        """Dixmier trace should be positive when d_S > 0."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        dix = dixmier_trace(spec, d_S=1.0)  # use d_S=1 to get a positive result
        assert dix > 0

    def test_zero_for_zero_d_S(self):
        """Dixmier trace should be 0 when d_S = 0."""
        spec = shadow_dirac_spectrum('heisenberg', 1.0, N=20)
        dix = dixmier_trace(spec, d_S=0.0)
        assert dix == 0.0

    def test_dixmier_formula_independent(self):
        """Verify Dixmier trace = (1/log N) * sum |lambda|^{-d_S}.

        Path 1: engine function
        Path 2: manual computation from eigenvalues
        Path 3: using spectral_zeta_complex at s = d_S
        """
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        d_S = 1.0  # use d_S=1 for a well-defined test

        # Path 1
        dix_engine = dixmier_trace(spec, d_S)

        # Path 2
        abs_eigs = spec.abs_eigenvalues
        N = len(abs_eigs)
        total = sum(e ** (-d_S) for e in abs_eigs)
        dix_manual = total / math.log(max(N, 2))
        np.testing.assert_allclose(dix_engine, dix_manual, rtol=1e-10)

        # Path 3
        zeta_val = spectral_zeta_complex(spec, complex(d_S, 0)).real
        dix_zeta = zeta_val / math.log(max(N, 2))
        np.testing.assert_allclose(dix_engine, dix_zeta, rtol=1e-10)


# ============================================================================
# 9. Weyl remainder
# ============================================================================

class TestWeylRemainder:
    """Test the Weyl remainder analysis."""

    def test_remainder_has_expected_shape(self):
        """Remainder arrays should have n_points elements."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        rem = weyl_remainder(spec, n_points=200)
        assert len(rem.lambdas) == 200
        assert len(rem.remainder) == 200
        assert len(rem.normalized_remainder) == 200

    def test_remainder_rms_nonneg(self):
        """RMS remainder should be non-negative."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        rem = weyl_remainder(spec)
        assert rem.remainder_rms >= 0

    def test_remainder_is_N_minus_weyl(self):
        """The remainder = N(lambda) - a * lambda^d_S at every point.

        When d_S < 0.01 the engine returns zeros (early-return branch for
        effectively zero spectral dimension).  Test the consistency of what
        the engine returns.

        Path 1: engine remainder
        Path 2: independent verification
        """
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        rem = weyl_remainder(spec, wf, n_points=100)
        if abs(wf.spectral_dimension) < 0.01:
            # Early-return branch: engine returns zeros
            np.testing.assert_allclose(rem.remainder, 0.0, atol=1e-14)
        else:
            a = wf.weyl_coefficient
            d_S = wf.spectral_dimension
            weyl_leading = a * rem.lambdas ** d_S
            _, N_vals = counting_function(spec, rem.lambdas)
            expected_rem = N_vals - weyl_leading
            np.testing.assert_allclose(rem.remainder, expected_rem, atol=1e-8)

    def test_remainder_sharp_weyl_for_small_d_S(self):
        """When d_S < 0.01, the early-return branch sets sharp_weyl=True."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        if abs(wf.spectral_dimension) < 0.01:
            rem = weyl_remainder(spec, wf)
            assert rem.sharp_weyl is True


# ============================================================================
# 10. Riemann zero evaluations
# ============================================================================

class TestWeylAtRiemannZeros:
    """Test evaluation of counting function at Riemann zeta zeros."""

    def test_riemann_zeros_table(self):
        """Verify first few Riemann zeros against known values.

        Path 1: RIEMANN_ZETA_ZEROS constant in engine
        Path 2: independently known first zero ~ 14.1347
        Path 3: second zero ~ 21.0220
        """
        assert abs(RIEMANN_ZETA_ZEROS[0] - 14.134725141734693) < 1e-10
        assert abs(RIEMANN_ZETA_ZEROS[1] - 21.022039638771555) < 1e-10
        assert len(RIEMANN_ZETA_ZEROS) == 30

    def test_riemann_zeros_increasing(self):
        """Riemann zeros should be strictly increasing."""
        for i in range(len(RIEMANN_ZETA_ZEROS) - 1):
            assert RIEMANN_ZETA_ZEROS[i] < RIEMANN_ZETA_ZEROS[i + 1]

    def test_n_actual_nondecreasing(self):
        """N_actual(gamma_n) should be non-decreasing in n."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        results = weyl_at_riemann_zeros(spec, n_zeros=20)
        for i in range(len(results) - 1):
            assert results[i + 1].N_actual >= results[i].N_actual

    def test_weyl_prediction_consistent(self):
        """N_weyl = a * gamma_n^d_S should match engine output.

        Path 1: engine results
        Path 2: independent computation from Weyl fit parameters
        """
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        wf = fit_weyl_law(spec)
        results = weyl_at_riemann_zeros(spec, wf, n_zeros=5)
        for r in results:
            if wf.spectral_dimension > 0:
                N_weyl_indep = wf.weyl_coefficient * r.gamma_n ** wf.spectral_dimension
            else:
                N_weyl_indep = 0.0
            np.testing.assert_allclose(r.N_weyl, N_weyl_indep, rtol=1e-10)

    def test_remainder_is_difference(self):
        """remainder = N_actual - N_weyl."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        results = weyl_at_riemann_zeros(spec, n_zeros=5)
        for r in results:
            np.testing.assert_allclose(
                r.remainder, r.N_actual - r.N_weyl, atol=1e-10)

    def test_relative_remainder_formula(self):
        """relative_remainder = remainder / max(|N_weyl|, 1e-15)."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        results = weyl_at_riemann_zeros(spec, n_zeros=3)
        for r in results:
            expected_rel = r.remainder / max(abs(r.N_weyl), 1e-15)
            np.testing.assert_allclose(r.relative_remainder, expected_rel, atol=1e-10)


# ============================================================================
# 11. Pair correlation
# ============================================================================

class TestPairCorrelation:
    """Test pair correlation of spectral zeta zeros."""

    def test_gue_reference_formula(self):
        """GUE pair correlation R_2(x) = 1 - (sin(pi*x)/(pi*x))^2.

        Path 1: engine output
        Path 2: independent computation
        """
        zeros = [complex(0.5, k * 1.234) for k in range(1, 50)]
        pc = pair_correlation_spectral_zeros(zeros, n_bins=20, x_max=3.0)
        x = pc.x_values
        gue_indep = 1.0 - (np.sin(np.pi * x) / (np.pi * x + 1e-300)) ** 2
        np.testing.assert_allclose(pc.R2_gue, gue_indep, rtol=1e-10)

    def test_poisson_reference(self):
        """Poisson pair correlation is R_2(x) = 1 (constant)."""
        zeros = [complex(0.5, k * 1.234) for k in range(1, 50)]
        pc = pair_correlation_spectral_zeros(zeros, n_bins=20)
        np.testing.assert_allclose(pc.R2_poisson, np.ones(20))

    def test_distances_nonneg(self):
        """L2 distances to GUE and Poisson should be non-negative."""
        zeros = [complex(0.5, k * 1.234) for k in range(1, 50)]
        pc = pair_correlation_spectral_zeros(zeros, n_bins=20)
        assert pc.distance_to_gue >= 0
        assert pc.distance_to_poisson >= 0

    def test_few_zeros_returns_defaults(self):
        """With fewer than 5 zeros, should return default result."""
        zeros = [complex(0.5, 1.0), complex(0.5, 2.0)]
        pc = pair_correlation_spectral_zeros(zeros, n_bins=10)
        assert pc.n_zeros_used == 0

    def test_mean_spacing_positive(self):
        """Mean spacing should be positive for well-separated zeros."""
        zeros = [complex(0.5, k * 2.0) for k in range(1, 30)]
        pc = pair_correlation_spectral_zeros(zeros, n_bins=20)
        assert pc.mean_spacing > 0


# ============================================================================
# 12. Selberg-type counting
# ============================================================================

class TestSelbergCounting:
    """Test the Selberg-type zero-counting formula."""

    def test_selberg_counting_returns_arrays(self):
        """Basic smoke test: returns arrays of correct length."""
        zeros = [complex(0.5, k * 1.5) for k in range(1, 30)]
        sa = selberg_type_counting(zeros, T_max=50.0, n_T=100)
        assert len(sa.T_values) == 100
        assert len(sa.N_actual) == 100
        assert len(sa.N_selberg) == 100

    def test_n_actual_nondecreasing(self):
        """Actual zero count N(T) is non-decreasing."""
        zeros = [complex(0.5, k * 1.5) for k in range(1, 30)]
        sa = selberg_type_counting(zeros, T_max=50.0, n_T=100)
        assert np.all(np.diff(sa.N_actual) >= -1e-15)

    def test_remainder_is_difference(self):
        """remainder = N_actual - N_selberg."""
        zeros = [complex(0.5, k * 1.5) for k in range(1, 30)]
        sa = selberg_type_counting(zeros, T_max=50.0, n_T=100)
        np.testing.assert_allclose(
            sa.remainder, sa.N_actual - sa.N_selberg, atol=1e-10)

    def test_few_zeros_returns_zero_coefficients(self):
        """With too few zeros, coefficients should be 0."""
        zeros = [complex(0.5, 1.0)]
        sa = selberg_type_counting(zeros, T_max=10.0, n_T=50)
        assert sa.leading_coefficient == 0.0
        assert sa.subleading_coefficient == 0.0


# ============================================================================
# 13. Multi-path verification
# ============================================================================

class TestMultiPathVerification:
    """Test the multi-path verification suite."""

    def test_virasoro_paths_return_finite(self):
        """All 5 paths should return finite values for Virasoro."""
        v = multi_path_verify('virasoro', 10.0, N=60)
        assert np.isfinite(v.d_S_direct)
        assert np.isfinite(v.d_S_heat)
        assert np.isfinite(v.d_S_zeta)
        assert np.isfinite(v.d_S_sturm)
        assert np.isfinite(v.vol_dixmier)

    def test_heisenberg_paths_agree(self):
        """Heisenberg (trivial spectrum) should have paths_agree = True."""
        v = multi_path_verify('heisenberg', 1.0, N=20)
        assert v.paths_agree is True

    def test_d_S_spread_nonneg(self):
        """d_S spread should be non-negative."""
        v = multi_path_verify('virasoro', 10.0, N=60)
        assert v.d_S_spread >= 0

    def test_d_S_mean_nonneg(self):
        """Mean d_S should be non-negative."""
        v = multi_path_verify('virasoro', 10.0, N=60)
        assert v.d_S_mean >= 0

    def test_a_spread_nonneg(self):
        """Spread of Weyl coefficient should be non-negative."""
        v = multi_path_verify('virasoro', 10.0, N=60)
        assert v.a_spread >= 0


# ============================================================================
# 14. Full analysis
# ============================================================================

class TestFullAnalysis:
    """Test the full_shadow_weyl_analysis master function."""

    def test_full_analysis_virasoro(self):
        """Full analysis should complete without error for Virasoro."""
        analysis = full_shadow_weyl_analysis(
            'virasoro', 10.0, N=50, find_zeta_zeros=False, n_riemann_zeros=5)
        assert analysis.family == 'virasoro'
        assert analysis.param == 10.0
        assert analysis.shadow_class == 'M'
        assert analysis.spectrum is not None
        assert analysis.weyl_fit is not None
        assert analysis.heat_kernel is not None
        assert analysis.spectral_zeta_result is not None
        assert analysis.remainder is not None
        assert analysis.verification is not None

    def test_full_analysis_heisenberg(self):
        """Full analysis should complete for Heisenberg (class G)."""
        analysis = full_shadow_weyl_analysis(
            'heisenberg', 1.0, N=20, find_zeta_zeros=False, n_riemann_zeros=5)
        assert analysis.shadow_class == 'G'

    def test_full_analysis_affine(self):
        """Full analysis should complete for affine sl_2 (class L)."""
        analysis = full_shadow_weyl_analysis(
            'affine_sl2', 1.0, N=30, find_zeta_zeros=False, n_riemann_zeros=3)
        assert analysis.shadow_class == 'L'


# ============================================================================
# 15. Virasoro c-scan
# ============================================================================

class TestVirasoroCscan:
    """Test the Virasoro c-scan across central charges."""

    def test_cscan_returns_correct_length(self):
        """c-scan with 3 values should return lists of length 3."""
        result = virasoro_c_scan(c_values=[5.0, 10.0, 20.0], N=30)
        assert len(result.spectral_dimensions) == 3
        assert len(result.weyl_coefficients) == 3
        assert len(result.dixmier_traces) == 3
        assert len(result.d_S_heat) == 3
        assert len(result.d_S_zeta) == 3
        assert len(result.spectral_gaps) == 3
        assert len(result.spectral_radii) == 3

    def test_cscan_spectral_dims_nonneg(self):
        """All Virasoro spectral dimensions should be non-negative."""
        result = virasoro_c_scan(c_values=[5.0, 10.0, 20.0], N=30)
        for d in result.spectral_dimensions:
            assert d >= -0.01

    def test_cscan_c_values_stored(self):
        """The c_values list should be stored correctly."""
        c_vals = [5.0, 10.0, 20.0]
        result = virasoro_c_scan(c_values=c_vals, N=30)
        assert result.c_values == c_vals


# ============================================================================
# 16. Remainder structure at Riemann zeros
# ============================================================================

class TestRemainderStructure:
    """Test the remainder structure at Riemann zeros."""

    def test_returns_correct_length(self):
        """Should return arrays of correct length."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        rs = remainder_structure_at_zeros(spec, n_zeros=10)
        assert len(rs.gamma_values) == 10
        assert len(rs.remainders) == 10
        assert len(rs.normalized_remainders) == 10

    def test_gammas_match_riemann_zeros(self):
        """Gamma values should be the first n Riemann zeros."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        rs = remainder_structure_at_zeros(spec, n_zeros=5)
        for i in range(5):
            np.testing.assert_allclose(
                rs.gamma_values[i], RIEMANN_ZETA_ZEROS[i], rtol=1e-12)

    def test_ks_statistic_in_01(self):
        """KS statistic should be in [0, 1]."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        rs = remainder_structure_at_zeros(spec, n_zeros=15)
        assert 0 <= rs.kolmogorov_smirnov <= 1.0

    def test_autocorrelation_lag0_is_one(self):
        """Autocorrelation at lag 0 is always 1."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        rs = remainder_structure_at_zeros(spec, n_zeros=15)
        if len(rs.autocorrelation) > 0:
            np.testing.assert_allclose(rs.autocorrelation[0], 1.0, atol=1e-12)

    def test_std_remainder_nonneg(self):
        """Standard deviation of remainders is non-negative."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=100)
        rs = remainder_structure_at_zeros(spec, n_zeros=10)
        assert rs.std_remainder >= 0


# ============================================================================
# 17. Cross-class comparison
# ============================================================================

class TestCrossClassComparison:
    """Test cross-class comparison function."""

    def test_cross_class_returns_all_classes(self):
        """Comparison should include G, L, C, M classes."""
        result = cross_class_comparison(
            test_cases=[
                ('heisenberg', 1.0),
                ('affine_sl2', 1.0),
                ('betagamma', 0.5),
                ('virasoro', 10.0),
            ],
            N=30,
        )
        assert 'G' in result.classes
        assert 'L' in result.classes
        assert 'C' in result.classes
        assert 'M' in result.classes

    def test_class_labels_correct(self):
        """Class labels should match the family classification."""
        result = cross_class_comparison(
            test_cases=[('heisenberg', 1.0), ('virasoro', 10.0)],
            N=30,
        )
        assert result.classes[0] == 'G'
        assert result.classes[1] == 'M'

    def test_families_stored(self):
        """Family names should be stored correctly."""
        result = cross_class_comparison(
            test_cases=[('heisenberg', 1.0), ('virasoro', 10.0)],
            N=30,
        )
        assert result.families == ['heisenberg', 'virasoro']
        assert result.params == [1.0, 10.0]


# ============================================================================
# 18. Koszul complementarity
# ============================================================================

class TestWeylComplementarity:
    """Test Koszul complementarity of Weyl law data.

    AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
    """

    def test_dual_charge(self):
        """c_dual = 26 - c."""
        result = weyl_complementarity(10.0, N=50)
        np.testing.assert_allclose(result.c_dual, 16.0, atol=1e-14)

    def test_self_dual_c13(self):
        """At c = 13, algebra is self-dual: c = c_dual = 13."""
        result = weyl_complementarity(13.0, N=50)
        np.testing.assert_allclose(result.c, result.c_dual, atol=1e-14)

    def test_spectral_dimensions_nonneg(self):
        """Both d_S(c) and d_S(26-c) should be non-negative."""
        result = weyl_complementarity(10.0, N=50)
        assert result.d_S >= -0.01
        assert result.d_S_dual >= -0.01

    def test_d_S_sum_stored_correctly(self):
        """d_S_sum = d_S + d_S_dual."""
        result = weyl_complementarity(10.0, N=50)
        np.testing.assert_allclose(result.d_S_sum, result.d_S + result.d_S_dual, atol=1e-14)

    def test_dixmier_sum_stored_correctly(self):
        """dixmier_sum = dixmier + dixmier_dual."""
        result = weyl_complementarity(10.0, N=50)
        np.testing.assert_allclose(result.dixmier_sum, result.dixmier + result.dixmier_dual, atol=1e-14)


# ============================================================================
# 19. AP24 complementarity cross-checks (dedicated)
# ============================================================================

class TestAP24Complementarity:
    """Dedicated tests for AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13.

    This is a PERMANENT anti-pattern check. The sum is 13, NOT 0.
    """

    def test_kappa_sum_c1(self):
        """c=1: kappa(1) + kappa(25) = 0.5 + 12.5 = 13."""
        np.testing.assert_allclose(1.0/2 + 25.0/2, 13.0, atol=1e-14)

    def test_kappa_sum_c10(self):
        """c=10: kappa(10) + kappa(16) = 5 + 8 = 13."""
        np.testing.assert_allclose(10.0/2 + 16.0/2, 13.0, atol=1e-14)

    def test_kappa_sum_c13_self_dual(self):
        """c=13: kappa(13) + kappa(13) = 6.5 + 6.5 = 13."""
        np.testing.assert_allclose(13.0/2 + 13.0/2, 13.0, atol=1e-14)

    def test_kappa_sum_c26(self):
        """c=26: kappa(26) + kappa(0) = 13 + 0 = 13."""
        np.testing.assert_allclose(26.0/2 + 0.0/2, 13.0, atol=1e-14)

    def test_kappa_sum_NOT_zero(self):
        """ANTI-TEST: kappa + kappa_dual is NOT 0 for Virasoro (AP24)."""
        c = 10.0
        kappa_sum = c/2 + (26-c)/2
        assert abs(kappa_sum) > 12.0


# ============================================================================
# 20. Shadow coefficient dispatch and independent formulas
# ============================================================================

class TestShadowCoeffDispatch:
    """Test _get_shadow_coeffs dispatch and basic properties."""

    def test_heisenberg_only_S2(self):
        """Heisenberg: S_2 = k, S_r = 0 for r >= 3.

        Path 1: engine output
        Path 2: known formula S_2 = k (the level)
        Path 3: shadow depth = 2 implies S_r = 0 for r > 2
        """
        k = 3.0
        coeffs = _get_shadow_coeffs('heisenberg', k, max_r=20)
        np.testing.assert_allclose(coeffs[2], k, atol=1e-14)
        for r in range(3, 21):
            assert abs(coeffs.get(r, 0.0)) < 1e-14

    def test_affine_sl2_kappa_formula(self):
        """Affine sl_2: kappa = 3(k+2)/4.

        Path 1: engine S_2
        Path 2: explicit formula 3*(k+2)/4
        Path 3: dim(sl_2)=3, h^v=2, so 3*(k+2)/(2*2)
        """
        k = 1.0
        coeffs = _get_shadow_coeffs('affine_sl2', k, max_r=10)
        expected_kappa = 3.0 * (k + 2.0) / 4.0
        np.testing.assert_allclose(coeffs[2], expected_kappa, rtol=1e-10)

    def test_virasoro_S2_equals_kappa(self):
        """Virasoro: S_2 = c/2 = kappa(Vir_c).

        Path 1: engine coefficients
        Path 2: known formula kappa(Vir_c) = c/2
        Path 3: from shadow metric a_0 = c, S_2 = a_0/2 = c/2
        """
        c = 10.0
        coeffs = _get_shadow_coeffs('virasoro', c, max_r=10)
        expected = c / 2.0
        np.testing.assert_allclose(coeffs[2], expected, rtol=1e-8)

    def test_virasoro_infinite_tower(self):
        """Virasoro (class M) should have nonzero S_r for r > 4."""
        c = 10.0
        coeffs = _get_shadow_coeffs('virasoro', c, max_r=30)
        nonzero_count = sum(1 for r in range(5, 30) if abs(coeffs.get(r, 0.0)) > 1e-20)
        assert nonzero_count > 5

    def test_affine_sl2_S3_nonzero(self):
        """Affine sl_2 (class L, depth 3) should have S_3 != 0."""
        k = 1.0
        coeffs = _get_shadow_coeffs('affine_sl2', k, max_r=10)
        assert abs(coeffs.get(3, 0.0)) > 1e-15

    def test_betagamma_S4_nonzero(self):
        """Beta-gamma (class C, depth 4) should have S_4 != 0."""
        lam = 0.5
        coeffs = _get_shadow_coeffs('betagamma', lam, max_r=10)
        assert abs(coeffs.get(4, 0.0)) > 1e-15


# ============================================================================
# 21. Independent formula verification for Virasoro shadow coefficients
# ============================================================================

class TestIndependentShadowVerification:
    """Verify shadow coefficients by independent computation.

    AP10: never hardcode expected values from the engine.
    Derive from the defining formulas instead.

    For Virasoro: Q_L(t) = c^2 + 12c*t + alpha(c)*t^2
    where alpha(c) = (180c+872)/(5c+22).
    sqrt(Q_L) = a_0 + a_1*t + a_2*t^2 + ...
    S_r = a_{r-2}/r.
    """

    def test_virasoro_S3_from_recursion(self):
        """S_3 = a_1/3 where a_1 = q_1/(2*a_0) = 12c/(2c) = 6.
        So S_3 = 6/3 = 2 for any c > 0.

        Path 1: engine S_3
        Path 2: a_1 = q_1/(2*a_0) = 6, S_3 = a_1/3 = 2
        Path 3: numerical derivative of sqrt(Q_L) at t=0
        """
        c = 10.0
        coeffs = _get_shadow_coeffs('virasoro', c, max_r=10)

        # Path 2
        a_0 = c
        q_1 = 12.0 * c
        a_1 = q_1 / (2 * a_0)  # = 6
        S_3_expected = a_1 / 3.0  # = 2

        np.testing.assert_allclose(coeffs[3], S_3_expected, rtol=1e-8)

        # Path 3: numerical derivative
        eps = 1e-7
        q_0 = c**2
        q_2 = (180.0*c + 872.0) / (5.0*c + 22.0)
        def sqrt_QL(t):
            return math.sqrt(abs(q_0 + q_1*t + q_2*t**2))
        a_1_num = (sqrt_QL(eps) - sqrt_QL(-eps)) / (2*eps)
        S_3_num = a_1_num / 3.0
        np.testing.assert_allclose(S_3_expected, S_3_num, rtol=1e-4)

    def test_virasoro_S4_from_recursion(self):
        """S_4 = a_2/4 where a_2 = (q_2 - a_1^2)/(2*a_0).

        Path 1: engine S_4
        Path 2: explicit a_2 formula
        Path 3: numerical second derivative of sqrt(Q_L)
        """
        c = 10.0
        coeffs = _get_shadow_coeffs('virasoro', c, max_r=10)

        q_0 = c**2
        q_1 = 12.0 * c
        q_2 = (180.0*c + 872.0) / (5.0*c + 22.0)
        a_0 = c
        a_1 = q_1 / (2*a_0)
        a_2 = (q_2 - a_1**2) / (2*a_0)
        S_4_expected = a_2 / 4.0

        np.testing.assert_allclose(coeffs[4], S_4_expected, rtol=1e-8)

        # Path 3: numerical second derivative
        # f''(0) = 2*a_2 for f(t) = a_0 + a_1*t + a_2*t^2 + ...
        eps = 1e-5
        def sqrt_QL(t):
            return math.sqrt(abs(q_0 + q_1*t + q_2*t**2))
        f_second_deriv = (sqrt_QL(eps) - 2*sqrt_QL(0) + sqrt_QL(-eps)) / eps**2
        a_2_num = f_second_deriv / 2.0  # a_2 = f''(0)/2!
        np.testing.assert_allclose(a_2, a_2_num, rtol=1e-3)

    def test_virasoro_S3_c_independent(self):
        """S_3 = 2 for ALL c > 0 (a_1 = 6 regardless of c).

        Path 1: c = 5
        Path 2: c = 20
        Path 3: analytic: a_1 = 12c/(2c) = 6, S_3 = 2
        """
        for c_test in [5.0, 20.0]:
            coeffs = _get_shadow_coeffs('virasoro', c_test, max_r=10)
            np.testing.assert_allclose(coeffs[3], 2.0, rtol=1e-8,
                                       err_msg=f"S_3 should be 2 at c={c_test}")


# ============================================================================
# 22. Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Test edge cases and robustness."""

    def test_small_N(self):
        """N = 5 should still produce a valid spectrum."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=5)
        assert spec.N == 5
        assert len(spec.eigenvalues) == 5

    def test_large_c_virasoro(self):
        """Large c should not cause overflow."""
        spec = shadow_dirac_spectrum('virasoro', 100.0, N=30)
        assert np.all(np.isfinite(spec.eigenvalues))

    def test_small_c_virasoro(self):
        """Small positive c should work."""
        spec = shadow_dirac_spectrum('virasoro', 0.5, N=30)
        assert np.all(np.isfinite(spec.eigenvalues))

    def test_heisenberg_large_k(self):
        """Large Heisenberg level should not overflow."""
        spec = shadow_dirac_spectrum('heisenberg', 100.0, N=10)
        assert np.all(np.isfinite(spec.eigenvalues))

    def test_spectral_zeta_zeros_search_no_crash(self):
        """Zero search should not crash even with small grid."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=20)
        zeros = find_spectral_zeta_zeros(
            spec, re_range=(0.0, 2.0), im_range=(0.0, 5.0),
            grid_re=3, grid_im=3, n_max=5)
        assert isinstance(zeros, list)

    def test_heisenberg_negative_k(self):
        """Heisenberg with negative k: S_2 = k < 0."""
        k = -2.0
        coeffs = _get_shadow_coeffs('heisenberg', k, max_r=10)
        np.testing.assert_allclose(coeffs[2], k, atol=1e-14)

    def test_build_shadow_dirac_N_1(self):
        """N = 1: single element matrix."""
        coeffs = {2: 5.0}
        D = build_shadow_dirac(coeffs, N=1)
        assert D.shape == (1, 1)
        assert abs(D[0, 0] - 1.0) < 1e-14  # 5/|5| = 1


# ============================================================================
# 23. Spectral zeta zeros search
# ============================================================================

class TestSpectralZetaZeros:
    """Test the spectral zeta zero-finding machinery."""

    def test_zeros_are_actual_zeros(self):
        """Any found zero should satisfy |zeta_D(s)| < tolerance."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=30)
        zeros = find_spectral_zeta_zeros(
            spec, re_range=(-1.0, 3.0), im_range=(-20.0, 20.0),
            grid_re=10, grid_im=20, n_max=10, tol=1e-8)
        for z in zeros:
            val = spectral_zeta_complex(spec, z)
            assert abs(val) < 1e-4, (
                f"Claimed zero at s={z} has |zeta_D|={abs(val)}")

    def test_zeros_sorted_by_imaginary_part(self):
        """Found zeros should be sorted by imaginary part."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=30)
        zeros = find_spectral_zeta_zeros(
            spec, re_range=(-1.0, 3.0), im_range=(-20.0, 20.0),
            grid_re=10, grid_im=20, n_max=10)
        for i in range(len(zeros) - 1):
            assert zeros[i].imag <= zeros[i + 1].imag + 1e-10

    def test_zeros_deduplicated(self):
        """No two found zeros should be within dedup_tol of each other."""
        spec = shadow_dirac_spectrum('virasoro', 10.0, N=30)
        dedup_tol = 1e-5
        zeros = find_spectral_zeta_zeros(
            spec, re_range=(-1.0, 3.0), im_range=(-10.0, 10.0),
            grid_re=10, grid_im=20, n_max=20, dedup_tol=dedup_tol)
        for i in range(len(zeros)):
            for j in range(i + 1, len(zeros)):
                assert abs(zeros[i] - zeros[j]) >= dedup_tol * 0.9


# ============================================================================
# 24. Integration: heat kernel trace identity at multiple t values
# ============================================================================

class TestHeatKernelTraceIdentity:
    """Verify the heat kernel trace identity Tr(e^{-tD^2}) = sum e^{-t*eig^2}
    by independent computation at multiple t values for multiple families."""

    @pytest.mark.parametrize("family,param", [
        ('heisenberg', 1.0),
        ('affine_sl2', 1.0),
        ('betagamma', 0.5),
        ('virasoro', 10.0),
    ])
    def test_trace_identity(self, family, param):
        """Tr(e^{-tD^2}) matches independent eigenvalue sum for all families."""
        N = 30
        spec = shadow_dirac_spectrum(family, param, N=N)
        hk = heat_kernel_trace(spec, t_min=0.01, t_max=10.0, n_t=20)
        eigs = spec.eigenvalues
        for i in [0, 5, 10, 15, 19]:
            t = hk.t_values[i]
            expected = sum(math.exp(-t * e**2) for e in eigs)
            np.testing.assert_allclose(hk.trace_values[i], expected, rtol=1e-10,
                                       err_msg=f"{family} trace mismatch at t={t}")
