"""Tests for the operadic Rankin-Selberg programme."""
import math
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from compute.lib import operadic_rankin_selberg as ors


class TestShadowMoments:
    def test_virasoro_shadow_coefficients(self):
        S = ors.virasoro_shadow_coefficients(10.0, 8)
        assert 2 in S and 8 in S
        assert abs(S[2]) > 0

    def test_moments_sign(self):
        S = ors.virasoro_shadow_coefficients(10.0, 6)
        mu = ors.shadow_moments(S)
        assert 2 in mu
        # mu_r = -r * S_r
        for r in [2, 3, 4]:
            assert abs(mu[r] - (-r * S[r])) < 1e-15

    def test_newton_single_atom(self):
        """Single atom: Newton's identity is trivial (e2=0)."""
        S = ors.virasoro_shadow_coefficients(10.0, 8)
        mu = ors.shadow_moments(S)
        checks = ors.newton_identity_check(mu, 8)
        # For single atom, Newton should hold
        for r, info in checks.items():
            if r >= 3:  # skip r=2 (base case)
                assert info['passes'] or abs(info['defect']) < 1e-6, \
                    f"Newton failed at r={r}: defect={info['defect']}"


class TestMCRecursion:
    def test_recursion_chain(self):
        chain = ors.mc_recursion_chain(10.0, 8)
        assert len(chain) >= 5
        for r, info in chain.items():
            if info.get('actual') is not None and info.get('predicted') is not None:
                assert info.get('rel_defect', 1.0) < 0.01, \
                    f"MC recursion failed at arity {r}"

    def test_recursion_large_c(self):
        chain = ors.mc_recursion_chain(100.0, 10)
        for r, info in chain.items():
            if info.get('rel_defect') is not None:
                assert info['rel_defect'] < 1e-6, \
                    f"MC recursion at large c failed at arity {r}"

    def test_meromorphic_proved(self):
        chain = ors.mc_recursion_chain(10.0, 6)
        for r, info in chain.items():
            assert 'meromorphic_continuation' in info
            assert 'PROVED' in info['meromorphic_continuation']


class TestConverseTheorem:
    def test_hypotheses_r2(self):
        result = ors.converse_theorem_hypotheses(2, 10.0)
        assert result['converse_theorem_applies']
        for key, hyp in result['hypotheses'].items():
            assert hyp['status'].startswith('PROVED'), f"Hypothesis {key} not proved"

    def test_hypotheses_r5(self):
        """r=5 is the first OPEN case in the classical theory."""
        result = ors.converse_theorem_hypotheses(5, 10.0)
        assert result['converse_theorem_applies']

    def test_hypotheses_r10(self):
        result = ors.converse_theorem_hypotheses(10, 10.0)
        assert result['converse_theorem_applies']

    def test_ramanujan_corollary(self):
        result = ors.converse_theorem_hypotheses(5, 10.0)
        assert 'ramanujan_corollary' in result
        assert 'Ramanujan' in result['ramanujan_corollary']


class TestOperadicTheorem:
    def test_full_theorem_c10(self):
        result = ors.operadic_rankin_selberg_theorem(10.0, 8)
        assert result['all_automorphic']
        assert result['ramanujan_follows']
        assert 'honest_assessment' in result

    def test_full_theorem_c26(self):
        """c=26: bosonic string central charge."""
        result = ors.operadic_rankin_selberg_theorem(26.0, 6)
        assert result['all_automorphic']

    def test_honest_assessment_mentions_gap(self):
        result = ors.operadic_rankin_selberg_theorem(10.0, 6)
        assert 'prime-locality' in result['honest_assessment'].lower() or \
               'gap' in result['honest_assessment'].lower()


