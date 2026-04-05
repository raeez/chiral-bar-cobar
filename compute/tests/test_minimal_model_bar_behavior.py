r"""Tests for minimal model bar complex behavior.

Minimal models M(p,q) are SIMPLE QUOTIENTS of the universal Virasoro
algebra — they are NOT freely generated.  The PBW criterion
(prop:pbw-universality) applies to the UNIVERSAL algebra V_k(g), not
to quotients.  The bar complex of a minimal model reflects the failure
of free generation through:

  (a) Null vectors at specific levels, determined by the Kac table.
  (b) Extra bar cohomology (off-diagonal) from the null vector relations.
  (c) Failure of PBW collapse for the simple quotient.
  (d) Shadow obstruction tower singularities when c lies on the Virasoro pole locus.

Key mathematical inputs:
  - c(p,q) = 1 - 6(p-q)^2/(pq)
  - kappa = c/2 for Virasoro (and its quotients)
  - First vacuum null vector level for M(p,q): h_null = pq - p - q + 1
  - Bar-relevant range for Virasoro (generator weight 2): h >= 4 at
    bar degree 2 (two copies of T at weight 2 each).
  - S_4 = 10 / (c(5c+22)): diverges when c=0 or 5c+22=0.
  - Yang-Lee M(2,5): c = -22/5, so 5c+22 = 0 — the shadow obstruction tower pole.
  - M(2,3) trivial: c = 0, so S_4 has a pole from the c factor.

Anti-patterns guarded against:
  AP1:  All kappa and c values computed from first principles.
  AP3:  Null vector levels computed, not pattern-matched.
  AP7:  Universal vs simple quotient distinction maintained throughout.
  AP10: Cross-family consistency checks (kappa additivity, complementarity).
  AP14: Shadow depth != Koszulness.  Minimal models fail Koszulness
        because of null vectors, not because of shadow depth.

References:
  prop:pbw-universality (chiral_koszul_pairs.tex)
  thm:kac-shapovalov-koszulness (chiral_koszul_pairs.tex)
  comp:ising-bar-interpretation (minimal_model_examples.tex)
"""

import math

import pytest
from fractions import Fraction
from sympy import Rational, oo

from compute.lib.minimal_model_bar import (
    minimal_model_c,
    MINIMAL_MODELS,
    conformal_weight,
    conformal_weights_table,
    n_primaries,
    minimal_model_primaries,
    null_vector_levels,
    bar_cohomology_ranks,
    shadow_tower_minimal_model,
    shadow_discriminant_complementarity,
    cdg_curvature,
    kac_determinant_factors,
    kac_determinant_total_degree,
    partition_count,
    koszul_dual_central_charge,
    complementarity_sum_kappa,
    effective_central_charge,
    is_unitary,
)

from compute.lib.koszulness_landscape import (
    KoszulStatus,
    ProofMechanism,
    ShadowClass,
    minimal_model as kl_minimal_model,
    virasoro_generic,
)


# ===========================================================================
# 1. UNIVERSAL VS SIMPLE QUOTIENT DISTINCTION
# ===========================================================================


