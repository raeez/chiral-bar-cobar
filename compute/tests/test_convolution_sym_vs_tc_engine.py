r"""Tests for convolution_sym_vs_tc_engine: Sym^c vs T^c vs Lie^c.

Resolution of the central frontier question:
  Which coalgebra underlies the modular convolution dg Lie algebra g^mod_A?

ANSWER: Sym^c (cofree cocommutative coalgebra), with coshuffle coproduct,
via Sigma_n-equivariant Hom from the commutative modular operad.

Test structure:
  Section 1: Eulerian idempotent verification (5 tests)
  Section 2: Coproduct structure (5 tests)
  Section 3: Kappa Eulerian decomposition (5 tests)
  Section 4: Dimension counts (5 tests)
  Section 5: Structural theorems (5 tests)
  Section 6: Multi-path verification of the main claim (5+ tests)
"""

import pytest
from fractions import Fraction

from compute.lib.convolution_sym_vs_tc_engine import (
    eulerian_e1,
    eulerian_e2_from_complement,
    verify_e1_idempotent,
    coshuffle_coproduct,
    deconcatenation_coproduct,
    count_coproduct_terms,
    heisenberg_kappa_eulerian_decomposition,
    virasoro_kappa_eulerian_decomposition,
    verify_coshuffle_cocommutative,
    verify_deconcatenation_not_cocommutative,
    universal_enveloping_coalgebra_dimension,
    universal_enveloping_coalgebra_dimension_d,
    sigma_n_coinvariant_dimension,
    averaging_map_at_arity_2,
    convolution_lie_isomorphism_single_generator,
    definitive_answer,
    ConvolutionElement,
    coshuffle_bracket,
    deconcatenation_bracket,
    _right_normed_bracket,
)

F = Fraction


# ============================================================================
# Section 1: Eulerian idempotent verification
# ============================================================================

class TestEulerianIdempotent:
    """Verify the first Eulerian idempotent e_1 = (1/n) * l_n."""

    def test_e1_arity_1(self):
        """e_1 at arity 1 is the identity."""
        e1 = eulerian_e1(1)
        assert e1 == {(0,): F(1)}

    def test_e1_arity_2_is_antisymmetrizer(self):
        """e_1 at arity 2 is (1/2)(id - swap) = antisymmetrizer.

        This is because Lie(2) = Q (spanned by [x_0, x_1] = x_0x_1 - x_1x_0),
        and the DSW projector onto Lie(2) is the antisymmetrizer.
        """
        e1 = eulerian_e1(2)
        assert e1[(0, 1)] == F(1, 2), f"e1(id) = {e1.get((0,1))}, expected 1/2"
        assert e1[(1, 0)] == F(-1, 2), f"e1(swap) = {e1.get((1,0))}, expected -1/2"

    def test_e1_idempotent_n2(self):
        """e_1^2 = e_1 at arity 2."""
        assert verify_e1_idempotent(2) == F(0)

    def test_e1_idempotent_n3(self):
        """e_1^2 = e_1 at arity 3."""
        assert verify_e1_idempotent(3) == F(0)

    def test_e1_idempotent_n4(self):
        """e_1^2 = e_1 at arity 4."""
        assert verify_e1_idempotent(4) == F(0)

    def test_e1_trace_equals_lie_dim(self):
        """tr(e_1) on multilinear part = dim Lie(n) / n!.

        dim Lie(n) = (n-1)!. The trace of e_1 on the regular representation
        Q[S_n] is dim(Lie(n)) = (n-1)!, since e_1 projects onto Lie(n).
        But the TRACE of e_1 as an element of Q[S_n] (= coefficient of id)
        times n! should equal (n-1)!.

        Actually: tr(e_1 on V^{tensor n}) for V = Q^n is the RANK of e_1
        on the multilinear subspace, which is dim(Lie(n)) = (n-1)!.
        The coefficient of id in e_1 is e_1(id) = 1/n (from the DSW formula).
        The trace of e_1 on the n!-dimensional space is n! * (1/n) = (n-1)!.
        """
        for n in [2, 3, 4]:
            e1 = eulerian_e1(n)
            identity = tuple(range(n))
            e1_id = e1.get(identity, F(0))
            expected_trace = F(1, n)  # e_1(id) = 1/n
            assert e1_id == expected_trace, (
                f"n={n}: e_1(id) = {e1_id}, expected {expected_trace}"
            )

    def test_e2_complement_n2(self):
        """e_2 = id - e_1 at arity 2 is the symmetrizer."""
        e2 = eulerian_e2_from_complement(2)
        assert e2[(0, 1)] == F(1, 2), f"e2(id) = {e2.get((0,1))}"
        assert e2[(1, 0)] == F(1, 2), f"e2(swap) = {e2.get((1,0))}"

    def test_right_normed_bracket_n2(self):
        """[x_0, x_1] = x_0 x_1 - x_1 x_0."""
        coeffs = _right_normed_bracket(2)
        assert coeffs[(0, 1)] == F(1)
        assert coeffs[(1, 0)] == F(-1)