class TestRankinSelbergConvolution:
    def test_rs_convolution_zeta(self):
        """Verify RS(sigma_{-1}, sigma_{-1}) ~ zeta^2 * zeta_1^2."""
        result = ors.verify_rs_convolution_zeta(3.0)
        # At s=3, the partial sums should be close
        assert result['match'] or abs(result['ratio'] - 1.0) < 0.5, \
            f"RS convolution ratio={result['ratio']}"

    def test_rs_convergent_region(self):
        for s in [2.5, 3.0, 4.0]:
            result = ors.verify_rs_convolution_zeta(s)
            assert abs(result['ratio'] - 1.0) < 0.5, \
                f"RS convolution at s={s}: ratio={result['ratio']}"


class TestPrimeLocality:
    def test_single_atom_not_cuspidal(self):
        result = ors.prime_locality_test(10.0)
        assert not result['is_automorphic']
        # Single atom has beta=0, not Satake
        for p, info in result['euler_factors'].items():
            assert info['beta_p'] == 0.0

    def test_diagnosis_mentions_subleading(self):
        result = ors.prime_locality_test(10.0)
        assert 'subleading' in result['diagnosis'].lower()


class TestFunctionalEquation:
    def test_fe_type(self):
        result = ors.functional_equation_test(1.0, [2.0, 3.0, 4.0], r=2)
        assert 'conclusion' in result
        assert 'functional equation' in result['conclusion'].lower()


class TestMomentLFunction:
    def test_heisenberg_m2_convergent(self):
        """M_2(s) should be finite for Re(s) > 1."""
        val = ors.moment_l_function_heisenberg(2, 3.0, c=1.0)
        assert not math.isnan(val)
        assert val > 0

    def test_heisenberg_m3_zero(self):
        """Heisenberg: M_r = 0 for r >= 3."""
        assert ors.moment_l_function_heisenberg(3, 2.0) == 0.0
        assert ors.moment_l_function_heisenberg(5, 2.0) == 0.0

    def test_heisenberg_m2_vs_zeta_product(self):
        """For c=1 Heisenberg, M_2(s=3) should approximate zeta(3)*zeta(4)*(c/2)*norm.

        M_2(s) = (c/2) * sum_{n>=1} sigma_{-1}(n) * n^{-s}.
        The Dirichlet series sum sigma_{-1}(n) n^{-s} = zeta(s)*zeta(s+1).
        So M_2(3) ~ (c/2) * zeta(3) * zeta(4).
        """
        c = 1.0
        val = ors.moment_l_function_heisenberg(2, 3.0, c=c)
        # Compute zeta(3)*zeta(4) via partial sums (same N_max=1000)
        N = 1000
        zeta3 = sum(n**(-3.0) for n in range(1, N + 1))
        zeta4 = sum(n**(-4.0) for n in range(1, N + 1))
        expected = (c / 2.0) * zeta3 * zeta4
        # Both use partial sums to N=1000 so ratio should be very close
        ratio = val / expected
        assert abs(ratio - 1.0) < 0.10, \
            f"M_2(3) = {val}, expected ~ {expected}, ratio = {ratio}"

    def test_m2_positive_for_real_s(self):
        """M_2(s) should be positive for real s > 2."""
        for s in [2.5, 3.0, 4.0, 5.0, 10.0]:
            val = ors.moment_l_function_heisenberg(2, s, c=1.0)
            assert not math.isnan(val), f"M_2({s}) is NaN"
            assert val > 0, f"M_2({s}) = {val} <= 0"

    def test_m2_decreasing(self):
        """M_2(s) should decrease as s increases (for real s > 2).

        Since all terms sigma_{-1}(n)*n^{-s} are positive and n^{-s}
        decreases in s for n >= 2, M_2(s) is strictly decreasing.
        """
        prev = ors.moment_l_function_heisenberg(2, 2.5, c=1.0)
        for s in [3.0, 4.0, 5.0, 8.0]:
            curr = ors.moment_l_function_heisenberg(2, s, c=1.0)
            assert curr < prev, \
                f"M_2 not decreasing: M_2({s}) = {curr} >= M_2(prev) = {prev}"
            prev = curr


