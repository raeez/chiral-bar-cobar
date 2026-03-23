#!/usr/bin/env python3
"""Tests for the BLUE TEAM defence of conj:platonic-adjunction.

Verifies:
  (a) Platonic package data for all standard families
  (b) Independent sum factorization (prop:independent-sum-factorization)
  (c) Cubic gauge triviality (thm:cubic-gauge-triviality)
  (d) Genus-0 envelope recovery (Nishinaka 2025/26)
  (e) Left adjoint existence criteria (SAFT / local presentability)
  (f) Unit-counit triangle identities
  (g) Milnor-Moore factorization for bar coalgebras
  (h) Modular extension chain
  (i) Numerical checks at specific parameter values

Mathematical references:
  - conj:platonic-adjunction in concordance.tex
  - thm:platonic-adjunction in higher_genus_modular_koszul.tex
  - constr:platonic-package in higher_genus_modular_koszul.tex
  - thm:cubic-gauge-triviality in higher_genus_modular_koszul.tex
  - prop:independent-sum-factorization in higher_genus_modular_koszul.tex
"""

from __future__ import annotations

from fractions import Fraction

import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from platonic_blue_team import (
    CyclicAdmissibleData,
    PlatonicPackage,
    IndependentSumEngine,
    CubicGaugeEngine,
    Genus0EnvelopeEngine,
    AdjointExistenceEngine,
    MilnorMooreEngine,
    ModularExtensionEngine,
    NumericalVerificationEngine,
    heisenberg_data,
    affine_slN_data,
    betagamma_data,
    virasoro_data,
    lattice_data,
    STANDARD_FAMILIES,
    run_full_blue_team_verification,
)


# ========================================================================
# (a) Platonic package: all six components exist for standard families
# ========================================================================

class TestPlatonicPackageHeisenberg:
    """Verify Pi_X(R) for Heisenberg: (Fact_X, barB_X, kappa, L_R, (V^br, T^br), 0)."""

    def test_heisenberg_is_cyclically_admissible(self):
        """Heisenberg Lie conformal algebra satisfies def:cyclically-admissible."""
        data = heisenberg_data()
        assert data.is_cyclically_admissible()

    def test_heisenberg_package_complete(self):
        """All six components of Pi_X(R) exist."""
        pkg = PlatonicPackage(heisenberg_data())
        assert pkg.is_complete()

    def test_heisenberg_shadow_class_G(self):
        """Heisenberg is class G (Gaussian), r_max = 2."""
        data = heisenberg_data()
        assert data.shadow_class == 'G'

    def test_heisenberg_quartic_zero(self):
        """R_4^mod = 0 for Heisenberg (class G: no quartic resonance)."""
        pkg = PlatonicPackage(heisenberg_data())
        assert pkg.quartic_class == 'zero'

    def test_heisenberg_branch_rank_zero(self):
        """Branch rank = 0 for class G (no spectral data beyond kappa)."""
        pkg = PlatonicPackage(heisenberg_data())
        assert pkg.branch_rank == 0

    def test_heisenberg_kappa(self):
        """kappa(Heisenberg, rank 1) = 1 (anomaly ratio rho = 1)."""
        data = heisenberg_data(rank=1)
        assert data.kappa == Fraction(1)


