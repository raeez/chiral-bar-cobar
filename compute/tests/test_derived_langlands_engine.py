"""Tests for the derived Langlands computation engine.

Ground truth (sl_2, critical level k = -2, h^v = 2):
  - kappa = k + h^v = 0 => bar complex UNCURVED (d^2 = 0)
  - Z(V_{-2}(sl_2)) = C[S_{-2}, S_{-3}, ...] (Feigin-Frenkel)
  - dim Z_n = p_2(n) = partitions of n into parts >= 2
  - Sequence: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21, ...
  - Op_{PGL_2}(D) = {d^2 + q(z)}, parametrized by q in C[[z]]
  - dim Op_n = p_2(n) = dim Z_n (Feigin-Frenkel theorem)
  - Shapovalov det vanishes at k = -2 for weight >= 2
  - Wakimoto: V_{-2} -> beta-gamma x boson, d*gamma term vanishes
  - Quantum: q = exp(pi i / (k+2)) degenerates at k = -2

References:
  - Feigin-Frenkel (1992), Frenkel-Ben-Zvi (2004)
  - Kac-Kazhdan (1979): Shapovalov determinant formula
  - chapters/theory/derived_langlands.tex
  - CLAUDE.md: Sugawara UNDEFINED at critical level
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.derived_langlands_engine import (
    # Module 1: FF center
    partitions_min_part,
    ff_center_dims_sl2,
    ff_center_generating_function,
    segal_sugawara_states,
    ff_center_character_sl2,
    # Module 2: Opers
    oper_jet_dim_sl2,
    oper_jet_dims_sl2,
    oper_jet_dim_sln,
    oper_jet_dims_sln,
    oper_description_sln,
    verify_ff_center_matches_opers,
    # Module 3: Bar cohomology
    pbw_basis_sl2,
    vacuum_module_dim_sl2,
    vacuum_module_dims_sl2,
    bar_chain_dim_critical,
    bar_h0_dims_critical_sl2,
    # Module 4: Kac-Kazhdan
    shapovalov_form_sl2,
    kac_kazhdan_det_sl2,
    kac_kazhdan_nullspace_dim_sl2,
    kac_kazhdan_null_dims_sl2,
    kac_kazhdan_det_factors_sl2,
    # Module 5: Wakimoto
    wakimoto_sl2_critical_data,
    wakimoto_vacuum_dims,
    wakimoto_ope_verification,
    wakimoto_screening_operator,
    # Module 6: Quantum Langlands
    quantum_parameter,
    kl_multiplicity_matrix_sl2,
    critical_level_degeneration,
    admissible_level_data_sl2,
    # Cross-module
    verify_ff_theorem_sl2,
    verify_oper_jet_consistency,
    character_identity_critical,
    g_invariant_dims_critical_sl2,
    center_vs_invariants_critical,
    # Geometry
    hitchin_fiber_sl2,
    langlands_dual_data,
    oper_monodromy_sl2,
    oper_accessory_parameter,
    # Constants
    SL2_DIM,
    SL2_DUAL_COXETER,
    SL2_CRITICAL,
)


# =========================================================================
# Module 1: Feigin-Frenkel center
# =========================================================================

class TestFFCenter:
    """Tests for the Feigin-Frenkel center at critical level."""

    def test_partitions_base_cases(self):
        """p_2(0) = 1, p_2(1) = 0, p_2(2) = 1."""
        assert partitions_min_part(0, 2) == 1
        assert partitions_min_part(1, 2) == 0
        assert partitions_min_part(2, 2) == 1

    def test_partitions_small_values(self):
        """Verify p_2(n) for n = 0..10 against known sequence (OEIS A002865)."""
        # A002865: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12]
        for n, exp in enumerate(expected):
            assert partitions_min_part(n, 2) == exp, f"p_2({n}) = {partitions_min_part(n, 2)}, expected {exp}"

    def test_ff_center_dims_match_partitions(self):
        """FF center dims should be p_2(n) = partitions with parts >= 2."""
        dims = ff_center_dims_sl2(12)
        for n in range(13):
            assert dims[n] == partitions_min_part(n, 2)

    def test_ff_center_gf_matches_dims(self):
        """Generating function computation should agree with recursive formula."""
        dims = ff_center_dims_sl2(15)
        gf = ff_center_generating_function(15)
        assert dims == gf

    def test_segal_sugawara_states_weight2(self):
        """At weight 2: only one state S_{-2}|0>."""
        states = segal_sugawara_states(2)
        assert states == [(2,)]

    def test_segal_sugawara_states_weight4(self):
        """At weight 4: S_{-4}|0> and S_{-2}^2|0>."""
        states = segal_sugawara_states(4)
        assert len(states) == 2
        assert (4,) in states
        assert (2, 2) in states

    def test_segal_sugawara_states_weight6(self):
        """At weight 6: four states."""
        states = segal_sugawara_states(6)
        assert len(states) == 4
        expected = [(6,), (3, 3), (2, 4), (2, 2, 2)]
        for s in expected:
            assert s in states, f"Missing state {s}"

    def test_ff_center_is_polynomial_algebra(self):
        """Verify the character matches that of a polynomial algebra
        with generators at weights 2, 3, 4, ...."""
        char_data = ff_center_character_sl2(10)
        assert char_data['is_polynomial_algebra'] is True
        assert char_data['generator_weights'][:3] == [2, 3, 4]

    def test_ff_center_weight0_is_1(self):
        """Z_0 = C (the vacuum)."""
        dims = ff_center_dims_sl2(0)
        assert dims[0] == 1

    def test_ff_center_weight1_is_0(self):
        """Z_1 = 0 (no Sugawara mode at weight 1)."""
        dims = ff_center_dims_sl2(1)
        assert dims[1] == 0


# =========================================================================
# Module 2: Oper space
# =========================================================================

class TestOperSpace:
    """Tests for oper jet space dimensions."""

    def test_sl2_oper_dims_match_center(self):
        """The Feigin-Frenkel theorem: dim Z_n = dim Op_n for sl_2."""
        result = verify_ff_center_matches_opers(12)
        assert result['match'], f"Mismatches: {result['mismatches']}"

    def test_sl2_oper_weight0(self):
        """dim Op_0 = 1 (constant term)."""
        assert oper_jet_dim_sl2(0) == 1

    def test_sl2_oper_weight1(self):
        """dim Op_1 = 0 (no weight-1 oper parameter)."""
        assert oper_jet_dim_sl2(1) == 0

    def test_sl2_oper_weight2(self):
        """dim Op_2 = 1 (the q_0 parameter)."""
        assert oper_jet_dim_sl2(2) == 1

    def test_sln_oper_weight0_all_ranks(self):
        """dim Op_0(sl_N) = 1 for all N."""
        for N in range(2, 8):
            assert oper_jet_dim_sln(N, 0) == 1, f"Failed for sl_{N}"

    def test_sln_oper_weight1_all_ranks(self):
        """dim Op_1(sl_N) = 0 for all N (no weight-1 generators)."""
        for N in range(2, 8):
            assert oper_jet_dim_sln(N, 1) == 0, f"Failed for sl_{N}"

    def test_sln_oper_weight2(self):
        """dim Op_2(sl_N) = 1 for all N >= 2 (only q_2 at weight 2)."""
        for N in range(2, 8):
            assert oper_jet_dim_sln(N, 2) == 1, f"Failed for sl_{N}"

    def test_sl3_oper_weight3(self):
        """dim Op_3(sl_3) = 2 (from q_2 and q_3 contributions)."""
        assert oper_jet_dim_sln(3, 3) == 2

    def test_sl2_oper_weight3_is_1(self):
        """dim Op_3(sl_2) = 1 (only q_2 at weight 3 for sl_2)."""
        assert oper_jet_dim_sln(2, 3) == 1

    def test_oper_description_sl2(self):
        """sl_2-oper structure: d^2 + q_2(z)."""
        desc = oper_description_sln(2)
        assert desc['rank'] == 2
        assert desc['n_generating_fields'] == 1
        assert desc['generating_weights'] == [2]
        assert desc['critical_level'] == -2

    def test_oper_description_sl3(self):
        """sl_3-oper structure: d^3 + q_2(z) d + q_3(z)."""
        desc = oper_description_sln(3)
        assert desc['rank'] == 3
        assert desc['n_generating_fields'] == 2
        assert desc['generating_weights'] == [2, 3]
        assert desc['critical_level'] == -3

    def test_oper_jet_consistency(self):
        """Cross-check all oper jet dimension formulas."""
        result = verify_oper_jet_consistency(5, 8)
        for key, val in result.items():
            assert val, f"Failed check: {key}"


# =========================================================================
# Module 3: Bar cohomology at critical level
# =========================================================================

class TestBarCohomologyCritical:
    """Tests for the bar complex at critical level."""

    def test_pbw_basis_weight0(self):
        """Weight 0: vacuum state only."""
        basis = pbw_basis_sl2(0)
        assert len(basis) == 1
        assert basis[0] == ()

    def test_pbw_basis_weight1(self):
        """Weight 1: three states e_{-1}, h_{-1}, f_{-1}."""
        basis = pbw_basis_sl2(1)
        assert len(basis) == 3

    def test_vacuum_dims_known_values(self):
        """Verify vacuum module dimensions against prod 1/(1-q^n)^3."""
        expected = [1, 3, 9, 22, 51, 108, 221, 429, 810]
        dims = vacuum_module_dims_sl2(8)
        assert dims == expected

    def test_bar_chain_dim_degree0(self):
        """B^0 = C concentrated at weight 0."""
        assert bar_chain_dim_critical(0, 0) == 1
        assert bar_chain_dim_critical(0, 1) == 0
        assert bar_chain_dim_critical(0, 5) == 0

    def test_bar_chain_dim_degree1_matches_vacuum(self):
        """B^1_n = V_n (vacuum module at weight n)."""
        for n in range(6):
            assert bar_chain_dim_critical(1, n) == vacuum_module_dim_sl2(n)

    def test_bar_h0_matches_center(self):
        """H^0 of the bar complex at critical level = FF center."""
        h0 = bar_h0_dims_critical_sl2(8)
        center = ff_center_dims_sl2(8)
        assert h0 == center

    def test_curvature_vanishes(self):
        """kappa = k + h^v = -2 + 2 = 0 at critical level."""
        assert SL2_CRITICAL + SL2_DUAL_COXETER == 0


# =========================================================================
# Module 4: Kac-Kazhdan determinant
# =========================================================================

class TestKacKazhdan:
    """Tests for Shapovalov form and Kac-Kazhdan determinant."""

    def test_shapovalov_weight0(self):
        """At weight 0: S_0 = (1) (just the vacuum)."""
        S = shapovalov_form_sl2(0)
        assert S == Rational(1) * S.eye(1)

    def test_shapovalov_weight1_diagonal(self):
        """At weight 1: S_1 = diag(k, 2k, k)."""
        k = Symbol('k')
        S = shapovalov_form_sl2(1, k)
        assert S.shape == (3, 3)
        # Diagonal: (e_{-1}|0>, e_{-1}|0>) = <0|e_1 e_{-1}|0>
        # = <0| [e_1, e_{-1}] |0> + 0 = <0| h_0 |0> + k*kappa(e,f)*1 = k
        # (since h_0|0> = 0 and kappa(e,f) = 1)
        assert S[0, 0] == k
        assert S[1, 1] == 2 * k
        assert S[2, 2] == k

    def test_shapovalov_weight1_at_critical(self):
        """At k=-2, S_1 = diag(-2, -4, -2): invertible."""
        S = shapovalov_form_sl2(1, Rational(-2))
        assert S.rank() == 3
        assert kac_kazhdan_nullspace_dim_sl2(1, -2) == 0

    def test_kk_det_weight1(self):
        """det S_1 = 2k^3 (product of diagonal entries)."""
        k = Symbol('k')
        det = kac_kazhdan_det_sl2(1, k)
        # S_1 = diag(k, 2k, k), det = k * 2k * k = 2k^3
        assert det == 2 * k**3

    def test_kk_null_weight2_at_critical(self):
        """At k=-2, weight 2: null space dimension is 1 (first singular vector)."""
        null = kac_kazhdan_nullspace_dim_sl2(2, -2)
        assert null == 1

    def test_kk_null_weight3_at_critical(self):
        """At k=-2, weight 3: null space dimension is 4."""
        null = kac_kazhdan_nullspace_dim_sl2(3, -2)
        assert null == 4

    def test_kk_null_weight4_at_critical(self):
        """At k=-2, weight 4: null space dimension is 13."""
        null = kac_kazhdan_nullspace_dim_sl2(4, -2)
        assert null == 13

    def test_kk_null_weight0(self):
        """At any level, weight 0 has no null vectors."""
        assert kac_kazhdan_nullspace_dim_sl2(0, -2) == 0
        assert kac_kazhdan_nullspace_dim_sl2(0, 0) == 0

    def test_kk_null_increases_with_weight(self):
        """Null dimensions should be nondecreasing at critical level."""
        nulls = kac_kazhdan_null_dims_sl2(4, -2)
        for i in range(1, len(nulls)):
            assert nulls[i] >= nulls[i - 1], f"Decrease at weight {i}: {nulls}"

    def test_kk_det_factors(self):
        """Analyze the determinant factorization at weight 2."""
        factors = kac_kazhdan_det_factors_sl2(2)
        assert factors['weight'] == 2
        # At k=-2, the determinant should vanish
        assert factors['critical_is_zero']

    def test_shapovalov_symmetric(self):
        """The Shapovalov form should be symmetric."""
        k = Symbol('k')
        S = shapovalov_form_sl2(2, k)
        for i in range(S.rows):
            for j in range(i + 1, S.cols):
                assert S[i, j] == S[j, i], f"Asymmetric at ({i},{j})"

    def test_simple_quotient_dims_vs_null(self):
        """dim L_n(k=-2) = dim V_n - null_dim_n.

        The simple quotient L_{-2}(sl_2) at each weight has dimension
        equal to the vacuum dimension minus the null space dimension.
        """
        vac = vacuum_module_dims_sl2(4)
        nulls = kac_kazhdan_null_dims_sl2(4, -2)
        simple = [vac[n] - nulls[n] for n in range(5)]
        # All should be positive (the simple quotient exists)
        for n, d in enumerate(simple):
            assert d >= 0, f"Negative simple dim at weight {n}: {d}"


# =========================================================================
# Module 5: Wakimoto realization
# =========================================================================

class TestWakimoto:
    """Tests for the Wakimoto free-field realization."""

    def test_wakimoto_critical_data(self):
        """The Wakimoto data should be at level -2."""
        data = wakimoto_sl2_critical_data()
        assert data['level'] == -2

    def test_wakimoto_dgamma_vanishes(self):
        """At k=-2, the d*gamma coefficient k+2 = 0."""
        data = wakimoto_sl2_critical_data()
        assert 'vanishes' in data['critical_simplification'].lower()

    def test_wakimoto_character_matches_vacuum(self):
        """Wakimoto Fock space character = vacuum module character."""
        wak = wakimoto_vacuum_dims(8)
        vac = vacuum_module_dims_sl2(8)
        assert wak == vac

    def test_wakimoto_ope_verification_all_pass(self):
        """All OPE checks should pass."""
        results = wakimoto_ope_verification()
        for key, val in results.items():
            assert val, f"Wakimoto OPE check failed: {key}"

    def test_wakimoto_screening_operator(self):
        """Screening operator data is well-formed."""
        data = wakimoto_screening_operator()
        assert data['commutes_with_currents'] is True
        assert data['conformal_weight_of_V'] == 1


# =========================================================================
# Module 6: Quantum Langlands
# =========================================================================

class TestQuantumLanglands:
    """Tests for quantum Langlands data."""

    def test_quantum_parameter_critical_degenerate(self):
        """At k=-2, q -> infinity (degenerate)."""
        from sympy import oo
        q = quantum_parameter(-2)
        assert q == oo

    def test_critical_level_degeneration_data(self):
        """Critical level degeneration is classical limit."""
        data = critical_level_degeneration()
        assert data['kappa'] == 0
        assert data['classical_limit'] is True
        assert data['center_commutative'] is True

    def test_kl_multiplicity_at_admissible(self):
        """KL data at admissible level k = -2 + 3/2 = -1/2."""
        data = kl_multiplicity_matrix_sl2(3, 2)
        assert data['n_simple_modules'] == 2
        assert data['singular_vector_weight'] == 3
        assert data['periodicity'] == 3

    def test_kl_multiplicity_critical_error(self):
        """KL at critical level should flag degeneration."""
        data = kl_multiplicity_matrix_sl2(0, 1)
        # k = -2 + 0/1 = -2: kappa = 0
        assert 'error' in data or data.get('kappa') == '0'

    def test_admissible_levels_include_minimal_models(self):
        """Admissible levels should include the unitary minimal model series."""
        levels = admissible_level_data_sl2(6)
        # k = -2 + (m+2)/(m+1) for m >= 1 are the unitary ones (p = q+1).
        unitary = [l for l in levels if l['is_unitary']]
        # p=2,q=1 -> k=0 (trivial); p=3,q=2 -> k=-1/2; p=4,q=3 -> k=-2/3
        assert len(unitary) >= 2

    def test_admissible_coprimality(self):
        """All admissible levels have gcd(p,q) = 1."""
        from math import gcd
        levels = admissible_level_data_sl2(8)
        for l in levels:
            assert gcd(l['p'], l['q']) == 1


# =========================================================================
# Cross-module verifications
# =========================================================================

class TestCrossModule:
    """Cross-cutting verification tests."""

    def test_ff_theorem_master(self):
        """Master verification of Feigin-Frenkel theorem."""
        result = verify_ff_theorem_sl2(8)
        assert result['center_equals_opers']
        assert result['gf_matches_center']
        assert result['wakimoto_character_match']
        assert result['curvature_vanishes']

    def test_character_identity_ratio_positive(self):
        """ch(V) / ch(Z) should have nonneg coefficients (quotient module)."""
        ci = character_identity_critical(10)
        assert ci['ratio_positive']

    def test_character_identity_ratio_values(self):
        """Verify first few values of the character ratio."""
        ci = character_identity_critical(6)
        # ratio[0] = 1, ratio[1] = 3 (three weight-1 states, none central)
        assert ci['ratio_dims'][0] == 1
        assert ci['ratio_dims'][1] == 3

    def test_center_contained_in_invariants(self):
        """Z_n <= (V_n)^g at critical level."""
        data = center_vs_invariants_critical(6)
        assert data['center_contained']

    def test_center_strictly_smaller_than_invariants(self):
        """For weight >= 4, Z_n < (V_n)^g (center is strict subset)."""
        data = center_vs_invariants_critical(6)
        # First discrepancy should be at weight 4
        assert data['first_discrepancy'] == 4

    def test_g_invariant_dims_at_critical(self):
        """Known g-invariant dims at k=-2: 1, 0, 1, 1, 3, 3, 8."""
        inv = g_invariant_dims_critical_sl2(6)
        expected = [1, 0, 1, 1, 3, 3, 8]
        assert inv == expected


# =========================================================================
# Geometry
# =========================================================================

class TestGeometry:
    """Tests for spectral geometry and Langlands duality."""

    def test_hitchin_fiber_nilpotent(self):
        """q = 0 gives the nilpotent fiber."""
        data = hitchin_fiber_sl2(0)
        assert data['singular'] is True
        assert data['fiber_type'] == 'nilpotent'

    def test_hitchin_fiber_semisimple(self):
        """q != 0 gives a smooth fiber."""
        data = hitchin_fiber_sl2(1.0)
        assert data['singular'] is False
        assert data['fiber_type'] == 'semisimple'

    def test_langlands_dual_sl2(self):
        """sl_2 is dual to PGL_2."""
        table = langlands_dual_data()
        assert table['sl_2']['dual'] == 'PGL_2'
        assert table['sl_2']['h_v'] == '2'

    def test_langlands_dual_g2_self_dual(self):
        """g_2 is self-dual under Langlands duality."""
        table = langlands_dual_data()
        assert table['g_2']['self_dual'] == 'yes'

    def test_oper_monodromy_trivial(self):
        """For q = 0 (trivial oper), monodromy trace ~ 2."""
        import numpy as np
        tr = oper_monodromy_sl2([0], z0=0.0, z1=0.1, n_steps=1000)
        assert abs(tr - 2.0) < 0.01, f"Trivial oper trace = {tr}, expected ~2"

    def test_oper_accessory_weight2(self):
        """Weight 2: one accessory parameter."""
        data = oper_accessory_parameter(2)
        assert data['n_parameters'] == 1


# =========================================================================
# Dimensional consistency
# =========================================================================

class TestDimensionalConsistency:
    """Tests for dimensional consistency across all modules."""

    def test_vacuum_dim_at_weight_matches_basis(self):
        """vacuum_module_dim_sl2 should match pbw_basis length."""
        for n in range(7):
            assert vacuum_module_dim_sl2(n) == len(pbw_basis_sl2(n))

    def test_null_plus_rank_equals_total(self):
        """null_dim + rank = total dim (from Shapovalov)."""
        for n in range(4):
            S = shapovalov_form_sl2(n, Rational(-2))
            total = S.rows
            rank = S.rank()
            null = total - rank
            assert null == kac_kazhdan_nullspace_dim_sl2(n, -2)

    def test_center_dims_monotonic_except_weight1(self):
        """Z_n should be nondecreasing for n >= 2."""
        dims = ff_center_dims_sl2(12)
        for n in range(3, 13):
            assert dims[n] >= dims[n - 1], f"Decrease at weight {n}"

    def test_oper_dims_sl2_equals_sl_n_2(self):
        """oper_jet_dim_sl2(n) == oper_jet_dim_sln(2, n) for all n."""
        for n in range(12):
            assert oper_jet_dim_sl2(n) == oper_jet_dim_sln(2, n)

    def test_segal_sugawara_count_matches_dim(self):
        """Number of SS states at weight n should equal p_2(n)."""
        for n in range(10):
            states = segal_sugawara_states(n)
            assert len(states) == partitions_min_part(n, 2), f"Mismatch at weight {n}"


# =========================================================================
# Edge cases and constants
# =========================================================================

class TestConstantsAndEdgeCases:
    """Tests for constants and edge cases."""

    def test_sl2_constants(self):
        """Verify sl_2 constants."""
        assert SL2_DIM == 3
        assert SL2_DUAL_COXETER == 2
        assert SL2_CRITICAL == -2

    def test_partitions_negative(self):
        """p_2(n) = 0 for n < 0."""
        assert partitions_min_part(-1, 2) == 0
        assert partitions_min_part(-5, 2) == 0

    def test_partitions_min_part_1(self):
        """p_1(n) = p(n) (unrestricted partitions)."""
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
        expected = [1, 1, 2, 3, 5, 7, 11]
        for n, exp in enumerate(expected):
            assert partitions_min_part(n, 1) == exp

    def test_oper_jet_dim_negative_weight(self):
        """dim Op_n = 0 for n < 0."""
        assert oper_jet_dim_sln(2, -1) == 0
        assert oper_jet_dim_sln(3, -1) == 0

    def test_bar_chain_dim_negative(self):
        """Bar chain dimension = 0 for negative inputs."""
        assert bar_chain_dim_critical(-1, 0) == 0
        assert bar_chain_dim_critical(0, -1) == 0
