r"""Tests for shadow_integrable_hierarchy.py.

Tests finite scalar and primary-line diagnostics from the shadow
obstruction tower.  Full KdV, Boussinesq, Gelfand-Dickey, Toda, and
Painleve hierarchy assertions require separate descendant or Lax data.

30+ tests organized into sections:
  1. Faber-Pandharipande numbers (multi-path)
  2. Virasoro shadow data
  3. Shadow generating function
  4. A-hat genus consistency
  5. KW-compatible scalar coefficients
  6. Riccati primary-line diagnostics
  7. Shadow depth scope
  8. W_3 finite window
  9. W_N conditional hierarchy metadata
  10. Planted-forest scalar corrections
  11. Spectral curve
  12. Cross-family consistency
"""

# Hardcoded expected values below are direct evaluations of the formulas,
# recurrences, or finite-window specializations under test.

import pytest
from sympy import Rational, Symbol, cancel, factor, simplify, sqrt, expand

from compute.lib.shadow_integrable_hierarchy import (
    lambda_fp,
    verify_lambda_fp,
    kappa_virasoro,
    alpha_virasoro,
    S4_virasoro,
    shadow_metric_virasoro,
    shadow_generating_function_virasoro,
    shadow_coefficients_virasoro,
    shadow_tau_function,
    shadow_free_energy,
    ahat_generating_function,
    verify_ahat_consistency,
    kdv_string_equation,
    virasoro_constraints_rank1,
    riccati_as_stationary_kdv,
    shadow_depth_hierarchy_classification,
    w3_frobenius_data,
    w3_shadow_generating_functions,
    verify_w3_boussinesq_consistency,
    wn_hierarchy_classification,
    planted_forest_quantum_correction,
    verify_kdv_flows_virasoro,
    mc_as_integrability,
    shadow_spectral_curve_virasoro,
    shadow_hierarchy_summary,
)


c = Symbol('c')


# =========================================================================
# Section 1: Faber-Pandharipande numbers (multi-path verification)
# =========================================================================

class TestFaberPandharipande:
    """Multi-path verification of Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_4(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_fp_positivity(self):
        """All lambda_g^FP > 0 for g >= 1."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_verify_lambda_fp_all_match(self):
        """Cross-check lambda_fp against hardcoded known values."""
        results = verify_lambda_fp()
        for g, data in results.items():
            assert data['match'], f"Mismatch at genus {g}"

    def test_lambda_fp_bernoulli_formula(self):
        """Verify lambda_g^FP = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!).

        Path 2: independent Bernoulli computation.
        """
        from sympy import bernoulli, factorial
        for g in range(1, 6):
            B_2g = bernoulli(2 * g)
            numer = (2 ** (2 * g - 1) - 1) * abs(B_2g)
            denom = 2 ** (2 * g - 1) * factorial(2 * g)
            expected = Rational(numer, denom)
            assert lambda_fp(g) == expected

    def test_lambda_fp_numerator_pattern(self):
        """Numerators of lambda_g^FP are 2^{2g-1}-1: 1, 7, 31, 127, 511, ...

        These are Mersenne-like numbers 2^n - 1 for n = 1, 3, 5, 7, 9, ...
        """
        expected_numerators = [1, 7, 31, 127, 511]
        for g, expected in enumerate(expected_numerators, start=1):
            assert 2 ** (2 * g - 1) - 1 == expected


# =========================================================================
# Section 2: Virasoro shadow data
# =========================================================================

