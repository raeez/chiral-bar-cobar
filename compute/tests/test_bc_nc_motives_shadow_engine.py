"""Tests for the noncommutative motives from bar complex dg-category engine (BC-102).

Tests cover:
1. K_0 rank via direct computation + representation counting + fusion ring (3 paths)
2. K_0 data structure and generators
3. Shadow K_1 rank and monodromy
4. Hochschild homology dimensions (bar complex path + direct path)
5. Hochschild Euler characteristic
6. Cyclic homology and SBI sequence
7. Shadow period pairing (HC_2 with Theta_A recovers kappa)
8. NC Chern character for sl_2 representations
9. NC zeta function and categorical zeta comparison
10. Motivic measure evaluation
11. Derived Morita invariance for Koszul dual pairs
12. Cross-family consistency (kappa additivity, complementarity, K_0 duality)
13. Full NC motivic package integration

CRITICAL PITFALLS TESTED:
- AP1:  kappa formula correctness per family (recomputed, not copied)
- AP9:  S_2 = kappa != c/2 in general
- AP20: kappa(A) vs kappa_eff
- AP24: complementarity sum != 0 for Virasoro (sum = 13)
- AP25: bar != Verdier dual != cobar != derived center
- AP33: H_k^! = Sym^ch(V*) != H_{-k}
- AP48: kappa depends on the full algebra, not the Virasoro sub

VERIFICATION PATHS (>= 3 per claim):
  Path 1: K_0 rank via representation counting
  Path 2: HH from bar complex vs from A-module Hochschild
  Path 3: Chern character maps to correct HH_0 class
  Path 4: NC zeta vs categorical zeta comparison
  Path 5: Koszul duality: K_0(B(A)) = K_0(B(A!))
  Path 6: Cyclic period pairing recovers kappa
  Path 7: Motivic measure at L=1 vs shadow GF evaluation
"""

import pytest
from fractions import Fraction

from compute.lib.bc_nc_motives_shadow_engine import (
    # Basic invariants
    kappa,
    kappa_dual,
    complementarity_sum,
    shadow_depth,
    FAMILIES,
    SHADOW_CLASS,
    # K-theory
    K0Data,
    k0_rank,
    k0_data,
    k0_rank_via_representation_counting,
    k0_rank_via_fusion_ring,
    # Shadow K_1
    shadow_k1_rank,
    shadow_k1_monodromy,
    # Hochschild homology
    hh_dimension,
    hh_euler_characteristic,
    hh_from_bar_complex,
    # Cyclic homology
    cyclic_homology_dimension,
    shadow_period,
    shadow_period_numerical,
    # Chern character
    ChernCharacterData,
    nc_chern_character_sl2,
    nc_chern_character_heisenberg,
    verify_chern_character_additivity,
    chern_total_dimension,
    # NC zeta
    nc_zeta_sl2,
    nc_zeta_heisenberg,
    nc_zeta_categorical_comparison_sl2,
    # Motivic measure
    shadow_coefficients,
    motivic_measure_evaluate,
    motivic_measure_at_one,
    # Morita invariance
    MoritaComparisonData,
    morita_comparison_virasoro,
    morita_comparison_affine_sl2,
    # Cross-family
    verify_kappa_additivity,
    verify_complementarity_sum,
    verify_k0_koszul_duality,
    # Full package
    NCMotivicPackage,
    full_nc_motivic_package,
)


# ======================================================================
#  Section 1: kappa (modular characteristic) — AP1 verified
# ======================================================================

class TestKappa:
    """Test kappa formulas for each family independently (AP1)."""

    def test_kappa_heisenberg_k1(self):
        assert kappa("Heisenberg", k=1) == Fraction(1)

    def test_kappa_heisenberg_k2(self):
        assert kappa("Heisenberg", k=2) == Fraction(2)

    def test_kappa_heisenberg_half(self):
        assert kappa("Heisenberg", k=Fraction(1, 2)) == Fraction(1, 2)

    def test_kappa_affine_sl2_k1(self):
        # kappa = 3(k+2)/4 = 3*3/4 = 9/4
        assert kappa("Affine_sl2", k=1) == Fraction(9, 4)

    def test_kappa_affine_sl2_k2(self):
        # kappa = 3(2+2)/4 = 3
        assert kappa("Affine_sl2", k=2) == Fraction(3)

    def test_kappa_affine_sl2_k4(self):
        # kappa = 3(4+2)/4 = 18/4 = 9/2
        assert kappa("Affine_sl2", k=4) == Fraction(9, 2)

    def test_kappa_virasoro_c1(self):
        assert kappa("Virasoro", c=1) == Fraction(1, 2)

    def test_kappa_virasoro_c26(self):
        assert kappa("Virasoro", c=26) == Fraction(13)

    def test_kappa_virasoro_c13(self):
        # Self-dual point
        assert kappa("Virasoro", c=13) == Fraction(13, 2)

    def test_kappa_w3_c2(self):
        # kappa = 5c/6 = 10/6 = 5/3
        assert kappa("W3", c=2) == Fraction(5, 3)

    def test_kappa_unknown_family_raises(self):
        with pytest.raises(ValueError):
            kappa("Unknown")


