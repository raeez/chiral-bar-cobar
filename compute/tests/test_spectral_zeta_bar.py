#!/usr/bin/env python3
r"""
test_spectral_zeta_bar.py -- Tests for spectral zeta from bar cohomology.

Tests organized by mathematical content:

    1. Partition infrastructure
    2. Quasi-primary counts d(h)
    3. Bar cohomology H^1 via CE
    4. d(h) != H^1(B(V))_h (the central falsification)
    5. Koszul dual Hilbert series
    6. Koszul character identity chi_V * chi_{A!}(-q) = 1
    7. Spectral zeta computation
    8. Divergence analysis
    9. Comparison table
   10. Bar route to spectrum
   11. Motzkin differences vs quasi-primaries
   12. Growth rate comparisons
   13. c-independence
   14. Cross-checks with existing modules
"""

import sys
import os
import math
import pytest
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from spectral_zeta_bar import (
    partition_count,
    p_ge2,
    quasi_primary_count,
    bar_h1_ce_virasoro,
    bar_h2_ce_virasoro,
    koszul_dual_hilbert_series,
    koszul_dual_unsigned_hilbert,
    comparison_table,
    spectral_zeta_bar,
    spectral_zeta_koszul_dual,
    verify_koszul_character_identity,
    growth_comparison,
    dirichlet_abscissa,
    truncated_functional_equation,
    bar_route_to_spectrum,
    c_dependence_of_quasi_primaries,
    motzkin_vs_quasi_primary,
)


# ================================================================
# 1. Partition infrastructure
# ================================================================

class TestPartitions:
    """Partition counting functions."""

    def test_partition_base_cases(self):
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7

    def test_partition_oeis(self):
        """OEIS A000041 values."""
        expected = {10: 42, 15: 176, 20: 627, 50: 204226}
        for n, val in expected.items():
            assert partition_count(n) == val

    def test_p_ge2_base_cases(self):
        assert p_ge2(0) == 1
        assert p_ge2(1) == 0
        assert p_ge2(2) == 1
        assert p_ge2(3) == 1
        assert p_ge2(4) == 2
        assert p_ge2(5) == 2
        assert p_ge2(6) == 4

    def test_p_ge2_equals_p_minus_p_prev(self):
        """p_{>=2}(n) = p(n) - p(n-1) for n >= 2."""
        for n in range(2, 30):
            assert p_ge2(n) == partition_count(n) - partition_count(n - 1)

    def test_p_ge2_nondecreasing(self):
        """p_{>=2}(h) is nondecreasing for h >= 2."""
        for h in range(2, 50):
            assert p_ge2(h + 1) >= p_ge2(h), f"p_ge2 decreased at h={h}"


# ================================================================
# 2. Quasi-primary counts d(h)
# ================================================================

class TestQuasiPrimaryCounts:
    """d(h) = p_{>=2}(h) - p_{>=2}(h-1) for the Virasoro vacuum."""

    def test_d_0(self):
        assert quasi_primary_count(0) == 1

    def test_d_1(self):
        assert quasi_primary_count(1) == 0

    def test_d_2(self):
        """Weight 2: single quasi-primary T."""
        assert quasi_primary_count(2) == 1

    def test_d_3(self):
        """Weight 3: L_{-3}|0> = L_{-1}(L_{-2}|0>) is a descendant."""
        assert quasi_primary_count(3) == 0

    def test_d_4(self):
        """Weight 4: one quasi-primary (Lambda = :TT: - (3/10)partial^2 T)."""
        assert quasi_primary_count(4) == 1

    def test_d_odd_low(self):
        """Odd weights 3, 5, 7 have no quasi-primaries."""
        assert quasi_primary_count(3) == 0
        assert quasi_primary_count(5) == 0
        assert quasi_primary_count(7) == 0

    def test_d_9_first_odd(self):
        """Weight 9: first odd-weight quasi-primary."""
        assert quasi_primary_count(9) == 1

    def test_d_sequence(self):
        """Full sequence of d(h) for h = 0..20."""
        expected = [1, 0, 1, 0, 1, 0, 2, 0, 3, 1, 4, 2, 7, 3, 10, 7, 14, 11, 22, 17, 32]
        for h, d in enumerate(expected):
            assert quasi_primary_count(h) == d, f"d({h}) should be {d}"

    def test_d_nonneg(self):
        """d(h) >= 0 for all h >= 2."""
        for h in range(2, 100):
            assert quasi_primary_count(h) >= 0

    def test_d_first_values_match_constrained_epstein(self):
        """Cross-check with virasoro_constrained_epstein.py."""
        from virasoro_constrained_epstein import quasi_primary_count as qpc_ref
        for h in range(50):
            assert quasi_primary_count(h) == qpc_ref(h), f"Mismatch at h={h}"


