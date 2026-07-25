"""Tests for exact finite windows of the associative bar--cobar counit.

Tests cover:
 1. DGA construction (AugDGA) for all standard families
 2. Bar construction: d^2 = 0 at each bar degree
 3. Mixed-word cobar differential: d^2 = 0
 4. Bigraded basis and exact finite-window homology
 5. Twisting morphism tau: MC equation d(tau) + tau*tau = 0
 6. Counit chain map psi: chain map property d*psi = psi*d
 7. Typed containment of the full counit theorem
 8. A-infinity extraction: transferred operations satisfy Stasheff relations
 9. Koszul sign conventions: explicit sign checks
10. Cross-checks with existing modules (bar_complex.py, verdier_bar_cobar_pairing.py)
11. Edge cases: trivial algebra, one-generator augmented algebra

References:
  thm:bar-cobar-adjunction (bar_cobar_adjunction_curved.tex)
  thm:bar-cobar-inversion (bar_cobar_adjunction_inversion.tex)
"""

from __future__ import annotations

import pytest
from sympy import Matrix, Rational, zeros, eye, simplify

from compute.lib.bar_cobar_chain_maps import (
    AugDGA,
    BarConstruction,
    MultiplicationDualComplex,
    BarCobarComposition,
    FiniteOmegaBarComplex,
    augmented_dga_axioms,
    finite_bar_cobar_report,
    truncated_polynomial_dga,
    dual_numbers_dga,
    matrix_2x2_upper_dga,
    exterior_on_one_generator,
    free_assoc_on_one_generator,
    lie_sl2_as_assoc,
    polynomial_with_diff,
    counit_map,
    counit_chain_map_verify,
    twisting_morphism_tau,
    verify_twisting_mc,
    twisted_tensor_product_diff,
    cohomology_dims_exact,
    kernel_dim_exact,
    image_dim_exact,
    verify_bar_cobar_quasi_iso,
    extract_ainfty_operations,
    verify_ainfty_relations,
    multiplication_dual_functoriality,
    bar_cobar_comparison_table,
    heisenberg_bar_cobar,
    free_fermion_bar_cobar,
    sl2_affine_bar_cobar_genus0,
    _kronecker,
)


def _assert_finite_scope(result):
    assert result["calculation_status"] == "computed finite truncation"
    assert result["convergence_status"] == "unresolved beyond finite truncation"
    assert result["global_quasi_isomorphism"] == "unresolved"
    assert result["is_quasi_iso"] is None


# ============================================================================
# Section 1: DGA construction for all standard families
# ============================================================================

class TestDGAConstruction:
    """Tests for AugDGA construction and basic properties."""

    def test_dual_numbers_dim(self):
        """Dual numbers k[eps]/(eps^2) has dimension 2."""
        dga = dual_numbers_dga()
        assert dga.dim == 2
        assert dga.name == "k[x]/(x^2)"

    def test_dual_numbers_associative(self):
        """Dual numbers is associative."""
        dga = dual_numbers_dga()
        assert dga.is_associative()

    def test_dual_numbers_d_squared_zero(self):
        """Dual numbers has d = 0, so d^2 = 0."""
        dga = dual_numbers_dga()
        assert dga.d_squared_zero()

    def test_truncated_poly_3_dim(self):
        """k[x]/(x^3) has dimension 3: {1, x, x^2}."""
        dga = truncated_polynomial_dga(3)
        assert dga.dim == 3
        assert dga.degrees == [0, 0, 0]

    def test_truncated_poly_3_associative(self):
        """k[x]/(x^3) is associative: (x^i * x^j) * x^k = x^i * (x^j * x^k)."""
        dga = truncated_polynomial_dga(3)
        assert dga.is_associative()

    def test_truncated_poly_4_dim(self):
        """k[x]/(x^4) has dimension 4."""
        dga = truncated_polynomial_dga(4)
        assert dga.dim == 4
        assert dga.is_associative()

    def test_truncated_poly_product(self):
        """k[x]/(x^3): x*x = x^2 (index 1*1 = 2), x*x^2 = 0 (1+2 >= 3)."""
        dga = truncated_polynomial_dga(3)
        assert dga.mult[(1, 1)] == {2: Rational(1)}
        assert (1, 2) not in dga.mult  # x * x^2 = x^3 = 0

    def test_exterior_algebra_dim(self):
        """Exterior algebra Lambda(1): {1, eps} with |eps| = 1."""
        ext = exterior_on_one_generator()
        assert ext.dim == 2
        assert ext.degrees == [0, 1]

    def test_exterior_algebra_eps_squared_zero(self):
        """eps^2 = 0 in the exterior algebra."""
        ext = exterior_on_one_generator()
        assert (1, 1) not in ext.mult

    def test_exterior_algebra_associative(self):
        """Exterior algebra on one generator is associative (trivially)."""
        ext = exterior_on_one_generator()
        assert ext.is_associative()

    def test_upper_triangular_2x2(self):
        """UT_2 has dim 3 and is associative."""
        ut = matrix_2x2_upper_dga()
        assert ut.dim == 3
        assert ut.is_associative()

    def test_upper_triangular_products(self):
        """UT_2 in the basis (1,p,u) has p^2=p and pu=u."""
        ut = matrix_2x2_upper_dga()
        assert ut.mult[(0, 2)] == {2: Rational(1)}
        assert ut.mult[(1, 1)] == {1: Rational(1)}
        assert ut.mult[(1, 2)] == {2: Rational(1)}
        assert (2, 2) not in ut.mult

    def test_lie_sl2_not_associative(self):
        """sl_2 with Lie bracket is NOT associative."""
        sl2 = lie_sl2_as_assoc()
        assert not sl2.is_associative()

    def test_lie_sl2_bracket(self):
        """sl_2: [e,f] = h, [h,e] = 2e, [h,f] = -2f."""
        sl2 = lie_sl2_as_assoc()
        E, H, F = 0, 1, 2
        assert sl2.mult[(E, F)] == {H: Rational(1)}
        assert sl2.mult[(H, E)] == {E: Rational(2)}
        assert sl2.mult[(H, F)] == {F: Rational(-2)}

    def test_polynomial_with_diff_d_squared_zero(self):
        """The square-zero pair d(x)=y is a cohomological DGA."""
        pwd = polynomial_with_diff()
        assert pwd.d_squared_zero()
        assert pwd.is_associative()
        assert pwd.degrees == [0, 0, 1]
        assert all(augmented_dga_axioms(pwd).values())

    def test_free_assoc_is_truncated_poly(self):
        """free_assoc_on_one_generator(n) = truncated_polynomial_dga(n+1)."""
        fa = free_assoc_on_one_generator(3)
        tp = truncated_polynomial_dga(4)
        assert fa.dim == tp.dim
        assert fa.name == tp.name


# ============================================================================
# Section 2: Bar construction d^2 = 0
# ============================================================================

