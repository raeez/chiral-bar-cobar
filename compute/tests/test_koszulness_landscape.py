"""Tests for the 15-algebra Koszulness landscape.

Verifies the PBW criterion computationally for each algebra,
cross-checks consistency, and tests corrections to initial claims.

The four checks per algebra:
    1. Strongly generated (finitely many generators)?
    2. PBW filtration exists?
    3. PBW spectral sequence collapses at E_2?
    4. Bar cohomology concentrated in bar degree 1?

These are linked: (1)+(2)+(3) => (4) by thm:pbw-koszulness-criterion.

CRITICAL CORRECTIONS verified in these tests:
    - L_1(sl_2) is NOT proved Koszul (null vector at h=2 in bar range)
    - Symplectic fermion IS Koszul (not "NOT Koszul")
    - Triplet W(2) is OPEN (not "NOT Koszul")
    - W_{1+infty} Koszulness requires MC4 completion (not plain PBW)
    - V_{-2}(sl_2) IS Koszul (critical level does not break UNIVERSAL)

Anti-pattern guards:
    AP1:  kappa formulas independently computed per family
    AP3:  each verdict from specific proof mechanism
    AP7:  universal claims tested against exceptions
    AP10: cross-family consistency (additivity, complementarity)
    AP14: shadow depth != Koszulness
    AP24: kappa + kappa' = 0 for KM, != 0 for Virasoro

References:
    thm:pbw-koszulness-criterion (chiral_koszul_pairs.tex)
    prop:pbw-universality (chiral_koszul_pairs.tex)
    cor:universal-koszul (chiral_koszul_pairs.tex)
    thm:kac-shapovalov-koszulness (chiral_koszul_pairs.tex)
    thm:lattice:koszul-morphism (lattice_foundations.tex)
    rem:sf-koszul-dual (deformation_quantization_examples.tex)
    rem:symplectic-logarithmic (beta_gamma.tex)
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, oo

from compute.lib.koszulness_landscape import (
    # Enums
    KoszulStatus,
    ProofMechanism,
    ShadowClass,
    # Algebra constructors
    heisenberg,
    affine_sl2_universal,
    affine_sl2_critical,
    affine_sl2_integrable_k1,
    virasoro_generic,
    virasoro_c0,
    minimal_model,
    w3_universal,
    betagamma_lambda1,
    free_fermion,
    d4_lattice,
    symplectic_fermion,
    triplet_w2,
    admissible_sl2,
    admissible_sl2_simple,
    w_1_plus_infinity,
    # Landscape
    build_landscape,
    # Verification
    verify_pbw_criterion,
    verify_landscape,
    # Cross-checks
    check_kappa_additivity,
    check_complementarity_consistency,
    check_shadow_depth_koszulness_independence,
    run_all_checks,
    # Kac-Shapovalov tools
    kac_determinant_sl2_null_weight,
    null_in_bar_range_sl2,
)


# ============================================================================
# Section 1: Individual algebra tests
# ============================================================================

class TestHeisenberg:
    """Algebra 1: Heisenberg H_k."""

    def test_koszul_status(self):
        h = heisenberg()
        assert h.koszul_status == KoszulStatus.PROVED

    def test_strongly_generated(self):
        h = heisenberg()
        assert h.strongly_generated is True
        assert h.num_generators == 1

    def test_pbw_criterion(self):
        h = heisenberg()
        assert h.pbw_filtration_exists is True
        assert h.pbw_collapse is True
        assert h.bar_concentrated is True

    def test_shadow_class(self):
        h = heisenberg()
        assert h.shadow_class == ShadowClass.G
        assert h.shadow_depth == 2

    def test_kappa(self):
        h = heisenberg(k=Rational(1))
        assert h.kappa == Rational(1)

    def test_proof_mechanism(self):
        h = heisenberg()
        assert h.proof_mechanism == ProofMechanism.PBW_UNIVERSALITY


class TestAffineSl2Universal:
    """Algebra 2: V_k(sl_2) at generic k."""

    def test_koszul_status(self):
        data = affine_sl2_universal()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_three_generators(self):
        data = affine_sl2_universal()
        assert data.num_generators == 3
        assert data.strongly_generated is True

    def test_pbw_criterion(self):
        data = affine_sl2_universal()
        assert data.pbw_filtration_exists is True
        assert data.pbw_collapse is True
        assert data.bar_concentrated is True

    def test_kappa_formula(self):
        """kappa(sl_2) = 3(k+2)/4 = dim(g)*(k+h^v)/(2*h^v).

        Independent computation:
        dim(sl_2) = 3, h^vee(sl_2) = 2.
        kappa = 3*(k+2)/(2*2) = 3(k+2)/4.
        """
        data = affine_sl2_universal(k=Rational(1))
        assert data.kappa == Rational(9, 4)  # 3*(1+2)/4

    def test_kappa_at_k0(self):
        data = affine_sl2_universal(k=Rational(0))
        assert data.kappa == Rational(3, 2)  # 3*(0+2)/4

    def test_shadow_class(self):
        data = affine_sl2_universal()
        assert data.shadow_class == ShadowClass.L
        assert data.shadow_depth == 3


class TestAffineSl2Critical:
    """Algebra 3: V_{-2}(sl_2) at critical level k = -h^vee = -2."""

    def test_koszul_status(self):
        """CRITICAL: the UNIVERSAL algebra is Koszul even at critical level.

        cor:universal-koszul applies at ALL k, including k = -h^vee.
        The critical level does not break Koszulness of V_k(g);
        it breaks Koszulness of the SIMPLE QUOTIENT L_k(g).
        """
        data = affine_sl2_critical()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_kappa_zero(self):
        """At critical level, kappa = 0 (uncurved)."""
        data = affine_sl2_critical()
        assert data.kappa == Rational(0)

    def test_still_universal(self):
        data = affine_sl2_critical()
        assert data.algebra_type == "universal"


class TestAffineSl2IntegrableK1:
    """Algebra 4: L_1(sl_2) simple quotient at integrable level k=1.

    CORRECTION: The user claimed 'Koszul (simple quotient of Koszul
    algebra — check!)'.  This is WRONG.

    Being a quotient of a Koszul algebra does NOT imply Koszulness.
    The null vector at h = 2 is in the bar-relevant range [h >= 2].
    Status: OPEN.
    """

    def test_koszul_status_is_open(self):
        """L_1(sl_2) Koszulness is OPEN, not proved."""
        data = affine_sl2_integrable_k1()
        assert data.koszul_status == KoszulStatus.OPEN

    def test_null_vector_in_bar_range(self):
        """First null at h=2 IS in bar-relevant range."""
        # k=1: p=3, q=1
        h_null = kac_determinant_sl2_null_weight(3, 1)
        assert h_null == 2
        assert null_in_bar_range_sl2(3, 1) is True

    def test_is_simple_quotient(self):
        data = affine_sl2_integrable_k1()
        assert data.algebra_type == "simple_quotient"

    def test_pbw_fails(self):
        data = affine_sl2_integrable_k1()
        assert data.pbw_filtration_exists is False

    def test_proof_mechanism(self):
        data = affine_sl2_integrable_k1()
        assert data.proof_mechanism == ProofMechanism.NULL_VECTOR_OBSTRUCTION


class TestVirasoroGeneric:
    """Algebra 5: Vir_c at generic c."""

    def test_koszul_status(self):
        data = virasoro_generic()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_single_generator(self):
        data = virasoro_generic()
        assert data.num_generators == 1
        assert data.generator_weights == [2]

    def test_pbw_criterion(self):
        data = virasoro_generic()
        assert data.pbw_filtration_exists is True
        assert data.pbw_collapse is True
        assert data.bar_concentrated is True

    def test_shadow_class_M(self):
        """Shadow depth infinity does NOT prevent Koszulness (AP14)."""
        data = virasoro_generic()
        assert data.shadow_class == ShadowClass.M
        assert data.shadow_depth == 10**9
        assert data.is_koszul is True  # Koszul despite infinite depth


class TestVirasoroC0:
    """Algebra 6: Vir at c = 0."""

    def test_koszul_status(self):
        data = virasoro_c0()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_kappa_zero(self):
        """kappa = c/2 = 0. Uncurved but still Koszul."""
        data = virasoro_c0()
        assert data.kappa == Rational(0)

    def test_still_strongly_generated(self):
        data = virasoro_c0()
        assert data.strongly_generated is True


class TestMinimalModel:
    """Algebra 7: Minimal model L(c_{p,q}, 0).

    Null vectors break PBW. Status: NOT Koszul (for models
    where the null vector is in the bar-relevant range).
    """

    def test_ising_not_koszul(self):
        """Ising model (3,4): c = 1/2, null at h = 6."""
        data = minimal_model(3, 4)
        assert data.koszul_status == KoszulStatus.NOT_KOSZUL
        assert data.central_charge == Rational(1, 2)

    def test_yang_lee_not_koszul(self):
        """Yang-Lee (2,5): c = -22/5, null at h = 4."""
        data = minimal_model(2, 5)
        assert data.koszul_status == KoszulStatus.NOT_KOSZUL
        assert data.central_charge == Rational(-22, 5)

    def test_trivial_model(self):
        """(2,3) model: c = 0, null at h = 2."""
        data = minimal_model(2, 3)
        # h_null = 2*3 - 2 - 3 + 1 = 2; bar-relevant min is 4
        # h_null = 2 < 4: NOT in bar-relevant range!
        # So this case is OPEN, not NOT_KOSZUL
        assert data.central_charge == Rational(0)

    def test_null_weight_ising(self):
        """Ising: first null at h = pq - p - q + 1 = 12 - 3 - 4 + 1 = 6."""
        data = minimal_model(3, 4)
        # h_null = 6, bar-relevant min = 4
        # 6 >= 4: in bar-relevant range
        assert data.koszul_status == KoszulStatus.NOT_KOSZUL

    def test_null_weight_yang_lee(self):
        """Yang-Lee: first null at h = 10 - 2 - 5 + 1 = 4."""
        data = minimal_model(2, 5)
        # h_null = 4, bar-relevant min = 4
        # 4 >= 4: in bar-relevant range
        assert data.koszul_status == KoszulStatus.NOT_KOSZUL

    def test_simple_quotient_type(self):
        data = minimal_model(3, 4)
        assert data.algebra_type == "simple_quotient"

    def test_invalid_inputs(self):
        with pytest.raises(ValueError):
            minimal_model(1, 3)  # p < 2
        with pytest.raises(ValueError):
            minimal_model(4, 3)  # p >= q
        with pytest.raises(ValueError):
            minimal_model(2, 4)  # gcd != 1


class TestW3Universal:
    """Algebra 8: W_3 (universal) at generic c."""

    def test_koszul_status(self):
        data = w3_universal()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_two_generators(self):
        data = w3_universal()
        assert data.num_generators == 2
        assert 2 in data.generator_weights
        assert 3 in data.generator_weights

    def test_shadow_class_M(self):
        """W_3 has infinite shadow depth (class M) but IS Koszul (AP14)."""
        data = w3_universal()
        assert data.shadow_class == ShadowClass.M
        assert data.is_koszul is True


class TestBetagamma:
    """Algebra 9: betagamma at lambda = 1."""

    def test_koszul_status(self):
        data = betagamma_lambda1()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_shadow_class_C(self):
        data = betagamma_lambda1()
        assert data.shadow_class == ShadowClass.C
        assert data.shadow_depth == 4

    def test_kappa(self):
        data = betagamma_lambda1()
        assert data.kappa == Rational(1)
        assert data.central_charge == Rational(2)


class TestFreeFermion:
    """Algebra 10: Free fermion."""

    def test_koszul_status(self):
        data = free_fermion()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_single_generator(self):
        data = free_fermion()
        assert data.num_generators == 1
        assert data.generator_weights == [Rational(1, 2)]

    def test_kappa(self):
        data = free_fermion()
        assert data.kappa == Rational(1, 4)

    def test_shadow_class_G(self):
        data = free_fermion()
        assert data.shadow_class == ShadowClass.G
        assert data.shadow_depth == 2


class TestD4Lattice:
    """Algebra 11: D_4 lattice VOA."""

    def test_koszul_status(self):
        data = d4_lattice()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_proof_mechanism_is_lattice(self):
        """Lattice VOAs use lattice filtration, NOT PBW universality."""
        data = d4_lattice()
        assert data.proof_mechanism == ProofMechanism.LATTICE_FILTRATION

    def test_kappa(self):
        """kappa = rank = 4 for D_4 (all generators weight 1)."""
        data = d4_lattice()
        assert data.kappa == Rational(4)

    def test_shadow_class_G(self):
        data = d4_lattice()
        assert data.shadow_class == ShadowClass.G


class TestSymplecticFermion:
    """Algebra 12: Symplectic fermion.

    CRITICAL CORRECTION: The user claimed 'NOT Koszul? (logarithmic
    VOA)'.  This is WRONG.

    The symplectic fermion IS Koszul (rem:symplectic-logarithmic:
    "the system is Koszul").  Logarithmic phenomena appear in the
    MODULE category, not in the bar complex of the algebra.
    """

    def test_is_koszul(self):
        """Symplectic fermion IS Koszul."""
        data = symplectic_fermion()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_strongly_generated(self):
        data = symplectic_fermion()
        assert data.strongly_generated is True

    def test_pbw_criterion(self):
        data = symplectic_fermion()
        assert data.pbw_filtration_exists is True
        assert data.pbw_collapse is True
        assert data.bar_concentrated is True

    def test_kappa(self):
        """c = -1, kappa = -1/2 for symplectic fermion at lambda=1/2."""
        data = symplectic_fermion()
        assert data.kappa == Rational(-1, 2)
        assert data.central_charge == Rational(-1)

    def test_proof_mechanism(self):
        data = symplectic_fermion()
        assert data.proof_mechanism == ProofMechanism.PBW_UNIVERSALITY


class TestTripletW2:
    """Algebra 13: Triplet W(2) at c = -2.

    CORRECTION: The user claimed 'NOT Koszul (logarithmic)'.
    The correct status is OPEN.

    The triplet MAY fail bar concentration, but this is not proved.
    C_2-cofiniteness does not determine Koszulness.
    """

    def test_koszul_status_is_open(self):
        """Triplet W(2) Koszulness is OPEN, not 'NOT Koszul'."""
        data = triplet_w2()
        assert data.koszul_status == KoszulStatus.OPEN

    def test_logarithmic_type(self):
        data = triplet_w2()
        assert data.algebra_type == "logarithmic"

    def test_central_charge(self):
        data = triplet_w2()
        assert data.central_charge == Rational(-2)


class TestAdmissibleSl2:
    """Algebra 14: V_k(sl_2) at admissible k.

    Universal algebra: ALWAYS Koszul.
    Simple quotient: OPEN.
    """

    def test_universal_is_koszul(self):
        data = admissible_sl2(3, 2)  # k = -1/2
        assert data.koszul_status == KoszulStatus.PROVED

    def test_simple_is_open(self):
        data = admissible_sl2_simple(3, 2)  # k = -1/2
        assert data.koszul_status == KoszulStatus.OPEN

    def test_null_in_bar_range_admissible(self):
        """At k = -1/2 (p=3, q=2): first null at h = (3-1)*2 = 4."""
        h_null = kac_determinant_sl2_null_weight(3, 2)
        assert h_null == 4
        assert null_in_bar_range_sl2(3, 2) is True

    def test_universal_vs_simple_distinction(self):
        """Universal and simple quotient have different Koszul status."""
        u = admissible_sl2(3, 2)
        s = admissible_sl2_simple(3, 2)
        assert u.koszul_status == KoszulStatus.PROVED
        assert s.koszul_status == KoszulStatus.OPEN


class TestW1PlusInfinity:
    """Algebra 15: W_{1+infinity}.

    Infinitely many generators.  Koszulness proved via MC4
    completion tower, not plain PBW universality.
    """

    def test_koszul_status(self):
        data = w_1_plus_infinity()
        assert data.koszul_status == KoszulStatus.PROVED

    def test_infinite_generators(self):
        data = w_1_plus_infinity()
        assert data.num_generators >= 10**9
        assert data.finite_generators is False

    def test_proof_mechanism(self):
        """MC4 completion tower, not plain PBW."""
        data = w_1_plus_infinity()
        assert data.proof_mechanism == ProofMechanism.COMPLETION_TOWER

    def test_shadow_class_M(self):
        data = w_1_plus_infinity()
        assert data.shadow_class == ShadowClass.M


# ============================================================================
# Section 2: Landscape-wide tests
# ============================================================================

class TestLandscapeCompleteness:
    """Verify the full 15-algebra landscape."""

    def test_landscape_has_15_algebras(self):
        landscape = build_landscape()
        assert len(landscape) == 15

    def test_all_have_verdicts(self):
        landscape = build_landscape()
        for name, data in landscape.items():
            assert data.koszul_status in KoszulStatus, (
                f"{name} missing Koszul verdict"
            )

    def test_proved_count(self):
        """Count proved Koszul algebras."""
        landscape = build_landscape()
        proved = sum(1 for d in landscape.values()
                     if d.koszul_status == KoszulStatus.PROVED)
        # Expected: 11 proved (all except L_1(sl_2), minimal model,
        # triplet W(2), admissible simple quotient... but we included
        # admissible UNIVERSAL which is proved)
        # Proved: heisenberg, sl2_universal, sl2_critical, virasoro_generic,
        # virasoro_c0, w3_universal, betagamma, free_fermion, d4_lattice,
        # symplectic_fermion, sl2_admissible_universal, w_1_plus_infinity
        assert proved == 12

    def test_open_count(self):
        """Count OPEN algebras."""
        landscape = build_landscape()
        open_count = sum(1 for d in landscape.values()
                         if d.koszul_status == KoszulStatus.OPEN)
        # Expected: sl2_integrable_k1, triplet_w2 = 2
        assert open_count == 2

    def test_not_koszul_count(self):
        """Count NOT Koszul algebras."""
        landscape = build_landscape()
        not_koszul = sum(1 for d in landscape.values()
                         if d.koszul_status == KoszulStatus.NOT_KOSZUL)
        # Expected: minimal_model_3_4 = 1
        assert not_koszul == 1


# ============================================================================
# Section 3: PBW criterion verification
# ============================================================================

class TestPBWCriterionVerification:
    """Test the verify_pbw_criterion function."""

    def test_heisenberg_passes(self):
        result = verify_pbw_criterion(heisenberg())
        assert result["koszul_verdict"] == "proved"
        assert result["strongly_generated"] is True
        assert result["pbw_filtration"] is True
        assert result["pbw_collapse"] is True
        assert result["bar_concentrated"] is True
        assert len(result["corrections"]) == 0

    def test_minimal_model_fails(self):
        result = verify_pbw_criterion(minimal_model(3, 4))
        assert result["koszul_verdict"] == "not_koszul"
        assert result["pbw_filtration"] is False

    def test_full_landscape_verification(self):
        results = verify_landscape()
        assert len(results) == 15
        for name, result in results.items():
            assert "koszul_verdict" in result
            assert "corrections" in result


# ============================================================================
# Section 4: Cross-family consistency checks (AP10)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks that catch hardcoded errors."""

    def test_kappa_additivity(self):
        """kappa is additive under tensor products."""
        findings = check_kappa_additivity()
        assert len(findings) == 0, f"kappa additivity failures: {findings}"

    def test_complementarity_consistency(self):
        """kappa + kappa' = 0 for KM, = 13 for Virasoro (AP24)."""
        findings = check_complementarity_consistency()
        assert len(findings) == 0, (
            f"Complementarity failures: {findings}"
        )

    def test_shadow_depth_koszulness_independence(self):
        """Shadow depth does NOT determine Koszulness (AP14).

        All four shadow classes (G, L, C, M) must have Koszul members.
        """
        findings = check_shadow_depth_koszulness_independence()
        assert len(findings) == 0, (
            f"Shadow-depth independence failures: {findings}"
        )


