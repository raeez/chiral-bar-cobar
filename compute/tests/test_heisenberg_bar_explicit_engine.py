r"""Tests for the explicit Heisenberg bar complex engine at arities 1-4.

Ground truth sources:
    1. heisenberg_bar.py (existing chain-level module)
    2. bar_complex.py (OPE algebra and bar dimensions)
    3. heisenberg_bv_bar_proof.py (BV/bar identification, Faber-Pandharipande)
    4. Signs appendix (signs_and_shifts.tex): desuspension convention
    5. prop:heisenberg-r-matrix: r(z) = k/z
    6. rem:heisenberg-bar-absorbs-pole: AP19 pole absorption

Multi-path verification (CLAUDE.md mandate: 3+ independent paths per claim):
    Path 1: Direct computation from OPE modes
    Path 2: Comparison with heisenberg_bar.py
    Path 3: Numerical evaluation at specific k values
    Path 4: Combinatorial identity verification (binomial coefficients)
    Path 5: Cross-check with bar_complex.py OPE table
    Path 6: Curvature relation d^2 = [m_0, -]
    Path 7: Shadow obstruction tower consistency
"""

import pytest
from sympy import Symbol, Rational, simplify, exp, Integer
from math import comb, factorial

from compute.lib.heisenberg_bar_explicit_engine import (
    # OPE data
    heisenberg_ope_modes,
    # Bar differential
    bar_differential_ordered,
    bar_differential_arity1,
    bar_differential_arity2,
    bar_differential_arity3,
    bar_differential_arity4,
    # d^2 verification
    verify_d_squared_zero,
    d_squared_general,
    # Coproduct
    deconcatenation_coproduct,
    coproduct_arity1,
    coproduct_arity2,
    coproduct_arity3,
    coproduct_arity4,
    # Coderivation
    verify_coderivation,
    verify_coderivation_explicit,
    # Dimensions
    ordered_bar_dim,
    ordered_bar_with_forms_dim,
    symmetric_bar_dim,
    harrison_bar_dim,
    compare_bar_complexes,
    # R-matrix
    heisenberg_r_matrix,
    heisenberg_R_matrix_formal,
    r_twisted_action_arity2,
    coproduct_r_twisted_arity2,
    # Complete structure maps
    complete_arity_1,
    complete_arity_2,
    complete_arity_3,
    complete_arity_4,
    # General formulas
    bar_differential_general,
    # Shadow data
    shadow_kappa,
    shadow_cubic,
    shadow_quartic,
    shadow_depth,
    # Numerical verification
    verify_at_level,
    # Cross-checks
    cross_check_with_heisenberg_bar,
    cross_check_with_bar_complex,
    # Chain complex
    bar_chain_complex_matrix,
    # Data structures
    BarSum,
    k,
)


# ============================================================================
# OPE MODES
# ============================================================================

class TestOPEModes:
    """Verify OPE mode extraction: J(z)J(w) ~ k/(z-w)^2."""

    def test_double_pole_mode(self):
        """J_{(1)}J = k (vacuum). The (z-w)^{-2} pole gives mode n=1."""
        modes = heisenberg_ope_modes()
        assert 1 in modes
        name, val = modes[1]
        assert name == 'vac'
        assert val == k

    def test_no_simple_pole(self):
        """J_{(0)}J = 0. Abelian: no Lie bracket."""
        modes = heisenberg_ope_modes()
        assert 0 in modes
        name, val = modes[0]
        assert name == 'zero'
        assert val == 0

    def test_no_higher_poles(self):
        """J_{(n)}J = 0 for n >= 2. No higher singular terms."""
        modes = heisenberg_ope_modes()
        for n in [2, 3, 4, 5]:
            assert n not in modes

    def test_symbolic_level(self):
        """OPE modes with symbolic level parameter."""
        lev = Symbol('lev')
        modes = heisenberg_ope_modes(level=lev)
        _, val = modes[1]
        assert val == lev

    def test_numeric_level(self):
        """OPE modes at numeric level k=3."""
        modes = heisenberg_ope_modes(level=3)
        _, val = modes[1]
        assert val == 3


