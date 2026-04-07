r"""Tests for logarithmic (non-semisimple) Pixton ideal extension.

Tests the extension of thm:pixton-from-mc-semisimple to non-semisimple CohFTs,
verifying the obstruction analysis and explicit computations for W(2), W(3),
symplectic fermions, and admissible sl_2.

Test structure:
  1. Central charge computations (multi-path verification)
  2. Kappa computations (multi-path verification)
  3. Shadow data for non-semisimple algebras
  4. Nilpotent Frobenius algebra structure
  5. Givental-Teleman obstruction analysis
  6. Genus-1 free energy (unconditional)
  7. Genus-2 free energy and planted-forest correction
  8. W(2) explicit computation at genus 2
  9. W(3) computation at genus 2
  10. Admissible sl_2 at genus 2
  11. Semisimple quotient obstruction
  12. Cross-family comparison (semisimple vs non-semisimple)
  13. Shadow metric irreducibility (class M confirmation)
  14. W-matrix analysis
  15. Summary consistency checks
"""

import pytest
from fractions import Fraction

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from sympy import Rational, Integer, Symbol, cancel, simplify

from logarithmic_pixton import (
    admissible_sl2_central_charge,
    admissible_sl2_genus2,
    admissible_sl2_shadow_data,
    analyze_givental_obstruction,
    genus1_free_energy,
    genus2_free_energy_scalar,
    genus2_mc_relation_nonsemisimple,
    genus2_planted_forest_correction,
    logarithmic_pixton_summary,
    semisimple_quotient_analysis,
    symplectic_fermion_central_charge,
    symplectic_fermion_shadow_data,
    triplet_central_charge,
    triplet_central_charge_symbolic,
    triplet_frobenius_data,
    triplet_shadow_data,
    verify_kappa_admissible_sl2,
    verify_kappa_triplet,
    w2_genus2_explicit,
    w3_triplet_genus2,
    w_matrix_analysis,
)

from pixton_shadow_bridge import (
    ShadowData,
    c_sym,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    planted_forest_polynomial,
)


# ============================================================================
# Section 1: Central charge computations
# ============================================================================

class TestCentralCharges:
    """Verify central charges for non-semisimple algebras."""

    def test_w2_central_charge(self):
        """W(2): c = 1 - 6(1)^2/2 = 1 - 3 = -2."""
        assert triplet_central_charge(2) == Rational(-2)

    def test_w3_central_charge(self):
        """W(3): c = 1 - 6(2)^2/3 = 1 - 8 = -7."""
        assert triplet_central_charge(3) == Rational(-7)

    def test_w4_central_charge(self):
        """W(4): c = 1 - 6(3)^2/4 = 1 - 54/4 = 1 - 27/2 = -25/2."""
        assert triplet_central_charge(4) == Rational(-25, 2)

    def test_w5_central_charge(self):
        """W(5): c = 1 - 6(4)^2/5 = 1 - 96/5 = -91/5."""
        assert triplet_central_charge(5) == Rational(-91, 5)

    def test_symplectic_fermion(self):
        """Symplectic fermions: c = -2."""
        assert symplectic_fermion_central_charge() == Rational(-2)

    def test_admissible_sl2_k_minus_half(self):
        """L_{-1/2}(sl_2): c = 3(3-4)/3 = -1."""
        assert admissible_sl2_central_charge(3, 2) == Rational(-1)

    def test_admissible_sl2_k_zero(self):
        """L_0(sl_2) (integrable): c = 3(2-2)/2 = 0."""
        assert admissible_sl2_central_charge(2, 1) == Rational(0)

    def test_admissible_sl2_k_minus_two_thirds(self):
        """L_{-2/3}(sl_2): c = 3(4-6)/4 = -3/2."""
        assert admissible_sl2_central_charge(4, 3) == Rational(-3, 2)

    def test_central_charge_all_negative_for_p_ge_2(self):
        """c(W(p)) < 0 for all p >= 2."""
        for p in range(2, 20):
            assert triplet_central_charge(p) < 0, f"c(W({p})) >= 0"

    def test_central_charge_monotone(self):
        """c(W(p)) is decreasing for p >= 2."""
        for p in range(2, 19):
            assert triplet_central_charge(p) > triplet_central_charge(p + 1), (
                f"c(W({p})) <= c(W({p+1}))"
            )

    def test_w2_equals_symplectic_fermion(self):
        """W(2) and symplectic fermions have the same central charge."""
        assert triplet_central_charge(2) == symplectic_fermion_central_charge()


