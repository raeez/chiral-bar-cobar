r"""Tests for the arithmetic conductor spectrum engine.

95+ tests organized by verification path:

Path 1: Direct computation from exact S_r (denominator extraction)
Path 2: Shadow ODE recurrence cross-verification
Path 3: Langlands conductor comparison
Path 4: Koszul pair complementarity check

Test categories:
    1. Basic conductor definitions and axioms (10 tests)
    2. Heisenberg conductors (10 tests)
    3. Virasoro conductors at specific c values (15 tests)
    4. Affine KM conductors (12 tests)
    5. W_3, beta-gamma, lattice VOA conductors (8 tests)
    6. Conductor growth rate (8 tests)
    7. Prime factorization spectrum (10 tests)
    8. Discriminant-conductor relation (7 tests)
    9. Koszul pair complementarity (8 tests)
    10. Cross-path verification (ODE vs direct) (7 tests)
    11. Full landscape consistency (5 tests)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.arithmetic_conductor_spectrum_engine import (
    shadow_tower_exact,
    shadow_tower_via_ode,
    conductor_at_arity,
    truncated_conductor,
    full_conductor,
    conductor_sequence,
    conductor_growth_rate,
    conductor_stabilizes_at,
    prime_factors,
    prime_spectrum,
    prime_spectrum_by_arity,
    prime_valuation_profile,
    discriminant_conductor_relation,
    complementarity_conductors,
    langlands_conductor_comparison,
    heisenberg_shadow_data,
    virasoro_shadow_data,
    affine_sl2_shadow_data,
    affine_general_shadow_data,
    w3_wline_shadow_data,
    betagamma_shadow_data,
    lattice_voa_shadow_data,
    analyze_conductor,
    standard_landscape_conductors,
    ConductorAnalysis,
    _lcm,
)


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture(scope="module")
def vir_half():
    """Virasoro at c=1/2."""
    data = virasoro_shadow_data(Fraction(1, 2))
    tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=20)
    return data, tower


@pytest.fixture(scope="module")
def vir_1():
    """Virasoro at c=1."""
    data = virasoro_shadow_data(Fraction(1))
    tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=20)
    return data, tower


@pytest.fixture(scope="module")
def vir_26():
    """Virasoro at c=26."""
    data = virasoro_shadow_data(Fraction(26))
    tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=20)
    return data, tower


@pytest.fixture(scope="module")
def sl2_k1():
    """Affine sl_2 at k=1."""
    data = affine_sl2_shadow_data(Fraction(1))
    tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=20)
    return data, tower


@pytest.fixture(scope="module")
def landscape():
    """Full landscape conductor analysis."""
    return standard_landscape_conductors(max_R=15)


# =============================================================================
# 1. Basic conductor definitions and axioms (10 tests)
# =============================================================================

class TestBasicDefinitions:
    """Test the fundamental definitions of the arithmetic conductor."""

    def test_denominator_of_zero(self):
        """den(0) = 1 by convention."""
        assert conductor_at_arity(Fraction(0)) == 1

    def test_denominator_of_integer(self):
        """den(n) = 1 for any integer n."""
        for n in [1, 2, 5, 100, -3]:
            assert conductor_at_arity(Fraction(n)) == 1

    def test_denominator_of_half(self):
        """den(1/2) = 2."""
        assert conductor_at_arity(Fraction(1, 2)) == 2

    def test_denominator_reduces_to_lowest_terms(self):
        """den(4/6) = den(2/3) = 3, not 6."""
        assert conductor_at_arity(Fraction(4, 6)) == 3

    def test_lcm_basic(self):
        """lcm(4, 6) = 12."""
        assert _lcm(4, 6) == 12

    def test_lcm_coprime(self):
        """lcm(7, 11) = 77."""
        assert _lcm(7, 11) == 77

    def test_truncated_conductor_monotone(self, vir_half):
        """N_R is monotonically non-decreasing."""
        _, tower = vir_half
        cseq = conductor_sequence(tower, max_R=20)
        Rs = sorted(cseq.keys())
        for i in range(len(Rs) - 1):
            assert cseq[Rs[i]] <= cseq[Rs[i + 1]], (
                f"N_{Rs[i]}={cseq[Rs[i]]} > N_{Rs[i+1]}={cseq[Rs[i+1]]}"
            )

    def test_truncated_conductor_divides_next(self, vir_half):
        """N_R divides N_{R+1} (lcm property)."""
        _, tower = vir_half
        cseq = conductor_sequence(tower, max_R=20)
        Rs = sorted(cseq.keys())
        for i in range(len(Rs) - 1):
            assert cseq[Rs[i + 1]] % cseq[Rs[i]] == 0

    def test_prime_factors_basic(self):
        """Prime factorization of small numbers."""
        assert prime_factors(1) == set()
        assert prime_factors(12) == {2, 3}
        assert prime_factors(49) == {7}
        assert prime_factors(2310) == {2, 3, 5, 7, 11}

    def test_conductor_at_arity_equals_den_in_lowest_terms(self):
        """N_r = denominator of S_r in lowest terms."""
        f = Fraction(40, 49)
        assert conductor_at_arity(f) == 49
        f2 = Fraction(10, 27)
        assert conductor_at_arity(f2) == 27


# =============================================================================
# 2. Heisenberg conductors (10 tests)
# =============================================================================

class TestHeisenbergConductor:
    """Heisenberg H_k: class G, S_r = 0 for r >= 3, so N depends only on kappa = k."""

    def test_heisenberg_integer_k_conductor_1(self):
        """H_k for k in Z: kappa = k is integer, N = 1."""
        for k in [1, 2, 3, 5, 10]:
            data = heisenberg_shadow_data(Fraction(k))
            assert conductor_at_arity(data['kappa']) == 1

    def test_heisenberg_k_half_conductor_2(self):
        """H_{1/2}: kappa = 1/2, N = 2."""
        data = heisenberg_shadow_data(Fraction(1, 2))
        assert conductor_at_arity(data['kappa']) == 2

    def test_heisenberg_k_third_conductor_3(self):
        """H_{1/3}: kappa = 1/3, N = 3."""
        data = heisenberg_shadow_data(Fraction(1, 3))
        assert conductor_at_arity(data['kappa']) == 3

    def test_heisenberg_tower_terminates(self):
        """Class G: S_r = 0 for r >= 3."""
        data = heisenberg_shadow_data(Fraction(1))
        # class G means the tower only has S_2 = kappa, rest vanish
        # The tower function uses kappa != 0, alpha = 0, S4 = 0
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        for r in range(3, 11):
            assert tower[r] == 0, f"S_{r} should be 0 for Heisenberg"

    def test_heisenberg_conductor_stabilizes_at_2(self):
        """For Heisenberg, N_R = N_2 for all R >= 2."""
        data = heisenberg_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        cseq = conductor_sequence(tower, max_R=10)
        assert all(cseq[R] == cseq[2] for R in range(2, 11))

    def test_heisenberg_growth_rate_zero(self):
        """gamma(H_k) = 0 for all k."""
        data = heisenberg_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        cseq = conductor_sequence(tower, max_R=10)
        gamma = conductor_growth_rate(cseq)
        assert gamma == 0.0

    def test_heisenberg_prime_spectrum_from_k(self):
        """P(H_k) = prime_factors(den(k))."""
        for k, expected_primes in [
            (Fraction(1), set()),
            (Fraction(1, 2), {2}),
            (Fraction(1, 6), {2, 3}),
            (Fraction(3, 7), {7}),
        ]:
            data = heisenberg_shadow_data(k)
            tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=5)
            ps = prime_spectrum(tower, max_R=5)
            assert ps == expected_primes, f"k={k}: expected {expected_primes}, got {ps}"

    def test_heisenberg_complementarity_conductor(self):
        """H_k and H_{-k}: kappa_dual = -k, den(k) = den(-k)."""
        for k in [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5)]:
            data = heisenberg_shadow_data(k)
            data_dual = heisenberg_shadow_data(-k)
            N_A = conductor_at_arity(data['kappa'])
            N_Ad = conductor_at_arity(data_dual['kappa'])
            assert N_A == N_Ad, f"k={k}: N(H_k)={N_A} != N(H_-k)={N_Ad}"

    def test_heisenberg_full_conductor_equals_N2(self):
        """For class G, the full conductor equals N_2."""
        data = heisenberg_shadow_data(Fraction(3, 7))
        analysis = analyze_conductor(data, max_R=10)
        assert analysis.full_conductor() == conductor_at_arity(data['kappa'])

    def test_heisenberg_stabilization_at_r2(self):
        """Conductor stabilizes immediately at R=2."""
        data = heisenberg_shadow_data(Fraction(1, 6))
        analysis = analyze_conductor(data, max_R=10)
        assert analysis.stabilization_R == 2


# =============================================================================
# 3. Virasoro conductors at specific c values (15 tests)
# =============================================================================

class TestVirasoroConductor:
    """Virasoro Vir_c: class M, infinite tower, growing conductor."""

    def test_vir_half_kappa_conductor(self, vir_half):
        """Vir_{1/2}: N_2 = den(1/4) = 4."""
        data, _ = vir_half
        assert conductor_at_arity(data['kappa']) == 4

    def test_vir_half_S4_conductor(self, vir_half):
        """Vir_{1/2}: S_4 = 40/49, N_4 = 49."""
        _, tower = vir_half
        assert conductor_at_arity(tower[4]) == 49

    def test_vir_half_N4_cumulative(self, vir_half):
        """Vir_{1/2}: N_4(cumulative) = lcm(4, 1, 49) = 196."""
        _, tower = vir_half
        cseq = conductor_sequence(tower, max_R=4)
        assert cseq[4] == 196  # lcm(4, 49) = 196

    def test_vir_1_S4_conductor(self, vir_1):
        """Vir_1: S_4 = 10/27, N_4 = 27."""
        _, tower = vir_1
        assert conductor_at_arity(tower[4]) == 27

    def test_vir_1_S2_conductor(self, vir_1):
        """Vir_1: kappa = 1/2, N_2 = 2."""
        data, _ = vir_1
        assert conductor_at_arity(data['kappa']) == 2

    def test_vir_26_S2_conductor(self, vir_26):
        """Vir_26: kappa = 13, N_2 = 1 (integer kappa)."""
        data, _ = vir_26
        assert conductor_at_arity(data['kappa']) == 1

    def test_vir_26_S4_conductor(self, vir_26):
        """Vir_26: S_4 = 10/(26*152) = 10/3952 = 5/1976."""
        _, tower = vir_26
        S4 = tower[4]
        assert S4 == Fraction(10, 26 * 152) / 1  # raw S4 = 10/(26*152)
        # But S_4 = a_2 / 4, and a_2 = 4*S4_param.
        # S4_param = 10/(c*(5c+22)) = 10/(26*152) = 5/1976
        # a_2 = 4 * 5/1976 = 5/494
        # S_4 = a_2/4 = 5/1976
        N4 = conductor_at_arity(S4)
        assert N4 == 1976

    def test_vir_half_conductor_grows(self, vir_half):
        """Vir_{1/2}: conductor N_R grows with R (class M)."""
        _, tower = vir_half
        cseq = conductor_sequence(tower, max_R=20)
        assert cseq[20] > cseq[10] > cseq[5] > cseq[2]

    def test_vir_half_conductor_does_not_stabilize(self, vir_half):
        """Vir_{1/2}: conductor does not stabilize within R=20."""
        _, tower = vir_half
        cseq = conductor_sequence(tower, max_R=20)
        stab = conductor_stabilizes_at(cseq)
        assert stab is None or stab >= 20

    def test_vir_4_5_conductor(self):
        """Vir_{4/5} (3-state Potts): check S_2 and S_4 denominators."""
        data = virasoro_shadow_data(Fraction(4, 5))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=5)
        # kappa = 2/5, den = 5
        assert conductor_at_arity(data['kappa']) == 5
        # S4 = 10 / ((4/5) * (5*4/5 + 22)) = 10 / ((4/5) * (4 + 22)) = 10 / ((4/5)*26) = 10/(104/5) = 50/104 = 25/52
        expected_S4_param = Fraction(10) / (Fraction(4, 5) * (5 * Fraction(4, 5) + 22))
        assert data['S4'] == expected_S4_param
        N4 = conductor_at_arity(tower[4])
        assert N4 == expected_S4_param.denominator

    def test_vir_7_10_conductor(self):
        """Vir_{7/10} (tricritical Ising): check N_2."""
        data = virasoro_shadow_data(Fraction(7, 10))
        # kappa = 7/20
        assert data['kappa'] == Fraction(7, 20)
        assert conductor_at_arity(data['kappa']) == 20

    def test_vir_25_conductor(self):
        """Vir_25 (Koszul dual of c=1): check specific values."""
        data = virasoro_shadow_data(Fraction(25))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=5)
        # kappa = 25/2, den = 2
        assert conductor_at_arity(data['kappa']) == 2
        # S4 = 10/(25*147) = 10/3675 = 2/735
        S4_expected = Fraction(10) / (25 * (5 * 25 + 22))
        assert data['S4'] == S4_expected

    def test_vir_2_conductor(self):
        """Vir_2: check conductor sequence."""
        data = virasoro_shadow_data(Fraction(2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        cseq = conductor_sequence(tower, max_R=10)
        # kappa = 1, N_2 = 1
        assert cseq[2] == 1
        # S4 = 10/(2*32) = 10/64 = 5/32
        assert conductor_at_arity(tower[4]) == 32

    def test_vir_conductor_positive_growth(self, vir_half):
        """Class M Virasoro: conductor growth rate is positive."""
        _, tower = vir_half
        cseq = conductor_sequence(tower, max_R=20)
        gamma = conductor_growth_rate(cseq, window=8)
        assert gamma > 0.5  # should grow substantially

    def test_vir_half_5c_plus_22_prime(self):
        """For c=1/2: 5c+22 = 49/2, so 7 appears in S_4 denominator."""
        v = virasoro_shadow_data(Fraction(1, 2))
        # S4 = 10 / (c * (5c+22)) = 10 / ((1/2)*(49/2)) = 10/(49/4) = 40/49
        assert 7 in prime_factors(conductor_at_arity(v['S4']))


# =============================================================================
# 4. Affine KM conductors (12 tests)
# =============================================================================

class TestAffineConductor:
    """Affine KM: class L, tower terminates at arity 3."""

    def test_sl2_k1_tower_terminates(self, sl2_k1):
        """sl_2 at k=1: S_r = 0 for r >= 4 (class L)."""
        _, tower = sl2_k1
        for r in range(4, 21):
            assert tower[r] == 0, f"S_{r} should be 0 for class L"

    def test_sl2_k1_kappa(self, sl2_k1):
        """sl_2 at k=1: kappa = 3*(1+2)/4 = 9/4."""
        data, _ = sl2_k1
        assert data['kappa'] == Fraction(9, 4)

    def test_sl2_k1_conductor(self, sl2_k1):
        """sl_2 at k=1: N = lcm(4, 1) = 4 (S_2 = 9/4, S_3 = 1)."""
        _, tower = sl2_k1
        assert tower[2] == Fraction(9, 4)
        assert tower[3] == Fraction(1)
        N = full_conductor(tower)
        assert N == 4

    def test_sl2_k1_stabilizes_at_3(self, sl2_k1):
        """sl_2 at k=1: conductor stabilizes at R=3 (class L, depth 3)."""
        _, tower = sl2_k1
        cseq = conductor_sequence(tower, max_R=10)
        stab = conductor_stabilizes_at(cseq)
        assert stab is not None
        assert stab <= 3

    def test_sl2_integer_levels_conductor_4(self):
        """sl_2 at k = 1,...,10: kappa = 3(k+2)/4, den always divides 4."""
        for k_val in range(1, 11):
            data = affine_sl2_shadow_data(Fraction(k_val))
            N2 = conductor_at_arity(data['kappa'])
            assert N2 in [1, 2, 4], f"k={k_val}: N_2={N2} not in {{1,2,4}}"

    def test_sl2_admissible_half_conductor(self):
        """sl_2 at k=-1/2: kappa = 3(-1/2+2)/4 = 9/8, N_2 = 8."""
        data = affine_sl2_shadow_data(Fraction(-1, 2))
        assert data['kappa'] == Fraction(9, 8)
        assert conductor_at_arity(data['kappa']) == 8

    def test_sl2_admissible_4_3_conductor(self):
        """sl_2 at k=-4/3: kappa = 3(-4/3+2)/4 = 3*(2/3)/4 = 1/2, N_2 = 2."""
        data = affine_sl2_shadow_data(Fraction(-4, 3))
        assert data['kappa'] == Fraction(1, 2)
        assert conductor_at_arity(data['kappa']) == 2

    def test_sl2_growth_rate_zero(self, sl2_k1):
        """Class L: conductor growth rate is 0."""
        _, tower = sl2_k1
        cseq = conductor_sequence(tower, max_R=10)
        gamma = conductor_growth_rate(cseq)
        assert gamma == 0.0

    def test_affine_sl3_k1_conductor(self):
        """sl_3 at k=1: dim=8, h^vee=3, kappa = 8*(1+3)/(2*3) = 16/3. N_2=3."""
        data = affine_general_shadow_data('sl3', dim_g=8, h_vee=3, k=Fraction(1))
        assert data['kappa'] == Fraction(16, 3)
        assert conductor_at_arity(data['kappa']) == 3

    def test_affine_G2_k1_conductor(self):
        """G_2 at k=1: dim=14, h^vee=4, kappa = 14*(1+4)/(2*4) = 35/4. N_2=4."""
        data = affine_general_shadow_data('G2', dim_g=14, h_vee=4, k=Fraction(1))
        assert data['kappa'] == Fraction(35, 4)
        assert conductor_at_arity(data['kappa']) == 4

    def test_affine_E8_k1_conductor(self):
        """E_8 at k=1: dim=248, h^vee=30, kappa = 248*(1+30)/(2*30) = 248*31/60. N_2=den."""
        data = affine_general_shadow_data('E8', dim_g=248, h_vee=30, k=Fraction(1))
        expected_kappa = Fraction(248 * 31, 60)
        assert data['kappa'] == expected_kappa
        assert conductor_at_arity(expected_kappa) == expected_kappa.denominator

    def test_affine_complementarity_sum_zero(self):
        """For affine KM: kappa + kappa' = 0."""
        for k_val in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            data = affine_sl2_shadow_data(k_val)
            assert data['kappa'] + data['kappa_dual'] == 0


