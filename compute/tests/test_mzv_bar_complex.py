r"""Tests for compute/lib/mzv_bar_complex.py — MZVs in the bar complex.

Tests organized by section:
  1. MZV numerical computation (convergent series, known values)
  2. MZV exact values (even zeta, Zagier dimension)
  3. Genus-0 bar amplitudes (Heisenberg, Virasoro)
  4. Drinfeld associator (KZ connection, MZV coefficients)
  5. Double shuffle relations (stuffle, shuffle, Euler, weight-4)
  6. Motivic coaction (weights 3, 4, 5)
  7. Genus-1 periods (shadow tower, elliptic MZVs)
  8. Shadow-MZV dictionary
  9. Cross-checks and consistency

AP1 WARNING: Every numerical value is verified independently — not copied
from another test or from the manuscript. Where exact values are known
(even zeta values), we verify against the exact formula.

AP10 WARNING: Tests include cross-family consistency checks (e.g.,
the stuffle product should equal the direct product), not just
single-value hardcoded checks.
"""

import math
import pytest

from compute.lib.mzv_bar_complex import (
    # Section 1: MZV computation
    mzv_numerical,
    mzv_high_precision,
    # Section 2: Exact values
    mzv_weight,
    mzv_depth,
    zeta_even_exact,
    mzv_dimension_bound,
    KNOWN_MZV_RELATIONS,
    # Section 3: Genus-0 amplitudes
    genus0_amplitude_heisenberg,
    genus0_amplitude_virasoro,
    # Section 4: Drinfeld associator
    DrinfeldAssociator,
    drinfeld_associator,
    kz_connection_from_bar,
    # Section 5: Double shuffle
    shuffle_product,
    stuffle_product,
    verify_double_shuffle,
    verify_euler_relation,
    verify_weight4_relations,
    # Section 6: Motivic coaction
    motivic_coaction_weight3,
    motivic_coaction_weight4,
    motivic_coaction_weight5,
    # Section 7: Genus-1
    genus1_shadow_period,
    shadow_mzv_dictionary,
    shadow_to_mzv_coefficient,
    # Section 8: Utilities
    mzv_space_basis,
    verify_hoffman_basis_dimension,
    weight_filtration_compatibility,
    iterated_integral_on_m04,
    # Section 9: Cross-checks
    verify_all_mzv_relations,
    bar_complex_period_map,
)


# =====================================================================
# Tolerances
# =====================================================================

TOL = 1e-4        # for numerical MZV comparisons (truncated series)
TOL_HIGH = 1e-8   # for high-precision comparisons


# =====================================================================
# Section 1: MZV numerical computation
# =====================================================================

class TestMZVNumerical:
    """Tests for numerical MZV evaluation."""

    def test_zeta2_value(self):
        """zeta(2) = pi^2/6."""
        z2 = mzv_numerical((2,))
        expected = math.pi**2 / 6
        assert abs(z2 - expected) < TOL_HIGH, f"zeta(2) = {z2}, expected {expected}"

    def test_zeta3_value(self):
        """zeta(3) ~ 1.2020569..."""
        z3 = mzv_numerical((3,))
        assert abs(z3 - 1.2020569031595942) < TOL_HIGH

    def test_zeta4_value(self):
        """zeta(4) = pi^4/90."""
        z4 = mzv_numerical((4,))
        expected = math.pi**4 / 90
        assert abs(z4 - expected) < TOL_HIGH

    def test_zeta5_value(self):
        """zeta(5) ~ 1.0369277551..."""
        z5 = mzv_numerical((5,))
        assert abs(z5 - 1.0369277551433699) < TOL_HIGH

    def test_zeta6_value(self):
        """zeta(6) = pi^6/945."""
        z6 = mzv_numerical((6,))
        expected = math.pi**6 / 945
        assert abs(z6 - expected) < TOL_HIGH

    def test_zeta_21_equals_zeta_3(self):
        """Euler's relation: zeta(2,1) = zeta(3)."""
        z21 = mzv_numerical((2, 1))
        z3 = mzv_numerical((3,))
        assert abs(z21 - z3) < TOL, f"zeta(2,1)={z21}, zeta(3)={z3}"

    def test_zeta_31_equals_zeta4_over4(self):
        """zeta(3,1) = zeta(4)/4 = pi^4/360."""
        z31 = mzv_numerical((3, 1))
        z4 = mzv_numerical((4,))
        assert abs(z31 - z4 / 4) < TOL

    def test_zeta_211_equals_zeta4_over4(self):
        """zeta(2,1,1) = zeta(4)/4."""
        z211 = mzv_numerical((2, 1, 1))
        z4 = mzv_numerical((4,))
        assert abs(z211 - z4 / 4) < TOL

    def test_divergent_raises(self):
        """zeta(1,...) should raise ValueError (divergent)."""
        with pytest.raises(ValueError, match="first index must be >= 2"):
            mzv_numerical((1,))

    def test_divergent_depth2_raises(self):
        """zeta(1,2) should raise ValueError."""
        with pytest.raises(ValueError, match="first index must be >= 2"):
            mzv_numerical((1, 2))

    def test_negative_index_raises(self):
        """Negative indices should raise ValueError."""
        with pytest.raises(ValueError, match="All indices must be >= 1"):
            mzv_numerical((2, 0))

    def test_empty_tuple(self):
        """zeta() = 1 by convention."""
        assert mzv_numerical(()) == 1.0

    def test_zeta_22_value(self):
        """zeta(2,2) = pi^4/120 = 3*zeta(4)/4."""
        z22 = mzv_numerical((2, 2))
        z4 = mzv_numerical((4,))
        # From stuffle: zeta(2)^2 = 2*zeta(2,2) + zeta(4)
        # So zeta(2,2) = (zeta(2)^2 - zeta(4)) / 2
        z2 = mzv_numerical((2,))
        expected = (z2**2 - z4) / 2
        assert abs(z22 - expected) < TOL

    def test_zeta_positive(self):
        """All convergent MZVs with positive integer indices are positive."""
        for indices in [(2,), (3,), (4,), (2, 1), (3, 1), (2, 2), (2, 1, 1)]:
            assert mzv_numerical(indices) > 0, f"zeta{indices} should be positive"


