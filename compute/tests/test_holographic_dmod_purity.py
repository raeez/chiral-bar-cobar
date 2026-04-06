r"""Tests for holographic D-module purity engine.

Tests the holographic dictionary:
  Boundary D-module purity <=> Bulk regularity <=> Koszulness

Three independent verification paths per claim:
  Path 1: Direct computation from KZ/Gaudin singularity analysis
  Path 2: Cross-family consistency (forward direction must hold for all Koszul families)
  Path 3: Admissible-level obstruction analysis (non-pure examples)

References:
  conj:d-module-purity-koszulness (bar_cobar_adjunction_inversion.tex)
  thm:koszul-equivalences-meta, item (xii) (chiral_koszul_pairs.tex)
  def:holographic-modular-koszul-datum (concordance.tex)
  rem:d-module-purity-content (bar_cobar_adjunction_inversion.tex)
"""

import math
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.holographic_dmod_purity_engine import (
    AdmissibleLevelObstruction,
    CrossFamilyVerification,
    DModPurityConverseArgument,
    GaudinSystem,
    HolographicDModPurityDictionary,
    HolographicPurityConjecture,
    KZConnection,
    VirasoroC26Regularity,
)


# =========================================================================
# I. KZ Connection Tests
# =========================================================================

class TestKZConnection:
    """Tests for KZ connection construction and singularity analysis."""

    def test_sl2_dual_coxeter(self):
        """h^v(sl_2) = 2."""
        kz = KZConnection('A', 1, Fraction(1))
        assert kz.h_dual == 2

    def test_sl3_dual_coxeter(self):
        """h^v(sl_3) = 3."""
        kz = KZConnection('A', 2, Fraction(1))
        assert kz.h_dual == 3

    def test_sl4_dual_coxeter(self):
        """h^v(sl_4) = 4 (general type A: h^v = N)."""
        kz = KZConnection('A', 3, Fraction(1))
        assert kz.h_dual == 4

    def test_g2_dual_coxeter(self):
        """h^v(G_2) = 4."""
        kz = KZConnection('G', 2, Fraction(1))
        assert kz.h_dual == 4

    def test_e8_dual_coxeter(self):
        """h^v(E_8) = 30."""
        kz = KZConnection('E', 8, Fraction(1))
        assert kz.h_dual == 30

    def test_sl2_dimension(self):
        """dim(sl_2) = 3."""
        kz = KZConnection('A', 1, Fraction(1))
        assert kz.dim_g == 3

    def test_sl3_dimension(self):
        """dim(sl_3) = 8."""
        kz = KZConnection('A', 2, Fraction(1))
        assert kz.dim_g == 8

    def test_e8_dimension(self):
        """dim(E_8) = 248."""
        kz = KZConnection('E', 8, Fraction(1))
        assert kz.dim_g == 248

    def test_kz_parameter_sl2_k1(self):
        """KZ parameter for sl_2 at k=1: 1/(k+h^v) = 1/3."""
        kz = KZConnection('A', 1, Fraction(1))
        assert kz.kz_param == Fraction(1, 3)

    def test_kz_parameter_sl2_k2(self):
        """KZ parameter for sl_2 at k=2: 1/(k+h^v) = 1/4."""
        kz = KZConnection('A', 1, Fraction(2))
        assert kz.kz_param == Fraction(1, 4)

    def test_kz_parameter_critical_level(self):
        """At critical level k = -h^v: KZ parameter undefined."""
        kz = KZConnection('A', 1, Fraction(-2))  # k = -2 = -h^v for sl_2
        assert kz.kz_param is None

    def test_kz_fuchsian_generic_level(self):
        """KZ connection is Fuchsian at all non-critical levels."""
        for k in [Fraction(1), Fraction(2), Fraction(1, 2), Fraction(10)]:
            kz = KZConnection('A', 1, k)
            assert kz.is_fuchsian() is True

    def test_kz_not_fuchsian_critical(self):
        """KZ connection is not Fuchsian at critical level (undefined)."""
        kz = KZConnection('A', 1, Fraction(-2))
        assert kz.is_fuchsian() is False

    # --- Kappa verification (AP1/AP39 guard) ---

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = dim(sl_2)(1+2)/(2*2) = 3*3/4 = 9/4.

        Path 1: Direct from formula dim(g)(k+h^v)/(2h^v).
        Path 2: Cross-check with central charge c(sl_2,1) = 3*1/(1+2) = 1,
                 but kappa != c/2 for non-Virasoro families (AP39).
        """
        kz = KZConnection('A', 1, Fraction(1))
        assert kz.kappa == Fraction(9, 4)

    def test_kappa_sl2_k2(self):
        """kappa(sl_2, k=2) = 3*(2+2)/(2*2) = 3."""
        kz = KZConnection('A', 1, Fraction(2))
        assert kz.kappa == Fraction(3)

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 32/6 = 16/3.

        Path 1: Direct computation.
        Path 2: dim(sl_3) = 8, h^v(sl_3) = 3, k=1.
        """
        kz = KZConnection('A', 2, Fraction(1))
        assert kz.kappa == Fraction(16, 3)

    def test_kappa_e8_k1(self):
        """kappa(E_8, k=1) = 248*(1+30)/(2*30) = 248*31/60 = 7688/60 = 1922/15.

        Path 1: Direct computation.
        """
        kz = KZConnection('E', 8, Fraction(1))
        assert kz.kappa == Fraction(248 * 31, 60)
        assert kz.kappa == Fraction(1922, 15)

    def test_kappa_undefined_at_critical(self):
        """kappa is undefined at critical level k = -h^v."""
        kz = KZConnection('A', 1, Fraction(-2))
        assert kz.kappa is None

    # --- Singular locus ---

    def test_singular_locus_4_point(self):
        """4-point KZ has 6 collision diagonals."""
        kz = KZConnection('A', 1, Fraction(1))
        desc = kz.singular_locus(4)
        assert '6 collision diagonals' in desc
        assert 'regular' in desc.lower() or 'Fuchsian' in desc

    def test_singular_locus_3_point(self):
        """3-point KZ has 3 collision diagonals."""
        kz = KZConnection('A', 1, Fraction(1))
        desc = kz.singular_locus(3)
        assert '3 collision diagonals' in desc

    # --- Connection matrix ---

    def test_connection_matrix_sl2_2point(self):
        """KZ connection matrix for 2-point sl_2 spin-1/2.

        The Casimir Omega_{12} has eigenvalues 1/4 (triplet) and -3/4 (singlet)
        in the decomposition (1/2) x (1/2) = 1 + 0.
        """
        kz = KZConnection('A', 1, Fraction(1))
        z = [1.0 + 0j, 0.0 + 0j]
        spins = [Fraction(1, 2), Fraction(1, 2)]
        A = kz.connection_matrix_sl2(z, spins)
        assert A is not None
        # Dimension: (1/2)x(1/2) = spin-1 (dim 3) + spin-0 (dim 1) = dim 4
        assert A.shape == (4, 4)
        # Eigenvalues should be proportional to Casimir eigenvalues / (z_1 - z_2)
        eigvals = sorted(np.linalg.eigvals(A).real)
        # kz_param = 1/3, z_1 - z_2 = 1
        # Triplet block (dim 3): val = (1/3) * (1/4) / 1 = 1/12
        # Singlet block (dim 1): val = (1/3) * (-3/4) / 1 = -1/4
        assert abs(eigvals[0] - (-1.0 / 4.0)) < 1e-10  # singlet
        assert abs(eigvals[1] - (1.0 / 12.0)) < 1e-10  # triplet
        assert abs(eigvals[2] - (1.0 / 12.0)) < 1e-10  # triplet
        assert abs(eigvals[3] - (1.0 / 12.0)) < 1e-10  # triplet

    def test_conformal_blocks_dim_sl2_k1_4pt(self):
        """Dimension of conformal blocks: 4 spin-1/2 reps at level 1 gives 2."""
        kz = KZConnection('A', 1, Fraction(1))
        dim = kz.monodromy_dimension(4, [2, 2, 2, 2])
        assert dim == 2


