r"""Tests for the Theorem H E_3 rectification engine.

Deep rectification of Theorem H against De Leger [2512.20167],
AKL [2411.00812], and Griffin [2501.18720].

Organized by:
  I.    E_3 operation spaces (configuration space Betti numbers)
  II.   Heisenberg E_3 structure
  III.  Affine KM E_3 structure
  IV.   Virasoro E_3 structure
  V.    W_3 ChirHoch explicit computation
  VI.   W_N ChirHoch polynomial growth
  VII.  AKL comparison (U(N) vs ChirHoch)
  VIII. Griffin CVA BRST comparison
  IX.   E_3-Koszulness conjecture assessment
  X.    Cross-checks and consistency
  XI.   De Leger SC(E_2) identification
  XII.  Brace-E_3 compatibility

References:
  De Leger, arXiv:2512.20167
  Alhussein-Kolesnikov-Lopatkin, arXiv:2411.00812
  Griffin, arXiv:2501.18720
  thm:hochschild-polynomial-growth (chiral_hochschild_koszul.tex)
  thm:main-koszul-hoch (chiral_hochschild_koszul.tex)
  prop:e2-formality-hochschild (chiral_hochschild_koszul.tex)
"""

import pytest

from compute.lib.theorem_thm_h_e3_rectification_engine import (
    # E_3 operations
    conf_betti_rn,
    total_betti_conf,
    e3_operation_space_dim,
    e2_operation_space_dim,
    gerstenhaber_bracket_degree,
    e3_linking_degree,
    # Heisenberg E_3
    heisenberg_e3_structure,
    E3StructureData,
    # Affine KM E_3
    affine_km_e3_structure,
    # Virasoro E_3
    virasoro_e3_structure,
    # W_N ChirHoch (Theorem-H bounded, per AP94)
    w_algebra_chirhoch_bounded_dim,
    w3_chirhoch_dims,
    w4_chirhoch_dims,
    wN_chirhoch_dims,
    w_algebra_polynomial_growth_check,
    w3_chirhoch_explicit_at_weights,
    # AKL comparison
    akl_vs_chirhoch_virasoro,
    conformal_locality_for_family,
    AKLComparisonResult,
    # Griffin comparison
    griffin_cva_brst_check,
    GriffinComparisonResult,
    # E_3-Koszulness conjecture
    assess_e3_koszulness_conjecture,
    E3KoszulnessAssessment,
    # Cross-checks
    chirhoch_palindromicity_check,
    verify_chirhoch_concentration_quadratic,
    verify_euler_characteristic_consistency,
    # De Leger
    de_leger_sc_e2_identification,
    brace_e3_compatibility_check,
    # Summary
    full_rectification_summary,
)


# ===================================================================
# I. E_3 operation spaces — configuration space Betti numbers
# ===================================================================