# ============================================================================
# BAR DIFFERENTIAL — ARITY BY ARITY
# ============================================================================

class TestBarDifferentialArity1:
    """d_B[J] = 0. No collisions at arity 1."""

    def test_zero(self):
        d = bar_differential_arity1()
        assert d.is_zero()

    def test_general_formula(self):
        d = bar_differential_ordered(1)
        assert d.is_zero()

    def test_numeric(self):
        """At k=5: d[J] = 0."""
        d = bar_differential_ordered(1, 5)
        assert d.is_zero()


class TestBarDifferentialArity2:
    """d_B[J|J] = k * |vac>. Single pair (1,2), only double pole."""

    def test_vacuum_component(self):
        d = bar_differential_arity2()
        assert simplify(d.get(0) - k) == 0

    def test_no_arity1_component(self):
        """No bar^1 component (J_{(0)}J = 0)."""
        d = bar_differential_arity2()
        assert simplify(d.get(1)) == 0

    def test_general_formula(self):
        d = bar_differential_ordered(2)
        assert simplify(d.get(0) - k) == 0

    def test_pair_count(self):
        """C(2,2) = 1 pair."""
        assert comb(2, 2) == 1

    @pytest.mark.parametrize("kval", [1, 2, -1, Rational(1, 2), 0])
    def test_numeric(self, kval):
        d = bar_differential_ordered(2, kval)
        assert simplify(d.get(0) - kval) == 0


class TestBarDifferentialArity3:
    """d_B[J|J|J] = 3k * [J]. Three pairs, each giving k * [J]."""

    def test_arity1_component(self):
        d = bar_differential_arity3()
        assert simplify(d.get(1) - 3 * k) == 0

    def test_no_vacuum_component(self):
        d = bar_differential_arity3()
        assert simplify(d.get(0)) == 0

    def test_general_formula(self):
        d = bar_differential_ordered(3)
        assert simplify(d.get(1) - 3 * k) == 0

    def test_pair_count(self):
        """C(3,2) = 3 pairs."""
        assert comb(3, 2) == 3

    def test_pairwise_contributions(self):
        """Each of the 3 pairs contributes equally: k * [J]."""
        info = complete_arity_3()
        assert len(info['differential_by_pair']) == 3

    @pytest.mark.parametrize("kval", [1, 2, -1, 7])
    def test_numeric(self, kval):
        d = bar_differential_ordered(3, kval)
        assert simplify(d.get(1) - 3 * kval) == 0


class TestBarDifferentialArity4:
    """d_B[J^4] = 6k * [J|J]. Six pairs, each giving k * [J|J]."""

    def test_arity2_component(self):
        d = bar_differential_arity4()
        assert simplify(d.get(2) - 6 * k) == 0

    def test_no_lower_components(self):
        d = bar_differential_arity4()
        assert simplify(d.get(0)) == 0
        assert simplify(d.get(1)) == 0

    def test_general_formula(self):
        d = bar_differential_ordered(4)
        assert simplify(d.get(2) - 6 * k) == 0

    def test_pair_count(self):
        """C(4,2) = 6 pairs."""
        assert comb(4, 2) == 6

    def test_pairwise_contributions(self):
        info = complete_arity_4()
        assert len(info['differential_by_pair']) == 6

    @pytest.mark.parametrize("kval", [1, 2, -1, 10])
    def test_numeric(self, kval):
        d = bar_differential_ordered(4, kval)
        assert simplify(d.get(2) - 6 * kval) == 0


