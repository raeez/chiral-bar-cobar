#!/usr/bin/env python3
r"""Tests for shifted_symplectic_dag_engine.py -- Shifted symplectic geometry
and derived algebraic geometry foundations.

MULTI-PATH VERIFICATION:
    Path 1: PTVV shifted symplectic from cyclic pairing
    Path 2: Lagrangian from Koszul pair (Theorem C)
    Path 3: AKSZ mapping stack shifts
    Path 4: dCrit(W) and bar curvature comparison
    Path 5: BV/bar dictionary consistency
    Path 6: Joyce d-critical locus / DT invariants
    Path 7: Safronov Poisson reduction for DS
    Path 8: Cross-family consistency (additivity, complementarity)

CONVENTIONS (from CLAUDE.md):
    AP1:  kappa formulas recomputed per family
    AP8:  Virasoro self-dual at c=13, NOT c=26
    AP24: kappa + kappa' = 0 for KM; = 13 for Vir
    AP39: kappa != c/2 for general VOA
    AP45: desuspension LOWERS degree
    AP48: kappa depends on full algebra
"""

from fractions import Fraction
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from shifted_symplectic_dag_engine import (
    # Utilities
    _frac, _harmonic, _bernoulli_fraction, lambda_fp,
    # Family constructors
    DAGAlgebraFamily, heisenberg, virasoro, affine_sl, betagamma,
    w_algebra, lattice_voa, STANDARD_FAMILIES,
    # Shifted symplectic
    ShiftedSymplecticStructure, shifted_symplectic_on_bar_moduli,
    cyclic_pairing_degree, poisson_bracket_degree,
    # Lagrangian
    LagrangianData, lagrangian_from_koszul_pair, lagrangian_self_dual_test,
    # AKSZ
    AKSZData, aksz_construction, aksz_shift,
    # PTVV
    ptvv_shift_rloc, ptvv_shift_mapping_stack, ptvv_shift_ambient_genus,
    rloc_comparison_affine,
    # dCrit
    DerivedCriticalLocusData, derived_critical_locus,
    dcrit_is_shifted_symplectic, dcrit_matches_bar_moduli,
    # Calaque
    CalaqueDerivedAKSZData, calaque_aksz, modular_operad_as_aksz,
    # BV
    BVBarDictionary, bv_bar_dictionary, bv_antibracket_is_poisson,
    qme_is_mc,
    # Joyce
    DCriticalLocusData, joyce_d_critical_locus,
    dt_invariant_genus_g, dt_invariant_additivity,
    behrend_weighted_euler,
    # Safronov
    SafronovReductionData, safronov_ds_reduction,
    safronov_shift_preservation, ds_preserves_bar_shift,
    # Full package and verification
    full_dag_package,
    verify_ptvv_shifts_all_genera,
    verify_lagrangian_complementarity_all_families,
    verify_aksz_action_consistency,
    verify_bv_bar_shifts,
)


# ============================================================================
# SECTION 1: FAMILY CONSTRUCTION (AP1/AP24/AP39/AP48 recomputation)
# ============================================================================