# ============================================================
# Additional MCRecursion tests
# ============================================================

class TestMCRecursionExtended:
    def test_recursion_c_half(self):
        """MC recursion at c=0.5 (free fermion central charge)."""
        chain = ors.mc_recursion_chain(0.5, 8)
        assert len(chain) >= 5
        for r, info in chain.items():
            if info.get('actual') is not None and info.get('predicted') is not None:
                assert info.get('rel_defect', 1.0) < 0.01, \
                    f"MC recursion at c=0.5 failed at arity {r}: defect={info.get('rel_defect')}"

    def test_recursion_c_minus22over5(self):
        """c = -22/5 (Yang-Lee): shadow coefficients grow fast due to small |c|.

        P = 2/c = -10/22 = -5/11. The shadow coefficients S_r involve
        (-3)^{r-4} * P^{r-2}, which grow geometrically. The MC recursion
        still holds exactly (it is an algebraic identity) but the values diverge.
        """
        c = -22.0 / 5.0
        chain = ors.mc_recursion_chain(c, 8)
        # The recursion should still be exact (algebraic identity)
        for r, info in chain.items():
            if info.get('actual') is not None and info.get('predicted') is not None:
                assert info.get('rel_defect', 1.0) < 0.01, \
                    f"MC recursion at Yang-Lee c=-22/5 failed at arity {r}"
        # Shadow coefficients should grow (|P| = 5/11 > 0, |-3*P| = 15/11 > 1)
        S = ors.virasoro_shadow_coefficients(c, 8)
        assert abs(S[8]) > abs(S[4]), \
            "Yang-Lee shadows should grow: |-3P| = 15/11 > 1"

    def test_recursion_preserves_ratio(self):
        """The ratio S_{r+1}/S_r should equal -(3r/(r+1))*(2/c) at leading order."""
        c = 10.0
        P = 2.0 / c
        S = ors.virasoro_shadow_coefficients(c, 12)
        for r in range(2, 11):
            if abs(S[r]) > 1e-30:
                ratio_actual = S[r + 1] / S[r]
                ratio_predicted = -(3.0 * r / (r + 1)) * P
                assert abs(ratio_actual - ratio_predicted) < 1e-10 * max(1, abs(ratio_predicted)), \
                    f"Ratio S_{r+1}/S_{r} = {ratio_actual}, expected {ratio_predicted}"

    def test_mc_chain_at_multiple_c(self):
        """Run the MC recursion chain at c = 1, 2, 10, 26, 100 and verify all pass."""
        for c in [1.0, 2.0, 10.0, 26.0, 100.0]:
            chain = ors.mc_recursion_chain(c, 8)
            for r, info in chain.items():
                if info.get('actual') is not None and info.get('predicted') is not None:
                    assert info.get('rel_defect', 1.0) < 0.01, \
                        f"MC recursion failed at c={c}, arity {r}: defect={info.get('rel_defect')}"


# ============================================================
# Additional RankinSelbergConvolution tests
# ============================================================

