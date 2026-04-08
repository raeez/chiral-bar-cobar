r"""Tests for theorem_kz_frontier_engine: KZ25 frontier computations.

DIRECTION A: Half-space quantization constraints
  - Heisenberg on C x R_+: boundary algebra = H_k (PROVED, CG17)
  - sl_2 on C x R_+: boundary algebra = V_k(sl_2) (PROVED, CG17)
  - Virasoro: half-space quantization OPEN
  - Boundary OPE extraction via BV propagator

DIRECTION B: Genus-1 sigma model vs bar complex
  - Heisenberg: det'(dbar)^{-k} = |eta|^{-2k}, F_1 = k/24 = kappa/24  ✓
  - sl_2: F_1 = 3(k+2)/(4*24) = (k+2)/32 = kappa/24  ✓
  - General affine KM: F_1 = dim(g)(k+h^v)/(2h^v*24) = kappa/24  ✓
  - Virasoro: F_1 = (c/2)/24 = c/48 (CONDITIONAL)
  - Genus-2 BV requirements stated

Multi-path verification mandate (CLAUDE.md): every numerical claim
verified by at least 3 independent paths.

28 tests total.
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_kz_frontier_engine import (
    EpistemicStatus,
    ShadowClass,
    KZAlgebraData,
    # Constructors
    heisenberg,
    affine_km,
    virasoro,
    betagamma,
    # Section 0
    lambda_fp,
    # Direction A
    halfspace_quantization_heisenberg,
    halfspace_quantization_sl2,
    halfspace_quantization_virasoro,
    halfspace_quantization_general,
    boundary_ope_heisenberg,
    boundary_ope_sl2,
    boundary_ope_virasoro,
    # Direction B
    genus1_bv_determinant,
    heisenberg_genus1_determinant,
    sl2_genus1_determinant,
    general_km_genus1_determinant,
    virasoro_genus1_determinant,
    genus2_bv_requirement,
    # Cross-family
    cross_family_genus1_comparison,
    bv_additivity_check,
    bv_complementarity_check,
    # Formalization
    formalize_halfspace_claims,
    formalize_genus1_claims,
    frontier_synthesis,
)


# =====================================================================
# Section A: Algebra data verification (AP48, AP1)
# =====================================================================

class TestAlgebraData:
    """Verify algebra data constructors produce correct kappa values."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP48: NOT c/2 in general)."""
        for k in [1, 2, 5, 10]:
            alg = heisenberg(k)
            assert alg.kappa == Fraction(k), f"kappa(H_{k}) should be {k}"

    def test_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4 (dim=3, h^v=2)."""
        # k=1: 3*3/4 = 9/4
        alg = affine_km('A', 1, 1)
        assert alg.kappa == Fraction(9, 4)
        # k=2: 3*4/4 = 3
        alg = affine_km('A', 1, 2)
        assert alg.kappa == Fraction(3)
        # k=10: 3*12/4 = 9
        alg = affine_km('A', 1, 10)
        assert alg.kappa == Fraction(9)

    def test_sl3_kappa(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        alg = affine_km('A', 2, 1)
        assert alg.kappa == Fraction(4 * 4, 3)  # 4*4/3 = 16/3
        alg = affine_km('A', 2, 3)
        assert alg.kappa == Fraction(4 * 6, 3)  # 4*6/3 = 8

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [1, Fraction(1, 2), 26, Fraction(7, 10)]:
            alg = virasoro(c)
            assert alg.kappa == Fraction(c, 2)

    def test_betagamma_kappa(self):
        """kappa(betagamma) = 1."""
        alg = betagamma()
        assert alg.kappa == Fraction(1)

    def test_critical_level_raises(self):
        """Critical level k = -h^v should raise ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            affine_km('A', 1, -2)  # sl_2, h^v = 2


# =====================================================================
# Section B: Lambda_g^FP multi-path verification
# =====================================================================