# ============================================================================
# Section 2: Kappa verification
# ============================================================================

class TestKappaVerification:
    """Multi-path kappa verification for non-semisimple algebras."""

    def test_kappa_w2(self):
        """kappa(W(2)) = c/2 = -1."""
        result = verify_kappa_triplet(2)
        assert result.kappa == Rational(-1)
        assert result.all_agree

    def test_kappa_w3(self):
        """kappa(W(3)) = c/2 = -7/2."""
        result = verify_kappa_triplet(3)
        assert result.kappa == Rational(-7, 2)
        assert result.all_agree

    def test_kappa_admissible_sl2(self):
        """kappa(L_{-1/2}(sl_2)) = 3*3/8 = 9/8.

        NOT c/2 = -1/2 (AP39: kappa != c/2 for affine KM).
        """
        result = verify_kappa_admissible_sl2(3, 2)
        assert result.kappa == Rational(9, 8)
        assert result.all_agree
        # AP39 check
        c_val = admissible_sl2_central_charge(3, 2)
        assert result.kappa != c_val / 2, "AP39 violated: kappa should != c/2 for KM"

    def test_kappa_negative_for_w2(self):
        """kappa(W(2)) = -1 < 0: negative kappa for logarithmic algebra."""
        result = verify_kappa_triplet(2)
        assert result.kappa < 0

    def test_kappa_positive_for_admissible(self):
        """kappa(L_{-1/2}(sl_2)) = 9/8 > 0: positive kappa."""
        result = verify_kappa_admissible_sl2(3, 2)
        assert result.kappa > 0


# ============================================================================
# Section 3: Shadow data
# ============================================================================

class TestShadowData:
    """Test shadow obstruction tower data for non-semisimple algebras."""

    def test_w2_shadow_kappa(self):
        """W(2) shadow kappa = -1."""
        sd = triplet_shadow_data(2)
        assert sd.kappa == Rational(-1)

    def test_w2_shadow_S3(self):
        """W(2) shadow S_3 = 2 (universal for Virasoro)."""
        sd = triplet_shadow_data(2)
        assert sd.S3 == Rational(2)

    def test_w2_shadow_S4(self):
        """W(2) shadow S_4 = 10/((-2)(5(-2)+22)) = 10/((-2)(12)) = -5/12."""
        sd = triplet_shadow_data(2)
        assert sd.S4 == Rational(-5, 12)

    def test_w3_shadow_S4(self):
        """W(3) shadow S_4 = 10/((-7)(5(-7)+22)) = 10/((-7)(-13)) = 10/91."""
        sd = triplet_shadow_data(3)
        assert sd.S4 == Rational(10, 91)

    def test_admissible_shadow_S4_zero(self):
        """Admissible sl_2: S_4 = 0 (class L, Jacobi identity)."""
        sd = admissible_sl2_shadow_data(3, 2)
        assert sd.S4 == Rational(0)

    def test_w2_depth_class_M(self):
        """W(2) has depth class M (infinite shadow depth)."""
        sd = triplet_shadow_data(2)
        assert sd.depth_class == "M"

    def test_admissible_depth_class_L(self):
        """Admissible sl_2 has depth class L (terminates at arity 3)."""
        sd = admissible_sl2_shadow_data(3, 2)
        assert sd.depth_class == "L"

    def test_symplectic_fermion_equals_w2(self):
        """Symplectic fermion shadow data equals W(2) shadow data."""
        sf = symplectic_fermion_shadow_data()
        w2 = triplet_shadow_data(2)
        assert sf.kappa == w2.kappa
        assert sf.S3 == w2.S3
        assert sf.S4 == w2.S4


