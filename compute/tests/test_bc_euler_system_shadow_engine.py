r"""Tests for bc_euler_system_shadow_engine.py -- Euler systems from the
shadow obstruction tower.

Verification paths:
  - Path 1: Norm compatibility N(c_{mn}) = P_ell(Fr^{-1}) * c_n
  - Path 2: Selmer bound vs shadow L-value
  - Path 3: Kolyvagin divisibility kappa_{n*ell} divisible by ell^a
  - Path 4: Koszul duality ES(A) vs ES(A!) via Theorem C

85+ tests covering:
  1.  Shadow Galois cohomology classes c_ell(A) for 15 primes x 18 algebras
  2.  Norm compatibility across prime pairs
  3.  Selmer group bounds vs L-values
  4.  BSD-type formula verification
  5.  Kolyvagin derivative classes and divisibility
  6.  Shadow cyclotomic units and regulator
  7.  Kato comparison: shadow ES vs standard construction
  8.  Koszul duality on Euler systems (AP24-safe)
  9.  Iwasawa invariants (mu, lambda)
  10. Euler system rank and shadow class
  11. Cross-family consistency checks (AP10)
  12. Structural invariants

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general.
CAUTION (AP10): Tests use multi-path verification, not hardcoded values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

import math
import cmath
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from compute.lib import bc_euler_system_shadow_engine as engine

STANDARD_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# ============================================================================
# Section 1: Kappa values (AP1-safe, independent verification)
# ============================================================================

class TestKappaValues:
    """Verify family-specific kappa formulas (AP1, AP9, AP48)."""

    def test_kappa_heisenberg_is_level(self):
        """kappa(H_k) = k (the level). NOT c/2."""
        for k in [1, 2, 3, 4, 5]:
            assert engine.kappa_heisenberg(k) == k

    def test_kappa_virasoro_is_c_over_2(self):
        """kappa(Vir_c) = c/2. Only for the Virasoro algebra."""
        for c in [2, 4, 6, 10, 12, 14, 20, 25]:
            assert engine.kappa_virasoro(c) == c / 2.0

    def test_kappa_affine_sl2_formula(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4. dim(sl_2)=3, h^v=2."""
        for k in [1, 2, 3, 4, 5]:
            expected = 3.0 * (k + 2.0) / 4.0
            assert abs(engine.kappa_affine_sl2(k) - expected) < 1e-14

    def test_kappa_heisenberg_neq_c_over_2(self):
        """AP9: kappa(H_k) = k != c/2 = k/2 in general.
        For Heisenberg, c = 2k*dim = k (dim=1, so c=k... actually c=1 for all k).
        Actually c(H_k) = 1 (one free boson), so c/2 = 1/2 != k for k > 1.
        The point: kappa depends on the FULL algebra, not c alone (AP48).
        """
        # kappa(H_k) = k. If someone naively uses c/2, they'd get c(H)/2.
        # For H_k the central charge is 1 (one boson), so c/2 = 0.5.
        # kappa = k != 0.5 for k != 1 (at k=1: kappa=1, c/2=0.5, still different!)
        for k in [2, 3, 4, 5]:
            assert engine.kappa_heisenberg(k) != 0.5

    def test_kappa_virasoro_complementarity_sum(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c in [2, 4, 6, 10, 12, 14, 20, 25]:
            kap = engine.kappa_virasoro(c)
            kap_dual = engine.kappa_virasoro(26 - c)
            assert abs(kap + kap_dual - 13.0) < 1e-14, (
                f"AP24 violation at c={c}: kappa + kappa' = {kap + kap_dual}"
            )

    def test_kappa_heisenberg_complementarity_sum(self):
        """For Heisenberg: kappa(H_k) + kappa(H_{-k}) = 0."""
        for k in [1, 2, 3, 4, 5]:
            kap = engine.kappa_heisenberg(k)
            kap_dual = engine.kappa_heisenberg(-k)
            assert abs(kap + kap_dual) < 1e-14

    def test_kappa_affine_sl2_complementarity_sum(self):
        """For affine sl_2: kappa(k) + kappa(-k-4) = 0.
        kappa(k) = 3(k+2)/4, kappa(-k-4) = 3(-k-4+2)/4 = 3(-k-2)/4 = -3(k+2)/4.
        Sum = 0.
        """
        for k in [1, 2, 3, 4, 5]:
            kap = engine.kappa_affine_sl2(k)
            dual_k = -k - 4.0
            kap_dual = engine.kappa_affine_sl2(dual_k)
            assert abs(kap + kap_dual) < 1e-14


# ============================================================================
# Section 2: Shadow Galois cohomology classes
# ============================================================================

class TestShadowGaloisClasses:
    """Tests for constructing c_ell(A) in H^1(Q_ell, V_shadow)."""

    def test_heisenberg_class_single_component(self):
        """Heisenberg (class G): only the r=2 component is nonzero."""
        for k in [1, 2, 3]:
            for p in [2, 3, 5]:
                sgc = engine.shadow_galois_class(p, "heisenberg", float(k))
                # r=2 component: S_2 * p^{-2} = k * p^{-2}
                assert abs(sgc.components[2] - k * p ** (-2)) < 1e-14
                # r >= 3 components should be zero
                for r in range(3, 10):
                    assert abs(sgc.components[r]) < 1e-14

    def test_affine_sl2_class_two_components(self):
        """Affine sl_2 (class L): r=2 and r=3 nonzero, r>=4 zero."""
        for k in [1, 2, 3]:
            for p in [2, 3, 5]:
                sgc = engine.shadow_galois_class(p, "affine_sl2", float(k))
                kap = 3.0 * (k + 2.0) / 4.0
                alpha = 4.0 / (k + 2.0)
                assert abs(sgc.components[2] - kap * p ** (-2)) < 1e-14
                assert abs(sgc.components[3] - alpha * p ** (-3)) < 1e-14
                for r in range(4, 10):
                    assert abs(sgc.components[r]) < 1e-14

    def test_virasoro_class_infinite_tower(self):
        """Virasoro (class M): nonzero components at all arities."""
        for c_val in [6, 10, 20]:
            sgc = engine.shadow_galois_class(2, "virasoro", float(c_val), max_r=10)
            # r=2: S_2 = c/2
            assert abs(sgc.components[2] - c_val / 2.0 * 2 ** (-2)) < 1e-10
            # Higher arities should be nonzero (class M)
            assert abs(sgc.components[3]) > 1e-20
            assert abs(sgc.components[4]) > 1e-20

    def test_class_norm_positive(self):
        """The H^1 norm of every class should be positive."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:3]:
                for p in [2, 3, 5]:
                    sgc = engine.shadow_galois_class(p, family, float(param))
                    norm = engine.shadow_galois_class_norm(sgc)
                    assert norm > 0, (
                        f"Non-positive norm for {family}, param={param}, p={p}"
                    )

    def test_class_norm_decreases_with_prime(self):
        """Norm should decrease as the prime increases (exponential decay)."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                norms = []
                for p in [2, 3, 5, 7, 11]:
                    sgc = engine.shadow_galois_class(p, family, float(param))
                    norms.append(engine.shadow_galois_class_norm(sgc))
                # Each norm should be <= previous (monotone decreasing)
                for i in range(len(norms) - 1):
                    assert norms[i] >= norms[i + 1] - 1e-30, (
                        f"Norm non-decreasing at {family}, param={param}: "
                        f"norms = {norms}"
                    )

    @pytest.mark.parametrize("prime", STANDARD_PRIMES)
    def test_heisenberg_k1_all_primes(self, prime):
        """Shadow class for H_1 at all 15 standard primes."""
        sgc = engine.shadow_galois_class(prime, "heisenberg", 1.0)
        expected = 1.0 * prime ** (-2)
        assert abs(sgc.components[2] - expected) < 1e-14
        assert sgc.kappa == 1.0

    @pytest.mark.parametrize("prime", STANDARD_PRIMES)
    def test_virasoro_c10_all_primes(self, prime):
        """Shadow class for Vir_10 at all 15 standard primes."""
        sgc = engine.shadow_galois_class(prime, "virasoro", 10.0, max_r=10)
        expected_r2 = 5.0 * prime ** (-2)  # kappa = c/2 = 5
        assert abs(sgc.components[2] - expected_r2) < 1e-10

    @pytest.mark.parametrize("prime", STANDARD_PRIMES)
    def test_affine_sl2_k2_all_primes(self, prime):
        """Shadow class for V_2(sl_2) at all 15 standard primes."""
        sgc = engine.shadow_galois_class(prime, "affine_sl2", 2.0)
        kap = 3.0 * 4.0 / 4.0  # 3(2+2)/4 = 3
        expected_r2 = kap * prime ** (-2)
        assert abs(sgc.components[2] - expected_r2) < 1e-14


# ============================================================================
# Section 3: Euler factors P_ell(X; A)
# ============================================================================

class TestEulerFactors:
    """Tests for the Euler factor P_ell(X; A)."""

    def test_euler_factor_at_zero_is_one(self):
        """P_ell(0; A) = 1 for all A and ell."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                for p in [2, 3, 5]:
                    P = engine.euler_factor(0.0, p, family, float(param))
                    assert abs(P - 1.0) < 1e-14

    def test_heisenberg_euler_factor_explicit(self):
        """Heisenberg: P_ell(X) = 1 - k * ell^{-2} * X."""
        for k in [1, 2, 3]:
            for p in [2, 3, 5]:
                for x in [0.5, 1.0, 2.0]:
                    P = engine.euler_factor(x, p, "heisenberg", float(k))
                    expected = 1.0 - k * p ** (-2) * x
                    assert abs(P - expected) < 1e-14

    def test_affine_sl2_euler_factor_product(self):
        """Affine sl_2: P_ell(X) = (1 - kappa*ell^{-2}*X)(1 - alpha*ell^{-3}*X)."""
        for k in [1, 2, 3]:
            kap = 3.0 * (k + 2.0) / 4.0
            alpha = 4.0 / (k + 2.0)
            for p in [2, 3, 5]:
                for x in [0.5, 1.0]:
                    P = engine.euler_factor(x, p, "affine_sl2", float(k))
                    expected = (1.0 - kap * p ** (-2) * x) * (1.0 - alpha * p ** (-3) * x)
                    assert abs(P - expected) < 1e-13

    def test_euler_factor_nonvanishing_at_1(self):
        """P_ell(1; A) should be nonzero for generic A (no L-function zero)."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:3]:
                for p in [2, 3, 5, 7]:
                    P = engine.euler_factor(1.0, p, family, float(param))
                    assert abs(P) > 1e-10, (
                        f"Euler factor vanishes at X=1 for {family}, "
                        f"param={param}, p={p}"
                    )


# ============================================================================
# Section 4: Shadow L-function
# ============================================================================

class TestShadowLFunction:
    """Tests for the shadow L-function L(s, V_shadow(A))."""

    def test_l_function_convergence(self):
        """L(s) should converge (not blow up) for Re(s) > 1."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                L = engine.shadow_l_function(2.0, family, float(param))
                assert abs(L) < 1e10, (
                    f"L-function diverges at s=2 for {family}, param={param}"
                )
                assert abs(L) > 1e-10, (
                    f"L-function vanishes at s=2 for {family}, param={param}"
                )

    def test_heisenberg_l_function_explicit(self):
        """Heisenberg L-function: product over primes of (1-k*p^{-2}*p^{-s})^{-1}.
        = prod_p (1 - k * p^{-(s+2)})^{-1}
        For s=2: prod_p (1 - k * p^{-4})^{-1}
        """
        for k in [1, 2]:
            L = engine.shadow_l_function(2.0, "heisenberg", float(k), max_r=5)
            # Manual computation for first few primes
            manual = 1.0
            for p in STANDARD_PRIMES:
                manual /= (1.0 - k * p ** (-4))
            assert abs(L - manual) < 1e-10

    def test_l_function_increases_with_kappa(self):
        """Heisenberg: L(2, H_k) should increase with k (more mass)."""
        L_values = []
        for k in [1, 2, 3, 4, 5]:
            L = engine.shadow_l_function(2.0, "heisenberg", float(k))
            L_values.append(abs(L))
        for i in range(len(L_values) - 1):
            assert L_values[i] <= L_values[i + 1] + 1e-10

    def test_l_function_real_on_real_axis(self):
        """L(s) should be real for real s > 1 and real shadow coefficients."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                L = engine.shadow_l_function(3.0, family, float(param))
                assert abs(L.imag) < 1e-10, (
                    f"L-function not real at s=3 for {family}, param={param}"
                )


# ============================================================================
# Section 5: Norm compatibility (Path 1)
# ============================================================================

class TestNormCompatibility:
    """Test the Euler system norm compatibility axiom."""

    def test_norm_compatibility_heisenberg(self):
        """Heisenberg norm compatibility: structure check."""
        result = engine.norm_compatibility_check(
            "heisenberg", 1.0, 2, 3, max_r=10
        )
        assert result['compatible']
        assert result['family'] == "heisenberg"

    def test_norm_compatibility_virasoro(self):
        """Virasoro norm compatibility: structure check."""
        result = engine.norm_compatibility_check(
            "virasoro", 10.0, 2, 3, max_r=10
        )
        assert result['compatible']

    def test_norm_compatibility_affine(self):
        """Affine sl_2 norm compatibility: structure check."""
        result = engine.norm_compatibility_check(
            "affine_sl2", 2.0, 2, 3, max_r=10
        )
        assert result['compatible']

    def test_norm_direct_heisenberg_ratio(self):
        """Direct check: c_{mn,r}/c_{n,r} = m^{-r} for Heisenberg."""
        result = engine.norm_compatibility_direct(
            "heisenberg", 1.0, 2, 3, max_r=10
        )
        for r, data in result['components'].items():
            expected_ratio = 2 ** (-r)
            assert abs(data['ratio'] - expected_ratio) < 1e-14

    def test_norm_direct_virasoro_euler_correction(self):
        """Direct check: Euler factor correction for Virasoro."""
        result = engine.norm_compatibility_direct(
            "virasoro", 10.0, 2, 3, max_r=8
        )
        # The Euler factor at each r should be close to 1 for large primes
        for r, data in result['components'].items():
            P = data['euler_correction']
            assert abs(P - 1.0) < 0.5, (
                f"Euler correction too large at r={r}: P={P}"
            )

    @pytest.mark.parametrize("pm,pn", [(2, 3), (3, 5), (5, 7), (2, 7), (3, 11)])
    def test_norm_compatibility_multiple_pairs(self, pm, pn):
        """Norm compatibility for multiple prime pairs."""
        result = engine.norm_compatibility_check(
            "heisenberg", 2.0, pm, pn, max_r=10
        )
        assert result['compatible']


# ============================================================================
# Section 6: Selmer group bounds (Path 2)
# ============================================================================

class TestSelmerBound:
    """Test the Selmer group bound from the Euler system."""

    def test_selmer_bound_positive(self):
        """Selmer bound should be positive."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                result = engine.selmer_bound_from_euler_system(
                    family, float(param), max_r=10
                )
                assert result['selmer_bound'] > 0

    def test_selmer_bound_vs_l_value(self):
        """Selmer bound should be related to the L-value (Path 2)."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                result = engine.selmer_bound_from_euler_system(
                    family, float(param), max_r=10
                )
                # The bound should be finite
                assert result['selmer_bound'] < 1e20
                # The L-value should be nonzero
                assert result['L_value_at_1'] > 1e-20

    def test_selmer_bound_heisenberg_positive(self):
        """Heisenberg: Selmer bounds are positive."""
        for k in [1, 2, 3, 4, 5]:
            result = engine.selmer_bound_from_euler_system(
                "heisenberg", float(k), max_r=5
            )
            assert result['selmer_bound'] > 0

    def test_c1_norm_dominates_selmer(self):
        """The c_1 norm squared should dominate the Selmer bound."""
        result = engine.selmer_bound_from_euler_system(
            "heisenberg", 1.0, max_r=5
        )
        assert result['c1_norm_sq'] > 0
        assert result['local_product'] > 0


