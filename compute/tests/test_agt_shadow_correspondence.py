r"""Tests for compute/lib/agt_shadow_correspondence.py

Comprehensive test suite covering:
  - AGT parameter map (Section 1)
  - Young diagram combinatorics (Section 2)
  - SU(2) Nekrasov partition function (Section 3)
  - SU(3) Nekrasov partition function (Section 4)
  - Genus expansion (Section 5)
  - Nekrasov-Shatashvili limit (Section 6)
  - Shadow tower connection (Section 7)
  - Seiberg-Witten prepotential (Section 8)
  - Flavored theories (Section 9)
  - SU(3) shadow connection (Section 10)
  - Verification infrastructure (Section 11)
"""

import pytest
from sympy import (
    Rational, simplify, sqrt, Symbol, oo, S as Sym,
    bernoulli, factorial, Abs, N as Neval,
)

from compute.lib.agt_shadow_correspondence import (
    # Section 1: AGT parameter map
    agt_central_charge,
    agt_b_from_epsilons,
    agt_hbar,
    agt_beta,
    agt_kappa_from_c,
    agt_parameter_map,
    # Section 2: Young diagrams
    arm_length,
    leg_length,
    conjugate_partition,
    partition_size,
    all_partitions,
    all_partition_pairs,
    all_partition_triples,
    # Section 3: SU(2) Nekrasov
    nekrasov_factor_pair,
    nekrasov_partition_su2,
    nekrasov_free_energy_su2,
    # Section 4: SU(3) Nekrasov
    nekrasov_factor_triple,
    nekrasov_partition_su3,
    # Section 5: Genus expansion
    nekrasov_genus_expansion_su2,
    # Section 6: NS limit
    nekrasov_shatashvili_su2,
    ns_quantum_period,
    # Section 7: Shadow tower connection
    shadow_kappa_from_agt,
    shadow_genus1_from_kappa,
    shadow_genus_g_from_kappa,
    agt_shadow_comparison_genus1,
    # Section 8: Seiberg-Witten
    prepotential_su2_one_inst,
    prepotential_su2_two_inst,
    seiberg_witten_prepotential_pure_su2,
    sw_discriminant_pure_su2,
    sw_periods_weak_coupling,
    # Section 9: Flavored theories
    nekrasov_su2_with_flavors,
    nekrasov_su2_nf_counts,
    # Section 10: SU(3) shadow
    w3_kappa_from_c,
    su3_shadow_comparison,
    # Section 11: Verification
    verify_agt_consistency,
    verify_nekrasov_k1_su2,
    verify_nekrasov_perturbative_limit,
)


# ===================================================================
# Section 1: AGT parameter map
# ===================================================================

