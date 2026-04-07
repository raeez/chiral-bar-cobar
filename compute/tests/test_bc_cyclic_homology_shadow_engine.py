r"""Tests for BC-127: Cyclic homology of shadow algebras and Chern character at zeros.

85+ tests covering:
  1. Hochschild homology HH_n via HKR (Omega^n)
  2. Cyclic homology HC_n via SBI sequence
  3. Periodic cyclic HP_n
  4. Chern character ch: K_0 -> HP_0
  5. Connes periodicity operator S
  6. Loday-Quillen-Tsygan verification
  7. Family-specific computations (Heisenberg, Virasoro, sl_2, beta-gamma, W_3)
  8. Evaluation at zeta zeros rho_1, ..., rho_20
  9. Cross-path consistency (5 verification paths)
  10. Deformation-theoretic data at zeros

Multi-path verification:
  (i) HKR isomorphism
  (ii) SBI exact sequence
  (iii) Chern character
  (iv) Loday-Quillen-Tsygan
  (v) Numerical evaluation
"""

import math
import pytest

from compute.lib.bc_cyclic_homology_shadow_engine import (
    # Data constructors
    ShadowAlgebraData,
    heisenberg_shadow_data,
    virasoro_shadow_data,
    affine_sl2_shadow_data,
    betagamma_shadow_data,
    w3_shadow_data,
    # HH
    binomial,
    hh_dimension,
    hh_dimensions_all,
    hh_euler_characteristic,
    hh_graded_vector,
    # HC
    hc_dimension_module,
    hc_dimensions_all,
    hc_euler_characteristic_truncated,
    connes_b_rank,
    # SBI
    sbi_sequence_check,
    # HP
    hp_dimension,
    hp_dimensions,
    # Chern character
    chern_character_rank_one,
    chern_character_projective,
    # LQT
    lqt_verification,
    # Zeta zeros
    get_zeta_zero_gamma,
    get_zeta_zero,
    c_from_zeta_zero,
    kappa_from_zeta_zero,
    # Computations at zeros
    shadow_data_at_zeta_zero,
    hh_at_zeta_zero,
    hc_at_zeta_zeros_batch,
    # Connes periodicity
    connes_periodicity_data,
    periodicity_at_zeta_zeros,
    # Numerical
    numerical_hh_evaluated,
    hh_family_table,
    # Kahler
    kahler_differentials_basis,
    kahler_module_data,
    # Negative cyclic / Dennis
    negative_cyclic_dimension,
    dennis_trace_data,
    # Full verification
    full_verification,
    # Master
    master_cyclic_homology_at_zeros,
    # Deformation
    deformation_hh_virasoro,
    deformation_data_at_zeros,
)


# ============================================================================
# Test group 1: Binomial coefficients and basic combinatorics
# ============================================================================

class TestBinomial:
    def test_binom_0_0(self):
        assert binomial(0, 0) == 1

    def test_binom_n_0(self):
        for n in range(10):
            assert binomial(n, 0) == 1

    def test_binom_n_n(self):
        for n in range(10):
            assert binomial(n, n) == 1

    def test_binom_negative(self):
        assert binomial(5, -1) == 0
        assert binomial(5, 6) == 0

    def test_binom_pascal(self):
        """Pascal's rule: C(n,k) = C(n-1,k-1) + C(n-1,k)."""
        for n in range(1, 10):
            for k in range(1, n):
                assert binomial(n, k) == binomial(n-1, k-1) + binomial(n-1, k)

    def test_binom_sum_2d(self):
        """Sum of binomials = 2^d."""
        for d in range(8):
            assert sum(binomial(d, k) for k in range(d+1)) == 2**d


# ============================================================================
# Test group 2: Hochschild homology via HKR
# ============================================================================

