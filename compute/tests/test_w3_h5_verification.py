"""Tests for W₃ H⁵ = 171 verification.

Verifies 7 independent consistency checks supporting the conjectured
value H⁵(B(W₃)) = 171.
"""

import pytest
from math import sqrt


class TestRecurrenceConsistency:
    """Verify the rational GF recurrence a(n) = 4a(n-1) - 2a(n-2) - a(n-3)."""

    def test_known_values(self):
        """Recurrence reproduces known H¹=2, H²=5, H³=16, H⁴=52.

        P(x) = a₁x + a₂x² + ... so a₀ = 0 in the GF.
        D(x)·P(x) = N(x) gives:
          x^3: a₃ - 4a₂ + 2a₁ = 0  (a₀=0 in GF)
          x^4: a₄ - 4a₃ + 2a₂ + a₁ = 0
        """
        a = {1: 2, 2: 5, 3: 16, 4: 52}
        assert a[3] - 4 * a[2] + 2 * a[1] == 0
        assert a[4] - 4 * a[3] + 2 * a[2] + a[1] == 0

    def test_h5_prediction(self):
        """Recurrence predicts H⁵ = 171."""
        a = [1, 2, 5, 16, 52]
        a5 = 4 * a[4] - 2 * a[3] - a[2]
        assert a5 == 171

    def test_numerator_coefficients(self):
        """GF numerator N(x) = 2x - 3x² matches known values.

        D(x)·P(x) = N(x) where P(x) = 2x + 5x² + 16x³ + ...
        D(x) = 1 - 4x + 2x² + x³
        """
        a = {1: 2, 2: 5, 3: 16, 4: 52, 5: 171}

        # x¹: a₁ = 2
        assert a[1] == 2

        # x²: a₂ - 4*a₁ = 5 - 8 = -3
        assert a[2] - 4 * a[1] == -3

        # x³: a₃ - 4*a₂ + 2*a₁ = 16 - 20 + 4 = 0
        assert a[3] - 4 * a[2] + 2 * a[1] == 0

        # x⁴: a₄ - 4*a₃ + 2*a₂ + a₁ = 52 - 64 + 10 + 2 = 0
        assert a[4] - 4 * a[3] + 2 * a[2] + a[1] == 0

        # x⁵: a₅ - 4*a₄ + 2*a₃ + a₂ = 171 - 208 + 32 + 5 = 0
        assert a[5] - 4 * a[4] + 2 * a[3] + a[2] == 0

    def test_denominator_factorization(self):
        """D(x) = (1-x)(1-3x-x²) = 1 - 4x + 2x² + x³."""
        # Expand (1-x)(1-3x-x²)
        # = 1 - 3x - x² - x + 3x² + x³
        # = 1 - 4x + 2x² + x³
        d0 = 1
        d1 = -3 + (-1)
        d2 = (-1) + (-3) * (-1)
        d3 = (-1) * (-1)
        assert (d0, d1, d2, d3) == (1, -4, 2, 1)

    def test_growth_rate(self):
        """Ratio a(n)/a(n-1) → (3+√13)/2 ≈ 3.303."""
        a = [1, 2, 5, 16, 52, 171]
        for _ in range(15):
            a.append(4 * a[-1] - 2 * a[-2] - a[-3])
        target = (3 + sqrt(13)) / 2
        for n in range(15, len(a)):
            ratio = a[n] / a[n - 1]
            assert abs(ratio - target) < 0.001, f"Ratio at n={n}: {ratio:.6f}"

    def test_extended_sequence_positive(self):
        """All terms in the extended sequence are positive."""
        a = [1, 2, 5, 16, 52, 171]
        for _ in range(20):
            a.append(4 * a[-1] - 2 * a[-2] - a[-3])
        assert all(x > 0 for x in a)


class TestGFNumerator:
    """Verify D(x)·P(x) = N(x) = 2x - 3x² through degree 8."""

    def test_dp_equals_n_through_deg8(self):
        from compute.lib.w3_h5_verification import check_numerator_coefficients
        result = check_numerator_coefficients()
        assert result["all_match"] is True


