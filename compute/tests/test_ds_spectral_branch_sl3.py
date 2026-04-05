"""Tests for DS spectral branch preservation (conj:ds-spectral-branch-preservation).

Verifies the conjecture that Drinfeld--Sokolov reduction preserves the
spectral branch object T_br (not merely its determinant Delta).

Core structure:
  1. Lie algebra data and DS central charges
  2. Bar cohomology dimensions and recurrences
  3. Discriminant and eigenvalue analysis
  4. Branch transport operator construction
  5. DS-invariant sub-discriminant preservation (sl₂ and sl₃ families)
  6. Generating function evaluation
  7. Characteristic polynomial factorization
  8. Full catalog verification

Ground truth references:
  - conj:ds-spectral-branch-preservation (examples_summary.tex)
  - def:spectral-branch-object (concordance.tex)
  - thm:ds-bar-gf-discriminant, thm:dominant-branch-point
  - conj:sl3-bar-gf, conj:w3-algebraicity
  - CLAUDE.md: central charge formulas, CE cohomology, W₃ composite
"""

import pytest
from sympy import Rational, Symbol, expand, factor, simplify, sqrt

from compute.lib.ds_spectral_branch_sl3 import (
    SL2_BAR_DIMS_EXTENDED,
    SL2_BAR_DIMS_PROVED,
    SL2_DATA,
    SL3_BAR_DIMS_CONJECTURED,
    SL3_BAR_DIMS_PROVED,
    SL3_DATA,
    SL4_DATA,
    VIR_BAR_DIMS,
    W3_BAR_DIMS_CONJECTURED,
    W3_BAR_DIMS_PROVED,
    BETAGAMMA_BAR_DIMS,
    BranchTransportOperator,
    DSSpectralBranchEntry,
    DiscriminantData,
    LieAlgebraData,
    SpectralBranchComparison,
    betagamma_discriminant,
    branch_operator_expected_rank,
    build_catalog,
    build_companion_matrix,
    build_transport_operator,
    ce_cohomology_sl2,
    ce_cohomology_sl3,
    ce_poincare_polynomial_sl_n,
    check_ds_invariant_eigenvalues_match,
    compare_spectral_branches,
    convergence_radius,
    discriminant_to_char_poly,
    discriminant_to_recurrence_coeffs,
    ds_invariant_eigenvalues_sl2,
    ds_invariant_eigenvalues_sl3,
    ds_invariant_factor_check_sl2,
    ds_invariant_factor_check_sl3,
    ds_invariant_factor_sl2,
    ds_invariant_factor_sl3,
    eigenvalues_distinct,
    eval_rational_gf,
    general_wn_complementarity_sum,
    generate_from_recurrence,
    lie_data,
    matrices_have_same_char_poly,
    matrices_similar_by_eigenvalues,
    non_shared_eigenvalues,
    num_weyl_generators,
    shared_eigenvalues,
    shared_quadratic_factor,
    sl2_discriminant,
    sl2_family_analysis,
    sl3_bar_recurrence,
    sl3_char_poly_factors,
    sl3_discriminant,
    sl3_family_analysis,
    sl3_gf_coefficients,
    spectral_radius,
    transport_operator_det_check,
    verify_catalog,
    verify_sl2_bar_from_discriminant,
    verify_sl3_bar_from_discriminant,
    verify_w3_bar_from_discriminant,
    virasoro_complementarity_sum,
    virasoro_discriminant,
    virasoro_ds_central_charge,
    w3_bar_recurrence,
    w3_char_poly_factors,
    w3_complementarity_sum,
    w3_discriminant,
    w3_ds_central_charge,
    w3_gf_coefficients,
    w_n_ds_central_charge,
    weyl_group_size,
)


# ===========================================================================
# 1. Lie algebra data
# ===========================================================================

class TestLieAlgebraData:
    """Verify root system data for simple Lie algebras."""

    def test_sl2_dimension(self):
        """dim(sl₂) = 3."""
        assert SL2_DATA.dimension == 3

    def test_sl2_rank(self):
        """rank(sl₂) = 1."""
        assert SL2_DATA.rank == 1

    def test_sl2_coxeter(self):
        """Coxeter number h(sl₂) = 2."""
        assert SL2_DATA.coxeter_number == 2

    def test_sl2_dual_coxeter(self):
        """Dual Coxeter h∨(sl₂) = 2 (simply-laced: h = h∨)."""
        assert SL2_DATA.dual_coxeter_number == 2

    def test_sl3_dimension(self):
        """dim(sl₃) = 8."""
        assert SL3_DATA.dimension == 8

    def test_sl3_rank(self):
        """rank(sl₃) = 2."""
        assert SL3_DATA.rank == 2

    def test_sl3_coxeter(self):
        """Coxeter number h(sl₃) = 3."""
        assert SL3_DATA.coxeter_number == 3

    def test_sl3_dual_coxeter(self):
        """h∨(sl₃) = 3 (simply-laced)."""
        assert SL3_DATA.dual_coxeter_number == 3

    def test_sl3_positive_roots(self):
        """sl₃ has 3 positive roots: α₁, α₂, α₁+α₂."""
        assert SL3_DATA.num_positive_roots == 3

    def test_sl3_exponents(self):
        """Exponents of sl₃ are (1, 2)."""
        assert SL3_DATA.exponents == (1, 2)

    def test_sl4_dimension(self):
        """dim(sl₄) = 15."""
        assert SL4_DATA.dimension == 15

    def test_lie_data_lookup(self):
        """lie_data catalog works."""
        assert lie_data("A1") == SL2_DATA
        assert lie_data("A2") == SL3_DATA