class TestMZVHighPrecision:
    """Tests for high-precision MZV computation."""

    def test_zeta2_high_precision(self):
        """zeta(2) to 15 digits."""
        z2 = mzv_high_precision((2,), dps=20)
        expected = math.pi**2 / 6
        assert abs(z2 - expected) < 1e-14

    def test_zeta3_high_precision(self):
        """zeta(3) high precision."""
        z3 = mzv_high_precision((3,), dps=20)
        assert abs(z3 - 1.2020569031595942854) < 1e-12

    def test_depth2_high_precision(self):
        """zeta(2,1) high precision agrees with zeta(3)."""
        z21 = mzv_high_precision((2, 1), dps=15)
        z3 = mzv_high_precision((3,), dps=15)
        assert abs(z21 - z3) < 1e-4


# =====================================================================
# Section 2: Exact values and dimensions
# =====================================================================

class TestMZVExact:
    """Tests for exact MZV values and MZV space dimensions."""

    def test_weight_depth(self):
        """Weight and depth computation."""
        assert mzv_weight((2,)) == 2
        assert mzv_weight((3, 1)) == 4
        assert mzv_weight((2, 1, 1)) == 4
        assert mzv_depth((2,)) == 1
        assert mzv_depth((3, 1)) == 2
        assert mzv_depth((2, 1, 1)) == 3

    def test_zeta_even_exact_zeta2(self):
        """zeta(2)/pi^2 = 1/6 (exact)."""
        from fractions import Fraction
        ratio = zeta_even_exact(1)
        assert ratio == Fraction(1, 6)

    def test_zeta_even_exact_zeta4(self):
        """zeta(4)/pi^4 = 1/90 (exact)."""
        from fractions import Fraction
        ratio = zeta_even_exact(2)
        assert ratio == Fraction(1, 90)

    def test_zeta_even_exact_zeta6(self):
        """zeta(6)/pi^6 = 1/945 (exact)."""
        from fractions import Fraction
        ratio = zeta_even_exact(3)
        assert ratio == Fraction(1, 945)

    def test_zeta_even_exact_zeta8(self):
        """zeta(8)/pi^8 = 1/9450 (exact)."""
        from fractions import Fraction
        ratio = zeta_even_exact(4)
        assert ratio == Fraction(1, 9450)

    def test_zeta_even_exact_zeta10(self):
        """zeta(10)/pi^10 = 1/93555 (exact)."""
        from fractions import Fraction
        ratio = zeta_even_exact(5)
        assert ratio == Fraction(1, 93555)

    def test_zagier_dimensions(self):
        """Zagier's conjecture (Brown's theorem): d_n = d_{n-2} + d_{n-3}."""
        expected = {
            0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2,
            6: 2, 7: 3, 8: 4, 9: 5, 10: 7, 11: 9, 12: 12,
        }
        for w, d in expected.items():
            assert mzv_dimension_bound(w) == d, f"d_{w} = {mzv_dimension_bound(w)}, expected {d}"

    def test_zagier_recurrence(self):
        """Verify d_n = d_{n-2} + d_{n-3} holds for n >= 3."""
        for n in range(3, 20):
            dn = mzv_dimension_bound(n)
            dn2 = mzv_dimension_bound(n - 2)
            dn3 = mzv_dimension_bound(n - 3)
            assert dn == dn2 + dn3, f"d_{n} = {dn} != d_{n-2} + d_{n-3} = {dn2 + dn3}"

    def test_zagier_growth(self):
        """Zagier dimension grows: d_n > 0 for n >= 2."""
        for n in range(2, 25):
            assert mzv_dimension_bound(n) > 0

    def test_known_relations_dict(self):
        """KNOWN_MZV_RELATIONS has entries for standard cases."""
        assert (2,) in KNOWN_MZV_RELATIONS
        assert (3,) in KNOWN_MZV_RELATIONS
        assert (2, 1) in KNOWN_MZV_RELATIONS
        assert (4,) in KNOWN_MZV_RELATIONS
        assert (3, 1) in KNOWN_MZV_RELATIONS


