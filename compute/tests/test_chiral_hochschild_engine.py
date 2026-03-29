"""Tests for the chiral Hochschild cohomology engine.

Verifies Theorem H computationally: ChirHoch*(A) concentrated in degrees
{0, 1, 2} with polynomial P_A(t) = dim Z(A) + dim H^1·t + dim Z(A!)·t².

Organized by:
  I.   ChirHoch^0 = Z(A) (center computation)
  II.  ChirHoch^2 = Z(A!)^∨ (Koszul dual center)
  III. ChirHoch^1 (derivation analysis — FRONTIER)
  IV.  Hilbert polynomial P_A(t) (unified)
  V.   Deformation-obstruction pairing
  VI.  Koszul functoriality and FF involution
  VII. W-algebra regime
  VIII. Cross-family consistency
  IX.  OPE-based verification
  X.   Spectral sequence and concentration

References:
  thm:hochschild-polynomial-growth (chiral_hochschild_koszul.tex)
  thm:main-koszul-hoch (chiral_hochschild_koszul.tex)
  thm:w-algebra-hochschild (hochschild_cohomology.tex)
"""

import pytest
from sympy import Symbol, Rational

from compute.lib.chiral_hochschild_engine import (
    # Data constructors
    ChiralAlgebraData,
    heisenberg_data,
    affine_sl2_data,
    affine_sl3_data,
    affine_slN_data,
    betagamma_data,
    bc_ghosts_data,
    free_fermion_data,
    virasoro_data,
    w3_data,
    wN_data,
    # ChirHoch^0
    center_dimension,
    center_dimension_koszul_dual,
    # ChirHoch^1
    DerivationAnalysis,
    derivation_analysis,
    # Polynomial
    HochschildPolynomial,
    compute_hochschild_polynomial,
    # W-algebra
    WAlgebraHochschild,
    compute_w_algebra_hochschild,
    # Deformation-obstruction
    DeformationObstruction,
    deformation_obstruction_analysis,
    all_deformations_unobstructed,
    # Koszul duality
    KoszulDualityRelation,
    koszul_duality_check,
    ff_involution_on_hochschild,
    # Master
    ChirHochResult,
    compute_chirhoch,
    compute_all_standard_families,
    # Verification
    verify_theorem_h_complete,
    verify_universal_polynomial,
    verify_km_h1_equals_dim_g,
    verify_additivity_under_tensor,
    verify_euler_char_additivity,
    # Spectral sequence
    hochschild_spectral_sequence_E2,
    # Whitehead
    whitehead_lemma_check,
    # OPE checks
    _ope_derivation_check_heisenberg,
    _ope_derivation_check_virasoro,
    _ope_derivation_check_w3,
    # Summary
    summary_table,
)


# ===================================================================
# I. ChirHoch^0 = Z(A) — center computation
# ===================================================================

class TestChirHoch0:
    """dim ChirHoch^0(A) = dim Z(A) = 1 for all standard families at generic level."""

    def test_heisenberg_center(self):
        """Z(H_k) = C at generic k."""
        assert center_dimension(heisenberg_data()) == 1

    def test_affine_sl2_center(self):
        """Z(ŝl_2_k) = C at generic k (not critical level)."""
        assert center_dimension(affine_sl2_data()) == 1

    def test_affine_sl3_center(self):
        """Z(ŝl_3_k) = C at generic k."""
        assert center_dimension(affine_sl3_data()) == 1

    def test_virasoro_center(self):
        """Z(Vir_c) = C at generic c."""
        assert center_dimension(virasoro_data()) == 1

    def test_w3_center(self):
        """Z(W_3) = C at generic c."""
        assert center_dimension(w3_data()) == 1

    def test_betagamma_center(self):
        """Z(βγ) = C."""
        assert center_dimension(betagamma_data()) == 1

    def test_bc_ghosts_center(self):
        """Z(bc) = C."""
        assert center_dimension(bc_ghosts_data()) == 1

    def test_free_fermion_center(self):
        """Z(ψ) = C."""
        assert center_dimension(free_fermion_data()) == 1

    def test_affine_slN_center_parametric(self):
        """Z(ŝl_N) = C for N = 2, ..., 10."""
        for N in range(2, 11):
            assert center_dimension(affine_slN_data(N)) == 1

    def test_wN_center_parametric(self):
        """Z(W_N) = C for N = 2, ..., 8."""
        for N in range(2, 9):
            assert center_dimension(wN_data(N)) == 1


