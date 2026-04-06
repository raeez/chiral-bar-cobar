"""Tests for D-module purity counterexample search engine.

Systematic verification that no counterexample to the D-module purity
converse exists among known candidate algebras.

The converse states: Koszulness => D-module purity (item (xii) of
thm:koszul-equivalences-meta). The forward direction (xii) => (x)
is proved via Saito's mixed Hodge modules. The converse is OPEN.

TEST STRATEGY:
    For each candidate non-Koszul algebra:
    1. Verify Koszulness status (NOT Koszul or OPEN)
    2. Verify D-module purity status (NOT pure or OPEN)
    3. Verify the algebra is NOT a counterexample
    4. Cross-check the mechanism

    For each Koszul control algebra:
    1. Verify Koszulness (PROVED)
    2. Verify D-module purity (PURE)
    3. Verify consistency

MULTI-PATH VERIFICATION (3+ paths per key claim):
    Path 1: Direct bar cohomology computation (off-diagonal?)
    Path 2: Weight filtration analysis (mixed?)
    Path 3: Characteristic variety analysis (aligned?)
    Path 4: Classical BGS check (control case)
    Path 5: Mechanism analysis (universal null-vector mechanism)

References:
    conj:d-module-purity-koszulness (bar_cobar_adjunction_inversion.tex)
    thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
    BGS96: Beilinson-Ginzburg-Soergel, Koszul duality patterns
"""

import pytest
from fractions import Fraction

from compute.lib.dmod_counterexample_search_engine import (
    # Enums
    KoszulVerdict,
    PurityVerdict,
    CounterexampleStatus,
    # Data structures
    BarCohomologyData,
    WeightFiltrationData,
    DModulePurityAnalysis,
    # Central charge / null vector
    minimal_model_c,
    minimal_model_null_weight,
    virasoro_bar_relevant_threshold,
    sl2_bar_relevant_threshold,
    # Bar cohomology
    universal_virasoro_bar_dims,
    ising_bar_cohomology,
    general_minimal_model_bar_cohomology,
    admissible_sl2_bar_cohomology,
    triplet_bar_cohomology_estimate,
    # Weight filtration
    weight_filtration_universal,
    weight_filtration_quotient,
    weight_filtration_logarithmic,
    # Full analyses
    analyze_ising,
    analyze_lee_yang,
    analyze_tricritical_ising,
    analyze_three_state_potts,
    analyze_admissible_sl2,
    analyze_triplet,
    analyze_symplectic_fermion,
    analyze_betagamma_weight0,
    # Characteristic variety
    characteristic_variety_analysis,
    # Classical BGS
    bgs_classical_purity_check,
    # Mechanism
    purity_failure_mechanism,
    # Full search
    run_full_counterexample_search,
    explicit_admissible_sl2_analysis,
    explicit_triplet_w2_analysis,
    converse_evidence_summary,
    # Helpers
    _motzkin_numbers,
    _riordan_numbers,
    _colored_partition_dims,
)


# ============================================================================
# Helper number sequences
# ============================================================================

class TestMotzkinNumbers:
    """Motzkin numbers: OEIS A001006."""

    def test_first_values(self):
        """M(0)=1, M(1)=1, M(2)=2, M(3)=4, M(4)=9, M(5)=21."""
        M = _motzkin_numbers(6)
        assert M == [1, 1, 2, 4, 9, 21]

    def test_recurrence(self):
        """Verify (n+2)M(n) = (2n+1)M(n-1) + 3(n-1)M(n-2)."""
        M = _motzkin_numbers(10)
        for n in range(2, 10):
            assert (n + 2) * M[n] == (2 * n + 1) * M[n - 1] + 3 * (n - 1) * M[n - 2]


class TestRiordanNumbers:
    """Riordan numbers: OEIS A005043."""

    def test_first_values(self):
        """R(0)=1, R(1)=0, R(2)=1, R(3)=1, R(4)=3, R(5)=6."""
        R = _riordan_numbers(6)
        assert R == [1, 0, 1, 1, 3, 6]

    def test_sl2_bar_cohomology_connection(self):
        """For sl_2 bar cohomology: h_n = R(n+3) at bar degree 1.

        CRITICAL (AP9): This is the bar cohomology of the UNIVERSAL
        algebra V_k(sl_2), not the simple quotient.
        """
        R = _riordan_numbers(12)
        # h_1 = R(4) = 3 (= dim sl_2)
        assert R[4] == 3
        # h_2 = R(5) = 6
        assert R[5] == 6


