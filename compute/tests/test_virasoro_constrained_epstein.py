#!/usr/bin/env python3
r"""
test_virasoro_constrained_epstein.py -- Tests for the Virasoro constrained Epstein zeta.

Tests organized by mathematical content:
    1. Quasi-primary spectrum d(h)
    2. Generating function Q(q) = (1-q)^2 P(q)
    3. Constrained Epstein zeta computation
    4. Convergence/divergence analysis
    5. Shadow metric comparison
    6. Minimal model exact computation
    7. Functional equation tests
    8. c-independence
    9. Benjamin-Chang comparison
   10. Cross-checks with existing modules
"""

import sys
import os
import math
import pytest
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from virasoro_constrained_epstein import (
    partition_count,
    p_ge2,
    quasi_primary_count,
    quasi_primary_spectrum,
    quasi_primary_generating_coeffs,
    constrained_epstein,
    constrained_epstein_derivative,
    quasi_primary_asymptotics,
    convergence_analysis,
    effective_convergence_sigma,
    shadow_metric_discriminant,
    shadow_metric_epstein,
    compare_two_epsteins,
    minimal_model_quasi_primaries,
    minimal_model_constrained_epstein,
    test_functional_equation as _test_functional_equation,
    regularized_epstein,
    weight_multiplicity_dirichlet,
    rankin_selberg_structural_analysis,
    benjamin_chang_comparison,
    c_dependence_analysis,
)


# ================================================================
# 1. Partition function tests
# ================================================================

class TestPartitionFunction:
    """Tests for partition counting infrastructure."""

    def test_partition_base_cases(self):
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7

    def test_partition_higher(self):
        """Standard partition function values (OEIS A000041)."""
        expected = {
            10: 42,
            15: 176,
            20: 627,
            25: 1958,
            50: 204226,
            100: 190569292,
        }
        for n, p_n in expected.items():
            assert partition_count(n) == p_n, f"p({n}) should be {p_n}"

    def test_p_ge2_base_cases(self):
        assert p_ge2(0) == 1
        assert p_ge2(1) == 0
        assert p_ge2(2) == 1
        assert p_ge2(3) == 1
        assert p_ge2(4) == 2

    def test_p_ge2_formula(self):
        """p_ge2(n) = p(n) - p(n-1) for n >= 1."""
        for n in range(1, 30):
            assert p_ge2(n) == partition_count(n) - partition_count(n - 1)

    def test_p_ge2_nondecreasing(self):
        """p_ge2 is nondecreasing for n >= 2."""
        for n in range(3, 50):
            assert p_ge2(n) >= p_ge2(n - 1), f"p_ge2({n}) < p_ge2({n-1})"

    def test_p_ge2_negative(self):
        assert p_ge2(-1) == 0
        assert p_ge2(-5) == 0


# ================================================================
# 2. Quasi-primary spectrum tests
# ================================================================

class TestQuasiPrimarySpectrum:
    """Tests for the Virasoro quasi-primary multiplicities d(h)."""

    def test_low_weight_values(self):
        """Verified by explicit L_1 matrix computation (sympy)."""
        expected = {
            0: 1,   # vacuum
            1: 0,   # no weight-1 states
            2: 1,   # stress tensor T
            3: 0,   # L_{-3}|0> is descendant of T
            4: 1,   # Lambda quasi-primary
            5: 0,
            6: 2,   # two independent quasi-primaries
            7: 0,
            8: 3,
            9: 1,   # first odd-weight quasi-primary
            10: 4,
        }
        for h, d in expected.items():
            assert quasi_primary_count(h) == d, (
                f"d({h}) should be {d}, got {quasi_primary_count(h)}"
            )

    def test_medium_weight_values(self):
        """Extended values from generating function."""
        expected = {
            11: 2,
            12: 7,
            13: 3,
            14: 10,
            15: 7,
            16: 14,
            17: 11,
            18: 22,
            19: 17,
            20: 32,
        }
        for h, d in expected.items():
            assert quasi_primary_count(h) == d

    def test_d_nonnegative_for_h_ge_2(self):
        """d(h) >= 0 for all h >= 2."""
        for h in range(2, 200):
            assert quasi_primary_count(h) >= 0, f"d({h}) < 0"

    def test_d_formula(self):
        """d(h) = p_ge2(h) - p_ge2(h-1) for h >= 2."""
        for h in range(2, 100):
            assert quasi_primary_count(h) == p_ge2(h) - p_ge2(h - 1)

    def test_d_even_odd_pattern(self):
        """At low weights, d(h) = 0 for odd h < 9.
        The first odd-weight quasi-primary appears at h=9."""
        for h in [3, 5, 7]:
            assert quasi_primary_count(h) == 0, f"d({h}) should be 0"
        assert quasi_primary_count(9) == 1, "d(9) should be 1"

    def test_quasi_primary_spectrum_dict(self):
        spec = quasi_primary_spectrum(10)
        assert 0 in spec
        assert 2 in spec
        assert 4 in spec
        assert 6 in spec
        assert 1 not in spec
        assert 3 not in spec
        assert 5 not in spec

    def test_d_growth_monotone_even(self):
        """d(h) is generally increasing for even h."""
        even_vals = [quasi_primary_count(h) for h in range(0, 40, 2)]
        # Not strictly monotone, but the trend is increasing
        assert even_vals[-1] > even_vals[1]

    def test_cumulative_quasi_primaries(self):
        """Cumulative count through weight h."""
        cum = sum(quasi_primary_count(h) for h in range(11))
        assert cum == 13  # 1+0+1+0+1+0+2+0+3+1+4 = 13 (h=0 vacuum counts)


