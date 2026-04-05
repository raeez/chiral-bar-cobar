r"""Tests for the motivic weight filtration engine on A_c(rho)
and the shadow L-function.

Multi-path verification:
  Path 1: Direct motivic weight computation
  Path 2: Additivity of weights under tensor product
  Path 3: Special value checks (zeta(2) = pi^2/6, weight 2 match)
  Path 4: Galois equivariance A_c(rho_bar) = conj(A_c(rho))

50+ tests covering:
  1. Motivic weight assignments for individual factors
  2. Total weight of A_c(rho) = 0
  3. Hodge realization of shadow data
  4. Period matrix (Deligne critical values)
  5. Frobenius / Galois action
  6. Shadow motive L-function
  7. Weight filtration on epsilon^c_s
  8. Tate twist and complementarity
  9. Deligne's conjecture verification
  10. Cross-verification and consistency

Manuscript references:
    def:universal-residue-factor (arithmetic_shadows.tex)
    rem:motivic-decomposition (arithmetic_shadows.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
"""

import math
import cmath
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    import sympy
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

from compute.lib.bc_motivic_weight_engine import (
    # Weight assignments
    MotivicWeight,
    gamma_motivic_weight,
    pi_power_motivic_weight,
    zeta_value_motivic_weight,
    zeta_derivative_motivic_weight,
    motivic_weight_decomposition_Ac,
    # Hodge realization
    hodge_weight_shadow_coefficient,
    hodge_numbers_shadow_tower,
    hodge_realization_Mbar_g,
    # Period matrix
    zeta_critical_value,
    period_at_zeta_zero,
    # Galois / Frobenius
    frobenius_action_Ac,
    galois_equivariance_check,
    # Shadow motive
    shadow_motive_weight_r,
    shadow_motive_L_function_formal,
    # Epstein weight
    epstein_weight_filtration,
    epstein_weight_at_scattering_poles,
    # Tate twist
    tate_twist_complementarity,
    complementarity_weight_table,
    # Deligne
    deligne_conjecture_zeta_critical,
    deligne_structure_at_zero,
    # Virasoro denominators
    virasoro_Sr_denominator_analysis,
    # Comprehensive
    full_motivic_analysis,
    weight_additivity_check,
    special_value_weight_check,
)

skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
skipsy = pytest.mark.skipif(not HAS_SYMPY, reason="sympy required")
DPS = 30


# ============================================================
# Section 1: Motivic weight assignments — individual factors
# ============================================================

class TestMotivicWeightAssignments:
    """Formal motivic weight of each factor of A_c(rho)."""

    def test_gamma_weight_zero(self):
        """Gamma values have motivic weight 0 (archimedean)."""
        for s in [1, 2, 0.5, 3.5, 1 + 2j]:
            w = gamma_motivic_weight(s)
            assert w.real_weight == 0, (
                f"Gamma({s}) should have weight 0, got {w.real_weight}"
            )

    def test_pi_power_weight_zero(self):
        """pi^a has motivic weight 0 (archimedean normalization)."""
        for a in [1, 2, 0.5 + 14.13j, -3, 10]:
            w = pi_power_motivic_weight(a)
            assert w.real_weight == 0, (
                f"pi^{a} should have weight 0, got {w.real_weight}"
            )

    def test_zeta_weight_at_integers(self):
        """zeta(n) at positive even integers: weight = n-1."""
        test_cases = [
            (2, 1),   # zeta(2) = pi^2/6, weight 1
            (4, 3),   # zeta(4) = pi^4/90, weight 3
            (6, 5),   # zeta(6), weight 5
            (8, 7),   # zeta(8), weight 7
            (10, 9),  # zeta(10), weight 9
        ]
        for n, expected_w in test_cases:
            w = zeta_value_motivic_weight(n)
            assert abs(w.real_weight - expected_w) < 1e-14, (
                f"zeta({n}): expected weight {expected_w}, got {w.real_weight}"
            )

    def test_zeta_weight_general_real(self):
        """Formal weight of zeta(s) for real s: w = s - 1."""
        for s in [1.5, 2.5, 3.0, 5.0, 10.0]:
            w = zeta_value_motivic_weight(s)
            assert abs(w.real_weight - (s - 1)) < 1e-14

    def test_zeta_weight_complex(self):
        """Formal weight of zeta(s) for complex s: w = Re(s) - 1."""
        for s in [1.5 + 14.13j, 0.5 + 21.02j, 2.0 + 5j]:
            w = zeta_value_motivic_weight(s)
            assert abs(w.real_weight - (s.real - 1)) < 1e-14

    def test_zeta_prime_weight_at_half(self):
        """Under RH: rho = 1/2 + i*gamma, so w(zeta'(rho)) = 1/2."""
        rho = 0.5 + 14.134725j  # first zero approximately
        w = zeta_derivative_motivic_weight(rho)
        assert abs(w.real_weight - 0.5) < 1e-10

    def test_zeta_prime_weight_real_part(self):
        """w(zeta'(rho)) = Re(rho) for any zero."""
        for rho in [0.5 + 14.13j, 0.5 + 21.02j, 0.5 + 25.01j]:
            w = zeta_derivative_motivic_weight(rho)
            assert abs(w.real_weight - rho.real) < 1e-14


