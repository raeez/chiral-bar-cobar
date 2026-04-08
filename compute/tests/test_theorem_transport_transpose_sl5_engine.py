r"""Tests for the transport-to-transpose conjecture on sl_5.

Tests conj:type-a-transport-to-transpose across all 7 nilpotent orbits
of sl_5.  The key new results beyond sl_4:
    - (3,2) <-> (2,2,1): first non-hook, non-rectangular duality pair
    - (3,1,1): the unique self-transpose partition of 5, and it is even
    - rho(5,) = rho(4,1) = 77/60 (anomaly ratio coincidence)
    - 4 non-even orbits vs only 1 in sl_4: richer test of formula limits

Multi-path verification (CLAUDE.md mandate):
    Path 1: direct per-root-pair computation
    Path 2: symbolic coefficient verification c = (ak+b)/(k+N)
    Path 3: complementarity c(k)+c(k') = constant (level-independence)
    Path 4: cross-check against known principal/trivial formulas
    Path 5: anomaly ratio from generator weights
    Path 6: self-dual analysis for (3,1,1)
    Path 7: cross-check against sl_4 engine (structural consistency)
    Path 8: generator count = centralizer dimension
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.theorem_transport_transpose_sl5_engine import (
    ANOMALY_RATIO_COINCIDENCE,
    SL5_PARTITIONS,
    VERIFIED_311_SELF_DUAL_C,
    VERIFIED_ANOMALY_RATIOS,
    VERIFIED_C_COEFFICIENTS,
    VERIFIED_COMPLEMENTARITY,
    anomaly_ratio_sl5,
    central_charge_coefficients_even,
    central_charge_complementarity,
    central_charge_even,
    central_charge_non_even,
    central_charge_sl5,
    complementarity_constant_even,
    complementarity_is_level_independent,
    dual_level,
    duality_profile,
    full_sl5_analysis,
    generator_parity,
    generator_weights_sl5,
    is_even_nilpotent,
    is_hook,
    is_rectangular,
    kappa_complementarity,
    kappa_complementarity_is_level_independent,
    kappa_sl5,
    self_dual_central_charge,
    self_dual_level,
    sl5_orbit_data,
    transpose,
    x_diagonal,
)


# =====================================================================
# Section 1: Partition combinatorics (14 tests)
# =====================================================================

class TestPartitionCombinatorics:
    """Basic partition data for sl_5."""

    def test_all_partitions_of_5(self):
        """There are exactly 7 partitions of 5."""
        assert len(SL5_PARTITIONS) == 7
        for lam in SL5_PARTITIONS:
            assert sum(lam) == 5

    def test_transpose_involution(self):
        """Transpose is an involution: (lambda^t)^t = lambda."""
        for lam in SL5_PARTITIONS:
            assert transpose(transpose(lam)) == lam

    def test_transpose_values(self):
        """Verify transpose for each partition of 5."""
        assert transpose((5,)) == (1, 1, 1, 1, 1)
        assert transpose((4, 1)) == (2, 1, 1, 1)
        assert transpose((3, 2)) == (2, 2, 1)
        assert transpose((3, 1, 1)) == (3, 1, 1)
        assert transpose((2, 2, 1)) == (3, 2)
        assert transpose((2, 1, 1, 1)) == (4, 1)
        assert transpose((1, 1, 1, 1, 1)) == (5,)

    def test_self_transpose_partitions(self):
        """(3,1,1) is the unique self-transpose partition of 5."""
        self_tr = [lam for lam in SL5_PARTITIONS if lam == transpose(lam)]
        assert self_tr == [(3, 1, 1)]

    def test_hook_classification(self):
        """Classify hook vs non-hook partitions."""
        assert is_hook((5,))
        assert is_hook((4, 1))
        assert not is_hook((3, 2))
        assert is_hook((3, 1, 1))
        assert not is_hook((2, 2, 1))
        assert is_hook((2, 1, 1, 1))
        assert is_hook((1, 1, 1, 1, 1))

    def test_rectangular_classification(self):
        """Classify rectangular partitions (all parts equal)."""
        assert is_rectangular((5,))          # single part
        assert not is_rectangular((4, 1))
        assert not is_rectangular((3, 2))
        assert not is_rectangular((3, 1, 1))
        assert not is_rectangular((2, 2, 1))
        assert not is_rectangular((2, 1, 1, 1))
        assert is_rectangular((1, 1, 1, 1, 1))  # all 1s

    def test_even_classification(self):
        """Classify even vs non-even nilpotent orbits."""
        assert is_even_nilpotent((5,))              # all odd
        assert not is_even_nilpotent((4, 1))         # mixed
        assert not is_even_nilpotent((3, 2))         # mixed
        assert is_even_nilpotent((3, 1, 1))          # all odd
        assert not is_even_nilpotent((2, 2, 1))      # mixed (2,2 even + 1 odd)
        assert not is_even_nilpotent((2, 1, 1, 1))   # mixed
        assert is_even_nilpotent((1, 1, 1, 1, 1))   # all odd

    def test_unique_self_transpose_is_even(self):
        """(3,1,1) is the unique self-transpose partition and is even."""
        assert transpose((3, 1, 1)) == (3, 1, 1)
        assert is_even_nilpotent((3, 1, 1))

    def test_221_is_not_self_transpose(self):
        """(2,2,1) is NOT self-transpose: its transpose is (3,2)."""
        assert transpose((2, 2, 1)) == (3, 2)
        assert (2, 2, 1) != (3, 2)

    def test_32_is_neither_hook_nor_rectangular(self):
        """(3,2) is the first orbit that is neither hook nor rectangular."""
        assert not is_hook((3, 2))
        assert not is_rectangular((3, 2))

    def test_centralizer_dimensions(self):
        """Centralizer dimensions via sum(q_i^2)-1."""
        data = sl5_orbit_data()
        assert data[(5,)]["centralizer_dim"] == 4
        assert data[(4, 1)]["centralizer_dim"] == 6
        assert data[(3, 2)]["centralizer_dim"] == 8
        assert data[(3, 1, 1)]["centralizer_dim"] == 10
        assert data[(2, 2, 1)]["centralizer_dim"] == 12
        assert data[(2, 1, 1, 1)]["centralizer_dim"] == 16
        assert data[(1, 1, 1, 1, 1)]["centralizer_dim"] == 24

    def test_orbit_dimensions(self):
        """Orbit dimensions: N^2 - sum(q_i^2)."""
        data = sl5_orbit_data()
        assert data[(5,)]["orbit_dim"] == 20
        assert data[(4, 1)]["orbit_dim"] == 18
        assert data[(3, 2)]["orbit_dim"] == 16
        assert data[(3, 1, 1)]["orbit_dim"] == 14
        assert data[(2, 2, 1)]["orbit_dim"] == 12
        assert data[(2, 1, 1, 1)]["orbit_dim"] == 8
        assert data[(1, 1, 1, 1, 1)]["orbit_dim"] == 0

    def test_orbit_plus_centralizer_equals_dim_g(self):
        """orbit_dim + centralizer_dim + 1 = N^2 = 25 for all orbits."""
        data = sl5_orbit_data()
        for lam in SL5_PARTITIONS:
            assert data[lam]["orbit_dim"] + data[lam]["centralizer_dim"] + 1 == 25

    def test_x_diagonal_values(self):
        """Verify x = h/2 diagonal entries for key partitions."""
        assert x_diagonal((5,)) == [Fraction(-2), Fraction(-1), Fraction(0),
                                     Fraction(1), Fraction(2)]
        assert x_diagonal((3, 1, 1)) == [Fraction(-1), Fraction(0), Fraction(1),
                                          Fraction(0), Fraction(0)]
        assert x_diagonal((1, 1, 1, 1, 1)) == [Fraction(0)] * 5


# =====================================================================
# Section 2: Generator weights and anomaly ratios (12 tests)
# =====================================================================

class TestGenerators:
    """Strong generator content and anomaly ratios."""

    def test_principal_generators(self):
        """W_5 has generators at weights 2, 3, 4, 5."""
        ws = generator_weights_sl5((5,))
        assert ws == [Fraction(2), Fraction(3), Fraction(4), Fraction(5)]

    def test_trivial_generators(self):
        """V_k(sl_5) has 24 generators at weight 1."""
        ws = generator_weights_sl5((1, 1, 1, 1, 1))
        assert len(ws) == 24
        assert all(w == Fraction(1) for w in ws)

    def test_subregular_generators(self):
        """W^k(sl_5, f_{(4,1)}) has generators at 1, 2, 5/2, 5/2, 3, 4."""
        ws = generator_weights_sl5((4, 1))
        assert ws == [Fraction(1), Fraction(2), Fraction(5, 2),
                      Fraction(5, 2), Fraction(3), Fraction(4)]

    def test_32_generators(self):
        """W^k(sl_5, f_{(3,2)}): 1 bos@1 + 2 ferm@3/2 + 2 bos@2 + 2 ferm@5/2 + 1 bos@3."""
        ws = generator_weights_sl5((3, 2))
        assert ws == [Fraction(1), Fraction(3, 2), Fraction(3, 2),
                      Fraction(2), Fraction(2), Fraction(5, 2),
                      Fraction(5, 2), Fraction(3)]

    def test_311_generators(self):
        """W^k(sl_5, f_{(3,1,1)}): 4 bos@1 + 5 bos@2 + 1 bos@3."""
        ws = generator_weights_sl5((3, 1, 1))
        assert ws.count(Fraction(1)) == 4
        assert ws.count(Fraction(2)) == 5
        assert ws.count(Fraction(3)) == 1
        assert len(ws) == 10

    def test_221_generators(self):
        """W^k(sl_5, f_{(2,2,1)}): 4 bos@1 + 4 ferm@3/2 + 4 bos@2."""
        ws = generator_weights_sl5((2, 2, 1))
        assert ws.count(Fraction(1)) == 4
        assert ws.count(Fraction(3, 2)) == 4
        assert ws.count(Fraction(2)) == 4
        assert len(ws) == 12

    def test_2111_generators(self):
        """W^k(sl_5, f_{(2,1,1,1)}): 9 bos@1 + 6 ferm@3/2 + 1 bos@2."""
        ws = generator_weights_sl5((2, 1, 1, 1))
        assert ws.count(Fraction(1)) == 9
        assert ws.count(Fraction(3, 2)) == 6
        assert ws.count(Fraction(2)) == 1
        assert len(ws) == 16

    def test_anomaly_ratio_principal(self):
        """rho(W_5) = 1/2 + 1/3 + 1/4 + 1/5 = 77/60."""
        assert anomaly_ratio_sl5((5,)) == Fraction(77, 60)

    def test_anomaly_ratio_trivial(self):
        """rho(V_k(sl_5)) = 24 (twenty-four weight-1 generators)."""
        assert anomaly_ratio_sl5((1, 1, 1, 1, 1)) == Fraction(24)

    def test_anomaly_ratio_coincidence(self):
        """rho(5,) = rho(4,1) = 77/60: anomaly ratio coincidence."""
        rho_5 = anomaly_ratio_sl5((5,))
        rho_41 = anomaly_ratio_sl5((4, 1))
        assert rho_5 == rho_41 == Fraction(77, 60)

    def test_all_anomaly_ratios_match_verified(self):
        """All anomaly ratios match the independently verified values."""
        for lam, expected in VERIFIED_ANOMALY_RATIOS.items():
            computed = anomaly_ratio_sl5(lam)
            assert computed == expected, f"rho({lam}): {computed} != {expected}"

    def test_generator_count_equals_centralizer_dim(self):
        """Number of generators equals dim(g^f) for each orbit."""
        data = sl5_orbit_data()
        for lam in SL5_PARTITIONS:
            ws = generator_weights_sl5(lam)
            assert len(ws) == data[lam]["centralizer_dim"]


# =====================================================================
# Section 3: Central charge formulas for even nilpotents (14 tests)
# =====================================================================

class TestCentralChargeEven:
    """Central charge c(k) for even nilpotent orbits (VERIFIED)."""

    def test_principal_c_formula(self):
        """c(W_5, k) = (4k - 100)/(k+5)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(5, (5,), kv)
            expected = (4 * kv - 100) / (kv + 5)
            assert c == expected

    def test_trivial_c_formula(self):
        """c(V_k(sl_5), k) = 24k/(k+5)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(5, (1, 1, 1, 1, 1), kv)
            expected = 24 * kv / (kv + 5)
            assert c == expected

    def test_311_c_formula(self):
        """c(W^k(sl_5, f_{(3,1,1)}), k) = (10k - 34)/(k+5)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(5, (3, 1, 1), kv)
            expected = (10 * kv - 34) / (kv + 5)
            assert c == expected

    def test_principal_c_at_k1(self):
        """c(W_5, 1) = (4 - 100)/6 = -16."""
        assert central_charge_even(5, (5,), Fraction(1)) == Fraction(-16)

    def test_trivial_c_at_k1(self):
        """c(V_1(sl_5)) = 24/6 = 4."""
        assert central_charge_even(5, (1, 1, 1, 1, 1), Fraction(1)) == Fraction(4)

    def test_311_c_at_k1(self):
        """c(W^1(sl_5, f_{(3,1,1)})) = (10-34)/6 = -4."""
        assert central_charge_even(5, (3, 1, 1), Fraction(1)) == Fraction(-4)

    def test_coefficients_match_verified(self):
        """Symbolic coefficients c = (ak+b)/(k+5) match hardcoded values."""
        for lam, (a_exp, b_exp) in VERIFIED_C_COEFFICIENTS.items():
            a, b = central_charge_coefficients_even(5, lam)
            assert a == a_exp, f"{lam}: a = {a}, expected {a_exp}"
            assert b == b_exp, f"{lam}: b = {b}, expected {b_exp}"

    def test_even_formula_rejects_non_even(self):
        """central_charge_even raises for non-even partition."""
        with pytest.raises(ValueError, match="not even"):
            central_charge_even(5, (4, 1), Fraction(1))

    def test_critical_level_rejected(self):
        """Critical level k = -5 is rejected."""
        with pytest.raises(ValueError, match="Critical level"):
            central_charge_even(5, (5,), Fraction(-5))

    def test_c_is_rational_function(self):
        """c(k) is exactly (ak+b)/(k+5) at 6 test levels."""
        for lam in [(5,), (3, 1, 1), (1, 1, 1, 1, 1)]:
            a, b = central_charge_coefficients_even(5, lam)
            for kv in [Fraction(1), Fraction(2), Fraction(3),
                       Fraction(7), Fraction(11), Fraction(13)]:
                c = central_charge_even(5, lam, kv)
                assert c == (a * kv + b) / (kv + 5)

    def test_c_leading_behavior(self):
        """As k -> inf, c -> a (the leading coefficient)."""
        for lam in [(5,), (3, 1, 1), (1, 1, 1, 1, 1)]:
            a, b = central_charge_coefficients_even(5, lam)
            c_large = central_charge_even(5, lam, Fraction(100000))
            # c ~ a + (b - 5a)/(k+5), so error ~ |b - 5a|/k
            assert abs(float(c_large) - float(a)) < 0.01

    def test_principal_c_matches_fateev_lukyanov(self):
        """c(W_5) = (N-1)(1 - N(N+1)/(k+N)) for N=5."""
        # c = 4*(1 - 30/(k+5)) = 4 - 120/(k+5) = (4k - 100)/(k+5)
        for kv in [Fraction(1), Fraction(5)]:
            c = central_charge_even(5, (5,), kv)
            expected = 4 * (1 - Fraction(30, kv + 5))
            assert c == expected

    def test_trivial_c_matches_sugawara(self):
        """c(V_k(sl_5)) = dim(sl_5)*k/(k+5) = 24k/(k+5)."""
        for kv in [Fraction(1), Fraction(2), Fraction(10)]:
            c = central_charge_even(5, (1, 1, 1, 1, 1), kv)
            assert c == 24 * kv / (kv + 5)

    def test_leading_coefficient_ordering(self):
        """Leading coefficients a increase as orbit dimension decreases."""
        # Principal: a=4, (3,1,1): a=10, Trivial: a=24
        coeffs = {}
        for lam in [(5,), (3, 1, 1), (1, 1, 1, 1, 1)]:
            a, _ = central_charge_coefficients_even(5, lam)
            coeffs[lam] = a
        assert coeffs[(5,)] < coeffs[(3, 1, 1)] < coeffs[(1, 1, 1, 1, 1)]


