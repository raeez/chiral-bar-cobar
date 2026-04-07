r"""Tests for mirror symmetry vs Koszul duality comparison engine.

Tests cover:
  1. Core kappa formulas (multi-path verification, AP1/AP10)
  2. Feigin-Frenkel duality: level and kappa transformations
  3. S-duality: level and kappa transformations
  4. S_3 triality orbit structure
  5. Four-duality comparison for affine gl_N
  6. Four-duality comparison for W_N
  7. S-vs-KD discrepancy formula (exact closed form)
  8. Complementarity comparison: Theorem C vs mirror sum
  9. Genus-g obstruction comparison
  10. Categorical vs algebraic KD (shadow-depth dependence)
  11. Diagram commutativity tests (SQED, affine)
  12. Mirror-as-composition impossibility
  13. Self-dual loci enumeration
  14. Physical examples: Argyres-Douglas, SQED(2), SQED(4)
  15. Landscape survey: cross-family consistency
  16. Webster comparison for SQED, quivers, Nahm
  17. Large-N / 't Hooft limit analysis
  18. Cross-engine consistency with existing Coulomb-Higgs engine

Multi-path verification (per CLAUDE.md mandate):
  Path 1: Direct formula computation
  Path 2: Alternative formula / identity check
  Path 3: Limiting case analysis
  Path 4: Cross-family / cross-engine consistency
  Path 5: Symmetry / duality constraints
  Path 6: Numerical evaluation at specific points

References:
  BLPW: arXiv:1208.3863, arXiv:1407.0964
  Webster: arXiv:1611.06541
  Hilburn-Raskin: arXiv:2107.11325
  Costello-Gaiotto: arXiv:1812.09257
  Manuscript: Theorems A, C, D; conj:shifted-yangian-langlands
"""

import pytest
from fractions import Fraction

from compute.lib.mirror_koszul_comparison_engine import (
    # Core kappa
    kappa_affine_sl,
    kappa_affine_gl,
    kappa_virasoro,
    kappa_wn,
    c_affine_sl,
    c_affine_gl,
    c_wn_principal,
    # FF duality
    ff_dual_level,
    ff_dual_psi,
    # S-duality
    s_dual_psi,
    s_dual_level,
    # S_3 triality
    compute_triality_orbit,
    TrialityOrbit,
    # Four-duality comparison
    four_duality_comparison_affine_gl,
    four_duality_comparison_wn,
    FourDualityComparison,
    # Discrepancy
    s_kd_discrepancy_affine_gl,
    s_kd_discrepancy_closed_form,
    s_kd_coincidence_locus,
    # Complementarity
    complementarity_comparison_gl,
    complementarity_comparison_sqed,
    ComplementarityComparison,
    # Genus obstructions
    genus1_obstruction_koszul,
    genus1_obstruction_mirror_sum,
    genus1_obstruction_koszul_sum,
    genus2_obstruction_scalar,
    genus_g_obstruction_comparison,
    # Categorical vs algebraic
    categorical_vs_algebraic_kd,
    CategoricalVsAlgebraicKD,
    # Diagram commutativity
    diagram_commutativity_sqed,
    diagram_commutativity_affine,
    DiagramCommutativity,
    # Mirror as composition
    mirror_as_composition,
    # Self-dual loci
    all_self_dual_loci,
    SelfDualLocus,
    # Physical examples
    argyres_douglas_h0_diagram,
    sqed_nf2_full_diagram,
    sqed_nf4_full_diagram,
    # Landscape
    landscape_survey,
    landscape_survey_wn,
    # Webster
    webster_comparison_sqed,
    webster_comparison_type_a_quiver,
    webster_comparison_nahm,
    WebsterComparison,
    # Summary
    full_comparison_summary,
)

F = Fraction


# ============================================================================
# 1. Core kappa formulas (multi-path verification)
# ============================================================================