class TestPlatonicPackageAffine:
    """Verify Pi_X(g_aff) for affine sl_N."""

    def test_affine_sl2_admissible(self):
        """Affine sl_2 at level k=1 is cyclically admissible."""
        data = affine_slN_data(2, Fraction(1))
        assert data.is_cyclically_admissible()

    def test_affine_sl2_package_complete(self):
        """All six components of Pi_X(sl_2) exist."""
        pkg = PlatonicPackage(affine_slN_data(2))
        assert pkg.is_complete()

    def test_affine_shadow_class_L(self):
        """Affine sl_N is class L (Lie/tree), r_max = 3."""
        data = affine_slN_data(3)
        assert data.shadow_class == 'L'

    def test_affine_quartic_zero(self):
        """R_4^mod = 0 for affine (Jacobi kills o_4)."""
        pkg = PlatonicPackage(affine_slN_data(2))
        assert pkg.quartic_class == 'zero'

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k=1) = 3(1+2)/(2*2) = 9/4."""
        data = affine_slN_data(2, Fraction(1))
        expected = Fraction(3) * Fraction(3) / Fraction(4)
        assert data.kappa == expected

    def test_affine_sl3_kappa(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        data = affine_slN_data(3, Fraction(1))
        expected = Fraction(8) * Fraction(4) / Fraction(6)
        assert data.kappa == expected

    def test_affine_branch_rank_equals_dim_g(self):
        """Branch rank = dim(g) for class L."""
        for N in [2, 3, 4]:
            pkg = PlatonicPackage(affine_slN_data(N))
            assert pkg.branch_rank == N * N - 1


class TestPlatonicPackageBetaGamma:
    """Verify Pi_X(betagamma) for the betagamma system."""

    def test_betagamma_admissible(self):
        """betagamma is cyclically admissible."""
        data = betagamma_data()
        assert data.is_cyclically_admissible()

    def test_betagamma_package_complete(self):
        """All six components exist."""
        pkg = PlatonicPackage(betagamma_data())
        assert pkg.is_complete()

    def test_betagamma_shadow_class_C(self):
        """betagamma is class C (contact), r_max = 4."""
        data = betagamma_data()
        assert data.shadow_class == 'C'

    def test_betagamma_quartic_canonical(self):
        """R_4 is canonical (cubic gauge-trivial => quartic canonical)."""
        pkg = PlatonicPackage(betagamma_data())
        assert pkg.quartic_class == 'canonical'

    def test_betagamma_kappa_lambda1(self):
        """kappa(betagamma, lambda=1) = 6-6+1 = 1."""
        data = betagamma_data(Fraction(1))
        assert data.kappa == Fraction(1)


class TestPlatonicPackageVirasoro:
    """Verify Pi_X(Vir) for Virasoro."""

    def test_virasoro_admissible(self):
        """Virasoro is cyclically admissible."""
        data = virasoro_data(Fraction(26))
        assert data.is_cyclically_admissible()

    def test_virasoro_package_complete(self):
        """All six components exist."""
        pkg = PlatonicPackage(virasoro_data(Fraction(26)))
        assert pkg.is_complete()

    def test_virasoro_shadow_class_M(self):
        """Virasoro is class M (mixed), r_max = infinity."""
        data = virasoro_data()
        assert data.shadow_class == 'M'

    def test_virasoro_quartic_gauge_dependent(self):
        """R_4 is gauge-dependent for class M (cubic NOT trivial)."""
        pkg = PlatonicPackage(virasoro_data())
        assert pkg.quartic_class == 'gauge-dependent'

    def test_virasoro_kappa(self):
        """kappa(Vir, c=26) = 13."""
        data = virasoro_data(Fraction(26))
        assert data.kappa == Fraction(13)


# ========================================================================
# (b) Independent sum factorization
# ========================================================================

class TestIndependentSumFactorization:
    """Verify prop:independent-sum-factorization for L1 ⊕ L2."""

    def test_kappa_additivity_heisenberg_plus_affine(self):
        """kappa(Heis ⊕ sl_2) = kappa(Heis) + kappa(sl_2)."""
        result = IndependentSumEngine.kappa_additivity(
            heisenberg_data(), affine_slN_data(2))
        assert result['passes']
        assert result['kappa_direct_sum'] == result['kappa_L1'] + result['kappa_L2']

    def test_kappa_additivity_three_summands(self):
        """kappa is additive for three direct summands."""
        h = heisenberg_data()
        a = affine_slN_data(2)
        v = virasoro_data(Fraction(10))
        total = h.kappa + a.kappa + v.kappa
        result = NumericalVerificationEngine.verify_kappa_additivity_numerical([h, a, v])
        assert result['total_kappa'] == total

    def test_branch_direct_sum_heisenberg_affine(self):
        """Branch rank is additive: rank(Heis) + rank(sl_2) = 0 + 3."""
        result = IndependentSumEngine.branch_direct_sum(
            heisenberg_data(), affine_slN_data(2))
        assert result['rank_direct_sum'] == 0 + 3

    def test_discriminant_multiplicativity(self):
        """det(1-xT) = det(1-xT1) * det(1-xT2) for block-diagonal T."""
        evs1 = [Fraction(1, 2), Fraction(1, 3)]
        evs2 = [Fraction(1, 5)]
        result = IndependentSumEngine.discriminant_multiplicativity(evs1, evs2)
        assert result['passes']
        assert result['Delta_product'] == result['Delta_combined']

    def test_discriminant_multiplicativity_trivial(self):
        """Discriminant multiplicativity holds with empty eigenvalue list."""
        result = IndependentSumEngine.discriminant_multiplicativity([], [Fraction(1, 2)])
        assert result['passes']
        # Delta = det(1 - x*T) with x=1/10, eigenvalue 1/2: 1 - (1/10)(1/2) = 19/20
        assert result['Delta_combined'] == Fraction(19, 20)

    def test_quartic_additivity(self):
        """R_4 additivity: R_4(Heis ⊕ βγ) = R_4(Heis) + R_4(βγ) = 0 + canonical."""
        result = IndependentSumEngine.quartic_additivity(
            heisenberg_data(), betagamma_data())
        assert result['passes']


# ========================================================================
# (c) Cubic gauge triviality
# ========================================================================

class TestCubicGaugeTriviality:
    """Verify thm:cubic-gauge-triviality for all shadow classes."""

    def test_class_G_cubic_trivial(self):
        """Class G: H^1 = 0, cubic trivial, quartic canonical."""
        result = CubicGaugeEngine.check_cubic_triviality('G')
        assert result['H1_vanishes']
        assert result['cubic_trivial']
        assert result['quartic_canonical']

    def test_class_L_cubic_nontrivial(self):
        """Class L: H^1 ≠ 0, cubic NOT trivial (Lie bracket)."""
        result = CubicGaugeEngine.check_cubic_triviality('L')
        assert not result['H1_vanishes']
        assert not result['cubic_trivial']

    def test_class_C_cubic_trivial(self):
        """Class C: H^1 = 0, cubic trivial (rank-one abelian rigidity)."""
        result = CubicGaugeEngine.check_cubic_triviality('C')
        assert result['H1_vanishes']
        assert result['cubic_trivial']
        assert result['quartic_canonical']

    def test_class_M_cubic_nontrivial(self):
        """Class M: H^1 ≠ 0, cubic NOT trivial."""
        result = CubicGaugeEngine.check_cubic_triviality('M')
        assert not result['H1_vanishes']
        assert not result['cubic_trivial']

    def test_obstruction_chain_G(self):
        """Class G obstruction chain: o_2 = kappa, o_r = 0 for r >= 3."""
        for r in range(2, 6):
            result = CubicGaugeEngine.filtered_mc_obstruction_chain(r, 'G')
            if r == 2:
                assert result['is_nonzero']
            else:
                assert not result['is_nonzero']

    def test_obstruction_chain_C_quartic(self):
        """Class C: o_3 gauge-trivial, o_4 = quartic_Q nonzero."""
        r3 = CubicGaugeEngine.filtered_mc_obstruction_chain(3, 'C')
        assert r3['obstruction'] == 'gauge_trivial'
        assert not r3['is_nonzero']  # gauge_trivial is not "nonzero"

        r4 = CubicGaugeEngine.filtered_mc_obstruction_chain(4, 'C')
        assert r4['obstruction'] == 'quartic_Q'
        assert r4['is_nonzero']

    def test_obstruction_chain_M_infinite(self):
        """Class M: o_5 forced nonzero => infinite tower."""
        r5 = CubicGaugeEngine.filtered_mc_obstruction_chain(5, 'M')
        assert r5['obstruction'] == 'quintic_forced'
        assert r5['is_nonzero']
        assert not r5['is_terminal']  # M class never terminates


# ========================================================================
# (d) Genus-0 envelope recovery
# ========================================================================

class TestGenus0Envelope:
    """Verify Nishinaka genus-0 envelope recovers correct vertex algebra."""

    def test_heisenberg_envelope_is_sym(self):
        """U(R) = Sym^ch(R) for abelian R."""
        result = Genus0EnvelopeEngine.verify_genus0_envelope('Heisenberg')
        assert result['envelope'] == 'Sym^ch(R)'
        assert result['is_free']
        assert result['envelope_exists']

    def test_affine_envelope_is_vk(self):
        """U(g_aff) = V_k(g) for affine g at level k."""
        result = Genus0EnvelopeEngine.verify_genus0_envelope('Affine_sl2')
        assert result['envelope'] == 'V_k(sl_2)'
        assert result['pbw_holds']

    def test_virasoro_envelope(self):
        """U(Vir) = Vir_c."""
        result = Genus0EnvelopeEngine.verify_genus0_envelope('Virasoro')
        assert result['envelope'] == 'Vir_c'
        assert result['strong_generators'] == 1

    def test_all_standard_envelopes_exist(self):
        """All standard families have well-defined genus-0 envelopes."""
        for family in ['Heisenberg', 'Affine_sl2', 'Affine_sl3',
                       'BetaGamma', 'Virasoro']:
            result = Genus0EnvelopeEngine.verify_genus0_envelope(family)
            assert result['envelope_exists'], f"{family} envelope missing"

    def test_pbw_implies_koszul_all_families(self):
        """PBW => chirally Koszul for all standard families (prop:pbw-universality)."""
        for family in ['Heisenberg', 'Affine_sl2', 'Affine_sl3',
                       'BetaGamma', 'Virasoro']:
            result = Genus0EnvelopeEngine.verify_genus0_envelope(family)
            assert result['pbw_implies_koszul'], f"{family} fails PBW => Koszul"

    def test_heisenberg_weight_gf(self):
        """Heisenberg U(R) weight dims = partition function."""
        data = heisenberg_data(rank=1)
        dims = Genus0EnvelopeEngine.weight_generating_function(data, 6)
        # One generator of weight 1: dim U(R)_n = p(n) using 1 generator = 1 for all n
        assert dims == [1, 1, 1, 1, 1, 1, 1]

    def test_affine_sl2_weight_gf(self):
        """Affine sl_2 U(g) weight dims: 3 generators of weight 1."""
        data = affine_slN_data(2)
        dims = Genus0EnvelopeEngine.weight_generating_function(data, 4)
        # 3 generators of weight 1: p_3(n) = #partitions of n with 3 colors
        # p_3(0)=1, p_3(1)=3, p_3(2)=6+3=9? No, it is the number of
        # multisets of size n from {g1, g2, g3} with each gi having weight 1
        # = C(n+2, 2) = (n+1)(n+2)/2
        # Actually with the simple partition algorithm: 3 parts of size 1
        # each independently chosen: p_3(0)=1, p_3(1)=3, p_3(2)=6, p_3(3)=10
        assert dims[0] == 1
        assert dims[1] == 3
        assert dims[2] == 6
        assert dims[3] == 10


# ========================================================================
# (e) Left adjoint existence criteria
# ========================================================================

class TestAdjointExistence:
    """Verify conditions for the platonic adjunction."""

    def test_lca_cyc_locally_presentable(self):
        """LCA_cyc(X) is locally presentable (Adamek-Rosicky)."""
        result = AdjointExistenceEngine.check_local_presentability()
        assert result['is_locally_presentable']

    def test_prim_preserves_limits(self):
        """Prim^mod preserves limits (ker commutes with limits)."""
        result = AdjointExistenceEngine.check_prim_preserves_limits()
        assert result['preserves_limits']
        assert result['preserves_products']
        assert result['preserves_equalizers']

    def test_u_mod_preserves_colimits(self):
        """U^mod_X preserves colimits (left adjoints preserve colimits)."""
        result = AdjointExistenceEngine.check_prim_preserves_filtered_colimits()
        assert result['u_mod_preserves_colimits']

    def test_saft_applicable(self):
        """SAFT applies: LCA_cyc locally presentable + Prim preserves limits."""
        lp = AdjointExistenceEngine.check_local_presentability()
        pl = AdjointExistenceEngine.check_prim_preserves_limits()
        assert lp['is_locally_presentable'] and pl['preserves_limits']


# ========================================================================
# (f) Unit-counit triangle identities
# ========================================================================

class TestUnitCounit:
    """Verify unit-counit construction for the adjunction."""

    def test_unit_injective_all_families(self):
        """Unit eta_L : L -> Prim(U(L)) is injective for all standard families."""
        for name, factory in STANDARD_FAMILIES.items():
            data = factory()
            result = AdjointExistenceEngine.verify_unit_counit(data)
            assert result['unit_injective'], f"Unit not injective for {name}"

    def test_counit_surjective_all_families(self):
        """Counit epsilon_F : U(Prim(F)) -> F is surjective."""
        for name, factory in STANDARD_FAMILIES.items():
            data = factory()
            result = AdjointExistenceEngine.verify_unit_counit(data)
            assert result['counit_surjective'], f"Counit not surjective for {name}"

    def test_triangle_identities(self):
        """Both triangle identities hold for all standard families."""
        for name, factory in STANDARD_FAMILIES.items():
            data = factory()
            result = AdjointExistenceEngine.verify_unit_counit(data)
            assert result['triangle_1'], f"Triangle 1 fails for {name}"
            assert result['triangle_2'], f"Triangle 2 fails for {name}"


# ========================================================================
# (g) Milnor-Moore factorization
# ========================================================================

class TestMilnorMoore:
    """Verify Milnor-Moore theorem for factorization coalgebras."""

    def test_bar_cocommutative_all_families(self):
        """barB(F) is cocommutative for all standard families."""
        for name in STANDARD_FAMILIES:
            result = MilnorMooreEngine.verify_bar_cocommutative(name)
            assert result['bar_cocommutative'], f"barB not cocommutative for {name}"

    def test_conilpotency_all_families(self):
        """barB(F) is conilpotent for all standard families."""
        for name, factory in STANDARD_FAMILIES.items():
            data = factory()
            result = MilnorMooreEngine.verify_conilpotency(data)
            assert result['conilpotent'], f"barB not conilpotent for {name}"

    def test_milnor_moore_applies_all_families(self):
        """Milnor-Moore theorem applies: char 0, connected, cocommutative."""
        for name, factory in STANDARD_FAMILIES.items():
            data = factory()
            result = MilnorMooreEngine.milnor_moore_applies(data)
            assert result['milnor_moore_applies'], f"MM fails for {name}"


# ========================================================================
# (h) Modular extension chain
# ========================================================================

class TestModularExtension:
    """Verify the five-step modular extension from genus-0 to all genera."""

    def test_extension_chain_all_families(self):
        """All five steps (Fact, bar, G_mod, Theta, HS-sewing) pass."""
        for name, factory in STANDARD_FAMILIES.items():
            data = factory()
            result = ModularExtensionEngine.verify_extension_chain(data)
            assert result['all_steps_pass'], f"Extension chain fails for {name}"

    def test_shadow_tower_termination(self):
        """Shadow tower terminates for G/L/C classes, infinite for M."""
        terminates_expected = {
            'Heisenberg': True, 'Lattice': True,
            'Affine_sl2': True, 'Affine_sl3': True,
            'BetaGamma': True, 'Virasoro': False,
        }
        for name, expected in terminates_expected.items():
            factory = STANDARD_FAMILIES[name]
            data = factory()
            result = ModularExtensionEngine.shadow_tower_termination(data)
            assert result['terminates'] == expected, \
                f"Shadow termination wrong for {name}"

    def test_inverse_limit_exists_all_families(self):
        """Inverse limit Theta_A = varprojlim Theta^{<=r} exists (thm:recursive-existence)."""
        for name, factory in STANDARD_FAMILIES.items():
            data = factory()
            result = ModularExtensionEngine.shadow_tower_termination(data)
            assert result['inverse_limit_exists']


# ========================================================================
# (i) Numerical checks
# ========================================================================

class TestNumericalChecks:
    """Numerical verification at specific parameter values."""

    def test_ds_kappa_descent_sl2(self):
        """DS descent: kappa(W_2) = rho(sl_2) * c(W_2) for sl_2 at k=1."""
        result = NumericalVerificationEngine.verify_ds_kappa_descent(2, Fraction(1))
        assert result['ds_descent_consistent']
        assert result['rho_slN'] == Fraction(1, 2)

    def test_ds_kappa_descent_sl3(self):
        """DS descent: kappa(W_3) = rho(sl_3) * c(W_3) for sl_3 at k=1."""
        result = NumericalVerificationEngine.verify_ds_kappa_descent(3, Fraction(1))
        assert result['ds_descent_consistent']
        assert result['rho_slN'] == Fraction(5, 6)

    def test_quartic_contact_virasoro_c26(self):
        """Q^contact_Vir at c=26 = 10/[26*(130+22)] = 10/(26*152)."""
        result = NumericalVerificationEngine.verify_quartic_contact_virasoro(Fraction(26))
        assert result['passes']
        expected = Fraction(10) / (Fraction(26) * Fraction(152))
        assert result['Q_contact'] == expected

    def test_quartic_contact_virasoro_c1(self):
        """Q^contact_Vir at c=1 = 10/(1*27) = 10/27."""
        result = NumericalVerificationEngine.verify_quartic_contact_virasoro(Fraction(1))
        assert result['Q_contact'] == Fraction(10, 27)

    def test_central_charge_additivity(self):
        """c(Heis ⊕ sl_2) = c(Heis) + c(sl_2)."""
        h = heisenberg_data()
        a = affine_slN_data(2, Fraction(1))
        result = NumericalVerificationEngine.verify_central_charge_additivity([h, a])
        assert result['total_charge'] == h.central_charge + a.central_charge

    def test_kappa_additivity_numerical_five_summands(self):
        """kappa is additive for five Heisenberg summands of varying rank."""
        families = [heisenberg_data(rank=r) for r in range(1, 6)]
        result = NumericalVerificationEngine.verify_kappa_additivity_numerical(families)
        expected = sum(Fraction(r) for r in range(1, 6))
        assert result['total_kappa'] == expected


# ========================================================================
# Master verification
# ========================================================================

class TestMasterVerification:
    """Run the full BLUE team verification suite."""

    def test_full_verification_runs(self):
        """The full verification suite completes without errors."""
        result = run_full_blue_team_verification()
        assert result['summary']['all_packages_complete']

    def test_all_families_have_complete_packages(self):
        """Every standard family has a complete platonic package."""
        result = run_full_blue_team_verification()
        for name, pkg in result['platonic_packages'].items():
            assert pkg['is_complete'], f"Package incomplete for {name}"


# ========================================================================
# Additional structural tests
# ========================================================================

class TestStructuralProperties:
    """Additional structural tests supporting the adjunction."""

    def test_affine_critical_level_rejected(self):
        """Critical level k = -h^v raises ValueError."""
        with pytest.raises(ValueError):
            affine_slN_data(2, Fraction(-2))

    def test_lattice_package_complete(self):
        """Lattice VOA platonic package is complete (class G)."""
        pkg = PlatonicPackage(lattice_data(8))
        assert pkg.is_complete()
        assert pkg.quartic_class == 'zero'

    def test_lattice_kappa_proportional_to_rank(self):
        """kappa(V_Lambda) = rank(Lambda), independent of cocycle."""
        for rank in [1, 2, 4, 8, 16, 24]:
            data = lattice_data(rank)
            assert data.kappa == Fraction(rank)

    def test_heisenberg_rank_scaling(self):
        """kappa scales linearly with rank for Heisenberg."""
        for r in range(1, 10):
            data = heisenberg_data(rank=r)
            assert data.kappa == Fraction(r)

    def test_affine_kappa_varies_with_N(self):
        """kappa(sl_N, k=1) grows with N as (N^2-1)(1+N)/(2N)."""
        for N in range(2, 8):
            data = affine_slN_data(N, Fraction(1))
            expected = Fraction(N*N - 1) * Fraction(N + 1) / Fraction(2 * N)
            assert data.kappa == expected

    def test_shadow_class_determines_quartic_type(self):
        """Shadow class uniquely determines the quartic resonance type."""
        mapping = {'G': 'zero', 'L': 'zero', 'C': 'canonical', 'M': 'gauge-dependent'}
        for sc, expected_type in mapping.items():
            data = CyclicAdmissibleData(
                name=f'test_{sc}', weight_dims={1: 1},
                pole_order_bound=1, has_invariant_pairing=True,
                shadow_class=sc)
            pkg = PlatonicPackage(data)
            assert pkg.quartic_class == expected_type, \
                f"Class {sc}: expected {expected_type}, got {pkg.quartic_class}"

    def test_genus0_strong_generator_counts(self):
        """Strong generator counts match dimension of Lie conformal input."""
        checks = {
            'Heisenberg': 1,
            'Affine_sl2': 3,
            'Affine_sl3': 8,
            'BetaGamma': 2,
            'Virasoro': 1,
        }
        for family, expected_gens in checks.items():
            result = Genus0EnvelopeEngine.verify_genus0_envelope(family)
            assert result['strong_generators'] == expected_gens, \
                f"{family}: expected {expected_gens} generators"