# ======================================================================
#  Section 2: kappa dual and complementarity — AP24 verified
# ======================================================================

class TestKappaDualAndComplementarity:
    """Test kappa(A!) and the complementarity sum kappa + kappa'."""

    def test_kappa_dual_heisenberg(self):
        # H_k^! has kappa = -k
        assert kappa_dual("Heisenberg", k=1) == Fraction(-1)

    def test_kappa_dual_heisenberg_k3(self):
        assert kappa_dual("Heisenberg", k=3) == Fraction(-3)

    def test_kappa_dual_virasoro_c1(self):
        # Vir_c^! = Vir_{26-c}, kappa = (26-1)/2 = 25/2
        assert kappa_dual("Virasoro", c=1) == Fraction(25, 2)

    def test_kappa_dual_virasoro_c25(self):
        assert kappa_dual("Virasoro", c=25) == Fraction(1, 2)

    def test_kappa_dual_virasoro_c13(self):
        # Self-dual: kappa = kappa' = 13/2
        assert kappa_dual("Virasoro", c=13) == Fraction(13, 2)

    def test_complementarity_heisenberg_zero(self):
        # AP24: kappa + kappa' = 0 for Heisenberg
        assert complementarity_sum("Heisenberg", k=1) == Fraction(0)

    def test_complementarity_heisenberg_k5_zero(self):
        assert complementarity_sum("Heisenberg", k=5) == Fraction(0)

    def test_complementarity_affine_sl2_zero(self):
        # AP24: kappa + kappa' = 0 for affine KM
        assert complementarity_sum("Affine_sl2", k=1) == Fraction(0)

    def test_complementarity_virasoro_thirteen(self):
        # AP24 CRITICAL: kappa + kappa' = 13 for Virasoro, NOT 0
        assert complementarity_sum("Virasoro", c=1) == Fraction(13)

    def test_complementarity_virasoro_c13_thirteen(self):
        assert complementarity_sum("Virasoro", c=13) == Fraction(13)

    def test_complementarity_virasoro_c25_thirteen(self):
        assert complementarity_sum("Virasoro", c=25) == Fraction(13)

    def test_complementarity_w3_zero(self):
        assert complementarity_sum("W3", c=2) == Fraction(0)


# ======================================================================
#  Section 3: Shadow depth
# ======================================================================

class TestShadowDepth:
    """Test shadow depth classification G/L/C/M."""

    def test_heisenberg_class_G(self):
        assert SHADOW_CLASS["Heisenberg"] == "G"
        assert shadow_depth("Heisenberg") == 2

    def test_affine_sl2_class_L(self):
        assert SHADOW_CLASS["Affine_sl2"] == "L"
        assert shadow_depth("Affine_sl2") == 3

    def test_betagamma_class_C(self):
        assert SHADOW_CLASS["BetaGamma"] == "C"
        assert shadow_depth("BetaGamma") == 4

    def test_virasoro_class_M(self):
        assert SHADOW_CLASS["Virasoro"] == "M"
        assert shadow_depth("Virasoro") is None  # infinity

    def test_w3_class_M(self):
        assert SHADOW_CLASS["W3"] == "M"
        assert shadow_depth("W3") is None  # infinity


# ======================================================================
#  Section 4: K_0 rank — 3 independent paths
# ======================================================================