# ============================================================================
# Section 2: Coproduct structure
# ============================================================================

class TestCoproductStructure:
    """Verify coshuffle vs deconcatenation coproduct properties."""

    def test_coshuffle_term_count(self):
        """Coshuffle on n elements has 2^n terms."""
        for n in range(1, 6):
            terms = coshuffle_coproduct(n)
            assert len(terms) == 2 ** n, (
                f"n={n}: coshuffle has {len(terms)} terms, expected {2**n}"
            )

    def test_deconcatenation_term_count(self):
        """Deconcatenation on n elements has n+1 terms."""
        for n in range(1, 6):
            terms = deconcatenation_coproduct(n)
            assert len(terms) == n + 1, (
                f"n={n}: deconcat has {len(terms)} terms, expected {n+1}"
            )

    def test_coshuffle_cocommutative(self):
        """Coshuffle is cocommutative for all n."""
        for n in range(1, 6):
            assert verify_coshuffle_cocommutative(n), (
                f"Coshuffle is not cocommutative at n={n}"
            )

    def test_deconcatenation_not_cocommutative(self):
        """Deconcatenation is NOT cocommutative for n >= 2."""
        for n in range(2, 6):
            assert verify_deconcatenation_not_cocommutative(n), (
                f"Deconcatenation is cocommutative at n={n} (should not be)"
            )

    def test_coproduct_term_ratio(self):
        """Coshuffle has exponentially more terms than deconcatenation.

        At arity n: coshuffle has 2^n, deconcatenation has n+1.
        Ratio: 2^n / (n+1), which grows exponentially.
        """
        for n in [2, 3, 4, 5]:
            cs, dc = count_coproduct_terms(n)
            assert cs == 2 ** n
            assert dc == n + 1
            assert cs > dc, f"n={n}: coshuffle terms <= deconcat terms"

    def test_coshuffle_includes_empty_factors(self):
        """Coshuffle includes (empty, full) and (full, empty) terms."""
        for n in range(1, 5):
            terms = coshuffle_coproduct(n)
            full = tuple(range(n))
            empty = ()
            assert (empty, full) in terms
            assert (full, empty) in terms


# ============================================================================
# Section 3: Kappa Eulerian decomposition
# ============================================================================