# ===========================================================================
# 2. DS central charges
# ===========================================================================

class TestDSCentralCharges:
    """DS reduction central charge formulas."""

    def test_virasoro_at_k0(self):
        """c_Vir(k=0) = 1 - 6·1/2 = -2."""
        assert virasoro_ds_central_charge(0) == -2

    def test_virasoro_at_k1(self):
        """c_Vir(k=1) = 1 - 6/3 = -1."""
        assert virasoro_ds_central_charge(1) == -1

    def test_virasoro_at_k_neg2(self):
        """k = -h∨ = -2 is critical level; c undefined (division by zero)."""
        # k = -2 gives denominator k + 2 = 0
        with pytest.raises((ZeroDivisionError, Exception)):
            virasoro_ds_central_charge(-2)

    def test_w3_at_k0(self):
        """c_W₃(k=0) = 2 - 24/3 = -6."""
        assert w3_ds_central_charge(0) == -6

    def test_w3_at_k1(self):
        """c_W₃(k=1) = 2 - 24/4 = -4."""
        assert w3_ds_central_charge(1) == -4

    def test_w3_at_critical(self):
        """k = -h∨ = -3 is critical level for sl₃; c undefined."""
        with pytest.raises((ZeroDivisionError, Exception)):
            w3_ds_central_charge(-3)

    def test_virasoro_complementarity(self):
        """c_Vir(k) + c_Vir(-k-4) = 2."""
        assert virasoro_complementarity_sum() == 2

    def test_w3_complementarity(self):
        """c_W₃(k) + c_W₃(-k-6) = 4."""
        assert w3_complementarity_sum() == 4

    def test_wn_virasoro_consistency(self):
        """W_N formula at N=2 gives Virasoro formula."""
        k = Symbol('k')
        c_wn2 = w_n_ds_central_charge(2, k)
        c_vir = virasoro_ds_central_charge(k)
        assert simplify(c_wn2 - c_vir) == 0

    def test_wn_w3_consistency(self):
        """W_N formula at N=3 gives W₃ formula."""
        k = Symbol('k')
        c_wn3 = w_n_ds_central_charge(3, k)
        c_w3 = w3_ds_central_charge(k)
        assert simplify(c_wn3 - c_w3) == 0

    def test_wn_complementarity_n2(self):
        """W₂ complementarity sum = 2."""
        assert general_wn_complementarity_sum(2) == 2

    def test_wn_complementarity_n3(self):
        """W₃ complementarity sum = 4."""
        assert general_wn_complementarity_sum(3) == 4


# ===========================================================================
# 3. Bar cohomology dimensions
# ===========================================================================

class TestBarCohomologyDimensions:
    """Ground truth bar cohomology data."""

    def test_sl2_h1(self):
        """H¹(B(sl₂)) = 3 = dim(sl₂)."""
        assert SL2_BAR_DIMS_PROVED[0] == 3

    def test_sl2_h2_corrected(self):
        """H²(B(sl₂)) = 5 (CE, corrected from Riordan R(5)=6)."""
        assert SL2_BAR_DIMS_PROVED[1] == 5

    def test_sl3_h1(self):
        """H¹(B(sl₃)) = 8 = dim(sl₃)."""
        assert SL3_BAR_DIMS_PROVED[0] == 8

    def test_sl3_h2(self):
        """H²(B(sl₃)) = 36."""
        assert SL3_BAR_DIMS_PROVED[1] == 36

    def test_sl3_h3(self):
        """H³(B(sl₃)) = 204."""
        assert SL3_BAR_DIMS_PROVED[2] == 204

    def test_w3_h1(self):
        """H¹(B(W₃)) = 2 (two generators T, W)."""
        assert W3_BAR_DIMS_PROVED[0] == 2

    def test_w3_h2(self):
        """H²(B(W₃)) = 5."""
        assert W3_BAR_DIMS_PROVED[1] == 5

    def test_w3_h3(self):
        """H³(B(W₃)) = 16."""
        assert W3_BAR_DIMS_PROVED[2] == 16

    def test_virasoro_h1(self):
        """H¹(B(Vir)) = 1."""
        assert VIR_BAR_DIMS[0] == 1

    def test_virasoro_h2(self):
        """H²(B(Vir)) = 2."""
        assert VIR_BAR_DIMS[1] == 2

    def test_betagamma_h1(self):
        """H¹(B(βγ)) = 2."""
        assert BETAGAMMA_BAR_DIMS[0] == 2