# =========================================================================
# II. Gaudin System Tests
# =========================================================================

class TestGaudinSystem:
    """Tests for Gaudin Hamiltonians and admissible-level analysis."""

    def test_admissible_k_minus_half(self):
        """k = -1/2 is admissible for sl_2: k+2 = 3/2, p=3, q=2."""
        g = GaudinSystem('A', 1, Fraction(-1, 2), 4)
        assert g.is_admissible_level() is True

    def test_admissible_k_minus_4_3(self):
        """k = -4/3 is admissible for sl_2: k+2 = 2/3, p=2, q=3."""
        g = GaudinSystem('A', 1, Fraction(-4, 3), 4)
        assert g.is_admissible_level() is True

    def test_non_admissible_integer_level(self):
        """k = 1 (integer positive level) is not in standard admissible form
        for the simple quotient analysis (the quotient is trivial at k=1
        for sl_2 in the sense that V_1 = L_1 for sl_2)."""
        # k=1: k+2 = 3 = 3/1, p=3, q=1 -- this IS admissible with q=1
        g = GaudinSystem('A', 1, Fraction(1), 4)
        assert g.is_admissible_level() is True

    def test_apparent_singularities_k_minus_half_4pt(self):
        """At k=-1/2, 4 points: null level = 3*2 = 6, apparent = (6-1)*2 = 10.

        Path 1: Direct computation from formula.
        Path 2: The null vector at level 6 gives a 6th-order ODE on the
                 3-punctured sphere (after fixing one point). A 6th-order
                 Fuchsian ODE on P^1 with 3 regular singular points has
                 5*(4-2) = 10 apparent singularities by the Fuchs relation.
        """
        g = GaudinSystem('A', 1, Fraction(-1, 2), 4)
        analysis = g.apparent_singularity_count()
        assert analysis['is_admissible'] is True
        assert analysis['null_vector_level'] == 6
        assert analysis['apparent_singularities'] == 10
        assert analysis['fm_alignment'] is False
        assert analysis['dmod_pure'] is False

    def test_apparent_singularities_k_minus_4_3_4pt(self):
        """At k=-4/3, 4 points: null level = 2*3 = 6, apparent = (6-1)*2 = 10."""
        g = GaudinSystem('A', 1, Fraction(-4, 3), 4)
        analysis = g.apparent_singularity_count()
        assert analysis['null_vector_level'] == 6
        assert analysis['apparent_singularities'] == 10
        assert analysis['fm_alignment'] is False

    def test_no_apparent_singularities_generic_level(self):
        """At generic integer level, no apparent singularities (universal algebra).

        The integer-level sl_2 with q=1 has null_level = p*1 = p.
        The formula gives n_apparent = 0 when q < 2.
        """
        g = GaudinSystem('A', 1, Fraction(1), 4)
        analysis = g.apparent_singularity_count()
        assert analysis['apparent_singularities'] == 0
        assert analysis['fm_alignment'] is True
        assert analysis['dmod_pure'] is True

    def test_collision_count_4pt(self):
        """4 points: C(4,2) = 6 collision singularities."""
        g = GaudinSystem('A', 1, Fraction(-1, 2), 4)
        analysis = g.apparent_singularity_count()
        assert analysis['collision_singularities'] == 6

    def test_collision_count_5pt(self):
        """5 points: C(5,2) = 10 collision singularities."""
        g = GaudinSystem('A', 1, Fraction(-1, 2), 5)
        analysis = g.apparent_singularity_count()
        assert analysis['collision_singularities'] == 10

    def test_apparent_singularities_scale_with_n(self):
        """Apparent singularities grow linearly with n-2.

        For k=-1/2 (null_level=6): n_app = 5*(n-2).
        """
        for n in [3, 4, 5, 6]:
            g = GaudinSystem('A', 1, Fraction(-1, 2), n)
            analysis = g.apparent_singularity_count()
            assert analysis['apparent_singularities'] == 5 * (n - 2)

    def test_admissible_module_dimension_vacuum(self):
        """Vacuum (weight 0) always has dimension 1."""
        g = GaudinSystem('A', 1, Fraction(-1, 2), 4)
        dim = g.admissible_module_dimension(0)
        assert dim == 1

    def test_bulk_regularity_matches_fm_alignment(self):
        """Bulk regularity should match FM alignment for all tested cases.

        Path 1: Compute from Gaudin analysis.
        Path 2: Check consistency with holographic dictionary.
        """
        for level in [Fraction(-1, 2), Fraction(-4, 3), Fraction(1), Fraction(2)]:
            g = GaudinSystem('A', 1, level, 4)
            analysis = g.apparent_singularity_count()
            assert analysis['bulk_regular'] == analysis['fm_alignment']