# ================================================================
# 3. Bar cohomology H^1 via CE
# ================================================================

class TestBarH1CE:
    """CE computation of H^1(B(Vir))."""

    def test_h1_at_2(self):
        h1 = bar_h1_ce_virasoro(4)
        assert h1[2] == 1

    def test_h1_at_3(self):
        h1 = bar_h1_ce_virasoro(4)
        assert h1[3] == 1

    def test_h1_at_4(self):
        h1 = bar_h1_ce_virasoro(5)
        assert h1[4] == 1

    def test_h1_at_5(self):
        """H^1 vanishes at weight 5 (the pair (2,3) gives nonzero d)."""
        h1 = bar_h1_ce_virasoro(6)
        assert h1[5] == 0

    def test_h1_vanishes_above_4(self):
        """H^1(B(Vir))_h = 0 for all h >= 5."""
        h1 = bar_h1_ce_virasoro(30)
        for h in range(5, 31):
            assert h1.get(h, 0) == 0, f"H^1 should vanish at weight {h}"

    def test_total_h1(self):
        """Total dim H^1 = 3 (three generators of A!)."""
        h1 = bar_h1_ce_virasoro(20)
        total = sum(v for v in h1.values() if v > 0)
        assert total == 3

    def test_h1_matches_virasoro_bar_explicit(self):
        """Cross-check with virasoro_bar_explicit.py CE computation."""
        try:
            from virasoro_bar_explicit import virasoro_bar_h1_dims
            ref = virasoro_bar_h1_dims(14)
            h1 = bar_h1_ce_virasoro(14)
            for h in range(2, 15):
                assert h1.get(h, 0) == ref.get(h, 0), f"Mismatch at weight {h}"
        except ImportError:
            pytest.skip("virasoro_bar_explicit not available")


# ================================================================
# 4. THE CENTRAL FALSIFICATION: d(h) != H^1(B(V))_h
# ================================================================

class TestCentralFalsification:
    """Prove that d(h) is NOT H^1(B(V))_h."""

    def test_d_and_h1_agree_at_2(self):
        """At weight 2, both are 1 (coincidence)."""
        assert quasi_primary_count(2) == 1
        h1 = bar_h1_ce_virasoro(3)
        assert h1[2] == 1

    def test_d_and_h1_disagree_at_3(self):
        """At weight 3: d(3) = 0 but H^1_3 = 1."""
        assert quasi_primary_count(3) == 0
        h1 = bar_h1_ce_virasoro(4)
        assert h1[3] == 1
        # DIFFERENT!

    def test_d_and_h1_disagree_at_6(self):
        """At weight 6: d(6) = 2 but H^1_6 = 0."""
        assert quasi_primary_count(6) == 2
        h1 = bar_h1_ce_virasoro(7)
        assert h1[6] == 0
        # DIFFERENT!

    def test_d_and_h1_disagree_at_8(self):
        """At weight 8: d(8) = 3 but H^1_8 = 0."""
        assert quasi_primary_count(8) == 3
        h1 = bar_h1_ce_virasoro(9)
        assert h1[8] == 0

    def test_d_grows_h1_terminates(self):
        """d(h) grows without bound; H^1_h is eventually zero."""
        h1 = bar_h1_ce_virasoro(50)
        # d(h) > 0 for infinitely many h
        assert quasi_primary_count(20) > 0
        assert quasi_primary_count(50) > 0
        # H^1_h = 0 for h >= 5
        for h in range(5, 51):
            assert h1.get(h, 0) == 0

    def test_total_h1_is_3_but_total_d_is_infinite(self):
        """Sum of H^1 = 3 (finite); sum of d(h) diverges."""
        h1 = bar_h1_ce_virasoro(20)
        assert sum(v for v in h1.values()) == 3
        assert sum(quasi_primary_count(h) for h in range(20)) > 50