class TestRecurrences:
    """Bar cohomology recurrences."""

    def test_sl3_recurrence_matches_proved(self):
        """sl₃ recurrence a(n)=11a(n-1)-23a(n-2)-8a(n-3) matches proved values."""
        dims = sl3_bar_recurrence(SL3_BAR_DIMS_PROVED, 7)
        assert dims[:3] == SL3_BAR_DIMS_PROVED

    def test_sl3_recurrence_conjectured(self):
        """sl₃ recurrence produces conjectured H⁴ = 1352."""
        dims = sl3_bar_recurrence(SL3_BAR_DIMS_PROVED, 4)
        assert dims[3] == 1352

    def test_sl3_recurrence_full(self):
        """sl₃ recurrence through degree 7."""
        dims = sl3_bar_recurrence(SL3_BAR_DIMS_PROVED, 7)
        assert dims == SL3_BAR_DIMS_CONJECTURED

    def test_w3_recurrence_matches_proved(self):
        """W₃ recurrence a(n)=3a(n-1)+a(n-2)-1 matches proved values."""
        initial = [W3_BAR_DIMS_PROVED[0], W3_BAR_DIMS_PROVED[1]]
        dims = w3_bar_recurrence(initial, 3)
        assert dims[2] == W3_BAR_DIMS_PROVED[2]

    def test_w3_recurrence_conjectured(self):
        """W₃ recurrence produces conjectured H⁴ = 52."""
        initial = [W3_BAR_DIMS_PROVED[0], W3_BAR_DIMS_PROVED[1]]
        dims = w3_bar_recurrence(initial, 4)
        assert dims[3] == 52

    def test_w3_recurrence_h5(self):
        """W₃ recurrence produces conjectured H⁵ = 171."""
        initial = [W3_BAR_DIMS_PROVED[0], W3_BAR_DIMS_PROVED[1]]
        dims = w3_bar_recurrence(initial, 5)
        assert dims[4] == 171

    def test_w3_recurrence_full(self):
        """W₃ recurrence through degree 8."""
        initial = [W3_BAR_DIMS_PROVED[0], W3_BAR_DIMS_PROVED[1]]
        dims = w3_bar_recurrence(initial, 8)
        assert dims == W3_BAR_DIMS_CONJECTURED


# ===========================================================================
# 4. Discriminant data
# ===========================================================================

class TestDiscriminants:
    """Discriminant polynomials and eigenvalues."""

    def test_sl2_discriminant_coeffs(self):
        """sl₂ Δ = 1 - 2x - 3x² = (1-3x)(1+x)."""
        d = sl2_discriminant()
        assert d.discriminant_coeffs == (1, -2, -3)

    def test_sl2_discriminant_rank(self):
        """sl₂ T_br has rank 2."""
        assert sl2_discriminant().rank == 2

    def test_sl2_eigenvalues(self):
        """sl₂ T_br eigenvalues: {3, -1}."""
        d = sl2_discriminant()
        assert d.eigenvalues == (Rational(3), Rational(-1))

    def test_virasoro_matches_sl2(self):
        """Virasoro discriminant = sl₂ discriminant (DS invariance)."""
        assert (virasoro_discriminant().discriminant_coeffs ==
                sl2_discriminant().discriminant_coeffs)

    def test_betagamma_matches_sl2(self):
        """βγ discriminant = sl₂ discriminant (same branch locus)."""
        assert (betagamma_discriminant().discriminant_coeffs ==
                sl2_discriminant().discriminant_coeffs)

    def test_sl3_discriminant_coeffs(self):
        """sl₃ Δ = 1 - 11x + 23x² + 8x³ = (1-8x)(1-3x-x²)."""
        d = sl3_discriminant()
        assert d.discriminant_coeffs == (1, -11, 23, 8)

    def test_sl3_discriminant_factorization(self):
        """Verify (1-8x)(1-3x-x²) = 1 - 11x + 23x² + 8x³."""
        x = Symbol('x')
        product = expand((1 - 8*x) * (1 - 3*x - x**2))
        assert product == 1 - 11*x + 23*x**2 + 8*x**3

    def test_sl3_discriminant_rank(self):
        """sl₃ T_br has rank 3."""
        assert sl3_discriminant().rank == 3

    def test_sl3_dominant_eigenvalue(self):
        """sl₃ dominant eigenvalue = 8 = dim(sl₃)."""
        d = sl3_discriminant()
        assert d.eigenvalues[0] == Rational(8)

    def test_w3_discriminant_coeffs(self):
        """W₃ Δ = 1 - 4x + 2x² + x³ = (1-x)(1-3x-x²)."""
        d = w3_discriminant()
        assert d.discriminant_coeffs == (1, -4, 2, 1)

    def test_w3_discriminant_factorization(self):
        """Verify (1-x)(1-3x-x²) = 1 - 4x + 2x² + x³."""
        x = Symbol('x')
        product = expand((1 - x) * (1 - 3*x - x**2))
        assert product == 1 - 4*x + 2*x**2 + x**3

    def test_sl3_w3_discriminants_differ(self):
        """sl₃ and W₃ have DIFFERENT discriminants."""
        assert (sl3_discriminant().discriminant_coeffs !=
                w3_discriminant().discriminant_coeffs)


# ===========================================================================
# 5. Branch transport operator
# ===========================================================================

class TestBranchTransportOperator:
    """Construction and verification of T_br."""

    def test_sl2_companion_matrix(self):
        """sl₂ companion matrix is 2×2."""
        d = sl2_discriminant()
        mat = build_companion_matrix(d)
        assert mat.shape == (2, 2)

    def test_sl2_det_check(self):
        """det(1 - x·T_br) = 1 - 2x - 3x² for sl₂."""
        d = sl2_discriminant()
        op = build_transport_operator(d)
        det_expr = transport_operator_det_check(op)
        x = Symbol('x')
        expected = 1 - 2*x - 3*x**2
        assert expand(det_expr - expected) == 0

    def test_sl3_companion_matrix(self):
        """sl₃ companion matrix is 3×3."""
        d = sl3_discriminant()
        mat = build_companion_matrix(d)
        assert mat.shape == (3, 3)

    def test_sl3_det_check(self):
        """det(1 - x·T_br) = 1 - 11x + 23x² + 8x³ for sl₃."""
        d = sl3_discriminant()
        op = build_transport_operator(d)
        det_expr = transport_operator_det_check(op)
        x = Symbol('x')
        expected = 1 - 11*x + 23*x**2 + 8*x**3
        assert expand(det_expr - expected) == 0

    def test_w3_det_check(self):
        """det(1 - x·T_br) = 1 - 4x + 2x² + x³ for W₃."""
        d = w3_discriminant()
        op = build_transport_operator(d)
        det_expr = transport_operator_det_check(op)
        x = Symbol('x')
        expected = 1 - 4*x + 2*x**2 + x**3
        assert expand(det_expr - expected) == 0

    def test_virasoro_det_check(self):
        """det(1 - x·T_br) = 1 - 2x - 3x² for Virasoro."""
        d = virasoro_discriminant()
        op = build_transport_operator(d)
        det_expr = transport_operator_det_check(op)
        x = Symbol('x')
        expected = 1 - 2*x - 3*x**2
        assert expand(det_expr - expected) == 0

    def test_sl2_transport_eigenvalues(self):
        """T_br for sl₂ has eigenvalues {3, -1}."""
        d = sl2_discriminant()
        op = build_transport_operator(d)
        eigs = op.matrix.eigenvals()
        assert Rational(3) in eigs
        assert Rational(-1) in eigs


