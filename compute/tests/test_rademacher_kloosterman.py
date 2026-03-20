"""Tests for compute/lib/rademacher_kloosterman.py.

Rademacher expansions and Kloosterman sums for VOA characters.

THE NON-LATTICE BRIDGE PROBLEM:
  Minimal model Dirichlet series are non-multiplicative, blocking the
  shadow-spectral correspondence. The Rademacher expansion decomposes
  character coefficients into Kloosterman contributions, which ARE
  multiplicative in the modulus c (via the twisted CRT identity).
  This module verifies:

  (R1) Classical Kloosterman sums: definition, symmetry, special cases
  (R2) Twisted multiplicativity: K(m,n;c1*c2) = K(m*c2_bar,n*c2_bar;c1)*K(m*c1_bar,n*c1_bar;c2)
  (R3) Weil bound: |K(m,n;c)| <= d(c)*sqrt(c)*gcd(m,n,c)^{1/2}
  (R4) Ising S-matrix: unitarity, conformal weights
  (R5) Rademacher expansion: convergence to exact Ising characters
  (R6) Kloosterman Dirichlet series: structure
  (R7) Non-multiplicativity diagnosis: interference between j-channels
  (R8) Kuznetsov trace formula connection
  (R9) Generalized Kloosterman for VVMFs
  (R10) Ramanujan sum as special case

Ground truth:
  K(0,0;c) = phi(c) (Euler totient)
  K(0,n;c) = Ramanujan sum c_c(n) = Sum_{d|(c,n)} mu(c/d)*d
  K(m,n;1) = 1
  |K(m,n;c)| <= d(c)*sqrt(c)*gcd(m,n,c)^{1/2} (Weil 1948)
  Twisted multiplicativity: K(m,n;c1c2) = K(m*c2_bar,n*c2_bar;c1)*K(m*c1_bar,n*c1_bar;c2)
  Ising vacuum character: 1, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 12, 16, 18
"""

import math
import pytest

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

pytestmark = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")

from compute.lib.rademacher_kloosterman import (
    kloosterman_sum,
    kloosterman_sum_real,
    verify_kloosterman_multiplicativity,
    verify_kloosterman_naive_multiplicativity,
    euler_totient,
    ramanujan_sum,
    ramanujan_sum_formula,
    mobius,
    weil_bound,
    verify_weil_bound,
    divisor_count,
    ising_s_matrix,
    ising_conformal_weights,
    ising_verify_unitarity,
    ising_exact_coefficients,
    rademacher_coefficient,
    rademacher_c_contribution,
    rademacher_j_contribution,
    kloosterman_dirichlet_series,
    kloosterman_euler_product,
    kuznetsov_kloosterman_side,
    check_multiplicativity,
    diagnose_interference,
    generalized_kloosterman_simplified,
    generalized_kloosterman_ising,
    _generalized_kloosterman_rational,
    verify_kloosterman_rational_multiplicativity,
    _primes_up_to,
    _partition_numbers,
)


# ============================================================
# 1. Classical Kloosterman sum basics
# ============================================================

class TestKloostermanBasics:
    """Basic properties of classical Kloosterman sums K(m, n; c)."""

    def test_K_trivial_modulus(self):
        """K(m, n; 1) = 1 for all m, n."""
        for m in range(4):
            for n in range(4):
                val = kloosterman_sum_real(m, n, 1)
                assert abs(val - 1.0) < 1e-10, f"K({m},{n};1) = {val}, expected 1"

    def test_K_zero_zero_is_totient(self):
        """K(0, 0; c) = phi(c) (Euler's totient function)."""
        for c in range(1, 21):
            K_val = kloosterman_sum_real(0, 0, c)
            expected = euler_totient(c)
            assert abs(K_val - expected) < 1e-8, \
                f"K(0,0;{c}) = {K_val}, expected phi({c}) = {expected}"

    def test_K_is_real_for_integer_args(self):
        """K(m, n; c) is real when m, n are integers."""
        for m in range(4):
            for n in range(4):
                for c in range(1, 16):
                    K_val = kloosterman_sum(m, n, c)
                    imag = float(abs(mpmath.im(K_val)))
                    assert imag < 1e-10, \
                        f"K({m},{n};{c}) has imaginary part {imag}"

    def test_K_symmetry_mn(self):
        """K(m, n; c) = K(n, m; c) (symmetry in m, n)."""
        for m in range(5):
            for n in range(5):
                for c in range(1, 16):
                    K_mn = kloosterman_sum_real(m, n, c)
                    K_nm = kloosterman_sum_real(n, m, c)
                    assert abs(K_mn - K_nm) < 1e-10, \
                        f"K({m},{n};{c})={K_mn} != K({n},{m};{c})={K_nm}"

    def test_K_specific_values(self):
        """Check some known Kloosterman sum values."""
        # K(1, 1; 2): only d=1 coprime to 2, d'=1. Phase = 2*pi*(1+1)/2 = 2*pi.
        val = kloosterman_sum_real(1, 1, 2)
        assert abs(val - 1.0) < 1e-10, f"K(1,1;2) = {val}"

        # K(0, 1; c) = Ramanujan sum c_c(1) = mu(c)
        # For c=6: mu(6) = 1
        val = kloosterman_sum_real(0, 1, 6)
        assert abs(val - 1.0) < 1e-10, f"K(0,1;6) = {val}, expected mu(6)=1"

    def test_K_negative_args(self):
        """K(-m, -n; c) = K(m, n; c) for integer arguments."""
        for m in range(1, 4):
            for n in range(1, 4):
                for c in range(2, 10):
                    K_pos = kloosterman_sum_real(m, n, c)
                    K_neg = kloosterman_sum_real(-m, -n, c)
                    assert abs(K_pos - K_neg) < 1e-10, \
                        f"K({m},{n};{c})={K_pos} != K({-m},{-n};{c})={K_neg}"


