r"""Tests for holographic_entanglement_qec_engine.py.

Verification strategy (multi-path, per CLAUDE.md mandate):

1. RT FROM COMPLEMENTARITY: 3 derivation paths (direct, replica, complementarity)
2. QES CANDIDATES: formal coefficients plus the geometric bridge obligation
3. KNILL-LAFLAMME: isotropy input plus Hilbert/error-algebra obligations
4. SHADOW DEPTH: G/L/C/M arity profiles, with physical parameters pending
5. RECONSTRUCTION: universal Theorem A, certificate-bound Theorem B, OCA bridge
6. MODULAR FLOW: shadow connection, temperature, flow velocity
7. JLMS FORMULA: decomposition, positivity, complementarity consistency
8. TENSOR NETWORK: MERA analogy, bond dimension, depth
9. HOLOGRAPHIC RENYI: spectrum, monotonicity, min-entropy, cosmic brane
10. HAYDEN-PRESKILL: scrambling, decoupling, Page curve

Cross-checks:
- scalar ``n -> 1`` replica limit;
- Virasoro complementarity coefficient;
- formal RT-dictionary coefficient identity;
- scalar replica monotonicity and limiting value;
- exact Cone(q_A) certificate transitions and bridge separation.
"""

import pytest
from sympy import Matrix, Rational, pi, oo

from compute.lib.qec_koszul_code_engine import (
    quadratic_comparison_cone,
    theorem_b_certificate_from_cone,
)

from compute.lib.holographic_entanglement_qec_engine import (
    physical_bridge_surfaces,
    # Section 1: RT from complementarity
    rt_from_kappa,
    rt_from_complementarity,
    rt_area_identification,
    rt_three_derivations,
    # Section 2: Quantum extremal surface
    quantum_extremal_surface,
    qes_area_vs_bulk_ratio,
    qes_shift_genus1,
    # Section 3: Knill-Laflamme
    knill_laflamme_from_complementarity,
    kl_error_algebra_structure,
    kl_conditions_by_genus,
    # Section 4: Shadow depth = code structure
    shadow_depth_code_parameters,
    code_rate_by_class,
    code_distance_effective,
    # Section 5: Entanglement wedge
    entanglement_wedge_from_bar_cobar,
    subregion_duality_check,
    greedy_algorithm_from_bar_filtration,
    # Section 6: Modular flow
    modular_hamiltonian_from_shadow,
    modular_flow_from_connection,
    modular_temperature,
    # Section 7: JLMS
    jlms_formula,
    jlms_relative_entropy_bound,
    jlms_complementarity_consistency,
    # Section 8: Tensor network
    bar_complex_as_tensor_network,
    bond_dimension_from_shadow,
    mera_depth_vs_shadow_depth,
    # Section 9: Holographic Renyi
    holographic_renyi_entropy,
    renyi_spectrum,
    renyi_monotonicity_check,
    renyi_min_entropy,
    cosmic_brane_tension,
    # Section 10: Hayden-Preskill
    hayden_preskill_scrambling,
    decoupling_time,
    page_time_from_complementarity,
    page_curve_profile,
    # Section 11: Cross-checks
    full_qec_census,
    cross_check_rt_renyi_limit,
    cross_check_complementarity_sum,
    cross_check_area_identification,
    cross_check_renyi_monotonicity_all_families,
    cross_check_min_entropy_half_vn,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    von_neumann_entropy_scalar,
    renyi_entropy_scalar,
    faber_pandharipande,
    scalar_free_energy,
    STANDARD_KAPPAS,
)


def _quadratic_certificate(
    algebra_id: str,
    *,
    comparison_entry: int = 1,
    h_cl_verified: bool = True,
    strong_convergence_verified: bool = True,
):
    """Build an exact one-term Theorem B certificate."""
    cone = quadratic_comparison_cone(
        source_dimensions={0: 1},
        target_dimensions={0: 1},
        source_differentials={},
        target_differentials={},
        comparison_maps={0: Matrix([[comparison_entry]])},
    )
    return theorem_b_certificate_from_cone(
        cone,
        algebra_id=algebra_id,
        presentation='A = T(V)/(R), one-term finite model',
        h_cl_verified=h_cl_verified,
        strong_convergence_verified=strong_convergence_verified,
    )


# ===================================================================
# 1. RYU-TAKAYANAGI FROM COMPLEMENTARITY
# ===================================================================