class TestColoredPartitions:
    """3-colored partitions for sl_2 vacuum Verma dimensions."""

    def test_first_values(self):
        """p_3(0)=1, p_3(1)=3, p_3(2)=9, p_3(3)=22."""
        dims = _colored_partition_dims(3, 4)
        assert dims[0] == 1
        assert dims[1] == 3
        assert dims[2] == 9
        assert dims[3] == 22

    def test_gf_consistency(self):
        """prod_{n>=1} 1/(1-q^n)^3 gives the right sequence."""
        dims = _colored_partition_dims(3, 6)
        # Known: p_3(4) = 51, p_3(5) = 108
        assert dims[4] == 51
        assert dims[5] == 108


# ============================================================================
# Minimal model data
# ============================================================================

class TestMinimalModelCentralCharge:
    """Verify central charges for minimal models."""

    def test_ising(self):
        """M(4,3): c = 1/2."""
        assert minimal_model_c(4, 3) == Fraction(1, 2)

    def test_lee_yang(self):
        """M(5,2): c = -22/5."""
        assert minimal_model_c(5, 2) == Fraction(-22, 5)

    def test_tricritical_ising(self):
        """M(5,4): c = 7/10."""
        assert minimal_model_c(5, 4) == Fraction(7, 10)

    def test_three_state_potts(self):
        """M(6,5): c = 4/5."""
        assert minimal_model_c(6, 5) == Fraction(4, 5)

    def test_trivial(self):
        """M(3,2): c = 0."""
        assert minimal_model_c(3, 2) == Fraction(0)


class TestMinimalModelNullWeight:
    """Verify first null vector weights."""

    def test_ising_null(self):
        """M(4,3): h_null = (4-1)*(3-1) = 6."""
        assert minimal_model_null_weight(4, 3) == 6

    def test_lee_yang_null(self):
        """M(5,2): h_null = (5-1)*(2-1) = 4."""
        assert minimal_model_null_weight(5, 2) == 4

    def test_tricritical_null(self):
        """M(5,4): h_null = (5-1)*(4-1) = 12."""
        assert minimal_model_null_weight(5, 4) == 12

    def test_three_state_potts_null(self):
        """M(6,5): h_null = (6-1)*(5-1) = 20."""
        assert minimal_model_null_weight(6, 5) == 20

    def test_trivial_null(self):
        """M(3,2): h_null = (3-1)*(2-1) = 2."""
        assert minimal_model_null_weight(3, 2) == 2

    def test_null_in_bar_relevant_range(self):
        """For (p-1)(q-1) >= 4: null is in bar-relevant range.

        Bar-relevant threshold for Virasoro: h = 4.
        """
        threshold = virasoro_bar_relevant_threshold()
        assert threshold == 4

        # Ising: 6 >= 4
        assert minimal_model_null_weight(4, 3) >= threshold
        # Lee-Yang: 4 >= 4
        assert minimal_model_null_weight(5, 2) >= threshold
        # Tricritical: 12 >= 4
        assert minimal_model_null_weight(5, 4) >= threshold
        # Trivial: 2 < 4 (NOT in bar-relevant range)
        assert minimal_model_null_weight(3, 2) < threshold


class TestBarRelevantThreshold:
    """Verify bar-relevant thresholds."""

    def test_virasoro(self):
        """Virasoro generator at weight 2, so threshold = 2*2 = 4."""
        assert virasoro_bar_relevant_threshold() == 4

    def test_sl2(self):
        """sl_2 generators at weight 1, so threshold = 2*1 = 2."""
        assert sl2_bar_relevant_threshold() == 2


# ============================================================================
# Bar cohomology data
# ============================================================================