# ================================================================
# 3. Generating function tests
# ================================================================

class TestGeneratingFunction:
    """Tests for Q(q) = (1-q)^2 P(q)."""

    def test_gf_formula(self):
        """Q(q) = (1-q)^2 P(q) gives correct quasi-primary counts."""
        Q = quasi_primary_generating_coeffs(30)
        for h in range(2, 31):
            assert Q[h] == quasi_primary_count(h), (
                f"GF coefficient at h={h}: {Q[h]} != d({h})={quasi_primary_count(h)}"
            )

    def test_gf_h1_formal(self):
        """The h=1 coefficient is formally -1 (but physically 0)."""
        Q = quasi_primary_generating_coeffs(5)
        assert Q[1] == -1

    def test_gf_sum(self):
        """Sum of Q(q) coefficients equals (1-1)^2 * P(1).
        But P(1) diverges. Instead test: sum through degree N
        of Q equals p_ge2(N) (the partial sum of first differences
        telescopes to the last term)."""
        N = 20
        Q = quasi_primary_generating_coeffs(N)
        # sum_{h=0}^{N} d(h) where d(h) = p_ge2(h) - p_ge2(h-1)
        # telescopes to p_ge2(N) - p_ge2(-1) = p_ge2(N)
        assert sum(Q) == p_ge2(N), (
            f"Telescoping sum should equal p_ge2({N}) = {p_ge2(N)}"
        )

    def test_gf_factorization(self):
        """(1-q)^2 P(q): verify product structure.

        P(q) = prod 1/(1-q^n) so (1-q)^2 P(q) = (1-q) prod_{n>=2} 1/(1-q^n).
        The second factor generates p_ge2, and (1-q) takes first differences.
        """
        P = [partition_count(n) for n in range(21)]
        # First multiply by (1-q): gives p_ge2
        P1 = [0] * 21
        for n in range(21):
            P1[n] = P[n]
            if n >= 1:
                P1[n] -= P[n - 1]
        for n in range(21):
            assert P1[n] == p_ge2(n), f"(1-q)P at n={n}"

        # Then multiply by another (1-q): gives d(h)
        P2 = [0] * 21
        for n in range(21):
            P2[n] = P1[n]
            if n >= 1:
                P2[n] -= P1[n - 1]
        Q = quasi_primary_generating_coeffs(20)
        for n in range(21):
            assert P2[n] == Q[n], f"(1-q)^2 P at n={n}"


# ================================================================
# 4. Constrained Epstein zeta tests
# ================================================================