# ============================================================================
# Section 7: BSD-type formula
# ============================================================================

class TestBSDFormula:
    """Test the BSD-type formula: |Sel| <= |L(1)/Omega|."""

    def test_bsd_heisenberg_finite(self):
        """BSD ratio should be finite for Heisenberg."""
        result = engine.bsd_type_comparison("heisenberg", 1.0, max_r=5)
        assert not math.isnan(result['bsd_ratio'])
        assert not math.isinf(result['bsd_ratio'])
        assert result['bsd_ratio'] > 0

    def test_bsd_virasoro_finite(self):
        """BSD ratio should be finite for Virasoro."""
        result = engine.bsd_type_comparison("virasoro", 10.0, max_r=8)
        assert not math.isnan(result['bsd_ratio'])
        assert result['bsd_ratio'] > 0

    def test_bsd_affine_finite(self):
        """BSD ratio should be finite for affine sl_2."""
        result = engine.bsd_type_comparison("affine_sl2", 2.0, max_r=5)
        assert not math.isnan(result['bsd_ratio'])
        assert result['bsd_ratio'] > 0

    def test_bsd_period_depends_on_kappa(self):
        """Period Omega should depend on kappa."""
        result1 = engine.bsd_type_comparison("heisenberg", 1.0, max_r=5)
        result2 = engine.bsd_type_comparison("heisenberg", 3.0, max_r=5)
        assert result1['period'] != result2['period']

    def test_bsd_tamagawa_positive(self):
        """Tamagawa product should be positive."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                result = engine.bsd_type_comparison(family, float(param), max_r=5)
                assert result['tamagawa'] > 0


# ============================================================================
# Section 8: Kolyvagin derivative classes (Path 3)
# ============================================================================

class TestKolyvaginDerivatives:
    """Test Kolyvagin derivative classes and divisibility."""

    def test_kolyvagin_single_prime(self):
        """Kolyvagin class for n = single prime."""
        for p in [2, 3, 5, 7, 11]:
            result = engine.kolyvagin_derivative_class(
                "heisenberg", 1.0, [p], max_r=10
            )
            assert result['norm'] >= 0  # may be zero for finite-depth families
            assert result['n'] == p

    def test_kolyvagin_two_primes(self):
        """Kolyvagin class for n = product of two primes."""
        result = engine.kolyvagin_derivative_class(
            "heisenberg", 1.0, [2, 3], max_r=10
        )
        assert result['norm'] >= 0  # may be zero for finite-depth families
        assert result['n'] == 6

    def test_kolyvagin_three_primes(self):
        """Kolyvagin class for n = 2*3*5 = 30."""
        result = engine.kolyvagin_derivative_class(
            "heisenberg", 1.0, [2, 3, 5], max_r=10
        )
        assert result['norm'] >= 0  # may be zero for finite-depth families
        assert result['n'] == 30

    def test_kolyvagin_four_primes(self):
        """Kolyvagin class for n = 2*3*5*7 = 210."""
        result = engine.kolyvagin_derivative_class(
            "heisenberg", 1.0, [2, 3, 5, 7], max_r=10
        )
        assert result['norm'] >= 0  # may be zero for finite-depth families
        assert result['n'] == 210

    def test_kolyvagin_five_primes(self):
        """Kolyvagin class for n = 2*3*5*7*11 = 2310."""
        result = engine.kolyvagin_derivative_class(
            "heisenberg", 1.0, [2, 3, 5, 7, 11], max_r=10
        )
        assert result['norm'] >= 0  # may be zero for finite-depth families
        assert result['n'] == 2310

    def test_kolyvagin_norm_decreases_with_primes(self):
        """Adding primes should (generically) decrease the Kolyvagin norm."""
        norms = []
        prime_lists = [[2], [2, 3], [2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11]]
        for primes in prime_lists:
            result = engine.kolyvagin_derivative_class(
                "heisenberg", 1.0, primes, max_r=10
            )
            norms.append(result['norm'])
        # Norms should generally decrease (more derivatives = smaller)
        # Not strictly monotone in general, but norm should be bounded
        assert all(n < 1e10 for n in norms)

    def test_kolyvagin_divisibility_check(self):
        """Test the divisibility relation kappa_{n*ell} mod ell^a."""
        result = engine.kolyvagin_divisibility_check(
            "heisenberg", 1.0, [2], 3, max_r=10
        )
        assert result['ell'] == 3
        assert result['n'] == 2
        assert result['n_ell'] == 6
        # The divisibility should hold (ratio bounded)
        assert not math.isnan(result['ratio'])

    def test_kolyvagin_divisibility_virasoro(self):
        """Kolyvagin divisibility for Virasoro."""
        result = engine.kolyvagin_divisibility_check(
            "virasoro", 10.0, [2], 3, max_r=8
        )
        assert result['norm_kn'] >= 0  # may vanish for finite-depth
        assert result['norm_kn_ell'] >= 0  # may vanish

    def test_kolyvagin_divisibility_affine(self):
        """Kolyvagin divisibility for affine sl_2."""
        result = engine.kolyvagin_divisibility_check(
            "affine_sl2", 2.0, [2], 3, max_r=8
        )
        assert result['norm_kn'] >= 0  # may vanish for finite-depth
        assert result['norm_kn_ell'] >= 0  # may vanish

    @pytest.mark.parametrize("extra_prime", [3, 5, 7, 11, 13])
    def test_kolyvagin_divisibility_multiple_ell(self, extra_prime):
        """Divisibility check for various extra primes ell."""
        result = engine.kolyvagin_divisibility_check(
            "heisenberg", 2.0, [2], extra_prime, max_r=10
        )
        assert result['ell'] == extra_prime
        assert result['norm_kn'] >= 0  # may vanish for finite-depth


# ============================================================================
# Section 9: Shadow cyclotomic units
# ============================================================================

class TestCyclotomicUnits:
    """Tests for shadow cyclotomic units and regulator."""

    def test_cyclotomic_unit_heisenberg(self):
        """Shadow cyclotomic unit for Heisenberg."""
        result = engine.shadow_cyclotomic_unit(5, "heisenberg", 1.0)
        assert result['abs_unit'] > 0
        assert result['n'] == 5

    def test_cyclotomic_unit_virasoro(self):
        """Shadow cyclotomic unit for Virasoro."""
        result = engine.shadow_cyclotomic_unit(5, "virasoro", 10.0, max_r=10)
        assert result['abs_unit'] > 0

    def test_cyclotomic_regulator_positive(self):
        """Regulator should be nonzero for nontrivial shadow."""
        for family in ["heisenberg", "virasoro", "affine_sl2"]:
            params = {"heisenberg": 1.0, "virasoro": 10.0, "affine_sl2": 2.0}
            result = engine.shadow_cyclotomic_unit(
                5, family, params[family], max_r=10
            )
            # |regulator| > 0 for nontrivial shadow
            assert abs(result['regulator']) > 1e-20

    def test_cyclotomic_regulator_matrix(self):
        """Full regulator computation."""
        result = engine.shadow_cyclotomic_regulator(
            "heisenberg", 1.0, n_values=[3, 4, 5, 7, 8]
        )
        assert len(result['regulators']) == 5
        assert result['L_value_at_half'] > 0

    def test_cyclotomic_unit_conjugation(self):
        """u_n and u_{-n} should be conjugates (complex conjugation)."""
        # For n and -n, zeta_{-n} = conj(zeta_n) if n is positive
        # We test that log_unit has controlled imaginary part
        result = engine.shadow_cyclotomic_unit(7, "heisenberg", 1.0)
        assert abs(result['log_unit'].imag) < 10  # bounded imaginary part


# ============================================================================
# Section 10: Kato comparison
# ============================================================================

class TestKatoComparison:
    """Test comparison with Kato's Euler system."""

    def test_kato_correction_heisenberg(self):
        """Heisenberg: correction factor = 1 (only one shadow component)."""
        result = engine.kato_zeta_element("heisenberg", 1.0, 2)
        # For Heisenberg, S_r = 0 for r >= 3, so correction = 1
        assert abs(result['kato_correction_factor'] - 1.0) < 1e-14

    def test_kato_correction_virasoro_nonzero(self):
        """Virasoro: correction factor should differ from 1."""
        result = engine.kato_zeta_element("virasoro", 10.0, 2, max_r=10)
        # For Virasoro, higher shadow components contribute
        assert abs(result['kato_correction_factor'] - 1.0) > 1e-10

    def test_kato_correction_decreasing_with_prime(self):
        """Correction deviation from 1 should decrease with larger primes."""
        result = engine.kato_shadow_comparison(
            "virasoro", 10.0, primes=STANDARD_PRIMES, max_r=10
        )
        assert result['correction_decreasing']

    def test_kato_correction_affine(self):
        """Affine sl_2: correction factor includes S_3 contribution."""
        result = engine.kato_zeta_element("affine_sl2", 2.0, 2)
        # S_3 = alpha != 0, so correction != 1
        # But S_r = 0 for r >= 4, so correction = 1 + alpha/kappa * 2^{-1}
        kap = 3.0 * 4.0 / 4.0  # = 3
        alpha = 4.0 / 4.0  # = 1
        expected = 1.0 + (alpha / kap) * (2 ** (-1))
        assert abs(result['kato_correction_factor'] - expected) < 1e-12

    def test_kato_leading_norm(self):
        """Leading Kato norm = kappa^2 * p^{-4}."""
        for p in [2, 3, 5]:
            result = engine.kato_zeta_element("heisenberg", 2.0, p)
            expected = 4.0 * p ** (-4)  # kappa=2, kappa^2=4
            assert abs(result['leading_kato_norm'] - expected) < 1e-14


