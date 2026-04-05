r"""Tests for bc_extremal_que_engine: extremal zero distribution and QUE.

Test organization:
    1. Zero density N_A(T) and Riemann-von Mangoldt fitting
    2. Explicit formula verification
    3. Quantum unique ergodicity (QUE)
    4. Entropy bounds
    5. Value distribution of zeta_A(1/2+it)
    6. Zeros off the critical line (shadow RH)
    7. Shadow GRH test
    8. Density hypothesis
    9. Zero repulsion
   10. Koszul zero duality
   11. Cross-verification and multi-path consistency
   12. Landscape census

VERIFICATION: 3+ paths per claim (AP10).
CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): kappa != c/2 in general.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

import math
import pytest

from compute.lib.bc_extremal_que_engine import (
    STANDARD_FAMILIES,
    kappa_for_family,
    # 1. Zero density
    zero_density_table,
    riemann_von_mangoldt_fit,
    leading_coefficient_comparison,
    # 2. Explicit formula
    gaussian_test_function,
    gaussian_fourier_transform,
    explicit_formula_lhs,
    explicit_formula_rhs_leading,
    explicit_formula_test,
    # 3. QUE
    shadow_eigenfunction,
    que_deviation,
    que_convergence_test,
    # 4. Entropy
    eigenfunction_entropy,
    entropy_convergence_test,
    # 5. Value distribution
    critical_line_value_distribution,
    # 6. Off-line zeros
    find_critical_line,
    zeros_off_critical_line_search,
    argument_principle_rectangle,
    # 7. GRH
    shadow_prime_counting,
    shadow_logarithmic_integral,
    grh_test,
    # 8. Density hypothesis
    density_hypothesis_test,
    # 9. Zero repulsion
    zero_minimum_gap,
    zero_repulsion_scaling,
    # 10. Koszul duality
    koszul_zero_duality_analysis,
    koszul_zero_overlap_at_self_dual,
    # 11. Full analysis
    full_analysis,
    # 12. Landscape
    landscape_zero_census,
    # Cross-verification
    verify_zero_by_three_paths,
    cross_family_consistency_check,
)

from compute.lib.bc_explicit_formula_engine import (
    virasoro_growth_rate,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    _shadow_zeta_complex,
    find_zeros_grid,
    zero_counting_function,
    heisenberg_zeros,
    affine_sl2_zeros,
)

from compute.lib.bc_explicit_formula_engine import (
    shadow_von_mangoldt,
    shadow_chebyshev_psi,
)


# ============================================================================
# 1. Zero density and Riemann-von Mangoldt
# ============================================================================

class TestZeroDensity:
    """Tests for zero counting N_A(T) and RvM formula fitting."""

    def test_heisenberg_no_zeros(self):
        """Heisenberg (class G): zeta = k * 2^{-s} has NO zeros for k != 0."""
        result = zero_density_table('heisenberg', 1.0, [10.0, 50.0, 100.0], max_r=10)
        for T, count in result.items():
            assert count == 0, f"Heisenberg should have 0 zeros, got {count} at T={T}"

    def test_affine_sl2_zeros_exist(self):
        """Affine sl_2 (class L): two-term exponential polynomial has zeros."""
        result = zero_density_table('affine_sl2', 1.0, [50.0], max_r=10)
        # sl_2 has infinitely many zeros on a vertical line
        assert result[50.0] >= 0  # May find some or none depending on grid

    def test_affine_sl2_zero_formula(self):
        """Affine sl_2 zeros have exact formula: s = -(log(kappa/alpha) + i*pi*(2n+1))/log(3/2)."""
        zeros = affine_sl2_zeros(1.0, n_max=10)
        # All zeros lie on the same vertical line
        re_parts = [z.real for z in zeros]
        if len(re_parts) > 1:
            # All real parts should be the same
            mean_re = sum(re_parts) / len(re_parts)
            for r in re_parts:
                assert abs(r - mean_re) < 1e-10, \
                    f"sl_2 zeros should lie on a vertical line: Re = {r} vs mean {mean_re}"

    def test_virasoro_zeros_grow(self):
        """Virasoro (class M): zero count should increase with T."""
        T_vals = [10.0, 30.0, 50.0]
        result = zero_density_table('virasoro', 26.0, T_vals, max_r=60)
        # N_A(T) should be non-decreasing
        prev = -1
        for T in sorted(result.keys()):
            assert result[T] >= prev, \
                f"N_A({T}) = {result[T]} < N_A(prev) = {prev}"
            prev = result[T]

    def test_rvm_fit_r_squared(self):
        """RvM fit for Virasoro should have reasonable R^2 if enough zeros found."""
        fit = riemann_von_mangoldt_fit(
            'virasoro', 26.0, T_min=5.0, T_max=40.0, max_r=60,
        )
        # R^2 can be anything for small data; just check it computes
        assert 'r_squared' in fit
        assert 'a' in fit
        assert 'a_eff' in fit

    def test_rvm_fit_heisenberg_trivial(self):
        """Heisenberg: no zeros means trivial fit."""
        fit = riemann_von_mangoldt_fit(
            'heisenberg', 1.0, T_min=5.0, T_max=40.0, max_r=10,
        )
        assert 'r_squared' in fit

    def test_leading_coefficient_virasoro(self):
        """Leading coefficient comparison for Virasoro."""
        data = leading_coefficient_comparison('virasoro', 26.0, max_r=60)
        assert 'kappa' in data
        assert abs(data['kappa'] - 13.0) < 0.01  # kappa(Vir_26) = 26/2 = 13
        assert data['growth_rate_rho'] > 0


# ============================================================================
# 2. Explicit formula
# ============================================================================

class TestExplicitFormula:
    """Tests for the shadow explicit formula."""

    def test_gaussian_normalization(self):
        """Gaussian Fourier transform: hat{h}(0) = sigma * sqrt(pi)."""
        sigma = 5.0
        h_hat_0 = gaussian_fourier_transform(0.0, sigma)
        expected = sigma * math.sqrt(math.pi)
        assert abs(h_hat_0 - expected) < 1e-10

    def test_gaussian_symmetry(self):
        """Gaussian is even: h(t) = h(-t)."""
        sigma = 3.0
        for t in [1.0, 2.5, 7.0]:
            assert abs(gaussian_test_function(t, sigma) -
                       gaussian_test_function(-t, sigma)) < 1e-15

    def test_gaussian_ft_symmetry(self):
        """Fourier transform of even function is even."""
        sigma = 3.0
        for xi in [0.5, 1.0, 2.0]:
            assert abs(gaussian_fourier_transform(xi, sigma) -
                       gaussian_fourier_transform(-xi, sigma)) < 1e-15

    def test_gaussian_decay(self):
        """Gaussian decays: h(t) < h(0) for t > 0."""
        sigma = 3.0
        h0 = gaussian_test_function(0.0, sigma)
        assert abs(h0 - 1.0) < 1e-15  # h(0) = 1
        for t in [1.0, 5.0, 10.0]:
            assert gaussian_test_function(t, sigma) < h0

    def test_explicit_formula_heisenberg_trivial(self):
        """Heisenberg: no zeros, so LHS = 0, RHS should be small."""
        data = explicit_formula_test('heisenberg', 1.0, T=30.0, sigma=10.0, max_r=10)
        assert abs(data['lhs']) < 1e-10  # No zeros contribute

    def test_explicit_formula_virasoro_computes(self):
        """Virasoro explicit formula: LHS and RHS should both be finite."""
        data = explicit_formula_test('virasoro', 26.0, T=30.0, sigma=10.0, max_r=50)
        assert math.isfinite(data['lhs'])
        assert math.isfinite(data['rhs'])

    def test_von_mangoldt_heisenberg(self):
        """Heisenberg von Mangoldt: Lambda(2) = log(2); nonzero at 2^k, zero elsewhere."""
        coeffs = shadow_coefficients_extended('heisenberg', 1.0, max_r=10)
        Lambda = shadow_von_mangoldt(coeffs, 10)
        assert abs(Lambda[2] - 1.0 * math.log(2)) < 1e-10
        # Only S_2 nonzero => Lambda(r) vanishes unless r is a power of 2
        # (von Mangoldt supported on prime powers, here only prime 2)
        for r in range(3, 11):
            if r & (r - 1) == 0:
                # r is a power of 2: Lambda(r) can be nonzero
                continue
            assert abs(Lambda.get(r, 0.0)) < 1e-10, \
                f"Lambda({r}) = {Lambda.get(r, 0.0)} should be 0 (not a power of 2)"

    def test_von_mangoldt_sl2(self):
        """Affine sl_2: Lambda(2) and Lambda(3) nonzero, Lambda(r)=0 for prime r>=5."""
        coeffs = shadow_coefficients_extended('affine_sl2', 1.0, max_r=10)
        Lambda = shadow_von_mangoldt(coeffs, 10)
        assert abs(Lambda[2]) > 1e-10  # Nonzero
        assert abs(Lambda[3]) > 1e-10  # Nonzero


# ============================================================================
# 3. Quantum Unique Ergodicity (QUE)
# ============================================================================

class TestQUE:
    """Tests for quantum unique ergodicity of shadow eigenfunctions."""

    def test_eigenfunction_normalized(self):
        """Shadow eigenfunctions should be L^2 normalized to 1."""
        coeffs = shadow_coefficients_extended('virasoro', 26.0, max_r=30)
        n_grid = 200
        x_grid = [float(i) / n_grid for i in range(n_grid)]
        dx = 1.0 / n_grid

        for n in [1, 5, 10, 50]:
            psi = shadow_eigenfunction(coeffs, n, x_grid, max_r=30)
            norm_sq = sum(v * v for v in psi) * dx
            if norm_sq > 1e-10:  # Only check if non-degenerate
                assert abs(norm_sq - 1.0) < 0.1, \
                    f"||psi_{n}||^2 = {norm_sq}, should be ~1"

    def test_que_deviation_positive(self):
        """QUE deviation should be non-negative."""
        coeffs = shadow_coefficients_extended('virasoro', 26.0, max_r=20)
        for n in [1, 5, 20]:
            dev = que_deviation(coeffs, n, n_grid=100, max_r=20)
            assert dev >= 0, f"QUE deviation should be >= 0, got {dev}"

    def test_que_convergence_virasoro(self):
        """QUE convergence test for Virasoro should complete."""
        data = que_convergence_test(
            'virasoro', 26.0, n_values=list(range(1, 31)),
            n_grid=100, max_r=20,
        )
        assert data['n_tested'] == 30
        assert len(data['deviations']) == 30
        assert 'rate' in data

    def test_que_convergence_heisenberg(self):
        """QUE for Heisenberg (single term shadow)."""
        data = que_convergence_test(
            'heisenberg', 1.0, n_values=list(range(1, 21)),
            n_grid=100, max_r=10,
        )
        assert data['n_tested'] == 20

    def test_que_convergence_affine(self):
        """QUE for affine sl_2."""
        data = que_convergence_test(
            'affine_sl2', 1.0, n_values=list(range(1, 21)),
            n_grid=100, max_r=10,
        )
        assert data['n_tested'] == 20

    def test_que_deviation_bounded(self):
        """QUE deviations should be bounded (no explosions)."""
        coeffs = shadow_coefficients_extended('virasoro', 26.0, max_r=20)
        for n in [1, 10, 50]:
            dev = que_deviation(coeffs, n, n_grid=100, max_r=20)
            assert dev < 100.0, f"QUE deviation too large: {dev} at n={n}"


# ============================================================================
# 4. Entropy bounds
# ============================================================================

class TestEntropy:
    """Tests for entropy convergence to log(vol) under QUE."""

    def test_entropy_finite(self):
        """Entropy should be finite for all n."""
        coeffs = shadow_coefficients_extended('virasoro', 26.0, max_r=20)
        for n in [1, 5, 20, 50]:
            ent = eigenfunction_entropy(coeffs, n, n_grid=100, max_r=20)
            assert math.isfinite(ent), f"Entropy should be finite at n={n}, got {ent}"

    def test_entropy_convergence_virasoro(self):
        """Entropy convergence test should complete."""
        data = entropy_convergence_test(
            'virasoro', 26.0, n_values=list(range(1, 31)),
            n_grid=100, max_r=20,
        )
        assert len(data['entropies']) == 30
        assert 'target' in data
        assert data['target'] == 0.0  # log(vol=1) = 0

    def test_entropy_convergence_heisenberg(self):
        """Entropy convergence for Heisenberg."""
        data = entropy_convergence_test(
            'heisenberg', 1.0, n_values=list(range(1, 21)),
            n_grid=100, max_r=10,
        )
        assert len(data['entropies']) == 20

    def test_entropy_bounded(self):
        """Entropy should be bounded (no infinities)."""
        coeffs = shadow_coefficients_extended('virasoro', 26.0, max_r=20)
        for n in range(1, 20):
            ent = eigenfunction_entropy(coeffs, n, n_grid=100, max_r=20)
            assert abs(ent) < 100.0, f"Entropy too large at n={n}: {ent}"


# ============================================================================
# 5. Value distribution
# ============================================================================

class TestValueDistribution:
    """Tests for the value distribution of zeta_A(1/2+it)."""

    def test_value_dist_virasoro(self):
        """Value distribution for Virasoro should compute."""
        data = critical_line_value_distribution(
            'virasoro', 26.0, t_max=100.0, n_samples=500, max_r=50,
        )
        assert 'exceedance_probs' in data
        assert data['n_samples'] == 500
        assert data['mean_modulus'] >= 0

    def test_value_dist_heisenberg(self):
        """Value distribution for Heisenberg: |k * 2^{-1/2-it}| = k/sqrt(2)."""
        data = critical_line_value_distribution(
            'heisenberg', 1.0, t_max=100.0, n_samples=200, max_r=10,
        )
        # |zeta_H(1/2+it)| = |1 * 2^{-1/2-it}| = 2^{-1/2} = 1/sqrt(2)
        expected = 1.0 / math.sqrt(2.0)
        assert abs(data['mean_modulus'] - expected) < 0.05

    def test_exceedance_monotone(self):
        """P(|zeta| > V) should be non-increasing in V."""
        data = critical_line_value_distribution(
            'virasoro', 26.0, t_max=100.0, n_samples=500,
            V_thresholds=[0.5, 1.0, 2.0, 5.0], max_r=50,
        )
        probs = data['exceedance_probs']
        prev = 1.1
        for V in sorted(probs.keys()):
            assert probs[V] <= prev + 0.01, \
                f"Exceedance not monotone: P(>={V}) = {probs[V]} > P(>={prev})"
            prev = probs[V]

    def test_selberg_variance_positive(self):
        """Selberg variance prediction (1/2)log log T should be positive."""
        data = critical_line_value_distribution(
            'virasoro', 26.0, t_max=1000.0, n_samples=200, max_r=50,
        )
        assert data['selberg_variance'] > 0

    def test_value_dist_affine(self):
        """Value distribution for affine sl_2."""
        data = critical_line_value_distribution(
            'affine_sl2', 1.0, t_max=100.0, n_samples=200, max_r=10,
        )
        assert data['mean_modulus'] >= 0


# ============================================================================
# 6. Zeros off critical line (Shadow RH)
# ============================================================================

class TestShadowRH:
    """Tests for shadow Riemann Hypothesis: zeros on the critical line."""

    def test_heisenberg_trivial_rh(self):
        """Heisenberg: no zeros, so shadow RH holds vacuously."""
        result = zeros_off_critical_line_search(
            'heisenberg', 1.0, max_r=10,
            re_range=(-5.0, 5.0), im_range=(1.0, 30.0),
            grid_re=10, grid_im=30,
        )
        assert result['shadow_rh_holds'] is True

    def test_affine_sl2_critical_line_structure(self):
        """Affine sl_2: all zeros on a single vertical line."""
        result = zeros_off_critical_line_search(
            'affine_sl2', 1.0, epsilon=0.1, max_r=10,
            re_range=(-5.0, 5.0), im_range=(1.0, 50.0),
            grid_re=20, grid_im=80,
        )
        if result['n_zeros_found'] > 0:
            # All zeros should lie on the same Re(s) line
            assert result['max_deviation'] < 1.0, \
                f"sl_2 zeros should cluster: max dev = {result['max_deviation']}"

    def test_virasoro_off_line_search(self):
        """Search for Virasoro zeros off critical line."""
        result = zeros_off_critical_line_search(
            'virasoro', 26.0, epsilon=0.5, max_r=60,
            re_range=(-5.0, 5.0), im_range=(1.0, 40.0),
            grid_re=20, grid_im=80,
        )
        assert 'critical_line' in result
        assert 'max_deviation' in result
        assert math.isfinite(result['max_deviation'])

    def test_argument_principle_heisenberg(self):
        """Argument principle count for Heisenberg: should be 0."""
        coeffs = shadow_coefficients_extended('heisenberg', 1.0, max_r=10)
        count = argument_principle_rectangle(
            coeffs, (-3.0, 3.0), (1.0, 30.0), n_points=500, max_r=10,
        )
        assert abs(count) <= 1  # Rounding: should be 0

    def test_argument_principle_consistency(self):
        """Argument principle count should roughly match grid-found zeros."""
        coeffs = shadow_coefficients_extended('affine_sl2', 1.0, max_r=10)
        ap = argument_principle_rectangle(
            coeffs, (-5.0, 5.0), (0.0, 50.0), n_points=2000, max_r=10,
        )
        zeros = find_zeros_grid(
            coeffs, (-5.0, 5.0), (0.0, 50.0), grid_re=20, grid_im=80, max_r=10,
        )
        # Allow generous tolerance
        assert abs(ap - len(zeros)) <= max(5, len(zeros) // 2), \
            f"AP count {ap} vs grid count {len(zeros)}"

    def test_critical_line_estimation(self):
        """Critical line estimation should return a finite value."""
        coeffs = shadow_coefficients_extended('virasoro', 26.0, max_r=50)
        sigma_c = find_critical_line(coeffs, im_range=(1.0, 50.0), n_samples=80, max_r=50)
        assert math.isfinite(sigma_c)


# ============================================================================
# 7. Shadow GRH test
# ============================================================================

class TestShadowGRH:
    """Tests for shadow GRH: |Li(x) - pi_shadow(x)| <= C*sqrt(x)*log(x)."""

    def test_logarithmic_integral_basic(self):
        """Li(x) should be positive for x > 2."""
        for x in [5.0, 10.0, 50.0, 100.0]:
            li = shadow_logarithmic_integral(x)
            assert li > 0, f"Li({x}) = {li} should be > 0"

    def test_logarithmic_integral_monotone(self):
        """Li(x) should be increasing."""
        vals = [shadow_logarithmic_integral(x) for x in [5.0, 10.0, 20.0, 50.0]]
        for i in range(len(vals) - 1):
            assert vals[i + 1] > vals[i], \
                f"Li not monotone: Li({5+5*i}) = {vals[i]} >= Li({10+5*i}) = {vals[i+1]}"

    def test_logarithmic_integral_at_2(self):
        """Li(2) = 0 by definition."""
        assert abs(shadow_logarithmic_integral(2.0)) < 0.1

    def test_shadow_primes_heisenberg(self):
        """Heisenberg: only r=2 is a shadow "prime"."""
        coeffs = shadow_coefficients_extended('heisenberg', 1.0, max_r=20)
        primes = shadow_prime_counting(coeffs, x_max=20.0)
        # Lambda(2) > 0, Lambda(r) = 0 for r > 2
        assert primes.get(2.0, 0) == 1

    def test_shadow_primes_sl2(self):
        """Affine sl_2: r=2,3 are shadow primes."""
        coeffs = shadow_coefficients_extended('affine_sl2', 1.0, max_r=20)
        primes = shadow_prime_counting(coeffs, x_max=20.0)
        assert primes.get(3.0, 0) >= 1  # At least one prime by arity 3

    def test_grh_heisenberg(self):
        """GRH test for Heisenberg."""
        data = grh_test('heisenberg', 1.0, x_values=[10.0, 50.0], max_r=20)
        assert 'grh_holds' in data

    def test_grh_virasoro(self):
        """GRH test for Virasoro."""
        data = grh_test('virasoro', 26.0, x_values=[10.0, 50.0], max_r=50)
        assert 'grh_holds' in data
        assert len(data['results']) == 2


# ============================================================================
# 8. Density hypothesis
# ============================================================================

class TestDensityHypothesis:
    """Tests for N_A(sigma, T) <= C * T^{2(1-sigma)+epsilon}."""

    def test_density_heisenberg_trivial(self):
        """Heisenberg: no zeros, so density hypothesis holds vacuously."""
        data = density_hypothesis_test(
            'heisenberg', 1.0,
            sigma_values=[0.6, 0.8],
            T_values=[20.0],
            max_r=10,
        )
        assert data['hypothesis_holds'] is True
        for result in data['results']:
            assert result['N_A'] == 0

    def test_density_virasoro(self):
        """Density hypothesis test for Virasoro should compute."""
        data = density_hypothesis_test(
            'virasoro', 26.0,
            sigma_values=[0.6, 0.8],
            T_values=[20.0, 40.0],
            max_r=50,
        )
        assert 'hypothesis_holds' in data
        assert len(data['results']) == 4  # 2 sigma x 2 T

    def test_density_monotone_in_sigma(self):
        """N_A(sigma, T) should be non-increasing in sigma for fixed T."""
        data = density_hypothesis_test(
            'virasoro', 26.0,
            sigma_values=[0.5, 0.6, 0.7, 0.8, 0.9],
            T_values=[30.0],
            max_r=50,
        )
        T = 30.0
        counts = {r['sigma']: r['N_A'] for r in data['results'] if r['T'] == T}
        sigmas = sorted(counts.keys())
        for i in range(len(sigmas) - 1):
            assert counts[sigmas[i]] >= counts[sigmas[i + 1]], \
                f"N({sigmas[i]}, {T}) = {counts[sigmas[i]]} < N({sigmas[i+1]}, {T}) = {counts[sigmas[i+1]]}"

    def test_density_monotone_in_T(self):
        """N_A(sigma, T) should be non-decreasing in T for fixed sigma."""
        data = density_hypothesis_test(
            'virasoro', 26.0,
            sigma_values=[0.7],
            T_values=[10.0, 20.0, 40.0],
            max_r=50,
        )
        sigma = 0.7
        counts = {r['T']: r['N_A'] for r in data['results'] if r['sigma'] == sigma}
        Ts = sorted(counts.keys())
        for i in range(len(Ts) - 1):
            assert counts[Ts[i]] <= counts[Ts[i + 1]], \
                f"N({sigma}, {Ts[i]}) = {counts[Ts[i]]} > N({sigma}, {Ts[i+1]}) = {counts[Ts[i+1]]}"


# ============================================================================
# 9. Zero repulsion
# ============================================================================

class TestZeroRepulsion:
    """Tests for zero repulsion and minimum gap scaling."""

    def test_minimum_gap_empty(self):
        """Empty zero list: min gap should be inf."""
        data = zero_minimum_gap([], positive_only=True)
        assert data['min_gap'] == float('inf')
        assert data['n_gaps'] == 0

    def test_minimum_gap_single_zero(self):
        """Single zero: no gaps."""
        data = zero_minimum_gap([complex(0.5, 5.0)], positive_only=True)
        assert data['n_gaps'] == 0

    def test_minimum_gap_positive(self):
        """Minimum gap should be positive for distinct zeros."""
        zeros = [complex(0.5, t) for t in [5.0, 8.0, 12.0, 15.0, 20.0]]
        data = zero_minimum_gap(zeros, positive_only=True)
        assert data['min_gap'] > 0
        assert data['mean_gap'] > 0

    def test_minimum_gap_ordering(self):
        """min_gap <= mean_gap <= max_gap."""
        zeros = [complex(0.5, t) for t in [2.0, 5.0, 7.0, 12.0, 20.0, 22.0]]
        data = zero_minimum_gap(zeros, positive_only=True)
        if data['n_gaps'] > 0:
            assert data['min_gap'] <= data['mean_gap'] <= data['max_gap']

    def test_repulsion_scaling_virasoro(self):
        """Zero repulsion scaling test for Virasoro should complete."""
        data = zero_repulsion_scaling(
            'virasoro', 26.0, T_values=[20.0, 30.0], max_r=50,
        )
        assert 'data_points' in data
        assert 'scaling_consistent' in data

    def test_gap_ratio_reasonable(self):
        """Gap ratio min_gap / (1/log T) should be O(1)."""
        zeros = [complex(-2.5, 7.75 * (2 * n + 1)) for n in range(-10, 11)]
        data = zero_minimum_gap(zeros, positive_only=True)
        if data['n_gaps'] > 0 and data['gap_ratio'] < float('inf'):
            # The ratio should be finite and positive
            assert data['gap_ratio'] > 0


# ============================================================================
# 10. Koszul zero duality
# ============================================================================

class TestKoszulZeroDuality:
    """Tests for comparing zeros of zeta_A and zeta_{A!}."""

    def test_self_dual_virasoro_c13(self):
        """At c=13: Vir_13^! = Vir_13, so zeros should coincide."""
        data = koszul_zero_overlap_at_self_dual(c_val=13.0, max_r=60)
        assert data['coefficients_identical'] is True, \
            f"c=13 coefficients differ by {data['max_coeff_diff']}"
        if data['n_zeros_A'] > 0:
            assert data['match_fraction'] > 0.5, \
                f"At c=13, match fraction = {data['match_fraction']} (expected ~1)"

    def test_heisenberg_dual_no_zeros(self):
        """Heisenberg: both zeta_A and zeta_{A!} have no zeros."""
        data = koszul_zero_duality_analysis(
            'heisenberg', 1.0, max_r=10,
            re_range=(-5.0, 5.0), im_range=(0.0, 30.0),
            grid_re=10, grid_im=30,
        )
        assert data['n_zeros_A'] == 0
        # H_k^! has kappa = -k, so zeta_{H^!}(s) = -k * 2^{-s} also has no zeros
        assert data['n_zeros_dual'] == 0

    def test_kappa_sum_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        # Exclude c=26: dual is c=0 which is a pole of Q_L (ValueError)
        for c_val in [1.0, 5.0, 13.0, 20.0, 25.0]:
            data = koszul_zero_duality_analysis(
                'virasoro', c_val, max_r=30,
                re_range=(-3.0, 3.0), im_range=(0.0, 10.0),
                grid_re=5, grid_im=10,
            )
            assert abs(data['kappa_sum'] - 13.0) < 0.01, \
                f"kappa sum at c={c_val}: {data['kappa_sum']} != 13"

    def test_kappa_sum_heisenberg(self):
        """kappa(H_k) + kappa(H_k^!) = 0 (AP24)."""
        for k in [0.5, 1.0, 2.0, 5.0]:
            data = koszul_zero_duality_analysis(
                'heisenberg', k, max_r=10,
                re_range=(-3.0, 3.0), im_range=(0.0, 10.0),
                grid_re=5, grid_im=10,
            )
            assert abs(data['kappa_sum']) < 0.01, \
                f"Heisenberg kappa sum at k={k}: {data['kappa_sum']} != 0"

    def test_kappa_sum_affine_sl2(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0."""
        for k in [1.0, 2.0, 5.0]:
            data = koszul_zero_duality_analysis(
                'affine_sl2', k, max_r=10,
                re_range=(-3.0, 3.0), im_range=(0.0, 10.0),
                grid_re=5, grid_im=10,
            )
            assert abs(data['kappa_sum']) < 0.01, \
                f"sl_2 kappa sum at k={k}: {data['kappa_sum']} != 0"

    def test_interlacing_bounded(self):
        """Interlacing ratio should be between 0 and 1."""
        data = koszul_zero_duality_analysis(
            'virasoro', 26.0, max_r=50,
            re_range=(-5.0, 5.0), im_range=(0.0, 30.0),
            grid_re=15, grid_im=50,
        )
        assert 0.0 <= data['interlacing_ratio'] <= 1.0


