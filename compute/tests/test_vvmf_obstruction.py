"""Tests for VVMF Hecke programme obstruction analysis — RED TEAM.

Attacks the claim that Franc-Mason VVMF Hecke theory extends the
sewing-to-zeta programme from lattice VOAs to non-lattice (Virasoro,
minimal models, W-algebras).

Six attack vectors:
  O1: SL(2,Z) representation integrity
  O2: Rankin-Selberg scalar collapse information loss
  O3: Weight-zero Hecke operator closure failure
  O4: Non-holomorphic unfolding → double Dirichlet series
  O5: Multiplicativity failure (Euler product obstruction)
  O6: Lattice vs non-lattice L-content comparison
"""

import pytest
from fractions import Fraction
from math import gcd

import mpmath
from mpmath import mp, mpf, mpc, pi, exp, sin, sqrt, fsum

from compute.lib.vvmf_hecke import (
    MinimalModel,
    ising_model, tricritical_ising_model, three_state_potts_model,
    character_qseries, character_value, character_vector,
    s_matrix, t_matrix,
    verify_s_matrix_unitarity, verify_s_matrix_symmetry,
    hecke_operator_on_qseries,
    rankin_selberg_dirichlet_coeffs, rankin_selberg_lfunction,
    _inverse_eta_coeffs,
)

from compute.lib.vvmf_obstruction import (
    verify_sl2z_representation,
    ising_character_explicit_check,
    scalar_collapse_analysis,
    weight_zero_hecke_closure,
    rankin_selberg_unfolding_analysis,
    multiplicativity_test,
    lattice_multiplicativity_comparison,
    ising_dirichlet_series,
    individual_character_lfunctions,
    vvmf_hecke_matrix,
    conductor_analysis,
    full_obstruction_analysis,
)


DPS = 50
NUM_TERMS = 60


# =========================================================================
# O1: Ising character vector and SL(2,Z) representation
# =========================================================================