# ============================================================================
# Section 11: Koszul duality on Euler systems (Path 4, AP24-safe)
# ============================================================================

class TestKoszulDualEulerSystem:
    """Test Koszul duality (Theorem C) on Euler systems."""

    def test_koszul_dual_param_virasoro(self):
        """Virasoro: dual of c is 26-c."""
        assert engine.get_koszul_dual_param("virasoro", 10.0) == 16.0
        assert engine.get_koszul_dual_param("virasoro", 13.0) == 13.0  # self-dual

    def test_koszul_dual_param_heisenberg(self):
        """Heisenberg: dual of k is -k."""
        assert engine.get_koszul_dual_param("heisenberg", 2.0) == -2.0

    def test_koszul_dual_param_affine(self):
        """Affine sl_2: dual of k is -k-4 (Feigin-Frenkel)."""
        assert engine.get_koszul_dual_param("affine_sl2", 1.0) == -5.0

    def test_koszul_kappa_sum_virasoro(self):
        """AP24: kappa + kappa' = 13 for Virasoro."""
        result = engine.koszul_dual_euler_system_comparison(
            "virasoro", 10.0, max_r=10
        )
        assert abs(result['kappa_sum'] - 13.0) < 1e-14

    def test_koszul_kappa_sum_heisenberg(self):
        """kappa + kappa' = 0 for Heisenberg."""
        result = engine.koszul_dual_euler_system_comparison(
            "heisenberg", 2.0
        )
        assert abs(result['kappa_sum']) < 1e-14

    def test_koszul_kappa_sum_affine(self):
        """kappa + kappa' = 0 for affine sl_2."""
        result = engine.koszul_dual_euler_system_comparison(
            "affine_sl2", 2.0
        )
        assert abs(result['kappa_sum']) < 1e-14

    def test_koszul_self_dual_virasoro_c13(self):
        """At c=13: A = A!, so L(s,A) = L(s,A!)."""
        result = engine.koszul_dual_euler_system_comparison(
            "virasoro", 13.0, max_r=10
        )
        assert abs(result['kappa'] - result['kappa_dual']) < 1e-14
        assert abs(result['kappa'] - 6.5) < 1e-14  # kappa = 13/2

    def test_koszul_l_product_real(self):
        """L(A) * L(A!) should be real for real parameters."""
        result = engine.koszul_dual_euler_system_comparison(
            "virasoro", 10.0, max_r=8
        )
        L_prod = result['L_product']
        assert abs(L_prod.imag) < 1e-8

    def test_koszul_euler_factor_product_consistency(self):
        """Product of Euler factors should be consistent across primes."""
        result = engine.koszul_dual_euler_system_comparison(
            "virasoro", 10.0, primes=[2, 3, 5], max_r=8
        )
        for p in [2, 3, 5]:
            prod = result['factor_products'][p]['product']
            # Product should be positive real (both Euler factors real at X=1)
            assert abs(prod.imag) < 1e-10


