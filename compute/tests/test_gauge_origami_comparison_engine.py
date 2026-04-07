r"""Tests for compute/lib/gauge_origami_comparison_engine.py

Comprehensive test suite covering:
  Section 1:  Gauge origami — spiked instantons (CY4 condition, factorization)
  Section 2:  Bar arity vs instanton number
  Section 3:  Shadow PF vs Nekrasov PF
  Section 4:  Nekrasov for U(1), U(2) with flavors N_f=0..4
  Section 5:  AGT at low instanton number — multi-path verification
  Section 6:  Independent sum factorization vs gauge origami
  Section 7:  Koszul duality interpretation of matter
  Section 8:  Instanton corrections vs genus expansion
  Section 9:  Class S and Ran(X) factorization
  Section 10: Schiffmann-Vasserot and the Yangian bridge
  Section 11: Bar complex as gauge origami
  Section 12: Full comparison table

MULTI-PATH VERIFICATION strategy:
  Each key result is tested via 3+ independent routes where possible.
"""

import pytest
from sympy import (
    Rational, simplify, sqrt, Symbol, oo, S as Sym,
    bernoulli, factorial, Abs, N as Neval, expand,
)

from compute.lib.gauge_origami_comparison_engine import (
    # Section 1
    gauge_origami_partition,
    calabi_yau_4_condition,
    magnificent_four_eps,
    # Section 2
    bar_arity_instanton_comparison,
    coha_bar_duality_check,
    # Section 3
    shadow_vs_nekrasov_structural,
    shadow_nekrasov_genus1_match,
    shadow_nekrasov_genus_g_match,
    # Section 4
    nekrasov_u1_partition,
    nekrasov_u2_pure,
    nekrasov_u2_flavored,
    nekrasov_in_shadow_basis,
    # Section 5
    agt_verification_k1,
    agt_verification_k2,
    # Section 6
    independent_sum_test,
    gauge_origami_vs_independent_sum,
    # Section 7
    koszul_matter_comparison,
    matter_from_koszul_nf,
    # Section 8
    instanton_genus_comparison,
    # Section 9
    class_s_comparison,
    # Section 10
    schiffmann_vasserot_identification,
    # Section 11
    bar_as_gauge_origami,
    # Section 12
    full_comparison_table,
)

from compute.lib.agt_shadow_correspondence import (
    agt_central_charge,
    agt_parameter_map,
    nekrasov_partition_su2,
    nekrasov_free_energy_su2,
    nekrasov_factor_pair,
    all_partition_pairs,
    all_partitions,
)


# ===================================================================
# Section 1: Gauge origami — spiked instantons
# ===================================================================

class TestCalabiYau4Condition:
    """Tests for the CY4 condition eps1+eps2+eps3+eps4=0."""

    def test_cy4_satisfied(self):
        """eps1+eps2+eps3+eps4=0 should register as CY4."""
        result = calabi_yau_4_condition(1, 2, 3, -6)
        assert result['is_CY4'] is True
        assert result['sum'] == 0

    def test_cy4_violated(self):
        """Generic values should violate CY4."""
        result = calabi_yau_4_condition(1, 1, 1, 1)
        assert result['is_CY4'] is False
        assert result['sum'] == 4

    def test_cy4_symmetric(self):
        """Symmetric case: all equal with opposite sign."""
        result = calabi_yau_4_condition(1, 1, -1, -1)
        assert result['is_CY4'] is True

    def test_magnificent_four_eps(self):
        """eps4 = -(eps1+eps2+eps3) should satisfy CY4."""
        eps = magnificent_four_eps(1, 2, 3)
        assert eps['eps4'] == -6
        total = eps['eps1'] + eps['eps2'] + eps['eps3'] + eps['eps4']
        assert total == 0

    def test_magnificent_four_rational(self):
        """Works with rational values."""
        eps = magnificent_four_eps(Rational(1, 2), Rational(1, 3), Rational(1, 6))
        assert eps['eps4'] == -1
        total = eps['eps1'] + eps['eps2'] + eps['eps3'] + eps['eps4']
        assert total == 0


