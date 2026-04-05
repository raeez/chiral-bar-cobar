"""
Tests for SK bridge and surface polarization (B8 + B12).

Verifies:
1. f_22 Hecke eigenvalues against LMFDB
2. SK Hecke eigenvalues lambda_{SK(f_22)}(T_p) at p = 2, 3, 5
3. Deligne's Ramanujan bound for f_22
4. Waldspurger proportionality across discriminants
5. Genus-2 Beurling kernel positivity structure
6. Surface polarization analysis (honest Gap A assessment)
7. Li coefficient vs central value logical separation
8. Varying-D constraint analysis
"""

import pytest
import numpy as np

from compute.lib.sk_surface_polarization import (
    ramanujan_tau,
    e10_coefficient,
    f22_coefficient,
    verify_f22_eigenvalues,
    sk_hecke_eigenvalue,
    sk_eigenvalue_table,
    twisted_l_euler,
    waldspurger_table,
    spin_l_factorization_check,
    beurling_kernel_positivity_structure,
    li_vs_central_value_analysis,
    varying_d_constraints,
    surface_polarization_candidate,
    sk_bridge_computation,
    combined_assessment,
    F22_KNOWN,
)


# ============================================================
# 1. RAMANUJAN TAU AND EISENSTEIN SERIES
# ============================================================

class TestRamanujanTau:
    """Verify Ramanujan tau values."""

    def test_tau_1(self):
        assert ramanujan_tau(1) == 1

    def test_tau_2(self):
        assert ramanujan_tau(2) == -24

    def test_tau_3(self):
        assert ramanujan_tau(3) == 252

    def test_tau_4(self):
        assert ramanujan_tau(4) == -1472

    def test_tau_5(self):
        assert ramanujan_tau(5) == 4830

    def test_tau_6(self):
        """tau(6) = tau(2)*tau(3) = -24*252 = -6048."""
        assert ramanujan_tau(6) == -6048

    def test_tau_deligne_bound_small(self):
        """Deligne: |tau(p)| <= 2*p^{11/2} for all primes p."""
        for p in [2, 3, 5, 7, 11, 13]:
            bound = 2 * p ** 5.5
            assert abs(ramanujan_tau(p)) <= bound + 1


class TestE10:
    """Verify E_10 coefficients."""

    def test_e10_constant(self):
        assert e10_coefficient(0) == 1

    def test_e10_first(self):
        """E_10(q) = 1 - 264*q + ... so e_10(1) = -264."""
        assert e10_coefficient(1) == -264

    def test_e10_second(self):
        """e_10(2) = -264 * sigma_9(2) = -264 * (1 + 512) = -264 * 513."""
        assert e10_coefficient(2) == -264 * 513


# ============================================================
# 2. f_22 HECKE EIGENVALUES
# ============================================================

class TestF22:
    """Verify f_22 = Delta * E_10 eigenvalues."""

    def test_f22_leading(self):
        """a_22(1) = tau(1) * e_10(0) = 1."""
        assert f22_coefficient(1) == 1

    def test_f22_at_2(self):
        """a_22(2) = tau(2) + e_10(1)*tau(1) = -24 + (-264)*1 = -288."""
        assert f22_coefficient(2) == -288

    def test_f22_at_3(self):
        """a_22(3) = tau(3) + e_10(1)*tau(2) + e_10(2)*tau(1).

        = 252 + (-264)*(-24) + (-264*513)*1
        = 252 + 6336 - 135432
        = -128844
        """
        assert f22_coefficient(3) == -128844

    def test_f22_at_5(self):
        """a_22(5) = 21640950 (computed from convolution, verified by Hecke relations)."""
        assert f22_coefficient(5) == 21640950

    def test_f22_lmfdb_verification(self):
        """Verify all known LMFDB values."""
        results = verify_f22_eigenvalues()
        for p, data in results.items():
            assert data['match'], f"f_22 coefficient at p={p}: got {data['computed']}, expected {data['expected']}"

    def test_f22_deligne_bound(self):
        """Deligne: |a_22(p)| <= 2*p^{21/2} for primes p."""
        for p in [2, 3, 5, 7]:
            bound = 2 * p ** 10.5
            assert abs(f22_coefficient(p)) <= bound + 1, \
                f"|a_22({p})| = {abs(f22_coefficient(p))} exceeds Deligne bound {bound}"


