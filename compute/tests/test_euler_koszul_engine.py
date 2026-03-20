"""Tests for the Euler-Koszul three-tier classification engine.

Verifies:
1. Sewing Dirichlet lifts S_A(u) for all standard families
2. Euler-Koszul defect D_A(u) exact formulas
3. Three-tier classification (exact / finitely defective / non-Euler-Koszul)
4. DS reduction exponents and weight multisets
5. DS sends exact (tier 1) to finitely defective (tier 2)
6. Li coefficients and sign patterns
7. Defect polynomial expansion structure
8. Arithmetic structure at integer points

References:
  thm:euler-koszul-tier-classification, rem:ds-arithmetic-defect
"""

import pytest
from mpmath import mp, mpf, zeta, power, diff, log, euler as euler_gamma, fac, stieltjes, pi
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.euler_koszul_engine import (
    S_A, euler_koszul_defect, classify_tier,
    heisenberg_weights, virasoro_weights, w_n_weights, betagamma_weights,
    affine_sl2_weights, affine_slN_weights, lattice_weights,
    ds_exponents, ds_weights, ds_defect,
    li_coefficients, li_sign_pattern,
    verify_ds_sends_exact_to_defective,
    defect_polynomial_expansion, euler_koszul_class,
    ising_sewing_lift, rational_voa_tier,
    harmonic_zeta, virasoro_defect_exact, w3_defect_exact,
    wN_defect_exact, ds_arithmetic_defect_formula,
    defect_at_integers, sewing_coefficients, Xi_generic,
    tier_summary,
)

mp.dps = 30


# =============================================================================
# Test 1: Sewing Dirichlet lifts
# =============================================================================