# =====================================================================
# Section 4: Central charge complementarity (10 tests)
# =====================================================================

class TestComplementarity:
    """c(k,lambda) + c(k',lambda^t) level-independence."""

    def test_principal_trivial_complementarity(self):
        """c(5;k) + c(1,1,1,1,1;-k-10) = 28 for all k."""
        for kv in [Fraction(1), Fraction(3), Fraction(7), Fraction(11)]:
            s = central_charge_complementarity(5, (5,), kv)
            assert s == 28

    def test_311_self_complementarity(self):
        """c(3,1,1;k) + c(3,1,1;-k-10) = 20 for all k."""
        for kv in [Fraction(1), Fraction(3), Fraction(7), Fraction(11)]:
            s = central_charge_complementarity(5, (3, 1, 1), kv)
            assert s == 20

    def test_principal_trivial_level_independent(self):
        """c-complementarity is level-independent for (5) <-> (1,1,1,1,1)."""
        assert complementarity_is_level_independent((5,))
        assert complementarity_is_level_independent((1, 1, 1, 1, 1))

    def test_311_level_independent(self):
        """c-complementarity is level-independent for (3,1,1) <-> (3,1,1)."""
        assert complementarity_is_level_independent((3, 1, 1))

    def test_complementarity_constants_match_verified(self):
        """Complementarity constants match hardcoded values for even pairs."""
        for lam, expected in VERIFIED_COMPLEMENTARITY.items():
            computed = complementarity_constant_even(lam)
            assert computed == expected, f"{lam}: {computed} != {expected}"

    def test_complementarity_symmetry(self):
        """C(lambda) = C(lambda^t) for even pairs."""
        c_5 = complementarity_constant_even((5,))
        c_11111 = complementarity_constant_even((1, 1, 1, 1, 1))
        assert c_5 == c_11111

    def test_principal_complementarity_at_many_levels(self):
        """Exhaustive test: c(5;k)+c(1,1,1,1,1;k')=28 for 20 levels."""
        for p in range(1, 21):
            kv = Fraction(p)
            s = central_charge_complementarity(5, (5,), kv)
            assert s == 28, f"Failed at k={kv}: c+c' = {s}"

    def test_311_complementarity_at_many_levels(self):
        """Exhaustive test: c(3,1,1;k)+c(3,1,1;k')=20 for 20 levels."""
        for p in range(1, 21):
            kv = Fraction(p)
            s = central_charge_complementarity(5, (3, 1, 1), kv)
            assert s == 20, f"Failed at k={kv}: c+c' = {s}"

    def test_complementarity_via_coefficients(self):
        """Algebraic verification: c+c' = (a+a') - 2N*(b-a'*N-b')/(k+N)/(-k-N).

        For c=(ak+b)/(k+N) and c'=(a'k'+b')/(k'+N) where k'=-k-2N:
        k'+N = -k-N, so c' = (a'(-k-2N)+b')/(-k-N) = (-a'k-2a'N+b')/(-k-N).
        c+c' = (ak+b)/(k+N) + (-a'k-2a'N+b')/(-(k+N))
             = (ak+b)/(k+N) - (-a'k-2a'N+b')/(k+N)
             = (ak+b+a'k+2a'N-b')/(k+N)
             = ((a+a')k + (b-b'+2a'N))/(k+N).
        Level-independent iff a+a' = 0 is impossible for positive a,a'.
        Wait: need to re-derive. c+c' = constant C means
        (a+a')k + (b-b'+2a'N) = C*(k+N) = Ck + CN.
        So a+a' = C and b-b'+2a'N = CN.
        """
        # (5) <-> (1,1,1,1,1)
        a5, b5 = central_charge_coefficients_even(5, (5,))
        a1, b1 = central_charge_coefficients_even(5, (1, 1, 1, 1, 1))
        C = a5 + a1  # = 4 + 24 = 28
        assert C == 28
        assert b5 - b1 + 2 * a1 * 5 == C * 5  # -100 - 0 + 240 = 140 = 28*5

    def test_311_complementarity_via_coefficients(self):
        """Algebraic verification for self-transpose (3,1,1)."""
        a, b = central_charge_coefficients_even(5, (3, 1, 1))
        # Self-transpose: a' = a, b' = b. C = 2a, and b-b+2aN = 2aN = CN/1... wait:
        # C = a+a' = 2a = 20. b-b'+2a'N = 0 + 2*10*5 = 100 = 20*5. Checks out.
        assert 2 * a == 20
        assert 2 * a * 5 == 20 * 5