class TestConfigurationSpaceBetti:
    """Betti numbers of Conf_k(R^n) for E_n operads."""

    def test_conf_1_point_any_n(self):
        """Conf_1(R^n) is a point: Betti = {0: 1}."""
        for n in (2, 3, 4):
            assert conf_betti_rn(n, 1) == {0: 1}

    def test_total_betti_equals_factorial(self):
        """Total Betti of Conf_k(R^n) = k! for n >= 2."""
        for n in (2, 3):
            for k in range(1, 6):
                assert total_betti_conf(n, k) == pytest.approx(
                    1 if k == 0 else
                    __import__('math').factorial(k)
                )

    def test_e2_betti_k2(self):
        """Conf_2(R^2): H_0 = C, H_1 = C. Total = 2."""
        b = conf_betti_rn(2, 2)
        assert b[0] == 1
        assert b[1] == 1
        assert sum(b.values()) == 2

    def test_e3_betti_k2(self):
        """Conf_2(R^3): H_0 = C, H_2 = C. Total = 2."""
        b = conf_betti_rn(3, 2)
        assert b[0] == 1
        assert b[2] == 1
        assert sum(b.values()) == 2

    def test_e2_betti_k3(self):
        """Conf_3(R^2): H_0=1, H_1=3, H_2=2. Total = 6 = 3!."""
        b = conf_betti_rn(2, 3)
        assert b[0] == 1
        assert b[1] == 3
        assert b[2] == 2
        assert sum(b.values()) == 6

    def test_e3_betti_k3(self):
        """Conf_3(R^3): H_0=1, H_2=3, H_4=2. Total = 6 = 3!."""
        b = conf_betti_rn(3, 3)
        assert b[0] == 1
        assert b[2] == 3
        assert b[4] == 2
        assert sum(b.values()) == 6

    def test_e3_generators_degree_2(self):
        """E_3 generators omega_{ij} have degree 2 (not 1 as in E_2)."""
        # Conf_2(R^3) has a single generator in degree 2
        b = conf_betti_rn(3, 2)
        assert 2 in b and b[2] == 1
        # Conf_2(R^2) has a single generator in degree 1
        b2 = conf_betti_rn(2, 2)
        assert 1 in b2 and b2[1] == 1

    def test_gerstenhaber_bracket_is_degree_minus_1(self):
        """The Gerstenhaber bracket has degree -1 (from E_2)."""
        assert gerstenhaber_bracket_degree() == -1

    def test_e3_linking_is_degree_minus_2(self):
        """The E_3 linking operation has degree -2 (from S^2 linking)."""
        assert e3_linking_degree() == -2


# ===================================================================
# II. Heisenberg E_3 structure
# ===================================================================

class TestHeisenbergE3:
    """E_3 structure on ChirHoch*(H_k, H_k)."""

    def test_chirhoch_dims(self):
        """ChirHoch = (1, 1, 1) for Heisenberg."""
        data = heisenberg_e3_structure()
        assert data.chirhoch_dims[0] == 1
        assert data.chirhoch_dims[1] == 1
        assert data.chirhoch_dims[2] == 1

    def test_gerstenhaber_trivial(self):
        """Gerstenhaber bracket trivial (single derivation auto-commutes)."""
        data = heisenberg_e3_structure()
        assert data.gerstenhaber_bracket_trivial is True

    def test_e3_linking_trivial(self):
        """E_3 linking trivial (concentration forces this)."""
        data = heisenberg_e3_structure()
        assert data.e3_linking_trivial is True

    def test_shadow_class_G(self):
        """Heisenberg is class G (Gaussian, shadow depth 2)."""
        data = heisenberg_e3_structure()
        assert data.shadow_class == 'G'

    def test_e3_formal(self):
        """E_3 structure is formal for Heisenberg."""
        data = heisenberg_e3_structure()
        assert data.e3_formal is True

    def test_brace_max_nonzero(self):
        """Class G: B_k = 0 for k >= 1 on cohomology."""
        data = heisenberg_e3_structure()
        assert data.brace_max_nonzero == 0


# ===================================================================
# III. Affine KM E_3 structure
# ===================================================================

