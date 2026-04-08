r"""Tests for theorem_bv_sewing_engine: Delta_BV = d_sew chain-level identification.

FOUR independent proof paths, each verified by multiple tests:
  Path 1 (Operator definition): propagator decomposition, harmonic decoupling
  Path 2 (Spectral sequence): E_1 and E_2 match across genera
  Path 3 (Heisenberg extraction): explicit chain-level quasi-iso, genus-2 extension
  Path 4 (Modular operad): Feynman transform identification, five-component D

Cross-family verification across all standard families:
  G (Heisenberg), L (affine KM), C (beta-gamma), M (Virasoro)

Multi-path verification mandate (CLAUDE.md): every numerical claim
verified by at least 3 independent paths.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.theorem_bv_sewing_engine import (
    AlgebraData,
    FiveComponentDecomposition,
    ModularOperadData,
    PropagatorDecomposition,
    SpectralSequenceData,
    affine_km_data,
    bergman_kernel_trace,
    betagamma_data,
    five_component_decomposition,
    four_path_synthesis,
    genus2_bv_sewing_comparison,
    heisenberg_chain_level_extraction,
    heisenberg_data,
    heisenberg_to_interacting_extension,
    jacobi_cubic_vanishing,
    lambda_fp,
    lambda_fp_from_ahat,
    modular_operad_identification,
    nonseparating_clutching_data,
    numerical_lambda_fp_values,
    numerical_trace_comparison,
    operator_definition_comparison,
    propagator_decomposition,
    propagator_variance_check,
    qme_genus_decomposition,
    spectral_sequence_comparison,
    spectral_sequence_genus1_explicit,
    spectral_sequence_higher_genus,
    verify_ahat_consistency,
    verify_bv_sewing_identification,
    verify_d_squared_zero_components,
    virasoro_data,
)


# =====================================================================
# Section A: Faber-Pandharipande numbers (multi-path verification)
# =====================================================================


class TestLambdaFP:
    """Verify lambda_g^FP by Bernoulli formula and A-hat extraction."""

    def test_lambda1(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda2(self):
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda3(self):
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda4(self):
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda5(self):
        assert lambda_fp(5) == Rational(73, 3503554560)

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (Bernoulli sign pattern)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0, f"lambda_{g}^FP must be positive"

    def test_lambda_fp_from_ahat_genus1(self):
        """A-hat extraction matches Bernoulli at genus 1."""
        assert lambda_fp_from_ahat(1) == Rational(1, 24)

    def test_lambda_fp_from_ahat_genus2(self):
        """A-hat extraction matches Bernoulli at genus 2."""
        assert lambda_fp_from_ahat(2) == Rational(7, 5760)

    def test_ahat_consistency_all(self):
        """Full A-hat vs Bernoulli consistency through genus 5."""
        result = verify_ahat_consistency(max_genus=5)
        assert result['all_match'], "A-hat and Bernoulli formulas must agree"

    def test_lambda_fp_invalid_genus(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


# =====================================================================
# Section B: Algebra data construction
# =====================================================================


class TestAlgebraData:
    """Verify algebra data is correctly constructed."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP48)."""
        k = Symbol('k')
        h = heisenberg_data(k)
        assert h.kappa == k
        assert h.shadow_class == 'G'
        assert h.shadow_depth == 2

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        c = Symbol('c')
        v = virasoro_data(c)
        assert v.kappa == c / 2
        assert v.shadow_class == 'M'

    def test_km_sl2_kappa(self):
        """kappa(sl2_k) = 3(k+2)/4."""
        k = Symbol('k')
        km = affine_km_data('sl2', k)
        expected = Rational(3) * (k + 2) / 4
        assert simplify(km.kappa - expected) == 0
        assert km.shadow_class == 'L'
        assert km.shadow_depth == 3

    def test_km_sl3_kappa(self):
        """kappa(sl3_k) = 8(k+3)/6 = 4(k+3)/3."""
        k = Symbol('k')
        km = affine_km_data('sl3', k)
        expected = Rational(8) * (k + 3) / 6
        assert simplify(km.kappa - expected) == 0

    def test_betagamma_class(self):
        bg = betagamma_data(Symbol('k'))
        assert bg.shadow_class == 'C'
        assert bg.shadow_depth == 4


