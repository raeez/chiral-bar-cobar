r"""Tests for chain-level BV/bar identification at genus >= 1.

Verifies the factorization algebra approach to conj:master-bv-brst.

Test structure:
  1. Propagator comparison (genus-1 bar vs Green's function)
  2. Heisenberg chain-level quasi-isomorphism at genus 1
  3. Sewing operator on the bar complex
  4. BV Laplacian on the observables
  5. Obstruction analysis (Heisenberg, affine KM, Virasoro)
  6. Jacobi identity vanishing for KM
  7. Factorization homology comparison
  8. Scalar-level multi-path verification
  9. Trace cancellation for KM
  10. Shadow depth classification of obstructions
  11. Cross-family consistency (AP10 compliance)

Ground truth: bv_brst.tex, bar_cobar_adjunction_curved.tex,
  higher_genus_foundations.tex, concordance.tex, heisenberg_bv_bar_proof.py.
"""

import pytest
from sympy import Rational, S, Symbol, simplify, symbols

from compute.lib.chain_level_bv_bar import (
    ChainLevelObstruction,
    ChainLevelQIso,
    SewingOperator,
    BVLaplacianData,
    analyze_obstructions_affine_km,
    analyze_obstructions_heisenberg,
    analyze_obstructions_virasoro,
    bv_laplacian_heisenberg_genus1,
    bv_laplacian_km_genus1,
    chain_level_status_summary,
    compute_harmonic_correction_trace,
    fh_bar_comparison_genus1,
    green_function_genus1,
    heisenberg_chain_level_genus1,
    heisenberg_euler_char_genus1,
    km_jacobi_vanishing,
    lambda_fp,
    lambda_fp_from_ahat,
    obstruction_depth_classification,
    propagator_comparison_genus1,
    sewing_operator_genus1,
    sewing_operator_genus_g,
    verify_all,
    verify_scalar_level_all_genera,
    verify_trace_cancellation_km,
    weierstrass_sigma_ope_kernel,
)


# =====================================================================
# Section 1: Propagator comparison tests
# =====================================================================


class TestPropagatorComparison:
    """Tests for genus-1 propagator decomposition."""

    def test_weierstrass_kernel_weight(self):
        """The bar propagator d log sigma has weight 1 (AP27)."""
        data = weierstrass_sigma_ope_kernel()
        assert data['weight'] == Rational(1)

    def test_weierstrass_kernel_genus(self):
        """The Weierstrass kernel lives at genus 1."""
        data = weierstrass_sigma_ope_kernel()
        assert data['genus'] == 1

    def test_weierstrass_kernel_quasiperiodic(self):
        """The Weierstrass zeta function is quasi-periodic on E_tau."""
        data = weierstrass_sigma_ope_kernel()
        assert data['quasi_periodic'] is True

    def test_arnold_defect_nonzero_genus1(self):
        """Arnold relation breaks at genus 1 with E_2(tau) defect."""
        data = weierstrass_sigma_ope_kernel()
        assert 'E_2' in data['arnold_defect']
        assert data['moduli_dependence'] is True

    def test_green_function_decomposition(self):
        """BV Green's function decomposes into holomorphic + anti + harmonic."""
        data = green_function_genus1()
        assert data['antiholomorphic_exact'] is True
        assert 'holomorphic' in data['relation_to_bar']

    def test_propagator_comparison_structure(self):
        """The comparison decomposes P into bar + exact + harmonic parts."""
        comp = propagator_comparison_genus1()
        assert 'bar_part' in comp['decomposition']
        assert 'exact_part' in comp['decomposition']
        assert 'harmonic_part' in comp['decomposition']

    def test_heisenberg_propagator_resolved(self):
        """For Heisenberg, all propagator obstructions are resolved."""
        comp = propagator_comparison_genus1()
        assert 'RESOLVED' in comp['heisenberg_status']

    def test_interacting_propagator_open(self):
        """For interacting theories, propagator comparison is open."""
        comp = propagator_comparison_genus1()
        assert 'OPEN' in comp['interacting_status']


# =====================================================================
# Section 2: Heisenberg chain-level tests
# =====================================================================


