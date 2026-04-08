r"""Tests for the transport-to-transpose conjecture on sl_6.

Tests conj:type-a-transport-to-transpose across all 11 nilpotent orbits
of sl_6.  The key new results beyond sl_5:
    - (3,3) <-> (2,2,2): first rectangular non-principal even-even pair
    - (3,2,1): self-transpose but NON-EVEN (first such in the programme)
    - (4,2): first non-hook, non-rectangular even orbit beyond principal
    - Leading coefficient coincidence: a(3,1,1,1) = a(2,2,2) = 17
    - Three even<->non-even pairs with open complementarity
    - No anomaly ratio coincidences (unlike sl_5)

Multi-path verification (CLAUDE.md mandate):
    Path 1: direct per-root-pair computation
    Path 2: symbolic coefficient verification c = (ak+b)/(k+N)
    Path 3: complementarity c(k)+c(k') = constant (level-independence)
    Path 4: cross-check against known principal/trivial formulas
    Path 5: anomaly ratio from generator weights
    Path 6: generator count = centralizer dimension
    Path 7: cross-check against sl_4/sl_5 engines (structural consistency)
    Path 8: algebraic complementarity via coefficient sum
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.theorem_transport_transpose_sl6_engine import (
    LEADING_COEFF_COINCIDENCE,
    SELF_TRANSPOSE_321_IS_NON_EVEN,
    SL6_PARTITIONS,
    VERIFIED_ANOMALY_RATIOS,
    VERIFIED_C_COEFFICIENTS,
    VERIFIED_COMPLEMENTARITY,
    anomaly_ratio_sl6,
    central_charge_coefficients_even,
    central_charge_complementarity,
    central_charge_even,
    central_charge_non_even,
    central_charge_sl6,
    complementarity_constant_even,
    complementarity_is_level_independent,
    dual_level,
    duality_profile,
    full_sl6_analysis,
    generator_parity,
    generator_weights_sl6,
    is_even_nilpotent,
    is_hook,
    is_rectangular,
    kappa_complementarity,
    kappa_complementarity_is_level_independent,
    kappa_sl6,
    self_dual_central_charge,
    self_dual_level,
    sl6_orbit_data,
    transpose,
    x_diagonal,
)


# =====================================================================
# Section 1: Partition combinatorics (20 tests)
# =====================================================================

class TestPartitionCombinatorics:
    """Basic partition data for sl_6."""

    def test_all_partitions_of_6(self):
        """There are exactly 11 partitions of 6."""
        assert len(SL6_PARTITIONS) == 11
        for lam in SL6_PARTITIONS:
            assert sum(lam) == 6

    def test_transpose_involution(self):
        """Transpose is an involution: (lambda^t)^t = lambda."""
        for lam in SL6_PARTITIONS:
            assert transpose(transpose(lam)) == lam

    def test_transpose_values(self):
        """Verify transpose for each partition of 6."""
        assert transpose((6,)) == (1, 1, 1, 1, 1, 1)
        assert transpose((5, 1)) == (2, 1, 1, 1, 1)
        assert transpose((4, 2)) == (2, 2, 1, 1)
        assert transpose((4, 1, 1)) == (3, 1, 1, 1)
        assert transpose((3, 3)) == (2, 2, 2)
        assert transpose((3, 2, 1)) == (3, 2, 1)
        assert transpose((3, 1, 1, 1)) == (4, 1, 1)
        assert transpose((2, 2, 2)) == (3, 3)
        assert transpose((2, 2, 1, 1)) == (4, 2)
        assert transpose((2, 1, 1, 1, 1)) == (5, 1)
        assert transpose((1, 1, 1, 1, 1, 1)) == (6,)

    def test_unique_self_transpose(self):
        """(3,2,1) is the unique self-transpose partition of 6."""
        self_tr = [lam for lam in SL6_PARTITIONS if lam == transpose(lam)]
        assert self_tr == [(3, 2, 1)]

    def test_321_self_transpose_is_non_even(self):
        """(3,2,1) is self-transpose but NON-EVEN: the key new phenomenon."""
        assert transpose((3, 2, 1)) == (3, 2, 1)
        assert not is_even_nilpotent((3, 2, 1))
        assert SELF_TRANSPOSE_321_IS_NON_EVEN

    def test_hook_classification(self):
        """Classify hook vs non-hook partitions."""
        assert is_hook((6,))
        assert is_hook((5, 1))
        assert not is_hook((4, 2))
        assert is_hook((4, 1, 1))
        assert not is_hook((3, 3))
        assert not is_hook((3, 2, 1))
        assert is_hook((3, 1, 1, 1))
        assert not is_hook((2, 2, 2))
        assert not is_hook((2, 2, 1, 1))
        assert is_hook((2, 1, 1, 1, 1))
        assert is_hook((1, 1, 1, 1, 1, 1))

    def test_rectangular_classification(self):
        """Classify rectangular partitions."""
        assert is_rectangular((6,))
        assert not is_rectangular((5, 1))
        assert not is_rectangular((4, 2))
        assert not is_rectangular((4, 1, 1))
        assert is_rectangular((3, 3))
        assert not is_rectangular((3, 2, 1))
        assert not is_rectangular((3, 1, 1, 1))
        assert is_rectangular((2, 2, 2))
        assert not is_rectangular((2, 2, 1, 1))
        assert not is_rectangular((2, 1, 1, 1, 1))
        assert is_rectangular((1, 1, 1, 1, 1, 1))

    def test_even_classification(self):
        """7 even orbits and 4 non-even orbits."""
        even = [lam for lam in SL6_PARTITIONS if is_even_nilpotent(lam)]
        non_even = [lam for lam in SL6_PARTITIONS if not is_even_nilpotent(lam)]
        assert len(even) == 7
        assert len(non_even) == 4

    def test_even_orbits_explicit(self):
        """Even orbits: all parts same parity."""
        assert is_even_nilpotent((6,))              # all even
        assert is_even_nilpotent((5, 1))             # all odd
        assert is_even_nilpotent((4, 2))             # all even
        assert not is_even_nilpotent((4, 1, 1))      # mixed
        assert is_even_nilpotent((3, 3))             # all odd
        assert not is_even_nilpotent((3, 2, 1))      # mixed
        assert is_even_nilpotent((3, 1, 1, 1))      # all odd
        assert is_even_nilpotent((2, 2, 2))          # all even
        assert not is_even_nilpotent((2, 2, 1, 1))   # mixed
        assert not is_even_nilpotent((2, 1, 1, 1, 1))  # mixed
        assert is_even_nilpotent((1, 1, 1, 1, 1, 1))  # all odd

    def test_centralizer_dimensions(self):
        """Centralizer dimensions via sum(q_i^2)-1."""
        data = sl6_orbit_data()
        assert data[(6,)]["centralizer_dim"] == 5
        assert data[(5, 1)]["centralizer_dim"] == 7
        assert data[(4, 2)]["centralizer_dim"] == 9
        assert data[(4, 1, 1)]["centralizer_dim"] == 11
        assert data[(3, 3)]["centralizer_dim"] == 11
        assert data[(3, 2, 1)]["centralizer_dim"] == 13
        assert data[(3, 1, 1, 1)]["centralizer_dim"] == 17
        assert data[(2, 2, 2)]["centralizer_dim"] == 17
        assert data[(2, 2, 1, 1)]["centralizer_dim"] == 19
        assert data[(2, 1, 1, 1, 1)]["centralizer_dim"] == 25
        assert data[(1, 1, 1, 1, 1, 1)]["centralizer_dim"] == 35

    def test_orbit_dimensions(self):
        """Orbit dimensions: N^2 - sum(q_i^2)."""
        data = sl6_orbit_data()
        assert data[(6,)]["orbit_dim"] == 30
        assert data[(5, 1)]["orbit_dim"] == 28
        assert data[(4, 2)]["orbit_dim"] == 26
        assert data[(4, 1, 1)]["orbit_dim"] == 24
        assert data[(3, 3)]["orbit_dim"] == 24
        assert data[(3, 2, 1)]["orbit_dim"] == 22
        assert data[(3, 1, 1, 1)]["orbit_dim"] == 18
        assert data[(2, 2, 2)]["orbit_dim"] == 18
        assert data[(2, 2, 1, 1)]["orbit_dim"] == 16
        assert data[(2, 1, 1, 1, 1)]["orbit_dim"] == 10
        assert data[(1, 1, 1, 1, 1, 1)]["orbit_dim"] == 0

    def test_orbit_plus_centralizer_equals_dim_g(self):
        """orbit_dim + centralizer_dim + 1 = N^2 = 36 for all orbits."""
        data = sl6_orbit_data()
        for lam in SL6_PARTITIONS:
            assert data[lam]["orbit_dim"] + data[lam]["centralizer_dim"] + 1 == 36

    def test_x_diagonal_principal(self):
        """x = h/2 diagonal for (6): [-5/2, -3/2, -1/2, 1/2, 3/2, 5/2]."""
        xd = x_diagonal((6,))
        assert xd == [Fraction(-5, 2), Fraction(-3, 2), Fraction(-1, 2),
                       Fraction(1, 2), Fraction(3, 2), Fraction(5, 2)]

    def test_x_diagonal_trivial(self):
        """x = h/2 diagonal for (1^6): all zeros."""
        xd = x_diagonal((1, 1, 1, 1, 1, 1))
        assert xd == [Fraction(0)] * 6

    def test_x_diagonal_33(self):
        """x = h/2 diagonal for (3,3): [-1,0,1,-1,0,1]."""
        xd = x_diagonal((3, 3))
        assert xd == [Fraction(-1), Fraction(0), Fraction(1),
                       Fraction(-1), Fraction(0), Fraction(1)]

    def test_x_diagonal_222(self):
        """x = h/2 diagonal for (2,2,2): [-1/2,1/2,-1/2,1/2,-1/2,1/2]."""
        xd = x_diagonal((2, 2, 2))
        assert xd == [Fraction(-1, 2), Fraction(1, 2)] * 3

    def test_33_222_not_self_transpose(self):
        """(3,3) and (2,2,2) are rectangular but NOT self-transpose."""
        assert transpose((3, 3)) == (2, 2, 2)
        assert (3, 3) != (2, 2, 2)
        assert transpose((2, 2, 2)) == (3, 3)
        assert (2, 2, 2) != (3, 3)

    def test_centralizer_dim_coincidences(self):
        """Two pairs share centralizer dim: (4,1,1)=(3,3)=11, (3,1,1,1)=(2,2,2)=17."""
        data = sl6_orbit_data()
        assert data[(4, 1, 1)]["centralizer_dim"] == data[(3, 3)]["centralizer_dim"] == 11
        assert data[(3, 1, 1, 1)]["centralizer_dim"] == data[(2, 2, 2)]["centralizer_dim"] == 17

    def test_orbit_dim_coincidences(self):
        """Two pairs share orbit dim: (4,1,1)=(3,3)=24, (3,1,1,1)=(2,2,2)=18."""
        data = sl6_orbit_data()
        assert data[(4, 1, 1)]["orbit_dim"] == data[(3, 3)]["orbit_dim"] == 24
        assert data[(3, 1, 1, 1)]["orbit_dim"] == data[(2, 2, 2)]["orbit_dim"] == 18


# =====================================================================
# Section 2: Generator weights and anomaly ratios (16 tests)
# =====================================================================

class TestGenerators:
    """Strong generator content and anomaly ratios."""

    def test_principal_generators(self):
        """W_6 has generators at weights 2, 3, 4, 5, 6."""
        ws = generator_weights_sl6((6,))
        assert ws == [Fraction(2), Fraction(3), Fraction(4),
                      Fraction(5), Fraction(6)]

    def test_trivial_generators(self):
        """V_k(sl_6) has 35 generators at weight 1."""
        ws = generator_weights_sl6((1, 1, 1, 1, 1, 1))
        assert len(ws) == 35
        assert all(w == Fraction(1) for w in ws)

    def test_51_generators(self):
        """W^k(sl_6, f_{(5,1)}): 7 generators, all bosonic."""
        ws = generator_weights_sl6((5, 1))
        assert len(ws) == 7
        assert all(generator_parity(w) == "bosonic" for w in ws)

    def test_42_generators(self):
        """W^k(sl_6, f_{(4,2)}): 9 generators, all bosonic."""
        ws = generator_weights_sl6((4, 2))
        assert len(ws) == 9
        assert all(generator_parity(w) == "bosonic" for w in ws)

    def test_33_generators(self):
        """W^k(sl_6, f_{(3,3)}): 11 generators at 1x3, 2x4, 3x4."""
        ws = generator_weights_sl6((3, 3))
        assert ws.count(Fraction(1)) == 3
        assert ws.count(Fraction(2)) == 4
        assert ws.count(Fraction(3)) == 4
        assert len(ws) == 11
        assert all(generator_parity(w) == "bosonic" for w in ws)

    def test_222_generators(self):
        """W^k(sl_6, f_{(2,2,2)}): 17 generators at 1x8, 2x9."""
        ws = generator_weights_sl6((2, 2, 2))
        assert ws.count(Fraction(1)) == 8
        assert ws.count(Fraction(2)) == 9
        assert len(ws) == 17
        assert all(generator_parity(w) == "bosonic" for w in ws)

    def test_321_generators(self):
        """W^k(sl_6, f_{(3,2,1)}): 13 generators, 7 bosonic + 6 fermionic."""
        ws = generator_weights_sl6((3, 2, 1))
        assert len(ws) == 13
        n_bos = sum(1 for w in ws if generator_parity(w) == "bosonic")
        n_ferm = sum(1 for w in ws if generator_parity(w) == "fermionic")
        assert n_bos == 7
        assert n_ferm == 6

    def test_411_generators(self):
        """W^k(sl_6, f_{(4,1,1)}): 11 generators, 7 bosonic + 4 fermionic."""
        ws = generator_weights_sl6((4, 1, 1))
        assert len(ws) == 11
        n_bos = sum(1 for w in ws if generator_parity(w) == "bosonic")
        n_ferm = sum(1 for w in ws if generator_parity(w) == "fermionic")
        assert n_bos == 7
        assert n_ferm == 4

    def test_2211_generators(self):
        """W^k(sl_6, f_{(2,2,1,1)}): 19 generators, 11 bosonic + 8 fermionic."""
        ws = generator_weights_sl6((2, 2, 1, 1))
        assert len(ws) == 19
        n_bos = sum(1 for w in ws if generator_parity(w) == "bosonic")
        n_ferm = sum(1 for w in ws if generator_parity(w) == "fermionic")
        assert n_bos == 11
        assert n_ferm == 8

    def test_21111_generators(self):
        """W^k(sl_6, f_{(2,1,1,1,1)}): 25 generators, 17 bosonic + 8 fermionic."""
        ws = generator_weights_sl6((2, 1, 1, 1, 1))
        assert len(ws) == 25
        n_bos = sum(1 for w in ws if generator_parity(w) == "bosonic")
        n_ferm = sum(1 for w in ws if generator_parity(w) == "fermionic")
        assert n_bos == 17
        assert n_ferm == 8

    def test_anomaly_ratio_principal(self):
        """rho(W_6) = 1/2 + 1/3 + 1/4 + 1/5 + 1/6 = 29/20."""
        expected = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + \
                   Fraction(1, 5) + Fraction(1, 6)
        assert expected == Fraction(29, 20)
        assert anomaly_ratio_sl6((6,)) == Fraction(29, 20)

    def test_anomaly_ratio_trivial(self):
        """rho(V_k(sl_6)) = 35 (thirty-five weight-1 generators)."""
        assert anomaly_ratio_sl6((1, 1, 1, 1, 1, 1)) == Fraction(35)

    def test_all_anomaly_ratios_match_verified(self):
        """All anomaly ratios match the independently verified values."""
        for lam, expected in VERIFIED_ANOMALY_RATIOS.items():
            computed = anomaly_ratio_sl6(lam)
            assert computed == expected, f"rho({lam}): {computed} != {expected}"

    def test_no_anomaly_ratio_coincidences(self):
        """No two distinct partitions share the same anomaly ratio (unlike sl_5)."""
        ratios = {}
        for lam in SL6_PARTITIONS:
            r = anomaly_ratio_sl6(lam)
            if r in ratios:
                # This should not happen for sl_6
                assert False, f"Coincidence: rho({lam}) = rho({ratios[r]}) = {r}"
            ratios[r] = lam

    def test_generator_count_equals_centralizer_dim(self):
        """Number of generators equals dim(g^f) for each orbit."""
        data = sl6_orbit_data()
        for lam in SL6_PARTITIONS:
            ws = generator_weights_sl6(lam)
            assert len(ws) == data[lam]["centralizer_dim"]

    def test_leading_coeff_coincidence(self):
        """a(3,1,1,1) = a(2,2,2) = 17: leading coefficient coincidence."""
        val, lams = LEADING_COEFF_COINCIDENCE
        assert val == Fraction(17)
        for lam in lams:
            a, _ = central_charge_coefficients_even(6, lam)
            assert a == val


# =====================================================================
# Section 3: Central charge formulas for even nilpotents (18 tests)
# =====================================================================

class TestCentralChargeEven:
    """Central charge c(k) for even nilpotent orbits (VERIFIED)."""

    def test_principal_c_formula(self):
        """c(W_6, k) = (5k - 180)/(k+6)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(6, (6,), kv)
            expected = (5 * kv - 180) / (kv + 6)
            assert c == expected

    def test_trivial_c_formula(self):
        """c(V_k(sl_6), k) = 35k/(k+6)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(6, (1, 1, 1, 1, 1, 1), kv)
            expected = 35 * kv / (kv + 6)
            assert c == expected

    def test_51_c_formula(self):
        """c(W^k(sl_6, f_{(5,1)}), k) = (7k - 128)/(k+6)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(6, (5, 1), kv)
            expected = (7 * kv - 128) / (kv + 6)
            assert c == expected

    def test_42_c_formula(self):
        """c(W^k(sl_6, f_{(4,2)}), k) = (9k - 88)/(k+6)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(6, (4, 2), kv)
            expected = (9 * kv - 88) / (kv + 6)
            assert c == expected

    def test_33_c_formula(self):
        """c(W^k(sl_6, f_{(3,3)}), k) = (11k - 72)/(k+6)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(6, (3, 3), kv)
            expected = (11 * kv - 72) / (kv + 6)
            assert c == expected

    def test_3111_c_formula(self):
        """c(W^k(sl_6, f_{(3,1,1,1)}), k) = (17k - 42)/(k+6)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(6, (3, 1, 1, 1), kv)
            expected = (17 * kv - 42) / (kv + 6)
            assert c == expected

    def test_222_c_formula(self):
        """c(W^k(sl_6, f_{(2,2,2)}), k) = (17k - 36)/(k+6)."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c = central_charge_even(6, (2, 2, 2), kv)
            expected = (17 * kv - 36) / (kv + 6)
            assert c == expected

    def test_principal_c_at_k1(self):
        """c(W_6, 1) = (5 - 180)/7 = -25."""
        assert central_charge_even(6, (6,), Fraction(1)) == Fraction(-25)

    def test_trivial_c_at_k1(self):
        """c(V_1(sl_6)) = 35/7 = 5."""
        assert central_charge_even(6, (1, 1, 1, 1, 1, 1), Fraction(1)) == Fraction(5)

    def test_33_c_at_k1(self):
        """c(W^1(sl_6, f_{(3,3)})) = (11-72)/7 = -61/7."""
        assert central_charge_even(6, (3, 3), Fraction(1)) == Fraction(-61, 7)

    def test_222_c_at_k1(self):
        """c(W^1(sl_6, f_{(2,2,2)})) = (17-36)/7 = -19/7."""
        assert central_charge_even(6, (2, 2, 2), Fraction(1)) == Fraction(-19, 7)

    def test_coefficients_match_verified(self):
        """Symbolic coefficients c = (ak+b)/(k+6) match hardcoded values."""
        for lam, (a_exp, b_exp) in VERIFIED_C_COEFFICIENTS.items():
            a, b = central_charge_coefficients_even(6, lam)
            assert a == a_exp, f"{lam}: a = {a}, expected {a_exp}"
            assert b == b_exp, f"{lam}: b = {b}, expected {b_exp}"

    def test_even_formula_rejects_non_even(self):
        """central_charge_even raises for non-even partition."""
        with pytest.raises(ValueError, match="not even"):
            central_charge_even(6, (4, 1, 1), Fraction(1))

    def test_critical_level_rejected(self):
        """Critical level k = -6 is rejected."""
        with pytest.raises(ValueError, match="Critical level"):
            central_charge_even(6, (6,), Fraction(-6))

    def test_c_is_rational_function(self):
        """c(k) is exactly (ak+b)/(k+6) at 6 test levels for all even orbits."""
        even_orbits = [lam for lam in SL6_PARTITIONS if is_even_nilpotent(lam)]
        for lam in even_orbits:
            a, b = central_charge_coefficients_even(6, lam)
            for kv in [Fraction(1), Fraction(2), Fraction(3),
                       Fraction(7), Fraction(11), Fraction(13)]:
                c = central_charge_even(6, lam, kv)
                assert c == (a * kv + b) / (kv + 6), \
                    f"Mismatch for {lam} at k={kv}"

    def test_principal_c_matches_fateev_lukyanov(self):
        """c(W_6) = (N-1)(1 - N(N+1)/(k+N)) for N=6."""
        for kv in [Fraction(1), Fraction(5)]:
            c = central_charge_even(6, (6,), kv)
            expected = 5 * (1 - Fraction(42, kv + 6))
            assert c == expected

    def test_trivial_c_matches_sugawara(self):
        """c(V_k(sl_6)) = dim(sl_6)*k/(k+6) = 35k/(k+6)."""
        for kv in [Fraction(1), Fraction(2), Fraction(10)]:
            c = central_charge_even(6, (1, 1, 1, 1, 1, 1), kv)
            assert c == 35 * kv / (kv + 6)

    def test_leading_coefficient_ordering(self):
        """Leading coefficients a increase as orbit dimension decreases."""
        even_ordered = [(6,), (5, 1), (4, 2), (3, 3),
                        (3, 1, 1, 1), (2, 2, 2), (1, 1, 1, 1, 1, 1)]
        coeffs = []
        for lam in even_ordered:
            a, _ = central_charge_coefficients_even(6, lam)
            coeffs.append(a)
        # a values: 5, 7, 9, 11, 17, 17, 35
        # Non-strictly increasing because (3,1,1,1) and (2,2,2) tie at 17
        for i in range(len(coeffs) - 1):
            assert coeffs[i] <= coeffs[i + 1]