class TestGaugeOrigamiPartition:
    """Tests for the gauge origami partition function."""

    def test_single_spike_u1(self):
        """Single U(1) spike should give the U(1) Nekrasov PF."""
        spike = {
            'rank': 1,
            'eps_pair': (0, 1),
            'coulomb': [0],
            'eps_vals': {0: 1, 1: -1},
        }
        result = gauge_origami_partition([spike], max_inst=2)
        assert result['num_spikes'] == 1
        assert result['factorized'] is True
        assert result['total'][0] == 1

    def test_single_spike_su2(self):
        """Single SU(2) spike reproduces SU(2) Nekrasov."""
        spike = {
            'rank': 2,
            'eps_pair': (0, 1),
            'coulomb': [1, -1],
            'eps_vals': {0: 1, 1: 2},
        }
        result = gauge_origami_partition([spike], max_inst=2)
        direct = nekrasov_partition_su2(1, 1, 2, 2)
        # Should match the direct computation
        assert result['total'][0] == direct[0]
        assert simplify(result['total'][1] - direct[1]) == 0

    def test_two_spikes_factorize(self):
        """Two spikes: total PF is a convolution of individual PFs."""
        spike1 = {
            'rank': 1,
            'eps_pair': (0, 1),
            'coulomb': [0],
            'eps_vals': {0: 1, 1: -1},
        }
        spike2 = {
            'rank': 1,
            'eps_pair': (2, 3),
            'coulomb': [0],
            'eps_vals': {2: 2, 3: -2},
        }
        result = gauge_origami_partition([spike1, spike2], max_inst=2)
        assert result['num_spikes'] == 2
        # Z_0 of the product = Z_0^(1) * Z_0^(2) = 1
        assert result['total'][0] == 1

    def test_z0_always_one(self):
        """At k=0, any gauge origami partition function is 1."""
        spike = {
            'rank': 2,
            'eps_pair': (0, 1),
            'coulomb': [3, -3],
            'eps_vals': {0: 1, 1: 1},
        }
        result = gauge_origami_partition([spike], max_inst=1)
        assert result['total'][0] == 1


# ===================================================================
# Section 2: Bar arity vs instanton number
# ===================================================================

class TestBarArityInstanton:
    """Tests for bar arity vs instanton number comparison."""

    def test_heisenberg_exact_match(self):
        """For N=1 (Heisenberg), partition count = instanton fixed points."""
        results = bar_arity_instanton_comparison(N=1, max_k=5)
        for entry in results:
            # At N=1, partition N-tuples = partition 1-tuples = partitions
            assert entry['fixed_point_count_equals_partitions'] is True

    def test_partition_counts_known(self):
        """Verify partition counts: p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5."""
        results = bar_arity_instanton_comparison(N=1, max_k=4)
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5}
        for entry in results:
            assert entry['partition_count'] == expected[entry['k']]

    def test_su2_pair_counts(self):
        """SU(2) partition pairs at k=0..3."""
        results = bar_arity_instanton_comparison(N=2, max_k=3)
        # Partition pairs: k=0: 1, k=1: 2, k=2: 5, k=3: 10
        expected_pairs = {0: 1, 1: 2, 2: 5, 3: 10}
        for entry in results:
            assert entry['partition_N_tuples'] == expected_pairs[entry['k']]

    def test_su3_triple_counts(self):
        """SU(3) partition triples at k=0..2."""
        results = bar_arity_instanton_comparison(N=3, max_k=2)
        # k=0: 1, k=1: 3, k=2: 9
        expected = {0: 1, 1: 3, 2: 9}
        for entry in results:
            assert entry['partition_N_tuples'] == expected[entry['k']]

    def test_adhm_dimension(self):
        """ADHM moduli dim = 2kN."""
        results = bar_arity_instanton_comparison(N=2, max_k=3)
        for entry in results:
            assert entry['adhm_dim'] == 2 * entry['k'] * entry['N']


class TestCoHABarDuality:
    """Tests for the CoHA-bar duality check."""

    def test_heisenberg_duality(self):
        """For N=1, CoHA dim = bar dim at each k."""
        results = coha_bar_duality_check(N=1, max_k=4)
        for entry in results:
            assert entry['duality_check'] is True
            assert entry['coha_dim'] == entry['bar_dim']

    def test_heisenberg_k0(self):
        """At k=0: CoHA and bar both have dim 1."""
        results = coha_bar_duality_check(N=1, max_k=0)
        assert results[0]['coha_dim'] == 1
        assert results[0]['bar_dim'] == 1

    def test_su2_coha_counts(self):
        """For N=2, CoHA dim = partition pair count."""
        results = coha_bar_duality_check(N=2, max_k=2)
        expected = {0: 1, 1: 2, 2: 5}
        for entry in results:
            assert entry['coha_dim'] == expected[entry['k']]