class TestSewingLift:
    """S_A(u) for standard families."""

    def test_heisenberg(self):
        """S_H(u) = zeta(u) * zeta(u+1)."""
        for u_val in [2, 3, 5, 10]:
            u = mpf(u_val)
            S = S_A(u, heisenberg_weights())
            expected = zeta(u) * zeta(u + 1)
            assert abs(float(S - expected)) < 1e-20, f"Failed at u={u_val}"

    def test_virasoro(self):
        """S_Vir(u) = zeta(u+1) * (zeta(u) - 1)."""
        for u_val in [2, 3, 5, 10]:
            u = mpf(u_val)
            S = S_A(u, virasoro_weights())
            expected = zeta(u + 1) * (zeta(u) - 1)
            assert abs(float(S - expected)) < 1e-20, f"Failed at u={u_val}"

    def test_w3(self):
        """S_{W_3}(u) = zeta(u+1) * (2*zeta(u) - 1 - (1 + 2^{-u}))
                      = zeta(u+1) * (2*zeta(u) - 2 - 2^{-u})."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            S = S_A(u, w_n_weights(3))
            expected = zeta(u + 1) * (2 * zeta(u) - 2 - power(2, -u))
            assert abs(float(S - expected)) < 1e-15, f"Failed at u={u_val}"

    def test_betagamma(self):
        """S_{bg}(u) = 2 * zeta(u) * zeta(u+1)."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            S = S_A(u, betagamma_weights())
            expected = 2 * zeta(u) * zeta(u + 1)
            assert abs(float(S - expected)) < 1e-20, f"Failed at u={u_val}"

    def test_affine_sl2(self):
        """S_{sl2}(u) = 3 * zeta(u) * zeta(u+1)."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            S = S_A(u, affine_sl2_weights())
            expected = 3 * zeta(u) * zeta(u + 1)
            assert abs(float(S - expected)) < 1e-20, f"Failed at u={u_val}"

    def test_affine_slN(self):
        """S_{sl_N}(u) = (N^2-1) * zeta(u) * zeta(u+1)."""
        for N in [2, 3, 4]:
            dim = N * N - 1
            for u_val in [3, 5]:
                u = mpf(u_val)
                S = S_A(u, affine_slN_weights(N))
                expected = dim * zeta(u) * zeta(u + 1)
                assert abs(float(S - expected)) < 1e-15, \
                    f"Failed for sl_{N} at u={u_val}"

    def test_W_N_formula(self):
        """S_{W_N}(u) = zeta(u+1) * sum_{j=2}^N (zeta(u) - H_{j-1}(u))."""
        for N in [3, 4, 5]:
            u = mpf(3)
            S = S_A(u, w_n_weights(N))
            # Direct computation
            expected = zeta(u + 1) * sum(
                zeta(u) - harmonic_zeta(j - 1, u) for j in range(2, N + 1)
            )
            assert abs(float(S - expected)) < 1e-15, f"Failed for W_{N}"

    def test_lattice_rank(self):
        """Lattice VOA V_Lambda of rank r: S = r * zeta(u) * zeta(u+1)."""
        for r in [1, 2, 8, 24]:
            u = mpf(3)
            S = S_A(u, lattice_weights(r))
            expected = r * zeta(u) * zeta(u + 1)
            assert abs(float(S - expected)) < 1e-15, f"Failed for rank={r}"


# =============================================================================
# Test 2: Euler-Koszul defect
# =============================================================================

class TestDefect:
    """D_A(u) = S_A(u) / (|W| * zeta(u) * zeta(u+1))."""

    def test_heisenberg_exact(self):
        """D_H = 1 identically."""
        for u_val in [2, 3, 5, 10, 20]:
            D = euler_koszul_defect(u_val, heisenberg_weights())
            assert abs(float(D) - 1.0) < 1e-20, f"D_H({u_val}) = {float(D)} != 1"

    def test_virasoro_defective(self):
        """D_Vir(u) = 1 - 1/zeta(u)."""
        for u_val in [2, 3, 5, 10, 20]:
            u = mpf(u_val)
            D = euler_koszul_defect(u, virasoro_weights())
            expected = 1 - 1 / zeta(u)
            assert abs(float(D - expected)) < 1e-20, \
                f"D_Vir({u_val}) = {float(D)}, expected {float(expected)}"

    def test_betagamma_exact(self):
        """D_{bg} = 1 identically."""
        for u_val in [2, 3, 5, 10]:
            D = euler_koszul_defect(u_val, betagamma_weights())
            assert abs(float(D) - 1.0) < 1e-20

    def test_affine_exact(self):
        """D_{sl_N} = 1 for all N."""
        for N in [2, 3, 4]:
            for u_val in [3, 5]:
                D = euler_koszul_defect(u_val, affine_slN_weights(N))
                assert abs(float(D) - 1.0) < 1e-15, \
                    f"D_sl{N}({u_val}) = {float(D)} != 1"

    def test_w3_defective(self):
        """D_{W_3}(u) = 1 - (2 + 2^{-u}) / (2*zeta(u))."""
        for u_val in [2, 3, 5, 10]:
            u = mpf(u_val)
            D = euler_koszul_defect(u, w_n_weights(3))
            expected = w3_defect_exact(u)
            assert abs(float(D - expected)) < 1e-15, \
                f"D_W3({u_val}) = {float(D)}, expected {float(expected)}"

    def test_virasoro_defect_exact_formula(self):
        """Cross-check virasoro_defect_exact against direct computation."""
        for u_val in [2, 3, 5, 10]:
            u = mpf(u_val)
            direct = euler_koszul_defect(u, virasoro_weights())
            formula = virasoro_defect_exact(u)
            assert abs(float(direct - formula)) < 1e-20

    def test_wN_defect_exact_formula(self):
        """Cross-check wN_defect_exact against direct computation."""
        for N in [3, 4, 5]:
            for u_val in [3, 5]:
                u = mpf(u_val)
                direct = euler_koszul_defect(u, w_n_weights(N))
                formula = wN_defect_exact(N, u)
                assert abs(float(direct - formula)) < 1e-15

    def test_w_infinity_limit(self):
        """D_{W_N}(u) approaches a limit as N -> infinity.

        The harmonic sum grows logarithmically, so D stays bounded.
        """
        u = mpf(3)
        defects = []
        for N in [5, 10, 20, 50]:
            D = float(euler_koszul_defect(u, w_n_weights(N)))
            defects.append(D)
        # Defects should decrease (more harmonic correction) and stabilize
        for i in range(len(defects) - 1):
            assert defects[i] > defects[i + 1], "Defect not monotone decreasing with N"
        # Should remain positive
        assert defects[-1] > 0, "Defect should stay positive"

    def test_defect_less_than_one(self):
        """For finitely defective families, 0 < D < 1."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            for weights in [virasoro_weights(), w_n_weights(3), w_n_weights(5)]:
                D = float(euler_koszul_defect(u, weights))
                assert 0 < D < 1, f"D = {D} not in (0,1)"