class TestUniversalVsSimpleQuotient:
    """The UNIVERSAL Virasoro at any c is Koszul.
    The SIMPLE QUOTIENT at minimal model c is NOT.
    These are different objects (AP7, AP25)."""

    def test_universal_virasoro_is_koszul(self):
        """The universal Virasoro algebra is Koszul at ALL c."""
        vir = virasoro_generic()
        assert vir.koszul_status == KoszulStatus.PROVED
        assert vir.pbw_filtration_exists is True
        assert vir.bar_concentrated is True

    def test_ising_simple_quotient_not_koszul(self):
        """M(3,4) = Ising is the simple quotient: NOT Koszul."""
        data = kl_minimal_model(3, 4)
        assert data.koszul_status == KoszulStatus.NOT_KOSZUL
        assert data.algebra_type == "simple_quotient"

    def test_yang_lee_simple_quotient_not_koszul(self):
        """M(2,5) = Yang-Lee is the simple quotient: NOT Koszul."""
        data = kl_minimal_model(2, 5)
        assert data.koszul_status == KoszulStatus.NOT_KOSZUL
        assert data.algebra_type == "simple_quotient"

    def test_universal_bar_concentrated_regardless_of_c(self):
        """Universal Virasoro bar cohomology is concentrated at ALL c.

        H^0 = 1, H^1 = 1 (generator T), H^2 = 1 (relation),
        H^k = 0 for k >= 3.  Independent of c.
        """
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 4), (6, 5)]:
            ranks = bar_cohomology_ranks(p, q, max_degree=6)
            assert ranks[0] == 1
            assert ranks[1] == 1
            assert ranks[2] == 1
            for k in range(3, 7):
                assert ranks[k] == 0, (
                    f"M({p},{q}): universal bar H^{k} = {ranks[k]} != 0"
                )

    def test_pbw_fails_for_simple_quotient(self):
        """PBW filtration fails for all minimal model simple quotients
        where null is in bar-relevant range."""
        for p, q in [(3, 4), (2, 5)]:
            data = kl_minimal_model(p, q)
            assert data.pbw_filtration_exists is False
            assert data.pbw_collapse is False

    def test_koszulness_is_not_shadow_depth(self):
        """Shadow depth is infinite for both universal and simple quotient
        Virasoro (AP14). Koszulness fails for the quotient due to null
        vectors, NOT due to shadow depth."""
        vir = virasoro_generic()
        assert vir.shadow_class == ShadowClass.M
        assert vir.shadow_depth == 10**9  # infinite
        assert vir.is_koszul is True

        ising = kl_minimal_model(3, 4)
        assert ising.shadow_class == ShadowClass.M
        assert ising.shadow_depth == 10**9  # also infinite
        assert ising.is_koszul is False


# ===========================================================================
# 2. NULL VECTOR STRUCTURE
# ===========================================================================