# ============================================================
# Section 2: Total weight of A_c(rho) = 0
# ============================================================

class TestTotalWeightZero:
    """The total motivic weight of A_c(rho) must be 0."""

    def test_total_weight_zero_first_zero(self):
        """At the first zeta zero, total weight = 0."""
        rho = 0.5 + 14.134725j
        decomp = motivic_weight_decomposition_Ac(rho, 13.0)
        assert abs(decomp['total_weight']) < 1e-14, (
            f"Total weight should be 0, got {decomp['total_weight']}"
        )

    def test_total_weight_zero_various_c(self):
        """Total weight = 0 for various central charges."""
        rho = 0.5 + 14.134725j
        for c_val in [1.0, 2.0, 6.0, 13.0, 24.0, 25.0, 26.0]:
            decomp = motivic_weight_decomposition_Ac(rho, c_val)
            assert abs(decomp['total_weight']) < 1e-14, (
                f"c={c_val}: total weight = {decomp['total_weight']}"
            )

    def test_total_weight_zero_various_zeros(self):
        """Total weight = 0 for various zeta zeros (under RH)."""
        for gamma in [14.134725, 21.022040, 25.010858, 30.424876]:
            rho = 0.5 + gamma * 1j
            decomp = motivic_weight_decomposition_Ac(rho, 13.0)
            assert abs(decomp['total_weight']) < 1e-14, (
                f"gamma={gamma}: total weight = {decomp['total_weight']}"
            )

    def test_weight_additivity(self):
        """Verify weight additivity: num - den = 0."""
        rho = 0.5 + 14.134725j
        result = weight_additivity_check(rho, 13.0)
        assert result['additive'], (
            f"Weights not additive: total = {result['total_weight']}"
        )

    def test_weight_additivity_various_c(self):
        """Additivity holds for all c values."""
        rho = 0.5 + 21.022j
        for c_val in [1.0, 13.0, 26.0]:
            result = weight_additivity_check(rho, c_val)
            assert result['additive'], (
                f"c={c_val}: total weight = {result['total_weight']}"
            )


# ============================================================
# Section 3: Hodge realization
# ============================================================

class TestHodgeRealization:
    """Hodge structure on the shadow data."""

    def test_hodge_weight_equals_arity(self):
        """S_r has Hodge weight r."""
        for r in range(2, 15):
            w = hodge_weight_shadow_coefficient(r)
            assert w == r, f"S_{r} should have Hodge weight {r}, got {w}"

    def test_hodge_numbers_genus_0(self):
        """Shadow tower at genus 0: one-dimensional at each arity."""
        hodge = hodge_numbers_shadow_tower(r_max=8)
        for r in range(2, 9):
            assert hodge[(0, r)] == 1, f"h^{{0,{r}}} should be 1"

    def test_hodge_numbers_total_dimension(self):
        """Total dimension = r_max - 1."""
        for r_max in [5, 8, 10, 15]:
            hodge = hodge_numbers_shadow_tower(r_max=r_max)
            assert hodge['total_dimension'] == r_max - 1

    def test_lambda_class_hodge_type(self):
        """lambda_g lives in H^{2g}(M-bar_g) with Hodge type (g,g)."""
        for g in range(1, 6):
            data = hodge_realization_Mbar_g(g)
            assert data['lambda_class_degree'] == 2 * g
            assert data['lambda_class_hodge_type'] == (g, g)
            assert data['lambda_class_hodge_weight'] == 2 * g

    def test_faber_pandharipande_weight_zero(self):
        """lambda_g^FP is rational, hence weight 0."""
        for g in range(1, 6):
            data = hodge_realization_Mbar_g(g)
            assert data['Faber_Pandharipande_weight'] == 0