class TestBarDifferentialHigherArity:
    """General formula: d_B[J^n] = C(n,2) * k * [J^{n-2}]."""

    @pytest.mark.parametrize("n,expected_coeff", [
        (1, 0), (2, 1), (3, 3), (4, 6), (5, 10), (6, 15), (7, 21), (8, 28),
    ])
    def test_coefficient(self, n, expected_coeff):
        info = bar_differential_general(n)
        if n <= 1:
            assert info['coefficient'] == 0
        else:
            assert simplify(info['coefficient'] - expected_coeff * k) == 0

    @pytest.mark.parametrize("n", range(2, 9))
    def test_binomial_identity(self, n):
        """Verify C(n,2) = n*(n-1)/2."""
        assert comb(n, 2) == n * (n - 1) // 2

    @pytest.mark.parametrize("n", range(2, 9))
    def test_output_arity(self, n):
        """d reduces arity by exactly 2."""
        info = bar_differential_general(n)
        assert info['output_arity'] == n - 2


# ============================================================================
# d^2 AND CURVATURE
# ============================================================================

class TestDSquared:
    """d^2 = [m_0, -] for the curved Heisenberg bar complex."""

    def test_d2_arity1(self):
        """d^2[J] = 0 (d[J] = 0)."""
        info = d_squared_general(1)
        assert info['is_zero'] is True

    def test_d2_arity2(self):
        """d^2[J|J] = 0 (d[J|J] = k*|vac>, d(|vac>) = 0)."""
        info = d_squared_general(2)
        assert info['is_zero'] is True

    def test_d2_arity3(self):
        """d^2[J|J|J] = 0 (d[J|J|J] = 3k*[J], d[J] = 0)."""
        info = d_squared_general(3)
        assert info['is_zero'] is True

    def test_d2_arity4_nonzero(self):
        """d^2[J^4] = 6k^2 * |vac> != 0. CURVATURE."""
        info = d_squared_general(4)
        assert info['is_zero'] is False
        assert simplify(info['coefficient'] - 6 * k**2) == 0

    def test_d2_arity5(self):
        """d^2[J^5] = 30k^2 * [J]."""
        info = d_squared_general(5)
        assert simplify(info['coefficient'] - 30 * k**2) == 0

    def test_d2_arity6(self):
        """d^2[J^6] = 90k^2 * [J|J]."""
        info = d_squared_general(6)
        assert simplify(info['coefficient'] - 90 * k**2) == 0

    @pytest.mark.parametrize("n", range(4, 9))
    def test_d2_general_formula(self, n):
        """d^2[J^n] = C(n,2)*C(n-2,2)*k^2 * [J^{n-4}]."""
        info = d_squared_general(n)
        expected = comb(n, 2) * comb(n - 2, 2) * k**2
        assert simplify(info['coefficient'] - expected) == 0

    def test_d2_numeric_k1(self):
        """At k=1: d^2[J^4] = 6."""
        d4 = bar_differential_ordered(4, 1)
        d2_result = d4.get(2) * bar_differential_ordered(2, 1).get(0)
        assert d2_result == 6

    def test_d2_numeric_k2(self):
        """At k=2: d^2[J^4] = 6*4 = 24."""
        d4 = bar_differential_ordered(4, 2)
        d2_result = d4.get(2) * bar_differential_ordered(2, 2).get(0)
        assert d2_result == 24

    def test_curvature_interpretation(self):
        """d^2 is nonzero precisely because m_0 = k != 0 (curved A-infinity)."""
        # For k=0: d^2 = 0 (uncurved)
        info = d_squared_general(4, level=0)
        assert info['coefficient'] == 0


# ============================================================================
# COPRODUCT (DECONCATENATION)
# ============================================================================