class TestBarConstruction:
    """Tests for BarConstruction and bar differential d^2 = 0."""

    def test_bar_dual_numbers_aug_dim(self):
        """Bar of dual numbers: aug ideal has dim 1 (just eps)."""
        bar = BarConstruction(dual_numbers_dga(), 5)
        assert bar.aug_dim == 1

    def test_bar_dual_numbers_dims(self):
        """Bar degrees: B^n of dual numbers has dim 1^n = 1."""
        bar = BarConstruction(dual_numbers_dga(), 5)
        for n in range(1, 6):
            assert bar.dim_at(n) == 1

    def test_bar_dual_numbers_d_squared(self):
        """Bar of dual numbers: d^2 = 0 at all bar degrees."""
        bar = BarConstruction(dual_numbers_dga(), 5)
        results = bar.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"d^2 != 0 at bar degree {n} for dual numbers"

    def test_bar_trunc_poly_3_d_squared(self):
        """Bar of k[x]/(x^3): d^2 = 0 (associative algebra)."""
        bar = BarConstruction(truncated_polynomial_dga(3), 5)
        results = bar.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"d^2 != 0 at bar degree {n} for k[x]/(x^3)"

    def test_bar_trunc_poly_4_d_squared(self):
        """Bar of k[x]/(x^4): d^2 = 0."""
        bar = BarConstruction(truncated_polynomial_dga(4), 4)
        results = bar.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"d^2 != 0 at bar degree {n} for k[x]/(x^4)"

    def test_bar_exterior_d_squared(self):
        """Bar of exterior algebra Lambda(1): d^2 = 0."""
        bar = BarConstruction(exterior_on_one_generator(), 5)
        results = bar.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"d^2 != 0 at bar degree {n} for Lambda(1)"

    def test_bar_ut2_d_squared(self):
        """Bar of UT_2: d^2 = 0."""
        bar = BarConstruction(matrix_2x2_upper_dga(), 4)
        results = bar.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"d^2 != 0 at bar degree {n} for UT_2"

    def test_bar_sl2_d_squared_fails(self):
        """Bar of sl_2 (non-associative): d^2 != 0 at bar degree 3."""
        bar = BarConstruction(lie_sl2_as_assoc(), 4)
        results = bar.verify_d_squared()
        # d^2 = 0 at degree 2 (no room for failure), but fails at degree 3
        assert results[2] is True
        assert results[3] is False

    def test_bar_trunc_poly_3_explicit_differential(self):
        """Bar of k[x]/(x^3): d_B^2 has correct explicit form.

        Bar basis B^1 = {(1,), (2,)} = {x, x^2}.
        Bar basis B^2 = {(1,1), (1,2), (2,1), (2,2)}.
        d_B^2(s^{-1}x|s^{-1}x) = -s^{-1}(x*x) = -s^{-1}(x^2).
        d_B^2(others involving x^2) = 0 since x*x^2 = x^3 = 0.
        """
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 3)
        d2 = bar.differential(2)
        assert d2.shape == (2, 4)
        # Column 0 = (1,1): maps to (2,) with the suspension sign -1
        assert d2[1, 0] == Rational(-1)
        # All other columns are zero
        assert d2[0, 0] == 0
        for j in range(1, 4):
            for i in range(2):
                assert d2[i, j] == 0

    def test_bar_differential_degree_1_is_zero(self):
        """Bar differential d_B^1: B^1 -> B^0 is zero (no contraction possible)."""
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 3)
        d1 = bar.differential(1)
        assert d1.equals(zeros(d1.rows, d1.cols))

    def test_bar_basis_enumeration(self):
        """Bar basis B^n for k[x]/(x^3) (aug indices {1,2}) has 2^n elements."""
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 4)
        for n in range(1, 5):
            assert len(bar.basis(n)) == 2 ** n


# ============================================================================
# Section 3: Multiplication-transpose complex
# ============================================================================

class TestMultiplicationDualComplex:
    """Tests for the tensor complex dual to multiplication on the ideal."""

    def test_dual_numbers_d_squared(self):
        """The multiplication transpose squares to zero for dual numbers."""
        bar = BarConstruction(dual_numbers_dga(), 5)
        cobar = MultiplicationDualComplex(bar, 5)
        results = cobar.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"Cobar d^2 != 0 at degree {n} for dual numbers"

    def test_trunc_poly_3_d_squared(self):
        """Associativity gives delta^2=0 for k[x]/(x^3)."""
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 5)
        cobar = MultiplicationDualComplex(bar, 5)
        results = cobar.verify_d_squared()
        assert all(results.values())

    def test_exterior_d_squared(self):
        """The exterior-algebra multiplication transpose squares to zero."""
        bar = BarConstruction(exterior_on_one_generator(), 5)
        cobar = MultiplicationDualComplex(bar, 5)
        results = cobar.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"Cobar d^2 != 0 at degree {n} for Lambda(1)"

    def test_tensor_dimensions(self):
        """Tensor length n has dimension (dim A_bar)^n."""
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 4)
        cobar = MultiplicationDualComplex(bar, 4)
        assert cobar.dim_at(1) == 2   # aug_dim = 2
        assert cobar.dim_at(2) == 4
        assert cobar.dim_at(3) == 8

    def test_trunc_poly_3_explicit_transpose(self):
        """For k[x]/(x^3), delta(u_{x^2}) contains u_x tensor u_x.

        Coproduct: Delta(x^2) = x tensor x (from m_2(x,x) = x^2).
        So d_Omega(x^2) = x tensor x = basis element (1, 1) in Omega^2.
        d_Omega(x) = 0 (no coproduct for x in aug ideal).
        """
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 4)
        cobar = MultiplicationDualComplex(bar, 4)
        d1 = cobar.differential(1)
        assert d1.shape == (4, 2)
        # Column 1 (x^2, index 2 mapped to position 1 in aug basis): maps to (1,1) = row 0
        assert d1[0, 1] == Rational(1)
        # Column 0 (x): all zero
        for i in range(4):
            assert d1[i, 0] == 0

    def test_dual_numbers_all_differentials_zero(self):
        """The square-zero ideal gives a zero multiplication transpose."""
        bar = BarConstruction(dual_numbers_dga(), 4)
        cobar = MultiplicationDualComplex(bar, 4)
        for n in range(1, 4):
            d = cobar.differential(n)
            if d.rows > 0 and d.cols > 0:
                assert d.equals(zeros(d.rows, d.cols)), \
                    f"Multiplication transpose at degree {n} should vanish"


# ============================================================================
# Section 4: Bar-cobar composition bigraded structure
# ============================================================================

