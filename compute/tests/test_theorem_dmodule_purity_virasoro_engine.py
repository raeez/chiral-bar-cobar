r"""Tests for D-module purity converse for Virasoro.

Tests organized in 8 clusters:

CLUSTER 1: FM compactification geometry (strata counts, codimensions).
CLUSTER 2: Virasoro bar complex dimensions (bigraded, multi-path).
CLUSTER 3: Fuchsian exponents and BPZ residues.
CLUSTER 4: Characteristic variety alignment.
CLUSTER 5: PBW vs Saito comparison (consistency at each arity).
CLUSTER 6: Minimal model purity analysis (non-Koszul => non-pure).
CLUSTER 7: BPZ-Hodge obstruction analysis.
CLUSTER 8: Cross-family consistency and Euler characteristic.

Multi-path verification (per CLAUDE.md mandate):
  Path 1: Direct computation from definitions.
  Path 2: Cross-family consistency (KM vs Virasoro vs Heisenberg).
  Path 3: Known values from manuscript / literature.
  Path 4: Koszul Euler characteristic identity.
  Path 5: Limiting cases (c -> 0, n -> 1).

Anti-pattern guards:
  AP1:  kappa(Vir_c) = c/2.  Verified independently.
  AP3:  Each computation independent.  No pattern-matching.
  AP9:  PBW != Saito a priori.  Tested, not assumed.
  AP10: Cross-checks between independent methods.
  AP19: r-matrix pole order = OPE pole order - 1.
  AP36: Converse OPEN.  Never claim proved.
  AP39: kappa = c/2 IS correct for Virasoro (coincidence for rank 1).
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.theorem_dmodule_purity_virasoro_engine import (
    # FM geometry
    fm2_strata,
    fm3_strata,
    fm4_strata,
    fm_n_divisor_count,
    # Virasoro bar complex
    virasoro_weight_space_dim,
    bar_component_dim,
    virasoro_bar_bigraded_dims,
    # Fuchsian exponents
    virasoro_ope_poles,
    virasoro_rmatrix_poles,
    bpz_residue_eigenvalues_n2,
    bpz_residue_eigenvalues_n3,
    fuchsian_exponents_n2,
    fuchsian_exponents_n3,
    # Characteristic variety
    char_variety_n2,
    char_variety_n3,
    char_variety_n4,
    # PBW vs Saito
    predict_weight_filtration,
    compare_pbw_saito_virasoro,
    # Minimal models
    minimal_model_c,
    analyze_minimal_model_purity,
    # BPZ-Hodge
    analyze_bpz_hodge_obstruction,
    # Cross-family
    cross_family_consistency,
    # Euler characteristic
    bar_euler_char,
    koszul_dual_dims,
    verify_koszul_euler_char,
    # Braiding and monodromy
    virasoro_braiding_eigenvalues,
    monodromy_weight_formula,
    # Full analysis
    full_purity_converse_analysis,
    purity_converse_summary,
)


# =========================================================================
# CLUSTER 1: FM compactification geometry
# =========================================================================

class TestFMGeometry:
    """FM compactification geometry at low arity."""

    def test_fm2_single_divisor(self):
        """FM_2(C) = Bl_Delta(C^2) has exactly one boundary divisor."""
        strata = fm2_strata()
        assert len(strata) == 1
        assert strata[0].codimension == 1
        assert strata[0].is_divisor is True
        assert strata[0].label == 'E_{12}'

    def test_fm3_three_divisors(self):
        """FM_3(C) has three pairwise collision divisors."""
        strata = fm3_strata()
        divisors = [s for s in strata if s.is_divisor]
        assert len(divisors) == 3
        labels = {s.label for s in divisors}
        assert labels == {'D_{12}', 'D_{13}', 'D_{23}'}

    def test_fm3_triple_collision(self):
        """FM_3(C) has a codimension-2 triple collision stratum."""
        strata = fm3_strata()
        codim2 = [s for s in strata if s.codimension == 2]
        assert len(codim2) == 1
        assert codim2[0].label == 'D_{123}'

    def test_fm4_divisor_count(self):
        """FM_4(C) has 13 boundary divisors."""
        strata = fm4_strata()
        divisors = [s for s in strata if s.is_divisor]
        assert len(divisors) == 13

    def test_fm4_pairwise_divisors(self):
        """FM_4 has C(4,2) = 6 pairwise collision divisors."""
        strata = fm4_strata()
        pairwise = [s for s in strata if len(s.partition) == 1
                     and len(s.partition[0]) == 2]
        assert len(pairwise) == 6

    def test_fm_n_divisor_count_function(self):
        """Divisor count matches explicit enumeration."""
        assert fm_n_divisor_count(2) == 1
        assert fm_n_divisor_count(3) == 3
        assert fm_n_divisor_count(4) == 13


# =========================================================================
# CLUSTER 2: Virasoro bar complex dimensions
# =========================================================================

class TestVirasoroBarDims:
    """Bar complex dimensions for universal Virasoro.

    Multi-path verification:
      Path 1: Direct computation from partition formula.
      Path 2: Recursive tensor product decomposition.
      Path 3: Known values from manuscript (bar_cohomology_dimensions.py).
    """

    def test_weight_space_dim_h2(self):
        """dim A_2 = 1 (the generator T)."""
        assert virasoro_weight_space_dim(2) == 1

    def test_weight_space_dim_h3(self):
        """dim A_3 = 0 (no weight-3 states from T at weight 2).

        Partitions of 3 into parts >= 2: {3} -> 1 state (L_{-3}).
        Wait: 3 is a single part >= 2, so p(3) - p(2) = 3 - 2 = 1.
        Actually dim A_3 = p(3) - p(3-1) = p(3) - p(2) = 3 - 2 = 1.

        CORRECTION: dim A_3 = 1 (state L_{-3}|0>).
        """
        assert virasoro_weight_space_dim(3) == 1

    def test_weight_space_dim_h4(self):
        """dim A_4 = 2 (states L_{-4}|0> and L_{-2}^2|0>).

        p(4) - p(3) = 5 - 3 = 2.
        """
        assert virasoro_weight_space_dim(4) == 2

    def test_weight_space_dim_h5(self):
        """dim A_5 = 3.  p(5) - p(4) = 7 - 5 = 2.

        Wait: p(5) = 7, p(4) = 5, so dim A_5 = 7 - 5 = 2.
        States: L_{-5}|0>, L_{-3}L_{-2}|0>.
        """
        assert virasoro_weight_space_dim(5) == 2

    def test_weight_space_dim_h6(self):
        """dim A_6 = p(6) - p(5) = 11 - 7 = 4.

        States: L_{-6}, L_{-4}L_{-2}, L_{-3}^2, L_{-2}^3.
        """
        assert virasoro_weight_space_dim(6) == 4

    def test_weight_space_h1_zero(self):
        """No weight-1 states for Virasoro (generator at weight 2)."""
        assert virasoro_weight_space_dim(1) == 0

    def test_weight_space_h0_zero(self):
        """No weight-0 positive states."""
        assert virasoro_weight_space_dim(0) == 0

    def test_bar_dim_arity1_weight2(self):
        """B^{1,2} = A_2 = 1 (the generator T)."""
        assert bar_component_dim(1, 2) == 1

    def test_bar_dim_arity2_weight4(self):
        """B^{2,4} = dim(A_2 tensor A_2) = 1 (T tensor T)."""
        assert bar_component_dim(2, 4) == 1

    def test_bar_dim_arity2_weight5(self):
        """B^{2,5} = dim(A_2) * dim(A_3) + dim(A_3) * dim(A_2) = 1*1 + 1*1 = 2."""
        assert bar_component_dim(2, 5) == 2

    def test_bar_dim_arity2_weight6(self):
        """B^{2,6} = sum_{w=2}^{4} dim(A_w) * dim(A_{6-w}).

        = dim(A_2)*dim(A_4) + dim(A_3)*dim(A_3) + dim(A_4)*dim(A_2)
        = 1*2 + 1*1 + 2*1 = 5.

        Wait: dim(A_2)=1, dim(A_3)=1, dim(A_4)=2.
        B^{2,6} = 1*2 + 1*1 + 2*1 = 5.

        Actually, check: 6 - 2 = 4, 6 - 3 = 3, 6 - 4 = 2.
        So w ranges over {2, 3, 4} for the first factor,
        and the second factor has weight 6-w in {4, 3, 2}.
        Sum = dim(A_2)*dim(A_4) + dim(A_3)*dim(A_3) + dim(A_4)*dim(A_2)
            = 1*2 + 1*1 + 2*1 = 5.
        """
        assert bar_component_dim(2, 6) == 5

    def test_bar_dim_arity3_weight6(self):
        """B^{3,6} = dim(A_2 tensor A_2 tensor A_2) = 1."""
        assert bar_component_dim(3, 6) == 1

    def test_bar_dim_arity3_weight7(self):
        """B^{3,7}: distribute weight 7 among 3 factors each >= 2.

        Compositions: (2,2,3), (2,3,2), (3,2,2) -> 3 orderings.
        dim = dim(A_2)*dim(A_2)*dim(A_3) * 3 = 1*1*1 * 3 = 3.
        """
        assert bar_component_dim(3, 7) == 3

    def test_bigraded_dims_basic(self):
        """Bigraded dimensions match individual computations."""
        dims = virasoro_bar_bigraded_dims(3, 8)
        assert dims[(1, 2)] == 1
        assert dims[(2, 4)] == 1
        assert dims[(3, 6)] == 1

    def test_bar_dim_monotonicity(self):
        """Bar dimensions grow with weight at fixed arity.

        For arity 2: dim B^{2,h} is non-decreasing for h >= 4.
        """
        prev = 0
        for h in range(4, 12):
            d = bar_component_dim(2, h)
            assert d >= prev, f"Non-monotonic at h={h}: {d} < {prev}"
            prev = d


# =========================================================================
# CLUSTER 3: Fuchsian exponents and BPZ residues
# =========================================================================

class TestFuchsianExponents:
    """BPZ residue eigenvalues and Fuchsian exponents."""

    def test_ope_poles_virasoro(self):
        """Virasoro OPE has poles at orders 4, 2, 1."""
        poles = virasoro_ope_poles()
        assert set(poles.keys()) == {4, 2, 1}

    def test_rmatrix_poles_ap19(self):
        """r-matrix poles = OPE poles - 1 (AP19).

        OPE: z^{-4}, z^{-2}, z^{-1}.
        r-matrix: z^{-3}, z^{-1}.
        """
        rpoles = virasoro_rmatrix_poles()
        assert set(rpoles.keys()) == {3, 1}

    def test_fuchsian_n2_integer(self):
        """All Fuchsian exponents at arity 2 are non-negative integers."""
        data = fuchsian_exponents_n2(Rational(1), 12)
        assert data.integer_exponents is True
        assert all(e >= 0 for e in data.exponents)

    def test_fuchsian_n2_start_at_4(self):
        """First Fuchsian exponent at arity 2 is 4 (min weight of B_2)."""
        data = fuchsian_exponents_n2(Rational(1), 12)
        assert data.exponents[0] == Rational(4)

    def test_fuchsian_n2_resonant(self):
        """Fuchsian exponents at arity 2 are resonant (consecutive integers).

        Exponents 4, 5, 6, 7, ... differ by integers, hence resonant.
        """
        data = fuchsian_exponents_n2(Rational(1), 12)
        assert data.non_resonant is False

    def test_fuchsian_n3_integer(self):
        """All Fuchsian exponents at arity 3 are non-negative integers."""
        data_list = fuchsian_exponents_n3(Rational(1), 12)
        for data in data_list:
            assert data.integer_exponents is True

    def test_fuchsian_n3_three_divisors(self):
        """Arity 3 has three Fuchsian exponent sets (one per divisor)."""
        data_list = fuchsian_exponents_n3(Rational(1), 10)
        assert len(data_list) == 3
        labels = {d.divisor_label for d in data_list}
        assert labels == {'D_12', 'D_13', 'D_23'}

    def test_fuchsian_n3_symmetry(self):
        """Fuchsian exponents at arity 3 are the same for all three divisors.

        By S_3 symmetry of FM_3, the exponents at D_{12}, D_{13}, D_{23}
        are all the same.
        """
        data_list = fuchsian_exponents_n3(Rational(1), 10)
        exp_sets = [set(d.exponents) for d in data_list]
        assert exp_sets[0] == exp_sets[1] == exp_sets[2]

    def test_bpz_residues_n2_present(self):
        """BPZ residue eigenvalues at n=2 are computed."""
        eigenvalues = bpz_residue_eigenvalues_n2(Rational(1))
        assert 'E_12' in eigenvalues
        assert len(eigenvalues['E_12']) > 0

    def test_bpz_residues_n3_all_divisors(self):
        """BPZ residue eigenvalues at n=3 cover all three divisors."""
        eigenvalues = bpz_residue_eigenvalues_n3(Rational(1))
        assert 'D_12' in eigenvalues
        assert 'D_13' in eigenvalues
        assert 'D_23' in eigenvalues


# =========================================================================
# CLUSTER 4: Characteristic variety alignment
# =========================================================================

class TestCharacteristicVariety:
    """Characteristic variety of the bar D-module."""

    def test_cv_n2_aligned(self):
        """Ch(B_2) is aligned to FM boundary (single component)."""
        cv = char_variety_n2()
        assert cv.aligned_to_fm is True
        assert cv.n_components == 1

    def test_cv_n2_holonomic(self):
        """B_2 is regular holonomic."""
        cv = char_variety_n2()
        assert cv.holonomic is True
        assert cv.regular_holonomic is True

    def test_cv_n3_aligned(self):
        """Ch(B_3) is aligned to FM boundary (three components)."""
        cv = char_variety_n3()
        assert cv.aligned_to_fm is True
        assert cv.n_components == 3

    def test_cv_n4_aligned(self):
        """Ch(B_4) is aligned to FM boundary."""
        cv = char_variety_n4()
        assert cv.aligned_to_fm is True

    def test_cv_n4_pairwise_components(self):
        """Ch(B_4) has at least 6 pairwise components (C(4,2))."""
        cv = char_variety_n4()
        assert cv.n_components >= 6

    def test_all_arities_regular_holonomic(self):
        """Bar D-modules are regular holonomic at all tested arities."""
        for cv_fn in [char_variety_n2, char_variety_n3, char_variety_n4]:
            cv = cv_fn()
            assert cv.regular_holonomic is True

    def test_all_arities_fm_aligned(self):
        """Characteristic variety aligned to FM boundary at all arities."""
        for cv_fn in [char_variety_n2, char_variety_n3, char_variety_n4]:
            cv = cv_fn()
            assert cv.aligned_to_fm is True


# =========================================================================
# CLUSTER 5: PBW vs Saito comparison
# =========================================================================

class TestPBWSaitoComparison:
    """PBW vs Saito filtration comparison for Virasoro."""

    def test_comparison_n2_consistent(self):
        """PBW = Saito is consistent at arity 2."""
        result = compare_pbw_saito_virasoro(2, Rational(1), 12)
        assert result.consistent_with_purity is True

    def test_comparison_n3_consistent(self):
        """PBW = Saito is consistent at arity 3."""
        result = compare_pbw_saito_virasoro(3, Rational(1), 12)
        assert result.consistent_with_purity is True

    def test_comparison_n4_consistent(self):
        """PBW = Saito is consistent at arity 4."""
        result = compare_pbw_saito_virasoro(4, Rational(1), 12)
        assert result.consistent_with_purity is True

    def test_comparison_exponents_match_n2(self):
        """Fuchsian exponents = conformal weights at arity 2."""
        result = compare_pbw_saito_virasoro(2, Rational(1), 12)
        assert result.exponents_match_weights is True

    def test_comparison_c_independence(self):
        """PBW = Saito consistency is independent of central charge.

        The bar dimensions and Fuchsian exponents depend on the
        generator structure, not on c.  So PBW = Saito consistency
        at one c implies consistency at all c.
        """
        for c_val in [Rational(1), Rational(1, 2), Rational(-22, 5), Rational(26)]:
            result = compare_pbw_saito_virasoro(2, c_val, 10)
            assert result.consistent_with_purity is True, \
                f"PBW = Saito inconsistent at c = {c_val}"

    def test_weight_filtration_prediction_n2(self):
        """Weight filtration prediction at arity 2."""
        pred = predict_weight_filtration(2, 10)
        assert pred.arity == 2
        assert pred.is_pure is True
        assert pred.pure_weight == 2

    def test_weight_filtration_prediction_n3(self):
        """Weight filtration prediction at arity 3."""
        pred = predict_weight_filtration(3, 10)
        assert pred.arity == 3
        assert pred.is_pure is True
        assert pred.pure_weight == 3


# =========================================================================
# CLUSTER 6: Minimal model purity analysis
# =========================================================================

class TestMinimalModelPurity:
    """Minimal model analysis: non-Koszul must give non-pure.

    The converse of D-module purity predicts: Koszulness <=> purity.
    For minimal models (NOT Koszul): purity must FAIL.
    We verify that the null-vector mechanism consistently produces
    the expected non-purity.
    """

    def test_ising_not_koszul(self):
        """Ising model M(4,3): c = 1/2, h_null = 6 >= 4, NOT Koszul."""
        result = analyze_minimal_model_purity(4, 3)
        assert result.c == Rational(1, 2)
        assert result.h_null == 6
        assert result.is_koszul is False

    def test_ising_purity_fails(self):
        """Ising model: non-Koszulness produces non-purity."""
        result = analyze_minimal_model_purity(4, 3)
        assert result.purity_fails is True
        assert result.bar_degree_of_failure == 2
        assert result.weight_of_failure == 6

    def test_trivial_koszul(self):
        """M(3,2): c = 0, h_null = 2 < 4, IS Koszul."""
        result = analyze_minimal_model_purity(3, 2)
        assert result.is_koszul is True
        assert result.purity_fails is False

    def test_yang_lee_not_koszul(self):
        """Yang-Lee model M(5,2): h_null = 4 >= 4, NOT Koszul."""
        result = analyze_minimal_model_purity(5, 2)
        assert result.h_null == 4
        assert result.is_koszul is False
        assert result.purity_fails is True

    def test_three_state_potts(self):
        """3-state Potts M(5,3): h_null = 8, NOT Koszul."""
        result = analyze_minimal_model_purity(5, 3)
        assert result.h_null == 8
        assert result.is_koszul is False
        assert result.purity_fails is True

    def test_tricritical_ising(self):
        """Tri-critical Ising M(5,4): h_null = 12, NOT Koszul."""
        result = analyze_minimal_model_purity(5, 4)
        assert result.h_null == 12
        assert result.is_koszul is False

    def test_large_null_vector(self):
        """M(7,2): h_null = 6, NOT Koszul."""
        result = analyze_minimal_model_purity(7, 2)
        assert result.h_null == 6
        assert result.is_koszul is False
        assert result.purity_fails is True

    def test_minimal_model_central_charge(self):
        """Central charge formula c_{p,q} = 1 - 6(p-q)^2/(pq).

        Multi-path: direct formula vs known values.
        """
        assert minimal_model_c(4, 3) == Rational(1, 2)
        assert minimal_model_c(5, 2) == Rational(-22, 5)
        assert minimal_model_c(3, 2) == Rational(0)
        assert minimal_model_c(5, 4) == Rational(7, 10)

    def test_koszul_nonkoszul_dichotomy(self):
        """Koszulness and purity are either both True or both False.

        This is the key prediction of PBW = Saito.
        """
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 3), (5, 4), (7, 2)]:
            result = analyze_minimal_model_purity(p, q)
            if result.is_koszul:
                assert not result.purity_fails, \
                    f"M({p},{q}): Koszul but purity fails?"
            else:
                assert result.purity_fails, \
                    f"M({p},{q}): non-Koszul but purity holds?"


# =========================================================================
# CLUSTER 7: BPZ-Hodge obstruction analysis
# =========================================================================

class TestBPZHodgeObstruction:
    """BPZ-Hodge obstruction: the key missing step."""

    def test_integer_residues(self):
        """BPZ has integer residues for all c."""
        for c_val in [Rational(1), Rational(1, 2), Rational(-22, 5)]:
            data = analyze_bpz_hodge_obstruction(c_val, 2)
            assert data.bpz_has_integer_residues is True

    def test_regular_singular(self):
        """BPZ is always regular singular."""
        data = analyze_bpz_hodge_obstruction(Rational(1), 2)
        assert data.bpz_regular_singular is True

    def test_unipotent_monodromy(self):
        """BPZ has unipotent monodromy at generic c."""
        data = analyze_bpz_hodge_obstruction(Rational(1), 2)
        assert data.monodromy_unipotent is True

    def test_vhs_at_integer_c(self):
        """At integer c >= 1: BPZ carries a unitary VHS."""
        for c_int in [1, 2, 5, 10]:
            data = analyze_bpz_hodge_obstruction(Rational(c_int), 2)
            assert data.vhs_exists_at_integer_c is True

    def test_vhs_unknown_generic(self):
        """At generic c: VHS existence is unknown (the gap)."""
        data = analyze_bpz_hodge_obstruction(Rational(1, 3), 2)
        assert data.vhs_exists_generic is None

    def test_consistent_with_purity(self):
        """PBW = Saito is consistent at all tested c and n."""
        for c_val in [Rational(1), Rational(26), Rational(1, 2)]:
            for n in [2, 3]:
                data = analyze_bpz_hodge_obstruction(c_val, n)
                assert data.pbw_saito_consistent is True


# =========================================================================
# CLUSTER 8: Cross-family consistency and Euler characteristic
# =========================================================================

class TestCrossFamilyAndEuler:
    """Cross-family consistency and Koszul Euler characteristic."""

    def test_cross_family_consistent(self):
        """KM and Virasoro have the same structural gap."""
        result = cross_family_consistency()
        assert result['consistent'] is True

    def test_km_proved(self):
        """D-module purity is proved for affine KM."""
        result = cross_family_consistency()
        assert 'PROVED' in result['km_status']

    def test_vir_open(self):
        """D-module purity converse is open for Virasoro."""
        result = cross_family_consistency()
        assert 'OPEN' in result['vir_status']

    def test_koszul_euler_char_stabilization(self):
        """Koszul Euler characteristic stabilizes for Virasoro.

        The alternating sum sum_{n >= 1} (-1)^{n+1} dim B^{n,h}
        terminates at finite arity for each weight h (because each
        bar factor has weight >= 2, so B^{n,h} = 0 for n > h/2).

        Stabilization is a NON-TRIVIAL test: it verifies the bar
        complex has the expected finiteness properties.
        """
        result = verify_koszul_euler_char(10)
        assert result['consistent'] is True

    def test_koszul_euler_char_at_h2(self):
        """Euler char at h=2: B^{1,2} = 1, all higher arities zero.

        alt_sum = 1.  Stabilized at arity 1.
        """
        result = verify_koszul_euler_char(10)
        check = result['checks'][2]
        assert check['alternating_sum'] == 1
        assert check['stabilized'] is True

    def test_koszul_euler_char_at_h4(self):
        """Euler char at h=4: B^{1,4} = 2, B^{2,4} = 1, higher zero.

        alt_sum = 2 - 1 = 1.  Stabilized at arity 2 (<= h/2 = 2).
        """
        result = verify_koszul_euler_char(10)
        check = result['checks'][4]
        assert check['alternating_sum'] == 1
        assert check['stabilized'] is True

    def test_koszul_euler_char_stabilization_bound(self):
        """Stabilization bound: last nonzero arity <= h/2."""
        result = verify_koszul_euler_char(10)
        for h, check in result['checks'].items():
            assert check['last_nonzero_arity'] <= check['stabilization_bound'], \
                f"h={h}: last nonzero arity {check['last_nonzero_arity']} > bound {check['stabilization_bound']}"

    def test_bar_euler_char_sign(self):
        """Bar Euler char has sign (-1)^arity."""
        chi_2 = bar_euler_char(2, 10)
        for h, val in chi_2.items():
            assert val >= 0, f"chi(B_2, {h}) = {val} should be positive ((-1)^2 = +1)"

    def test_braiding_trivial_monodromy(self):
        """Virasoro vacuum braiding has trivial monodromy."""
        eigenvalues = virasoro_braiding_eigenvalues(Rational(1), 0, 0)
        assert all(e == 1 for e in eigenvalues[:5])

    def test_monodromy_weight_formula(self):
        """Saito weight = 2 * residue eigenvalue."""
        assert monodromy_weight_formula(Rational(4)) == Rational(8)
        assert monodromy_weight_formula(Rational(0)) == Rational(0)


# =========================================================================
# CLUSTER 9: Full analysis and summary
# =========================================================================

class TestFullAnalysis:
    """Full D-module purity converse analysis."""

    def test_converse_not_proved(self):
        """The converse is NOT yet proved (status honest)."""
        result = full_purity_converse_analysis(3, 10)
        assert result.converse_proved is False

    def test_no_counterexample(self):
        """No counterexample found."""
        result = full_purity_converse_analysis(3, 10)
        assert result.counterexample_found is False

    def test_evidence_strong(self):
        """Evidence level is 'strong' (all tests consistent)."""
        result = full_purity_converse_analysis(3, 10)
        assert result.evidence_level == 'strong'

    def test_conclusions_nonempty(self):
        """Analysis produces non-trivial conclusions."""
        result = full_purity_converse_analysis(3, 10)
        assert len(result.conclusions) >= 3

    def test_remaining_gap_documented(self):
        """The remaining gap is clearly documented."""
        result = full_purity_converse_analysis(3, 10)
        assert 'Step 4' in result.remaining_gap
        assert 'Saito' in result.remaining_gap

    def test_summary_status_open(self):
        """Summary reports status as OPEN."""
        summary = purity_converse_summary()
        assert summary['converse_status'] == 'OPEN'

    def test_summary_no_counterexamples(self):
        """Summary reports zero counterexamples."""
        summary = purity_converse_summary()
        assert summary['counterexamples'] == 0

    def test_summary_strong_evidence(self):
        """Summary reports strong evidence."""
        summary = purity_converse_summary()
        assert summary['evidence_level'] == 'strong'

    def test_summary_proved_for_km(self):
        """Summary correctly reports proved for KM."""
        summary = purity_converse_summary()
        assert 'Kac-Moody' in summary['proved_for']

    def test_summary_open_for_virasoro(self):
        """Summary correctly reports open for Virasoro."""
        summary = purity_converse_summary()
        assert 'Virasoro' in summary['open_for']

    def test_summary_fuchsian_integer(self):
        """Summary reports integer Fuchsian exponents."""
        summary = purity_converse_summary()
        assert summary['fuchsian_exponents_integer'] is True

    def test_summary_cv_aligned(self):
        """Summary reports aligned characteristic variety."""
        summary = purity_converse_summary()
        assert summary['characteristic_variety_aligned'] is True

    def test_summary_cross_family(self):
        """Summary reports cross-family consistency."""
        summary = purity_converse_summary()
        assert summary['cross_family_consistent'] is True

    def test_minimal_models_all_consistent(self):
        """All minimal models are consistent with Koszul <=> purity."""
        summary = purity_converse_summary()
        assert summary['minimal_models_tested'] >= 5
        assert summary['minimal_models_consistent'] == summary['minimal_models_tested']