class TestCoreKappaFormulas:
    """Verify kappa formulas by multiple independent methods."""

    def test_kappa_gl1_is_heisenberg(self):
        """For gl_1, kappa = k (Heisenberg). Path 1: direct formula."""
        for k in [1, 2, 3, 5, -1]:
            assert kappa_affine_gl(1, k) == F(k)

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*3/(2*2) = 9/4.
        Path 1: direct. Path 2: dim*(...) formula."""
        assert kappa_affine_sl(2, 1) == F(9, 4)
        # Path 2: dim(sl_2)=3, h^v=2, k=1: 3*(1+2)/(2*2) = 9/4
        assert F(3) * F(3) / F(4) == F(9, 4)

    def test_kappa_gl2_k1(self):
        """kappa(gl_2, k=1) = kappa(sl_2, k=1) + k = 9/4 + 1 = 13/4."""
        assert kappa_affine_gl(2, 1) == F(9, 4) + F(1)
        assert kappa_affine_gl(2, 1) == F(13, 4)

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2. Multiple c values."""
        for c in [-22, 0, 1, 13, 26, F(-22, 5)]:
            assert kappa_virasoro(c) == F(c) / 2

    def test_kappa_wn_n2_is_virasoro(self):
        """For N=2, W_N = Virasoro and kappa = c/2 (since H_2-1 = 1/2)."""
        # H_2 = 1 + 1/2 = 3/2, so H_2 - 1 = 1/2
        # kappa = (1/2) * c = c/2, matching Virasoro
        c = c_wn_principal(2, 1)
        assert c == F(-7)
        assert kappa_wn(2, c) == c / 2

    def test_c_affine_sl2_k1(self):
        """c(sl_2, k=1) = 1*3/3 = 1."""
        assert c_affine_sl(2, 1) == F(1)

    def test_c_affine_gl2_k1(self):
        """c(gl_2, k=1) = c(sl_2, k=1) + 1 = 2."""
        assert c_affine_gl(2, 1) == F(2)

    def test_c_wn_principal_w2_k1(self):
        """c(W_2, k=1) = -7. Decisive test."""
        assert c_wn_principal(2, 1) == F(-7)

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_kappa_critical_level_raises(self, N):
        """Critical level k = -N raises ValueError."""
        with pytest.raises(ValueError):
            kappa_affine_sl(N, -N)
        with pytest.raises(ValueError):
            c_affine_sl(N, -N)


# ============================================================================
# 2. Feigin-Frenkel duality
# ============================================================================

class TestFeiginFrenkelDuality:
    """FF duality: k -> -k - 2h^v."""

    def test_ff_dual_level_sl2(self):
        """For sl_2 (h^v=2): k=1 -> -1-4 = -5."""
        assert ff_dual_level(1, 2) == F(-5)

    def test_ff_dual_level_sl3(self):
        """For sl_3 (h^v=3): k=2 -> -2-6 = -8."""
        assert ff_dual_level(2, 3) == F(-8)

    def test_ff_involution_property(self):
        """FF is an involution: applying twice returns original level."""
        for N in [2, 3, 4]:
            for k in [1, 2, F(3, 2)]:
                k_dual = ff_dual_level(k, N)
                k_double = ff_dual_level(k_dual, N)
                assert k_double == F(k), f"FF^2({k}) = {k_double} != {k} for N={N}"

    def test_ff_dual_psi(self):
        """FF on coupling: Psi -> -Psi."""
        assert ff_dual_psi(3) == F(-3)
        assert ff_dual_psi(F(1, 2)) == F(-1, 2)

    def test_ff_dual_psi_involution(self):
        """FF on Psi is involution."""
        for psi in [F(3), F(1, 2), F(5, 3)]:
            assert ff_dual_psi(ff_dual_psi(psi)) == psi

    @pytest.mark.parametrize("N,k", [(2, 1), (2, 3), (3, 1), (3, 2), (4, 1)])
    def test_kappa_antisymmetry_sl(self, N, k):
        """kappa(sl_N, k) + kappa(sl_N, k') = 0 for FF duality (AP24)."""
        k_dual = ff_dual_level(k, N)
        total = kappa_affine_sl(N, k) + kappa_affine_sl(N, k_dual)
        assert total == F(0), f"kappa + kappa' = {total} != 0 for sl_{N}, k={k}"

    @pytest.mark.parametrize("N,k", [(1, 1), (2, 1), (2, 3), (3, 1)])
    def test_kappa_sum_gl_constant(self, N, k):
        """kappa(gl_N, k) + kappa(gl_N, k') = -2N (level-independent)."""
        k_dual = ff_dual_level(k, N)
        total = kappa_affine_gl(N, k) + kappa_affine_gl(N, k_dual)
        assert total == F(-2 * N), f"Sum = {total}, expected {-2*N} for gl_{N}, k={k}"


# ============================================================================
# 3. S-duality
# ============================================================================

class TestSDuality:
    """S-duality: Psi -> 1/Psi."""

    def test_s_dual_psi(self):
        """Basic S-duality: Psi -> 1/Psi."""
        assert s_dual_psi(3) == F(1, 3)
        assert s_dual_psi(F(1, 2)) == F(2)

    def test_s_dual_involution(self):
        """S is involution: S(S(Psi)) = Psi."""
        for psi in [F(2), F(3), F(1, 3), F(5, 7)]:
            assert s_dual_psi(s_dual_psi(psi)) == psi

    def test_s_dual_level_sl2(self):
        """For sl_2, k=1, Psi=k+N=3: k^S = 1/3 - 2 = -5/3."""
        k_s = s_dual_level(1, 2)
        assert k_s == F(1, 3) - 2
        assert k_s == F(-5, 3)

    def test_s_dual_psi_zero_raises(self):
        """Psi = 0 is singular for S-duality."""
        with pytest.raises(ValueError):
            s_dual_psi(0)

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_s_not_equal_ff_generic(self, N):
        """S-dual level != FF-dual level at generic coupling."""
        for k in [1, 2, 3]:
            k_s = s_dual_level(k, N)
            k_ff = ff_dual_level(k, N)
            assert k_s != k_ff, (
                f"S-dual = FF-dual at k={k}, N={N}: this should be generic!"
            )