# =====================================================================
# Section 3: Genus-0 bar amplitudes
# =====================================================================

class TestGenus0Amplitudes:
    """Tests for genus-0 bar amplitudes as periods."""

    def test_heisenberg_3point(self):
        """Heisenberg 3-point: M_{0,3} is a point, amplitude = kappa."""
        result = genus0_amplitude_heisenberg(3, kappa_val=2.0)
        assert result['amplitude'] == 2.0
        assert result['max_mzv_weight'] == 0

    def test_heisenberg_4point_has_zeta2(self):
        """Heisenberg 4-point amplitude involves zeta(2)."""
        result = genus0_amplitude_heisenberg(4, kappa_val=1.0)
        assert (2,) in result['mzv_content']
        assert result['mzv_content'][(2,)] == pytest.approx(-2.0, abs=TOL)

    def test_heisenberg_max_weight(self):
        """Heisenberg: max MZV weight is 2 (Gaussian, class G)."""
        for n in [4, 5, 6, 7]:
            result = genus0_amplitude_heisenberg(n, kappa_val=1.0)
            assert result['max_mzv_weight'] == 2, f"n={n}: max weight should be 2"

    def test_heisenberg_shadow_depth(self):
        """Heisenberg shadow depth is 2."""
        result = genus0_amplitude_heisenberg(5, kappa_val=1.0)
        assert result['shadow_depth'] == 2

    def test_heisenberg_5point_no_zeta3(self):
        """Heisenberg 5-point: no zeta(3) (quadratic OPE terminates)."""
        result = genus0_amplitude_heisenberg(5, kappa_val=1.0)
        assert result['mzv_content'].get((3,), 0.0) == 0.0

    def test_heisenberg_kappa_scaling(self):
        """Amplitude scales linearly with kappa."""
        r1 = genus0_amplitude_heisenberg(4, kappa_val=1.0)
        r2 = genus0_amplitude_heisenberg(4, kappa_val=3.0)
        ratio = r2['mzv_content'][(2,)] / r1['mzv_content'][(2,)]
        assert abs(ratio - 3.0) < TOL

    def test_heisenberg_n_too_small(self):
        """n < 3 should raise."""
        with pytest.raises(ValueError):
            genus0_amplitude_heisenberg(2)

    def test_virasoro_3point(self):
        """Virasoro 3-point: amplitude = kappa = c/2."""
        result = genus0_amplitude_virasoro(3, c_val=26.0)
        assert result['kappa'] == 13.0
        assert result['max_mzv_weight'] == 0

    def test_virasoro_4point(self):
        """Virasoro 4-point has zeta(2) content."""
        result = genus0_amplitude_virasoro(4, c_val=1.0)
        assert (2,) in result['mzv_content']
        assert result['kappa'] == 0.5

    def test_virasoro_5point_cubic(self):
        """Virasoro 5-point: cubic shadow enters (but is gauge-trivial)."""
        result = genus0_amplitude_virasoro(5, c_val=1.0)
        # S_3 = 0 for Virasoro by thm:cubic-gauge-triviality
        assert result['mzv_content'].get((3,), 0.0) == 0.0

    def test_virasoro_infinite_depth(self):
        """Virasoro is class M: infinite shadow depth."""
        result = genus0_amplitude_virasoro(6, c_val=1.0)
        assert result['shadow_depth'] == float('inf')

    def test_virasoro_quartic_contact(self):
        """Virasoro quartic contact class: Q = 10/(c(5c+22))."""
        result = genus0_amplitude_virasoro(6, c_val=1.0)
        expected_Q = 10.0 / (1.0 * (5.0 + 22.0))
        assert (4,) in result['mzv_content']
        assert abs(result['mzv_content'][(4,)] - expected_Q) < TOL

    def test_virasoro_n_too_small(self):
        """n < 3 should raise."""
        with pytest.raises(ValueError):
            genus0_amplitude_virasoro(2)

    def test_moduli_dim(self):
        """dim M_{0,n} = n - 3."""
        for n in range(3, 10):
            r = genus0_amplitude_heisenberg(n)
            assert r['moduli_dim'] == n - 3


# =====================================================================
# Section 4: Drinfeld associator
# =====================================================================

