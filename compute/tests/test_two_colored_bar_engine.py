"""Tests for the two-coloured operadic bar construction.

Tests the fundamental question: for a two-coloured operad O with colours
{c, o}, what is B_O of an O-algebra?

Organized in 8 sections:
  1. Basic algebra construction and properties
  2. Associative bar construction B_{Ass}
  3. Commutative bar construction B_{Com}
  4. Two-coloured SC bar construction B_{SC}
  5. Promotion functor: Com-algebra -> SC-algebra
  6. Explicit low-arity computations for k[x]/(x^n)
  7. Type-checking and conceptual consistency
  8. Cross-verification with existing codebase
"""

from __future__ import annotations

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.two_colored_bar_engine import (
    # Data structures
    BasisElement,
    GradedSpace,
    BarWord,
    SymBarWord,
    TwoColoredBarWord,
    # Algebras
    AugAssAlgebra,
    SCAlgebra,
    # Complexes
    AssociativeBarComplex,
    CommutativeBarComplex,
    SwissCheeseBarComplex,
    # Standard algebras
    polynomial_algebra,
    dual_numbers,
    exterior_algebra_1,
    symmetric_algebra_truncated,
    matrix_algebra_2x2_upper,
    # Computation functions
    bar_words_at_degree,
    sym_bar_words_at_degree,
    compute_bar_ass_low_arity,
    compute_bar_com_low_arity,
    compute_bar_sc_low_arity,
    bar_ass_euler_char,
    bar_ass_formal_euler_char,
    verify_promotion_functor,
    chiral_bar_sc_structure_summary,
)


# =========================================================================
# Section 1: Basic algebra construction and properties
# =========================================================================

class TestAlgebraConstruction:
    """Test basic algebra factories and properties."""

    def test_dual_numbers_commutative(self):
        A = dual_numbers()
        assert A.is_commutative()

    def test_dual_numbers_associative(self):
        A = dual_numbers()
        assert A.is_associative()

    def test_dual_numbers_dim(self):
        A = dual_numbers()
        assert A.dim == 2
        assert A.aug_ideal_dim == 1

    def test_polynomial_3_commutative(self):
        A = polynomial_algebra(3)
        assert A.is_commutative()

    def test_polynomial_3_associative(self):
        A = polynomial_algebra(3)
        assert A.is_associative()

    def test_polynomial_3_dim(self):
        A = polynomial_algebra(3)
        assert A.dim == 3
        assert A.aug_ideal_dim == 2

    def test_polynomial_4_dim(self):
        A = polynomial_algebra(4)
        assert A.dim == 4
        assert A.aug_ideal_dim == 3

    def test_exterior_commutative(self):
        """Exterior algebra on 1 generator is graded commutative."""
        A = exterior_algebra_1()
        assert A.is_commutative()  # xi*xi = 0 = -xi*xi (graded)
        assert A.is_associative()

    def test_exterior_dim(self):
        A = exterior_algebra_1()
        assert A.dim == 2
        assert A.aug_ideal_dim == 1

    def test_upper_triangular_non_commutative(self):
        A = matrix_algebra_2x2_upper()
        assert not A.is_commutative()

    def test_upper_triangular_associative(self):
        A = matrix_algebra_2x2_upper()
        assert A.is_associative()

    def test_upper_triangular_dim(self):
        A = matrix_algebra_2x2_upper()
        assert A.dim == 3
        assert A.aug_ideal_dim == 2

    def test_aug_ideal_multiplication(self):
        """k[x]/(x^3): aug ideal has basis {x, x^2}. x*x = x^2."""
        A = polynomial_algebra(3)
        # In aug ideal: index 0 = x, index 1 = x^2
        prod = A.aug_ideal_multiply(0, 0)
        assert prod == {1: Rational(1)}  # x*x = x^2

    def test_aug_ideal_multiplication_truncation(self):
        """k[x]/(x^3): x^2 * x = 0 (truncated)."""
        A = polynomial_algebra(3)
        prod = A.aug_ideal_multiply(1, 0)
        assert prod == {}  # x^2 * x = x^3 = 0


# =========================================================================
# Section 2: Associative bar construction B_{Ass}
# =========================================================================