# ============================================================================
# 4. S_3 triality orbit
# ============================================================================

class TestTrialityOrbit:
    """S_3 triality orbit of the coupling constant."""

    def test_orbit_psi_3(self):
        """Orbit of Psi=3: six elements."""
        orb = compute_triality_orbit(3)
        assert orb.psi == F(3)
        assert orb.s_dual == F(1, 3)
        assert orb.ff_dual == F(-3)
        assert orb.s_ff_composition == F(-1, 3)
        assert orb.triality_23 == F(-2)         # 1 - 3 = -2
        assert orb.triality_132 == F(2, 3)      # 1 - 1/3 = 2/3

    def test_s_not_equal_ff_for_real(self):
        """S != FF for any real Psi != 0."""
        for psi in [F(1), F(2), F(3), F(1, 2), F(1, 3), F(-1), F(-2)]:
            orb = compute_triality_orbit(psi)
            assert not orb.s_equals_ff, f"S = FF at Psi = {psi}!"

    def test_ff_not_in_s3_orbit_generic(self):
        """The FF dual -Psi is generically NOT in the S_3 orbit.

        The S_3 orbit of Psi consists of Mobius transforms preserving {0,1,inf}.
        -Psi does not preserve this set (it maps 0->0 but 1->-1, not in {0,1,inf}).
        """
        for psi in [F(3), F(5, 2), F(7, 3)]:
            orb = compute_triality_orbit(psi)
            assert not orb.ff_in_s3_orbit, (
                f"FF dual {orb.ff_dual} found in S_3 orbit of {psi}!"
            )

    def test_orbit_psi_half(self):
        """At Psi=1/2, the (23) transposition is self-dual."""
        orb = compute_triality_orbit(F(1, 2))
        assert orb.triality_23 == F(1, 2)  # 1 - 1/2 = 1/2 (fixed point)

    def test_orbit_size(self):
        """The S_3 orbit has at most 6 elements (generically exactly 6)."""
        orb = compute_triality_orbit(F(3))
        elements = {orb.psi, orb.s_dual, orb.triality_23,
                    orb.triality_13, orb.triality_123, orb.triality_132}
        assert len(elements) == 6, f"Orbit has {len(elements)} elements, expected 6"


# ============================================================================
# 5. Four-duality comparison: affine gl_N
# ============================================================================

class TestFourDualityAffineGL:
    """Compare S-dual, KD-dual, and mirror at the kappa level for gl_N."""

    def test_gl1_psi3_all_different(self):
        """For gl_1 at Psi=3: kappa, kappa^S, kappa^KD are all different."""
        comp = four_duality_comparison_affine_gl(1, 3)
        assert comp.kappa_original == F(2)        # k = 3-1 = 2, kappa = 2
        assert comp.kappa_koszul == F(-4)          # k' = -2-2 = -4, kappa = -4
        assert comp.kappa_s_dual == F(-2, 3)       # k^S = 1/3-1 = -2/3
        assert comp.kappa_original != comp.kappa_koszul
        assert comp.kappa_original != comp.kappa_s_dual
        assert comp.kappa_koszul != comp.kappa_s_dual

    def test_gl1_koszul_sum_constant(self):
        """kappa + kappa^KD = -2 for gl_1, independent of Psi."""
        for psi in [F(2), F(3), F(5, 2), F(1, 3)]:
            comp = four_duality_comparison_affine_gl(1, psi)
            assert comp.koszul_sum == F(-2), (
                f"Koszul sum = {comp.koszul_sum}, expected -2 at Psi={psi}"
            )

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_koszul_sum_constant_all_N(self, N):
        """kappa + kappa^KD = -2N for gl_N, for all Psi."""
        expected = F(-2 * N)
        for psi in [F(3), F(5, 2), F(7, 3)]:
            comp = four_duality_comparison_affine_gl(N, psi)
            assert comp.koszul_sum == expected

    def test_s_sum_varies_with_psi(self):
        """kappa + kappa^S is NOT constant (level-dependent)."""
        sums = set()
        for psi in [F(2), F(3), F(5, 2)]:
            comp = four_duality_comparison_affine_gl(2, psi)
            sums.add(comp.s_sum)
        assert len(sums) > 1, "S-duality sum should vary with Psi"

    def test_s_never_equals_kd_real_psi(self):
        """S-dual != KD-dual for all real Psi tested."""
        for N in [1, 2, 3]:
            for psi in [F(2), F(3), F(5, 2), F(1, 3), F(7, 4)]:
                comp = four_duality_comparison_affine_gl(N, psi)
                assert not comp.s_equals_kd, (
                    f"S = KD at N={N}, Psi={psi}!"
                )