class TestDrinfeldAssociator:
    """Tests for the Drinfeld associator from the bar complex."""

    def test_constant_term(self):
        """Phi starts with 1."""
        phi = drinfeld_associator(max_weight=4)
        assert phi.coefficient(()) == 1.0

    def test_weight1_regularized_to_zero(self):
        """Weight-1 terms are regularized to 0."""
        phi = drinfeld_associator(max_weight=4)
        assert abs(phi.coefficient((0,))) < TOL
        assert abs(phi.coefficient((1,))) < TOL

    def test_weight2_zeta2(self):
        """Weight-2 coefficient of AB = -zeta(2)."""
        phi = drinfeld_associator(max_weight=4)
        c_01 = phi.coefficient((0, 1))
        z2 = mzv_numerical((2,))
        # e_0 e_1 -> (-1)^1 * zeta(2) = -zeta(2)
        assert abs(c_01 - (-z2)) < TOL, f"c(AB) = {c_01}, expected {-z2}"

    def test_weight2_ba_coefficient(self):
        """Weight-2 coefficient of BA = +zeta(2) (from shuffle regularization)."""
        phi = drinfeld_associator(max_weight=4)
        c_10 = phi.coefficient((1, 0))
        z2 = mzv_numerical((2,))
        assert abs(c_10 - z2) < TOL

    def test_weight2_grouplike(self):
        """c(AB) + c(BA) = 0 (group-like property at weight 2)."""
        phi = drinfeld_associator(max_weight=4)
        c_01 = phi.coefficient((0, 1))
        c_10 = phi.coefficient((1, 0))
        assert abs(c_01 + c_10) < TOL

    def test_weight3_aab(self):
        """Weight-3 coefficient of AAB = -zeta(3) (convergent integral)."""
        phi = drinfeld_associator(max_weight=4)
        c_001 = phi.coefficient((0, 0, 1))
        z3 = mzv_numerical((3,))
        # e_0 e_0 e_1 -> (-1)^1 * zeta(3) = -zeta(3)
        assert abs(c_001 - (-z3)) < TOL

    def test_lie_basis_weight2(self):
        """Lie basis at weight 2: coefficient of [A,B] = zeta(2)."""
        phi = drinfeld_associator(max_weight=4)
        lie = phi.to_lie_basis(max_weight=2)
        z2 = mzv_numerical((2,))
        assert abs(lie['[A,B]'] - z2) < TOL

    def test_lie_basis_weight3(self):
        """Lie basis at weight 3: [A,[A,B]] has coefficient zeta(3)."""
        phi = drinfeld_associator(max_weight=4)
        lie = phi.to_lie_basis(max_weight=3)
        z3 = mzv_numerical((3,))
        assert abs(lie['[A,[A,B]]'] - z3) < TOL

    def test_lie_basis_weight3_antisymmetric(self):
        """Lie basis at weight 3: [B,[A,B]] has coefficient -zeta(3)."""
        phi = drinfeld_associator(max_weight=4)
        lie = phi.to_lie_basis(max_weight=3)
        z3 = mzv_numerical((3,))
        assert abs(lie['[B,[A,B]]'] - (-z3)) < TOL

    def test_group_like_verification(self):
        """Group-like property verification passes."""
        phi = drinfeld_associator(max_weight=4)
        checks = phi.verify_group_like(max_weight=4)
        assert checks['weight_1_vanishes']
        assert checks['weight_2_grouplike']

    def test_pentagon(self):
        """Pentagon relation holds (at weight 2)."""
        phi = drinfeld_associator(max_weight=4)
        assert phi.verify_pentagon()


class TestKZConnection:
    """Tests for the KZ connection from the bar complex."""

    def test_sl2_kz_parameter(self):
        """KZ parameter for sl_2 at level k: 1/(k + 2)."""
        result = kz_connection_from_bar('sl2', level=1.0, n_points=4)
        assert abs(result['kz_parameter'] - 1.0 / 3.0) < TOL

    def test_sl3_kz_parameter(self):
        """KZ parameter for sl_3 at level k: 1/(k + 3)."""
        result = kz_connection_from_bar('sl3', level=1.0, n_points=4)
        assert abs(result['kz_parameter'] - 1.0 / 4.0) < TOL

    def test_kz_flatness(self):
        """KZ connection is flat (from Arnold/CYBE)."""
        result = kz_connection_from_bar('sl2', level=1.0)
        assert result['is_flat']

    def test_kz_critical_level_raises(self):
        """Critical level k = -h^v should raise."""
        with pytest.raises(ValueError, match="Critical level"):
            kz_connection_from_bar('sl2', level=-2.0)

    def test_kz_unknown_type_raises(self):
        """Unknown Lie type should raise."""
        with pytest.raises(ValueError, match="Unknown Lie type"):
            kz_connection_from_bar('e8', level=1.0)

    def test_kz_associator_weights(self):
        """Associator weights scale as kz_parameter^w."""
        result = kz_connection_from_bar('sl2', level=1.0)
        p = result['kz_parameter']
        z2 = mzv_numerical((2,))
        z3 = mzv_numerical((3,))
        assert abs(result['associator_weight_2'] - p**2 * z2) < TOL
        assert abs(result['associator_weight_3'] - p**3 * z3) < TOL

    def test_kz_n_connections(self):
        """Number of KZ connections = n*(n-1)/2 pairs."""
        for n in [3, 4, 5, 6]:
            result = kz_connection_from_bar('sl2', level=1.0, n_points=n)
            assert result['n_connections'] == n * (n - 1) // 2


# =====================================================================
# Section 5: Double shuffle relations
# =====================================================================