# ============================================================================
# Section 4: Nilpotent Frobenius algebra
# ============================================================================

class TestNilpotentFrobenius:
    """Test the nilpotent Frobenius algebra structure."""

    def test_w2_rank(self):
        """W(2) Frobenius algebra has rank 3."""
        frob = triplet_frobenius_data(2)
        assert frob.rank == 3

    def test_w2_nilpotent_rank(self):
        """W(2) nilpotent radical has dimension 1."""
        frob = triplet_frobenius_data(2)
        assert frob.nilpotent_rank == 1

    def test_w2_semisimple_rank(self):
        """W(2) semisimple quotient has rank 2."""
        frob = triplet_frobenius_data(2)
        assert frob.semisimple_rank == 2

    def test_w3_rank(self):
        """W(3) Frobenius algebra has rank 5."""
        frob = triplet_frobenius_data(3)
        assert frob.rank == 5

    def test_w3_nilpotent_rank(self):
        """W(3) nilpotent radical has dimension 2."""
        frob = triplet_frobenius_data(3)
        assert frob.nilpotent_rank == 2

    def test_rank_formula(self):
        """rank(W(p)) = 2p - 1 for all p."""
        for p in range(2, 10):
            frob = triplet_frobenius_data(p)
            assert frob.rank == 2 * p - 1

    def test_nilpotent_rank_formula(self):
        """nilpotent_rank(W(p)) = p - 1 for all p."""
        for p in range(2, 10):
            frob = triplet_frobenius_data(p)
            assert frob.nilpotent_rank == p - 1

    def test_rank_decomposition(self):
        """rank = semisimple_rank + nilpotent_rank for all p."""
        for p in range(2, 10):
            frob = triplet_frobenius_data(p)
            assert frob.rank == frob.semisimple_rank + frob.nilpotent_rank

    def test_w2_primaries_count(self):
        """W(2) has 3 primary fields."""
        frob = triplet_frobenius_data(2)
        assert len(frob.primaries) == 3


# ============================================================================
# Section 5: Givental-Teleman obstruction
# ============================================================================

class TestGiventalObstruction:
    """Test the Givental-Teleman obstruction analysis."""

    def test_w2_not_semisimple(self):
        """W(2) Frobenius algebra is not semisimple."""
        frob = triplet_frobenius_data(2)
        obs = analyze_givental_obstruction(frob)
        assert not obs.is_semisimple

    def test_w2_givental_fails(self):
        """Givental-Teleman does not apply to W(2)."""
        frob = triplet_frobenius_data(2)
        obs = analyze_givental_obstruction(frob)
        assert not obs.givental_applies

    def test_w2_obstruction_degree(self):
        """W(2) obstruction degree = 1/3."""
        frob = triplet_frobenius_data(2)
        obs = analyze_givental_obstruction(frob)
        assert obs.obstruction_degree == Rational(1, 3)

    def test_w3_obstruction_degree(self):
        """W(3) obstruction degree = 2/5."""
        frob = triplet_frobenius_data(3)
        obs = analyze_givental_obstruction(frob)
        assert obs.obstruction_degree == Rational(2, 5)

    def test_obstruction_degree_increases(self):
        """Obstruction degree (p-1)/(2p-1) increases with p."""
        prev = Rational(0)
        for p in range(2, 10):
            frob = triplet_frobenius_data(p)
            obs = analyze_givental_obstruction(frob)
            assert obs.obstruction_degree > prev
            prev = obs.obstruction_degree

    def test_obstruction_degree_bounded(self):
        """Obstruction degree < 1/2 for all p (approaches 1/2 as p -> inf)."""
        for p in range(2, 100):
            frob = triplet_frobenius_data(p)
            obs = analyze_givental_obstruction(frob)
            assert obs.obstruction_degree < Rational(1, 2)