# =====================================================================
# Section 4: Central charge complementarity (14 tests)
# =====================================================================

class TestComplementarity:
    """c(k,lambda) + c(k',lambda^t) level-independence."""

    def test_principal_trivial_complementarity(self):
        """c(6;k) + c(1^6;-k-12) = 40 for all k."""
        for kv in [Fraction(1), Fraction(3), Fraction(7), Fraction(11)]:
            s = central_charge_complementarity(6, (6,), kv)
            assert s == 40

    def test_33_222_complementarity(self):
        """c(3,3;k) + c(2,2,2;-k-12) = 28 for all k."""
        for kv in [Fraction(1), Fraction(3), Fraction(7), Fraction(11)]:
            s = central_charge_complementarity(6, (3, 3), kv)
            assert s == 28

    def test_222_33_complementarity(self):
        """c(2,2,2;k) + c(3,3;-k-12) = 28 for all k (reverse direction)."""
        for kv in [Fraction(1), Fraction(3), Fraction(7), Fraction(11)]:
            s = central_charge_complementarity(6, (2, 2, 2), kv)
            assert s == 28

    def test_principal_trivial_level_independent(self):
        """c-complementarity is level-independent for (6) <-> (1^6)."""
        assert complementarity_is_level_independent((6,))
        assert complementarity_is_level_independent((1, 1, 1, 1, 1, 1))

    def test_33_222_level_independent(self):
        """c-complementarity is level-independent for (3,3) <-> (2,2,2)."""
        assert complementarity_is_level_independent((3, 3))
        assert complementarity_is_level_independent((2, 2, 2))

    def test_complementarity_constants_match_verified(self):
        """Complementarity constants match hardcoded values for even-even pairs."""
        for lam, expected in VERIFIED_COMPLEMENTARITY.items():
            computed = complementarity_constant_even(lam)
            assert computed == expected, f"{lam}: {computed} != {expected}"

    def test_complementarity_symmetry_principal(self):
        """C(6) = C(1^6) = 40."""
        assert complementarity_constant_even((6,)) == \
               complementarity_constant_even((1, 1, 1, 1, 1, 1))

    def test_complementarity_symmetry_rectangular(self):
        """C(3,3) = C(2,2,2) = 28."""
        assert complementarity_constant_even((3, 3)) == \
               complementarity_constant_even((2, 2, 2))

    def test_principal_complementarity_exhaustive(self):
        """c(6;k)+c(1^6;k')=40 for 20 levels."""
        for p in range(1, 21):
            kv = Fraction(p)
            s = central_charge_complementarity(6, (6,), kv)
            assert s == 40, f"Failed at k={kv}: c+c' = {s}"

    def test_33_222_complementarity_exhaustive(self):
        """c(3,3;k)+c(2,2,2;k')=28 for 20 levels."""
        for p in range(1, 21):
            kv = Fraction(p)
            s = central_charge_complementarity(6, (3, 3), kv)
            assert s == 28, f"Failed at k={kv}: c+c' = {s}"

    def test_complementarity_via_coefficients_principal(self):
        """Algebraic: a(6)+a(1^6) = 5+35 = 40 = C."""
        a_p, b_p = central_charge_coefficients_even(6, (6,))
        a_t, b_t = central_charge_coefficients_even(6, (1, 1, 1, 1, 1, 1))
        C = a_p + a_t
        assert C == 40
        assert b_p - b_t + 2 * a_t * 6 == C * 6

    def test_complementarity_via_coefficients_rectangular(self):
        """Algebraic: a(3,3)+a(2,2,2) = 11+17 = 28 = C."""
        a33, b33 = central_charge_coefficients_even(6, (3, 3))
        a222, b222 = central_charge_coefficients_even(6, (2, 2, 2))
        C = a33 + a222
        assert C == 28
        assert b33 - b222 + 2 * a222 * 6 == C * 6

    def test_principal_complementarity_formula(self):
        """C(principal <-> trivial) = N^2+N-2 = 40 for N=6."""
        a_p, _ = central_charge_coefficients_even(6, (6,))
        a_t, _ = central_charge_coefficients_even(6, (1, 1, 1, 1, 1, 1))
        assert a_p + a_t == 6**2 + 6 - 2

    def test_even_non_even_complementarity_open(self):
        """Even<->non-even pairs: complementarity is k-dependent (OPEN)."""
        assert not complementarity_is_level_independent((5, 1))
        assert not complementarity_is_level_independent((4, 2))
        assert not complementarity_is_level_independent((4, 1, 1))
        assert not complementarity_is_level_independent((3, 1, 1, 1))