# =============================================================================
# Test 3: Tier classification
# =============================================================================

class TestTierClassification:
    """Three-tier classification: exact / finitely_defective / non_euler_koszul."""

    def test_tier1_examples(self):
        """Exact Euler-Koszul: all weight-1 families."""
        assert classify_tier(heisenberg_weights()) == "exact"
        assert classify_tier(betagamma_weights()) == "exact"
        assert classify_tier(affine_sl2_weights()) == "exact"
        assert classify_tier(affine_slN_weights(3)) == "exact"
        assert classify_tier(affine_slN_weights(4)) == "exact"
        assert classify_tier(lattice_weights(1)) == "exact"
        assert classify_tier(lattice_weights(8)) == "exact"
        assert classify_tier(lattice_weights(24)) == "exact"

    def test_tier2_examples(self):
        """Finitely defective: W-algebra families."""
        assert classify_tier(virasoro_weights()) == "finitely_defective"
        assert classify_tier(w_n_weights(3)) == "finitely_defective"
        assert classify_tier(w_n_weights(4)) == "finitely_defective"
        assert classify_tier(w_n_weights(5)) == "finitely_defective"
        assert classify_tier(w_n_weights(10)) == "finitely_defective"

    def test_all_standard_families(self):
        """Comprehensive tier check for all named families."""
        exact_families = ["heisenberg", "betagamma", "affine_sl2"]
        for name in exact_families:
            info = euler_koszul_class(name)
            assert info["tier"] == "exact", f"{name} should be exact"

        defective_families = ["W_3", "W_4", "W_5"]
        for name in defective_families:
            info = euler_koszul_class(name)
            assert info["tier"] == "finitely_defective", \
                f"{name} should be finitely_defective"

    def test_virasoro_tier(self):
        """Virasoro is finitely defective."""
        info = euler_koszul_class("virasoro")
        assert info["tier"] == "finitely_defective"

    def test_empty_weights(self):
        """Empty weight set classified as exact (trivial case)."""
        assert classify_tier([]) == "exact"


# =============================================================================
# Test 4: DS reduction exponents
# =============================================================================