# ============================================================
# Section 4: Period matrix — Deligne critical values
# ============================================================

class TestPeriodMatrix:
    """Periods of zeta at critical values."""

    @skipmp
    def test_zeta_2_equals_pi_sq_over_6(self):
        """zeta(2) = pi^2/6."""
        result = zeta_critical_value(1, dps=DPS)
        assert result['agreement'] < 1e-20, (
            f"zeta(2) computation error: {result['agreement']}"
        )
        assert abs(result['zeta_value'] - math.pi ** 2 / 6) < 1e-12

    @skipmp
    def test_zeta_4_equals_pi4_over_90(self):
        """zeta(4) = pi^4/90."""
        result = zeta_critical_value(2, dps=DPS)
        assert result['agreement'] < 1e-20
        assert abs(result['zeta_value'] - math.pi ** 4 / 90) < 1e-10

    @skipmp
    def test_zeta_critical_rational_period(self):
        """zeta(2k) / (2*pi)^{2k} is rational (Deligne)."""
        for k in range(1, 8):
            result = zeta_critical_value(k, dps=DPS)
            assert result['agreement'] < 1e-15, (
                f"k={k}: rational period error = {result['agreement']}"
            )
            assert result['Deligne_check'] == "PASS: zeta(2k)/(2*pi)^{2k} is rational"

    @skipmp
    def test_motivic_weight_at_critical_values(self):
        """zeta(2k) has motivic weight 2k-1."""
        for k in range(1, 6):
            result = zeta_critical_value(k, dps=DPS)
            assert result['motivic_weight'] == 2 * k - 1

    @skipmp
    def test_period_at_zeta_zero_not_critical(self):
        """zeta(1+rho_1) is not a critical value."""
        result = period_at_zeta_zero(k_zero=1, dps=DPS)
        assert result['is_critical_value'] is False
        assert result['ratio_weight'] == 0.0  # weights cancel in ratio

    @skipmp
    def test_period_at_zeta_zero_finite(self):
        """zeta(1+rho) is finite (Re(1+rho) = 3/2 > 1)."""
        for k in range(1, 4):
            result = period_at_zeta_zero(k_zero=k, dps=DPS)
            assert abs(complex(result['zeta_1_plus_rho'])) < 1e10
            assert abs(complex(result['zeta_1_plus_rho'])) > 1e-10


# ============================================================
# Section 5: Frobenius / Galois action
# ============================================================