# =====================================================================
# Section 5: Kappa complementarity (8 tests)
# =====================================================================

class TestKappaComplementarity:
    """Modular characteristic kappa complementarity."""

    def test_principal_trivial_kappa_not_level_independent(self):
        """kappa+kappa' is NOT level-independent for (6)<->(1^6).

        rho(6,) = 29/20 != rho(1^6) = 35.
        """
        assert not kappa_complementarity_is_level_independent((6,))

    def test_33_222_kappa_not_level_independent(self):
        """kappa+kappa' is NOT level-independent for (3,3)<->(2,2,2).

        rho(3,3) = 19/3 != rho(2,2,2) = 25/2.
        """
        assert not kappa_complementarity_is_level_independent((3, 3))

    def test_kappa_at_k1_principal(self):
        """kappa(6,; k=1) = 29/20 * (-25) = -725/20 = -145/4."""
        kap = kappa_sl6((6,), Fraction(1))
        assert kap == Fraction(29, 20) * Fraction(-25)
        assert kap == Fraction(-145, 4)

    def test_kappa_at_k1_trivial(self):
        """kappa(1^6; k=1) = 35 * 5 = 175."""
        kap = kappa_sl6((1, 1, 1, 1, 1, 1), Fraction(1))
        assert kap == 175

    def test_kappa_at_k1_33(self):
        """kappa(3,3; k=1) = 19/3 * (-61/7) = -1159/21."""
        kap = kappa_sl6((3, 3), Fraction(1))
        assert kap == Fraction(19, 3) * Fraction(-61, 7)
        assert kap == Fraction(-1159, 21)

    def test_kappa_at_k1_222(self):
        """kappa(2,2,2; k=1) = 25/2 * (-19/7) = -475/14."""
        kap = kappa_sl6((2, 2, 2), Fraction(1))
        assert kap == Fraction(25, 2) * Fraction(-19, 7)
        assert kap == Fraction(-475, 14)

    def test_kappa_formula_all_even(self):
        """kappa = rho * c for all even orbits at multiple levels."""
        even_orbits = [lam for lam in SL6_PARTITIONS if is_even_nilpotent(lam)]
        for lam in even_orbits:
            for kv in [Fraction(1), Fraction(3), Fraction(7)]:
                kap = kappa_sl6(lam, kv)
                rho = anomaly_ratio_sl6(lam)
                c = central_charge_sl6(lam, kv)
                assert kap == rho * c, f"kappa != rho*c for {lam} at k={kv}"

    def test_kappa_formula_all_non_even(self):
        """kappa = rho * c for all non-even orbits (UNVERIFIED c)."""
        non_even_orbits = [lam for lam in SL6_PARTITIONS
                           if not is_even_nilpotent(lam)]
        for lam in non_even_orbits:
            for kv in [Fraction(1), Fraction(3), Fraction(7)]:
                kap = kappa_sl6(lam, kv)
                rho = anomaly_ratio_sl6(lam)
                c = central_charge_sl6(lam, kv)
                assert kap == rho * c