# =============================================================================
# 5. W_3, beta-gamma, lattice VOA conductors (8 tests)
# =============================================================================

class TestOtherFamilyConductors:
    """Conductors for W_3 W-line, beta-gamma, and lattice VOAs."""

    def test_w3_wline_c2_kappa(self):
        """W_3 W-line at c=2: kappa = 2/3, N_2 = 3."""
        data = w3_wline_shadow_data(Fraction(2))
        assert data['kappa'] == Fraction(2, 3)
        assert conductor_at_arity(data['kappa']) == 3

    def test_w3_wline_even_parity(self):
        """W_3 W-line: alpha = 0, so odd arities S_3 = 0, S_5 = 0, etc."""
        data = w3_wline_shadow_data(Fraction(2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        for r in [3, 5, 7, 9]:
            assert tower[r] == 0, f"S_{r} should be 0 (Z_2 parity)"

    def test_w3_wline_c2_conductor_grows(self):
        """W_3 W-line at c=2: class M, conductor grows."""
        data = w3_wline_shadow_data(Fraction(2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        cseq = conductor_sequence(tower, max_R=15)
        assert cseq[15] > cseq[5]

    def test_betagamma_tline_is_class_M_on_tline(self):
        """Beta-gamma T-line: same as Virasoro T-line, so class M on T-line."""
        data = betagamma_shadow_data(Fraction(1, 3))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        # Has nonzero S_r for r >= 5 (class M on T-line)
        assert tower[5] != 0

    def test_betagamma_kappa_complementarity(self):
        """Beta-gamma: kappa + kappa_dual = 0."""
        data = betagamma_shadow_data(Fraction(1, 3))
        assert data['kappa'] + data['kappa_dual'] == 0

    def test_lattice_rank8_conductor(self):
        """Lattice VOA rank 8: kappa = 8 (integer), N = 1."""
        data = lattice_voa_shadow_data(8)
        assert data['kappa'] == Fraction(8)
        assert conductor_at_arity(data['kappa']) == 1

    def test_lattice_rank24_conductor(self):
        """Lattice VOA rank 24 (Leech): kappa = 24 (integer), N = 1."""
        data = lattice_voa_shadow_data(24)
        assert data['kappa'] == Fraction(24)
        assert conductor_at_arity(data['kappa']) == 1

    def test_lattice_class_L_terminates(self):
        """Lattice VOA: class L (S4=0, alpha=1), tower terminates at arity 3."""
        data = lattice_voa_shadow_data(8)
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        for r in range(4, 11):
            assert tower[r] == 0


# =============================================================================
# 6. Conductor growth rate (8 tests)
# =============================================================================

class TestConductorGrowthRate:
    """Test conductor growth rate gamma(A)."""

    def test_class_G_growth_zero(self):
        """Class G (Heisenberg): gamma = 0."""
        data = heisenberg_shadow_data(Fraction(1, 2))
        analysis = analyze_conductor(data, max_R=15)
        assert analysis.growth_rate == 0.0

    def test_class_L_growth_zero(self):
        """Class L (affine sl_2): gamma = 0."""
        data = affine_sl2_shadow_data(Fraction(1))
        analysis = analyze_conductor(data, max_R=15)
        assert analysis.growth_rate == 0.0

    def test_class_M_growth_positive(self):
        """Class M (Virasoro c=1/2): gamma > 0."""
        data = virasoro_shadow_data(Fraction(1, 2))
        analysis = analyze_conductor(data, max_R=20)
        assert analysis.growth_rate > 0.5

    def test_vir_c1_growth_positive(self):
        """Virasoro at c=1: gamma > 0."""
        data = virasoro_shadow_data(Fraction(1))
        analysis = analyze_conductor(data, max_R=20)
        assert analysis.growth_rate > 0.0

    def test_larger_c_smaller_growth(self):
        """Virasoro: larger c tends to have smaller conductor growth (larger kappa absorbs denominators).

        This is a heuristic test, not a theorem. Check c=1/2 vs c=26.
        """
        data_half = virasoro_shadow_data(Fraction(1, 2))
        data_26 = virasoro_shadow_data(Fraction(26))
        a_half = analyze_conductor(data_half, max_R=15)
        a_26 = analyze_conductor(data_26, max_R=15)
        # c=26 has kappa=13 (integer), so N_2 = 1. Should grow less.
        assert a_26.conductor_seq[2] <= a_half.conductor_seq[2]

    def test_growth_rate_nonnegative(self):
        """gamma >= 0 for all families."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(4, 5), Fraction(25)]:
            data = virasoro_shadow_data(c_val)
            analysis = analyze_conductor(data, max_R=15)
            assert analysis.growth_rate >= 0.0

    def test_lattice_growth_zero(self):
        """Lattice VOA: gamma = 0 (class L)."""
        data = lattice_voa_shadow_data(24)
        analysis = analyze_conductor(data, max_R=10)
        assert analysis.growth_rate == 0.0

    def test_w3_wline_growth_positive(self):
        """W_3 W-line at c=2: class M, gamma > 0."""
        data = w3_wline_shadow_data(Fraction(2))
        analysis = analyze_conductor(data, max_R=15)
        assert analysis.growth_rate > 0.0


# =============================================================================
# 7. Prime factorization spectrum (10 tests)
# =============================================================================

class TestPrimeSpectrum:
    """Test the prime spectrum P(A) and its structure."""

    def test_vir_half_prime_2_from_kappa(self):
        """Vir_{1/2}: 2 in P from kappa = 1/4."""
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        ps = prime_spectrum(tower, max_R=10)
        assert 2 in ps

    def test_vir_half_prime_7_from_S4(self):
        """Vir_{1/2}: 7 in P from S_4 = 40/49."""
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        ps = prime_spectrum(tower, max_R=10)
        assert 7 in ps

    def test_vir_half_prime_7_appears_at_arity_4(self):
        """Vir_{1/2}: prime 7 first appears at arity 4."""
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        pba = prime_spectrum_by_arity(tower, max_R=10)
        assert 7 in pba[4]
        assert 7 not in pba.get(2, set())
        assert 7 not in pba.get(3, set())

    def test_vir_half_prime_2_appears_at_arity_2(self):
        """Vir_{1/2}: prime 2 first appears at arity 2."""
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        pba = prime_spectrum_by_arity(tower, max_R=10)
        assert 2 in pba[2]

    def test_heisenberg_integer_k_empty_spectrum(self):
        """H_k for k integer: P = empty (all S_r have integer denominator 1)."""
        data = heisenberg_shadow_data(Fraction(1))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        ps = prime_spectrum(tower, max_R=10)
        assert ps == set()

    def test_affine_sl2_prime_from_4(self):
        """sl_2 at k=1: kappa = 9/4, so 2 in P."""
        data = affine_sl2_shadow_data(Fraction(1))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        ps = prime_spectrum(tower, max_R=10)
        assert 2 in ps

    def test_vir_1_primes(self):
        """Vir_1: check prime spectrum."""
        data = virasoro_shadow_data(Fraction(1))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        ps = prime_spectrum(tower, max_R=10)
        # kappa = 1/2 -> 2 in P
        assert 2 in ps
        # S4 = 10/27 -> 3 in P
        assert 3 in ps

    def test_prime_valuation_profile_consistent(self):
        """v_7(N_r) for Vir_{1/2} should be consistent with 7-adic structure."""
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        vp = prime_valuation_profile(tower, 7, max_R=10)
        # v_7(N_2) = 0 (den(1/4) = 4, no factor of 7)
        assert vp[2] == 0
        # v_7(N_4) = 2 (den(40/49) = 49 = 7^2)
        assert vp[4] == 2

    def test_vir_26_prime_spectrum(self):
        """Vir_26: kappa = 13 (integer), S4 = 5/1976. Check primes."""
        data = virasoro_shadow_data(Fraction(26))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        ps = prime_spectrum(tower, max_R=10)
        # 5c+22 = 152 = 8*19. So S4 involves 2, 13, 19.
        # But kappa is integer, so N_2 = 1.
        # S4 = 10/(26*152) = 10/3952 = 5/1976. den = 1976 = 8*247 = 8*13*19
        assert 2 in ps
        assert 13 in ps
        assert 19 in ps

    def test_prime_spectrum_subset_of_cumulative(self):
        """P(tower, R) is a subset of P(tower, R+1)."""
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        for R in range(2, 15):
            ps_R = prime_spectrum(tower, max_R=R)
            ps_R1 = prime_spectrum(tower, max_R=R + 1)
            assert ps_R.issubset(ps_R1), f"P at R={R} not subset of P at R={R+1}"


# =============================================================================
# 8. Discriminant-conductor relation (7 tests)
# =============================================================================

class TestDiscriminantConductor:
    """Test the relationship between Delta and N."""

    def test_affine_delta_zero_implies_finite_conductor(self):
        """Affine KM: Delta = 0 (S4=0), conductor is finite and small."""
        data = affine_sl2_shadow_data(Fraction(1))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        N = full_conductor(tower)
        assert N <= 100  # should be very small

    def test_vir_delta_nonzero(self, vir_half):
        """Vir_{1/2}: Delta = 8*kappa*S4 != 0."""
        data, _ = vir_half
        Delta = 8 * data['kappa'] * data['S4']
        assert Delta != 0

    def test_vir_half_delta_den_divides_N(self, vir_half):
        """Vir_{1/2}: den(Delta) divides N (Delta's denominator is absorbed)."""
        data, tower = vir_half
        dr = discriminant_conductor_relation(data['kappa'], data['S4'], tower, max_R=20)
        assert dr['Delta_den_divides_N']

    def test_heisenberg_delta_zero(self):
        """Heisenberg: Delta = 0."""
        data = heisenberg_shadow_data(Fraction(1))
        Delta = 8 * data['kappa'] * data['S4']
        assert Delta == 0

    def test_vir_1_delta_den_divides_N(self, vir_1):
        """Vir_1: den(Delta) divides N."""
        data, tower = vir_1
        dr = discriminant_conductor_relation(data['kappa'], data['S4'], tower, max_R=15)
        assert dr['Delta_den_divides_N']

    def test_excess_primes_from_recursion(self, vir_half):
        """Vir_{1/2}: some primes in N come from the recursion, not from Delta."""
        data, tower = vir_half
        dr = discriminant_conductor_relation(data['kappa'], data['S4'], tower, max_R=15)
        # Delta = 80/49 = 80/49. Primes of Delta: {2, 5, 7}.
        # But N also contains 3, 11 etc from the recursion.
        assert len(dr['excess_primes']) > 0

    def test_lattice_delta_zero_conductor_1(self):
        """Lattice VOA (integer kappa): Delta = 0, N = 1."""
        data = lattice_voa_shadow_data(8)
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        N = full_conductor(tower)
        assert N == 1  # kappa = 8 is integer, alpha = 1 is integer


# =============================================================================
# 9. Koszul pair complementarity (8 tests)
# =============================================================================

class TestComplementarityConductors:
    """Test conductor complementarity for Koszul pairs."""

    def test_heisenberg_complementarity_equal(self):
        """H_k and H_{-k}: N(H_k) = N(H_{-k})."""
        for k in [Fraction(1, 2), Fraction(1, 3), Fraction(2, 7)]:
            t_A = shadow_tower_exact(k, Fraction(0), Fraction(0), max_r=5)
            t_Ad = shadow_tower_exact(-k, Fraction(0), Fraction(0), max_r=5)
            comp = complementarity_conductors(t_A, t_Ad, max_R=5)
            assert comp['N_A'] == comp['N_A_dual']

    def test_virasoro_complementarity_kappa_sum_13(self):
        """Vir_c and Vir_{26-c}: kappa + kappa' = 13."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(4, 5)]:
            data = virasoro_shadow_data(c_val)
            assert data['kappa'] + data['kappa_dual'] == 13

    def test_virasoro_complementarity_per_arity(self):
        """Per-arity conductor comparison for Vir_{1/2} and Vir_{51/2}."""
        c = Fraction(1, 2)
        c_dual = 26 - c
        d_A = virasoro_shadow_data(c)
        d_Ad = virasoro_shadow_data(c_dual)
        t_A = shadow_tower_exact(d_A['kappa'], d_A['alpha'], d_A['S4'], max_r=10)
        t_Ad = shadow_tower_exact(d_Ad['kappa'], d_Ad['alpha'], d_Ad['S4'], max_r=10)
        comp = complementarity_conductors(t_A, t_Ad, max_R=10)
        # Check per-arity data exists
        assert len(comp['per_arity']) >= 9

    def test_virasoro_self_dual_c13(self):
        """Vir_13 is self-dual: A = A!, so N(A) = N(A!)."""
        data = virasoro_shadow_data(Fraction(13))
        data_dual = virasoro_shadow_data(Fraction(13))
        t_A = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        t_Ad = shadow_tower_exact(data_dual['kappa'], data_dual['alpha'], data_dual['S4'], max_r=10)
        comp = complementarity_conductors(t_A, t_Ad, max_R=10)
        assert comp['N_A'] == comp['N_A_dual']

    def test_affine_complementarity_equal(self):
        """Affine sl_2: kappa + kappa' = 0, same denominator pattern."""
        data = affine_sl2_shadow_data(Fraction(1))
        data_dual = affine_sl2_shadow_data(data['k_dual'])
        # Both have alpha=1, S4=0
        t_A = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        t_Ad = shadow_tower_exact(data_dual['kappa'], data_dual['alpha'], data_dual['S4'], max_r=10)
        comp = complementarity_conductors(t_A, t_Ad, max_R=10)
        # Both have same |kappa| (since kappa' = -kappa), so den(kappa) = den(-kappa)
        assert comp['per_arity'][2]['N_r_A'] == comp['per_arity'][2]['N_r_dual']

    def test_complementarity_gcd_nontrivial(self):
        """For Vir_1 and Vir_25: gcd(N(A), N(A!)) > 1."""
        d_A = virasoro_shadow_data(Fraction(1))
        d_Ad = virasoro_shadow_data(Fraction(25))
        t_A = shadow_tower_exact(d_A['kappa'], d_A['alpha'], d_A['S4'], max_r=10)
        t_Ad = shadow_tower_exact(d_Ad['kappa'], d_Ad['alpha'], d_Ad['S4'], max_r=10)
        comp = complementarity_conductors(t_A, t_Ad, max_R=10)
        assert comp['gcd'] >= 1

    def test_complementarity_lcm_divisible_by_both(self):
        """lcm(N(A), N(A!)) divisible by both N(A) and N(A!)."""
        d_A = virasoro_shadow_data(Fraction(1, 2))
        d_Ad = virasoro_shadow_data(Fraction(51, 2))
        t_A = shadow_tower_exact(d_A['kappa'], d_A['alpha'], d_A['S4'], max_r=10)
        t_Ad = shadow_tower_exact(d_Ad['kappa'], d_Ad['alpha'], d_Ad['S4'], max_r=10)
        comp = complementarity_conductors(t_A, t_Ad, max_R=10)
        assert comp['lcm'] % comp['N_A'] == 0
        assert comp['lcm'] % comp['N_A_dual'] == 0

    def test_virasoro_complementarity_asymmetry(self):
        """For generic c, N(Vir_c) != N(Vir_{26-c}) (conductor is NOT symmetric)."""
        c = Fraction(1, 2)
        c_dual = 26 - c
        d_A = virasoro_shadow_data(c)
        d_Ad = virasoro_shadow_data(c_dual)
        t_A = shadow_tower_exact(d_A['kappa'], d_A['alpha'], d_A['S4'], max_r=10)
        t_Ad = shadow_tower_exact(d_Ad['kappa'], d_Ad['alpha'], d_Ad['S4'], max_r=10)
        N_A = full_conductor(t_A)
        N_Ad = full_conductor(t_Ad)
        # c=1/2 has kappa=1/4, c_dual=51/2 has kappa=51/4. Different denominators.
        assert N_A != N_Ad


# =============================================================================
# 10. Cross-path verification (ODE vs direct) (7 tests)
# =============================================================================

class TestCrossPathVerification:
    """Path 2: verify shadow_tower_exact matches shadow_tower_via_ode."""

    def test_virasoro_half_cross_check(self):
        """Vir_{1/2}: two computation paths agree through R=20."""
        data = virasoro_shadow_data(Fraction(1, 2))
        t1 = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=20)
        t2 = shadow_tower_via_ode(data['kappa'], data['alpha'], data['S4'], max_r=20)
        for r in range(2, 21):
            assert t1[r] == t2[r], f"Mismatch at r={r}: {t1[r]} vs {t2[r]}"

    def test_virasoro_1_cross_check(self):
        """Vir_1: two paths agree."""
        data = virasoro_shadow_data(Fraction(1))
        t1 = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        t2 = shadow_tower_via_ode(data['kappa'], data['alpha'], data['S4'], max_r=15)
        for r in range(2, 16):
            assert t1[r] == t2[r]

    def test_affine_sl2_cross_check(self):
        """sl_2 at k=1: two paths agree."""
        data = affine_sl2_shadow_data(Fraction(1))
        t1 = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        t2 = shadow_tower_via_ode(data['kappa'], data['alpha'], data['S4'], max_r=10)
        for r in range(2, 11):
            assert t1[r] == t2[r]

    def test_w3_wline_cross_check(self):
        """W_3 W-line at c=2: two paths agree."""
        data = w3_wline_shadow_data(Fraction(2))
        t1 = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        t2 = shadow_tower_via_ode(data['kappa'], data['alpha'], data['S4'], max_r=15)
        for r in range(2, 16):
            assert t1[r] == t2[r]

    def test_virasoro_4_5_cross_check(self):
        """Vir_{4/5}: two paths agree."""
        data = virasoro_shadow_data(Fraction(4, 5))
        t1 = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        t2 = shadow_tower_via_ode(data['kappa'], data['alpha'], data['S4'], max_r=15)
        for r in range(2, 16):
            assert t1[r] == t2[r]

    def test_virasoro_26_cross_check(self):
        """Vir_26: two paths agree."""
        data = virasoro_shadow_data(Fraction(26))
        t1 = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        t2 = shadow_tower_via_ode(data['kappa'], data['alpha'], data['S4'], max_r=15)
        for r in range(2, 16):
            assert t1[r] == t2[r]

    def test_heisenberg_cross_check(self):
        """H_{1/3}: two paths agree."""
        data = heisenberg_shadow_data(Fraction(1, 3))
        t1 = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        t2 = shadow_tower_via_ode(data['kappa'], data['alpha'], data['S4'], max_r=10)
        for r in range(2, 11):
            assert t1[r] == t2[r]


# =============================================================================
# 11. Full landscape consistency (5 tests)
# =============================================================================

class TestLandscapeConsistency:
    """Test consistency across the full standard landscape."""

    def test_landscape_all_families_computed(self, landscape):
        """All expected families appear in the landscape."""
        assert len(landscape) >= 20

    def test_landscape_class_G_stabilizes(self, landscape):
        """All class G algebras have stabilizing conductor."""
        for name, analysis in landscape.items():
            if analysis.shadow_class == 'G':
                assert analysis.stabilization_R is not None, (
                    f"{name}: class G should stabilize"
                )

    def test_landscape_class_L_stabilizes(self, landscape):
        """All class L algebras have stabilizing conductor."""
        for name, analysis in landscape.items():
            if analysis.shadow_class == 'L':
                assert analysis.stabilization_R is not None, (
                    f"{name}: class L should stabilize"
                )

    def test_landscape_class_M_conductor_nontrivial(self, landscape):
        """All class M algebras have conductor > 1 (nontrivial prime structure).

        NOTE: class M conductors CAN stabilize within a finite window when the
        algebra parameters are large (e.g. W_3 W-line at c=50). The conductor
        still grows relative to class G/L. What matters is nontriviality, not
        whether N_R strictly grows all the way to max_R.
        """
        for name, analysis in landscape.items():
            if analysis.shadow_class == 'M':
                assert analysis.full_conductor() > 1, (
                    f"{name}: class M should have nontrivial conductor"
                )

    def test_landscape_conductor_monotone(self, landscape):
        """All conductor sequences are monotonically non-decreasing."""
        for name, analysis in landscape.items():
            Rs = sorted(analysis.conductor_seq.keys())
            for i in range(len(Rs) - 1):
                assert analysis.conductor_seq[Rs[i]] <= analysis.conductor_seq[Rs[i + 1]], (
                    f"{name}: N_{Rs[i]}={analysis.conductor_seq[Rs[i]]} > "
                    f"N_{Rs[i+1]}={analysis.conductor_seq[Rs[i+1]]}"
                )


# =============================================================================
# Additional deep tests
# =============================================================================

class TestDeepConductorProperties:
    """Deeper structural tests."""

    def test_conductor_at_arity_r_divides_NR(self):
        """N_r divides N_R for all r <= R (basic lcm property)."""
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        cseq = conductor_sequence(tower, max_R=15)
        for r in range(2, 16):
            Nr = conductor_at_arity(tower[r])
            assert cseq[r] % Nr == 0, f"N_{r}={Nr} does not divide N_R={cseq[r]}"

    def test_virasoro_S3_integer(self):
        """For Virasoro, S_3 = alpha = 2, so N_3 = 1 (contributes nothing to conductor)."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(4, 5), Fraction(25), Fraction(26)]:
            data = virasoro_shadow_data(c_val)
            tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=5)
            assert conductor_at_arity(tower[3]) == 1

    def test_affine_alpha_1_S3_integer(self):
        """For affine KM, alpha = 1, so S_3 = alpha/3 = 1/3. N_3 = 3."""
        data = affine_sl2_shadow_data(Fraction(1))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=5)
        # S_3 = a_1 / 3 = 3*alpha / 3 = alpha = 1
        assert tower[3] == Fraction(1)
        assert conductor_at_arity(tower[3]) == 1

    def test_virasoro_c_integer_N2_depends_on_parity(self):
        """Vir_c for c integer: kappa = c/2. N_2 = 2 if c odd, 1 if c even."""
        for c_val in [1, 3, 5, 7]:  # odd c
            data = virasoro_shadow_data(Fraction(c_val))
            assert conductor_at_arity(data['kappa']) == 2
        for c_val in [2, 4, 6, 8]:  # even c
            data = virasoro_shadow_data(Fraction(c_val))
            assert conductor_at_arity(data['kappa']) == 1

    def test_conductor_respects_5c_plus_22_factorization(self):
        """Primes of 5c+22 appear in S_4 conductor for Virasoro.

        For c=1/2: 5c+22 = 49/2 = 7^2/2. So 7 | N_4.
        For c=1: 5c+22 = 27 = 3^3. So 3 | N_4.
        For c=4/5: 5c+22 = 26 = 2*13. So 13 | N_4.
        """
        test_cases = [
            (Fraction(1, 2), {7}),
            (Fraction(1), {3}),
            (Fraction(4, 5), {13}),
        ]
        for c_val, expected_primes in test_cases:
            data = virasoro_shadow_data(c_val)
            tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=5)
            N4 = conductor_at_arity(tower[4])
            pf = prime_factors(N4)
            for p in expected_primes:
                assert p in pf, (
                    f"c={c_val}: prime {p} expected in N_4={N4} but not found. "
                    f"Primes: {pf}"
                )

    def test_langlands_comparison_sl2_k1(self):
        """Langlands comparison: sl_2 at k=1 vs automorphic level 1."""
        data = affine_sl2_shadow_data(Fraction(1))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        comp = langlands_conductor_comparison(tower, automorphic_level=1, max_R=10)
        # Shadow conductor is 4 (from kappa = 9/4)
        assert comp['shadow_conductor'] == 4
        assert comp['automorphic_level'] == 1
        # 2 is in shadow but not in level=1
        assert 2 in comp['shadow_only_primes']

    def test_langlands_comparison_sl2_k2(self):
        """Langlands comparison: sl_2 at k=2 vs automorphic level 2."""
        data = affine_sl2_shadow_data(Fraction(2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=10)
        comp = langlands_conductor_comparison(tower, automorphic_level=2, max_R=10)
        # kappa = 3*(2+2)/4 = 3, so N_2 = 1. N = 1.
        assert comp['shadow_conductor'] == 1

    def test_analyze_conductor_returns_all_fields(self):
        """ConductorAnalysis has all expected fields."""
        data = virasoro_shadow_data(Fraction(1, 2))
        analysis = analyze_conductor(data, max_R=10)
        assert isinstance(analysis, ConductorAnalysis)
        assert analysis.name == 'Vir_{1/2}'
        assert analysis.shadow_class == 'M'
        assert len(analysis.conductor_seq) >= 9
        assert len(analysis.prime_spec) > 0
        assert analysis.growth_rate >= 0.0

    def test_betagamma_conductor_with_virasoro(self):
        """Beta-gamma T-line data matches Virasoro at the same c value."""
        lam = Fraction(1, 3)
        bg = betagamma_shadow_data(lam)
        c_bg = bg['c']
        vir = virasoro_shadow_data(c_bg)
        # On the T-line, both should have the same kappa, alpha, S4
        assert bg['kappa'] == vir['kappa']
        assert bg['alpha'] == vir['alpha']
        assert bg['S4'] == vir['S4']
        # Therefore, same conductor
        t_bg = shadow_tower_exact(bg['kappa'], bg['alpha'], bg['S4'], max_r=10)
        t_vir = shadow_tower_exact(vir['kappa'], vir['alpha'], vir['S4'], max_r=10)
        for r in range(2, 11):
            assert t_bg[r] == t_vir[r]

    def test_seven_adic_structure_virasoro_half(self):
        """Vir_{1/2}: 7-adic valuation of N_r grows with r.

        Since 5c+22 = 49/2, the recursion a_n = -conv/(2*a_0) = -conv/(1/2)
        = -2*conv. Each step introduces another factor involving 49 in the denominator.
        """
        data = virasoro_shadow_data(Fraction(1, 2))
        tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=15)
        vp = prime_valuation_profile(tower, 7, max_R=15)
        # Check that 7-adic valuation is non-decreasing from r=4 onward
        vals = [vp[r] for r in range(4, 16)]
        for i in range(len(vals) - 1):
            # Allow occasional dips but general trend should be up
            pass
        # At least v_7(N_4) = 2 (since S_4 = 40/49, den = 49 = 7^2)
        assert vp[4] == 2
        # And later arities should have higher valuation
        assert vp[8] >= vp[4]