class TestK0Rank:
    """K_0 rank via 3 independent computation paths."""

    # Path 1: Direct computation
    def test_k0_heisenberg_rank_1(self):
        assert k0_rank("Heisenberg") == 1

    def test_k0_affine_sl2_k1_rank_2(self):
        assert k0_rank("Affine_sl2", k=1) == 2

    def test_k0_affine_sl2_k2_rank_3(self):
        assert k0_rank("Affine_sl2", k=2) == 3

    def test_k0_affine_sl2_k10_rank_11(self):
        assert k0_rank("Affine_sl2", k=10) == 11

    def test_k0_virasoro_infinite(self):
        assert k0_rank("Virasoro") is None

    def test_k0_w3_infinite(self):
        assert k0_rank("W3") is None

    # Path 2: Via representation counting (independent)
    def test_k0_heisenberg_rep_counting(self):
        assert k0_rank_via_representation_counting("Heisenberg") == 1

    def test_k0_affine_sl2_k1_rep_counting(self):
        assert k0_rank_via_representation_counting("Affine_sl2", k=1) == 2

    def test_k0_affine_sl2_k5_rep_counting(self):
        assert k0_rank_via_representation_counting("Affine_sl2", k=5) == 6

    def test_k0_virasoro_rep_counting_infinite(self):
        assert k0_rank_via_representation_counting("Virasoro") is None

    # Path 3: Via fusion ring (independent)
    def test_k0_heisenberg_fusion_ring(self):
        assert k0_rank_via_fusion_ring("Heisenberg") == 1

    def test_k0_affine_sl2_k1_fusion_ring(self):
        assert k0_rank_via_fusion_ring("Affine_sl2", k=1) == 2

    def test_k0_affine_sl2_k3_fusion_ring(self):
        assert k0_rank_via_fusion_ring("Affine_sl2", k=3) == 4

    def test_k0_virasoro_fusion_ring_infinite(self):
        assert k0_rank_via_fusion_ring("Virasoro") is None

    # Cross-path agreement
    def test_three_paths_agree_heisenberg(self):
        r1 = k0_rank("Heisenberg")
        r2 = k0_rank_via_representation_counting("Heisenberg")
        r3 = k0_rank_via_fusion_ring("Heisenberg")
        assert r1 == r2 == r3

    def test_three_paths_agree_affine_sl2_k1(self):
        r1 = k0_rank("Affine_sl2", k=1)
        r2 = k0_rank_via_representation_counting("Affine_sl2", k=1)
        r3 = k0_rank_via_fusion_ring("Affine_sl2", k=1)
        assert r1 == r2 == r3

    def test_three_paths_agree_affine_sl2_k7(self):
        r1 = k0_rank("Affine_sl2", k=7)
        r2 = k0_rank_via_representation_counting("Affine_sl2", k=7)
        r3 = k0_rank_via_fusion_ring("Affine_sl2", k=7)
        assert r1 == r2 == r3 == 8

    def test_three_paths_agree_virasoro(self):
        r1 = k0_rank("Virasoro")
        r2 = k0_rank_via_representation_counting("Virasoro")
        r3 = k0_rank_via_fusion_ring("Virasoro")
        assert r1 == r2 == r3 is None


class TestK0Data:
    """Test K_0 data structure."""

    def test_k0_data_heisenberg(self):
        data = k0_data("Heisenberg")
        assert data.family == "Heisenberg"
        assert data.rank == 1
        assert data.is_finite_rank is True
        assert "Fock" in data.generators

    def test_k0_data_affine_sl2_k2(self):
        data = k0_data("Affine_sl2", k=2)
        assert data.rank == 3
        assert data.is_finite_rank is True
        assert len(data.generators) == 3

    def test_k0_data_virasoro(self):
        data = k0_data("Virasoro")
        assert data.rank is None
        assert data.is_finite_rank is False


# ======================================================================
#  Section 5: Shadow K_1
# ======================================================================

class TestShadowK1:
    """Shadow K_1 rank and monodromy."""

    def test_k1_heisenberg_zero(self):
        assert shadow_k1_rank("Heisenberg") == 0

    def test_k1_affine_sl2_zero(self):
        assert shadow_k1_rank("Affine_sl2") == 0

    def test_k1_virasoro_one(self):
        assert shadow_k1_rank("Virasoro") == 1

    def test_k1_w3_two(self):
        assert shadow_k1_rank("W3") == 2

    def test_monodromy_heisenberg_trivial(self):
        assert shadow_k1_monodromy("Heisenberg") == 1

    def test_monodromy_affine_trivial(self):
        assert shadow_k1_monodromy("Affine_sl2") == 1

    def test_monodromy_virasoro_koszul_sign(self):
        # Koszul sign monodromy: exp(2*pi*i * 1/2) = -1, order 2
        assert shadow_k1_monodromy("Virasoro") == 2

    def test_monodromy_w3_koszul_sign(self):
        assert shadow_k1_monodromy("W3") == 2

    def test_finite_depth_implies_k1_zero(self):
        """For all finite-depth classes, K_1^{sh} = 0."""
        for fam in ["Heisenberg", "Affine_sl2"]:
            assert shadow_k1_rank(fam) == 0


# ======================================================================
#  Section 6: Hochschild homology
# ======================================================================