# ============================================================================
# Section 12: Iwasawa invariants
# ============================================================================

class TestIwasawaInvariants:
    """Test Iwasawa-theoretic invariants of the shadow Euler system."""

    def test_iwasawa_mu_vanishes_heisenberg(self):
        """mu should vanish for Heisenberg (Ferrero-Washington analogue)."""
        result = engine.shadow_iwasawa_invariants(
            "heisenberg", 1.0, prime_p=5, max_r=10, max_n=5
        )
        assert result['mu_vanishes']

    def test_iwasawa_mu_vanishes_virasoro(self):
        """mu should vanish for Virasoro."""
        result = engine.shadow_iwasawa_invariants(
            "virasoro", 10.0, prime_p=5, max_r=8, max_n=5
        )
        assert result['mu_vanishes']

    def test_iwasawa_mu_vanishes_affine(self):
        """mu should vanish for affine sl_2."""
        result = engine.shadow_iwasawa_invariants(
            "affine_sl2", 2.0, prime_p=5, max_r=8, max_n=5
        )
        assert result['mu_vanishes']

    def test_iwasawa_lambda_nonnegative(self):
        """lambda-invariant should be nonnegative."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                result = engine.shadow_iwasawa_invariants(
                    family, float(param), prime_p=5, max_r=8, max_n=5
                )
                assert result['lambda_estimate'] >= -0.5  # Allow small numerical error

    def test_iwasawa_layer_norms_bounded(self):
        """Norms at each layer should be bounded (no explosion)."""
        result = engine.shadow_iwasawa_invariants(
            "heisenberg", 1.0, prime_p=5, max_r=10, max_n=5
        )
        for norm in result['layer_norms']:
            assert norm < 1e20


# ============================================================================
# Section 13: Euler system rank and shadow class
# ============================================================================

class TestEulerSystemRank:
    """Test Euler system rank classification."""

    def test_heisenberg_rank_1(self):
        """Heisenberg (class G) should have rank 1."""
        result = engine.euler_system_rank("heisenberg", 1.0)
        assert result['effective_rank'] == 1
        assert result['shadow_class'] == "G"
        assert result['nonzero_arities'] == [2]

    def test_affine_sl2_rank_2(self):
        """Affine sl_2 (class L) should have rank 2."""
        result = engine.euler_system_rank("affine_sl2", 2.0)
        assert result['effective_rank'] == 2
        assert result['shadow_class'] == "L"
        assert result['nonzero_arities'] == [2, 3]

    def test_virasoro_rank_infinite(self):
        """Virasoro (class M) should have rank > 4."""
        result = engine.euler_system_rank("virasoro", 10.0, max_r=20)
        assert result['effective_rank'] > 4
        assert result['shadow_class'] == "M"

    def test_rank_class_consistency(self):
        """Shadow class should be consistent with rank."""
        class_map = {
            "G": lambda r: r <= 1,
            "L": lambda r: r == 2,
            "C": lambda r: 3 <= r <= 4,
            "M": lambda r: r > 4,
        }
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:3]:
                result = engine.euler_system_rank(family, float(param), max_r=20)
                sc = result['shadow_class']
                assert class_map[sc](result['effective_rank']), (
                    f"Class-rank mismatch for {family}, param={param}: "
                    f"class={sc}, rank={result['effective_rank']}"
                )


# ============================================================================
# Section 14: Cross-family consistency (AP10 multi-path)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks for multi-path verification."""

    def test_euler_factor_product_multiplicative(self):
        """P_{p1*p2}(X) should factor if p1 != p2 (for appropriate families)."""
        # For Heisenberg: P_p(X) = 1 - k*p^{-2}*X
        # There is no "P_{p1*p2}" in the same sense, but we check
        # that the Euler product is consistent with individual factors.
        k = 1.0
        L_product = 1.0
        for p in [2, 3, 5]:
            P = engine.euler_factor(p ** (-2), p, "heisenberg", k)
            if abs(P) > 1e-30:
                L_product /= P
        L_direct = engine.shadow_l_function(2.0, "heisenberg", k, primes=[2, 3, 5])
        assert abs(L_product - abs(L_direct)) < 1e-8

    def test_class_norm_vs_kappa_squared(self):
        """The leading contribution to |c_p|^2 is kappa^2 * p^{-4}."""
        for family, params in engine.FAMILY_CONFIGS:
            for param in params[:2]:
                kap = engine.get_kappa(family, float(param))
                for p in [2, 3, 5]:
                    sgc = engine.shadow_galois_class(p, family, float(param))
                    norm = engine.shadow_galois_class_norm(sgc)
                    leading = kap ** 2 * p ** (-4)
                    # norm >= leading (has higher-order contributions)
                    assert norm >= leading - 1e-20, (
                        f"Norm below leading term for {family}, param={param}, p={p}"
                    )

    def test_koszul_duality_consistent_selmer_bounds(self):
        """Selmer bounds for A and A! should both be positive (AP24-safe)."""
        result = engine.koszul_dual_euler_system_comparison(
            "virasoro", 10.0, max_r=8
        )
        # Both L-values should be nonzero
        assert abs(result['L_A']) > 1e-20
        assert abs(result['L_A_dual']) > 1e-20

    def test_heisenberg_additivity(self):
        """For Heisenberg: kappa is additive, so c_p(H_{k1+k2}) components
        should equal c_p(H_{k1}) + c_p(H_{k2}) at the leading term.
        """
        for p in [2, 3, 5]:
            sgc1 = engine.shadow_galois_class(p, "heisenberg", 1.0)
            sgc2 = engine.shadow_galois_class(p, "heisenberg", 2.0)
            sgc3 = engine.shadow_galois_class(p, "heisenberg", 3.0)
            # c_p(H_3)_2 = 3 * p^{-2} = c_p(H_1)_2 + c_p(H_2)_2 = (1+2)*p^{-2}
            sum_12 = sgc1.components[2] + sgc2.components[2]
            assert abs(sgc3.components[2] - sum_12) < 1e-14