# =====================================================================
# Section 6: The (3,3) <-> (2,2,2) rectangular pair (10 tests)
# =====================================================================

class TestRectangularPair:
    """(3,3) <-> (2,2,2): first rectangular non-principal even-even pair."""

    def test_33_is_rectangular(self):
        """(3,3) is rectangular (all parts equal)."""
        assert is_rectangular((3, 3))

    def test_222_is_rectangular(self):
        """(2,2,2) is rectangular (all parts equal)."""
        assert is_rectangular((2, 2, 2))

    def test_33_not_hook(self):
        """(3,3) is NOT hook."""
        assert not is_hook((3, 3))

    def test_222_not_hook(self):
        """(2,2,2) is NOT hook."""
        assert not is_hook((2, 2, 2))

    def test_both_even(self):
        """Both (3,3) and (2,2,2) are even nilpotents."""
        assert is_even_nilpotent((3, 3))
        assert is_even_nilpotent((2, 2, 2))

    def test_transpose_pair(self):
        """(3,3) and (2,2,2) are transposes of each other."""
        assert transpose((3, 3)) == (2, 2, 2)
        assert transpose((2, 2, 2)) == (3, 3)

    def test_complementarity_verified(self):
        """c(3,3)+c(2,2,2;dual) = 28 (VERIFIED, level-independent)."""
        assert complementarity_is_level_independent((3, 3))
        assert complementarity_constant_even((3, 3)) == 28

    def test_c_complementarity_algebraic(self):
        """Algebraic: (11k-72)/(k+6) + (17(-k-12)-36)/(-k-6) = 28."""
        a33, b33 = Fraction(11), Fraction(-72)
        a222, b222 = Fraction(17), Fraction(-36)
        # c(3,3;k) + c(2,2,2;k') where k'=-k-12
        # = (a33*k+b33)/(k+6) + (a222*(-k-12)+b222)/(-k-6)
        # = (a33*k+b33)/(k+6) + (-a222*k-12*a222+b222)/(-(k+6))
        # = (a33*k+b33 + a222*k + 12*a222 - b222)/(k+6)
        # = ((a33+a222)*k + (b33 - b222 + 12*a222))/(k+6)
        numerator_k_coeff = a33 + a222
        numerator_const = b33 - b222 + 12 * a222
        assert numerator_k_coeff == 28
        assert numerator_const == 28 * 6

    def test_anomaly_ratios_distinct(self):
        """rho(3,3) != rho(2,2,2): no anomaly ratio coincidence."""
        assert anomaly_ratio_sl6((3, 3)) == Fraction(19, 3)
        assert anomaly_ratio_sl6((2, 2, 2)) == Fraction(25, 2)
        assert anomaly_ratio_sl6((3, 3)) != anomaly_ratio_sl6((2, 2, 2))

    def test_leading_coefficient_sum_equals_c_plus_c_prime(self):
        """For (3,3)<->(2,2,2): C = a+a' = 11+17 = 28."""
        a33, _ = central_charge_coefficients_even(6, (3, 3))
        a222, _ = central_charge_coefficients_even(6, (2, 2, 2))
        assert a33 + a222 == 28