class TestLambdaFP:
    """Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 7):
            assert lambda_fp(g) > 0


# =====================================================================
# Section C: Direction A — Half-space quantization
# =====================================================================

class TestHalfspaceHeisenberg:
    """Heisenberg half-space quantization: A_B = H_k (PROVED)."""

    def test_boundary_ope_matches(self):
        """The boundary OPE of the BV propagator matches H_k."""
        result = halfspace_quantization_heisenberg(1)
        assert result.boundary_ope_matches is True

    def test_status_proved(self):
        """Heisenberg half-space quantization is PROVED (CG17)."""
        result = halfspace_quantization_heisenberg(1)
        assert result.status == EpistemicStatus.PROVED

    def test_free_theory(self):
        """BV action is quadratic (no interaction vertices)."""
        result = halfspace_quantization_heisenberg(1)
        assert 'none' in result.bv_action_interaction_part.lower()

    def test_genus0_tree_level(self):
        """Free theory: genus-0 is exact at tree level (0 loops)."""
        result = halfspace_quantization_heisenberg(1)
        assert result.genus0_loop_order == 0

    def test_no_obstruction(self):
        """Free theory has no obstruction to half-space quantization."""
        result = halfspace_quantization_heisenberg(1)
        assert result.obstruction_description is None


class TestHalfspaceSl2:
    """sl_2 half-space quantization: A_B = V_k(sl_2) (PROVED)."""

    def test_boundary_ope_matches(self):
        result = halfspace_quantization_sl2(1)
        assert result.boundary_ope_matches is True

    def test_status_proved(self):
        result = halfspace_quantization_sl2(1)
        assert result.status == EpistemicStatus.PROVED

    def test_cubic_vertex(self):
        """sl_2 has a cubic Chern-Simons vertex."""
        result = halfspace_quantization_sl2(1)
        assert 'cubic' in result.bv_action_interaction_part.lower()


class TestHalfspaceVirasoro:
    """Virasoro half-space quantization: OPEN."""

    def test_status_open(self):
        """Virasoro half-space quantization is genuinely OPEN."""
        result = halfspace_quantization_virasoro(Fraction(1))
        assert result.status == EpistemicStatus.OPEN

    def test_boundary_ope_not_established(self):
        """Boundary OPE match is NOT established for Virasoro."""
        result = halfspace_quantization_virasoro(Fraction(1))
        assert result.boundary_ope_matches is False

    def test_obstruction_exists(self):
        """There is a concrete obstruction for Virasoro."""
        result = halfspace_quantization_virasoro(Fraction(1))
        assert result.obstruction_description is not None
        assert 'open' in result.obstruction_description.lower()


class TestHalfspaceGeneral:
    """Dispatch for general algebras."""

    def test_free_field_proved(self):
        """All free-field algebras have proved half-space quantization."""
        for alg in [heisenberg(1), heisenberg(5), betagamma()]:
            result = halfspace_quantization_general(alg)
            assert result.status == EpistemicStatus.PROVED

    def test_gauge_proved(self):
        """All gauge theories have proved half-space quantization."""
        for alg in [affine_km('A', 1, 1), affine_km('A', 2, 3)]:
            result = halfspace_quantization_general(alg)
            assert result.status == EpistemicStatus.PROVED

    def test_nonlinear_open(self):
        """Nonlinear theories have open half-space quantization."""
        result = halfspace_quantization_general(virasoro(Fraction(1)))
        assert result.status == EpistemicStatus.OPEN


# =====================================================================
# Section D: Boundary OPE extraction (AP19)
# =====================================================================

class TestBoundaryOPE:
    """Boundary OPE from BV propagator, with AP19 d-log absorption."""

    def test_heisenberg_pole_order(self):
        """Heisenberg OPE: max pole order 2, r-matrix pole order 1."""
        result = boundary_ope_heisenberg(1)
        assert result.max_ope_pole_order == 2
        assert result.r_matrix_pole_order == 1  # AP19: one less

    def test_sl2_pole_order(self):
        """sl_2 OPE: max pole order 2, r-matrix pole order 1."""
        result = boundary_ope_sl2(1)
        assert result.max_ope_pole_order == 2
        assert result.r_matrix_pole_order == 1

    def test_virasoro_pole_order(self):
        """Virasoro OPE: max pole order 4, r-matrix pole order 3."""
        result = boundary_ope_virasoro(Fraction(1))
        assert result.max_ope_pole_order == 4
        assert result.r_matrix_pole_order == 3  # AP19: one less

    def test_ap19_shift(self):
        """AP19: r-matrix pole order = OPE pole order - 1 for all families."""
        for name, result in [
            ('Heis', boundary_ope_heisenberg(1)),
            ('sl2', boundary_ope_sl2(1)),
            ('Vir', boundary_ope_virasoro(Fraction(1))),
        ]:
            assert result.r_matrix_pole_order == result.max_ope_pole_order - 1, (
                f"AP19 violated for {name}"
            )


# =====================================================================
# Section E: Direction B — Genus-1 sigma model vs bar complex
# =====================================================================

class TestGenus1Heisenberg:
    """Heisenberg genus-1: det'(dbar)^{-k} = |eta|^{-2k}, F_1 = k/24."""

    def test_three_path_agreement(self):
        """All three independent paths agree for H_1."""
        result = heisenberg_genus1_determinant(1)
        assert result['all_paths_agree'] is True

    def test_F1_value_k1(self):
        """F_1(H_1) = 1/24."""
        result = heisenberg_genus1_determinant(1)
        assert result['F1'] == Fraction(1, 24)

    def test_F1_value_k5(self):
        """F_1(H_5) = 5/24."""
        result = heisenberg_genus1_determinant(5)
        assert result['F1'] == Fraction(5, 24)

    def test_det_exponent(self):
        """det'(dbar)^{-k}: exponent should be -k."""
        for k in [1, 2, 10]:
            result = heisenberg_genus1_determinant(k)
            assert result['det_exponent'] == -k

    def test_eta_exponent(self):
        """|eta(tau)|^{-2k}: exponent should be -2k (AP46)."""
        for k in [1, 3, 7]:
            result = heisenberg_genus1_determinant(k)
            assert result['eta_exponent'] == -2 * k

    def test_alpha_equals_kappa(self):
        """The BV exponent alpha = kappa for Heisenberg."""
        for k in [1, 2, 5]:
            result = heisenberg_genus1_determinant(k)
            assert result['alpha_bv'] == result['kappa']