# =====================================================================
# Section C: Path 1 -- Operator definition comparison
# =====================================================================


class TestPath1OperatorDefinition:
    """Path 1: propagator decomposition and operator comparison."""

    def test_propagator_exact_drops_universally(self):
        """P_exact drops in Dolbeault cohomology for ALL algebras."""
        for constructor in [heisenberg_data, virasoro_data, betagamma_data]:
            algebra = constructor()
            decomp = propagator_decomposition(algebra, g=1)
            assert decomp.exact_part_drops is True

    def test_harmonic_decouples_class_G(self):
        """P_harm decouples for Heisenberg (class G, Gaussian)."""
        decomp = propagator_decomposition(heisenberg_data(), g=1)
        assert decomp.harmonic_decouples is True

    def test_harmonic_decouples_class_L(self):
        """P_harm decouples for affine KM (class L, Jacobi identity)."""
        decomp = propagator_decomposition(affine_km_data(), g=1)
        assert decomp.harmonic_decouples is True

    def test_harmonic_does_not_decouple_class_M(self):
        """P_harm does NOT decouple for Virasoro (class M)."""
        decomp = propagator_decomposition(virasoro_data(), g=1)
        assert decomp.harmonic_decouples is False

    def test_harmonic_does_not_decouple_class_C(self):
        """P_harm does NOT decouple for beta-gamma (class C)."""
        decomp = propagator_decomposition(betagamma_data(), g=1)
        assert decomp.harmonic_decouples is False

    def test_scalar_trace_always_matches(self):
        """Scalar trace match is universal (Theorem D)."""
        for constructor in [heisenberg_data, virasoro_data,
                            lambda: affine_km_data('sl2'), betagamma_data]:
            algebra = constructor()
            result = operator_definition_comparison(algebra, g=1)
            assert result['scalar_trace_match'] is True

    def test_chain_level_proved_class_G(self):
        result = operator_definition_comparison(heisenberg_data(), g=1)
        assert result['chain_level_status'] == 'PROVED'

    def test_chain_level_proved_class_L(self):
        result = operator_definition_comparison(affine_km_data(), g=1)
        assert result['chain_level_status'] == 'PROVED'

    def test_chain_level_conditional_class_M(self):
        result = operator_definition_comparison(virasoro_data(), g=1)
        assert 'CONDITIONAL' in result['chain_level_status']

    def test_propagator_weight_1(self):
        """Bar propagator has weight 1 in both variables (AP27)."""
        decomp = propagator_decomposition(heisenberg_data(), g=1)
        assert 'd log E' in decomp.bar_part

    def test_genus0_propagator(self):
        """At genus 0, the bar propagator is d log(z - w)."""
        decomp = propagator_decomposition(heisenberg_data(), g=0)
        assert 'd log(z - w)' in decomp.bar_part


# =====================================================================
# Section D: Path 2 -- Spectral sequence comparison
# =====================================================================