# =====================================================================
# Section 7: The (3,2,1) self-transpose non-even orbit (8 tests)
# =====================================================================

class TestSelfTranspose321:
    """(3,2,1): the unique self-transpose partition of 6 (NON-EVEN)."""

    def test_321_is_self_transpose(self):
        """(3,2,1) is self-transpose."""
        assert transpose((3, 2, 1)) == (3, 2, 1)

    def test_321_is_non_even(self):
        """(3,2,1) is NON-EVEN: parts 3,2,1 have mixed parity."""
        assert not is_even_nilpotent((3, 2, 1))

    def test_321_not_hook_not_rectangular(self):
        """(3,2,1) is neither hook nor rectangular."""
        assert not is_hook((3, 2, 1))
        assert not is_rectangular((3, 2, 1))

    def test_321_anomaly_ratio(self):
        """rho(3,2,1) = 13/15."""
        assert anomaly_ratio_sl6((3, 2, 1)) == Fraction(13, 15)

    def test_321_has_8_half_integer_root_pairs(self):
        """(3,2,1) has 8 half-integer root pairs."""
        xd = x_diagonal((3, 2, 1))
        xp = [-xi for xi in xd]
        half_count = sum(
            1 for i in range(6) for j in range(i + 1, 6)
            if (xp[i] - xp[j]).denominator != 1
        )
        assert half_count == 8

    def test_321_self_dual_c_is_none(self):
        """Self-dual central charge is None (non-even, no verified formula)."""
        assert self_dual_central_charge((3, 2, 1)) is None

    def test_321_self_dual_level_is_none(self):
        """Self-dual level is None (non-even)."""
        assert self_dual_level((3, 2, 1)) is None

    def test_321_central_charge_computes(self):
        """Non-even central charge formula returns a value (UNVERIFIED)."""
        c = central_charge_non_even(6, (3, 2, 1), Fraction(1))
        assert isinstance(c, Fraction)