# ===================================================================
# II. ChirHoch^2 = Z(A!)^∨ — Koszul dual center
# ===================================================================

class TestChirHoch2:
    """dim ChirHoch^2(A) = dim Z(A!) = 1 for all standard families."""

    def test_heisenberg_dual_center(self):
        """Z(H_k!) = Z(Sym^ch(V*)) = C."""
        assert center_dimension_koszul_dual(heisenberg_data()) == 1

    def test_virasoro_dual_center(self):
        """Z(Vir_{26-c}) = C (Koszul dual of Vir_c)."""
        assert center_dimension_koszul_dual(virasoro_data()) == 1

    def test_affine_sl2_dual_center(self):
        """Z(ŝl_2_{-k-4}) = C (FF dual)."""
        assert center_dimension_koszul_dual(affine_sl2_data()) == 1

    def test_betagamma_dual_center(self):
        """Z(bc) = C (βγ! = bc)."""
        assert center_dimension_koszul_dual(betagamma_data()) == 1

    def test_bc_dual_center(self):
        """Z(βγ) = C (bc! = βγ)."""
        assert center_dimension_koszul_dual(bc_ghosts_data()) == 1


# ===================================================================
# III. ChirHoch^1 — derivation analysis (FRONTIER)
# ===================================================================

class TestChirHoch1Heisenberg:
    """ChirHoch^1(H_k) = C (level deformation k → k+ε)."""

    def test_dim_h1(self):
        da = derivation_analysis(heisenberg_data())
        assert da.dim_chirhoch1 == 1

    def test_outer_eq_total(self):
        """For Heisenberg, all derivations are outer."""
        da = derivation_analysis(heisenberg_data())
        assert da.outer_derivations == da.total_derivations

    def test_level_deformation_type(self):
        da = derivation_analysis(heisenberg_data())
        assert 'level_deformation' in da.derivation_types


class TestChirHoch1AffineSl2:
    """ChirHoch^1(ŝl_2_k) = sl_2 (dim = 3).

    On the curve, the current algebra derivations J^a(z) contribute
    dim(g) = 3 to ChirHoch^1. The level deformation is absorbed.
    """

    def test_dim_h1(self):
        da = derivation_analysis(affine_sl2_data())
        assert da.dim_chirhoch1 == 3

    def test_equals_dim_g(self):
        """dim ChirHoch^1 = dim(sl_2) = 3."""
        data = affine_sl2_data()
        da = derivation_analysis(data)
        assert da.dim_chirhoch1 == data.lie_dim

    def test_all_unobstructed(self):
        da = derivation_analysis(affine_sl2_data())
        assert all(v for v in da.obstruction_to_extension.values())


class TestChirHoch1AffineSl3:
    """ChirHoch^1(ŝl_3_k) = sl_3 (dim = 8)."""

    def test_dim_h1(self):
        da = derivation_analysis(affine_sl3_data())
        assert da.dim_chirhoch1 == 8

    def test_equals_dim_g(self):
        data = affine_sl3_data()
        da = derivation_analysis(data)
        assert da.dim_chirhoch1 == data.lie_dim


class TestChirHoch1Virasoro:
    """ChirHoch^1(Vir_c) = C (c-deformation)."""

    def test_dim_h1(self):
        da = derivation_analysis(virasoro_data())
        assert da.dim_chirhoch1 == 1

    def test_c_deformation(self):
        da = derivation_analysis(virasoro_data())
        assert 'central_charge_deformation' in da.derivation_types

    def test_unobstructed(self):
        """Vir_c exists at all c — c-deformation unobstructed."""
        da = derivation_analysis(virasoro_data())
        for v in da.obstruction_to_extension.values():
            assert v is True