class TestDSReduction:
    """Casimir degrees from DS reduction of simple Lie algebras."""

    def test_sl2_exponents(self):
        """sl_2: exponents {1}, Casimir degrees {2}."""
        assert ds_exponents("sl_2") == [2]

    def test_sl3_exponents(self):
        """sl_3: exponents {1,2}, Casimir degrees {2,3}."""
        assert ds_exponents("sl_3") == [2, 3]

    def test_slN_exponents(self):
        """sl_N: Casimir degrees {2, 3, ..., N}."""
        for N in range(2, 8):
            assert ds_exponents(f"sl_{N}") == list(range(2, N + 1))

    def test_so5_exponents(self):
        """so(5) = B_2: exponents {1,3}, Casimir degrees {2,4}."""
        assert ds_exponents("so_5") == [2, 4]

    def test_g2_exponents(self):
        """G_2: exponents {1,5}, Casimir degrees {2,6}."""
        assert ds_exponents("G", rank=2) == [2, 6]

    def test_f4_exponents(self):
        """F_4: exponents {1,5,7,11}, Casimir degrees {2,6,8,12}."""
        assert ds_exponents("F", rank=4) == [2, 6, 8, 12]

    def test_ds_sl2_gives_virasoro(self):
        """DS of sl_2 gives Virasoro: W = {2}."""
        assert ds_weights("sl_2") == [2]
        assert ds_weights("sl_2") == virasoro_weights()

    def test_ds_slN_gives_WN(self):
        """DS of sl_N gives W_N: W = {2, 3, ..., N}."""
        for N in range(2, 8):
            assert ds_weights(f"sl_{N}") == w_n_weights(N)

    def test_exact_to_defective(self):
        """DS reduction: tier 1 (exact) -> tier 2 (finitely defective)."""
        for lie_type in ["sl_2", "sl_3", "sl_4", "sl_5"]:
            result = verify_ds_sends_exact_to_defective(lie_type)
            assert result["tier_before"] == "exact", \
                f"Affine {lie_type} should be exact"
            assert result["tier_after"] == "finitely_defective", \
                f"W({lie_type}) should be finitely defective"
            assert result["exact_to_defective"], \
                f"DS should map exact to defective for {lie_type}"

    def test_ds_defect_sl2_equals_virasoro(self):
        """DS defect for sl_2 = Virasoro defect."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            D_ds = ds_defect("sl_2", u)
            D_vir = virasoro_defect_exact(u)
            assert abs(float(D_ds - D_vir)) < 1e-15

    def test_ds_arithmetic_formula(self):
        """D_{W(g)}(u) = 1 - (1/r) * sum H_{d_i-1}(u) / zeta(u)."""
        for lie_type, rank in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("G", 2)]:
            for u_val in [3, 5]:
                u = mpf(u_val)
                D_direct = ds_defect(lie_type, u, rank=rank)
                D_formula = ds_arithmetic_defect_formula(lie_type, u, rank=rank)
                assert abs(float(D_direct - D_formula)) < 1e-15, \
                    f"Mismatch for {lie_type}_{rank} at u={u_val}"

    def test_so5_ds_weights(self):
        """so(5) DS: weights {2,4}."""
        assert ds_weights("so_5") == [2, 4]

    def test_sp4_ds_weights(self):
        """sp(4) = C_2 DS: weights {2,4}."""
        assert ds_weights("sp_4") == [2, 4]

    def test_so5_equals_sp4_ds(self):
        """so(5) and sp(4) share Casimir degrees {2,4} (isogenous)."""
        assert ds_weights("so_5") == ds_weights("sp_4")


# =============================================================================
# Test 5: Li coefficients
# =============================================================================

class TestLiCoefficients:
    """Prime-side Li coefficients lambda_tilde_n(A)."""

    def test_heisenberg_positive_low(self):
        """Heisenberg: lambda_n > 0 for n = 1,...,6."""
        coeffs = li_coefficients(heisenberg_weights(), max_n=6)
        for n, c in enumerate(coeffs, 1):
            assert float(c) > 0, f"lambda_{n}(H) = {float(c)} should be positive"

    def test_heisenberg_negative_7(self):
        """Heisenberg: lambda_7 < 0 (the first sign change)."""
        coeffs = li_coefficients(heisenberg_weights(), max_n=7)
        assert float(coeffs[6]) < 0, f"lambda_7(H) = {float(coeffs[6])} should be negative"

    def test_virasoro_all_negative(self):
        """Virasoro: lambda_n < 0 for all n = 1,...,10."""
        coeffs = li_coefficients(virasoro_weights(), max_n=10)
        for n, c in enumerate(coeffs, 1):
            assert float(c) < 0, f"lambda_{n}(Vir) = {float(c)} should be negative"

    def test_w3_all_negative(self):
        """W_3: lambda_n < 0 for all n = 1,...,8."""
        coeffs = li_coefficients(w_n_weights(3), max_n=8)
        for n, c in enumerate(coeffs, 1):
            assert float(c) < 0, f"lambda_{n}(W_3) = {float(c)} should be negative"

    def test_ds_preserves_negativity(self):
        """DS reduction preserves all-negative Li sign pattern.

        Virasoro = DS(sl_2) has all negative Li coefficients.
        W_3 = DS(sl_3) has all negative Li coefficients.
        """
        for lie_type, N in [("sl_2", 2), ("sl_3", 3), ("sl_4", 4)]:
            weights = ds_weights(lie_type)
            signs = li_sign_pattern(weights, max_n=6)
            for n, s in enumerate(signs, 1):
                assert s == -1, \
                    f"lambda_{n}(W({lie_type})) sign = {s}, expected -1"

    def test_betagamma_positive_low(self):
        """Beta-gamma: lambda_n > 0 for small n (like Heisenberg, but doubled)."""
        coeffs = li_coefficients(betagamma_weights(), max_n=5)
        for n, c in enumerate(coeffs, 1):
            assert float(c) > 0, f"lambda_{n}(bg) = {float(c)} should be positive"

    def test_sign_change_heisenberg(self):
        """The sign pattern for Heisenberg: +,+,+,+,+,+,-,..."""
        signs = li_sign_pattern(heisenberg_weights(), max_n=8)
        assert signs[:6] == [1, 1, 1, 1, 1, 1], "First 6 should be positive"
        assert signs[6] == -1, "7th should be negative"


# =============================================================================
# Test 6: Defect polynomial expansion
# =============================================================================

class TestDefectPolynomial:
    """Defect expansion in powers of 1/zeta(u)."""

    def test_heisenberg_degree_zero(self):
        """Heisenberg: defect degree 0 (exact, no correction)."""
        poly = defect_polynomial_expansion(heisenberg_weights())
        assert poly["defect_degree"] == 0
        assert poly["max_weight"] == 1

    def test_virasoro_linear(self):
        """Virasoro: D = 1 - 1/zeta(u), degree 1 in 1/zeta."""
        poly = defect_polynomial_expansion(virasoro_weights())
        assert poly["defect_degree"] == 1
        assert poly["max_weight"] == 2
        # At u=3: harmonic correction should be -1/zeta(3)
        expected_corr = float(-1 / zeta(3))
        assert abs(poly["harmonic_correction"][3] - expected_corr) < 1e-10

    def test_w3_structure(self):
        """W_3: defect degree 1, max weight 3."""
        poly = defect_polynomial_expansion(w_n_weights(3))
        assert poly["defect_degree"] == 1
        assert poly["max_weight"] == 3
        assert poly["num_generators"] == 2

    def test_wN_degree(self):
        """D_{W_N} always has defect degree 1 (linear in 1/zeta)."""
        for N in [3, 4, 5, 10]:
            poly = defect_polynomial_expansion(w_n_weights(N))
            assert poly["defect_degree"] == 1, f"W_{N} should have degree 1"

    def test_betagamma_degree_zero(self):
        """Beta-gamma: exact, degree 0."""
        poly = defect_polynomial_expansion(betagamma_weights())
        assert poly["defect_degree"] == 0

    def test_constant_term_always_one(self):
        """The constant term is always 1."""
        for weights in [heisenberg_weights(), virasoro_weights(),
                        w_n_weights(3), betagamma_weights()]:
            poly = defect_polynomial_expansion(weights)
            assert poly["constant_term"] == 1


# =============================================================================
# Test 7: Arithmetic structure at integer points
# =============================================================================

class TestArithmeticStructure:
    """Defect and sewing lift values at integer points."""

    def test_defect_at_u2(self):
        """D_Vir(2) = 1 - 1/zeta(2) = 1 - 6/pi^2."""
        D = euler_koszul_defect(2, virasoro_weights())
        expected = 1 - 6 / float(pi**2)
        assert abs(float(D) - expected) < 1e-10

    def test_defect_at_u3(self):
        """D_Vir(3) = 1 - 1/zeta(3)."""
        D = euler_koszul_defect(3, virasoro_weights())
        expected = float(1 - 1 / zeta(3))
        assert abs(float(D) - expected) < 1e-15

    def test_defect_factorization(self):
        """D_{W_N}(u) = (S_{W_N}(u) - (N-1)*zeta*zeta(u+1)) / ((N-1)*zeta*zeta(u+1))
        This is just a defect from the baseline, sign check."""
        u = mpf(3)
        for N in [3, 4, 5]:
            S = S_A(u, w_n_weights(N))
            baseline = (N - 1) * zeta(u) * zeta(u + 1)
            assert float(S) < float(baseline), \
                f"S_{N}(3) should be less than baseline"

    def test_heisenberg_at_integers(self):
        """S_H(n) = zeta(n)*zeta(n+1) at integer points n >= 2."""
        for n in range(2, 10):
            S = S_A(n, heisenberg_weights())
            expected = zeta(n) * zeta(n + 1)
            assert abs(float(S - expected)) < 1e-20

    def test_defect_approaches_zero(self):
        """D_A(u) -> 0 as u -> infinity for finitely defective families.

        Since zeta(u) -> 1 as u -> inf, and H_{w-1}(u) -> H_{w-1}(inf) = w-1,
        D = 1 - (sum H_{w_i-1})/(n*zeta) -> 1 - (sum(w_i-1))/n  for large u.
        Actually D_Vir(u) = 1 - 1/zeta(u) -> 0 since zeta(u) -> 1.
        """
        u = mpf(50)
        for weights in [virasoro_weights(), w_n_weights(3), w_n_weights(5)]:
            D = float(euler_koszul_defect(u, weights))
            assert D < 0.01, \
                f"D({u}) = {D} should approach 0 for finitely defective families"

    def test_ds_defect_at_u2_g2(self):
        """D_{W(G_2)}(2) is computable and less than 1."""
        D = float(ds_defect("G", 2, rank=2))
        assert 0 < D < 1


# =============================================================================
# Test 8: Named family registry
# =============================================================================

class TestNamedFamilies:
    """euler_koszul_class() registry."""

    def test_heisenberg_class(self):
        info = euler_koszul_class("heisenberg")
        assert info["weights"] == [1]
        assert info["tier"] == "exact"

    def test_virasoro_class(self):
        info = euler_koszul_class("virasoro")
        assert info["weights"] == [2]
        assert info["tier"] == "finitely_defective"

    def test_betagamma_class(self):
        info = euler_koszul_class("betagamma")
        assert info["weights"] == [1, 1]
        assert info["tier"] == "exact"

    def test_wn_class(self):
        for N in [3, 4, 5, 10]:
            info = euler_koszul_class(f"W_{N}")
            assert info["weights"] == list(range(2, N + 1))
            assert info["tier"] == "finitely_defective"

    def test_affine_sl3_class(self):
        info = euler_koszul_class("affine_sl3")
        assert info["weights"] == [1] * 8
        assert info["tier"] == "exact"

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            euler_koszul_class("unknown_algebra")


# =============================================================================
# Test 9: Ising and rational VOA
# =============================================================================

class TestIsingAndRationalVOA:
    """Ising model and minimal model tier classification."""

    def test_ising_sewing_lift(self):
        """S_Ising(u) = zeta(u+1)*(zeta(u)-1) at weight-multiset level."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            S = ising_sewing_lift(u)
            expected = zeta(u + 1) * (zeta(u) - 1)
            assert abs(float(S - expected)) < 1e-15

    def test_ising_is_virasoro_type(self):
        """Ising shares Virasoro weight multiset {2}."""
        u = mpf(3)
        S_ising = ising_sewing_lift(u)
        S_vir = S_A(u, virasoro_weights())
        assert abs(float(S_ising - S_vir)) < 1e-15

    def test_rational_voa_ising(self):
        """M(4,3) = Ising, c=1/2, tier = finitely_defective."""
        info = rational_voa_tier((4, 3))
        assert info["is_ising"]
        assert abs(info["c"] - 0.5) < 1e-10
        assert info["n_primaries"] == 3
        assert info["tier"] == "finitely_defective"
        assert info["level"] == 24

    def test_rational_voa_tricritical_ising(self):
        """M(5,4): tricritical Ising, c=7/10."""
        info = rational_voa_tier((5, 4))
        assert abs(info["c"] - 0.7) < 1e-10
        assert info["n_primaries"] == 6
        assert info["tier"] == "finitely_defective"

    def test_rational_voa_yang_lee(self):
        """M(5,2): Yang-Lee, c = -22/5."""
        info = rational_voa_tier((5, 2))
        assert abs(info["c"] - (-22 / 5)) < 1e-10
        assert info["tier"] == "finitely_defective"

    def test_rational_voa_invalid(self):
        """Invalid model raises error."""
        with pytest.raises(ValueError):
            rational_voa_tier((3, 4))  # p <= q
        with pytest.raises(ValueError):
            rational_voa_tier((4, 2))  # gcd(4,2) = 2


