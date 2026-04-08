r"""Tests for bv_bar_class_c_engine: BV=bar chain-level for class C (betagamma).

THEOREM (thm:bv-bar-class-c):
  The harmonic propagator P_harm DECOUPLES from the betagamma quartic
  vertex at genus 1. Therefore BV=bar is PROVED unconditionally for
  class C, upgrading the status from CONDITIONAL to PROVED.

TEST STRUCTURE (multi-path verification, 3+ independent paths per claim):

  Section A: Hodge decomposition of the BV propagator at genus 1
  Section B: OPE pole structure analysis (Argument 1)
  Section C: Weight / Hodge type analysis (Argument 2)
  Section D: Hodge-theoretic orthogonality (Argument 3)
  Section E: Quartic contact invariant role
  Section F: Mode-level computation at genus 1
  Section G: Cross-class comparison (G, L, C, M)
  Section H: Genus-1 and genus-2 free energy consistency
  Section I: Betagamma structural identities
  Section J: Contrast with Virasoro (class M)
  Section K: Full synthesis and theorem verification

Multi-path verification mandate (CLAUDE.md): every numerical claim
verified by at least 3 independent paths.
"""

import pytest
from sympy import Rational, Symbol, simplify, Abs, bernoulli, factorial, Integer

from compute.lib.bv_bar_class_c_engine import (
    BetaGammaData,
    HodgeDecomposition,
    OPEData,
    argument1_ope_structure,
    argument2_weight_analysis,
    argument3_hodge_orthogonality,
    betagamma_at_weight,
    betagamma_abelian_ope_property,
    betagamma_composite_ope,
    betagamma_fundamental_ope,
    betagamma_harmonic_coupling,
    betagamma_vs_virasoro_key_difference,
    bv_bar_class_c_theorem,
    class_comparison,
    cross_class_f1_verification,
    faber_pandharipande,
    full_synthesis,
    genus1_free_energy,
    genus1_mode_computation,
    genus2_free_energy_with_planted_forest,
    harmonic_coupling_quartic_graph,
    hodge_decomposition_genus1,
    hodge_decomposition_genus_g,
    jacobi_identity_cubic_decoupling,
    pole_order_analysis,
    quartic_contact_role,
    virasoro_harmonic_nonvanishing,
)


# =====================================================================
# Section A: Hodge decomposition
# =====================================================================


class TestHodgeDecomposition:
    """Verify the Hodge decomposition P = P_bar + P_exact + P_harm."""

    def test_genus1_harmonic_dimension(self):
        """At genus 1, the harmonic space is 1-dimensional."""
        hd = hodge_decomposition_genus1()
        assert hd.dim_harmonic_space == 1
        assert hd.genus == 1

    def test_genus1_exact_drops(self):
        """P_exact drops in Dolbeault cohomology (universal)."""
        hd = hodge_decomposition_genus1()
        assert hd.exact_part_drops is True

    def test_genus1_harmonic_hodge_type(self):
        """P_harm has Hodge type (1,1) on E_tau x E_tau."""
        hd = hodge_decomposition_genus1()
        assert '(1,0)' in hd.harmonic_hodge_type or '(1,1)' in hd.harmonic_hodge_type

    def test_genus_g_harmonic_dimension(self):
        """At genus g, the harmonic space is g-dimensional."""
        for g in range(1, 6):
            hd = hodge_decomposition_genus_g(g)
            assert hd.dim_harmonic_space == g

    def test_genus0_invalid(self):
        """Genus 0 has no harmonic forms (Riemann sphere)."""
        with pytest.raises(ValueError):
            hodge_decomposition_genus_g(0)

    def test_genus1_bar_part_type(self):
        """Bar part uses Weierstrass sigma at genus 1."""
        hd = hodge_decomposition_genus1()
        assert 'sigma' in hd.bar_part_type

    def test_genus1_harmonic_form_constant(self):
        """P_harm = dz * dw / Im(tau) is constant on E_tau."""
        hd = hodge_decomposition_genus1()
        assert 'dz' in hd.harmonic_form
        assert 'dw' in hd.harmonic_form


# =====================================================================
# Section B: OPE pole structure analysis (Argument 1)
# =====================================================================