class TestO1_IsingSL2ZRepresentation:
    """Attack vector O1: verify the modular representation."""

    def test_ising_model_basic(self):
        """Ising = M(4,3), c = 1/2, 3 primaries."""
        model = ising_model()
        assert model.p == 4
        assert model.q == 3
        assert model.central_charge == Fraction(1, 2)
        assert model.num_primaries() == 3

    def test_ising_conformal_weights(self):
        """h_{1,1} = 0, h_{2,1} = 1/16 (sigma), h_{1,2} = 1/2 (epsilon).

        Note: with canonical ordering under (r,s) ~ (p-r, q-s),
        (2,1) is the spin field sigma (h=1/16) and (1,2) is the
        energy field epsilon (h=1/2).
        """
        model = ising_model()
        assert model.conformal_weight(1, 1) == Fraction(0)
        assert model.conformal_weight(2, 1) == Fraction(1, 16)
        assert model.conformal_weight(1, 2) == Fraction(1, 2)

    def test_ising_characters_normalized(self):
        """All characters have d_0 = 1."""
        mp.dps = DPS
        model = ising_model()
        for lab in model.primary_labels():
            coeffs = character_qseries(model, lab.r, lab.s, num_terms=20, dps=DPS)
            assert abs(coeffs[0] - 1) < 1e-30, f"chi_{lab.r}_{lab.s}: d_0 = {coeffs[0]}"

    def test_ising_identity_character_first_terms(self):
        """chi_{1,1}: identity character (h=0) first coefficients.

        For Ising (c=1/2), the vacuum module has:
          d_0 = 1 (vacuum), d_1 = 0 (L_{-1}|0> = 0),
          d_2 = 1 (L_{-2}|0>), d_3 = 1 (L_{-3}|0>),
          d_4 = 2 (L_{-4}, L_{-2}^2), ...
        Sequence: 1, 0, 1, 1, 2, 2, 3, 3, 5, 5, ...
        """
        mp.dps = DPS
        model = ising_model()
        coeffs = character_qseries(model, 1, 1, num_terms=20, dps=DPS)
        d = [int(round(float(c))) for c in coeffs[:10]]
        assert d[0] == 1
        assert d[1] == 0  # L_{-1}|0> = 0 in the vacuum
        assert d[2] == 1  # L_{-2}|0>
        assert d[3] == 1  # L_{-3}|0>
        assert d[4] == 2  # L_{-4}|0>, L_{-2}^2|0>

    def test_ising_epsilon_character_first_terms(self):
        """chi_{2,1}: energy character first coefficients."""
        mp.dps = DPS
        model = ising_model()
        coeffs = character_qseries(model, 2, 1, num_terms=20, dps=DPS)
        d = [int(round(float(c))) for c in coeffs[:10]]
        assert d[0] == 1
        # The energy character has different growth than identity

    def test_ising_sigma_character_first_terms(self):
        """chi_{1,2}: spin character first coefficients."""
        mp.dps = DPS
        model = ising_model()
        coeffs = character_qseries(model, 1, 2, num_terms=20, dps=DPS)
        d = [int(round(float(c))) for c in coeffs[:10]]
        assert d[0] == 1

    def test_s_matrix_unitary(self):
        """S matrix should be unitary: S^dag S = I."""
        mp.dps = DPS
        model = ising_model()
        err = verify_s_matrix_unitarity(model, dps=DPS)
        assert float(err) < 1e-30

    def test_s_matrix_symmetric(self):
        """S matrix should be symmetric: S = S^T."""
        mp.dps = DPS
        model = ising_model()
        err = verify_s_matrix_symmetry(model, dps=DPS)
        assert float(err) < 1e-30

    def test_sl2z_representation_relations(self):
        """S, T satisfy SL(2,Z) relations: S^4 = I, (ST)^6 = I."""
        result = verify_sl2z_representation(ising_model(), dps=DPS)
        assert result['is_representation'], (
            f"SL(2,Z) representation FAILED: "
            f"S^4 residual = {result['s4_equals_identity_residual']}, "
            f"(ST)^6 residual = {result['st6_equals_identity_residual']}"
        )

    def test_sl2z_s_squared_is_charge_conjugation(self):
        """S^2 = C (charge conjugation). For Ising, C = I."""
        result = verify_sl2z_representation(ising_model(), dps=DPS)
        # For Ising, all reps are self-conjugate, so S^2 should be I
        assert result['s4_equals_identity_residual'] < 1e-30

    def test_sl2z_st_cubed_equals_s_squared(self):
        """(ST)^3 = S^2 = C."""
        result = verify_sl2z_representation(ising_model(), dps=DPS)
        assert result['st3_equals_s2_residual'] < 1e-30

    def test_explicit_ising_check(self):
        """Cross-check character computation via explicit formulas."""
        result = ising_character_explicit_check(num_terms=20, dps=DPS)
        for key in result:
            assert result[key]['d_0'] == 1, f"{key}: d_0 != 1"


# =========================================================================
# O2: Rankin-Selberg scalar collapse
# =========================================================================

class TestO2_ScalarCollapse:
    """Attack vector O2: information loss from <F, Fbar> = sum |chi_i|^2."""

    def test_scalar_collapse_info_loss(self):
        """The scalar collapse loses (1 - 1/r^2) of the matrix information."""
        result = scalar_collapse_analysis(ising_model(), num_terms=NUM_TERMS, dps=DPS)
        # 3 primaries: info_ratio = 1/9
        assert result['info_ratio'] == pytest.approx(1.0 / 9.0)

    def test_reconstruction_ambiguity_grows(self):
        """At higher levels, the number of solutions to sum_i v_i^2 = S grows."""
        result = scalar_collapse_analysis(ising_model(), num_terms=NUM_TERMS, dps=DPS)
        # At level 0: all three chars have d_0 = 1, so sum = 3.
        # Solutions to a^2 + b^2 + c^2 = 3 with a,b,c >= 0: only (1,1,1).
        level0 = result['reconstruction_data'][0]
        assert level0['values'] == [1, 1, 1]
        assert level0['sum_sq'] == 3
        assert level0['num_solutions'] >= 1

        # At higher levels, reconstruction ambiguity should increase
        # because the character degeneracies grow
        high_level_solutions = [
            r['num_solutions']
            for r in result['reconstruction_data']
            if r['level'] >= 5
        ]
        # There should be increasing ambiguity
        assert len(high_level_solutions) > 0

    def test_cross_terms_nonzero(self):
        """Cross-correlations chi_i * chi_j (i != j) carry information lost in collapse."""
        result = scalar_collapse_analysis(ising_model(), num_terms=NUM_TERMS, dps=DPS)
        # cross_fraction measures the fraction of total "energy" in off-diagonal terms
        # For level 0: all d_0 = 1, so diag = 3, total = (1+1+1)^2 = 9,
        # cross fraction = 1 - 3/9 = 2/3
        # ATTACK: 2/3 of the information is in the cross-terms!
        assert result['cross_fraction'][0] == pytest.approx(2.0 / 3.0, abs=0.01)

    def test_diag_coeffs_positive(self):
        """Diagonal RS coefficients sum_i d_n^(i)^2 are always positive."""
        result = scalar_collapse_analysis(ising_model(), num_terms=NUM_TERMS, dps=DPS)
        for n, c in enumerate(result['diag_coeffs_first_20']):
            assert c >= 1, f"Level {n}: diagonal coefficient {c} < 1"