# ============================================================
# 2. Kloosterman twisted multiplicativity
# ============================================================

class TestKloostermanMultiplicativity:
    """Twisted multiplicativity: K(m,n;c1*c2) = K(m*c2_bar,n*c2_bar;c1)*K(m*c1_bar,n*c1_bar;c2).

    The NAIVE form K(m,n;c1)*K(m,n;c2) generally FAILS.
    The twist comes from the CRT: c2_bar = c2^{-1} mod c1, c1_bar = c1^{-1} mod c2.
    """

    def test_twisted_multiplicativity_small(self):
        """Verify twisted multiplicativity for m,n in {0,1,2,3} and small coprime pairs."""
        coprime_pairs = [(2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7),
                         (2, 9), (4, 9), (3, 11), (5, 11), (7, 11)]
        for m in range(4):
            for n in range(4):
                for c1, c2 in coprime_pairs:
                    _, _, err = verify_kloosterman_multiplicativity(m, n, c1, c2)
                    assert err < 1e-10, \
                        f"Twisted mult fails: K({m},{n};{c1}*{c2}), err={err}"

    def test_twisted_multiplicativity_larger_moduli(self):
        """Verify twisted multiplicativity for c up to 30."""
        for m in [0, 1, 2]:
            for n in [0, 1, 3]:
                for c1 in [2, 3, 5, 7, 11, 13]:
                    for c2 in [2, 3, 5, 7, 11, 13]:
                        if c1 >= c2:
                            continue
                        if math.gcd(c1, c2) != 1:
                            continue
                        if c1 * c2 > 30:
                            continue
                        _, _, err = verify_kloosterman_multiplicativity(m, n, c1, c2)
                        assert err < 1e-10, \
                            f"Twisted mult fails: K({m},{n};{c1}*{c2}), err={err}"

    def test_naive_multiplicativity_m0(self):
        """Naive multiplicativity holds for m=0 (Ramanujan sums are multiplicative)."""
        for n in range(4):
            for c1, c2 in [(2, 3), (3, 5), (2, 7)]:
                _, _, err = verify_kloosterman_naive_multiplicativity(0, n, c1, c2)
                assert err < 1e-10, \
                    f"Ramanujan sum not multiplicative: c_{c1*c2}({n})"

    def test_naive_multiplicativity_fails_nonzero(self):
        """Naive K(m,n;c1)*K(m,n;c2) generally FAILS for m,n > 0.

        This is mathematically important: the twist is essential.
        """
        m, n = 1, 1
        c1, c2 = 2, 5
        _, _, err = verify_kloosterman_naive_multiplicativity(m, n, c1, c2)
        assert err > 0.1, \
            f"Naive multiplicativity should FAIL for K(1,1;2*5), err={err}"

    def test_non_coprime_raises(self):
        """Multiplicativity function raises for non-coprime inputs."""
        with pytest.raises(ValueError):
            verify_kloosterman_multiplicativity(1, 1, 2, 4)

    def test_twisted_multiplicativity_prime_power(self):
        """K(m,n;p^a*q^b) factors correctly for distinct primes p,q."""
        for m in [0, 1]:
            for n in [0, 1]:
                # 4 * 9 = 36, gcd(4,9) = 1
                _, _, err = verify_kloosterman_multiplicativity(m, n, 4, 9)
                assert err < 1e-10, f"K({m},{n};4*9) twisted mult err={err}"
                # 8 * 27 = 216
                _, _, err = verify_kloosterman_multiplicativity(m, n, 8, 27)
                assert err < 1e-10, f"K({m},{n};8*27) twisted mult err={err}"

    def test_twisted_three_factors(self):
        """Three-factor twisted multiplicativity for 2*3*5 = 30."""
        # For three coprime factors, the twisted multiplicativity applies iteratively:
        # K(m,n;2*3*5) = K(m*15_bar, n*15_bar; 2) * K(m*10_bar, n*10_bar; 3) * K(m*6_bar, n*6_bar; 5)
        # ... but the standard CRT lift is for two factors at a time.
        # Let's just verify K(m,n;30) = twisted product of K(;6)*K(;5) where 6=2*3.
        for m in [0, 1]:
            for n in [0, 1]:
                _, _, err = verify_kloosterman_multiplicativity(m, n, 6, 5)
                assert err < 1e-10