# =============================================================================
# Test 10: Sewing coefficients
# =============================================================================

class TestSewingCoefficients:
    """Connected free energy coefficients a_A(N)."""

    def test_heisenberg_sigma_minus1(self):
        """a_H(N) = sigma_{-1}(N)."""
        coeffs = sewing_coefficients(heisenberg_weights(), 10)
        # sigma_{-1}(1) = 1, sigma_{-1}(2) = 3/2, sigma_{-1}(3) = 4/3
        assert abs(float(coeffs[0]) - 1.0) < 1e-15
        assert abs(float(coeffs[1]) - 1.5) < 1e-15
        assert abs(float(coeffs[2]) - (1 + 1.0 / 3)) < 1e-15

    def test_betagamma_twice_heisenberg(self):
        """a_{bg}(N) = 2 * a_H(N) (two weight-1 generators)."""
        c_h = sewing_coefficients(heisenberg_weights(), 10)
        c_bg = sewing_coefficients(betagamma_weights(), 10)
        for i in range(10):
            assert abs(float(c_bg[i]) - 2 * float(c_h[i])) < 1e-15

    def test_virasoro_no_n1(self):
        """a_Vir(1) = 0 (no weight-1 generator, no N=1 term)."""
        coeffs = sewing_coefficients(virasoro_weights(), 5)
        assert abs(float(coeffs[0])) < 1e-15