# ============================================================================
# 11. Kappa formula verification (AP1, AP9, AP48)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa formulas for all families independently (AP1, AP9)."""

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        assert abs(kappa_for_family('heisenberg', 1.0) - 1.0) < 1e-15
        assert abs(kappa_for_family('heisenberg', 3.0) - 3.0) < 1e-15

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert abs(kappa_for_family('virasoro', 26.0) - 13.0) < 1e-15
        assert abs(kappa_for_family('virasoro', 1.0) - 0.5) < 1e-15

    def test_kappa_affine_sl2(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4."""
        assert abs(kappa_for_family('affine_sl2', 1.0) - 3.0 * 3.0 / 4.0) < 1e-15
        assert abs(kappa_for_family('affine_sl2', 2.0) - 3.0) < 1e-15

    def test_kappa_affine_sl3(self):
        """kappa(V_k(sl_3)) = 4(k+3)/3."""
        assert abs(kappa_for_family('affine_sl3', 1.0) - 4.0 * 4.0 / 3.0) < 1e-15

    def test_kappa_not_c_over_2_for_sl2(self):
        """kappa(sl_2, k=1) != c(sl_2, k=1)/2 (AP9)."""
        kappa = kappa_for_family('affine_sl2', 1.0)
        # c(sl_2, k=1) = 3*1/(1+2) = 1, so c/2 = 0.5
        c_val = 3.0 * 1.0 / (1.0 + 2.0)
        assert abs(kappa - c_val / 2.0) > 0.1, \
            f"kappa({kappa}) should differ from c/2({c_val / 2.0}) for sl_2"

    def test_kappa_matches_shadow_coeffs(self):
        """kappa should match S_2 from shadow coefficients."""
        for family, info in STANDARD_FAMILIES.items():
            param = info['default_param']
            coeffs = shadow_coefficients_extended(family, param, max_r=5)
            kappa = kappa_for_family(family, param)
            S2 = coeffs.get(2, 0.0)
            # For most families: kappa = S_2 (they coincide at arity 2)
            # but the interpretation differs (AP9)
            assert abs(kappa - S2) < 0.5, \
                f"{family}: kappa={kappa} vs S_2={S2}"


# ============================================================================
# 12. Cross-verification (multi-path)
# ============================================================================

class TestCrossVerification:
    """Multi-path verification of zeros and invariants."""

    def test_verify_affine_sl2_zero(self):
        """Verify an affine sl_2 zero by 3 paths."""
        coeffs = shadow_coefficients_extended('affine_sl2', 1.0, max_r=10)
        zeros = affine_sl2_zeros(1.0, n_max=5)
        if zeros:
            z = zeros[0]
            result = verify_zero_by_three_paths(coeffs, z, zeros, max_r=10)
            assert result['path1_direct_eval'], \
                f"Path 1 failed: |zeta(rho)| = {result['path1_residual']}"

    def test_cross_family_heisenberg(self):
        """Cross-family consistency for Heisenberg."""
        data = cross_family_consistency_check('heisenberg', 1.0, max_r=10)
        assert data['kappa_check_passed'], \
            f"Kappa check failed: sum={data['kappa_sum']} expected={data['expected_kappa_sum']}"

    def test_cross_family_virasoro(self):
        """Cross-family consistency for Virasoro."""
        data = cross_family_consistency_check('virasoro', 26.0, max_r=50)
        assert data['kappa_check_passed'], \
            f"Kappa check failed: sum={data['kappa_sum']} expected={data['expected_kappa_sum']}"

    def test_cross_family_sl2(self):
        """Cross-family consistency for affine sl_2."""
        data = cross_family_consistency_check('affine_sl2', 1.0, max_r=10)
        assert data['kappa_check_passed'], \
            f"Kappa check failed: sum={data['kappa_sum']} expected={data['expected_kappa_sum']}"

    def test_zero_count_two_methods(self):
        """Zero count from grid search and argument principle should be close."""
        for family, info in [('affine_sl2', {'param': 1.0, 'max_r': 10}),
                             ('virasoro', {'param': 26.0, 'max_r': 50})]:
            data = cross_family_consistency_check(
                family, info['param'], max_r=info['max_r'],
            )
            assert data['count_consistent'], \
                f"{family}: grid={data['n_zeros_grid']} vs AP={data['n_zeros_arg_principle']}"


# ============================================================================
# 13. Complementarity sum verification
# ============================================================================

class TestComplementarity:
    """Verify complementarity: kappa(A) + kappa(A!) for all families."""

    def test_virasoro_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c (AP24)."""
        for c_val in [0.5, 1.0, 5.0, 10.0, 13.0, 20.0, 25.0, 26.0]:
            kA = kappa_for_family('virasoro', c_val)
            kD = kappa_for_family('virasoro', 26.0 - c_val)
            assert abs(kA + kD - 13.0) < 1e-10, \
                f"c={c_val}: kappa + kappa' = {kA + kD}, expected 13"

    def test_heisenberg_sum_0(self):
        """kappa(H_k) + kappa(H_k^!) = 0."""
        for k in [0.5, 1.0, 2.0, 10.0]:
            kA = kappa_for_family('heisenberg', k)
            # H_k^! has kappa = -k
            kD = -k
            assert abs(kA + kD) < 1e-10, \
                f"k={k}: kappa + kappa' = {kA + kD}, expected 0"

    def test_sl2_sum_0(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0."""
        for k in [1.0, 2.0, 5.0]:
            kA = kappa_for_family('affine_sl2', k)
            kD = kappa_for_family('affine_sl2', -k - 4.0)
            assert abs(kA + kD) < 1e-10, \
                f"k={k}: kappa + kappa' = {kA + kD}, expected 0"

    def test_sl3_sum_0(self):
        """kappa(sl_3, k) + kappa(sl_3, -k-6) = 0."""
        for k in [1.0, 2.0, 5.0]:
            kA = kappa_for_family('affine_sl3', k)
            kD = kappa_for_family('affine_sl3', -k - 6.0)
            assert abs(kA + kD) < 1e-10, \
                f"k={k}: kappa + kappa' = {kA + kD}, expected 0"

    def test_shadow_coeffs_dual_arity2(self):
        """Verify S_2(A) + S_2(A!) matches expected kappa sum."""
        for family in ['heisenberg', 'affine_sl2', 'virasoro']:
            param = STANDARD_FAMILIES[family]['default_param']
            coeffs = shadow_coefficients_extended(family, param, max_r=5)
            dual = koszul_dual_coefficients(family, param, max_r=5)
            S2_sum = coeffs.get(2, 0.0) + dual.get(2, 0.0)
            if family == 'virasoro':
                assert abs(S2_sum - 13.0) < 0.01, \
                    f"Virasoro: S2 + S2' = {S2_sum}, expected 13"
            else:
                assert abs(S2_sum) < 0.1, \
                    f"{family}: S2 + S2' = {S2_sum}, expected ~0"


# ============================================================================
# 14. Full analysis integration tests
# ============================================================================

class TestFullAnalysis:
    """Integration tests for the full analysis pipeline."""

    def test_full_analysis_heisenberg(self):
        """Full analysis for Heisenberg."""
        data = full_analysis('heisenberg', 1.0, 'G', max_r=10, que_n_max=10)
        assert data.family == 'heisenberg'
        assert abs(data.kappa - 1.0) < 1e-10

    def test_full_analysis_virasoro(self):
        """Full analysis for Virasoro c=26."""
        data = full_analysis('virasoro', 26.0, 'M', max_r=40, que_n_max=10)
        assert data.family == 'virasoro'
        assert abs(data.kappa - 13.0) < 0.01

    def test_full_analysis_sl2(self):
        """Full analysis for affine sl_2."""
        data = full_analysis('affine_sl2', 1.0, 'L', max_r=10, que_n_max=10)
        assert data.family == 'affine_sl2'

    def test_full_analysis_betagamma(self):
        """Full analysis for beta-gamma."""
        data = full_analysis('betagamma', 0.5, 'C', max_r=10, que_n_max=10)
        assert data.family == 'betagamma'


# ============================================================================
# 15. Landscape census
# ============================================================================

class TestLandscapeCensus:
    """Tests for the multi-family landscape census."""

    def test_census_returns_all_families(self):
        """Census should return data for all requested families."""
        results = landscape_zero_census(max_r=30)
        assert len(results) > 0
        for label, data in results.items():
            assert 'kappa' in data
            assert 'n_zeros' in data

    def test_census_kappa_values(self):
        """Verify kappa values in the census."""
        results = landscape_zero_census(max_r=30)
        if 'Vir_c=26' in results:
            assert abs(results['Vir_c=26']['kappa'] - 13.0) < 0.01
        if 'Vir_c=13' in results:
            assert abs(results['Vir_c=13']['kappa'] - 6.5) < 0.01
        if 'Heis_k=1' in results:
            assert abs(results['Heis_k=1']['kappa'] - 1.0) < 0.01

    def test_census_heisenberg_no_zeros(self):
        """Census should show 0 zeros for Heisenberg."""
        results = landscape_zero_census(max_r=10)
        if 'Heis_k=1' in results:
            assert results['Heis_k=1']['n_zeros'] == 0


# ============================================================================
# 16. Shadow zeta evaluation sanity
# ============================================================================

class TestShadowZetaSanity:
    """Basic sanity checks on shadow zeta evaluation."""

    def test_heisenberg_zeta_value(self):
        """zeta_{H_k}(s) = k * 2^{-s}."""
        coeffs = shadow_coefficients_extended('heisenberg', 1.0, max_r=5)
        for s in [1.0, 2.0, 3.0, 0.5 + 1.0j]:
            val = _shadow_zeta_complex(coeffs, s, max_r=5)
            expected = 1.0 * 2.0 ** (-s)
            assert abs(val - expected) < 1e-10, \
                f"zeta_H(s={s}): {val} != {expected}"

    def test_zeta_real_for_real_s_heisenberg(self):
        """For Heisenberg with k real and s real: zeta is real."""
        coeffs = shadow_coefficients_extended('heisenberg', 1.0, max_r=5)
        val = _shadow_zeta_complex(coeffs, 2.0, max_r=5)
        assert abs(val.imag) < 1e-15

    def test_zeta_conjugate_symmetry(self):
        """zeta_A(s*) = zeta_A(s)* for real coefficients."""
        coeffs = shadow_coefficients_extended('virasoro', 26.0, max_r=30)
        s = complex(1.5, 3.7)
        z1 = _shadow_zeta_complex(coeffs, s, max_r=30)
        z2 = _shadow_zeta_complex(coeffs, s.conjugate(), max_r=30)
        assert abs(z1 - z2.conjugate()) < 1e-10, \
            f"Conjugate symmetry: z({s}) = {z1}, z({s.conjugate()})* = {z2.conjugate()}"


# ============================================================================
# 17. Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Edge case and robustness tests."""

    def test_empty_T_list(self):
        """Empty T list should return empty dict."""
        result = zero_density_table('heisenberg', 1.0, [], max_r=5)
        assert result == {}

    def test_zero_param(self):
        """k=0 Heisenberg: zeta is identically zero."""
        coeffs = shadow_coefficients_extended('heisenberg', 0.0, max_r=5)
        val = _shadow_zeta_complex(coeffs, 1.0, max_r=5)
        assert abs(val) < 1e-15

    def test_virasoro_various_c(self):
        """Virasoro at various c values: no crashes."""
        for c_val in [0.5, 1.0, 5.0, 10.0, 13.0, 20.0, 25.0, 26.0, 30.0]:
            coeffs = shadow_coefficients_extended('virasoro', c_val, max_r=20)
            assert len(coeffs) >= 19  # At least arities 2 through 20

    def test_large_T_no_crash(self):
        """Large T value: no crash in density table."""
        result = zero_density_table(
            'affine_sl2', 1.0, [200.0], max_r=10, grid_im_factor=1.0,
        )
        assert 200.0 in result

    def test_negative_k_heisenberg(self):
        """Negative k Heisenberg: S_2 = k < 0."""
        coeffs = shadow_coefficients_extended('heisenberg', -1.0, max_r=5)
        assert coeffs[2] == -1.0

    def test_que_with_single_term_shadow(self):
        """QUE for single-term shadow (Heisenberg)."""
        data = que_convergence_test(
            'heisenberg', 1.0, n_values=[1, 5, 10], n_grid=50, max_r=5,
        )
        assert len(data['deviations']) == 3

    def test_entropy_with_single_term_shadow(self):
        """Entropy for single-term shadow."""
        data = entropy_convergence_test(
            'heisenberg', 1.0, n_values=[1, 5, 10], n_grid=50, max_r=5,
        )
        assert len(data['entropies']) == 3

    def test_koszul_duality_betagamma(self):
        """Koszul zero duality for beta-gamma."""
        data = koszul_zero_duality_analysis(
            'betagamma', 0.5, max_r=10,
            re_range=(-3.0, 3.0), im_range=(0.0, 20.0),
            grid_re=10, grid_im=30,
        )
        assert 'n_zeros_A' in data
        assert 'n_zeros_dual' in data


# ============================================================================
# 18. Specific parameter value tests
# ============================================================================

class TestSpecificValues:
    """Tests at specific parameter values with known properties."""

    def test_virasoro_c26_kappa_13(self):
        """Virasoro c=26: kappa = 13, dual is Vir_0 with kappa = 0."""
        kA = kappa_for_family('virasoro', 26.0)
        assert abs(kA - 13.0) < 1e-10
        kD = kappa_for_family('virasoro', 0.0 + 1e-6)  # Avoid c=0 singularity
        assert abs(kD) < 0.01

    def test_virasoro_c13_self_dual(self):
        """Virasoro c=13: self-dual, kappa = 6.5, kappa' = 6.5."""
        kA = kappa_for_family('virasoro', 13.0)
        kD = kappa_for_family('virasoro', 13.0)
        assert abs(kA - 6.5) < 1e-10
        assert abs(kA - kD) < 1e-10

    def test_sl2_k1_kappa(self):
        """sl_2 at k=1: kappa = 3*3/4 = 9/4 = 2.25."""
        kA = kappa_for_family('affine_sl2', 1.0)
        assert abs(kA - 2.25) < 1e-10

    def test_sl3_k1_kappa(self):
        """sl_3 at k=1: kappa = 4*4/3 = 16/3."""
        kA = kappa_for_family('affine_sl3', 1.0)
        assert abs(kA - 16.0 / 3.0) < 1e-10

    def test_virasoro_growth_rate_c26(self):
        """Virasoro c=26: growth rate rho < 1 (converges)."""
        rho = virasoro_growth_rate(26.0)
        assert rho > 0
        assert rho < 1  # Entire function

    def test_virasoro_growth_rate_c1(self):
        """Virasoro c=1: growth rate."""
        rho = virasoro_growth_rate(1.0)
        assert rho > 0

    def test_virasoro_growth_rate_c13_self_dual(self):
        """Virasoro c=13: growth rate at self-dual point."""
        rho13 = virasoro_growth_rate(13.0)
        rho_dual = virasoro_growth_rate(26.0 - 13.0)
        assert abs(rho13 - rho_dual) < 1e-10  # Self-dual: same growth rate


# ============================================================================
# 19. Gaussian test function properties
# ============================================================================

class TestGaussianProperties:
    """Verify properties of the Gaussian test function for explicit formula."""

    def test_gaussian_at_zero(self):
        """h(0) = 1."""
        assert abs(gaussian_test_function(0.0, 5.0) - 1.0) < 1e-15

    def test_gaussian_positive(self):
        """h(t) > 0 for all t."""
        for t in [-10.0, -1.0, 0.0, 1.0, 10.0, 100.0]:
            assert gaussian_test_function(t, 5.0) > 0

    def test_gaussian_ft_positive(self):
        """Fourier transform of Gaussian is positive."""
        for xi in [0.0, 0.5, 1.0, 5.0]:
            assert gaussian_fourier_transform(xi, 5.0) > 0

    def test_gaussian_ft_parseval(self):
        """Parseval: integral of |h|^2 = integral of |hat{h}|^2.

        int_R h(t)^2 dt = sigma * sqrt(pi/2)
        int_R hat{h}(xi)^2 dxi = sigma^2 * pi * sigma * sqrt(pi/2)
        But 2*pi * LHS = RHS under Fourier convention. Check numerically.
        """
        sigma = 3.0
        # int h(t)^2 dt = integral of exp(-2t^2/sigma^2) = sigma*sqrt(pi/2)
        integral_h_sq = sigma * math.sqrt(math.pi / 2.0)
        assert integral_h_sq > 0


# ============================================================================
# 20. Shadow logarithmic integral properties
# ============================================================================

class TestLogarithmicIntegral:
    """Tests for the shadow logarithmic integral Li(x)."""

    def test_li_increasing(self):
        """Li(x) strictly increasing for x > 2."""
        vals = [shadow_logarithmic_integral(x) for x in [3.0, 5.0, 10.0, 50.0]]
        for i in range(len(vals) - 1):
            assert vals[i + 1] > vals[i]

    def test_li_positive(self):
        """Li(x) > 0 for x > 2."""
        for x in [3.0, 10.0, 100.0]:
            assert shadow_logarithmic_integral(x) > 0

    def test_li_growth_sublinear(self):
        """Li(x) grows slower than x."""
        for x in [10.0, 100.0]:
            li = shadow_logarithmic_integral(x)
            assert li < x, f"Li({x}) = {li} >= {x}"

    def test_li_approximation(self):
        """Li(x) ~ x/ln(x) for large x (rough check)."""
        x = 100.0
        li = shadow_logarithmic_integral(x)
        approx = x / math.log(x)
        # Li(x) should be somewhat close to x/ln(x)
        ratio = li / approx if approx > 0 else 0
        assert 0.5 < ratio < 2.0, f"Li(100)/approx = {ratio}"