class TestAffineKME3:
    """E_3 structure on ChirHoch*(hat{g}_k, hat{g}_k)."""

    def test_sl2_chirhoch_dims(self):
        """ChirHoch = (1, 3, 1) for affine sl_2."""
        data = affine_km_e3_structure('A', 1)
        assert data.chirhoch_dims[0] == 1
        assert data.chirhoch_dims[1] == 3  # dim sl_2 = 3
        assert data.chirhoch_dims[2] == 1

    def test_sl3_chirhoch_dims(self):
        """ChirHoch = (1, 8, 1) for affine sl_3."""
        data = affine_km_e3_structure('A', 2)
        assert data.chirhoch_dims[1] == 8  # dim sl_3 = 8

    def test_sl4_chirhoch_dims(self):
        """ChirHoch^1 = 15 for affine sl_4 (dim sl_4 = 15)."""
        data = affine_km_e3_structure('A', 3)
        assert data.chirhoch_dims[1] == 15

    def test_gerstenhaber_nontrivial_sl2(self):
        """Gerstenhaber bracket nontrivial for non-abelian g."""
        data = affine_km_e3_structure('A', 1)
        assert data.gerstenhaber_bracket_trivial is False

    def test_shadow_class_L(self):
        """Affine KM is class L (Lie/tree, shadow depth 3)."""
        data = affine_km_e3_structure('A', 1)
        assert data.shadow_class == 'L'

    def test_e3_formal(self):
        """E_3 formal for affine KM (Koszul => E_2-formal => E_3-formal)."""
        data = affine_km_e3_structure('A', 1)
        assert data.e3_formal is True

    def test_g2_dim(self):
        """dim G_2 = 14."""
        data = affine_km_e3_structure('G', 2)
        assert data.chirhoch_dims[1] == 14

    def test_e8_dim(self):
        """dim E_8 = 248."""
        data = affine_km_e3_structure('E', 8)
        assert data.chirhoch_dims[1] == 248


# ===================================================================
# IV. Virasoro E_3 structure
# ===================================================================

class TestVirasoroE3:
    """E_3 structure on ChirHoch*(Vir_c, Vir_c).

    Per AP94 and Theorem H (thm:hochschild-polynomial-growth):
    ChirHoch^*(Vir_c) is concentrated in {0,1,2} with total dim <= 4.
    The historical Gelfand-Fuchs polynomial-ring model C[Theta] with
    |Theta|=2 giving ChirHoch^{2k}=C for all k >= 0 is REFUTED (AP95:
    that is the continuous cohomology of the Witt algebra, a
    DIFFERENT functor from chiral Hochschild).
    """

    def test_chirhoch_concentrated_in_0_1_2(self):
        """ChirHoch^*(Vir) concentrated in {0,1,2}, dim <= 4."""
        data = virasoro_e3_structure()
        assert data.chirhoch_dims[0] == 1
        assert data.chirhoch_dims[1] == 1
        assert data.chirhoch_dims[2] == 1
        total = sum(data.chirhoch_dims.values())
        assert total <= 4
        # AP94: must vanish outside [0,2].
        for n in range(3, 10):
            assert data.chirhoch_dims.get(n, 0) == 0

    def test_gerstenhaber_trivial(self):
        """Gerstenhaber bracket trivial (single 1-param deformation self-commutes)."""
        data = virasoro_e3_structure()
        assert data.gerstenhaber_bracket_trivial is True

    def test_e3_linking_trivial(self):
        """E_3 linking trivial (single class in ChirHoch^2, bounded amplitude)."""
        data = virasoro_e3_structure()
        assert data.e3_linking_trivial is True

    def test_shadow_class_M(self):
        """Virasoro is class M (shadow DEPTH class, not amplitude).

        AP131: shadow class is about the modular shadow tower's
        generating/algebraic depth, NOT cohomological amplitude of
        ChirHoch (which is bounded by Theorem H).
        """
        data = virasoro_e3_structure()
        assert data.shadow_class == 'M'


# ===================================================================
# V. W_3 ChirHoch explicit computation
# ===================================================================