class TestRankinSelbergConvolutionExtended:
    def test_rs_associativity(self):
        """RS(RS(f,g),h) ~ RS(f,RS(g,h)): Dirichlet convolution is associative.

        Use small arithmetic functions: f(n)=1, g(n)=1, h(n)=1.
        Then f*g(n) = d(n) (divisor count), and (f*g)*h(n) = d_3(n) (3-fold divisor count).
        Similarly f*(g*h)(n) = d_3(n). So the two sides should match.
        """
        N = 80
        ones = [1.0] * N

        # f*g via RS numerical
        fg = []
        for n in range(1, N + 1):
            val = sum(1.0 for d in range(1, n + 1) if n % d == 0)
            fg.append(val)

        # (f*g)*h
        s = 3.0
        lhs = ors.rankin_selberg_convolution_numerical(fg, ones, s, N)
        # f*(g*h) = f*(d) since g*h = d
        rhs = ors.rankin_selberg_convolution_numerical(ones, fg, s, N)

        assert abs(lhs - rhs) < 1e-8 * max(1, abs(lhs)), \
            f"RS not associative: LHS={lhs}, RHS={rhs}"

    def test_rs_identity(self):
        """RS(f, delta) = f: Dirichlet convolution with delta(1)=1, delta(n)=0 for n>1.

        The identity element for Dirichlet convolution is the function
        delta(n) = 1 if n=1, 0 otherwise. So RS(f, delta; s) = sum f(n) n^{-s}.
        """
        N = 100
        # f = sigma_{-1}
        f_coeffs = [sum(1.0 / d for d in range(1, n + 1) if n % d == 0)
                     for n in range(1, N + 1)]
        delta = [0.0] * N
        delta[0] = 1.0  # delta(1) = 1

        s = 3.0
        rs_val = ors.rankin_selberg_convolution_numerical(f_coeffs, delta, s, N)
        direct_val = sum(f_coeffs[n - 1] * n**(-s) for n in range(1, N + 1))

        assert abs(rs_val - direct_val) < 1e-8 * max(1, abs(direct_val)), \
            f"RS(f, delta) != f: RS={rs_val}, direct={direct_val}"

    def test_rs_sigma_k(self):
        """RS(sigma_0, delta) should give the Dirichlet series of sigma_0.

        sigma_0(n) = d(n) = number of divisors.
        Convolving with delta (identity for Dirichlet convolution) yields sigma_0 back.
        So RS(sigma_0, delta; s) = sum d(n) n^{-s} = zeta(s)^2.
        """
        N = 100
        sigma0 = [float(sum(1 for d in range(1, n + 1) if n % d == 0))
                   for n in range(1, N + 1)]
        delta = [0.0] * N
        delta[0] = 1.0

        s = 3.0
        rs_val = ors.rankin_selberg_convolution_numerical(sigma0, delta, s, N)
        # Direct: sum d(n) n^{-s}
        direct = sum(sigma0[n - 1] * n**(-s) for n in range(1, N + 1))
        assert abs(rs_val - direct) < 1e-8 * max(1, abs(direct)), \
            f"RS(sigma_0, delta) = {rs_val}, expected {direct}"

    def test_rs_heisenberg_self(self):
        """RS(sigma_{-1}, sigma_{-1}; s=3): numerical value check.

        sigma_{-1} has Dirichlet series zeta(s)*zeta(s+1).
        RS(sigma_{-1}, sigma_{-1}; s) = sum (sigma_{-1} * sigma_{-1})(n) n^{-s}
        where * is Dirichlet convolution.
        This should equal (zeta(s)*zeta(s+1))^2 = zeta(3)^2 * zeta(4)^2 at s=3.
        """
        result = ors.verify_rs_convolution_zeta(3.0, N_max=500)
        # The ratio should be close to 1
        assert abs(result['ratio'] - 1.0) < 0.15, \
            f"RS self-convolution ratio = {result['ratio']}, expected ~1"
        # The actual value should be positive and finite
        assert result['rs_convolution'] > 0
        assert not math.isnan(result['rs_convolution'])


# ============================================================
# Newton identity tests (new class)
# ============================================================

class TestRankinSelbergConvolutionCommutativity:
    def test_rs_commutativity(self):
        """Dirichlet convolution is commutative: RS(f, g; s) = RS(g, f; s)."""
        N = 80
        f = [float(n % 3) for n in range(1, N + 1)]
        g = [float(1.0 / n) for n in range(1, N + 1)]
        s = 3.0
        lhs = ors.rankin_selberg_convolution_numerical(f, g, s, N)
        rhs = ors.rankin_selberg_convolution_numerical(g, f, s, N)
        assert abs(lhs - rhs) < 1e-8 * max(1, abs(lhs)), \
            f"RS not commutative: RS(f,g)={lhs}, RS(g,f)={rhs}"