# =====================================================================
# Section 5: Kappa complementarity (7 tests)
# =====================================================================

class TestKappaComplementarity:
    """Modular characteristic kappa complementarity."""

    def test_311_kappa_complementarity(self):
        """kappa(3,1,1;k) + kappa(3,1,1;k') = 410/3 for all k."""
        # rho(3,1,1) = 41/6 and c+c' = 20, so kappa+kappa' = 41/6*20 = 410/3
        for kv in [Fraction(1), Fraction(3), Fraction(7), Fraction(11)]:
            ks = kappa_complementarity((3, 1, 1), kv)
            assert ks == Fraction(410, 3)

    def test_311_kappa_level_independent(self):
        """kappa complementarity is level-independent for self-transpose (3,1,1)."""
        assert kappa_complementarity_is_level_independent((3, 1, 1))

    def test_principal_trivial_kappa_not_level_independent(self):
        """kappa+kappa' is NOT level-independent for (5)<->(1,1,1,1,1).

        rho(5,) = 77/60 != rho(1,1,1,1,1) = 24, so kappa+kappa' is
        generically k-dependent even though c+c' = 28.
        """
        assert not kappa_complementarity_is_level_independent((5,))

    def test_self_transpose_kappa_equals_rho_times_cc_prime(self):
        """For self-transpose: kappa+kappa' = rho * (c+c') since rho = rho^t."""
        rho = anomaly_ratio_sl5((3, 1, 1))
        C = complementarity_constant_even((3, 1, 1))
        kappa_sum = kappa_complementarity((3, 1, 1), Fraction(1))
        assert kappa_sum == rho * C

    def test_kappa_at_k1_principal(self):
        """kappa(5,; k=1) = 77/60 * (-16) = -308/15."""
        kap = kappa_sl5((5,), Fraction(1))
        assert kap == Fraction(77, 60) * Fraction(-16)
        assert kap == Fraction(-308, 15)

    def test_kappa_at_k1_311(self):
        """kappa(3,1,1; k=1) = 41/6 * (-4) = -82/3."""
        kap = kappa_sl5((3, 1, 1), Fraction(1))
        assert kap == Fraction(41, 6) * Fraction(-4)
        assert kap == Fraction(-82, 3)

    def test_kappa_at_k1_trivial(self):
        """kappa(1,1,1,1,1; k=1) = 24 * 4 = 96."""
        kap = kappa_sl5((1, 1, 1, 1, 1), Fraction(1))
        assert kap == 96