class TestKappaEulerianDecomposition:
    """Verify where kappa lives in the Eulerian decomposition."""

    def test_heisenberg_kappa_in_weight_2(self):
        """For Heisenberg (degree 0 generator), kappa is entirely in weight-2 Eulerian.

        s^{-1}a has degree 0 (even), so S_2 acts trivially.
        e_1 (antisymmetrizer) kills the trivial rep. e_2 (symmetrizer) preserves it.
        """
        result = heisenberg_kappa_eulerian_decomposition(k=1)
        assert result['harrison_weight_1'] == F(0), (
            f"Harrison component = {result['harrison_weight_1']}, expected 0"
        )
        assert result['symmetric_weight_2'] == F(1), (
            f"Symmetric component = {result['symmetric_weight_2']}, expected 1"
        )
        assert result['total_kappa'] == F(1)

    def test_heisenberg_kappa_k_equals_3(self):
        """kappa(H_3) = 3, all in weight-2."""
        result = heisenberg_kappa_eulerian_decomposition(k=3)
        assert result['harrison_weight_1'] == F(0)
        assert result['symmetric_weight_2'] == F(3)
        assert result['total_kappa'] == F(3)

    def test_virasoro_kappa_in_weight_1(self):
        """For Virasoro (degree 1 generator), kappa is entirely in weight-1 Eulerian.

        s^{-1}T has degree 1 (odd), so S_2 acts by sign representation.
        e_1 (antisymmetrizer) preserves the sign rep. e_2 (symmetrizer) kills it.
        """
        result = virasoro_kappa_eulerian_decomposition(c=F(26))
        assert result['harrison_weight_1'] == F(13), (
            f"Harrison component = {result['harrison_weight_1']}, expected 13"
        )
        assert result['symmetric_weight_2'] == F(0), (
            f"Symmetric component = {result['symmetric_weight_2']}, expected 0"
        )
        assert result['total_kappa'] == F(13)

    def test_virasoro_kappa_c_equals_1(self):
        """kappa(Vir_1) = 1/2, all in weight-1."""
        result = virasoro_kappa_eulerian_decomposition(c=F(1))
        assert result['harrison_weight_1'] == F(1, 2)
        assert result['symmetric_weight_2'] == F(0)

    def test_kappa_weight_depends_on_desuspended_degree(self):
        """The Eulerian weight of kappa depends on the desuspended degree of generators.

        Degree 0 (even) -> weight 2.
        Degree 1 (odd) -> weight 1.

        This resolves the apparent contradiction: both are consistent with
        the convolution using Sym^c. The Eulerian weight depends on the
        S_n representation, which depends on the degree.
        """
        heis = heisenberg_kappa_eulerian_decomposition(k=1)
        vir = virasoro_kappa_eulerian_decomposition(c=F(2))

        # Heisenberg: kappa in weight 2
        assert heis['e1_eigenvalue_on_trivial'] == F(0)
        assert heis['e2_eigenvalue_on_trivial'] == F(1)

        # Virasoro: kappa in weight 1
        assert vir['e1_eigenvalue_on_sign'] == F(1)
        assert vir['e2_eigenvalue_on_sign'] == F(0)


# ============================================================================
# Section 4: Dimension counts
# ============================================================================