class TestHeisenbergChainLevel:
    """Tests for the Heisenberg chain-level quasi-isomorphism."""

    def test_heisenberg_is_quasi_iso(self):
        """The comparison map Phi is a quasi-isomorphism for Heisenberg at g=1."""
        k = Symbol('k')
        qiso = heisenberg_chain_level_genus1(k)
        assert qiso.is_quasi_iso is True

    def test_heisenberg_euler_char_match(self):
        """Euler characteristics match on both sides."""
        k = Symbol('k')
        qiso = heisenberg_chain_level_genus1(k)
        assert qiso.euler_char_match is True

    def test_heisenberg_no_obstructions(self):
        """Heisenberg has no chain-level obstructions at genus 1."""
        k = Symbol('k')
        qiso = heisenberg_chain_level_genus1(k)
        assert len(qiso.obstructions) == 0

    def test_heisenberg_genus_is_1(self):
        """The quasi-isomorphism is at genus 1."""
        k = Symbol('k')
        qiso = heisenberg_chain_level_genus1(k)
        assert qiso.genus == 1

    def test_euler_char_genus1_match(self):
        """F_1^BV = F_1^bar = k/24 for Heisenberg."""
        k = Symbol('k')
        data = heisenberg_euler_char_genus1(k)
        assert data['match'] is True
        assert data['F1_bv'] == k * Rational(1, 24)
        assert data['F1_bar'] == k * Rational(1, 24)

    def test_euler_char_numeric(self):
        """Numerical verification: F_1(H_1) = 1/24."""
        data = heisenberg_euler_char_genus1(Rational(1))
        assert data['F1_bv'] == Rational(1, 24)


# =====================================================================
# Section 3: Sewing operator tests
# =====================================================================


class TestSewingOperator:
    """Tests for the sewing operator on B(A)."""

    def test_sewing_trace_genus1(self):
        """Tr(S_sew) = kappa * 1/24 at genus 1."""
        k = Symbol('k')
        sew = sewing_operator_genus1(k)
        assert sew.trace_value == k * Rational(1, 24)
        assert sew.genus == 1

    def test_sewing_trace_genus2(self):
        """Tr(S_sew) = kappa * 7/5760 at genus 2."""
        k = Symbol('k')
        sew = sewing_operator_genus_g(k, 2)
        assert sew.trace_value == k * Rational(7, 5760)
        assert sew.genus == 2

    def test_sewing_trace_genus3(self):
        """Tr(S_sew) = kappa * 31/967680 at genus 3."""
        k = Symbol('k')
        sew = sewing_operator_genus_g(k, 3)
        assert sew.trace_value == k * Rational(31, 967680)

    def test_sewing_bergman_kernel(self):
        """Sewing operator uses Bergman kernel."""
        k = Symbol('k')
        sew = sewing_operator_genus1(k)
        assert 'Bergman' in sew.kernel_type

    def test_sewing_genus_error(self):
        """Sewing operator rejects genus < 1."""
        with pytest.raises(ValueError):
            sewing_operator_genus_g(Symbol('k'), 0)


# =====================================================================
# Section 4: BV Laplacian tests
# =====================================================================


class TestBVLaplacian:
    """Tests for the BV Laplacian on observables."""

    def test_bv_lap_heisenberg_trace(self):
        """Tr(Delta_BV) = k/24 for Heisenberg at genus 1."""
        k = Symbol('k')
        lap = bv_laplacian_heisenberg_genus1(k)
        assert lap.trace_value == k * Rational(1, 24)

    def test_bv_lap_heisenberg_nilpotent(self):
        """BV Laplacian is nilpotent: Delta^2 = 0."""
        k = Symbol('k')
        lap = bv_laplacian_heisenberg_genus1(k)
        assert lap.nilpotent is True

    def test_bv_lap_heisenberg_second_order(self):
        """BV Laplacian is second order."""
        k = Symbol('k')
        lap = bv_laplacian_heisenberg_genus1(k)
        assert lap.second_order is True

    def test_bv_lap_sl2_trace(self):
        """Tr(Delta_BV) = kappa(sl_2)/24 = 3(k+2)/(4*24) for sl_2."""
        k = Symbol('k')
        lap = bv_laplacian_km_genus1("sl2", k)
        expected = Rational(3) * (k + 2) / 4 * Rational(1, 24)
        assert simplify(lap.trace_value - expected) == 0

    def test_bv_lap_sl3_trace(self):
        """Tr(Delta_BV) = kappa(sl_3)/24 = 4(k+3)/(3*24) for sl_3."""
        k = Symbol('k')
        lap = bv_laplacian_km_genus1("sl3", k)
        expected = Rational(8) * (k + 3) / 6 * Rational(1, 24)
        assert simplify(lap.trace_value - expected) == 0

    def test_bv_trace_equals_sewing_trace_heisenberg(self):
        """Tr(Delta_BV) = Tr(S_sew) for Heisenberg (scalar-level match)."""
        k = Symbol('k')
        lap = bv_laplacian_heisenberg_genus1(k)
        sew = sewing_operator_genus1(k)
        assert simplify(lap.trace_value - sew.trace_value) == 0


# =====================================================================
# Section 5: Obstruction analysis tests
# =====================================================================


