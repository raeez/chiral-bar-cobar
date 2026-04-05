"""GREEN TEAM tests: Alternative approaches to modular factorization adjunction.

Tests five strategies for constructing/bootstrapping toward
U^mod_X ⊣ Prim^mod (thm:platonic-adjunction).

Target: ≥ 25 tests covering all five strategies with verification
on Heisenberg and affine sl_2.
"""

import pytest
from fractions import Fraction

from compute.lib.platonic_green_team import (
    ShadowClass,
    LieConformalAlgebra,
    heisenberg_lca,
    affine_sl2_lca,
    affine_slN_lca,
    virasoro_lca,
    betagamma_lca,
    GenusTowerStrategy,
    KanExtensionStrategy,
    BarCobarResolutionStrategy,
    DeformationStrategy,
    ShadowTowerBootstrap,
    StrategySynthesis,
)


# ========================================================================
# Standard examples: basic sanity
# ========================================================================

class TestLieConformalAlgebras:
    """Verify the standard LCA data."""

    def test_heisenberg_properties(self):
        L = heisenberg_lca()
        assert L.is_abelian()
        assert L.shadow_class == ShadowClass.G
        assert L.r_max == 2
        assert L.rank == 1

    def test_heisenberg_kappa(self):
        """kappa(Heis, k) = k for rank 1."""
        L = heisenberg_lca()
        assert L.kappa(Fraction(1)) == Fraction(1)
        assert L.kappa(Fraction(3)) == Fraction(3)
        assert L.kappa(Fraction(-1, 2)) == Fraction(-1, 2)

    def test_affine_sl2_properties(self):
        L = affine_sl2_lca()
        assert not L.is_abelian()
        assert L.shadow_class == ShadowClass.L
        assert L.r_max == 3
        assert L.rank == 3

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        L = affine_sl2_lca()
        # k=1: kappa = 3*3/4 = 9/4
        assert L.kappa(Fraction(1)) == Fraction(9, 4)
        # k=0: kappa = 3*2/4 = 3/2
        assert L.kappa(Fraction(0)) == Fraction(3, 2)
        # k=2: kappa = 3*4/4 = 3
        assert L.kappa(Fraction(2)) == Fraction(3)

    def test_affine_sl2_central_charge(self):
        """c(sl_2, k) = 3k/(k+2)."""
        L = affine_sl2_lca()
        # k=1: c = 3/3 = 1
        assert L.central_charge(Fraction(1)) == Fraction(1)
        # k=2: c = 6/4 = 3/2
        assert L.central_charge(Fraction(2)) == Fraction(3, 2)

    def test_virasoro_properties(self):
        L = virasoro_lca()
        assert not L.is_abelian()
        assert L.shadow_class == ShadowClass.M
        assert L.r_max is None
        assert L.rank == 1

    def test_virasoro_kappa(self):
        """kappa(Vir, c) = c/2."""
        L = virasoro_lca()
        assert L.kappa(Fraction(26)) == Fraction(13)
        assert L.kappa(Fraction(1)) == Fraction(1, 2)

    def test_betagamma_properties(self):
        L = betagamma_lca()
        assert L.shadow_class == ShadowClass.C
        assert L.r_max == 4


# ========================================================================
# STRATEGY A: Genus tower
# ========================================================================