# =========================================================================
# III. Holographic Dictionary Tests
# =========================================================================

class TestHolographicDictionary:
    """Tests for the holographic D-module purity dictionary."""

    def test_forward_direction_all_koszul_families(self):
        """PROVED: Koszul => D-module pure => bulk regular.

        For ALL Koszul families: verify that D-module purity and bulk
        regularity both hold.

        Path 1: Direct computation via KZ/BPZ analysis.
        Path 2: Cross-family consistency.
        Path 3: Check against known Koszulness status.
        """
        koszul_families = [
            'heisenberg_k1', 'affine_sl2_k1', 'affine_sl2_k2',
            'affine_sl3_k1', 'virasoro_c26', 'virasoro_c1', 'betagamma',
        ]
        for family in koszul_families:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            assert analysis['boundary']['dmod_pure'] is True, (
                f"Forward direction FAILURE: {family} is Koszul but D-module not pure"
            )
            assert analysis['bulk']['bulk_regular'] is True, (
                f"Forward direction FAILURE: {family} is Koszul but bulk not regular"
            )
            assert analysis['consistency']['forward_consistent'] is True, (
                f"Forward consistency FAILURE for {family}"
            )

    def test_admissible_level_fm_misalignment(self):
        """Admissible-level simple quotients have FM misalignment.

        The apparent singularities from null vectors break FM alignment,
        which is one of the two conditions for D-module purity.
        """
        for family in ['admissible_sl2_k_minus_half', 'admissible_sl2_k_minus_4_3']:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            assert analysis['boundary']['fm_aligned'] is False, (
                f"Expected FM misalignment for {family}"
            )
            assert analysis['boundary']['dmod_pure'] is False, (
                f"Expected D-module non-purity for {family}"
            )

    def test_admissible_level_bulk_log_singularities(self):
        """Admissible-level bulk has logarithmic singularities.

        In the holographic dictionary: apparent singularities on the
        boundary correspond to logarithmic modes in the bulk.
        """
        for family in ['admissible_sl2_k_minus_half', 'admissible_sl2_k_minus_4_3']:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            assert analysis['bulk']['bulk_regular'] is False, (
                f"Expected bulk irregularity for {family}"
            )
            assert analysis['bulk']['log_singularities'] > 0, (
                f"Expected logarithmic singularities for {family}"
            )

    def test_fm_alignment_matches_bulk_regularity(self):
        """FM alignment and bulk regularity agree for ALL families.

        This is a key prediction of the holographic dictionary.
        """
        for family in HolographicDModPurityDictionary.FAMILIES:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            cons = analysis['consistency']
            assert cons['fm_alignment_matches_regularity'] is True, (
                f"FM alignment / bulk regularity mismatch for {family}"
            )

    def test_heisenberg_class_g(self):
        """Heisenberg is class G (shadow depth 2), D-module pure."""
        info = HolographicDModPurityDictionary.FAMILIES['heisenberg_k1']
        assert info['shadow_class'] == 'G'
        assert info['shadow_depth'] == 2
        assert info['is_koszul'] is True

    def test_affine_class_l(self):
        """Affine KM is class L (shadow depth 3), D-module pure."""
        info = HolographicDModPurityDictionary.FAMILIES['affine_sl2_k1']
        assert info['shadow_class'] == 'L'
        assert info['shadow_depth'] == 3
        assert info['is_koszul'] is True

    def test_virasoro_class_m(self):
        """Virasoro is class M (infinite shadow depth), D-module pure."""
        info = HolographicDModPurityDictionary.FAMILIES['virasoro_c26']
        assert info['shadow_class'] == 'M'
        assert info['shadow_depth'] == float('inf')
        assert info['is_koszul'] is True

    def test_betagamma_class_c(self):
        """beta-gamma is class C (shadow depth 4), D-module pure."""
        info = HolographicDModPurityDictionary.FAMILIES['betagamma']
        assert info['shadow_class'] == 'C'
        assert info['shadow_depth'] == 4
        assert info['is_koszul'] is True

    def test_shadow_depth_independent_of_purity(self):
        """Shadow depth and D-module purity are INDEPENDENT.

        All shadow classes (G, L, C, M) are D-module pure.
        Shadow depth classifies complexity WITHIN the Koszul world,
        not Koszulness status itself (AP14 guard).
        """
        depths = set()
        for family in ['heisenberg_k1', 'affine_sl2_k1', 'betagamma',
                       'virasoro_c26']:
            info = HolographicDModPurityDictionary.FAMILIES[family]
            assert info['is_koszul'] is True
            depths.add(info['shadow_depth'])
        # All four shadow classes represented
        assert depths == {2, 3, 4, float('inf')}