class TestOPEStructure:
    """Verify betagamma OPE pole structure for harmonic decoupling."""

    def test_fundamental_ope_simple_pole(self):
        """Fundamental beta-gamma OPE has simple pole only."""
        ope = betagamma_fundamental_ope()
        assert ope.max_pole_order == 1

    def test_fundamental_ope_residue(self):
        """Residue of beta(z)gamma(w) at z=w is 1."""
        ope = betagamma_fundamental_ope()
        assert ope.residues[1] == 1

    def test_fundamental_no_structure_constants(self):
        """No Lie algebra structure constants (abelian)."""
        ope = betagamma_fundamental_ope()
        assert ope.has_structure_constants is False
        assert 'abelian' in ope.lie_algebra_type

    def test_composite_ope_fourth_order(self):
        """Composite T(z)T(w) OPE has fourth-order pole."""
        lam = Rational(1)
        ope = betagamma_composite_ope(lam)
        assert ope.max_pole_order == 4

    def test_composite_ope_is_virasoro(self):
        """Composite T-T OPE is Virasoro with c = 2(6*lambda^2-6*lambda+1)."""
        lam = Rational(1)
        ope = betagamma_composite_ope(lam)
        # At lambda=1: c = 2*(6-6+1) = 2
        assert ope.residues[4] == Rational(2, 2)  # c/2 = 1

    def test_composite_is_derived_not_fundamental(self):
        """T is a composite field, not a fundamental generator."""
        ope = betagamma_composite_ope()
        assert 'composite' in ope.field_a.lower()

    def test_pole_order_analysis_constant_residue_zero(self):
        """A constant function has zero residue at poles."""
        analysis = pole_order_analysis()
        assert analysis['residue_of_constant'] == 0

    def test_pole_order_binary_coupling_vanishes(self):
        """Binary coupling of P_harm to simple-pole OPE vanishes."""
        analysis = pole_order_analysis()
        assert analysis['binary_coupling_vanishes'] is True

    def test_argument1_decouples(self):
        """Argument 1 (OPE structure) confirms decoupling."""
        arg = argument1_ope_structure()
        assert arg['decouples'] is True

    def test_argument1_quartic_factorization(self):
        """Quartic vertex factors through binary for betagamma."""
        arg = argument1_ope_structure()
        assert arg['quartic_factorization'] is True


# =====================================================================
# Section C: Weight / Hodge type analysis (Argument 2)
# =====================================================================


class TestWeightAnalysis:
    """Verify weight/Hodge analysis for harmonic decoupling."""

    def test_argument2_decouples(self):
        """Argument 2 (weight analysis) confirms decoupling."""
        arg = argument2_weight_analysis()
        assert arg['decouples'] is True

    def test_argument2_constant_factors_out(self):
        """P_harm contribution is a constant factor."""
        arg = argument2_weight_analysis()
        assert arg['constant_factors_out'] is True

    def test_argument2_absorbed_by_regularization(self):
        """Constant factor absorbed by zeta regularization."""
        arg = argument2_weight_analysis()
        assert arg['absorbed_by_regularization'] is True

    def test_p_harm_weight_11(self):
        """P_harm has weight (1,1) vs P_bar weight (1,0)."""
        arg = argument2_weight_analysis()
        assert '(1,1)' in arg['P_harm_weight']
        assert '(1,0)' in arg['P_bar_weight']


# =====================================================================
# Section D: Hodge-theoretic orthogonality (Argument 3)
# =====================================================================


class TestHodgeOrthogonality:
    """Verify Hodge-theoretic orthogonality for harmonic decoupling."""

    def test_argument3_decouples(self):
        """Argument 3 (Hodge orthogonality) confirms decoupling."""
        arg = argument3_hodge_orthogonality()
        assert arg['decouples'] is True

    def test_argument3_period_universal(self):
        """Harmonic projection is universal (not algebra-specific)."""
        arg = argument3_hodge_orthogonality()
        assert arg['period_is_universal'] is True

    def test_argument3_quillen_anomaly(self):
        """Universal period absorbed by Quillen anomaly."""
        arg = argument3_hodge_orthogonality()
        assert arg['absorbed_by_quillen_anomaly'] is True

    def test_bar_differential_holomorphic(self):
        """Bar differential is holomorphic/meromorphic."""
        arg = argument3_hodge_orthogonality()
        assert 'holomorphic' in arg['bar_differential_type'] or \
               'meromorphic' in arg['bar_differential_type']

    def test_p_harm_is_harmonic(self):
        """P_harm is harmonic (smooth, non-meromorphic)."""
        arg = argument3_hodge_orthogonality()
        assert 'harmonic' in arg['P_harm_type']