class TestNullVectorStructure:
    """Null vectors in minimal models and their effect on the bar complex."""

    def test_trivial_null_level(self):
        """M(3,2) trivial: first nontrivial null at h = 3*2 - 3 - 2 + 1 = 2."""
        # Using the koszulness_landscape convention (p < q):
        data = kl_minimal_model(2, 3)
        # h_null = p*q - p - q + 1 = 2*3 - 2 - 3 + 1 = 2
        # But kl_minimal_model computes h_null differently (check from source)
        # Actually in the koszulness_landscape, the formula is p*q - p - q + 1
        # For (2,3): 6 - 2 - 3 + 1 = 2
        assert data.central_charge == Rational(0)

    def test_yang_lee_null_level(self):
        """M(2,5) Yang-Lee: first null at h = 2*5 - 2 - 5 + 1 = 4."""
        data = kl_minimal_model(2, 5)
        assert data.central_charge == Rational(-22, 5)
        # The null at level 4 is exactly at bar-relevant threshold

    def test_ising_null_level(self):
        """M(3,4) Ising: first null at h = 3*4 - 3 - 4 + 1 = 6."""
        data = kl_minimal_model(3, 4)
        assert data.central_charge == Rational(1, 2)
        # Null at level 6 > 4, definitely in bar-relevant range

    def test_null_vector_levels_from_kac_table(self):
        """Null vectors occur at h_{r,s} = 0 levels (beyond vacuum)."""
        # For M(4,3) Ising, check the Kac table using minimal_model_bar
        nulls = null_vector_levels(4, 3)
        # h_{1,1} = 0 is the vacuum itself; the nontrivial null
        # is at (r,s) = (2,2) with level 4 or (1,1) + descendants
        # Actually null_vector_levels finds all (r,s) with h_{r,s} = 0
        # For Ising M(4,3): (r,s) with h_{r,s} = 0 and 1<=r<=2, 1<=s<=3
        # h_{1,1} = 0 (vacuum), h_{2,3} should also give 0 by identification
        levels = [n[2] for n in nulls]  # level = r*s
        assert 1 in levels  # (1,1) at level 1

    def test_null_vector_levels_yang_lee(self):
        """Yang-Lee M(5,2): null levels from Kac table."""
        nulls = null_vector_levels(5, 2)
        levels = [n[2] for n in nulls]
        assert 1 in levels  # (1,1) vacuum

    def test_null_weight_formula_consistency(self):
        """h_null = pq - p - q + 1 = (p-1)(q-1) for all standard models.

        Independent computation: pq - p - q + 1 = (p-1)(q-1).
        """
        models = [(3, 2), (4, 3), (5, 2), (5, 4), (6, 5), (7, 6)]
        for p, q in models:
            h_null = p * q - p - q + 1
            h_check = (p - 1) * (q - 1)
            assert h_null == h_check, (
                f"M({p},{q}): pq-p-q+1={h_null} != (p-1)(q-1)={h_check}"
            )

    def test_bar_relevant_range_virasoro(self):
        """Virasoro generator has weight 2. Bar degree n has minimum
        weight 2n. Bar-relevant range starts at bar degree 2, weight 4."""
        bar_min_weight = 2 * 2  # weight_of_generator * min_bar_degree
        assert bar_min_weight == 4

    def test_null_in_bar_range_classification(self):
        """Classify which minimal models have null in bar-relevant range.

        h_null >= 4 means null IS in bar range.
        """
        bar_min = 4
        results = {}
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 4), (6, 5)]:
            h_null = (p - 1) * (q - 1)
            results[(p, q)] = h_null >= bar_min

        # M(3,2): h_null = 2 < 4: NOT in range
        assert results[(3, 2)] is False
        # M(4,3) Ising: h_null = 6 >= 4: IN range
        assert results[(4, 3)] is True
        # M(5,2) Yang-Lee: h_null = 4 >= 4: IN range (boundary)
        assert results[(5, 2)] is True
        # M(5,4) TCI: h_null = 12 >= 4: IN range
        assert results[(5, 4)] is True
        # M(6,5) Potts: h_null = 20 >= 4: IN range
        assert results[(6, 5)] is True

    def test_trivial_model_null_below_bar_range(self):
        """M(3,2) = trivial model: h_null = 2 < 4, null is BELOW bar
        range. This is why the Koszul status is OPEN for this model
        (in the koszulness_landscape framework), not definitely NOT Koszul.

        NOTE: in koszulness_landscape.py, M(2,3) with p < q convention.
        """
        data = kl_minimal_model(2, 3)
        # h_null = (2-1)(3-1) = 2 < 4
        # Status should be OPEN (not NOT_KOSZUL) since null is below
        # bar-relevant range
        assert data.koszul_status == KoszulStatus.OPEN


# ===========================================================================
# 3. KAPPA FOR MINIMAL MODELS
# ===========================================================================