# ===========================================================================
# 6. DS-invariant factor
# ===========================================================================

class TestDSInvariantFactor:
    """DS-invariant sub-discriminant analysis."""

    def test_sl2_invariant_factor(self):
        """DS-invariant factor for sl₂ is (1+x)."""
        assert ds_invariant_factor_sl2() == (1, 1)

    def test_sl3_invariant_factor(self):
        """DS-invariant factor for sl₃ is (1-3x-x²)."""
        assert ds_invariant_factor_sl3() == (1, -3, -1)

    def test_sl2_invariant_eigenvalues(self):
        """DS-invariant eigenvalues for sl₂: {3, -1}."""
        eigs = ds_invariant_eigenvalues_sl2()
        assert eigs == (Rational(3), Rational(-1))

    def test_sl3_invariant_eigenvalues(self):
        """DS-invariant eigenvalues for sl₃: {(3±√13)/2}."""
        eigs = ds_invariant_eigenvalues_sl3()
        assert len(eigs) == 2
        # Sum should be 3, product should be -1
        assert simplify(eigs[0] + eigs[1]) == 3
        assert simplify(eigs[0] * eigs[1]) == -1

    def test_sl3_invariant_eigenvalue_product(self):
        """Product of DS-invariant eigenvalues = -1 (from t²-3t-1)."""
        eigs = ds_invariant_eigenvalues_sl3()
        assert simplify(eigs[0] * eigs[1]) == -1

    def test_sl3_invariant_eigenvalue_sum(self):
        """Sum of DS-invariant eigenvalues = 3 (from t²-3t-1)."""
        eigs = ds_invariant_eigenvalues_sl3()
        assert simplify(eigs[0] + eigs[1]) == 3

    def test_sl2_family_all_match(self):
        """All sl₂ family members share full discriminant."""
        result = ds_invariant_factor_check_sl2()
        assert result["all_match"] is True

    def test_sl3_discriminants_not_equal(self):
        """sl₃ and W₃ have different discriminants."""
        result = ds_invariant_factor_check_sl3()
        assert result["discriminants_equal"] is False

    def test_sl3_two_shared_eigenvalues(self):
        """sl₃ and W₃ share exactly 2 eigenvalues."""
        result = ds_invariant_factor_check_sl3()
        assert result["num_shared_eigenvalues"] == 2

    def test_sl3_shared_eigenvalues_are_ds_invariant(self):
        """Shared eigenvalues match the DS-invariant ones."""
        result = ds_invariant_factor_check_sl3()
        assert result["shared_eigenvalues_match_expected"] is True

    def test_sl3_dominant_eigenvalue_is_dim_g(self):
        """sl₃ dominant eigenvalue = 8 = dim(sl₃)."""
        result = ds_invariant_factor_check_sl3()
        assert result["sl3_dominant_eigenvalue"] == 8

    def test_w3_non_shared_eigenvalue(self):
        """W₃ non-shared eigenvalue = 1."""
        result = ds_invariant_factor_check_sl3()
        assert result["w3_non_shared_eigenvalue"] == 1


# ===========================================================================
# 7. Spectral branch comparison
# ===========================================================================

class TestSpectralBranchComparison:
    """Full spectral branch comparison under DS reduction."""

    def test_sl2_family_full_match(self):
        """sl₂ → Virasoro: full T_br similarity (proved)."""
        comp = sl2_family_analysis()
        assert comp.discriminants_match is True
        assert comp.eigenvalues_match is True
        assert comp.conjecture_holds is True

    def test_sl3_family_disc_no_match(self):
        """sl₃ → W₃: discriminants do NOT match."""
        comp = sl3_family_analysis()
        assert comp.discriminants_match is False

    def test_sl3_family_eig_no_match(self):
        """sl₃ → W₃: eigenvalues do NOT all match."""
        comp = sl3_family_analysis()
        assert comp.eigenvalues_match is False

    def test_sl3_family_ds_invariant_matches(self):
        """sl₃ → W₃: DS-invariant sub-discriminant DOES match."""
        comp = sl3_family_analysis()
        assert comp.ds_invariant_factor_matches is True

    def test_sl3_family_two_shared(self):
        """sl₃ → W₃: exactly 2 shared eigenvalues."""
        comp = sl3_family_analysis()
        assert len(comp.shared_eigenvalues) == 2

    def test_sl3_source_only_eigenvalue(self):
        """sl₃-hat has one eigenvalue not in W₃: 8."""
        comp = sl3_family_analysis()
        assert len(comp.source_only_eigenvalues) == 1
        assert comp.source_only_eigenvalues[0] == Rational(8)

    def test_sl3_target_only_eigenvalue(self):
        """W₃ has one eigenvalue not in sl₃-hat: 1."""
        comp = sl3_family_analysis()
        assert len(comp.target_only_eigenvalues) == 1
        assert comp.target_only_eigenvalues[0] == Rational(1)

    def test_sl2_eigenvalues_distinct(self):
        """sl₂ eigenvalues {3, -1} are distinct."""
        d = sl2_discriminant()
        assert eigenvalues_distinct(d.eigenvalues)

    def test_sl3_eigenvalues_distinct(self):
        """sl₃ eigenvalues are distinct."""
        d = sl3_discriminant()
        assert eigenvalues_distinct(d.eigenvalues)

    def test_w3_eigenvalues_distinct(self):
        """W₃ eigenvalues are distinct."""
        d = w3_discriminant()
        assert eigenvalues_distinct(d.eigenvalues)