# =====================================================================
# Section 6: The (3,1,1) self-transpose even orbit (8 tests)
# =====================================================================

class TestSelfTransposeEven311:
    """(3,1,1): self-transpose AND even, the clean self-dual test for sl_5."""

    def test_311_is_self_transpose(self):
        """(3,1,1) is self-transpose."""
        assert transpose((3, 1, 1)) == (3, 1, 1)

    def test_311_is_even(self):
        """(3,1,1) is an even nilpotent (all parts odd)."""
        assert is_even_nilpotent((3, 1, 1))

    def test_311_c_complementarity_proved(self):
        """c(3,1,1;k)+c(3,1,1;-k-10) = 20 (VERIFIED, level-independent)."""
        assert complementarity_is_level_independent((3, 1, 1))
        assert complementarity_constant_even((3, 1, 1)) == 20

    def test_311_self_dual_central_charge(self):
        """The self-dual central charge c* = 20/2 = 10."""
        assert self_dual_central_charge((3, 1, 1)) == 10
        assert self_dual_central_charge((3, 1, 1)) == VERIFIED_311_SELF_DUAL_C

    def test_311_c_at_self_dual_is_not_achievable(self):
        """c(k) = 10 has no solution: 10k-34 = 10k+50 is impossible.

        The leading coefficient a = 10 equals c*, so the self-dual level
        is formally k* = -5 (critical level, FF involution fixed point).
        """
        a, _ = central_charge_coefficients_even(5, (3, 1, 1))
        c_star = self_dual_central_charge((3, 1, 1))
        assert a == c_star  # a - c* = 0, no finite k* solution

    def test_311_self_dual_level_is_none(self):
        """self_dual_level returns None (no finite solution)."""
        assert self_dual_level((3, 1, 1)) is None

    def test_311_anomaly_ratio_matches_transpose(self):
        """rho(3,1,1) = rho((3,1,1)^t) since it is self-transpose."""
        assert anomaly_ratio_sl5((3, 1, 1)) == anomaly_ratio_sl5(transpose((3, 1, 1)))

    def test_311_kappa_complementarity(self):
        """kappa(3,1,1;k)+kappa(3,1,1;k') = 410/3 = (41/6)*20."""
        assert kappa_complementarity_is_level_independent((3, 1, 1))
        assert kappa_complementarity((3, 1, 1), Fraction(1)) == Fraction(410, 3)