# ================================================================
# 5. Koszul dual Hilbert series
# ================================================================

class TestKoszulDualHilbert:
    """Koszul dual A! alternating character from bar cohomology.

    chi_{A!}(q) = 1 - 1/chi_V(q) = sum_h [H^1_h - H^2_h + ...] q^h
    """

    def test_kd_weight_0(self):
        """At weight 0: chi_{A!}(0) = 0 (ground field cancels)."""
        kd = koszul_dual_hilbert_series(10)
        assert kd[0] == 0

    def test_kd_weight_1(self):
        kd = koszul_dual_hilbert_series(10)
        assert kd[1] == 0

    def test_kd_weight_2(self):
        """A! has one generator at weight 2 (H^1_2 = 1)."""
        kd = koszul_dual_hilbert_series(10)
        assert kd[2] == 1

    def test_kd_weight_3(self):
        """A! has one generator at weight 3 (H^1_3 = 1)."""
        kd = koszul_dual_hilbert_series(10)
        assert kd[3] == 1

    def test_kd_weight_4(self):
        """A! has one generator at weight 4 (H^1_4 = 1)."""
        kd = koszul_dual_hilbert_series(10)
        assert kd[4] == 1

    def test_kd_weight_5_6_vanish(self):
        """No bar cohomology at weights 5, 6."""
        kd = koszul_dual_hilbert_series(10)
        assert kd[5] == 0
        assert kd[6] == 0

    def test_kd_weight_7_negative(self):
        """Weight 7: H^2 = 1, so alternating character = -1."""
        kd = koszul_dual_hilbert_series(10)
        assert kd[7] == -1

    def test_kd_first_values(self):
        """Full alternating character through weight 11."""
        kd = koszul_dual_hilbert_series(12)
        # chi_{A!} = 1 - 1/chi_V
        # = 0 + 0 + q^2 + q^3 + q^4 + 0 + 0 - q^7 - q^8 - q^9 - q^10 - q^11 + ...
        assert kd[:12] == [0, 0, 1, 1, 1, 0, 0, -1, -1, -1, -1, -1]

    def test_kd_recovers_chi_V(self):
        """chi_V(q) = 1/(1 - chi_{A!}(q)), verified through order 20."""
        N = 20
        kd = koszul_dual_hilbert_series(N)
        # (1 - chi_{A!}(q)) coefficients
        one_minus_kd = [Fraction(0)] * N
        one_minus_kd[0] = Fraction(1) - Fraction(kd[0])
        for h in range(1, N):
            one_minus_kd[h] = -Fraction(kd[h])

        # Invert to get chi_V = 1/(1 - chi_{A!})
        chi_V_recovered = [Fraction(0)] * N
        chi_V_recovered[0] = Fraction(1)
        for h in range(1, N):
            s = Fraction(0)
            for j in range(1, h + 1):
                s += one_minus_kd[j] * chi_V_recovered[h - j]
            chi_V_recovered[h] = -s

        for h in range(N):
            assert chi_V_recovered[h] == p_ge2(h), f"chi_V mismatch at h={h}"

    def test_unsigned_hilbert(self):
        """Unsigned bar cohomology dimensions from known computation."""
        known = koszul_dual_unsigned_hilbert(10)
        assert known[2] == {1: 1}
        assert known[3] == {1: 1}
        assert known[4] == {1: 1}
        assert known[7] == {2: 1}