class TestFamilyConstruction:
    """Verify kappa formulas are correct per AP1/AP39/AP48."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP1)."""
        fam = heisenberg(3)
        assert fam.kappa == Fraction(3)
        assert fam.kappa_dual == Fraction(-3)

    def test_heisenberg_complementarity_zero(self):
        """kappa + kappa' = 0 for Heisenberg (AP24)."""
        for k in [1, 2, 5, Fraction(1, 2)]:
            fam = heisenberg(k)
            assert fam.complementarity_sum == Fraction(0)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP1)."""
        fam = virasoro(26)
        assert fam.kappa == Fraction(13)

    def test_virasoro_complementarity_13(self):
        """kappa + kappa' = 13 for Virasoro (AP24: NOT 0)."""
        for c in [1, 2, 13, 24, 26]:
            fam = virasoro(c)
            assert fam.complementarity_sum == Fraction(13), (
                f"Failed at c={c}: sum={fam.complementarity_sum}")

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro self-dual at c=13 (AP8: NOT c=26)."""
        fam = virasoro(13)
        assert fam.kappa == fam.kappa_dual == Fraction(13, 2)

    def test_virasoro_NOT_self_dual_at_c26(self):
        """Virasoro NOT self-dual at c=26 (AP8)."""
        fam = virasoro(26)
        assert fam.kappa != fam.kappa_dual

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k=1) = 3*3/(2*2) = 9/4 (AP1, AP39)."""
        fam = affine_sl(2, 1)
        assert fam.kappa == Fraction(9, 4)

    def test_affine_sl2_kappa_not_c_over_2(self):
        """kappa(sl_2, k=1) != c/2 (AP39)."""
        fam = affine_sl(2, 1)
        c_half = fam.central_charge / 2
        assert fam.kappa != c_half

    def test_affine_complementarity_zero(self):
        """kappa + kappa' = 0 for affine KM (AP24)."""
        for N in [2, 3, 4]:
            for k in [Fraction(1), Fraction(2)]:
                fam = affine_sl(N, k)
                assert fam.complementarity_sum == Fraction(0)

    def test_betagamma_complementarity_zero(self):
        """kappa + kappa' = 0 for betagamma (AP24)."""
        fam = betagamma(-2)
        assert fam.complementarity_sum == Fraction(0)

    def test_lattice_kappa_is_rank(self):
        """kappa(V_Lambda) = rank (AP48: NOT c/2)."""
        fam = lattice_voa(24)
        assert fam.kappa == Fraction(24)

    def test_w3_kappa(self):
        """kappa(W_3, c) = 5c/6 (AP1: H_3 - 1 = 5/6)."""
        fam = w_algebra(3, 2)
        assert fam.kappa == Fraction(5) * Fraction(2) / Fraction(6)

    def test_uniform_weight_classification(self):
        """Heisenberg, Virasoro, affine are uniform-weight."""
        assert heisenberg().is_uniform_weight
        assert virasoro().is_uniform_weight
        assert affine_sl(2).is_uniform_weight

    def test_betagamma_not_uniform_weight(self):
        """Beta-gamma has generators of weight 0 and 1."""
        fam = betagamma()
        assert not fam.is_uniform_weight

    def test_w3_not_uniform_weight(self):
        """W_3 has generators of weight 2 and 3."""
        fam = w_algebra(3)
        assert not fam.is_uniform_weight


# ============================================================================
# SECTION 2: (-1)-SHIFTED SYMPLECTIC STRUCTURE
# ============================================================================

class TestShiftedSymplectic:
    """Verify the (-1)-shifted symplectic structure on bar moduli."""

    def test_shift_is_minus_1(self):
        """Bar moduli M_B(A) is (-1)-shifted symplectic."""
        for fam in STANDARD_FAMILIES.values():
            symp = shifted_symplectic_on_bar_moduli(fam)
            assert symp.shift == -1

    def test_pairing_degree_minus_1(self):
        """Cyclic pairing on g^mod_A has degree -1."""
        assert cyclic_pairing_degree(1) == -1

    def test_pairing_degree_general(self):
        """Cyclic pairing degree = -(2d - 1) for d-dimensional source."""
        assert cyclic_pairing_degree(1) == -1
        assert cyclic_pairing_degree(2) == -3
        assert cyclic_pairing_degree(3) == -5

    def test_poisson_degree_plus_1(self):
        """Poisson bracket on (-1)-shifted is degree +1."""
        assert poisson_bracket_degree(-1) == 1

    def test_poisson_degree_general(self):
        """Poisson bracket degree = -n for n-shifted."""
        assert poisson_bracket_degree(0) == 0
        assert poisson_bracket_degree(-2) == 2
        assert poisson_bracket_degree(2) == -2

    def test_symplectic_rank_arity_5(self):
        """Symplectic rank = 2*(max_arity - 1) = 8 for max_arity=5."""
        fam = heisenberg()
        symp = shifted_symplectic_on_bar_moduli(fam, max_arity=5)
        assert symp.symplectic_rank == 8

    def test_nondegeneracy_standard_landscape(self):
        """All standard families have nondegenerate cyclic pairing."""
        for fam in STANDARD_FAMILIES.values():
            symp = shifted_symplectic_on_bar_moduli(fam)
            assert symp.is_nondegenerate


# ============================================================================
# SECTION 3: LAGRANGIAN STRUCTURE (THEOREM C)
# ============================================================================