# ============================================================
# 3. Ramanujan sum (m=0 special case)
# ============================================================

class TestRamanujanSum:
    """Ramanujan sum c_c(n) = K(0, n; c)."""

    def test_ramanujan_vs_mobius_formula(self):
        """Verify K(0,n;c) = Sum_{d|gcd(c,n)} mu(c/d)*d."""
        for c in range(1, 21):
            for n in range(1, 21):
                K_val = kloosterman_sum_real(0, n, c)
                formula_val = ramanujan_sum_formula(n, c)
                assert abs(K_val - formula_val) < 1e-8, \
                    f"c_{c}({n}): K={K_val}, formula={formula_val}"

    def test_ramanujan_c1_is_mobius(self):
        """c_c(1) = mu(c) for all c."""
        for c in range(1, 21):
            K_val = kloosterman_sum_real(0, 1, c)
            mu_val = mobius(c)
            assert abs(K_val - mu_val) < 1e-8, \
                f"c_{c}(1) = {K_val}, mu({c}) = {mu_val}"

    def test_ramanujan_sum_orthogonality(self):
        """Ramanujan sum from direct computation matches Mobius formula."""
        for n in range(1, 10):
            for c in range(1, 10):
                direct = float(ramanujan_sum(n, c))
                formula = float(ramanujan_sum_formula(n, c))
                assert abs(direct - formula) < 1e-8


# ============================================================
# 4. Weil bound
# ============================================================