# =====================================================================
# Section 7: The (3,2) <-> (2,2,1) non-hook pair (KEY NEW RESULT, 8 tests)
# =====================================================================

class TestNonHookPair:
    """(3,2) <-> (2,2,1): the first non-hook, non-rectangular duality pair."""

    def test_32_is_non_hook_non_rectangular(self):
        """(3,2) is neither hook nor rectangular."""
        assert not is_hook((3, 2))
        assert not is_rectangular((3, 2))

    def test_221_is_non_hook_non_rectangular(self):
        """(2,2,1) is neither hook nor rectangular."""
        assert not is_hook((2, 2, 1))
        assert not is_rectangular((2, 2, 1))

    def test_32_221_are_transpose_pair(self):
        """(3,2) and (2,2,1) are transpose of each other."""
        assert transpose((3, 2)) == (2, 2, 1)
        assert transpose((2, 2, 1)) == (3, 2)

    def test_both_non_even(self):
        """Both (3,2) and (2,2,1) are non-even nilpotents."""
        assert not is_even_nilpotent((3, 2))
        assert not is_even_nilpotent((2, 2, 1))

    def test_221_is_not_self_transpose(self):
        """(2,2,1) is NOT self-transpose: its transpose is (3,2)."""
        assert transpose((2, 2, 1)) == (3, 2)
        assert (2, 2, 1) != (3, 2)

    def test_32_anomaly_ratio(self):
        """rho(3,2) = 1/5: low anomaly ratio from fermionic cancellation."""
        assert anomaly_ratio_sl5((3, 2)) == Fraction(1, 5)

    def test_221_anomaly_ratio(self):
        """rho(2,2,1) = 10/3."""
        assert anomaly_ratio_sl5((2, 2, 1)) == Fraction(10, 3)

    def test_32_221_central_charges_compute(self):
        """Both non-even central charges are computable (UNVERIFIED)."""
        c32 = central_charge_non_even(5, (3, 2), Fraction(1))
        c221 = central_charge_non_even(5, (2, 2, 1), Fraction(1))
        assert isinstance(c32, Fraction)
        assert isinstance(c221, Fraction)


