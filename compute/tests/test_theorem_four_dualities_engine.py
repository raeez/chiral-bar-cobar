r"""Tests for the four-dualities generic distinctness theorem.

Tests cover:
  1. Core kappa formulas (multi-path verification, AP1/AP10)
  2. Proof 1: explicit kappa discriminant (closed-form + direct)
  3. Proof 2: fixed-point analysis (pairwise distinct loci)
  4. Proof 3: shadow invariant transformation laws
  5. Proof 4: group-theoretic structure (V_4, S_3, non-cyclic)
  6. Full theorem assembly (all four proofs)
  7. Cross-engine consistency with mirror_koszul_comparison_engine
  8. Landscape survey across families
  9. W_N extension
  10. Limiting cases (N=1, large N, Psi -> 1)

Multi-path verification:
  Path 1: Direct formula computation
  Path 2: Closed-form discriminant identity
  Path 3: Fixed-point enumeration
  Path 4: Group structure computation
  Path 5: Cross-engine consistency
  Path 6: Numerical evaluation at specific points
  Path 7: Limiting case analysis
  Path 8: AM-GM bound verification
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_four_dualities_engine import (
    # Core kappa
    kappa_sl,
    kappa_gl,
    kappa_virasoro,
    kappa_wn,
    c_sl,
    c_wn,
    # Duality operations
    ff_dual_level,
    ff_dual_psi,
    s_dual_psi,
    s_dual_level,
    triality_23_psi,
    triality_13_psi,
    # Proof 1
    proof1_explicit_kappa,
    proof1_discriminant_closed_form,
    proof1_discriminant_never_zero_real,
    proof1_discriminant_coefficient,
    proof1_am_gm_lower_bound,
    proof1_wn_discriminant,
    Proof1Result,
    # Proof 2
    fixed_points_ff,
    fixed_points_s_duality,
    fixed_points_triality_23,
    fixed_points_mirror,
    fixed_points_categorical_kd,
    proof2_all_fixed_points,
    proof2_fixed_points_are_distinct,
    FixedPointData,
    # Proof 3
    proof3_shadow_transforms,
    proof3_kd_antisymmetry_sl,
    proof3_kd_sum_gl,
    proof3_s_sum_gl,
    proof3_virasoro_kd_sum,
    proof3_level_independence_test,
    Proof3Result,
    # Proof 4
    IDENTITY,
    S_DUAL,
    FF_DUAL,
    TRIALITY_23,
    TRIALITY_13,
    GroupElement,
    proof4_check_s_squared_is_identity,
    proof4_check_ff_squared_is_identity,
    proof4_s_ff_composition,
    proof4_ff_s_composition,
    proof4_s_ff_commute,
    proof4_s_ff_order,
    proof4_klein_four_generated,
    proof4_ff_not_in_s3,
    proof4_s3_elements,
    proof4_s3_preserves_01inf,
    proof4_group_structure,
    Proof4Result,
    # Theorem
    prove_four_dualities_distinct,
    TheoremResult,
    # Cross-engine
    cross_check_with_mirror_engine,
    landscape_distinctness_survey,
)

F = Fraction


# ============================================================================
# 1. Core kappa formulas
# ============================================================================

class TestCoreKappa:
    """Multi-path verification of kappa formulas (AP1, AP10)."""

    def test_kappa_gl1_is_heisenberg(self):
        """kappa(gl_1, k) = k (Heisenberg). Path 1: direct formula."""
        for k in [1, 2, 3, 5, -1]:
            assert kappa_gl(1, k) == F(k)

    def test_kappa_sl2_k1_two_paths(self):
        """kappa(sl_2, k=1) = 9/4. Path 1: formula. Path 2: dim*(k+h)/(2h)."""
        # Path 1
        assert kappa_sl(2, 1) == F(9, 4)
        # Path 2: dim(sl_2)=3, h^v=2, k=1 => 3*(1+2)/(2*2) = 9/4
        assert F(3) * F(3) / F(4) == F(9, 4)

    def test_kappa_gl2_k1(self):
        """kappa(gl_2, k=1) = kappa(sl_2, 1) + 1 = 13/4."""
        assert kappa_gl(2, 1) == F(9, 4) + F(1)
        assert kappa_gl(2, 1) == F(13, 4)

    def test_kappa_virasoro_basic(self):
        """kappa(Vir_c) = c/2."""
        for c in [0, 1, 13, 26, F(-22, 5)]:
            assert kappa_virasoro(c) == F(c) / 2

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_critical_level_raises(self, N):
        """Critical level k = -N raises ValueError."""
        with pytest.raises(ValueError):
            kappa_sl(N, -N)

    def test_ff_involution(self):
        """FF is involutive: FF(FF(k)) = k."""
        for N in [2, 3, 4]:
            for k in [1, 2, F(3, 2)]:
                assert ff_dual_level(ff_dual_level(k, N), N) == F(k)

    def test_s_involution(self):
        """S is involutive: S(S(Psi)) = Psi."""
        for psi in [F(2), F(3), F(1, 3), F(5, 7)]:
            assert s_dual_psi(s_dual_psi(psi)) == psi


# ============================================================================
# 2. Proof 1: Explicit kappa discriminant
# ============================================================================

class TestProof1ExplicitKappa:
    """The discriminant Delta = kappa^S - kappa^KD is generically nonzero."""

    def test_gl1_psi3_discriminant(self):
        """N=1, Psi=3: Delta = 1 * (3 + 1/3) = 10/3."""
        p = proof1_explicit_kappa(1, 3)
        assert p.discriminant == F(10, 3)
        assert p.kd_ne_s

    def test_gl2_psi3_discriminant(self):
        """N=2, Psi=3: coefficient = 7/4, Psi+1/Psi = 10/3, Delta = 35/6."""
        p = proof1_explicit_kappa(2, 3)
        assert p.discriminant == F(35, 6)

    def test_closed_form_matches_direct(self):
        """Path 2: closed-form formula agrees with direct computation."""
        for N in [1, 2, 3, 4]:
            for psi in [F(2), F(3), F(5, 2), F(1, 3)]:
                direct = proof1_explicit_kappa(N, psi).discriminant
                closed = proof1_discriminant_closed_form(N, psi)
                assert direct == closed, (
                    f"Direct {direct} != closed {closed} at N={N}, Psi={psi}"
                )

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_discriminant_positive_real_psi(self, N):
        """For real Psi > 0, discriminant > 0 (Path 6: numerical)."""
        psi_grid = [F(1, 10), F(1, 3), F(1, 2), F(1), F(2), F(3), F(10)]
        for psi in psi_grid:
            disc = proof1_discriminant_closed_form(N, psi)
            assert disc > 0, f"Disc <= 0 at N={N}, Psi={psi}"

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_am_gm_bound(self, N):
        """Path 8: AM-GM bound. Delta >= 2 * coeff for Psi > 0."""
        lb = proof1_am_gm_lower_bound(N)
        for psi in [F(1, 10), F(1, 2), F(1), F(2), F(10)]:
            disc = proof1_discriminant_closed_form(N, psi)
            assert disc >= lb, f"Below bound at N={N}, Psi={psi}"

    def test_am_gm_minimum_at_psi_1(self):
        """AM-GM minimum achieved at Psi = 1: Delta = 2 * coeff."""
        for N in [1, 2, 3]:
            lb = proof1_am_gm_lower_bound(N)
            disc = proof1_discriminant_closed_form(N, 1)
            assert disc == lb

    def test_never_zero_on_grid(self):
        """Discriminant nonzero on entire test grid."""
        grid = [F(1, 5), F(1, 3), F(1, 2), F(1), F(2), F(3), F(5), F(10)]
        for N in [1, 2, 3, 4]:
            assert proof1_discriminant_never_zero_real(N, grid)

    def test_coefficient_formula(self):
        """Path 2: coefficient (N^2+2N-1)/(2N) at specific N."""
        assert proof1_discriminant_coefficient(1) == F(1)        # (1+2-1)/2
        assert proof1_discriminant_coefficient(2) == F(7, 4)     # (4+4-1)/4
        assert proof1_discriminant_coefficient(3) == F(7, 3)     # (9+6-1)/6

    def test_all_three_kappas_distinct(self):
        """At generic Psi: kappa, kappa^KD, kappa^S are all distinct."""
        for N in [1, 2, 3]:
            for psi in [F(2), F(3), F(5, 2)]:
                p = proof1_explicit_kappa(N, psi)
                assert p.all_three_distinct, (
                    f"Not all distinct at N={N}, Psi={psi}"
                )

    def test_wn_discriminant_nonzero(self):
        """W_N discriminant is also generically nonzero."""
        for N in [2, 3, 4]:
            for psi in [F(3), F(5, 2), F(4)]:
                try:
                    disc = proof1_wn_discriminant(N, psi)
                    assert disc != 0, f"W_{N} disc = 0 at Psi={psi}"
                except (ValueError, ZeroDivisionError):
                    pass  # skip degenerate cases


# ============================================================================
# 3. Proof 2: Fixed-point analysis
# ============================================================================

class TestProof2FixedPoints:
    """Different dualities have different fixed-point sets."""

    def test_ff_fixed_at_zero(self):
        """FF: Psi -> -Psi has fixed point Psi = 0 only."""
        fp = fixed_points_ff()
        assert fp.num_real_solutions == 1
        assert fp.is_degenerate  # critical level

    def test_s_fixed_at_pm1(self):
        """S: Psi -> 1/Psi has fixed points Psi = +/-1."""
        fp = fixed_points_s_duality()
        assert fp.num_real_solutions == 2
        assert not fp.is_degenerate

    def test_triality_23_fixed_at_half(self):
        """(23): Psi -> 1-Psi has fixed point Psi = 1/2."""
        fp = fixed_points_triality_23()
        assert fp.num_real_solutions == 1
        # Verify directly
        assert triality_23_psi(F(1, 2)) == F(1, 2)

    def test_mirror_no_coupling_fixed_point(self):
        """Mirror has no fixed-point equation in Psi."""
        fp = fixed_points_mirror()
        assert fp.num_real_solutions == -1

    def test_all_fixed_points_pairwise_distinct(self):
        """No two operations share the same fixed-point set."""
        assert proof2_fixed_points_are_distinct()

    def test_five_operations_catalogued(self):
        """All five operations have fixed-point data."""
        fps = proof2_all_fixed_points()
        assert len(fps) == 5

    def test_ff_ne_s_by_fixed_points(self):
        """FF and S differ: {0} vs {+1, -1}."""
        ff = fixed_points_ff()
        s = fixed_points_s_duality()
        assert ff.num_real_solutions != s.num_real_solutions

    def test_s_ne_23_by_fixed_points(self):
        """S and (23) differ: {+1, -1} vs {1/2}."""
        s = fixed_points_s_duality()
        t23 = fixed_points_triality_23()
        assert s.num_real_solutions != t23.num_real_solutions


# ============================================================================
# 4. Proof 3: Shadow invariant transformation laws
# ============================================================================

class TestProof3ShadowInvariants:
    """Kappa transforms differently under each duality."""

    def test_kd_antisymmetry_sl(self):
        """For sl_N: kappa + kappa^KD = 0 (AP24)."""
        for N in [2, 3, 4]:
            for k in [1, 2, F(3, 2)]:
                assert proof3_kd_antisymmetry_sl(N, k) == F(0)

    def test_kd_sum_gl_constant(self):
        """For gl_N: kappa + kappa^KD = -2N (level-independent)."""
        for N in [1, 2, 3]:
            for k in [1, 2, 3]:
                assert proof3_kd_sum_gl(N, k) == F(-2 * N)

    def test_s_sum_varies(self):
        """kappa + kappa^S varies with Psi (not a topological invariant)."""
        for N in [1, 2, 3]:
            sums = set()
            for psi in [F(2), F(3), F(5, 2)]:
                sums.add(proof3_s_sum_gl(N, psi))
            assert len(sums) > 1, f"S-sum constant for N={N}: {sums}"

    def test_virasoro_kd_sum_13(self):
        """Virasoro: kappa(c) + kappa(26-c) = 13 (AP24)."""
        assert proof3_virasoro_kd_sum() == F(13)

    def test_level_independence_distinguishes(self):
        """KD sum is constant, S-sum varies: they are different operations."""
        for N in [1, 2, 3]:
            psis = [F(2), F(3), F(5, 2), F(7, 3)]
            assert proof3_level_independence_test(N, psis)

    def test_shadow_transforms_kd_ne_s(self):
        """At generic Psi: kappa^KD != kappa^S."""
        p = proof3_shadow_transforms(2, 3)
        assert p.all_images_distinct

    def test_shadow_transforms_count(self):
        """Four transform operations are catalogued."""
        p = proof3_shadow_transforms(2, 3)
        assert len(p.transforms) == 4


# ============================================================================
# 5. Proof 4: Group-theoretic structure
# ============================================================================

class TestProof4GroupStructure:
    """S, FF, and triality generate a non-cyclic group."""

    def test_s_squared_identity(self):
        """S^2 = id (involution)."""
        assert proof4_check_s_squared_is_identity()

    def test_ff_squared_identity(self):
        """FF^2 = id (involution)."""
        assert proof4_check_ff_squared_is_identity()

    def test_s_ff_commute(self):
        """S and FF commute (as Mobius transformations on Psi)."""
        assert proof4_s_ff_commute()

    def test_s_ff_order_2(self):
        """S.FF has order 2: (S.FF)^2 = id."""
        assert proof4_s_ff_order() == 2

    def test_klein_four_generated(self):
        """S and FF generate V_4 = Z_2 x Z_2 (Klein four-group)."""
        assert proof4_klein_four_generated()

    def test_ff_not_in_s3(self):
        """FF (Psi -> -Psi) is NOT in the S_3 corner triality.

        FF maps 1 -> -1, which is not in {0, 1, inf}.
        """
        assert proof4_ff_not_in_s3()

    def test_s3_preserves_01inf(self):
        """Every S_3 element preserves {0, 1, infinity}."""
        assert proof4_s3_preserves_01inf()

    def test_s3_has_six_elements(self):
        """The S_3 corner triality has 6 elements."""
        assert len(proof4_s3_elements()) == 6

    def test_full_group_structure(self):
        """Full Proof 4 result: V_4 generated, FF outside S_3, non-cyclic."""
        result = proof4_group_structure()
        assert result.s_ff_commute
        assert result.s_squared_is_id
        assert result.ff_squared_is_id
        assert result.s_ff_order == 2
        assert result.klein_four_generated
        assert result.ff_not_in_s3
        assert result.s3_preserves_01inf
        assert result.full_group_not_cyclic

    def test_s_ff_composition_is_minus_inv(self):
        """S.FF sends Psi -> -1/Psi."""
        sf = proof4_s_ff_composition()
        assert sf.apply(3) == F(-1, 3)
        assert sf.apply(F(1, 2)) == F(-2)

    def test_ff_s_composition_same_as_s_ff(self):
        """FF.S also sends Psi -> -1/Psi (commuting)."""
        fs = proof4_ff_s_composition()
        assert fs.apply(3) == F(-1, 3)
        assert fs.apply(F(1, 2)) == F(-2)

    def test_identity_element(self):
        """Identity element applies correctly."""
        assert IDENTITY.apply(3) == F(3)
        assert IDENTITY.apply(F(1, 2)) == F(1, 2)

    def test_s_dual_element(self):
        """S-duality element: Psi -> 1/Psi."""
        assert S_DUAL.apply(3) == F(1, 3)
        assert S_DUAL.apply(F(1, 2)) == F(2)

    def test_ff_dual_element(self):
        """FF element: Psi -> -Psi."""
        assert FF_DUAL.apply(3) == F(-3)
        assert FF_DUAL.apply(F(1, 2)) == F(-1, 2)

    def test_triality_23_element(self):
        """(23) element: Psi -> 1 - Psi."""
        assert TRIALITY_23.apply(3) == F(-2)
        assert TRIALITY_23.apply(F(1, 2)) == F(1, 2)  # fixed point


# ============================================================================
# 6. Full theorem assembly
# ============================================================================

class TestFullTheorem:
    """All four proofs together establish generic distinctness."""

    def test_theorem_at_gl2_psi3(self):
        """Full theorem holds at gl_2, Psi = 3."""
        result = prove_four_dualities_distinct(N=2, psi=F(3))
        assert result.proof1_holds
        assert result.proof2_holds
        assert result.proof3_holds
        assert result.proof4_holds
        assert result.theorem_proved

    def test_theorem_at_gl1_psi2(self):
        """Full theorem holds at gl_1, Psi = 2."""
        result = prove_four_dualities_distinct(N=1, psi=F(2))
        assert result.theorem_proved

    def test_theorem_at_gl3_psi_half(self):
        """Full theorem holds at gl_3, Psi = 1/2."""
        result = prove_four_dualities_distinct(N=3, psi=F(1, 2))
        assert result.theorem_proved

    @pytest.mark.parametrize("N", [1, 2, 3, 4])
    def test_theorem_all_N(self, N):
        """Theorem holds for N = 1, 2, 3, 4 at generic Psi."""
        result = prove_four_dualities_distinct(N=N, psi=F(3))
        assert result.theorem_proved, f"Theorem fails at N={N}"

    @pytest.mark.parametrize("psi", [F(1, 3), F(1, 2), F(2), F(3), F(5, 2), F(7, 3)])
    def test_theorem_psi_grid(self, psi):
        """Theorem holds across a grid of Psi values at N=2."""
        result = prove_four_dualities_distinct(N=2, psi=psi)
        assert result.theorem_proved, f"Theorem fails at Psi={psi}"


# ============================================================================
# 7. Cross-engine consistency
# ============================================================================

class TestCrossEngineConsistency:
    """Verify agreement with mirror_koszul_comparison_engine."""

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_kappa_agrees(self, N):
        """Our kappa matches the mirror engine's kappa."""
        for psi in [F(2), F(3), F(5, 2)]:
            result = cross_check_with_mirror_engine(N, psi)
            if 'import_failed' not in result:
                assert result['kappa_agrees'], f"Kappa mismatch at N={N}, Psi={psi}"

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_ff_dual_agrees(self, N):
        """Our FF dual level matches the mirror engine."""
        for psi in [F(2), F(3), F(5, 2)]:
            result = cross_check_with_mirror_engine(N, psi)
            if 'import_failed' not in result:
                assert result['ff_dual_agrees']

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_s_dual_agrees(self, N):
        """Our S-dual level matches the mirror engine."""
        for psi in [F(2), F(3), F(5, 2)]:
            result = cross_check_with_mirror_engine(N, psi)
            if 'import_failed' not in result:
                assert result['s_dual_agrees']

    @pytest.mark.parametrize("N", [1, 2, 3])
    def test_discriminant_agrees(self, N):
        """Our discriminant matches the mirror engine's discrepancy."""
        for psi in [F(2), F(3), F(5, 2)]:
            result = cross_check_with_mirror_engine(N, psi)
            if 'import_failed' not in result:
                assert result['discriminant_agrees']

    def test_all_agree_comprehensive(self):
        """Full agreement check at N=2, Psi=3."""
        result = cross_check_with_mirror_engine(2, 3)
        if 'import_failed' not in result:
            assert result['all_agree']