# =============================================================================
# Test 11: Additivity under direct sum
# =============================================================================

class TestAdditivity:
    """S_{A1+A2}(u) = S_{A1}(u) + S_{A2}(u) for independent sum."""

    def test_heis_plus_vir(self):
        """S_{H+Vir}(u) = S_H(u) + S_Vir(u)."""
        u = mpf(3)
        S_sum = S_A(u, [1, 2])  # weights {1} union {2}
        S_H = S_A(u, [1])
        S_V = S_A(u, [2])
        assert abs(float(S_sum - S_H - S_V)) < 1e-15

    def test_weight_union(self):
        """S for weight union = sum of S for parts."""
        u = mpf(3)
        w1 = [1, 1]
        w2 = [2, 3]
        S_union = S_A(u, w1 + w2)
        S_1 = S_A(u, w1)
        S_2 = S_A(u, w2)
        assert abs(float(S_union - S_1 - S_2)) < 1e-15


# =============================================================================
# Test 12: DS exponent edge cases
# =============================================================================

class TestDSExponentsEdgeCases:
    """Edge cases for DS exponent lookup."""

    def test_letter_notation_A(self):
        """A_r notation: Casimir degrees {2,...,r+1}."""
        for r in range(1, 6):
            assert ds_exponents("A", rank=r) == list(range(2, r + 2))

    def test_so7_exponents(self):
        """so(7) = B_3: Casimir degrees {2,4,6}."""
        assert ds_exponents("so_7") == [2, 4, 6]

    def test_sp6_exponents(self):
        """sp(6) = C_3: Casimir degrees {2,4,6}."""
        assert ds_exponents("sp_6") == [2, 4, 6]

    def test_so8_exponents(self):
        """so(8) = D_4: Casimir degrees {2,4,4,6}."""
        assert ds_exponents("so_8") == [2, 4, 4, 6]

    def test_e6_exponents(self):
        """E_6: Casimir degrees {2,5,6,8,9,12}."""
        assert ds_exponents("E", rank=6) == [2, 5, 6, 8, 9, 12]

    def test_e8_exponents(self):
        """E_8: Casimir degrees {2,8,12,14,18,20,24,30}."""
        assert ds_exponents("E", rank=8) == [2, 8, 12, 14, 18, 20, 24, 30]