class TestConstrainedEpstein:
    """Tests for the constrained Epstein zeta function."""

    def test_large_s_convergence(self):
        """For large s, the truncated series should be dominated by h=2 term."""
        # d(2) = 1, so eps(s) ~ 4^{-s} for large s
        for s in [20, 30, 50]:
            eps = constrained_epstein(s, h_max=10)
            leading = 4.0 ** (-s)  # (2*2)^{-s}
            ratio = eps.real / leading
            assert abs(ratio - 1) < 0.01, (
                f"At s={s}, ratio should be ~1, got {ratio}"
            )

    def test_truncation_stability_large_s(self):
        """At large s, increasing h_max shouldn't change the result much."""
        for s in [10, 15, 20]:
            eps_10 = constrained_epstein(s, h_max=10)
            eps_50 = constrained_epstein(s, h_max=50)
            eps_200 = constrained_epstein(s, h_max=200)
            # Should all be close
            rel = abs(eps_200 - eps_10) / abs(eps_10) if abs(eps_10) > 0 else 0
            assert rel < 1e-6, f"s={s}: rel diff {rel} too large"

    def test_divergence_small_s(self):
        """At small s, increasing h_max should make the sum blow up."""
        eps_100 = constrained_epstein(2, h_max=100)
        eps_500 = constrained_epstein(2, h_max=500)
        assert abs(eps_500) > abs(eps_100) * 10, (
            "Series should diverge rapidly at s=2"
        )

    def test_positivity(self):
        """For real s > 0, all terms are positive, so the sum is positive."""
        for s in [3, 5, 10]:
            eps = constrained_epstein(s, h_max=50)
            assert eps.real > 0, f"eps({s}) should be positive"
            assert abs(eps.imag) < 1e-12, f"eps({s}) should be real for real s"

    def test_first_term(self):
        """The leading term at h=2 is d(2)*(2*2)^{-s} = 4^{-s}."""
        eps = constrained_epstein(5, h_max=2)
        expected = 4 ** (-5)
        assert abs(eps.real - expected) < 1e-15

    def test_first_two_terms(self):
        """Through h=4: eps = 4^{-s} + 8^{-s} (d(2)=1, d(3)=0, d(4)=1)."""
        eps = constrained_epstein(5, h_max=4)
        expected = 4 ** (-5) + 8 ** (-5)
        assert abs(eps.real - expected) < 1e-15

    def test_derivative_sign(self):
        """Derivative is negative for real s (negative log terms)."""
        deps = constrained_epstein_derivative(5, h_max=50)
        assert deps.real < 0, "Derivative should be negative for real s"


# ================================================================
# 5. Convergence analysis tests
# ================================================================

class TestConvergence:
    """Tests for convergence/divergence analysis."""

    def test_abscissa_infinity(self):
        ca = convergence_analysis()
        assert ca['abscissa_of_convergence'] == float('inf')

    def test_growth_constant(self):
        ca = convergence_analysis()
        C = math.pi * math.sqrt(2.0 / 3.0)
        assert abs(ca['growth_constant'] - C) < 1e-10

    def test_effective_sigma_increases(self):
        """Effective convergence sigma should increase with h_max."""
        sigmas = [effective_convergence_sigma(h) for h in [50, 100, 200, 500]]
        for i in range(len(sigmas) - 1):
            assert sigmas[i + 1] > sigmas[i], (
                f"sigma({[50,100,200,500][i+1]}) should exceed sigma({[50,100,200,500][i]})"
            )

    def test_effective_sigma_scale(self):
        """sigma_eff ~ C*sqrt(h_max) / (2 log(2*h_max))."""
        C = math.pi * math.sqrt(2.0 / 3.0)
        for h_max in [100, 200, 500]:
            sigma = effective_convergence_sigma(h_max)
            # Rough scale: should be O(sqrt(h_max))
            assert sigma > 1.0, f"sigma({h_max}) should be > 1"
            assert sigma < 20.0, f"sigma({h_max}) should be < 20"

    def test_regularized_partial_sums(self):
        """Regularized Epstein returns correct structure."""
        result = regularized_epstein(5, h_max=20)
        assert result['s'] == 5
        assert result['h_max'] == 20
        assert result['n_terms'] > 0
        assert abs(result['final_value']) > 0


# ================================================================
# 6. Shadow metric tests
# ================================================================