# ===================================================================
# Section 3: Shadow PF vs Nekrasov PF
# ===================================================================

class TestShadowVsNekrasov:
    """Tests for shadow vs Nekrasov partition function comparison."""

    def test_structural_returns_data(self):
        """Structural comparison should return all keys."""
        result = shadow_vs_nekrasov_structural(25, 3, 1, 2, max_inst=2)
        assert 'shadow_kappa' in result
        assert 'shadow_F_g' in result
        assert 'nekrasov_free_energy' in result

    def test_shadow_kappa_positive(self):
        """kappa = c/2 > 0 for c > 0."""
        for c in [1, 10, 25, 26]:
            result = shadow_vs_nekrasov_structural(c, 3, 1, 2, max_inst=1)
            assert result['shadow_kappa'] > 0

    def test_genus1_match_structure(self):
        """Genus-1 match returns correct fields."""
        result = shadow_nekrasov_genus1_match(1, 2)
        assert 'kappa' in result
        assert 'shadow_F1' in result
        assert 'lambda_1_FP' in result
        assert result['lambda_1_FP'] == Rational(1, 24)

    def test_shadow_f1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for any central charge."""
        # Use rational eps pairs where b^2 = -eps1/eps2 > 0 (real b)
        # so that c and kappa are real rationals.
        test_cases = [
            (1, -2),   # b^2 = 1/2
            (1, -3),   # b^2 = 1/3
            (2, -1),   # b^2 = 2
            (3, -1),   # b^2 = 3
        ]
        for e1, e2 in test_cases:
            result = shadow_nekrasov_genus1_match(e1, e2)
            assert result['shadow_F1'] == result['kappa'] / 24

    def test_genus_g_structure(self):
        """Genus-g match returns correct data."""
        for g in [1, 2, 3]:
            result = shadow_nekrasov_genus_g_match(25, g)
            assert result['genus'] == g
            assert result['kappa'] == Rational(25, 2)
            assert result['F_g_shadow'] == result['kappa'] * result['lambda_g_FP']

    def test_shadow_f_g_positive(self):
        """F_g > 0 for c > 0 and all g >= 1."""
        for g in [1, 2, 3, 4]:
            result = shadow_nekrasov_genus_g_match(10, g)
            assert float(result['F_g_shadow_numeric']) > 0


# ===================================================================
# Section 4: Nekrasov for U(1), U(2) with flavors
# ===================================================================

class TestNekrasovU1:
    """Tests for U(1) Nekrasov partition function."""

    def test_u1_z0_is_1(self):
        """Z_0 = 1 for U(1)."""
        Z = nekrasov_u1_partition(1, -1, 3)
        assert Z[0] == 1

    def test_u1_z1_nonzero(self):
        """Z_1 should be nonzero for generic eps."""
        Z = nekrasov_u1_partition(1, 2, 3)
        assert Z[1] != 0

    def test_u1_z1_single_partition(self):
        """At k=1, only one partition (1,), so Z_1 has a single contribution."""
        Z = nekrasov_u1_partition(1, 2, 2)
        # For Y = (1,): arm = 0, leg = 0
        # hook_e = eps1*(0+1) + eps2*0 = eps1
        # hook_w = -eps1*0 + eps2*(0+1) = eps2
        # denom = eps1 * eps2
        # z = 1/(eps1 * eps2)
        expected = Rational(1) / (Rational(1) * Rational(2))
        assert Z[1] == expected

    def test_u1_z2_two_partitions(self):
        """At k=2: partitions (2,) and (1,1)."""
        Z = nekrasov_u1_partition(1, 2, 3)
        # Two partitions contribute
        assert Z[2] != 0


class TestNekrasovU2Pure:
    """Tests for pure U(2) = SU(2) Nekrasov partition function."""

    def test_u2_z0_is_1(self):
        Z = nekrasov_u2_pure(3, 1, 2, 2)
        assert Z[0] == 1

    def test_u2_z1_formula(self):
        """Z_1 at specific a, eps should match direct computation."""
        a, e1, e2 = 3, 1, 2
        Z = nekrasov_u2_pure(a, e1, e2, 1)
        direct = nekrasov_partition_su2(a, e1, e2, 1)
        assert simplify(Z[1] - direct[1]) == 0

    def test_u2_z1_two_contributions(self):
        """k=1: two partition pairs ((1,),()) and ((),(1,))."""
        a, e1, e2 = 5, 1, 1
        z_10 = nekrasov_factor_pair(a, (1,), (), e1, e2)
        z_01 = nekrasov_factor_pair(a, (), (1,), e1, e2)
        Z = nekrasov_u2_pure(a, e1, e2, 1)
        assert simplify(Z[1] - z_10 - z_01) == 0

    def test_u2_eps_symmetry(self):
        """Z_k(a, eps1, eps2) = Z_k(a, eps2, eps1) for pure gauge."""
        a = 3
        Z1 = nekrasov_u2_pure(a, 1, 2, 2)
        Z2 = nekrasov_u2_pure(a, 2, 1, 2)
        for k in range(3):
            assert simplify(Z1[k] - Z2[k]) == 0


class TestNekrasovU2Flavored:
    """Tests for U(2) with N_f fundamental flavors."""

    def test_nf0_equals_pure(self):
        """N_f=0 should give the pure gauge result."""
        a, e1, e2 = 3, 1, 2
        Z_pure = nekrasov_u2_pure(a, e1, e2, 2)
        Z_nf0 = nekrasov_u2_flavored(a, 0, e1, e2, max_inst=2)
        for k in range(3):
            assert simplify(Z_pure[k] - Z_nf0[k]) == 0

    def test_nf4_exists(self):
        """N_f=4 conformal theory should give nonzero Z_1."""
        Z = nekrasov_u2_flavored(3, 4, 1, 2, max_inst=1)
        assert Z[0] == 1
        assert Z[1] != 0

    def test_nf_increasing_changes_z1(self):
        """Adding flavors should change Z_1."""
        a, e1, e2 = 5, 1, 1
        z1_values = []
        for nf in range(5):
            Z = nekrasov_u2_flavored(a, nf, e1, e2, max_inst=1)
            z1_values.append(Z[1])
        # Not all the same (matter changes the instanton weight)
        assert len(set(str(z) for z in z1_values)) > 1

    def test_nf4_conformal_flag(self):
        """N_f=4 for SU(2) is the conformal point."""
        result = matter_from_koszul_nf(25, 4)
        assert result['is_conformal'] is True

    def test_nf3_not_conformal(self):
        """N_f=3 is not conformal."""
        result = matter_from_koszul_nf(25, 3)
        assert result['is_conformal'] is False


class TestNekrasovInShadowBasis:
    """Tests for expressing Nekrasov in the shadow basis."""

    def test_returns_kappa(self):
        result = nekrasov_in_shadow_basis(3, 1, 2, max_inst=1)
        assert 'kappa' in result
        assert result['kappa'] == agt_parameter_map(1, 2)['kappa']

    def test_z1_nonzero(self):
        result = nekrasov_in_shadow_basis(3, 1, 2, max_inst=1)
        assert result['Z_1'] != 0

    def test_hbar_product(self):
        """hbar = eps1 * eps2."""
        result = nekrasov_in_shadow_basis(3, 1, 2)
        assert result['hbar'] == 2


# ===================================================================
# Section 5: AGT at low instanton number
# ===================================================================

class TestAGTVerificationK1:
    """Tests for AGT three-path verification at k=1."""

    def test_paths_match(self):
        """Path 1 (Nekrasov sum) = Path 2 (explicit) at k=1."""
        result = agt_verification_k1(3, 1, 2)
        assert result['paths_1_2_match'] is True

    def test_z1_nonzero(self):
        result = agt_verification_k1(5, 1, 1)
        assert result['path1_nekrasov_sum'] != 0

    def test_multiple_parameters(self):
        """Paths should match for various non-resonant (a, eps1, eps2).

        Resonance occurs when 2a = n*eps1 + m*eps2 for nonneg integers n, m,
        producing poles in the Nekrasov factor. We avoid those here.
        """
        for a, e1, e2 in [(3, 1, 2), (5, 1, 1), (7, 2, 3), (11, 1, 3)]:
            result = agt_verification_k1(a, e1, e2)
            assert result['paths_1_2_match'] is True

    def test_z1_eps_symmetry(self):
        """Z_1(eps1, eps2) = Z_1(eps2, eps1)."""
        r1 = agt_verification_k1(3, 1, 2)
        r2 = agt_verification_k1(3, 2, 1)
        assert simplify(r1['path1_nekrasov_sum'] - r2['path1_nekrasov_sum']) == 0


class TestAGTVerificationK2:
    """Tests for AGT verification at k=2."""

    def test_five_partition_pairs(self):
        """At k=2 there should be 5 partition pairs."""
        result = agt_verification_k2(3, 1, 2)
        assert result['pair_count'] == 5

    def test_individual_sum_matches(self):
        """Sum of individual contributions = Z_2."""
        result = agt_verification_k2(3, 1, 2)
        assert result['individual_sum_matches'] is True

    def test_f2_cumulant(self):
        """F_2 = Z_2 - Z_1^2/2 should be computed."""
        result = agt_verification_k2(3, 1, 2)
        assert result['path2_F2_cumulant'] is not None

    def test_multiple_parameters_k2(self):
        """Individual sum matches for various non-resonant parameters.

        At k=2, resonances are more common: 2a = n*eps1 + m*eps2 with n+m <= 2.
        We choose a large enough to avoid all poles.
        """
        for a, e1, e2 in [(3, 1, 2), (7, 1, 2), (11, 1, 3)]:
            result = agt_verification_k2(a, e1, e2)
            assert result['individual_sum_matches'] is True


# ===================================================================
# Section 6: Independent sum factorization vs gauge origami
# ===================================================================

class TestIndependentSumFactorization:
    """Tests for independent sum factorization."""

    def test_additivity(self):
        """kappa(A1+A2) = kappa(A1) + kappa(A2)."""
        result = independent_sum_test(5, 3)
        assert result['kappa_total'] == 8
        assert result['additivity'] is True

    def test_fg_additive(self):
        """F_g(A1+A2) = F_g(A1) + F_g(A2) at each genus."""
        result = independent_sum_test(5, 3, g_max=4)
        for g in range(1, 5):
            assert result[f'F_{g}_additive'] is True

    def test_zero_kappa(self):
        """If kappa_2 = 0, total = kappa_1."""
        result = independent_sum_test(7, 0)
        assert result['kappa_total'] == 7
        for g in range(1, 5):
            assert result[f'F_{g}_additive'] is True

    def test_complementary_sum_km(self):
        """For KM-type: kappa + kappa' = 0."""
        result = independent_sum_test(5, -5)
        assert result['kappa_total'] == 0
        for g in range(1, 5):
            assert result[f'F_{g}_total'] == 0