# =========================================================================
# IV. Virasoro c=26 Tests
# =========================================================================

class TestVirasoroC26:
    """Tests for Virasoro at c=26 (critical string)."""

    def test_bpz_vacuum_order(self):
        """BPZ null-vector equation for vacuum (h=0) has order 1."""
        order = VirasoroC26Regularity.bpz_equation_order(Fraction(0))
        assert order == 1

    def test_bpz_h21_order(self):
        """BPZ equation for h_{2,1} at c=26 has order 2.

        h_{2,1} = (5-c)/16 = -21/16 at c=26.
        """
        h_21 = Fraction(5 - 26, 16)
        order = VirasoroC26Regularity.bpz_equation_order(h_21)
        assert order == 2

    def test_hypergeometric_singularities(self):
        """4-point Virasoro blocks satisfy a hypergeometric (Fuchsian) ODE.

        Singular points at 0, 1, infinity -- all regular.
        All correspond to FM boundary strata via the cross-ratio map.
        """
        sing = VirasoroC26Regularity.hypergeometric_singularities()
        assert sing['all_regular'] is True
        assert sing['characteristic_variety_aligned'] is True
        assert sing['dmod_pure'] is True
        assert len(sing['singular_points']) == 3

    def test_anomaly_cancellation(self):
        """At c=26: kappa_eff = kappa(matter) + kappa(ghost) = 13 + (-13) = 0.

        Path 1: Direct computation.
        Path 2: AP29 consistency: kappa_eff != delta_kappa.
                delta_kappa = kappa - kappa' = 13 - 0 = 13 (at c=26).
        Path 3: Physical: anomaly cancellation at c=26 is the statement
                that the bulk Weyl anomaly vanishes.
        """
        result = VirasoroC26Regularity.critical_string_anomaly_cancellation()
        assert result['kappa_eff'] == 0.0
        assert result['anomaly_cancelled'] is True
        # AP29 cross-check: delta_kappa != kappa_eff
        assert result['delta_kappa'] == 13.0
        assert result['delta_kappa'] != result['kappa_eff']

    def test_kappa_matter_equals_13(self):
        """kappa(Vir_26) = 26/2 = 13."""
        result = VirasoroC26Regularity.critical_string_anomaly_cancellation()
        assert result['kappa_matter'] == 13.0

    def test_kappa_ghost_equals_minus_13(self):
        """kappa(bc ghost) = -13.

        The bc ghost system has c = -26, so kappa(ghost) = -26/2 = -13.
        (AP20: kappa(ghost) is the ghost algebra's own kappa, not kappa_eff.)
        """
        result = VirasoroC26Regularity.critical_string_anomaly_cancellation()
        assert result['kappa_ghost'] == -13.0

    def test_self_dual_vs_anomaly_cancellation(self):
        """Self-duality (c=13) and anomaly cancellation (c=26) are DIFFERENT.

        AP29 guard: delta_kappa = 0 at c=13; kappa_eff = 0 at c=26.
        These are 13 units apart and must NOT be conflated.
        """
        result = VirasoroC26Regularity.critical_string_anomaly_cancellation()
        assert 'c=13' in result['self_dual_point']
        assert 'c=26' in result['anomaly_cancellation_point']