# ================================================================
# 6. Koszul character identity
# ================================================================

class TestKoszulCharacterIdentity:
    """chi_V(q) * (1 - chi_{A!}(q)) = 1."""

    def test_identity_order_10(self):
        result = verify_koszul_character_identity(10)
        assert result['verified'], f"Errors: {result['errors']}"

    def test_identity_order_20(self):
        result = verify_koszul_character_identity(20)
        assert result['verified'], f"Errors: {result['errors']}"

    def test_identity_order_30(self):
        result = verify_koszul_character_identity(30)
        assert result['verified'], f"Errors: {result['errors']}"

    def test_identity_is_the_correct_one(self):
        """The identity is chi_V * (1 - chi_{A!}) = 1, not chi_V * chi_{A!}(-q) = 1."""
        result = verify_koszul_character_identity(10)
        assert 'chi_V(q) * (1 - chi_{A!}(q)) = 1' in result['identity']


# ================================================================
# 7. Spectral zeta computation
# ================================================================

class TestSpectralZeta:
    """Spectral zeta from bar cohomology."""

    def test_spectral_zeta_s2_positive(self):
        """At s=2, the truncated sum should be positive (all terms positive)."""
        eps = spectral_zeta_bar(2.0, h_max=50)
        assert eps.real > 0

    def test_spectral_zeta_s2_first_term(self):
        """First term: d(2)*(4)^{-2} = 1/16."""
        eps_1 = spectral_zeta_bar(2.0, h_max=2)
        assert abs(eps_1 - 1 / 16) < 1e-12

    def test_spectral_zeta_s3_first_term(self):
        """At s=3: first term d(2)*(4)^{-3} = 1/64."""
        eps_1 = spectral_zeta_bar(3.0, h_max=2)
        assert abs(eps_1 - 1 / 64) < 1e-12

    def test_spectral_zeta_increases_with_hmax(self):
        """Truncated sum increases with h_max (all terms positive)."""
        eps_50 = spectral_zeta_bar(2.0, h_max=50).real
        eps_100 = spectral_zeta_bar(2.0, h_max=100).real
        assert eps_100 > eps_50

    def test_spectral_zeta_diverges(self):
        """At s=2, the sum grows without bound as h_max increases."""
        vals = [spectral_zeta_bar(2.0, h_max=N).real
                for N in [50, 100, 200, 500]]
        # Each should be larger than the previous
        for i in range(len(vals) - 1):
            assert vals[i + 1] > vals[i]
        # And the differences should be GROWING (divergence)
        diff1 = vals[1] - vals[0]
        diff2 = vals[2] - vals[1]
        diff3 = vals[3] - vals[2]
        assert diff3 > diff2 > diff1

    def test_spectral_zeta_complex_s(self):
        """Computation at complex s."""
        eps = spectral_zeta_bar(2 + 1j, h_max=50)
        assert isinstance(eps, complex)
        assert eps.real != 0

    def test_regularized_spectral_zeta(self):
        """Cesaro regularization gives a finite value."""
        eps_reg = spectral_zeta_bar(2.0, h_max=200, regularize=True)
        assert math.isfinite(eps_reg.real)


# ================================================================
# 8. Divergence analysis
# ================================================================

class TestDivergence:
    """Abscissa of convergence and divergence analysis."""

    def test_abscissa_infinite(self):
        result = dirichlet_abscissa()
        assert result['abscissa_absolute'] == float('inf')
        assert result['abscissa_conditional'] == float('inf')

    def test_turning_points_exist(self):
        result = dirichlet_abscissa()
        for sigma in [2, 5, 10, 20]:
            assert sigma in result['turning_points']
            assert result['turning_points'][sigma] > 0

    def test_growth_constant(self):
        result = dirichlet_abscissa()
        C = math.pi * math.sqrt(2 / 3)
        assert abs(result['growth_constant_C'] - C) < 1e-10