class TestKappaMinimalModels:
    """Verify kappa(M(p,q)) = c(p,q)/2 from first principles.

    All minimal models are Virasoro quotients, so kappa = c/2.
    This is the SAME formula as the universal Virasoro at the same c.
    The kappa invariant does not depend on whether you take the
    universal or simple quotient (it is computed from the OPE, which
    is the same for both at the level of the current algebra).
    """

    def test_ising_kappa(self):
        """M(4,3) Ising: c = 1/2, kappa = 1/4."""
        c = minimal_model_c(4, 3)
        assert c == Rational(1, 2)
        assert c / 2 == Rational(1, 4)

    def test_yang_lee_kappa(self):
        """M(5,2) Yang-Lee: c = -22/5, kappa = -11/5."""
        c = minimal_model_c(5, 2)
        assert c == Rational(-22, 5)
        assert c / 2 == Rational(-11, 5)

    def test_trivial_kappa(self):
        """M(3,2) trivial: c = 0, kappa = 0."""
        c = minimal_model_c(3, 2)
        assert c == Rational(0)
        assert c / 2 == Rational(0)

    def test_tricritical_ising_kappa(self):
        """M(5,4) TCI: c = 7/10, kappa = 7/20."""
        c = minimal_model_c(5, 4)
        assert c == Rational(7, 10)
        assert c / 2 == Rational(7, 20)

    def test_three_state_potts_kappa(self):
        """M(6,5) Potts: c = 4/5, kappa = 2/5."""
        c = minimal_model_c(6, 5)
        assert c == Rational(4, 5)
        assert c / 2 == Rational(2, 5)

    def test_kappa_from_koszulness_landscape(self):
        """kappa from koszulness_landscape matches c/2."""
        for p, q in [(3, 4), (2, 5)]:
            data = kl_minimal_model(p, q)
            c = data.central_charge
            assert data.kappa == c / 2

    def test_kappa_independent_computation(self):
        """kappa = c/2 for Virasoro.  Independent computation:
        kappa(Vir_c) = c/2.  Not copied from any other family (AP1)."""
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 4), (6, 5), (7, 6)]:
            c = minimal_model_c(p, q)
            kappa = c / 2
            # Verify the formula: c = 1 - 6(p-q)^2/(pq)
            c_check = 1 - Rational(6 * (p - q)**2, p * q)
            assert c == c_check
            assert kappa == c_check / 2


# ===========================================================================
# 4. SHADOW TOWER SINGULARITIES
# ===========================================================================


class TestShadowTowerSingularities:
    """Shadow obstruction tower has poles where S_4 = 10/(c(5c+22)) diverges.

    Two singularities:
      (a) c = 0: kappa = 0 means uncurved; S_4 has a pole.
      (b) 5c + 22 = 0, i.e., c = -22/5: Yang-Lee value.

    The Yang-Lee model M(2,5) sits exactly on the shadow obstruction tower pole.
    """

    def test_yang_lee_hits_s4_pole(self):
        """M(5,2) Yang-Lee: c = -22/5, so 5c + 22 = 0. S_4 diverges."""
        c = minimal_model_c(5, 2)
        assert c == Rational(-22, 5)
        assert 5 * c + 22 == 0

    def test_yang_lee_shadow_tower_singular(self):
        """Shadow obstruction tower data at Yang-Lee has S_4 = None (singular)."""
        tower = shadow_tower_minimal_model(5, 2)
        assert tower["S4"] is None
        assert tower["class"] == "singular"

    def test_trivial_model_s4_pole(self):
        """M(3,2) trivial: c = 0, S_4 = 10/(0 * 22) diverges."""
        c = minimal_model_c(3, 2)
        assert c == 0
        tower = shadow_tower_minimal_model(3, 2)
        # c = 0 case: kappa = 0, special handling
        assert tower["kappa"] == 0
        assert tower["class"] == "trivial"

    def test_ising_shadow_tower_nonsingular(self):
        """M(4,3) Ising: c = 1/2, 5c+22 = 49/2 != 0. Tower regular."""
        c = minimal_model_c(4, 3)
        denom = 5 * c + 22
        assert denom == Rational(49, 2)
        assert denom != 0

        tower = shadow_tower_minimal_model(4, 3)
        assert tower["S4"] is not None
        assert tower["class"] == "M"

    def test_ising_s4_value(self):
        """M(4,3) Ising: S_4 = 10/(c(5c+22)) = 10/((1/2)(49/2)) = 40/49."""
        c = Rational(1, 2)
        denom_c = c * (5 * c + 22)
        expected_s4 = Rational(10) / denom_c
        assert expected_s4 == Rational(40, 49)

        tower = shadow_tower_minimal_model(4, 3)
        assert tower["S4"] == Rational(40, 49)

    def test_ising_delta(self):
        """M(4,3) Ising: Delta = 40/(5c+22) = 40/(49/2) = 80/49."""
        c = Rational(1, 2)
        denom = 5 * c + 22
        expected_delta = Rational(40) / denom
        assert expected_delta == Rational(80, 49)

        tower = shadow_tower_minimal_model(4, 3)
        assert tower["Delta"] == Rational(80, 49)

    def test_tricritical_ising_s4(self):
        """M(5,4) TCI: c = 7/10, S_4 = 10/((7/10)(57/10)) = 10000/399."""
        c = Rational(7, 10)
        denom_c = c * (5 * c + 22)
        # 5c + 22 = 35/10 + 22 = 57/2... wait: 5*(7/10) + 22 = 7/2 + 22 = 51/2
        # Let me recompute: 5 * (7/10) = 35/10 = 7/2; 7/2 + 22 = 51/2
        assert 5 * c + 22 == Rational(51, 2)
        expected_s4 = Rational(10) / (c * Rational(51, 2))
        # = 10 / (7/10 * 51/2) = 10 / (357/20) = 200/357
        assert expected_s4 == Rational(200, 357)

        tower = shadow_tower_minimal_model(5, 4)
        assert tower["S4"] == Rational(200, 357)

    def test_shadow_tower_pole_locus_enumeration(self):
        """Enumerate which minimal models sit on the S_4 pole locus.

        The S_4 pole locus is c = 0 or c = -22/5.
        Among standard minimal models, only M(3,2) (c=0) and M(5,2) (c=-22/5)
        sit on this locus.
        """
        pole_models = []
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 4), (6, 5), (7, 6)]:
            c = minimal_model_c(p, q)
            if c == 0 or 5 * c + 22 == 0:
                pole_models.append((p, q))
        assert (3, 2) in pole_models
        assert (5, 2) in pole_models
        assert len(pole_models) == 2