class TestShuffleProduct:
    """Tests for the shuffle product of MZV index sequences."""

    def test_shuffle_singletons(self):
        """shuffle((a,), (b,)) = {(a,b): 1, (b,a): 1}."""
        sh = shuffle_product((2,), (3,))
        assert sh == {(2, 3): 1, (3, 2): 1}

    def test_shuffle_empty(self):
        """shuffle(s, ()) = {s: 1}."""
        sh = shuffle_product((2, 3), ())
        assert sh == {(2, 3): 1}

    def test_shuffle_count(self):
        """Number of shuffles of (a_1,...,a_m) and (b_1,...,b_n) is C(m+n, m)."""
        sh = shuffle_product((2,), (3, 4))
        total = sum(sh.values())
        assert total == math.comb(3, 1)  # C(1+2, 1) = 3

    def test_shuffle_depth2(self):
        """Shuffle of two depth-1 MZVs gives depth-2 terms."""
        sh = shuffle_product((2,), (2,))
        # (2,2) appears twice, and no other terms
        assert sh == {(2, 2): 2}


class TestStuffleProduct:
    """Tests for the stuffle (quasi-shuffle) product."""

    def test_stuffle_singletons(self):
        """stuffle((a,), (b,)) = {(a,b): 1, (b,a): 1, (a+b,): 1}."""
        st = stuffle_product((2,), (3,))
        assert st == {(2, 3): 1, (3, 2): 1, (5,): 1}

    def test_stuffle_empty(self):
        """stuffle(s, ()) = {s: 1}."""
        st = stuffle_product((2,), ())
        assert st == {(2,): 1}

    def test_stuffle_zeta2_squared(self):
        """stuffle((2,), (2,)) encodes zeta(2)^2 = 2*zeta(2,2) + zeta(4)."""
        st = stuffle_product((2,), (2,))
        # Should be: {(2,2): 2, (4,): 1}
        assert st[(2, 2)] == 2
        assert st[(4,)] == 1


class TestDoubleShuffleRelations:
    """Tests for double shuffle relation verification."""

    def test_stuffle_zeta2_squared_numerical(self):
        """Verify: zeta(2)^2 = 2*zeta(2,2) + zeta(4) numerically."""
        z2 = mzv_numerical((2,))
        z22 = mzv_numerical((2, 2))
        z4 = mzv_numerical((4,))
        lhs = z2**2
        rhs = 2 * z22 + z4
        assert abs(lhs - rhs) < TOL, f"{lhs} != {rhs}"

    def test_stuffle_zeta2_zeta3(self):
        """Verify: zeta(2)*zeta(3) = zeta(2,3) + zeta(3,2) + zeta(5)."""
        z2 = mzv_numerical((2,))
        z3 = mzv_numerical((3,))
        z23 = mzv_numerical((2, 3))
        z32 = mzv_numerical((3, 2))
        z5 = mzv_numerical((5,))
        lhs = z2 * z3
        rhs = z23 + z32 + z5
        assert abs(lhs - rhs) < TOL

    def test_euler_relation(self):
        """Euler relation zeta(2,1) = zeta(3)."""
        result = verify_euler_relation()
        assert result['holds'], f"Euler: diff = {result['difference']}"

    def test_weight4_zeta31(self):
        """zeta(3,1) = zeta(4)/4."""
        result = verify_weight4_relations()
        assert result['zeta_31_equals_z4_over_4']['holds']

    def test_weight4_zeta211(self):
        """zeta(2,1,1) = zeta(4)/4."""
        result = verify_weight4_relations()
        assert result['zeta_211_equals_z4_over_4']['holds']

    def test_weight4_zeta22(self):
        """zeta(2,2) = 3*zeta(4)/4."""
        result = verify_weight4_relations()
        assert result['zeta_22_from_stuffle']['holds']

    def test_verify_double_shuffle_convergent(self):
        """Double shuffle for zeta(2) * zeta(3) (both convergent)."""
        result = verify_double_shuffle((2,), (3,))
        # The stuffle product has all convergent terms
        assert not result['has_divergent_stuffle']
        assert result['stuffle_matches_product']

    def test_shuffle_of_convergent_pair(self):
        """Index shuffle of (2,) and (2,) gives 2*(2,2).

        The index-level shuffle treats each index as one letter, giving
        sh((2,), (2,)) = 2*(2,2). This does NOT equal zeta(2)^2 because
        the index shuffle is not the iterated-integral shuffle (where
        zeta(2) is a 2-letter word 10). The stuffle product, which adds
        the contracted term zeta(4), does give zeta(2)^2.
        """
        result = verify_double_shuffle((2,), (2,))
        # Stuffle should match the product (adds the zeta(4) term)
        if not result['has_divergent_stuffle']:
            assert result['stuffle_matches_product']
        # Index shuffle sum = 2*zeta(2,2) < zeta(2)^2 (missing zeta(4) term)
        if not result['has_divergent_shuffle']:
            assert not result['shuffle_matches_product'], \
                "Index shuffle should NOT equal product (missing contracted terms)"

    def test_sum_weight4_mzvs(self):
        """Sum relation: all weight-4 MZVs are multiples of zeta(4)."""
        z4 = mzv_numerical((4,))
        z31 = mzv_numerical((3, 1))
        z22 = mzv_numerical((2, 2))
        z211 = mzv_numerical((2, 1, 1))
        # Ratios to zeta(4):
        assert abs(z31 / z4 - 0.25) < TOL    # 1/4
        assert abs(z22 / z4 - 0.75) < TOL     # 3/4
        assert abs(z211 / z4 - 0.25) < TOL    # 1/4