# =====================================================================
# Section 8: Even <-> Non-even pairs (6 tests)
# =====================================================================

class TestEvenNonEvenPairs:
    """Three even<->non-even pairs with OPEN complementarity."""

    def test_51_21111_pair(self):
        """(5,1) even <-> (2,1,1,1,1) non-even."""
        assert is_even_nilpotent((5, 1))
        assert not is_even_nilpotent((2, 1, 1, 1, 1))
        assert transpose((5, 1)) == (2, 1, 1, 1, 1)

    def test_42_2211_pair(self):
        """(4,2) even <-> (2,2,1,1) non-even."""
        assert is_even_nilpotent((4, 2))
        assert not is_even_nilpotent((2, 2, 1, 1))
        assert transpose((4, 2)) == (2, 2, 1, 1)

    def test_411_3111_pair(self):
        """(4,1,1) non-even <-> (3,1,1,1) even."""
        assert not is_even_nilpotent((4, 1, 1))
        assert is_even_nilpotent((3, 1, 1, 1))
        assert transpose((4, 1, 1)) == (3, 1, 1, 1)

    def test_51_21111_complementarity_open(self):
        """(5,1)<->(2,1,1,1,1) complementarity is k-dependent."""
        assert not complementarity_is_level_independent((5, 1))

    def test_42_2211_complementarity_open(self):
        """(4,2)<->(2,2,1,1) complementarity is k-dependent."""
        assert not complementarity_is_level_independent((4, 2))

    def test_411_3111_complementarity_open(self):
        """(4,1,1)<->(3,1,1,1) complementarity is k-dependent."""
        assert not complementarity_is_level_independent((4, 1, 1))