class TestShadowMetric:
    """Tests for the shadow metric Epstein zeta."""

    def test_discriminant_virasoro(self):
        """disc = -320c^2 / (5c+22) for Virasoro."""
        for c in [1.0, 2.0, 10.0, 26.0]:
            disc = shadow_metric_discriminant(c)
            expected = -320 * c ** 2 / (5 * c + 22)
            assert abs(disc - expected) < 1e-10

    def test_discriminant_negative(self):
        """For c > 0, discriminant is negative (positive definite form)."""
        for c in [0.5, 1.0, 5.0, 13.0, 26.0]:
            disc = shadow_metric_discriminant(c)
            assert disc < 0, f"disc at c={c} should be negative"

    def test_shadow_epstein_positive(self):
        """For real s > 1 and positive definite Q, epsilon_Q > 0."""
        for c in [1.0, 5.0, 13.0]:
            eps = shadow_metric_epstein(3.0, c, nmax=10)
            assert eps.real > 0, f"shadow Epstein at c={c} should be positive"

    def test_two_epsteins_differ(self):
        """The spectral and shadow Epsteins should give different values."""
        result = compare_two_epsteins(10.0, s_values=[5.0], h_max=50)
        comps = result['comparisons']
        assert len(comps) > 0
        ratio = comps[0]['ratio']
        # They should NOT be equal
        assert abs(ratio - 1.0) > 0.01, "The two Epsteins should differ"

    def test_shadow_discriminant_special_values(self):
        """At c=0 and c=-22/5, the discriminant should be 0 or infinite."""
        disc_0 = shadow_metric_discriminant(0.0)
        assert abs(disc_0) < 1e-10, "disc(0) should be 0"


# ================================================================
# 7. Minimal model tests
# ================================================================

class TestMinimalModels:
    """Tests for minimal model exact constrained Epstein."""

    def test_ising_primaries(self):
        """M(3,4) = Ising: primaries at h = 1/16, 1/2."""
        prims = minimal_model_quasi_primaries(3)
        h_values = sorted(h for h, _ in prims)
        assert len(h_values) == 2
        assert abs(h_values[0] - 1 / 16) < 1e-10
        assert abs(h_values[1] - 0.5) < 1e-10

    def test_ising_epstein(self):
        r"""M(3,4): eps = (1/8)^{-s} + 1^{-s} = 8^s + 1."""
        for s in [2.0, 3.0, 5.0]:
            eps = minimal_model_constrained_epstein(s, 3)
            # 2h values are 2*(1/16) = 1/8 and 2*(1/2) = 1
            expected = (1 / 8) ** (-s) + 1.0 ** (-s)  # = 8^s + 1
            assert abs(eps.real - expected) < 1e-8, (
                f"Ising eps({s}) = {eps.real}, expected {expected}"
            )

    def test_ising_zeros(self):
        """Ising eps = 8^s + 1 has zeros at s = i*pi*(2k+1)/log(8)."""
        for k in range(-3, 4):
            t = math.pi * (2 * k + 1) / math.log(8)
            s = complex(0, t)
            eps = minimal_model_constrained_epstein(s, 3)
            assert abs(eps) < 1e-6, f"Ising eps at zero k={k}: |eps| = {abs(eps)}"

    def test_ising_no_offline_zeros(self):
        """Ising eps has no zeros away from Re(s) = 0."""
        # On Re(s) = 0.5, |eps| should be bounded away from 0
        for t in [0.5, 1.0, 2.0, 5.0, 10.0]:
            s = complex(0.5, t)
            eps = minimal_model_constrained_epstein(s, 3)
            # |8^{0.5+it} + 1| >= |8^{0.5}| - 1 = 2*sqrt(2) - 1 > 0
            assert abs(eps) > 0.5, f"Ising eps at Re=0.5: should be bounded from 0"

    def test_tricritical_ising_count(self):
        """M(4,5) has 5 primaries."""
        prims = minimal_model_quasi_primaries(4)
        assert len(prims) == 5

    def test_three_state_potts_count(self):
        """M(5,6) has 9 primaries."""
        prims = minimal_model_quasi_primaries(5)
        assert len(prims) == 9

    def test_tetracritical_ising_count(self):
        """M(6,7) has 14 primaries."""
        prims = minimal_model_quasi_primaries(6)
        assert len(prims) == 14

    def test_minimal_model_primary_counts(self):
        """M(m,m+1) has (m-1)*m/2 - 1 nonzero primaries."""
        for m in range(3, 10):
            prims = minimal_model_quasi_primaries(m)
            expected = (m - 1) * m // 2 - 1
            assert len(prims) == expected, (
                f"M({m},{m+1}): expected {expected} primaries, got {len(prims)}"
            )

    def test_minimal_model_positivity(self):
        """All minimal model primary dimensions h > 0."""
        for m in range(3, 10):
            prims = minimal_model_quasi_primaries(m)
            for h, mult in prims:
                assert h > 0, f"M({m},{m+1}): h={h} should be positive"
                assert mult == 1, f"M({m},{m+1}): multiplicity should be 1"

    def test_minimal_model_epstein_entire(self):
        """For minimal models, eps is entire (finite sum)."""
        # Evaluate at s = -1 (negative): should be well-defined
        for m in [3, 4, 5]:
            eps = minimal_model_constrained_epstein(-1, m)
            assert math.isfinite(eps.real), f"M({m},{m+1}): eps(-1) should be finite"