class TestHochschildHKR:
    """HH_n(k[x_1,...,x_d]) = Omega^n, rank C(d,n)."""

    def test_hh_d1(self):
        """Heisenberg: d=1, HH = [1, 1, 0, 0, ...]."""
        dims = hh_dimensions_all(1, 6)
        assert dims[0] == 1
        assert dims[1] == 1
        for n in range(2, 7):
            assert dims[n] == 0

    def test_hh_d2(self):
        """Affine sl_2: d=2, HH = [1, 2, 1, 0, ...]."""
        dims = hh_dimensions_all(2, 6)
        assert dims == {0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0}

    def test_hh_d3(self):
        """Beta-gamma: d=3, HH = [1, 3, 3, 1, 0, ...]."""
        dims = hh_dimensions_all(3, 6)
        assert dims == {0: 1, 1: 3, 2: 3, 3: 1, 4: 0, 5: 0, 6: 0}

    def test_hh_d4(self):
        """d=4: HH = [1, 4, 6, 4, 1, 0, 0]."""
        dims = hh_dimensions_all(4, 6)
        assert dims == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1, 5: 0, 6: 0}

    def test_hh_euler_char_vanishes(self):
        """chi_HH = sum (-1)^n C(d,n) = 0 for d >= 1."""
        for d in range(1, 10):
            assert hh_euler_characteristic(d) == 0

    def test_hh_euler_char_d0(self):
        """chi_HH = 1 for d = 0 (trivial algebra)."""
        assert hh_euler_characteristic(0) == 1

    def test_hh_total_rank_2d(self):
        """Total rank sum_{n} HH_n = 2^d."""
        for d in range(8):
            total = sum(hh_dimension(d, n) for n in range(d + 1))
            assert total == 2 ** d

    def test_hh_heisenberg_data(self):
        """HH for Heisenberg via shadow data object."""
        for k in [1, 2, 3, 4, 5]:
            data = heisenberg_shadow_data(k)
            hh = hh_graded_vector(data, 6)
            assert hh[0] == 1
            assert hh[1] == 1
            assert hh[2] == 0

    def test_hh_virasoro_data(self):
        """HH for Virasoro: class M, d depends on max_arity."""
        for c in [1, 10, 13, 25, 26]:
            data = virasoro_shadow_data(c, max_arity=10)
            d = data.effective_dim
            assert d >= 3  # At least kappa, alpha, S_4 for class M
            hh = hh_graded_vector(data, 6)
            assert hh[0] == 1
            assert hh[1] == d

    def test_hh_sl2_data(self):
        """HH for affine sl_2: d=2, class L."""
        for k in [1, 2, 3, 4, 5, 6, 7, 8]:
            data = affine_sl2_shadow_data(k)
            assert data.effective_dim == 2
            hh = hh_graded_vector(data, 6)
            assert hh == {0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0}


# ============================================================================
# Test group 3: Cyclic homology HC_n
# ============================================================================

class TestCyclicHomology:
    """HC_n for polynomial ring: HC_0=1, HC_{2m}=1 (m>=1), HC_{odd}=0."""

    def test_hc_d1(self):
        dims = hc_dimensions_all(1, 6)
        assert dims[0] == 1
        assert dims[1] == 0
        assert dims[2] == 1
        assert dims[3] == 0
        assert dims[4] == 1

    def test_hc_d2(self):
        dims = hc_dimensions_all(2, 6)
        # Same pattern: HC_0=1, HC_{even>=2}=1, HC_{odd}=0
        assert dims[0] == 1
        assert dims[1] == 0
        assert dims[2] == 1

    def test_hc_dimension_independent_of_d(self):
        """For polynomial rings, HC_n (as k-vsp at a point) depends only on parity.

        HC_0 = 1, HC_{2m} = 1 for m >= 1, HC_{2m+1} = 0.
        This is INDEPENDENT of d (the number of variables).
        """
        for d in range(1, 8):
            for n in range(7):
                expected = 1 if (n == 0 or (n >= 2 and n % 2 == 0)) else 0
                assert hc_dimension_module(d, n) == expected, \
                    f"HC_{n} wrong for d={d}: got {hc_dimension_module(d, n)}, expected {expected}"

    def test_hc_euler_truncated(self):
        """Truncated Euler char of HC."""
        for d in range(1, 5):
            chi = hc_euler_characteristic_truncated(d, 6)
            # HC_0=1, HC_2=1, HC_4=1, HC_6=1 (all +1)
            # HC_1=HC_3=HC_5=0
            # chi = 1 + 0 + 1 + 0 + 1 + 0 + 1 = 4
            assert chi == 4


# ============================================================================
# Test group 4: SBI exact sequence
# ============================================================================

class TestSBI:
    """Verify the SBI long exact sequence holds."""

    def test_sbi_d1(self):
        results = sbi_sequence_check(1, 6)
        for entry in results:
            assert entry['status'] == 'PASS'

    def test_sbi_d2(self):
        results = sbi_sequence_check(2, 6)
        for entry in results:
            assert entry['status'] == 'PASS'

    def test_sbi_d3(self):
        results = sbi_sequence_check(3, 6)
        for entry in results:
            assert entry['status'] == 'PASS'

    def test_sbi_all_dimensions(self):
        """SBI holds for all d = 1, ..., 10."""
        for d in range(1, 11):
            results = sbi_sequence_check(d, 8)
            for entry in results:
                assert entry['status'] == 'PASS'