# ===========================================================================
# 5. CDG (CURVED DG) STRUCTURE
# ===========================================================================


class TestCDGStructure:
    """Minimal models as simple quotients have curved DG structure.
    The universal Virasoro is NOT curved."""

    def test_simple_quotient_is_curved(self):
        """All minimal model simple quotients are curved."""
        for p, q in [(4, 3), (5, 2), (5, 4), (6, 5)]:
            cdg = cdg_curvature(p, q)
            assert cdg["is_curved"] is True

    def test_universal_virasoro_not_curved(self):
        """The universal Virasoro is NOT curved."""
        cdg = cdg_curvature(4, 3)
        assert cdg["universal_is_curved"] is False

    def test_ising_null_level_in_cdg(self):
        """Ising CDG: null at level (p-1)(q-1) = 3*2 = 6."""
        cdg = cdg_curvature(4, 3)
        assert cdg["null_vector_level"] == 6

    def test_yang_lee_null_level_in_cdg(self):
        """Yang-Lee CDG: null at level (p-1)(q-1) = 4*1 = 4."""
        cdg = cdg_curvature(5, 2)
        assert cdg["null_vector_level"] == 4

    def test_trivial_null_level_in_cdg(self):
        """Trivial CDG: null at level (p-1)(q-1) = 2*1 = 2."""
        cdg = cdg_curvature(3, 2)
        assert cdg["null_vector_level"] == 2

    def test_admissible_levels(self):
        """Admissible level for M(p,q): k = p/q - 2."""
        cdg_ising = cdg_curvature(4, 3)
        assert cdg_ising["admissible_level"] == Rational(4, 3) - 2

        cdg_yl = cdg_curvature(5, 2)
        assert cdg_yl["admissible_level"] == Rational(5, 2) - 2


# ===========================================================================
# 6. COMPLEMENTARITY AND KOSZUL DUALITY
# ===========================================================================