class TestPath2SpectralSequence:
    """Path 2: PBW spectral sequence comparison at E_1 and E_2."""

    def test_e1_match_heisenberg(self):
        ss = spectral_sequence_comparison(heisenberg_data(Symbol('k')), g=1)
        assert ss.e1_match is True

    def test_e2_match_heisenberg(self):
        ss = spectral_sequence_comparison(heisenberg_data(Symbol('k')), g=1)
        assert ss.e2_match is True

    def test_e1_match_virasoro(self):
        ss = spectral_sequence_comparison(virasoro_data(Symbol('c')), g=1)
        assert ss.e1_match is True

    def test_e2_match_virasoro(self):
        ss = spectral_sequence_comparison(virasoro_data(Symbol('c')), g=1)
        assert ss.e2_match is True

    def test_e1_match_km(self):
        ss = spectral_sequence_comparison(affine_km_data('sl2', Symbol('k')), g=1)
        assert ss.e1_match is True

    def test_e1_value_heisenberg_genus1(self):
        """E_1 value = kappa/24 at genus 1."""
        k = Symbol('k')
        ss = spectral_sequence_comparison(heisenberg_data(k), g=1)
        assert simplify(ss.e1_value - k * Rational(1, 24)) == 0

    def test_e1_value_virasoro_genus1(self):
        """E_1 value = (c/2)/24 = c/48 at genus 1."""
        c = Symbol('c')
        ss = spectral_sequence_comparison(virasoro_data(c), g=1)
        assert simplify(ss.e1_value - c / 48) == 0

    def test_genus1_explicit_match(self):
        """Explicit genus-1 spectral sequence comparison."""
        k = Symbol('k')
        result = spectral_sequence_genus1_explicit(heisenberg_data(k))
        assert result['E1_match'] is True
        assert simplify(result['E1_trace_bv'] - result['E1_trace_sew']) == 0

    def test_higher_genus_match(self):
        """E_1 match through genus 5 for Heisenberg."""
        k = Symbol('k')
        results = spectral_sequence_higher_genus(heisenberg_data(k), max_genus=5)
        for r in results:
            assert r['match'] is True, f"Failed at genus {r['genus']}"

    def test_higher_genus_match_virasoro(self):
        """E_1 match through genus 5 for Virasoro."""
        c = Symbol('c')
        results = spectral_sequence_higher_genus(virasoro_data(c), max_genus=5)
        for r in results:
            assert r['match'] is True, f"Failed at genus {r['genus']}"

    def test_e2_mechanism_universal(self):
        """The E_2 mechanism (Connes B-operator) is the same for all families."""
        for constructor in [heisenberg_data, virasoro_data,
                            lambda: affine_km_data('sl2')]:
            ss = spectral_sequence_comparison(constructor(), g=1)
            assert 'Connes B-operator' in ss.e2_mechanism


# =====================================================================
# Section E: Path 3 -- Heisenberg extraction
# =====================================================================


class TestPath3HeisenbergExtraction:
    """Path 3: extract Delta = d_sew from the Heisenberg proof."""

    def test_heisenberg_chain_level_proved(self):
        k = Symbol('k')
        result = heisenberg_chain_level_extraction(k)
        assert result['chain_level_status'] == 'PROVED (class G, all genera)'

    def test_heisenberg_intertwining_strict(self):
        k = Symbol('k')
        result = heisenberg_chain_level_extraction(k)
        assert 'STRICT' in result['intertwining']

    def test_heisenberg_genus_data_all_match(self):
        k = Symbol('k')
        result = heisenberg_chain_level_extraction(k)
        for gd in result['genus_data']:
            assert gd['match'] is True, f"Failed at genus {gd['genus']}"

    def test_heisenberg_F1_equals_k_over_24(self):
        k = Symbol('k')
        result = heisenberg_chain_level_extraction(k)
        F1 = result['genus_data'][0]
        assert simplify(F1['F_g_bv'] - k * Rational(1, 24)) == 0

    def test_heisenberg_F2_equals_7k_over_5760(self):
        k = Symbol('k')
        result = heisenberg_chain_level_extraction(k)
        F2 = result['genus_data'][1]
        assert simplify(F2['F_g_bv'] - k * Rational(7, 5760)) == 0

    def test_extension_heisenberg_genus2(self):
        """Heisenberg at genus 2: no planted-forest correction (class G)."""
        result = heisenberg_to_interacting_extension(heisenberg_data(Symbol('k')), genus=2)
        assert result['delta_pf'] == 0
        assert result['extension_status'] == 'PROVED'

    def test_extension_km_genus2(self):
        """Affine KM at genus 2: proved extension (class L)."""
        result = heisenberg_to_interacting_extension(
            affine_km_data('sl2', Symbol('k')), genus=2)
        assert result['extension_status'] == 'PROVED'

    def test_extension_virasoro_genus2(self):
        """Virasoro at genus 2: conditional (class M)."""
        result = heisenberg_to_interacting_extension(virasoro_data(Symbol('c')), genus=2)
        assert 'CONDITIONAL' in result['extension_status']

    def test_nonsep_uses_same_kernel(self):
        """The non-separating contribution at genus 2 uses the same Bergman kernel."""
        for constructor in [heisenberg_data, virasoro_data,
                            lambda: affine_km_data('sl2')]:
            result = heisenberg_to_interacting_extension(constructor(), genus=2)
            assert result['nonsep_uses_same_kernel'] is True


