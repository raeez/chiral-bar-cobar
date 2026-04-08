r"""Tests for the transport-to-transpose conjecture on sl_4.

Tests conj:type-a-transport-to-transpose across all 5 nilpotent orbits
of sl_4.  The key new result is the RECTANGULAR orbit (2,2), which is
the first non-hook test of the conjecture.

Multi-path verification (CLAUDE.md mandate):
    Path 1: direct per-root-pair computation
    Path 2: symbolic coefficient verification c = (ak+b)/(k+N)
    Path 3: complementarity c(k)+c(k') = constant (level-independence)
    Path 4: cross-check against known principal/trivial formulas
    Path 5: anomaly ratio from generator weights
    Path 6: self-dual analysis for (2,2)
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.theorem_transport_transpose_sl4_engine import (
    SL4_PARTITIONS,
    VERIFIED_ANOMALY_RATIOS,
    VERIFIED_C_COEFFICIENTS,
    VERIFIED_COMPLEMENTARITY,
    anomaly_ratio_sl4,
    central_charge_coefficients_even,
    central_charge_complementarity,
    central_charge_even,
    central_charge_non_even,
    central_charge_sl4,
    complementarity_constant_even,
    complementarity_is_level_independent,
    dual_level,
    duality_profile,
    full_sl4_analysis,
    generator_parity,
    generator_weights_sl4,
    is_even_nilpotent,
    is_hook,
    kappa_complementarity,
    kappa_complementarity_is_level_independent,
    kappa_sl4,
    self_dual_central_charge,
    sl4_orbit_data,
    transpose,
    x_diagonal,
)


# =====================================================================
# Section 1: Partition combinatorics (10 tests)
# =====================================================================

class TestPartitionCombinatorics:
    """Basic partition data for sl_4."""

    def test_all_partitions_of_4(self):
        """There are exactly 5 partitions of 4."""
        assert len(SL4_PARTITIONS) == 5
        for lam in SL4_PARTITIONS:
            assert sum(lam) == 4

    def test_transpose_involution(self):
        """Transpose is an involution: (lambda^t)^t = lambda."""
        for lam in SL4_PARTITIONS:
            assert transpose(transpose(lam)) == lam

    def test_transpose_values(self):
        """Verify transpose for each partition of 4."""
        assert transpose((4,)) == (1, 1, 1, 1)
        assert transpose((3, 1)) == (2, 1, 1)
        assert transpose((2, 2)) == (2, 2)
        assert transpose((2, 1, 1)) == (3, 1)
        assert transpose((1, 1, 1, 1)) == (4,)

    def test_self_transpose_22(self):
        """(2,2) is the unique non-trivial self-transpose partition of 4."""
        self_tr = [lam for lam in SL4_PARTITIONS if lam == transpose(lam)]
        assert (2, 2) in self_tr

    def test_hook_classification(self):
        """Classify hook vs non-hook partitions."""
        assert is_hook((4,))
        assert is_hook((3, 1))
        assert not is_hook((2, 2))
        assert is_hook((2, 1, 1))
        assert is_hook((1, 1, 1, 1))

    def test_even_classification(self):
        """Classify even vs non-even nilpotent orbits."""
        assert is_even_nilpotent((4,))        # all parts odd
        assert is_even_nilpotent((3, 1))      # all parts odd
        assert is_even_nilpotent((2, 2))      # all parts even
        assert not is_even_nilpotent((2, 1, 1))  # mixed parity
        assert is_even_nilpotent((1, 1, 1, 1))   # all parts odd

    def test_22_is_non_hook(self):
        """(2,2) is the first non-hook orbit in sl_4."""
        assert not is_hook((2, 2))

    def test_centralizer_dimensions(self):
        """Centralizer dimensions via sum(q_i^2)-1."""
        data = sl4_orbit_data()
        assert data[(4,)]["centralizer_dim"] == 3       # principal
        assert data[(3, 1)]["centralizer_dim"] == 5      # subregular
        assert data[(2, 2)]["centralizer_dim"] == 7      # rectangular
        assert data[(2, 1, 1)]["centralizer_dim"] == 9   # minimal
        assert data[(1, 1, 1, 1)]["centralizer_dim"] == 15  # trivial

    def test_orbit_dimensions(self):
        """Orbit dimensions: N^2 - sum(q_i^2)."""
        data = sl4_orbit_data()
        assert data[(4,)]["orbit_dim"] == 12        # principal
        assert data[(3, 1)]["orbit_dim"] == 10       # subregular
        assert data[(2, 2)]["orbit_dim"] == 8        # rectangular
        assert data[(2, 1, 1)]["orbit_dim"] == 6     # minimal
        assert data[(1, 1, 1, 1)]["orbit_dim"] == 0  # trivial

    def test_x_diagonal_values(self):
        """Verify x = h/2 diagonal entries."""
        assert x_diagonal((4,)) == [Fraction(-3, 2), Fraction(-1, 2),
                                     Fraction(1, 2), Fraction(3, 2)]
        assert x_diagonal((2, 2)) == [Fraction(-1, 2), Fraction(1, 2),
                                       Fraction(-1, 2), Fraction(1, 2)]
        assert x_diagonal((1, 1, 1, 1)) == [Fraction(0)] * 4


# =====================================================================
# Section 2: Generator weights and anomaly ratios (10 tests)
# =====================================================================

class TestGenerators:
    """Strong generator content and anomaly ratios."""

    def test_principal_generators(self):
        """W_4 has generators at weights 2, 3, 4."""
        ws = generator_weights_sl4((4,))
        assert ws == [Fraction(2), Fraction(3), Fraction(4)]

    def test_trivial_generators(self):
        """V_k(sl_4) has 15 generators at weight 1."""
        ws = generator_weights_sl4((1, 1, 1, 1))
        assert len(ws) == 15
        assert all(w == Fraction(1) for w in ws)

    def test_subregular_generators(self):
        """W^k(sl_4, f_{(3,1)}) has generators at weights 1, 2, 2, 2, 3."""
        ws = generator_weights_sl4((3, 1))
        assert ws == [Fraction(1), Fraction(2), Fraction(2), Fraction(2), Fraction(3)]

    def test_rectangular_generators(self):
        """W^k(sl_4, f_{(2,2)}) has generators at weights 1,1,1,2,2,2,2."""
        ws = generator_weights_sl4((2, 2))
        expected = [Fraction(1)] * 3 + [Fraction(2)] * 4
        assert ws == expected

    def test_minimal_generators(self):
        """W^k(sl_4, f_{(2,1,1)}) has 4 weight-1 bos + 4 weight-3/2 ferm + 1 weight-2 bos."""
        ws = generator_weights_sl4((2, 1, 1))
        assert ws.count(Fraction(1)) == 4
        assert ws.count(Fraction(3, 2)) == 4
        assert ws.count(Fraction(2)) == 1
        assert len(ws) == 9

    def test_minimal_has_fermionic_generators(self):
        """(2,1,1) is the only orbit with fermionic generators."""
        for lam in SL4_PARTITIONS:
            ws = generator_weights_sl4(lam)
            parities = [generator_parity(w) for w in ws]
            if lam == (2, 1, 1):
                assert "fermionic" in parities
            else:
                assert "fermionic" not in parities

    def test_anomaly_ratio_principal(self):
        """rho(W_4) = 1/2 + 1/3 + 1/4 = 13/12."""
        assert anomaly_ratio_sl4((4,)) == Fraction(13, 12)

    def test_anomaly_ratio_trivial(self):
        """rho(V_k(sl_4)) = 15 (fifteen weight-1 generators)."""
        assert anomaly_ratio_sl4((1, 1, 1, 1)) == Fraction(15)

    def test_anomaly_ratio_rectangular(self):
        """rho(W^k(sl_4, f_{(2,2)})) = 3*1 + 4*(1/2) = 5."""
        assert anomaly_ratio_sl4((2, 2)) == Fraction(5)

    def test_all_anomaly_ratios_match_verified(self):
        """All anomaly ratios match the independently verified values."""
        for lam, expected in VERIFIED_ANOMALY_RATIOS.items():
            computed = anomaly_ratio_sl4(lam)
            assert computed == expected, f"rho({lam}): {computed} != {expected}"


# =====================================================================
# Section 3: Central charge formulas for even nilpotents (12 tests)
# =====================================================================

class TestCentralChargeEven:
    """Central charge c(k) for even nilpotent orbits (VERIFIED)."""

    def test_principal_c_formula(self):
        """c(W_4, k) = 3 - 60/(k+4) = (3k-48)/(k+4)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(4, (4,), kv)
            expected = (3 * kv - 48) / (kv + 4)
            assert c == expected

    def test_trivial_c_formula(self):
        """c(V_k(sl_4), k) = 15k/(k+4)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(4, (1, 1, 1, 1), kv)
            expected = 15 * kv / (kv + 4)
            assert c == expected

    def test_subregular_c_formula(self):
        """c(W^k(sl_4, f_{(3,1)}), k) = (5k-26)/(k+4)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(4, (3, 1), kv)
            expected = (5 * kv - 26) / (kv + 4)
            assert c == expected

    def test_rectangular_c_formula(self):
        """c(W^k(sl_4, f_{(2,2)}), k) = (7k-16)/(k+4)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(4, (2, 2), kv)
            expected = (7 * kv - 16) / (kv + 4)
            assert c == expected

    def test_principal_c_at_k1(self):
        """c(W_4, 1) = -9."""
        assert central_charge_even(4, (4,), Fraction(1)) == Fraction(-9)

    def test_trivial_c_at_k1(self):
        """c(V_1(sl_4)) = 3."""
        assert central_charge_even(4, (1, 1, 1, 1), Fraction(1)) == Fraction(3)

    def test_rectangular_c_at_k1(self):
        """c(W^1(sl_4, f_{(2,2)})) = (7-16)/5 = -9/5."""
        assert central_charge_even(4, (2, 2), Fraction(1)) == Fraction(-9, 5)

    def test_coefficients_match_verified(self):
        """Symbolic coefficients c = (ak+b)/(k+4) match hardcoded values."""
        for lam, (a_exp, b_exp) in VERIFIED_C_COEFFICIENTS.items():
            a, b = central_charge_coefficients_even(4, lam)
            assert a == a_exp, f"{lam}: a = {a}, expected {a_exp}"
            assert b == b_exp, f"{lam}: b = {b}, expected {b_exp}"

    def test_even_formula_rejects_non_even(self):
        """central_charge_even raises for non-even partition."""
        with pytest.raises(ValueError, match="not even"):
            central_charge_even(4, (2, 1, 1), Fraction(1))

    def test_critical_level_rejected(self):
        """Critical level k = -4 is rejected."""
        with pytest.raises(ValueError, match="Critical level"):
            central_charge_even(4, (4,), Fraction(-4))

    def test_c_is_rational_function(self):
        """c(k) is exactly (ak+b)/(k+4) at 6 test levels."""
        for lam in [(4,), (3, 1), (2, 2), (1, 1, 1, 1)]:
            a, b = central_charge_coefficients_even(4, lam)
            for kv in [Fraction(1), Fraction(2), Fraction(3),
                       Fraction(5), Fraction(7), Fraction(11)]:
                c = central_charge_even(4, lam, kv)
                assert c == (a * kv + b) / (kv + 4)

    def test_c_leading_behavior(self):
        """As k -> inf, c -> a (the leading coefficient)."""
        for lam in [(4,), (3, 1), (2, 2), (1, 1, 1, 1)]:
            a, _ = central_charge_coefficients_even(4, lam)
            c_large = central_charge_even(4, lam, Fraction(10000))
            # c ~ a - stuff/k, so c is close to a for large k
            assert abs(float(c_large) - float(a)) < 0.01


# =====================================================================
# Section 4: Central charge complementarity (8 tests)
# =====================================================================

class TestComplementarity:
    """c(k,lambda) + c(k',lambda^t) level-independence."""

    def test_principal_trivial_complementarity(self):
        """c(4;k) + c(1,1,1,1;-k-8) = 18 for all k."""
        for kv in [Fraction(1), Fraction(3), Fraction(5), Fraction(7)]:
            s = central_charge_complementarity(4, (4,), kv)
            assert s == 18

    def test_rectangular_self_complementarity(self):
        """c(2,2;k) + c(2,2;-k-8) = 14 for all k."""
        for kv in [Fraction(1), Fraction(3), Fraction(5), Fraction(7)]:
            s = central_charge_complementarity(4, (2, 2), kv)
            assert s == 14

    def test_principal_trivial_level_independent(self):
        """c-complementarity is level-independent for (4) <-> (1,1,1,1)."""
        assert complementarity_is_level_independent((4,))
        assert complementarity_is_level_independent((1, 1, 1, 1))

    def test_rectangular_level_independent(self):
        """c-complementarity is level-independent for (2,2) <-> (2,2)."""
        assert complementarity_is_level_independent((2, 2))

    def test_complementarity_constants_match_verified(self):
        """Complementarity constants match hardcoded values for even pairs."""
        for lam, expected in VERIFIED_COMPLEMENTARITY.items():
            computed = complementarity_constant_even(lam)
            assert computed == expected, f"{lam}: {computed} != {expected}"

    def test_complementarity_symmetry(self):
        """C(lambda) = C(lambda^t) for even pairs."""
        c_4 = complementarity_constant_even((4,))
        c_1111 = complementarity_constant_even((1, 1, 1, 1))
        assert c_4 == c_1111

    def test_rectangular_complementarity_at_many_levels(self):
        """Exhaustive test: c(2,2;k)+c(2,2;k')=14 for 20 levels."""
        for p in range(1, 21):
            kv = Fraction(p)
            s = central_charge_complementarity(4, (2, 2), kv)
            assert s == 14, f"Failed at k={kv}: c+c' = {s}"

    def test_principal_complementarity_at_many_levels(self):
        """Exhaustive test: c(4;k)+c(1,1,1,1;k')=18 for 20 levels."""
        for p in range(1, 21):
            kv = Fraction(p)
            s = central_charge_complementarity(4, (4,), kv)
            assert s == 18, f"Failed at k={kv}: c+c' = {s}"


# =====================================================================
# Section 5: Kappa complementarity (5 tests)
# =====================================================================

class TestKappaComplementarity:
    """Modular characteristic kappa complementarity."""

    def test_rectangular_kappa_complementarity(self):
        """kappa(2,2;k) + kappa(2,2;k') = 70 for all k."""
        # rho(2,2) = 5 and c+c' = 14, so kappa+kappa' = 5*14 = 70
        for kv in [Fraction(1), Fraction(3), Fraction(5), Fraction(7)]:
            ks = kappa_complementarity((2, 2), kv)
            assert ks == 70

    def test_rectangular_kappa_level_independent(self):
        """kappa complementarity is level-independent for self-transpose (2,2)."""
        assert kappa_complementarity_is_level_independent((2, 2))

    def test_principal_trivial_kappa_not_level_independent(self):
        """kappa+kappa' is NOT level-independent for (4)<->(1,1,1,1).

        This is because rho(4) = 13/12 != rho(1,1,1,1) = 15, so
        kappa+kappa' = 13/12 * c(4;k) + 15 * c(1,1,1,1;k') is
        generically k-dependent even though c+c' = 18.
        """
        assert not kappa_complementarity_is_level_independent((4,))

    def test_self_transpose_kappa_equals_rho_times_cc_prime(self):
        """For self-transpose: kappa+kappa' = rho * (c+c') since rho = rho^t."""
        rho = anomaly_ratio_sl4((2, 2))
        C = complementarity_constant_even((2, 2))
        kappa_sum = kappa_complementarity((2, 2), Fraction(1))
        assert kappa_sum == rho * C

    def test_kappa_at_k1_rectangular(self):
        """kappa(2,2; k=1) = 5 * (-9/5) = -9."""
        kap = kappa_sl4((2, 2), Fraction(1))
        assert kap == -9


# =====================================================================
# Section 6: The (2,2) rectangular orbit (KEY NEW RESULT, 8 tests)
# =====================================================================

class TestRectangularOrbit:
    """The (2,2) orbit: first non-hook test of transport-to-transpose."""

    def test_22_is_first_non_hook(self):
        """(2,2) is the only non-hook partition of 4."""
        non_hooks = [lam for lam in SL4_PARTITIONS if not is_hook(lam)]
        assert non_hooks == [(2, 2)]

    def test_22_is_even(self):
        """(2,2) is an even nilpotent."""
        assert is_even_nilpotent((2, 2))

    def test_22_self_transpose(self):
        """(2,2) is self-transpose."""
        assert transpose((2, 2)) == (2, 2)

    def test_22_c_complementarity_proved(self):
        """c(2,2;k)+c(2,2;-k-8) = 14 (VERIFIED, level-independent)."""
        assert complementarity_is_level_independent((2, 2))
        assert complementarity_constant_even((2, 2)) == 14

    def test_22_self_dual_central_charge(self):
        """The self-dual central charge c* = 14/2 = 7."""
        assert self_dual_central_charge((2, 2)) == 7

    def test_22_c_at_self_dual_is_not_achievable(self):
        """c(k) = 7 has no solution: 7k-16 = 7k+28 is impossible.

        The FF fixed point k* = -4 is the critical level.
        The self-dual central charge c* = 7 is achieved only in the
        limit k -> -4, which is the critical level singularity.
        """
        # c(k) = (7k-16)/(k+4). For c = 7: 7k-16 = 7(k+4) = 7k+28.
        # -16 = 28: no solution.
        # So the leading coefficient a=7 equals c*, meaning the self-dual
        # level is formally infinite (or the critical level).
        a, _ = central_charge_coefficients_even(4, (2, 2))
        c_star = self_dual_central_charge((2, 2))
        assert a == c_star  # This means (a-c*) = 0, no finite k* solution

    def test_22_anomaly_ratio_matches_transpose(self):
        """rho(2,2) = rho((2,2)^t) since (2,2) is self-transpose."""
        assert anomaly_ratio_sl4((2, 2)) == anomaly_ratio_sl4(transpose((2, 2)))

    def test_22_kappa_complementarity(self):
        """kappa(2,2;k)+kappa(2,2;k') = 70 = 5*14."""
        assert kappa_complementarity_is_level_independent((2, 2))
        assert kappa_complementarity((2, 2), Fraction(1)) == 70


# =====================================================================
# Section 7: Non-even (2,1,1) orbit (4 tests)
# =====================================================================

class TestMinimalOrbit:
    """The (2,1,1) minimal nilpotent: non-even, fermionic generators."""

    def test_211_is_non_even(self):
        """(2,1,1) is non-even: parts 2,1,1 have mixed parity."""
        assert not is_even_nilpotent((2, 1, 1))

    def test_211_has_half_integer_grades(self):
        """(2,1,1) has half-integer ad(x)-eigenvalues."""
        xd = x_diagonal((2, 1, 1))
        xp = [-xi for xi in xd]
        half_int_count = 0
        for i in range(4):
            for j in range(i + 1, 4):
                if (xp[i] - xp[j]).denominator != 1:
                    half_int_count += 1
        assert half_int_count == 4  # 4 half-integer root pairs

    def test_211_anomaly_ratio(self):
        """rho(2,1,1) = 4 - 8/3 + 1/2 = 11/6."""
        assert anomaly_ratio_sl4((2, 1, 1)) == Fraction(11, 6)

    def test_211_central_charge_computes(self):
        """central_charge_non_even returns a value (UNVERIFIED)."""
        c = central_charge_non_even(4, (2, 1, 1), Fraction(1))
        assert isinstance(c, Fraction)
        # The value -43/5 is what the per-root-pair formula gives,
        # but this is UNVERIFIED for non-even nilpotents.
        assert c == Fraction(-43, 5)


# =====================================================================
# Section 8: Dual level (3 tests)
# =====================================================================

class TestDualLevel:
    """Feigin-Frenkel dual level k' = -k - 2N."""

    def test_dual_level_values(self):
        """k' = -k - 8 for sl_4."""
        assert dual_level(4, Fraction(1)) == Fraction(-9)
        assert dual_level(4, Fraction(5)) == Fraction(-13)
        assert dual_level(4, Fraction(0)) == Fraction(-8)

    def test_dual_level_involution(self):
        """(k')' = k: the dual level is an involution."""
        for kv in [Fraction(1), Fraction(5), Fraction(-3)]:
            assert dual_level(4, dual_level(4, kv)) == kv

    def test_dual_level_fixed_point(self):
        """The FF involution has fixed point k* = -N = -4 (critical level)."""
        assert dual_level(4, Fraction(-4)) == Fraction(-4)


# =====================================================================
# Section 9: Full analysis integration (4 tests)
# =====================================================================

class TestFullAnalysis:
    """Integration tests for the complete sl_4 analysis."""

    def test_full_analysis_covers_all_partitions(self):
        """full_sl4_analysis returns data for all 5 partitions."""
        analysis = full_sl4_analysis()
        assert len(analysis) == 5
        for lam in SL4_PARTITIONS:
            assert lam in analysis

    def test_duality_profile_keys(self):
        """Each profile has the expected keys."""
        expected_keys = {
            "partition", "transpose", "is_hook", "is_even",
            "is_self_transpose", "generators", "anomaly_ratio",
            "c_formula_verified", "c_at_k1", "c_coefficients",
            "c_complementarity_level_independent",
            "c_complementarity_value",
            "kappa_complementarity_level_independent",
            "self_dual_c", "self_dual_k",
        }
        for lam in SL4_PARTITIONS:
            profile = duality_profile(lam)
            assert set(profile.keys()) == expected_keys

    def test_even_orbits_have_verified_c(self):
        """All even orbits are flagged as c_formula_verified."""
        for lam in [(4,), (3, 1), (2, 2), (1, 1, 1, 1)]:
            profile = duality_profile(lam)
            assert profile["c_formula_verified"]

    def test_non_even_orbit_flagged_unverified(self):
        """(2,1,1) is flagged as c_formula NOT verified."""
        profile = duality_profile((2, 1, 1))
        assert not profile["c_formula_verified"]


# =====================================================================
# Section 10: Cross-checks against w_algebra_transport_propagation (5 tests)
# =====================================================================

class TestCrossChecks:
    """Cross-check against the existing transport infrastructure."""

    def test_c_principal_matches_fateev_lukyanov(self):
        """c(W_4) = (N-1)(1 - N(N+1)/(k+N)) for N=4."""
        # c = 3*(1 - 20/(k+4)) = 3 - 60/(k+4) = (3k-48)/(k+4) at k=1: -9.
        assert central_charge_even(4, (4,), Fraction(1)) == Fraction(-9)
        assert central_charge_even(4, (4,), Fraction(5)) == Fraction(-11, 3)

    def test_c_trivial_matches_sugawara(self):
        """c(V_k(sl_4)) = 15k/(k+4) (Sugawara formula)."""
        for kv in [Fraction(1), Fraction(2), Fraction(10)]:
            c = central_charge_even(4, (1, 1, 1, 1), kv)
            assert c == 15 * kv / (kv + 4)

    def test_dual_level_matches_existing(self):
        """Dual level matches w_algebra_transport_propagation convention."""
        for kv in [Fraction(1), Fraction(3), Fraction(7)]:
            assert dual_level(4, kv) == -kv - 8

    def test_generator_count_equals_centralizer_dim(self):
        """Number of generators equals dim(g^f) for each orbit."""
        data = sl4_orbit_data()
        for lam in SL4_PARTITIONS:
            ws = generator_weights_sl4(lam)
            assert len(ws) == data[lam]["centralizer_dim"]

    def test_anomaly_ratio_matches_hook_type_w_duality(self):
        """Anomaly ratios match the hook_type_w_duality module where applicable."""
        # Principal W_4: rho = 1/2 + 1/3 + 1/4 = 13/12
        assert anomaly_ratio_sl4((4,)) == Fraction(13, 12)
        # Subregular (3,1): rho = 1 + 3/2 + 1/3 = 17/6
        assert anomaly_ratio_sl4((3, 1)) == Fraction(17, 6)
        # Minimal (2,1,1): rho = 4 - 8/3 + 1/2 = 11/6
        assert anomaly_ratio_sl4((2, 1, 1)) == Fraction(11, 6)