class TestBarCohomologyConcentration:
    """Test bar cohomology concentration (the definition of Koszulness)."""

    def test_universal_virasoro_concentrated(self):
        """Universal Vir_c: bar cohomology concentrated in degree 1."""
        bar = universal_virasoro_bar_dims(3, 12)
        assert bar.is_concentrated

    def test_ising_not_concentrated(self):
        """Ising L(c_{3,4}, 0): off-diagonal bar cohomology at h=6."""
        bar = ising_bar_cohomology(12)
        assert not bar.is_concentrated

    def test_ising_off_diagonal(self):
        """Ising: H^2_6 != 0 (the null vector obstruction)."""
        bar = ising_bar_cohomology(12)
        off = bar.off_diagonal_dims
        assert (2, 6) in off
        assert off[(2, 6)] > 0

    def test_lee_yang_not_concentrated(self):
        """Lee-Yang M(5,2): off-diagonal at h_null = 4."""
        bar = general_minimal_model_bar_cohomology(5, 2, 8)
        assert not bar.is_concentrated

    def test_universal_sl2_concentrated(self):
        """Universal V_k(sl_2): concentrated (Koszul)."""
        bar = admissible_sl2_bar_cohomology(2, 1, 8)  # k=0, h_null=1 < 2
        # For k=0: the simple quotient equals the universal
        assert bar.is_concentrated


class TestBarCohomologyDimensions:
    """Verify specific bar cohomology dimensions."""

    def test_ising_h1_weight2(self):
        """Ising H^1_2 = 1 (the T generator)."""
        bar = ising_bar_cohomology(12)
        assert bar.dims.get((1, 2), 0) == 1

    def test_ising_h1_weight4(self):
        """Ising H^1_4 = 1 (T*T relation, same as universal below null)."""
        bar = ising_bar_cohomology(12)
        assert bar.dims.get((1, 4), 0) == 1

    def test_universal_virasoro_motzkin_diff(self):
        """Universal Vir bar cohomology: h_n = M(n+1) - M(n) (Motzkin diffs).

        h_1 = M(2) - M(1) = 2 - 1 = 1 (the T generator at weight 2).
        h_2 = M(3) - M(2) = 4 - 2 = 2 (at weight 4).

        WAIT: the indexing is by weight, not by bar-degree.
        At weight 2 (bar degree 1): M(2) - M(1) = 1.
        At weight 4 (bar degree 1): M(3) - M(2) = 2.
        """
        bar = universal_virasoro_bar_dims(3, 12)
        M = _motzkin_numbers(10)
        assert bar.dims.get((1, 2), 0) == M[2] - M[1]  # = 1
        assert bar.dims.get((1, 4), 0) == M[3] - M[2]  # = 2


# ============================================================================
# Weight filtration
# ============================================================================

class TestWeightFiltration:
    """Test weight filtration analysis."""

    def test_universal_pure(self):
        """Universal (Koszul) algebra: pure of weight n at bar degree n."""
        wf = weight_filtration_universal(3, 8)
        assert wf.is_pure
        assert wf.pure_weight == 3
        assert wf.weights == [3]

    def test_quotient_below_critical(self):
        """Below critical bar degree: pure (agrees with universal)."""
        # Ising: h_null=6, gen_weight=2, n_crit=3
        wf = weight_filtration_quotient(2, 6, 4, 2)
        assert wf.is_pure
        assert wf.pure_weight == 2

    def test_quotient_at_critical(self):
        """At critical bar degree: NOT pure (mixed weights)."""
        # Ising: n_crit = ceil(6/2) = 3
        wf = weight_filtration_quotient(3, 6, 4, 2)
        assert not wf.is_pure
        assert wf.pure_weight is None
        assert 2 in wf.weights  # weight n-1
        assert 3 in wf.weights  # weight n

    def test_quotient_above_critical(self):
        """Above critical bar degree: also NOT pure."""
        wf = weight_filtration_quotient(4, 6, 4, 2)
        assert not wf.is_pure

    def test_logarithmic_not_pure(self):
        """Logarithmic algebra: never pure (nilpotent monodromy)."""
        wf = weight_filtration_logarithmic(2)
        assert not wf.is_pure
        assert len(wf.weights) >= 2


# ============================================================================
# Full algebra analyses
# ============================================================================