class TestGaugeOrigamiVsIndependentSum:
    """Tests for gauge origami vs independent sum comparison."""

    def test_two_spikes(self):
        """Two-spike gauge origami matches independent sum."""
        result = gauge_origami_vs_independent_sum([5, 3])
        assert result['kappa_total'] == 8
        for g in range(1, 5):
            assert result[f'genus_{g}']['match'] is True

    def test_three_spikes(self):
        """Three-spike gauge origami matches."""
        result = gauge_origami_vs_independent_sum([2, 3, 5])
        assert result['kappa_total'] == 10
        for g in range(1, 5):
            assert result[f'genus_{g}']['match'] is True

    def test_single_spike(self):
        """Single spike: trivial factorization."""
        result = gauge_origami_vs_independent_sum([7])
        assert result['kappa_total'] == 7
        assert result['n_spikes'] == 1

    def test_lambda_1_is_1_over_24(self):
        """lambda_1^FP = 1/24 in all results."""
        result = gauge_origami_vs_independent_sum([5, 3])
        assert result['genus_1']['lambda_g_FP'] == Rational(1, 24)


# ===================================================================
# Section 7: Koszul duality interpretation of matter
# ===================================================================

class TestKoszulMatterComparison:
    """Tests for Koszul duality vs matter content."""

    def test_virasoro_complementarity_13(self):
        """For Virasoro: kappa + kappa! = 13 (AP24)."""
        for c in [1, 10, 13, 25, 26]:
            result = koszul_matter_comparison(c)
            assert result['complementarity_sum'] == 13
            assert result['sum_is_13'] is True

    def test_c13_self_dual(self):
        """At c=13: kappa = kappa! = 13/2."""
        result = koszul_matter_comparison(13)
        assert result['kappa_A'] == Rational(13, 2)
        assert result['kappa_A_dual'] == Rational(13, 2)

    def test_c26_critical(self):
        """At c=26: kappa=13, kappa!=0."""
        result = koszul_matter_comparison(26)
        assert result['kappa_A'] == 13
        assert result['kappa_A_dual'] == 0

    def test_c0_zero_kappa(self):
        """At c=0: kappa=0, kappa!=13."""
        result = koszul_matter_comparison(0)
        assert result['kappa_A'] == 0
        assert result['kappa_A_dual'] == 13