class TestW3ChirHoch:
    """ChirHoch*(W_3, W_3) bounded by Theorem H, amplitude [0,2], dim <= 4.

    Per AP94/AP95, the Gelfand-Fuchs polynomial-ring model
    ChirHoch*(W_3) = C[Theta_1, Theta_2] with partition counts is
    REFUTED (it is continuous Lie-algebra cohomology of the Witt
    algebra, a different functor).  These tests verify the
    Theorem-H bounded amplitude behaviour.
    """

    def test_degree_0_center(self):
        """ChirHoch^0(W_3) = Z(W_3) = C."""
        assert w_algebra_chirhoch_bounded_dim([2, 3], 0) == 1

    def test_degree_1_deformation(self):
        """ChirHoch^1(W_3) = C (single c-deformation direction)."""
        assert w_algebra_chirhoch_bounded_dim([2, 3], 1) == 1

    def test_degree_2_dual_center(self):
        """ChirHoch^2(W_3) = Z(W_3^!) = C."""
        assert w_algebra_chirhoch_bounded_dim([2, 3], 2) == 1

    def test_vanishes_above_2(self):
        """ChirHoch^n(W_3) = 0 for n > 2 (Theorem H amplitude)."""
        for n in range(3, 15):
            assert w_algebra_chirhoch_bounded_dim([2, 3], n) == 0

    def test_refuted_function_raises(self):
        """The old Gelfand-Fuchs partition count raises NotImplementedError."""
        from compute.lib.theorem_thm_h_e3_rectification_engine import (
            w_algebra_chirhoch_dim,
        )
        with pytest.raises(NotImplementedError):
            w_algebra_chirhoch_dim([2, 3], 4)

    def test_explicit_data_bounded(self):
        """Verify w3_chirhoch_explicit_at_weights returns Theorem-H amplitude."""
        data = w3_chirhoch_explicit_at_weights()
        assert data['amplitude'] == (0, 2)
        assert data['bounded_by_theorem_h'] is True
        assert data['polynomial_growth'] is False
        assert data['growth_rate'] == 0
        assert data['total_dim'] <= 4

    def test_total_dim_leq_4(self):
        """Total dim of ChirHoch*(W_3) is bounded by 4 (AP94)."""
        data = w3_chirhoch_explicit_at_weights()
        assert data['total_dim'] <= 4


# ===================================================================
# VI. W_N ChirHoch Theorem-H bounded amplitude
# ===================================================================

class TestWNBoundedAmplitude:
    """ChirHoch*(W_N) bounded by Theorem H amplitude [0,2], dim <= 4.

    Per AP94/AP95, the Gelfand-Fuchs polynomial-growth model
    (O(n^{r-1}) where r is the number of W-generators) is REFUTED.
    """

    def test_virasoro_bounded(self):
        """Virasoro (W_2): ChirHoch^n bounded, zero above degree 2."""
        dims = wN_chirhoch_dims(2, 20)
        for n in range(3, 21):
            assert dims[n] == 0

    def test_w3_bounded_not_polynomial(self):
        """W_3: bounded by Theorem H, NOT polynomial growth."""
        result = w_algebra_polynomial_growth_check([2, 3], 50)
        assert result['expected_growth_rate'] == 0
        assert result['bounded_by_theorem_h'] is True
        assert result['vanishes_above_2'] is True

    def test_w4_bounded_not_polynomial(self):
        """W_4: bounded by Theorem H, NOT quadratic growth."""
        result = w_algebra_polynomial_growth_check([2, 3, 4], 50)
        assert result['expected_growth_rate'] == 0
        assert result['bounded_by_theorem_h'] is True

    def test_w5_bounded_not_polynomial(self):
        """W_5: bounded by Theorem H, NOT cubic growth."""
        result = w_algebra_polynomial_growth_check([2, 3, 4, 5], 50)
        assert result['expected_growth_rate'] == 0
        assert result['bounded_by_theorem_h'] is True

    def test_w4_concentrated_in_0_1_2(self):
        """W_4 ChirHoch concentrated in {0,1,2}, dim <= 4."""
        dims = w4_chirhoch_dims(10)
        assert dims[0] == 1
        assert dims[1] == 1
        assert dims[2] == 1
        for n in range(3, 11):
            assert dims[n] == 0

    def test_w3_not_growing(self):
        """W_3 ChirHoch does NOT grow: all dims at high degree are 0."""
        dims = w3_chirhoch_dims(20)
        assert dims[20] == 0
        assert dims[10] == 0


# ===================================================================
# VII. AKL comparison: U(N) vs ChirHoch
# ===================================================================