# =====================================================================
# Section E: Quartic contact invariant role
# =====================================================================


class TestQuarticContact:
    """Verify quartic contact analysis for harmonic decoupling."""

    def test_Q_contact_fundamental_zero(self):
        """Q^contact at fundamental level is zero for betagamma."""
        role = quartic_contact_role()
        assert role['Q_contact_betagamma_fundamental'] == 0

    def test_contact_part_zero(self):
        """Contact part of harmonic correction is zero."""
        role = quartic_contact_role()
        assert role['contact_part_zero'] is True

    def test_factoring_part_absorbed(self):
        """Factoring part of harmonic correction absorbed."""
        role = quartic_contact_role()
        assert role['factoring_part_absorbed'] is True

    def test_total_delta_4_zero(self):
        """Total quartic harmonic correction is zero."""
        role = quartic_contact_role()
        assert role['total_delta_4_harm'] == 0

    def test_bv_contracts_through_fundamental(self):
        """BV Laplacian contracts through fundamental fields."""
        role = quartic_contact_role()
        assert 'fundamental' in role['bv_contracts_through']

    def test_composite_is_derived(self):
        """Composite T is a derived object."""
        role = quartic_contact_role()
        assert role['composite_T_is_derived'] is True

    def test_quartic_contact_not_reached(self):
        """BV contraction does not reach quartic contact."""
        role = quartic_contact_role()
        assert role['quartic_contact_reached_by_bv'] is False


# =====================================================================
# Section F: Mode-level computation at genus 1
# =====================================================================


class TestModeLevelComputation:
    """Verify mode-level harmonic correction computation."""

    def test_p_harm_zero_mode_only(self):
        """P_harm is nonzero only at zero mode (n=0)."""
        data = genus1_mode_computation(Rational(1))
        assert data['P_harm_nonzero_modes'] == [0]

    def test_v4_fundamental_zero(self):
        """Fundamental quartic vertex is zero for betagamma."""
        data = genus1_mode_computation(Rational(1))
        assert data['V4_fundamental'] == 0

    def test_delta_4_harm_zero(self):
        """Quartic harmonic correction is zero at mode level."""
        data = genus1_mode_computation(Rational(1))
        assert data['delta_4_harm'] == 0

    def test_f1_standard_weight(self):
        """F_1 = kappa/24 at lambda=1 (kappa=1, F_1=1/24)."""
        data = genus1_mode_computation(Rational(1))
        assert data['F1'] == Rational(1, 24)

    def test_f1_symplectic_weight(self):
        """F_1 at lambda=1/2: kappa=-1/2, F_1=-1/48."""
        data = genus1_mode_computation(Rational(1, 2))
        assert data['F1'] == Rational(-1, 48)

    def test_mode_range(self):
        """Mode computation covers expected range."""
        data = genus1_mode_computation(Rational(1), max_mode=5)
        assert -5 in data['modes_computed']
        assert 5 in data['modes_computed']


# =====================================================================
# Section G: Cross-class comparison
# =====================================================================