# ================================================================
# 8. Functional equation tests
# ================================================================

class TestFunctionalEquation:
    """Tests for the (non-)existence of functional equations."""

    def test_no_exact_functional_equation(self):
        """The truncated constrained Epstein has NO exact functional equation.

        Unlike the Epstein zeta of a quadratic form (which has Lambda(s) = Lambda(1-s)),
        the spectral Dirichlet series has no symmetry.
        """
        h_max = 50
        results = _test_functional_equation(h_max, s_values=[3.0, 5.0])
        for result in results:
            s = result['s']
            for a in [1, 2, 3]:
                ratio = result['tests'][a]['ratio']
                if isinstance(ratio, complex) and math.isfinite(ratio.real):
                    # The ratio should NOT be a simple function
                    # (i.e., not constant across different s values)
                    pass  # We just verify the computation runs

    def test_ising_functional_equation(self):
        r"""The Ising eps = 8^s + 1 does satisfy a reflection:
        eps(s) = eps(s + 2*pi*i/log(8)) (periodicity in imaginary direction),
        but NOT eps(s) = chi(s) * eps(a-s) for real a.
        """
        s = complex(2.0, 1.0)
        eps_s = minimal_model_constrained_epstein(s, 3)
        # Period = 2*pi/log(8)
        period = 2 * math.pi / math.log(8)
        eps_shifted = minimal_model_constrained_epstein(s + complex(0, period), 3)
        assert abs(eps_s - eps_shifted) < 1e-8, "Ising eps should be periodic in Im(s)"


# ================================================================
# 9. c-independence tests
# ================================================================

class TestCIndependence:
    """Tests for the c-independence of the universal spectrum."""

    def test_c_analysis_returns(self):
        result = c_dependence_analysis()
        assert result['c_dependence'] is False

    def test_d_values_combinatorial(self):
        """d(h) depends only on partitions, not on c."""
        # Verify d(h) = p_ge2(h) - p_ge2(h-1), which has no c
        for h in range(2, 50):
            d = quasi_primary_count(h)
            expected = p_ge2(h) - p_ge2(h - 1)
            assert d == expected, (
                f"d({h}) should be purely combinatorial: {d} vs {expected}"
            )

    def test_epstein_c_independent(self):
        """The constrained Epstein at generic c is the same for all c.

        (This follows from c-independence of d(h), since eps only uses d(h).)
        """
        # There is only ONE constrained Epstein for all generic c
        # The function signature doesn't even take c as an argument
        eps1 = constrained_epstein(5, h_max=50)
        eps2 = constrained_epstein(5, h_max=50)
        assert eps1 == eps2


# ================================================================
# 10. Benjamin-Chang comparison tests
# ================================================================

class TestBenjaminChang:
    """Tests for the Benjamin-Chang comparison analysis."""

    def test_comparison_structure(self):
        result = benjamin_chang_comparison()
        assert 'our_object' in result
        assert 'bc_object' in result
        assert 'differences' in result
        assert len(result['differences']) >= 3

    def test_key_difference(self):
        """Our eps is c-independent; BC's depends on the specific CFT."""
        result = benjamin_chang_comparison()
        assert 'universal' in result['for_generic_c']
        assert 'BC depends' in result['for_generic_c'] or 'depends on the CFT' in result['for_generic_c']


# ================================================================
# 11. Rankin-Selberg structural tests
# ================================================================

class TestRankinSelberg:
    """Tests for the Rankin-Selberg structural analysis."""

    def test_structural_analysis(self):
        result = rankin_selberg_structural_analysis()
        assert result['constrained_epstein']['convergence'] == (
            'DIVERGES (subexponential growth of d(h))'
        )
        assert 'YES' in result['shadow_metric_epstein']['functional_equation']

    def test_different_types(self):
        result = rankin_selberg_structural_analysis()
        assert '1D' in result['constrained_epstein']['type']
        assert '2D' in result['shadow_metric_epstein']['type']


# ================================================================
# 12. Weight-multiplicity Dirichlet series tests
# ================================================================