class TestLagrangian:
    """Verify Lagrangian structure from Koszul pair."""

    def test_all_standard_are_lagrangian(self):
        """All standard families give Lagrangian subspaces."""
        for fam in STANDARD_FAMILIES.values():
            lagr = lagrangian_from_koszul_pair(fam)
            assert lagr.is_lagrangian

    def test_heisenberg_theta_primitive(self):
        """Heisenberg: theta_2 = k * (-k) = -k^2."""
        fam = heisenberg(3)
        lagr = lagrangian_from_koszul_pair(fam)
        assert lagr.theta_primitive_arity2 == Fraction(-9)

    def test_virasoro_theta_primitive(self):
        """Virasoro: theta_2 = (c/2) * ((26-c)/2) = c(26-c)/4."""
        fam = virasoro(2)
        lagr = lagrangian_from_koszul_pair(fam)
        expected = Fraction(2) * Fraction(24) / Fraction(4)  # 48/4 = 12
        assert lagr.theta_primitive_arity2 == expected

    def test_virasoro_c13_theta_primitive(self):
        """At c=13 (self-dual): theta_2 = (13/2)^2 = 169/4."""
        fam = virasoro(13)
        lagr = lagrangian_from_koszul_pair(fam)
        assert lagr.theta_primitive_arity2 == Fraction(169, 4)

    def test_intersection_degree_heisenberg(self):
        """Heisenberg: intersection_degree = -(0) = 0 (transverse)."""
        fam = heisenberg()
        lagr = lagrangian_from_koszul_pair(fam)
        assert lagr.intersection_degree == Fraction(0)

    def test_intersection_degree_virasoro(self):
        """Virasoro: intersection_degree = -13 (non-transverse)."""
        fam = virasoro(1)
        lagr = lagrangian_from_koszul_pair(fam)
        assert lagr.intersection_degree == Fraction(-13)

    def test_intersection_degree_affine(self):
        """Affine KM: intersection_degree = 0 (transverse)."""
        fam = affine_sl(2, 1)
        lagr = lagrangian_from_koszul_pair(fam)
        assert lagr.intersection_degree == Fraction(0)

    def test_ptvv_shift_genus_1(self):
        """PTVV shift at genus 1: -(3*1-3) = 0."""
        fam = heisenberg()
        lagr = lagrangian_from_koszul_pair(fam, genus=1)
        assert lagr.ptvv_shift == 0

    def test_ptvv_shift_genus_2(self):
        """PTVV shift at genus 2: -(3*2-3) = -3."""
        fam = heisenberg()
        lagr = lagrangian_from_koszul_pair(fam, genus=2)
        assert lagr.ptvv_shift == -3

    def test_self_dual_only_vir_c13(self):
        """Only Virasoro at c=13 is Lagrangian self-dual."""
        sd = lagrangian_self_dual_test(virasoro(13))
        assert sd['is_self_dual']

        for name, fam in STANDARD_FAMILIES.items():
            sd = lagrangian_self_dual_test(fam)
            if name == 'Virasoro_c13':
                assert sd['is_self_dual']
            else:
                assert not sd['is_self_dual'], f"{name} should not be self-dual"

    def test_complementarity_all_families(self):
        """Cross-family complementarity check (AP24)."""
        results = verify_lagrangian_complementarity_all_families()
        for r in results:
            assert r['is_lagrangian']
            # Check the complementarity sum is correct
            expected_sum = r['kappa'] + r['kappa_dual']
            assert r['sum'] == expected_sum


# ============================================================================
# SECTION 4: AKSZ CONSTRUCTION
# ============================================================================

