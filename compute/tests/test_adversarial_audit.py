"""Adversarial audit tests targeting fragile computations.

Targets:
1. is_prime bug (FIXED)
2. lambda_fp Bernoulli number edge cases
3. Genus expansion off-by-one
4. Sewing determinant identity consistency
5. Kappa formula cross-checks
6. E2 q-expansion sign convention
7. Complementarity sum universality
"""

from __future__ import annotations

import math
import pytest
from fractions import Fraction
from sympy import Rational, Symbol, bernoulli, factorial, simplify, pi, Abs

from compute.lib.utils import lambda_fp, F_g, partition_number
from compute.lib.sewing_euler_product import (
    is_prime, primes_up_to, sigma_k, sigma_minus_1, sigma_0, sigma_1,
    von_mangoldt, log_det_full, log_det_sigma,
    prime_contribution, trace_K_power,
)
from compute.lib.mc5_genus1_bridge import (
    eisenstein_E2_q_expansion,
    lambda_fp_genus1,
    genus1_free_energy,
)
from compute.lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3,
    kappa_sl2, kappa_sl3, kappa_g2, kappa_b2,
    complementarity_sum_km,
)
from compute.lib.mc5_higher_genus import (
    STANDARD_FAMILIES,
    theta_characteristics_count,
    sewing_correction,
)


# ============================================================
# 1. is_prime (was buggy, now fixed)
# ============================================================

class TestIsPrimeFix:
    """Verify the is_prime fix: (n+2)%d -> n%(d+2)."""

    def test_small_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for p in primes:
            assert is_prime(p), f"{p} should be prime"

    def test_small_composites(self):
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 25, 27, 28]
        for n in composites:
            assert not is_prime(n), f"{n} should not be prime"

    def test_squares_of_primes(self):
        """These were the main failure mode of the old bug."""
        for p in [7, 11, 13, 17, 19, 23, 29, 31]:
            assert not is_prime(p * p), f"{p}^2 = {p*p} should not be prime"

    def test_49_not_prime(self):
        """49 = 7*7 was incorrectly reported as prime before fix."""
        assert not is_prime(49)

    def test_43_is_prime(self):
        """43 was incorrectly reported as composite before fix."""
        assert is_prime(43)

    def test_comprehensive_to_1000(self):
        """Brute-force cross-check against trial division."""
        def trial_division(n):
            if n < 2:
                return False
            for d in range(2, int(n**0.5) + 1):
                if n % d == 0:
                    return False
            return True

        for n in range(2, 1000):
            assert is_prime(n) == trial_division(n), f"is_prime({n}) wrong"


# ============================================================
# 2. lambda_fp edge cases and Bernoulli conventions
# ============================================================