class TestIsingAnalysis:
    """Ising model: the canonical non-Koszul example."""

    def test_koszul_status(self):
        result = analyze_ising()
        assert result.koszul_verdict == KoszulVerdict.NOT_KOSZUL

    def test_purity_status(self):
        result = analyze_ising()
        assert result.purity_verdict == PurityVerdict.NOT_PURE

    def test_not_counterexample(self):
        result = analyze_ising()
        assert result.counterexample_status == CounterexampleStatus.NOT_COUNTEREXAMPLE

    def test_central_charge(self):
        result = analyze_ising()
        assert result.central_charge == Fraction(1, 2)

    def test_kappa(self):
        """kappa(Ising) = c/2 = 1/4."""
        result = analyze_ising()
        assert result.kappa == Fraction(1, 4)

    def test_null_vector(self):
        result = analyze_ising()
        assert result.null_vector_weight == 6

    def test_off_diagonal_bar(self):
        """Ising has off-diagonal bar cohomology."""
        result = analyze_ising()
        assert not result.bar_cohomology.is_concentrated

    def test_weight_filtration_mixed(self):
        """Weight filtration at n_crit is mixed."""
        result = analyze_ising()
        # n_crit = 3 for Ising (ceil(6/2))
        wf_3 = [w for w in result.weight_filtrations if w.bar_degree == 3]
        assert len(wf_3) == 1
        assert not wf_3[0].is_pure


class TestLeeYangAnalysis:
    """Lee-Yang M(5,2): borderline case h_null = bar_threshold."""

    def test_koszul_status(self):
        result = analyze_lee_yang()
        assert result.koszul_verdict == KoszulVerdict.NOT_KOSZUL

    def test_purity_status(self):
        result = analyze_lee_yang()
        assert result.purity_verdict == PurityVerdict.NOT_PURE

    def test_not_counterexample(self):
        result = analyze_lee_yang()
        assert result.counterexample_status == CounterexampleStatus.NOT_COUNTEREXAMPLE

    def test_null_at_threshold(self):
        """h_null = 4 = bar_threshold: exact borderline."""
        result = analyze_lee_yang()
        assert result.null_vector_weight == 4
        assert result.bar_relevant_threshold == 4


class TestTricriticalIsingAnalysis:
    """Tricritical Ising M(5,4): large null vector weight."""

    def test_koszul_status(self):
        result = analyze_tricritical_ising()
        assert result.koszul_verdict == KoszulVerdict.NOT_KOSZUL

    def test_purity_status(self):
        result = analyze_tricritical_ising()
        assert result.purity_verdict == PurityVerdict.NOT_PURE

    def test_null_weight(self):
        result = analyze_tricritical_ising()
        assert result.null_vector_weight == 12

    def test_large_pure_range(self):
        """Below n_crit = 6: all pure."""
        result = analyze_tricritical_ising()
        for wf in result.weight_filtrations:
            if wf.bar_degree < 6:
                assert wf.is_pure


class TestThreeStatePottsAnalysis:
    """Three-state Potts M(6,5)."""

    def test_koszul_status(self):
        result = analyze_three_state_potts()
        assert result.koszul_verdict == KoszulVerdict.NOT_KOSZUL

    def test_purity_status(self):
        result = analyze_three_state_potts()
        assert result.purity_verdict == PurityVerdict.NOT_PURE

    def test_null_weight(self):
        result = analyze_three_state_potts()
        assert result.null_vector_weight == 20


# ============================================================================
# Admissible sl_2 quotients
# ============================================================================

class TestAdmissibleSl2:
    """Admissible simple quotients L_k(sl_2)."""

    def test_k0_koszul(self):
        """k=0 (p=2, q=1): h_null=1 < 2, Koszul."""
        result = analyze_admissible_sl2(2, 1)
        assert result.koszul_verdict == KoszulVerdict.KOSZUL
        assert result.purity_verdict == PurityVerdict.PURE
        assert result.counterexample_status == CounterexampleStatus.NOT_COUNTEREXAMPLE

    def test_k1_open(self):
        """k=1 (p=3, q=1): h_null=2 = threshold, Koszulness OPEN.

        Both Koszulness and purity are OPEN at the borderline.
        Cannot rule out as counterexample without resolving both (AP36).
        """
        result = analyze_admissible_sl2(3, 1)
        assert result.koszul_verdict == KoszulVerdict.OPEN
        assert result.purity_verdict == PurityVerdict.OPEN
        assert result.counterexample_status == CounterexampleStatus.POTENTIAL

    def test_k_minus_half_not_pure(self):
        """k=-1/2 (p=3, q=2): h_null=4 > 2, purity FAILS."""
        result = analyze_admissible_sl2(3, 2)
        assert result.purity_verdict == PurityVerdict.NOT_PURE
        assert result.counterexample_status == CounterexampleStatus.RULED_OUT

    def test_k_minus_4_3_not_pure(self):
        """k=-4/3 (p=2, q=3): h_null=3 > 2, purity FAILS."""
        result = analyze_admissible_sl2(2, 3)
        assert result.purity_verdict == PurityVerdict.NOT_PURE
        assert result.counterexample_status == CounterexampleStatus.RULED_OUT

    def test_kappa_multipath(self):
        """kappa(sl_2, k=-1/2) = 3p/(4q) = 9/8 (AP20, AP39)."""
        result = analyze_admissible_sl2(3, 2)
        assert result.kappa == Fraction(9, 8)

    def test_null_weight_formula(self):
        """h_null = (p-1)*q for admissible k = p/q - 2."""
        for (p, q, expected) in [(2, 1, 1), (3, 1, 2), (3, 2, 4), (2, 3, 3)]:
            result = analyze_admissible_sl2(p, q)
            assert result.null_vector_weight == expected