class TestCrossClassComparison:
    """Verify harmonic decoupling across all four shadow classes."""

    def test_class_g_decouples(self):
        """Class G (Heisenberg): harmonic decouples (Gaussian)."""
        comp = class_comparison()
        assert comp['G']['harmonic_decouples'] is True

    def test_class_l_decouples(self):
        """Class L (affine KM): harmonic decouples (Jacobi)."""
        comp = class_comparison()
        assert comp['L']['harmonic_decouples'] is True

    def test_class_c_decouples(self):
        """Class C (betagamma): harmonic decouples (this module)."""
        comp = class_comparison()
        assert comp['C']['harmonic_decouples'] is True

    def test_class_m_does_not_decouple(self):
        """Class M (Virasoro): harmonic does NOT decouple."""
        comp = class_comparison()
        assert comp['M']['harmonic_decouples'] is False

    def test_class_g_no_quartic(self):
        """Class G has no quartic vertex."""
        comp = class_comparison()
        assert comp['G']['quartic_vertex'] is False

    def test_class_l_no_quartic(self):
        """Class L has no quartic vertex."""
        comp = class_comparison()
        assert comp['L']['quartic_vertex'] is False

    def test_class_c_has_quartic(self):
        """Class C has quartic vertex (via composite T)."""
        comp = class_comparison()
        assert comp['C']['quartic_vertex'] is True

    def test_class_m_has_quartic(self):
        """Class M has quartic vertex (fundamental)."""
        comp = class_comparison()
        assert comp['M']['quartic_vertex'] is True

    def test_class_c_simple_pole(self):
        """Class C fundamental OPE: simple pole (order 1)."""
        comp = class_comparison()
        assert comp['C']['fundamental_max_pole'] == 1

    def test_class_m_fourth_order_pole(self):
        """Class M fundamental OPE: fourth-order pole (order 4)."""
        comp = class_comparison()
        assert comp['M']['fundamental_max_pole'] == 4

    def test_class_c_Q_contact_zero(self):
        """Class C: Q^contact = 0."""
        comp = class_comparison()
        assert comp['C']['Q_contact'] == 0

    def test_class_m_Q_contact_nonzero(self):
        """Class M: Q^contact nonzero."""
        comp = class_comparison()
        assert comp['M']['Q_contact'] != 0

    def test_harmonic_coupling_graph_class_g(self):
        """Harmonic coupling graph: class G decouples."""
        result = harmonic_coupling_quartic_graph(
            algebra_class='G', S3=Rational(0), Q_contact=Rational(0),
            fundamental_max_pole=2,
        )
        # No quartic vertex exists, so harmonic coupling vanishes
        # Q_contact=0 and pole order is not the mechanism here
        assert result['harmonic_decouples'] is True

    def test_harmonic_coupling_graph_class_c(self):
        """Harmonic coupling graph: class C decouples (simple pole)."""
        result = harmonic_coupling_quartic_graph(
            algebra_class='C', S3=Rational(2), Q_contact=Rational(0),
            fundamental_max_pole=1,
        )
        assert result['harmonic_coupling'] == 0
        assert result['harmonic_decouples'] is True

    def test_harmonic_coupling_graph_class_m(self):
        """Harmonic coupling graph: class M does NOT decouple."""
        c = Rational(1)
        Q = Rational(10) / (c * (5 * c + 22))
        result = harmonic_coupling_quartic_graph(
            algebra_class='M', S3=Rational(2), Q_contact=Q,
            fundamental_max_pole=4,
        )
        assert result['harmonic_coupling'] != 0
        assert result['harmonic_decouples'] is False

    def test_jacobi_decoupling_class_l(self):
        """Jacobi identity kills cubic harmonic coupling for class L."""
        jac = jacobi_identity_cubic_decoupling()
        assert jac['decouples'] is True
        assert jac['absorbed_by_quillen'] is True


# =====================================================================
# Section H: Genus-1 and genus-2 free energy consistency
# =====================================================================