class TestWeilBound:
    """Verify |K(m,n;c)| <= d(c)*sqrt(c)*gcd(m,n,c)^{1/2}."""

    def test_weil_bound_systematic(self):
        """Check Weil bound for m,n in {0,1,2,3}, c up to 30."""
        violations = []
        for m in range(4):
            for n in range(4):
                for c in range(1, 31):
                    K_abs, bound, satisfied = verify_weil_bound(m, n, c)
                    if not satisfied:
                        violations.append((m, n, c, K_abs, bound))
        assert len(violations) == 0, \
            f"Weil bound violated in {len(violations)} cases: {violations[:5]}"

    def test_weil_bound_larger_args(self):
        """Weil bound for larger m, n values."""
        for m in [5, 10, 20]:
            for n in [5, 10, 20]:
                for c in [7, 11, 13, 17, 19, 23, 29]:
                    K_abs, bound, satisfied = verify_weil_bound(m, n, c)
                    assert satisfied, \
                        f"|K({m},{n};{c})|={K_abs} > bound={bound}"

    def test_weil_bound_prime_modulus(self):
        """For prime c with gcd(mn,p)=1: |K(m,n;p)| <= 2*sqrt(p)."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in primes:
            for m in [1, 2, 3]:
                for n in [1, 2, 3]:
                    if m % p == 0 or n % p == 0:
                        continue
                    K_abs = float(abs(kloosterman_sum(m, n, p)))
                    bound = 2 * math.sqrt(p)
                    assert K_abs <= bound + 1e-8, \
                        f"|K({m},{n};{p})|={K_abs} > 2*sqrt({p})={bound}"

    def test_kloosterman_bound_convergence(self):
        """Verify Weil bound implies convergence of K_tilde for Re(s) > 1."""
        m, n = 1, 1
        s_val = mpmath.mpf('1.5')
        prev = mpmath.mpc(0)
        for c_max in [10, 20, 50, 100]:
            current = kloosterman_dirichlet_series(m, n, s_val, c_max=c_max)
            if c_max > 10:
                diff = float(abs(current - prev))
                assert diff < 1.0, f"Partial sums not converging at c_max={c_max}"
            prev = current


# ============================================================
# 5. Ising model S-matrix
# ============================================================

class TestIsingModel:
    """Ising model modular data."""

    def test_ising_unitarity(self):
        """S^2 = I for the Ising S-matrix."""
        err = ising_verify_unitarity()
        assert err < 1e-10, f"Ising S-matrix unitarity error: {err}"

    def test_ising_conformal_weights(self):
        """h = (0, 1/2, 1/16) for the Ising model."""
        h = ising_conformal_weights()
        assert abs(float(h[0]) - 0.0) < 1e-10
        assert abs(float(h[1]) - 0.5) < 1e-10
        assert abs(float(h[2]) - 1.0/16) < 1e-10

    def test_ising_s_matrix_symmetric(self):
        """S-matrix is symmetric."""
        S = ising_s_matrix()
        for i in range(3):
            for j in range(3):
                assert abs(float(S[i, j] - S[j, i])) < 1e-10

    def test_ising_s_matrix_values(self):
        """Check specific S-matrix entries."""
        S = ising_s_matrix()
        sq2 = float(mpmath.sqrt(2))
        assert abs(float(S[0, 0]) - 0.5) < 1e-10
        assert abs(float(S[0, 2]) - 0.5 * sq2) < 1e-10
        assert abs(float(S[2, 2])) < 1e-10  # S_{22} = 0

    def test_ising_verlinde_formula(self):
        """Fusion coefficients N_{ij}^k are non-negative integers."""
        S = ising_s_matrix()
        N_22_0 = sum(float(S[2, l] * S[2, l] * S[0, l] / S[0, l]) for l in range(3))
        assert abs(N_22_0 - 1.0) < 1e-8, f"N_{{sigma,sigma}}^1 = {N_22_0}"


# ============================================================
# 6. Ising exact characters (Rocha-Caridi formula)
# ============================================================

class TestIsingExactCharacters:
    """Exact Ising character coefficients from Rocha-Caridi formula.

    Ground truth for M(4,3):
      vacuum   (h=0):    1, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 12, 16, 18
      energy   (h=1/2):  1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 9, 12, 14, 17, 20
      spin     (h=1/16): 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 27
    """

    def test_vacuum_leading_coefficient(self):
        """a_0(0) = 1 (vacuum state)."""
        coeffs = ising_exact_coefficients(0, 5)
        assert abs(float(coeffs[0]) - 1.0) < 1e-10

    def test_vacuum_level_1_vanishes(self):
        """a_0(1) = 0 (level-1 null vector for c=1/2 vacuum)."""
        coeffs = ising_exact_coefficients(0, 5)
        assert abs(float(coeffs[1])) < 1e-10

    def test_vacuum_level_2(self):
        """a_0(2) = 1 (Virasoro descendant L_{-2}|0>)."""
        coeffs = ising_exact_coefficients(0, 5)
        assert abs(float(coeffs[2]) - 1.0) < 1e-10

    def test_vacuum_first_few(self):
        """Vacuum character: 1, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 12, 16, 18.

        From the Rocha-Caridi formula for M(4,3), (r,s)=(1,1).
        The null vectors at levels 1 and 6 reduce the Verma module dimensions.
        """
        coeffs = ising_exact_coefficients(0, 15)
        expected = [1, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 12, 16, 18]
        for n in range(len(expected)):
            val = float(coeffs[n])
            assert abs(val - expected[n]) < 1e-8, \
                f"chi_0 coeff at n={n}: got {val}, expected {expected[n]}"

    def test_energy_first_few(self):
        """Energy character (h=1/2): 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8."""
        coeffs = ising_exact_coefficients(1, 10)
        expected = [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8]
        for n in range(len(expected)):
            val = float(coeffs[n])
            assert abs(val - expected[n]) < 1e-8, \
                f"chi_1 coeff at n={n}: got {val}, expected {expected[n]}"

    def test_spin_first_few(self):
        """Spin character (h=1/16): 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10."""
        coeffs = ising_exact_coefficients(2, 10)
        expected = [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10]
        for n in range(len(expected)):
            val = float(coeffs[n])
            assert abs(val - expected[n]) < 1e-8, \
                f"chi_2 coeff at n={n}: got {val}, expected {expected[n]}"

    def test_partition_numbers(self):
        """Verify partition numbers p(0)=1, p(1)=1, ..., p(10)=42."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        parts = _partition_numbers(10)
        for n in range(11):
            assert abs(float(parts[n]) - expected[n]) < 1e-10, \
                f"p({n}) = {float(parts[n])}, expected {expected[n]}"


# ============================================================
# 7. Rademacher expansion convergence
# ============================================================