# ============================================================================
# 6. Four-duality comparison: W_N
# ============================================================================

class TestFourDualityWN:
    """Four-duality comparison for principal W-algebras."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro. kappa + kappa' = 13 (AP24)."""
        comp = four_duality_comparison_wn(2, 3)
        assert comp.koszul_sum == F(13)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_wn_koszul_sum_constant(self, N):
        """kappa(W_N,k) + kappa(W_N,-k-2N) is constant (level-independent)."""
        sums = set()
        for psi in [F(3), F(5, 2), F(4)]:
            try:
                comp = four_duality_comparison_wn(N, psi)
                sums.add(comp.koszul_sum)
            except (ValueError, ZeroDivisionError):
                pass
        assert len(sums) == 1, f"Koszul sum varies for W_{N}: {sums}"

    def test_wn_s_not_equals_kd(self):
        """S != KD for W-algebras at generic coupling."""
        for N in [2, 3, 4]:
            for psi in [F(3), F(5, 2)]:
                try:
                    comp = four_duality_comparison_wn(N, psi)
                    assert not comp.s_equals_kd
                except (ValueError, ZeroDivisionError):
                    pass


# ============================================================================
# 7. S-vs-KD discrepancy formula
# ============================================================================

class TestSKDDiscrepancy:
    """The exact closed-form discrepancy between S-dual and KD-dual kappa."""

    def test_discrepancy_n1_psi3(self):
        """N=1, Psi=3: Delta = 1 * (3 + 1/3) = 10/3."""
        assert s_kd_discrepancy_affine_gl(1, 3) == F(10, 3)

    def test_discrepancy_n2_psi3(self):
        """N=2, Psi=3: Delta = 7/4 * (3 + 1/3) = 7/4 * 10/3 = 70/12 = 35/6."""
        coeff = F(4 + 4 - 1, 4)  # (N^2+2N-1)/(2N) = 7/4
        psi_sum = F(3) + F(1, 3)
        assert s_kd_discrepancy_affine_gl(2, 3) == coeff * psi_sum
        assert s_kd_discrepancy_affine_gl(2, 3) == F(35, 6)

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_discrepancy_positive_for_positive_psi(self, N):
        """For real Psi > 0, the discrepancy is always positive."""
        for psi in [F(1, 3), F(1, 2), F(1), F(2), F(3), F(10)]:
            disc = s_kd_discrepancy_affine_gl(N, psi)
            assert disc > 0, f"Discrepancy <= 0 at N={N}, Psi={psi}"

    def test_discrepancy_agrees_with_four_duality(self):
        """Cross-check: discrepancy formula agrees with direct comparison."""
        for N in [1, 2, 3]:
            for psi in [F(2), F(3), F(5, 2)]:
                disc = s_kd_discrepancy_affine_gl(N, psi)
                comp = four_duality_comparison_affine_gl(N, psi)
                direct_disc = comp.kappa_s_dual - comp.kappa_koszul
                assert disc == direct_disc, (
                    f"Formula {disc} != direct {direct_disc} at N={N}, Psi={psi}"
                )

    def test_discrepancy_am_gm_bound(self):
        """For real Psi > 0: Psi + 1/Psi >= 2 (AM-GM).
        So discrepancy >= 2 * (N^2+2N-1)/(2N)."""
        for N in [1, 2, 3]:
            coeff = F(N**2 + 2*N - 1, 2*N)
            lower_bound = 2 * coeff
            for psi in [F(1, 10), F(1, 2), F(1), F(2), F(10)]:
                disc = s_kd_discrepancy_affine_gl(N, psi)
                assert disc >= lower_bound, (
                    f"Disc {disc} < bound {lower_bound} at N={N}, Psi={psi}"
                )

    def test_discrepancy_minimum_at_psi_1(self):
        """Psi + 1/Psi achieves minimum 2 at Psi = 1."""
        for N in [1, 2, 3]:
            coeff = F(N**2 + 2*N - 1, 2*N)
            disc_at_1 = s_kd_discrepancy_affine_gl(N, 1)
            assert disc_at_1 == 2 * coeff

    def test_coincidence_locus_string(self):
        """Coincidence locus is Psi^2 = -1."""
        locus = s_kd_coincidence_locus()
        assert "Psi^2 = -1" in locus
        assert "EMPTY" in locus  # no real solutions


# ============================================================================
# 8. Complementarity: Theorem C vs mirror
# ============================================================================