# ============================================================================
# Section 6: Genus-1 free energy
# ============================================================================

class TestGenus1FreeEnergy:
    """Test genus-1 free energy (unconditional for all algebras)."""

    def test_w2_F1(self):
        """F_1(W(2)) = kappa * 1/24 = -1/24."""
        sd = triplet_shadow_data(2)
        assert genus1_free_energy(sd) == Rational(-1, 24)

    def test_w3_F1(self):
        """F_1(W(3)) = (-7/2) * 1/24 = -7/48."""
        sd = triplet_shadow_data(3)
        assert genus1_free_energy(sd) == Rational(-7, 48)

    def test_admissible_F1(self):
        """F_1(L_{-1/2}(sl_2)) = (9/8) * 1/24 = 3/64."""
        sd = admissible_sl2_shadow_data(3, 2)
        assert genus1_free_energy(sd) == Rational(3, 64)

    def test_F1_negative_for_negative_kappa(self):
        """F_1 < 0 when kappa < 0 (e.g., W(p) for p >= 2)."""
        for p in range(2, 10):
            sd = triplet_shadow_data(p)
            assert genus1_free_energy(sd) < 0


# ============================================================================
# Section 7: Genus-2 computations
# ============================================================================

class TestGenus2Computations:
    """Test genus-2 free energy and planted-forest corrections."""

    def test_w2_F2_scalar(self):
        """F_2^{scalar}(W(2)) = (-1) * 7/5760 = -7/5760."""
        sd = triplet_shadow_data(2)
        assert genus2_free_energy_scalar(sd) == Rational(-7, 5760)

    def test_w2_planted_forest(self):
        """delta_pf(W(2)) = 2*(20+1)/48 = 42/48 = 7/8."""
        sd = triplet_shadow_data(2)
        pf = genus2_planted_forest_correction(sd)
        assert pf == Rational(7, 8), f"Got {pf}"

    def test_w3_F2_scalar(self):
        """F_2^{scalar}(W(3)) = (-7/2) * 7/5760 = -49/11520."""
        sd = triplet_shadow_data(3)
        F2 = genus2_free_energy_scalar(sd)
        assert F2 == Rational(-49, 11520)

    def test_admissible_F2_scalar(self):
        """F_2^{scalar}(L_{-1/2}(sl_2)) = (9/8) * 7/5760 = 63/46080 = 7/5120."""
        sd = admissible_sl2_shadow_data(3, 2)
        F2 = genus2_free_energy_scalar(sd)
        assert F2 == Rational(7, 5120)

    def test_admissible_planted_forest(self):
        """delta_pf for admissible sl_2 at k=-1/2: S_3=2, kappa=9/8.
        pf = 2*(20 - 9/8)/48 = 2*(151/8)/48 = 302/(8*48) = 151/192."""
        sd = admissible_sl2_shadow_data(3, 2)
        pf = genus2_planted_forest_correction(sd)
        assert pf == Rational(151, 192), f"Got {pf}"

    def test_planted_forest_nonzero_for_nonzero_S3(self):
        """Planted-forest is nonzero whenever S_3 != 0."""
        for p in range(2, 10):
            sd = triplet_shadow_data(p)
            pf = genus2_planted_forest_correction(sd)
            assert pf != 0, f"pf = 0 for W({p})"


# ============================================================================
# Section 8: W(2) explicit genus-2 computation
# ============================================================================