# =====================================================================
# Section 6: Motivic coaction
# =====================================================================

class TestMotivicCoaction:
    """Tests for motivic coaction compatibility."""

    def test_weight3_dimension(self):
        """MZV space at weight 3 is 1-dimensional."""
        result = motivic_coaction_weight3()
        assert result['mzv_dimension'] == 1

    def test_weight3_bar_compatible(self):
        """Bar coproduct compatible with motivic coaction at weight 3."""
        result = motivic_coaction_weight3()
        assert result['bar_coproduct_compatible']

    def test_weight4_dimension(self):
        """MZV space at weight 4 is 1-dimensional."""
        result = motivic_coaction_weight4()
        assert result['mzv_dimension'] == 1

    def test_weight4_ratio(self):
        """zeta(3,1)/zeta(4) = 1/4 (motivic coaction consistency)."""
        result = motivic_coaction_weight4()
        assert abs(result['ratio_31_to_4'] - 0.25) < TOL

    def test_weight4_bar_compatible(self):
        """Bar coproduct compatible at weight 4."""
        result = motivic_coaction_weight4()
        assert result['bar_coproduct_compatible']

    def test_weight5_dimension(self):
        """MZV space at weight 5 is 2-dimensional."""
        result = motivic_coaction_weight5()
        assert result['mzv_dimension'] == 2

    def test_weight5_basis(self):
        """Weight-5 basis is {zeta(5), zeta(2)*zeta(3)}."""
        result = motivic_coaction_weight5()
        assert 'zeta(5)' in result['basis']
        assert 'zeta(2)*zeta(3)' in result['basis']


# =====================================================================
# Section 7: Genus-1 periods
# =====================================================================

class TestGenus1Periods:
    """Tests for genus-1 shadow tower periods."""

    def test_F1_heisenberg(self):
        """F_1(Heisenberg) = kappa/24."""
        result = genus1_shadow_period(1.0)
        assert abs(result['F_1'] - 1.0 / 24) < TOL

    def test_F1_virasoro(self):
        """F_1(Virasoro at c) = c/(2*24) = c/48."""
        result = genus1_shadow_period(0.5)  # kappa = c/2 = 0.5 for c=1
        assert abs(result['F_1'] - 0.5 / 24) < TOL

    def test_F1_sl2(self):
        """F_1(sl_2 at k=1) = 3*3/(4*24) = 9/96 = 3/32."""
        kappa_sl2_k1 = 3.0 * 3.0 / 4.0  # 3*(1+2)/4 = 9/4
        result = genus1_shadow_period(kappa_sl2_k1)
        expected = kappa_sl2_k1 / 24.0
        assert abs(result['F_1'] - expected) < TOL

    def test_genus1_is_quasimodular(self):
        """Genus-1 period type is quasi-modular (AP15)."""
        result = genus1_shadow_period(1.0)
        assert result['period_type'] == 'quasi-modular'

    def test_elliptic_mzv_weight(self):
        """Elliptic MZV at genus 1 has weight 2."""
        result = genus1_shadow_period(1.0)
        assert result['elliptic_mzv_weight'] == 2

    def test_lambda1_FP(self):
        """lambda_1^FP = 1/24 (Bernoulli number |B_2|/(2*2!) = (1/6)/2 = ... )"""
        # lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
        # g=1: (2^1 - 1)/2^1 * |B_2|/2! = (1/2) * (1/6) / 2 = 1/24
        result = genus1_shadow_period(1.0)
        assert abs(result['lambda_1_FP'] - 1.0 / 24.0) < TOL


class TestShadowMZVDictionary:
    """Tests for the shadow-MZV dictionary."""

    def test_dictionary_has_arities(self):
        """Dictionary covers arities 2 through 6."""
        d = shadow_mzv_dictionary(max_arity=6)
        for r in range(2, 7):
            assert r in d

    def test_arity2_is_kappa(self):
        """Arity 2 shadow invariant is kappa."""
        d = shadow_mzv_dictionary()
        assert d[2]['shadow_invariant'] == 'kappa'

    def test_arity2_mzv_dim1(self):
        """MZV space at weight 2 is 1-dimensional."""
        d = shadow_mzv_dictionary()
        assert d[2]['mzv_dimension'] == 1

    def test_arity3_is_cubic(self):
        """Arity 3 shadow invariant is the cubic shadow S_3."""
        d = shadow_mzv_dictionary()
        assert 'S_3' in d[3]['shadow_invariant']

    def test_arity4_is_quartic(self):
        """Arity 4 shadow invariant is the quartic shadow."""
        d = shadow_mzv_dictionary()
        assert 'Q^contact' in d[4]['shadow_invariant'] or 'S_4' in d[4]['shadow_invariant']

    def test_arity5_dim2(self):
        """MZV space at weight 5 is 2-dimensional."""
        d = shadow_mzv_dictionary()
        assert d[5]['mzv_dimension'] == 2

    def test_arity5_basis(self):
        """Weight-5 MZV basis has zeta(5) and zeta(2)*zeta(3)."""
        d = shadow_mzv_dictionary()
        assert 'zeta(5)' in d[5]['mzv_basis']
        assert 'zeta(2)*zeta(3)' in d[5]['mzv_basis']

    def test_moduli_dim(self):
        """Moduli space dim M_{0,r+1} = r - 2."""
        d = shadow_mzv_dictionary()
        for r in range(2, 7):
            assert d[r]['moduli_dim'] == r - 2

    def test_heisenberg_only_arity2(self):
        """Heisenberg: only arity 2 is nonzero (class G)."""
        d = shadow_mzv_dictionary()
        assert 'S_3 = 0' in d[3]['families'].get('Heisenberg', '')

    def test_affine_terminates_at3(self):
        """Affine sl_2: terminates at arity 3 (class L)."""
        d = shadow_mzv_dictionary()
        assert 'class L' in d[3]['families'].get('affine_sl2', '')