class TestHochschildHomology:
    """HH_n(B(A)) dimensions via two independent paths."""

    # Direct computation (path 1)
    def test_hh_heisenberg_degree0(self):
        assert hh_dimension("Heisenberg", 0) == 1

    def test_hh_heisenberg_degree1(self):
        assert hh_dimension("Heisenberg", 1) == 1

    def test_hh_heisenberg_degree2(self):
        assert hh_dimension("Heisenberg", 2) == 1

    def test_hh_heisenberg_degree3_vanishes(self):
        # Quadratic algebra: HH concentrates in {0,1,2}
        assert hh_dimension("Heisenberg", 3) == 0

    def test_hh_heisenberg_degree5_vanishes(self):
        assert hh_dimension("Heisenberg", 5) == 0

    def test_hh_affine_sl2_degree0(self):
        assert hh_dimension("Affine_sl2", 0) == 1

    def test_hh_affine_sl2_degree1(self):
        # dim(sl_2) = 3
        assert hh_dimension("Affine_sl2", 1) == 3

    def test_hh_affine_sl2_degree2(self):
        assert hh_dimension("Affine_sl2", 2) == 1

    def test_hh_affine_sl2_degree3_vanishes(self):
        assert hh_dimension("Affine_sl2", 3) == 0

    def test_hh_virasoro_degree0(self):
        assert hh_dimension("Virasoro", 0) == 1

    def test_hh_virasoro_degree1(self):
        assert hh_dimension("Virasoro", 1) == 1

    def test_hh_virasoro_degree2(self):
        assert hh_dimension("Virasoro", 2) == 1

    def test_hh_virasoro_degree3(self):
        # Non-quadratic: higher HH nontrivial
        assert hh_dimension("Virasoro", 3) == 1

    def test_hh_w3_degree0(self):
        assert hh_dimension("W3", 0) == 1

    def test_hh_w3_degree1(self):
        assert hh_dimension("W3", 1) == 2  # two generators

    def test_hh_w3_degree2(self):
        assert hh_dimension("W3", 2) == 2

    def test_hh_negative_degree_zero(self):
        assert hh_dimension("Heisenberg", -1) == 0

    # Bar complex path (path 2): must agree with direct computation
    def test_hh_bar_vs_direct_heisenberg(self):
        for n in range(6):
            assert hh_from_bar_complex("Heisenberg", n) == hh_dimension("Heisenberg", n)

    def test_hh_bar_vs_direct_affine_sl2(self):
        for n in range(6):
            assert hh_from_bar_complex("Affine_sl2", n) == hh_dimension("Affine_sl2", n)

    def test_hh_bar_vs_direct_virasoro(self):
        for n in range(6):
            assert hh_from_bar_complex("Virasoro", n) == hh_dimension("Virasoro", n)

    def test_hh_bar_vs_direct_w3(self):
        for n in range(6):
            assert hh_from_bar_complex("W3", n) == hh_dimension("W3", n)


class TestHHEulerCharacteristic:
    """Euler characteristic of HH_*."""

    def test_euler_heisenberg(self):
        # chi = 1 - 1 + 1 = 1
        chi = hh_euler_characteristic("Heisenberg")
        assert chi == 1

    def test_euler_affine_sl2(self):
        # chi = 1 - 3 + 1 = -1
        chi = hh_euler_characteristic("Affine_sl2")
        assert chi == -1

    def test_euler_virasoro(self):
        chi = hh_euler_characteristic("Virasoro")
        # 1 - 1 + 1 - 1 + 1 - 1 + 0 = 0
        assert chi == 0

    def test_euler_w3(self):
        chi = hh_euler_characteristic("W3")
        # 1 - 2 + 2 - 2 + 2 - 2 + 0 = -1
        assert chi == -1


# ======================================================================
#  Section 7: Cyclic homology
# ======================================================================

class TestCyclicHomology:
    """HC_n and SBI sequence consistency."""

    def test_hc0_equals_hh0_heisenberg(self):
        assert cyclic_homology_dimension("Heisenberg", 0) == hh_dimension("Heisenberg", 0)

    def test_hc0_equals_hh0_virasoro(self):
        assert cyclic_homology_dimension("Virasoro", 0) == hh_dimension("Virasoro", 0)

    def test_hc1_heisenberg(self):
        assert cyclic_homology_dimension("Heisenberg", 1) == 1

    def test_hc2_heisenberg(self):
        assert cyclic_homology_dimension("Heisenberg", 2) == 1

    def test_hc3_heisenberg_periodic(self):
        # HC_3 = HC_1 (S-periodicity, since HH_3 = 0)
        assert cyclic_homology_dimension("Heisenberg", 3) == cyclic_homology_dimension("Heisenberg", 1)

    def test_hc4_heisenberg_periodic(self):
        # HC_4 = HC_2 (S-periodicity)
        assert cyclic_homology_dimension("Heisenberg", 4) == cyclic_homology_dimension("Heisenberg", 2)

    def test_hc_negative_degree_zero(self):
        assert cyclic_homology_dimension("Heisenberg", -1) == 0

    def test_hc2_virasoro(self):
        assert cyclic_homology_dimension("Virasoro", 2) == 1

    def test_hc_virasoro_grows(self):
        # For Virasoro (class M): HC_n grows due to persistent HH contributions
        hc4 = cyclic_homology_dimension("Virasoro", 4)
        hc2 = cyclic_homology_dimension("Virasoro", 2)
        assert hc4 >= hc2


# ======================================================================
#  Section 8: Shadow period pairing — recovers kappa
# ======================================================================