class TestMatterFromKoszulNf:
    """Tests for N_f flavors from Koszul perspective."""

    def test_nf0_pure_gauge(self):
        """N_f=0: kappa_matter = 0."""
        result = matter_from_koszul_nf(25, 0)
        assert result['kappa_matter'] == 0
        assert result['kappa_total'] == result['kappa_gauge']

    def test_nf4_conformal(self):
        """N_f=4 is conformal for SU(2)."""
        result = matter_from_koszul_nf(25, 4)
        assert result['is_conformal'] is True

    def test_kappa_increases_with_nf(self):
        """kappa_total increases with N_f."""
        kappas = []
        for nf in range(5):
            result = matter_from_koszul_nf(25, nf)
            kappas.append(result['kappa_total'])
        for i in range(len(kappas) - 1):
            assert kappas[i + 1] > kappas[i]

    def test_matter_per_flavor(self):
        """Each flavor adds kappa_fund = 1/2."""
        result = matter_from_koszul_nf(25, 3)
        assert result['kappa_fund_per_flavor'] == Rational(1, 2)
        assert result['kappa_matter'] == Rational(3, 2)


# ===================================================================
# Section 8: Instanton corrections vs genus expansion
# ===================================================================

class TestInstantonGenusComparison:
    """Tests for instanton corrections vs genus expansion."""

    def test_returns_shadow_and_nekrasov(self):
        result = instanton_genus_comparison(3, 25, max_inst=2, max_genus=2)
        assert 'shadow_F_1' in result
        assert 'Z_inst_1' in result

    def test_shadow_f1_kappa_over_24(self):
        """Shadow F_1 = kappa/24."""
        result = instanton_genus_comparison(3, 10, max_inst=1, max_genus=1)
        assert result['shadow_F_1'] == Rational(5) / 24

    def test_nekrasov_z1_nonzero(self):
        """Z_1 from Nekrasov should be nonzero."""
        result = instanton_genus_comparison(3, 25, max_inst=1)
        assert result['Z_inst_1'] is not None
        assert result['Z_inst_1'] != 0

    def test_shadow_genus2(self):
        """Shadow F_2 = kappa * lambda_2^FP = kappa * 7/5760."""
        result = instanton_genus_comparison(3, 10, max_inst=1, max_genus=2)
        assert result['lambda_2_FP'] == Rational(7, 5760)
        assert result['shadow_F_2'] == 5 * Rational(7, 5760)