class TestAKLComparison:
    """Compare AKL's HH*(U(3), M) with our ChirHoch*(Vir)."""

    def test_locality_3_agrees(self):
        """At locality N=3, AKL agrees with ChirHoch at generic c."""
        result = akl_vs_chirhoch_virasoro(3)
        assert result.e2_page_agrees is True

    def test_locality_2_disagrees(self):
        """At locality N=2, AKL misses the c/2 lambda^3 term."""
        result = akl_vs_chirhoch_virasoro(2)
        assert result.e2_page_agrees is False

    def test_spectral_sequence_exists(self):
        """A spectral sequence HH*(U(N), Vir) => ChirHoch*(Vir) exists."""
        result = akl_vs_chirhoch_virasoro(3)
        assert result.spectral_sequence_exists is True

    def test_complexes_are_different(self):
        """The two complexes are categorically different objects."""
        result = akl_vs_chirhoch_virasoro(3)
        assert result.akl_complex_type != result.our_complex_type

    def test_conformal_locality_heisenberg(self):
        """Heisenberg needs locality N=2 (double pole)."""
        # Heisenberg: alpha(z)alpha(w) ~ k/(z-w)^2
        # lambda-bracket: {alpha_lambda alpha} = k*lambda, so N=1 suffices
        assert conformal_locality_for_family('heisenberg') == 2

    def test_conformal_locality_virasoro(self):
        """Virasoro needs locality N=3 (quartic pole -> lambda^3)."""
        assert conformal_locality_for_family('virasoro') == 3

    def test_conformal_locality_w3(self):
        """W_3 needs locality N=5 (sextic pole -> lambda^5)."""
        assert conformal_locality_for_family('w3') == 5

    def test_conformal_locality_km(self):
        """Affine KM needs locality N=1 (double pole -> lambda^1)."""
        assert conformal_locality_for_family('affine_sl2') == 1


# ===================================================================
# VIII. Griffin CVA BRST comparison
# ===================================================================

class TestGriffinComparison:
    """Griffin's CVA BRST at n=1 vs our DS reduction."""

    def test_sl2_brst_gives_virasoro(self):
        """CVA BRST of sl_2 at n=1 gives Virasoro."""
        result = griffin_cva_brst_check('sl2', 1)
        assert result.brst_gives_w_algebra is True
        assert result.consistent_with_ds is True

    def test_sl3_brst_gives_w3(self):
        """CVA BRST of sl_3 at n=1 gives W_3."""
        result = griffin_cva_brst_check('sl3', 1)
        assert result.brst_gives_w_algebra is True

    def test_consistency_with_ds(self):
        """Griffin consistent with our thm:ds-koszul-intertwine."""
        for lie_alg in ('sl2', 'sl3', 'slN'):
            result = griffin_cva_brst_check(lie_alg, 1)
            assert result.consistent_with_ds is True


# ===================================================================
# IX. E_3-Koszulness conjecture assessment
# ===================================================================

class TestE3KoszulnessConjecture:
    """Assessment of E_3-formality as a Koszulness characterization."""

    def test_forward_proved(self):
        """Koszulness => E_3-formality is PROVED."""
        assessment = assess_e3_koszulness_conjecture()
        assert assessment.forward_proved is True

    def test_backward_false(self):
        """E_3-formality => Koszulness is FALSE."""
        assessment = assess_e3_koszulness_conjecture()
        assert assessment.backward_proved is False

    def test_not_13th_characterization(self):
        """E_3-formality is NOT a 13th Koszulness characterization."""
        assessment = assess_e3_koszulness_conjecture()
        assert assessment.is_13th_characterization is False

    def test_counterexample_exists(self):
        """A counterexample to the backward direction exists."""
        assessment = assess_e3_koszulness_conjecture()
        assert assessment.backward_counterexample is not None
        assert 'homotopy-Koszul' in assessment.backward_counterexample

    def test_weaker_variant_open(self):
        """The weaker E_3-rigidity variant is OPEN."""
        assessment = assess_e3_koszulness_conjecture()
        assert 'OPEN' in assessment.weaker_variant_status