class TestBarCobarComposition:
    """Tests for BarCobarComposition bigraded structure."""

    def test_bigraded_basis_bar_deg_1(self):
        """Bidegree (1,1) contains the suspended length-one bar words."""
        dga = truncated_polynomial_dga(3)
        bcc = BarCobarComposition(dga, 3)
        basis_11 = bcc.bigraded_basis(1, 1)
        assert basis_11 == [((1,),), ((2,),)]

    def test_bigraded_basis_bar_deg_2(self):
        """Bidegree (1,2) contains one length-two bar word."""
        dga = dual_numbers_dga()
        bcc = BarCobarComposition(dga, 3)
        basis_12 = bcc.bigraded_basis(1, 2)
        assert basis_12 == [((1, 1),)]

    def test_total_degree_basis(self):
        """The total degree records bar and cobar suspensions together."""
        dga = dual_numbers_dga()
        bcc = BarCobarComposition(dga, 3)
        tdb = bcc.total_degree_basis(0)
        assert (0, 0, ()) in tdb
        assert any(q == 1 and p == 1 for q, p, _ in tdb)
        assert any(q == 2 and p == 2 for q, p, _ in tdb)

    def test_bar_cobar_composition_bar_property(self):
        """BarCobarComposition bar property returns the bar construction."""
        dga = dual_numbers_dga()
        bcc = BarCobarComposition(dga, 3)
        assert bcc.bar.dga is dga

    def test_bar_cobar_composition_multiplication_dual_property(self):
        """The comparison object retains the quadratic-row diagnostic."""
        dga = dual_numbers_dga()
        bcc = BarCobarComposition(dga, 3)
        assert bcc.multiplication_dual.bar is bcc.bar

    def test_bar_cobar_composition_omega_property(self):
        """The omega property carries all mixed bar-word lengths."""
        bcc = BarCobarComposition(dual_numbers_dga(), 3)
        assert bcc.omega.includes_all_bar_lengths
        assert ((1, 1),) in bcc.omega.basis()
        assert ((1,), (1, 1)) in bcc.omega.basis()

    def test_bigraded_basis_cobar_deg_0(self):
        """The cobar unit has bidegree (0,0)."""
        dga = dual_numbers_dga()
        bcc = BarCobarComposition(dga, 3)
        assert bcc.bigraded_basis(0, 0) == [()]


# ============================================================================
# Section 5: Full finite Omega(B(A)) engine
# ============================================================================

class TestFiniteOmegaBarComplex:
    """First-principles checks for the mixed bar/cobar differential."""

    def test_dual_numbers_basis_contains_every_bar_length(self):
        """For one augmentation generator, ordered compositions give 8 vectors."""
        complex_ = FiniteOmegaBarComplex(dual_numbers_dga(), 3, 3)
        assert len(complex_.basis()) == 8
        assert complex_.bidegree_dimensions() == {
            (0, 0): 1,
            (1, 1): 1,
            (1, 2): 1,
            (1, 3): 1,
            (2, 2): 1,
            (2, 3): 2,
            (3, 3): 1,
        }
        assert complex_.allowed_bar_letter_lengths == (1, 2, 3)

    def test_bar_and_cobar_parts_are_both_present(self):
        """For k[x]/x^3, one source has a multiplication term and a split term."""
        complex_ = FiniteOmegaBarComplex(truncated_polynomial_dga(3), 2, 2)
        assert complex_.differential_terms(((1, 1),)) == {
            ((2,),): Rational(1),
            ((1,), (1,)): Rational(-1),
        }

    def test_internal_part_is_present(self):
        """The suspended bar differential carries d(x)=y to d(s[s^-1x])=s[s^-1y]."""
        complex_ = FiniteOmegaBarComplex(polynomial_with_diff(), 2, 2)
        assert complex_.differential_terms(((1,),))[((2,),)] == Rational(1)

    def test_full_differential_squares_to_zero(self):
        """Internal, multiplication, and deconcatenation terms cancel exactly."""
        for dga in (
            dual_numbers_dga(),
            exterior_on_one_generator(),
            truncated_polynomial_dga(3),
            polynomial_with_diff(),
        ):
            complex_ = FiniteOmegaBarComplex(dga, 3, 3)
            assert all(complex_.verify_d_squared().values())

    def test_counit_is_multiplicative(self):
        """The word s[x]s[x] maps to x^2 in k[x]/x^3."""
        complex_ = FiniteOmegaBarComplex(truncated_polynomial_dga(3), 2, 2)
        degree_zero_basis = complex_.basis_in_degree(0)
        column = degree_zero_basis.index(((1,), (1,)))
        target = complex_.algebra_basis_in_degree(0)
        row = target.index(2)
        assert complex_.counit_matrix(0)[row, column] == Rational(1)
        assert complex_.counit_chain_map()["is_chain_map"]

    def test_dual_numbers_homology_by_direct_dimension_count(self):
        """The composition complexes in bar lengths 2 and 3 are acyclic."""
        complex_ = FiniteOmegaBarComplex(dual_numbers_dga(), 3, 3)
        assert complex_.differential_matrix(-2).rank() == 1
        assert complex_.differential_matrix(-1).rank() == 2
        report = finite_bar_cobar_report(dual_numbers_dga(), 3, 3)
        assert report["finite_window_homology"] == {-2: 0, -1: 0, 0: 2}
        assert report["A_homology"] == {0: 2}
        assert report["mapping_cone_homology"] == {-3: 0, -2: 0, -1: 0, 0: 0}
        assert report["finite_window_counit_is_quasi_isomorphism"]

    def test_exterior_algebra_grading(self):
        """For |e|=1, the two surviving classes lie in degrees 0 and 1."""
        report = finite_bar_cobar_report(exterior_on_one_generator(), 3, 3)
        assert report["finite_window_homology"] == {0: 1, 1: 1, 2: 0, 3: 0}
        assert report["A_homology"] == {0: 1, 1: 1}
        assert report["counit"]["is_chain_map"]

    def test_higher_bar_length_mutation_changes_homology(self):
        """Keeping only length-one bar generators leaves two extra dual-number classes."""
        full = FiniteOmegaBarComplex(dual_numbers_dga(), 3, 3)
        mutated = FiniteOmegaBarComplex(
            dual_numbers_dga(),
            3,
            3,
            allowed_bar_letter_lengths=(1,),
        )
        assert full.homology_dimensions() == {-2: 0, -1: 0, 0: 2}
        assert mutated.homology_dimensions() == {0: 4}
        assert mutated.mapping_cone_homology_dimensions() == {-1: 2, 0: 0}

    def test_finite_scope_is_explicit(self):
        """The report distinguishes the computed window from its filtered limit."""
        report = verify_bar_cobar_quasi_iso(dual_numbers_dga(), 3)
        _assert_finite_scope(report)


# ============================================================================
# Section 6: Twisting morphism tau and MC equation
# ============================================================================