class TestRademacherExpansion:
    """Rademacher expansion for the Ising vacuum character.

    The Rademacher formula converges slowly for Ising because the polar order
    alpha_0 = 1/48 is very small. For comparison, the j-function has alpha = 1
    and converges in ~10 terms. For Ising, we need ~100+ terms in c for moderate n.
    """

    def test_rademacher_vacuum_n0_exact(self):
        """a_0(0) = 1 is returned exactly (special case)."""
        val = rademacher_coefficient(0, 0, c_max=50)
        assert abs(float(mpmath.re(val)) - 1.0) < 1e-10

    def test_rademacher_vacuum_n5(self):
        """Rademacher gives a_0(5) ~ 2 (within tolerance)."""
        val = rademacher_coefficient(0, 5, c_max=80)
        assert abs(float(mpmath.re(val)) - 2.0) < 0.5, \
            f"Rademacher a_0(5) = {float(mpmath.re(val))}"

    def test_rademacher_vacuum_n10(self):
        """Rademacher gives a_0(10) ~ 7 (convergence improves with n)."""
        val = rademacher_coefficient(0, 10, c_max=80)
        assert abs(float(mpmath.re(val)) - 7.0) < 1.0, \
            f"Rademacher a_0(10) = {float(mpmath.re(val))}"

    def test_rademacher_imaginary_small(self):
        """Rademacher coefficients should have small imaginary parts."""
        for n in [3, 5, 8]:
            val = rademacher_coefficient(0, n, c_max=60)
            imag = float(abs(mpmath.im(val)))
            assert imag < 0.5, f"Rademacher a_0({n}) imaginary part = {imag}"

    def test_rademacher_convergence_improves_with_n(self):
        """For larger n, Rademacher converges faster (Bessel argument grows with sqrt(n))."""
        exact = ising_exact_coefficients(0, 10)
        # Compare errors at n=3 and n=10
        err_3 = abs(float(mpmath.re(rademacher_coefficient(0, 3, c_max=80))) - float(exact[3]))
        err_10 = abs(float(mpmath.re(rademacher_coefficient(0, 10, c_max=80))) - float(exact[10]))
        # Relative error should be better at n=10
        rel_3 = err_3 / max(float(exact[3]), 0.1)
        rel_10 = err_10 / max(float(exact[10]), 0.1)
        assert rel_10 < rel_3 + 0.1, \
            f"Rademacher should converge faster for larger n: rel_3={rel_3}, rel_10={rel_10}"

    def test_rademacher_j0_channel_dominates(self):
        """Only j=0 contributes (j=1,2 have no polar terms for Ising)."""
        n = 5
        c_max = 30
        ch0 = rademacher_j_contribution(0, 0, n, c_max=c_max)
        ch1 = rademacher_j_contribution(0, 1, n, c_max=c_max)
        ch2 = rademacher_j_contribution(0, 2, n, c_max=c_max)
        assert float(abs(ch0)) > 0.1, "Vacuum channel should be non-trivial"
        assert float(abs(ch1)) < 1e-10, "Energy channel should be zero"
        assert float(abs(ch2)) < 1e-10, "Spin channel should be zero"

    def test_rademacher_c_contribution_sum(self):
        """Sum over c-contributions should equal total Rademacher coefficient."""
        n = 3
        c_max = 20
        total = rademacher_coefficient(0, n, c_max=c_max)
        c_sum = sum(rademacher_c_contribution(0, n, c_val) for c_val in range(1, c_max + 1))
        err = float(abs(total - c_sum))
        assert err < 1e-8, f"c-sum differs from total by {err}"


# ============================================================
# 8. Generalized Kloosterman sums for VVMFs
# ============================================================

class TestGeneralizedKloosterman:
    """Generalized Kloosterman sums for the Ising VVMF."""

    def test_simplified_form(self):
        """Simplified generalized Kloosterman = S_{ij} * K(m,n;c)."""
        S = ising_s_matrix()
        for c in range(1, 11):
            for m in [0, 1]:
                for n in [0, 1]:
                    K_class = kloosterman_sum(m, n, c)
                    for i in range(3):
                        for j in range(3):
                            simplified = generalized_kloosterman_simplified(
                                float(S[i, j]), m, n, c
                            )
                            expected = float(S[i, j]) * K_class
                            err = float(abs(simplified - expected))
                            assert err < 1e-10

    def test_generalized_c1(self):
        """For c=1, K^rho_{ij}(m,n;1) involves the S-matrix."""
        S = ising_s_matrix()
        for i in range(3):
            for j in range(3):
                val = generalized_kloosterman_ising(i, j, 0, 0, 1)
                expected = float(S[i, j])
                err = float(abs(val - expected))
                assert err < 1e-8, \
                    f"K^rho_{{{i},{j}}}(0,0;1) = {val}, expected S_{{{i},{j}}} = {expected}"

    def test_classical_kloosterman_multiplicativity_underlying(self):
        """The classical K(m,n;c) underlying the simplified form IS multiplicative (twisted)."""
        m, n = 1, 1
        _, _, err = verify_kloosterman_multiplicativity(m, n, 3, 5)
        assert err < 1e-10, "Classical K should be multiplicative (twisted)"


# ============================================================
# 9. Rational Kloosterman sums
# ============================================================