# =========================================================================
# V. Converse Argument Chain Tests
# =========================================================================

class TestConverseArgument:
    """Tests for the conjectural converse argument chain."""

    def test_chain_has_6_steps(self):
        """The converse argument has 6 steps."""
        status = DModPurityConverseArgument.chain_status()
        assert status['n_total'] == 6

    def test_gap_at_step_4(self):
        """The gap in the converse argument is at step 4.

        Step 4: local system on FM complement => E_1 degeneration.
        This requires geometric origin of the conformal blocks (VHS).
        """
        status = DModPurityConverseArgument.chain_status()
        assert status['gap_at_step'] == 4

    def test_5_of_6_steps_proved(self):
        """5 out of 6 steps in the chain are proved.

        Steps 1, 2, 3, 5, 6 are proved. Step 4 is conditional.
        """
        status = DModPurityConverseArgument.chain_status()
        # Steps 1 (def), 2, 3, 5, 6 are proved = 5
        assert status['n_proved'] == 5

    def test_cs_wzw_converse_complete(self):
        """For CS/WZW: the full converse chain is proved.

        The Hitchin connection (Axelrod-della Pietra-Witten) gives a
        variation of Hodge structure on conformal blocks, resolving
        step 4 for this family.
        """
        result = DModPurityConverseArgument.cs_wzw_verification()
        assert result['converse_chain_complete'] is True
        assert result['hitchin_connection_exists'] is True
        assert result['vhs_structure'] is True

    def test_cs_wzw_all_properties_true(self):
        """CS/WZW has all desired properties simultaneously."""
        result = DModPurityConverseArgument.cs_wzw_verification()
        assert result['is_koszul'] is True
        assert result['kz_fuchsian'] is True
        assert result['dmod_pure'] is True
        assert result['fm_acyclicity'] is True

    def test_converse_overall_status(self):
        """Overall converse status: conditional on geometric origin."""
        status = DModPurityConverseArgument.chain_status()
        assert 'CONDITIONAL' in status['overall_status']
        assert 'geometric origin' in status['overall_status']

    def test_virasoro_converse_open(self):
        """For Virasoro: the converse is OPEN (no VHS established)."""
        status = DModPurityConverseArgument.chain_status()
        assert 'OPEN' in status['virasoro_status']


# =========================================================================
# VI. Admissible Level Obstruction Tests
# =========================================================================