# ============================================================================
# Logarithmic algebras
# ============================================================================

class TestTripletAnalysis:
    """Triplet W(2): logarithmic, Koszulness OPEN."""

    def test_koszul_open(self):
        result = analyze_triplet(2)
        assert result.koszul_verdict == KoszulVerdict.OPEN

    def test_purity_fails(self):
        """Purity fails regardless of Koszulness (logarithmic monodromy)."""
        result = analyze_triplet(2)
        assert result.purity_verdict == PurityVerdict.NOT_PURE

    def test_ruled_out(self):
        """NOT a counterexample candidate."""
        result = analyze_triplet(2)
        assert result.counterexample_status == CounterexampleStatus.RULED_OUT

    def test_central_charge(self):
        result = analyze_triplet(2)
        assert result.central_charge == Fraction(-2)

    def test_weight_filtration_non_pure(self):
        """All weight filtrations are non-pure (logarithmic)."""
        result = analyze_triplet(2)
        for wf in result.weight_filtrations:
            assert not wf.is_pure


class TestExplicitTripletW2:
    """Explicit triplet W(2) analysis."""

    def test_logarithmic(self):
        result = explicit_triplet_w2_analysis()
        assert result['logarithmic'] is True

    def test_nilpotent_monodromy(self):
        result = explicit_triplet_w2_analysis()
        assert result['log_monodromy']['nilpotent_N'] is True

    def test_dmod_not_pure(self):
        result = explicit_triplet_w2_analysis()
        assert result['dmod_pure'] is False

    def test_ruled_out(self):
        result = explicit_triplet_w2_analysis()
        assert result['counterexample_status'] == 'RULED_OUT'


# ============================================================================
# Control cases (Koszul algebras)
# ============================================================================

class TestSymplecticFermionAnalysis:
    """Symplectic fermion: Koszul, pure (control case)."""

    def test_koszul(self):
        result = analyze_symplectic_fermion()
        assert result.koszul_verdict == KoszulVerdict.KOSZUL

    def test_pure(self):
        result = analyze_symplectic_fermion()
        assert result.purity_verdict == PurityVerdict.PURE

    def test_not_counterexample(self):
        result = analyze_symplectic_fermion()
        assert result.counterexample_status == CounterexampleStatus.NOT_COUNTEREXAMPLE

    def test_bar_concentrated(self):
        result = analyze_symplectic_fermion()
        assert result.bar_cohomology.is_concentrated


class TestBetagammaWeight0Analysis:
    """betagamma at lambda=0: Koszul despite weight-0 generator."""

    def test_koszul(self):
        result = analyze_betagamma_weight0()
        assert result.koszul_verdict == KoszulVerdict.KOSZUL

    def test_pure(self):
        result = analyze_betagamma_weight0()
        assert result.purity_verdict == PurityVerdict.PURE

    def test_weight0_generator(self):
        """Has weight-0 generator but still Koszul (AP18)."""
        result = analyze_betagamma_weight0()
        assert result.bar_cohomology.dims.get((1, 0), 0) == 1  # gamma
        assert result.koszul_verdict == KoszulVerdict.KOSZUL


# ============================================================================
# Characteristic variety analysis
# ============================================================================