class TestGenusTowerStrategy:
    """Strategy A: bottom-up genus tower."""

    def test_genus0_exists_heisenberg(self):
        L = heisenberg_lca()
        result = GenusTowerStrategy.genus0_envelope_exists(L)
        assert result['genus0_exists']

    def test_genus0_exists_affine_sl2(self):
        L = affine_sl2_lca()
        result = GenusTowerStrategy.genus0_envelope_exists(L)
        assert result['genus0_exists']

    def test_genus1_correction_heisenberg(self):
        """Genus-1 correction for Heisenberg is κ = k."""
        L = heisenberg_lca()
        result = GenusTowerStrategy.genus1_correction(L, Fraction(3))
        assert result['kappa'] == Fraction(3)
        assert result['genus1_correction'] == Fraction(3)

    def test_genus1_correction_affine_sl2(self):
        """Genus-1 correction for sl_2 at k=1 is κ = 9/4."""
        L = affine_sl2_lca()
        result = GenusTowerStrategy.genus1_correction(L, Fraction(1))
        assert result['kappa'] == Fraction(9, 4)

    def test_genus_tower_convergence_heisenberg(self):
        """Genus tower converges for Heisenberg (HS-sewing holds)."""
        L = heisenberg_lca()
        result = GenusTowerStrategy.genus_tower_converges(L)
        assert result['hs_sewing_holds']
        assert result['genus_tower_converges']
        assert result['constructive']  # class G: finite depth

    def test_genus_tower_convergence_virasoro(self):
        """Genus tower converges for Virasoro but is not constructive."""
        L = virasoro_lca()
        result = GenusTowerStrategy.genus_tower_converges(L)
        assert result['hs_sewing_holds']
        assert result['genus_tower_converges']
        assert not result['constructive']  # class M: infinite depth

    def test_genus_tower_heisenberg_detail(self):
        """Detailed genus tower for Heisenberg at k=2."""
        result = GenusTowerStrategy.genus_tower_heisenberg(Fraction(2))
        assert result['kappa'] == Fraction(2)
        assert result['terminates']
        assert result['shadow_class'] == 'G'
        assert result['genus_corrections'][0] == 0
        assert result['genus_corrections'][1] == Fraction(2)

    def test_genus_tower_affine_sl2_detail(self):
        """Detailed genus tower for sl_2 at k=1."""
        result = GenusTowerStrategy.genus_tower_affine_sl2(Fraction(1))
        assert result['kappa'] == Fraction(9, 4)
        assert result['has_cubic_shadow']
        assert result['quartic_vanishes']
        assert result['terminates_at_arity'] == 3

    def test_rating(self):
        rating = GenusTowerStrategy.rate()
        assert rating['rating'] == 8
        assert len(rating['strengths']) >= 3


# ========================================================================
# STRATEGY B: Operadic left Kan extension
# ========================================================================

class TestKanExtensionStrategy:
    """Strategy B: operadic left Kan extension."""

    def test_classical_milnor_moore_sl2(self):
        """Milnor-Moore for dim-3 Lie algebra."""
        result = KanExtensionStrategy.classical_milnor_moore(3)
        assert result['PBW_dimensions'][0] == 1
        assert result['PBW_dimensions'][1] == 3
        # dim Sym^2(3) = binom(4,2) = 6
        assert result['PBW_dimensions'][2] == 6
        assert result['adjunction_holds']

    def test_kan_genus0_heisenberg(self):
        L = heisenberg_lca()
        result = KanExtensionStrategy.kan_extension_genus0(L)
        assert result['kan_extension_exists']
        assert result['equals_nishinaka']

    def test_kan_modular_obstruction(self):
        """Plain Kan extension does NOT include modular data."""
        result = KanExtensionStrategy.kan_extension_modular_obstruction()
        assert not result['plain_kan_includes_modular']
        assert result['circular']

    def test_verify_heisenberg(self):
        result = KanExtensionStrategy.verify_on_heisenberg(Fraction(1))
        assert result['adjunction_at_genus0']
        assert result['prim_recovers_input']
        assert result['prim_rank'] == 1

    def test_verify_affine_sl2(self):
        result = KanExtensionStrategy.verify_on_affine_sl2(Fraction(1))
        assert result['adjunction_at_genus0']
        assert result['prim_recovers_input']
        assert result['prim_rank'] == 3

    def test_rating(self):
        rating = KanExtensionStrategy.rate()
        assert rating['rating'] == 5
        assert 'circular' in rating['verdict'].lower() or 'circular' in str(rating['weaknesses']).lower()


# ========================================================================
# STRATEGY C: Bar-cobar resolution
# ========================================================================