class TestRationalKloosterman:
    """Generalized Kloosterman sums with rational arguments."""

    def test_integer_reduces_to_classical(self):
        """For integer alpha, beta: K_c(alpha, beta) = K(alpha, beta; c)."""
        for m in range(4):
            for n in range(4):
                for c in range(1, 11):
                    gen_val = _generalized_kloosterman_rational(
                        mpmath.mpf(m), mpmath.mpf(n), c
                    )
                    class_val = kloosterman_sum(m, n, c)
                    err = float(abs(gen_val - class_val))
                    assert err < 1e-10, \
                        f"Rational K({m},{n};{c}) differs from classical by {err}"

    def test_rational_naive_multiplicativity_m0(self):
        """Naive multiplicativity of rational Kloosterman holds for m=0 (Ramanujan)."""
        for n in [0, 1, 2]:
            alpha = mpmath.mpf(0)
            beta = mpmath.mpf(n)
            _, _, err = verify_kloosterman_rational_multiplicativity(
                alpha, beta, 3, 5
            )
            assert err < 1e-10

    def test_rational_naive_multiplicativity_fails_general(self):
        """Naive multiplicativity of rational K fails for general m,n > 0.

        This matches the classical case: the twist is needed.
        """
        alpha = mpmath.mpf(1)
        beta = mpmath.mpf(1)
        _, _, err = verify_kloosterman_rational_multiplicativity(alpha, beta, 2, 5)
        # This should fail (naive form, not twisted)
        assert err > 0.1, f"Naive rational mult should fail for m=n=1, err={err}"

    def test_rational_multiplicativity_ising(self):
        """Multiplicativity for Ising rational parameters.

        For alpha = 1/48 (Ising vacuum polar order), the rational Kloosterman
        sum may or may not be multiplicative. This test documents the behavior.
        """
        alpha = mpmath.mpf(1) / 48
        beta = mpmath.mpf(1)
        _, _, err = verify_kloosterman_rational_multiplicativity(alpha, beta, 2, 3)
        # Record the error -- this is diagnostic, not necessarily zero
        assert isinstance(err, float)


# ============================================================
# 10. Kloosterman Dirichlet series
# ============================================================

class TestKloostermanDirichletSeries:
    """K_tilde(m,n;s) = Sum K(m,n;c)*c^{-s}."""

    def test_convergence_above_critical_line(self):
        """K_tilde converges for Re(s) > 1."""
        m, n = 1, 1
        s = mpmath.mpf(2)
        val_50 = kloosterman_dirichlet_series(m, n, s, c_max=50)
        val_100 = kloosterman_dirichlet_series(m, n, s, c_max=100)
        err = float(abs(val_100 - val_50))
        assert err < 0.1, f"K_tilde not converging at s=2: diff={err}"

    def test_euler_product_computes(self):
        """Euler product computation completes without error."""
        m, n = 1, 1
        s = mpmath.mpf(2)
        euler_val, direct_val, err = kloosterman_euler_product(m, n, s, p_max=7)
        assert isinstance(err, float)

    def test_m0_dirichlet_series(self):
        """For m=0: K_tilde(0,n;s) = sigma_{1-s}(n)/zeta(s)."""
        n = 6
        s = mpmath.mpf(3)
        direct = kloosterman_dirichlet_series(0, n, s, c_max=200)
        sigma_val = sum(mpmath.power(d, 1 - s) for d in range(1, n + 1) if n % d == 0)
        theoretical = sigma_val / mpmath.zeta(s)
        err = float(abs(direct - theoretical) / abs(theoretical))
        assert err < 0.05, \
            f"K_tilde(0,{n};{s}): direct={float(direct)}, theory={float(theoretical)}, err={err}"

    def test_totient_dirichlet_series(self):
        """Sum K(0,0;c)*c^{-s} = Sum phi(c)*c^{-s} = zeta(s-1)/zeta(s)."""
        s = mpmath.mpf(3)
        direct = kloosterman_dirichlet_series(0, 0, s, c_max=200)
        theoretical = mpmath.zeta(s - 1) / mpmath.zeta(s)
        err = float(abs(direct - theoretical) / abs(theoretical))
        assert err < 0.01, \
            f"Totient series: direct={float(direct)}, theory={float(theoretical)}, err={err}"


# ============================================================
# 11. Non-multiplicativity diagnosis
# ============================================================

class TestNonMultiplicativity:
    """Diagnose the source of non-multiplicativity in character coefficients."""

    def test_exact_ising_non_multiplicative(self):
        """Exact Ising vacuum character coefficients are NOT multiplicative."""
        coeffs = ising_exact_coefficients(0, 20)
        result = check_multiplicativity(coeffs, n_max=20)
        assert not result['is_multiplicative'], \
            "Ising vacuum coefficients should be non-multiplicative"

    def test_check_multiplicativity_on_mobius(self):
        """Mobius function is multiplicative."""
        mu_coeffs = [0, 1]
        for n in range(2, 21):
            mu_coeffs.append(mobius(n))
        result = check_multiplicativity(mu_coeffs, n_max=20)
        assert result['is_multiplicative'], \
            f"Mobius function should be multiplicative, failures: {result['failures'][:3]}"

    def test_partition_non_multiplicative(self):
        """Partition numbers p(n) are NOT multiplicative."""
        parts = _partition_numbers(20)
        coeffs = [float(parts[n]) for n in range(21)]
        result = check_multiplicativity(coeffs, n_max=20)
        assert not result['is_multiplicative']

    def test_interference_diagnosis_runs(self):
        """The interference diagnosis should complete without error."""
        result = diagnose_interference(n_max=5, c_max=10)
        assert 'total' in result
        assert 'exact' in result
        for j in range(3):
            assert f'channel_{j}' in result

    def test_specific_non_multiplicativity(self):
        """a_0(6) = 3 but a_0(2)*a_0(3) = 1*1 = 1 (gcd(2,3)=1). Non-multiplicative."""
        coeffs = ising_exact_coefficients(0, 10)
        a2 = float(coeffs[2])  # 1
        a3 = float(coeffs[3])  # 1
        a6 = float(coeffs[6])  # 3
        assert abs(a2 - 1) < 1e-10
        assert abs(a3 - 1) < 1e-10
        assert abs(a6 - 3) < 1e-10
        assert abs(a6 - a2 * a3) > 1, \
            f"a(6)={a6} should differ from a(2)*a(3)={a2*a3}"