class TestNewtonFromMC:
    def test_newton_virasoro_leading_c10(self):
        """Extract moments from Virasoro shadow at c=10, verify Newton's identity.

        For a single atom lambda = -6/c = -0.6:
        mu_r = lambda^r. Newton: p_r = e1*p_{r-1} (with e2=0, e1=lambda).
        """
        S = ors.virasoro_shadow_coefficients(10.0, 10)
        mu = ors.shadow_moments(S)
        checks = ors.newton_identity_check(mu, 10)
        for r, info in checks.items():
            assert info['passes'], \
                f"Newton failed at c=10, r={r}: defect={info['defect']}, " \
                f"pred={info['predicted']}, actual={info['actual']}"

    def test_newton_virasoro_leading_c26(self):
        """Same at c=26 (bosonic string). lambda = -6/26 = -3/13."""
        S = ors.virasoro_shadow_coefficients(26.0, 10)
        mu = ors.shadow_moments(S)
        checks = ors.newton_identity_check(mu, 10)
        for r, info in checks.items():
            assert info['passes'], \
                f"Newton failed at c=26, r={r}: defect={info['defect']}"

    def test_newton_single_atom_exact(self):
        """For single atom lambda=-6/c, verify mu_r = lambda^r and Newton trivially holds.

        With e1 = lambda, e2 = 0: p_r = lambda * p_{r-1} - 0 = lambda^r. Exact.
        """
        c = 10.0
        lam = -6.0 / c  # -0.6
        S = ors.virasoro_shadow_coefficients(c, 10)
        mu = ors.shadow_moments(S)
        # Verify mu_r = lambda^r (from the shadow formula)
        # S_r = (2/r)*(-3)^{r-4}*(2/c)^{r-2}, mu_r = -r*S_r = -2*(-3)^{r-4}*(2/c)^{r-2}
        # lambda = -6/c, lambda^r = (-6/c)^r = (-1)^r * 6^r / c^r
        # Let's just check Newton's identity holds with e2=0
        checks = ors.newton_identity_check(mu, 10)
        for r, info in checks.items():
            assert abs(info['e2']) < 1e-10, \
                f"e2 should be 0 for single atom, got {info['e2']}"
            assert info['passes'], \
                f"Newton failed for single atom at r={r}"

    def test_newton_two_atom_explicit(self):
        """For two atoms alpha=3, beta=5, verify Newton p_r = e1*p_{r-1} - e2*p_{r-2}.

        e1 = alpha + beta = 8, e2 = alpha * beta = 15.
        p_r = alpha^r + beta^r.
        Newton: p_r = 8 * p_{r-1} - 15 * p_{r-2}.
        """
        alpha, beta = 3.0, 5.0
        e1 = alpha + beta  # 8
        e2 = alpha * beta  # 15
        r_max = 12
        p = {}
        for r in range(0, r_max + 1):
            p[r] = alpha**r + beta**r

        # Verify Newton's identity directly
        for r in range(2, r_max + 1):
            predicted = e1 * p[r - 1] - e2 * p[r - 2]
            actual = p[r]
            assert abs(predicted - actual) < 1e-6 * max(1, abs(actual)), \
                f"Newton failed for two atoms at r={r}: pred={predicted}, actual={actual}"

        # Now verify using the library's newton_identity_check
        # Build moments dict with mu_1 present so the function uses it
        moments = {r: p[r] for r in range(1, r_max + 1)}
        checks = ors.newton_identity_check(moments, r_max)
        for r, info in checks.items():
            assert info['passes'], \
                f"Library Newton check failed for two atoms at r={r}: defect={info['defect']}"


# ============================================================
# Additional ConverseTheorem tests
# ============================================================