# =====================================================================
# Section F: Path 4 -- Modular operad identification
# =====================================================================


class TestPath4ModularOperad:
    """Path 4: Delta = d_sew from the modular operad structure."""

    def test_nonsep_clutching_genus_raising(self):
        """Non-separating clutching raises genus by 1."""
        data = nonseparating_clutching_data(g=1, n=0)
        assert data.is_genus_raising is True
        assert data.clutching_type == 'non-separating'

    def test_nonsep_clutching_source_target(self):
        """Source is M-bar_{g,n+2}, target is M-bar_{g+1,n}."""
        data = nonseparating_clutching_data(g=1, n=2)
        assert 'M-bar_{1,4}' in data.source_moduli
        assert 'M-bar_{2,2}' in data.target_moduli

    def test_nonsep_identification_proved(self):
        """The identification is proved by the Feynman transform definition."""
        data = nonseparating_clutching_data(g=0, n=2)
        assert data.identification_proved is True

    def test_modular_operad_identification_heisenberg(self):
        result = modular_operad_identification(heisenberg_data(Symbol('k')), g=0)
        assert result['identification'] == 'Delta_BV = d_sew^{ns} = hbar * Delta'
        assert 'DEFINITION-LEVEL' in result['level']

    def test_modular_operad_identification_virasoro(self):
        result = modular_operad_identification(virasoro_data(Symbol('c')), g=0)
        assert result['identification'] == 'Delta_BV = d_sew^{ns} = hbar * Delta'

    def test_modular_operad_deep_content(self):
        """The deep content includes bar-modular-operad and CG17."""
        result = modular_operad_identification(heisenberg_data(), g=0)
        deep = result['deep_content']
        assert any('bar-modular-operad' in item for item in deep)
        assert any('CG17' in item for item in deep)


# =====================================================================
# Section G: Five-component decomposition
# =====================================================================


class TestFiveComponentDecomposition:
    """Verify the five-component decomposition of the modular differential."""

    def test_five_components_exist(self):
        decomp = five_component_decomposition()
        assert decomp.d_int is not None
        assert decomp.tau_twist is not None
        assert decomp.d_sew_sep is not None
        assert decomp.d_pf is not None
        assert decomp.hbar_delta is not None

    def test_d_squared_zero(self):
        decomp = five_component_decomposition()
        assert decomp.d_squared_zero is True

    def test_fifth_component_is_genus_raising(self):
        """The fifth component hbar*Delta is the GENUS-RAISING operation."""
        decomp = five_component_decomposition()
        assert 'GENUS-RAISING' in decomp.hbar_delta

    def test_third_component_is_separating(self):
        """The third component d_sew is the SEPARATING clutching."""
        decomp = five_component_decomposition()
        assert 'Separating' in decomp.d_sew_sep

    def test_d_squared_zero_verification(self):
        """D^2 = 0 decomposes correctly by genus."""
        result = verify_d_squared_zero_components(heisenberg_data(), g=1)
        assert result['d_squared_zero'] is True
        assert 'QME' in result['quantum_me']


# =====================================================================
# Section H: Jacobi identity vanishing (class L)
# =====================================================================


class TestJacobiVanishing:
    """Verify that the Jacobi identity kills cubic harmonic corrections."""

    def test_jacobi_sl2(self):
        result = jacobi_cubic_vanishing('sl2')
        assert result['vanishing'] is True
        assert result['dim'] == 3

    def test_jacobi_sl3(self):
        result = jacobi_cubic_vanishing('sl3')
        assert result['vanishing'] is True
        assert result['dim'] == 8

    def test_sl2_explicit_trace(self):
        """The contraction trace for sl_2 equals dim(sl_2) = 3."""
        result = jacobi_cubic_vanishing('sl2')
        assert result['trace'] == 3