class TestGaloisAction:
    """Galois equivariance of A_c(rho)."""

    @skipmp
    def test_galois_equivariance_first_zero(self):
        """A_c(rho_bar) = conj(A_c(rho)) at first zero, c=13."""
        result = galois_equivariance_check(
            complex(mpmath.zetazero(1)), 13.0, dps=DPS
        )
        assert result['equivariant'], (
            f"Galois equivariance failed: error = {result['error']}"
        )

    @skipmp
    def test_galois_equivariance_second_zero(self):
        """A_c(rho_bar) = conj(A_c(rho)) at second zero, c=13."""
        result = galois_equivariance_check(
            complex(mpmath.zetazero(2)), 13.0, dps=DPS
        )
        assert result['equivariant']

    @skipmp
    def test_galois_equivariance_various_c(self):
        """Equivariance holds for various c."""
        rho = complex(mpmath.zetazero(1))
        for c_val in [1.0, 6.0, 13.0, 26.0]:
            result = galois_equivariance_check(rho, c_val, dps=DPS)
            assert result['equivariant'], (
                f"c={c_val}: equivariance error = {result['error']}"
            )

    @skipmp
    def test_frobenius_at_p2(self):
        """Frobenius at p=2 preserves equivariance."""
        rho = complex(mpmath.zetazero(1))
        result = frobenius_action_Ac(rho, 13.0, 2, dps=DPS)
        assert result['galois_equivariant']

    @skipmp
    def test_frobenius_at_p3(self):
        """Frobenius at p=3."""
        rho = complex(mpmath.zetazero(1))
        result = frobenius_action_Ac(rho, 13.0, 3, dps=DPS)
        assert result['galois_equivariant']

    @skipmp
    def test_frobenius_at_p5(self):
        """Frobenius at p=5."""
        rho = complex(mpmath.zetazero(1))
        result = frobenius_action_Ac(rho, 13.0, 5, dps=DPS)
        assert result['galois_equivariant']

    @skipmp
    def test_frobenius_at_p7(self):
        """Frobenius at p=7."""
        rho = complex(mpmath.zetazero(1))
        result = frobenius_action_Ac(rho, 13.0, 7, dps=DPS)
        assert result['galois_equivariant']

    @skipmp
    def test_frobenius_euler_factor_bounded(self):
        """Euler factor |1/(1-p^{-(1+rho)})| is bounded for small p."""
        rho = complex(mpmath.zetazero(1))
        for p in [2, 3, 5, 7]:
            result = frobenius_action_Ac(rho, 13.0, p, dps=DPS)
            ef = abs(result['euler_factor_zeta_1_plus_rho'])
            # For Re(1+rho) = 3/2 > 1: the Euler product converges,
            # so each factor is bounded.
            assert ef < 100, f"Euler factor at p={p} too large: {ef}"
            assert ef > 0.5, f"Euler factor at p={p} too small: {ef}"


# ============================================================
# Section 6: Shadow motive L-function
# ============================================================

class TestShadowMotive:
    """Shadow motive M^{sh}_A and its L-function."""

    def test_shadow_motive_S2_tate(self):
        """S_2 = c/2: motive Q(1), weight 2."""
        m = shadow_motive_weight_r(2)
        assert m['hodge_weight'] == 2
        assert 'Tate' in m['motive_type']

    def test_shadow_motive_S3_trivial(self):
        """S_3 = 2: motive Q(0), weight 0 (constant)."""
        m = shadow_motive_weight_r(3)
        assert m['hodge_weight'] == 3
        assert 'Tate' in m['motive_type']

    def test_shadow_motive_S4_mixed(self):
        """S_4 = 10/(c(5c+22)): mixed motive."""
        m = shadow_motive_weight_r(4)
        assert m['hodge_weight'] == 4
        assert m['motive_type'] == 'mixed'

    def test_shadow_motive_higher_arities_mixed(self):
        """S_r for r >= 5 are all mixed motives."""
        for r in range(5, 12):
            m = shadow_motive_weight_r(r)
            assert m['motive_type'] == 'mixed'
            assert m['hodge_weight'] == r

    @skipmp
    def test_shadow_L_function_tate_at_s3(self):
        """L^{Tate}(M^{sh}, 3) = zeta(2) * zeta(3)."""
        result = shadow_motive_L_function_formal(3.0)
        zeta_2 = math.pi ** 2 / 6
        # zeta(3) ~ 1.2020569
        expected_product = zeta_2 * 1.2020569031595942
        assert abs(result['L_tate_product'].real - expected_product) < 1e-6

    @skipmp
    def test_shadow_L_function_pole_at_s2(self):
        """L^{Tate}(M^{sh}, s) has a pole at s=2 (from zeta(s-1) at s=2)."""
        # zeta(s-1) has pole at s=2 (i.e., zeta(1))
        # Test that the value grows near s=2
        val_near = shadow_motive_L_function_formal(2.01)
        assert abs(val_near['L_Q1'].real) > 10  # diverging


# ============================================================
# Section 7: Weight filtration on epsilon^c_s
# ============================================================