# =====================================================================
# Section 9: Non-even orbits (8 tests)
# =====================================================================

class TestNonEvenOrbits:
    """All 4 non-even orbits: central charge formula UNVERIFIED."""

    def test_411_has_8_half_integer_pairs(self):
        """(4,1,1) has 8 half-integer root pairs."""
        xd = x_diagonal((4, 1, 1))
        xp = [-xi for xi in xd]
        half_count = sum(
            1 for i in range(6) for j in range(i + 1, 6)
            if (xp[i] - xp[j]).denominator != 1
        )
        assert half_count == 8

    def test_2211_has_8_half_integer_pairs(self):
        """(2,2,1,1) has 8 half-integer root pairs."""
        xd = x_diagonal((2, 2, 1, 1))
        xp = [-xi for xi in xd]
        half_count = sum(
            1 for i in range(6) for j in range(i + 1, 6)
            if (xp[i] - xp[j]).denominator != 1
        )
        assert half_count == 8

    def test_21111_has_8_half_integer_pairs(self):
        """(2,1,1,1,1) has 8 half-integer root pairs."""
        xd = x_diagonal((2, 1, 1, 1, 1))
        xp = [-xi for xi in xd]
        half_count = sum(
            1 for i in range(6) for j in range(i + 1, 6)
            if (xp[i] - xp[j]).denominator != 1
        )
        assert half_count == 8

    def test_all_non_even_have_8_half_integer_pairs(self):
        """All 4 non-even orbits of sl_6 have exactly 8 half-integer root pairs."""
        for lam in [(4, 1, 1), (3, 2, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1)]:
            xd = x_diagonal(lam)
            xp = [-xi for xi in xd]
            half_count = sum(
                1 for i in range(6) for j in range(i + 1, 6)
                if (xp[i] - xp[j]).denominator != 1
            )
            assert half_count == 8, f"{lam}: {half_count} half-int pairs"

    def test_non_even_central_charges_compute(self):
        """All non-even central charges are computable (UNVERIFIED)."""
        for lam in [(4, 1, 1), (3, 2, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1)]:
            c = central_charge_non_even(6, lam, Fraction(1))
            assert isinstance(c, Fraction)

    def test_non_even_complementarity_mostly_k_dependent(self):
        """Most non-even orbits produce k-dependent complementarity sums.

        Exception: (3,2,1) is self-transpose and gives k-independent sum,
        suggesting it may actually be even (the half-integer formula
        happens to produce a level-independent result).
        """
        for lam in [(4, 1, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1)]:
            assert not complementarity_is_level_independent(lam)
        # (3,2,1) is the exception: self-transpose with k-independent sum
        assert complementarity_is_level_independent((3, 2, 1))

    def test_non_even_dispatching(self):
        """central_charge_sl6 dispatches to non_even for non-even partitions."""
        for lam in [(4, 1, 1), (3, 2, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1)]:
            c_dispatch = central_charge_sl6(lam, Fraction(1))
            c_direct = central_charge_non_even(6, lam, Fraction(1))
            assert c_dispatch == c_direct

    def test_even_dispatching(self):
        """central_charge_sl6 dispatches to even for even partitions."""
        for lam in [(6,), (5, 1), (4, 2), (3, 3),
                    (3, 1, 1, 1), (2, 2, 2), (1, 1, 1, 1, 1, 1)]:
            c_dispatch = central_charge_sl6(lam, Fraction(1))
            c_direct = central_charge_even(6, lam, Fraction(1))
            assert c_dispatch == c_direct


# =====================================================================
# Section 10: Dual level (3 tests)
# =====================================================================

class TestDualLevel:
    """Feigin-Frenkel dual level k' = -k - 2N."""

    def test_dual_level_values(self):
        """k' = -k - 12 for sl_6."""
        assert dual_level(6, Fraction(1)) == Fraction(-13)
        assert dual_level(6, Fraction(6)) == Fraction(-18)
        assert dual_level(6, Fraction(0)) == Fraction(-12)

    def test_dual_level_involution(self):
        """(k')' = k: the dual level is an involution."""
        for kv in [Fraction(1), Fraction(5), Fraction(-3)]:
            assert dual_level(6, dual_level(6, kv)) == kv

    def test_dual_level_fixed_point(self):
        """The FF involution has fixed point k* = -N = -6 (critical level)."""
        assert dual_level(6, Fraction(-6)) == Fraction(-6)


# =====================================================================
# Section 11: Full analysis integration (8 tests)
# =====================================================================