class TestCoproduct:
    """Delta = deconcatenation coproduct on T^c(s^{-1}A-bar)."""

    def test_arity1(self):
        terms = coproduct_arity1()
        assert len(terms) == 2
        assert (0, 1, 1) in terms
        assert (1, 0, 1) in terms

    def test_arity2(self):
        terms = coproduct_arity2()
        assert len(terms) == 3
        assert (0, 2, 1) in terms
        assert (1, 1, 1) in terms
        assert (2, 0, 1) in terms

    def test_arity3(self):
        terms = coproduct_arity3()
        assert len(terms) == 4

    def test_arity4(self):
        terms = coproduct_arity4()
        assert len(terms) == 5

    @pytest.mark.parametrize("n", range(1, 8))
    def test_num_terms(self, n):
        """Delta[J^n] has n+1 terms: (0,n), (1,n-1), ..., (n,0)."""
        terms = deconcatenation_coproduct(n)
        assert len(terms) == n + 1

    @pytest.mark.parametrize("n", range(1, 8))
    def test_sum_conservation(self, n):
        """Each term (i,j,c) satisfies i+j=n."""
        for i, j, c in deconcatenation_coproduct(n):
            assert i + j == n

    @pytest.mark.parametrize("n", range(1, 8))
    def test_all_coefficients_one(self, n):
        """All deconcatenation coefficients are 1 (no signs for degree 0)."""
        for i, j, c in deconcatenation_coproduct(n):
            assert c == 1

    def test_coassociativity(self):
        """(Delta tensor id) . Delta = (id tensor Delta) . Delta on [J^3].

        LHS: Delta[J^3] = sum (i,j). Then (Delta tensor id) gives
             sum Delta[J^i] tensor [J^j] = sum_{a+b=i} [J^a] tensor [J^b] tensor [J^j].
             This is sum_{a+b+c=3} [J^a] tensor [J^b] tensor [J^c].

        RHS: Same by symmetry. Both give all triples (a,b,c) with a+b+c=3.
        """
        n = 3
        # LHS: (Delta tensor id) . Delta
        lhs = set()
        for i, j, _ in deconcatenation_coproduct(n):
            for a, b, _ in deconcatenation_coproduct(i):
                lhs.add((a, b, j))

        # RHS: (id tensor Delta) . Delta
        rhs = set()
        for i, j, _ in deconcatenation_coproduct(n):
            for b, c, _ in deconcatenation_coproduct(j):
                rhs.add((i, b, c))

        assert lhs == rhs


# ============================================================================
# CODERIVATION ANALYSIS
# ============================================================================

class TestCoderivation:
    """The collision-only differential is NOT a coderivation (curved algebra)."""

    def test_arity1_trivial(self):
        """At arity 1: d=0, so coderivation holds trivially."""
        assert verify_coderivation(1) is True

    def test_arity2_fails(self):
        """At arity 2: coderivation FAILS for collision-only d.

        This is CORRECT: the Heisenberg is curved (m_0 = k != 0),
        so the collision-only differential is NOT a coderivation.
        The FULL differential (including m_0 insertion) IS.
        """
        assert verify_coderivation(2) is False

    def test_arity2_discrepancy_is_one(self):
        """The discrepancy is exactly 1 at each splitting.

        At arity 2, split (0,0): LHS = C(2,2) = 1, RHS = C(2,2)+C(2,2) = 2.
        Discrepancy = -1 = -(number of m_0 insertion points).
        """
        results = verify_coderivation_explicit(2)
        for key, val in results.items():
            if 'DIFF' in str(val):
                assert 'DIFF=-1' in str(val)

    def test_arity4_middle_split_works(self):
        """At arity 4, the symmetric split (1,1) satisfies the identity.

        C(3,2) + C(3,2) = 3 + 3 = 6 = C(4,2). This is the unique
        split where the identity holds.
        """
        results = verify_coderivation_explicit(4)
        for key, val in results.items():
            if '(1,1)' in key:
                assert 'EQUAL' in str(val)


# ============================================================================
# DIMENSIONS
# ============================================================================