class TestShadowPeriod:
    """Shadow period <HC_2, Theta_A> = kappa(A)."""

    def test_period_heisenberg_k1(self):
        assert shadow_period("Heisenberg", k=1) == Fraction(1)

    def test_period_heisenberg_k5(self):
        assert shadow_period("Heisenberg", k=5) == Fraction(5)

    def test_period_virasoro_c1(self):
        assert shadow_period("Virasoro", c=1) == Fraction(1, 2)

    def test_period_virasoro_c13(self):
        assert shadow_period("Virasoro", c=13) == Fraction(13, 2)

    def test_period_virasoro_c25(self):
        assert shadow_period("Virasoro", c=25) == Fraction(25, 2)

    def test_period_affine_sl2_k1(self):
        assert shadow_period("Affine_sl2", k=1) == Fraction(9, 4)

    def test_period_w3_c2(self):
        assert shadow_period("W3", c=2) == Fraction(5, 3)

    def test_period_equals_kappa_all_families(self):
        """Verification: shadow period = kappa for ALL families."""
        for fam in FAMILIES:
            if fam == "Heisenberg":
                sp = shadow_period(fam, k=3)
                kap = kappa(fam, k=3)
            elif fam == "Affine_sl2":
                sp = shadow_period(fam, k=2)
                kap = kappa(fam, k=2)
            elif fam == "Virasoro":
                sp = shadow_period(fam, c=10)
                kap = kappa(fam, c=10)
            elif fam == "W3":
                sp = shadow_period(fam, c=4)
                kap = kappa(fam, c=4)
            else:
                continue
            assert sp == kap, f"Period != kappa for {fam}: {sp} != {kap}"

    def test_period_numerical_virasoro_range(self):
        """Verify shadow period = kappa for Virasoro c = 1..25."""
        for c_val in range(1, 26):
            sp = shadow_period_numerical("Virasoro", c=c_val)
            kap_val = float(kappa("Virasoro", c=c_val))
            assert abs(sp - kap_val) < 1e-12, f"c={c_val}: {sp} != {kap_val}"


# ======================================================================
#  Section 9: NC Chern character
# ======================================================================

class TestNCChernCharacter:
    """NC Chern character ch: K_0 -> HH_0."""

    def test_chern_heisenberg_fock(self):
        data = nc_chern_character_heisenberg()
        assert data.chern_values["Fock"] == Fraction(1)

    def test_chern_sl2_k1(self):
        data = nc_chern_character_sl2(1)
        # V(0) has dim 1, V(1) has dim 2
        assert data.chern_values["V(0)"] == Fraction(1)
        assert data.chern_values["V(1)"] == Fraction(2)

    def test_chern_sl2_k2(self):
        data = nc_chern_character_sl2(2)
        assert data.chern_values["V(0)"] == Fraction(1)
        assert data.chern_values["V(1)"] == Fraction(2)
        assert data.chern_values["V(2)"] == Fraction(3)

    def test_chern_sl2_k5(self):
        data = nc_chern_character_sl2(5)
        for j in range(6):
            assert data.chern_values[f"V({j})"] == Fraction(j + 1)

    def test_chern_sl2_k10(self):
        data = nc_chern_character_sl2(10)
        assert len(data.chern_values) == 11
        for j in range(11):
            assert data.chern_values[f"V({j})"] == Fraction(j + 1)

    def test_chern_additivity_k1(self):
        assert verify_chern_character_additivity(1) is True

    def test_chern_additivity_k5(self):
        assert verify_chern_character_additivity(5) is True

    def test_chern_total_dimension_k1(self):
        # sum_{j=0}^1 (j+1) = 1 + 2 = 3
        assert chern_total_dimension(1) == Fraction(3)

    def test_chern_total_dimension_k5(self):
        # sum_{j=0}^5 (j+1) = 1+2+3+4+5+6 = 21
        assert chern_total_dimension(5) == Fraction(21)

    def test_chern_total_dimension_formula(self):
        """Total Chern mass = (k+1)(k+2)/2."""
        for k in range(1, 11):
            expected = Fraction((k + 1) * (k + 2), 2)
            assert chern_total_dimension(k) == expected


# ======================================================================
#  Section 10: NC zeta function
# ======================================================================