class TestBarCobarResolutionStrategy:
    """Strategy C: bar-cobar as free resolution."""

    def test_classical_ce_sl2(self):
        """CE coalgebra for dim-3: total dim = 2^3 = 8."""
        result = BarCobarResolutionStrategy.classical_ce_coalgebra(3)
        assert result['total_dim'] == 8
        assert result['CE_dimensions'][0] == 1
        assert result['CE_dimensions'][1] == 3
        assert result['CE_dimensions'][2] == 3
        assert result['CE_dimensions'][3] == 1
        assert result['cobar_gives_U']

    def test_chiral_ce_heisenberg(self):
        """Chiral CE for Heisenberg: trivial differential (abelian)."""
        L = heisenberg_lca()
        result = BarCobarResolutionStrategy.chiral_ce_coalgebra(L)
        assert result['genus0_CE_exists']
        assert result['is_cocommutative']
        assert not result['differential_from_bracket']

    def test_chiral_ce_sl2(self):
        """Chiral CE for sl_2: nontrivial differential from bracket."""
        L = affine_sl2_lca()
        result = BarCobarResolutionStrategy.chiral_ce_coalgebra(L)
        assert result['genus0_CE_exists']
        assert result['is_cocommutative']
        assert result['differential_from_bracket']

    def test_cobar_heisenberg(self):
        """Cobar of CE gives Heisenberg VOA."""
        result = BarCobarResolutionStrategy.cobar_gives_envelope_heisenberg(Fraction(2))
        assert result['correct']
        assert result['kappa_from_cobar'] == 2

    def test_cobar_affine_sl2(self):
        """Cobar of CE gives V_k(sl_2)."""
        result = BarCobarResolutionStrategy.cobar_gives_envelope_sl2(Fraction(1))
        assert result['correct']
        assert result['koszul_holds']
        assert result['kappa'] == Fraction(9, 4)

    def test_modular_extension_not_circular(self):
        """Modular extension via B_ch ⊗̂ G_mod is NOT circular."""
        result = BarCobarResolutionStrategy.modular_extension_analysis()
        assert not result['circular']
        assert result['gives_adjunction']

    def test_rating_highest(self):
        """Strategy C should be rated highest."""
        rating = BarCobarResolutionStrategy.rate()
        assert rating['rating'] == 9
        # Check it is the highest among all strategies
        all_ratings = StrategySynthesis.compare_all()
        assert all_ratings[0]['strategy'] == 'C: Bar-cobar as free resolution'


# ========================================================================
# STRATEGY D: Deformation-theoretic construction
# ========================================================================

class TestDeformationStrategy:
    """Strategy D: deformation-theoretic construction."""

    def test_free_va_dimensions(self):
        """Free VA has exponential growth."""
        result = DeformationStrategy.free_va_dimensions(3, 4)
        assert result['free_dimensions'][0] == 1
        assert result['free_dimensions'][1] == 3
        assert result['free_dimensions'][2] == 9
        assert result['free_dimensions'][3] == 27
        assert result['free_dimensions'][4] == 81
        assert 'exponential' in result['growth']

    def test_mc_quotient_heisenberg(self):
        result = DeformationStrategy.verify_on_heisenberg(Fraction(1))
        assert result['correct']
        assert result['genus0_correct']
        assert result['curvature'] == 1

    def test_mc_quotient_sl2(self):
        result = DeformationStrategy.verify_on_affine_sl2(Fraction(1))
        assert result['correct']
        assert result['kappa'] == Fraction(9, 4)

    def test_mc_quotient_analysis(self):
        L = affine_sl2_lca()
        result = DeformationStrategy.mc_quotient_analysis(L)
        assert result['mc_genus0_gives_nishinaka']
        assert result['well_defined']

    def test_rating(self):
        rating = DeformationStrategy.rate()
        assert rating['rating'] == 6


# ========================================================================
# STRATEGY E: Shadow-tower bootstrap
# ========================================================================

class TestShadowTowerBootstrap:
    """Strategy E: shadow-tower bootstrap."""

    def test_truncated_envelope_heisenberg_at_2(self):
        """Heisenberg: U^{≤2} is complete (class G)."""
        L = heisenberg_lca()
        result = ShadowTowerBootstrap.truncated_envelope(L, 2)
        assert result['is_complete']
        assert 'κ' in result['shadow_components'][0]

    def test_truncated_envelope_sl2_at_2(self):
        """sl_2: U^{≤2} is NOT complete (class L, needs r=3)."""
        L = affine_sl2_lca()
        result = ShadowTowerBootstrap.truncated_envelope(L, 2)
        assert not result['is_complete']

    def test_truncated_envelope_sl2_at_3(self):
        """sl_2: U^{≤3} IS complete (class L)."""
        L = affine_sl2_lca()
        result = ShadowTowerBootstrap.truncated_envelope(L, 3)
        assert result['is_complete']

    def test_truncated_envelope_virasoro_at_any(self):
        """Virasoro: U^{≤r} is never complete (class M)."""
        L = virasoro_lca()
        for r in [2, 5, 10, 100]:
            result = ShadowTowerBootstrap.truncated_envelope(L, r)
            assert not result['is_complete']

    def test_finite_termination_classes(self):
        """Verify the three finite-depth classes."""
        classes = ShadowTowerBootstrap.finite_termination_classes()
        assert classes['G']['r_max'] == 2
        assert classes['G']['termination']
        assert classes['L']['r_max'] == 3
        assert classes['L']['termination']
        assert classes['C']['r_max'] == 4
        assert classes['C']['termination']
        assert not classes['M']['termination']

    def test_inverse_limit_exists(self):
        """Inverse limit exists for class M."""
        result = ShadowTowerBootstrap.inverse_limit_exists()
        assert result['inverse_limit_exists']
        assert result['ML_automatic']

    def test_bootstrap_heisenberg(self):
        result = ShadowTowerBootstrap.bootstrap_heisenberg(Fraction(5))
        assert result['terminates']
        assert result['r_max'] == 2
        assert result['equals_full']

    def test_bootstrap_affine_sl2(self):
        result = ShadowTowerBootstrap.bootstrap_affine_sl2(Fraction(1))
        assert result['terminates']
        assert result['r_max'] == 3
        assert result['kappa'] == Fraction(9, 4)

    def test_bootstrap_virasoro_does_not_terminate(self):
        result = ShadowTowerBootstrap.bootstrap_virasoro(Fraction(26))
        assert not result['terminates']
        assert result['kappa'] == Fraction(13)
        assert result['Q_contact'] is not None

    def test_virasoro_quartic_contact_value(self):
        """Q^contact_Vir(c=1) = 10/(1*27) = 10/27."""
        result = ShadowTowerBootstrap.bootstrap_virasoro(Fraction(1))
        assert result['Q_contact'] == Fraction(10, 27)

    def test_rating(self):
        rating = ShadowTowerBootstrap.rate()
        assert rating['rating'] == 7