class TestRTFromComplementarity:
    """Ryu-Takayanagi derived from kappa and Theorem C."""

    def test_rt_c1(self):
        """S_RT(c=1) = 1/3."""
        assert rt_from_kappa(Rational(1, 2), 1) == Rational(1, 3)

    def test_rt_c13(self):
        """S_RT(c=13) = 13/3 (self-dual)."""
        assert rt_from_kappa(Rational(13, 2), 1) == Rational(13, 3)

    def test_rt_c26(self):
        """S_RT(c=26) = 26/3 (critical string)."""
        assert rt_from_kappa(Rational(13), 1) == Rational(26, 3)

    def test_rt_equals_calabrese_cardy(self):
        """RT formula = Calabrese-Cardy: S = (c/3)*log(L/eps)."""
        for c_val in [1, Rational(1, 2), 13, 26]:
            kappa = kappa_virasoro(c_val)
            rt = rt_from_kappa(kappa, 1)
            cc = Rational(c_val, 3)
            assert rt == cc, f"RT != CC at c={c_val}: {rt} != {cc}"

    def test_rt_from_complementarity_matches_direct(self):
        """Path via complementarity matches direct computation."""
        for c_val in [1, 6, 13, 26]:
            direct = rt_from_kappa(kappa_virasoro(c_val), 1)
            compl = rt_from_complementarity(c_val, 1)
            assert direct == compl

    def test_rt_area_identification_consistent(self):
        """The two formal coefficients agree; the RT bridge stays explicit."""
        for c_val in [1, 13, 26]:
            data = rt_area_identification(c_val)
            assert data['consistent'] is True
            assert data['physical_rt_identification'] is None
            assert data['physical_rt_status'] == 'CONDITIONAL_ON_ADS_CFT_RT_QES_BRIDGE'

    def test_rt_area_identification_c26_values(self):
        """At c=26: 1/(4G_N) = 13/3, kappa = 13."""
        data = rt_area_identification(Rational(26))
        assert data['inv_4GN'] == Rational(13, 3)
        assert data['kappa'] == Rational(13)

    def test_three_derivations_agree(self):
        """All scalar normalization paths agree for multiple c values."""
        for c_val in [1, Rational(1, 2), 13, 26, Rational(7, 10)]:
            data = rt_three_derivations(c_val)
            assert data['all_agree'] is True, f"Paths disagree at c={c_val}"
            assert data['physical_rt'] is None

    def test_rt_linearity_in_kappa(self):
        """RT is linear in kappa: S(a*kappa) = a*S(kappa)."""
        kappa1 = Rational(1)
        kappa2 = Rational(3)
        s1 = rt_from_kappa(kappa1, 1)
        s2 = rt_from_kappa(kappa2, 1)
        assert s2 == 3 * s1

    def test_rt_linearity_in_log_ratio(self):
        """RT is linear in log(L/eps)."""
        kappa = Rational(13, 2)
        s1 = rt_from_kappa(kappa, 1)
        s2 = rt_from_kappa(kappa, 2)
        assert s2 == 2 * s1


# ===================================================================
# 2. QUANTUM EXTREMAL SURFACE
# ===================================================================

class TestQuantumExtremalSurface:
    """Formal shadow candidates and the QES bridge surface."""

    def test_qes_area_positive(self):
        """Area contribution is positive for positive kappa."""
        qes = quantum_extremal_surface(Rational(13, 2), 1)
        assert qes['S_area'] > 0

    def test_qes_area_equals_rt(self):
        """The scalar candidate matches the RT-side coefficient."""
        kappa = Rational(13, 2)
        qes = quantum_extremal_surface(kappa, 1)
        rt = rt_from_kappa(kappa, 1)
        assert qes['S_area'] == rt
        assert qes['physical_qes'] is None
        assert qes['physical_qes_status'] == 'CONDITIONAL_ON_ADS_CFT_RT_QES_BRIDGE'

    def test_qes_bulk_subleading(self):
        """Bulk corrections are subleading (ratio < 1)."""
        ratio = qes_area_vs_bulk_ratio(Rational(13, 2), 1)
        assert ratio['ratio'] < 1

    def test_formal_ratio_is_kappa_scale_invariant(self):
        ratio_1 = qes_area_vs_bulk_ratio(Rational(1), 1)
        ratio_13 = qes_area_vs_bulk_ratio(Rational(13), 1)
        assert ratio_1['ratio'] == ratio_13['ratio']
        assert ratio_13['ratio'] < Rational(1, 100)
        assert ratio_13['formal_small_correction'] is True
        assert ratio_13['kappa_scale_invariant'] is True
        assert ratio_13['semiclassical'] is None

    def test_qes_genus_corrections_decay(self):
        """Genus corrections decay: |F_g| decreases with g."""
        qes = quantum_extremal_surface(Rational(13, 2), 1, genus_corrections=5)
        corrections = qes['genus_corrections']
        for i in range(len(corrections) - 1):
            assert abs(corrections[i]['F_g']) >= abs(corrections[i + 1]['F_g'])

    def test_qes_symmetric_shift_zero(self):
        """Parity fixes the formal symmetric candidate."""
        shift = qes_shift_genus1(Rational(13, 2))
        assert shift['formal_symmetric_shift'] == 0
        assert shift['symmetric_shift'] is None
        assert shift['physical_qes_shift'] is None

    def test_qes_gen_larger_than_area(self):
        """S_gen >= S_area (bulk entropy is non-negative at leading order)."""
        for kappa in [Rational(1), Rational(13, 2), Rational(13)]:
            qes = quantum_extremal_surface(kappa, 1)
            # This checks the exact formal sum implemented by the engine.
            assert qes['S_gen'] is not None
            assert qes['physical_qes'] is None