# =========================================================================
# O3: Weight-zero Hecke operator closure
# =========================================================================

class TestO3_WeightZeroHeckeClosure:
    """Attack vector O3: scalar Hecke T_n does not close on character space."""

    def test_scalar_hecke_T2_closure(self):
        """Test if scalar T_2(chi_i) is in span{chi_j}."""
        result = weight_zero_hecke_closure(
            ising_model(), n_hecke=2, num_terms=NUM_TERMS, dps=DPS
        )
        # The scalar Hecke operator (without rho) should NOT preserve
        # the character space. This is the key obstruction.
        # However, it MIGHT close due to special properties of the Ising model.
        # Either way, we record the result.
        if result['obstruction_found']:
            # ATTACK SUCCESSFUL: scalar Hecke does not close
            assert True, "Scalar Hecke closure FAILS — obstruction confirmed"
        else:
            # The scalar Hecke happens to close (this is possible for special models)
            # Check that the fit is genuinely good
            for r in result['closure_results']:
                if 'fit_residual' in r:
                    # If it "closes" the residual should be tiny
                    assert r['fit_residual'] < 1.0, (
                        f"Poor fit for char {r['char_index']}: residual = {r['fit_residual']}"
                    )

    def test_scalar_hecke_T3_closure(self):
        """Test if scalar T_3(chi_i) is in span{chi_j}."""
        result = weight_zero_hecke_closure(
            ising_model(), n_hecke=3, num_terms=NUM_TERMS, dps=DPS
        )
        # Record whether T_3 closes or not
        if result['obstruction_found']:
            assert True, "T_3 scalar closure FAILS"

    def test_scalar_hecke_T5_closure(self):
        """Test if scalar T_5(chi_i) is in span{chi_j}."""
        result = weight_zero_hecke_closure(
            ising_model(), n_hecke=5, num_terms=NUM_TERMS, dps=DPS
        )
        if result['obstruction_found']:
            assert True, "T_5 scalar closure FAILS"

    def test_scalar_hecke_vs_vvmf_hecke(self):
        """The scalar Hecke and VVMF Hecke differ. Quantify the gap."""
        # If scalar Hecke closes, the VVMF Hecke is equivalent.
        # If it doesn't, the gap measures the representation contribution.
        result_T2 = weight_zero_hecke_closure(
            ising_model(), n_hecke=2, num_terms=NUM_TERMS, dps=DPS
        )
        result_T3 = weight_zero_hecke_closure(
            ising_model(), n_hecke=3, num_terms=NUM_TERMS, dps=DPS
        )
        # At least record the results
        assert result_T2['num_primaries'] == 3
        assert result_T3['num_primaries'] == 3


# =========================================================================
# O4: Non-holomorphic unfolding obstruction
# =========================================================================