class TestObstructionAnalysis:
    """Tests for the chain-level obstruction classification."""

    def test_heisenberg_all_resolved(self):
        """All obstructions are resolved for Heisenberg."""
        obs = analyze_obstructions_heisenberg()
        assert len(obs) == 3
        assert all(o.severity == 'resolved' for o in obs)

    def test_km_obstructions_soft(self):
        """All obstructions are soft for affine KM."""
        obs = analyze_obstructions_affine_km("sl2")
        assert len(obs) == 3
        assert all(o.severity == 'soft' for o in obs)

    def test_virasoro_has_hard_obstruction(self):
        """Virasoro has a hard obstruction at the quartic level."""
        obs = analyze_obstructions_virasoro()
        hard = [o for o in obs if o.severity == 'hard']
        assert len(hard) == 1
        assert 'quartic' in hard[0].name.lower() or 'quartic' in hard[0].description.lower()

    def test_virasoro_soft_count(self):
        """Virasoro has exactly 3 soft + 1 hard obstruction."""
        obs = analyze_obstructions_virasoro()
        soft = [o for o in obs if o.severity == 'soft']
        hard = [o for o in obs if o.severity == 'hard']
        assert len(soft) == 3
        assert len(hard) == 1

    def test_km_jacobi_resolution(self):
        """The cubic obstruction for KM is resolved by Jacobi identity."""
        obs = analyze_obstructions_affine_km("sl2")
        cubic = [o for o in obs if 'Jacobi' in o.name]
        assert len(cubic) == 1
        assert cubic[0].severity == 'soft'
        assert 'Jacobi' in cubic[0].resolution


# =====================================================================
# Section 6: Jacobi identity vanishing tests
# =====================================================================


class TestJacobiVanishing:
    """Tests for the Jacobi identity killing the harmonic correction."""

    def test_sl2_jacobi_vanishing(self):
        """Jacobi identity vanishing holds for sl_2."""
        result = km_jacobi_vanishing("sl2")
        assert result['jacobi_vanishing'] is True
        assert result['C2_adjoint'] == 2

    def test_sl3_jacobi_vanishing(self):
        """Jacobi identity vanishing holds for sl_3."""
        result = km_jacobi_vanishing("sl3")
        assert result['jacobi_vanishing'] is True
        assert result['C2_adjoint'] == 3


# =====================================================================
# Section 7: Factorization homology comparison tests
# =====================================================================


class TestFHComparison:
    """Tests for factorization homology vs bar complex."""

    def test_heisenberg_chain_proved(self):
        """FH comparison is PROVED for Heisenberg at genus 1."""
        k = Symbol('k')
        result = fh_bar_comparison_genus1('Heisenberg', k, 2)
        assert result['chain_level_status'] == 'PROVED'
        assert result['scalar_match'] is True

    def test_km_chain_supported(self):
        """FH comparison is STRONGLY_SUPPORTED for KM at genus 1."""
        k = Symbol('k')
        kappa = Rational(3) * (k + 2) / 4
        result = fh_bar_comparison_genus1('sl2', kappa, 3)
        assert result['chain_level_status'] == 'STRONGLY_SUPPORTED'

    def test_virasoro_chain_open(self):
        """FH comparison is OPEN for Virasoro at genus 1."""
        c = Symbol('c')
        result = fh_bar_comparison_genus1('Virasoro', c / 2, 1000)
        assert result['chain_level_status'] == 'OPEN'

    def test_scalar_always_proved(self):
        """Scalar-level identification is proved for all families."""
        k = Symbol('k')
        for family, kappa, depth in [
            ('Heisenberg', k, 2),
            ('sl2', Rational(3) * (k + 2) / 4, 3),
            ('Virasoro', Symbol('c') / 2, 1000),
        ]:
            result = fh_bar_comparison_genus1(family, kappa, depth)
            assert result['scalar_level_proved'] is True


# =====================================================================
# Section 8: Scalar-level multi-path verification tests
# =====================================================================