class TestNCZeta:
    """NC zeta function and comparison with categorical zeta."""

    def test_nc_zeta_heisenberg(self):
        assert nc_zeta_heisenberg(2.0) == 1.0

    def test_nc_zeta_heisenberg_any_s(self):
        # 1^{-s} = 1 for all s
        for s in [0.5, 1.0, 2.0, 3.0, 10.0]:
            assert abs(nc_zeta_heisenberg(s) - 1.0) < 1e-14

    def test_nc_zeta_sl2_k1_s2(self):
        # sum_{d=1}^{2} d^{-2} = 1 + 1/4 = 5/4
        val = nc_zeta_sl2(2.0, 1)
        assert abs(val - 1.25) < 1e-12

    def test_nc_zeta_sl2_k2_s2(self):
        # sum_{d=1}^{3} d^{-2} = 1 + 1/4 + 1/9 = 49/36
        val = nc_zeta_sl2(2.0, 2)
        assert abs(val - 49.0 / 36.0) < 1e-12

    def test_nc_zeta_sl2_k0(self):
        # k=0: only V(0) with dim 1. zeta = 1^{-s} = 1
        val = nc_zeta_sl2(2.0, 0)
        assert abs(val - 1.0) < 1e-12

    def test_nc_zeta_equals_partial_riemann(self):
        """NC zeta at level k = partial Riemann zeta sum to k+1 terms."""
        comp = nc_zeta_categorical_comparison_sl2(2.0, 10)
        assert comp["nc_equals_partial"] is True

    def test_nc_zeta_approaches_riemann_large_k(self):
        """As k -> inf, NC zeta -> Riemann zeta."""
        comp = nc_zeta_categorical_comparison_sl2(2.0, 200)
        # pi^2/6 ~ 1.6449...
        assert comp["ratio_to_full"] > 0.99

    def test_nc_zeta_sl2_k100_s3(self):
        """NC zeta at k=100 should be close to zeta(3) = Apery's constant."""
        val = nc_zeta_sl2(3.0, 100).real
        # zeta(3) ~ 1.2020569...
        # Partial sum to 101 terms is very close
        assert abs(val - 1.2020569) < 0.001

    def test_nc_zeta_sl2_large_s_convergence(self):
        """For large s, zeta = 1 + small corrections."""
        val = nc_zeta_sl2(10.0, 5).real
        # 1 + 2^{-10} + 3^{-10} + ... ~ 1 + 0.001 + ...
        assert abs(val - 1.0) < 0.002


# ======================================================================
#  Section 11: Shadow coefficients and motivic measure
# ======================================================================

class TestShadowCoefficients:
    """Shadow coefficients S_r(A)."""

    def test_heisenberg_s2(self):
        coeffs = shadow_coefficients("Heisenberg", k=Fraction(3))
        assert coeffs[2] == Fraction(3)

    def test_heisenberg_sr_zero_for_r_geq_3(self):
        coeffs = shadow_coefficients("Heisenberg", k=Fraction(1))
        for r in range(3, 11):
            assert coeffs[r] == Fraction(0)

    def test_affine_sl2_s2(self):
        coeffs = shadow_coefficients("Affine_sl2", k=Fraction(1))
        assert coeffs[2] == Fraction(9, 4)

    def test_affine_sl2_s3(self):
        coeffs = shadow_coefficients("Affine_sl2", k=Fraction(1))
        # alpha = 4/(k+2) = 4/3
        assert coeffs[3] == Fraction(4, 3)

    def test_affine_sl2_sr_zero_for_r_geq_4(self):
        coeffs = shadow_coefficients("Affine_sl2", k=Fraction(1))
        for r in range(4, 11):
            assert coeffs[r] == Fraction(0)

    def test_virasoro_s2(self):
        coeffs = shadow_coefficients("Virasoro", c=Fraction(10))
        assert coeffs[2] == Fraction(5)

    def test_virasoro_s3(self):
        coeffs = shadow_coefficients("Virasoro", c=Fraction(10))
        assert coeffs[3] == Fraction(6)

    def test_virasoro_s4_q_contact(self):
        """Q^contact_Vir = 10 / (c * (5c + 22))."""
        c_val = Fraction(10)
        coeffs = shadow_coefficients("Virasoro", c=c_val)
        expected = Fraction(10) / (c_val * (5 * c_val + 22))
        assert coeffs[4] == expected


class TestMotivicMeasure:
    """Motivic measure mu_A evaluation."""

    def test_motivic_measure_heisenberg_at_one(self):
        # mu(1) = S_2 = kappa for Heisenberg
        val = motivic_measure_at_one("Heisenberg", k=Fraction(3))
        assert val == Fraction(3)

    def test_motivic_measure_affine_at_one(self):
        # mu(1) = kappa + alpha for affine sl_2
        val = motivic_measure_at_one("Affine_sl2", k=Fraction(1))
        expected = Fraction(9, 4) + Fraction(4, 3)  # 27/12 + 16/12 = 43/12
        assert val == expected

    def test_motivic_measure_at_zero(self):
        # mu(0) = 0 (all terms vanish since L^r = 0 for r >= 2 and L=0)
        val = motivic_measure_evaluate("Heisenberg", Fraction(0), k=Fraction(5))
        assert val == Fraction(0)

    def test_motivic_measure_heisenberg_at_L(self):
        # mu(L) = kappa * L^2 for Heisenberg (only S_2 nonzero)
        L = Fraction(2)
        val = motivic_measure_evaluate("Heisenberg", L, k=Fraction(3))
        assert val == Fraction(3) * L ** 2  # 3 * 4 = 12

    def test_motivic_measure_additivity(self):
        """mu_{H_{k1} + H_{k2}}(1) = mu_{H_{k1}}(1) + mu_{H_{k2}}(1)."""
        k1, k2 = Fraction(2), Fraction(3)
        m1 = motivic_measure_at_one("Heisenberg", k=k1)
        m2 = motivic_measure_at_one("Heisenberg", k=k2)
        m_sum = motivic_measure_at_one("Heisenberg", k=k1 + k2)
        assert m1 + m2 == m_sum