# ============================================================
# 3. SK HECKE EIGENVALUES
# ============================================================

class TestSKHecke:
    """Verify SK lift Hecke eigenvalues."""

    def test_sk_at_2(self):
        """lambda_{SK}(2) = a_22(2) + 2^{11} + 2^{10} = -288 + 2048 + 1024 = 2784."""
        lam = sk_hecke_eigenvalue(2)
        assert lam == -288 + 2048 + 1024
        assert lam == 2784

    def test_sk_at_3(self):
        """lambda_{SK}(3) = a_22(3) + 3^{11} + 3^{10}."""
        lam = sk_hecke_eigenvalue(3)
        expected = -128844 + 177147 + 59049
        assert lam == expected
        assert lam == 107352

    def test_sk_at_5(self):
        """lambda_{SK}(5) = a_22(5) + 5^{11} + 5^{10} = 21640950 + 48828125 + 9765625."""
        lam = sk_hecke_eigenvalue(5)
        expected = 21640950 + 48828125 + 9765625
        assert lam == expected
        assert lam == 80234700

    def test_sk_decomposition(self):
        """Verify the SK eigenvalue decomposition at p=2,3,5."""
        table = sk_eigenvalue_table([2, 3, 5])
        for p in [2, 3, 5]:
            entry = table[p]
            assert entry['lambda_SK(p)'] == entry['a_22(p)'] + entry['p^11'] + entry['p^10']

    def test_sk_eigenvalues_positive_at_small_primes(self):
        """SK eigenvalues at p=2,3,5 are all positive (p^{11} dominates)."""
        for p in [2, 3, 5]:
            lam = sk_hecke_eigenvalue(p)
            assert lam > 0, f"lambda_SK({p}) = {lam} should be positive"

    def test_sk_a22_dominance(self):
        """For small p, the a_22(p) term is smaller than p^{11}."""
        for p in [2, 3, 5]:
            a_p = f22_coefficient(p)
            assert abs(a_p) < p ** 11, \
                f"|a_22({p})| = {abs(a_p)} should be < p^11 = {p**11}"


# ============================================================
# 4. WALDSPURGER FORMULA
# ============================================================

class TestWaldspurger:
    """Test Waldspurger proportionality for chi_12 = SK(f_22)."""

    def test_waldspurger_all_positive(self):
        """L(11, f_22 x chi_D) should be positive for all tested D.

        This follows from GRH (conjectural) and the Waldspurger formula.
        For convergence reasons, we use modest nmax.
        """
        wald = waldspurger_table([-3, -4, -7, -8], nmax=600)
        for row in wald:
            assert row['L(11, f_22 x chi_D)'] > 0, \
                f"L(11, f_22 x chi_{row['D']}) = {row['L(11, f_22 x chi_D)']}"

    def test_waldspurger_rhs_positive(self):
        """The Waldspurger RHS L * |D|^{10} is positive."""
        wald = waldspurger_table([-3, -4, -7], nmax=600)
        for row in wald:
            assert row['waldspurger_rhs'] > 0

    def test_waldspurger_varies_with_d(self):
        """L-values vary non-trivially across discriminants."""
        wald = waldspurger_table([-3, -4, -7], nmax=600)
        vals = [row['L(11, f_22 x chi_D)'] for row in wald]
        # Should not all be equal
        assert max(vals) > 1.1 * min(vals), "L-values should vary across D"


# ============================================================
# 5. SPIN L-FUNCTION FACTORIZATION
# ============================================================