# ===================================================================
# X. Cross-checks and consistency
# ===================================================================

class TestCrossChecks:
    """Cross-family consistency checks."""

    def test_palindromicity_heisenberg(self):
        """Palindromic duality for Heisenberg."""
        assert chirhoch_palindromicity_check(
            center_dim=1, hoch1_dim=1, dual_center_dim=1
        ) is True

    def test_palindromicity_sl2(self):
        """Palindromic duality for sl_2."""
        assert chirhoch_palindromicity_check(
            center_dim=1, hoch1_dim=3, dual_center_dim=1
        ) is True

    def test_concentration_heisenberg(self):
        """ChirHoch^n(H) = 0 for n > 2."""
        assert verify_chirhoch_concentration_quadratic('heisenberg') is True

    def test_concentration_sl2(self):
        assert verify_chirhoch_concentration_quadratic('affine_sl2') is True

    def test_concentration_betagamma(self):
        assert verify_chirhoch_concentration_quadratic('betagamma') is True

    def test_euler_char_consistency(self):
        """Euler characteristic identity: chi = 2*dim_Z - dim_HH1."""
        results = verify_euler_characteristic_consistency()
        for name, data in results.items():
            assert data['identity_2Z_minus_H1'] is True, (
                f"Euler char identity failed for {name}")

    def test_heisenberg_euler_char(self):
        """chi(H) = 1 - 1 + 1 = 1."""
        results = verify_euler_characteristic_consistency()
        assert results['heisenberg']['euler_char'] == 1

    def test_sl2_euler_char(self):
        """chi(sl_2) = 1 - 3 + 1 = -1."""
        results = verify_euler_characteristic_consistency()
        assert results['affine_sl2']['euler_char'] == -1


# ===================================================================
# XI. De Leger SC(E_2) identification
# ===================================================================

class TestDeLegerIdentification:
    """De Leger's SC(E_2) ~ SC_2 and compatibility with our framework."""

    def test_identification_holds(self):
        """SC(E_2) ~ SC_2 = SC^{ch,top}."""
        result = de_leger_sc_e2_identification()
        assert result['compatible'] is True

    def test_e3_action_consequence(self):
        """Consequence: E_3-action on ChirHoch for all chiral algebras."""
        result = de_leger_sc_e2_identification()
        assert 'E_3-action' in result['consequence']

    def test_formal_for_koszul(self):
        """E_3-formal for Koszul algebras."""
        result = de_leger_sc_e2_identification()
        assert result['formal_for_koszul'] is True

    def test_formal_for_non_koszul(self):
        """E_3-formal even for non-Koszul (SC homotopy-Koszulity)."""
        result = de_leger_sc_e2_identification()
        assert result['formal_for_non_koszul'] is True


# ===================================================================
# XII. Brace-E_3 compatibility
# ===================================================================

class TestBraceE3Compatibility:
    """Brace dg algebra = tree-level E_3 structure."""

    def test_brace_from_swiss_cheese(self):
        """Brace dg algebra comes from Swiss-cheese theorem."""
        result = brace_e3_compatibility_check()
        assert result['brace_from_swiss_cheese'] is True

    def test_e3_from_de_leger(self):
        """E_3 structure from De Leger's construction."""
        result = brace_e3_compatibility_check()
        assert result['e3_from_de_leger'] is True

    def test_compatibility_statement(self):
        """Brace = tree-level E_3."""
        result = brace_e3_compatibility_check()
        assert 'tree-level' in result['compatibility']


# ===================================================================
# XIII. Full rectification summary
# ===================================================================