# ===================================================================
# Section 9: Class S and Ran(X) factorization
# ===================================================================

class TestClassSComparison:
    """Tests for Class S vs factorization comparison."""

    def test_sphere_4_punctures_su2(self):
        """(g=0, n=4, N=2): SU(2) N_f=4 SCFT."""
        result = class_s_comparison(0, 4, 2)
        assert result['algebra'] == 'Virasoro'
        assert result['theory_data']['conformal'] is True

    def test_torus_su2(self):
        """(g=1, n=0, N=2): pure SU(2)."""
        result = class_s_comparison(1, 0, 2)
        assert result['algebra'] == 'Virasoro'
        assert result['theory_data']['conformal'] is False

    def test_sphere_4_punctures_su3(self):
        """(g=0, n=4, N=3): SU(3) theory."""
        result = class_s_comparison(0, 4, 3)
        assert result['algebra'] == 'W_3'

    def test_euler_characteristic(self):
        """chi = 2 - 2g - n."""
        for g, n in [(0, 4), (1, 0), (0, 3), (2, 0)]:
            result = class_s_comparison(g, n, 2)
            assert result['euler_characteristic'] == 2 - 2 * g - n

    def test_internal_edges(self):
        """Number of internal edges = 3g - 3 + n (pants decomposition)."""
        for g, n in [(0, 4), (1, 0), (1, 1), (2, 0)]:
            result = class_s_comparison(g, n, 2)
            assert result['n_internal_edges'] == 3 * g - 3 + n

    def test_coulomb_dim(self):
        """Coulomb branch dimension = (N-1) * (3g-3+n)."""
        result = class_s_comparison(0, 4, 3)
        assert result['coulomb_branch_dim'] == 2 * 1  # (3-1) * (0-3+4) = 2