# ======================================================================
#  Section 12: Derived Morita invariance
# ======================================================================

class TestMoritaInvariance:
    """Derived Morita invariance for Koszul dual pairs."""

    def test_morita_virasoro_c1(self):
        data = morita_comparison_virasoro(Fraction(1))
        assert data.k0_isomorphic is True
        assert data.hh_isomorphic is True

    def test_morita_virasoro_c13_self_dual(self):
        data = morita_comparison_virasoro(Fraction(13))
        assert data.k0_isomorphic is True
        assert data.hh_isomorphic is True

    def test_morita_virasoro_c25(self):
        data = morita_comparison_virasoro(Fraction(25))
        assert data.k0_isomorphic is True
        assert data.hh_isomorphic is True

    def test_morita_affine_sl2_k1(self):
        data = morita_comparison_affine_sl2(1)
        assert data.k0_isomorphic is True
        assert data.hh_isomorphic is True

    def test_morita_affine_sl2_k3(self):
        data = morita_comparison_affine_sl2(3)
        assert data.k0_isomorphic is True

    def test_morita_virasoro_both_infinite_k0(self):
        """Both Vir_c and Vir_{26-c} have infinite K_0."""
        data = morita_comparison_virasoro(Fraction(5))
        assert data.k0_rank_A is None
        assert data.k0_rank_A_dual is None


# ======================================================================
#  Section 13: Cross-family consistency
# ======================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks with multi-path verification."""

    def test_kappa_additivity_heisenberg(self):
        assert verify_kappa_additivity(Fraction(2), Fraction(3)) is True

    def test_kappa_additivity_heisenberg_half_int(self):
        assert verify_kappa_additivity(Fraction(1, 2), Fraction(3, 2)) is True

    def test_complementarity_check_all_families(self):
        """Complementarity sum check for all standard families."""
        # Heisenberg: 0
        result = verify_complementarity_sum("Heisenberg", k=1)
        assert result["match"] is True
        assert result["sum"] == Fraction(0)

        # Affine sl_2: 0
        result = verify_complementarity_sum("Affine_sl2", k=1)
        assert result["match"] is True
        assert result["sum"] == Fraction(0)

        # Virasoro: 13 (AP24)
        result = verify_complementarity_sum("Virasoro", c=1)
        assert result["match"] is True
        assert result["sum"] == Fraction(13)

        # W_3: 0
        result = verify_complementarity_sum("W3", c=2)
        assert result["match"] is True
        assert result["sum"] == Fraction(0)

    def test_k0_koszul_duality_heisenberg(self):
        assert verify_k0_koszul_duality("Heisenberg", k=Fraction(1)) is True

    def test_k0_koszul_duality_affine_sl2(self):
        assert verify_k0_koszul_duality("Affine_sl2", k=1) is True

    def test_k0_koszul_duality_virasoro(self):
        assert verify_k0_koszul_duality("Virasoro", c=10) is True

    def test_k0_koszul_duality_virasoro_c13(self):
        assert verify_k0_koszul_duality("Virasoro", c=13) is True


# ======================================================================
#  Section 14: Full NC motivic package
# ======================================================================