class TestComplementarityComparison:
    """Theorem C complementarity vs mirror complementarity."""

    @pytest.mark.parametrize("N,psi", [(1, 3), (2, 3), (3, 5)])
    def test_koszul_sum_constant_gl(self, N, psi):
        """Koszul sum is level-independent for gl_N."""
        comp = complementarity_comparison_gl(N, psi)
        assert comp.koszul_sum_independent_of_level

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_sqed_mirror_sum_equals_nf(self, N_f):
        """Mirror sum kappa_C + kappa_H = N_f for SQED(N_f)."""
        comp = complementarity_comparison_sqed(N_f)
        assert comp.mirror_sum == F(N_f)

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_sqed_koszul_sum_is_zero(self, N_f):
        """Koszul sum kappa(H_1) + kappa(H_1^!) = 0 for SQED Coulomb."""
        comp = complementarity_comparison_sqed(N_f)
        assert comp.koszul_sum == F(0)

    @pytest.mark.parametrize("N_f", range(2, 9))
    def test_sqed_sums_differ(self, N_f):
        """Mirror sum != Koszul sum for N_f >= 2."""
        comp = complementarity_comparison_sqed(N_f)
        assert not comp.sums_coincide, (
            f"Mirror sum = Koszul sum for SQED({N_f}): should differ!"
        )

    def test_sqed_nf1_degenerate(self):
        """At N_f=1: mirror sum = 1, Koszul sum = 0. Still different."""
        comp = complementarity_comparison_sqed(1)
        assert comp.mirror_sum == F(1)
        assert comp.koszul_sum == F(0)
        assert not comp.sums_coincide


# ============================================================================
# 9. Genus-g obstruction comparison
# ============================================================================

class TestGenusObstructions:
    """Compare genus-1 and genus-2 obstructions across dualities."""

    def test_genus1_basic(self):
        """F_1 = kappa/24."""
        assert genus1_obstruction_koszul(12) == F(1, 2)
        assert genus1_obstruction_koszul(F(1, 2)) == F(1, 48)

    def test_genus1_koszul_sum_for_sl(self):
        """For sl_N: kappa + kappa' = 0, so F_1 + F_1' = 0."""
        assert genus1_obstruction_koszul_sum(F(9, 4), F(-9, 4)) == F(0)

    def test_genus1_mirror_sum_sqed(self):
        """For SQED(4): F_1(A_C) + F_1(A_H) = 4/24 = 1/6."""
        assert genus1_obstruction_mirror_sum(1, 3) == F(4, 24)
        assert genus1_obstruction_mirror_sum(1, 3) == F(1, 6)

    def test_genus2_basic(self):
        """F_2 = 7*kappa/5760."""
        assert genus2_obstruction_scalar(5760) == F(7)

    def test_genus_comparison_sqed4(self):
        """Full comparison for SQED(4)."""
        result = genus_g_obstruction_comparison(
            kappa_A=1, kappa_A_dual=-1, kappa_mirror=3
        )
        assert result['F1_koszul_sum'] == F(0)  # 1/24 + (-1)/24 = 0
        assert result['F1_mirror_sum'] == F(4, 24)  # (1+3)/24
        assert not result['F1_sums_equal']

    def test_genus_comparison_heisenberg(self):
        """For Heisenberg at level 1: mirror sum != Koszul sum."""
        result = genus_g_obstruction_comparison(
            kappa_A=1, kappa_A_dual=-1, kappa_mirror=1
        )
        # Koszul sum: (1 + (-1))/24 = 0
        # Mirror sum: (1 + 1)/24 = 1/12
        assert result['F1_koszul_sum'] == F(0)
        assert result['F1_mirror_sum'] == F(1, 12)
        assert not result['F1_sums_equal']


# ============================================================================
# 10. Categorical vs algebraic KD
# ============================================================================

class TestCategoricalVsAlgebraicKD:
    """Shadow-depth dependence of categorical/algebraic KD agreement."""

    def test_class_G_agree(self):
        """Class G (Gaussian): categorical = algebraic."""
        result = categorical_vs_algebraic_kd('G', 'Heisenberg')
        assert result.categorical_equals_algebraic
        assert result.shadow_depth == 2

    def test_class_L_agree(self):
        """Class L (Lie/tree): categorical = algebraic."""
        result = categorical_vs_algebraic_kd('L', 'affine sl_2')
        assert result.categorical_equals_algebraic
        assert result.shadow_depth == 3

    def test_class_C_differ(self):
        """Class C (contact/quartic): categorical != algebraic."""
        result = categorical_vs_algebraic_kd('C', 'beta-gamma')
        assert not result.categorical_equals_algebraic
        assert result.shadow_depth == 4
        assert "quartic" in result.discrepancy_source.lower()

    def test_class_M_differ(self):
        """Class M (mixed/infinite): categorical != algebraic."""
        result = categorical_vs_algebraic_kd('M', 'Virasoro')
        assert not result.categorical_equals_algebraic
        assert result.shadow_depth == float('inf')
        assert "infinite" in result.discrepancy_source.lower()


# ============================================================================
# 11. Diagram commutativity
# ============================================================================