class TestLambdaFP:
    """Verify lambda_fp against independent computation."""

    def test_lambda1(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda2(self):
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda3(self):
        assert lambda_fp(3) == Rational(31, 967680)

    def test_bernoulli_sign_convention(self):
        """B_2 = 1/6, B_4 = -1/30, B_6 = 1/42.
        lambda_fp uses |B_{2g}|, so signs must not matter."""
        # B_2 = 1/6 (positive)
        assert bernoulli(2) == Rational(1, 6)
        # B_4 = -1/30 (negative)
        assert bernoulli(4) == Rational(-1, 30)
        # Verify lambda_fp handles the sign correctly
        B4 = bernoulli(4)
        manual = (2**3 - 1) * Abs(B4) / (2**3 * factorial(4))
        assert lambda_fp(2) == manual

    def test_genus0_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(-1)

    def test_all_positive(self):
        """lambda_fp(g) > 0 for all g >= 1."""
        for g in range(1, 20):
            assert lambda_fp(g) > 0

    def test_decreasing(self):
        """lambda_fp(g) is strictly decreasing."""
        for g in range(1, 15):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_ratio_converges_to_1_over_4pi2(self):
        """lambda_{g+1}/lambda_g -> 1/(4*pi^2) as g -> inf."""
        target = 1.0 / (4 * float(pi)**2)
        ratio = float(lambda_fp(15) / lambda_fp(14))
        assert abs(ratio - target) / target < 0.01


# ============================================================
# 3. Genus expansion F_g consistency
# ============================================================

class TestGenusExpansion:
    def test_F_g_linearity_in_kappa(self):
        """F_g(a*kappa) = a * F_g(kappa)."""
        kappa = Symbol('kappa')
        for g in range(1, 6):
            assert simplify(F_g(3 * kappa, g) - 3 * F_g(kappa, g)) == 0

    def test_F1_heisenberg(self):
        assert genus1_free_energy(Rational(1)) == Rational(1, 24)

    def test_F1_virasoro_c26(self):
        """F_1(Vir_26) = 26/2 * 1/24 = 13/24."""
        assert genus1_free_energy(Rational(13)) == Rational(13, 24)


# ============================================================
# 4. Sewing determinant identities
# ============================================================

class TestSewingDeterminant:
    def test_log_det_two_methods_agree(self):
        """log det via product vs sigma_{-1} sum."""
        q = 0.3
        val1 = log_det_full(q, nmax=300)
        val2 = log_det_sigma(q, Nmax=300)
        assert abs(val1 - val2) / abs(val1) < 1e-8

    def test_sigma_minus1_multiplicative(self):
        """sigma_{-1} is multiplicative: sigma_{-1}(mn) = sigma_{-1}(m)*sigma_{-1}(n) for gcd(m,n)=1."""
        for m in range(1, 20):
            for n in range(1, 20):
                if math.gcd(m, n) == 1:
                    assert abs(sigma_minus_1(m * n) - sigma_minus_1(m) * sigma_minus_1(n)) < 1e-12, \
                        f"sigma_{{-1}} not multiplicative at ({m},{n})"

    def test_sigma0_is_divisor_count(self):
        known = {1: 1, 2: 2, 3: 2, 4: 3, 6: 4, 12: 6, 24: 8}
        for n, d in known.items():
            assert sigma_0(n) == d, f"sigma_0({n}) = {sigma_0(n)}, expected {d}"

    def test_sigma1_values(self):
        """sigma_1(n) = sum of divisors."""
        assert sigma_1(1) == 1
        assert sigma_1(6) == 1 + 2 + 3 + 6  # = 12
        assert sigma_1(12) == 1 + 2 + 3 + 4 + 6 + 12  # = 28

    def test_von_mangoldt_primes(self):
        for p in [2, 3, 5, 7, 11, 13]:
            assert abs(von_mangoldt(p) - math.log(p)) < 1e-12

    def test_von_mangoldt_prime_powers(self):
        assert abs(von_mangoldt(8) - math.log(2)) < 1e-12  # 2^3
        assert abs(von_mangoldt(27) - math.log(3)) < 1e-12  # 3^3

    def test_von_mangoldt_composites(self):
        """Λ(n) = 0 for n not a prime power."""
        assert von_mangoldt(6) == 0.0
        assert von_mangoldt(10) == 0.0
        assert von_mangoldt(12) == 0.0

    def test_trace_formula(self):
        """tr(K_q^N) = q^N/(1-q^N)."""
        q = 0.4
        for N in [1, 2, 5, 10]:
            expected = q**N / (1 - q**N)
            assert abs(trace_K_power(q, N) - expected) < 1e-12


# ============================================================
# 5. Kappa cross-checks
# ============================================================

class TestKappaCrossChecks:
    def test_kappa_km_formula(self):
        """kappa(g_k) = dim(g) * (k + h^v) / (2*h^v)."""
        # sl2: dim=3, h^v=2
        assert kappa_sl2(1) == Rational(9, 4)
        assert kappa_sl2(0) == Rational(3, 2)
        # sl3: dim=8, h^v=3
        assert kappa_sl3(1) == Rational(16, 3)

    def test_kappa_critical_level(self):
        """At critical level k = -h^v, kappa = 0."""
        assert kappa_sl2(-2) == 0
        assert kappa_sl3(-3) == 0

    def test_virasoro_self_dual_c13(self):
        """Vir self-dual at c=13, NOT c=26."""
        assert kappa_virasoro(13) == Rational(13, 2)
        dual_kappa = Rational(26 - 13, 2)
        assert kappa_virasoro(13) == dual_kappa

    def test_virasoro_NOT_self_dual_c26(self):
        assert kappa_virasoro(26) != Rational(26 - 26, 2)

    def test_complementarity_km_all_families(self):
        """kappa(g_k) + kappa(g_{-k-2h^v}) = 0 for KM families."""
        for (t, r) in [("A", 1), ("A", 2), ("G", 2)]:
            s = complementarity_sum_km(t, r)
            assert simplify(s) == 0, f"Complementarity fails for ({t},{r}): sum = {s}"


# ============================================================
# 6. E2 q-expansion
# ============================================================

class TestE2QExpansion:
    def test_constant_term(self):
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[0] == 1

    def test_q1_coefficient(self):
        """E2: q^1 coefficient is -24 * sigma_1(1) = -24."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[1] == -24

    def test_q2_coefficient(self):
        """sigma_1(2) = 3, so coeff = -72."""
        coeffs = eisenstein_E2_q_expansion(5)
        assert coeffs[2] == -72

    def test_q6_coefficient(self):
        """sigma_1(6) = 12, so coeff = -288."""
        coeffs = eisenstein_E2_q_expansion(10)
        assert coeffs[6] == -288


# ============================================================
# 7. Complementarity universality
# ============================================================

class TestComplementarityUniversality:
    def test_heisenberg_complement_zero(self):
        fam = STANDARD_FAMILIES["Heisenberg"]
        k = Symbol('kappa')
        assert simplify(fam["kappa"](k) + fam["dual_kappa"](k)) == 0

    def test_virasoro_complement_13(self):
        fam = STANDARD_FAMILIES["Virasoro"]
        c = Symbol('c')
        assert simplify(fam["kappa"](c) + fam["dual_kappa"](c) - 13) == 0

    def test_w3_complement_250_3(self):
        fam = STANDARD_FAMILIES["W3"]
        c = Symbol('c')
        assert simplify(fam["kappa"](c) + fam["dual_kappa"](c) - Rational(250, 3)) == 0

    def test_km_complement_zero_all(self):
        """All KM families have complementarity sum = 0."""
        k = Symbol('k')
        for name in ["sl2", "sl3", "G2", "B2"]:
            fam = STANDARD_FAMILIES[name]
            s = simplify(fam["kappa"](k) + fam["dual_kappa"](k))
            assert s == 0, f"{name}: complementarity sum = {s}, expected 0"


# ============================================================
# 8. Theta characteristics
# ============================================================

class TestThetaCharacteristics:
    def test_genus1(self):
        assert theta_characteristics_count(1, 'odd') == 1
        assert theta_characteristics_count(1, 'even') == 3
        assert theta_characteristics_count(1, 'total') == 4

    def test_genus2(self):
        assert theta_characteristics_count(2, 'odd') == 6
        assert theta_characteristics_count(2, 'even') == 10
        assert theta_characteristics_count(2, 'total') == 16

    def test_odd_plus_even_equals_total(self):
        for g in range(1, 8):
            assert (theta_characteristics_count(g, 'odd') +
                    theta_characteristics_count(g, 'even') ==
                    theta_characteristics_count(g, 'total'))


# ============================================================
# 9. Sewing correction sign
# ============================================================

class TestSewingCorrection:
    def test_all_negative_g2_to_g20(self):
        """Sewing correction lambda_g - lambda_{g-1} < 0 for g >= 2."""
        for g in range(2, 20):
            sc = sewing_correction(g)
            assert sc < 0, f"Sewing correction at g={g} is {sc}, expected negative"


# ============================================================
# 10. Partition numbers
# ============================================================

class TestPartitionNumbers:
    def test_known_values(self):
        known = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15, 8: 22}
        for n, p in known.items():
            assert partition_number(n) == p, f"p({n}) = {partition_number(n)}, expected {p}"

    def test_negative(self):
        assert partition_number(-1) == 0