# ============================================================================
# Test group 5: Periodic cyclic homology HP_n
# ============================================================================

class TestPeriodicCyclic:
    """HP_n: 2-periodic, HP_0 = 1, HP_1 = 0."""

    def test_hp_periodicity(self):
        """HP is 2-periodic: HP_n = HP_{n+2}, with HP_even = 1, HP_odd = 0."""
        dims = hp_dimensions(8)
        for n in range(6):
            assert dims[n] == dims[n + 2], \
                f"HP_{n} = {dims[n]} != HP_{n+2} = {dims[n+2]}"
        for n in range(8):
            assert dims[n] == (1 if n % 2 == 0 else 0), \
                f"HP_{n} = {dims[n]}, expected {1 if n % 2 == 0 else 0}"

    def test_hp_0_is_1(self):
        assert hp_dimension(0, 0) == 1

    def test_hp_1_is_0(self):
        assert hp_dimension(0, 1) == 0

    def test_hp_independent_of_d(self):
        """HP depends only on de Rham, which is trivial for poly rings."""
        for d in range(1, 8):
            # HP is the same for all d (polynomial rings are contractible)
            assert hp_dimension(d, 0) == 1
            assert hp_dimension(d, 1) == 0


# ============================================================================
# Test group 6: Chern character
# ============================================================================

class TestChernCharacter:
    """ch: K_0(A^sh) -> HP_0(A^sh)."""

    def test_ch_rank_one(self):
        """ch([A^sh]) = 1 in HP_0."""
        for d in range(1, 6):
            ch = chern_character_rank_one(d)
            assert ch['ch_value'] == 1
            assert ch['ch_is_rational']
            assert ch['ch_is_iso']
            assert ch['quillen_suslin']

    def test_ch_rank_r(self):
        """ch(r * [A^sh]) = r."""
        for r in range(1, 10):
            ch = chern_character_projective(3, r)
            assert ch['ch_value'] == r
            assert ch['is_rational']
            assert ch['is_algebraic']

    def test_ch_additivity(self):
        """ch([P] + [Q]) = ch([P]) + ch([Q])."""
        for r1 in range(1, 5):
            for r2 in range(1, 5):
                ch1 = chern_character_projective(3, r1)
                ch2 = chern_character_projective(3, r2)
                ch_sum = chern_character_projective(3, r1 + r2)
                assert ch1['ch_value'] + ch2['ch_value'] == ch_sum['ch_value']


# ============================================================================
# Test group 7: Loday-Quillen-Tsygan verification
# ============================================================================

class TestLQT:
    """LQT: HC_n = H_{n+1}(gl(A), gl(A); k) for n >= 1."""

    def test_lqt_d1(self):
        result = lqt_verification(1, 6)
        assert result['agreement']

    def test_lqt_d2(self):
        result = lqt_verification(2, 6)
        assert result['agreement']

    def test_lqt_d3(self):
        result = lqt_verification(3, 6)
        assert result['agreement']

    def test_lqt_all_d(self):
        """LQT agrees with SBI for all d = 1, ..., 10."""
        for d in range(1, 11):
            result = lqt_verification(d, 6)
            assert result['agreement'], f"LQT failed for d={d}"


# ============================================================================
# Test group 8: Zeta zeros infrastructure
# ============================================================================

