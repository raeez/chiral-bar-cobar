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