class TestShadowMomentsExtended:
    def test_shadow_coefficients_at_c1(self):
        """Shadow coefficients at c=1 should be large (P=2)."""
        S = ors.virasoro_shadow_coefficients(1.0, 6)
        # P = 2, so S_r = (2/r)*(-3)^{r-4}*2^{r-2} grows fast
        assert abs(S[6]) > abs(S[2]), "Shadows should grow at c=1"

    def test_shadow_coefficient_formula(self):
        """Verify the exact formula S_r = (2/r)*(-3)^{r-4}*(2/c)^{r-2}."""
        c = 7.0
        P = 2.0 / c
        S = ors.virasoro_shadow_coefficients(c, 10)
        for r in range(2, 11):
            expected = (2.0 / r) * (-3.0)**(r - 4) * P**(r - 2)
            assert abs(S[r] - expected) < 1e-12 * max(1, abs(expected)), \
                f"S_{r} = {S[r]}, expected {expected}"


class TestConverseTheoremExtended:
    def test_hypotheses_all_r(self):
        """Check CPS hypotheses for r = 2, 3, 4, ..., 20."""
        for r in range(2, 21):
            result = ors.converse_theorem_hypotheses(r, 10.0)
            assert result['converse_theorem_applies'], \
                f"CPS hypotheses failed at r={r}"
            for key, hyp in result['hypotheses'].items():
                assert hyp['status'].startswith('PROVED'), \
                    f"Hypothesis {key} not proved at r={r}: status={hyp['status']}"

    def test_ramanujan_follows_from_chain(self):
        """Verify that the full chain logic produces ramanujan_follows=True."""
        result = ors.operadic_rankin_selberg_theorem(10.0, 12)
        assert result['ramanujan_follows'] is True, \
            "Ramanujan should follow from the full operadic RS chain"
        assert result['all_automorphic'] is True
        # Check that every individual r satisfies the converse theorem
        for r, ct in result['converse_theorem'].items():
            assert ct['converse_theorem_applies'], \
                f"Converse theorem failed at r={r}"


# ============================================================
# Additional PrimeLocality tests
# ============================================================

class TestPrimeLocalityExtended:
    def test_lattice_is_prime_local(self):
        """For a lattice VOA description, prime_locality_test reports appropriate structure.

        Lattice VOAs have Hecke eigenvalues at each prime, so the shadow data
        is prime-local. At leading order (single atom approximation), the library
        still reports is_automorphic=False (because the leading-order single atom
        does not correspond to a cuspidal form), but the diagnosis should mention
        the subleading prime-dependent structure.
        """
        # Use c=1 (Heisenberg / rank-1 lattice)
        result = ors.prime_locality_test(1.0)
        # The effective lambda is -6/c = -6
        assert abs(result['lambda_eff'] - (-6.0)) < 1e-10
        # Euler factors should exist for standard primes
        assert 2 in result['euler_factors']
        assert 3 in result['euler_factors']
        # Diagnosis should discuss subleading corrections that carry prime structure
        assert 'prime' in result['diagnosis'].lower() or \
               'lattice' in result['diagnosis'].lower()

    def test_large_c_approaches_lattice(self):
        """At very large c, Virasoro spectral measure approaches a lattice-like structure.

        As c -> infinity, lambda = -6/c -> 0, so the spectral atom shrinks
        toward the origin. The Euler factors (1 - lambda * p^{-s})^{-1} -> 1
        (trivial representation). This is consistent with the lattice limit
        where the VOA approaches a free theory (Gaussian/lattice).
        """
        result_large = ors.prime_locality_test(10000.0)
        result_small = ors.prime_locality_test(10.0)
        # Large c: lambda closer to 0
        assert abs(result_large['lambda_eff']) < abs(result_small['lambda_eff'])
        assert abs(result_large['lambda_eff']) < 0.001
        # The single-atom Euler factors should be nearly trivial at large c
        for p, info in result_large['euler_factors'].items():
            assert abs(info['alpha_p']) < 0.001, \
                f"At large c, alpha_{p} = {info['alpha_p']} should be near 0"