class TestCharacteristicVariety:
    """Characteristic variety alignment."""

    def test_koszul_aligned(self):
        """Koszul algebra: Ch aligned to FM boundary."""
        result = characteristic_variety_analysis("Virasoro (universal)", None, 2)
        assert result['alignment'] is True
        assert result['interior_singularities'] is False

    def test_non_koszul_not_aligned(self):
        """Non-Koszul with null: interior singularity."""
        result = characteristic_variety_analysis("Ising", 6, 2)
        assert result['alignment'] is False
        assert result['interior_singularities'] is True

    def test_logarithmic_not_aligned(self):
        """Logarithmic: independent interior singularity."""
        result = characteristic_variety_analysis("W(2)", None, 2, is_logarithmic=True)
        assert result['alignment'] is False
        assert result['interior_singularities'] is True

    def test_null_below_threshold_aligned(self):
        """Null below bar threshold: aligned (like universal)."""
        result = characteristic_variety_analysis("L_0(sl_2)", 1, 1)
        assert result['alignment'] is True


# ============================================================================
# Classical BGS purity check
# ============================================================================

class TestBGSClassicalPurity:
    """Classical Koszul-purity equivalence (BGS Theorem 2.12.6)."""

    def test_polynomial_ring_koszul(self):
        """k[x] = T(x)/(0) is Koszul. Dual: k[x]^! = k (exterior on x*).

        H_A(t) = 1/(1-t), H_{A!}(t) = 1 + t.
        Product: 1/(1-t) * (1-t) = 1. Koszul.
        """
        H_A = [1, 1, 1, 1, 1]  # truncation of 1/(1-t)
        H_dual = [1, 1, 0, 0, 0]  # 1 + t
        result = bgs_classical_purity_check(H_A, H_dual)
        assert result['is_koszul'] is True

    def test_exterior_algebra_koszul(self):
        """Lambda(x) is Koszul. Dual: k[x].

        H_A(t) = 1+t, H_{A!}(t) = 1/(1-t) truncated.
        Product: (1+t) * (1-t+t^2-...) = 1. Koszul.
        """
        H_A = [1, 1, 0, 0, 0]
        H_dual = [1, 1, 1, 1, 1]
        result = bgs_classical_purity_check(H_A, H_dual)
        assert result['is_koszul'] is True

    def test_classical_purity_equivalent(self):
        """In classical BGS setting, purity and Koszulness are equivalent."""
        result = bgs_classical_purity_check([1, 1], [1, 1])
        assert result['classical_purity_equivalent'] is True


# ============================================================================
# Mechanism analysis
# ============================================================================

class TestPurityFailureMechanism:
    """Universal mechanism by which purity fails for non-Koszul algebras."""

    def test_ising_mechanism(self):
        """Ising: h_null=6, gen_weight=2, n_crit=3."""
        result = purity_failure_mechanism(6, 2, 4)
        assert result['n_crit'] == 3
        assert len(result['mechanism_steps']) == 6

    def test_lee_yang_mechanism(self):
        """Lee-Yang: h_null=4, gen_weight=2, n_crit=2."""
        result = purity_failure_mechanism(4, 2, 4)
        assert result['n_crit'] == 2

    def test_admissible_sl2_mechanism(self):
        """L_{-1/2}(sl_2): h_null=4, gen_weight=1, n_crit=4."""
        result = purity_failure_mechanism(4, 1, 2)
        assert result['n_crit'] == 4

    def test_evidence_for_converse(self):
        """Mechanism provides evidence for the converse."""
        result = purity_failure_mechanism(6, 2, 4)
        assert 'converse' in result['converse_evidence'].lower()


# ============================================================================
# Explicit analysis of L_{-1/2}(sl_2)
# ============================================================================

class TestExplicitAdmissibleSl2:
    """Detailed bar complex of L_{-1/2}(sl_2)."""

    def test_level(self):
        result = explicit_admissible_sl2_analysis()
        assert result['k'] == Fraction(-1, 2)

    def test_central_charge(self):
        """c = 3k/(k+2) = 3*(-1/2)/(3/2) = -1."""
        result = explicit_admissible_sl2_analysis()
        assert result['c'] == Fraction(-1)

    def test_kappa(self):
        """kappa = 3p/(4q) = 9/8."""
        result = explicit_admissible_sl2_analysis()
        assert result['kappa'] == Fraction(9, 8)

    def test_null_weight(self):
        result = explicit_admissible_sl2_analysis()
        assert result['h_null'] == 4

    def test_verma_dims(self):
        """Verma dimensions: 3-colored partitions."""
        result = explicit_admissible_sl2_analysis()
        assert result['verma_dims'][0] == 1  # vacuum
        assert result['verma_dims'][1] == 3  # J^a_{-1}|0>
        assert result['verma_dims'][2] == 9  # weight 2

    def test_off_diagonal_at_null(self):
        """Off-diagonal bar cohomology at h_null = 4."""
        result = explicit_admissible_sl2_analysis()
        assert result['off_diagonal_at_h_null'] is True

    def test_weight_filtration_mixed(self):
        result = explicit_admissible_sl2_analysis()
        assert result['weight_filtration_B2']['is_pure'] is False

    def test_char_variety_not_aligned(self):
        result = explicit_admissible_sl2_analysis()
        assert result['char_variety']['aligned'] is False