# ================================================================
# 9. Comparison table
# ================================================================

class TestComparisonTable:
    """Three-way comparison: d(h), H^1_h, (A!)_h."""

    def test_table_has_correct_columns(self):
        table = comparison_table(10)
        row = table[2]  # weight 2
        assert 'weight' in row
        assert 'd_h' in row
        assert 'bar_H1_h' in row
        assert 'koszul_dual_dim_h' in row

    def test_table_weight_2(self):
        table = comparison_table(10)
        row = table[2]
        assert row['weight'] == 2
        assert row['d_h'] == 1
        assert row['bar_H1_h'] == 1
        assert row['dim_V_h'] == 1

    def test_table_weight_6(self):
        """At weight 6: d(6) = 2, H^1_6 = 0."""
        table = comparison_table(10)
        row = table[6]
        assert row['d_h'] == 2
        assert row['bar_H1_h'] == 0

    def test_all_three_differ(self):
        """The three sequences are genuinely different."""
        table = comparison_table(15)
        d_seq = [row['d_h'] for row in table[2:]]
        h1_seq = [row['bar_H1_h'] for row in table[2:]]
        # d and H^1 are different sequences
        assert d_seq != h1_seq


# ================================================================
# 10. Bar route to spectrum
# ================================================================

class TestBarRoute:
    """Full chain: B(V) -> H^* -> A! -> chi_V -> d(h) -> eps."""

    def test_step1_bar_cohomology(self):
        result = bar_route_to_spectrum(14)
        h1 = result['step1_bar_cohomology']
        assert h1 == {2: 1, 3: 1, 4: 1}

    def test_step5_quasi_primaries(self):
        result = bar_route_to_spectrum(10)
        qp = result['step5_quasi_primaries']
        assert qp[2] == 1
        assert qp[4] == 1
        assert qp[6] == 2
        assert qp[8] == 3

    def test_step4_matches_p_ge2(self):
        result = bar_route_to_spectrum(10)
        chi_V = result['step4_vacuum_character']
        for h in range(11):
            assert chi_V[h] == p_ge2(h)

    def test_chain_consistency(self):
        """The chain B(V) -> ... -> d(h) recovers the correct d(h)."""
        result = bar_route_to_spectrum(14)
        qp = result['step5_quasi_primaries']
        for h in range(2, 15):
            expected = quasi_primary_count(h)
            got = qp.get(h, 0)
            assert got == expected, f"Chain inconsistent at h={h}: {got} vs {expected}"


# ================================================================
# 11. Motzkin differences vs quasi-primaries
# ================================================================

class TestMotzkinVsQuasiPrimary:
    """The Motzkin differences are NOT quasi-primary counts."""

    def test_sequences_differ(self):
        result = motzkin_vs_quasi_primary()
        md = result['motzkin_differences']['sequence']
        qp = result['quasi_primary_counts']['sequence']
        assert md != qp

    def test_motzkin_diffs_grow_faster(self):
        """Motzkin diffs grow as 3^n, quasi-primaries grow as exp(C sqrt(h))."""
        result = motzkin_vs_quasi_primary()
        md = result['motzkin_differences']['sequence']
        qp = result['quasi_primary_counts']['sequence']
        # At comparable indices, Motzkin diffs are larger for large n
        # md[10] vs qp[10] (h=12 for qp since it starts at h=2)
        assert md[10] > qp[10]

    def test_not_equal_flag(self):
        result = motzkin_vs_quasi_primary()
        assert result['are_equal'] is False

    def test_motzkin_first_values(self):
        """Motzkin diffs: 1, 2, 5, 12, 30, 76, 196, ..."""
        result = motzkin_vs_quasi_primary()
        md = result['motzkin_differences']['sequence']
        assert md[:7] == [1, 2, 5, 12, 30, 76, 196]

    def test_quasi_primary_first_values(self):
        """d(h) for h=2..15: 1, 0, 1, 0, 2, 0, 3, 1, 4, 2, 7, 3, 10, 7."""
        result = motzkin_vs_quasi_primary()
        qp = result['quasi_primary_counts']['sequence']
        assert qp[:14] == [1, 0, 1, 0, 2, 0, 3, 1, 4, 2, 7, 3, 10, 7]