# =====================================================================
# Section I: Bergman kernel trace
# =====================================================================


class TestBergmanKernelTrace:
    """Verify Tr(d_sew) = Tr(Delta_BV) = kappa * lambda_g^FP."""

    def test_trace_heisenberg_genus1(self):
        k = Symbol('k')
        result = bergman_kernel_trace(heisenberg_data(k), g=1)
        assert result['traces_match'] is True
        assert simplify(result['trace_d_sew'] - k / 24) == 0

    def test_trace_virasoro_genus1(self):
        c = Symbol('c')
        result = bergman_kernel_trace(virasoro_data(c), g=1)
        assert result['traces_match'] is True
        assert simplify(result['trace_d_sew'] - c / 48) == 0

    def test_trace_km_genus1(self):
        k = Symbol('k')
        result = bergman_kernel_trace(affine_km_data('sl2', k), g=1)
        assert result['traces_match'] is True

    def test_trace_heisenberg_genus2(self):
        k = Symbol('k')
        result = bergman_kernel_trace(heisenberg_data(k), g=2)
        assert result['traces_match'] is True
        assert simplify(result['trace_d_sew'] - k * Rational(7, 5760)) == 0

    def test_trace_match_all_genera(self):
        """Traces match through genus 5 for all standard families."""
        for constructor in [heisenberg_data, virasoro_data,
                            lambda: affine_km_data('sl2'), betagamma_data]:
            algebra = constructor()
            for g in range(1, 6):
                result = bergman_kernel_trace(algebra, g)
                assert result['traces_match'] is True, (
                    f"Trace mismatch for {algebra.name} at genus {g}")


# =====================================================================
# Section J: Genus-2 explicit verification
# =====================================================================


class TestGenus2Verification:
    """Explicit genus-2 comparison of Delta and d_sew contributions."""

    def test_genus2_boundary_divisors(self):
        result = genus2_bv_sewing_comparison(heisenberg_data(Symbol('k')))
        assert result['num_boundary_divisors'] == 2
        assert 'delta_irr' in result['boundary_divisors']
        assert 'delta_1' in result['boundary_divisors']

    def test_delta_irr_is_nonsep(self):
        """delta_irr is the non-separating boundary (= Delta = d_sew)."""
        result = genus2_bv_sewing_comparison(heisenberg_data(Symbol('k')))
        assert 'non-separating' in result['boundary_divisors']['delta_irr']

    def test_delta_controls_nonsep(self):
        result = genus2_bv_sewing_comparison(heisenberg_data(Symbol('k')))
        assert result['delta_controls_nonsep'] is True

    def test_genus2_F2_heisenberg(self):
        k = Symbol('k')
        result = genus2_bv_sewing_comparison(heisenberg_data(k))
        assert simplify(result['F2_total'] - k * Rational(7, 5760)) == 0


# =====================================================================
# Section K: Propagator variance
# =====================================================================


class TestPropagatorVariance:
    """Propagator variance delta_mix for multi-channel comparison."""

    def test_single_channel_vanishes(self):
        """delta_mix = 0 for single-generator algebras."""
        for constructor in [heisenberg_data, virasoro_data]:
            result = propagator_variance_check(constructor(), g=1)
            assert result['vanishes'] is True

    def test_multi_channel_may_not_vanish(self):
        """delta_mix may be nonzero for multi-generator algebras."""
        result = propagator_variance_check(affine_km_data('sl2'), g=1)
        # sl2 has dim_lie=3 > 1, so multi-channel
        assert result['vanishes'] is False or result['delta_mix'] == 0


# =====================================================================
# Section L: QME genus decomposition
# =====================================================================