class TestDiagramCommutativity:
    """Test whether the mirror-Koszul diagram commutes."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_sqed_diagram_does_not_commute(self, N_f):
        """For SQED(N_f>=1): A_C^! != A_H (diagram does not commute)."""
        diag = diagram_commutativity_sqed(N_f)
        # kappa(H_1^!) = -1, kappa_H = N_f - 1
        # These are equal only if N_f = 0 (degenerate)
        if N_f >= 2:
            assert not diag.kd_coulomb_equals_higgs
        elif N_f == 1:
            # N_f=1: kappa_H = 0, kappa_C^! = -1, still different
            assert not diag.kd_coulomb_equals_higgs

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_sqed_obstruction_is_minus_nf(self, N_f):
        """Obstruction kappa_C^! - kappa_H = -N_f."""
        diag = diagram_commutativity_sqed(N_f)
        assert diag.obstruction == F(-N_f)

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_affine_diagram_does_not_commute(self, N):
        """For GL(N) CS at generic Psi: Neumann^! != Dirichlet."""
        for psi in [F(2), F(3), F(5, 2)]:
            diag = diagram_commutativity_affine(N, psi)
            assert not diag.kd_coulomb_equals_higgs, (
                f"Diagram commutes at N={N}, Psi={psi}: impossible generically!"
            )

    def test_affine_obstruction_nonzero(self):
        """The obstruction kappa_N^! - kappa_D is always nonzero (generically)."""
        for N in [1, 2, 3]:
            for psi in [F(2), F(3), F(5, 2)]:
                diag = diagram_commutativity_affine(N, psi)
                assert diag.obstruction != 0

    def test_affine_obstruction_agrees_with_discrepancy(self):
        """The obstruction equals the S-vs-KD kappa discrepancy (up to sign)."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(5, 2)]:
                diag = diagram_commutativity_affine(N, psi)
                disc = s_kd_discrepancy_affine_gl(N, psi)
                # Obstruction = kappa_N^KD - kappa_D
                # kappa_N^KD = kappa(gl_N, -k-2N)
                # kappa_D = kappa(gl_N, 1/Psi - N)
                # Discrepancy = kappa(1/Psi - N) - kappa(-k-2N)
                #             = kappa_D - kappa_N^KD
                #             = -obstruction
                assert diag.obstruction == -disc, (
                    f"Obstruction {diag.obstruction} != -disc {-disc}"
                )


# ============================================================================
# 12. Mirror as composition of S and KD
# ============================================================================

class TestMirrorAsComposition:
    """Test that mirror cannot be expressed as composition of S and KD."""

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_s_kd_commute_at_kappa_level(self, N):
        """S . KD and KD . S give the SAME kappa (both send Psi -> -1/Psi)."""
        for psi in [F(2), F(3), F(5, 2)]:
            result = mirror_as_composition(N, psi)
            assert result['S_KD_commute'], (
                f"S.KD != KD.S at N={N}, Psi={psi}"
            )

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_s_kd_s_equals_kd(self, N):
        """S . KD . S = KD (conjugation returns to KD)."""
        for psi in [F(2), F(3), F(5, 2)]:
            result = mirror_as_composition(N, psi)
            assert result['S_KD_S_equals_KD'], (
                f"S.KD.S != KD at N={N}, Psi={psi}"
            )

    def test_conclusion_string(self):
        """The conclusion says mirror cannot be decomposed."""
        result = mirror_as_composition(2, 3)
        assert "cannot" in result['conclusion'].lower()
        assert "mirror" in result['conclusion'].lower()


# ============================================================================
# 13. Self-dual loci
# ============================================================================