class TestZetaZeros:
    """Zeta zero parameterization: c(rho_n) = 13 + 26*i*gamma_n."""

    def test_first_zero(self):
        """gamma_1 = 14.134725..."""
        gamma = get_zeta_zero_gamma(1)
        assert abs(gamma - 14.134725141734693) < 1e-10

    def test_rho_on_critical_line(self):
        """Re(rho_n) = 1/2 (critical line)."""
        for n in range(1, 21):
            rho = get_zeta_zero(n)
            assert abs(rho.real - 0.5) < 1e-10

    def test_c_at_self_dual_real(self):
        """Re(c(rho_n)) = 13 (Virasoro self-dual point)."""
        for n in range(1, 21):
            c_val = c_from_zeta_zero(n)
            assert abs(c_val.real - 13.0) < 1e-10

    def test_kappa_at_zero(self):
        """kappa(Vir_{c(rho_n)}) = c/2 (AP9: Virasoro-specific)."""
        for n in range(1, 21):
            kappa = kappa_from_zeta_zero(n)
            c_val = c_from_zeta_zero(n)
            assert abs(kappa - c_val / 2) < 1e-10

    def test_koszul_dual_conjugate(self):
        """c'(rho_n) = 26 - c(rho_n) = conj(c(rho_n)).

        Under Koszul duality c -> 26-c:
        26 - (13 + 26i*gamma) = 13 - 26i*gamma = conj(c(rho_n)).
        """
        for n in range(1, 21):
            c_val = c_from_zeta_zero(n)
            c_dual = 26.0 - c_val
            c_conj = c_val.conjugate()
            assert abs(c_dual - c_conj) < 1e-10

    def test_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24).

        At c(rho_n): kappa + kappa' = c/2 + (26-c)/2 = 13 exactly.
        """
        for n in range(1, 21):
            kappa = kappa_from_zeta_zero(n)
            c_val = c_from_zeta_zero(n)
            kappa_dual = (26.0 - c_val) / 2.0
            assert abs(kappa + kappa_dual - 13.0) < 1e-10


# ============================================================================
# Test group 9: HH/HC at zeta zeros
# ============================================================================

class TestHomologyAtZeros:
    """Homological invariants at c = c(rho_n)."""

    def test_hh_at_first_zero(self):
        """HH at rho_1 is well-defined."""
        result = hh_at_zeta_zero(1)
        assert result['zeta_zero_index'] == 1
        assert result['effective_dim'] >= 3  # class M
        assert result['HH'][0] == 1  # HH_0 = A^sh

    def test_hh_uniform_across_zeros(self):
        """HH module ranks are the same at all zeros (topological invariance)."""
        results = hc_at_zeta_zeros_batch(20, max_deg=6)
        hh_at_1 = tuple(results[0]['HH'][k] for k in range(7))
        for r in results[1:]:
            hh_at_n = tuple(r['HH'][k] for k in range(7))
            assert hh_at_n == hh_at_1, \
                f"HH differs at zero #{r['zeta_zero_index']}"

    def test_hc_uniform_across_zeros(self):
        """HC is the same at all zeros."""
        results = hc_at_zeta_zeros_batch(20, max_deg=6)
        hc_at_1 = tuple(results[0]['HC'][k] for k in range(7))
        for r in results[1:]:
            hc_at_n = tuple(r['HC'][k] for k in range(7))
            assert hc_at_n == hc_at_1

    def test_chi_hh_zero_at_zeros(self):
        """chi_HH = 0 at all zeta zeros (standard result for d >= 1)."""
        results = hc_at_zeta_zeros_batch(20, max_deg=6)
        for r in results:
            assert r['chi_HH'] == 0

    def test_chi_hc_positive_at_zeros(self):
        """chi_HC (truncated) is positive at all zeros."""
        results = hc_at_zeta_zeros_batch(20, max_deg=6)
        for r in results:
            # chi_HC = 1 + 1 + 1 + 1 = 4 for max_deg=6
            assert r['chi_HC'] == 4

    def test_chi_hc_is_integer(self):
        """chi_HC is always an integer (as it must be)."""
        results = hc_at_zeta_zeros_batch(20, max_deg=6)
        for r in results:
            assert isinstance(r['chi_HC'], int)


# ============================================================================
# Test group 10: Connes periodicity
# ============================================================================

class TestConnesPeriodicity:
    """Connes S operator: HC_n -> HC_{n-2}."""

    def test_periodicity_never_degenerates_poly(self):
        """S: HC_n -> HC_{n-2} is id: k->k for n even >= 4, never degenerates."""
        for d in range(1, 8):
            per = connes_periodicity_data(d, 8)
            assert not per['any_degeneration']

    def test_periodicity_at_zeros(self):
        """S does not degenerate at any zeta zero."""
        result = periodicity_at_zeta_zeros(20)
        assert result['universal_non_degeneration']

    def test_periodicity_d_independence(self):
        """Periodicity structure is independent of d for d >= 1."""
        per1 = connes_periodicity_data(1, 8)
        per3 = connes_periodicity_data(3, 8)
        per5 = connes_periodicity_data(5, 8)
        # All should have the same degeneration status
        assert per1['any_degeneration'] == per3['any_degeneration'] == per5['any_degeneration']


# ============================================================================
# Test group 11: Family-specific tables
# ============================================================================

class TestFamilyTables:
    """HH for specific families at multiple parameter values."""

    def test_heisenberg_table(self):
        result = hh_family_table('heisenberg', [1, 2, 3, 4, 5], max_deg=6)
        assert len(result['rows']) == 5
        for row in result['rows']:
            assert row['depth_class'] == 'G'
            assert row['effective_dim'] == 1
            assert row['HH'] == {0: 1, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def test_virasoro_table(self):
        result = hh_family_table('virasoro', [1, 10, 13, 25, 26], max_deg=6)
        assert len(result['rows']) == 5
        for row in result['rows']:
            assert row['depth_class'] == 'M'
            assert row['effective_dim'] >= 3

    def test_sl2_table(self):
        result = hh_family_table('affine_sl2', [1, 2, 3, 4, 5, 6, 7, 8], max_deg=6)
        assert len(result['rows']) == 8
        for row in result['rows']:
            assert row['depth_class'] == 'L'
            assert row['effective_dim'] == 2
            # HH for d=2
            assert row['HH'][0] == 1
            assert row['HH'][1] == 2
            assert row['HH'][2] == 1
            assert row['HH'][3] == 0

    def test_betagamma_table(self):
        result = hh_family_table('betagamma', [0.5, 1.0, 1.5], max_deg=6)
        assert len(result['rows']) == 3
        for row in result['rows']:
            assert row['depth_class'] == 'C'
            assert row['effective_dim'] == 3

    def test_w3_table(self):
        result = hh_family_table('w3', [10, 13, 20], max_deg=6)
        assert len(result['rows']) == 3
        for row in result['rows']:
            assert row['depth_class'] == 'M'

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 3, 4, 5]:
            data = heisenberg_shadow_data(k)
            assert data.kappa == k

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2 (AP1, AP9)."""
        for c in [1, 10, 13, 25, 26]:
            data = virasoro_shadow_data(c)
            assert abs(data.kappa - c / 2.0) < 1e-10

    def test_kappa_sl2(self):
        """kappa(sl_2_k) = 3(k+2)/4 (AP1)."""
        for k in [1, 2, 3, 4]:
            data = affine_sl2_shadow_data(k)
            expected = 3.0 * (k + 2) / 4.0
            assert abs(data.kappa - expected) < 1e-10