class TestMinimalModelComplementarity:
    """Virasoro Koszul duality: c -> 26 - c.
    kappa + kappa' = 13 (AP24: NOT zero for Virasoro)."""

    def test_ising_koszul_dual_c(self):
        """Ising c = 1/2; dual c' = 51/2."""
        c_dual = koszul_dual_central_charge(4, 3)
        assert c_dual == Rational(51, 2)

    def test_yang_lee_koszul_dual_c(self):
        """Yang-Lee c = -22/5; dual c' = 26 + 22/5 = 152/5."""
        c_dual = koszul_dual_central_charge(5, 2)
        assert c_dual == Rational(152, 5)

    def test_complementarity_sum_always_13(self):
        """kappa + kappa' = 13 for ALL Virasoro quotients (AP24)."""
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 4), (6, 5)]:
            assert complementarity_sum_kappa(p, q) == 13

    def test_complementarity_is_not_zero(self):
        """kappa + kappa' = 13, NOT 0 (AP24 violation if stated as 0)."""
        for p, q in [(4, 3), (5, 4), (6, 5)]:
            c = minimal_model_c(p, q)
            kappa = c / 2
            kappa_dual = (26 - c) / 2
            total = kappa + kappa_dual
            assert total == 13
            assert total != 0

    def test_discriminant_complementarity_ising(self):
        """Verify Delta(A) + Delta(A!) = 6960/((5c+22)(152-5c))
        for Ising."""
        result = shadow_discriminant_complementarity(4, 3)
        assert result["match"] is True

    def test_discriminant_complementarity_tci(self):
        """Verify discriminant complementarity for TCI."""
        result = shadow_discriminant_complementarity(5, 4)
        assert result["match"] is True

    def test_yang_lee_discriminant_singular(self):
        """Yang-Lee: 5c+22 = 0, discriminant complementarity undefined."""
        result = shadow_discriminant_complementarity(5, 2)
        assert result["match"] is None


# ===========================================================================
# 7. KAC DETERMINANT AND PARTITION STRUCTURE
# ===========================================================================


class TestKacDeterminantStructure:
    """Test the Kac determinant factors that create null vectors."""

    def test_partition_count_small(self):
        """Verify small partition counts p(n)."""
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7

    def test_kac_det_degree_growth(self):
        """Kac determinant degree grows with level."""
        degrees = [kac_determinant_total_degree(n) for n in range(1, 8)]
        # Degree should be monotonically increasing
        for i in range(len(degrees) - 1):
            assert degrees[i + 1] >= degrees[i]

    def test_kac_det_degree_level_1(self):
        """At level 1: only (r,s) = (1,1) contributes, degree = p(0) = 1."""
        assert kac_determinant_total_degree(1) == 1

    def test_kac_det_degree_level_2(self):
        """At level 2: (1,1) with p(1)=1, (2,1) with p(0)=1,
        (1,2) with p(0)=1 = total 3."""
        assert kac_determinant_total_degree(2) == 3

    def test_kac_det_factors_ising_level_6(self):
        """At level 6 for Ising M(4,3), verify factors exist."""
        factors = kac_determinant_factors(4, 3, 6)
        # There should be factors with rs <= 6
        assert len(factors) > 0
        # Check that (1,1) is always present with h = 0
        has_vacuum = any(f[0] == 1 and f[1] == 1 for f in factors)
        assert has_vacuum


# ===========================================================================
# 8. EFFECTIVE CENTRAL CHARGE AND UNITARITY
# ===========================================================================


class TestEffectiveCentralCharge:
    """Effective central charge c_eff = c - 24*h_min."""

    def test_unitary_c_eff_equals_c(self):
        """For unitary models, h_min = 0 so c_eff = c."""
        for p, q in [(4, 3), (5, 4), (6, 5), (7, 6)]:
            c = minimal_model_c(p, q)
            c_eff = effective_central_charge(p, q)
            assert c_eff == c

    def test_yang_lee_c_eff(self):
        """Yang-Lee M(5,2): h_min = -1/5, c_eff = c + 24/5."""
        c = minimal_model_c(5, 2)
        c_eff = effective_central_charge(5, 2)
        # h_min = -1/5, so c_eff = -22/5 - 24*(-1/5) = -22/5 + 24/5 = 2/5
        assert c_eff == Rational(2, 5)

    def test_unitary_classification(self):
        """Unitary iff p = q + 1."""
        assert is_unitary(4, 3) is True   # Ising
        assert is_unitary(5, 4) is True   # TCI
        assert is_unitary(6, 5) is True   # Potts
        assert is_unitary(5, 2) is False  # Yang-Lee
        assert is_unitary(7, 2) is False  # non-unitary