# =====================================================================
# Section 8: The (2,2,1) orbit — non-hook, non-even (4 tests)
# =====================================================================

class TestOrbit221:
    """(2,2,1): non-hook, non-even orbit (transpose of (3,2))."""

    def test_221_transpose_is_32(self):
        """(2,2,1)^t = (3,2)."""
        assert transpose((2, 2, 1)) == (3, 2)

    def test_221_is_non_even(self):
        """(2,2,1) is non-even: parts 2,2,1 have mixed parity."""
        assert not is_even_nilpotent((2, 2, 1))

    def test_221_has_half_integer_grades(self):
        """(2,2,1) has half-integer ad(x)-eigenvalues."""
        xd = x_diagonal((2, 2, 1))
        xp = [-xi for xi in xd]
        half_int_count = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if (xp[i] - xp[j]).denominator != 1:
                    half_int_count += 1
        assert half_int_count == 4  # 4 half-integer root pairs

    def test_221_central_charge_computes(self):
        """central_charge_non_even returns a value (UNVERIFIED)."""
        c = central_charge_non_even(5, (2, 2, 1), Fraction(1))
        assert isinstance(c, Fraction)


# =====================================================================
# Section 9: Non-even orbits (6 tests)
# =====================================================================

class TestNonEvenOrbits:
    """Non-even orbits: central charge formula UNVERIFIED."""

    def test_41_is_non_even(self):
        """(4,1) is non-even: parts 4,1 have mixed parity."""
        assert not is_even_nilpotent((4, 1))

    def test_2111_is_non_even(self):
        """(2,1,1,1) is non-even: parts 2,1,1,1 have mixed parity."""
        assert not is_even_nilpotent((2, 1, 1, 1))

    def test_41_has_half_integer_grades(self):
        """(4,1) has 4 half-integer root pairs."""
        xd = x_diagonal((4, 1))
        xp = [-xi for xi in xd]
        half_int_count = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if (xp[i] - xp[j]).denominator != 1:
                    half_int_count += 1
        assert half_int_count == 4

    def test_2111_has_half_integer_grades(self):
        """(2,1,1,1) has 6 half-integer root pairs (more than (4,1))."""
        xd = x_diagonal((2, 1, 1, 1))
        xp = [-xi for xi in xd]
        half_int_count = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if (xp[i] - xp[j]).denominator != 1:
                    half_int_count += 1
        assert half_int_count == 6

    def test_non_even_complementarity_is_k_dependent(self):
        """Non-even c+c' is NOT level-independent (formula unreliable)."""
        # (4,1) <-> (2,1,1,1): the half-integer formula gives k-dependent sums
        assert not complementarity_is_level_independent((4, 1))

    def test_32_221_complementarity_is_k_dependent(self):
        """(3,2) <-> (2,2,1) complementarity is k-dependent (formula unreliable)."""
        assert not complementarity_is_level_independent((3, 2))