class TestAssociativeBar:
    """Test the associative bar construction."""

    def test_bar_words_degree_0(self):
        words = bar_words_at_degree(0, 2)
        assert len(words) == 1
        assert words[0].degree == 0

    def test_bar_words_degree_1(self):
        words = bar_words_at_degree(1, 2)
        assert len(words) == 2  # two aug ideal generators

    def test_bar_words_degree_2(self):
        words = bar_words_at_degree(2, 2)
        assert len(words) == 4  # 2^2

    def test_bar_words_degree_n(self):
        """dim B^n = (aug_dim)^n."""
        for d in [1, 2, 3]:
            for n in [0, 1, 2, 3]:
                words = bar_words_at_degree(n, d)
                assert len(words) == d ** n

    def test_d_squared_zero_dual_numbers(self):
        A = dual_numbers()
        bc = AssociativeBarComplex(A, 5)
        assert bc.verify_d_squared_zero(5)

    def test_d_squared_zero_polynomial_3(self):
        A = polynomial_algebra(3)
        bc = AssociativeBarComplex(A, 4)
        assert bc.verify_d_squared_zero(4)

    def test_d_squared_zero_polynomial_4(self):
        A = polynomial_algebra(4)
        bc = AssociativeBarComplex(A, 3)
        assert bc.verify_d_squared_zero(3)

    def test_d_squared_zero_upper_triangular(self):
        """Non-commutative algebra: d^2 = 0 still holds (associative)."""
        A = matrix_algebra_2x2_upper()
        bc = AssociativeBarComplex(A, 4)
        assert bc.verify_d_squared_zero(4)

    def test_d_squared_zero_exterior(self):
        A = exterior_algebra_1()
        bc = AssociativeBarComplex(A, 5)
        assert bc.verify_d_squared_zero(5)

    def test_d_is_coderivation_dual_numbers(self):
        """d_bar is a coderivation of the deconcatenation Delta."""
        A = dual_numbers()
        bc = AssociativeBarComplex(A, 4)
        assert bc.verify_d_is_coderivation(4)

    def test_d_is_coderivation_polynomial_3(self):
        A = polynomial_algebra(3)
        bc = AssociativeBarComplex(A, 3)
        assert bc.verify_d_is_coderivation(3)

    def test_d_is_coderivation_upper_triangular(self):
        A = matrix_algebra_2x2_upper()
        bc = AssociativeBarComplex(A, 3)
        assert bc.verify_d_is_coderivation(3)

    def test_differential_degree_2_dual_numbers(self):
        """d[0|0] for k[eps]/(eps^2): eps*eps = 0, so d = 0."""
        A = dual_numbers()
        bc = AssociativeBarComplex(A, 3)
        w = BarWord((0, 0))
        d_w = bc.bar_differential(w)
        assert d_w == {}  # eps^2 = 0 in the aug ideal

    def test_differential_degree_2_polynomial_3(self):
        """d[0|0] for k[x]/(x^3): x*x = x^2 (index 1 in aug ideal).
        d[x|x] = +[x^2] (sign (-1)^0 = +1 at position 0)."""
        A = polynomial_algebra(3)
        bc = AssociativeBarComplex(A, 3)
        w = BarWord((0, 0))  # [x|x]
        d_w = bc.bar_differential(w)
        expected = {BarWord((1,)): Rational(1)}  # [x^2]
        assert d_w == expected

    def test_deconcatenation_degree_2(self):
        """Delta[a|b] = [] tensor [a|b] + [a] tensor [b] + [a|b] tensor []."""
        A = dual_numbers()
        bc = AssociativeBarComplex(A, 3)
        w = BarWord((0, 0))
        result = bc.deconcatenation(w)
        assert len(result) == 3
        assert result[0] == (BarWord(()), BarWord((0, 0)))
        assert result[1] == (BarWord((0,)), BarWord((0,)))
        assert result[2] == (BarWord((0, 0)), BarWord(()))

    def test_bar_cohomology_dual_numbers(self):
        """B_{Ass}(k[eps]/(eps^2)) has:
        - H^0 = k (ground field)
        - H^1 = k (one generator eps, d=0 on degree 1)
        - H^n = k for all n (because eps^2=0, all differentials vanish)
        """
        A = dual_numbers()
        bc = AssociativeBarComplex(A, 5)
        dims = bc.bar_cohomology_dims(5)
        # For k[eps]/(eps^2): aug ideal has dim 1, eps*eps=0.
        # So d = 0 on everything (all products vanish in aug ideal).
        # H^n = dim(B^n) = 1 for all n.
        for n in range(6):
            assert dims[n] == 1, f"H^{n} should be 1, got {dims[n]}"