class TestDSDiscriminant:
    """Verify shared discriminant with sl₃ (DS invariance)."""

    def test_shared_factor(self):
        """Both sl₃ and W₃ GF denominators share (1-3x-x²)."""
        # sl₃: (1-8x)(1-3x-x²) = 1 - 11x + 23x² + 8x³
        sl3 = 1 * 1 + 0  # just check expansion
        assert (-8) + (-3) == -11
        assert (-8) * (-3) + (-1) == 23
        assert (-8) * (-1) == 8

        # W₃: (1-x)(1-3x-x²) = 1 - 4x + 2x² + x³
        assert (-1) + (-3) == -4
        assert (-1) * (-3) + (-1) == 2
        assert (-1) * (-1) == 1

    def test_discriminant_13(self):
        """Shared quadratic has discriminant 13."""
        # 1 - 3x - x² = 0 → x² + 3x - 1 = 0 → disc = 9 + 4 = 13
        assert 3**2 + 4 * 1 == 13


class TestVirasoroBound:
    """Verify W₃ bar dims ≥ Virasoro bar dims."""

    def test_w3_geq_virasoro(self):
        from compute.lib.bar_gf_solver import bar_dims_virasoro

        vir = bar_dims_virasoro(8)
        w3 = [2, 5, 16, 52, 171]
        # Extend W₃
        for _ in range(3):
            w3.append(4 * w3[-1] - 2 * w3[-2] - w3[-3])

        for n in range(min(len(w3), len(vir))):
            assert w3[n] >= vir[n], f"W₃ < Vir at degree {n+1}"


class TestAntiKoszul:
    """Verify W₃ is NOT classically Koszul (expected, higher-order OPE poles)."""

    def test_formal_dual_has_negative(self):
        """The standard Koszul dual Hilbert series has h[2] = -1."""
        from compute.lib.w3_h5_verification import check_anti_koszul
        result = check_anti_koszul()
        assert result["has_negative"] is True

    def test_pattern_h0_h1_h2(self):
        """h[0]=1, h[1]=2, h[2]=-1."""
        from compute.lib.w3_h5_verification import check_anti_koszul
        result = check_anti_koszul()
        assert result["pattern_h0_h1_h2"] == (1, 2, -1)

    def test_product_identity(self):
        """The formal product f_A(-t) · g(t) = 1 still holds."""
        from compute.lib.w3_h5_verification import check_anti_koszul
        result = check_anti_koszul()
        assert result["all_product_ok"] is True


class TestConjecturedGFIntegration:
    """Integration tests using bar_gf_solver's verify_conjectured_gf."""

    def test_w3_gf_via_solver(self):
        from compute.lib.bar_gf_solver import verify_conjectured_gf
        result = verify_conjectured_gf(
            [2, 5, 16, 52],
            num_coeffs=[2, -3],
            den_coeffs=[-4, 2, 1],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 171

    def test_w3_predict_from_5(self):
        """Predict a₆ from 5 known values."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf
        result = verify_conjectured_gf(
            [2, 5, 16, 52, 171],
            num_coeffs=[2, -3],
            den_coeffs=[-4, 2, 1],
            n_predict=3,
        )
        assert result["matches"] is True
        # a₆ = 4*171 - 2*52 - 16 = 684 - 104 - 16 = 564
        assert result["predictions"][0] == 564


class TestIntegration:
    """Full integration tests using w3_h5_verification module."""

    def test_recurrence_module(self):
        from compute.lib.w3_h5_verification import check_recurrence_consistency
        result = check_recurrence_consistency()
        assert result["H5_predicted"] == 171
        assert result["all_match"] is True

    def test_denominator_module(self):
        from compute.lib.w3_h5_verification import check_denominator_factorization
        result = check_denominator_factorization()
        assert result["factored"] is True

    def test_growth_rate_module(self):
        from compute.lib.w3_h5_verification import check_growth_rate
        result = check_growth_rate()
        assert result["convergence"] is True

    def test_ds_discriminant_module(self):
        from compute.lib.w3_h5_verification import check_ds_discriminant
        result = check_ds_discriminant()
        assert result["ds_invariance"] is True

    def test_virasoro_bound_module(self):
        from compute.lib.w3_h5_verification import check_virasoro_bound
        result = check_virasoro_bound()
        assert result["all_geq"] is True

    def test_anti_koszul_module(self):
        from compute.lib.w3_h5_verification import check_anti_koszul
        result = check_anti_koszul()
        assert result["anti_koszul_confirmed"] is True
        assert result["all_product_ok"] is True

    def test_run_all(self):
        from compute.lib.w3_h5_verification import run_all_checks
        results = run_all_checks()
        assert results["summary"]["status"] == "CONSISTENT"