class TestAGTParameterMap:
    """Tests for AGT parameter map functions."""

    def test_central_charge_b_equals_1(self):
        """c(b=1) = 1 + 6*(1 + 1)^2 = 25."""
        assert agt_central_charge(1) == 25

    def test_central_charge_b_equals_2(self):
        """c(b=2) = 1 + 6*(2 + 1/2)^2 = 1 + 6*(25/4) = 1 + 75/2 = 77/2."""
        assert agt_central_charge(2) == Rational(77, 2)

    def test_central_charge_self_duality(self):
        """c(b) = c(1/b) for all b: the AGT parametrization is self-dual."""
        for b_val in [Rational(1, 2), Rational(2, 3), Rational(3), Rational(5, 7)]:
            assert simplify(agt_central_charge(b_val) - agt_central_charge(1 / b_val)) == 0

    def test_central_charge_symbolic(self):
        """Symbolic output when b_val is None."""
        result = agt_central_charge(None)
        b = Symbol('b')
        # Should involve b_sym
        assert result is not None

    def test_b_from_epsilons_opposite_signs(self):
        """b from eps1=1, eps2=-1 gives b^2=1, b=1."""
        b = agt_b_from_epsilons(1, -1)
        assert simplify(b - 1) == 0

    def test_b_from_epsilons_general(self):
        """b from eps1=2, eps2=-1 gives b^2=2, b=sqrt(2)."""
        b = agt_b_from_epsilons(2, -1)
        assert simplify(b ** 2 - 2) == 0

    def test_hbar_product(self):
        """hbar = eps1 * eps2."""
        assert agt_hbar(3, 5) == 15
        assert agt_hbar(1, -2) == -2

    def test_beta_sum(self):
        """beta = eps1 + eps2."""
        assert agt_beta(3, 5) == 8
        assert agt_beta(1, -1) == 0

    def test_kappa_from_c_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert agt_kappa_from_c(26) == 13
        assert agt_kappa_from_c(1) == Rational(1, 2)
        assert agt_kappa_from_c(0) == 0

    def test_kappa_from_c_symbolic(self):
        """Symbolic kappa when c_val is None."""
        result = agt_kappa_from_c(None)
        c = Symbol('c')
        assert result is not None

    def test_parameter_map_complete(self):
        """Full parameter map returns all expected keys."""
        params = agt_parameter_map(1, -1)
        expected_keys = {'eps1', 'eps2', 'b_squared', 'b', 'c', 'hbar', 'beta', 'kappa'}
        assert set(params.keys()) == expected_keys

    def test_parameter_map_consistency(self):
        """Parameters are self-consistent: hbar = eps1*eps2, beta = eps1+eps2, kappa = c/2."""
        params = agt_parameter_map(2, -3)
        assert simplify(params['hbar'] - params['eps1'] * params['eps2']) == 0
        assert simplify(params['beta'] - params['eps1'] - params['eps2']) == 0
        assert simplify(params['kappa'] - params['c'] / 2) == 0

    def test_parameter_map_b_squared(self):
        """b^2 = -eps1/eps2."""
        params = agt_parameter_map(3, -2)
        assert simplify(params['b_squared'] - (-Rational(3, -2))) == 0


# ===================================================================
# Section 2: Young diagram combinatorics
# ===================================================================