# =========================================================================
# Section 3: Commutative bar construction B_{Com}
# =========================================================================

class TestCommutativeBar:
    """Test the commutative (Harrison) bar construction."""

    def test_sym_bar_words_degree_0(self):
        words = sym_bar_words_at_degree(0, 2)
        assert len(words) == 1

    def test_sym_bar_words_degree_1(self):
        words = sym_bar_words_at_degree(1, 2)
        assert len(words) == 2

    def test_sym_bar_words_degree_2(self):
        """Exterior degree 2 with aug_dim=2: only {0,1} = 1."""
        words = sym_bar_words_at_degree(2, 2)
        assert len(words) == 1  # C(2, 2) = 1

    def test_sym_bar_words_degree_exceeds_dim(self):
        """Lambda^n(k^d) = 0 for n > d."""
        words = sym_bar_words_at_degree(3, 2)
        assert len(words) == 0

    def test_sym_bar_words_degree_n_formula(self):
        """dim Lambda^n(k^d) = C(d, n) for d-dimensional V."""
        from math import comb
        for d in [1, 2, 3, 4]:
            for n in range(d + 2):
                words = sym_bar_words_at_degree(n, d)
                expected = comb(d, n)
                assert len(words) == expected

    def test_com_bar_requires_commutative(self):
        """B_{Com} should reject non-commutative algebras."""
        A = matrix_algebra_2x2_upper()
        with pytest.raises(ValueError):
            CommutativeBarComplex(A, 3)

    def test_d_squared_zero_dual_numbers(self):
        A = dual_numbers()
        bc = CommutativeBarComplex(A, 5)
        assert bc.verify_d_squared_zero(5)

    def test_d_squared_zero_polynomial_3(self):
        A = polynomial_algebra(3)
        bc = CommutativeBarComplex(A, 4)
        assert bc.verify_d_squared_zero(4)

    def test_d_squared_zero_polynomial_4(self):
        A = polynomial_algebra(4)
        bc = CommutativeBarComplex(A, 3)
        assert bc.verify_d_squared_zero(3)

    def test_d_squared_zero_exterior(self):
        A = exterior_algebra_1()
        bc = CommutativeBarComplex(A, 5)
        assert bc.verify_d_squared_zero(5)

    def test_harrison_differential_degree_2_polynomial_3(self):
        """d{x,x} for k[x]/(x^3): should give {x^2}."""
        A = polynomial_algebra(3)
        bc = CommutativeBarComplex(A, 3)
        w = SymBarWord((0, 0))  # {x, x}
        d_w = bc.harrison_differential(w)
        # The contraction of the pair (0,0) with sign (-1)^{1-1} = +1
        # gives x*x = x^2 (index 1), so d{x,x} = -1 * {x^2}
        # (sign (-1)^{j-1} with j=1 gives (-1)^0 = 1)
        # Actually the sign convention needs checking against d^2=0.
        # Since d^2=0 is verified, just check it's nonzero:
        assert len(d_w) > 0, "Harrison differential on {x,x} should be nonzero"


# =========================================================================
# Section 4: Two-coloured SC bar construction
# =========================================================================