class TestW2Explicit:
    """Detailed verification of W(2) genus-2 computation."""

    def test_w2_explicit_returns(self):
        """w2_genus2_explicit() returns without error."""
        result = w2_genus2_explicit()
        assert result is not None

    def test_w2_kappa(self):
        """W(2) kappa = -1."""
        result = w2_genus2_explicit()
        assert result['kappa'] == Rational(-1)

    def test_w2_S4(self):
        """W(2) S_4 = -5/12."""
        result = w2_genus2_explicit()
        assert result['S4'] == Rational(-5, 12)

    def test_w2_critical_discriminant(self):
        """W(2) Delta = 8*(-1)*(-5/12) = 10/3."""
        result = w2_genus2_explicit()
        assert result['critical_discriminant'] == Rational(10, 3)

    def test_w2_shadow_metric_discriminant(self):
        """W(2) shadow metric discriminant = -320/3 < 0."""
        result = w2_genus2_explicit()
        assert result['shadow_metric_discriminant'] == Rational(-320, 3)

    def test_w2_shadow_metric_irreducible(self):
        """W(2) shadow metric is irreducible (class M)."""
        result = w2_genus2_explicit()
        assert result['shadow_metric_irreducible']

    def test_w2_in_pixton(self):
        """W(2) MC relation lies in I_Pixton."""
        result = w2_genus2_explicit()
        assert result['mc_relation_in_pixton']

    def test_w2_generation_open(self):
        """W(2) Pixton generation is OPEN."""
        result = w2_genus2_explicit()
        assert result['generates_pixton'] == 'OPEN'

    def test_w2_planted_forest_dominance(self):
        """Planted-forest dominates scalar Hodge by factor 720."""
        result = w2_genus2_explicit()
        ratio = result['planted_forest_dominance_ratio']
        assert abs(ratio - 720.0) < 0.01

    def test_w2_F2_matches_tautological(self):
        """F_2^{scalar} = kappa * lambda_2^FP at c = -2.

        Multi-path check:
        Path 1: kappa * 7/5760 = (-1) * 7/5760 = -7/5760.
        Path 2: From the Virasoro formula at c = -2.
        """
        # Path 1
        kappa = Rational(-1)
        F2_p1 = kappa * Rational(7, 5760)

        # Path 2: from Virasoro shadow data at c = -2
        vir_sd = virasoro_shadow_data()
        F2_p2 = cancel(vir_sd.kappa * Rational(7, 5760))
        F2_p2_at_c = F2_p2.subs(c_sym, -2)

        assert F2_p1 == Rational(-7, 5760)
        assert F2_p2_at_c == Rational(-7, 5760)


# ============================================================================
# Section 9: W(3) genus-2 computation
# ============================================================================

class TestW3Triplet:
    """Test W(3) triplet genus-2 computation."""

    def test_w3_returns(self):
        """w3_triplet_genus2() returns without error."""
        result = w3_triplet_genus2()
        assert result is not None

    def test_w3_kappa(self):
        """W(3) kappa = -7/2."""
        result = w3_triplet_genus2()
        assert result['kappa'] == Rational(-7, 2)

    def test_w3_S4(self):
        """W(3) S_4 = 10/91."""
        result = w3_triplet_genus2()
        assert result['S4'] == Rational(10, 91)

    def test_w3_mc_in_pixton(self):
        """W(3) MC relation lies in I_Pixton."""
        result = w3_triplet_genus2()
        assert result['mc_relation_in_pixton']


# ============================================================================
# Section 10: Admissible level
# ============================================================================

class TestAdmissibleLevel:
    """Test admissible sl_2 at genus 2."""

    def test_admissible_returns(self):
        """admissible_sl2_genus2(3, 2) returns without error."""
        result = admissible_sl2_genus2(3, 2)
        assert result is not None

    def test_admissible_kappa(self):
        """kappa = 9/8 for k = -1/2."""
        result = admissible_sl2_genus2(3, 2)
        assert result['kappa'] == Rational(9, 8)

    def test_admissible_class_L(self):
        """Admissible sl_2 is class L."""
        result = admissible_sl2_genus2(3, 2)
        assert result['depth_class'] == 'L'

    def test_admissible_delta_zero(self):
        """Delta = 0 for class L."""
        result = admissible_sl2_genus2(3, 2)
        assert result['critical_discriminant'] == 0

    def test_admissible_mc_in_pixton(self):
        """Admissible MC relation lies in I_Pixton."""
        result = admissible_sl2_genus2(3, 2)
        assert result['mc_relation_in_pixton']


# ============================================================================
# Section 11: Semisimple quotient obstruction
# ============================================================================

