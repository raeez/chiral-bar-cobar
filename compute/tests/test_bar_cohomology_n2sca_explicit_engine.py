"""Tests for bar cohomology of the N=2 superconformal algebra.

Tests the CE cohomology of the negative-mode Lie superalgebra g_- of
the N=2 SCA, which gives the E_2 page of the PBW spectral sequence.

The N=2 SCA has 4 generators: T(2, bos), G+(3/2, ferm), G-(3/2, ferm), J(1, bos).
The N=2 SCA is the FIRST super algebra computed at the chain level.

Key findings verified here:
  - The N=2 SCA is NOT chirally Koszul: H^n != 0 for n >= 2.
  - H^1 generators: J at h=1 (charge 0), G+/G- at h=3/2 (charges +/-1),
    2 at h=2 (charge 0), then NO H^1 at h >= 5/2.
  - Higher bar cohomology appears starting at h=3 (bar degree 2).
  - The charge decomposition is symmetric under charge conjugation (q -> -q).
  - The CE complex uses shifted parities: bosonic -> odd, fermionic -> even.
  - The super-Jacobi identity is satisfied with {G+_r, G-_s} = 2L_{r+s} + (r-s)J_{r+s}.
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.bar_cohomology_n2sca_explicit_engine import (
    SuperCEComplex,
    bracket,
    compare_n1_n2,
    enumerate_creating_modes,
    enumerate_n2_states,
    kappa_n2,
    mode_charge,
    mode_label,
    mode_parity,
    mode_weight_half,
    n1_states,
    n2_weight_space_table,
    state_charge,
    state_parity,
    verify_bracket_relations,
    verify_d_squared_all,
    verify_super_jacobi,
)


# ============================================================
# Bracket relations
# ============================================================

class TestBracketRelations:
    """Verify the N=2 SCA mode algebra bracket."""

    def test_all_basic_brackets(self):
        checks = verify_bracket_relations(Rational(1))
        for name, ok in checks.items():
            assert ok, f"Bracket check failed: {name}"

    def test_G_plus_G_minus_basic(self):
        """anti-comm = 2 L_{-3}, no J, no central."""
        br = bracket(('G+', Fraction(-3, 2)), ('G-', Fraction(-3, 2)))
        assert br == {('L', Fraction(-3)): Rational(2)}

    def test_G_plus_G_minus_higher(self):
        """anti-comm = 2L_{-4} + J_{-4}."""
        br = bracket(('G+', Fraction(-3, 2)), ('G-', Fraction(-5, 2)))
        assert br == {('L', Fraction(-4)): Rational(2), ('J', Fraction(-4)): Rational(1)}

    def test_G_minus_G_plus_symmetry(self):
        """anti-commutator is symmetric."""
        br1 = bracket(('G+', Fraction(-3, 2)), ('G-', Fraction(-5, 2)))
        br2 = bracket(('G-', Fraction(-5, 2)), ('G+', Fraction(-3, 2)))
        assert br1 == br2

    def test_L_G_plus(self):
        """[L_{-2}, G+_{-3/2}] = (1/2)G+_{-7/2}."""
        br = bracket(('L', Fraction(-2)), ('G+', Fraction(-3, 2)))
        assert br == {('G+', Fraction(-7, 2)): Fraction(1, 2)}

    def test_J_G_plus(self):
        """[J_{-1}, G+_{-3/2}] = G+_{-5/2}."""
        br = bracket(('J', Fraction(-1)), ('G+', Fraction(-3, 2)))
        assert br == {('G+', Fraction(-5, 2)): Rational(1)}

    def test_J_G_minus(self):
        """[J_{-1}, G-_{-3/2}] = -G-_{-5/2}."""
        br = bracket(('J', Fraction(-1)), ('G-', Fraction(-3, 2)))
        assert br == {('G-', Fraction(-5, 2)): Rational(-1)}

    def test_G_plus_G_plus_zero(self):
        """{G+, G+} = 0."""
        br = bracket(('G+', Fraction(-3, 2)), ('G+', Fraction(-3, 2)))
        assert len(br) == 0

    def test_G_minus_G_minus_zero(self):
        """{G-, G-} = 0."""
        br = bracket(('G-', Fraction(-3, 2)), ('G-', Fraction(-5, 2)))
        assert len(br) == 0

    def test_J_J_zero_in_g_minus(self):
        """[J, J] = 0 in g_- (no central extension)."""
        br = bracket(('J', Fraction(-1)), ('J', Fraction(-2)))
        assert len(br) == 0

    def test_L_L_basic(self):
        """[L_{-2}, L_{-3}] = L_{-5}."""
        br = bracket(('L', Fraction(-2)), ('L', Fraction(-3)))
        assert br == {('L', Fraction(-5)): Rational(1)}

    def test_L_J_basic(self):
        """[L_{-2}, J_{-1}] = J_{-3}."""
        br = bracket(('L', Fraction(-2)), ('J', Fraction(-1)))
        assert br == {('J', Fraction(-3)): Rational(1)}


class TestSuperJacobi:
    """Verify the super-Jacobi identity."""

    def test_super_jacobi_wh6(self):
        assert verify_super_jacobi(6, Rational(1)) == 0

    def test_super_jacobi_wh8(self):
        assert verify_super_jacobi(8, Rational(1)) == 0


# ============================================================
# Mode enumeration
# ============================================================

class TestModeEnumeration:
    """Test mode properties and enumeration."""

    def test_parities(self):
        assert mode_parity(('L', Fraction(-2))) == 0
        assert mode_parity(('J', Fraction(-1))) == 0
        assert mode_parity(('G+', Fraction(-3, 2))) == 1
        assert mode_parity(('G-', Fraction(-3, 2))) == 1

    def test_charges(self):
        assert mode_charge(('L', Fraction(-2))) == 0
        assert mode_charge(('J', Fraction(-1))) == 0
        assert mode_charge(('G+', Fraction(-3, 2))) == 1
        assert mode_charge(('G-', Fraction(-3, 2))) == -1

    def test_weights(self):
        assert mode_weight_half(('L', Fraction(-2))) == 4
        assert mode_weight_half(('J', Fraction(-1))) == 2
        assert mode_weight_half(('G+', Fraction(-3, 2))) == 3
        assert mode_weight_half(('G-', Fraction(-3, 2))) == 3

    def test_creating_modes_count(self):
        modes = enumerate_creating_modes(6)
        # wh=2: J_{-1}  (1 bos)
        # wh=3: G+_{-3/2}, G-_{-3/2}  (2 ferm)
        # wh=4: L_{-2}, J_{-2}  (2 bos)
        # wh=5: G+_{-5/2}, G-_{-5/2}  (2 ferm)
        # wh=6: L_{-3}, J_{-3}  (2 bos)
        assert len(modes) == 9

    def test_mode_ordering(self):
        modes = enumerate_creating_modes(6)
        for i in range(len(modes) - 1):
            assert mode_weight_half(modes[i]) <= mode_weight_half(modes[i + 1])


# ============================================================
# PBW states
# ============================================================

class TestPBWStates:
    """Test PBW state enumeration and properties."""

    def test_weight_1(self):
        """h=1 (wh=2): only J_{-1}."""
        states = enumerate_n2_states(2)
        assert len(states) == 1

    def test_weight_3_2(self):
        """h=3/2 (wh=3): G+_{-3/2} and G-_{-3/2}."""
        states = enumerate_n2_states(3)
        assert len(states) == 2

    def test_weight_2(self):
        """h=2 (wh=4): L_{-2}, J_{-2}, J_{-1}^2."""
        states = enumerate_n2_states(4)
        assert len(states) == 3

    def test_weight_5_2(self):
        """h=5/2 (wh=5): 4 states."""
        states = enumerate_n2_states(5)
        assert len(states) == 4

    def test_weight_3(self):
        """h=3 (wh=6): 6 states."""
        states = enumerate_n2_states(6)
        assert len(states) == 6

    def test_weight_4(self):
        """h=4 (wh=8): 15 states."""
        states = enumerate_n2_states(8)
        assert len(states) == 15

    def test_weight_space_dimensions(self):
        """Verify weight space dimension sequence."""
        expected = {2: 1, 3: 2, 4: 3, 5: 4, 6: 6, 7: 10, 8: 15, 9: 20, 10: 28, 11: 42, 12: 59}
        for wh, dim in expected.items():
            assert len(enumerate_n2_states(wh)) == dim, f"wh={wh}: expected {dim}"

    def test_charge_symmetry(self):
        """Charge distribution is symmetric under q -> -q."""
        ws = n2_weight_space_table(12)
        for wh, data in ws.items():
            charges = data['charges']
            for q, count in charges.items():
                assert charges.get(-q, 0) == count, f"wh={wh}: charge asymmetry at q={q}"

    def test_fermionic_no_repeat(self):
        """Fermionic modes appear at most once in PBW states."""
        for wh in range(2, 10):
            for state in enumerate_n2_states(wh):
                ferm_modes = [m for m in state if mode_parity(m) == 1]
                assert len(ferm_modes) == len(set(ferm_modes)), f"Repeated fermion in {state}"

    def test_charge_at_weight_4(self):
        """h=4 (wh=8): charges {-2: 1, 0: 13, 2: 1}."""
        ws = n2_weight_space_table(8)
        charges = ws[8]['charges']
        assert charges.get(-2, 0) == 1
        assert charges.get(0, 0) == 13
        assert charges.get(2, 0) == 1


# ============================================================
# CE complex structure
# ============================================================

class TestCEComplexStructure:
    """Test CE chain group dimensions and basis."""

    @pytest.fixture
    def ce(self):
        return SuperCEComplex(12, Rational(1))

    def test_ce_degree0_weight0(self, ce):
        """CE^0 at weight 0: dimension 1 (the constants)."""
        # Weight 0 is not in our range (min weight = 2 for creating modes)
        assert ce.chain_dim(0, 0) == 1

    def test_ce_degree1_generators(self, ce):
        """CE^1 at various weights: single generators."""
        assert ce.chain_dim(1, 2) == 1   # J_{-1}
        assert ce.chain_dim(1, 3) == 2   # G+_{-3/2}, G-_{-3/2}
        assert ce.chain_dim(1, 4) == 2   # L_{-2}, J_{-2}

    def test_ce_degree2_weight4(self, ce):
        """CE^2 at h=2 (wh=4): 0.
        Only candidate is (J_{-1}, J_{-1}) but J is bosonic (exterior, no repeat)."""
        assert ce.chain_dim(2, 4) == 0

    def test_ce_degree2_weight6(self, ce):
        """CE^2 at h=3 (wh=6): pairs summing to weight 6."""
        dim = ce.chain_dim(2, 6)
        assert dim >= 3  # (J_{-1}, L_{-2}), (J_{-1}, J_{-2}), (G+_{-3/2}, G-_{-3/2})


# ============================================================
# d^2 = 0
# ============================================================

class TestDSquaredZero:
    """Verify d^2 = 0 at all weights."""

    def test_d_squared_all_weights(self):
        fails = verify_d_squared_all(12, Rational(1))
        assert len(fails) == 0, f"d^2 != 0 at: {list(fails.keys())}"

    def test_d_squared_wh6(self):
        ce = SuperCEComplex(8, Rational(1))
        assert ce.verify_d_squared(0, 6)
        assert ce.verify_d_squared(1, 6)

    def test_d_squared_wh8(self):
        """wh=8 was the first failure case before the sign fix."""
        ce = SuperCEComplex(10, Rational(1))
        assert ce.verify_d_squared(0, 8)
        assert ce.verify_d_squared(1, 8)

    def test_d_squared_wh9(self):
        ce = SuperCEComplex(10, Rational(1))
        assert ce.verify_d_squared(0, 9)
        assert ce.verify_d_squared(1, 9)


# ============================================================
# Bar cohomology (CE cohomology) values
# ============================================================

class TestBarCohomology:
    """Test H^n at each weight.

    This is the main computational result: the CE cohomology of g_-
    for the N=2 SCA, which gives the E_2 page of the PBW spectral
    sequence and (for Koszul algebras) the bar cohomology.
    """

    @pytest.fixture
    def ce(self):
        return SuperCEComplex(12, Rational(1))

    def test_h1_weight_1(self, ce):
        """H^1 at h=1: 1 (the J generator)."""
        assert ce.cohomology_dim(1, 2) == 1

    def test_h1_weight_3_2(self, ce):
        """H^1 at h=3/2: 2 (G+ and G-)."""
        assert ce.cohomology_dim(1, 3) == 2

    def test_h1_weight_2(self, ce):
        """H^1 at h=2: 2 (T and J_{-2} or similar)."""
        assert ce.cohomology_dim(1, 4) == 2

    def test_h1_weight_5_2(self, ce):
        """H^1 at h=5/2: 0."""
        assert ce.cohomology_dim(1, 5) == 0

    def test_h2_weight_3(self, ce):
        """H^2 at h=3: 3. Non-Koszul!"""
        assert ce.cohomology_dim(2, 6) == 3

    def test_h2_weight_7_2(self, ce):
        """H^2 at h=7/2: 4."""
        assert ce.cohomology_dim(2, 7) == 4

    def test_h2_weight_4(self, ce):
        """H^2 at h=4: 2."""
        assert ce.cohomology_dim(2, 8) == 2

    def test_h3_weight_9_2(self, ce):
        """H^3 at h=9/2: 2."""
        assert ce.cohomology_dim(3, 9) == 2

    def test_h3_weight_5(self, ce):
        """H^3 at h=5: 2."""
        assert ce.cohomology_dim(3, 10) == 2

    def test_h3_weight_6(self, ce):
        """H^3 at h=6: 3."""
        assert ce.cohomology_dim(3, 12) == 3

    def test_h4_weight_6(self, ce):
        """H^4 at h=6: 2."""
        assert ce.cohomology_dim(4, 12) == 2

    def test_not_koszul(self, ce):
        """N=2 SCA is NOT chirally Koszul: H^2 != 0."""
        assert ce.cohomology_dim(2, 6) > 0

    def test_full_table_through_weight_6(self, ce):
        """Verify the complete cohomology table through h=6."""
        expected = {
            (1, 2): 1,    # h=1: J
            (1, 3): 2,    # h=3/2: G+, G-
            (1, 4): 2,    # h=2: T, one more
            (2, 6): 3,    # h=3
            (2, 7): 4,    # h=7/2
            (2, 8): 2,    # h=4
            (2, 9): 2,    # h=9/2
            (3, 9): 2,    # h=9/2
            (2, 10): 2,   # h=5
            (3, 10): 2,   # h=5
            (3, 12): 3,   # h=6
            (4, 12): 2,   # h=6
        }
        for (deg, wh), exp_dim in expected.items():
            computed = ce.cohomology_dim(deg, wh)
            assert computed == exp_dim, (
                f"H^{deg} at wh={wh} (h={Fraction(wh,2)}): expected {exp_dim}, got {computed}"
            )


# ============================================================
# Charge decomposition
# ============================================================

class TestChargeDecomposition:
    """Test U(1) charge decomposition of cohomology."""

    @pytest.fixture
    def ce(self):
        return SuperCEComplex(12, Rational(1))

    def test_h1_weight1_charge0(self, ce):
        charges = ce.cohomology_by_charge(1, 2)
        assert charges == {0: 1}

    def test_h1_weight3_2_charges(self, ce):
        charges = ce.cohomology_by_charge(1, 3)
        assert charges == {-1: 1, 1: 1}

    def test_h1_weight2_charge0(self, ce):
        charges = ce.cohomology_by_charge(1, 4)
        assert charges == {0: 2}

    def test_h2_weight3_charges(self, ce):
        """H^2 at h=3: charges {-2: 1, 0: 1, 2: 1}."""
        charges = ce.cohomology_by_charge(2, 6)
        assert charges == {-2: 1, 0: 1, 2: 1}

    def test_h2_weight7_2_charges(self, ce):
        """H^2 at h=7/2: charges {-1: 2, 1: 2}."""
        charges = ce.cohomology_by_charge(2, 7)
        assert charges == {-1: 2, 1: 2}

    def test_h3_weight9_2_charges(self, ce):
        """H^3 at h=9/2: charges {-3: 1, 3: 1}."""
        charges = ce.cohomology_by_charge(3, 9)
        assert charges == {-3: 1, 3: 1}

    def test_charge_conjugation_symmetry(self, ce):
        """All cohomology is symmetric under q -> -q."""
        for wh in range(2, 13):
            for deg in range(0, 6):
                charges = ce.cohomology_by_charge(deg, wh)
                for q, dim in charges.items():
                    assert charges.get(-q, 0) == dim, (
                        f"Charge asymmetry at deg={deg}, wh={wh}: q={q} has {dim}, q={-q} has {charges.get(-q, 0)}"
                    )


# ============================================================
# N=1 comparison
# ============================================================

class TestN1Comparison:
    """Compare with N=1 SCA."""

    def test_n1_weight_space_dims(self):
        """N=1 SCA dimensions: 0, 1, 1, 1, 1, 2, 3, 3, 3, 5, 7."""
        expected = {2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 2, 8: 3, 9: 3, 10: 3, 11: 5, 12: 7}
        for wh, dim in expected.items():
            assert len(n1_states(wh)) == dim, f"N=1 at wh={wh}: expected {dim}"

    def test_n2_larger_than_n1(self):
        """N=2 always has at least as many states as N=1."""
        comp = compare_n1_n2(12)
        for wh, d in comp.items():
            assert d['N2'] >= d['N1'], f"wh={wh}: N2={d['N2']} < N1={d['N1']}"


# ============================================================
# Kappa
# ============================================================

class TestKappa:
    """Verify kappa(N=2 SCA)."""

    def test_kappa_formula(self):
        """kappa = (6-c)/(2(3-c))."""
        assert kappa_n2(1) == Rational(5, 4)

    def test_kappa_k1(self):
        """At k=1 (c=1): kappa = 5/4."""
        assert kappa_n2(1) == Rational(5, 4)

    def test_kappa_complementarity(self):
        """kappa(c) + kappa(6-c) = 1."""
        for c_val in [1, 2, Rational(1, 2), Rational(5, 2)]:
            k1 = kappa_n2(c_val)
            k2 = kappa_n2(6 - c_val)
            assert k1 + k2 == 1, f"c={c_val}: kappa + kappa' = {k1 + k2}"


# ============================================================
# c-independence of CE cohomology
# ============================================================

class TestCIndependence:
    """CE cohomology of g_- is c-independent (no central terms)."""

    def test_c_independence(self):
        """Cohomology at c=1 equals cohomology at c=3."""
        ce1 = SuperCEComplex(10, Rational(1))
        ce3 = SuperCEComplex(10, Rational(3))
        for wh in range(2, 11):
            for deg in range(0, 5):
                h1 = ce1.cohomology_dim(deg, wh)
                h3 = ce3.cohomology_dim(deg, wh)
                assert h1 == h3, f"c-dependence at deg={deg}, wh={wh}: c=1 gives {h1}, c=3 gives {h3}"


# ============================================================
# Vanishing at half-integer weights
# ============================================================

class TestVanishingPatterns:
    """Test vanishing patterns in the cohomology."""

    @pytest.fixture
    def ce(self):
        return SuperCEComplex(12, Rational(1))

    def test_h1_vanishes_at_wh5(self, ce):
        """H^1 = 0 at h=5/2 (wh=5)."""
        assert ce.cohomology_dim(1, 5) == 0

    def test_total_vanishes_at_wh5(self, ce):
        """Total cohomology = 0 at h=5/2 (wh=5)."""
        total = sum(ce.cohomology_dim(deg, 5) for deg in range(6))
        assert total == 0

    def test_total_vanishes_at_wh11(self, ce):
        """Total cohomology = 0 at h=11/2 (wh=11)."""
        total = sum(ce.cohomology_dim(deg, 11) for deg in range(8))
        assert total == 0

    def test_h1_stops_at_weight_2(self, ce):
        """H^1 is nonzero only at h=1, 3/2, 2."""
        for wh in range(5, 13):
            assert ce.cohomology_dim(1, wh) == 0, f"H^1 nonzero at wh={wh}"


# ============================================================
# Euler characteristic
# ============================================================

class TestEulerCharacteristic:
    """Verify Euler characteristic sum = alternating chain group dims."""

    @pytest.fixture
    def ce(self):
        return SuperCEComplex(12, Rational(1))

    def test_euler_char_wh6(self, ce):
        """chi(CE) at wh=6: alternating sum of chain dims = alt sum of H dims."""
        chi_chains = sum((-1)**deg * ce.chain_dim(deg, 6) for deg in range(8))
        chi_cohom = sum((-1)**deg * ce.cohomology_dim(deg, 6) for deg in range(8))
        assert chi_chains == chi_cohom

    def test_euler_char_wh8(self, ce):
        chi_chains = sum((-1)**deg * ce.chain_dim(deg, 8) for deg in range(10))
        chi_cohom = sum((-1)**deg * ce.cohomology_dim(deg, 8) for deg in range(10))
        assert chi_chains == chi_cohom

    def test_euler_char_wh10(self, ce):
        chi_chains = sum((-1)**deg * ce.chain_dim(deg, 10) for deg in range(10))
        chi_cohom = sum((-1)**deg * ce.cohomology_dim(deg, 10) for deg in range(10))
        assert chi_chains == chi_cohom