# ===========================================================================
# 8. Recurrence from discriminant
# ===========================================================================

class TestRecurrenceFromDiscriminant:
    """Extracting linear recurrences from discriminant data."""

    def test_sl2_recurrence_coeffs(self):
        """sl₂ Δ = 1-2x-3x² gives recurrence [2, 3]."""
        d = sl2_discriminant()
        rec = discriminant_to_recurrence_coeffs(d)
        assert rec == [2, 3]

    def test_sl3_recurrence_coeffs(self):
        """sl₃ Δ = 1-11x+23x²+8x³ gives recurrence [11, -23, -8]."""
        d = sl3_discriminant()
        rec = discriminant_to_recurrence_coeffs(d)
        assert rec == [11, -23, -8]

    def test_w3_recurrence_coeffs(self):
        """W₃ Δ = 1-4x+2x²+x³ gives recurrence [4, -2, -1]."""
        d = w3_discriminant()
        rec = discriminant_to_recurrence_coeffs(d)
        assert rec == [4, -2, -1]

    def test_sl3_recurrence_generates_dims(self):
        """sl₃ recurrence from discriminant generates correct bar dims."""
        v = verify_sl3_bar_from_discriminant()
        assert v["matches_conjectured"] is True

    def test_w3_recurrence_generates_dims(self):
        """W₃ recurrence from discriminant generates correct bar dims."""
        v = verify_w3_bar_from_discriminant()
        assert v["matches_conjectured"] is True

    def test_w3_homogeneous_equals_inhomogeneous(self):
        """W₃ homogeneous depth-3 recurrence equals inhomogeneous depth-2.

        a(n) = 4a(n-1) - 2a(n-2) - a(n-3)   [homogeneous]
        a(n) = 3a(n-1) + a(n-2) - 1           [inhomogeneous]
        """
        # Generate from both
        hom = generate_from_recurrence(W3_BAR_DIMS_PROVED, [4, -2, -1], 8)
        inhom = w3_bar_recurrence(
            [W3_BAR_DIMS_PROVED[0], W3_BAR_DIMS_PROVED[1]], 8
        )
        assert hom == inhom


# ===========================================================================
# 9. Generating function evaluation
# ===========================================================================

class TestGeneratingFunctions:
    """Evaluation of conjectured rational generating functions."""

    def test_sl3_gf_first_coeff_zero(self):
        """sl₃ GF: a₀ = 0 (no constant term)."""
        coeffs = sl3_gf_coefficients(5)
        assert coeffs[0] == 0

    def test_sl3_gf_matches_proved(self):
        """sl₃ GF matches proved values 8, 36, 204."""
        coeffs = sl3_gf_coefficients(5)
        assert coeffs[1:4] == [8, 36, 204]

    def test_sl3_gf_h4_prediction(self):
        """sl₃ GF predicts H⁴ = 1352."""
        coeffs = sl3_gf_coefficients(5)
        assert coeffs[4] == 1352

    def test_sl3_gf_h5_prediction(self):
        """sl₃ GF predicts H⁵ = 9892."""
        coeffs = sl3_gf_coefficients(6)
        assert coeffs[5] == 9892

    def test_w3_gf_first_coeff_zero(self):
        """W₃ GF: a₀ = 0."""
        coeffs = w3_gf_coefficients(5)
        assert coeffs[0] == 0

    def test_w3_gf_matches_proved(self):
        """W₃ GF matches proved values 2, 5, 16."""
        coeffs = w3_gf_coefficients(5)
        assert coeffs[1:4] == [2, 5, 16]

    def test_w3_gf_h4_prediction(self):
        """W₃ GF predicts H⁴ = 52."""
        coeffs = w3_gf_coefficients(5)
        assert coeffs[4] == 52

    def test_w3_gf_h5_prediction(self):
        """W₃ GF predicts H⁵ = 171."""
        coeffs = w3_gf_coefficients(6)
        assert coeffs[5] == 171

    def test_w3_gf_extended(self):
        """W₃ GF matches all conjectured values."""
        coeffs = w3_gf_coefficients(9)
        assert coeffs[1:9] == W3_BAR_DIMS_CONJECTURED

    def test_sl3_gf_extended(self):
        """sl₃ GF matches all conjectured values."""
        coeffs = sl3_gf_coefficients(8)
        assert coeffs[1:8] == SL3_BAR_DIMS_CONJECTURED


# ===========================================================================
# 10. Characteristic polynomial factorization
# ===========================================================================