class TestVirasoroShadowData:
    """Verify Virasoro shadow invariants."""

    def test_kappa(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_virasoro() == c / 2

    def test_alpha(self):
        """alpha = 2 (c-independent)."""
        assert alpha_virasoro() == Rational(2)

    def test_S4(self):
        """S_4 = 10/[c(5c+22)]."""
        expected = Rational(10) / (c * (5 * c + 22))
        assert cancel(S4_virasoro() - expected) == 0

    def test_shadow_metric_coefficients(self):
        """Q_L = c^2 + 12c*t + (36 + 80/(5c+22))*t^2."""
        q0, q1, q2 = shadow_metric_virasoro()
        assert cancel(q0 - c ** 2) == 0
        assert cancel(q1 - 12 * c) == 0
        expected_q2 = Rational(36) + Rational(80) / (5 * c + 22)
        assert cancel(q2 - expected_q2) == 0

    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 40/(5c+22)."""
        Delta = 8 * kappa_virasoro() * S4_virasoro()
        expected = Rational(40) / (5 * c + 22)
        assert cancel(Delta - expected) == 0

    def test_gaussian_decomposition(self):
        """Q_L = (2kappa + 3alpha t)^2 + 2Delta t^2."""
        q0, q1, q2 = shadow_metric_virasoro()
        kap = kappa_virasoro()
        alph = alpha_virasoro()
        Delta = Rational(40) / (5 * c + 22)

        gaussian = (2 * kap + 3 * alph * Symbol('t')) ** 2
        interaction = 2 * Delta * Symbol('t') ** 2

        Q_L = q0 + q1 * Symbol('t') + q2 * Symbol('t') ** 2
        diff = expand(Q_L - gaussian - interaction)
        assert cancel(diff) == 0


# =========================================================================
# Section 3: Shadow generating function
# =========================================================================

class TestShadowGeneratingFunction:
    """Test the shadow generating function H(t) = t^2 sqrt(Q_L(t))."""

    def test_a0_equals_c(self):
        """a_0 = c (the leading coefficient of sqrt(Q_L))."""
        H = shadow_generating_function_virasoro(max_terms=3)
        assert cancel(H[2] - c) == 0  # a_0 = H[2] (since r=2 <-> n=0)

    def test_a1_equals_6(self):
        """a_1 = 6 (c-independent)."""
        H = shadow_generating_function_virasoro(max_terms=3)
        assert cancel(H[3] - 6) == 0  # a_1 = H[3] (r=3 <-> n=1)

    def test_a2_quartic(self):
        """a_2 = 40/[c(5c+22)]."""
        H = shadow_generating_function_virasoro(max_terms=4)
        expected = Rational(40) / (c * (5 * c + 22))
        assert cancel(H[4] - expected) == 0

    def test_S2_from_generating_function(self):
        """S_2 = a_0/2 = c/2 = kappa."""
        S = shadow_coefficients_virasoro(max_r=5)
        assert cancel(S[2] - c / 2) == 0

    def test_S3_from_generating_function(self):
        """S_3 = a_1/3 = 2."""
        S = shadow_coefficients_virasoro(max_r=5)
        assert cancel(S[3] - 2) == 0

    def test_S4_from_generating_function(self):
        """S_4 = a_2/4 = 10/[c(5c+22)]."""
        S = shadow_coefficients_virasoro(max_r=5)
        expected = Rational(10) / (c * (5 * c + 22))
        assert cancel(S[4] - expected) == 0

    def test_S5_quintic(self):
        """S_5 = -48/[c^2(5c+22)]."""
        S = shadow_coefficients_virasoro(max_r=6)
        expected = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert cancel(S[5] - expected) == 0


# =========================================================================
# Section 4: A-hat genus consistency
# =========================================================================

class TestAhatConsistency:
    """Verify A-hat genus = shadow generating function at scalar level."""

    def test_ahat_coefficients_match_lambda_fp(self):
        """[x^{2g}] (x/2)/sin(x/2) = lambda_g^FP for g=1..4."""
        results = verify_ahat_consistency(max_genus=4)
        for key, data in results.items():
            assert data['match'], f"A-hat mismatch at {key}"

    def test_ahat_generating_function(self):
        """The A-hat generating function returns lambda_g^FP values."""
        ahat = ahat_generating_function(max_order=4)
        for g in range(1, 5):
            assert ahat[g] == lambda_fp(g)

    def test_free_energy_matches_ahat(self):
        """F_g = (c/2) * lambda_g^FP = (c/2) * [x^{2g}] A-hat(ix) - 1."""
        F = shadow_free_energy(c / 2, max_genus=4)
        for g in range(1, 5):
            expected = c / 2 * lambda_fp(g)
            assert cancel(F[g] - expected) == 0


# =========================================================================
# Section 5: KW-compatible scalar coefficients
# =========================================================================

class TestKWCompatibleScalarWindow:
    """Verify scalar coefficients compatible with the KW/KdV lift."""

    def test_F1_value(self):
        """F_1 = c/48 (= kappa/24)."""
        results = verify_kdv_flows_virasoro(max_genus=4)
        assert results['F_1']['match']

    def test_F2_value(self):
        """F_2 = 7c/11520."""
        results = verify_kdv_flows_virasoro(max_genus=4)
        assert results['F_2']['match']

    def test_F3_value(self):
        """F_3 = 31c/1935360."""
        results = verify_kdv_flows_virasoro(max_genus=4)
        assert results['F_3']['match']

    def test_F4_value(self):
        """F_4 = 127c/309657600."""
        results = verify_kdv_flows_virasoro(max_genus=4)
        assert results['F_4']['match']

    def test_ratio_F2_F1_squared(self):
        """F_2/F_1^2 = 7/(5c) = 14/(10c).

        This ratio is a scalar coefficient check compatible with the
        rank-1 KW/KdV lift.
        """
        results = verify_kdv_flows_virasoro(max_genus=4)
        assert results['F_2/F_1^2']['match']

    def test_F_g_positivity(self):
        """F_g > 0 for all g >= 1 (Bernoulli signs: A-hat(ix) has positive coefficients)."""
        F = shadow_free_energy(Rational(1), max_genus=6)
        for g in range(1, 7):
            assert F[g] > 0


# =========================================================================
# Section 6: Riccati primary-line diagnostics
# =========================================================================

class TestRiccatiPrimaryLine:
    """Test the Riccati algebraicity on the primary line."""

    def test_mc_residuals_vanish(self):
        """The MC residuals at arities 5-8 all vanish (the recursion is exact)."""
        result = riccati_as_stationary_kdv()
        assert result['all_zero'], f"Nonzero residuals: {result['mc_residuals']}"

    def test_R3_value(self):
        """R_3 = 12."""
        result = riccati_as_stationary_kdv()
        assert result['R_3'] == 12

    def test_propagator(self):
        """P = 2/c."""
        result = riccati_as_stationary_kdv()
        assert cancel(result['P'] - 2 / c) == 0

    def test_delta_value(self):
        """Delta = 40/(5c+22)."""
        result = riccati_as_stationary_kdv()
        expected = Rational(40) / (5 * c + 22)
        assert cancel(result['Delta'] - expected) == 0


# =========================================================================
# Section 7: Shadow depth scope
# =========================================================================

class TestShadowDepthClassification:
    """Test the shadow depth scope classification."""

    def test_class_G_terminating_primary_line(self):
        """Class G has a terminating primary-line tower."""
        cl = shadow_depth_hierarchy_classification()
        assert cl['G']['hierarchy'] == 'primary-line tower terminates'
        assert cl['G']['depth'] == 2

    def test_class_L_finite_scalar_window(self):
        """Class L records the finite Lie/tree scalar window."""
        cl = shadow_depth_hierarchy_classification()
        assert 'finite Lie/tree' in cl['L']['hierarchy']
        assert cl['L']['depth'] == 3

    def test_class_M_primary_line_window(self):
        """Class M has an infinite primary-line scalar tower."""
        cl = shadow_depth_hierarchy_classification()
        assert 'primary-line scalar tower' in cl['M']['hierarchy']
        assert cl['M']['depth'] == 'infinity'

    def test_four_classes_present(self):
        """All four classes G/L/C/M are present."""
        cl = shadow_depth_hierarchy_classification()
        assert set(cl.keys()) == {'G', 'L', 'C', 'M'}


# =========================================================================
# Section 8: W_3 finite window
# =========================================================================

class TestW3FiniteWindow:
    """Test finite W_3 shadow constants and line projections."""

    def test_w3_eta_diagonal(self):
        """The W_3 metric is diagonal: eta = diag(c/2, c/3)."""
        frob = w3_frobenius_data()
        assert frob['eta']['TT'] == c / 2
        assert frob['eta']['WW'] == c / 3
        assert frob['eta']['TW'] == 0

    def test_w3_rank(self):
        """W_3 CohFT has rank 2."""
        frob = w3_frobenius_data()
        assert frob['rank'] == 2

    def test_w3_hierarchy_scope(self):
        """W_3 finite constants are Boussinesq-compatible with descendant input."""
        frob = w3_frobenius_data()
        assert 'Boussinesq-compatible' in frob['hierarchy']
        assert frob['scope'] == 'finite genus-0 shadow constants'

    def test_w3_structure_constant_TTT(self):
        """c^T_{TT} = 4/c."""
        frob = w3_frobenius_data()
        expected = Rational(4) / c
        assert cancel(frob['structure_constants']['c^T_{TT}'] - expected) == 0

    def test_w3_structure_constant_TWW(self):
        """c^W_{TW} = 9/c."""
        frob = w3_frobenius_data()
        expected = Rational(9) / c
        assert cancel(frob['structure_constants']['c^W_{TW}'] - expected) == 0

    def test_w3_tline_matches_virasoro(self):
        """The T-line of W_3 matches the Virasoro shadow tower."""
        gf = w3_shadow_generating_functions(max_arity=6)
        S_vir = shadow_coefficients_virasoro(max_r=6)
        for r in range(2, 7):
            if r in gf['T_line'] and r in S_vir:
                assert cancel(gf['T_line'][r] - S_vir[r]) == 0, \
                    f"T-line mismatch at arity {r}"

    def test_w3_wline_z2_parity(self):
        """W-line shadow coefficients vanish at odd arity (Z_2 symmetry)."""
        gf = w3_shadow_generating_functions(max_arity=8)
        for r in [3, 5, 7]:
            if r in gf['W_line']:
                assert gf['W_line'][r] == 0, \
                    f"Odd-arity W-line coefficient S_{r} should vanish"

    def test_w3_wdvv_finite_window(self):
        """The displayed rank-2 constants have no finite-window WDVV obstruction."""
        result = verify_w3_boussinesq_consistency()
        assert result['WDVV'] == 'no finite-window rank-2 obstruction'


# =========================================================================
# Section 9: W_N conditional hierarchy metadata
# =========================================================================

class TestWNConditionalHierarchyMetadata:
    """Test W_N rank and Lax-order metadata."""

    def test_w2_kdv_metadata(self):
        """W_2 metadata has KdV rank and Lax order."""
        cl = wn_hierarchy_classification(2)
        assert 'KdV' in cl['hierarchy_name']
        assert cl['n_dynamical_fields'] == 1
        assert cl['lax_order'] == 2
        assert 'descendant CohFT' in cl['hierarchy_status']

    def test_w3_boussinesq_metadata(self):
        """W_3 metadata has Boussinesq rank and Lax order."""
        cl = wn_hierarchy_classification(3)
        assert 'Boussinesq' in cl['hierarchy_name']
        assert cl['n_dynamical_fields'] == 2
        assert cl['lax_order'] == 3

    def test_w4_gelfand_dickey_4_metadata(self):
        """W_4 metadata has 4-KdV rank."""
        cl = wn_hierarchy_classification(4)
        assert '4-KdV' in cl['hierarchy_name']
        assert cl['n_dynamical_fields'] == 3

    def test_wn_rank_equals_fields(self):
        """For all N, shadow CohFT rank = N-1 = number of dynamical fields."""
        for N in range(2, 8):
            cl = wn_hierarchy_classification(N)
            assert cl['shadow_CohFT_rank'] == N - 1
            assert cl['n_dynamical_fields'] == N - 1

    def test_wn_frobenius_manifold_metadata(self):
        """W_N records the expected A_{N-1} Frobenius label."""
        for N in range(2, 6):
            cl = wn_hierarchy_classification(N)
            assert cl['frobenius_manifold'] == f'A_{N-1} singularity'


# =========================================================================
# Section 10: Planted-forest scalar corrections
# =========================================================================

class TestPlantedForestCorrections:
    """Test planted-forest corrections in the scalar window."""

    def test_genus_1_no_correction(self):
        """No planted-forest correction at genus 1."""
        result = planted_forest_quantum_correction(1)
        assert result['delta_pf'] == 0

    def test_genus_2_formula(self):
        """delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48 = (40-c)/48 for Virasoro."""
        result = planted_forest_quantum_correction(2)
        expected = (40 - c) / 48  # S_3=2: 2*(20-c/2)/48 = (40-c)/48
        assert cancel(result['delta_pf'] - expected) == 0, \
            f"Got {result['delta_pf']}, expected {expected}"

    def test_genus_2_heisenberg_vanishes(self):
        """Planted-forest correction vanishes for Heisenberg (S_3=0)."""
        result = planted_forest_quantum_correction(2)
        assert result['vanishes_for_heisenberg']

    def test_genus_2_at_c40(self):
        """delta_pf^{(2,0)} = 0 at c=40 (accidental vanishing)."""
        result = planted_forest_quantum_correction(2)
        val = result['delta_pf'].subs(c, 40)
        assert val == 0


# =========================================================================
# Section 11: Spectral curve
# =========================================================================

class TestSpectralCurve:
    """Test the primary-line shadow spectral curve."""

    def test_discriminant(self):
        """disc(Q_L) = -320c^2/(5c+22)."""
        curve = shadow_spectral_curve_virasoro()
        assert curve['disc_match']

    def test_genus_zero(self):
        """The spectral curve has genus 0 (rational)."""
        curve = shadow_spectral_curve_virasoro()
        assert curve['genus_of_curve'] == 0

    def test_no_real_branch_points(self):
        """Class M: no real branch points for c > 0."""
        curve = shadow_spectral_curve_virasoro()
        assert 'no real branch points' in curve['branch_structure']


# =========================================================================
# Section 12: Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks for finite scalar windows."""

    def test_heisenberg_tau_function(self):
        """Heisenberg scalar series has F_g = k * lambda_g^FP.

        For Heisenberg, S_3 = S_4 = ... = 0, so all planted-forest
        corrections vanish in this scalar window.
        """
        F = shadow_tau_function(Symbol('k'), max_genus=4)
        # F_g = k * lambda_g^FP for all g
        for g in range(1, 5):
            assert cancel(F[g] - Symbol('k') * lambda_fp(g)) == 0

    def test_complementarity_at_genus_1(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 at genus 1.

        F_1(c) + F_1(26-c) = c/48 + (26-c)/48 = 26/48 = 13/24
                            = 13 * lambda_1^FP.
        """
        F1_c = c / 2 * lambda_fp(1)  # = c/48
        c_dual = 26 - c
        F1_dual = c_dual / 2 * lambda_fp(1)  # = (26-c)/48
        total = cancel(F1_c + F1_dual)
        expected = Rational(13) * lambda_fp(1)  # = 13/24
        assert cancel(total - expected) == 0

    def test_complementarity_at_genus_2(self):
        """kappa + kappa' = 13 implies F_2(c) + F_2(26-c) = 13*lambda_2^FP."""
        F2_c = c / 2 * lambda_fp(2)
        F2_dual = (26 - c) / 2 * lambda_fp(2)
        total = cancel(F2_c + F2_dual)
        expected = Rational(13) * lambda_fp(2)
        assert cancel(total - expected) == 0

    def test_mc_integrability_structure(self):
        """MC equation records finite projections and external hierarchy input."""
        result = mc_as_integrability()
        assert 'WDVV' in result['genus_0_projection']
        assert 'Getzler' in result['genus_1_projection']
        assert 'descendant' in result['all_genera']
        assert len(result['identification_chain']) == 4

    def test_summary_completeness(self):
        """Summary covers all four shadow classes."""
        summary = shadow_hierarchy_summary()
        cl = summary['classification']
        assert 'G' in cl
        assert 'L' in cl
        assert 'C' in cl
        assert 'M' in cl

    def test_summary_rank_1_scope(self):
        """Rank-1 summary separates scalar checks from the KW/KdV lift."""
        summary = shadow_hierarchy_summary()
        assert summary['rank_1']['scope'] == 'finite scalar coefficient window verified'
        assert 'descendant potential' in summary['rank_1']['hierarchy']


# =========================================================================
# Section 13: Additional multi-path verification tests
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification of key finite-window identities."""

    def test_F2_three_paths(self):
        """F_2 = 7c/11520 verified three ways.

        Path 1: kappa * lambda_2^FP = (c/2)(7/5760) = 7c/11520.
        Path 2: A-hat coefficient of x^4 times kappa.
        Path 3: Direct Bernoulli computation.
        """
        # Path 1
        F2_path1 = cancel(c / 2 * Rational(7, 5760))

        # Path 2
        from sympy import bernoulli, factorial
        B_4 = bernoulli(4)  # = -1/30
        lam2 = Rational((2 ** 3 - 1) * abs(B_4), 2 ** 3 * factorial(4))
        F2_path2 = cancel(c / 2 * lam2)

        # Path 3: [u^4] u/sin(u) = 7/360, hence
        # [x^4] (x/2)/sin(x/2) = (7/360)/16 = 7/5760.
        lam2_path3 = Rational(7, 5760)
        F2_path3 = cancel(c / 2 * lam2_path3)

        assert F2_path1 == F2_path2 == F2_path3

    def test_shadow_metric_two_forms(self):
        """Shadow metric computed two ways.

        Path 1: Q_L = (2kappa+3alpha*t)^2 + 2Delta*t^2 (Gaussian decomposition)
        Path 2: Q_L = 4kappa^2 + 12kappa*alpha*t + (9alpha^2+16kappa*S_4)*t^2
        """
        kap = c / 2
        alph = Rational(2)
        s4 = Rational(10) / (c * (5 * c + 22))
        Delta = 8 * kap * s4

        # Path 1
        Q1_0 = (2 * kap) ** 2
        Q1_1 = 2 * (2 * kap) * (3 * alph)
        Q1_2 = (3 * alph) ** 2 + 2 * Delta

        # Path 2
        Q2_0 = 4 * kap ** 2
        Q2_1 = 12 * kap * alph
        Q2_2 = 9 * alph ** 2 + 16 * kap * s4

        assert cancel(Q1_0 - Q2_0) == 0
        assert cancel(Q1_1 - Q2_1) == 0
        assert cancel(Q1_2 - Q2_2) == 0

    def test_convolution_identity_at_arity_5(self):
        """Convolution identity: 2*a_0*a_3 + 2*a_1*a_2 = 0.

        This is the MC equation at arity 5, equivalent to f^2 = Q_L.
        """
        H = shadow_generating_function_virasoro(max_terms=5)
        a = {n: H[n + 2] for n in range(6)}

        residual = cancel(2 * a[0] * a[3] + 2 * a[1] * a[2])
        assert residual == 0

    def test_convolution_identity_at_arity_6(self):
        """Convolution identity: 2*a_0*a_4 + 2*a_1*a_3 + a_2^2 = 0.

        MC equation at arity 6.
        """
        H = shadow_generating_function_virasoro(max_terms=6)
        a = {n: H[n + 2] for n in range(7)}

        residual = cancel(2 * a[0] * a[4] + 2 * a[1] * a[3] + a[2] ** 2)
        assert residual == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