class TestTwistingMorphism:
    """Tests for the universal twisting morphism tau: B(A) -> A."""

    def test_tau_degree_1(self):
        """tau on B^1 = s^{-1}A_bar is the inclusion: tau(s^{-1}a) = a."""
        dga = truncated_polynomial_dga(3)
        tau = twisting_morphism_tau(dga)
        mat = tau[1]
        assert mat.shape == (3, 2)
        # tau(s^{-1}x) = x (index 1), tau(s^{-1}x^2) = x^2 (index 2)
        assert mat[1, 0] == Rational(1)
        assert mat[2, 1] == Rational(1)
        # Zero elsewhere
        assert mat[0, 0] == 0
        assert mat[0, 1] == 0

    def test_tau_higher_degree_zero(self):
        """tau is zero on B^n for n >= 2."""
        dga = dual_numbers_dga()
        tau = twisting_morphism_tau(dga)
        for n in range(2, 6):
            mat = tau[n]
            assert mat.equals(zeros(mat.rows, mat.cols)), \
                f"tau should be zero at bar degree {n}"

    def test_mc_dual_numbers(self):
        """MC equation for dual numbers (trivial product on aug ideal)."""
        dga = dual_numbers_dga()
        mc = verify_twisting_mc(dga, 3)
        assert mc["mc_satisfied"]

    def test_mc_trunc_poly_3(self):
        """The universal twisting morphism satisfies MC for k[x]/(x^3).

        At B^2: tau(d_B(s^{-1}x|s^{-1}x)) + tau(s^{-1}x)*tau(s^{-1}x).
        The bar term is ``-x^2`` and the convolution product is ``+x^2``.
        """
        dga = truncated_polynomial_dga(3)
        mc = verify_twisting_mc(dga, 3)
        assert mc["mc_at_degree"][1] is True
        assert mc["mc_at_degree"][2] is True
        assert mc["mc_satisfied"]

    def test_mc_exterior(self):
        """MC equation for exterior algebra Lambda(1)."""
        ext = exterior_on_one_generator()
        mc = verify_twisting_mc(ext, 3)
        assert mc["mc_satisfied"]

    def test_mc_trunc_poly_4(self):
        """The same suspension sign proves MC for k[x]/(x^4)."""
        dga = truncated_polynomial_dga(4)
        mc = verify_twisting_mc(dga, 3)
        assert mc["mc_at_degree"][1] is True
        assert mc["mc_at_degree"][2] is True
        assert mc["mc_satisfied"]

    def test_mc_free_fermion_fails_at_degree_2(self):
        """Free fermion: MC fails at bar degree 2 because psi*psi = unit.

        The product psi*psi = 1 (unit) means the convolution product
        tau*tau at B^2 produces a unit component that is not cancelled
        by the bar differential (which sends B^2 -> B^0 via unit contraction).
        """
        ff_data = free_fermion_bar_cobar()
        mc = verify_twisting_mc(ff_data["dga"], 3)
        assert mc["mc_at_degree"][1] is True
        assert mc["mc_at_degree"][2] is False


# ============================================================================
# Section 6: Counit chain map psi
# ============================================================================

class TestCounitChainMap:
    """Tests for the strict counit on the mixed-word finite window."""

    def test_counit_contains_unit_and_augmentation_ideal(self):
        """The degree-zero matrix sends the cobar unit, x, and x^2 identically."""
        dga = truncated_polynomial_dga(3)
        psi = counit_map(dga, 3)
        complex_ = FiniteOmegaBarComplex(dga, 3, 3)
        basis = complex_.basis_in_degree(0)
        mat = psi[0]
        assert mat[0, basis.index(())] == Rational(1)
        assert mat[1, basis.index(((1,),))] == Rational(1)
        assert mat[2, basis.index(((2,),))] == Rational(1)

    def test_counit_multiplies_cobar_words(self):
        """For k[x]/x^3, the two-factor word maps to x^2."""
        dga = truncated_polynomial_dga(3)
        complex_ = FiniteOmegaBarComplex(dga, 3, 3)
        basis = complex_.basis_in_degree(0)
        assert counit_map(dga, 3)[0][2, basis.index(((1,), (1,)))] == Rational(1)

    def test_chain_map_dual_numbers(self):
        """psi is a chain map for dual numbers."""
        result = counit_chain_map_verify(dual_numbers_dga(), 3)
        assert result["is_chain_map"]

    def test_chain_map_trunc_poly_3(self):
        """psi is a chain map for k[x]/(x^3)."""
        result = counit_chain_map_verify(truncated_polynomial_dga(3), 3)
        assert result["is_chain_map"]

    def test_chain_map_exterior(self):
        """psi is a chain map for exterior algebra."""
        result = counit_chain_map_verify(exterior_on_one_generator(), 3)
        assert result["is_chain_map"]

    def test_chain_map_ut2(self):
        """psi is a chain map for UT_2."""
        result = counit_chain_map_verify(matrix_2x2_upper_dga(), 3)
        assert result["is_chain_map"]

    def test_chain_map_at_each_degree(self):
        """Chain map condition holds at each individual degree."""
        result = counit_chain_map_verify(truncated_polynomial_dga(3), 3)
        for n, ok in result["chain_map_at_degree"].items():
            assert ok, f"Chain map condition fails at degree {n}"


# ============================================================================
# Section 7: Quasi-isomorphism verification
# ============================================================================

class TestQuasiIsomorphism:
    """Tests for exact finite-window homology and the stated limit problem."""

    def test_qi_dual_numbers(self):
        """The dual-number window has the cohomology of its target algebra."""
        result = verify_bar_cobar_quasi_iso(dual_numbers_dga(), 3)
        _assert_finite_scope(result)
        assert result["aug_ideal_dim"] == 1
        assert not result["aug_has_product"]
        assert result["cobar_cohomology"] == {-2: 0, -1: 0, 0: 2}
        assert result["finite_window_counit_is_quasi_isomorphism"]

    def test_qi_trunc_poly_3(self):
        """The k[x]/x^3 window recovers three degree-zero classes."""
        result = verify_bar_cobar_quasi_iso(truncated_polynomial_dga(3), 3)
        _assert_finite_scope(result)
        assert result["cobar_cohomology"] == {-2: 0, -1: 0, 0: 3}
        assert result["counit"]["is_chain_map"]

    def test_qi_exterior(self):
        """The exterior grading survives in finite-window homology."""
        result = verify_bar_cobar_quasi_iso(exterior_on_one_generator(), 3)
        _assert_finite_scope(result)
        assert result["cobar_cohomology"] == {0: 1, 1: 1, 2: 0, 3: 0}

    def test_qi_bar_d_squared(self):
        """Quasi-iso check includes bar d^2 = 0 verification."""
        result = verify_bar_cobar_quasi_iso(dual_numbers_dga(), 3)
        bar_d2 = result["bar_d_squared"]
        for n, ok in bar_d2.items():
            assert ok

    def test_qi_cobar_d_squared(self):
        """The report checks the total mixed-word differential."""
        result = verify_bar_cobar_quasi_iso(dual_numbers_dga(), 3)
        cobar_d2 = result["cobar_d_squared"]
        for n, ok in cobar_d2.items():
            assert ok

    def test_qi_a_cohomology_trivial_diff(self):
        """For algebras with d = 0: H^*(A) = A concentrated in degree 0."""
        result = verify_bar_cobar_quasi_iso(dual_numbers_dga(), 3)
        a_coh = result["A_cohomology"]
        # Both generators (1 and eps) are in degree 0
        assert a_coh.get(0, 0) == 2

    def test_qi_polynomial_with_diff(self):
        """polynomial_with_diff: nontrivial internal differential."""
        result = verify_bar_cobar_quasi_iso(polynomial_with_diff(), 3)
        # The result includes A_cohomology computed from the nontrivial diff
        a_coh = result["A_cohomology"]
        # d(x) = x^2, so H^0 has basis {1, x} / im(d from deg -1) and ker(d).
        # Since d(1)=0, d(x)=x^2: ker(d: deg0 -> deg1) = {1} (1-dim).
        # H^0 = ker(d at deg 0) = span{1} = 1-dimensional.
        assert a_coh.get(0, 0) == 1