class TestCharPolyFactors:
    """Characteristic polynomial factorization."""

    def test_sl3_factorization_correct(self):
        """t³ - 11t² + 23t + 8 = (t-8)(t²-3t-1)."""
        result = sl3_char_poly_factors()
        assert result["factorization_correct"] is True

    def test_sl3_dominant_root(self):
        """sl₃ dominant root = 8."""
        result = sl3_char_poly_factors()
        assert result["dominant_root"] == 8

    def test_sl3_ds_invariant_quadratic(self):
        """sl₃ DS-invariant quadratic = t²-3t-1."""
        t = Symbol('t')
        result = sl3_char_poly_factors()
        assert expand(result["ds_invariant_quadratic"] - (t**2 - 3*t - 1)) == 0

    def test_w3_factorization_correct(self):
        """t³ - 4t² + 2t + 1 = (t-1)(t²-3t-1)."""
        result = w3_char_poly_factors()
        assert result["factorization_correct"] is True

    def test_w3_non_ds_root(self):
        """W₃ non-DS root = 1."""
        result = w3_char_poly_factors()
        assert result["non_ds_root"] == 1

    def test_shared_quadratic(self):
        """sl₃ and W₃ share the same DS-invariant quadratic t²-3t-1."""
        sl3_f = sl3_char_poly_factors()
        w3_f = w3_char_poly_factors()
        t = Symbol('t')
        diff = expand(sl3_f["ds_invariant_quadratic"] -
                      w3_f["ds_invariant_quadratic"])
        assert diff == 0


class TestSharedQuadratic:
    """Properties of the shared quadratic t²-3t-1."""

    def test_discriminant_is_13(self):
        """Discriminant of t²-3t-1 is 13."""
        result = shared_quadratic_factor()
        assert result["discriminant"] == 13

    def test_product_of_roots(self):
        """Product of roots = -1."""
        result = shared_quadratic_factor()
        assert result["product_of_roots"] == -1

    def test_sum_of_roots(self):
        """Sum of roots = 3."""
        result = shared_quadratic_factor()
        assert result["sum_of_roots"] == 3

    def test_roots_are_algebraic(self):
        """Roots (3±√13)/2 are algebraic of degree 2."""
        result = shared_quadratic_factor()
        roots = result["roots"]
        # Each root satisfies t²-3t-1=0
        for r in roots:
            assert simplify(r**2 - 3*r - 1) == 0

    def test_positive_root_approx(self):
        """(3+√13)/2 ≈ 3.303."""
        result = shared_quadratic_factor()
        val = float(result["roots"][0])
        assert abs(val - 3.303) < 0.001

    def test_negative_root_approx(self):
        """(3-√13)/2 ≈ -0.303."""
        result = shared_quadratic_factor()
        val = float(result["roots"][1])
        assert abs(val - (-0.303)) < 0.001


# ===========================================================================
# 11. Spectral radius and convergence
# ===========================================================================

class TestSpectralRadius:
    """Spectral radius = dim(g) for KM algebras."""

    def test_sl2_spectral_radius(self):
        """Spectral radius of sl₂ T_br = 3 = dim(sl₂)."""
        d = sl2_discriminant()
        assert simplify(spectral_radius(d) - 3) == 0

    def test_sl3_spectral_radius(self):
        """Spectral radius of sl₃ T_br = 8 = dim(sl₃)."""
        d = sl3_discriminant()
        assert simplify(spectral_radius(d) - 8) == 0

    def test_sl2_convergence_radius(self):
        """Convergence radius for sl₂: R = 1/3."""
        d = sl2_discriminant()
        assert simplify(convergence_radius(d) - Rational(1, 3)) == 0

    def test_sl3_convergence_radius(self):
        """Convergence radius for sl₃: R = 1/8."""
        d = sl3_discriminant()
        assert simplify(convergence_radius(d) - Rational(1, 8)) == 0


# ===========================================================================
# 12. CE cohomology cross-checks
# ===========================================================================

class TestCECohomology:
    """Chevalley-Eilenberg cohomology data."""

    def test_sl2_ce(self):
        """H*(sl₂) = (1, 0, 0, 1)."""
        assert ce_cohomology_sl2() == (1, 0, 0, 1)

    def test_sl3_ce(self):
        """H*(sl₃) = (1, 0, 0, 1, 0, 1, 0, 0, 1)."""
        assert ce_cohomology_sl3() == (1, 0, 0, 1, 0, 1, 0, 0, 1)

    def test_sl2_ce_total_dim(self):
        """Total dim H*(sl₂) = 2."""
        assert sum(ce_cohomology_sl2()) == 2

    def test_sl3_ce_total_dim(self):
        """Total dim H*(sl₃) = 4."""
        assert sum(ce_cohomology_sl3()) == 4

    def test_sl2_poincare_poly(self):
        """Poincare polynomial of sl₂: (1+t³)."""
        p = ce_poincare_polynomial_sl_n(2)
        expected = [0] * 4
        expected[0] = 1
        expected[3] = 1
        assert p == expected

    def test_sl3_poincare_poly(self):
        """Poincare polynomial of sl₃: (1+t³)(1+t⁵)."""
        p = ce_poincare_polynomial_sl_n(3)
        # (1+t³)(1+t⁵) = 1 + t³ + t⁵ + t⁸
        expected = [0] * 9
        expected[0] = 1
        expected[3] = 1
        expected[5] = 1
        expected[8] = 1
        assert p == expected

    def test_sl3_ce_matches_poincare(self):
        """CE cohomology of sl₃ matches Poincare polynomial."""
        ce = ce_cohomology_sl3()
        p = ce_poincare_polynomial_sl_n(3)
        assert list(ce) == p