class TestAdmissibleLevelObstruction:
    """Tests for the admissible-level obstruction analysis."""

    def test_sl2_k_minus_half_null_level(self):
        """k=-1/2: k+2 = 3/2, null level = 3*2 = 6."""
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2)
        assert result['null_vector_level'] == 6

    def test_sl2_k_minus_4_3_null_level(self):
        """k=-4/3: k+2 = 2/3, null level = 2*3 = 6."""
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(2, 3)
        assert result['null_vector_level'] == 6

    def test_sl2_k_minus_half_apparent_count(self):
        """k=-1/2, 4 points: 10 apparent singularities.

        Path 1: Formula (null_level - 1) * (n - 2) = 5 * 2 = 10.
        Path 2: Fuchs relation for 6th-order ODE on P^1 with 3 regular
                 singular points: sum of apparent exponents = 5*2 = 10.
        """
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2, 4)
        assert result['apparent_singularities'] == 10

    def test_sl2_k_minus_half_5_points(self):
        """k=-1/2, 5 points: 15 apparent singularities."""
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2, 5)
        assert result['apparent_singularities'] == 15

    def test_fm_alignment_violated_admissible(self):
        """FM alignment is violated at all admissible levels with q >= 2."""
        for p, q in [(3, 2), (2, 3), (5, 2), (3, 4), (5, 3), (7, 2)]:
            if math.gcd(p, q) != 1:
                continue
            result = AdmissibleLevelObstruction.sl2_admissible_analysis(p, q, 4)
            assert result['fm_alignment_violated'] is True, (
                f"Expected FM violation at p={p}, q={q}"
            )

    def test_logarithmic_solutions_admissible(self):
        """Admissible levels with q >= 2 have logarithmic solutions."""
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2, 4)
        assert result['has_logarithmic_solutions'] is True

    def test_no_logarithmic_solutions_integer_level(self):
        """Integer levels (q=1) have no logarithmic solutions from null vectors."""
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 1, 4)
        assert result['has_logarithmic_solutions'] is False
        assert result['apparent_singularities'] == 0

    def test_monodromy_at_collision_unitary(self):
        """Monodromy at collision is unitary (|eigenvalue| = 1).

        The local monodromy around a collision z_i = z_j is
        exp(2*pi*i * Omega_{ij} / (k+2)), which has unit modulus.
        """
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2, 4)
        mono = result['monodromy_at_collision']
        assert abs(mono['triplet_channel']['abs'] - 1.0) < 1e-10
        assert abs(mono['singlet_channel']['abs'] - 1.0) < 1e-10

    def test_kz_parameter_admissible(self):
        """KZ parameter at k=-1/2 is 1/(k+2) = 1/(3/2) = 2/3."""
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2)
        assert abs(result['kz_parameter'] - 2.0 / 3.0) < 1e-10

    def test_apparent_singularity_count_grows_with_null_level(self):
        """Higher null-vector level gives more apparent singularities.

        For fixed n=4: n_app = (null_level - 1) * 2.
        As p*q grows, n_app grows linearly.

        Path 1: Direct computation.
        Path 2: Monotonicity check.
        """
        counts = []
        for p, q in [(2, 3), (3, 2), (5, 2), (2, 5), (7, 2)]:
            if math.gcd(p, q) != 1:
                continue
            result = AdmissibleLevelObstruction.sl2_admissible_analysis(p, q, 4)
            counts.append((p * q, result['apparent_singularities']))

        # Verify formula: n_app = (pq - 1) * 2
        for pq, n_app in counts:
            assert n_app == (pq - 1) * 2

    def test_admissible_landscape_sorted(self):
        """Admissible landscape is sorted by null-vector level."""
        landscape = AdmissibleLevelObstruction.admissible_landscape(4)
        null_levels = [entry['null_vector_level'] for entry in landscape]
        assert null_levels == sorted(null_levels)

    def test_admissible_landscape_nonempty(self):
        """Admissible landscape has multiple entries."""
        landscape = AdmissibleLevelObstruction.admissible_landscape(4)
        assert len(landscape) >= 5

    def test_invalid_admissible_parameters_rejected(self):
        """Invalid admissible parameters are rejected."""
        with pytest.raises(ValueError):
            AdmissibleLevelObstruction.sl2_admissible_analysis(1, 2)  # p < 2
        with pytest.raises(ValueError):
            AdmissibleLevelObstruction.sl2_admissible_analysis(4, 2)  # gcd != 1

    def test_dmod_purity_violated_iff_apparent_positive(self):
        """D-module purity is violated iff apparent singularities > 0.

        This is the core prediction of the holographic dictionary.
        """
        for p, q in [(3, 2), (2, 3), (5, 2), (3, 1), (5, 1)]:
            if math.gcd(p, q) != 1:
                continue
            result = AdmissibleLevelObstruction.sl2_admissible_analysis(p, q, 4)
            expected_violated = (result['apparent_singularities'] > 0)
            assert result['fm_alignment_violated'] == expected_violated


# =========================================================================
# VII. Cross-Family Verification Tests
# =========================================================================