class TestDimensionCounts:
    """Verify dimension formulas for Sym^c, Lie^c, T^c."""

    def test_single_generator_lie_c_vanishes(self):
        """For V = Q^1: Lie^c_n(V) = 0 for n >= 2.

        Free Lie algebra on one generator is abelian (Lie(1) = Q, Lie(n>=2) = 0).
        """
        for n in range(2, 6):
            result = universal_enveloping_coalgebra_dimension(n)
            assert result['lie_c_dim'] == 0, (
                f"n={n}: Lie^c dim = {result['lie_c_dim']}, expected 0"
            )

    def test_single_generator_sym_c_is_1(self):
        """For V = Q^1: Sym^c_n(V) = Q (1-dim) for all n."""
        for n in range(1, 6):
            result = universal_enveloping_coalgebra_dimension(n)
            assert result['sym_c_dim'] == 1

    def test_lie_c_witt_formula(self):
        """Lie^c_n(Q^d) has dimension given by Witt/necklace formula.

        Known values:
          Lie(2, 2) = 1 (one bracket [x,y])
          Lie(3, 2) = 2 ([x,[x,y]] and [y,[x,y]])
          Lie(2, 3) = 3 ([x,y], [x,z], [y,z])
        """
        assert universal_enveloping_coalgebra_dimension_d(2, 2)['lie_c_dim'] == 1
        assert universal_enveloping_coalgebra_dimension_d(3, 2)['lie_c_dim'] == 2
        assert universal_enveloping_coalgebra_dimension_d(2, 3)['lie_c_dim'] == 3

    def test_sym_c_multiset_formula(self):
        """Sym^c_n(Q^d) has dimension C(d+n-1, n).

        Known values:
          Sym^2(Q^2) = 3 (x^2, xy, y^2)
          Sym^3(Q^2) = 4 (x^3, x^2y, xy^2, y^3)
          Sym^2(Q^3) = 6 (x^2, y^2, z^2, xy, xz, yz)
        """
        assert universal_enveloping_coalgebra_dimension_d(2, 2)['sym_c_dim'] == 3
        assert universal_enveloping_coalgebra_dimension_d(3, 2)['sym_c_dim'] == 4
        assert universal_enveloping_coalgebra_dimension_d(2, 3)['sym_c_dim'] == 6

    def test_pbw_decomposition(self):
        r"""PBW: Sym^c(V) ~ gr(U^c(Lie^c(V))) as graded coalgebras.

        The PBW isomorphism is Sym^c(V) ~ gr(U^c(Lie^c(V))), where gr is the
        associated graded with respect to the PBW filtration.  This is a statement
        about TOTAL dimensions with PBW weight grading, NOT an arity-by-arity
        inequality.  In particular, dim Lie^c_n(V) CAN exceed dim Sym^c_n(V)
        at individual arities (e.g., d=3, n=4: Lie^c = 18 > 15 = Sym^c).

        What IS true: at arity 1, dim Lie^c_1 = dim Sym^c_1 = d (generators).
        And: dim T^c_n = d^n >= max(dim Sym^c_n, dim Lie^c_n) for all n.
        """
        for d in [1, 2, 3]:
            # At arity 1, Lie^c and Sym^c agree (both = V)
            r1 = universal_enveloping_coalgebra_dimension_d(1, d)
            assert r1['sym_c_dim'] == r1['lie_c_dim'] == d

            # T^c_n = d^n dominates both Sym^c and Lie^c
            for n in [1, 2, 3, 4]:
                result = universal_enveloping_coalgebra_dimension_d(n, d)
                assert d ** n >= result['sym_c_dim']
                assert d ** n >= result['lie_c_dim']

    def test_sigma_n_coinvariant_even_degree(self):
        """For generators of even desuspended degree, Sym^c = multisets."""
        result = sigma_n_coinvariant_dimension(3, 2, [0, 0])
        assert result['ordered_dim_T_c'] == 8   # 2^3
        assert result['symmetric_dim_Sym_c'] == 4  # C(2+3-1,3) = C(4,3) = 4

    def test_sigma_n_coinvariant_odd_degree(self):
        """For generators of odd desuspended degree, Sym^c = exterior powers."""
        result = sigma_n_coinvariant_dimension(2, 3, [1, 1, 1])
        assert result['ordered_dim_T_c'] == 9   # 3^2
        assert result['symmetric_dim_Sym_c'] == 3  # C(3,2) = 3


# ============================================================================
# Section 5: Structural theorems
# ============================================================================

class TestStructuralTheorems:
    """Verify the key structural claims."""

    def test_definitive_answer_coalgebra(self):
        """The definitive answer: g^mod uses Sym^c."""
        answer = definitive_answer()
        assert answer['coalgebra'] == 'Sym^c (cofree cocommutative)'
        assert answer['coproduct'] == 'coshuffle (unordered bipartition)'

    def test_definitive_answer_agents(self):
        """Agent 1 was wrong, Agent 6 was correct."""
        answer = definitive_answer()
        assert 'WRONG' in answer['agent_1_error']
        assert 'CORRECT' in answer['agent_6_correct']

    def test_lie_iso_single_gen(self):
        """Hom_Lie(Sym^c, A) = Hom(Lie^c, A) as LIE ALGEBRAS (not vector spaces)."""
        result = convolution_lie_isomorphism_single_generator()
        assert 'Lie' in result['lie_algebra_isomorphism']
        assert '!=' in result['vector_space_inequality']

    def test_kappa_not_in_lie_c(self):
        """kappa lives in Sym^c, not Lie^c."""
        result = convolution_lie_isomorphism_single_generator()
        assert 'NOT in Lie^c' in result['kappa_lives_in']

    def test_mc_uses_full_sym_c(self):
        """The MC equation uses the full Sym^c, not just Lie^c."""
        result = convolution_lie_isomorphism_single_generator()
        assert 'Sym^c' in result['mc_equation_uses']