class TestSemisimpleQuotient:
    """Test the semisimple quotient strategy and its obstruction."""

    def test_w2_quotient_fails(self):
        """Semisimple quotient strategy fails for W(2)."""
        result = semisimple_quotient_analysis(2)
        assert not result['quotient_strategy_works']

    def test_w2_block_fails(self):
        """Semisimple block strategy fails for W(2)."""
        result = semisimple_quotient_analysis(2)
        assert not result['block_strategy_works']

    def test_w2_N_not_eta_orthogonal(self):
        """Nilpotent radical of W(2) is NOT eta-orthogonal."""
        result = semisimple_quotient_analysis(2)
        assert not result['N_eta_orthogonal']

    def test_w3_quotient_fails(self):
        """Semisimple quotient strategy fails for W(3) too."""
        result = semisimple_quotient_analysis(3)
        assert not result['quotient_strategy_works']


# ============================================================================
# Section 12: Cross-family comparison
# ============================================================================

class TestCrossFamilyComparison:
    """Compare semisimple and non-semisimple algebras."""

    def test_w2_vs_virasoro_at_c_minus_2(self):
        """W(2) and Virasoro at c = -2 have the SAME scalar shadow data.

        The difference is in the module category (semisimple vs non-semisimple),
        not in the OPE structure of the stress tensor.
        """
        w2_sd = triplet_shadow_data(2)
        vir_sd = virasoro_shadow_data()

        # Evaluate Virasoro at c = -2
        vir_kappa = cancel(vir_sd.kappa.subs(c_sym, -2))
        vir_S4 = cancel(vir_sd.S4.subs(c_sym, -2))

        assert w2_sd.kappa == vir_kappa, f"{w2_sd.kappa} vs {vir_kappa}"
        assert w2_sd.S3 == vir_sd.S3
        assert w2_sd.S4 == vir_S4, f"{w2_sd.S4} vs {vir_S4}"

    def test_planted_forest_same_at_c_minus_2(self):
        """Planted-forest correction is the same for W(2) and Vir at c = -2.

        The planted-forest depends only on (kappa, S_3, S_4, ...), which
        are determined by the Virasoro OPE. W(2) and Vir_c at the same c
        give the same planted-forest correction.
        """
        w2_sd = triplet_shadow_data(2)
        vir_sd = virasoro_shadow_data()

        pf_w2 = planted_forest_polynomial(w2_sd)
        pf_vir = cancel(planted_forest_polynomial(vir_sd).subs(c_sym, -2))

        assert pf_w2 == pf_vir, f"W(2): {pf_w2}, Vir: {pf_vir}"

    def test_heisenberg_planted_forest_zero(self):
        """Heisenberg planted-forest is zero (class G control)."""
        heis = heisenberg_shadow_data()
        assert planted_forest_polynomial(heis) == 0


# ============================================================================
# Section 13: Shadow metric analysis
# ============================================================================

class TestShadowMetric:
    """Test shadow metric irreducibility for non-semisimple algebras."""

    def test_w2_discriminant_negative(self):
        """W(2) shadow metric discriminant < 0 (class M)."""
        result = w2_genus2_explicit()
        assert result['shadow_metric_discriminant'] < 0

    def test_w2_discriminant_exact(self):
        """W(2) disc = -320/3 (exact rational value)."""
        result = w2_genus2_explicit()
        assert result['shadow_metric_discriminant'] == Rational(-320, 3)

    def test_all_triplet_class_M(self):
        """All W(p) for p >= 2 are class M (infinite shadow depth).

        The CORRECT criterion (thm:single-line-dichotomy, CLAUDE.md):
        Delta = 8*kappa*S_4 classifies shadow depth.
        Delta = 0 iff tower terminates (class G or L).
        Delta != 0 iff tower is infinite (class M).

        For W(p): kappa = c/2 != 0 (since c < 0) and S_4 != 0
        (since c != 0 and 5c+22 != 0), so Delta != 0 for all p >= 2.

        NOTE: The quadratic polynomial discriminant Q_lin^2 - 4*Q_const*Q_quad
        is a DIFFERENT object from the critical discriminant Delta.
        The former determines whether Q_L(t) has real roots as a polynomial;
        the latter determines shadow depth class.  Only Delta = 0 implies
        finite tower.  The polynomial discriminant can be positive (Q_L has
        real roots) while still having Delta != 0 (infinite tower).
        This happens for W(p), p >= 3: the shadow metric has real roots
        but the tower does not terminate because the roots are irrational.
        """
        for p in range(2, 10):
            sd = triplet_shadow_data(p)
            kappa = sd.kappa
            S4 = sd.S4

            # Critical discriminant (the correct depth classifier)
            Delta = 8 * kappa * S4

            assert Delta != 0, (
                f"W({p}): Delta = {Delta} = 0, but should be nonzero for class M"
            )

            # Cross-check: kappa != 0 and S4 != 0 independently
            assert kappa != 0, f"W({p}): kappa = 0"
            assert S4 != 0, f"W({p}): S_4 = 0"