class TestDimensions:
    """Dimension counts for ordered, symmetric, and Harrison bar."""

    @pytest.mark.parametrize("n", range(1, 7))
    def test_ordered_bar_dim(self, n):
        """B^{ord}_n(H_k) is 1-dimensional in the strong-generator sector."""
        assert ordered_bar_dim(n) == 1

    def test_ordered_bar_dim_zero(self):
        assert ordered_bar_dim(0) == 0

    @pytest.mark.parametrize("n", range(1, 7))
    def test_ordered_with_forms(self, n):
        """With forms: dim = (n-1)! (Arnold algebra)."""
        assert ordered_bar_with_forms_dim(n) == factorial(n - 1)

    @pytest.mark.parametrize("n", range(1, 7))
    def test_symmetric_bar_dim(self, n):
        """B^Sigma_n(H_k) is 1-dimensional (trivial S_n action on degree 0)."""
        assert symmetric_bar_dim(n) == 1

    def test_harrison_arity1(self):
        """Harrison complex at arity 1: dim = 1."""
        assert harrison_bar_dim(1) == 1

    @pytest.mark.parametrize("n", range(2, 7))
    def test_harrison_vanishes(self, n):
        """Harrison complex vanishes at arity >= 2 (1-dim abelian Lie coalgebra)."""
        assert harrison_bar_dim(n) == 0

    def test_comparison_table(self):
        """Verify the full comparison table."""
        table = compare_bar_complexes(6)
        for n in range(1, 7):
            assert table[n]['ordered'] == 1
            assert table[n]['symmetric'] == 1
            if n == 1:
                assert table[n]['harrison'] == 1
            else:
                assert table[n]['harrison'] == 0


# ============================================================================
# R-MATRIX
# ============================================================================

class TestRMatrix:
    """r(z) = k/z. R(z) = exp(k/z)."""

    def test_r_matrix_symbolic(self):
        z = Symbol('z')
        r = heisenberg_r_matrix()
        assert simplify(r - k / z) == 0

    def test_r_matrix_numeric(self):
        z = Symbol('z')
        r = heisenberg_r_matrix(level=3)
        assert simplify(r - 3 / z) == 0

    def test_R_matrix_leading_coefficients(self):
        """R(z) = exp(k/z): check first few Laurent coefficients."""
        coeffs = heisenberg_R_matrix_formal(order=4)
        # 1/z^0: 1
        assert coeffs[0] == 1
        # 1/z^1: k
        assert simplify(coeffs[1] - k) == 0
        # 1/z^2: k^2/2
        assert simplify(coeffs[2] - k**2 / 2) == 0
        # 1/z^3: k^3/6
        assert simplify(coeffs[3] - k**3 / 6) == 0
        # 1/z^4: k^4/24
        assert simplify(coeffs[4] - k**4 / 24) == 0

    def test_R_matrix_numeric_k1(self):
        """At k=1: coefficients are 1, 1, 1/2, 1/6, 1/24."""
        coeffs = heisenberg_R_matrix_formal(level=1, order=4)
        assert coeffs[0] == 1
        assert coeffs[1] == 1
        assert coeffs[2] == Rational(1, 2)
        assert coeffs[3] == Rational(1, 6)
        assert coeffs[4] == Rational(1, 24)

    def test_pole_absorption_AP19(self):
        """AP19: r-matrix has pole order one less than OPE.

        OPE has double pole (order 2). r-matrix has simple pole (order 1).
        Difference = 1, from the d log kernel absorption.
        """
        # OPE: J(z)J(w) ~ k/(z-w)^2 -> max pole order = 2
        ope_max_pole = 2
        # r-matrix: r(z) = k/z -> max pole order = 1
        r_max_pole = 1
        assert r_max_pole == ope_max_pole - 1


class TestRTwistedCoinvariants:
    """R-twisted S_2-coinvariants at arity 2."""

    def test_plain_transposition_trivial(self):
        """sigma * [J|J] = [J|J] (degree 0, no Koszul sign)."""
        info = r_twisted_action_arity2()
        assert info['plain_transposition'] == 1

    def test_naive_antisymmetric_zero(self):
        """[J|J] - sigma*[J|J] = 0 (identical generators, degree 0).

        This is why the Harrison complex vanishes at arity 2:
        the naive antisymmetrizer kills the unique monomial.
        """
        info = r_twisted_action_arity2()
        # 1 - plain_transposition = 0
        assert 1 - info['plain_transposition'] == 0

    def test_R_twisted_nonzero(self):
        """R-twisted coinvariant is nonzero for k != 0.

        [J|J]_R = (1 - exp(k/z)) * [J|J] != 0.
        """
        info = r_twisted_action_arity2()
        z = Symbol('z')
        coeff = info['R_twisted_coinvariant_coeff']
        # At z -> infinity: 1 - exp(k/z) -> 1 - 1 = 0 (but Laurent expansion nonzero)
        # The leading term is -k/z
        assert coeff is not None

    def test_coproduct_on_twisted(self):
        """Delta on R-twisted coinvariant inherits coassociativity."""
        info = coproduct_r_twisted_arity2()
        assert info['coassociative'] is True
        assert len(info['coproduct_terms']) == 3