# ============================================================================
# Section 8: A-infinity extraction and Stasheff relations
# ============================================================================

class TestAInfinityExtraction:
    """Tests for A-infinity operations extracted from bar-cobar."""

    def test_m1_is_differential(self):
        """m_1 = d_A (the original differential)."""
        pwd = polynomial_with_diff()
        ops = extract_ainfty_operations(pwd, 3)
        # d(x) = x^2 means m_1((1,)) = {2: 1}
        assert ops[1][(1,)] == {2: Rational(1)}

    def test_m1_zero_for_zero_diff(self):
        """m_1 = 0 when d_A = 0."""
        dga = dual_numbers_dga()
        ops = extract_ainfty_operations(dga, 3)
        assert ops[1] == {}

    def test_m2_is_multiplication(self):
        """m_2 reproduces the original multiplication."""
        dga = truncated_polynomial_dga(3)
        ops = extract_ainfty_operations(dga, 3)
        # x * x = x^2: m_2(1, 1) = {2: 1}
        assert ops[2][(1, 1)] == {2: Rational(1)}

    def test_m3_zero_for_associative(self):
        """m_3 = 0 for strictly associative algebras."""
        dga = dual_numbers_dga()
        ops = extract_ainfty_operations(dga, 3)
        assert ops[3] == {}

    def test_m3_zero_for_all_associative(self):
        """m_3 = 0 for all our strictly associative test algebras."""
        for dga_fn in [dual_numbers_dga, exterior_on_one_generator,
                       matrix_2x2_upper_dga]:
            dga = dga_fn()
            ops = extract_ainfty_operations(dga, 3)
            assert ops[3] == {}, f"m_3 nonzero for {dga.name}"

    def test_m3_nonzero_for_lie(self):
        """m_3 = Jacobiator for sl_2 (non-associative Lie bracket)."""
        sl2 = lie_sl2_as_assoc()
        ops = extract_ainfty_operations(sl2, 3)
        assert len(ops[3]) > 0

    def test_m3_sl2_specific_value(self):
        """sl_2: m_3(e, e, f) = 2e.

        (e*e)*f - e*(e*f):
          e*e = [e,e] = 0, so (e*e)*f = 0.
          e*f = [e,f] = h, e*h = [e,h] = -2e.
          m_3 = 0 - (-2e) = 2e.
        """
        sl2 = lie_sl2_as_assoc()
        E, H, F = 0, 1, 2
        ops = extract_ainfty_operations(sl2, 3)
        assert ops[3][(E, E, F)] == {E: Rational(2)}

    def test_m3_sl2_ehh(self):
        """sl_2: m_3(e, h, h) = 4e.

        (e*h)*h - e*(h*h):
          e*h = -2e, (-2e)*h = -2*[e,h] = 4e.
          h*h = 0, e*0 = 0.
          m_3 = 4e.
        """
        sl2 = lie_sl2_as_assoc()
        E, H, F = 0, 1, 2
        ops = extract_ainfty_operations(sl2, 3)
        assert ops[3][(E, H, H)] == {E: Rational(4)}

    def test_m4_zero_for_associative(self):
        """m_4 = 0 for associative algebras."""
        dga = truncated_polynomial_dga(3)
        ops = extract_ainfty_operations(dga, 4)
        assert ops[4] == {}

    def test_ainfty_relation_0(self):
        """Stasheff relation n=0: trivially satisfied (m_0 = 0)."""
        dga = dual_numbers_dga()
        results = verify_ainfty_relations(dga, 3)
        assert results[0]

    def test_ainfty_relation_1_d_squared(self):
        """Stasheff relation n=1: m_1^2 = d^2 = 0."""
        dga = dual_numbers_dga()
        results = verify_ainfty_relations(dga, 3)
        assert results[1]

    def test_ainfty_relation_2_leibniz(self):
        """Stasheff relation n=2: Leibniz rule for d and m_2."""
        pwd = polynomial_with_diff()
        results = verify_ainfty_relations(pwd, 3)
        assert results[2]

    def test_ainfty_relation_3_associativity(self):
        """Stasheff relation n=3: associativity (m_3 = 0 for assoc algebras)."""
        dga = truncated_polynomial_dga(3)
        results = verify_ainfty_relations(dga, 3)
        assert results[3]

    def test_ainfty_relation_3_for_lie(self):
        """Stasheff relation n=3 for sl_2: m_3 = Jacobiator satisfies the relation."""
        sl2 = lie_sl2_as_assoc()
        results = verify_ainfty_relations(sl2, 3)
        assert results[3]

    def test_all_ainfty_relations_for_all_associative(self):
        """All Stasheff relations n=0..3 hold for all associative test algebras."""
        for dga_fn in [dual_numbers_dga, exterior_on_one_generator,
                       matrix_2x2_upper_dga, lambda: truncated_polynomial_dga(3)]:
            dga = dga_fn()
            results = verify_ainfty_relations(dga, 3)
            for n, ok in results.items():
                assert ok, f"Stasheff relation n={n} fails for {dga.name}"


# ============================================================================
# Section 9: Koszul sign conventions
# ============================================================================