# ============================================================================
# Section 14: MC relation and Pixton membership
# ============================================================================

class TestMCRelation:
    """Test MC relation existence and Pixton membership."""

    def test_w2_mc_relation_exists(self):
        """MC relation exists for W(2) (unconditional)."""
        sd = triplet_shadow_data(2)
        result = genus2_mc_relation_nonsemisimple(sd)
        assert result['mc_relation_exists']

    def test_w2_mc_lies_in_pixton(self):
        """MC relation of W(2) lies in I_Pixton (unconditional)."""
        sd = triplet_shadow_data(2)
        result = genus2_mc_relation_nonsemisimple(sd)
        assert result['lies_in_pixton']

    def test_w2_generation_open(self):
        """Generation of I_Pixton by W(2) MC relations is OPEN."""
        sd = triplet_shadow_data(2)
        result = genus2_mc_relation_nonsemisimple(sd)
        assert 'OPEN' in result['generates_pixton']

    def test_admissible_mc_lies_in_pixton(self):
        """MC relation of admissible sl_2 lies in I_Pixton."""
        sd = admissible_sl2_shadow_data(3, 2)
        result = genus2_mc_relation_nonsemisimple(sd)
        assert result['lies_in_pixton']


# ============================================================================
# Section 15: W-matrix and summary
# ============================================================================

class TestWMatrix:
    """Test W-matrix analysis."""

    def test_w2_w_matrix(self):
        """W-matrix analysis for W(2) returns valid data."""
        result = w_matrix_analysis(2)
        assert result['w_matrix_defined']
        assert result['modified_symplecticity']
        assert result['preserves_pixton'] == 'OPEN'

    def test_w3_w_matrix(self):
        """W-matrix analysis for W(3)."""
        result = w_matrix_analysis(3)
        assert result['preserves_pixton'] == 'OPEN'


class TestSummary:
    """Test the overall summary."""

    def test_summary_returns(self):
        """Summary function returns without error."""
        result = logarithmic_pixton_summary()
        assert result is not None

    def test_summary_does_not_extend(self):
        """Summary correctly reports non-extension."""
        result = logarithmic_pixton_summary()
        assert not result['extends_to_nonsemisimple']

    def test_summary_obstruction_identified(self):
        """Summary identifies the obstruction."""
        result = logarithmic_pixton_summary()
        assert 'Givental' in result['obstruction']

    def test_summary_w2_data(self):
        """Summary includes W(2) data."""
        result = logarithmic_pixton_summary()
        assert result['w2_data']['kappa'] == Rational(-1)

    def test_summary_w3_data(self):
        """Summary includes W(3) data."""
        result = logarithmic_pixton_summary()
        assert result['w3_data']['kappa'] == Rational(-7, 2)

    def test_summary_admissible_data(self):
        """Summary includes admissible data."""
        result = logarithmic_pixton_summary()
        assert result['admissible_data']['kappa'] == Rational(9, 8)