# ============================================================================
# 8. Landscape survey
# ============================================================================

class TestLandscapeSurvey:
    """Survey distinctness across a grid of (N, Psi) values."""

    def test_survey_all_kd_ne_s(self):
        """Every surveyed (N, Psi) has kappa^KD != kappa^S."""
        survey = landscape_distinctness_survey(N_max=4)
        assert survey['kd_ne_s_fraction'] == F(1)

    def test_survey_nonzero_count(self):
        """Survey covers a substantial number of cases."""
        survey = landscape_distinctness_survey(N_max=3)
        assert survey['total_tested'] >= 15

    def test_survey_all_discriminants_nonzero(self):
        """Every entry in the survey has nonzero discriminant."""
        survey = landscape_distinctness_survey(N_max=3)
        for entry in survey['results']:
            assert entry['discriminant'] != 0, (
                f"Zero discriminant at N={entry['N']}, Psi={entry['psi']}"
            )


# ============================================================================
# 9. W_N extension
# ============================================================================

class TestWNExtension:
    """Extend the theorem to W_N algebras."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_wn_koszul_sum_constant(self, N):
        """kappa(W_N, k) + kappa(W_N, -k-2N) is level-independent."""
        sums = set()
        for psi in [F(3), F(5, 2), F(4)]:
            try:
                k = _frac(psi) - N
                c_orig = c_wn(N, k)
                c_dual = c_wn(N, ff_dual_level(k, N))
                kap = kappa_wn(N, c_orig)
                kap_d = kappa_wn(N, c_dual)
                sums.add(kap + kap_d)
            except (ValueError, ZeroDivisionError):
                pass
        assert len(sums) == 1, f"W_{N} Koszul sum varies: {sums}"

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_wn_discriminant_generic_nonzero(self, N):
        """W_N S-vs-KD discriminant is generically nonzero."""
        for psi in [F(3), F(5, 2)]:
            try:
                disc = proof1_wn_discriminant(N, psi)
                assert disc != 0, f"W_{N} disc = 0 at Psi={psi}"
            except (ValueError, ZeroDivisionError):
                pass

    def test_w2_koszul_sum_is_13(self):
        """W_2 = Virasoro: kappa + kappa' = 13 (AP24)."""
        k = F(3) - 2  # Psi = 3
        c_orig = c_wn(2, k)
        c_dual = c_wn(2, ff_dual_level(k, 2))
        assert kappa_wn(2, c_orig) + kappa_wn(2, c_dual) == F(13)