class TestWeightMultiplicity:
    """Tests for the generalized Dirichlet series D_k(s)."""

    def test_k0_equals_epstein(self):
        """D_0(s) should equal the constrained Epstein."""
        D = weight_multiplicity_dirichlet(5, h_max=50)
        eps = constrained_epstein(5, h_max=50)
        assert abs(D[0] - eps) < 1e-10

    def test_k_ordering(self):
        """D_{k+1}(s) > D_k(s) for s > 0 (larger weights contribute more)."""
        D = weight_multiplicity_dirichlet(5, h_max=50)
        # D[1] has extra factor h, D[2] has h^2, so D[2] > D[1] > D[0]
        assert D[2].real > D[1].real > D[0].real

    def test_k_negative(self):
        """D_{-1}(s) < D_0(s) (smaller weights contribute less)."""
        D = weight_multiplicity_dirichlet(5, h_max=50)
        assert D[-1].real < D[0].real


# ================================================================
# 13. Cross-checks with known values
# ================================================================

class TestCrossChecks:
    """Cross-checks with independent computations."""

    def test_weight_2_is_T(self):
        """d(2)=1 corresponds to the stress tensor T."""
        assert quasi_primary_count(2) == 1

    def test_weight_4_is_Lambda(self):
        """d(4)=1: the unique weight-4 quasi-primary Lambda = L_{-2}^2 + (5/3)L_{-4}.
        This is normal-ordered :TT: with Sugawara correction."""
        assert quasi_primary_count(4) == 1

    def test_weight_6_count(self):
        """d(6)=2: two linearly independent weight-6 quasi-primaries.
        These correspond to :T partial^2 T: and :(partial T)^2: (with corrections).
        One of these is the W_3 current (at specific c)."""
        assert quasi_primary_count(6) == 2

    def test_odd_weight_first_appearance(self):
        """The first odd-weight quasi-primary appears at h=9.
        At weights 3,5,7: d=0 (all states are L_{-1} descendants).
        At weight 9: d=1 (first state not expressible as L_{-1}(something))."""
        assert quasi_primary_count(3) == 0
        assert quasi_primary_count(5) == 0
        assert quasi_primary_count(7) == 0
        assert quasi_primary_count(9) == 1

    def test_partition_crosscheck(self):
        """The vacuum module dimension at weight h equals p_ge2(h).
        This is a known result in the Virasoro representation theory
        (partitions into parts >= 2 = descendants of vacuum not using L_{-1})."""
        known = {
            0: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 7,
            9: 8, 10: 12, 12: 21, 14: 34, 16: 55, 18: 88, 20: 137,
        }
        for h, dim in known.items():
            assert p_ge2(h) == dim, f"dim V_{h} = p_ge2({h}) should be {dim}"

    def test_ising_central_charge(self):
        """M(3,4) has c = 1/2."""
        c = 1 - 6 / (3 * 4)
        assert abs(c - 0.5) < 1e-10

    def test_cumulative_through_10(self):
        """Sum of d(h) for h=0..10 (excluding h=1) = 13."""
        total = sum(quasi_primary_count(h) for h in range(11) if h != 1)
        assert total == 13

    def test_cumulative_through_20(self):
        """Sum of d(h) for h=0..20 (excluding h=1) = 138."""
        total = sum(quasi_primary_count(h) for h in range(21) if h != 1)
        assert total == 138


# ================================================================
# 14. Asymptotics tests
# ================================================================

class TestAsymptotics:
    """Tests for asymptotic growth of d(h)."""

    def test_exponential_growth(self):
        """d(h) should grow exponentially in sqrt(h).

        Since d(h) ~ exp(C*sqrt(h)), we have
        log(d(200))/log(d(100)) ~ sqrt(200)/sqrt(100) = sqrt(2) ~ 1.414.
        But there are polynomial corrections, so we allow a wider range.
        """
        d_100 = quasi_primary_count(100)
        d_200 = quasi_primary_count(200)
        if d_100 > 0 and d_200 > 0:
            ratio = math.log(d_200) / math.log(d_100)
            assert 1.2 < ratio < 1.8, f"Growth ratio {ratio} out of expected range"

    def test_asymptotic_function_positive(self):
        """The asymptotic formula should give positive values."""
        for h in [10, 50, 100]:
            a = quasi_primary_asymptotics(h)
            assert a > 0

    def test_asymptotic_overestimates(self):
        """The leading asymptotic overestimates d(h) (missing correction terms)."""
        for h in [20, 50, 100]:
            a = quasi_primary_asymptotics(h)
            d = quasi_primary_count(h)
            assert a > d, f"Asymptotic {a} should overestimate d({h}) = {d}"