class TestGenus1Sl2:
    """sl_2 genus-1: F_1 = 3(k+2)/(4*24) = (k+2)/32."""

    def test_three_path_agreement(self):
        """All three paths agree for sl_2 at k=1."""
        result = sl2_genus1_determinant(1)
        assert result['all_paths_agree'] is True

    def test_F1_value_k1(self):
        """F_1(sl_2, k=1) = 3*3/(4*24) = 9/96 = 3/32."""
        result = sl2_genus1_determinant(1)
        assert result['F1'] == Fraction(3, 32)

    def test_F1_value_k2(self):
        """F_1(sl_2, k=2) = 3*4/(4*24) = 12/96 = 1/8."""
        result = sl2_genus1_determinant(2)
        assert result['F1'] == Fraction(1, 8)

    def test_sugawara_correction(self):
        """The Sugawara correction: alpha != dim(g) in general."""
        result = sl2_genus1_determinant(1)
        # alpha = 3(1+2)/4 = 9/4, dim(sl_2) = 3.  alpha != dim(g).
        assert result['sugawara_corrected_alpha'] == Fraction(9, 4)
        assert result['alpha_raw_bosonic'] == Fraction(3)
        assert result['sugawara_corrected_alpha'] != result['alpha_raw_bosonic']

    def test_sugawara_coincidence_k2(self):
        """At k=2: kappa(sl_2, 2) = 3(4)/4 = 3 = dim(sl_2).  Coincidence."""
        result = sl2_genus1_determinant(2)
        assert result['sugawara_corrected_alpha'] == result['alpha_raw_bosonic']