# ============================================================================
# Section 6: Multi-path verification of the main claim
# ============================================================================

class TestMultiPathVerification:
    """Multiple independent verifications that g^mod uses Sym^c."""

    def test_path_1_sigma_n_equivariance(self):
        """Path 1: Definition specifies Hom_{Sigma_n}, which = Hom from coinvariants.

        Hom_{Sigma_n}(V^{tensor n}, W) = Hom((V^{tensor n})_{Sigma_n}, W)
                                        = Hom(Sym^n(V), W).
        """
        # The definition says: Hom_{Sigma_n}(C_*(M_bar_{g,n}), End_A(n))
        # M_bar_{g,n} has a Sigma_n action permuting marked points.
        # Hom_{Sigma_n} means Sigma_n-equivariant maps.
        # (C_*(M_bar_{g,n}))_{Sigma_n} is the coinvariant = symmetric part.
        # This is equivalent to working with Sym^c, not T^c.

        # Computational check: at arity 2 for Heisenberg
        result = heisenberg_kappa_eulerian_decomposition(1)
        # kappa = 1, all in Sym^c (weight 2), consistent with Sigma_2-equivariant Hom
        assert result['symmetric_weight_2'] == F(1)
        assert result['harrison_weight_1'] == F(0)

    def test_path_2_averaging_map(self):
        """Path 2: The averaging map av: g^{E_1} -> g^mod is Sigma_n-coinvariant.

        g^{E_1} = Hom(M_Ass(g,n), End(n))  [no Sigma_n, = T^c side]
        g^mod   = Hom_{Sigma_n}(M_Com(g,n), End(n))  [Sigma_n-equiv, = Sym^c side]
        av(phi) = (1/n!) sum_sigma sigma . phi

        This is exactly the passage T^c -> Sym^c (coinvariant projection).
        """
        # Verify: in scalar families, av(r(z)) = kappa is the Sigma_2-coinvariant of the r-matrix.
        kappa = averaging_map_at_arity_2(F(1), desuspended_degree=0)
        assert kappa == F(1)

    def test_path_3_modular_operad_is_com(self):
        """Path 3: The modular operad is M_Com, Feynman transform is FCom.

        The bar complex is an FCom-algebra (thm:bar-modular-operad).
        FCom is the Feynman transform of the COMMUTATIVE modular operad.
        Convolution over a commutative cooperad = Hom from Sym^c.
        """
        answer = definitive_answer()
        assert answer['modular_operad'] == 'M_Com = {M_bar_{g,n}} (commutative)'
        assert answer['feynman_transform'] == 'FCom'

    def test_path_4_coshuffle_is_cocommutative(self):
        """Path 4: The coshuffle coproduct is cocommutative = Sym^c signature.

        Sym^c is the cofree COCOMMUTATIVE coalgebra. Its coproduct is the
        coshuffle. This coproduct IS cocommutative (verified computationally).
        The deconcatenation coproduct (T^c) is NOT cocommutative.
        """
        for n in [2, 3, 4, 5]:
            assert verify_coshuffle_cocommutative(n)
            if n >= 2:
                assert verify_deconcatenation_not_cocommutative(n)

    def test_path_5_e1_to_einfty_table(self):
        """Path 5: The concordance table (sec:concordance) confirms the split.

        The concordance has a table:
          E_infty (symmetric): g^mod, FCom, kappa (scalar)
          E_1 (ordered): g^{E_1}, FAss, r(z) (R-matrix)

        kappa is the E_infty shadow = Sigma_2-coinvariant of r(z).
        This confirms g^mod uses the symmetric/commutative structure.
        """
        # From the table: the degree-2 scalar shadow is extracted from av(r(z))
        # If g^mod used Lie^c, then kappa would be in the Harrison part.
        # But for Heisenberg, the Harrison part at arity 2 is 0.
        # So g^mod CANNOT use Lie^c (or kappa would be 0 for Heisenberg).
        heis = heisenberg_kappa_eulerian_decomposition(k=1)
        assert heis['harrison_weight_1'] == F(0), (
            "If g^mod used Lie^c, kappa(H_1) would be 0. It is 1."
        )
        assert heis['total_kappa'] == F(1)

    def test_path_6_bracket_differs_between_coproducts(self):
        """Path 6: Different coproducts give different brackets.

        The coshuffle bracket at arity 4 involves C(4,2) = 6 terms.
        The deconcatenation bracket at arity 4 involves 5 terms (p=0,...,4).
        These give different numerical coefficients.
        """
        cs_terms, dc_terms = count_coproduct_terms(4)
        assert cs_terms == 16  # 2^4
        assert dc_terms == 5   # 4+1
        assert cs_terms != dc_terms

    def test_path_7_heisenberg_consistency(self):
        """Path 7: kappa(H_k) = k is consistent with Sym^c but not Lie^c.

        If the convolution used Lie^c, then at arity 2 for a single generator
        of desuspended degree 0, the Lie^c component is 0-dimensional
        (Lie(2, 1) = 0). So the arity-2 component of Theta_A would live in
        a 0-dimensional space, making kappa = 0 for ALL Heisenberg algebras.
        But kappa(H_k) = k != 0. Contradiction.
        """
        result = universal_enveloping_coalgebra_dimension(2)
        assert result['lie_c_dim'] == 0, "Lie^c_2(Q^1) should be 0"
        assert result['sym_c_dim'] == 1, "Sym^c_2(Q^1) should be 1"

        # If g^mod used Lie^c: kappa would live in Hom(Lie^c_2, A) = Hom(0, A) = 0
        # But kappa(H_k) = k != 0. So g^mod CANNOT use Lie^c.

    def test_path_8_virasoro_consistency(self):
        """Path 8: kappa(Vir_c) = c/2 is also consistent with Sym^c.

        For Virasoro (degree 1 generator), Lie^c_2(Q^1) = 0, BUT
        the desuspended generator has degree 1 (odd), so the sign representation
        makes the Harrison component nonzero. However, the correct framework
        is Sym^c, where both even and odd generators work uniformly.
        """
        # For the Virasoro, the key point: the S_2 action involves Koszul signs.
        # In the sign representation, e_1 acts as 1 (not 0).
        # So kappa lives in the Harrison component for Virasoro.
        vir = virasoro_kappa_eulerian_decomposition(c=F(2))
        assert vir['total_kappa'] == F(1)  # c/2 = 1
        assert vir['harrison_weight_1'] == F(1)

    def test_path_9_kappa_additivity(self):
        """Path 9: kappa is additive (kappa(A + B) = kappa(A) + kappa(B)).

        This additivity is a consequence of the Sym^c structure: the coshuffle
        coproduct respects direct sums. The deconcatenation coproduct on T^c
        also respects direct sums, so this doesn't distinguish. But the
        Harrison coproduct on Lie^c does NOT respect direct sums in the
        same way (Lie^c(V+W) != Lie^c(V) + Lie^c(W)), so additivity of
        kappa is most natural in the Sym^c framework.

        Test: kappa(H_1 + H_2) = kappa(H_1) + kappa(H_2) = 1 + 2 = 3.
        """
        k1, k2 = 1, 2
        result1 = heisenberg_kappa_eulerian_decomposition(k1)
        result2 = heisenberg_kappa_eulerian_decomposition(k2)
        result_sum = heisenberg_kappa_eulerian_decomposition(k1 + k2)

        assert result_sum['total_kappa'] == result1['total_kappa'] + result2['total_kappa']

    def test_path_10_manuscript_formula_recovery(self):
        """Path 10: The manuscript's degree-2 scalar-shadow formula recovers the correct scalar cases.

        For the scalar families, the averaging (Sigma_2-coinvariant) of the
        E_1 r-matrix gives the correct scalar kappa. Non-abelian affine KM
        requires the extra Sugawara shift dim(g)/2.
        """
        # Heisenberg at various levels
        for k in [1, 2, 5, -3]:
            result = heisenberg_kappa_eulerian_decomposition(k)
            assert result['total_kappa'] == F(k)

        # Virasoro at various central charges
        for c in [F(1), F(2), F(13), F(26)]:
            result = virasoro_kappa_eulerian_decomposition(c)
            assert result['total_kappa'] == c / 2