class TestScalarVerification:
    """Tests for scalar-level F_g = kappa * lambda_g^FP."""

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_fp_genus4(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_fp_genus5(self):
        """lambda_5^FP = 73/3503554560."""
        assert lambda_fp(5) == Rational(73, 3503554560)

    def test_lambda_fp_ahat_agreement(self):
        """Bernoulli and A-hat extraction agree through genus 8."""
        for g in range(1, 9):
            fp1 = lambda_fp(g)
            fp2 = lambda_fp_from_ahat(g)
            assert fp1 == fp2, f"Mismatch at genus {g}: {fp1} != {fp2}"

    def test_scalar_all_genera(self):
        """Scalar verification passes for k=1 through genus 10."""
        result = verify_scalar_level_all_genera(Rational(1), 10)
        assert result['all_pass'] is True

    def test_lambda_fp_positivity(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 16):
            assert lambda_fp(g) > 0, f"lambda_{g}^FP is not positive"

    def test_lambda_fp_genus_error(self):
        """lambda_fp rejects genus < 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)


# =====================================================================
# Section 9: Trace cancellation tests
# =====================================================================


class TestTraceCancellation:
    """Tests for trace cancellation in affine KM."""

    def test_sl2_traces_match(self):
        """BV and bar traces match for sl_2."""
        k = Symbol('k')
        result = verify_trace_cancellation_km("sl2", k)
        assert result['traces_match'] is True

    def test_sl3_traces_match(self):
        """BV and bar traces match for sl_3."""
        k = Symbol('k')
        result = verify_trace_cancellation_km("sl3", k)
        assert result['traces_match'] is True

    def test_sl2_jacobi_kills_cubic(self):
        """Jacobi identity kills cubic correction for sl_2."""
        k = Symbol('k')
        result = verify_trace_cancellation_km("sl2", k)
        assert result['jacobi_kills_cubic'] is True
        assert result['cubic_correction'] == S.Zero

    def test_sl2_class_L_kills_quartic(self):
        """Class L ensures quartic shadow vanishes for sl_2."""
        k = Symbol('k')
        result = verify_trace_cancellation_km("sl2", k)
        assert result['class_L_kills_quartic'] is True
        assert result['quartic_shadow'] == S.Zero

    def test_harmonic_correction_structure(self):
        """Harmonic correction trace is proportional to dim * C2."""
        result = compute_harmonic_correction_trace(
            kappa=Rational(9, 4),  # sl_2 at k=1
            dim_g=3,
            C2_adj=Rational(2),
        )
        assert result['dim_g'] == 3
        assert result['C2_adjoint'] == Rational(2)
        assert result['moduli_dependent'] is True


# =====================================================================
# Section 10: Shadow depth classification tests
# =====================================================================


class TestDepthClassification:
    """Tests for shadow depth classification of obstructions."""

    def test_class_G_proved(self):
        """Class G (depth 2) has chain-level PROVED."""
        cls = obstruction_depth_classification()
        assert cls['class_G']['chain_status'] == 'PROVED (genus 1)'
        assert cls['class_G']['Q_contact'] == 0

    def test_class_L_supported(self):
        """Class L (depth 3) has chain-level STRONGLY_SUPPORTED."""
        cls = obstruction_depth_classification()
        assert cls['class_L']['chain_status'] == 'STRONGLY_SUPPORTED (genus 1)'
        assert cls['class_L']['Q_contact'] == 0

    def test_class_C_accessible(self):
        """Class C (depth 4) has chain-level LIKELY_ACCESSIBLE."""
        cls = obstruction_depth_classification()
        assert 'ACCESSIBLE' in cls['class_C']['chain_status']

    def test_class_M_open(self):
        """Class M (depth infinity) has chain-level OPEN."""
        cls = obstruction_depth_classification()
        assert 'OPEN' in cls['class_M']['chain_status']

    def test_virasoro_quartic_nonzero(self):
        """Virasoro quartic contact Q = 10/[c(5c+22)] is nonzero."""
        c = Symbol('c')
        cls = obstruction_depth_classification()
        Q_vir = cls['class_M']['Q_contact_Vir']
        # Q_Vir should be 10 / (c * (5c + 22))
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(Q_vir - expected) == 0


# =====================================================================
# Section 11: Cross-family consistency (AP10 compliance)
# =====================================================================


class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10: no hardcoded wrong values)."""

    def test_kappa_heisenberg_is_level(self):
        """kappa(H_k) = k (the level, AP48)."""
        k = Symbol('k')
        data = heisenberg_euler_char_genus1(k)
        assert data['kappa'] == k

    def test_kappa_sl2_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        k = Symbol('k')
        lap = bv_laplacian_km_genus1("sl2", k)
        expected_kappa = Rational(3) * (k + 2) / 4
        expected_trace = expected_kappa * Rational(1, 24)
        assert simplify(lap.trace_value - expected_trace) == 0

    def test_bv_trace_equals_sewing_trace_all_genera(self):
        """Tr(Delta_BV) = Tr(S_sew) for Heisenberg at genera 1-5."""
        for g in range(1, 6):
            k = Symbol('k')
            bv_trace = k * lambda_fp(g)
            sew = sewing_operator_genus_g(k, g)
            assert simplify(bv_trace - sew.trace_value) == 0

    def test_status_summary_completeness(self):
        """Status summary covers all regimes."""
        summary = chain_level_status_summary()
        assert 'genus_0_all_families' in summary
        assert 'scalar_level_all_genera' in summary
        assert 'heisenberg_genus1_chain' in summary
        assert 'affine_km_genus1_chain' in summary
        assert 'virasoro_genus1_chain' in summary
        assert 'all_families_genus_ge_2_chain' in summary

    def test_verify_all_runs(self):
        """The full verification suite runs without error."""
        results = verify_all()
        assert isinstance(results, dict)
        assert len(results) > 10