# ================================================================
# 12. Growth rate comparisons
# ================================================================

class TestGrowthRates:
    """Growth rate analysis of the three sequences."""

    def test_growth_data_nonempty(self):
        result = growth_comparison(30)
        assert len(result['quasi_primary_growth']) > 0
        assert len(result['koszul_dual_growth']) > 0
        assert len(result['bar_h1']) > 0

    def test_quasi_primary_growth_subexponential(self):
        """d(h) grows subexponentially: log(d(h)) ~ C*sqrt(h) for large h."""
        import math
        C = math.pi * math.sqrt(2 / 3)
        # For large h, log(d(h)) should be approximately C*sqrt(h) (up to log factors)
        # Test: log(d(h)) / sqrt(h) should stabilize for large h
        from spectral_zeta_bar import quasi_primary_count
        ratios = []
        for h in range(50, 101):
            d = quasi_primary_count(h)
            if d > 0:
                ratios.append(math.log(d) / math.sqrt(h))
        # Should cluster near C (but below it due to log correction)
        assert all(0.5 < r < C + 1 for r in ratios)

    def test_bar_h1_finite_support(self):
        """H^1 is zero for h >= 5."""
        result = growth_comparison(20)
        h1_data = result['bar_h1']
        for item in h1_data:
            if item['h'] >= 5:
                assert item['H^1_h'] == 0


# ================================================================
# 13. c-independence
# ================================================================

class TestCIndependence:
    """d(h) is independent of c at generic c."""

    def test_c_independent_flag(self):
        result = c_dependence_of_quasi_primaries(10)
        assert result['c_independent'] is True

    def test_generic_d_matches(self):
        result = c_dependence_of_quasi_primaries(14)
        for h, d in result['generic_d'].items():
            assert d == quasi_primary_count(h)

    def test_minimal_model_deviations_exist(self):
        """Minimal models have different d(h) due to null vectors."""
        result = c_dependence_of_quasi_primaries(14)
        assert len(result['minimal_model_deviations']) > 0

    def test_ising_model(self):
        """c=1/2 Ising model (4,3): 3 primaries at h=0, 1/2, 1/16."""
        result = c_dependence_of_quasi_primaries(14)
        ising = result['minimal_model_deviations'].get((4, 3))
        assert ising is not None
        assert abs(ising['c'] - 0.5) < 1e-10
        assert ising['num_primaries'] == 3  # (p-1)(q-1)/2 = 3*2/2 = 3

    def test_trivial_model(self):
        """c=0 trivial model (3,2): 1 primary (vacuum only)."""
        result = c_dependence_of_quasi_primaries(14)
        trivial = result['minimal_model_deviations'].get((3, 2))
        assert trivial is not None
        assert abs(trivial['c']) < 1e-10
        assert trivial['num_primaries'] == 1  # (2)(1)/2 = 1


# ================================================================
# 14. Cross-checks with existing modules
# ================================================================