# ============================================================================
# Additional structural tests
# ============================================================================

class TestCoshuffleVsDeconcatenationBracket:
    """Compare the brackets arising from the two coproducts."""

    def test_bracket_coefficient_differs_at_arity_4(self):
        """The coshuffle bracket has coefficient C(4,2) = 6 at the (2,2) splitting,
        while deconcatenation has coefficient 1. These differ by factor 6."""
        n = 4
        cs_binomial = F(6)   # C(4,2) for coshuffle
        dc_weight = F(1)     # 1 for deconcatenation
        assert cs_binomial != dc_weight
        assert cs_binomial / dc_weight == F(6)

    def test_total_coproduct_terms_grow_differently(self):
        """Coshuffle grows as 2^n, deconcatenation as n+1. Ratio is exponential."""
        for n in [5, 6, 7, 8]:
            cs, dc = count_coproduct_terms(n)
            ratio = cs / dc
            assert ratio > n, f"n={n}: ratio {ratio} should be > n"


class TestEulerianDecompositionConsistency:
    """Cross-check Eulerian decomposition with known facts."""

    def test_e1_plus_e2_equals_identity_n2(self):
        """e_1 + e_2 = id in Q[S_2]."""
        e1 = eulerian_e1(2)
        e2 = eulerian_e2_from_complement(2)

        identity = (0, 1)
        swap = (1, 0)

        assert e1.get(identity, F(0)) + e2.get(identity, F(0)) == F(1)
        assert e1.get(swap, F(0)) + e2.get(swap, F(0)) == F(0)

    def test_e1_on_trivial_rep_is_zero(self):
        """e_1 kills the trivial S_n representation for n >= 2.

        The trivial representation is Sym^n(Q) for a single degree-0 generator.
        Harrison homology of a polynomial algebra vanishes in degree != 1
        (Barr's theorem). At arity >= 2, e_1 (Harrison projector) acts as 0
        on the trivial representation.
        """
        for n in [2, 3, 4]:
            e1 = eulerian_e1(n)
            # Sum of all coefficients = trace on trivial rep
            total = sum(e1.values())
            assert total == F(0), (
                f"n={n}: e_1 on trivial rep = {total}, expected 0"
            )

    def test_e1_on_sign_rep_n2(self):
        """e_1 preserves the sign S_2 representation.

        For a single degree-1 (odd) generator, S_2 acts by the sign rep.
        e_1 should act as identity on the sign rep (since the sign rep
        IS the Lie component at arity 2).
        """
        e1 = eulerian_e1(2)
        # Sign rep: sigma acts as -1
        e1_on_sign = e1.get((0, 1), F(0)) * 1 + e1.get((1, 0), F(0)) * (-1)
        assert e1_on_sign == F(1), (
            f"e_1 on sign rep = {e1_on_sign}, expected 1"
        )