# ============================================================================
# Section 5: Kac-Shapovalov tools
# ============================================================================

class TestKacShapovalov:
    """Test the Kac-Shapovalov null vector weight computation."""

    def test_null_weight_k0(self):
        """k=0 (p=2, q=1): h_null = 1."""
        assert kac_determinant_sl2_null_weight(2, 1) == 1

    def test_null_weight_k1(self):
        """k=1 (p=3, q=1): h_null = 2."""
        assert kac_determinant_sl2_null_weight(3, 1) == 2

    def test_null_weight_k2(self):
        """k=2 (p=4, q=1): h_null = 3."""
        assert kac_determinant_sl2_null_weight(4, 1) == 3

    def test_null_weight_half_integer(self):
        """k=-1/2 (p=3, q=2): h_null = 4."""
        assert kac_determinant_sl2_null_weight(3, 2) == 4

    def test_null_weight_minus_four_thirds(self):
        """k=-4/3 (p=2, q=3): h_null = 3."""
        assert kac_determinant_sl2_null_weight(2, 3) == 3

    def test_null_in_bar_range_k0(self):
        """k=0: h_null = 1 < 2: NOT in bar range."""
        assert null_in_bar_range_sl2(2, 1) is False

    def test_null_in_bar_range_k1(self):
        """k=1: h_null = 2 >= 2: IN bar range."""
        assert null_in_bar_range_sl2(3, 1) is True

    def test_null_in_bar_range_k2(self):
        """k=2: h_null = 3 >= 2: IN bar range."""
        assert null_in_bar_range_sl2(4, 1) is True

    def test_invalid_inputs(self):
        with pytest.raises(ValueError):
            kac_determinant_sl2_null_weight(1, 1)  # p < 2
        with pytest.raises(ValueError):
            kac_determinant_sl2_null_weight(4, 2)  # gcd != 1