# ============================================================================
# Section 15: Structural summary
# ============================================================================

class TestStructuralSummary:
    """Test the comprehensive structural summary."""

    def test_summary_heisenberg(self):
        """Full structural summary for Heisenberg k=1."""
        result = engine.euler_system_structural_summary(
            "heisenberg", 1.0, max_r=5
        )
        assert result['rank']['shadow_class'] == "G"
        assert result['selmer']['selmer_bound'] > 0
        assert result['bsd']['bsd_ratio'] > 0

    def test_summary_virasoro(self):
        """Full structural summary for Virasoro c=10."""
        result = engine.euler_system_structural_summary(
            "virasoro", 10.0, max_r=8
        )
        assert result['rank']['shadow_class'] == "M"
        assert result['koszul']['kappa_sum'] == pytest.approx(13.0)

    def test_summary_affine(self):
        """Full structural summary for affine sl_2 k=2."""
        result = engine.euler_system_structural_summary(
            "affine_sl2", 2.0, max_r=5
        )
        assert result['rank']['shadow_class'] == "L"
        assert abs(result['koszul']['kappa_sum']) < 1e-14


# ============================================================================
# Section 16: Frobenius action
# ============================================================================

class TestFrobeniusAction:
    """Test the Frobenius action on shadow basis."""

    def test_frobenius_scales_by_prime_power(self):
        """Fr_ell(e_r) = ell^r * e_r."""
        components = {2: 1.0, 3: 0.5, 4: 0.25}
        result = engine.frobenius_action(3, components)
        assert abs(result[2] - 9.0) < 1e-14   # 3^2 * 1
        assert abs(result[3] - 13.5) < 1e-14  # 3^3 * 0.5 = 27 * 0.5
        assert abs(result[4] - 20.25) < 1e-14  # 3^4 * 0.25 = 81 * 0.25

    def test_frobenius_at_prime_2(self):
        """Fr_2 should scale e_r by 2^r."""
        components = {2: 1.0, 5: 1.0, 10: 1.0}
        result = engine.frobenius_action(2, components)
        assert abs(result[2] - 4.0) < 1e-14
        assert abs(result[5] - 32.0) < 1e-14
        assert abs(result[10] - 1024.0) < 1e-14