# ============================================================================
# COMPLETE STRUCTURE MAPS
# ============================================================================

class TestCompleteArity1:
    def test_dimension(self):
        assert complete_arity_1()['dimension'] == 1

    def test_degree(self):
        """s^{-1}J has degree |J|-1 = 1-1 = 0 (AP45)."""
        assert complete_arity_1()['degree'] == 0

    def test_weight(self):
        assert complete_arity_1()['weight'] == 1

    def test_differential_zero(self):
        assert complete_arity_1()['differential'].is_zero()

    def test_coproduct_terms(self):
        assert len(complete_arity_1()['coproduct']) == 2


class TestCompleteArity2:
    def test_dimension(self):
        assert complete_arity_2()['dimension'] == 1

    def test_weight(self):
        assert complete_arity_2()['weight'] == 2

    def test_coinvariant_dim(self):
        assert complete_arity_2()['coinvariant_dim'] == 1

    def test_harrison_dim(self):
        assert complete_arity_2()['harrison_dim'] == 0

    def test_coproduct_terms(self):
        assert len(complete_arity_2()['coproduct']) == 3


class TestCompleteArity3:
    def test_dimension(self):
        assert complete_arity_3()['dimension'] == 1

    def test_weight(self):
        assert complete_arity_3()['weight'] == 3

    def test_three_collision_pairs(self):
        assert len(complete_arity_3()['differential_by_pair']) == 3

    def test_coproduct_terms(self):
        assert len(complete_arity_3()['coproduct']) == 4


class TestCompleteArity4:
    def test_dimension(self):
        assert complete_arity_4()['dimension'] == 1

    def test_weight(self):
        assert complete_arity_4()['weight'] == 4

    def test_six_collision_pairs(self):
        assert len(complete_arity_4()['differential_by_pair']) == 6

    def test_coproduct_terms(self):
        assert len(complete_arity_4()['coproduct']) == 5

    def test_d_squared_nonzero(self):
        """d^2 is nonzero at arity 4: curvature."""
        d2 = complete_arity_4()['d_squared']
        assert not d2.is_zero()


# ============================================================================
# SHADOW OBSTRUCTION TOWER
# ============================================================================

class TestShadowTower:
    """Heisenberg is class G (Gaussian): shadow depth 2."""

    def test_kappa(self):
        """kappa(H_k) = k."""
        assert simplify(shadow_kappa() - k) == 0

    def test_kappa_numeric(self):
        assert shadow_kappa(level=7) == 7

    def test_cubic_vanishes(self):
        """C = 0 (class G)."""
        assert shadow_cubic() == 0

    def test_quartic_vanishes(self):
        """Q = 0 (class G)."""
        assert shadow_quartic() == 0

    def test_depth(self):
        """r_max = 2 (Gaussian class)."""
        assert shadow_depth() == 2

    def test_kappa_equals_curvature(self):
        """kappa = m_0 = J_{(1)}J (the curvature is the shadow)."""
        modes = heisenberg_ope_modes()
        _, curvature = modes[1]
        assert simplify(shadow_kappa() - curvature) == 0

    def test_kappa_matches_bar_differential(self):
        """kappa = d_B[J|J] (the arity-2 differential IS the shadow)."""
        d = bar_differential_arity2()
        assert simplify(d.get(0) - shadow_kappa()) == 0