# ===========================================================================
# 13. Similarity and matrix analysis
# ===========================================================================

class TestMatrixSimilarity:
    """Matrix similarity checks."""

    def test_sl2_sl2_same_char_poly(self):
        """sl₂ and Virasoro companion matrices have same char poly."""
        m1 = build_companion_matrix(sl2_discriminant())
        m2 = build_companion_matrix(virasoro_discriminant())
        assert matrices_have_same_char_poly(m1, m2)

    def test_sl3_w3_different_char_poly(self):
        """sl₃ and W₃ companion matrices have DIFFERENT char polys."""
        m1 = build_companion_matrix(sl3_discriminant())
        m2 = build_companion_matrix(w3_discriminant())
        assert not matrices_have_same_char_poly(m1, m2)

    def test_sl2_eigenvalues_similar(self):
        """sl₂ and Virasoro eigenvalues match (similarity follows)."""
        assert matrices_similar_by_eigenvalues(
            sl2_discriminant().eigenvalues,
            virasoro_discriminant().eigenvalues,
        )

    def test_sl3_w3_eigenvalues_not_similar(self):
        """sl₃ and W₃ eigenvalues do NOT match."""
        assert not matrices_similar_by_eigenvalues(
            sl3_discriminant().eigenvalues,
            w3_discriminant().eigenvalues,
        )


# ===========================================================================
# 14. Weyl group and expected rank
# ===========================================================================

class TestWeylGroupData:
    """Weyl group data for comparison."""

    def test_sl2_weyl_size(self):
        """|W(sl₂)| = 2."""
        assert weyl_group_size("A1") == 2

    def test_sl3_weyl_size(self):
        """|W(sl₃)| = 6."""
        assert weyl_group_size("A2") == 6

    def test_sl2_weyl_generators(self):
        """sl₂ has 1 simple reflection (rank 1)."""
        assert num_weyl_generators("A1") == 1

    def test_sl3_weyl_generators(self):
        """sl₃ has 2 simple reflections (rank 2)."""
        assert num_weyl_generators("A2") == 2

    def test_sl2_expected_rank(self):
        """Expected rank(T_br) for sl₂ = rank+1 = 2."""
        assert branch_operator_expected_rank("A1") == 2

    def test_sl3_expected_rank(self):
        """Expected rank(T_br) for sl₃ = rank+1 = 3."""
        assert branch_operator_expected_rank("A2") == 3


# ===========================================================================
# 15. Catalog
# ===========================================================================

class TestCatalog:
    """Full catalog consistency."""

    def test_catalog_has_two_entries(self):
        """Catalog has sl₂ and sl₃ entries."""
        cat = build_catalog()
        assert len(cat) == 2

    def test_catalog_sl2_status(self):
        """sl₂ entry has status 'proved'."""
        cat = build_catalog()
        assert cat[0].full_conjecture_status == "proved"

    def test_catalog_sl3_status(self):
        """sl₃ entry has status 'open'."""
        cat = build_catalog()
        assert cat[1].full_conjecture_status == "open"

    def test_verify_catalog_all_pass(self):
        """All catalog consistency checks pass."""
        results = verify_catalog()
        assert all(results.values()), f"Failed checks: {[k for k,v in results.items() if not v]}"

    def test_catalog_dominant_eigenvalues(self):
        """Dominant eigenvalue = dim(g) for both entries."""
        cat = build_catalog()
        assert cat[0].dominant_source_eigenvalue == 3
        assert cat[1].dominant_source_eigenvalue == 8

    def test_catalog_ds_invariant_sl3(self):
        """sl₃ entry DS-invariant factor = (1-3x-x²)."""
        cat = build_catalog()
        assert cat[1].ds_invariant_factor_coeffs == (1, -3, -1)


# ===========================================================================
# 16. Growth rate analysis
# ===========================================================================

class TestGrowthRates:
    """Exponential growth rates from discriminant eigenvalues."""

    def test_sl3_growth_rate(self):
        """sl₃ bar dims grow like 8^n (dominant eigenvalue)."""
        dims = sl3_bar_recurrence(SL3_BAR_DIMS_PROVED, 7)
        # Check ratio a(n)/a(n-1) → 8
        ratios = [dims[i] / dims[i-1] for i in range(3, 7)]
        # Should converge to 8
        assert all(6.5 < r < 8.5 for r in ratios)
        # Last ratio should be closest
        assert abs(ratios[-1] - 8) < abs(ratios[0] - 8)

    def test_w3_growth_rate(self):
        """W₃ bar dims grow like (3+√13)/2 ≈ 3.303."""
        dims = w3_bar_recurrence([2, 5], 10)
        ratios = [dims[i] / dims[i-1] for i in range(4, 10)]
        golden = (3 + 13**0.5) / 2  # ≈ 3.303
        # Should converge to golden
        assert all(2.5 < r < 4.0 for r in ratios)
        assert abs(ratios[-1] - golden) < 0.1

    def test_sl3_vs_w3_growth_rates_differ(self):
        """sl₃ grows faster than W₃ (8 > 3.303)."""
        sl3_dims = sl3_bar_recurrence(SL3_BAR_DIMS_PROVED, 7)
        w3_dims = w3_bar_recurrence([2, 5], 7)
        for i in range(1, 7):
            assert sl3_dims[i] > w3_dims[i]