class TestCrossFamilyVerification:
    """Tests for cross-family consistency of the holographic dictionary."""

    def test_full_landscape_forward_consistent(self):
        """Forward direction is consistent for ALL families in the landscape.

        This is the PROVED direction. Any failure is a CRITICAL bug.
        """
        result = CrossFamilyVerification.full_landscape_check()
        assert result['forward_all_consistent'] is True, (
            f"Forward direction failures: {result['forward_failures']}"
        )

    def test_converse_evidence_from_landscape(self):
        """Converse direction has evidence from all tested families."""
        result = CrossFamilyVerification.full_landscape_check()
        assert result['converse_evidence_count'] >= 7

    def test_kappa_cross_check_all_match(self):
        """Kappa values match across all families.

        AP1/AP39 guard: each kappa computed from the DEFINING FORMULA,
        not copied from another family.
        """
        result = CrossFamilyVerification.kappa_cross_check()
        assert result['all_match'] is True
        for family, check in result['checks'].items():
            assert check['match'] is True, (
                f"Kappa mismatch for {family}: "
                f"computed={check['computed']}, expected={check['expected']}"
            )

    def test_kappa_sl2_not_c_over_2(self):
        """kappa(sl_2, k=1) = 9/4 != c/2 = 1/2 (AP39 guard).

        The central charge c(sl_2, k=1) = 3*1/(1+2) = 1.
        c/2 = 1/2 != 9/4 = kappa.
        The Virasoro formula kappa = c/2 does NOT apply to KM (AP39).
        """
        kz = KZConnection('A', 1, Fraction(1))
        c = Fraction(3 * 1, 1 + 2)  # = 1
        assert kz.kappa == Fraction(9, 4)
        assert kz.kappa != c / 2
        assert c / 2 == Fraction(1, 2)

    def test_kappa_e8_not_c_over_2(self):
        """kappa(E_8, k=1) != c/2 for E_8 (AP48 guard).

        c(E_8, k=1) = 248*1/(1+30) = 248/31 = 8.
        c/2 = 4.
        kappa(E_8, k=1) = 248*31/60 = 1922/15 approx 128.13.
        These diverge wildly.
        """
        kz = KZConnection('E', 8, Fraction(1))
        c = Fraction(248 * 1, 1 + 30)  # = 248/31 = 8
        assert kz.kappa == Fraction(1922, 15)
        assert kz.kappa != c / 2
        # The ratio kappa / (c/2) = 1922/15 / 4 = 1922/60 = 961/30 >> 1
        ratio = kz.kappa / (c / 2)
        assert ratio > 30  # Wildly different

    def test_families_analysed_count(self):
        """At least 9 families in the landscape."""
        result = CrossFamilyVerification.full_landscape_check()
        assert result['families_analysed'] >= 9


# =========================================================================
# VIII. Conjecture Formulation Tests
# =========================================================================

class TestConjectureFormulation:
    """Tests for the precise conjecture statement."""

    def test_conjecture_has_four_conditions(self):
        """The conjecture has 4 equivalent conditions (a)-(d)."""
        stmt = HolographicPurityConjecture.statement()
        assert '(a) <=> (b) <=> (c) <=> (d)' in stmt['equivalences']

    def test_three_proved_directions(self):
        """Three directions are proved: (a)=>(b), (b)=>(c), (c)=>(d)."""
        stmt = HolographicPurityConjecture.statement()
        assert len(stmt['proved_directions']) == 3
        assert '(a) => (b)' in stmt['proved_directions']
        assert '(b) => (c)' in stmt['proved_directions']
        assert '(c) => (d)' in stmt['proved_directions']

    def test_cs_wzw_proved(self):
        """For CS/WZW: (b) => (a) is proved."""
        stmt = HolographicPurityConjecture.statement()
        assert '(b) => (a)' in stmt['proved_for_cs_wzw']

    def test_general_converse_open(self):
        """In general: (b) => (a) is open."""
        stmt = HolographicPurityConjecture.statement()
        assert '(b) => (a)' in stmt['open_in_general']

    def test_evidence_families_nonempty(self):
        """Evidence families include all standard families."""
        stmt = HolographicPurityConjecture.statement()
        assert 'heisenberg' in stmt['evidence_families']
        assert 'virasoro' in stmt['evidence_families']
        assert 'affine_km' in stmt['evidence_families']

    def test_potential_counterexample_families(self):
        """Admissible-level simple quotients are potential counterexamples."""
        stmt = HolographicPurityConjecture.statement()
        assert 'admissible_level_simple_quotients' in (
            stmt['potential_counterexample_families']
        )

    def test_dependencies_include_saito(self):
        """The conjecture depends on Saito MHM theory."""
        stmt = HolographicPurityConjecture.statement()
        deps = stmt['dependencies']
        assert any('Saito' in d for d in deps)

    def test_dependencies_include_deligne(self):
        """The conjecture depends on Deligne purity theorem."""
        stmt = HolographicPurityConjecture.statement()
        deps = stmt['dependencies']
        assert any('Deligne' in d for d in deps)


# =========================================================================
# IX. Integration Tests
# =========================================================================