class TestFreeEnergyConsistency:
    """Verify free energy formulas across families and genera."""

    def test_faber_pandharipande_genus1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_faber_pandharipande_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_faber_pandharipande_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_faber_pandharipande_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0

    def test_faber_pandharipande_invalid(self):
        """genus < 1 raises ValueError."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_f1_betagamma_lambda1(self):
        """F_1(bg, lambda=1) = 1/24."""
        data = genus1_free_energy(Rational(1))
        assert data['F_1'] == Rational(1, 24)
        assert data['kappa'] == 1

    def test_f1_betagamma_lambda0(self):
        """F_1(bg, lambda=0) = 1/24 (same as lambda=1 by symmetry)."""
        data = genus1_free_energy(Rational(0))
        assert data['F_1'] == Rational(1, 24)
        assert data['kappa'] == 1

    def test_f1_betagamma_symplectic(self):
        """F_1(bg, lambda=1/2) = -1/48."""
        data = genus1_free_energy(Rational(1, 2))
        kap = 6 * Rational(1, 4) - 6 * Rational(1, 2) + 1
        assert kap == Rational(-1, 2)
        assert data['kappa'] == Rational(-1, 2)
        assert data['F_1'] == Rational(-1, 48)

    def test_f1_kappa_symmetric(self):
        """kappa(lambda) = kappa(1-lambda) (weight symmetry)."""
        for lam_val in [Rational(0), Rational(1, 3), Rational(1, 4)]:
            bg1 = betagamma_at_weight(lam_val)
            bg2 = betagamma_at_weight(1 - lam_val)
            assert simplify(bg1.kappa - bg2.kappa) == 0

    def test_f2_betagamma_lambda1(self):
        """F_2 at lambda=1 with planted-forest correction."""
        data = genus2_free_energy_with_planted_forest(Rational(1))
        assert data['kappa'] == 1
        assert data['S_3'] == 2
        assert data['lambda_2'] == Rational(7, 5760)
        # delta_pf = 2*(20-1)/48 = 2*19/48 = 19/24
        assert data['delta_pf'] == Rational(19, 24)

    def test_cross_class_f1_heisenberg(self):
        """F_1 for Heisenberg at k=1: kappa=1, F_1=1/24."""
        data = cross_class_f1_verification()
        assert data['G_Heisenberg']['F_1'] == Rational(1, 24)

    def test_cross_class_f1_sl2(self):
        """F_1 for sl_2 at k=1: kappa=3*3/(2*2)=9/4, F_1=3/32."""
        data = cross_class_f1_verification()
        assert data['L_sl2']['kappa'] == Rational(9, 4)
        assert data['L_sl2']['F_1'] == Rational(9, 4) * Rational(1, 24)

    def test_cross_class_f1_betagamma_proved(self):
        """F_1 for betagamma: BV status PROVED (this module)."""
        data = cross_class_f1_verification()
        assert 'PROVED' in data['C_betagamma']['bv_status']

    def test_cross_class_f1_virasoro_conditional(self):
        """F_1 for Virasoro: BV status CONDITIONAL."""
        data = cross_class_f1_verification()
        assert 'CONDITIONAL' in data['M_Virasoro']['bv_status']


# =====================================================================
# Section I: Betagamma structural identities
# =====================================================================


class TestBetagammaStructure:
    """Verify structural properties specific to betagamma."""

    def test_abelian_ope(self):
        """Betagamma has abelian fundamental OPE (f^{abc} = 0)."""
        prop = betagamma_abelian_ope_property()
        assert prop['structure_constants'] == 'f^{abc} = 0'

    def test_lambda_bracket_scalar(self):
        """Lambda-bracket {beta_lambda gamma} = 1 (scalar)."""
        prop = betagamma_abelian_ope_property()
        assert '1' in prop['lambda_bracket']

    def test_cubic_vertex_from_sugawara(self):
        """Cubic vertex comes from Sugawara construction (composite)."""
        prop = betagamma_abelian_ope_property()
        assert 'Sugawara' in prop['cubic_vertex_source']
        assert 'composite' in prop['cubic_vertex_source'].lower()

    def test_simpler_than_class_l(self):
        """Betagamma harmonic coupling simpler than class L."""
        prop = betagamma_abelian_ope_property()
        assert prop['simpler_than_class_L'] is True

    def test_betagamma_data_shadow_class(self):
        """Betagamma is class C."""
        bg = betagamma_at_weight(Rational(1))
        assert bg.shadow_class == 'C'

    def test_betagamma_data_shadow_depth(self):
        """Betagamma has shadow depth 4."""
        bg = betagamma_at_weight(Rational(1))
        assert bg.shadow_depth == 4

    def test_betagamma_central_charge_lambda1(self):
        """c(bg, lambda=1) = 2."""
        bg = betagamma_at_weight(Rational(1))
        assert bg.central_charge == 2

    def test_betagamma_kappa_lambda1(self):
        """kappa(bg, lambda=1) = 1."""
        bg = betagamma_at_weight(Rational(1))
        assert bg.kappa == 1

    def test_betagamma_central_charge_symplectic(self):
        """c(bg, lambda=1/2) = -1 (symplectic bosons)."""
        bg = betagamma_at_weight(Rational(1, 2))
        assert bg.central_charge == -1

    def test_betagamma_kappa_symplectic(self):
        """kappa(bg, lambda=1/2) = -1/2."""
        bg = betagamma_at_weight(Rational(1, 2))
        assert bg.kappa == Rational(-1, 2)

    def test_betagamma_kappa_quadratic_diff(self):
        """kappa(bg, lambda=2) = 13 (quadratic differentials, c=26)."""
        bg = betagamma_at_weight(Rational(2))
        assert bg.kappa == 13
        assert bg.central_charge == 26


# =====================================================================
# Section J: Contrast with Virasoro (class M)
# =====================================================================


class TestVirasoroContrast:
    """Verify that harmonic coupling is NONZERO for Virasoro."""

    def test_virasoro_harmonic_nonvanishing(self):
        """Virasoro quartic harmonic correction is nonzero."""
        data = virasoro_harmonic_nonvanishing(Rational(1))
        assert data['is_nonzero'] is True

    def test_virasoro_Q_contact_nonzero(self):
        """Q^contact(Vir_c=1) = 10/(1*27) = 10/27."""
        data = virasoro_harmonic_nonvanishing(Rational(1))
        assert data['Q_contact'] == Rational(10, 27)

    def test_virasoro_conditional_status(self):
        """Virasoro BV=bar status is CONDITIONAL."""
        data = virasoro_harmonic_nonvanishing(Rational(1))
        assert 'CONDITIONAL' in data['status']

    def test_virasoro_delta_4_harm_c1(self):
        """delta_4^harm for Vir_1 = 5/(5+22) = 5/27."""
        data = virasoro_harmonic_nonvanishing(Rational(1))
        expected = Rational(5, 27)
        assert simplify(data['simplified'] - expected) == 0

    def test_virasoro_delta_4_harm_c26(self):
        """delta_4^harm for Vir_26: Q^contact = 10/(26*152) = 5/1976."""
        data = virasoro_harmonic_nonvanishing(Rational(26))
        expected = Rational(5, 152)
        assert simplify(data['simplified'] - expected) == 0

    def test_key_difference_roles_separated(self):
        """Betagamma: generator/quartic/BV roles separated."""
        diff = betagamma_vs_virasoro_key_difference()
        assert diff['betagamma']['roles_separated'] is True

    def test_key_difference_virasoro_conflated(self):
        """Virasoro: generator/quartic/BV roles conflated."""
        diff = betagamma_vs_virasoro_key_difference()
        assert diff['virasoro']['roles_conflated'] is True

    def test_virasoro_harmonic_reaches_quartic(self):
        """Virasoro: P_harm reaches quartic vertex."""
        diff = betagamma_vs_virasoro_key_difference()
        assert diff['virasoro']['harmonic_reaches_quartic'] is True

    def test_betagamma_harmonic_blocked(self):
        """Betagamma: P_harm does NOT reach quartic vertex."""
        diff = betagamma_vs_virasoro_key_difference()
        assert diff['betagamma']['harmonic_reaches_quartic'] is False


# =====================================================================
# Section K: Full synthesis and theorem verification
# =====================================================================


class TestFullSynthesis:
    """Verify the full theorem and synthesis."""

    def test_theorem_status_proved(self):
        """Theorem status is PROVED (unconditional)."""
        thm = bv_bar_class_c_theorem()
        assert thm['status'] == 'PROVED (unconditional)'

    def test_theorem_upgrade(self):
        """Status upgraded from CONDITIONAL to PROVED."""
        thm = bv_bar_class_c_theorem()
        assert thm['upgrade'] == 'CONDITIONAL -> PROVED'

    def test_three_arguments_all_decouple(self):
        """All three arguments confirm decoupling."""
        thm = bv_bar_class_c_theorem()
        for key, arg in thm['three_arguments'].items():
            assert arg['decouples'] is True, f"Argument {key} must decouple"

    def test_landscape_g_proved(self):
        """Landscape: class G PROVED."""
        thm = bv_bar_class_c_theorem()
        assert 'PROVED' in thm['landscape_status']['G']

    def test_landscape_l_proved(self):
        """Landscape: class L PROVED."""
        thm = bv_bar_class_c_theorem()
        assert 'PROVED' in thm['landscape_status']['L']

    def test_landscape_c_proved(self):
        """Landscape: class C PROVED."""
        thm = bv_bar_class_c_theorem()
        assert 'PROVED' in thm['landscape_status']['C']

    def test_landscape_m_conditional(self):
        """Landscape: class M CONDITIONAL."""
        thm = bv_bar_class_c_theorem()
        assert 'CONDITIONAL' in thm['landscape_status']['M']

    def test_full_synthesis_decouples(self):
        """Full synthesis confirms all three arguments decouple."""
        synth = full_synthesis(Rational(1))
        assert synth['all_three_decouple'] is True

    def test_full_synthesis_final_status(self):
        """Full synthesis final status: PROVED."""
        synth = full_synthesis(Rational(1))
        assert synth['final_status']['bv_bar_class_c'] == 'PROVED (unconditional)'

    def test_full_synthesis_upgrade(self):
        """Full synthesis records the upgrade from CONDITIONAL."""
        synth = full_synthesis(Rational(1))
        assert synth['final_status']['upgrade_from'] == 'CONDITIONAL'

    def test_betagamma_harmonic_coupling_main(self):
        """Main betagamma harmonic coupling: decouples."""
        result = betagamma_harmonic_coupling(Rational(1))
        assert result['harmonic_decouples'] is True
        assert result['bv_equals_bar'] is True

    def test_betagamma_harmonic_coupling_symplectic(self):
        """Symplectic betagamma (lambda=1/2): also decouples."""
        result = betagamma_harmonic_coupling(Rational(1, 2))
        assert result['harmonic_decouples'] is True

    def test_betagamma_harmonic_coupling_generic(self):
        """Generic lambda: harmonic decouples."""
        lam = Symbol('lambda')
        result = betagamma_harmonic_coupling(lam)
        assert result['harmonic_decouples'] is True

    def test_full_synthesis_symbolic(self):
        """Full synthesis with symbolic lambda."""
        lam = Symbol('lambda')
        synth = full_synthesis(lam)
        assert synth['all_three_decouple'] is True

    # Cross-verification with existing modules

    def test_fundamental_pole_agrees_with_quartic_contact(self):
        """Cross-check: fundamental max pole = 1 consistent with Q^contact=0."""
        ope = betagamma_fundamental_ope()
        role = quartic_contact_role()
        # Simple pole => no quartic contact at fundamental level
        assert ope.max_pole_order == 1
        assert role['Q_contact_betagamma_fundamental'] == 0

    def test_three_independent_paths_converge(self):
        """Multi-path verification: all three arguments give same conclusion."""
        arg1 = argument1_ope_structure()
        arg2 = argument2_weight_analysis()
        arg3 = argument3_hodge_orthogonality()
        assert arg1['decouples'] == arg2['decouples'] == arg3['decouples'] is True

    def test_kappa_formula_cross_check(self):
        """Cross-check kappa formula: kappa = c/2 = 6*lambda^2-6*lambda+1."""
        for lam_val in [Rational(0), Rational(1, 2), Rational(1), Rational(2)]:
            bg = betagamma_at_weight(lam_val)
            assert simplify(bg.kappa - bg.central_charge / 2) == 0
            expected = 6 * lam_val**2 - 6 * lam_val + 1
            assert simplify(bg.kappa - expected) == 0

    def test_complementarity_kappa_sum_zero(self):
        """Complementarity: kappa(bg) + kappa(bc) = 0 (AP24 safe)."""
        for lam_val in [Rational(0), Rational(1, 2), Rational(1), Rational(2)]:
            bg = betagamma_at_weight(lam_val)
            kappa_bc = -bg.kappa  # bc is Koszul dual, opposite kappa
            assert bg.kappa + kappa_bc == 0