class TestKoszulSigns:
    """Explicit sign checks for Koszul conventions."""

    def test_sign_even_even(self):
        """(-1)^{0*0} = 1: no sign for swapping even elements."""
        dga = dual_numbers_dga()
        assert dga.koszul_sign(0, 0) == 1

    def test_sign_odd_odd(self):
        """(-1)^{1*1} = -1: sign for swapping two odd elements."""
        dga = dual_numbers_dga()
        assert dga.koszul_sign(1, 1) == -1

    def test_sign_even_odd(self):
        """(-1)^{0*1} = 1: no sign for swapping even past odd."""
        dga = dual_numbers_dga()
        assert dga.koszul_sign(0, 1) == 1
        assert dga.koszul_sign(1, 0) == 1

    def test_sign_degree_2_3(self):
        """(-1)^{2*3} = 1: product of even degrees is even."""
        dga = dual_numbers_dga()
        assert dga.koszul_sign(2, 3) == 1

    def test_sign_degree_3_3(self):
        """(-1)^{3*3} = -1."""
        dga = dual_numbers_dga()
        assert dga.koszul_sign(3, 3) == -1

    def test_bar_diff_sign_at_degree_2(self):
        """Bar differential at degree 2: sign = (-1)^{|s^{-1}a_1|} = (-1)^1 = -1.

        For k[x]/(x^3) with all generators in degree 0:
        d_B(s^{-1}x|s^{-1}x) = (-1)^{|s^{-1}x|} * s^{-1}(x*x) = (-1)^1 * s^{-1}(x^2) = -s^{-1}(x^2).
        """
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 3)
        d2 = bar.differential(2)
        assert d2[1, 0] == Rational(-1)

    def test_bar_diff_sign_alternation(self):
        """Bar differential of k[x]/(x^3) at degree 3: signs alternate.

        d_B^3(s^{-1}x|s^{-1}x|s^{-1}x):
          p=0: -s^{-1}(x*x)|s^{-1}x gives (2,1) with -1
          p=1: +s^{-1}x|s^{-1}(x*x) gives (1,2) with +1
        """
        dga = truncated_polynomial_dga(3)
        bar = BarConstruction(dga, 4)
        d3 = bar.differential(3)
        # B^3 basis: (1,1,1), (1,1,2), (1,2,1), (1,2,2), (2,1,1), (2,1,2), (2,2,1), (2,2,2)
        # B^2 basis: (1,1), (1,2), (2,1), (2,2)
        basis_3 = bar.basis(3)
        basis_2 = bar.basis(2)
        col_111 = basis_3.index((1, 1, 1))
        row_21 = basis_2.index((2, 1))
        row_12 = basis_2.index((1, 2))
        assert d3[row_21, col_111] == Rational(-1)
        assert d3[row_12, col_111] == Rational(1)


# ============================================================================
# Section 10: Cross-checks with existing modules
# ============================================================================

class TestCrossChecks:
    """Cross-checks between bar_cobar_chain_maps and other modules."""

    def test_bar_complex_consistency(self):
        """Check that BarConstruction dimensions match bar_complex.py conventions.

        bar_complex.py uses OPEAlgebra; bar_cobar_chain_maps uses AugDGA.
        The bar degree n space has dimension (aug_dim)^n in both.

        NOTE: AugDGA treats index 0 as the unit. For sl_2 as an AugDGA
        with basis {e=0, h=1, f=2}, the augmentation ideal is {h, f}
        (indices 1 and 2), giving aug_dim = 2. This is an artifact of
        representing a Lie algebra in the AugDGA framework; the chiral
        bar_complex.py treats all generators as augmentation ideal elements.
        """
        sl2 = lie_sl2_as_assoc()
        bar = BarConstruction(sl2, 3)
        # Convention: index 0 = unit, aug_ideal = {1, 2}
        assert bar.aug_dim == 2
        assert bar.dim_at(1) == 2
        assert bar.dim_at(2) == 4
        assert bar.dim_at(3) == 8

    def test_verdier_dga_class_compatibility(self):
        """AugDGA and verdier_bar_cobar_pairing.DGA are structurally parallel.

        Both store (dim, degrees, diff, mult). AugDGA uses sympy Rational;
        DGA in verdier uses numpy floats. Results should be compatible.
        """
        dga = dual_numbers_dga()
        assert hasattr(dga, 'dim')
        assert hasattr(dga, 'degrees')
        assert hasattr(dga, 'diff')
        assert hasattr(dga, 'mult')
        assert hasattr(dga, 'd_squared_zero')

    def test_comparison_table_all_algebras(self):
        """The comparison table runs on all standard algebras without error."""
        table = bar_cobar_comparison_table(3)
        assert len(table) == 5
        for name, data in table.items():
            assert "associative" in data
            assert "bar_d_squared" in data
            assert "cobar_d_squared" in data

    def test_comparison_table_bar_d_squared_all_pass(self):
        """All associative algebras in the comparison table have bar d^2 = 0."""
        table = bar_cobar_comparison_table(3)
        for name, data in table.items():
            if data["associative"]:
                for n, ok in data["bar_d_squared"].items():
                    assert ok, f"bar d^2 != 0 for {name} at degree {n}"

    def test_comparison_table_counit_all_chain_maps(self):
        """Counit is a chain map for all algebras in the comparison table."""
        table = bar_cobar_comparison_table(3)
        for name, data in table.items():
            assert data["counit_chain_map"]["is_chain_map"], \
                f"counit not a chain map for {name}"

    def test_comparison_table_twisting_mc_trivial_aug_product(self):
        """MC equation satisfied for algebras with trivial product on aug ideal.

        MC holds when the product on the augmentation ideal is zero
        (dual numbers: eps*eps = 0; exterior: eps*eps = 0).
        It can fail for algebras with nontrivial aug ideal products
        (k[x]/(x^n), UT_2) due to sign convention in the code.
        """
        table = bar_cobar_comparison_table(3)
        # These should have MC satisfied
        assert table["dual_numbers"]["twisting_mc"]["mc_satisfied"]
        assert table["Lambda(1)"]["twisting_mc"]["mc_satisfied"]