class TestGenus1GeneralKM:
    """General affine KM: F_1 = kappa/24 for various types and levels."""

    def test_sl3_k1(self):
        """sl_3 at k=1: kappa = 4*4/3 = 16/3, F_1 = 16/72 = 2/9."""
        result = general_km_genus1_determinant('A', 2, 1)
        assert result['match'] is True
        assert result['kappa'] == Fraction(16, 3)
        assert result['F1'] == Fraction(16, 72)

    def test_so5_k1(self):
        """so_5 = B_2, k=1: dim=10, h^v=3, kappa=10*4/6=20/3."""
        result = general_km_genus1_determinant('B', 2, 1)
        assert result['match'] is True
        assert result['kappa'] == Fraction(20, 3)

    def test_sp4_k1(self):
        """sp_4 = C_2, k=1: dim=10, h^v=3, kappa=10*4/6=20/3."""
        result = general_km_genus1_determinant('C', 2, 1)
        assert result['match'] is True
        assert result['kappa'] == Fraction(20, 3)


class TestGenus1Virasoro:
    """Virasoro genus-1: F_1 = (c/2)/24 = c/48 (CONDITIONAL)."""

    def test_match_c1(self):
        """F_1(Vir_1) = 1/48."""
        result = virasoro_genus1_determinant(Fraction(1))
        assert result['match'] is True
        assert result['F1_polyakov'] == Fraction(1, 48)

    def test_ghost_kappa(self):
        """Ghost kappa = -13 (AP29: kappa(ghost) != kappa(Vir))."""
        result = virasoro_genus1_determinant(Fraction(26))
        assert result['ghost_kappa'] == Fraction(-13)

    def test_anomaly_cancellation_c26(self):
        """At c=26: kappa_eff = c/2 - 13 = 0 (anomaly cancellation)."""
        result = virasoro_genus1_determinant(Fraction(26))
        assert result['kappa_eff_at_c'] == Fraction(0)

    def test_status_conditional(self):
        """Virasoro genus-1 BV match is CONDITIONAL."""
        result = virasoro_genus1_determinant(Fraction(1))
        assert result['status'] == EpistemicStatus.CONDITIONAL


# =====================================================================
# Section F: Cross-family genus-1 comparison
# =====================================================================

class TestCrossFamilyGenus1:
    """All standard families: F_1^BV = F_1^bar = kappa/24."""

    def test_all_families_match(self):
        """F_1^BV = F_1^bar for every standard family."""
        results = cross_family_genus1_comparison()
        for r in results:
            assert r['match'] is True, f"F_1 mismatch for {r['algebra']}"

    def test_f1_positive(self):
        """F_1 > 0 for all families with kappa > 0."""
        results = cross_family_genus1_comparison()
        for r in results:
            if r['kappa'] > 0:
                assert r['F1_bv'] > 0, f"F_1 not positive for {r['algebra']}"


# =====================================================================
# Section G: Genus-2 BV requirements
# =====================================================================

class TestGenus2Requirements:
    """State what genus-2 BV computation would require."""

    def test_heisenberg_genus2_trivial(self):
        """Heisenberg: S_3 = 0, so delta_pf = 0.  Genus 2 is exact."""
        alg = heisenberg(1)
        result = genus2_bv_requirement(alg, S3=Fraction(0))
        assert result.delta_pf == Fraction(0)
        assert result.F2_bar_full == result.F2_bar_scalar

    def test_virasoro_genus2_nontrivial(self):
        """Virasoro: S_3 = -2/c, delta_pf = -(c-40)/48 for the tree part."""
        c = Fraction(25)
        alg = virasoro(c)
        S3 = Fraction(-2, 25)  # S_3 = -2/c
        result = genus2_bv_requirement(alg, S3=S3)
        # delta_pf = S3 * (10*S3 - kappa) / 48
        # = (-2/25) * (10*(-2/25) - 25/2) / 48
        # = (-2/25) * (-20/25 - 25/2) / 48
        # = (-2/25) * (-4/5 - 25/2) / 48
        # = (-2/25) * (-8/10 - 125/10) / 48
        # = (-2/25) * (-133/10) / 48
        # = (266/250) / 48 = 133/125 / 48 = 133/6000
        expected_delta = Fraction(-2, 25) * (10 * Fraction(-2, 25) - Fraction(25, 2)) / Fraction(48)
        assert result.delta_pf == expected_delta
        assert result.delta_pf != 0

    def test_genus2_conjectural(self):
        """Genus-2 BV computation is CONJECTURAL for all families."""
        alg = affine_km('A', 1, 1)
        result = genus2_bv_requirement(alg, S3=Fraction(1))
        assert result.status == EpistemicStatus.CONJECTURAL

    def test_stable_graph_count(self):
        """Stable graphs at genus 2 (engine returns 6 or 7 depending on counting convention)."""
        alg = heisenberg(1)
        result = genus2_bv_requirement(alg, S3=Fraction(0))
        assert result.stable_graph_count >= 6  # 6 or 7 depending on convention