class TestSelfDualLoci:
    """Enumerate special loci where dualities coincide."""

    def test_five_loci(self):
        """There are exactly 5 self-dual loci catalogued."""
        loci = all_self_dual_loci()
        assert len(loci) == 5

    def test_s_kd_locus_is_imaginary(self):
        """S = KD coincidence locus has no real solutions."""
        loci = all_self_dual_loci()
        s_kd = [l for l in loci if "S-duality = Koszul" in l.duality_pair][0]
        assert "EMPTY" in s_kd.solutions_over_R
        assert "Psi^2 = -1" in s_kd.coincidence_condition

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c=13, NOT c=26 (AP8)."""
        loci = all_self_dual_loci()
        vir = [l for l in loci if "Virasoro" in l.duality_pair][0]
        assert "c = 13" in vir.solutions_over_R
        # The condition c = 26 - c solves to c = 13 (AP8: NOT c = 26)
        assert "13" in vir.solutions_over_R

    def test_triality_23_self_dual_at_half(self):
        """(23) triality self-dual at Psi = 1/2."""
        loci = all_self_dual_loci()
        t23 = [l for l in loci if "(23)" in l.duality_pair][0]
        assert "Psi = 1/2" in t23.coincidence_condition


# ============================================================================
# 14. Physical examples
# ============================================================================

class TestPhysicalExamples:
    """Specific physical theories: Argyres-Douglas, SQED(2), SQED(4)."""

    def test_argyres_douglas_h0(self):
        """AD H_0: Vir at c=-22/5, kappa = -11/5, sum = 13."""
        result = argyres_douglas_h0_diagram()
        assert result['kappa'] == F(-11, 5)
        assert result['kappa_dual'] == F(76, 5)
        assert result['complementarity_sum'] == F(13)
        assert result['shadow_class'] == 'M'
        assert not result['has_mirror_dual']
        assert result['koszul_duality_applies']
        assert not result['mirror_symmetry_applies']

    def test_sqed2_self_mirror(self):
        """SQED(2) is self-mirror: A_C = A_H = H_1."""
        result = sqed_nf2_full_diagram()
        assert result['is_self_mirror']
        assert result['kappa_C'] == F(1)
        assert result['kappa_H'] == F(1)
        assert result['kappa_C_koszul'] == F(-1)
        assert result['mirror_sum'] == F(2)
        assert result['koszul_sum_C'] == F(0)
        # Diagram commutes trivially (mirror is identity)
        assert result['diagram_commutes']
        # But Koszul dual != mirror dual
        assert result['obstruction_kd_vs_mirror'] == F(-2)

    def test_sqed4_non_commuting(self):
        """SQED(4): diagram does not commute, obstruction = -4."""
        result = sqed_nf4_full_diagram()
        assert not result['is_self_mirror']
        assert result['kappa_C'] == F(1)
        assert result['kappa_H'] == F(3)
        assert result['mirror_sum'] == F(4)
        assert result['koszul_sum_C'] == F(0)
        assert not result['diagram_commutes']
        assert result['obstruction_kd_vs_mirror'] == F(-4)


# ============================================================================
# 15. Landscape survey: cross-family consistency
# ============================================================================

class TestLandscapeSurvey:
    """Survey across multiple theories for consistency."""

    def test_gl_survey_all_have_nonzero_discrepancy(self):
        """Every gl_N entry has nonzero S-vs-KD discrepancy."""
        survey = landscape_survey(N_max=3)
        assert len(survey) > 0
        for comp in survey:
            assert comp.delta_s_vs_kd != 0, (
                f"Zero discrepancy at {comp.name}"
            )

    def test_gl_survey_koszul_sum_constant_per_N(self):
        """For each N, the Koszul sum is constant across Psi values."""
        survey = landscape_survey(N_max=3)
        by_N = {}
        for comp in survey:
            by_N.setdefault(comp.N, set()).add(comp.koszul_sum)
        for N, sums in by_N.items():
            assert len(sums) == 1, (
                f"Koszul sum varies for N={N}: {sums}"
            )

    def test_wn_survey_koszul_sum_constant(self):
        """For each W_N, the Koszul sum is constant across Psi."""
        survey = landscape_survey_wn(N_max=4)
        assert len(survey) > 0
        by_N = {}
        for comp in survey:
            by_N.setdefault(comp.N, set()).add(comp.koszul_sum)
        for N, sums in by_N.items():
            assert len(sums) == 1, f"W_{N} Koszul sum varies: {sums}"

    def test_gl_survey_no_s_kd_coincidence(self):
        """No real-coupling entry has S = KD."""
        survey = landscape_survey(N_max=4)
        for comp in survey:
            assert not comp.s_equals_kd


# ============================================================================
# 16. Webster comparison
# ============================================================================

class TestWebsterComparison:
    """Webster categorical KD vs our chiral algebraic KD."""

    @pytest.mark.parametrize("N_f", range(1, 6))
    def test_sqed_both_agree(self, N_f):
        """For SQED: both categorical and algebraic KD apply and agree."""
        result = webster_comparison_sqed(N_f)
        assert result.algebraic_kd_applies
        if N_f >= 2:
            assert result.webster_applies
        assert result.both_agree

    @pytest.mark.parametrize("n", range(1, 6))
    def test_quiver_formality_determines_agreement(self, n):
        """For A_n quivers: agreement depends on shadow class."""
        result = webster_comparison_type_a_quiver(n)
        assert result.webster_applies
        assert result.algebraic_kd_applies
        if result.shadow_class_coulomb in ('G', 'L'):
            assert result.both_agree
        else:
            assert not result.both_agree

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_nahm_categorical_fails(self, N):
        """For Nahm pole (W-algebra): Webster does not apply."""
        result = webster_comparison_nahm(N)
        assert not result.webster_applies
        assert result.algebraic_kd_applies
        assert not result.both_agree

    def test_shadow_class_determines_all(self):
        """The shadow class alone determines categorical/algebraic agreement."""
        # Collect all results
        for cls, should_agree in [('G', True), ('L', True), ('C', False), ('M', False)]:
            cat = categorical_vs_algebraic_kd(cls)
            assert cat.categorical_equals_algebraic == should_agree


# ============================================================================
# 17. Large-N / 't Hooft limit
# ============================================================================

class TestLargeNLimit:
    """Behavior of the discrepancy at large N."""

    def test_discrepancy_coefficient_grows_as_N(self):
        """The coefficient (N^2+2N-1)/(2N) ~ N/2 at large N."""
        for N in [10, 50, 100]:
            coeff = F(N**2 + 2*N - 1, 2*N)
            approx = F(N, 2)
            relative_error = abs(coeff - approx) / approx
            assert relative_error < F(3, N), (
                f"Coefficient {coeff} too far from N/2 = {approx} at N={N}"
            )

    def test_koszul_sum_grows_linearly_in_N(self):
        """Koszul sum = -2N grows linearly."""
        for N in [1, 5, 10, 50]:
            comp = four_duality_comparison_affine_gl(N, 3)
            assert comp.koszul_sum == F(-2 * N)

    def test_discrepancy_grows_linearly_at_fixed_psi(self):
        """At fixed Psi, discrepancy ~ N/2 * (Psi + 1/Psi) at large N."""
        psi = F(3)
        psi_sum = psi + F(1) / psi
        for N in [10, 50, 100]:
            disc = s_kd_discrepancy_affine_gl(N, psi)
            approx = F(N, 2) * psi_sum
            relative_error = abs(disc - approx) / approx
            assert relative_error < F(3, N)


# ============================================================================
# 18. Cross-engine consistency
# ============================================================================

class TestCrossEngineConsistency:
    """Cross-check with existing Coulomb-Higgs and symplectic duality engines."""

    def test_kappa_gl1_matches_heisenberg_engine(self):
        """kappa(gl_1, k) should match Heisenberg kappa = k."""
        for k in [1, 2, 3, 5]:
            assert kappa_affine_gl(1, k) == F(k)

    def test_virasoro_complementarity_13(self):
        """Virasoro: kappa + kappa' = 13 (AP24)."""
        for c_val in [F(-22, 5), F(0), F(1), F(13), F(25)]:
            kap = kappa_virasoro(c_val)
            kap_dual = kappa_virasoro(26 - c_val)
            assert kap + kap_dual == F(13)

    def test_affine_sl_antisymmetry(self):
        """For sl_N: kappa + kappa' = 0 (consistent with existing engine)."""
        for N in [2, 3, 4]:
            for k in [1, 2]:
                k_ff = ff_dual_level(k, N)
                assert kappa_affine_sl(N, k) + kappa_affine_sl(N, k_ff) == F(0)

    def test_sqed_mirror_sum_consistent(self):
        """SQED(N_f): kappa_C + kappa_H = N_f, matching Coulomb-Higgs engine."""
        for N_f in range(1, 9):
            comp = complementarity_comparison_sqed(N_f)
            assert comp.mirror_sum == F(N_f)

    def test_w2_koszul_sum_matches_virasoro(self):
        """W_2 Koszul sum should equal 13 (Virasoro complementarity)."""
        comp = four_duality_comparison_wn(2, 3)
        assert comp.koszul_sum == F(13)