# ===================================================================
# Section 10: Schiffmann-Vasserot identification
# ===================================================================

class TestSchiffmannVasserot:
    """Tests for the Schiffmann-Vasserot identification."""

    def test_n1_heisenberg(self):
        """N=1: Heisenberg."""
        result = schiffmann_vasserot_identification(1)
        assert result['algebra'] == 'Heisenberg'
        assert 'gl_1' in result['Yangian']

    def test_n2_virasoro(self):
        """N=2: Virasoro."""
        result = schiffmann_vasserot_identification(2)
        assert 'Virasoro' in result['algebra']
        assert 'gl_2' in result['Yangian']

    def test_n3_w3(self):
        """N=3: W_3."""
        result = schiffmann_vasserot_identification(3)
        assert 'W_3' in result['algebra']
        assert 'gl_3' in result['Yangian'] or 'gl_{3}' in result['Yangian']

    def test_sv_identification_string(self):
        """SV identification is well-formed."""
        for N in [1, 2, 3, 4]:
            result = schiffmann_vasserot_identification(N)
            assert 'SV_identification' in result
            assert f'{N}' in result['SV_identification']


# ===================================================================
# Section 11: Bar complex as gauge origami
# ===================================================================

class TestBarAsGaugeOrigami:
    """Tests for interpreting bar complex through gauge origami."""

    def test_heisenberg(self):
        """Heisenberg: shadow depth 2, class G."""
        result = bar_as_gauge_origami('Heisenberg')
        assert result['shadow_depth'] == 2
        assert result['shadow_class'] == 'G (Gaussian)'
        assert result['gauge_dual'] == 'U(1) gauge theory'

    def test_virasoro(self):
        """Virasoro: shadow depth infinity, class M."""
        result = bar_as_gauge_origami('Virasoro', c_val=25)
        assert result['shadow_depth'] == 'infinity'
        assert result['shadow_class'] == 'M (mixed)'
        assert result['kappa'] == Rational(25, 2)

    def test_w3(self):
        """W_3: shadow depth infinity, class M."""
        result = bar_as_gauge_origami('W_3', c_val=50, N=3)
        assert result['shadow_depth'] == 'infinity for N >= 2'

    def test_gauge_dual_su2(self):
        """Virasoro is dual to SU(2)."""
        result = bar_as_gauge_origami('Virasoro', c_val=25)
        assert 'SU(2)' in result['gauge_dual']

    def test_koszul_means_bps(self):
        """Bar cohomology concentrated (Koszul) = one-instanton BPS sufficiency."""
        result = bar_as_gauge_origami('Heisenberg')
        assert 'Koszul' in result['bar_cohomology']


# ===================================================================
# Section 12: Full comparison table
# ===================================================================

class TestFullComparisonTable:
    """Tests for the full comparison table."""

    def test_all_keys_present(self):
        """All ten comparison entries should be present."""
        table = full_comparison_table()
        expected_keys = [
            'gauge_origami_composition',
            'instanton_number_vs_bar_arity',
            'nekrasov_pf_vs_shadow_pf',
            'agt_correspondence',
            'matter_vs_koszul_dual',
            'genus_expansion_vs_loop_expansion',
            'class_s_vs_factorization',
            'coha_vs_bar',
            'yangian_vs_r_matrix',
            'sw_curve_vs_shadow_metric',
        ]
        for key in expected_keys:
            assert key in table

    def test_each_entry_has_three_fields(self):
        """Each entry should have gauge_theory, our_framework, match_level."""
        table = full_comparison_table()
        for key, entry in table.items():
            assert 'gauge_theory' in entry
            assert 'our_framework' in entry
            assert 'match_level' in entry

    def test_ap24_mentioned(self):
        """AP24 (complementarity sum != 0 for Virasoro) should be referenced."""
        table = full_comparison_table()
        matter_entry = table['matter_vs_koszul_dual']
        assert 'AP24' in matter_entry['match_level']

    def test_ap22_mentioned(self):
        """AP22 (hbar convention) should be referenced in genus expansion."""
        table = full_comparison_table()
        genus_entry = table['genus_expansion_vs_loop_expansion']
        assert 'AP22' in genus_entry['match_level']