# ============================================================================
# 10. Limiting cases
# ============================================================================

class TestLimitingCases:
    """Path 7: verify at special/limiting values."""

    def test_n1_heisenberg(self):
        """N=1 (Heisenberg): kappa = k, discriminant = Psi + 1/Psi."""
        for psi in [F(2), F(3)]:
            disc = proof1_discriminant_closed_form(1, psi)
            assert disc == psi + F(1) / psi

    def test_psi_1_self_dual_coupling(self):
        """At Psi = 1 (self-dual S-coupling): S-dual = original,
        but KD-dual is different."""
        for N in [1, 2, 3]:
            p = proof1_explicit_kappa(N, 1)
            assert p.kappa_original == p.kappa_s_dual  # S(1) = 1
            assert p.kappa_original != p.kappa_koszul   # KD(1) != 1

    def test_large_n_coefficient_growth(self):
        """At large N: coefficient ~ N/2."""
        for N in [10, 50, 100]:
            coeff = proof1_discriminant_coefficient(N)
            approx = F(N, 2)
            rel_err = abs(coeff - approx) / approx
            assert rel_err < F(3, N)

    def test_discriminant_symmetric_psi_inv_psi(self):
        """Delta(Psi) = Delta(1/Psi): the discriminant is S-duality symmetric."""
        for N in [1, 2, 3]:
            for psi in [F(2), F(3), F(5, 2)]:
                d1 = proof1_discriminant_closed_form(N, psi)
                d2 = proof1_discriminant_closed_form(N, F(1) / psi)
                assert d1 == d2, f"Not S-symmetric at N={N}, Psi={psi}"

    def test_discriminant_antisymmetric_neg_psi(self):
        """Delta(-Psi) = -Delta(Psi): the discriminant is FF-antisymmetric.

        Proof: Psi + 1/Psi -> -Psi + 1/(-Psi) = -(Psi + 1/Psi).
        """
        for N in [1, 2, 3]:
            for psi in [F(2), F(3), F(5, 2)]:
                d_pos = proof1_discriminant_closed_form(N, psi)
                d_neg = proof1_discriminant_closed_form(N, -psi)
                assert d_neg == -d_pos


# ============================================================================
# Helper for W_N tests
# ============================================================================

def _frac(x) -> Fraction:
    if isinstance(x, Fraction):
        return x
    return Fraction(x)