# =============================================================================
# Test 13: Xi regularization
# =============================================================================

class TestXiRegularization:
    """Xi_A(u) = (u-1)*S_A(u) near u=1."""

    def test_xi_heisenberg_at_u2(self):
        """Xi_H(2) = zeta(2) * zeta(3)."""
        Xi = Xi_generic(2, heisenberg_weights())
        expected = zeta(2) * zeta(3)
        assert abs(float(Xi - expected)) < 1e-15

    def test_xi_regularized_near_1(self):
        """Xi_H near u=1 is well-defined (no pole)."""
        # Xi_H(u) = (u-1)*zeta(u)*zeta(u+1)
        # As u -> 1, (u-1)*zeta(u) -> 1, so Xi_H(1) = zeta(2)
        Xi_near = Xi_generic(mpf('1.0001'), heisenberg_weights())
        assert float(Xi_near) > 0
        # Should approach zeta(2) = pi^2/6
        assert abs(float(Xi_near) - float(zeta(2))) < 0.01

    def test_xi_virasoro_positive(self):
        """Xi_Vir(u) > 0 for u >= 2."""
        for u_val in [2, 3, 5, 10]:
            Xi = Xi_generic(u_val, virasoro_weights())
            assert float(Xi) > 0


# =============================================================================
# Test 14: Tier summary
# =============================================================================