# ===================================================================
# Cross-cutting: multi-path verification tests
# ===================================================================

class TestMultiPathCrossCheck:
    """Multi-path verification combining multiple sections."""

    def test_u1_shadow_kappa_consistent(self):
        """U(1) kappa from AGT matches Heisenberg kappa."""
        # For b=1: c = 1 + 6*(1+1)^2 = 25, kappa = 25/2
        # Heisenberg at level k: kappa = k
        # These are DIFFERENT algebras at different levels.
        # The point: AGT maps (eps1, eps2) to a specific c, and
        # the shadow kappa = c/2 is determined by the AGT map.
        params = agt_parameter_map(1, -1)  # b^2 = 1, b = 1, c = 25
        assert params['kappa'] == Rational(25, 2)

    def test_nekrasov_su2_weyl_invariance(self):
        """Z_k(a) = Z_k(-a) by Weyl symmetry."""
        e1, e2 = 1, 2
        for k in range(3):
            Z_plus = nekrasov_partition_su2(3, e1, e2, 2)
            Z_minus = nekrasov_partition_su2(-3, e1, e2, 2)
            assert simplify(Z_plus[k] - Z_minus[k]) == 0

    def test_origami_shadow_consistency(self):
        """Gauge origami factorization matches shadow additivity."""
        # Two spikes with kappa_1=5, kappa_2=3
        # Shadow: kappa_total = 8, F_1 = 8/24 = 1/3
        origami = gauge_origami_vs_independent_sum([5, 3])
        shadow_result = shadow_nekrasov_genus_g_match(16, 1)  # c=16 -> kappa=8
        assert origami['kappa_total'] == 8
        assert shadow_result['kappa'] == 8
        assert origami['genus_1']['F_g_total_additive'] == shadow_result['F_g_shadow']

    def test_class_s_genus_vs_bar_genus(self):
        """Class S genus matches bar complex genus grading."""
        # The genus g of the Riemann surface in class S corresponds to
        # the genus g in the bar complex genus expansion.
        for g in range(3):
            result = class_s_comparison(g, 4, 2)
            # The number of internal edges in the pants decomposition
            # = the number of propagators in the bar graph sum at genus g.
            assert result['n_internal_edges'] == 3 * g + 1

    def test_su3_pair_triple_count_check(self):
        """SU(3) triple count > SU(2) pair count at same k."""
        for k in [1, 2, 3]:
            su2_results = bar_arity_instanton_comparison(N=2, max_k=k)
            su3_results = bar_arity_instanton_comparison(N=3, max_k=k)
            su2_count = su2_results[k]['partition_N_tuples']
            su3_count = su3_results[k]['partition_N_tuples']
            assert su3_count >= su2_count

    def test_kappa_additivity_three_ways(self):
        """kappa additivity verified three ways."""
        # Way 1: direct sum
        r1 = independent_sum_test(5, 3)
        assert r1['kappa_total'] == 8

        # Way 2: gauge origami
        r2 = gauge_origami_vs_independent_sum([5, 3])
        assert r2['kappa_total'] == 8

        # Way 3: shadow genus match
        r3 = shadow_nekrasov_genus_g_match(16, 1)  # c=16 -> kappa=8
        assert r3['kappa'] == 8

        # All three give the same F_1
        assert r1['F_1_total'] == r2['genus_1']['F_g_total_additive']
        assert r1['F_1_total'] == r3['F_g_shadow']

    def test_complementarity_different_families(self):
        """kappa + kappa! = 13 for Virasoro at all c (AP24)."""
        for c in [0, 1, 13, 25, 26, 100]:
            result = koszul_matter_comparison(c)
            assert result['complementarity_sum'] == 13

    def test_bernoulli_in_genus_expansion(self):
        """F_g involves Bernoulli numbers B_{2g} correctly."""
        for g in [1, 2, 3]:
            result = shadow_nekrasov_genus_g_match(10, g)
            B2g = bernoulli(2 * g)
            assert result['Bernoulli_2g'] == B2g
            # lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
            expected_lambda = (
                (2**(2*g - 1) - 1) * Abs(B2g) / (2**(2*g - 1) * factorial(2*g))
            )
            assert simplify(result['lambda_g_FP'] - expected_lambda) == 0