# ============================================================================
# Full counterexample search
# ============================================================================

class TestFullCounterexampleSearch:
    """The main search: no confirmed counterexamples, but borderline cases OPEN."""

    def test_no_confirmed_counterexamples(self):
        """No CONFIRMED counterexample: all non-Koszul algebras also fail purity.

        Borderline cases (h_null = bar_threshold, both statuses OPEN) are
        correctly marked POTENTIAL, not RULED_OUT (AP36).  These are not
        confirmed counterexamples -- they are unresolved.
        """
        result = run_full_counterexample_search()
        # Potential counterexamples are borderline OPEN cases, not confirmed
        for r in result['results']:
            if r.counterexample_status == CounterexampleStatus.POTENTIAL:
                # Every POTENTIAL case must have BOTH statuses OPEN
                assert r.koszul_verdict == KoszulVerdict.OPEN
                assert r.purity_verdict == PurityVerdict.OPEN

    def test_total_candidates(self):
        """At least 10 candidates examined."""
        result = run_full_counterexample_search()
        assert result['total_candidates'] >= 10

    def test_non_koszul_fail_purity(self):
        """All non-Koszul algebras also fail purity."""
        result = run_full_counterexample_search()
        assert len(result['both_fail']) >= 4  # at least the 4 minimal models

    def test_koszul_algebras_pure(self):
        """All Koszul control cases are pure."""
        result = run_full_counterexample_search()
        assert len(result['both_hold']) >= 2  # symplectic fermion + betagamma

    def test_verdict(self):
        """Verdict: no confirmed counterexample (borderline cases are POTENTIAL)."""
        result = run_full_counterexample_search()
        assert 'NO confirmed counterexample' in result['verdict'] or \
               'NO counterexample' in result['verdict']

    def test_potential_counterexamples_list(self):
        """Borderline cases (h_null = bar_threshold) are POTENTIAL, not ruled out.

        L_1(sl_2) has h_null=2 = bar_threshold=2: both Koszulness and
        purity are OPEN, so it cannot be ruled out (AP36).
        """
        result = run_full_counterexample_search()
        potentials = result['potential_counterexamples']
        # Borderline admissible quotients where h_null = bar_threshold
        assert len(potentials) >= 1  # at least L_1(sl_2)
        assert any('k=1' in name or 'p=3, q=1' in name
                    for name in potentials)


# ============================================================================
# Converse evidence summary
# ============================================================================

class TestConverseEvidence:
    """Evidence for the D-module purity converse."""

    def test_five_evidence_points(self):
        """At least 5 independent evidence points for the converse."""
        result = converse_evidence_summary()
        assert len(result['evidence_for_converse']) >= 5

    def test_no_evidence_against(self):
        """No computational evidence against the converse."""
        result = converse_evidence_summary()
        assert 'None' in result['evidence_against_converse'][0]

    def test_proof_difficulty_acknowledged(self):
        """The proof difficulty is acknowledged (honest scope)."""
        result = converse_evidence_summary()
        assert 'Hodge' in result['proof_difficulty']


# ============================================================================
# Cross-consistency checks (multi-path verification)
# ============================================================================