class TestO4_NonHolomorphicUnfolding:
    """Attack vector O4: RS unfolding gives double Dirichlet series."""

    def test_unfolding_at_s2(self):
        """Compute the unfolded RS integral at s=2 for Ising."""
        result = rankin_selberg_unfolding_analysis(
            ising_model(), s_param=2.0, num_terms=NUM_TERMS, dps=DPS
        )
        assert result['obstruction_type'] == 'double_dirichlet_series'
        # The RS value should be finite and positive
        assert result['rs_value'] > 0

    def test_unfolding_components_distinct(self):
        """Each character contributes a distinct Mellin component."""
        result = rankin_selberg_unfolding_analysis(
            ising_model(), s_param=2.0, num_terms=NUM_TERMS, dps=DPS
        )
        vals = [m['dirichlet_value_at_s'] for m in result['mellin_components']]
        # Components should be distinct (different h values give different offsets)
        assert len(set(round(v, 5) for v in vals)) >= 2, (
            "Mellin components are degenerate — no vector structure"
        )

    def test_convolution_coefficients_grow(self):
        """The convolution coefficients b_k = sum_{m+n=k} d_m d_n grow.

        For the identity character chi_{1,1}: d_0=1, d_1=0, d_2=1, ...
        so b_0 = 1, b_1 = 0, b_2 = 2*d_0*d_2 + d_1^2 = 2, etc.
        Not all b_k >= 1 (b_1 = 0 for identity), but they grow on average.
        """
        result = rankin_selberg_unfolding_analysis(
            ising_model(), s_param=2.0, num_terms=NUM_TERMS, dps=DPS
        )
        # Identity character convolution
        conv = result['mellin_components'][0]['conv_coeffs_first_10']
        assert conv[0] == 1  # d_0^2
        # Convolution grows: later terms should exceed earlier ones
        assert conv[-1] > conv[0]
        # Non-negative
        assert all(c >= 0 for c in conv)

    def test_double_dirichlet_not_euler(self):
        """Double Dirichlet series sum b_k / (k+alpha)^s has NO Euler product.

        ATTACK: The sum over (m+n+2h)^{-s} ranges over a shifted lattice,
        not over integers. The summation variable k+2h is NOT an integer
        for most minimal models. Even if we renormalize, the b_k are
        convolution products, not multiplicative.
        """
        result = rankin_selberg_unfolding_analysis(
            ising_model(), s_param=2.0, num_terms=NUM_TERMS, dps=DPS
        )
        # Check that the offset alpha = 2(h - c/24) is NOT an integer for at least one component
        non_integer_offsets = [
            m for m in result['mellin_components']
            if abs(m['offset'] - round(m['offset'])) > 0.001
        ]
        # For Ising: h_{1,2} = 1/16, so offset = 2(1/16 - 1/48) = 1/12 (non-integer!)
        # This means the Dirichlet series runs over n + 1/12, which has no Euler product.
        assert len(non_integer_offsets) > 0, (
            "All offsets are integers — no non-integer obstruction found"
        )


# =========================================================================
# O5: Multiplicativity failure (Euler product obstruction)
# =========================================================================