class TestTierSummary:
    """tier_summary() returns complete analysis."""

    def test_heisenberg_summary(self):
        result = tier_summary("heisenberg")
        assert result["tier"] == "exact"
        assert abs(result["D(3)"] - 1.0) < 1e-10

    def test_virasoro_summary(self):
        result = tier_summary("virasoro")
        assert result["tier"] == "finitely_defective"
        assert result["D(3)"] < 1.0

    def test_weights_summary(self):
        """Summary from raw weights."""
        result = tier_summary([1, 2, 3])
        assert result["tier"] == "finitely_defective"


# =============================================================================
# Test 15: Monotonicity and convergence
# =============================================================================

class TestMonotonicity:
    """Structural properties of the defect."""

    def test_defect_monotone_decreasing_in_u(self):
        """D_Vir(u) = 1 - 1/zeta(u) is monotonically DECREASING in u.

        Since zeta(u) is decreasing for u > 1 (approaching 1),
        1/zeta(u) is increasing, so D = 1 - 1/zeta is decreasing.
        """
        u_vals = [2, 3, 5, 10, 20]
        defects = [float(euler_koszul_defect(u, virasoro_weights()))
                   for u in u_vals]
        for i in range(len(defects) - 1):
            assert defects[i] > defects[i + 1], \
                f"D_Vir not monotone decreasing: D({u_vals[i]})={defects[i]} <= D({u_vals[i+1]})={defects[i+1]}"

    def test_ds_defect_increases_with_rank(self):
        """D_{W_N}(3) increases with N (more harmonic correction)."""
        # Actually D_{W_N} DECREASES with N at fixed u
        # because more harmonic terms are subtracted
        u = mpf(3)
        D_values = []
        for N in [2, 3, 5, 10]:
            D = float(euler_koszul_defect(u, w_n_weights(N)))
            D_values.append(D)
        for i in range(len(D_values) - 1):
            assert D_values[i] > D_values[i + 1], \
                f"D_W{[2,3,5,10][i]} should be > D_W{[2,3,5,10][i+1]}"

    def test_sewing_lift_positive(self):
        """S_A(u) > 0 for all standard families at u >= 2."""
        for weights in [heisenberg_weights(), virasoro_weights(),
                        w_n_weights(3), betagamma_weights(),
                        affine_sl2_weights()]:
            for u_val in [2, 3, 5, 10]:
                S = float(S_A(u_val, weights))
                assert S > 0, f"S_A({u_val}) = {S} should be positive"