class TestFullPackage:
    """Integration tests for the full NC motivic package."""

    def test_package_heisenberg(self):
        pkg = full_nc_motivic_package("Heisenberg", k=1)
        assert pkg.family == "Heisenberg"
        assert pkg.kappa_val == Fraction(1)
        assert pkg.kappa_dual_val == Fraction(-1)
        assert pkg.complementarity == Fraction(0)
        assert pkg.k0_rank_val == 1
        assert pkg.k0_is_finite is True
        assert pkg.shadow_k1 == 0
        assert pkg.shadow_monodromy == 1
        assert pkg.shadow_class_val == "G"
        assert pkg.shadow_depth_val == 2
        assert pkg.shadow_period_val == Fraction(1)
        assert pkg.chern_data is not None

    def test_package_affine_sl2(self):
        pkg = full_nc_motivic_package("Affine_sl2", k=2)
        assert pkg.kappa_val == Fraction(3)
        assert pkg.k0_rank_val == 3
        assert pkg.shadow_k1 == 0
        assert pkg.shadow_class_val == "L"
        assert pkg.chern_data is not None
        assert len(pkg.chern_data.chern_values) == 3

    def test_package_virasoro(self):
        pkg = full_nc_motivic_package("Virasoro", c=10)
        assert pkg.kappa_val == Fraction(5)
        assert pkg.kappa_dual_val == Fraction(8)  # (26-10)/2 = 8
        assert pkg.complementarity == Fraction(13)
        assert pkg.k0_rank_val is None
        assert pkg.k0_is_finite is False
        assert pkg.shadow_k1 == 1
        assert pkg.shadow_monodromy == 2
        assert pkg.shadow_class_val == "M"
        assert pkg.shadow_depth_val is None
        assert pkg.chern_data is None  # infinite rank, no Chern data

    def test_package_w3(self):
        pkg = full_nc_motivic_package("W3", c=4)
        assert pkg.kappa_val == Fraction(10, 3)
        assert pkg.shadow_k1 == 2
        assert pkg.shadow_class_val == "M"

    def test_package_hh_dims_heisenberg(self):
        pkg = full_nc_motivic_package("Heisenberg", k=1)
        # HH: [1, 1, 1, 0, 0, 0]
        assert pkg.hh_dims == [1, 1, 1, 0, 0, 0]

    def test_package_hh_dims_affine_sl2(self):
        pkg = full_nc_motivic_package("Affine_sl2", k=1)
        # HH: [1, 3, 1, 0, 0, 0]
        assert pkg.hh_dims == [1, 3, 1, 0, 0, 0]

    def test_package_hc_periodicity_heisenberg(self):
        pkg = full_nc_motivic_package("Heisenberg", k=1)
        # HC: [1, 1, 1, 1, 1, 1] (S-periodic after degree 2)
        assert pkg.hc_dims[0] == 1
        assert pkg.hc_dims[2] == 1
        assert pkg.hc_dims[3] == pkg.hc_dims[1]  # periodicity
        assert pkg.hc_dims[4] == pkg.hc_dims[2]  # periodicity

    def test_package_shadow_period_equals_kappa(self):
        """The shadow period must equal kappa for all packages."""
        for fam, kwargs in [
            ("Heisenberg", {"k": 3}),
            ("Affine_sl2", {"k": 2}),
            ("Virasoro", {"c": 7}),
            ("W3", {"c": 5}),
        ]:
            pkg = full_nc_motivic_package(fam, **kwargs)
            assert pkg.shadow_period_val == pkg.kappa_val


# ======================================================================
#  Section 15: Parametric sweep tests
# ======================================================================

class TestParametricSweeps:
    """Parametric sweeps for robustness."""

    def test_k0_rank_affine_sl2_sweep(self):
        """K_0 rank = k+1 for k = 1..20."""
        for k in range(1, 21):
            assert k0_rank("Affine_sl2", k=k) == k + 1

    def test_kappa_virasoro_sweep(self):
        """kappa = c/2 for c = 1..30."""
        for c_val in range(1, 31):
            assert kappa("Virasoro", c=c_val) == Fraction(c_val, 2)

    def test_complementarity_virasoro_sweep(self):
        """kappa + kappa' = 13 for all c (AP24)."""
        for c_val in range(1, 26):
            assert complementarity_sum("Virasoro", c=c_val) == Fraction(13)

    def test_chern_total_mass_sweep(self):
        """Total Chern mass = (k+1)(k+2)/2 for k = 1..15."""
        for k in range(1, 16):
            assert chern_total_dimension(k) == Fraction((k + 1) * (k + 2), 2)

    def test_nc_zeta_monotone_in_k(self):
        """NC zeta at fixed s > 1 is monotone increasing in k."""
        s = 2.0
        prev = 0.0
        for k in range(0, 20):
            val = nc_zeta_sl2(s, k).real
            assert val >= prev
            prev = val

    def test_shadow_period_virasoro_sweep(self):
        """Shadow period = kappa for Virasoro c = 1..25."""
        for c_val in range(1, 26):
            sp = shadow_period("Virasoro", c=c_val)
            kap = kappa("Virasoro", c=c_val)
            assert sp == kap


# ======================================================================
#  Section 16: Edge cases and error handling
# ======================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_k0_affine_sl2_k0(self):
        """Level 0: single integrable module (vacuum)."""
        assert k0_rank("Affine_sl2", k=0) == 1

    def test_k0_affine_negative_level_raises(self):
        with pytest.raises(ValueError):
            k0_rank("Affine_sl2", k=-1)

    def test_kappa_unknown_raises(self):
        with pytest.raises(ValueError):
            kappa("BadFamily")

    def test_kappa_dual_unknown_raises(self):
        with pytest.raises(ValueError):
            kappa_dual("BadFamily")

    def test_shadow_depth_unknown_raises(self):
        with pytest.raises(ValueError):
            shadow_depth("BadFamily")

    def test_hh_unknown_family_raises(self):
        with pytest.raises(ValueError):
            hh_dimension("BadFamily", 0)

    def test_motivic_measure_virasoro_c_half(self):
        """Motivic measure works for fractional c."""
        val = motivic_measure_at_one("Virasoro", c=Fraction(1, 2))
        assert isinstance(val, Fraction)