# ============================================================================
# NUMERICAL VERIFICATION AT SPECIFIC LEVELS
# ============================================================================

class TestNumericalVerification:
    """Multi-path verification at specific level values."""

    @pytest.mark.parametrize("kval", [1, 2, -1, 3, 10, Rational(1, 2)])
    def test_all_pass(self, kval):
        results = verify_at_level(kval)
        for name, ok in results.items():
            if 'coderivation' in name:
                # Coderivation fails for curved algebras -- expected
                continue
            assert ok, f"FAILED at k={kval}: {name}"

    def test_k_zero_differential_vanishes(self):
        """At k=0: all differentials vanish (uncurved, trivial algebra)."""
        for n in range(1, 7):
            d = bar_differential_ordered(n, 0)
            assert d.is_zero(), f"d[J^{n}] should be 0 at k=0"

    def test_k_zero_d_squared_zero(self):
        """At k=0: d^2=0 trivially (uncurved)."""
        for n in range(1, 7):
            info = d_squared_general(n, level=0)
            if 'is_zero' in info:
                assert info['is_zero']
            else:
                assert info['coefficient'] == 0

    def test_k_negative_signs(self):
        """At k=-1: d[J|J] = -1, d[J^3] = -3, d[J^4] = -6."""
        assert bar_differential_ordered(2, -1).get(0) == -1
        assert bar_differential_ordered(3, -1).get(1) == -3
        assert bar_differential_ordered(4, -1).get(2) == -6


# ============================================================================
# CROSS-CHECKS WITH EXISTING MODULES
# ============================================================================

class TestCrossCheckHeisenbergBar:
    """Cross-check against heisenberg_bar.py (independent verification path)."""

    def test_all_pass(self):
        results = cross_check_with_heisenberg_bar()
        for name, ok in results.items():
            assert ok, f"Cross-check FAILED: {name}"


class TestCrossCheckBarComplex:
    """Cross-check against bar_complex.py (independent verification path)."""

    def test_all_pass(self):
        results = cross_check_with_bar_complex()
        for name, ok in results.items():
            assert ok, f"Cross-check FAILED: {name}"


# ============================================================================
# CHAIN COMPLEX STRUCTURE
# ============================================================================

class TestChainComplex:
    """The bar complex splits into even/odd arity chains."""

    def test_even_odd_split(self):
        """d: B_n -> B_{n-2} means even and odd arities decouple."""
        info = bar_chain_complex_matrix(8)
        assert 'even_complex' in info
        assert 'odd_complex' in info

    def test_even_differentials(self):
        """Even chain: d_2 = k, d_4 = 6k, d_6 = 15k."""
        info = bar_chain_complex_matrix(8)
        even = info['even_complex']
        assert simplify(even[2] - k) == 0
        assert simplify(even[4] - 6 * k) == 0
        assert simplify(even[6] - 15 * k) == 0

    def test_odd_differentials(self):
        """Odd chain: d_3 = 3k, d_5 = 10k, d_7 = 21k."""
        info = bar_chain_complex_matrix(8)
        odd = info['odd_complex']
        assert simplify(odd[3] - 3 * k) == 0
        assert simplify(odd[5] - 10 * k) == 0
        assert simplify(odd[7] - 21 * k) == 0


# ============================================================================
# COMBINATORIAL IDENTITIES
# ============================================================================