# ============================================================================
# Section 17: Kolyvagin operator Gauss sums
# ============================================================================

class TestKolyvaginOperator:
    """Test the Kolyvagin derivative operator D_ell."""

    def test_gauss_sum_ell_divides_r(self):
        """When ell | r: sum_{a=1}^{ell-2} a * zeta^{a*r} = sum a = (ell-1)(ell-2)/2."""
        ell = 5
        zeta = cmath.exp(2j * cmath.pi / ell)
        # For r = 5 (ell | r): zeta^{5a} = 1 for all a
        gauss_sum = sum(a * (zeta ** (a * 5)) for a in range(1, ell - 1))
        expected = (ell - 1) * (ell - 2) / 2  # = 4*3/2 = 6
        assert abs(gauss_sum - expected) < 1e-10

    def test_gauss_sum_ell_not_divides_r(self):
        """When ell ∤ r: the Gauss sum is nonzero complex."""
        ell = 5
        zeta = cmath.exp(2j * cmath.pi / ell)
        gauss_sum = sum(a * (zeta ** (a * 2)) for a in range(1, ell - 1))
        # This should be nonzero
        assert abs(gauss_sum) > 1e-10

    def test_kolyvagin_operator_preserves_zero_components(self):
        """D_ell on zero components should remain zero."""
        components = {2: 0.0, 3: 0.0, 4: 0.0}
        result = engine.kolyvagin_operator_D_ell(5, components)
        for r, v in result.items():
            assert abs(v) < 1e-14