# ============================================================================
# Section 6: Corrections to user's initial claims
# ============================================================================

class TestCorrections:
    """Verify corrections to the user's initial 15-algebra claims.

    The user's initial list had several errors that the PBW criterion
    analysis corrects.
    """

    def test_correction_1_heisenberg_correct(self):
        """User: 'Koszul (single generator, quadratic bar)'. CORRECT."""
        data = heisenberg()
        assert data.is_koszul is True

    def test_correction_2_sl2_generic_correct(self):
        """User: 'Koszul (PBW universality)'. CORRECT."""
        data = affine_sl2_universal()
        assert data.is_koszul is True

    def test_correction_3_sl2_critical_user_correct(self):
        """User: 'Koszul (center is commutative, still Koszul)'. CORRECT.

        But note: the reason is free strong generation of the UNIVERSAL
        algebra, not that the center is commutative.
        """
        data = affine_sl2_critical()
        assert data.is_koszul is True

    def test_correction_4_sl2_integrable_user_WRONG(self):
        """User: 'Koszul (simple quotient of Koszul algebra — check!)'.
        WRONG.

        Being a quotient of a Koszul algebra does NOT imply Koszulness.
        The null vector at h=2 blocks PBW. Status: OPEN.
        """
        data = affine_sl2_integrable_k1()
        assert data.koszul_status == KoszulStatus.OPEN
        assert data.is_koszul is False

    def test_correction_5_virasoro_correct(self):
        """User: 'Koszul (PBW universality)'. CORRECT."""
        data = virasoro_generic()
        assert data.is_koszul is True

    def test_correction_6_virasoro_c0_correct(self):
        """User: 'Koszul (still strongly generated)'. CORRECT."""
        data = virasoro_c0()
        assert data.is_koszul is True

    def test_correction_7_minimal_model_correct(self):
        """User: 'NOT Koszul (null vectors break PBW)'. CORRECT
        for Ising and Yang-Lee (null in bar range)."""
        ising = minimal_model(3, 4)
        assert ising.koszul_status == KoszulStatus.NOT_KOSZUL

    def test_correction_8_w3_correct(self):
        """User: 'Koszul (PBW universality for UNIVERSAL W_3)'. CORRECT."""
        data = w3_universal()
        assert data.is_koszul is True

    def test_correction_9_betagamma_correct(self):
        """User: 'Koszul'. CORRECT."""
        data = betagamma_lambda1()
        assert data.is_koszul is True

    def test_correction_10_free_fermion_correct(self):
        """User: 'Koszul'. CORRECT."""
        data = free_fermion()
        assert data.is_koszul is True

    def test_correction_11_d4_lattice_correct(self):
        """User: 'Koszul (lattice VOAs are Koszul by PBW)'. MOSTLY CORRECT.

        Koszulness is correct, but the proof mechanism is the lattice
        filtration (thm:lattice:koszul-morphism), not PBW universality.
        """
        data = d4_lattice()
        assert data.is_koszul is True
        assert data.proof_mechanism == ProofMechanism.LATTICE_FILTRATION

    def test_correction_12_symplectic_fermion_user_WRONG(self):
        """User: 'NOT Koszul? (logarithmic VOA)'. WRONG.

        The symplectic fermion IS Koszul. Logarithmic phenomena
        appear in the module category, not in the bar complex.
        """
        data = symplectic_fermion()
        assert data.is_koszul is True
        assert data.koszul_status == KoszulStatus.PROVED

    def test_correction_13_triplet_user_partially_wrong(self):
        """User: 'NOT Koszul (logarithmic)'. PARTIALLY WRONG.

        The correct status is OPEN, not NOT Koszul.
        Logarithmic module structure does not by itself determine
        bar concentration of the algebra.
        """
        data = triplet_w2()
        assert data.koszul_status == KoszulStatus.OPEN

    def test_correction_14_admissible_correct(self):
        """User: 'Koszul for UNIVERSAL, OPEN for SIMPLE quotient'. CORRECT."""
        u = admissible_sl2(3, 2)
        s = admissible_sl2_simple(3, 2)
        assert u.is_koszul is True
        assert s.koszul_status == KoszulStatus.OPEN

    def test_correction_15_w_1_plus_infinity_nuanced(self):
        """User: 'Koszul (PBW universality for infinite generators)'.
        PARTIALLY CORRECT but mechanism is wrong.

        Koszulness is correct, but requires MC4 completion tower
        (thm:completed-bar-cobar-strong), not plain PBW universality,
        because there are infinitely many generators.
        """
        data = w_1_plus_infinity()
        assert data.is_koszul is True
        assert data.proof_mechanism == ProofMechanism.COMPLETION_TOWER


# ============================================================================
# Section 7: Summary and full run
# ============================================================================

class TestFullRun:
    """Run the complete verification suite."""

    def test_run_all_checks(self):
        results = run_all_checks()
        assert "landscape" in results
        assert "kappa_additivity" in results
        assert "complementarity" in results
        assert "depth_independence" in results

        # No failures in cross-checks
        assert len(results["kappa_additivity"]) == 0
        assert len(results["complementarity"]) == 0
        assert len(results["depth_independence"]) == 0

    def test_summary_table(self):
        """Print a summary table of the 15-algebra landscape."""
        landscape = build_landscape()
        proved = [n for n, d in landscape.items() if d.is_koszul]
        open_ = [n for n, d in landscape.items()
                 if d.koszul_status == KoszulStatus.OPEN]
        not_k = [n for n, d in landscape.items()
                 if d.koszul_status == KoszulStatus.NOT_KOSZUL]

        assert len(proved) + len(open_) + len(not_k) == 15