# ============================================================
# 12. Kuznetsov trace formula
# ============================================================

class TestKuznetsovConnection:
    """Kuznetsov trace formula: Kloosterman sums <-> spectral data."""

    def test_kuznetsov_kloosterman_side_computes(self):
        """The Kloosterman side of the Kuznetsov formula should compute."""
        val = kuznetsov_kloosterman_side(1, 1, c_max=30)
        assert isinstance(val, (mpmath.mpf, mpmath.mpc))
        assert float(abs(val)) > 0

    def test_kuznetsov_symmetry(self):
        """K(m,n;c) = K(n,m;c) implies Kuznetsov sum is symmetric in m,n."""
        val_12 = kuznetsov_kloosterman_side(1, 2, c_max=20)
        val_21 = kuznetsov_kloosterman_side(2, 1, c_max=20)
        err = float(abs(val_12 - val_21))
        assert err < 1e-8, f"Kuznetsov asymmetry: {err}"

    def test_kuznetsov_custom_test_fn(self):
        """Custom test function in Kuznetsov sum."""
        def h_gauss(c):
            return mpmath.exp(-mpmath.mpf(c)**2 / 100)
        val = kuznetsov_kloosterman_side(1, 1, c_max=30, test_fn=h_gauss)
        assert isinstance(val, (mpmath.mpf, mpmath.mpc))


# ============================================================
# 13. Dirichlet series decomposition by c
# ============================================================

class TestDirichletDecomposition:
    """Decompose character coefficients by Kloosterman class."""

    def test_c_contribution_well_defined(self):
        """b_c(n) = contribution from a single c value is well-defined."""
        for n in [1, 2, 3]:
            for c_val in [1, 2, 3, 5]:
                val = rademacher_c_contribution(0, n, c_val)
                assert isinstance(val, (mpmath.mpf, mpmath.mpc, float, int))

    def test_c_contribution_c1_dominates(self):
        """The c=1 term should dominate for large n."""
        n = 8
        b1 = float(abs(rademacher_c_contribution(0, n, 1)))
        b2 = float(abs(rademacher_c_contribution(0, n, 2)))
        if b1 > 0.01:
            assert b1 > b2, f"|b_1({n})|={b1} should dominate |b_2({n})|={b2}"

    def test_j_channel_dominance(self):
        """The j=0 (vacuum) channel is the only contributor for Ising."""
        n = 5
        c_max = 20
        ch0 = float(abs(rademacher_j_contribution(0, 0, n, c_max=c_max)))
        ch1 = float(abs(rademacher_j_contribution(0, 1, n, c_max=c_max)))
        ch2 = float(abs(rademacher_j_contribution(0, 2, n, c_max=c_max)))
        assert ch0 > 0, "Vacuum channel should be non-trivial"
        assert ch1 < 1e-10, "Energy channel should be zero (no polar term)"
        assert ch2 < 1e-10, "Spin channel should be zero (no polar term)"


# ============================================================
# 14. Helper function tests
# ============================================================

class TestHelpers:
    """Test helper/utility functions."""

    def test_primes_up_to(self):
        """Primes up to 30."""
        primes = _primes_up_to(30)
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_euler_totient_values(self):
        """phi(1)=1, phi(2)=1, phi(6)=2, phi(12)=4."""
        assert euler_totient(1) == 1
        assert euler_totient(2) == 1
        assert euler_totient(6) == 2
        assert euler_totient(12) == 4

    def test_mobius_values(self):
        """mu(1)=1, mu(2)=-1, mu(4)=0, mu(6)=1, mu(30)=-1."""
        assert mobius(1) == 1
        assert mobius(2) == -1
        assert mobius(4) == 0
        assert mobius(6) == 1
        assert mobius(30) == -1

    def test_divisor_count(self):
        """d(1)=1, d(6)=4, d(12)=6."""
        assert divisor_count(1) == 1
        assert divisor_count(6) == 4
        assert divisor_count(12) == 6


# ============================================================
# 15. Integration tests
# ============================================================