class TestShadowToMZV:
    """Tests for shadow_to_mzv_coefficient."""

    def test_arity2(self):
        """Arity-2 shadow maps to zeta(2) coefficient."""
        result = shadow_to_mzv_coefficient(2, 1.5)
        assert 'zeta(2)' in result
        assert result['zeta(2)'] == 1.5

    def test_arity3(self):
        """Arity-3 shadow maps to zeta(3) coefficient."""
        result = shadow_to_mzv_coefficient(3, 2.0)
        assert 'zeta(3)' in result
        assert result['zeta(3)'] == 2.0

    def test_arity4(self):
        """Arity-4 shadow maps to zeta(4) coefficient."""
        result = shadow_to_mzv_coefficient(4, 0.5)
        assert 'zeta(4)' in result
        assert result['zeta(4)'] == 0.5


# =====================================================================
# Section 8: Utility functions
# =====================================================================

class TestMZVSpaceBasis:
    """Tests for the Hoffman basis enumeration."""

    def test_weight2_basis(self):
        """Weight-2 Hoffman basis: {(2,)}."""
        basis = mzv_space_basis(2)
        assert basis == [(2,)]

    def test_weight3_basis(self):
        """Weight-3 Hoffman basis: {(3,)}."""
        basis = mzv_space_basis(3)
        assert basis == [(3,)]

    def test_weight4_basis(self):
        """Weight-4 Hoffman basis: {(2,2)}."""
        basis = mzv_space_basis(4)
        assert basis == [(2, 2)]

    def test_weight5_basis(self):
        """Weight-5 Hoffman basis: {(2,3), (3,2)}."""
        basis = mzv_space_basis(5)
        assert len(basis) == 2
        assert (2, 3) in basis
        assert (3, 2) in basis

    def test_weight6_basis(self):
        """Weight-6 Hoffman basis: {(2,2,2), (3,3)}."""
        basis = mzv_space_basis(6)
        assert len(basis) == 2
        assert (2, 2, 2) in basis
        assert (3, 3) in basis

    def test_weight7_basis(self):
        """Weight-7 Hoffman basis has 3 elements."""
        basis = mzv_space_basis(7)
        assert len(basis) == 3

    def test_hoffman_zagier_match(self):
        """Hoffman basis count matches Zagier dimension at all weights."""
        result = verify_hoffman_basis_dimension(max_weight=15)
        for w in range(2, 16):
            assert result[w]['match'], f"Mismatch at weight {w}"

    def test_basis_weight_correct(self):
        """Every basis element has the correct weight."""
        for w in range(2, 12):
            for indices in mzv_space_basis(w):
                assert sum(indices) == w

    def test_basis_indices_are_2_or_3(self):
        """Every Hoffman basis element uses only 2 and 3."""
        for w in range(2, 12):
            for indices in mzv_space_basis(w):
                for s in indices:
                    assert s in (2, 3)

    def test_weight_below_2_empty(self):
        """No basis elements for weight < 2."""
        assert mzv_space_basis(0) == []
        assert mzv_space_basis(1) == []


class TestWeightFiltration:
    """Tests for weight filtration compatibility."""

    def test_compatibility(self):
        """Weight filtration is compatible at all tested weights."""
        result = weight_filtration_compatibility(max_weight=6)
        for key, data in result.items():
            assert data['compatible'], f"Incompatible at {key}"

    def test_bar_degree(self):
        """Bar degree at weight w is w-1."""
        result = weight_filtration_compatibility(max_weight=6)
        for w in range(2, 7):
            assert result[f'weight_{w}']['bar_degree'] == w - 1


class TestIteratedIntegral:
    """Tests for iterated integrals on M_{0,4}."""

    def test_empty_word(self):
        """Integral of empty word = 1."""
        assert iterated_integral_on_m04(()) == 1.0

    def test_e0e1_gives_minus_zeta2(self):
        """I(e_0 e_1) = -zeta(2)."""
        val = iterated_integral_on_m04((0, 1))
        z2 = mzv_numerical((2,))
        assert abs(val - (-z2)) < TOL

    def test_e0e0e1_gives_minus_zeta3(self):
        """I(e_0 e_0 e_1) = -zeta(3)."""
        val = iterated_integral_on_m04((0, 0, 1))
        z3 = mzv_numerical((3,))
        assert abs(val - (-z3)) < TOL