class TestAKSZ:
    """Verify AKSZ construction for Map(Sigma_g, M_B)."""

    def test_aksz_shift_minus_3(self):
        """AKSZ mapping shift = -1 - 2 = -3."""
        assert aksz_shift(-1, 2) == -3

    def test_aksz_shift_general(self):
        """AKSZ shift = target_shift - source_dim."""
        assert aksz_shift(0, 2) == -2
        assert aksz_shift(-2, 3) == -5
        assert aksz_shift(2, 1) == 1

    def test_aksz_kinetic_is_1(self):
        """AKSZ kinetic term is always 1."""
        for fam in STANDARD_FAMILIES.values():
            aksz = aksz_construction(fam, genus=1)
            assert aksz.aksz_kinetic == Fraction(1)

    def test_aksz_kappa_term(self):
        """AKSZ kappa term matches kappa(A)."""
        fam = virasoro(26)
        aksz = aksz_construction(fam, genus=1)
        assert aksz.aksz_kappa_term == Fraction(13)

    def test_aksz_genus_correction_g1(self):
        """Genus-1 AKSZ correction = kappa * lambda_1 = kappa/24."""
        fam = heisenberg(1)
        aksz = aksz_construction(fam, genus=1)
        assert aksz.aksz_genus_correction == Fraction(1) * lambda_fp(1)
        assert aksz.aksz_genus_correction == Fraction(1, 24)

    def test_aksz_genus_correction_g0(self):
        """Genus-0 AKSZ has no genus correction."""
        fam = heisenberg()
        aksz = aksz_construction(fam, genus=0)
        assert aksz.aksz_genus_correction == Fraction(0)

    def test_aksz_consistency(self):
        """Full AKSZ consistency check."""
        for fam in STANDARD_FAMILIES.values():
            result = verify_aksz_action_consistency(fam, genus=1)
            assert result['kinetic_is_1']
            assert result['kappa_term_matches']
            assert result['genus_correction_matches']
            assert result['mapping_shift_is_minus_3']


# ============================================================================
# SECTION 5: PTVV SHIFTS
# ============================================================================

class TestPTVV:
    """Verify PTVV shift formulas."""

    def test_rloc_surface_0_shifted(self):
        """RLoc_G(Sigma) on a surface is 0-shifted symplectic."""
        assert ptvv_shift_rloc(2) == 0

    def test_rloc_3fold_minus_1(self):
        """RLoc_G(X^3) on a 3-fold is (-1)-shifted symplectic."""
        assert ptvv_shift_rloc(3) == -1

    def test_rloc_curve_1_shifted(self):
        """RLoc_G(C) on a curve is 1-shifted symplectic."""
        assert ptvv_shift_rloc(1) == 1

    def test_mapping_stack_shift(self):
        """Map(Sigma, M_B) is (-3)-shifted."""
        assert ptvv_shift_mapping_stack(-1, 2) == -3

    def test_ambient_shift_genus_0(self):
        """Ambient at genus 0: shift = 0 (convention)."""
        assert ptvv_shift_ambient_genus(0) == 0

    def test_ambient_shift_genus_1(self):
        """Ambient at genus 1: -(3*1-3) = 0."""
        assert ptvv_shift_ambient_genus(1) == 0

    def test_ambient_shift_genus_2(self):
        """Ambient at genus 2: -(3*2-3) = -3."""
        assert ptvv_shift_ambient_genus(2) == -3

    def test_ambient_shift_genus_3(self):
        """Ambient at genus 3: -(3*3-3) = -6."""
        assert ptvv_shift_ambient_genus(3) == -6

    def test_ptvv_shifts_all_genera(self):
        """Verify PTVV shifts across genera 0-5."""
        results = verify_ptvv_shifts_all_genera(5)
        for r in results:
            g = r['genus']
            expected = -(3 * g - 3) if g >= 1 else 0
            assert r['ptvv_ambient_shift'] == expected
            assert r['mapping_stack_shift'] == -3  # independent of genus

    def test_rloc_comparison_sl2(self):
        """RLoc_{SL_2}(Sigma x R) shift matches bar moduli shift."""
        result = rloc_comparison_affine(2, 1)
        assert result['shifts_agree']
        assert result['rloc_sigma_shift'] == 0
        assert result['rloc_sigma_x_R_shift'] == -1
        assert result['bar_moduli_shift'] == -1

    def test_rloc_comparison_sl3(self):
        """RLoc_{SL_3}(Sigma x R) shift matches bar moduli shift."""
        result = rloc_comparison_affine(3, 1)
        assert result['shifts_agree']
        assert result['kappa_bar'] == Fraction(8) * Fraction(4) / Fraction(6)


# ============================================================================
# SECTION 6: DERIVED CRITICAL LOCUS
# ============================================================================