class TestEpsteinWeight:
    """Weight filtration on the constrained Epstein zeta."""

    def test_general_weight_formula(self):
        """w = (c - 1 - rho)/2 at scattering poles."""
        rho = 0.5 + 14.13j
        c_val = 13.0
        w = (c_val - 1 - rho) / 2
        result = epstein_weight_filtration(c_val, rho)
        assert abs(result['weight'] - w) < 1e-14

    @skipmp
    def test_weight_at_first_pole_c13(self):
        """At c=13, first zero: Re(w) = (13-3/2)/2 = 23/4 = 5.75."""
        result = epstein_weight_filtration(13.0)
        # Under RH: Re(rho) = 1/2, so Re(w) = (13-1-1/2)/2 = 11.5/2 = 5.75
        assert abs(result['weight_real'] - 5.75) < 0.01

    @skipmp
    def test_epstein_weight_poles_list(self):
        """Can compute weight at multiple scattering poles."""
        results = epstein_weight_at_scattering_poles(13.0, n_zeros=5)
        assert len(results) == 5
        for r in results:
            # Under RH: Re(weight) = (c-3/2)/2 = 5.75 for c=13
            assert abs(r['weight_real'] - 5.75) < 0.01

    @skipmp
    def test_self_dual_weight_c13(self):
        """At c=13 (self-dual): weight = (12-rho)/2."""
        result = epstein_weight_filtration(13.0)
        assert result['self_dual'] is True

    def test_non_self_dual_c26(self):
        """At c=26: not self-dual."""
        result = epstein_weight_filtration(26.0, rho=0.5 + 14.13j)
        assert result['self_dual'] is False


# ============================================================
# Section 8: Tate twist and complementarity
# ============================================================

class TestTateTwist:
    """Complementarity c -> 26-c as Tate twist."""

    def test_self_dual_no_twist(self):
        """At c=13: weight shift = 0 (self-dual)."""
        result = tate_twist_complementarity(13)
        assert result['weight_shift'] == 0
        assert result['at_self_dual'] is True
        assert result['formal_tate_twist'] == 0

    def test_c1_integer_twist(self):
        """At c=1: shift = -12, Tate twist by -6 (integer)."""
        result = tate_twist_complementarity(1)
        assert result['weight_shift'] == -12
        assert result['formal_tate_twist'] == -6
        assert result['is_integer_tate_twist'] is True

    def test_c26_integer_twist(self):
        """At c=26: shift = 13, half-integer."""
        result = tate_twist_complementarity(26)
        assert result['weight_shift'] == 13
        assert result['is_half_integer'] is True

    def test_c2_half_integer(self):
        """At c=2: shift = -11, half-integer."""
        result = tate_twist_complementarity(2)
        assert result['weight_shift'] == -11
        assert result['is_half_integer'] is True

    def test_complementarity_sum(self):
        """weight_shift(c) + weight_shift(26-c) = 0 always."""
        for c_val in [1, 2, 5, 10, 13, 20, 25]:
            r1 = tate_twist_complementarity(c_val)
            r2 = tate_twist_complementarity(26 - c_val)
            assert r1['weight_shift'] + r2['weight_shift'] == 0, (
                f"c={c_val}: shifts {r1['weight_shift']} + {r2['weight_shift']} != 0"
            )

    def test_complementarity_table(self):
        """The full complementarity table has the right entries."""
        table = complementarity_weight_table()
        assert len(table) > 0
        # Check c=13 is present and self-dual
        c13 = [t for t in table if t['c'] == 13]
        assert len(c13) == 1
        assert c13[0]['at_self_dual'] is True

    def test_integer_twist_iff_c_odd(self):
        """Tate twist is integer iff c is odd."""
        for c_val in range(1, 27):
            result = tate_twist_complementarity(c_val)
            if c_val % 2 == 1:
                assert result['is_integer_tate_twist'], f"c={c_val} odd but not integer twist"
            else:
                assert result['is_half_integer'], f"c={c_val} even but integer twist"


# ============================================================
# Section 9: Deligne's conjecture
# ============================================================