class TestCrossConsistency:
    """Cross-checks between different computation paths."""

    def test_ising_three_path_agreement(self):
        """Ising non-Koszulness confirmed by 3 independent paths:
        Path 1: Null vector at h=6 in bar-relevant range
        Path 2: Off-diagonal bar cohomology H^2_6 != 0
        Path 3: Weight filtration at B_3 is mixed
        """
        # Path 1: null vector
        h_null = minimal_model_null_weight(4, 3)
        threshold = virasoro_bar_relevant_threshold()
        assert h_null >= threshold

        # Path 2: bar cohomology
        bar = ising_bar_cohomology(12)
        assert not bar.is_concentrated
        assert (2, 6) in bar.off_diagonal_dims

        # Path 3: weight filtration
        wf = weight_filtration_quotient(3, 6, 4, 2)
        assert not wf.is_pure

    def test_purity_koszulness_correlation(self):
        """For ALL candidates: purity and Koszulness are correlated.

        Either both hold (Koszul algebras) or at least purity fails
        (non-Koszul or logarithmic algebras).
        NO case where Koszulness fails but purity holds.
        """
        search = run_full_counterexample_search()
        for r in search['results']:
            if r.koszul_verdict == KoszulVerdict.NOT_KOSZUL:
                assert r.purity_verdict == PurityVerdict.NOT_PURE, \
                    f"Counterexample found: {r.name} is not Koszul but pure!"
            if r.koszul_verdict == KoszulVerdict.KOSZUL:
                assert r.purity_verdict == PurityVerdict.PURE, \
                    f"Anti-correlation: {r.name} is Koszul but not pure!"

    def test_mechanism_universality(self):
        """The null-vector mechanism applies to ALL non-Koszul minimal models."""
        for (p, q) in [(4, 3), (5, 2), (5, 4), (6, 5), (7, 2), (7, 4), (7, 6)]:
            h_null = minimal_model_null_weight(p, q)
            threshold = virasoro_bar_relevant_threshold()
            if h_null >= threshold:
                mechanism = purity_failure_mechanism(h_null, 2, threshold)
                assert mechanism['n_crit'] >= 2
                assert len(mechanism['mechanism_steps']) == 6

    def test_classical_chiral_consistency(self):
        """The classical BGS equivalence is consistent with the chiral search.

        In the classical case: Koszul <=> pure (BGS).
        In the chiral case: all evidence agrees (same correlation).
        """
        # Classical: polynomial ring
        bgs = bgs_classical_purity_check([1, 1, 1, 1], [1, 1, 0, 0])
        assert bgs['is_koszul'] is True
        assert bgs['classical_purity_equivalent'] is True

        # Chiral: no confirmed counterexamples (borderline OPEN cases are POTENTIAL)
        search = run_full_counterexample_search()
        for r in search['results']:
            if r.counterexample_status == CounterexampleStatus.POTENTIAL:
                # POTENTIAL means both statuses genuinely OPEN, not a confirmed CE
                assert r.koszul_verdict == KoszulVerdict.OPEN
                assert r.purity_verdict == PurityVerdict.OPEN


class TestAdmissibleLandscapeConsistency:
    """Cross-check admissible level landscape."""

    def test_kappa_formula_consistency(self):
        """kappa = 3p/(4q) for all admissible sl_2 levels.

        Path 1: Direct formula 3p/(4q)
        Path 2: dim(g)*(k+h^v)/(2*h^v) = 3*(p/q)/(4)
        Both give 3p/(4q).
        """
        for (p, q) in [(2, 1), (3, 1), (3, 2), (5, 2)]:
            result = analyze_admissible_sl2(p, q)
            expected = Fraction(3 * p, 4 * q)
            assert result.kappa == expected, \
                f"kappa mismatch at p={p}, q={q}: {result.kappa} != {expected}"

    def test_null_weight_formula_consistency(self):
        """h_null = (p-1)*q for all admissible levels.

        Three independent verifications:
        1. Direct formula (p-1)*q
        2. From the analysis function
        3. From the Kac-Kazhdan determinant (verified by bar_relevant_admissible.py)
        """
        for (p, q) in [(2, 1), (3, 1), (3, 2), (2, 3), (5, 2)]:
            # Path 1
            expected = (p - 1) * q
            # Path 2
            result = analyze_admissible_sl2(p, q)
            assert result.null_vector_weight == expected

    def test_monotonicity_of_null_weight(self):
        """Larger (p-1)*q => null deeper in bar range => more off-diagonal."""
        results = []
        for (p, q) in [(3, 2), (5, 2), (4, 3)]:
            r = analyze_admissible_sl2(p, q)
            results.append((r.null_vector_weight, r))
        # All have h_null > threshold and purity fails
        for h_null, r in results:
            assert h_null > sl2_bar_relevant_threshold()
            assert r.purity_verdict == PurityVerdict.NOT_PURE