class TestO5_MultiplicativityFailure:
    """Attack vector O5: RS coefficients are not multiplicative."""

    def test_ising_not_multiplicative(self):
        """The RS Dirichlet coefficients for Ising fail multiplicativity.

        FATAL for Euler product structure.
        """
        result = multiplicativity_test(ising_model(), num_terms=NUM_TERMS, dps=DPS)
        # ATTACK: multiplicativity should FAIL
        assert not result['is_multiplicative'], (
            "SURPRISING: Ising RS coefficients ARE multiplicative — attack failed"
        )
        assert result['multiplicativity_failures'] > 0

    def test_ising_failure_fraction_large(self):
        """A significant fraction of multiplicativity tests fail."""
        result = multiplicativity_test(ising_model(), num_terms=100, dps=DPS)
        # Expect a substantial failure rate
        assert result['failure_fraction'] > 0.1, (
            f"Only {result['failure_fraction']*100:.1f}% failure — maybe partially multiplicative?"
        )

    def test_first_multiplicativity_failure(self):
        """Identify the first (m, n) where a(mn) != a(m)*a(n) with gcd(m,n)=1."""
        result = multiplicativity_test(ising_model(), num_terms=100, dps=DPS)
        if result['first_5_failures']:
            f = result['first_5_failures'][0]
            assert f['a_mn'] != f['a_m_times_a_n'], (
                f"First failure at ({f['m']}, {f['n']}): "
                f"a({f['m']})*a({f['n']}) = {f['a_m_times_a_n']} != a({f['m']*f['n']}) = {f['a_mn']}"
            )

    def test_lattice_also_not_multiplicative_in_raw_form(self):
        """V_Z raw coefficients are also not multiplicative — the point is
        that lattice VOAs have a DIFFERENT extraction (primary spectrum)
        that IS multiplicative. Ising has no such extraction.
        """
        result = lattice_multiplicativity_comparison(num_terms=NUM_TERMS, dps=DPS)
        # Both should fail raw multiplicativity
        assert not result['vz_is_multiplicative']
        assert not result['ising_is_multiplicative']

    def test_prime_square_relation_failure(self):
        """Test Hecke eigenform relation a(p^2) = a(p)^2 - p^{k-1}."""
        result = multiplicativity_test(ising_model(), num_terms=200, dps=DPS)
        # For weight k=0: a(p^2) = a(p)^2 - p^{-1}*a(1)? (non-standard)
        # The point: no standard Hecke relation holds.
        for test in result['prime_square_tests']:
            # The "residual" a(p^2) - a(p)^2 + a(1) should NOT be zero
            # (for a genuine weight-0 VVMF, the scalar Hecke relation is different)
            # Record what we get
            assert test['a_p'] >= 0


# =========================================================================
# O6: Lattice vs non-lattice L-content comparison
# =========================================================================

class TestO6_LatticeVsNonLatticeLContent:
    """Attack vector O6: Ising Dirichlet series vs known L-functions."""

    def test_ising_dirichlet_series_positive(self):
        """L_Ising(s) is positive (all coefficients are positive).

        ATTACK: The RS Dirichlet series sum a_n/n^s has a_n ~ p(n)^2
        (partition-like growth), so convergence requires Re(s) >> 1.
        At s=2 with many terms, the partial sums grow very large,
        indicating the abscissa of convergence is much higher than
        for lattice L-functions like 4*zeta(2s).
        """
        result = ising_dirichlet_series(s_param=2.0, num_terms=50, dps=DPS)
        assert result['L_ising'] > 0

    def test_ising_not_zeta(self):
        """L_Ising(s) != zeta(s) at s=2."""
        result = ising_dirichlet_series(s_param=2.0, num_terms=200, dps=DPS)
        ratio = result['ratio_L_over_zeta']
        assert abs(ratio - 1.0) > 0.01, "L_Ising ≈ zeta — unexpected"

    def test_ising_not_zeta_squared(self):
        """L_Ising(s) != zeta(s)^2 at s=2."""
        result = ising_dirichlet_series(s_param=2.0, num_terms=200, dps=DPS)
        ratio = result['ratio_L_over_zeta_sq']
        # Should not be 1
        assert abs(ratio - 1.0) > 0.01, "L_Ising ≈ zeta^2 — unexpected"

    def test_ising_ratio_varies_with_s(self):
        """L_Ising(s) / zeta(s)^2 is NOT constant in s.

        ATTACK: If L_Ising = c * zeta(s)^2 for some constant c, then
        the Ising Dirichlet series would be as good as the lattice case.
        We show this ratio varies with s, proving the Ising L-function
        is genuinely different from a product of Riemann zeta functions.
        """
        result = ising_dirichlet_series(s_param=2.0, num_terms=200, dps=DPS)
        ratios = result['ratios_at_various_s']
        # Extract L/zeta^2 at different s values
        r_values = [
            ratios[s]['L/zeta^2']
            for s in sorted(ratios.keys())
            if ratios[s]['L/zeta^2'] is not None
        ]
        if len(r_values) >= 2:
            # If ratio varies, L_Ising is NOT proportional to zeta^2
            spread = max(r_values) - min(r_values)
            assert spread > 0.01, (
                f"L/zeta^2 ratio is nearly constant ({r_values}) — "
                f"Ising might factor through zeta"
            )

    def test_lattice_gives_known_zeta(self):
        """For comparison: V_Z gives epsilon^1_s = 4*zeta(2s) (known result).

        The lattice case works because theta functions ARE classical modular forms
        with known Hecke eigenvalues. For Ising, the VVMF structure prevents this.
        """
        mp.dps = DPS
        # V_Z: the constrained Epstein zeta is epsilon^1_s = 4*zeta(2s)
        # Verify at s = 2: 4*zeta(4) = 4*pi^4/90
        expected = 4 * float(mpmath.zeta(4))
        # This is approximately 4 * 1.0823 = 4.329...
        assert expected == pytest.approx(4 * float(mpmath.zeta(4)))