# ========================================================================
# Strategy synthesis
# ========================================================================

class TestStrategySynthesis:
    """Compare and synthesize strategies."""

    def test_compare_all_ordering(self):
        """Strategies should be ordered by rating."""
        rankings = StrategySynthesis.compare_all()
        assert len(rankings) == 5
        # Check descending order
        for i in range(len(rankings) - 1):
            assert rankings[i]['rating'] >= rankings[i + 1]['rating']

    def test_best_strategy_C(self):
        """Strategy C should be rated highest overall."""
        rankings = StrategySynthesis.compare_all()
        assert rankings[0]['strategy'] == 'C: Bar-cobar as free resolution'
        assert rankings[0]['rating'] == 9

    def test_best_by_class(self):
        """Verify best strategy recommendations per class."""
        best = StrategySynthesis.best_strategy_by_class()
        assert 'E' in best['G']['best']  # Shadow bootstrap for Gaussian
        assert 'C' in best['M']['best']  # Bar-cobar for Mixed

    def test_combined_strategy(self):
        combined = StrategySynthesis.combined_strategy()
        assert 'C' in combined['foundation']
        assert 'E' in combined['constructive_supplement']
        assert 'A' in combined['analytic_supplement']

    def test_adjunction_unit_heisenberg(self):
        L = heisenberg_lca()
        result = StrategySynthesis.adjunction_unit_analysis(L, Fraction(1))
        assert result['unit_is_LCA_map']
        assert result['unit_preserves_pairing']
        assert result['unit_image_equals_prim']

    def test_adjunction_counit_sl2(self):
        L = affine_sl2_lca()
        result = StrategySynthesis.adjunction_counit_analysis(L, Fraction(1))
        assert result['counit_is_fact_map']
        assert result['triangle_identity_1']
        assert result['triangle_identity_2']

    def test_independence_heisenberg_pair(self):
        """Independent sum: Heis_k1 ⊕ Heis_k2 has additive κ."""
        L1 = heisenberg_lca()
        L2 = heisenberg_lca()
        result = StrategySynthesis.independence_check(
            L1, L2, Fraction(3), Fraction(5)
        )
        assert result['kappa_sum'] == Fraction(8)  # 3 + 5
        assert result['kappa_additive']
        assert result['left_adjoint_preserves_coproduct']

    def test_independence_heisenberg_sl2(self):
        """Independent sum: Heis_k ⊕ sl_2_k has additive κ."""
        L1 = heisenberg_lca()
        L2 = affine_sl2_lca()
        result = StrategySynthesis.independence_check(
            L1, L2, Fraction(1), Fraction(1)
        )
        # kappa_1 = 1 (Heisenberg at k=1), kappa_2 = 9/4 (sl_2 at k=1)
        assert result['kappa_sum'] == Fraction(1) + Fraction(9, 4)
        assert result['kappa_sum'] == Fraction(13, 4)
        assert result['kappa_additive']

    def test_affine_slN_kappa_additivity(self):
        """kappa(sl_N, k) = (N^2-1)(k+N)/(2N) for several N."""
        for N in [2, 3, 4, 5]:
            L = affine_slN_lca(N)
            k = Fraction(1)
            kappa = L.kappa(k)
            expected = Fraction(N * N - 1) * (k + N) / (2 * N)
            assert kappa == expected, f"kappa(sl_{N}, k=1) = {kappa} != {expected}"