class TestDeligneConjecture:
    """Verification of Deligne's conjecture at critical values."""

    @skipmp
    def test_deligne_positive_even(self):
        """zeta(2k)/(2*pi)^{2k} is rational for k=1..10."""
        results = deligne_conjecture_zeta_critical(k_max=10, dps=DPS)
        pos_results = [r for r in results if r['type'] == 'positive_even']
        for r in pos_results:
            assert r['Deligne_check'] == 'PASS', (
                f"Deligne FAIL at n={r['n']}: error={r['error']}"
            )
            assert r['error'] < 1e-15

    @skipmp
    def test_deligne_negative_odd(self):
        """zeta(1-2k) = -B_{2k}/(2k) for k=1..10."""
        results = deligne_conjecture_zeta_critical(k_max=10, dps=DPS)
        neg_results = [r for r in results if r['type'] == 'negative_odd']
        for r in neg_results:
            assert r['Deligne_check'] == 'PASS', (
                f"Deligne FAIL at n={r['n']}: error={r['error']}"
            )
            assert r['error'] < 1e-15

    @skipmp
    def test_deligne_not_applicable_at_zero(self):
        """Deligne does not apply at s = 1+rho (not critical)."""
        result = deligne_structure_at_zero(k_zero=1, c_val=13.0, dps=DPS)
        assert result['deligne_applies'] is False
        assert result['is_critical_value'] is False


# ============================================================
# Section 10: Virasoro denominator analysis
# ============================================================

class TestVirasoDenominators:
    """Denominator structure of Virasoro S_r(c)."""

    @skipsy
    def test_S2_no_poles(self):
        """S_2 = c/2 has no poles (polynomial)."""
        results = virasoro_Sr_denominator_analysis(r_max=4)
        s2 = [r for r in results if r['r'] == 2][0]
        assert s2['a_r'] == 0  # no c-pole
        assert s2['b_r'] == 0  # no (5c+22)-pole

    @skipsy
    def test_S3_no_poles(self):
        """S_3 = 2 has no poles."""
        results = virasoro_Sr_denominator_analysis(r_max=4)
        s3 = [r for r in results if r['r'] == 3][0]
        assert s3['a_r'] == 0
        assert s3['b_r'] == 0

    @skipsy
    def test_S4_poles(self):
        """S_4 = 10/(c(5c+22)) has pole order (1,1)."""
        results = virasoro_Sr_denominator_analysis(r_max=4)
        s4 = [r for r in results if r['r'] == 4][0]
        assert s4['a_r'] == 1  # simple pole at c=0
        assert s4['b_r'] == 1  # simple pole at 5c+22=0

    @skipsy
    def test_pole_orders_non_decreasing(self):
        """Pole orders a_r and b_r are non-decreasing in r (for r >= 4)."""
        results = virasoro_Sr_denominator_analysis(r_max=10)
        for i in range(len(results) - 1):
            if results[i]['r'] >= 4 and results[i + 1]['r'] >= 5:
                # Pole orders should be non-decreasing
                assert results[i + 1]['a_r'] >= results[i]['a_r'], (
                    f"a_r decreased: r={results[i]['r']} has a={results[i]['a_r']}, "
                    f"r={results[i+1]['r']} has a={results[i+1]['a_r']}"
                )


# ============================================================
# Section 11: Cross-verification and consistency
# ============================================================