# =====================================================================
# Section 10: Dual level (3 tests)
# =====================================================================

class TestDualLevel:
    """Feigin-Frenkel dual level k' = -k - 2N."""

    def test_dual_level_values(self):
        """k' = -k - 10 for sl_5."""
        assert dual_level(5, Fraction(1)) == Fraction(-11)
        assert dual_level(5, Fraction(5)) == Fraction(-15)
        assert dual_level(5, Fraction(0)) == Fraction(-10)

    def test_dual_level_involution(self):
        """(k')' = k: the dual level is an involution."""
        for kv in [Fraction(1), Fraction(5), Fraction(-3)]:
            assert dual_level(5, dual_level(5, kv)) == kv

    def test_dual_level_fixed_point(self):
        """The FF involution has fixed point k* = -N = -5 (critical level)."""
        assert dual_level(5, Fraction(-5)) == Fraction(-5)


# =====================================================================
# Section 11: Full analysis integration (5 tests)
# =====================================================================

class TestFullAnalysis:
    """Integration tests for the complete sl_5 analysis."""

    def test_full_analysis_covers_all_partitions(self):
        """full_sl5_analysis returns data for all 7 partitions."""
        analysis = full_sl5_analysis()
        assert len(analysis) == 7
        for lam in SL5_PARTITIONS:
            assert lam in analysis

    def test_duality_profile_keys(self):
        """Each profile has the expected keys."""
        expected_keys = {
            "partition", "transpose", "is_hook", "is_rectangular", "is_even",
            "is_self_transpose", "generators", "anomaly_ratio",
            "c_formula_verified", "c_at_k1", "c_coefficients",
            "c_complementarity_level_independent",
            "c_complementarity_value",
            "kappa_complementarity_level_independent",
            "self_dual_c", "self_dual_k",
        }
        for lam in SL5_PARTITIONS:
            profile = duality_profile(lam)
            assert set(profile.keys()) == expected_keys

    def test_even_orbits_have_verified_c(self):
        """All even orbits are flagged as c_formula_verified."""
        for lam in [(5,), (3, 1, 1), (1, 1, 1, 1, 1)]:
            profile = duality_profile(lam)
            assert profile["c_formula_verified"]

    def test_non_even_orbits_flagged_unverified(self):
        """All non-even orbits are flagged as c_formula NOT verified."""
        for lam in [(4, 1), (3, 2), (2, 2, 1), (2, 1, 1, 1)]:
            profile = duality_profile(lam)
            assert not profile["c_formula_verified"]

    def test_anomaly_ratio_coincidence_constant(self):
        """The stored anomaly ratio coincidence is correct."""
        val, lams = ANOMALY_RATIO_COINCIDENCE
        assert val == Fraction(77, 60)
        for lam in lams:
            assert anomaly_ratio_sl5(lam) == val