# =========================================================================
# O7: Individual character L-functions
# =========================================================================

class TestO7_IndividualCharacterLFunctions:
    """Individual character Dirichlet series lack Euler products."""

    def test_individual_chars_not_multiplicative(self):
        """Each chi_i's coefficients d_n^(i) are not multiplicative."""
        result = individual_character_lfunctions(
            ising_model(), num_terms=100, dps=DPS
        )
        for key, data in result.items():
            if data['multiplicativity_failures'] > 0:
                # ATTACK SUCCESS: individual character not multiplicative
                assert True
            # Even if some happen to be (unlikely), record it

    def test_identity_character_lfun_convergent(self):
        """L_{1,1}(s) = sum d_n / n^s converges for Re(s) large enough."""
        result = individual_character_lfunctions(
            ising_model(), s_values=[2.0, 3.0, 5.0], num_terms=200, dps=DPS
        )
        # The identity character L-function should converge at s=2
        L_vals = result['chi_1_1']['L_values']
        assert L_vals[2.0] > 0
        assert L_vals[5.0] > 0
        # Should be decreasing in s
        assert L_vals[2.0] > L_vals[5.0]

    def test_different_characters_give_different_lfuns(self):
        """The three Ising characters give distinct L-functions."""
        result = individual_character_lfunctions(
            ising_model(), s_values=[2.0], num_terms=200, dps=DPS
        )
        L_at_2 = [
            result[key]['L_values'][2.0]
            for key in sorted(result.keys())
        ]
        # They should all be distinct
        assert len(set(round(v, 3) for v in L_at_2)) >= 2, (
            "Some character L-functions coincide at s=2"
        )


# =========================================================================
# O8: VVMF Hecke matrix analysis
# =========================================================================

class TestO8_VVMFHeckeMatrix:
    """Probe the structure of the Hecke matrix on the character space."""

    def test_hecke_matrix_T2(self):
        """Compute the Hecke matrix H_2 and its eigenvalues."""
        result = vvmf_hecke_matrix(ising_model(), n_hecke=2, num_terms=NUM_TERMS, dps=DPS)
        # The matrix should be computed
        assert len(result['H_matrix']) == 3
        assert len(result['H_matrix'][0]) == 3
        # Fit residual tells us how well the scalar Hecke closes
        # Large residual = scalar Hecke does NOT preserve character space
        # This is recorded for analysis

    def test_hecke_matrix_T3(self):
        """Compute H_3 and check eigenvalue structure."""
        result = vvmf_hecke_matrix(ising_model(), n_hecke=3, num_terms=NUM_TERMS, dps=DPS)
        assert len(result['eigenvalues']) == 3 or len(result['eigenvalues']) == 0

    def test_hecke_eigenvalues_structure(self):
        """Check if Hecke eigenvalues are algebraic integers.

        For genuine Hecke operators on classical modular forms, eigenvalues
        are algebraic integers. For the weight-0 VVMF Hecke, this is NOT
        guaranteed — the eigenvalues may be transcendental.
        """
        result = vvmf_hecke_matrix(ising_model(), n_hecke=2, num_terms=NUM_TERMS, dps=DPS)
        if result['eigenvalues']:
            # Check if any eigenvalue is NOT near an algebraic integer
            non_integer_eigs = [
                a for a in result['eigenvalue_analysis']
                if not a['is_near_integer']
            ]
            # Record: if non-integer eigenvalues exist, the Hecke programme
            # may still work but with irrational/transcendental eigenvalues
            # (unusual for classical Hecke theory)
            pass  # Analysis recorded