# ============================================================================
# Section 11: Edge cases
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases: trivial algebra, minimal cases."""

    def test_trivial_algebra(self):
        """Trivial algebra {1}: augmentation ideal is empty.

        Bar construction has B^n = 0 for n >= 1.
        """
        trivial = AugDGA(
            dim=1, degrees=[0], diff=zeros(1, 1),
            mult={(0, 0): {0: Rational(1)}}, name="trivial"
        )
        assert trivial.is_associative()
        bar = BarConstruction(trivial, 3)
        assert bar.aug_dim == 0
        for n in range(1, 4):
            assert bar.dim_at(n) == 0

    def test_trivial_algebra_bar_d_squared(self):
        """Trivial algebra: bar d^2 = 0 trivially (all spaces are 0)."""
        trivial = AugDGA(1, [0], zeros(1, 1), {(0, 0): {0: Rational(1)}})
        bar = BarConstruction(trivial, 3)
        results = bar.verify_d_squared()
        for n, ok in results.items():
            assert ok

    def test_one_dim_aug_ideal(self):
        """Algebra with 1-dim augmentation ideal and zero product.

        This is the Heisenberg case: bar differential is zero.
        """
        dga = AugDGA(
            dim=2, degrees=[0, 0], diff=zeros(2, 2),
            mult={(0, 0): {0: Rational(1)}, (0, 1): {1: Rational(1)},
                  (1, 0): {1: Rational(1)}},
            name="one_gen_zero_prod"
        )
        bar = BarConstruction(dga, 4)
        assert bar.aug_dim == 1
        for n in range(2, 5):
            d = bar.differential(n)
            assert d.equals(zeros(d.rows, d.cols)), \
                f"Bar diff should be zero at degree {n} for zero product"

    def test_internal_differential_degree_0(self):
        """Internal differential at bar degree 0 is a 1x1 zero matrix."""
        dga = dual_numbers_dga()
        bar = BarConstruction(dga, 3)
        d0 = bar.internal_differential(0)
        assert d0.shape == (1, 1)
        assert d0[0, 0] == 0

    def test_unit_contraction_bar_degree_1(self):
        """Unit contraction from B^1 to B^{-1} is a zero matrix."""
        dga = dual_numbers_dga()
        bar = BarConstruction(dga, 3)
        uc = bar.unit_contraction(1)
        assert uc.equals(zeros(uc.rows, uc.cols))


# ============================================================================
# Section 12: Heisenberg-specific tests
# ============================================================================

class TestHeisenberg:
    """Tests specific to the Heisenberg algebra."""

    def test_heisenberg_bar_differential_zero(self):
        """Heisenberg at genus 0: bar differential = 0 (no product on aug ideal)."""
        result = heisenberg_bar_cobar()
        assert result["bar_differential_zero"]

    def test_heisenberg_bar_d_squared(self):
        """Heisenberg: d^2 = 0 at all bar degrees."""
        result = heisenberg_bar_cobar()
        for n, ok in result["bar_d_squared"].items():
            assert ok

    def test_heisenberg_twisting_mc(self):
        """Heisenberg: twisting morphism satisfies MC equation."""
        result = heisenberg_bar_cobar()
        assert result["twisting_mc"]["mc_satisfied"]

    def test_heisenberg_quasi_iso(self):
        """Heisenberg propagates the exact finite-window calculation."""
        result = heisenberg_bar_cobar()
        _assert_finite_scope(result["quasi_iso"])
        assert result["quasi_iso"]["counit"]["is_chain_map"]

    def test_heisenberg_kappa_parameter(self):
        """Heisenberg: kappa parameter is stored correctly."""
        result = heisenberg_bar_cobar(Rational(3, 2))
        assert result["kappa"] == Rational(3, 2)

    def test_heisenberg_cobar_d_squared(self):
        """Heisenberg: cobar d^2 = 0."""
        result = heisenberg_bar_cobar()
        for n, ok in result["cobar_d_squared"].items():
            assert ok


# ============================================================================
# Section 13: Free fermion tests
# ============================================================================

class TestFreeFermion:
    """Tests specific to the free fermion."""

    def test_free_fermion_bar_d_squared(self):
        """Free fermion: bar d^2 = 0 at all degrees."""
        result = free_fermion_bar_cobar()
        for n, ok in result["bar_d_squared"].items():
            assert ok

    def test_free_fermion_unit_contraction(self):
        """Free fermion: the shifted curvature term B^2 -> B^0 is [[-1]].

        The product psi*psi = 1 (unit, index 0) means the bar differential
        sends s^{-1}psi|s^{-1}psi -> 1 in B^0, captured by unit_contraction.
        """
        result = free_fermion_bar_cobar()
        uc = result["unit_contraction_B2"]
        # B^2 has dim 1 (one generator in aug ideal), B^0 has dim 1
        assert uc.shape == (1, 1)
        assert uc[0, 0] == Rational(-1)

    def test_free_fermion_curved_cobar_scope(self):
        """The relation psi^2=1 is routed to the curved cobar construction."""
        result = free_fermion_bar_cobar()
        assert result["bar_cobar_scope"] == "curved bar--cobar construction required"
        assert result["curved_cobar_status"] == "curvature differential awaits construction"


# ============================================================================
# Section 14: sl_2 affine tests
# ============================================================================

class TestSl2Affine:
    """Tests specific to sl_2 genus-0 bar-cobar."""

    def test_sl2_not_associative(self):
        """sl_2 Lie bracket is not associative."""
        result = sl2_affine_bar_cobar_genus0()
        assert not result["is_associative"]

    def test_sl2_bar_d_squared_fails(self):
        """sl_2: bar d^2 != 0 at degree 3 (non-associative)."""
        result = sl2_affine_bar_cobar_genus0()
        assert result["bar_d_squared"][3] is False

    def test_sl2_ainfty_m3_nonzero(self):
        """sl_2: m_3 (Jacobiator) is nonzero."""
        result = sl2_affine_bar_cobar_genus0()
        assert len(result["ainfty_ops"][3]) > 0

    def test_sl2_ainfty_relations_hold(self):
        """sl_2: all extracted A-infinity relations hold."""
        result = sl2_affine_bar_cobar_genus0()
        for n, ok in result["ainfty_relations"].items():
            assert ok, f"Stasheff relation n={n} fails for sl_2"


# ============================================================================
# Section 15: Functoriality
# ============================================================================

class TestFunctoriality:
    """Tests for bar-cobar functoriality."""

    def test_identity_map_is_chain_map(self):
        """Identity map on dual numbers: Omega(B(id)) is a chain map."""
        dga = dual_numbers_dga()
        f = eye(dga.dim)
        result = multiplication_dual_functoriality(dga, dga, f, 3)
        assert result["all_chain_map"]

    def test_identity_map_trunc_poly(self):
        """Identity map on k[x]/(x^3): functoriality holds."""
        dga = truncated_polynomial_dga(3)
        f = eye(dga.dim)
        result = multiplication_dual_functoriality(dga, dga, f, 3)
        assert result["all_chain_map"]

    def test_inclusion_is_chain_map(self):
        """Inclusion k[eps]/(eps^2) -> k[x]/(x^3): should be a chain map.

        Map: 1 -> 1, eps -> x (with x^2 in the larger algebra not in the image).
        """
        dga1 = dual_numbers_dga()
        dga2 = truncated_polynomial_dga(3)
        f = zeros(3, 2)
        f[0, 0] = Rational(1)  # 1 -> 1
        f[1, 1] = Rational(1)  # eps -> x
        result = multiplication_dual_functoriality(dga1, dga2, f, 3)
        assert result["all_chain_map"]


# ============================================================================
# Section 16: Cohomology helpers
# ============================================================================

class TestCohomologyHelpers:
    """Tests for exact cohomology computation helpers."""

    def test_kernel_dim_zero_matrix(self):
        """Kernel of the zero matrix is full space."""
        assert kernel_dim_exact(zeros(3, 3)) == 3

    def test_kernel_dim_identity(self):
        """Kernel of the identity matrix is 0."""
        assert kernel_dim_exact(eye(3)) == 0

    def test_image_dim_zero_matrix(self):
        """Image of the zero matrix is 0."""
        assert image_dim_exact(zeros(3, 3)) == 0

    def test_image_dim_identity(self):
        """Image of the identity matrix is full rank."""
        assert image_dim_exact(eye(3)) == 3

    def test_kernel_dim_empty_rows(self):
        """Kernel of a 0 x n matrix is n (no constraints)."""
        assert kernel_dim_exact(zeros(0, 3)) == 3

    def test_image_dim_empty_cols(self):
        """Image of an n x 0 matrix is 0 (no source)."""
        assert image_dim_exact(zeros(3, 0)) == 0

    def test_kernel_dim_rank_1(self):
        """Kernel of a rank-1 matrix has dim = cols - 1."""
        M = Matrix([[1, 2, 3]])
        assert kernel_dim_exact(M) == 2

    def test_cohomology_dims_exact_zero_complex(self):
        """Zero differentials: cohomology = total space at each degree."""
        diffs = {0: zeros(2, 2), 1: zeros(2, 2)}
        dims = {0: 2, 1: 2}
        coh = cohomology_dims_exact(diffs, dims)
        assert coh[0] == 2
        assert coh[1] == 2


# ============================================================================
# Section 17: Kronecker product
# ============================================================================

class TestKronecker:
    """Tests for the _kronecker helper function."""

    def test_kronecker_identity(self):
        """I_2 tensor I_2 = I_4."""
        result = _kronecker(eye(2), eye(2))
        assert result.equals(eye(4))

    def test_kronecker_scalar(self):
        """A tensor [[c]] = c*A."""
        A = Matrix([[1, 2], [3, 4]])
        c = Matrix([[Rational(5)]])
        result = _kronecker(A, c)
        expected = Rational(5) * A
        assert result.equals(expected)

    def test_kronecker_dimensions(self):
        """(m x n) tensor (p x q) = (mp x nq)."""
        A = zeros(2, 3)
        B = zeros(4, 5)
        result = _kronecker(A, B)
        assert result.shape == (8, 15)


# ============================================================================
# Section 18: Twisted tensor product
# ============================================================================

class TestTwistedTensorProduct:
    """Tests for the stated scope of the separate twisted tensor product."""

    def test_twisted_d_squared_dual_numbers(self):
        """Dual numbers retain the stated pending construction."""
        result = twisted_tensor_product_diff(dual_numbers_dga(), 3)
        assert result["calculation_status"] == "index range computed"
        assert result["construction_status"] == "total twisted differential pending"
        assert result["d_tau_squared_state"] == "pending construction"
        for n, ok in result["d_tau_squared"].items():
            assert ok is None

    def test_twisted_d_squared_trunc_poly(self):
        """The k[x]/(x^3) report carries the same stated scope."""
        result = twisted_tensor_product_diff(truncated_polynomial_dga(3), 3)
        assert result["calculation_status"] == "index range computed"
        assert result["construction_status"] == "total twisted differential pending"
        assert result["d_tau_squared_state"] == "pending construction"
        for n, ok in result["d_tau_squared"].items():
            assert ok is None


# ============================================================================
# Section 19: Polynomial with differential (nontrivial internal d)
# ============================================================================

class TestPolynomialWithDiff:
    """Tests for the square-zero pair d(x)=y."""

    def test_internal_differential_at_bar_1(self):
        """The shifted internal differential maps s^-1x to -s^-1y.

        Basis B^1 = {x, y}; the differential on A[-1] is -d_A.
        """
        pwd = polynomial_with_diff()
        bar = BarConstruction(pwd, 3)
        d1_int = bar.internal_differential(1)
        assert d1_int.shape == (2, 2)
        assert d1_int[1, 0] == Rational(-1)
        assert d1_int[0, 0] == 0
        assert d1_int[0, 1] == 0
        assert d1_int[1, 1] == 0

    def test_bar_d_squared_with_internal(self):
        """Bar of polynomial_with_diff: d_2^2 = 0 (mult component alone).

        The multiplication component d_2 satisfies d_2^2 = 0 because the algebra
        is associative. The TOTAL bar differential d = d_1 + d_2 should also
        satisfy d^2 = 0 when the Leibniz rule holds.
        """
        pwd = polynomial_with_diff()
        bar = BarConstruction(pwd, 4)
        # The verify_d_squared method only checks the multiplication component
        results = bar.verify_d_squared()
        for n in [2, 3]:
            assert results[n] is True


# ============================================================================
# Section 20: Regression and consistency checks
# ============================================================================

class TestConsistency:
    """Regression tests and internal consistency checks."""

    def test_bar_basis_caching(self):
        """Bar basis is cached and returns same object on repeated calls."""
        bar = BarConstruction(dual_numbers_dga(), 3)
        b1 = bar.basis(2)
        b2 = bar.basis(2)
        assert b1 is b2

    def test_bar_diff_caching(self):
        """Bar differential is cached and returns same object on repeated calls."""
        bar = BarConstruction(dual_numbers_dga(), 3)
        d1 = bar.differential(2)
        d2 = bar.differential(2)
        assert d1 is d2

    def test_multiplication_dual_basis_caching(self):
        """The multiplication-dual basis is cached."""
        bar = BarConstruction(dual_numbers_dga(), 3)
        cobar = MultiplicationDualComplex(bar, 3)
        b1 = cobar.basis(2)
        b2 = cobar.basis(2)
        assert b1 is b2

    def test_multiplication_dual_diff_caching(self):
        """The multiplication-dual differential is cached."""
        bar = BarConstruction(dual_numbers_dga(), 3)
        cobar = MultiplicationDualComplex(bar, 3)
        d1 = cobar.differential(1)
        d2 = cobar.differential(1)
        assert d1 is d2

    def test_bar_cobar_dual_numbers_self_consistent(self):
        """Dual numbers: bar, multiplication transpose, counit, and MC agree."""
        dga = dual_numbers_dga()
        bar = BarConstruction(dga, 4)
        cobar = MultiplicationDualComplex(bar, 4)

        # Bar d^2 = 0
        for n, ok in bar.verify_d_squared().items():
            assert ok
        # Multiplication transpose squares to zero.
        for n, ok in cobar.verify_d_squared().items():
            assert ok
        # Chain map
        cm = counit_chain_map_verify(dga, 3)
        assert cm["is_chain_map"]
        # MC
        mc = verify_twisting_mc(dga, 3)
        assert mc["mc_satisfied"]
        # Finite mixed-word calculation
        qi = verify_bar_cobar_quasi_iso(dga, 3)
        _assert_finite_scope(qi)

    def test_all_standard_families_bar_d_squared(self):
        """All associative standard algebras satisfy bar d^2 = 0.

        This is the fundamental theorem: associativity implies d_bar^2 = 0.
        """
        algebras = [
            dual_numbers_dga(),
            truncated_polynomial_dga(3),
            truncated_polynomial_dga(4),
            exterior_on_one_generator(),
            matrix_2x2_upper_dga(),
        ]
        for dga in algebras:
            assert dga.is_associative(), f"{dga.name} should be associative"
            bar = BarConstruction(dga, 4)
            results = bar.verify_d_squared()
            for n, ok in results.items():
                assert ok, f"d^2 != 0 for {dga.name} at bar degree {n}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