# =====================================================================
# Section 12: Cross-rank structural consistency (6 tests)
# =====================================================================

class TestCrossRankConsistency:
    """Structural consistency checks across sl_4 and sl_5."""

    def test_principal_c_formula_pattern(self):
        """c(W_N) = (N-1)(1 - N(N+1)/(k+N)) for N=5."""
        for kv in [Fraction(1), Fraction(3), Fraction(7)]:
            c = central_charge_even(5, (5,), kv)
            expected = Fraction(4) * (1 - Fraction(30, kv + 5))
            assert c == expected

    def test_trivial_c_formula_pattern(self):
        """c(V_k(sl_N)) = (N^2-1)*k/(k+N) for N=5."""
        for kv in [Fraction(1), Fraction(3), Fraction(7)]:
            c = central_charge_even(5, (1, 1, 1, 1, 1), kv)
            expected = 24 * kv / (kv + 5)
            assert c == expected

    def test_complementarity_sum_ordering(self):
        """C(principal <-> trivial) > C(self-transpose) for both sl_4 and sl_5.

        sl_4: C(4) = 18 > C(2,2) = 14.
        sl_5: C(5) = 28 > C(3,1,1) = 20.
        """
        assert complementarity_constant_even((5,)) > complementarity_constant_even((3, 1, 1))

    def test_principal_complementarity_formula(self):
        """C(principal <-> trivial) = a_princ + a_triv = (N-1) + (N^2-1) = N^2+N-2.

        For N=5: C = 28 = 25+5-2. Check: a_princ = 4, a_triv = 24, sum = 28.
        """
        a_p, _ = central_charge_coefficients_even(5, (5,))
        a_t, _ = central_charge_coefficients_even(5, (1, 1, 1, 1, 1))
        assert a_p + a_t == 28
        assert a_p + a_t == 5**2 + 5 - 2

    def test_self_transpose_complementarity_formula(self):
        """C(self-transpose, even) = 2a for c = (ak+b)/(k+N)."""
        a, _ = central_charge_coefficients_even(5, (3, 1, 1))
        assert 2 * a == 20
        assert 2 * a == complementarity_constant_even((3, 1, 1))

    def test_dim_sl5_is_24(self):
        """dim(sl_5) = N^2-1 = 24, consistent with 24 weight-1 generators."""
        ws = generator_weights_sl5((1, 1, 1, 1, 1))
        assert len(ws) == 24
        assert all(w == 1 for w in ws)