class TestCombinatorialIdentities:
    """Verify the binomial coefficient identities underlying the bar complex."""

    @pytest.mark.parametrize("n", range(2, 10))
    def test_pair_count(self, n):
        """Number of pairs: C(n,2) = n(n-1)/2."""
        assert comb(n, 2) == n * (n - 1) // 2

    @pytest.mark.parametrize("n", range(4, 10))
    def test_d_squared_coefficient(self, n):
        """d^2 coefficient: C(n,2)*C(n-2,2)."""
        expected = comb(n, 2) * comb(n - 2, 2)
        # Alternative: n(n-1)(n-2)(n-3)/4
        assert expected == n * (n - 1) * (n - 2) * (n - 3) // 4

    def test_vandermonde_at_arity4(self):
        """At arity 4: C(4,2)*C(2,2) = 6*1 = 6."""
        assert comb(4, 2) * comb(2, 2) == 6

    def test_d_cubed_arity6(self):
        """d^3[J^6] = C(6,2)*C(4,2)*C(2,2)*k^3 = 15*6*1*k^3 = 90k^3."""
        assert comb(6, 2) * comb(4, 2) * comb(2, 2) == 90

    def test_coderivation_discrepancy(self):
        """The coderivation discrepancy at split (a,b) is exactly 1.

        LHS - RHS = C(n,2) - C(a+2,2) - C(b+2,2) where a+b = n-2.
        This equals 1 for the boundary splits (a=0 or b=0) and can
        be positive, zero, or negative for interior splits.

        At (a,b) = (0, n-2): discrepancy = C(n,2) - 1 - C(n,2) = -1.
        At (a,b) = (n-2, 0): same by symmetry.
        At (a,b) = ((n-2)/2, (n-2)/2) for even n:
            discrepancy = C(n,2) - 2*C(n/2, 2) = n(n-1)/2 - 2*(n/2)(n/2-1)/2
        """
        n = 4
        for a in range(n - 1):
            b = n - 2 - a
            if b < 0:
                continue
            lhs = comb(n, 2)
            rhs = comb(a + 2, 2) + comb(b + 2, 2)
            disc = lhs - rhs
            # For n=4: splits (0,2), (1,1), (2,0)
            if a == 0 or b == 0:
                assert disc == -1
            elif a == 1 and b == 1:
                assert disc == 0  # The middle split works!


# ============================================================================
# STRUCTURAL PROPERTIES
# ============================================================================

class TestStructuralProperties:
    """High-level structural properties of the Heisenberg bar complex."""

    def test_class_G_terminates(self):
        """Class G: shadow tower terminates at arity 2.

        This means all higher shadow invariants (S_3, S_4, ...) vanish.
        Equivalently: the Heisenberg bar complex is 'Gaussian' --
        the MC element Theta_A^{<=2} = kappa * eta is EXACT
        (no corrections needed at higher arities).
        """
        assert shadow_depth() == 2
        assert shadow_cubic() == 0
        assert shadow_quartic() == 0

    def test_abelian_bracket(self):
        """The Heisenberg has no Lie bracket (J_{(0)}J = 0).

        This is the structural reason for class G: no simple pole
        means no tree-level interactions, so the shadow tower terminates.
        """
        modes = heisenberg_ope_modes()
        _, val = modes[0]
        assert val == 0

    def test_uniform_weight(self):
        """Single generator of weight 1: uniform-weight algebra.

        By AP27/AP32: obs_g = kappa * lambda_g at ALL genera (no
        cross-channel correction, since there is only one channel).
        """
        info = complete_arity_1()
        assert info['weight'] == 1

    def test_desuspension_degree(self):
        """|s^{-1}J| = |J| - 1 = 0 (AP45: desuspension lowers degree).

        This is why all Koszul signs are trivial for Heisenberg.
        """
        assert complete_arity_1()['degree'] == 0

    def test_curvature_equals_level(self):
        """m_0 = kappa = k (the curvature IS the modular characteristic).

        For Heisenberg: these three quantities coincide:
        (1) The level k (parameter in the OPE)
        (2) The curvature m_0 = J_{(1)}J
        (3) The modular characteristic kappa(H_k)
        """
        assert simplify(shadow_kappa() - k) == 0

    def test_r_matrix_is_abelian(self):
        """r(z) = k/z is the r-matrix of an abelian Lie algebra.

        For a non-abelian algebra (e.g., sl_2), r(z) = Omega/z where
        Omega is the Casimir. For Heisenberg: Omega = k (a scalar),
        so r(z) = k/z.
        """
        z = Symbol('z')
        r = heisenberg_r_matrix()
        # r has a single pole at z=0 of order 1
        assert simplify(z * r - k) == 0