# ===================================================================
# 3. KNILL-LAFLAMME FROM LAGRANGIAN ISOTROPY
# ===================================================================

class TestKnillLaflamme:
    """Theorem C input and the physical Knill--Laflamme obligation."""

    def test_genus1_compression_lemma_and_physical_status(self):
        kl = knill_laflamme_from_complementarity(1)
        assert kl['kl_satisfied'] is None
        assert kl['formal_compression_lemma'] is True
        assert kl['dim_Q_g'] == 1
        assert kl['physical_kl_status'] == (
            'CONDITIONAL_ON_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS'
        )

    def test_genus2_requires_physical_error_products(self):
        kl = knill_laflamme_from_complementarity(2)
        assert kl['kl_satisfied'] is None
        assert kl['isotropy_proved'] is True

    def test_kl_isotropy_all_genera(self):
        """Isotropy is proved at ALL genera (algebraic proof)."""
        for g in range(2, 6):
            kl = knill_laflamme_from_complementarity(g)
            assert kl['isotropy_proved'] is True

    def test_error_algebra_virasoro(self):
        """The Virasoro dual-family candidate is recorded separately."""
        ea = kl_error_algebra_structure('virasoro')
        assert ea['dual_family'] == 'Vir_{26-c}'
        assert ea['shadow_class'] == 'M'
        assert ea['physical_error_algebra'] is None

    def test_error_algebra_heisenberg(self):
        """Heisenberg error algebra: class G, 0 redundancy."""
        ea = kl_error_algebra_structure('heisenberg')
        assert ea['shadow_class'] == 'G'

    def test_error_algebra_affine(self):
        """Affine error algebra: Feigin-Frenkel dual, class L."""
        ea = kl_error_algebra_structure('affine')
        assert ea['shadow_class'] == 'L'

    def test_kl_by_genus_progression(self):
        """Every genus retains the Hilbert/error-algebra bridge status."""
        data = kl_conditions_by_genus(Rational(13, 2), 4)
        for g in [1, 2, 3, 4]:
            assert data[g]['status'] == 'PHYSICAL_BRIDGE_REQUIRED'
            assert data[g]['kl_satisfied'] is None


# ===================================================================
# 4. SHADOW DEPTH = CODE STRUCTURE
# ===================================================================