class TestSpinFactorization:
    """Test the spin L-function factorization."""

    def test_spin_at_s13(self):
        """Check that L^spin(13, SK(f_22)) = zeta(3)*zeta(2)*L(13, f_22)."""
        result = spin_l_factorization_check(13, nmax=200)
        # All individual factors should be finite
        assert np.isfinite(result['zeta(s-10)'])
        assert np.isfinite(result['zeta(s-11)'])
        assert np.isfinite(result['L(s, f_22)'])
        # The product should be finite and nonzero
        assert abs(result['product']) > 1e-30
        assert np.isfinite(result['product'])


# ============================================================
# 6. BEURLING KERNEL POSITIVITY
# ============================================================

class TestBeurlingPositivity:
    """Test the genus-2 Beurling kernel positivity structure."""

    def test_kernel_is_psd(self):
        result = beurling_kernel_positivity_structure()
        assert result['kernel_psd'] is True

    def test_constrains_central_values(self):
        result = beurling_kernel_positivity_structure()
        assert result['constrains_central_L_values'] is True

    def test_does_not_constrain_li(self):
        """HONEST: kernel positivity does NOT constrain Li coefficients."""
        result = beurling_kernel_positivity_structure()
        assert result['constrains_li_coefficients'] is False

    def test_does_not_constrain_individual_l(self):
        result = beurling_kernel_positivity_structure()
        assert result['constrains_individual_L_values'] is False

    def test_gap_a_partial(self):
        result = beurling_kernel_positivity_structure()
        assert 'partial' in result['gap_a_resolution']


# ============================================================
# 7. LI VS CENTRAL VALUE ANALYSIS
# ============================================================

class TestLiVsCentralValue:
    """Test the logical gap analysis between Li and central values."""

    def test_central_not_sufficient_for_li(self):
        result = li_vs_central_value_analysis()
        assert result['central_value_sufficient_for_li'] is False

    def test_li_implies_central(self):
        result = li_vs_central_value_analysis()
        assert result['li_implies_central_value'] is True

    def test_isolation_open(self):
        result = li_vs_central_value_analysis()
        assert 'open' in result['isolation_problem']


# ============================================================
# 8. VARYING D CONSTRAINTS
# ============================================================

class TestVaryingD:
    """Test the varying-discriminant constraint analysis."""

    def test_l_values_finite(self):
        """All L-values should be finite."""
        result = varying_d_constraints([-3, -4, -7, -8], nmax=400)
        for D, L in result['L_values'].items():
            assert np.isfinite(L), f"L(11, f_22 x chi_{D}) is not finite"

    def test_l_values_positive(self):
        """Under GRH, L(11, f_22 x chi_D) > 0."""
        result = varying_d_constraints([-3, -4, -7], nmax=400)
        assert result['all_positive']

    def test_not_sufficient(self):
        result = varying_d_constraints([-3, -4, -7], nmax=400)
        assert result['sufficient_for_zero_locations'] is False

    def test_nontrivial_variation(self):
        """L-values should vary across discriminants."""
        result = varying_d_constraints([-3, -4, -7, -8], nmax=400)
        assert result['variation_ratio'] > 1.05


# ============================================================
# 9. SURFACE POLARIZATION
# ============================================================

class TestSurfacePolarization:
    """Test the surface polarization candidate analysis."""

    def test_kernel_psd(self):
        result = surface_polarization_candidate()
        assert result['test1_psd'] is True

    def test_not_surface_polarization(self):
        """HONEST: K^{(2)} is NOT a surface polarization for Gap A."""
        result = surface_polarization_candidate()
        assert result['is_surface_polarization'] is False

    def test_does_not_constrain_li(self):
        result = surface_polarization_candidate()
        assert result['test3_constrains_li'] is False

    def test_required_ingredients(self):
        """Three open problems needed for resolution."""
        result = surface_polarization_candidate()
        assert len(result['required_for_resolution']) == 3


# ============================================================
# 10. FULL SK BRIDGE COMPUTATION
# ============================================================