# ============================================================================
# Test group 12: Kahler differentials
# ============================================================================

class TestKahler:
    def test_kahler_d1_basis(self):
        basis = kahler_differentials_basis(1, 0)
        assert basis == ['1']
        basis = kahler_differentials_basis(1, 1)
        assert len(basis) == 1
        assert 'dkappa' in basis[0]

    def test_kahler_d2_basis(self):
        basis = kahler_differentials_basis(2, 2)
        assert len(basis) == 1  # Just dkappa ^ dalpha

    def test_kahler_d3_basis(self):
        basis = kahler_differentials_basis(3, 2)
        assert len(basis) == 3  # C(3,2) = 3

    def test_kahler_count_matches_hh(self):
        """Kahler basis count = HH dimension (HKR verification)."""
        for d in range(1, 6):
            for n in range(d + 2):
                basis = kahler_differentials_basis(d, n)
                assert len(basis) == hh_dimension(d, n)

    def test_kahler_module_data(self):
        data = heisenberg_shadow_data(1)
        kd = kahler_module_data(data, 4)
        for n in range(5):
            assert kd[n]['dim_check']


# ============================================================================
# Test group 13: Negative cyclic and Dennis trace
# ============================================================================

class TestNegativeCyclic:
    def test_hn_d1(self):
        """HN_0 for d=1: C(1,0) + C(1,2) + ... = 1."""
        assert negative_cyclic_dimension(1, 0) == 1

    def test_hn_d2(self):
        """HN_0 for d=2: C(2,0) + C(2,2) = 1 + 1 = 2."""
        assert negative_cyclic_dimension(2, 0) == 2

    def test_hn_d3(self):
        """HN_0 for d=3: C(3,0) + C(3,2) = 1 + 3 = 4."""
        assert negative_cyclic_dimension(3, 0) == 4

    def test_dennis_trace(self):
        for d in range(1, 5):
            dt = dennis_trace_data(d)
            assert dt['K0'] == 'Z'
            assert dt['K_higher'] == 0
            assert dt['dennis_trace_image'] == 1