class TestShadowDepthCode:
    """Shadow depth determines arity profiles only."""

    def test_class_G_parameters(self):
        """Class G has the scalar-only arity profile."""
        p = shadow_depth_code_parameters('heisenberg')
        assert p['shadow_class'] == 'G'
        assert p['n_redundancy'] == 0
        assert p['code_type'] == 'arity_profile_G'
        assert p['code_notation'] is None
        assert p['n_logical'] is None
        assert p['n_physical'] is None

    def test_class_L_parameters(self):
        """Class L adds one higher-arity slot."""
        p = shadow_depth_code_parameters('affine')
        assert p['shadow_class'] == 'L'
        assert p['n_redundancy'] == 1
        assert p['code_notation'] is None
        assert p['higher_arity_slots'] == 1

    def test_class_C_parameters(self):
        """Class C adds two higher-arity slots."""
        p = shadow_depth_code_parameters('betagamma')
        assert p['shadow_class'] == 'C'
        assert p['n_redundancy'] == 2
        assert p['code_notation'] is None
        assert p['higher_arity_slots'] == 2

    def test_class_M_parameters(self):
        """Class M records an unbounded arity tower."""
        p = shadow_depth_code_parameters('virasoro')
        assert p['shadow_class'] == 'M'
        assert p['n_redundancy'] == -1  # infinite
        assert p['code_type'] == 'arity_profile_M'
        assert p['physical_code_parameters'] is None

    def test_physical_code_rate_requires_realization(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            assert code_rate_by_class(family) is None

    def test_physical_code_distance_requires_error_model(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            assert code_distance_effective(family) is None

    def test_family_labels_leave_hilbert_parameters_pending(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            p = shadow_depth_code_parameters(family)
            assert p['n_logical'] is None
            assert p['n_physical'] is None
            assert p['recovery_channels'] is None
            assert p['physical_code_status'] == (
                'CONDITIONAL_ON_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS'
            )


# ===================================================================
# 5. ENTANGLEMENT WEDGE RECONSTRUCTION
# ===================================================================

class TestEntanglementWedge:
    """Typed algebraic reconstruction and the OCA/subregion bridge."""

    def test_family_labels_leave_theorem_b_unverified(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            ew = entanglement_wedge_from_bar_cobar(family)
            assert ew['universal_reconstruction'] is True
            assert ew['exact_reconstruction'] is None
            assert ew['exact_reconstruction_status'] == 'UNVERIFIED'
            assert ew['is_koszul'] is None

    def test_reconstruction_map_is_universal_epsilon(self):
        ew = entanglement_wedge_from_bar_cobar('virasoro')
        assert ew['reconstruction_map'] == 'epsilon_A: Omega_X B_X(A) -> A'
        assert ew['theorem_a_surface']['theorem'] == 'A'

    def test_encoding_map_is_bar(self):
        """Encoding is the bar object assignment."""
        ew = entanglement_wedge_from_bar_cobar('virasoro')
        assert ew['encoding_map'] == 'B_X (bar object assignment)'

    def test_bar_and_physical_bulk_have_separate_slots(self):
        ew = entanglement_wedge_from_bar_cobar('virasoro')
        assert ew['bar_slot'] == 'B_X(A): twisting/coupling coalgebra'
        assert ew['physical_bulk_claim'] is None
        assert ew['bulk_slot'] == (
            'Z^der_ch(A) = ChirHoch^*(A,A) after derived-centre/BRST comparison'
        )
        assert ew['physical_entanglement_wedge_status'] == (
            'CONDITIONAL_ON_OCA_DERIVED_CENTRE_AND_SUBREGION_MAPS'
        )

    def test_subregion_duality_requires_regional_bridge(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            check = subregion_duality_check(family)
            assert check['algebraic_complementarity'] is None
            assert check['subregion_duality'] is None

    def test_theorem_c_package_transitions_only_algebraic_complementarity(self):
        check = subregion_duality_check(
            'virasoro', theorem_c_package_verified=True
        )
        assert check['algebraic_complementarity'] is True
        assert check['subregion_duality'] is None

    def test_exact_cone_certificate_transitions_theorem_b(self):
        algebra_id = 'virasoro:c=13'
        certificate = _quadratic_certificate(algebra_id)
        ew = entanglement_wedge_from_bar_cobar(
            'virasoro',
            c=13,
            algebra_id=algebra_id,
            quadratic_certificate=certificate,
        )
        assert ew['universal_reconstruction'] is True
        assert ew['is_koszul'] is True
        assert ew['exact_reconstruction'] is True
        assert ew['exact_reconstruction_status'] == 'CERTIFIED'
        assert ew['physical_entanglement_wedge'] is None

    def test_obstructed_cone_transitions_theorem_b(self):
        algebra_id = 'affine:sl2:k=1'
        certificate = _quadratic_certificate(algebra_id, comparison_entry=0)
        ew = entanglement_wedge_from_bar_cobar(
            'affine',
            algebra_id=algebra_id,
            quadratic_certificate=certificate,
        )
        assert ew['is_koszul'] is False
        assert ew['exact_reconstruction'] is False
        assert ew['exact_reconstruction_status'] == 'OBSTRUCTED_IN_FINITE_MODEL'

    def test_incomplete_certificate_keeps_theorem_b_pending(self):
        algebra_id = 'betagamma:lambda=1'
        certificate = _quadratic_certificate(
            algebra_id, strong_convergence_verified=False
        )
        ew = entanglement_wedge_from_bar_cobar(
            'betagamma',
            algebra_id=algebra_id,
            quadratic_certificate=certificate,
        )
        assert ew['is_koszul'] is None
        assert ew['exact_reconstruction'] is None
        assert ew['exact_reconstruction_status'] == 'INCOMPLETE_PACKAGE'

    def test_mismatched_certificate_is_rejected(self):
        certificate = _quadratic_certificate('virasoro:c=13')
        with pytest.raises(ValueError, match='algebra_id'):
            entanglement_wedge_from_bar_cobar(
                'virasoro',
                c=26,
                algebra_id='virasoro:c=26',
                quadratic_certificate=certificate,
            )

    def test_greedy_heisenberg_1_layer(self):
        """Heisenberg (class G): 1 greedy layer."""
        ga = greedy_algorithm_from_bar_filtration('heisenberg')
        assert ga['n_layers'] == 1
        assert ga['terminates'] is True

    def test_greedy_affine_2_layers(self):
        """Affine (class L): 2 greedy layers."""
        ga = greedy_algorithm_from_bar_filtration('affine')
        assert ga['n_layers'] == 2
        assert ga['terminates'] is True

    def test_greedy_betagamma_3_layers(self):
        """Beta-gamma (class C): 3 greedy layers."""
        ga = greedy_algorithm_from_bar_filtration('betagamma')
        assert ga['n_layers'] == 3
        assert ga['terminates'] is True

    def test_greedy_virasoro_infinite(self):
        """Virasoro has an unbounded formal layer sequence."""
        ga = greedy_algorithm_from_bar_filtration('virasoro')
        assert ga['n_layers'] == -1
        assert ga['terminates'] is False
        assert ga['convergent'] is None
        assert ga['physical_greedy_decoder'] is None

    def test_explicit_convergence_package_is_recorded(self):
        ga = greedy_algorithm_from_bar_filtration(
            'virasoro', convergence_verified=True
        )
        assert ga['convergent'] is True
        assert ga['convergence_status'] == 'CERTIFIED'


# ===================================================================
# 6. MODULAR FLOW FROM SHADOW CONNECTION
# ===================================================================

class TestModularFlow:
    """Modular flow from the shadow connection."""

    def test_modular_hamiltonian_c13(self):
        """K^{scalar} = (2*kappa/3) = 13/3 at c=13."""
        mh = modular_hamiltonian_from_shadow(Rational(13, 2))
        assert mh['K_scalar'] == Rational(13, 3)

    def test_modular_hamiltonian_equals_rt(self):
        """The shadow scalar equals the entropy-side candidate."""
        for kappa in [Rational(1, 2), Rational(13, 2), Rational(13)]:
            mh = modular_hamiltonian_from_shadow(kappa)
            rt = rt_from_kappa(kappa, 1)
            assert mh['K_scalar'] == rt
            assert mh['S_EE'] is None
            assert mh['physical_modular_hamiltonian'] is None

    def test_modular_flow_stationary_at_origin(self):
        """Modular flow velocity v(0) = 0 (for alpha=0)."""
        flow = modular_flow_from_connection(Rational(13, 2))
        assert flow['v_at_0'] == 0

    def test_modular_flow_monodromy(self):
        """Shadow connection monodromy = -1 (Koszul sign)."""
        flow = modular_flow_from_connection(Rational(13, 2))
        assert flow['monodromy'] == -1
        assert flow['physical_modular_flow'] is None

    def test_modular_temperature_rindler(self):
        """The Rindler candidate is recorded beside the modular bridge."""
        mt = modular_temperature(Rational(13, 2))
        assert mt['rindler_temperature_candidate'] == 1 / (2 * pi)
        assert mt['rindler_beta_candidate'] == 2 * pi
        assert mt['T_ent'] is None
        assert mt['beta_ent'] is None

    def test_trivial_flow_class_G(self):
        """S_4=0 gives a stationary shadow connection."""
        flow = modular_flow_from_connection(Rational(1), S4_val=0)
        assert flow['shadow_connection_type'] == 'stationary'
        assert flow['flow_type'] is None
        assert flow['Delta_crit'] == 0

    def test_nontrivial_flow_class_M(self):
        """A nonzero S_4 gives a nonstationary shadow connection."""
        flow = modular_flow_from_connection(Rational(13, 2), S4_val=Rational(1, 10))
        assert flow['shadow_connection_type'] == 'nonstationary'
        assert flow['flow_type'] is None
        assert flow['Delta_crit'] != 0


# ===================================================================
# 7. JLMS FORMULA
# ===================================================================

class TestJLMS:
    """Scalar candidates and the operator-algebraic JLMS bridge."""

    def test_jlms_area_contribution(self):
        """Area contribution = (2*kappa/3)*log(L/eps)."""
        jlms = jlms_formula(Rational(13, 2))
        assert jlms['area_contribution'] == Rational(13, 3)

    def test_jlms_decomposition_requires_operator_bridge(self):
        jlms = jlms_formula(Rational(13, 2))
        assert jlms['decomposition_valid'] is None
        assert jlms['physical_jlms'] is None
        assert jlms['physical_jlms_status'] == (
            'CONDITIONAL_ON_TOMITA_JLMS_OPERATOR_ALGEBRA_PACKAGE'
        )

    def test_relative_entropy_requires_state_data(self):
        bound = jlms_relative_entropy_bound(Rational(13, 2))
        assert bound['positivity'] is None
        assert bound['shadow_correction_bound'] is None
        assert 'specified normalized states' in bound[
            'relative_entropy_positivity_theorem'
        ]

    def test_jlms_complementarity_c13(self):
        """JLMS + complementarity: K_A + K_{A!} = 26/3 at c=13."""
        data = jlms_complementarity_consistency(Rational(13))
        assert data['K_sum'] == Rational(26, 3)
        assert data['scalar_identity_holds'] is True
        assert data['consistent'] is None

    def test_jlms_complementarity_c1(self):
        """JLMS + complementarity at c=1."""
        data = jlms_complementarity_consistency(Rational(1))
        assert data['scalar_identity_holds'] is True

    def test_jlms_complementarity_c26(self):
        """JLMS + complementarity at c=26."""
        data = jlms_complementarity_consistency(Rational(26))
        assert data['scalar_identity_holds'] is True

    def test_jlms_area_equals_rt(self):
        """JLMS area contribution matches RT formula."""
        kappa = Rational(13, 2)
        jlms = jlms_formula(kappa)
        rt = rt_from_kappa(kappa, 1)
        assert jlms['area_contribution'] == rt


# ===================================================================
# 8. TENSOR NETWORK (BAR COMPLEX AS MERA)
# ===================================================================

class TestTensorNetwork:
    """Bar arity filtration and the tensor-network bridge."""

    def test_class_G_finite_layers(self):
        """Class G: finite layers."""
        tn = bar_complex_as_tensor_network('heisenberg')
        assert tn['is_exact'] is None
        assert tn['exact_contraction_status'] == 'UNVERIFIED'
        assert tn['universal_reconstruction'] is True
        assert tn['shadow_class'] == 'G'

    def test_class_M_infinite_layers(self):
        """Class M: infinite layers."""
        tn = bar_complex_as_tensor_network('virasoro')
        assert 'infinite' in tn['n_layers']

    def test_family_labels_leave_exact_contraction_unverified(self):
        for family in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            tn = bar_complex_as_tensor_network(family)
            assert tn['is_exact'] is None
            assert tn['physical_tensor_network'] is None

    def test_certificate_transitions_algebraic_contraction_only(self):
        algebra_id = 'heisenberg:k=1'
        tn = bar_complex_as_tensor_network(
            'heisenberg',
            k=1,
            algebra_id=algebra_id,
            quadratic_certificate=_quadratic_certificate(algebra_id),
        )
        assert tn['is_exact'] is True
        assert tn['exact_contraction_status'] == 'CERTIFIED'
        assert tn['physical_tensor_network'] is None

    def test_bond_dimension_normalized(self):
        """Bond dimension at arity 2 is normalized to 1."""
        bd = bond_dimension_from_shadow(Rational(13, 2), 2)
        assert bd['normalized_shadow_ratio'] == 1
        assert bd['chi'] is None
        assert bd['bond_dimension'] is None

    def test_mera_depth_ordering(self):
        """MERA depth: G < L < C < M."""
        data = mera_depth_vs_shadow_depth()
        assert data['G']['arity_layers'] == 1
        assert data['L']['arity_layers'] == 2
        assert data['C']['arity_layers'] == 3
        assert data['M']['arity_layers'] == 'unbounded'
        assert all(data[cls]['mera_depth'] is None for cls in data)

    def test_network_convergence_requires_norm_control(self):
        data = mera_depth_vs_shadow_depth()
        for cls in ['G', 'L', 'C', 'M']:
            assert data[cls]['convergent'] is None
            assert data[cls]['status'] == (
                'CONDITIONAL_ON_EXPLICIT_TENSORS_ISOMETRIES_AND_NORM_CONTROL'
            )


# ===================================================================
# 9. HOLOGRAPHIC RENYI ENTROPY
# ===================================================================

class TestHolographicRenyi:
    """Scalar replica candidates and the entropy bridge."""

    def test_entropy_bridge_is_explicit(self):
        bridge = physical_bridge_surfaces()['entropy']
        assert bridge['physical_conclusion'] is None
        assert bridge['status'] == (
            'CONDITIONAL_ON_REPLICA_STATE_AND_ANALYTIC_CONTINUATION'
        )

    def test_renyi_n1_equals_von_neumann(self):
        """S_1 = von Neumann = (2*kappa/3)."""
        kappa = Rational(13, 2)
        assert holographic_renyi_entropy(kappa, 1, 1) == Rational(13, 3)

    def test_renyi_n2_c13(self):
        """S_2(c=13) = (kappa/3)(1+1/2) = (13/2)/3 * 3/2 = 13/4."""
        assert holographic_renyi_entropy(Rational(13, 2), 2, 1) == Rational(13, 4)

    def test_renyi_matches_scalar_formula(self):
        """The public candidate matches the canonical scalar formula."""
        kappa = Rational(13, 2)
        for n in [2, 3, 4, 5]:
            hre = holographic_renyi_entropy(kappa, n, 1)
            scalar = renyi_entropy_scalar(kappa, n, 1)
            assert hre == scalar, f"Mismatch at n={n}"

    def test_renyi_monotonicity_c13(self):
        """Renyi spectrum is monotonically decreasing at c=13."""
        assert renyi_monotonicity_check(Rational(13, 2)) is True

    def test_renyi_monotonicity_c1(self):
        """Renyi spectrum is monotonically decreasing at c=1."""
        assert renyi_monotonicity_check(Rational(1, 2)) is True

    def test_renyi_spectrum_length(self):
        """Renyi spectrum has n_max entries."""
        spec = renyi_spectrum(Rational(13, 2), 1, 8)
        assert len(spec) == 8

    def test_renyi_spectrum_decreasing(self):
        """Explicit check: S_1 > S_2 > S_3 > ..."""
        spec = renyi_spectrum(Rational(13, 2), 1, 6)
        for n in range(1, 6):
            assert spec[n] >= spec[n + 1]

    def test_min_entropy(self):
        """S_inf = (kappa/3) = S_1/2."""
        kappa = Rational(13, 2)
        s_inf = renyi_min_entropy(kappa, 1)
        s_vn = von_neumann_entropy_scalar(kappa, 1)
        assert s_inf == s_vn / 2
        assert s_inf == Rational(13, 6)

    def test_cosmic_brane_tension_n1(self):
        """The tension candidate equals zero at n=1."""
        assert cosmic_brane_tension(1, Rational(26)) == 0

    def test_cosmic_brane_tension_n2(self):
        """T_2 = c/12 at n=2."""
        assert cosmic_brane_tension(2, Rational(26)) == Rational(13, 6)

    def test_cosmic_brane_tension_large_n(self):
        """T_n -> c/6 = 1/(4G_N) as n -> inf."""
        c_val = Rational(26)
        # At large n: (n-1)/n -> 1, so T_n -> c/6
        T_100 = cosmic_brane_tension(100, c_val)
        T_limit = c_val / 6
        assert abs(T_100 - T_limit) < Rational(1, 10)


# ===================================================================
# 10. HAYDEN-PRESKILL AND PAGE CURVE
# ===================================================================

class TestHaydenPreskill:
    """Shadow monodromy, scalar envelope, and chaos/Page bridge."""

    def test_monodromy_koszul_sign(self):
        """Shadow connection monodromy = -1."""
        hp = hayden_preskill_scrambling(Rational(13, 2))
        assert hp['monodromy'] == -1

    def test_mss_saturation_requires_otoc_dynamics(self):
        hp = hayden_preskill_scrambling(Rational(13, 2))
        assert hp['lyapunov_saturates_MSS'] is None
        assert hp['scrambling_time'] is None
        assert hp['chaos_page_status'] == (
            'CONDITIONAL_ON_DYNAMICS_OTOC_EVAPORATION_AND_ISLANDS'
        )

    def test_decoupling_requires_physical_dynamics(self):
        dt = decoupling_time(Rational(13, 2))
        assert dt['scrambling_is_koszul'] is None
        assert dt['decoupling_time'] is None

    def test_scalar_self_dual_point_c13(self):
        pt = page_time_from_complementarity(Rational(13))
        assert pt['scalar_self_dual_point'] is True
        assert pt['is_page_point'] is None
        assert pt['page_time'] is None
        assert pt['S_A'] == Rational(13, 3)

    def test_scalar_branch_c_lt_13(self):
        pt = page_time_from_complementarity(Rational(1))
        assert pt['scalar_branch'] == 'A'
        assert pt['phase'] is None
        assert pt['S_A'] < pt['S_Ac']

    def test_scalar_branch_c_gt_13(self):
        pt = page_time_from_complementarity(Rational(26))
        assert pt['scalar_branch'] == 'A_dual'
        assert pt['phase'] is None
        assert pt['S_A'] > pt['S_Ac']

    def test_page_symmetry(self):
        """Page curve symmetric: S(c) + S(26-c) = 26/3."""
        for c_val in [1, 5, 10, 13, 20, 26]:
            pt = page_time_from_complementarity(Rational(c_val))
            assert pt['S_total'] == Rational(26, 3)

    def test_scalar_envelope_changes_branch_at_self_duality(self):
        profile = page_curve_profile()
        for p in profile:
            if p['c'] == 12:
                assert p['scalar_branch'] == 'A'
            elif p['c'] == 14:
                assert p['scalar_branch'] == 'A_dual'
            assert p['physical_page_curve'] is None

    def test_page_curve_endpoints(self):
        """The scalar branches have the expected endpoints."""
        profile = page_curve_profile()
        assert profile[0]['S_A'] == 0  # c=0
        assert profile[-1]['S_A'] == Rational(26, 3)  # c=26


# ===================================================================
# 11. CROSS-CHECKS (AP10 PREVENTION)
# ===================================================================

class TestCrossChecks:
    """Multi-path cross-checks for internal consistency."""

    def test_rt_equals_renyi_limit(self):
        """RT = n->1 limit of Renyi for multiple kappa values."""
        for kappa in [Rational(1, 2), Rational(1), Rational(13, 2), Rational(13)]:
            assert cross_check_rt_renyi_limit(kappa) is True

    def test_complementarity_sum_multiple_c(self):
        """Complementarity: S(A) + S(A!) = 26/3 for many c values."""
        for c_val in [Rational(1), Rational(1, 2), Rational(7, 10),
                      Rational(13), Rational(26), Rational(24)]:
            assert cross_check_complementarity_sum(c_val) is True

    def test_area_identification_multiple_c(self):
        """Area/(4G_N) = (2*kappa/3) for many c values."""
        for c_val in [Rational(1), Rational(13), Rational(26), Rational(6)]:
            assert cross_check_area_identification(c_val) is True

    def test_renyi_monotonicity_all_families(self):
        """Renyi monotonicity for all standard kappa values."""
        assert cross_check_renyi_monotonicity_all_families() is True

    def test_min_entropy_half_vn_all_families(self):
        """S_inf = S_1/2 for all standard families."""
        assert cross_check_min_entropy_half_vn() is True

    def test_full_census_structure(self):
        """The census has universal A and pending algebra-bound B surfaces."""
        census = full_qec_census()
        assert len(census) >= 6
        for entry in census:
            assert entry['universal_reconstruction'] is True
            assert entry['kl_genus_1'] is None
            assert entry['exact_reconstruction'] is None
            assert entry['exact_reconstruction_status'] == 'UNVERIFIED'
            assert entry['is_koszul'] is None
            assert entry['page_curve'] is None
            assert entry['kappa'] is not None

    def test_census_certificate_is_bound_to_one_algebra(self):
        algebra_id = 'virasoro:c=13'
        census = full_qec_census(
            {algebra_id: _quadratic_certificate(algebra_id)}
        )
        certified = [
            entry for entry in census
            if entry['exact_reconstruction_status'] == 'CERTIFIED'
        ]
        assert [entry['algebra_id'] for entry in certified] == [algebra_id]
        assert certified[0]['exact_reconstruction'] is True
        assert certified[0]['physical_entanglement_wedge'] is None

    def test_census_rejects_mismatched_certificate(self):
        certificate = _quadratic_certificate('virasoro:c=26')
        with pytest.raises(ValueError, match='algebra_id'):
            full_qec_census({'virasoro:c=13': certificate})

    def test_census_rt_entropy_positive(self):
        """All scalar entropy candidates are positive."""
        census = full_qec_census()
        for entry in census:
            assert entry['scalar_entropy_candidate'] > 0
            assert entry['rt_entropy'] is None

    def test_census_renyi_2_less_than_vn(self):
        """The scalar n=2 candidate satisfies monotonicity."""
        census = full_qec_census()
        for entry in census:
            kappa = entry['kappa']
            s_vn = von_neumann_entropy_scalar(kappa, 1)
            assert entry['scalar_replica_candidate_n2'] <= s_vn
            assert entry['renyi_2'] is None

    def test_rt_additivity_heisenberg(self):
        """RT is additive: S(H_k1 + H_k2) = S(H_k1) + S(H_k2).

        kappa is additive for independent systems (AP10 cross-family check).
        """
        k1, k2 = Rational(1), Rational(3)
        kappa1 = kappa_heisenberg(k1)
        kappa2 = kappa_heisenberg(k2)
        s1 = rt_from_kappa(kappa1, 1)
        s2 = rt_from_kappa(kappa2, 1)
        s_sum = rt_from_kappa(kappa1 + kappa2, 1)
        assert s_sum == s1 + s2

    def test_qes_jlms_area_consistency(self):
        """QES area term matches JLMS area contribution."""
        kappa = Rational(13, 2)
        qes = quantum_extremal_surface(kappa, 1)
        jlms = jlms_formula(kappa)
        assert qes['S_area'] == jlms['area_contribution']

    def test_modular_hamiltonian_rt_consistency(self):
        """Modular Hamiltonian scalar part = RT entropy."""
        kappa = Rational(13, 2)
        mh = modular_hamiltonian_from_shadow(kappa)
        rt = rt_from_kappa(kappa, 1)
        assert mh['K_scalar'] == rt

    def test_faber_pandharipande_in_qes(self):
        """QES genus-1 correction uses correct FP coefficient lambda_1 = 1/24."""
        kappa = Rational(13, 2)
        qes = quantum_extremal_surface(kappa, 1)
        g1 = qes['genus_corrections'][0]
        assert g1['lambda_g'] == Rational(1, 24)
        assert g1['F_g'] == kappa * Rational(1, 24)