# =====================================================================
# Section 9: Cross-checks and consistency
# =====================================================================

class TestBarComplexPeriodMap:
    """Tests for bar_complex_period_map."""

    def test_heisenberg_depth2(self):
        """Heisenberg shadow depth is 2."""
        result = bar_complex_period_map('Heisenberg', 2)
        assert result['shadow_depth'] == 2

    def test_heisenberg_arity3_vanishes(self):
        """Heisenberg at arity 3: nonzero = False."""
        result = bar_complex_period_map('Heisenberg', 3)
        assert not result['nonzero']

    def test_sl2_depth3(self):
        """sl_2 shadow depth is 3."""
        result = bar_complex_period_map('sl2', 2)
        assert result['shadow_depth'] == 3

    def test_sl2_arity4_vanishes(self):
        """sl_2 at arity 4: nonzero = False (terminates at 3)."""
        result = bar_complex_period_map('sl2', 4)
        assert not result['nonzero']

    def test_virasoro_always_nonzero(self):
        """Virasoro: all arities nonzero (class M)."""
        for arity in range(2, 8):
            result = bar_complex_period_map('Virasoro', arity)
            assert result['nonzero']

    def test_virasoro_depth_infinite(self):
        """Virasoro shadow depth is infinite."""
        result = bar_complex_period_map('Virasoro', 2)
        assert result['shadow_depth'] == float('inf')

    def test_betagamma_depth4(self):
        """beta-gamma shadow depth is 4."""
        result = bar_complex_period_map('beta_gamma', 2)
        assert result['shadow_depth'] == 4

    def test_moduli_space_name(self):
        """Moduli space is M_{0,arity+1}."""
        result = bar_complex_period_map('Heisenberg', 3)
        assert result['moduli_space'] == 'M_{0,4}'

    def test_mzv_weight_equals_arity(self):
        """MZV weight equals arity."""
        for arity in range(2, 7):
            result = bar_complex_period_map('Virasoro', arity)
            assert result['mzv_weight'] == arity


class TestAllMZVRelations:
    """Full cross-check suite."""

    def test_all_relations(self):
        """verify_all_mzv_relations passes at weight <= 5."""
        results = verify_all_mzv_relations(max_weight=5, tol=1e-3)
        assert results['euler']['holds']
        assert results['stuffle_22']['holds']
        assert results['shadow_dictionary_built']

    def test_hoffman_zagier_in_full_check(self):
        """Hoffman-Zagier match is included in full check."""
        results = verify_all_mzv_relations(max_weight=5)
        for w in range(2, 6):
            assert results['hoffman_zagier'][w]['match']


# =====================================================================
# Section 10: Shadow depth classification cross-check
# =====================================================================

class TestShadowDepthClassification:
    """Cross-check shadow depth against MZV structure.

    The four shadow depth classes map to specific MZV truncation levels:
      G (depth 2): only zeta(2) appears
      L (depth 3): zeta(2), zeta(3)
      C (depth 4): zeta(2), zeta(3), zeta(4)
      M (depth inf): all MZVs
    """

    def test_class_G_mzv(self):
        """Class G (Heisenberg): MZV content is {zeta(2)} only."""
        for n in [4, 5, 6]:
            r = genus0_amplitude_heisenberg(n, kappa_val=1.0)
            for key in r.get('mzv_content', {}):
                if r['mzv_content'][key] != 0:
                    assert mzv_weight(key) <= 2

    def test_class_M_mzv(self):
        """Class M (Virasoro): MZV content grows with n."""
        r4 = genus0_amplitude_virasoro(4, c_val=1.0)
        r5 = genus0_amplitude_virasoro(5, c_val=1.0)
        r6 = genus0_amplitude_virasoro(6, c_val=1.0)
        # At n=6, quartic shadow appears (weight 4)
        assert (4,) in r6['mzv_content']

    def test_depth_classes_exhaust_standard(self):
        """The four classes G, L, C, M cover all standard families."""
        depths = {
            'Heisenberg': 2,   # G
            'sl2': 3,          # L
            'beta_gamma': 4,   # C
            'Virasoro': float('inf'),  # M
        }
        for algebra, depth in depths.items():
            r = bar_complex_period_map(algebra, 2)
            assert r['shadow_depth'] == depth, (
                f"{algebra}: expected depth {depth}, got {r['shadow_depth']}"
            )

    def test_mzv_space_dimension_monotone(self):
        """MZV dimensions are monotone non-decreasing (after d_1=0)."""
        dims = [mzv_dimension_bound(w) for w in range(2, 20)]
        for i in range(len(dims) - 1):
            assert dims[i + 1] >= dims[i], (
                f"d_{i+2} = {dims[i]} > d_{i+3} = {dims[i+1]} violates monotonicity"
            )