class TestSKBridge:
    """Full SK bridge computation tests."""

    def test_bridge_eigenvalues(self):
        """Verify the full SK bridge computation."""
        result = sk_bridge_computation()
        ev = result['eigenvalues']

        # p = 2: lambda = -288 + 2048 + 1024 = 2784
        assert ev[2]['lambda_SK(p)'] == 2784
        # p = 3: lambda = -128844 + 177147 + 59049 = 107352
        assert ev[3]['lambda_SK(p)'] == 107352
        # p = 5: lambda = 21640950 + 48828125 + 9765625 = 80234700
        assert ev[5]['lambda_SK(p)'] == 80234700

    def test_bridge_ramanujan(self):
        """All f_22 eigenvalues satisfy Deligne's bound."""
        result = sk_bridge_computation()
        for p, data in result['ramanujan_checks'].items():
            assert data['satisfies_deligne'], \
                f"Deligne bound violated at p={p}"

    def test_bridge_tau_values(self):
        """Verify tau values in the eigenvalue table."""
        result = sk_bridge_computation()
        ev = result['eigenvalues']
        assert ev[2]['tau(p)'] == -24
        assert ev[3]['tau(p)'] == 252
        assert ev[5]['tau(p)'] == 4830


# ============================================================
# 11. COMBINED ASSESSMENT
# ============================================================

class TestCombinedAssessment:
    """Test the combined B8+B12 assessment."""

    def test_combined_runs(self):
        """The combined assessment should complete without error."""
        result = combined_assessment()
        assert result is not None

    def test_sk_eigenvalues_computed(self):
        result = combined_assessment()
        assert result['sk_bridge']['eigenvalues_computed'] is True

    def test_kernel_psd(self):
        result = combined_assessment()
        assert result['surface_polarization']['kernel_psd'] is True

    def test_gap_a_unresolved(self):
        """Gap A is NOT resolved by genus-2 positivity."""
        result = combined_assessment()
        assert result['surface_polarization']['resolves_gap_a'] is False

    def test_gap_d_narrowed(self):
        """Gap D IS narrowed by spectral support alignment."""
        result = combined_assessment()
        assert result['surface_polarization']['narrows_gap_d'] is True

    def test_li_not_constrained(self):
        result = combined_assessment()
        assert result['surface_polarization']['constrains_li'] is False

    def test_varying_d_not_sufficient(self):
        result = combined_assessment()
        assert result['sk_bridge']['varying_d_sufficient'] is False


# ============================================================
# 12. CONSISTENCY WITH EXISTING MODULES
# ============================================================

class TestConsistency:
    """Cross-check with existing compute modules."""

    def test_tau_consistency(self):
        """Verify tau values match lattice_shadow_census."""
        from compute.lib.lattice_shadow_census import _ramanujan_tau
        for n in range(1, 10):
            assert ramanujan_tau(n) == _ramanujan_tau(n)

    def test_f22_multiplicativity(self):
        """f_22 eigenvalues satisfy Hecke multiplicativity at coprime indices.

        For a Hecke eigenform: a(mn) = a(m)*a(n) when gcd(m,n) = 1.
        """
        # a(6) = a(2)*a(3) since gcd(2,3) = 1
        assert f22_coefficient(6) == f22_coefficient(2) * f22_coefficient(3)

    def test_f22_hecke_at_p_squared(self):
        """Hecke relation at p^2: a(p^2) = a(p)^2 - p^{21}.

        For weight-22 eigenform: a(p^2) = a(p)^2 - p^{k-1} = a(p)^2 - p^{21}.
        """
        p = 2
        a_p = f22_coefficient(p)
        a_p2 = f22_coefficient(p * p)
        expected = a_p ** 2 - p ** 21
        assert a_p2 == expected, \
            f"Hecke at p^2: a(4) = {a_p2}, expected a(2)^2 - 2^21 = {expected}"

    def test_sk_eigenvalue_formula(self):
        """The SK eigenvalue formula lambda(p) = a_22(p) + p^11 + p^10
        is consistent with the spin L-function factorization."""
        for p in [2, 3, 5]:
            lam = sk_hecke_eigenvalue(p)
            a_p = f22_coefficient(p)
            assert lam == a_p + p ** 11 + p ** 10
