"""Tests for Swiss-cheese wheel diagrams and shadow depth classification.

Verifies:
  - Wheel diagram combinatorics (loop count, internal edges, symmetry factors)
  - Wheel coefficient computation for all standard families
  - Transferred A-infinity operation m_k detection for all families
  - Shadow depth classification (G/L/C/M) for all families
  - Cross-validation with shadow_metric_census.py
  - Virasoro-specific computations (recursive tower, known values, nonvanishing)
  - Swiss-cheese factorization data

KEY MATHEMATICAL FACTS VERIFIED:
  - Heisenberg: m_k = 0 for k >= 3 (class G, depth 2)
  - Affine sl_2: m_3 != 0, m_k = 0 for k >= 4 (class L, depth 3)
  - betagamma: m_3 = 0, m_4 != 0, m_k = 0 for k >= 5 (class C, depth 4)
  - Virasoro: m_k != 0 for ALL k >= 2 (class M, infinite depth)

References:
  - def:shadow-depth-classification in higher_genus_modular_koszul.tex
  - thm:shadow-archetype-classification in higher_genus_modular_koszul.tex
  - shadow_metric_census.py for G/L/C/M classification
  - virasoro_shadow_gf.py for Virasoro shadow obstruction tower data
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, cancel, factor, simplify

from compute.lib.swiss_cheese_virasoro_wheels import (
    WheelDiagram,
    loop_count,
    wheel_internal_edges,
    wheel_symmetry_factor,
    enumerate_wheels,
    count_wheel_diagrams,
    wheel_coefficient_heisenberg,
    wheel_coefficient_affine,
    wheel_coefficient_betagamma,
    wheel_coefficient_virasoro,
    transferred_mk,
    shadow_depth_from_wheels,
    classify_depth,
    verify_depth_classification,
    virasoro_wheel_coefficients,
    virasoro_wheel_nonvanishing,
    virasoro_pole_check,
    verify_known_virasoro_coefficients,
    swiss_cheese_direction_data,
    depth_decomposition,
    _virasoro_shadow_coefficient,
    _heisenberg_shadow_coefficients,
    _affine_sl2_shadow_coefficients,
    _betagamma_shadow_coefficients,
    _DEPTH_TABLE,
    KNOWN_VIRASORO_COEFFICIENTS,
    c,
)


# ============================================================
# TestWheelCombinatorics: graph-theoretic properties
# ============================================================

class TestWheelCombinatorics:
    """Verify wheel diagram combinatorial properties."""

    def test_loop_count_n3(self):
        """Wheel with 3 legs has 1 loop (triangle)."""
        assert loop_count(3) == 1

    def test_loop_count_n4(self):
        """Wheel with 4 legs has 1 loop (square)."""
        assert loop_count(4) == 1

    def test_loop_count_n5(self):
        """Wheel with 5 legs has 1 loop (pentagon)."""
        assert loop_count(5) == 1

    def test_loop_count_n10(self):
        """Wheel with 10 legs has 1 loop."""
        assert loop_count(10) == 1

    def test_loop_count_n100(self):
        """Wheel with 100 legs has 1 loop."""
        assert loop_count(100) == 1

    def test_loop_count_n2_raises(self):
        """n < 3 is invalid for wheel diagrams."""
        with pytest.raises(ValueError):
            loop_count(2)

    def test_loop_count_n1_raises(self):
        with pytest.raises(ValueError):
            loop_count(1)

    def test_internal_edges_n3(self):
        """Triangle wheel: 3 internal edges."""
        assert wheel_internal_edges(3) == 3

    def test_internal_edges_n4(self):
        """Square wheel: 4 internal edges."""
        assert wheel_internal_edges(4) == 4

    def test_internal_edges_n7(self):
        """Heptagonal wheel: 7 internal edges."""
        assert wheel_internal_edges(7) == 7

    def test_internal_edges_n2_raises(self):
        with pytest.raises(ValueError):
            wheel_internal_edges(2)

    def test_symmetry_factor_n3(self):
        """Symmetry factor 1/6 for triangle wheel."""
        assert wheel_symmetry_factor(3) == Fraction(1, 6)

    def test_symmetry_factor_n4(self):
        """Symmetry factor 1/8 for square wheel."""
        assert wheel_symmetry_factor(4) == Fraction(1, 8)

    def test_symmetry_factor_n5(self):
        """Symmetry factor 1/10 for pentagon wheel."""
        assert wheel_symmetry_factor(5) == Fraction(1, 10)

    def test_symmetry_factor_n6(self):
        """Symmetry factor 1/12 for hexagon wheel."""
        assert wheel_symmetry_factor(6) == Fraction(1, 12)

    def test_symmetry_factor_decreases(self):
        """Symmetry factors decrease as 1/(2n)."""
        for n in range(3, 20):
            assert wheel_symmetry_factor(n) == Fraction(1, 2 * n)


class TestWheelEnumeration:
    """Verify wheel diagram enumeration."""

    def test_no_wheels_n0(self):
        assert enumerate_wheels(0) == []

    def test_no_wheels_n1(self):
        assert enumerate_wheels(1) == []

    def test_no_wheels_n2(self):
        assert enumerate_wheels(2) == []

    def test_one_wheel_n3(self):
        wheels = enumerate_wheels(3)
        assert len(wheels) == 1
        assert wheels[0].n_external == 3
        assert wheels[0].n_internal_edges == 3
        assert wheels[0].loop_number == 1

    def test_one_wheel_n4(self):
        wheels = enumerate_wheels(4)
        assert len(wheels) == 1
        assert wheels[0].n_external == 4

    def test_one_wheel_n10(self):
        wheels = enumerate_wheels(10)
        assert len(wheels) == 1

    def test_count_n2(self):
        assert count_wheel_diagrams(2) == 0

    def test_count_n3(self):
        assert count_wheel_diagrams(3) == 1

    def test_count_n50(self):
        assert count_wheel_diagrams(50) == 1

    def test_wheel_dataclass_defaults(self):
        w = WheelDiagram(n_external=5, n_internal_edges=5)
        assert w.loop_number == 1
        assert w.symmetry_factor == Fraction(1, 10)
        assert w.coefficient is None


# ============================================================
# TestHeisenberg: Gaussian class G, depth 2
# ============================================================

class TestHeisenberg:
    """Heisenberg algebra: class G (Gaussian), r_max = 2.

    The Heisenberg algebra has purely quadratic OPE: J(z)J(w) ~ k/(z-w)^2.
    All m_k for k >= 3 vanish.
    """

    def test_m2_nonzero(self):
        """m_2 = kappa = k (always nonzero)."""
        coeff = wheel_coefficient_heisenberg(2, level=1)
        assert coeff == Rational(1)

    def test_m2_level_k(self):
        """m_2 = k at level k."""
        for kk in [1, 2, 5, 10]:
            coeff = wheel_coefficient_heisenberg(2, level=kk)
            assert coeff == Rational(kk)

    def test_m3_zero(self):
        """m_3 = 0 (Gaussian class)."""
        assert wheel_coefficient_heisenberg(3) == 0

    def test_m4_zero(self):
        assert wheel_coefficient_heisenberg(4) == 0

    def test_m5_zero(self):
        assert wheel_coefficient_heisenberg(5) == 0

    def test_m10_zero(self):
        assert wheel_coefficient_heisenberg(10) == 0

    def test_all_higher_zero(self):
        """All m_k = 0 for k >= 3, up to arity 20."""
        for kk in range(3, 21):
            assert wheel_coefficient_heisenberg(kk) == 0

    def test_shadow_coefficients(self):
        """Shadow coefficients: S_2 = 1 (at k=1), S_r = 0 for r >= 3."""
        coeffs = _heisenberg_shadow_coefficients(10, level_val=1)
        assert coeffs[2] == Rational(1)
        for r in range(3, 11):
            assert coeffs[r] == Rational(0)

    def test_depth_classification(self):
        info = shadow_depth_from_wheels('Heisenberg')
        assert info['r_max'] == 2
        assert info['class'] == 'G'

    def test_transferred_mk_pattern(self):
        for kk in range(2, 8):
            result = transferred_mk('Heisenberg', kk)
            if kk == 2:
                assert result['nonzero'] is True
            else:
                assert result['nonzero'] is False


# ============================================================
# TestAffine: Lie/tree class L, depth 3
# ============================================================

class TestAffine:
    """Affine sl_2 / sl_N: class L (Lie/tree), r_max = 3.

    The Lie bracket gives nonzero m_3; Jacobi identity kills m_4+.
    """

    def test_m2_nonzero_sl2(self):
        """kappa = 3(k+2)/4 for sl_2."""
        coeff = wheel_coefficient_affine(2, rank=2, level=1)
        expected = Rational(3) * (1 + 2) / 4
        assert coeff == expected

    def test_m2_nonzero_sl3(self):
        """kappa = (9-1)(k+3)/(2*3) = 8(k+3)/6 for sl_3."""
        coeff = wheel_coefficient_affine(2, rank=3, level=1)
        expected = Rational(8) * (1 + 3) / 6
        assert coeff == expected

    def test_m3_nonzero_sl2(self):
        """m_3 != 0 from Lie bracket structure constants."""
        coeff = wheel_coefficient_affine(3, rank=2, level=1)
        assert coeff != 0

    def test_m3_nonzero_sl3(self):
        coeff = wheel_coefficient_affine(3, rank=3, level=1)
        assert coeff != 0

    def test_m4_zero(self):
        """Jacobi identity kills m_4."""
        assert wheel_coefficient_affine(4, rank=2, level=1) == 0

    def test_m5_zero(self):
        assert wheel_coefficient_affine(5, rank=2, level=1) == 0

    def test_m10_zero(self):
        assert wheel_coefficient_affine(10, rank=3, level=5) == 0

    def test_all_higher_zero(self):
        """m_k = 0 for k >= 4, all ranks and levels."""
        for rank in [2, 3, 4]:
            for level in [1, 2, 5]:
                for kk in range(4, 12):
                    assert wheel_coefficient_affine(kk, rank=rank, level=level) == 0

    def test_shadow_coefficients_sl2(self):
        coeffs = _affine_sl2_shadow_coefficients(8, level_val=1)
        assert coeffs[2] != Rational(0)
        assert coeffs[3] != Rational(0)
        for r in range(4, 9):
            assert coeffs[r] == Rational(0)

    def test_depth_classification_sl2(self):
        info = shadow_depth_from_wheels('Affine_sl2')
        assert info['r_max'] == 3
        assert info['class'] == 'L'

    def test_depth_classification_slN(self):
        info = shadow_depth_from_wheels('Affine_slN')
        assert info['r_max'] == 3
        assert info['class'] == 'L'

    def test_transferred_mk_pattern(self):
        for kk in range(2, 8):
            result = transferred_mk('Affine_sl2', kk)
            if kk in (2, 3):
                assert result['nonzero'] is True
            else:
                assert result['nonzero'] is False


# ============================================================
# TestBetaGamma: contact/quartic class C, depth 4
# ============================================================

class TestBetaGamma:
    """betagamma system: class C (contact/quartic), r_max = 4.

    m_3 = 0 on primary line (abelian), m_4 != 0 on charged stratum,
    m_5+ = 0 (rank-one rigidity).
    """

    def test_m2_nonzero_standard(self):
        """kappa = 1 at weight 0."""
        coeff = wheel_coefficient_betagamma(2, weight=0)
        assert coeff == Rational(1)

    def test_m2_nonzero_weight1(self):
        """kappa = 1 at weight 1."""
        coeff = wheel_coefficient_betagamma(2, weight=1)
        assert coeff == Rational(1)

    def test_m2_symplectic(self):
        """kappa = -1/2 at weight 1/2 (symplectic boson)."""
        coeff = wheel_coefficient_betagamma(2, weight=Rational(1, 2))
        assert coeff == Rational(-1, 2)

    def test_m3_zero(self):
        """m_3 = 0 on weight-changing primary line."""
        assert wheel_coefficient_betagamma(3) == 0

    def test_m4_nonzero(self):
        """m_4 != 0: quartic contact on charged stratum."""
        coeff = wheel_coefficient_betagamma(4)
        assert coeff != 0

    def test_m5_zero(self):
        """m_5 = 0: rank-one rigidity."""
        assert wheel_coefficient_betagamma(5) == 0

    def test_m6_zero(self):
        assert wheel_coefficient_betagamma(6) == 0

    def test_all_higher_zero(self):
        for kk in range(5, 15):
            assert wheel_coefficient_betagamma(kk) == 0

    def test_shadow_coefficients(self):
        coeffs = _betagamma_shadow_coefficients(10, weight_val=0)
        assert coeffs[2] == Rational(1)
        assert coeffs[3] == Rational(0)
        assert coeffs[4] != Rational(0)
        for r in range(5, 11):
            assert coeffs[r] == Rational(0)

    def test_depth_classification(self):
        info = shadow_depth_from_wheels('BetaGamma')
        assert info['r_max'] == 4
        assert info['class'] == 'C'

    def test_bc_classification(self):
        info = shadow_depth_from_wheels('bc')
        assert info['r_max'] == 4
        assert info['class'] == 'C'

    def test_transferred_mk_pattern(self):
        for kk in range(2, 8):
            result = transferred_mk('BetaGamma', kk)
            if kk in (2, 4):
                assert result['nonzero'] is True
            else:
                assert result['nonzero'] is False


# ============================================================
# TestVirasoro: mixed class M, infinite depth
# ============================================================

class TestVirasoro:
    """Virasoro algebra: class M (mixed), r_max = infinity.

    ALL m_k are nonzero for k >= 2.  This is the defining property
    of class M (infinite shadow depth).
    """

    def test_m2_equals_kappa(self):
        """m_2 = kappa = c/2."""
        coeff = wheel_coefficient_virasoro(2)
        assert simplify(coeff - c / 2) == 0

    def test_m2_at_c1(self):
        coeff = wheel_coefficient_virasoro(2, c_val=1)
        assert coeff == Rational(1, 2)

    def test_m2_at_c26(self):
        coeff = wheel_coefficient_virasoro(2, c_val=26)
        assert coeff == Rational(13)

    def test_m3_nonzero(self):
        """S_3 = 2 (gravitational cubic)."""
        coeff = wheel_coefficient_virasoro(3)
        assert simplify(coeff - 2) == 0

    def test_m3_at_c1(self):
        coeff = wheel_coefficient_virasoro(3, c_val=1)
        assert coeff == Rational(2)

    def test_m4_nonzero(self):
        """S_4 = 10/[c(5c+22)] (quartic contact)."""
        coeff = wheel_coefficient_virasoro(4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(coeff - expected) == 0

    def test_m4_at_c1(self):
        coeff = wheel_coefficient_virasoro(4, c_val=1)
        expected = Rational(10) / (1 * (5 + 22))
        assert coeff == expected

    def test_m5_nonzero(self):
        """S_5 = -48/[c^2(5c+22)] (quintic forced)."""
        coeff = wheel_coefficient_virasoro(5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(coeff - expected) == 0

    def test_m5_at_c1(self):
        coeff = wheel_coefficient_virasoro(5, c_val=1)
        expected = Rational(-48) / (1 * 27)
        assert coeff == expected

    def test_m6_nonzero(self):
        """S_6 is nonzero (class M)."""
        coeff = wheel_coefficient_virasoro(6)
        assert simplify(coeff) != 0

    def test_m6_at_c1(self):
        coeff = wheel_coefficient_virasoro(6, c_val=1)
        assert coeff != 0

    def test_m7_nonzero(self):
        coeff = wheel_coefficient_virasoro(7)
        assert simplify(coeff) != 0

    def test_m8_nonzero(self):
        coeff = wheel_coefficient_virasoro(8)
        assert simplify(coeff) != 0

    def test_all_nonzero_through_arity_10(self):
        """ALL m_k nonzero for k = 2..10 (class M proof)."""
        for kk in range(2, 11):
            coeff = wheel_coefficient_virasoro(kk)
            assert simplify(coeff) != 0, f"S_{kk} vanished unexpectedly"

    def test_all_nonzero_numerical_c1(self):
        """At c=1: all S_r nonzero for r = 2..12."""
        for r in range(2, 13):
            coeff = wheel_coefficient_virasoro(r, c_val=1)
            assert coeff != 0, f"S_{r}(1) = 0 unexpectedly"

    def test_all_nonzero_numerical_c26(self):
        """At c=26: all S_r nonzero for r = 2..10."""
        for r in range(2, 11):
            coeff = wheel_coefficient_virasoro(r, c_val=26)
            assert coeff != 0, f"S_{r}(26) = 0 unexpectedly"

    def test_all_nonzero_numerical_c13(self):
        """At c=13 (self-dual): all S_r nonzero for r = 2..10."""
        for r in range(2, 11):
            coeff = wheel_coefficient_virasoro(r, c_val=13)
            assert coeff != 0, f"S_{r}(13) = 0 unexpectedly"

    def test_depth_classification(self):
        info = shadow_depth_from_wheels('Virasoro')
        assert info['r_max'] is None
        assert info['class'] == 'M'

    def test_transferred_mk_all_nonzero(self):
        """transferred_mk reports nonzero for all k >= 2."""
        for kk in range(2, 10):
            result = transferred_mk('Virasoro', kk)
            assert result['nonzero'] is True


# ============================================================
# TestVirasoroKnownValues: verify against known closed forms
# ============================================================

class TestVirasoroKnownValues:
    """Verify Virasoro shadow coefficients against independently known values."""

    def test_S2_is_c_over_2(self):
        sr = _virasoro_shadow_coefficient(2)
        assert simplify(sr - c / 2) == 0

    def test_S3_is_2(self):
        sr = _virasoro_shadow_coefficient(3)
        assert simplify(sr - 2) == 0

    def test_S4_formula(self):
        sr = _virasoro_shadow_coefficient(4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(sr - expected) == 0

    def test_S5_formula(self):
        sr = _virasoro_shadow_coefficient(5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(sr - expected) == 0

    def test_verify_known_coefficients_function(self):
        """Use the built-in verification function."""
        results = verify_known_virasoro_coefficients()
        for label, ok in results.items():
            assert ok, f"Known coefficient check failed for {label}"

    def test_S4_at_c1(self):
        sr = _virasoro_shadow_coefficient(4, c_val=1)
        assert sr == Rational(10, 27)

    def test_S4_at_c26(self):
        sr = _virasoro_shadow_coefficient(4, c_val=26)
        expected = Rational(10) / (26 * (130 + 22))
        assert sr == expected

    def test_S5_at_c1(self):
        sr = _virasoro_shadow_coefficient(5, c_val=1)
        assert sr == Rational(-48, 27)


# ============================================================
# TestVirasoroParametric: varying central charge
# ============================================================

class TestVirasoroParametric:
    """Test Virasoro wheel coefficients across various central charges."""

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 20, 26, 50, 100])
    def test_S2_positive_for_positive_c(self, c_val):
        """kappa = c/2 > 0 for c > 0."""
        sr = _virasoro_shadow_coefficient(2, c_val=c_val)
        assert sr > 0

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 26])
    def test_S3_always_2(self, c_val):
        """S_3 = 2 independent of c."""
        sr = _virasoro_shadow_coefficient(3, c_val=c_val)
        assert sr == Rational(2)

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 26, 50])
    def test_S4_positive_for_positive_c(self, c_val):
        """S_4 = 10/[c(5c+22)] > 0 for c > 0."""
        sr = _virasoro_shadow_coefficient(4, c_val=c_val)
        assert sr > 0

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 26])
    def test_S5_negative_for_positive_c(self, c_val):
        """S_5 = -48/[c^2(5c+22)] < 0 for c > 0."""
        sr = _virasoro_shadow_coefficient(5, c_val=c_val)
        assert sr < 0

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    def test_all_nonzero_at_c(self, c_val):
        """All S_r nonzero at standard central charges, r = 2..8."""
        for r in range(2, 9):
            sr = _virasoro_shadow_coefficient(r, c_val=c_val)
            assert sr != 0, f"S_{r}({c_val}) = 0"


# ============================================================
# TestDepthClassification: G/L/C/M for all families
# ============================================================

class TestDepthClassification:
    """Verify G/L/C/M classification for all standard families."""

    def test_classify_depth_2(self):
        assert classify_depth(2) == 'G'

    def test_classify_depth_3(self):
        assert classify_depth(3) == 'L'

    def test_classify_depth_4(self):
        assert classify_depth(4) == 'C'

    def test_classify_depth_none(self):
        assert classify_depth(None) == 'M'

    def test_classify_depth_5(self):
        """Depth >= 5 is class M (mixed)."""
        assert classify_depth(5) == 'M'

    def test_classify_depth_100(self):
        assert classify_depth(100) == 'M'

    def test_all_families_classified(self):
        """Every family in the depth table has a valid classification."""
        for family, info in _DEPTH_TABLE.items():
            cls = info['class']
            assert cls in ('G', 'L', 'C', 'M'), f"{family} has invalid class {cls}"

    def test_verification_all_pass(self):
        """Full verification passes for all families."""
        results = verify_depth_classification()
        for family, res in results.items():
            assert res['all_ok'], f"{family}: class_consistent={res['class_consistent']}, pattern={res['pattern_consistent']}"

    def test_gaussian_families(self):
        """G class: Heisenberg, Lattice, FreeFermion."""
        for fam in ['Heisenberg', 'Lattice', 'FreeFermion']:
            assert _DEPTH_TABLE[fam]['class'] == 'G'
            assert _DEPTH_TABLE[fam]['r_max'] == 2

    def test_lie_families(self):
        """L class: Affine sl_2, sl_N."""
        for fam in ['Affine_sl2', 'Affine_slN']:
            assert _DEPTH_TABLE[fam]['class'] == 'L'
            assert _DEPTH_TABLE[fam]['r_max'] == 3

    def test_contact_families(self):
        """C class: BetaGamma, bc."""
        for fam in ['BetaGamma', 'bc']:
            assert _DEPTH_TABLE[fam]['class'] == 'C'
            assert _DEPTH_TABLE[fam]['r_max'] == 4

    def test_mixed_families(self):
        """M class: Virasoro, W3, W_N."""
        for fam in ['Virasoro', 'W3', 'W_N']:
            assert _DEPTH_TABLE[fam]['class'] == 'M'
            assert _DEPTH_TABLE[fam]['r_max'] is None


# ============================================================
# TestCrossValidation: match shadow_metric_census.py
# ============================================================

class TestCrossValidation:
    """Cross-validate with shadow_metric_census.py classification."""

    def test_heisenberg_matches_census(self):
        """Census says G; wheels say G."""
        from compute.lib.shadow_metric_census import build_census
        census = build_census()
        assert census['Heisenberg'].cls == 'G'
        info = shadow_depth_from_wheels('Heisenberg')
        assert info['class'] == 'G'

    def test_affine_sl2_matches_census(self):
        from compute.lib.shadow_metric_census import build_census
        census = build_census()
        assert census['Affine_sl2'].cls == 'L'
        info = shadow_depth_from_wheels('Affine_sl2')
        assert info['class'] == 'L'

    def test_betagamma_matches_census(self):
        from compute.lib.shadow_metric_census import build_census
        census = build_census()
        assert census['BetaGamma'].cls == 'C'
        info = shadow_depth_from_wheels('BetaGamma')
        assert info['class'] == 'C'

    def test_virasoro_matches_census(self):
        from compute.lib.shadow_metric_census import build_census
        census = build_census()
        assert census['Virasoro'].cls == 'M'
        info = shadow_depth_from_wheels('Virasoro')
        assert info['class'] == 'M'

    def test_w3_matches_census(self):
        from compute.lib.shadow_metric_census import build_census
        census = build_census()
        assert census['W3'].cls == 'M'
        info = shadow_depth_from_wheels('W3')
        assert info['class'] == 'M'

    def test_all_families_match(self):
        """All 10 families agree between wheels and census."""
        from compute.lib.shadow_metric_census import build_census
        census = build_census()
        family_map = {
            'Heisenberg': 'Heisenberg',
            'Lattice': 'Lattice',
            'FreeFermion': 'FreeFermion',
            'Affine_sl2': 'Affine_sl2',
            'Affine_slN': 'Affine_slN',
            'BetaGamma': 'BetaGamma',
            'bc': 'bc',
            'Virasoro': 'Virasoro',
            'W3': 'W3',
            'W_N': 'W_N',
        }
        for wheel_name, census_name in family_map.items():
            wheel_cls = _DEPTH_TABLE[wheel_name]['class']
            census_cls = census[census_name].cls
            assert wheel_cls == census_cls, f"{wheel_name}: wheel={wheel_cls} != census={census_cls}"


# ============================================================
# TestVirasoroWheelAnalysis: detailed Virasoro tower
# ============================================================

class TestVirasoroWheelAnalysis:
    """Detailed analysis of the Virasoro wheel coefficient tower."""

    def test_coefficients_dict(self):
        coeffs = virasoro_wheel_coefficients(8)
        assert set(coeffs.keys()) == set(range(2, 9))

    def test_nonvanishing_symbolic(self):
        """All S_r nonzero as rational functions of c."""
        nv = virasoro_wheel_nonvanishing(8)
        for r in range(2, 9):
            assert nv[r] is True, f"S_{r} vanished symbolically"

    def test_nonvanishing_numerical_c1(self):
        nv = virasoro_wheel_nonvanishing(10, c_val=1)
        for r in range(2, 11):
            assert nv[r] is True, f"S_{r}(1) vanished"

    def test_pole_check(self):
        poles = virasoro_pole_check(8)
        for r in range(2, 9):
            assert poles[r]['nonzero_at_1'] is True
            assert poles[r]['nonzero_at_13'] is True
            assert poles[r]['nonzero_at_26'] is True

    def test_self_dual_c13(self):
        """At the self-dual point c=13, all coefficients are finite and nonzero."""
        for r in range(2, 9):
            sr = _virasoro_shadow_coefficient(r, c_val=13)
            assert sr != 0


# ============================================================
# TestSwissCheese: factorization direction data
# ============================================================

class TestSwissCheese:
    """Verify Swiss-cheese factorization data."""

    def test_heisenberg_directions(self):
        data = swiss_cheese_direction_data('Heisenberg')
        assert data['class'] == 'G'
        assert data['first_wheel_arity'] is None

    def test_affine_directions(self):
        data = swiss_cheese_direction_data('Affine_sl2')
        assert data['class'] == 'L'

    def test_betagamma_directions(self):
        data = swiss_cheese_direction_data('BetaGamma')
        assert data['class'] == 'C'
        assert data['first_wheel_arity'] == 4

    def test_virasoro_directions(self):
        data = swiss_cheese_direction_data('Virasoro')
        assert data['class'] == 'M'
        assert data['first_wheel_arity'] == 4


# ============================================================
# TestDepthDecomposition: d = 1 + d_arith + d_alg
# ============================================================

class TestDepthDecomposition:
    """Verify depth decomposition into arithmetic and algebraic parts."""

    def test_gaussian_decomposition(self):
        dd = depth_decomposition('Heisenberg')
        assert dd['d_algebraic'] == 0
        assert dd['d_arithmetic'] == 0
        assert dd['d_total'] == 1

    def test_lie_decomposition(self):
        dd = depth_decomposition('Affine_sl2')
        assert dd['d_algebraic'] == 1
        assert dd['d_total'] == 2

    def test_contact_decomposition(self):
        dd = depth_decomposition('BetaGamma')
        assert dd['d_algebraic'] == 2
        assert dd['d_total'] == 3

    def test_mixed_decomposition(self):
        dd = depth_decomposition('Virasoro')
        assert dd['d_algebraic'] == float('inf')
        assert dd['d_total'] == float('inf')

    def test_all_families_have_decomposition(self):
        for fam in _DEPTH_TABLE:
            dd = depth_decomposition(fam)
            assert dd['d_algebraic'] is not None


# ============================================================
# TestEdgeCases: boundary conditions and special values
# ============================================================

class TestEdgeCases:
    """Edge cases: n=2 boundary, large n, critical/special c values."""

    def test_wheel_n2_returns_empty(self):
        """No wheel diagrams at n=2 (wheel requires cycle of length >= 3)."""
        assert enumerate_wheels(2) == []

    def test_wheel_n1_returns_empty(self):
        assert enumerate_wheels(1) == []

    def test_large_n_wheel(self):
        """Wheel with 100 legs is valid."""
        wheels = enumerate_wheels(100)
        assert len(wheels) == 1
        assert wheels[0].symmetry_factor == Fraction(1, 200)

    def test_virasoro_S2_at_c0_diverges(self):
        """S_2 = c/2 vanishes at c=0 (not a pole; value is 0)."""
        sr = _virasoro_shadow_coefficient(2, c_val=0)
        assert sr == Rational(0)

    def test_virasoro_large_c(self):
        """At large c, S_4 ~ 2/(c^2) (leading term)."""
        sr = _virasoro_shadow_coefficient(4, c_val=1000)
        expected = Rational(10) / (1000 * (5000 + 22))
        assert sr == expected
        # Check it is small (as expected for large c)
        assert sr < Rational(1, 100)

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            transferred_mk('Unknown', 3)

    def test_unknown_family_depth_raises(self):
        with pytest.raises(ValueError):
            shadow_depth_from_wheels('Unknown')

    def test_virasoro_at_c_half(self):
        """Minimal model c=1/2: all S_r should be finite and nonzero."""
        for r in range(2, 8):
            sr = _virasoro_shadow_coefficient(r, c_val=Rational(1, 2))
            assert sr != 0, f"S_{r}(1/2) = 0"

    def test_virasoro_at_c_minus_22_over_5_is_pole(self):
        """c = -22/5 is a pole of S_4 (Lee-Yang singularity)."""
        # S_4 has (5c+22) in denominator; at c=-22/5 this vanishes
        sr_symbolic = _virasoro_shadow_coefficient(4)
        denom = (5 * c + 22)
        # At c = -22/5, the denominator vanishes
        val = denom.subs(c, Rational(-22, 5))
        assert val == 0

    def test_w_n_families(self):
        """W3 and W_N both classified as M."""
        for fam in ['W3', 'W_N']:
            result = transferred_mk(fam, 5)
            assert result['nonzero'] is True


# ============================================================
# TestWheelDiagramDataclass: dataclass correctness
# ============================================================

class TestWheelDiagramDataclass:
    """Test WheelDiagram dataclass properties."""

    def test_default_loop_number(self):
        w = WheelDiagram(n_external=5, n_internal_edges=5)
        assert w.loop_number == 1

    def test_custom_coefficient(self):
        w = WheelDiagram(n_external=4, n_internal_edges=4,
                         coefficient=Rational(3, 7))
        assert w.coefficient == Rational(3, 7)

    def test_symmetry_factor_computed(self):
        w = WheelDiagram(n_external=6, n_internal_edges=6)
        assert w.symmetry_factor == Fraction(1, 12)

    def test_custom_symmetry_factor(self):
        w = WheelDiagram(n_external=4, n_internal_edges=4,
                         symmetry_factor=Fraction(1, 4))
        assert w.symmetry_factor == Fraction(1, 4)