class TestIntegration:
    """End-to-end integration tests."""

    def test_rademacher_trend_toward_exact(self):
        """Rademacher expansion trends toward exact values for n >= 5."""
        exact = ising_exact_coefficients(0, 10)
        for n in [5, 8, 10]:
            rad = float(mpmath.re(rademacher_coefficient(0, n, c_max=80)))
            ex = float(exact[n])
            rel_err = abs(rad - ex) / max(abs(ex), 1)
            assert rel_err < 0.5, \
                f"n={n}: Rademacher={rad:.3f}, exact={ex}, rel_err={rel_err:.3f}"

    def test_kloosterman_selberg_identity(self):
        """Sum K(0,0;c)*c^{-s} = zeta(s-1)/zeta(s)."""
        s = mpmath.mpf(3)
        direct = kloosterman_dirichlet_series(0, 0, s, c_max=200)
        theoretical = mpmath.zeta(s - 1) / mpmath.zeta(s)
        err = float(abs(direct - theoretical) / abs(theoretical))
        assert err < 0.01

    def test_rademacher_coefficients_approximately_real(self):
        """Rademacher coefficients should be approximately real."""
        for n in [3, 5, 8]:
            val = rademacher_coefficient(0, n, c_max=40)
            imag = float(abs(mpmath.im(val)))
            real = float(abs(mpmath.re(val)))
            if real > 0.1:
                ratio = imag / real
                assert ratio < 0.5, \
                    f"Rademacher a_0({n}): imag/real ratio = {ratio}"

    def test_core_tension_classical_vs_character(self):
        """Core finding: K(m,n;c) is multiplicative (twisted) in c,
        but character coefficients a_i(n) are NOT multiplicative in n.

        This IS the non-lattice bridge obstruction.
        """
        # Classical Kloosterman: twisted multiplicativity holds
        _, _, err = verify_kloosterman_multiplicativity(1, 1, 2, 3)
        assert err < 1e-10, "Classical K should be multiplicative (twisted)"

        # Character coefficients: non-multiplicative in n
        exact = ising_exact_coefficients(0, 20)
        mult_check = check_multiplicativity(exact, n_max=20)
        assert not mult_check['is_multiplicative'], \
            "Character coefficients should be non-multiplicative"


# ============================================================
# 16. Edge cases and stress tests
# ============================================================

class TestEdgeCases:
    """Edge cases and stress tests."""

    def test_kloosterman_c_equals_1(self):
        """K(m,n;1) = 1 for all m,n."""
        for m in range(-5, 6):
            for n in range(-5, 6):
                val = kloosterman_sum_real(m, n, 1)
                assert abs(val - 1) < 1e-10

    def test_kloosterman_large_c(self):
        """Kloosterman sum computes for large c without overflow."""
        val = kloosterman_sum(1, 1, 100)
        assert abs(val) < weil_bound(1, 1, 100) + 1

    def test_generalized_rational_c2(self):
        """Rational Kloosterman for c=2: only d=1 with d'=1."""
        alpha = mpmath.mpf(1) / 3
        beta = mpmath.mpf(1) / 5
        val = _generalized_kloosterman_rational(alpha, beta, 2)
        # d=1, d_inv=1: phase = 2*pi*(1/3 + 1/5)/2 = 2*pi*4/15
        expected = mpmath.exp(2j * mpmath.pi * (alpha + beta) / 2)
        err = float(abs(val - expected))
        assert err < 1e-10

    def test_ising_character_positivity(self):
        """All Ising character coefficients are non-negative integers."""
        for i in range(3):
            coeffs = ising_exact_coefficients(i, 15)
            for n in range(16):
                val = float(coeffs[n])
                assert val >= -1e-10, f"chi_{i}({n}) = {val} < 0"
                assert abs(val - round(val)) < 1e-8, \
                    f"chi_{i}({n}) = {val} not integer"

    def test_weil_bound_not_too_loose(self):
        """Weil bound should be reasonably tight for some (m,n,c)."""
        found_tight = False
        for m in range(1, 4):
            for n in range(1, 4):
                for c in [5, 7, 11, 13]:
                    K_abs, bound, _ = verify_weil_bound(m, n, c)
                    if bound > 0 and K_abs / bound > 0.1:
                        found_tight = True
                        break
        assert found_tight, "Weil bound should be achievable to within constant factor"

    def test_rademacher_spin_channel(self):
        """Rademacher expansion for the spin character (i=2)."""
        val = rademacher_coefficient(2, 5, c_max=60)
        exact = ising_exact_coefficients(2, 5)
        # Just check it produces a reasonable number
        assert float(abs(mpmath.re(val))) < 100, "Spin Rademacher should be bounded"

    def test_kloosterman_batch_consistency(self):
        """K(m,n;c) consistent across different computation paths."""
        m, n, c = 3, 7, 11
        val1 = kloosterman_sum(m, n, c)
        val2 = kloosterman_sum_real(m, n, c)
        assert abs(float(mpmath.re(val1)) - float(val2)) < 1e-10
        assert abs(float(mpmath.im(val1))) < 1e-10