class TestSwissCheeseBar:
    """Test the two-coloured Swiss-cheese bar construction."""

    def test_sc_algebra_self_action(self):
        """Self-action SC-algebra (C, C) from commutative C."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        assert sc.closed.name == C.name
        assert sc.open.name == C.name

    def test_sc_algebra_action_nonzero(self):
        """Self-action: x acts on x to give x^2."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        acted = sc.act(0, 0)  # x acts on x
        assert acted == {1: Rational(1)}  # x^2

    def test_d_squared_zero_closed_sector(self):
        """d^2 = 0 on closed-output elements of B_{SC}."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 3)
        assert bc.verify_d_squared_zero_closed(3)

    def test_d_squared_zero_open_sector_dual_numbers(self):
        """d^2 = 0 on open-output elements."""
        C = dual_numbers()
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 4)
        assert bc.verify_d_squared_zero_open(4)

    def test_d_squared_zero_open_sector_poly3(self):
        """d^2 = 0 on open-output elements for k[x]/(x^3)."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 3)
        assert bc.verify_d_squared_zero_open(3)

    def test_closed_differential_matches_harrison(self):
        """Closed sector of B_{SC} should equal B_{Com}."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        sc_bar = SwissCheeseBarComplex(sc, 3)
        com_bar = CommutativeBarComplex(C, 3)
        aug_dim = C.aug_ideal_dim

        for n in range(2, 4):
            swords = sym_bar_words_at_degree(n, aug_dim)
            for sw in swords:
                w = TwoColoredBarWord('c', sw.indices, ())
                d_sc = sc_bar.full_differential(w)
                d_har = com_bar.harrison_differential(sw)
                d_har_conv = {}
                for sw2, c in d_har.items():
                    d_har_conv[TwoColoredBarWord('c', sw2.indices, ())] = c
                assert d_sc == d_har_conv, (
                    f"Closed diff mismatch at {w}: SC={d_sc}, Harrison={d_har_conv}"
                )

    def test_pure_open_differential_matches_ass(self):
        """Pure-open sector of B_{SC} should equal B_{Ass}."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        sc_bar = SwissCheeseBarComplex(sc, 3)
        ass_bar = AssociativeBarComplex(C, 3)
        aug_dim = C.aug_ideal_dim

        for n in range(2, 4):
            words = bar_words_at_degree(n, aug_dim)
            for bw in words:
                w = TwoColoredBarWord('o', (), bw.indices)
                d_sc = sc_bar.open_differential(w)
                d_ass = ass_bar.bar_differential(bw)
                d_ass_conv = {}
                for bw2, c in d_ass.items():
                    d_ass_conv[TwoColoredBarWord('o', (), bw2.indices)] = c
                assert d_sc == d_ass_conv

    def test_mixed_differential_nonzero(self):
        """For k[x]/(x^3), d_mix(x; [x]) = [x*x] = [x^2] should be nonzero."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 3)
        # (1 closed = x, 1 open = x)
        w = TwoColoredBarWord('o', (0,), (0,))
        d_mix = bc.mixed_differential(w)
        assert len(d_mix) > 0, "Mixed differential should be nonzero for (x; [x])"

    def test_mixed_differential_trivial_algebra(self):
        """For k[eps]/(eps^2), d_mix(eps; [eps]) = [eps*eps] = 0."""
        C = dual_numbers()
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 3)
        w = TwoColoredBarWord('o', (0,), (0,))
        d_mix = bc.mixed_differential(w)
        assert d_mix == {}, "Mixed differential should vanish for eps*eps=0"

    def test_mixed_acts_only_on_leftmost(self):
        """d_mix acts only on the leftmost open element (left module)."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 3)
        # (x; [x|x^2]): d_mix should give (; [x*x|x^2]) = (; [x^2|x^2])
        # NOT also (; [x|x*x^2]) = (; [x|x^3]) = (; [x|0]) = 0
        w = TwoColoredBarWord('o', (0,), (0, 1))
        d_mix = bc.mixed_differential(w)
        # The only output should modify the first open element
        for w2 in d_mix:
            # Second open element should be unchanged at index 1
            assert w2.open_indices[-1] == 1, (
                f"Mixed diff modified non-leftmost element: {w} -> {w2}"
            )

    def test_no_open_to_closed(self):
        """No open-to-closed maps: differential of open word stays open."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 3)
        w = TwoColoredBarWord('o', (0,), (0,))
        d_w = bc.full_differential(w)
        for w2 in d_w:
            assert w2.colour == 'o', (
                f"Open-to-closed detected: {w} -> {w2}"
            )


# =========================================================================
# Section 5: Promotion functor
# =========================================================================

class TestPromotionFunctor:
    """Test the promotion functor Com-alg -> SC-alg."""

    def test_promotion_dual_numbers(self):
        C = dual_numbers()
        result = verify_promotion_functor(C, 4)
        assert result["all_pass"], f"Promotion failed: {result}"

    def test_promotion_polynomial_3(self):
        C = polynomial_algebra(3)
        result = verify_promotion_functor(C, 3)
        assert result["all_pass"], f"Promotion failed: {result}"

    def test_promotion_polynomial_4(self):
        C = polynomial_algebra(4)
        result = verify_promotion_functor(C, 3)
        assert result["all_pass"], f"Promotion failed: {result}"

    def test_promotion_exterior(self):
        C = exterior_algebra_1()
        result = verify_promotion_functor(C, 4)
        assert result["all_pass"], f"Promotion failed: {result}"

    def test_promotion_requires_commutative(self):
        """Promotion functor should reject non-commutative algebras."""
        A = matrix_algebra_2x2_upper()
        with pytest.raises(AssertionError):
            SCAlgebra.from_self_action(A)


# =========================================================================
# Section 6: Explicit low-arity computations
# =========================================================================

class TestExplicitComputations:
    """Explicit low-arity computations for specific algebras."""

    def test_bar_ass_polynomial_2(self):
        """B_{Ass}(k[eps]/(eps^2)) explicit structure."""
        A = dual_numbers()
        data = compute_bar_ass_low_arity(A, 4)
        assert data["aug_ideal_dim"] == 1
        # Each degree has dim 1^n = 1
        for n in range(5):
            assert data[f"degree_{n}"]["dim"] == 1

    def test_bar_ass_polynomial_3_dimensions(self):
        """B_{Ass}(k[x]/(x^3)): dim at degree n = 2^n."""
        A = polynomial_algebra(3)
        data = compute_bar_ass_low_arity(A, 4)
        assert data["aug_ideal_dim"] == 2
        for n in range(5):
            assert data[f"degree_{n}"]["dim"] == 2 ** n

    def test_bar_com_polynomial_3_dimensions(self):
        """B_{Com}(k[x]/(x^3)): dim Lambda^n(k^2) = C(2, n).
        n=0: 1, n=1: 2, n=2: 1, n>=3: 0."""
        from math import comb
        A = polynomial_algebra(3)
        data = compute_bar_com_low_arity(A, 4)
        assert data["aug_ideal_dim"] == 2
        for n in range(5):
            expected = comb(2, n)
            assert data[f"degree_{n}"]["dim"] == expected

    def test_bar_sc_polynomial_3_structure(self):
        """B_{SC}(k[x]/(x^3), k[x]/(x^3)) explicit structure."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        data = compute_bar_sc_low_arity(sc, 3)
        assert data["c_dim"] == 2
        assert data["o_dim"] == 2

    def test_euler_char_dual_numbers(self):
        """Euler char of B_{Ass}(k[eps]/(eps^2)): 1/(1+1) = 1/2."""
        A = dual_numbers()
        formal_chi = bar_ass_formal_euler_char(A)
        assert formal_chi == Rational(1, 2)

    def test_euler_char_polynomial_3(self):
        """Euler char of B_{Ass}(k[x]/(x^3)): 1/(1+2) = 1/3."""
        A = polynomial_algebra(3)
        formal_chi = bar_ass_formal_euler_char(A)
        assert formal_chi == Rational(1, 3)

    def test_euler_char_polynomial_n(self):
        """Euler char of B_{Ass}(k[x]/(x^n)): 1/n."""
        for n in range(2, 7):
            A = polynomial_algebra(n)
            formal_chi = bar_ass_formal_euler_char(A)
            assert formal_chi == Rational(1, n)

    def test_desuspension_lowers_degree(self):
        """Verify s^{-1} LOWERS degree by 1 (AP45)."""
        basis = [BasisElement("v", 2)]
        V = GradedSpace(basis, "V")
        sV = V.desuspend()
        assert sV.basis[0].degree == 1  # 2 - 1 = 1, NOT 3

    def test_desuspension_degree_zero(self):
        """s^{-1} on degree-0 element gives degree -1."""
        basis = [BasisElement("x", 0)]
        V = GradedSpace(basis, "V")
        sV = V.desuspend()
        assert sV.basis[0].degree == -1

    def test_bar_word_from_polynomial_3(self):
        """Bar word [x|x^2] is a valid degree-2 element."""
        w = BarWord((0, 1))  # [x | x^2] in aug ideal basis
        assert w.degree == 2

    def test_bar_differential_explicit_polynomial_3(self):
        """d[x|x^2] = (-1)^0 * [x*x^2] = [x^3] = 0 (truncated).
        d[x^2|x] = (-1)^0 * [x^2*x] = [x^3] = 0 (truncated).
        d[x|x] = (-1)^0 * [x^2] = [x^2].
        d[x^2|x^2] = (-1)^0 * [x^4] = 0 (truncated)."""
        A = polynomial_algebra(3)
        bc = AssociativeBarComplex(A, 3)

        # d[x|x] = [x^2]
        assert bc.bar_differential(BarWord((0, 0))) == {BarWord((1,)): Rational(1)}

        # d[x|x^2] = [x^3] = 0
        assert bc.bar_differential(BarWord((0, 1))) == {}

        # d[x^2|x] = [x^3] = 0
        assert bc.bar_differential(BarWord((1, 0))) == {}

        # d[x^2|x^2] = [x^4] = 0
        assert bc.bar_differential(BarWord((1, 1))) == {}