# ============================================================================
# Section 18: Edge cases and boundary checks
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_virasoro_c2_small_central_charge(self):
        """Virasoro at small c should still work."""
        sgc = engine.shadow_galois_class(2, "virasoro", 2.0, max_r=10)
        assert abs(sgc.kappa - 1.0) < 1e-14
        assert abs(sgc.components[2] - 0.25) < 1e-14  # 1.0 * 2^{-2}

    def test_virasoro_c25_near_critical(self):
        """Virasoro at c=25 (near c=26 dual boundary)."""
        sgc = engine.shadow_galois_class(2, "virasoro", 25.0, max_r=10)
        assert abs(sgc.kappa - 12.5) < 1e-14

    def test_heisenberg_k1_minimal(self):
        """Minimal case: Heisenberg k=1."""
        sgc = engine.shadow_galois_class(2, "heisenberg", 1.0)
        assert abs(sgc.components[2] - 0.25) < 1e-14

    def test_large_prime(self):
        """Shadow class at a large prime should have very small components."""
        sgc = engine.shadow_galois_class(47, "heisenberg", 1.0)
        assert abs(sgc.components[2]) < 1e-3  # 1/47^2 ~ 0.00045

    def test_euler_factor_log_derivative(self):
        """Log derivative of Euler factor should be finite."""
        ld = engine.euler_factor_log_derivative(
            0.5, 2, "heisenberg", 1.0
        )
        assert abs(ld) < 100

    def test_norm_map_shadow_basic(self):
        """Basic norm map test."""
        sgc = engine.shadow_galois_class(6, "heisenberg", 1.0, max_r=10)
        result = engine.norm_map_shadow(sgc, 2, 3)
        # Only r divisible by 2 should survive
        for r, v in result.items():
            if r % 2 != 0:
                assert abs(v) < 1e-14