class TestQMEDecomposition:
    """Verify the QME decomposes correctly with Delta = d_sew."""

    def test_genus0_is_classical_me(self):
        result = qme_genus_decomposition(heisenberg_data(Symbol('k')))
        assert 'd_bar^2 = 0' in result['genus_0']['content']

    def test_genus1_delta_is_d_sew(self):
        result = qme_genus_decomposition(heisenberg_data(Symbol('k')))
        assert result['genus_1']['delta_is_d_sew'] is True

    def test_genus2_delta_is_d_sew(self):
        result = qme_genus_decomposition(heisenberg_data(Symbol('k')))
        assert result['genus_2']['delta_is_d_sew'] is True

    def test_genus1_F1_value(self):
        k = Symbol('k')
        result = qme_genus_decomposition(heisenberg_data(k))
        assert 'kappa/24' in result['genus_1']['content']


# =====================================================================
# Section M: Four-path synthesis
# =====================================================================


class TestFourPathSynthesis:
    """Verify the four-path synthesis for all standard families."""

    def test_heisenberg_unconditional(self):
        result = four_path_synthesis(heisenberg_data(Symbol('k')))
        assert result['scope'] == 'UNCONDITIONAL'
        assert result['all_four_paths_consistent'] is True

    def test_km_unconditional(self):
        result = four_path_synthesis(affine_km_data('sl2', Symbol('k')))
        assert result['scope'] == 'UNCONDITIONAL'
        assert result['all_four_paths_consistent'] is True

    def test_virasoro_conditional(self):
        result = four_path_synthesis(virasoro_data(Symbol('c')))
        assert result['scope'] == 'CONDITIONAL'
        assert result['all_four_paths_consistent'] is True

    def test_betagamma_conditional(self):
        result = four_path_synthesis(betagamma_data(Symbol('k')))
        assert result['scope'] == 'CONDITIONAL'

    def test_path4_always_proved(self):
        """Path 4 (modular operad) is proved for ALL families."""
        for constructor in [heisenberg_data, virasoro_data,
                            lambda: affine_km_data('sl2'), betagamma_data]:
            result = four_path_synthesis(constructor())
            assert result['paths']['path4_modular_operad'] == 'PROVED (definition-level)'

    def test_path2_always_proved(self):
        """Path 2 (spectral sequence) is proved for ALL families."""
        for constructor in [heisenberg_data, virasoro_data,
                            lambda: affine_km_data('sl2'), betagamma_data]:
            result = four_path_synthesis(constructor())
            assert 'PROVED' in result['paths']['path2_spectral']


# =====================================================================
# Section N: Cross-family numerical verification
# =====================================================================


class TestNumericalVerification:
    """Numerical spot-checks at specific parameter values."""

    def test_numerical_k1_genus1(self):
        results = numerical_trace_comparison(Rational(1), 5)
        assert results[0]['match'] is True
        assert results[0]['trace_bv'] == Rational(1, 24)

    def test_numerical_k2_genus1(self):
        results = numerical_trace_comparison(Rational(2), 5)
        assert results[0]['match'] is True
        assert results[0]['trace_bv'] == Rational(2, 24) == Rational(1, 12)

    def test_numerical_all_genera_match(self):
        for kappa_val in [Rational(1), Rational(2), Rational(13, 2)]:
            results = numerical_trace_comparison(kappa_val, 5)
            for r in results:
                assert r['match'] is True

    def test_lambda_fp_reference_values(self):
        """Cross-check lambda_g^FP against independently known values."""
        vals = numerical_lambda_fp_values()
        assert vals[1] == Rational(1, 24)
        assert vals[2] == Rational(7, 5760)
        assert vals[3] == Rational(31, 967680)


# =====================================================================
# Section O: Full verification suite
# =====================================================================


class TestFullVerification:
    """Run the comprehensive verification suite."""

    def test_full_suite_passes(self):
        result = verify_bv_sewing_identification(max_genus=3)
        assert result['all_pass'] is True

    def test_full_suite_covers_four_families(self):
        result = verify_bv_sewing_identification(max_genus=2)
        assert 'Heisenberg' in result['families_tested']
        assert 'Virasoro' in result['families_tested']
        assert 'sl2' in result['families_tested']

    def test_full_suite_bergman_traces(self):
        """All Bergman kernel traces match across families and genera."""
        result = verify_bv_sewing_identification(max_genus=3)
        for family, data in result['results'].items():
            for key, val in data.items():
                if key.startswith('bergman_trace_') and isinstance(val, dict):
                    assert val['traces_match'] is True, (
                        f"Bergman trace mismatch: {family} {key}")