# ============================================================================
# Test group 14: Full 5-path verification
# ============================================================================

class TestFullVerification:
    def test_heisenberg_full(self):
        result = full_verification('heisenberg', 1.0)
        assert result['all_pass']

    def test_virasoro_full(self):
        result = full_verification('virasoro', 10.0)
        assert result['all_pass']

    def test_sl2_full(self):
        result = full_verification('affine_sl2', 3.0)
        assert result['all_pass']

    def test_betagamma_full(self):
        result = full_verification('betagamma', 1.0)
        assert result['all_pass']

    def test_w3_full(self):
        result = full_verification('w3', 10.0)
        assert result['all_pass']

    def test_virasoro_c13_full(self):
        """Self-dual point c=13."""
        result = full_verification('virasoro', 13.0)
        assert result['all_pass']

    def test_virasoro_c26_full(self):
        """Critical dimension c=26."""
        result = full_verification('virasoro', 26.0)
        assert result['all_pass']


# ============================================================================
# Test group 15: Master computation at zeros
# ============================================================================

class TestMasterAtZeros:
    def test_master_10_zeros(self):
        result = master_cyclic_homology_at_zeros(10, max_deg=4)
        assert result['n_zeros'] == 10
        assert len(result['results']) == 10
        assert result['analysis']['topological_invariance']

    def test_master_all_chi_equal(self):
        result = master_cyclic_homology_at_zeros(20, max_deg=6)
        assert result['analysis']['all_chi_HC_equal']

    def test_master_all_hh_equal(self):
        result = master_cyclic_homology_at_zeros(20, max_deg=6)
        assert result['analysis']['all_HH_equal']

    def test_master_chi_value(self):
        """chi_HC(trunc@6) = 4 universally."""
        result = master_cyclic_homology_at_zeros(10, max_deg=6)
        assert result['analysis']['chi_HC_value'] == 4


# ============================================================================
# Test group 16: Deformation data at zeros
# ============================================================================

class TestDeformationAtZeros:
    def test_deformation_first_zero(self):
        c_val = c_from_zeta_zero(1)
        data = deformation_hh_virasoro(c_val)
        assert abs(data['c'].real - 13.0) < 1e-10
        assert abs(data['kappa'] - c_val / 2.0) < 1e-10

    def test_deformation_kappa_nonzero(self):
        """kappa(c(rho_n)) is nonzero for all n (since c(rho_n) != 0)."""
        for n in range(1, 21):
            c_val = c_from_zeta_zero(n)
            data = deformation_hh_virasoro(c_val)
            assert abs(data['kappa']) > 1.0  # |c/2| >> 1

    def test_deformation_Q_contact_finite(self):
        """Q^contact is finite at c(rho_n) (c != 0 and 5c+22 != 0)."""
        for n in range(1, 21):
            c_val = c_from_zeta_zero(n)
            data = deformation_hh_virasoro(c_val)
            # Q_contact = 10 / (c * (5c + 22))
            # At c = 13 + 26i*gamma, both c and 5c+22 are nonzero
            assert abs(data['Q_contact']) > 0

    def test_deformation_discriminant_nonzero(self):
        """Critical discriminant Delta != 0 for class M at generic c."""
        for n in range(1, 21):
            c_val = c_from_zeta_zero(n)
            data = deformation_hh_virasoro(c_val)
            assert abs(data['discriminant']) > 0

    def test_deformation_batch(self):
        results = deformation_data_at_zeros(20)
        assert len(results) == 20
        for r in results:
            assert 'kappa' in r
            assert 'Q_contact' in r
            assert 'discriminant' in r


# ============================================================================
# Test group 17: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Verify consistency across families."""

    def test_depth_class_determines_d(self):
        """Depth class G -> d=1, L -> d=2, C -> d=3, M -> d>=3."""
        heis = heisenberg_shadow_data(1)
        assert heis.depth_class == 'G' and heis.effective_dim == 1

        sl2 = affine_sl2_shadow_data(1)
        assert sl2.depth_class == 'L' and sl2.effective_dim == 2

        bg = betagamma_shadow_data(1.0)
        assert bg.depth_class == 'C' and bg.effective_dim == 3

        vir = virasoro_shadow_data(10, max_arity=10)
        assert vir.depth_class == 'M' and vir.effective_dim >= 3

    def test_hh_monotone_in_d(self):
        """HH_1 increases with d (more generators = more differentials)."""
        for d in range(1, 8):
            assert hh_dimension(d, 1) == d

    def test_hp_universal(self):
        """HP is the same for all families: HP_0=1, HP_1=0."""
        for family, param in [('heisenberg', 1), ('virasoro', 10),
                              ('affine_sl2', 3), ('betagamma', 1.0)]:
            result = full_verification(family, param)
            hp = result['path_v_numerical']
            # HP_0 = 1 (the Chern character target)
            assert hp['fiber_dims'][0] == 1