class TestDerivedCriticalLocus:
    """Verify dCrit(W) and bar curvature comparison."""

    def test_dcrit_always_minus_1_shifted(self):
        """dCrit(W) is always (-1)-shifted symplectic."""
        assert dcrit_is_shifted_symplectic()

    def test_genus0_uncurved(self):
        """At genus 0, the bar complex is uncurved."""
        for fam in STANDARD_FAMILIES.values():
            dcrit = derived_critical_locus(fam, genus=0)
            assert not dcrit.is_curved
            assert dcrit.curvature_m0 == Fraction(0)

    def test_genus1_curved_unless_kappa_zero(self):
        """At genus >= 1, curved iff kappa != 0."""
        fam_curved = virasoro(26)  # kappa = 13 != 0
        fam_uncurved = virasoro(0)  # kappa = 0
        dcrit_c = derived_critical_locus(fam_curved, genus=1)
        dcrit_u = derived_critical_locus(fam_uncurved, genus=1)
        assert dcrit_c.is_curved
        assert not dcrit_u.is_curved

    def test_curvature_is_kappa_lambda(self):
        """Bar curvature m_0 = kappa * lambda_g^FP."""
        fam = virasoro(2)
        dcrit = derived_critical_locus(fam, genus=1)
        assert dcrit.curvature_m0 == Fraction(1) * Fraction(1, 24)

    def test_hessian_is_kappa(self):
        """The Hessian eigenvalue at the MC point is kappa."""
        fam = heisenberg(5)
        dcrit = derived_critical_locus(fam, genus=0)
        assert dcrit.hessian_eigenvalue_kappa == Fraction(5)

    def test_gaussian_unobstructed(self):
        """Class G (Gaussian) is unobstructed: vdim = num_generators."""
        fam = heisenberg()
        dcrit = derived_critical_locus(fam, genus=0)
        assert dcrit.is_smooth_derived
        assert dcrit.virtual_dimension == 1

    def test_lie_unobstructed(self):
        """Class L (Lie) is unobstructed at generic level."""
        fam = affine_sl(2, 1)
        dcrit = derived_critical_locus(fam, genus=0)
        assert dcrit.is_smooth_derived

    def test_mixed_obstructed(self):
        """Class M (mixed/Virasoro) is obstructed."""
        fam = virasoro(1)
        dcrit = derived_critical_locus(fam, genus=0)
        assert not dcrit.is_smooth_derived
        assert dcrit.obstruction_dim > 0

    def test_dcrit_bar_match_genus0(self):
        """dCrit and bar moduli agree at genus 0."""
        for fam in STANDARD_FAMILIES.values():
            result = dcrit_matches_bar_moduli(fam, genus=0)
            assert result['both_minus_1_shifted']
            assert result['curvature_agrees']
            assert result['hessian_is_kappa']
            assert result['is_global_comparison']

    def test_dcrit_bar_match_genus1_formal(self):
        """dCrit and bar moduli comparison at genus 1 is formal only."""
        fam = heisenberg()
        result = dcrit_matches_bar_moduli(fam, genus=1)
        assert result['both_minus_1_shifted']
        assert result['is_formal_comparison']
        assert not result['is_global_comparison']


# ============================================================================
# SECTION 7: CALAQUE DERIVED AKSZ
# ============================================================================

class TestCalaqueDerivedAKSZ:
    """Verify Calaque's derived AKSZ formulation."""

    def test_calaque_shift_curve_target(self):
        """For Sigma_g source and (-1)-shifted target: shift = -3."""
        data = calaque_aksz("Sigma_g", 2, -1)
        assert data.mapping_shift == -3

    def test_calaque_shift_3fold_target(self):
        """For M^3 source and (-1)-shifted target: shift = -4."""
        data = calaque_aksz("M^3", 3, -1)
        assert data.mapping_shift == -4

    def test_calaque_compact_oriented(self):
        """Source must be compact and oriented."""
        data = calaque_aksz("Sigma_g", 2, -1)
        assert data.is_compact_source
        assert data.is_oriented_source

    def test_modular_operad_is_aksz(self):
        """The modular operad construction IS derived AKSZ."""
        result = modular_operad_as_aksz()
        assert result['mapping_shift'] == -3
        assert result['target_shift'] == -1
        assert result['source_dim'] == 2
        assert result['proved']


# ============================================================================
# SECTION 8: BV FORMALISM
# ============================================================================