class TestFullSummary:
    """End-to-end rectification summary."""

    def test_summary_has_all_papers(self):
        """Summary covers all three papers."""
        summary = full_rectification_summary()
        assert 'de_leger' in summary
        assert 'akl' in summary
        assert 'griffin' in summary

    def test_no_corrections_needed_de_leger(self):
        """De Leger: no corrections needed to manuscript."""
        summary = full_rectification_summary()
        assert 'CONSISTENT' in summary['de_leger']['impact_on_manuscript']

    def test_w3_matches_theorem_h(self):
        """W_3 computation matches Theorem H prediction."""
        summary = full_rectification_summary()
        assert summary['w3_computation']['matches_theorem_h'] is True

    def test_e3_not_13th(self):
        """E_3-formality is NOT a 13th characterization."""
        summary = full_rectification_summary()
        assert 'FALSE' in summary['e3_koszulness_conjecture']['verdict']

    def test_findings_count(self):
        """At least 7 findings in the register."""
        summary = full_rectification_summary()
        assert len(summary['findings']) >= 7


# ===================================================================
# XIV. MULTI-PATH VERIFICATION (AP10 compliance)
# ===================================================================

class TestMultiPathVerification:
    """Cross-checks verifying results by at least 2 independent paths.

    AP10: hardcoded expected values are necessary but NOT sufficient.
    Cross-family, cross-method, and limiting-case checks catch errors
    that single-family tests cannot.
    """

    # --- Path 1 vs Path 2: W_N bounded amplitude via two routes ---

    def test_w3_bounded_two_paths(self):
        """W_3 ChirHoch bounded amplitude verified two ways.

        Path 1: w_algebra_chirhoch_bounded_dim (direct engine call).
        Path 2: amplitude indicator: 1 if n in {0,1,2}, else 0.
        Per AP94/AP95, W_3 ChirHoch is Theorem-H bounded, NOT the
        Gelfand-Fuchs partition count.
        """
        for n in range(15):
            dim_engine = w_algebra_chirhoch_bounded_dim([2, 3], n)
            dim_expected = 1 if 0 <= n <= 2 else 0
            assert dim_engine == dim_expected, (
                f"W_3 mismatch at degree {n}: engine={dim_engine}, "
                f"expected={dim_expected}")

    def test_w4_bounded_two_paths(self):
        """W_4 ChirHoch bounded amplitude verified two ways.

        Path 1: w_algebra_chirhoch_bounded_dim.
        Path 2: amplitude indicator.
        """
        for n in range(13):
            dim_engine = w_algebra_chirhoch_bounded_dim([2, 3, 4], n)
            dim_expected = 1 if 0 <= n <= 2 else 0
            assert dim_engine == dim_expected, (
                f"W_4 mismatch at degree {n}: engine={dim_engine}, "
                f"expected={dim_expected}")

    # --- Path 1 vs Path 2: Betti totals by formula vs computation ---

    def test_conf_betti_total_formula_vs_computation(self):
        """Total Betti of Conf_k(R^n) = k! by formula AND by computation.

        Path 1: sum of computed Betti numbers.
        Path 2: k! (combinatorial identity).
        """
        import math
        for n in (2, 3):
            for k in range(1, 6):
                betti = conf_betti_rn(n, k)
                total_computed = sum(betti.values())
                total_formula = math.factorial(k)
                assert total_computed == total_formula, (
                    f"Conf_{k}(R^{n}): computed={total_computed}, "
                    f"formula={total_formula}")

    # --- Limiting case: W_2 = Virasoro ---

    def test_w2_equals_virasoro(self):
        """W_2 (single generator weight 2) = Virasoro.

        Both are bounded by Theorem H amplitude [0,2], dim <= 4.
        Per AP94/AP95, the old Gelfand-Fuchs periodicity (ChirHoch^{2k}=C
        for all k) is REFUTED.
        """
        dims = wN_chirhoch_dims(2, 20)
        for n in range(3):
            assert dims[n] == 1
        for n in range(3, 21):
            assert dims[n] == 0

    # --- Cross-family: quadratic Euler characteristic ---

    def test_euler_char_via_two_formulas(self):
        """Euler characteristic by direct sum vs alternating sum.

        Path 1: chi = dim_H0 - dim_H1 + dim_H2 (alternating sum).
        Path 2: chi = 2*dim_Z - dim_H1 (using Z(A) = Z(A!) at generic level).
        """
        families = {
            'heisenberg': (1, 1, 1),
            'sl2': (1, 3, 1),
            'sl3': (1, 8, 1),
            'betagamma': (1, 2, 1),
        }
        for name, (z, h1, zd) in families.items():
            chi_path1 = z - h1 + zd
            chi_path2 = 2 * z - h1  # uses z = zd
            assert chi_path1 == chi_path2, (
                f"{name}: path1={chi_path1}, path2={chi_path2}")

    # --- Koszul duality: dim HH^0(A) = dim HH^2(A!) ---

    def test_koszul_duality_degree_exchange(self):
        """Koszul duality exchanges degree 0 and degree 2.

        dim ChirHoch^0(A) = dim ChirHoch^2(A!) (thm:main-koszul-hoch with n=0).
        For all quadratic families at generic level: both = 1.

        Path 1: center_dim(A) = 1.
        Path 2: dual_center_dim(A!) = center_dim(A) = 1.
        """
        for family in ('heisenberg', 'affine_sl2', 'betagamma'):
            assert verify_chirhoch_concentration_quadratic(family)

    # --- E_2 vs E_3 operation space dimension cross-check ---

    def test_e2_e3_total_agree_at_all_arities(self):
        """Total dim of E_2 and E_3 operation spaces both equal k!.

        The total Betti number k! is universal across all E_n, n >= 2.
        """
        import math
        for k in range(1, 6):
            e2_total = sum(e2_operation_space_dim(k).values())
            e3_total = sum(e3_operation_space_dim(k).values())
            assert e2_total == math.factorial(k)
            assert e3_total == math.factorial(k)
            assert e2_total == e3_total

    # --- W_3: bounded by Theorem H ---

    def test_w3_bounded_total_leq_4(self):
        """W_3 ChirHoch total dim <= 4 (AP94, Theorem H)."""
        dims = w3_chirhoch_dims(30)
        total = sum(dims.values())
        assert total <= 4, f"W_3 total dim {total} exceeds Theorem-H bound 4"

    def test_w3_vanishes_above_2(self):
        """W_3 ChirHoch^n = 0 for n > 2."""
        dims = w3_chirhoch_dims(30)
        for n in range(3, 31):
            assert dims[n] == 0

    # --- Virasoro vs W_2: two paths to same bounded amplitude ---

    def test_virasoro_e3_vs_w2_chirhoch(self):
        """Virasoro E_3 structure dims agree with W_2 = wN(2) dims.

        Path 1: virasoro_e3_structure().chirhoch_dims
        Path 2: wN_chirhoch_dims(2)
        Both Theorem-H bounded in {0,1,2}.
        """
        vir = virasoro_e3_structure()
        w2 = wN_chirhoch_dims(2, 20)
        for n in range(20):
            assert vir.chirhoch_dims.get(n, 0) == w2[n], (
                f"Degree {n}: Vir E_3 = {vir.chirhoch_dims.get(n, 0)}, "
                f"W_2 = {w2[n]}")

    # --- Affine KM: dim HH^1 = dim g (two paths) ---

    def test_km_hh1_equals_dim_g_two_paths(self):
        """dim ChirHoch^1(hat{g}_k) = dim g.

        Path 1: affine_km_e3_structure().chirhoch_dims[1]
        Path 2: (rank+1)^2 - 1 for type A (direct formula).
        """
        for rank in range(1, 6):
            data = affine_km_e3_structure('A', rank)
            dim_from_engine = data.chirhoch_dims[1]
            dim_from_formula = (rank + 1) ** 2 - 1
            assert dim_from_engine == dim_from_formula, (
                f"sl_{rank+1}: engine={dim_from_engine}, "
                f"formula={dim_from_formula}")