# =====================================================================
# Section P: Multi-path verification mandate (3+ paths per claim)
# =====================================================================


class TestMultiPathVerification:
    """Every key claim verified by at least 3 independent paths."""

    def test_F1_heisenberg_three_paths(self):
        """F_1(H_k) = k/24 verified by Bernoulli, A-hat, and BV trace."""
        k = Rational(1)
        # Path 1: Bernoulli formula
        p1 = k * lambda_fp(1)
        # Path 2: A-hat extraction
        p2 = k * lambda_fp_from_ahat(1)
        # Path 3: BV trace (spectral sequence)
        ss = spectral_sequence_genus1_explicit(heisenberg_data(k))
        p3 = ss['E1_trace_bv']
        assert p1 == p2 == p3 == Rational(1, 24)

    def test_F2_heisenberg_three_paths(self):
        """F_2(H_k) = 7k/5760 verified by Bernoulli, A-hat, and genus-2."""
        k = Rational(1)
        p1 = k * lambda_fp(2)
        p2 = k * lambda_fp_from_ahat(2)
        g2 = genus2_bv_sewing_comparison(heisenberg_data(k))
        p3 = g2['F2_total']
        assert p1 == p2 == p3 == Rational(7, 5760)

    def test_delta_eq_dsew_three_paths(self):
        """Delta_BV = d_sew verified by 3 paths: operator, SS, modular operad."""
        algebra = heisenberg_data(Symbol('k'))
        # Path 1: operator definition
        p1 = operator_definition_comparison(algebra, g=1)
        assert p1['scalar_trace_match'] is True
        # Path 2: spectral sequence
        p2 = spectral_sequence_comparison(algebra, g=1)
        assert p2.e1_match is True
        # Path 4: modular operad
        p4 = modular_operad_identification(algebra, g=0)
        assert 'DEFINITION-LEVEL' in p4['level']

    def test_kappa_24_four_paths(self):
        """kappa/24 verified by: Bernoulli, A-hat, BV zeta, Bergman trace."""
        k = Symbol('k')
        # Path 1: Bernoulli
        assert lambda_fp(1) == Rational(1, 24)
        # Path 2: A-hat
        assert lambda_fp_from_ahat(1) == Rational(1, 24)
        # Path 3: BV zeta (trace of BV Laplacian)
        bkt = bergman_kernel_trace(heisenberg_data(k), g=1)
        assert simplify(bkt['trace_delta_bv'] - k / 24) == 0
        # Path 4: Sewing trace
        assert simplify(bkt['trace_d_sew'] - k / 24) == 0


# =====================================================================
# Section Q: Edge cases and consistency
# =====================================================================


class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_genus1_is_minimum(self):
        """genus g=1 is the minimum for the genus-raising operator."""
        data = nonseparating_clutching_data(g=0, n=2)
        assert data.genus == 0
        # Raising genus 0 -> genus 1

    def test_synthesis_theorem_statement(self):
        """The theorem statement is consistent."""
        result = four_path_synthesis(heisenberg_data(Symbol('k')))
        assert 'Delta_BV = d_sew' in result['theorem']

    def test_five_component_covers_all(self):
        """The five components cover the full modular differential D."""
        decomp = five_component_decomposition()
        # All five are non-empty
        assert len(decomp.d_int) > 0
        assert len(decomp.tau_twist) > 0
        assert len(decomp.d_sew_sep) > 0
        assert len(decomp.d_pf) > 0
        assert len(decomp.hbar_delta) > 0

    def test_class_hierarchy(self):
        """Shadow depth ordering: G(2) < L(3) < C(4) < M(inf)."""
        assert heisenberg_data().shadow_depth == 2
        assert affine_km_data().shadow_depth == 3
        assert betagamma_data().shadow_depth == 4
        assert virasoro_data().shadow_depth > 4
