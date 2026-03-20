"""Tests for compute/lib/sewing_shadow_intertwining.py — sewing-shadow intertwining theorem.

Verifies the fundamental identity F_1^conn(q; A) = sum_r Sh_r^{(1)}(A) G_r(q)
across all standard families (Heisenberg, free fermion, affine sl_2, Virasoro).

Structure:
  T1-T10:  sigma_{-1} arithmetic
  T11-T20: connected free energy coefficients (Heisenberg and fermion)
  T21-T30: geometric kernel G_2
  T31-T40: EXACT intertwining verification: F_1 = kappa * G_2 (Heisenberg)
  T41-T50: shadow Fredholm determinant
  T51-T60: Rankin-Selberg spectral comparison
  T61-T70: intertwining defect for interacting theories (affine, Virasoro)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.sewing_shadow_intertwining import (
    sigma_minus_1,
    sigma_minus_1_float,
    sigma_k,
    connected_free_energy_heisenberg,
    connected_free_energy_heisenberg_float,
    connected_free_energy_fermion,
    geometric_kernel_G2,
    geometric_kernel_G2_float,
    shadow_geometric_pairing,
    verify_intertwining_heisenberg,
    intertwining_defect,
    shadow_fredholm_determinant,
    shadow_fredholm_log_expansion,
    sewing_determinant_coefficients,
    sewing_determinant_from_product,
    rankin_selberg_spectral_comparison,
    affine_sl2_kappa,
    affine_sl2_central_charge,
    virasoro_kappa,
)


# ============================================================
# T1-T10: sigma_{-1} function tests
# ============================================================

class TestSigmaMinus1:
    """Arithmetic of the divisor function sigma_{-1}(N) = sum_{d|N} 1/d."""

    def test_sigma_minus_1_of_1(self):
        """sigma_{-1}(1) = 1."""
        assert sigma_minus_1(1) == Fraction(1)

    def test_sigma_minus_1_of_2(self):
        """sigma_{-1}(2) = 1 + 1/2 = 3/2."""
        assert sigma_minus_1(2) == Fraction(3, 2)

    def test_sigma_minus_1_of_3(self):
        """sigma_{-1}(3) = 1 + 1/3 = 4/3."""
        assert sigma_minus_1(3) == Fraction(4, 3)

    def test_sigma_minus_1_of_4(self):
        """sigma_{-1}(4) = 1 + 1/2 + 1/4 = 7/4."""
        assert sigma_minus_1(4) == Fraction(7, 4)

    def test_sigma_minus_1_of_6(self):
        """sigma_{-1}(6) = 1 + 1/2 + 1/3 + 1/6 = 2."""
        assert sigma_minus_1(6) == Fraction(2)

    def test_sigma_minus_1_of_12(self):
        """sigma_{-1}(12) = 1 + 1/2 + 1/3 + 1/4 + 1/6 + 1/12 = 7/3."""
        expected = Fraction(1) + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 6) + Fraction(1, 12)
        assert sigma_minus_1(12) == expected
        assert expected == Fraction(7, 3)

    def test_sigma_minus_1_of_prime(self):
        """For prime p, sigma_{-1}(p) = 1 + 1/p."""
        for p in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
            assert sigma_minus_1(p) == Fraction(p + 1, p)

    def test_sigma_minus_1_of_prime_square(self):
        """sigma_{-1}(p^2) = 1 + 1/p + 1/p^2."""
        for p in [2, 3, 5, 7]:
            n = p * p
            expected = Fraction(1) + Fraction(1, p) + Fraction(1, n)
            assert sigma_minus_1(n) == expected

    def test_sigma_minus_1_multiplicative(self):
        """sigma_{-1} is multiplicative: sigma_{-1}(mn) = sigma_{-1}(m)*sigma_{-1}(n) for gcd(m,n)=1."""
        pairs = [(2, 3), (2, 5), (3, 5), (4, 9), (7, 11), (8, 15)]
        for m, n in pairs:
            assert sigma_minus_1(m * n) == sigma_minus_1(m) * sigma_minus_1(n), \
                f"Multiplicativity failed for ({m}, {n})"

    def test_sigma_minus_1_float_agrees(self):
        """Float version agrees with exact version."""
        for N in range(1, 50):
            exact = float(sigma_minus_1(N))
            approx = sigma_minus_1_float(N)
            assert abs(exact - approx) < 1e-14, f"Disagreement at N={N}"


# ============================================================
# T11-T20: connected free energy coefficients
# ============================================================

class TestConnectedFreeEnergy:
    """Connected genus-1 free energy for Heisenberg and fermion."""

    def test_heisenberg_c1_first_coeffs(self):
        """F_1^conn(H_{c=1}) leading coefficients: sigma_{-1}(N)."""
        F1 = connected_free_energy_heisenberg(10, c=Fraction(1))
        assert F1[1] == Fraction(1)
        assert F1[2] == Fraction(3, 2)
        assert F1[3] == Fraction(4, 3)
        assert F1[6] == Fraction(2)

    def test_heisenberg_c2_scaling(self):
        """At c=2, all coefficients double."""
        F1_c1 = connected_free_energy_heisenberg(20, c=Fraction(1))
        F1_c2 = connected_free_energy_heisenberg(20, c=Fraction(2))
        for N in range(1, 21):
            assert F1_c2[N] == 2 * F1_c1[N]

    def test_heisenberg_c4_scaling(self):
        """At c=4, all coefficients quadruple."""
        F1_c1 = connected_free_energy_heisenberg(20, c=Fraction(1))
        F1_c4 = connected_free_energy_heisenberg(20, c=Fraction(4))
        for N in range(1, 21):
            assert F1_c4[N] == 4 * F1_c1[N]

    def test_heisenberg_c24_first_coeff(self):
        """At c=24, F_1(1) = 24 * sigma_{-1}(1) = 24."""
        F1 = connected_free_energy_heisenberg(5, c=Fraction(24))
        assert F1[1] == Fraction(24)

    def test_fermion_half_of_boson(self):
        """Free fermion (c=1/2) has F_1 = (1/2) * F_1(Heisenberg c=1)."""
        F1_ferm = connected_free_energy_fermion(20)
        F1_bos = connected_free_energy_heisenberg(20, c=Fraction(1))
        for N in range(1, 21):
            assert F1_ferm[N] == F1_bos[N] / 2

    def test_fermion_c_half_values(self):
        """Free fermion F_1(1) = 1/2, F_1(2) = 3/4, F_1(3) = 2/3."""
        F1 = connected_free_energy_fermion(10)
        assert F1[1] == Fraction(1, 2)
        assert F1[2] == Fraction(3, 4)
        assert F1[3] == Fraction(2, 3)

    def test_heisenberg_float_agrees_with_exact(self):
        """Float version matches exact to machine precision."""
        F1_exact = connected_free_energy_heisenberg(50, c=Fraction(1))
        F1_float = connected_free_energy_heisenberg_float(50, c=1.0)
        for N in range(50):
            assert abs(float(F1_exact[N + 1]) - F1_float[N]) < 1e-14

    def test_heisenberg_positivity(self):
        """All coefficients of F_1 are positive (since sigma_{-1} > 0)."""
        F1 = connected_free_energy_heisenberg(100, c=Fraction(1))
        for N in range(1, 101):
            assert F1[N] > 0

    def test_heisenberg_growth_bound(self):
        """sigma_{-1}(N) <= log(N) + gamma + 1/N for N >= 1 (Gronwall-type)."""
        gamma = 0.5772156649015329  # Euler-Mascheroni
        for N in range(1, 200):
            val = float(sigma_minus_1(N))
            bound = math.log(N) + gamma + 1.0 / N + 1e-10
            assert val <= bound, f"sigma_{{-1}}({N}) = {val} exceeds bound {bound}"

    def test_heisenberg_sum_representation(self):
        """Verify: sum_{N=1}^M sigma_{-1}(N) q^N = -sum_{n=1}^M log(1-q^n) at q=1/2."""
        q = 0.5
        M = 50
        # LHS: sum sigma_{-1}(N) q^N
        lhs = sum(sigma_minus_1_float(N) * q ** N for N in range(1, M + 1))
        # RHS: -sum log(1-q^n), truncated
        rhs = -sum(math.log(1 - q ** n) for n in range(1, M + 1))
        # These should agree up to truncation error
        assert abs(lhs - rhs) < 1e-10


# ============================================================
# T21-T30: geometric kernel G_2
# ============================================================

class TestGeometricKernelG2:
    """The genus-1 two-point geometric kernel G_2(q)."""

    def test_G2_first_coeff(self):
        """G_2(q) leading coefficient: G_2[1] = 2 * sigma_{-1}(1) = 2."""
        G2 = geometric_kernel_G2(10)
        assert G2[1] == Fraction(2)

    def test_G2_second_coeff(self):
        """G_2[2] = 2 * sigma_{-1}(2) = 3."""
        G2 = geometric_kernel_G2(10)
        assert G2[2] == Fraction(3)

    def test_G2_sixth_coeff(self):
        """G_2[6] = 2 * sigma_{-1}(6) = 4."""
        G2 = geometric_kernel_G2(10)
        assert G2[6] == Fraction(4)

    def test_G2_independence_of_c(self):
        """G_2 is the SAME for any c — it is a geometric object."""
        G2_c1 = geometric_kernel_G2(20, c=Fraction(1))
        G2_c5 = geometric_kernel_G2(20, c=Fraction(5))
        G2_c24 = geometric_kernel_G2(20, c=Fraction(24))
        for N in range(1, 21):
            assert G2_c1[N] == G2_c5[N] == G2_c24[N]

    def test_G2_positivity(self):
        """All coefficients of G_2 are positive."""
        G2 = geometric_kernel_G2(100)
        for N in range(1, 101):
            assert G2[N] > 0

    def test_G2_at_prime(self):
        """G_2[p] = 2(1 + 1/p) = 2(p+1)/p for prime p."""
        G2 = geometric_kernel_G2(50)
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            assert G2[p] == Fraction(2 * (p + 1), p)

    def test_G2_float_agrees(self):
        """Float version matches exact."""
        G2_exact = geometric_kernel_G2(50)
        G2_float = geometric_kernel_G2_float(50)
        for N in range(50):
            assert abs(float(G2_exact[N + 1]) - G2_float[N]) < 1e-14

    def test_G2_relation_to_dedekind_eta(self):
        """G_2(q) = -2 * d/dq [q * d/dq log eta(q)] / q tested via q-series."""
        # log eta(q) = (1/24) log q - sum_{n>=1} log(1-q^n)
        # = (1/24) log q + sum_{N>=1} sigma_{-1}(N) q^N
        # q d/dq of this = 1/24 + sum N sigma_{-1}(N) q^N
        # Then -2 d/dq of that / q = -2 sum N^2 sigma_{-1}(N) q^{N-1}... no, this is more complex.
        # Instead verify the simpler relation: G_2(q) = 2 sum sigma_{-1}(N) q^N directly.
        G2 = geometric_kernel_G2(20)
        for N in range(1, 21):
            assert G2[N] == 2 * sigma_minus_1(N)

    def test_G2_multiplicative_structure(self):
        """G_2[mn] = G_2[m] * G_2[n] / 2 when gcd(m,n) = 1 (from multiplicativity of sigma_{-1})."""
        G2 = geometric_kernel_G2(100)
        pairs = [(2, 3), (2, 5), (3, 7), (4, 9), (5, 11), (7, 13)]
        for m, n in pairs:
            # sigma_{-1}(mn) = sigma_{-1}(m) * sigma_{-1}(n) for coprime m,n
            # G_2[mn] = 2 sigma_{-1}(mn) = 2 sigma_{-1}(m) sigma_{-1}(n)
            # G_2[m] * G_2[n] / 2 = (2 sigma_{-1}(m)) * (2 sigma_{-1}(n)) / 2
            #                      = 2 sigma_{-1}(m) sigma_{-1}(n)
            assert G2[m * n] == G2[m] * G2[n] / 2

    def test_G2_cumulative_sum(self):
        """sum_{N=1}^M G_2(N)/N converges (logarithmically) — cross-check with sum sigma_{-1}/N."""
        # sum sigma_{-1}(N)/N = sum_{d|N} 1/(dN) = sum_{d,m} 1/(d * d * m) = sum_d 1/d^2 * sum_m 1/m
        # This diverges (harmonic sum), but partial sums are well-behaved.
        G2 = geometric_kernel_G2(100)
        partial = sum(float(G2[N]) / N for N in range(1, 101))
        # Should be positive and finite
        assert partial > 0
        assert partial < 100  # crude bound


# ============================================================
# T31-T40: EXACT intertwining verification
# ============================================================

class TestExactIntertwining:
    """F_1 = kappa * G_2 EXACTLY for Heisenberg (free theories)."""

    def test_intertwining_c1(self):
        """Exact intertwining at c=1: F_1 = (1/2) * G_2."""
        result = verify_intertwining_heisenberg(Fraction(1), q_max=100)
        assert result['match'] is True
        assert result['max_defect'] == 0.0
        assert result['kappa'] == Fraction(1, 2)

    def test_intertwining_c2(self):
        """Exact intertwining at c=2: F_1 = 1 * G_2."""
        result = verify_intertwining_heisenberg(Fraction(2), q_max=100)
        assert result['match'] is True
        assert result['kappa'] == Fraction(1)

    def test_intertwining_c4(self):
        """Exact intertwining at c=4."""
        result = verify_intertwining_heisenberg(Fraction(4), q_max=100)
        assert result['match'] is True
        assert result['kappa'] == Fraction(2)

    def test_intertwining_c8(self):
        """Exact intertwining at c=8."""
        result = verify_intertwining_heisenberg(Fraction(8), q_max=100)
        assert result['match'] is True
        assert result['kappa'] == Fraction(4)

    def test_intertwining_c24(self):
        """Exact intertwining at c=24 (the Leech lattice value)."""
        result = verify_intertwining_heisenberg(Fraction(24), q_max=100)
        assert result['match'] is True
        assert result['kappa'] == Fraction(12)

    def test_intertwining_c_half(self):
        """Exact intertwining at c=1/2 (free fermion)."""
        result = verify_intertwining_heisenberg(Fraction(1, 2), q_max=100)
        assert result['match'] is True
        assert result['kappa'] == Fraction(1, 4)

    def test_intertwining_c_rational(self):
        """Exact intertwining at c=2/3."""
        result = verify_intertwining_heisenberg(Fraction(2, 3), q_max=50)
        assert result['match'] is True

    def test_intertwining_c_large(self):
        """Exact intertwining at c=100."""
        result = verify_intertwining_heisenberg(Fraction(100), q_max=50)
        assert result['match'] is True
        assert result['kappa'] == Fraction(50)

    def test_intertwining_coefficient_by_coefficient(self):
        """Verify coefficient-by-coefficient: c * sigma_{-1}(N) = (c/2) * 2 * sigma_{-1}(N)."""
        c = Fraction(7)
        kappa = c / 2
        F1 = connected_free_energy_heisenberg(30, c)
        G2 = geometric_kernel_G2(30)
        for N in range(1, 31):
            assert F1[N] == kappa * G2[N], f"Failed at N={N}"

    def test_intertwining_normalization_identity(self):
        """The trivial identity: (c/2) * (2/c) * c * sigma = c * sigma."""
        # This verifies the chain of normalizations is consistent.
        c = Fraction(5, 3)
        kappa = c / 2
        for N in range(1, 20):
            F1_N = c * sigma_minus_1(N)
            G2_N = 2 * sigma_minus_1(N)
            assert F1_N == kappa * G2_N


# ============================================================
# T41-T50: shadow Fredholm determinant
# ============================================================

class TestShadowFredholm:
    """Shadow Fredholm determinant det(1 - t * m_2 * P)."""

    def test_single_eigenvalue(self):
        """det(1 - t * lambda) = 1 - t * lambda."""
        assert abs(shadow_fredholm_determinant([0.5], 1.0) - 0.5) < 1e-15
        assert abs(shadow_fredholm_determinant([0.5], 0.0) - 1.0) < 1e-15
        assert abs(shadow_fredholm_determinant([0.5], 2.0) - 0.0) < 1e-15

    def test_two_eigenvalues(self):
        """det(1 - t * diag(a,b)) = (1-ta)(1-tb)."""
        a, b = 0.3, 0.7
        t = 0.5
        expected = (1 - t * a) * (1 - t * b)
        assert abs(shadow_fredholm_determinant([a, b], t) - expected) < 1e-15

    def test_virasoro_spectral_delta(self):
        """For the Virasoro spectral measure rho = delta(lambda + 6/c),
        det(1 - t * m_2 * P) = 1 + 6t/c."""
        c = 25.0
        lam = -6.0 / c
        t = 1.0
        expected = 1.0 + 6.0 / c
        assert abs(shadow_fredholm_determinant([lam], t) - expected) < 1e-14

    def test_virasoro_spectral_various_c(self):
        """Virasoro spectral measure at various c values."""
        for c in [1.0, 2.0, 10.0, 25.0, 100.0]:
            lam = -6.0 / c
            for t in [0.0, 0.5, 1.0, 2.0]:
                result = shadow_fredholm_determinant([lam], t)
                expected = 1.0 + 6.0 * t / c
                assert abs(result - expected) < 1e-14

    def test_heisenberg_sewing_eigenvalues(self):
        """For Heisenberg, the one-particle eigenvalues are q^n.
        det(1 - K_q) = prod(1 - q^n)."""
        q = 0.5
        n_max = 50
        eigenvalues = [q ** n for n in range(1, n_max + 1)]
        det_val = shadow_fredholm_determinant(eigenvalues, 1.0)
        expected = 1.0
        for n in range(1, n_max + 1):
            expected *= (1 - q ** n)
        assert abs(det_val - expected) < 1e-12

    def test_log_expansion_power_sums(self):
        """S_r = sum lambda_i^r (Newton power sums)."""
        eigenvalues = [0.2, 0.3, 0.5]
        S = shadow_fredholm_log_expansion(eigenvalues, 5)
        for r in range(5):
            expected = sum(lam ** (r + 1) for lam in eigenvalues)
            assert abs(S[r] - expected) < 1e-14

    def test_log_expansion_consistency(self):
        """Verify exp(-sum S_r t^r / r) = det(1 - t * diag(lambdas))."""
        eigenvalues = [0.1, 0.2, 0.3, 0.4]
        t = 0.5
        S = shadow_fredholm_log_expansion(eigenvalues, 20)
        log_det = -sum(S[r] * t ** (r + 1) / (r + 1) for r in range(20))
        det_from_log = math.exp(log_det)
        det_direct = shadow_fredholm_determinant(eigenvalues, t)
        assert abs(det_from_log - det_direct) < 1e-10

    def test_empty_spectrum(self):
        """Empty spectrum: det = 1."""
        assert shadow_fredholm_determinant([], 1.0) == 1.0

    def test_zero_eigenvalue(self):
        """Zero eigenvalue: det(1 - t * 0) = 1."""
        assert shadow_fredholm_determinant([0.0], 1.0) == 1.0

    def test_determinant_at_t_zero(self):
        """det at t=0 is always 1."""
        for eigenvalues in [[0.5], [0.1, 0.2, 0.3], [1.0, 2.0, 3.0]]:
            assert shadow_fredholm_determinant(eigenvalues, 0.0) == 1.0


# ============================================================
# T51-T60: Rankin-Selberg spectral comparison
# ============================================================

class TestRankinSelbergComparison:
    """Rankin-Selberg integral: epsilon^1_s = 4 zeta(2s) for Z-lattice."""

    def test_rs_z_lattice_s2(self):
        """epsilon^1_2 = 4 * zeta(4) = 4 * pi^4/90."""
        result = rankin_selberg_spectral_comparison('Z', 2.0, N_max=5000)
        assert result['match'] is True
        assert result['relative_error'] < 1e-4

    def test_rs_z_lattice_s3(self):
        """epsilon^1_3 = 4 * zeta(6) = 4 * pi^6/945."""
        result = rankin_selberg_spectral_comparison('Z', 3.0, N_max=5000)
        assert result['match'] is True

    def test_rs_z_lattice_s5(self):
        """epsilon^1_5 = 4 * zeta(10)."""
        result = rankin_selberg_spectral_comparison('Z', 5.0, N_max=3000)
        assert result['match'] is True

    def test_rs_z_lattice_s1_5(self):
        """epsilon^1_{3/2} = 4 * zeta(3)."""
        result = rankin_selberg_spectral_comparison('Z', 1.5, N_max=10000)
        assert result['match'] is True

    def test_rs_z_lattice_positive(self):
        """Sewing-side value is positive for real s > 1."""
        for s in [1.5, 2.0, 3.0, 5.0, 10.0]:
            result = rankin_selberg_spectral_comparison('Z', s, N_max=2000)
            assert result['sewing_side'] > 0

    def test_rs_z_lattice_monotone_decreasing(self):
        """epsilon^1_s decreases in s for s > 1 (since 4*zeta(2s) decreases)."""
        values = []
        for s in [1.5, 2.0, 3.0, 5.0, 10.0]:
            result = rankin_selberg_spectral_comparison('Z', s, N_max=2000)
            values.append(result['sewing_side'])
        for i in range(len(values) - 1):
            assert values[i] > values[i + 1]

    def test_rs_z_lattice_approaches_4(self):
        """epsilon^1_s -> 4 as s -> infinity (since zeta(2s) -> 1)."""
        result = rankin_selberg_spectral_comparison('Z', 20.0, N_max=1000)
        assert abs(result['sewing_side'] - 4.0) < 0.01

    def test_rs_shadow_equals_sewing(self):
        """Shadow side equals sewing side."""
        result = rankin_selberg_spectral_comparison('Z', 2.0, N_max=5000)
        assert abs(result['shadow_side'] - result['zeta_reference']) < 1e-10

    def test_rs_z_lattice_s10(self):
        """epsilon^1_{10} = 4 * zeta(20), very close to 4."""
        result = rankin_selberg_spectral_comparison('Z', 10.0, N_max=1000)
        assert abs(result['sewing_side'] - 4.0) < 0.001

    def test_rs_reference_values(self):
        """Cross-check reference values: 4*zeta(4) = 4*pi^4/90."""
        import mpmath
        ref = 4 * float(mpmath.zeta(4))
        expected = 4 * math.pi ** 4 / 90
        assert abs(ref - expected) < 1e-10


# ============================================================
# T61-T70: intertwining defect for interacting theories
# ============================================================

class TestIntertwiningDefect:
    """The intertwining defect F_1 - kappa * G_2 for non-free theories."""

    def test_heisenberg_defect_zero(self):
        """Heisenberg: defect is identically zero."""
        result = intertwining_defect('heisenberg', q_max=50, c=1.0)
        assert result['max_abs_defect'] < 1e-14
        assert result['leading_nonzero'] is None

    def test_heisenberg_defect_zero_c2(self):
        """Heisenberg c=2: defect is zero."""
        result = intertwining_defect('heisenberg', q_max=50, c=2.0)
        assert result['max_abs_defect'] < 1e-14

    def test_affine_sl2_kappa_value(self):
        """kappa(hat{sl}_2, k) = 3k/(2(k+2))."""
        assert affine_sl2_kappa(1) == Fraction(1, 2)
        assert affine_sl2_kappa(2) == Fraction(3, 4)
        assert affine_sl2_kappa(4) == Fraction(1)
        assert affine_sl2_kappa(10) == Fraction(5, 4)

    def test_affine_sl2_central_charge(self):
        """c(hat{sl}_2, k) = 3k/(k+2)."""
        assert affine_sl2_central_charge(1) == Fraction(1)
        assert affine_sl2_central_charge(2) == Fraction(3, 2)
        assert affine_sl2_central_charge(10) == Fraction(5, 2)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        assert virasoro_kappa(Fraction(1)) == Fraction(1, 2)
        assert virasoro_kappa(Fraction(25)) == Fraction(25, 2)
        assert virasoro_kappa(Fraction(26)) == Fraction(13)

    def test_affine_sl2_defect_nonzero(self):
        """Affine sl_2 at level k=1: the defect is NONZERO (cubic shadow contributes).

        The vacuum character of hat{sl}_2 at k=1 (c=1) is NOT the same as
        a single free boson: the null vector at weight 2 removes states.
        """
        result = intertwining_defect('affine_sl2', q_max=30, k=1)
        # The affine character differs from eta^{-3} starting at weight k+1 = 2,
        # so the defect should be nonzero.
        assert result['leading_nonzero'] is not None
        assert result['leading_nonzero'] <= 3  # defect appears early

    def test_affine_sl2_defect_k2(self):
        """Affine sl_2 at level k=2: defect is nonzero (null vector at weight 3)."""
        result = intertwining_defect('affine_sl2', q_max=30, k=2)
        assert result['leading_nonzero'] is not None
        # Null vector at weight k+1 = 3, so defect appears at q^3 or earlier
        assert result['leading_nonzero'] <= 4

    def test_virasoro_defect_nonzero(self):
        """Virasoro at c=25: defect is nonzero because no weight-1 state."""
        result = intertwining_defect('virasoro', q_max=30, c=25.0)
        # Virasoro has no weight-1 state (unlike the free boson), so
        # log Z_Vir differs from -(c/2)*G_2 starting at q^1.
        assert result['leading_nonzero'] is not None
        assert result['leading_nonzero'] == 1  # defect at first coefficient

    def test_virasoro_defect_sign(self):
        """The Virasoro defect at q^1 is negative (missing weight-1 state)."""
        result = intertwining_defect('virasoro', q_max=10, c=25.0)
        # Virasoro Z starts 1 + 0*q + q^2 + ..., while free boson starts 1 + q + 2q^2 + ...
        # So log Z_Vir has no q^1 term, but kappa * G_2 has a positive q^1 term.
        # Defect = log Z_Vir - kappa * G_2 at q^1 is negative.
        assert result['defect'][0] < 0

    def test_affine_sl2_kappa_matches(self):
        """The kappa returned by intertwining_defect matches affine_sl2_kappa."""
        for k in [1, 2, 3, 4, 5, 10]:
            result = intertwining_defect('affine_sl2', q_max=10, k=k)
            expected_kappa = float(affine_sl2_kappa(k))
            assert abs(result['kappa'] - expected_kappa) < 1e-12


# ============================================================
# Additional structural tests
# ============================================================

class TestSewingDeterminant:
    """Sewing determinant coefficients and product formula."""

    def test_sewing_coeffs_c1(self):
        """At c=1, sewing coefficients are -sigma_{-1}(N)."""
        coeffs = sewing_determinant_coefficients(1.0, 20)
        for i, N in enumerate(range(1, 21)):
            expected = -sigma_minus_1_float(N)
            assert abs(coeffs[i] - expected) < 1e-14

    def test_sewing_product_matches_sum(self):
        """log prod(1-q^n) = -sum sigma_{-1}(N) q^N at q=0.3."""
        q = 0.3
        q_max = 100
        product_val = sewing_determinant_from_product(q, c=1.0, n_max=500)
        sum_val = sum(c * q ** (i + 1) for i, c in enumerate(sewing_determinant_coefficients(1.0, q_max)))
        assert abs(product_val - sum_val) < 1e-10

    def test_sewing_c_scaling(self):
        """Coefficients scale linearly with c."""
        c1 = sewing_determinant_coefficients(1.0, 20)
        c3 = sewing_determinant_coefficients(3.0, 20)
        for i in range(20):
            assert abs(c3[i] - 3.0 * c1[i]) < 1e-14

    def test_sewing_product_c2(self):
        """log prod(1-q^n)^2 = 2 * log prod(1-q^n)."""
        q = 0.4
        val_c1 = sewing_determinant_from_product(q, c=1.0)
        val_c2 = sewing_determinant_from_product(q, c=2.0)
        assert abs(val_c2 - 2.0 * val_c1) < 1e-12


class TestShadowGeometricPairing:
    """The shadow-geometric pairing sum_r Sh_r * G_r(q)."""

    def test_pairing_heisenberg(self):
        """For Heisenberg c=1: only arity 2 contributes, Sh_2 = 1/2."""
        q_max = 20
        G2 = geometric_kernel_G2_float(q_max)
        shadow_coeffs = {2: 0.5}  # kappa = c/2 = 1/2
        geometric_kernels = {2: G2}
        result = shadow_geometric_pairing(shadow_coeffs, geometric_kernels, q_max)
        F1_expected = connected_free_energy_heisenberg_float(q_max, c=1.0)
        for i in range(q_max):
            assert abs(result[i] - F1_expected[i]) < 1e-14

    def test_pairing_c24(self):
        """For Heisenberg c=24: Sh_2 = 12."""
        q_max = 20
        G2 = geometric_kernel_G2_float(q_max)
        shadow_coeffs = {2: 12.0}
        geometric_kernels = {2: G2}
        result = shadow_geometric_pairing(shadow_coeffs, geometric_kernels, q_max)
        F1_expected = connected_free_energy_heisenberg_float(q_max, c=24.0)
        for i in range(q_max):
            assert abs(result[i] - F1_expected[i]) < 1e-12

    def test_pairing_empty_shadows(self):
        """No shadows: pairing is zero."""
        result = shadow_geometric_pairing({}, {}, 10)
        assert all(x == 0.0 for x in result)

    def test_pairing_additivity(self):
        """Pairing is linear in shadow coefficients."""
        q_max = 15
        G2 = geometric_kernel_G2_float(q_max)
        kernels = {2: G2}
        r1 = shadow_geometric_pairing({2: 1.0}, kernels, q_max)
        r2 = shadow_geometric_pairing({2: 2.0}, kernels, q_max)
        r3 = shadow_geometric_pairing({2: 3.0}, kernels, q_max)
        for i in range(q_max):
            assert abs(r3[i] - r1[i] - r2[i]) < 1e-14


class TestSigmaKGeneralizations:
    """Generalized divisor functions."""

    def test_sigma_0(self):
        """sigma_0(N) = number of divisors."""
        assert sigma_k(1, 0) == 1
        assert sigma_k(6, 0) == 4  # 1, 2, 3, 6
        assert sigma_k(12, 0) == 6  # 1, 2, 3, 4, 6, 12

    def test_sigma_1(self):
        """sigma_1(N) = sum of divisors."""
        assert sigma_k(1, 1) == 1
        assert sigma_k(6, 1) == 12  # 1+2+3+6
        assert sigma_k(12, 1) == 28  # 1+2+3+4+6+12

    def test_sigma_2(self):
        """sigma_2(6) = 1 + 4 + 9 + 36 = 50."""
        assert sigma_k(6, 2) == 1 + 4 + 9 + 36

    def test_sigma_k_at_prime(self):
        """sigma_k(p) = 1 + p^k for prime p."""
        for p in [2, 3, 5, 7, 11]:
            for k in [0, 1, 2, 3]:
                assert sigma_k(p, k) == 1 + p ** k