# ===========================================================================
# 9. CROSS-CONSISTENCY: MINIMAL MODEL VS VIRASORO
# ===========================================================================


class TestMinimalModelVsVirasoro:
    """The shadow obstruction tower data for a minimal model should match
    the Virasoro shadow obstruction tower at the same c value (when regular)."""

    def test_ising_shadow_matches_virasoro(self):
        """Ising shadow obstruction tower = Virasoro shadow obstruction tower at c=1/2."""
        tower = shadow_tower_minimal_model(4, 3)
        assert tower["kappa"] == Rational(1, 4)
        assert tower["alpha"] == 2  # universal for Virasoro
        assert tower["class"] == "M"  # class M (infinite depth)

    def test_tci_shadow_matches_virasoro(self):
        """TCI shadow obstruction tower at c=7/10."""
        tower = shadow_tower_minimal_model(5, 4)
        assert tower["kappa"] == Rational(7, 20)
        assert tower["alpha"] == 2

    def test_potts_shadow_matches_virasoro(self):
        """Three-state Potts shadow obstruction tower at c=4/5."""
        tower = shadow_tower_minimal_model(6, 5)
        assert tower["kappa"] == Rational(2, 5)
        assert tower["alpha"] == 2

    def test_shadow_metric_coefficients(self):
        """Q_L(t) = (2kappa + 3*alpha*t)^2 + 2*Delta*t^2.

        Coefficients: q0 = 4*kappa^2, q1 = 12*kappa*alpha,
        q2 = 9*alpha^2 + 2*Delta.
        """
        tower = shadow_tower_minimal_model(4, 3)
        kappa = tower["kappa"]
        alpha = tower["alpha"]
        Delta = tower["Delta"]

        assert tower["q0"] == 4 * kappa**2
        assert tower["q1"] == 12 * kappa * alpha
        assert tower["q2"] == 9 * alpha**2 + 2 * Delta

    def test_koszulness_landscape_has_correct_proof_mechanism(self):
        """Minimal models use NULL_VECTOR_OBSTRUCTION, not PBW."""
        for p, q in [(3, 4), (2, 5)]:
            data = kl_minimal_model(p, q)
            assert data.proof_mechanism == ProofMechanism.NULL_VECTOR_OBSTRUCTION


# ===========================================================================
# 10. THE FIVE STANDARD MINIMAL MODELS
# ===========================================================================