class TestChirHoch1W3:
    """ChirHoch^1(W_3) = C (c-deformation).

    W_3 has generators T (weight 2) and W (weight 3), but the only
    continuous deformation parameter is c. All other apparent
    deformations are gauge-equivalent.
    """

    def test_dim_h1(self):
        da = derivation_analysis(w3_data())
        assert da.dim_chirhoch1 == 1

    def test_c_deformation(self):
        da = derivation_analysis(w3_data())
        assert 'central_charge_deformation' in da.derivation_types

    def test_unobstructed(self):
        da = derivation_analysis(w3_data())
        for v in da.obstruction_to_extension.values():
            assert v is True


class TestChirHoch1Betagamma:
    """ChirHoch^1(βγ) = C^2 (charge rescaling + weight deformation)."""

    def test_dim_h1(self):
        da = derivation_analysis(betagamma_data())
        assert da.dim_chirhoch1 == 2

    def test_two_derivation_types(self):
        da = derivation_analysis(betagamma_data())
        assert len(da.derivation_types) == 2

    def test_charge_rescaling(self):
        da = derivation_analysis(betagamma_data())
        assert 'charge_rescaling' in da.derivation_types

    def test_weight_deformation(self):
        da = derivation_analysis(betagamma_data())
        assert 'weight_deformation' in da.derivation_types


class TestChirHoch1BcGhosts:
    """ChirHoch^1(bc) = C^2 (by Koszul duality with βγ)."""

    def test_dim_h1(self):
        da = derivation_analysis(bc_ghosts_data())
        assert da.dim_chirhoch1 == 2

    def test_matches_betagamma(self):
        """dim ChirHoch^1(bc) = dim ChirHoch^1(βγ) by Koszul duality."""
        da_bc = derivation_analysis(bc_ghosts_data())
        da_bg = derivation_analysis(betagamma_data())
        assert da_bc.dim_chirhoch1 == da_bg.dim_chirhoch1


class TestChirHoch1FreeFermion:
    """ChirHoch^1(ψ) = C (bilinear rescaling)."""

    def test_dim_h1(self):
        da = derivation_analysis(free_fermion_data())
        assert da.dim_chirhoch1 == 1


class TestChirHoch1KMParametric:
    """dim ChirHoch^1(ŝl_N) = N²-1 for all N."""

    @pytest.mark.parametrize("N,expected_dim", [
        (2, 3), (3, 8), (4, 15), (5, 24), (6, 35), (7, 48), (8, 63),
    ])
    def test_dim_h1_slN(self, N, expected_dim):
        data = affine_slN_data(N)
        da = derivation_analysis(data)
        assert da.dim_chirhoch1 == expected_dim
        assert da.dim_chirhoch1 == N * N - 1