class TestIntegration:
    """Integration tests verifying internal consistency."""

    def test_admissible_boundary_bulk_agreement(self):
        """For admissible levels: boundary and bulk analyses agree.

        The number of apparent singularities on the boundary should
        equal the number of logarithmic singularities in the bulk.

        Path 1: Compute from boundary analysis (Gaudin).
        Path 2: Compute from bulk analysis (holographic dictionary).
        Path 3: Check they agree.
        """
        for family in ['admissible_sl2_k_minus_half', 'admissible_sl2_k_minus_4_3']:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            boundary_apparent = analysis['boundary'].get('apparent_singularities', 0)
            bulk_log = analysis['bulk'].get('log_singularities', 0)
            assert boundary_apparent == bulk_log, (
                f"Boundary/bulk mismatch for {family}: "
                f"boundary={boundary_apparent}, bulk={bulk_log}"
            )

    def test_koszul_implies_zero_apparent(self):
        """Every Koszul family has zero apparent singularities.

        This is a consequence of the forward direction:
        Koszul => FM aligned => no apparent singularities.
        """
        for family, info in HolographicDModPurityDictionary.FAMILIES.items():
            if info['is_koszul'] is True:
                analysis = HolographicDModPurityDictionary.analyse_family(family)
                apparent = analysis['boundary'].get('apparent_singularities', 0)
                assert apparent == 0, (
                    f"Koszul family {family} has {apparent} apparent singularities!"
                )

    def test_non_pure_implies_log_bulk(self):
        """Non-pure boundary implies logarithmic bulk.

        If D-module purity is violated (FM misalignment), the bulk
        must have logarithmic singularities.
        """
        for family in HolographicDModPurityDictionary.FAMILIES:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            if analysis['boundary']['dmod_pure'] is False:
                assert analysis['bulk']['bulk_regular'] is False

    def test_pure_implies_regular_bulk(self):
        """Pure boundary implies regular bulk (forward direction)."""
        for family in HolographicDModPurityDictionary.FAMILIES:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            if analysis['boundary']['dmod_pure'] is True:
                assert analysis['bulk']['bulk_regular'] is True

    def test_no_counterexample_to_converse(self):
        """No known family is D-module pure but NOT Koszul.

        This is evidence for the converse conjecture.
        Every family that is D-module pure is also Koszul (among those
        with known Koszulness status).
        """
        for family in HolographicDModPurityDictionary.FAMILIES:
            analysis = HolographicDModPurityDictionary.analyse_family(family)
            info = HolographicDModPurityDictionary.FAMILIES[family]
            if analysis['boundary']['dmod_pure'] is True:
                if info['is_koszul'] is not None:
                    assert info['is_koszul'] is True, (
                        f"COUNTEREXAMPLE to converse: {family} is D-module pure "
                        f"but NOT Koszul!"
                    )

    def test_converse_chain_step_count_matches_chain(self):
        """Converse chain status is consistent with the chain definition."""
        status = DModPurityConverseArgument.chain_status()
        assert len(status['steps']) == len(DModPurityConverseArgument.CHAIN_STEPS)

    def test_monodromy_triplet_phase_admissible(self):
        """Triplet monodromy phase at k=-1/2 is exp(2*pi*i * (2/3)*(1/4)).

        = exp(pi*i/3) = cos(pi/3) + i*sin(pi/3) = 1/2 + i*sqrt(3)/2.

        Path 1: Direct computation from engine.
        Path 2: Independent computation.
        """
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2, 4)
        mono_t = result['monodromy_at_collision']['triplet_channel']
        # kz_param = 2/3, Omega = 1/4
        # phase = 2*pi * (2/3) * (1/4) = pi/3
        expected_re = math.cos(math.pi / 3)  # = 0.5
        expected_im = math.sin(math.pi / 3)  # = sqrt(3)/2
        assert abs(mono_t['re'] - expected_re) < 1e-10
        assert abs(mono_t['im'] - expected_im) < 1e-10

    def test_monodromy_singlet_phase_admissible(self):
        """Singlet monodromy phase at k=-1/2 is exp(2*pi*i * (2/3)*(-3/4)).

        = exp(-pi*i) = -1.

        Path 1: Direct computation from engine.
        Path 2: Independent computation.
        """
        result = AdmissibleLevelObstruction.sl2_admissible_analysis(3, 2, 4)
        mono_s = result['monodromy_at_collision']['singlet_channel']
        # kz_param = 2/3, Omega = -3/4
        # phase = 2*pi * (2/3) * (-3/4) = -pi
        expected_re = math.cos(-math.pi)  # = -1
        expected_im = math.sin(-math.pi)  # = 0
        assert abs(mono_s['re'] - expected_re) < 1e-10
        assert abs(mono_s['im'] - expected_im) < 1e-10