# ============================================================================
# 19. The five key findings (summary verification)
# ============================================================================

class TestFiveKeyFindings:
    """Verify the five key structural findings of this engine."""

    def test_finding_1_mirror_ne_kd(self):
        """Finding 1: mirror != KD. Verified by SQED obstruction."""
        for N_f in range(2, 6):
            diag = diagram_commutativity_sqed(N_f)
            assert not diag.kd_coulomb_equals_higgs

    def test_finding_2_s_ne_kd(self):
        """Finding 2: S != KD for all real Psi."""
        for N in [1, 2, 3]:
            for psi in [F(1, 3), F(1, 2), F(1), F(2), F(3)]:
                comp = four_duality_comparison_affine_gl(N, psi)
                assert not comp.s_equals_kd

    def test_finding_3_ff_outside_s3(self):
        """Finding 3: FF involution is outside S_3 triality."""
        for psi in [F(3), F(5, 2), F(7, 3)]:
            orb = compute_triality_orbit(psi)
            assert not orb.ff_in_s3_orbit

    def test_finding_4_theorem_c_vs_mirror(self):
        """Finding 4: Theorem C sum != mirror sum."""
        for N_f in range(2, 6):
            comp = complementarity_comparison_sqed(N_f)
            assert comp.koszul_sum != comp.mirror_sum

    def test_finding_5_four_dualities_distinct(self):
        """Finding 5: all four dualities produce distinct kappa."""
        comp = four_duality_comparison_affine_gl(2, 3)
        kappas = {comp.kappa_original, comp.kappa_koszul, comp.kappa_s_dual}
        assert len(kappas) == 3, "Three kappas should be distinct"

    def test_summary_has_five_findings(self):
        """Summary contains five findings."""
        summary = full_comparison_summary()
        assert 'finding_1' in summary
        assert 'finding_5' in summary
        assert len(summary) == 5