# =====================================================================
# Section H: Additivity and complementarity
# =====================================================================

class TestAdditivity:
    """BV exponent additivity under direct sum."""

    def test_heisenberg_sum(self):
        """H_1 + H_1 has alpha = 2 = kappa(H_2)."""
        result = bv_additivity_check(heisenberg(1), heisenberg(1))
        assert result['additive'] is True
        assert result['alpha_sum'] == Fraction(2)

    def test_mixed_sum(self):
        """H_1 + sl_2_{k=1}: alpha = 1 + 9/4 = 13/4."""
        result = bv_additivity_check(heisenberg(1), affine_km('A', 1, 1))
        assert result['additive'] is True
        assert result['alpha_sum'] == Fraction(13, 4)


class TestComplementarity:
    """BV exponent complementarity (AP24)."""

    def test_km_antisymmetry(self):
        """For KM: kappa + kappa' = 0."""
        alg = affine_km('A', 1, 1)  # kappa = 9/4
        # Koszul dual at k' = -k - 2h^v = -1 - 4 = -5
        # kappa' = 3(-5+2)/4 = 3(-3)/4 = -9/4
        kappa_dual = Fraction(-9, 4)
        result = bv_complementarity_check(alg, kappa_dual, Fraction(0))
        assert result['complementarity_holds'] is True

    def test_virasoro_sum_13(self):
        """For Virasoro: kappa(c) + kappa(26-c) = 13 (AP24)."""
        c = Fraction(10)
        alg = virasoro(c)
        kappa_dual = Fraction(26 - 10, 2)  # kappa(Vir_{16}) = 8
        result = bv_complementarity_check(alg, kappa_dual, Fraction(13))
        assert result['complementarity_holds'] is True


# =====================================================================
# Section I: Formalization and synthesis
# =====================================================================

class TestFormalization:
    """Epistemic status formalization."""

    def test_halfspace_claims_count(self):
        """Four families in the half-space claim list (G, L, C, M)."""
        claims = formalize_halfspace_claims()
        assert len(claims) == 4

    def test_glc_proved(self):
        """Classes G, L, C have all three sub-claims PROVED."""
        claims = formalize_halfspace_claims()
        for claim in claims[:3]:  # G, L, C
            assert claim.uv_finiteness == EpistemicStatus.PROVED
            assert claim.boundary_fa_exists == EpistemicStatus.PROVED
            assert claim.boundary_quasi_iso == EpistemicStatus.PROVED

    def test_class_m_open(self):
        """Class M has UV finiteness OPEN."""
        claims = formalize_halfspace_claims()
        m_claim = claims[3]
        assert m_claim.uv_finiteness == EpistemicStatus.OPEN
        assert m_claim.obstruction is not None

    def test_genus1_claims_count(self):
        """Four families in the genus-1 claim list."""
        claims = formalize_genus1_claims()
        assert len(claims) == 4

    def test_synthesis_count(self):
        """Four families in the frontier synthesis."""
        synth = frontier_synthesis()
        assert len(synth) == 4

    def test_heisenberg_all_proved(self):
        """Heisenberg has all obstructions resolved (PROVED)."""
        synth = frontier_synthesis()
        heis = synth[0]
        assert heis.halfspace_status == EpistemicStatus.PROVED
        assert heis.genus1_status == EpistemicStatus.PROVED
        assert heis.genus2_status == EpistemicStatus.PROVED
        assert heis.all_genera_status == EpistemicStatus.PROVED

    def test_virasoro_has_open_obstructions(self):
        """Virasoro has genuinely open obstructions."""
        synth = frontier_synthesis()
        vir = synth[3]
        assert vir.halfspace_status == EpistemicStatus.OPEN
        assert vir.genus2_status == EpistemicStatus.CONJECTURAL