class TestChirHoch1WNParametric:
    """dim ChirHoch^1(W_N) = 1 for all N >= 2."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_dim_h1_wN(self, N):
        if N == 2:
            data = virasoro_data()
        else:
            data = wN_data(N)
        da = derivation_analysis(data)
        assert da.dim_chirhoch1 == 1


# ===================================================================
# IV. Hilbert polynomial P_A(t) — unified
# ===================================================================

class TestHilbertPolynomial:
    """P_A(t) = 1 + dim(H^1)·t + t² for all standard quadratic families."""

    def test_heisenberg(self):
        poly = compute_hochschild_polynomial(heisenberg_data())
        assert poly.coefficients == [1, 1, 1]

    def test_affine_sl2(self):
        poly = compute_hochschild_polynomial(affine_sl2_data())
        assert poly.coefficients == [1, 3, 1]

    def test_affine_sl3(self):
        poly = compute_hochschild_polynomial(affine_sl3_data())
        assert poly.coefficients == [1, 8, 1]

    def test_betagamma(self):
        poly = compute_hochschild_polynomial(betagamma_data())
        assert poly.coefficients == [1, 2, 1]

    def test_bc_ghosts(self):
        poly = compute_hochschild_polynomial(bc_ghosts_data())
        assert poly.coefficients == [1, 2, 1]

    def test_free_fermion(self):
        poly = compute_hochschild_polynomial(free_fermion_data())
        assert poly.coefficients == [1, 1, 1]

    def test_w_algebra_raises(self):
        """W-algebras are not in quadratic regime — polynomial not defined."""
        with pytest.raises(ValueError, match="quadratic"):
            compute_hochschild_polynomial(virasoro_data())


class TestPolynomialProperties:
    """Properties of the Hochschild polynomial."""

    def test_heisenberg_euler_char(self):
        """χ(H_k) = P(-1) = 1 - 1 + 1 = 1."""
        poly = compute_hochschild_polynomial(heisenberg_data())
        assert poly.euler_characteristic == 1

    def test_affine_sl2_euler_char(self):
        """χ(ŝl_2) = 1 - 3 + 1 = -1."""
        poly = compute_hochschild_polynomial(affine_sl2_data())
        assert poly.euler_characteristic == -1

    def test_affine_sl3_euler_char(self):
        """χ(ŝl_3) = 1 - 8 + 1 = -6."""
        poly = compute_hochschild_polynomial(affine_sl3_data())
        assert poly.euler_characteristic == -6

    def test_betagamma_euler_char(self):
        """χ(βγ) = 1 - 2 + 1 = 0."""
        poly = compute_hochschild_polynomial(betagamma_data())
        assert poly.euler_characteristic == 0

    def test_palindromic_all_families(self):
        """P_A(t) is palindromic for all standard quadratic families
        (because dim Z(A) = dim Z(A!) = 1 at generic level)."""
        families = [
            heisenberg_data(), affine_sl2_data(), affine_sl3_data(),
            betagamma_data(), bc_ghosts_data(), free_fermion_data(),
        ]
        for data in families:
            poly = compute_hochschild_polynomial(data)
            assert poly.is_palindromic, f"Not palindromic: {data.name}"

    def test_total_dim_heisenberg(self):
        """P(1) = 1 + 1 + 1 = 3."""
        poly = compute_hochschild_polynomial(heisenberg_data())
        assert poly.total_dimension == 3

    def test_total_dim_affine_sl2(self):
        """P(1) = 1 + 3 + 1 = 5."""
        poly = compute_hochschild_polynomial(affine_sl2_data())
        assert poly.total_dimension == 5

    def test_evaluate_at_t(self):
        """P_A(t) evaluates correctly."""
        poly = compute_hochschild_polynomial(affine_sl2_data())
        assert poly.evaluate(0) == 1   # constant term
        assert poly.evaluate(1) == 5   # total dimension
        assert poly.evaluate(-1) == -1  # Euler characteristic

    def test_symbolic_polynomial(self):
        """Symbolic polynomial in t."""
        poly = compute_hochschild_polynomial(heisenberg_data())
        t = Symbol('t')
        expr = poly.symbolic()
        assert expr.subs(t, 0) == 1
        assert expr.subs(t, 1) == 3


class TestUniversalPolynomial:
    """Verify P_A(t) = 1 + dim(H^1)·t + t² universally."""

    def test_verify_universal(self):
        result = verify_universal_polynomial()
        assert result['all_passed'] is True

    def test_all_p0_eq_1(self):
        result = verify_universal_polynomial()
        for name, data in result['families'].items():
            assert data['p0_eq_1'], f"p0 ≠ 1 for {name}"

    def test_all_p2_eq_1(self):
        result = verify_universal_polynomial()
        for name, data in result['families'].items():
            assert data['p2_eq_1'], f"p2 ≠ 1 for {name}"


# ===================================================================
# V. Deformation-obstruction pairing
# ===================================================================

class TestDeformationObstruction:
    """[ξ, ξ] ∈ ChirHoch^2 for ξ ∈ ChirHoch^1."""

    def test_virasoro_c_unobstructed(self):
        """Vir_c exists at all c ⟹ [ξ_c, ξ_c] = 0."""
        assert all_deformations_unobstructed(virasoro_data())

    def test_w3_c_unobstructed(self):
        """W_3 exists at all generic c ⟹ [ξ_c, ξ_c] = 0."""
        assert all_deformations_unobstructed(w3_data())

    def test_affine_sl2_unobstructed(self):
        """ŝl_2_k exists at all k ⟹ all deformations unobstructed."""
        assert all_deformations_unobstructed(affine_sl2_data())

    def test_heisenberg_unobstructed(self):
        """H_k exists at all k ⟹ [ξ_k, ξ_k] = 0."""
        assert all_deformations_unobstructed(heisenberg_data())

    def test_betagamma_unobstructed(self):
        assert all_deformations_unobstructed(betagamma_data())

    def test_obstruction_list(self):
        """Deformation obstruction list is non-empty for each family."""
        obs = deformation_obstruction_analysis(virasoro_data())
        assert len(obs) >= 1
        assert obs[0].is_unobstructed

    def test_all_standard_unobstructed(self):
        """All standard families have unobstructed deformations."""
        families = [
            heisenberg_data(), affine_sl2_data(), affine_sl3_data(),
            betagamma_data(), bc_ghosts_data(), free_fermion_data(),
            virasoro_data(), w3_data(),
        ]
        for data in families:
            assert all_deformations_unobstructed(data), \
                f"Obstructed deformation in {data.name}"


# ===================================================================
# VI. Koszul functoriality and FF involution
# ===================================================================

class TestKoszulDuality:
    """ChirHoch^n(A) = ChirHoch^{2-n}(A!)^∨ ⊗ ω_X."""

    def test_betagamma_bc_duality(self):
        """βγ and bc are Koszul dual: Betti numbers reverse."""
        rel = koszul_duality_check(betagamma_data(), bc_ghosts_data())
        assert rel.relation_satisfied

    def test_bc_betagamma_duality(self):
        """Reverse direction: bc and βγ."""
        rel = koszul_duality_check(bc_ghosts_data(), betagamma_data())
        assert rel.relation_satisfied

    def test_heisenberg_self_palindromic(self):
        """H_k: Koszul dual has same dimensions."""
        # H_k! = Sym^ch: same center dimension
        rel = koszul_duality_check(heisenberg_data(), heisenberg_data())
        assert rel.relation_satisfied

    def test_affine_sl2_self_type(self):
        """ŝl_2_k and ŝl_2_{-k-4} have same Betti numbers."""
        rel = koszul_duality_check(affine_sl2_data(), affine_sl2_data())
        assert rel.relation_satisfied


class TestFFInvolution:
    """Feigin-Frenkel involution on ChirHoch."""

    def test_ff_sl2(self):
        result = ff_involution_on_hochschild(affine_sl2_data())
        assert result['ff_applicable'] is True
        assert result['h_dual'] == 2  # h∨(sl_2) = 2
        assert result['dimensions_match'] is True

    def test_ff_sl3(self):
        result = ff_involution_on_hochschild(affine_sl3_data())
        assert result['ff_applicable'] is True
        assert result['h_dual'] == 3

    def test_ff_virasoro(self):
        result = ff_involution_on_hochschild(virasoro_data())
        assert result['dimensions_match'] is True
        # Vir_c! = Vir_{26-c}
        assert 'Vir_c! = Vir_{26-c}' in result['note']

    def test_ff_betagamma(self):
        result = ff_involution_on_hochschild(betagamma_data())
        assert result['koszul_dual'] == 'bc_ghosts'

    def test_ff_not_applicable_to_free_field(self):
        """FF involution is specifically for KM algebras."""
        result = ff_involution_on_hochschild(free_fermion_data())
        assert result['ff_applicable'] is False


# ===================================================================
# VII. W-algebra regime
# ===================================================================

class TestWAlgebraVirasoro:
    """ChirHoch*(Vir_c) = C[Θ] with |Θ| = 2."""

    def test_gen_degrees(self):
        w = compute_w_algebra_hochschild(virasoro_data())
        assert w.gen_degrees == [2]

    def test_periodic(self):
        w = compute_w_algebra_hochschild(virasoro_data())
        assert w.is_periodic()

    def test_period_2(self):
        w = compute_w_algebra_hochschild(virasoro_data())
        assert w.quasi_period == 2

    def test_dim_even(self):
        """ChirHoch^{2k}(Vir) = C (one monomial Θ^k)."""
        w = compute_w_algebra_hochschild(virasoro_data())
        for k in range(10):
            assert w.dim_n(2 * k) == 1

    def test_dim_odd(self):
        """ChirHoch^{2k+1}(Vir) = 0."""
        w = compute_w_algebra_hochschild(virasoro_data())
        for k in range(10):
            assert w.dim_n(2 * k + 1) == 0

    def test_poincare_series(self):
        w = compute_w_algebra_hochschild(virasoro_data())
        expected = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        assert w.poincare_series(10) == expected


class TestWAlgebraW3:
    """ChirHoch*(W_3) = C[Θ_1, Θ_2] with |Θ_1|=2, |Θ_2|=3."""

    def test_gen_degrees(self):
        w = compute_w_algebra_hochschild(w3_data())
        assert w.gen_degrees == [2, 3]

    def test_not_periodic(self):
        w = compute_w_algebra_hochschild(w3_data())
        assert not w.is_periodic()

    def test_quasi_period(self):
        """lcm(2, 3) = 6."""
        w = compute_w_algebra_hochschild(w3_data())
        assert w.quasi_period == 6

    def test_first_values(self):
        """dim ChirHoch^n for n=0,...,12.

        Generators: Θ_1 (deg 2), Θ_2 (deg 3).
        Monomials by degree:
          0: 1 (empty)
          1: 0
          2: 1 (Θ_1)
          3: 1 (Θ_2)
          4: 1 (Θ_1²)
          5: 1 (Θ_1·Θ_2)
          6: 2 (Θ_1³, Θ_2²)
          7: 1 (Θ_1²·Θ_2)
          8: 2 (Θ_1⁴, Θ_1·Θ_2²)
          9: 2 (Θ_1³·Θ_2, Θ_2³)
          10: 2 (Θ_1⁵, Θ_1²·Θ_2²)
          11: 2 (Θ_1⁴·Θ_2, Θ_1·Θ_2³)
          12: 3 (Θ_1⁶, Θ_1³·Θ_2², Θ_2⁴)
        """
        w = compute_w_algebra_hochschild(w3_data())
        expected = [1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3]
        assert w.poincare_series(12) == expected

    def test_growth_rate(self):
        """Growth rate = 1 / (prod(h_i) * (r-1)!) = 1 / (2*3*1) = 1/6."""
        w = compute_w_algebra_hochschild(w3_data())
        assert abs(w.growth_coefficient() - 1.0 / 6.0) < 1e-10


class TestWAlgebraWN:
    """ChirHoch*(W_N) for higher N."""

    def test_w4_gen_degrees(self):
        """W_4: generators of weight 2, 3, 4."""
        w = compute_w_algebra_hochschild(wN_data(4))
        assert w.gen_degrees == [2, 3, 4]

    def test_w4_quasi_period(self):
        """lcm(2, 3, 4) = 12."""
        w = compute_w_algebra_hochschild(wN_data(4))
        assert w.quasi_period == 12

    def test_w5_gen_degrees(self):
        """W_5: generators of weight 2, 3, 4, 5."""
        w = compute_w_algebra_hochschild(wN_data(5))
        assert w.gen_degrees == [2, 3, 4, 5]

    def test_w5_first_values(self):
        """Verify first several Poincare numbers for W_5."""
        w = compute_w_algebra_hochschild(wN_data(5))
        series = w.poincare_series(10)
        # degree 0: 1, degree 1: 0, degree 2: 1 (Θ_2), degree 3: 1 (Θ_3),
        # degree 4: 2 (Θ_2², Θ_4), degree 5: 2 (Θ_2Θ_3, Θ_5)
        assert series[0] == 1
        assert series[1] == 0
        assert series[2] == 1
        assert series[3] == 1
        assert series[4] == 2
        assert series[5] == 2

    def test_w_algebra_dim0_always_1(self):
        """ChirHoch^0 = 1 (vacuum) for all W_N."""
        for N in range(2, 9):
            w = compute_w_algebra_hochschild(wN_data(N))
            assert w.dim_n(0) == 1

    def test_w_algebra_dim1_always_0(self):
        """ChirHoch^1 = 0 in the polynomial ring sense for all W_N.

        Note: dim ChirHoch^1 = 0 in the polynomial ring because the
        minimum generator degree is 2. The DERIVATION H^1 = 1 is a
        different computation (first-order deformation, not the
        polynomial ring grading).
        """
        for N in range(2, 9):
            w = compute_w_algebra_hochschild(wN_data(N))
            assert w.dim_n(1) == 0


# ===================================================================
# VIII. Cross-family consistency
# ===================================================================

class TestCrossFamilyConsistency:
    """Consistency checks across families."""

    def test_km_h1_equals_dim_g(self):
        """dim ChirHoch^1(ĝ_k) = dim(g) for all simple g."""
        result = verify_km_h1_equals_dim_g()
        assert result['all_passed'] is True

    def test_euler_char_multiplicativity(self):
        """χ(A ⊗ B) = χ(A) · χ(B)."""
        result = verify_euler_char_additivity(
            heisenberg_data(), affine_sl2_data()
        )
        assert result['matches'] is True

    def test_tensor_product_polynomial(self):
        """P_{H ⊗ ŝl_2}(t) properties."""
        result = verify_additivity_under_tensor(
            heisenberg_data(), affine_sl2_data()
        )
        assert result['applicable'] is True
        assert result['P_A'] == [1, 1, 1]
        assert result['P_B'] == [1, 3, 1]

    def test_betagamma_bc_euler_product(self):
        """χ(βγ) · χ(bc) = 0 · 0 = 0."""
        r = verify_euler_char_additivity(betagamma_data(), bc_ghosts_data())
        assert r['chi_A'] == 0
        assert r['chi_B'] == 0
        assert r['product'] == 0


# ===================================================================
# IX. OPE-based verification
# ===================================================================

class TestOPEVerification:
    """OPE compatibility of derivations."""

    def test_heisenberg_ope(self):
        result = _ope_derivation_check_heisenberg()
        assert result['consistent'] is True
        assert result['dim_derivation_space'] == 1

    def test_virasoro_ope(self):
        result = _ope_derivation_check_virasoro()
        assert result['consistent'] is True
        assert result['outer_quotient_dim'] == 1

    def test_w3_ope(self):
        result = _ope_derivation_check_w3()
        assert result['consistent'] is True
        assert result['outer_quotient_dim'] == 1


# ===================================================================
# X. Spectral sequence and concentration
# ===================================================================

class TestSpectralSequence:
    """E_2 page of Hochschild-to-ChirHoch spectral sequence."""

    def test_heisenberg_E2_collapses(self):
        """For Koszul Heisenberg: E_2^{p,q} = 0 for q > 0."""
        E2 = hochschild_spectral_sequence_E2(heisenberg_data(), max_p=5, max_q=3)
        for p in range(6):
            for q in range(1, 4):
                assert E2[p][q] == 0, f"E2[{p}][{q}] = {E2[p][q]} ≠ 0"

    def test_heisenberg_E2_row0(self):
        """E_2^{p,0} = dim ChirHoch^p."""
        E2 = hochschild_spectral_sequence_E2(heisenberg_data(), max_p=5)
        assert E2[0][0] == 1  # H^0
        assert E2[1][0] == 1  # H^1
        assert E2[2][0] == 1  # H^2
        assert E2[3][0] == 0  # H^3 = 0 (concentration)
        assert E2[4][0] == 0
        assert E2[5][0] == 0

    def test_virasoro_E2_row0(self):
        """E_2^{p,0} = dim ChirHoch^p for Virasoro."""
        E2 = hochschild_spectral_sequence_E2(virasoro_data(), max_p=10)
        expected = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        for p in range(11):
            assert E2[p][0] == expected[p]


# ===================================================================
# XI. Whitehead lemma compatibility
# ===================================================================

class TestWhiteheadCompatibility:
    """Whitehead H^n(g,g) = 0 is compatible with ChirHoch^1(ĝ_k) ≠ 0."""

    def test_whitehead_sl2(self):
        result = whitehead_lemma_check('A', 1)
        assert result['H1_g_g'] == 0
        assert result['H2_g_g'] == 0
        assert result['dim_g'] == 3

    def test_whitehead_sl3(self):
        result = whitehead_lemma_check('A', 2)
        assert result['H1_g_g'] == 0
        assert result['dim_g'] == 8


# ===================================================================
# XII. Master computation
# ===================================================================

class TestMasterComputation:
    """compute_chirhoch and compute_all_standard_families."""

    def test_heisenberg_master(self):
        result = compute_chirhoch(heisenberg_data())
        assert result.dim_H0 == 1
        assert result.dim_H1 == 1
        assert result.dim_H2 == 1
        assert result.polynomial is not None
        assert result.polynomial.coefficients == [1, 1, 1]
        assert result.all_unobstructed is True

    def test_affine_sl2_master(self):
        result = compute_chirhoch(affine_sl2_data())
        assert result.dim_H0 == 1
        assert result.dim_H1 == 3
        assert result.dim_H2 == 1
        assert result.poincare_polynomial == [1, 3, 1]

    def test_virasoro_master(self):
        result = compute_chirhoch(virasoro_data())
        assert result.dim_H0 == 1
        assert result.dim_H1 == 1
        assert result.dim_H2 == 1
        assert result.w_hochschild is not None
        assert result.w_hochschild.gen_degrees == [2]

    def test_w3_master(self):
        result = compute_chirhoch(w3_data())
        assert result.dim_H0 == 1
        assert result.dim_H1 == 1
        assert result.dim_H2 == 1
        assert result.w_hochschild.gen_degrees == [2, 3]

    def test_all_standard_families(self):
        all_results = compute_all_standard_families()
        assert len(all_results) >= 12
        for name, result in all_results.items():
            assert result.dim_H0 == 1, f"Z({name}) ≠ C"
            assert result.dim_H2 == 1, f"Z({name}!) ≠ C"
            assert result.dim_H1 >= 1, f"H^1({name}) = 0"
            assert result.all_unobstructed, f"Obstructed deformation in {name}"


class TestVerificationSuite:
    """Full verification suite."""

    def test_theorem_h_heisenberg(self):
        checks = verify_theorem_h_complete(heisenberg_data())
        assert checks['passed'] is True

    def test_theorem_h_affine_sl2(self):
        checks = verify_theorem_h_complete(affine_sl2_data())
        assert checks['passed'] is True

    def test_theorem_h_virasoro(self):
        checks = verify_theorem_h_complete(virasoro_data())
        assert checks['passed'] is True

    def test_theorem_h_w3(self):
        checks = verify_theorem_h_complete(w3_data())
        assert checks['passed'] is True

    def test_theorem_h_betagamma(self):
        checks = verify_theorem_h_complete(betagamma_data())
        assert checks['passed'] is True


class TestSummaryTable:
    """Summary table generation."""

    def test_table_nonempty(self):
        table = summary_table()
        assert len(table) >= 12

    def test_table_all_dim_h0_one(self):
        table = summary_table()
        for row in table:
            assert row['dim_H0'] == 1, f"dim_H0 ≠ 1 for {row['family']}"

    def test_table_all_unobstructed(self):
        table = summary_table()
        for row in table:
            assert row['unobstructed'] is True, \
                f"Obstructed for {row['family']}"


# ===================================================================
# XIII. Data constructor tests
# ===================================================================

class TestDataConstructors:
    """ChiralAlgebraData constructors."""

    def test_heisenberg_is_free_field(self):
        assert heisenberg_data().is_free_field()

    def test_affine_sl2_is_km(self):
        assert affine_sl2_data().is_km()

    def test_virasoro_is_w_algebra(self):
        assert virasoro_data().is_w_algebra()

    def test_betagamma_not_km(self):
        assert not betagamma_data().is_km()

    def test_affine_slN_lie_dim(self):
        for N in range(2, 8):
            data = affine_slN_data(N)
            assert data.lie_dim == N * N - 1

    def test_wN_gen_weights(self):
        for N in range(2, 8):
            data = wN_data(N)
            assert data.gen_weights == list(range(2, N + 1))
            assert data.n_generators == N - 1

    def test_symbolic_level(self):
        """Default level is symbolic."""
        data = affine_sl2_data()
        assert isinstance(data.level, Symbol)

    def test_numeric_level(self):
        """Numeric level when provided."""
        data = affine_sl2_data(k=1)
        assert data.level == 1

    def test_virasoro_central_charge(self):
        data = virasoro_data(c=26)
        assert data.central_charge == 26