class TestBVFormalism:
    """Verify BV formalism as (-1)-shifted symplectic geometry."""

    def test_bv_antibracket_is_poisson(self):
        """BV antibracket = (-1)-shifted Poisson bracket."""
        result = bv_antibracket_is_poisson(-1)
        assert result['degrees_agree']
        assert result['jacobi_identity']
        assert result['leibniz_rule']

    def test_qme_is_mc(self):
        """QME = MC equation identification."""
        result = qme_is_mc(-1)
        assert result['proved_genus0']
        assert result['proved_heisenberg_all_genus']
        assert result['conjectural_general']

    def test_bv_bar_shifts_agree(self):
        """BV and bar both give (-1)-shifted with +1 bracket degree."""
        result = verify_bv_bar_shifts()
        assert result['shifts_agree']
        assert result['degrees_agree']
        assert result['qme_mc_identification']

    def test_bv_dictionary_genus_corrections(self):
        """BV and bar genus corrections agree (both = kappa * lambda_g)."""
        fam = virasoro(26)
        bv = bv_bar_dictionary(fam, max_genus=3)
        for g in range(1, 4):
            expected = Fraction(13) * lambda_fp(g)
            assert bv.bv_effective_action_genus[g] == expected
            assert bv.bar_obstruction_genus[g] == expected

    def test_heisenberg_all_genera_proved(self):
        """For Heisenberg, BV=bar is proved at all genera."""
        fam = heisenberg()
        bv = bv_bar_dictionary(fam)
        assert bv.genus0_proved
        assert bv.higher_genus_status == "proved"

    def test_virasoro_conjectural_higher_genus(self):
        """For Virasoro, BV=bar at higher genus is conjectural."""
        fam = virasoro(1)
        bv = bv_bar_dictionary(fam)
        assert bv.genus0_proved
        assert bv.higher_genus_status == "conjectural"


# ============================================================================
# SECTION 9: JOYCE d-CRITICAL LOCI AND DT INVARIANTS
# ============================================================================

class TestJoyceDCritical:
    """Verify Joyce d-critical loci and DT invariants."""

    def test_d_critical_structure_exists(self):
        """Every family has a d-critical structure (BBDJS theorem)."""
        for fam in STANDARD_FAMILIES.values():
            data = joyce_d_critical_locus(fam)
            assert data.has_d_critical_structure
            assert data.has_orientation
            assert data.virtual_fundamental_class

    def test_dt_invariant_genus_1(self):
        """DT_1(A) = kappa/24 (Faber-Pandharipande lambda_1 = 1/24)."""
        fam = heisenberg(1)
        dt1 = dt_invariant_genus_g(fam, 1)
        assert dt1 == Fraction(1, 24)

    def test_dt_invariant_genus_2(self):
        """DT_2(A) = kappa * 7/5760."""
        fam = heisenberg(1)
        dt2 = dt_invariant_genus_g(fam, 2)
        assert dt2 == lambda_fp(2)

    def test_dt_invariant_additivity(self):
        """DT is additive for independent algebras."""
        fam1 = heisenberg(1)
        fam2 = heisenberg(2)
        result = dt_invariant_additivity(fam1, fam2, 1)
        assert result['additive']
        assert result['dt_sum_direct'] == result['dt_sum_kappa']

    def test_shadow_euler_characteristic(self):
        """Shadow Euler characteristic = sum_g F_g."""
        fam = heisenberg(1)
        data = joyce_d_critical_locus(fam, max_genus=3)
        expected = sum(lambda_fp(g) for g in range(1, 4))
        assert data.shadow_euler_characteristic == expected

    def test_behrend_weighted_euler(self):
        """Behrend weighted Euler characteristic matches shadow data."""
        fam = virasoro(26)
        result = behrend_weighted_euler(fam, max_genus=3)
        expected = Fraction(0)
        for g in range(1, 4):
            expected += Fraction(13) * lambda_fp(g)
        assert result['shadow_euler'] == expected


# ============================================================================
# SECTION 10: SAFRONOV POISSON REDUCTION
# ============================================================================