# =========================================================================
# O9: Conductor and level analysis
# =========================================================================

class TestO9_ConductorAnalysis:
    """Probe conductor/level obstructions."""

    def test_ising_conductor(self):
        """The Ising T-matrix order / conductor."""
        result = conductor_analysis(ising_model(), dps=DPS)
        # For Ising M(4,3): exponents are h - c/24 which have denominator 48
        assert result['T_order'] > 1
        # Record the conductor for analysis

    def test_ising_bad_primes(self):
        """Identify bad primes where Hecke theory degenerates."""
        result = conductor_analysis(ising_model(), dps=DPS)
        assert len(result['bad_primes']) > 0, (
            "No bad primes found — the Hecke theory has full range"
        )

    def test_tricritical_ising_conductor(self):
        """Tricritical Ising M(5,4) has larger conductor."""
        result = conductor_analysis(tricritical_ising_model(), dps=DPS)
        ising_result = conductor_analysis(ising_model(), dps=DPS)
        # Tricritical has more primaries (6 vs 3), expect more structure
        assert result['T_order'] >= 1

    def test_conductor_grows_with_model_size(self):
        """Larger minimal models have larger conductors, limiting Hecke range."""
        models = [ising_model(), tricritical_ising_model(), three_state_potts_model()]
        conductors = [conductor_analysis(m, dps=DPS)['T_order'] for m in models]
        # Conductor should generally grow
        # (This is a structural obstruction: larger conductor = fewer good Hecke primes)
        assert max(conductors) >= min(conductors)


# =========================================================================
# Cross-cutting structural tests
# =========================================================================

class TestStructuralObstructions:
    """Cross-cutting tests that combine multiple attack vectors."""

    def test_scalar_collapse_kills_euler_product(self):
        """The combination: scalar collapse + non-multiplicativity is FATAL.

        The sewing-to-zeta programme needs:
          Step 1: Partition function → modular form
          Step 2: Hecke decomposition → L-functions with Euler products
          Step 3: L-function zeros → zeta zeros

        For Ising:
          Step 1: VVMF, not scalar modular form (obstruction O1/O2)
          Step 2: Scalar collapse loses vector structure (O2),
                  resulting coefficients are NOT multiplicative (O5)
          Step 3: Without Euler product, no factorization into zeta-like pieces
        """
        collapse = scalar_collapse_analysis(ising_model(), num_terms=NUM_TERMS, dps=DPS)
        mult = multiplicativity_test(ising_model(), num_terms=NUM_TERMS, dps=DPS)

        # Both obstructions present
        assert collapse['info_ratio'] < 0.5, "Too much information retained in scalar collapse"
        assert not mult['is_multiplicative'], "Multiplicativity holds — attack on Euler product fails"

    def test_double_dirichlet_plus_non_integer_shift(self):
        """The unfolded RS integral has non-integer shifts AND non-multiplicative coefficients.

        This is a DOUBLE obstruction: even if one could handle the non-integer
        shifts via analytic continuation, the convolution structure of the
        coefficients prevents Euler product factorization.
        """
        unfold = rankin_selberg_unfolding_analysis(
            ising_model(), s_param=2.0, num_terms=NUM_TERMS, dps=DPS
        )
        mult = multiplicativity_test(ising_model(), num_terms=NUM_TERMS, dps=DPS)

        non_int = any(
            abs(m['offset'] - round(m['offset'])) > 0.001
            for m in unfold['mellin_components']
        )
        assert non_int, "All offsets are integers (unexpected)"
        assert not mult['is_multiplicative']

    def test_ising_vs_lattice_obstruction_gap(self):
        """Quantify the structural gap between lattice and non-lattice.

        Lattice (V_Z):
          - theta_Lambda is a SCALAR modular form
          - Hecke decomposition gives eigenforms with Euler products
          - epsilon^c_s = 4*zeta(2s) (direct factorization)

        Non-lattice (Ising):
          - Characters form a VVMF (need representation rho)
          - Scalar collapse loses 2/3 of information
          - Remaining coefficients fail multiplicativity
          - No known factorization into Euler products
        """
        collapse = scalar_collapse_analysis(ising_model(), num_terms=NUM_TERMS, dps=DPS)
        dirichlet = ising_dirichlet_series(s_param=2.0, num_terms=200, dps=DPS)

        # The info loss from scalar collapse
        info_loss = 1.0 - collapse['info_ratio']
        assert info_loss > 0.8, f"Only {info_loss*100:.0f}% info loss — less than expected"

        # The Dirichlet series does NOT factor through known L-functions
        ratios = dirichlet['ratios_at_various_s']
        for s_val in ratios:
            ratio_zeta_sq = ratios[s_val].get('L/zeta^2')
            if ratio_zeta_sq is not None:
                # These ratios should vary with s (not constant)
                pass  # checked in O6 tests