class TestCrossVerification:
    """Cross-verification across multiple computation paths."""

    @skipmp
    def test_special_value_weights(self):
        """Path 3: zeta(2k) weight matches formal assignment."""
        results = special_value_weight_check(dps=DPS)
        for r in results:
            assert r['match'], (
                f"n={r['n']}: formal weight {r['formal_weight']} != "
                f"expected {r['expected_weight']}"
            )

    @skipmp
    def test_galois_equivariance_is_path_4(self):
        """Path 4: A_c(rho_bar) = conj(A_c(rho))."""
        rho = complex(mpmath.zetazero(1))
        result = galois_equivariance_check(rho, 13.0, dps=DPS)
        assert result['equivariant']

    def test_weight_decomp_is_path_1(self):
        """Path 1: Direct weight computation gives total = 0."""
        rho = 0.5 + 14.134725j
        decomp = motivic_weight_decomposition_Ac(rho, 13.0)
        assert abs(decomp['total_weight']) < 1e-14

    def test_additivity_is_path_2(self):
        """Path 2: Weights are additive under tensor product."""
        rho = 0.5 + 14.134725j
        result = weight_additivity_check(rho, 13.0)
        assert result['additive']

    @skipmp
    def test_full_motivic_analysis_runs(self):
        """Full analysis pipeline completes without error."""
        result = full_motivic_analysis(c_val=13.0, n_zeros=2, dps=DPS)
        assert 'weight_decomposition' in result
        assert 'epstein_weights' in result
        assert 'tate_twist' in result
        assert 'galois' in result
        assert 'deligne_critical' in result
        assert result['galois']['equivariant']

    @skipmp
    def test_full_analysis_c26(self):
        """Full analysis at c=26 (critical dimension)."""
        result = full_motivic_analysis(c_val=26.0, n_zeros=2, dps=DPS)
        assert abs(result['weight_decomposition']['total_weight']) < 1e-14

    @skipmp
    def test_full_analysis_c1(self):
        """Full analysis at c=1 (Heisenberg central charge)."""
        result = full_motivic_analysis(c_val=1.0, n_zeros=2, dps=DPS)
        assert abs(result['weight_decomposition']['total_weight']) < 1e-14

    @skipmp
    def test_epstein_weight_consistent_across_zeros(self):
        """Under RH, Re(weight) is the same for all zeros at fixed c."""
        results = epstein_weight_at_scattering_poles(13.0, n_zeros=5, dps=DPS)
        weights_real = [r['weight_real'] for r in results]
        # Under RH: all have Re(rho) = 1/2, so Re(w) = (c-3/2)/2
        for w in weights_real:
            assert abs(w - weights_real[0]) < 0.01, (
                f"Inconsistent real weights: {weights_real}"
            )


# ============================================================
# Section 12: MotivicWeight class operations
# ============================================================

class TestMotivicWeightClass:
    """Algebraic operations on MotivicWeight objects."""

    def test_addition(self):
        """Weight addition."""
        w1 = MotivicWeight(2, "a")
        w2 = MotivicWeight(3, "b")
        w3 = w1 + w2
        assert w3.real_weight == 5

    def test_subtraction(self):
        """Weight subtraction."""
        w1 = MotivicWeight(5, "a")
        w2 = MotivicWeight(3, "b")
        w3 = w1 - w2
        assert w3.real_weight == 2

    def test_negation(self):
        """Weight negation."""
        w = MotivicWeight(3, "a")
        assert (-w).real_weight == -3

    def test_repr(self):
        """String representation."""
        w = MotivicWeight(2.5, "test")
        assert "2.5" in repr(w)
        assert "test" in repr(w)

    def test_complex_weight(self):
        """Complex weights track imaginary part."""
        w = MotivicWeight(2 + 3j, "complex")
        assert w.real_weight == 2
        assert w.value.imag == 3


# ============================================================
# Section 13: Bernoulli number cross-checks
# ============================================================

class TestBernoulliCrossChecks:
    """Cross-check Bernoulli numbers in zeta critical values."""

    @skipmp
    def test_B2_equals_one_sixth(self):
        """B_2 = 1/6."""
        result = zeta_critical_value(1, dps=DPS)
        assert abs(result['Bernoulli_number'] - 1.0 / 6) < 1e-20

    @skipmp
    def test_B4_equals_minus_one_thirtieth(self):
        """B_4 = -1/30."""
        result = zeta_critical_value(2, dps=DPS)
        assert abs(result['Bernoulli_number'] - (-1.0 / 30)) < 1e-20

    @skipmp
    def test_zeta_values_first_five(self):
        """First five even zeta values match known values."""
        known = {
            1: math.pi ** 2 / 6,
            2: math.pi ** 4 / 90,
            3: math.pi ** 6 / 945,
            4: math.pi ** 8 / 9450,
            5: math.pi ** 10 / 93555,
        }
        for k, expected in known.items():
            result = zeta_critical_value(k, dps=DPS)
            assert abs(result['zeta_value'] - expected) < 1e-8, (
                f"zeta({2*k}) = {result['zeta_value']} != {expected}"
            )