# ============================================================================
# Test group 18: Edge cases
# ============================================================================

class TestEdgeCases:
    def test_hh_d0(self):
        """d=0: trivial algebra, HH_0 = 1, rest = 0."""
        dims = hh_dimensions_all(0, 6)
        assert dims[0] == 1
        for n in range(1, 7):
            assert dims[n] == 0

    def test_virasoro_c0(self):
        """Virasoro at c=0: kappa = 0 (uncurved). Still class M structurally."""
        data = virasoro_shadow_data(0.0, max_arity=5)
        # kappa = 0 at c=0, but the tower structure is still class M
        assert data.kappa == 0.0

    def test_large_d(self):
        """HH for large d: C(20, 10) = 184756."""
        assert hh_dimension(20, 10) == 184756

    def test_hh_symmetry(self):
        """HH_n = HH_{d-n} (Poincare duality for exterior algebra)."""
        for d in range(1, 10):
            for n in range(d + 1):
                assert hh_dimension(d, n) == hh_dimension(d, d - n)

    def test_hc_at_high_degree(self):
        """HC_n for large n: alternating 1/0 pattern continues."""
        for n in range(2, 100, 2):
            assert hc_dimension_module(5, n) == 1
        for n in range(1, 100, 2):
            assert hc_dimension_module(5, n) == 0


# ============================================================================
# Test group 19: Numerical consistency cross-checks
# ============================================================================

class TestNumericalConsistency:
    def test_hh_sum_equals_2d_numerical(self):
        """sum HH_n = 2^d, verified numerically for several families."""
        for family, param in [('heisenberg', 2), ('affine_sl2', 3),
                              ('betagamma', 1.0)]:
            result = full_verification(family, param)
            d = result['effective_dim']
            hh = result['path_i_HKR']
            total = sum(hh[n] for n in range(d + 1))
            assert total == 2 ** d

    def test_numerical_fiber_total(self):
        """Total fiber dimension = 2^d at evaluated points."""
        for d in range(1, 8):
            data = ShadowAlgebraData(
                family='test', param=1.0, kappa=1.0,
                depth_class='M' if d >= 3 else ('L' if d == 2 else 'G'),
                n_generators=d,
                higher_S={r: 0.1 for r in range(5, 5 + max(0, d - 3))},
            )
            num = numerical_hh_evaluated(data, max_deg=d + 2)
            assert num['total_fiber'] == 2 ** d
            assert num['euler_char'] == 0


# ============================================================================
# Test group 20: Multi-path agreement summary
# ============================================================================

class TestMultiPathAgreement:
    """Verify that all 5 paths agree for every family."""

    def test_all_families_all_paths(self):
        """The master cross-check: 5 paths agree for each family."""
        test_cases = [
            ('heisenberg', 1.0),
            ('heisenberg', 5.0),
            ('virasoro', 1.0),
            ('virasoro', 13.0),
            ('virasoro', 26.0),
            ('affine_sl2', 1.0),
            ('affine_sl2', 8.0),
            ('betagamma', 1.0),
            ('w3', 10.0),
        ]
        for family, param in test_cases:
            result = full_verification(family, param)
            assert result['all_pass'], \
                f"5-path verification failed for {family} at param={param}"

    def test_chi_hh_universally_zero(self):
        """chi_HH = 0 for ALL families at ALL parameters (d >= 1).

        Uses hh_euler_characteristic which sums over the full range 0..d,
        not truncated to max_deg.
        """
        test_cases = [
            ('heisenberg', 1.0),
            ('virasoro', 10.0),
            ('affine_sl2', 3.0),
            ('betagamma', 1.0),
            ('w3', 15.0),
        ]
        for family, param in test_cases:
            result = full_verification(family, param)
            d = result['effective_dim']
            assert hh_euler_characteristic(d) == 0, \
                f"chi_HH != 0 for {family} at param={param}"