class TestCrossChecks:
    """Cross-validation with other compute modules."""

    def test_constrained_epstein_match(self):
        """spectral_zeta_bar matches constrained_epstein for same inputs."""
        from virasoro_constrained_epstein import constrained_epstein
        for s in [2.0, 3.0, 5.0]:
            eps_new = spectral_zeta_bar(s, h_max=100)
            eps_ref = constrained_epstein(s, h_max=100)
            assert abs(eps_new - eps_ref) < 1e-10, f"Mismatch at s={s}"

    def test_bar_character_algebraic_motzkin(self):
        """Motzkin numbers match between modules."""
        from bar_character_algebraic import motzkin_numbers
        M = motzkin_numbers(15)
        expected = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188, 5798, 15511, 41835, 113634]
        assert M == expected

    def test_bar_h1_explicit_vs_ce(self):
        """virasoro_bar_explicit CE matches our CE computation."""
        try:
            from virasoro_bar_explicit import virasoro_bar_h1_dims
            ref = virasoro_bar_h1_dims(20)
            ours = bar_h1_ce_virasoro(20)
            for h in range(2, 21):
                assert ours.get(h, 0) == ref.get(h, 0), f"h={h}"
        except ImportError:
            pytest.skip("virasoro_bar_explicit not available")

    def test_theta_deformation_quasi_primaries(self):
        """Cross-check d(h) against theta_deformation_complex at c=1."""
        try:
            from theta_deformation_complex import virasoro_quasi_primary_basis
            for h in [2, 4, 6, 8]:
                _, qp, _ = virasoro_quasi_primary_basis(h, c_val=1)
                assert len(qp) == quasi_primary_count(h), f"Mismatch at h={h}"
        except ImportError:
            pytest.skip("theta_deformation_complex not available")

    def test_koszul_dual_alternating_character(self):
        """Alternating character chi_{A!} has sign pattern matching bar degrees.

        Positive at weights where H^1 > 0 (generators: h = 2, 3, 4).
        Negative at weights where H^2 > 0 (relations: h = 7, 8, ...).
        """
        kd = koszul_dual_hilbert_series(12)
        # Generators (H^1): positive
        assert kd[2] > 0
        assert kd[3] > 0
        assert kd[4] > 0
        # Relations (H^2): negative
        assert kd[7] < 0
        assert kd[8] < 0


# ================================================================
# 15. Spectral zeta of Koszul dual
# ================================================================

class TestKoszulDualZeta:
    """Zeta function of A! Hilbert series."""

    def test_kd_zeta_computes(self):
        result = spectral_zeta_koszul_dual(2.0, N=30)
        assert isinstance(result, complex)

    def test_kd_zeta_positive_at_s2(self):
        """First term is dim(A!)_2 * 2^{-2} = 1/4."""
        result = spectral_zeta_koszul_dual(2.0, N=3)
        # Only weights 2 and possibly 3 contribute
        assert result.real > 0


# ================================================================
# 16. Truncated functional equation
# ================================================================

class TestFunctionalEquation:
    """Test truncated series for approximate symmetries."""

    def test_no_exact_functional_equation(self):
        """The truncated series has no exact s -> 1-s symmetry."""
        result = truncated_functional_equation(h_max=50, s_values=[2.0])
        r = result['results'][0]
        ratio_1 = r['tests'][1]['ratio']
        # If there were a functional equation s -> 1-s, the ratio would be
        # a simple function of s.  It should not be 1 or any simple value.
        if not (isinstance(ratio_1, float) and math.isnan(ratio_1)):
            assert abs(ratio_1 - 1.0) > 0.01  # not approximately 1


# ================================================================
# 17. Verma dimension cross-check
# ================================================================

class TestVermaModuleDimensions:
    """Verify dim V_h = p_{>=2}(h)."""

    def test_dim_V_sequence(self):
        """OEIS-verified: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21, 24, 34, ..."""
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21, 24, 34, 41, 55, 66, 88, 105]
        for h, val in enumerate(expected):
            assert p_ge2(h) == val, f"p_ge2({h}) = {p_ge2(h)}, expected {val}"

    def test_d_as_first_difference(self):
        """d(h) = p_{>=2}(h) - p_{>=2}(h-1)."""
        for h in range(2, 50):
            assert quasi_primary_count(h) == p_ge2(h) - p_ge2(h - 1)