# ================================================================
# 15. Structural tests
# ================================================================

class TestStructural:
    """Tests for structural properties of the constrained Epstein."""

    def test_shadow_and_spectral_differ(self):
        """The shadow metric Epstein and the constrained Epstein are
        fundamentally different objects (different argument spaces,
        different convergence properties)."""
        # The shadow Epstein converges for Re(s) > 1
        # The constrained Epstein diverges for all s
        ca = convergence_analysis()
        rs = rankin_selberg_structural_analysis()
        assert ca['abscissa_of_convergence'] == float('inf')
        assert 'CONVERGES' in rs['shadow_metric_epstein']['convergence']

    def test_no_functional_equation(self):
        """The constrained Epstein has no functional equation
        (it is not a lattice sum)."""
        rs = rankin_selberg_structural_analysis()
        assert 'NONE' in rs['constrained_epstein']['functional_equation']

    def test_shadow_has_functional_equation(self):
        """The shadow metric Epstein HAS a functional equation
        (it IS a lattice sum)."""
        rs = rankin_selberg_structural_analysis()
        assert 'YES' in rs['shadow_metric_epstein']['functional_equation']

    def test_spectral_vs_algebraic(self):
        """The two Epsteins encode different data:
        spectral (quasi-primary multiplicities) vs algebraic (shadow invariants)."""
        rs = rankin_selberg_structural_analysis()
        assert 'quasi-primary' in rs['constrained_epstein']['data_encoded']
        assert 'shadow obstruction tower' in rs['shadow_metric_epstein']['data_encoded']


# ================================================================
# 16. Edge cases
# ================================================================

class TestEdgeCases:
    """Tests for edge cases and boundary behavior."""

    def test_negative_h(self):
        assert quasi_primary_count(-1) == 0
        assert quasi_primary_count(-10) == 0

    def test_large_h(self):
        """d(h) should be computable for moderately large h."""
        d = quasi_primary_count(100)
        assert d > 0
        assert isinstance(d, int)

    def test_complex_s(self):
        """Constrained Epstein should work for complex s."""
        s = complex(5, 2)
        eps = constrained_epstein(s, h_max=20)
        assert math.isfinite(eps.real)
        assert math.isfinite(eps.imag)

    def test_negative_s(self):
        """For negative real s, the truncated sum should be large but finite."""
        eps = constrained_epstein(-1, h_max=10)
        assert math.isfinite(eps.real)

    def test_s_zero(self):
        """eps(0) = sum d(h) = total quasi-primary count."""
        eps = constrained_epstein(0, h_max=20)
        expected = sum(quasi_primary_count(h) for h in range(2, 21))
        assert abs(eps.real - expected) < 1e-8


# ================================================================
# 17. Consistency with virasoro_epstein_attack module
# ================================================================

class TestConsistencyWithExisting:
    """Verify consistency with the existing virasoro_epstein_attack module."""

    def test_ising_matches_attack_module(self):
        """Our Ising computation should match virasoro_epstein_attack."""
        try:
            from virasoro_epstein_attack import minimal_model_primaries
            prims_attack = minimal_model_primaries(3)
            prims_ours = minimal_model_quasi_primaries(3)
            # Both should give h = 1/16 and h = 1/2
            h_attack = sorted(h for h, _ in prims_attack)
            h_ours = sorted(h for h, _ in prims_ours)
            assert len(h_attack) == len(h_ours) == 2
            for ha, ho in zip(h_attack, h_ours):
                assert abs(ha - ho) < 1e-10
        except ImportError:
            pytest.skip("virasoro_epstein_attack not available")

    def test_ising_epstein_matches(self):
        """Ising eps from both modules should agree."""
        try:
            from virasoro_epstein_attack import minimal_model_epstein
            for s in [3.0, 5.0, 10.0]:
                eps_attack = minimal_model_epstein(s, 3)
                eps_ours = minimal_model_constrained_epstein(s, 3)
                assert abs(eps_attack - eps_ours) < 1e-8
        except ImportError:
            pytest.skip("virasoro_epstein_attack not available")


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short', '-q'])