class TestSafronovReduction:
    """Verify Safronov Poisson reduction for DS."""

    def test_shift_preservation(self):
        """Safronov reduction preserves the n-shifted symplectic degree."""
        for n in [-3, -2, -1, 0, 1, 2]:
            result = safronov_shift_preservation(n)
            assert result['shift_preserved']
            assert result['input_shift'] == n
            assert result['output_shift'] == n

    def test_ds_preserves_minus_1(self):
        """DS reduction preserves (-1)-shifted on bar moduli."""
        result = ds_preserves_bar_shift()
        assert result['shift_preserved']
        assert result['shadow_tower_descends']
        assert result['proved_principal']
        assert result['proved_hook_type_A']
        assert not result['proved_general']

    def test_safronov_ds_principal(self):
        """Principal DS from sl_3 to W_3."""
        fam = affine_sl(3, 1)
        red = safronov_ds_reduction(fam, 3, "principal")
        assert red.source_shift == -1
        assert red.target_shift == -1
        assert red.reduction_preserves_shift
        assert "all types" in red.proved_corridor

    def test_safronov_ds_hook(self):
        """Hook-type DS: proved corridor in type A."""
        fam = affine_sl(4, 1)
        red = safronov_ds_reduction(fam, 4, "hook")
        assert red.reduction_preserves_shift
        assert "type A" in red.proved_corridor

    def test_safronov_ds_general_open(self):
        """General non-principal DS: bar-cobar commutation OPEN."""
        fam = affine_sl(3, 1)
        red = safronov_ds_reduction(fam, 3, "minimal")
        assert red.reduction_preserves_shift
        assert "OPEN" in red.proved_corridor


# ============================================================================
# SECTION 11: FULL PACKAGE AND CROSS-CUTTING CONSISTENCY
# ============================================================================

class TestFullPackage:
    """Verify the full DAG package and cross-cutting consistency."""

    def test_full_package_heisenberg(self):
        """Full DAG package for Heisenberg is consistent."""
        fam = heisenberg()
        pkg = full_dag_package(fam, genus=1)
        assert pkg['consistency']['all_minus_1_shifted']
        assert pkg['consistency']['poisson_degree_plus_1']
        assert pkg['consistency']['lagrangian_is_lagrangian']
        assert pkg['consistency']['aksz_shift_minus_3']
        assert pkg['consistency']['dcrit_is_symplectic']
        assert pkg['consistency']['dcrit_bar_agree']

    def test_full_package_virasoro(self):
        """Full DAG package for Virasoro is consistent."""
        fam = virasoro(1)
        pkg = full_dag_package(fam, genus=1)
        for key, val in pkg['consistency'].items():
            assert val, f"Consistency check failed: {key}"

    def test_full_package_affine(self):
        """Full DAG package for affine sl_2 is consistent."""
        fam = affine_sl(2, 1)
        pkg = full_dag_package(fam, genus=1)
        for key, val in pkg['consistency'].items():
            assert val, f"Consistency check failed: {key}"

    def test_full_package_all_families(self):
        """Full DAG package for all standard families is consistent."""
        for name, fam in STANDARD_FAMILIES.items():
            pkg = full_dag_package(fam, genus=1)
            for key, val in pkg['consistency'].items():
                assert val, f"{name}: consistency check failed: {key}"


# ============================================================================
# SECTION 12: LAMBDA_FP AND BERNOULLI CROSS-CHECKS
# ============================================================================

class TestLambdaFP:
    """Multi-path verification of Faber-Pandharipande numbers."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_bernoulli_b0(self):
        """B_0 = 1."""
        assert _bernoulli_fraction(0) == Fraction(1)

    def test_bernoulli_b1(self):
        """B_1 = -1/2."""
        assert _bernoulli_fraction(1) == Fraction(-1, 2)

    def test_bernoulli_b2(self):
        """B_2 = 1/6."""
        assert _bernoulli_fraction(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        """B_4 = -1/30."""
        assert _bernoulli_fraction(4) == Fraction(-1, 30)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_fraction(n) == Fraction(0)

    def test_lambda_1_from_bernoulli(self):
        r"""lambda_1 = (2^1 - 1)|B_2| / (2^1 * 2!) = 1*1/6 / (2*2) = 1/24.

        Independent computation from Bernoulli number.
        """
        B2 = abs(_bernoulli_fraction(2))
        num = (2 ** 1 - 1) * B2
        den = Fraction(2 ** 1) * Fraction(2)
        assert num / den == Fraction(1, 24)

    def test_lambda_genus_positive(self):
        """All lambda_g are positive (from positive |B_{2g}|)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0