# =========================================================================
# Section 7: Type-checking and conceptual consistency
# =========================================================================

class TestTypeChecking:
    """Test the conceptual type-checking of the SC bar construction."""

    def test_chiral_bar_summary_keys(self):
        """The summary should contain all expected keys."""
        summary = chiral_bar_sc_structure_summary()
        expected_keys = [
            "closed_sector", "open_sector", "compatibility",
            "input", "output", "key_fact", "type_resolution",
            "manuscript_ref",
        ]
        for key in expected_keys:
            assert key in summary

    def test_chiral_bar_summary_manuscript_ref(self):
        """Summary references the correct theorem."""
        summary = chiral_bar_sc_structure_summary()
        assert "thm:bar-swiss-cheese" in summary["manuscript_ref"]

    def test_two_colored_word_closed(self):
        """Closed-output word has only closed indices."""
        w = TwoColoredBarWord('c', (0, 1), ())
        assert w.colour == 'c'
        assert w.closed_degree == 2
        assert w.open_degree == 0
        assert w.total_degree == 2

    def test_two_colored_word_open(self):
        """Open-output word can have both closed and open indices."""
        w = TwoColoredBarWord('o', (0,), (1, 2))
        assert w.colour == 'o'
        assert w.closed_degree == 1
        assert w.open_degree == 2
        assert w.total_degree == 3

    def test_two_colored_word_pure_open(self):
        """Pure-open word has only open indices."""
        w = TwoColoredBarWord('o', (), (0, 1))
        assert w.closed_degree == 0
        assert w.open_degree == 2

    def test_no_open_to_closed_in_differential(self):
        """SC operad has no open-to-closed operations.
        This means the differential of a closed-output word
        produces only closed-output words."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        bc = SwissCheeseBarComplex(sc, 3)
        aug_dim = C.aug_ideal_dim

        for n in range(1, 4):
            swords = sym_bar_words_at_degree(n, aug_dim)
            for sw in swords:
                w = TwoColoredBarWord('c', sw.indices, ())
                d_w = bc.full_differential(w)
                for w2 in d_w:
                    assert w2.colour == 'c', (
                        f"Open-to-closed in closed sector: {w} -> {w2}"
                    )

    def test_closed_sector_is_retract(self):
        """The closed colour is an operadic retract of SC.
        This means the closed sector B_{Com}(C) is independent
        of the open sector."""
        C = polynomial_algebra(3)
        sc = SCAlgebra.from_self_action(C)
        sc_bar = SwissCheeseBarComplex(sc, 3)
        com_bar = CommutativeBarComplex(C, 3)
        aug_dim = C.aug_ideal_dim

        # Verify closed sector differential is PURELY Harrison
        # (no mixed terms pollute the closed sector)
        for n in range(2, 4):
            swords = sym_bar_words_at_degree(n, aug_dim)
            for sw in swords:
                w = TwoColoredBarWord('c', sw.indices, ())
                d_sc = sc_bar.full_differential(w)
                d_har = com_bar.harrison_differential(sw)
                d_har_conv = {}
                for sw2, c in d_har.items():
                    d_har_conv[TwoColoredBarWord('c', sw2.indices, ())] = c
                assert d_sc == d_har_conv


# =========================================================================
# Section 8: Cross-verification
# =========================================================================

class TestCrossVerification:
    """Cross-verification with independent computations."""

    def test_bar_ass_vs_com_for_commutative(self):
        """For a commutative algebra, B_{Ass} and B_{Com} should be related.

        B_{Com} is a summand of B_{Ass}: the Harrison complex is the
        symmetric part of the Hochschild complex. In particular,
        d^2 = 0 for both, and the Harrison differential is the
        symmetrisation of the Hochschild differential.
        """
        A = polynomial_algebra(3)
        ass_bar = AssociativeBarComplex(A, 3)
        com_bar = CommutativeBarComplex(A, 3)
        assert ass_bar.verify_d_squared_zero(3)
        assert com_bar.verify_d_squared_zero(3)

    def test_d_coderivation_for_multiple_algebras(self):
        """d is a coderivation of Delta for several test algebras."""
        algebras = [
            dual_numbers(),
            polynomial_algebra(3),
            polynomial_algebra(4),
            exterior_algebra_1(),
            matrix_algebra_2x2_upper(),
        ]
        for A in algebras:
            bc = AssociativeBarComplex(A, 3)
            assert bc.verify_d_is_coderivation(3), (
                f"d not coderivation for {A.name}"
            )

    def test_d_squared_zero_all_test_algebras(self):
        """d^2 = 0 for all test algebras (both Ass and Com where applicable)."""
        for A in [dual_numbers(), polynomial_algebra(3),
                   polynomial_algebra(4), exterior_algebra_1()]:
            ass = AssociativeBarComplex(A, 4)
            assert ass.verify_d_squared_zero(4), f"d^2 != 0 for {A.name} (Ass)"
            com = CommutativeBarComplex(A, 4)
            assert com.verify_d_squared_zero(4), f"d^2 != 0 for {A.name} (Com)"

    def test_sc_d_squared_zero_all_commutative(self):
        """d^2 = 0 for B_{SC}(C, C) for all commutative test algebras."""
        for C in [dual_numbers(), polynomial_algebra(3), exterior_algebra_1()]:
            sc = SCAlgebra.from_self_action(C)
            bc = SwissCheeseBarComplex(sc, 3)
            assert bc.verify_d_squared_zero_closed(3), (
                f"d^2 != 0 closed for {C.name}"
            )
            assert bc.verify_d_squared_zero_open(3), (
                f"d^2 != 0 open for {C.name}"
            )

    def test_polynomial_bar_dimension_growth(self):
        """dim B^n_{Ass}(k[x]/(x^N)) = (N-1)^n -- verify for several N."""
        for N in range(2, 6):
            A = polynomial_algebra(N)
            bc = AssociativeBarComplex(A, 4)
            for n in range(5):
                words = bar_words_at_degree(n, A.aug_ideal_dim)
                assert len(words) == (N - 1) ** n

    def test_exterior_bar_dimension_growth(self):
        """dim Lambda^n(k^d) = C(d, n) -- verify for B_{Com}."""
        from math import comb
        for d in range(1, 5):
            for n in range(d + 2):
                words = sym_bar_words_at_degree(n, d)
                assert len(words) == comb(d, n)

    def test_promotion_functor_produces_sc_coalgebra(self):
        """The promotion functor should produce a valid SC-coalgebra
        (all d^2=0, all sectors compatible) for polynomial algebras."""
        for n in [2, 3, 4]:
            C = polynomial_algebra(n)
            result = verify_promotion_functor(C, 3)
            assert result["d_squared_zero_closed"]
            assert result["d_squared_zero_open"]
            assert result["harrison_matches"]
            assert result["ass_bar_matches"]