# ===========================================================================
# 17. Conjecture interpretation tests
# ===========================================================================

class TestConjectureInterpretation:
    """Tests clarifying the precise statement of the conjecture.

    The conjecture (conj:ds-spectral-branch-preservation) states that
    T_br is preserved up to similarity under DS reduction.

    For the sl₃ case, the FULL discriminants differ:
      sl₃-hat: (1-8x)(1-3x-x²)
      W₃:      (1-x)(1-3x-x²)
    So the conjecture in its literal form DOES NOT HOLD at the level
    of the full discriminant.

    What IS preserved is the DS-invariant sub-discriminant (1-3x-x²),
    as proved by Theorem thm:ds-bar-gf-discriminant.  The conjecture
    should be interpreted as asking whether a REFINED version of T_br,
    restricted to the DS-invariant eigenspace, is preserved.
    """

    def test_full_conjecture_fails_literally_for_sl3(self):
        """The literal reading (full T_br similar) fails for sl₃→W₃."""
        comp = sl3_family_analysis()
        # Full eigenvalue match fails
        assert comp.eigenvalues_match is False

    def test_ds_invariant_part_preserved(self):
        """The DS-invariant part (sub-discriminant) IS preserved."""
        comp = sl3_family_analysis()
        assert comp.ds_invariant_factor_matches is True

    def test_sl2_conjecture_trivially_true(self):
        """For sl₂, the full conjecture is trivially true."""
        comp = sl2_family_analysis()
        assert comp.conjecture_holds is True

    def test_sl2_automatic_similarity(self):
        """sl₂: distinct eigenvalues ⟹ automatic similarity."""
        d = sl2_discriminant()
        assert eigenvalues_distinct(d.eigenvalues)
        comp = sl2_family_analysis()
        assert comp.conjecture_holds is True

    def test_ds_reduces_dominant_eigenvalue(self):
        """DS reduction changes dominant eigenvalue: 8 → 1 for sl₃."""
        comp = sl3_family_analysis()
        src_only = comp.source_only_eigenvalues
        tgt_only = comp.target_only_eigenvalues
        assert src_only[0] == Rational(8)  # dim(sl₃)
        assert tgt_only[0] == Rational(1)  # from (1-x) factor

    def test_refined_conjecture_holds(self):
        """Refined conjecture: DS-invariant eigenvalues match.

        The sub-discriminant factor (1-3x-x²) is shared, and the
        eigenvalues (3±√13)/2 of the DS-invariant T_br match.
        This is the content of Theorem thm:ds-bar-gf-discriminant
        applied to the sl₃ case.
        """
        sl3_eigs = ds_invariant_eigenvalues_sl3()
        # These should appear in both sl₃ and W₃
        sl3_disc = sl3_discriminant()
        w3_disc = w3_discriminant()
        shared = shared_eigenvalues(sl3_disc, w3_disc)
        assert len(shared) == 2
        for eig in sl3_eigs:
            found = any(simplify(eig - s) == 0 for s in shared)
            assert found, f"Expected DS-invariant eigenvalue {eig} not found in shared"


# ===========================================================================
# 18. Utility function tests
# ===========================================================================

class TestUtilities:
    """Tests for utility functions."""

    def test_eval_rational_gf_simple(self):
        """P(x) = 1/(1-x) = 1 + x + x² + ..."""
        coeffs = eval_rational_gf([1], [1, -1], 5)
        assert coeffs == [Rational(1)] * 5

    def test_eval_rational_gf_geometric(self):
        """P(x) = 1/(1-2x) = 1 + 2x + 4x² + 8x³ + ..."""
        coeffs = eval_rational_gf([1], [1, -2], 5)
        assert coeffs == [Rational(1), Rational(2), Rational(4),
                          Rational(8), Rational(16)]

    def test_generate_from_recurrence(self):
        """Linear recurrence a(n) = 2a(n-1) + 3a(n-2) starting from [1, 1]."""
        result = generate_from_recurrence([1, 1], [2, 3], 5)
        # a(2) = 2·1 + 3·1 = 5, a(3) = 2·5 + 3·1 = 13, a(4) = 2·13 + 3·5 = 41
        assert result == [1, 1, 5, 13, 41]

    def test_shared_eigenvalues_identical_discs(self):
        """Same discriminant → all eigenvalues shared."""
        d1 = sl2_discriminant()
        d2 = virasoro_discriminant()
        shared = shared_eigenvalues(d1, d2)
        assert len(shared) == 2

    def test_non_shared_eigenvalues_no_overlap(self):
        """sl₃ has eigenvalue 8 not in W₃."""
        d1 = sl3_discriminant()
        shared = shared_eigenvalues(d1, w3_discriminant())
        non_shared = non_shared_eigenvalues(d1, shared)
        assert len(non_shared) == 1
        assert non_shared[0] == Rational(8)

    def test_discriminant_to_char_poly_sl2(self):
        """Char poly for sl₂: t² - 2t - 3."""
        d = sl2_discriminant()
        cp = discriminant_to_char_poly(d)
        # t² - cp[0]*t - cp[1] = t² - 2t - 3
        assert cp == (Rational(2), Rational(3))

    def test_discriminant_to_char_poly_sl3(self):
        """Char poly for sl₃: t³ - 11t² + 23t + 8."""
        d = sl3_discriminant()
        cp = discriminant_to_char_poly(d)
        # t³ - cp[0]*t² - cp[1]*t - cp[2]
        assert cp == (Rational(11), Rational(-23), Rational(-8))