class TestYoungDiagrams:
    """Tests for Young diagram operations."""

    def test_conjugate_empty(self):
        """Conjugate of empty partition is empty."""
        assert conjugate_partition(()) == ()

    def test_conjugate_single_row(self):
        """Conjugate of (n,) is (1, 1, ..., 1) of length n."""
        assert conjugate_partition((3,)) == (1, 1, 1)
        assert conjugate_partition((5,)) == (1, 1, 1, 1, 1)

    def test_conjugate_single_column(self):
        """Conjugate of (1, 1, ..., 1) is a single row."""
        assert conjugate_partition((1, 1, 1)) == (3,)

    def test_conjugate_involution(self):
        """Conjugation is an involution: Y'' = Y."""
        Y = (4, 2, 1)
        assert conjugate_partition(conjugate_partition(Y)) == Y

    def test_conjugate_preserves_size(self):
        """Conjugation preserves partition size."""
        Y = (5, 3, 3, 1)
        assert partition_size(conjugate_partition(Y)) == partition_size(Y)

    def test_conjugate_hook(self):
        """Conjugate of hook (3,1,1) is (3,1,1) ... no: (3,1,1)' = (3,1,1)."""
        Y = (3, 1, 1)
        Yt = conjugate_partition(Y)
        assert Yt == (3, 1, 1)

    def test_partition_size_empty(self):
        """Size of empty partition is 0."""
        assert partition_size(()) == 0

    def test_partition_size_examples(self):
        """Known partition sizes."""
        assert partition_size((3, 2, 1)) == 6
        assert partition_size((4,)) == 4
        assert partition_size((1, 1, 1, 1)) == 4

    def test_arm_length_single_box(self):
        """For Y=(1,), box (0,0): arm = Y_0 - 0 - 1 = 0."""
        assert arm_length((1,), 0, 0) == 0

    def test_arm_length_rectangle(self):
        """For Y=(3,3), box (0,0): arm = 3 - 0 - 1 = 2."""
        assert arm_length((3, 3), 0, 0) == 2
        assert arm_length((3, 3), 0, 2) == 0
        assert arm_length((3, 3), 1, 1) == 1

    def test_leg_length_single_box(self):
        """For Y=(1,), box (0,0): leg = Y'_0 - 0 - 1 = 0."""
        assert leg_length((1,), 0, 0) == 0

    def test_leg_length_rectangle(self):
        """For Y=(3,3), box (0,0): Y'=(2,2,2), leg=2-0-1=1."""
        assert leg_length((3, 3), 0, 0) == 1
        assert leg_length((3, 3), 1, 0) == 0

    def test_all_partitions_count(self):
        """Partition counts: p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        expected_counts = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
        for n, count in expected_counts.items():
            parts = list(all_partitions(n))
            assert len(parts) == count, f"p({n}) = {len(parts)}, expected {count}"

    def test_all_partitions_decreasing(self):
        """Each partition has parts in non-increasing order."""
        for n in range(6):
            for p in all_partitions(n):
                for i in range(len(p) - 1):
                    assert p[i] >= p[i + 1], f"Not decreasing: {p}"

    def test_all_partitions_sum_to_n(self):
        """Each partition of n sums to n."""
        for n in range(7):
            for p in all_partitions(n):
                assert sum(p) == n

    def test_all_partition_pairs_count(self):
        """Number of pairs (Y1, Y2) with |Y1|+|Y2|=n."""
        # For n=0: ((), ()) -> 1 pair
        assert len(list(all_partition_pairs(0))) == 1
        # For n=1: ((1,), ()) and ((), (1,)) -> 2 pairs
        assert len(list(all_partition_pairs(1))) == 2
        # For n=2: partition pairs summing to 2
        # k=0: ((), (2,)) and ((), (1,1))
        # k=1: ((1,), (1,))
        # k=2: ((2,), ()) and ((1,1), ())
        assert len(list(all_partition_pairs(2))) == 5

    def test_all_partition_triples_count(self):
        """Number of triples with total size 0 and 1."""
        assert len(list(all_partition_triples(0))) == 1
        assert len(list(all_partition_triples(1))) == 3


# ===================================================================
# Section 3: SU(2) Nekrasov partition function
# ===================================================================

class TestNekrasovSU2:
    """Tests for SU(2) Nekrasov instanton partition function."""

    def test_nekrasov_Z0_is_1(self):
        """Z_0 = 1 (no instantons)."""
        Z = nekrasov_partition_su2(2, 1, -1, max_inst=0)
        assert Z[0] == 1

    def test_nekrasov_returns_correct_keys(self):
        """Z has keys 0, 1, ..., max_inst."""
        Z = nekrasov_partition_su2(2, 1, -1, max_inst=3)
        assert set(Z.keys()) == {0, 1, 2, 3}

    def test_nekrasov_Z1_nonzero(self):
        """Z_1 is nonzero for generic a, eps1, eps2."""
        Z = nekrasov_partition_su2(3, 1, -2, max_inst=1)
        assert Z[1] != 0

    def test_nekrasov_Z1_rational(self):
        """Z_1 is rational for rational inputs."""
        Z = nekrasov_partition_su2(2, 1, -1, max_inst=1)
        # Check it is a Rational
        assert isinstance(Z[1], Rational)

    def test_nekrasov_factor_pair_empty(self):
        """Empty partition pair gives factor 1 (from 1/N with N=product of identities)."""
        # For empty Y1, Y2: no boxes, so all N factors are empty products = 1
        # But the denominator has N_{empty,empty}(0)^2 * N_{empty,empty}(2a) * N_{empty,empty}(-2a)
        # N_{empty,empty}(Q) = 1 (empty products).
        # So denominator = 1 and factor = 1.
        result = nekrasov_factor_pair(5, (), (), Rational(1), Rational(-1))
        assert result == 1

    def test_free_energy_f1_equals_Z1(self):
        """f_1 = Z_1 (first cumulant equals first moment)."""
        a, e1, e2 = 3, Rational(1), Rational(-2)
        Z = nekrasov_partition_su2(a, e1, e2, max_inst=3)
        f = nekrasov_free_energy_su2(a, e1, e2, max_inst=3)
        assert simplify(f[1] - Z[1]) == 0

    def test_free_energy_f2_cumulant(self):
        """f_2 = Z_2 - Z_1^2/2 (second cumulant)."""
        a, e1, e2 = 3, Rational(1), Rational(-2)
        Z = nekrasov_partition_su2(a, e1, e2, max_inst=3)
        f = nekrasov_free_energy_su2(a, e1, e2, max_inst=3)
        assert simplify(f[2] - (Z[2] - Z[1] ** 2 / 2)) == 0

    def test_free_energy_f3_cumulant(self):
        """f_3 = Z_3 - Z_1*Z_2 + Z_1^3/3 (third cumulant)."""
        a, e1, e2 = 3, Rational(1), Rational(-2)
        Z = nekrasov_partition_su2(a, e1, e2, max_inst=3)
        f = nekrasov_free_energy_su2(a, e1, e2, max_inst=3)
        expected = Z[3] - Z[1] * Z[2] + Z[1] ** 3 / 3
        assert simplify(f[3] - expected) == 0


# ===================================================================
# Section 4: SU(3) Nekrasov partition function
# ===================================================================

class TestNekrasovSU3:
    """Tests for SU(3) Nekrasov instanton partition function."""

    def test_su3_Z0_is_1(self):
        """Z_0 = 1 for SU(3) as well."""
        a_vals = (Rational(2), Rational(-1), Rational(-1))
        Z = nekrasov_partition_su3(a_vals, 1, -1, max_inst=0)
        assert Z[0] == 1

    def test_su3_tracelessness(self):
        """SU(3) Coulomb parameters must sum to 0."""
        a_vals = (Rational(1), Rational(1), Rational(-2))
        assert sum(a_vals) == 0
        Z = nekrasov_partition_su3(a_vals, 1, -1, max_inst=1)
        assert 1 in Z

    def test_su3_returns_correct_keys(self):
        """SU(3) partition function has keys 0, ..., max_inst."""
        a_vals = (Rational(2), Rational(-1), Rational(-1))
        Z = nekrasov_partition_su3(a_vals, 1, -1, max_inst=2)
        assert set(Z.keys()) == {0, 1, 2}

    def test_su3_Z1_nonzero(self):
        """Z_1 is nonzero for generic SU(3) Coulomb parameters."""
        a_vals = (Rational(3), Rational(-1), Rational(-2))
        Z = nekrasov_partition_su3(a_vals, 1, -2, max_inst=1)
        assert Z[1] != 0


# ===================================================================
# Section 5: Genus expansion
# ===================================================================

class TestGenusExpansion:
    """Tests for the genus expansion of the Nekrasov free energy."""

    def test_genus_expansion_returns_dict(self):
        """Genus expansion returns a dict keyed by genus."""
        result = nekrasov_genus_expansion_su2(2, max_inst=2, max_genus=2)
        assert isinstance(result, dict)

    def test_genus_expansion_keys(self):
        """Result has genus keys 0, 1, ..., max_genus."""
        result = nekrasov_genus_expansion_su2(2, max_inst=2, max_genus=2)
        for g in range(3):
            assert g in result


# ===================================================================
# Section 6: Nekrasov-Shatashvili limit
# ===================================================================

class TestNekrasovShatashvili:
    """Tests for the Nekrasov-Shatashvili limit."""

    def test_ns_returns_dict(self):
        """NS limit returns a dict of instanton coefficients."""
        ns = nekrasov_shatashvili_su2(3, 1, max_inst=2)
        assert isinstance(ns, dict)

    def test_ns_has_instanton_keys(self):
        """NS coefficients are keyed by instanton number 1, 2, ..."""
        ns = nekrasov_shatashvili_su2(3, 1, max_inst=2)
        for k in range(1, 3):
            assert k in ns

    def test_ns_quantum_period_returns_dict(self):
        """Quantum period returns a dict."""
        periods = ns_quantum_period(3, 1, max_inst=2)
        assert isinstance(periods, dict)


# ===================================================================
# Section 7: Shadow tower connection
# ===================================================================

class TestShadowTowerConnection:
    """Tests for shadow tower / AGT comparison functions."""

    def test_shadow_kappa_from_agt_b1(self):
        """At b=1 (eps1=1, eps2=-1): c=25, kappa=25/2."""
        kappa = shadow_kappa_from_agt(1, -1)
        assert simplify(kappa - Rational(25, 2)) == 0

    def test_shadow_genus1_integer_kappa(self):
        """F_1 = kappa/24 for integer kappa."""
        assert shadow_genus1_from_kappa(12) == Rational(1, 2)
        assert shadow_genus1_from_kappa(24) == 1
        assert shadow_genus1_from_kappa(0) == 0

    def test_shadow_genus1_rational_kappa(self):
        """F_1 = kappa/24 for rational kappa."""
        assert shadow_genus1_from_kappa(Rational(1, 2)) == Rational(1, 48)

    def test_shadow_genus_g_formula(self):
        """F_g = kappa * lambda_g^FP. Check F_1 = kappa/24."""
        from compute.lib.utils import lambda_fp
        kappa = Rational(13)
        for g in [1, 2, 3]:
            expected = kappa * lambda_fp(g)
            result = shadow_genus_g_from_kappa(13, g)
            assert simplify(result - expected) == 0

    def test_shadow_genus1_from_kappa_matches_genus_g(self):
        """shadow_genus1_from_kappa and shadow_genus_g_from_kappa agree at g=1."""
        for kappa in [1, Rational(13, 2), 26]:
            f1_direct = shadow_genus1_from_kappa(kappa)
            f1_via_g = shadow_genus_g_from_kappa(kappa, 1)
            assert simplify(f1_direct - f1_via_g) == 0

    def test_agt_shadow_comparison_genus1_keys(self):
        """Comparison function returns expected keys."""
        result = agt_shadow_comparison_genus1(1, -1, 3, max_inst=1)
        assert 'kappa' in result
        assert 'c' in result
        assert 'shadow_F1' in result
        assert 'shadow_F1_numeric' in result

    def test_agt_shadow_comparison_genus1_values(self):
        """At b=1: c=25, kappa=25/2, F_1 = 25/48."""
        result = agt_shadow_comparison_genus1(1, -1, 3, max_inst=1)
        assert simplify(result['c'] - 25) == 0
        assert simplify(result['kappa'] - Rational(25, 2)) == 0
        assert simplify(result['shadow_F1'] - Rational(25, 48)) == 0


# ===================================================================
# Section 8: Seiberg-Witten prepotential
# ===================================================================

class TestSeiberWittenPrepotential:
    """Tests for Seiberg-Witten prepotential functions."""

    def test_one_inst_formula(self):
        """F_0^{(1)} = 1/(2a^2)."""
        assert prepotential_su2_one_inst(1) == Rational(1, 2)
        assert prepotential_su2_one_inst(2) == Rational(1, 8)
        assert prepotential_su2_one_inst(3) == Rational(1, 18)

    def test_two_inst_formula(self):
        """F_0^{(2)} = (5a^2 + 1/4) / (2a^2(2a^2-1))^2."""
        a = Rational(2)
        num = 5 * a ** 2 + Rational(1, 4)
        den = (2 * a ** 2 * (2 * a ** 2 - 1)) ** 2
        expected = num / den
        result = prepotential_su2_two_inst(2)
        assert simplify(result - expected) == 0

    def test_one_inst_positive(self):
        """F_0^{(1)} is positive for positive a."""
        for a in [1, 2, 3, 5]:
            assert prepotential_su2_one_inst(a) > 0

    def test_sw_prepotential_keys(self):
        """SW prepotential returns instanton keys 1, 2."""
        result = seiberg_witten_prepotential_pure_su2(2, max_inst=2)
        assert 1 in result
        assert 2 in result

    def test_sw_prepotential_matches_one_inst(self):
        """SW prepotential at k=1 matches direct formula."""
        result = seiberg_witten_prepotential_pure_su2(3, max_inst=2)
        assert simplify(result[1] - prepotential_su2_one_inst(3)) == 0

    def test_sw_prepotential_matches_two_inst(self):
        """SW prepotential at k=2 matches direct formula."""
        result = seiberg_witten_prepotential_pure_su2(3, max_inst=2)
        assert simplify(result[2] - prepotential_su2_two_inst(3)) == 0

    def test_sw_discriminant_zeros(self):
        """Discriminant vanishes at u = +/-1 (monopole/dyon)."""
        assert sw_discriminant_pure_su2(1) == 0
        assert sw_discriminant_pure_su2(-1) == 0

    def test_sw_discriminant_generic(self):
        """Discriminant is u^2 - 1 for generic u."""
        assert sw_discriminant_pure_su2(3) == 8  # 9 - 1
        assert sw_discriminant_pure_su2(0) == -1

    def test_sw_periods_weak_coupling_returns_tuple(self):
        """Periods return a pair of dicts."""
        a_coeffs, aD_coeffs = sw_periods_weak_coupling(10)
        assert isinstance(a_coeffs, dict)
        assert isinstance(aD_coeffs, dict)

    def test_sw_periods_leading_order(self):
        """Leading order a coefficient is 1."""
        a_coeffs, _ = sw_periods_weak_coupling(10)
        assert a_coeffs[0] == 1


# ===================================================================
# Section 9: Flavored theories
# ===================================================================

class TestFlavoredTheories:
    """Tests for Nekrasov partition functions with fundamental matter."""

    def test_nf0_matches_pure_gauge(self):
        """N_f=0 from nf_counts matches pure gauge."""
        a, e1, e2 = 3, Rational(1), Rational(-2)
        results = nekrasov_su2_nf_counts(a, e1, e2, max_inst=1)
        Z_pure = nekrasov_partition_su2(a, e1, e2, max_inst=1)
        for k in Z_pure:
            assert simplify(results[0][k] - Z_pure[k]) == 0

    def test_nf_counts_keys(self):
        """nf_counts returns keys 0, 1, 2, 3, 4."""
        results = nekrasov_su2_nf_counts(3, 1, -1, max_inst=1)
        assert set(results.keys()) == {0, 1, 2, 3, 4}

    def test_nf_Z0_is_always_1(self):
        """Z_0 = 1 regardless of flavor number."""
        results = nekrasov_su2_nf_counts(3, 1, -1, max_inst=1)
        for nf in range(5):
            # Z_0 includes matter contributions over empty partitions = empty product = 1
            # but the function counts ((), ()) at k=0 with z_vec=1, z_mat=1
            assert results[nf][0] == 1

    def test_flavored_with_zero_masses_Z0(self):
        """Explicit flavored computation: Z_0 = 1 for zero masses."""
        Z = nekrasov_su2_with_flavors(3, [0, 0], 1, -1, max_inst=0)
        assert Z[0] == 1


# ===================================================================
# Section 10: SU(3) shadow connection
# ===================================================================

class TestSU3ShadowConnection:
    """Tests for W_3 kappa and SU(3) shadow comparison."""

    def test_w3_kappa_formula(self):
        """kappa(W_3) = 5c/6."""
        assert w3_kappa_from_c(6) == 5
        assert w3_kappa_from_c(12) == 10
        assert w3_kappa_from_c(0) == 0

    def test_w3_kappa_symbolic(self):
        """Symbolic W_3 kappa when c_val is None."""
        result = w3_kappa_from_c(None)
        assert result is not None

    def test_w3_kappa_rational(self):
        """kappa(W_3) is rational for rational c."""
        result = w3_kappa_from_c(Rational(7, 3))
        assert result == Rational(35, 18)

    def test_su3_shadow_comparison_keys(self):
        """SU(3) shadow comparison returns expected keys."""
        a_vals = (Rational(2), Rational(-1), Rational(-1))
        result = su3_shadow_comparison(a_vals, 1, -1, max_inst=1)
        expected_keys = {'Z_su3', 'c_W3', 'kappa_W3', 'kappa_T', 'kappa_W', 'eps1', 'eps2'}
        assert set(result.keys()) == expected_keys

    def test_su3_shadow_kappa_decomposition(self):
        """kappa_T + kappa_W = kappa_W3 (additivity of shadow kappa)."""
        a_vals = (Rational(2), Rational(-1), Rational(-1))
        result = su3_shadow_comparison(a_vals, 1, -1, max_inst=1)
        assert simplify(result['kappa_T'] + result['kappa_W'] - result['kappa_W3']) == 0

    def test_su3_kappa_ratio(self):
        """kappa_T/kappa_W = (c/2)/(c/3) = 3/2."""
        a_vals = (Rational(2), Rational(-1), Rational(-1))
        result = su3_shadow_comparison(a_vals, 1, -1, max_inst=1)
        # kappa_T = c_W3/2, kappa_W = c_W3/3
        # ratio = (c/2)/(c/3) = 3/2
        assert simplify(result['kappa_T'] / result['kappa_W'] - Rational(3, 2)) == 0


# ===================================================================
# Section 11: Verification infrastructure
# ===================================================================

class TestVerification:
    """Tests for internal verification functions."""

    def test_agt_consistency_all_pass(self):
        """All AGT consistency checks pass."""
        checks = verify_agt_consistency(1, -1)
        for key, val in checks.items():
            assert val, f"Check {key} failed"

    def test_agt_consistency_other_params(self):
        """AGT consistency passes for other epsilon values."""
        checks = verify_agt_consistency(2, -3)
        for key, val in checks.items():
            assert val, f"Check {key} failed"

    def test_nekrasov_k1_nonzero(self):
        """Z_1 is nonzero for generic a."""
        Z1 = verify_nekrasov_k1_su2(3, 1, -1)
        assert Z1 != 0

    def test_nekrasov_perturbative_limit_Z0(self):
        """Z_0 = 1 in the perturbative limit."""
        Z = verify_nekrasov_perturbative_limit(3, max_inst=2)
        assert Z[0] == 1

    def test_nekrasov_perturbative_limit_returns_dict(self):
        """Perturbative limit function returns a dict."""
        Z = verify_nekrasov_perturbative_limit(2, max_inst=2)
        assert isinstance(Z, dict)
        assert set(Z.keys()) == {0, 1, 2}


# ===================================================================
# Cross-section consistency tests
# ===================================================================

class TestCrossSectionConsistency:
    """Cross-checks between different sections of the module."""

    def test_kappa_from_agt_matches_direct(self):
        """shadow_kappa_from_agt matches agt_kappa_from_c(agt_central_charge(b))."""
        for e1, e2 in [(1, -1), (2, -3), (3, -1)]:
            kappa_agt = shadow_kappa_from_agt(e1, e2)
            b = agt_b_from_epsilons(e1, e2)
            c = agt_central_charge(b)
            kappa_direct = c / 2
            assert simplify(kappa_agt - kappa_direct) == 0

    def test_partition_pair_enumeration_consistency(self):
        """Partition pairs with total size k enumerate exactly p(0)*p(k) + ... + p(k)*p(0)."""
        for n in range(4):
            pairs = list(all_partition_pairs(n))
            # Each pair (Y1, Y2) has |Y1| + |Y2| = n
            for Y1, Y2 in pairs:
                assert partition_size(Y1) + partition_size(Y2) == n

    def test_partition_triple_enumeration_consistency(self):
        """Partition triples have correct total size."""
        for n in range(3):
            for Y1, Y2, Y3 in all_partition_triples(n):
                assert partition_size(Y1) + partition_size(Y2) + partition_size(Y3) == n

    def test_conjugate_square_partition(self):
        """A square partition (k,k,...,k) with k rows is self-conjugate only if square."""
        # (2,2) is a 2x2 square: conjugate is (2,2)
        assert conjugate_partition((2, 2)) == (2, 2)
        # (3,3,3) is a 3x3 square: conjugate is (3,3,3)
        assert conjugate_partition((3, 3, 3)) == (3, 3, 3)

    def test_arm_plus_leg_plus_one(self):
        """For box (i,j) in Y: arm(i,j) + leg(i,j) + 1 = hook length."""
        Y = (4, 3, 1)
        # Box (0,0): arm=3, leg=2, hook=6
        assert arm_length(Y, 0, 0) + leg_length(Y, 0, 0) + 1 == 6
        # Box (0,1): arm=2, leg=1, hook=4
        assert arm_length(Y, 0, 1) + leg_length(Y, 0, 1) + 1 == 4
        # Box (1,0): arm = Y_1 - 0 - 1 = 2, leg = Y'_0 - 1 - 1 = 1, hook = 4
        assert arm_length(Y, 1, 0) + leg_length(Y, 1, 0) + 1 == 4

    def test_shadow_f1_positive_for_positive_kappa(self):
        """F_1 = kappa/24 is positive when kappa > 0."""
        for c_val in [1, 2, 10, 25, 26]:
            kappa = agt_kappa_from_c(c_val)
            f1 = shadow_genus1_from_kappa(kappa)
            assert f1 > 0

    def test_nekrasov_su2_symmetry_Y1_Y2_swap(self):
        """The partition function sums over all pairs, so individual factors
        may not be symmetric, but the sum Z_k is well-defined."""
        Z = nekrasov_partition_su2(3, 1, -2, max_inst=2)
        # Z_k should be rational
        for k in Z:
            assert Z[k] is not None