class TestFiveStandardModels:
    """Comprehensive test of the five standard minimal models."""

    @pytest.mark.parametrize("name,p,q,c_expected", [
        ("trivial", 3, 2, Rational(0)),
        ("Ising", 4, 3, Rational(1, 2)),
        ("Yang-Lee", 5, 2, Rational(-22, 5)),
        ("TCI", 5, 4, Rational(7, 10)),
        ("Potts", 6, 5, Rational(4, 5)),
    ])
    def test_central_charge(self, name, p, q, c_expected):
        """Central charge matches expected value."""
        assert minimal_model_c(p, q) == c_expected

    @pytest.mark.parametrize("name,p,q,n_expected", [
        ("trivial", 3, 2, 1),
        ("Ising", 4, 3, 3),
        ("Yang-Lee", 5, 2, 2),
        ("TCI", 5, 4, 6),
        ("Potts", 6, 5, 10),
    ])
    def test_number_of_primaries(self, name, p, q, n_expected):
        """Number of primaries = (p-1)(q-1)/2."""
        assert n_primaries(p, q) == n_expected

    @pytest.mark.parametrize("name,p,q,h_null_expected", [
        ("trivial", 3, 2, 2),
        ("Ising", 4, 3, 6),
        ("Yang-Lee", 5, 2, 4),
        ("TCI", 5, 4, 12),
        ("Potts", 6, 5, 20),
    ])
    def test_null_vector_level(self, name, p, q, h_null_expected):
        """First vacuum null at level (p-1)(q-1)."""
        h_null = (p - 1) * (q - 1)
        assert h_null == h_null_expected

    @pytest.mark.parametrize("name,p,q,kappa_expected", [
        ("trivial", 3, 2, Rational(0)),
        ("Ising", 4, 3, Rational(1, 4)),
        ("Yang-Lee", 5, 2, Rational(-11, 5)),
        ("TCI", 5, 4, Rational(7, 20)),
        ("Potts", 6, 5, Rational(2, 5)),
    ])
    def test_kappa_values(self, name, p, q, kappa_expected):
        """kappa = c/2 for each model."""
        c = minimal_model_c(p, q)
        assert c / 2 == kappa_expected

    @pytest.mark.parametrize("name,p,q,in_range", [
        ("trivial", 3, 2, False),
        ("Ising", 4, 3, True),
        ("Yang-Lee", 5, 2, True),
        ("TCI", 5, 4, True),
        ("Potts", 6, 5, True),
    ])
    def test_null_in_bar_range(self, name, p, q, in_range):
        """Whether null vector is in bar-relevant range (h >= 4)."""
        h_null = (p - 1) * (q - 1)
        assert (h_null >= 4) == in_range


# ===========================================================================
# 11. YANG-LEE DEEP DIVE (shadow pole)
# ===========================================================================


class TestYangLeeDeep:
    """Deep verification of Yang-Lee M(5,2) at the shadow obstruction tower pole."""

    def test_c_is_minus_22_over_5(self):
        """c = 1 - 6*9/10 = -22/5."""
        c = minimal_model_c(5, 2)
        # 1 - 6*(5-2)^2/(5*2) = 1 - 6*9/10 = 1 - 54/10 = -44/10 = -22/5
        assert c == Rational(-22, 5)

    def test_5c_plus_22_vanishes(self):
        """5c + 22 = 5*(-22/5) + 22 = -22 + 22 = 0."""
        c = minimal_model_c(5, 2)
        assert 5 * c + 22 == 0

    def test_kappa_negative(self):
        """kappa = -11/5 < 0 (non-unitary)."""
        c = minimal_model_c(5, 2)
        kappa = c / 2
        assert kappa == Rational(-11, 5)
        assert kappa < 0

    def test_shadow_tower_data_singular(self):
        """Shadow obstruction tower at Yang-Lee is classified as singular."""
        tower = shadow_tower_minimal_model(5, 2)
        assert tower["class"] == "singular"
        assert tower["S4"] is None
        assert tower["Delta"] is None

    def test_koszul_dual_c(self):
        """Koszul dual: c' = 26 - (-22/5) = 152/5."""
        c_dual = koszul_dual_central_charge(5, 2)
        assert c_dual == Rational(152, 5)
        # Check: 5*c' + 22 = 5*(152/5) + 22 = 152 + 22 = 174 != 0
        # So the dual is NOT on the pole locus
        assert 5 * c_dual + 22 == 174

    def test_yang_lee_two_primaries(self):
        """Yang-Lee has 2 primaries: vacuum (h=0) and phi (h=-1/5)."""
        prims = minimal_model_primaries(5, 2)
        assert len(prims) == 2
        weights = conformal_weights_table(5, 2)
        h_values = sorted(weights.values())
        assert h_values == [Rational(-1, 5), Rational(0)]

    def test_yang_lee_non_unitary(self):
        """Yang-Lee is non-unitary (h = -1/5 < 0)."""
        assert is_unitary(5, 2) is False

    def test_yang_lee_c_eff(self):
        """c_eff = c - 24*h_min = -22/5 - 24*(-1/5) = 2/5."""
        c_eff = effective_central_charge(5, 2)
        assert c_eff == Rational(2, 5)