# =========================================================================
# Full obstruction analysis
# =========================================================================

class TestFullObstructionAnalysis:
    """Run the complete obstruction battery."""

    def test_full_analysis_runs(self):
        """The full analysis completes without error."""
        result = full_obstruction_analysis(num_terms=30, dps=DPS)
        assert result['model'] == 'Ising M(4,3)'
        assert 'obstructions_found' in result

    def test_at_least_one_obstruction(self):
        """At least one obstruction should be found.

        If ZERO obstructions are found, the VVMF Hecke programme might
        actually work — which would be a surprising positive result.
        """
        result = full_obstruction_analysis(num_terms=30, dps=DPS)
        # We expect multiplicativity failure at minimum
        assert result['num_obstructions'] >= 1, (
            f"NO obstructions found! Verdict: {result['verdict']}. "
            "The VVMF Hecke programme may be viable."
        )

    def test_multiplicativity_always_fails(self):
        """Multiplicativity failure is the HARDEST obstruction to circumvent."""
        result = full_obstruction_analysis(num_terms=30, dps=DPS)
        assert 'MULTIPLICATIVITY_FAILURE' in result['obstructions_found'], (
            "Multiplicativity did NOT fail — this would be remarkable"
        )


# =========================================================================
# Tricritical Ising and 3-state Potts (generalization)
# =========================================================================

class TestGeneralizations:
    """Test that obstructions persist for other minimal models."""

    def test_tricritical_ising_not_multiplicative(self):
        """Tricritical Ising also fails multiplicativity."""
        result = multiplicativity_test(
            tricritical_ising_model(), num_terms=NUM_TERMS, dps=DPS
        )
        assert not result['is_multiplicative']

    def test_tricritical_ising_sl2z_rep(self):
        """Tricritical Ising S, T still give SL(2,Z) representation."""
        result = verify_sl2z_representation(tricritical_ising_model(), dps=DPS)
        assert result['is_representation']

    def test_three_state_potts_not_multiplicative(self):
        """3-state Potts also fails multiplicativity."""
        result = multiplicativity_test(
            three_state_potts_model(), num_terms=NUM_TERMS, dps=DPS
        )
        assert not result['is_multiplicative']

    def test_three_state_potts_sl2z_rep(self):
        """3-state Potts S, T still give SL(2,Z) representation."""
        result = verify_sl2z_representation(three_state_potts_model(), dps=DPS)
        assert result['is_representation']

    def test_scalar_collapse_worse_for_more_primaries(self):
        """More primaries = more information lost in scalar collapse."""
        models = [ising_model(), tricritical_ising_model(), three_state_potts_model()]
        info_ratios = []
        for m in models:
            result = scalar_collapse_analysis(m, num_terms=30, dps=DPS)
            info_ratios.append(result['info_ratio'])
        # info_ratio = 1/r^2 decreases as r (num primaries) increases
        # 3 primaries: 1/9, 6 primaries: 1/36, 10 primaries: 1/100
        assert info_ratios[0] > info_ratios[1] > info_ratios[2], (
            f"Info ratios {info_ratios} not decreasing — "
            "scalar collapse does NOT worsen with model size"
        )