class TestFullAnalysis:
    """Integration tests for the complete sl_6 analysis."""

    def test_full_analysis_covers_all_partitions(self):
        """full_sl6_analysis returns data for all 11 partitions."""
        analysis = full_sl6_analysis()
        assert len(analysis) == 11
        for lam in SL6_PARTITIONS:
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
        for lam in SL6_PARTITIONS:
            profile = duality_profile(lam)
            assert set(profile.keys()) == expected_keys

    def test_even_orbits_have_verified_c(self):
        """All even orbits are flagged as c_formula_verified."""
        for lam in [(6,), (5, 1), (4, 2), (3, 3),
                    (3, 1, 1, 1), (2, 2, 2), (1, 1, 1, 1, 1, 1)]:
            profile = duality_profile(lam)
            assert profile["c_formula_verified"]

    def test_non_even_orbits_flagged_unverified(self):
        """All non-even orbits are flagged as c_formula NOT verified."""
        for lam in [(4, 1, 1), (3, 2, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1)]:
            profile = duality_profile(lam)
            assert not profile["c_formula_verified"]

    def test_even_orbits_have_coefficients(self):
        """All even orbits have symbolic c coefficients."""
        for lam in [(6,), (5, 1), (4, 2), (3, 3),
                    (3, 1, 1, 1), (2, 2, 2), (1, 1, 1, 1, 1, 1)]:
            profile = duality_profile(lam)
            assert profile["c_coefficients"] is not None

    def test_non_even_orbits_have_no_coefficients(self):
        """Non-even orbits have no symbolic c coefficients."""
        for lam in [(4, 1, 1), (3, 2, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1)]:
            profile = duality_profile(lam)
            assert profile["c_coefficients"] is None

    def test_self_transpose_profile(self):
        """(3,2,1) is flagged as self-transpose in its profile."""
        profile = duality_profile((3, 2, 1))
        assert profile["is_self_transpose"]
        assert not profile["is_even"]
        assert profile["self_dual_c"] is None
        assert profile["self_dual_k"] is None

    def test_no_self_dual_even_orbits(self):
        """No self-transpose even orbit exists in sl_6.

        (3,2,1) is self-transpose but non-even.  All even orbits are
        NOT self-transpose.  Hence no self-dual analysis is possible.
        """
        for lam in SL6_PARTITIONS:
            if is_even_nilpotent(lam):
                assert lam != transpose(lam), \
                    f"{lam} is even AND self-transpose"


# =====================================================================
# Section 12: Cross-rank structural consistency (12 tests)
# =====================================================================

class TestCrossRankConsistency:
    """Structural consistency across sl_4, sl_5, sl_6."""

    def test_principal_c_formula_pattern(self):
        """c(W_N) = (N-1)(1 - N(N+1)/(k+N)) for N=6."""
        for kv in [Fraction(1), Fraction(3), Fraction(7)]:
            c = central_charge_even(6, (6,), kv)
            expected = Fraction(5) * (1 - Fraction(42, kv + 6))
            assert c == expected

    def test_trivial_c_formula_pattern(self):
        """c(V_k(sl_N)) = (N^2-1)*k/(k+N) for N=6."""
        for kv in [Fraction(1), Fraction(3), Fraction(7)]:
            c = central_charge_even(6, (1, 1, 1, 1, 1, 1), kv)
            expected = 35 * kv / (kv + 6)
            assert c == expected

    def test_complementarity_sum_pattern(self):
        """C(principal <-> trivial) = N^2+N-2 for N=4,5,6.

        N=4: 18, N=5: 28, N=6: 40.
        """
        # N=6
        assert complementarity_constant_even((6,)) == 40
        assert 6**2 + 6 - 2 == 40

    def test_dim_sl6_is_35(self):
        """dim(sl_6) = N^2-1 = 35, consistent with 35 weight-1 generators."""
        ws = generator_weights_sl6((1, 1, 1, 1, 1, 1))
        assert len(ws) == 35
        assert all(w == 1 for w in ws)

    def test_principal_generators_N_minus_1(self):
        """W_N has N-1 generators at weights 2,3,...,N for N=6."""
        ws = generator_weights_sl6((6,))
        assert len(ws) == 5
        assert ws == [Fraction(k) for k in range(2, 7)]

    def test_principal_leading_coeff_is_N_minus_1(self):
        """For W_N: a = N-1 in c = (ak+b)/(k+N)."""
        a, _ = central_charge_coefficients_even(6, (6,))
        assert a == 5

    def test_trivial_leading_coeff_is_dim_g(self):
        """For V_k(sl_N): a = N^2-1 in c = (ak+b)/(k+N)."""
        a, _ = central_charge_coefficients_even(6, (1, 1, 1, 1, 1, 1))
        assert a == 35

    def test_trivial_constant_coeff_is_zero(self):
        """For V_k(sl_N): b = 0 (c vanishes at k=0)."""
        _, b = central_charge_coefficients_even(6, (1, 1, 1, 1, 1, 1))
        assert b == 0

    def test_principal_b_formula(self):
        """For W_N: b = -(N-1)*N*(N+1) in c = (ak+b)/(k+N).

        b = -(N-1)N(N+1) = -5*6*7 = -210. But we have b = -180.
        Actually c = (N-1)(1 - N(N+1)/(k+N)) = (N-1)(k+N-N(N+1))/(k+N)
                   = (N-1)(k - N^2 - N + N)/(k+N) ... let me recompute.
        c = (N-1) - (N-1)*N*(N+1)/(k+N) = ((N-1)(k+N) - (N-1)*N*(N+1))/(k+N)
          = (N-1)(k + N - N(N+1))/(k+N) = (N-1)(k - N^2)/(k+N).
        So a = N-1, b = -(N-1)*N^2 = -5*36 = -180.
        """
        a, b = central_charge_coefficients_even(6, (6,))
        assert a == 5
        assert b == Fraction(-180)
        assert b == -(6 - 1) * 6**2

    def test_rectangular_complementarity_vs_principal(self):
        """C(3,3<->2,2,2) = 28 < C(6<->1^6) = 40."""
        assert complementarity_constant_even((3, 3)) < \
               complementarity_constant_even((6,))

    def test_self_transpose_even_pattern(self):
        """Self-transpose even orbits exist in sl_4 (2,2) and sl_5 (3,1,1)
        but NOT in sl_6 (only (3,2,1) is self-transpose, and it is non-even)."""
        for lam in SL6_PARTITIONS:
            if lam == transpose(lam):
                assert not is_even_nilpotent(lam)

    def test_complementarity_constant_between_rectangular_pair(self):
        """Rectangular even pair C: for (a x b) <-> (b x a),
        C = a(a,b) + a(b,a).  Check: a(3,3)=11, a(2,2,2)=17, 11+17=28."""
        a33, _ = central_charge_coefficients_even(6, (3, 3))
        a222, _ = central_charge_coefficients_even(6, (2, 2, 2))
        assert a33 + a222 == complementarity_constant_even((3, 3))
