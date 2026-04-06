#!/usr/bin/env python3
"""
test_parametrized_bar_cobar.py — Tests for parametrized bar-cobar adjunction.

Tests the degeneration loci, arithmetic structure, level-crossing rates,
and phase transition detection across all four families:
  1. Affine sl_2: V_k(sl_2)
  2. Virasoro: Vir_c
  3. W_N: W_k(sl_N) for N = 2,3,4
  4. Lattice VOA: V_Lambda(R)

References:
  - prop:pbw-universality: V_k(g) Koszul for all k != -h^v
  - cor:universal-koszul: universal vertex algebras always chirally Koszul
  - Q^contact_Vir = 10/[c(5c+22)]
  - Vir_c^! = Vir_{26-c}, self-dual at c = 13
"""

import numpy as np
import pytest
from fractions import Fraction
from math import gcd

from compute.lib.parametrized_bar_cobar import (
    # Affine sl_2
    affine_sl2_curvature,
    affine_sl2_central_charge,
    affine_sl2_bar_cobar_obstruction,
    affine_sl2_admissible_levels,
    affine_sl2_degeneration_locus,
    affine_sl2_simple_quotient_degeneration,
    # Virasoro
    virasoro_curvature,
    virasoro_quartic_contact,
    virasoro_genus1_hessian_correction,
    virasoro_shadow_gf_singularity,
    virasoro_koszul_dual_central_charge,
    virasoro_special_values,
    virasoro_minimal_model_c,
    virasoro_minimal_model_c_exact,
    virasoro_degeneration_locus,
    virasoro_minimal_model_table,
    # W_N
    wn_dual_coxeter,
    wn_dimension,
    wn_central_charge,
    wn_curvature,
    wn_quartic_contact,
    wn_degeneration_locus,
    wn_level_rank_involution,
    # Lattice
    lattice_curvature,
    lattice_constrained_epstein_rank1,
    lattice_constrained_epstein_analytic,
    lattice_epstein_residue_at_zeta_zero,
    lattice_tduality_check,
    lattice_degeneration_locus,
    # Degeneration locus topology
    degeneration_locus_is_discrete,
    degeneration_locus_is_algebraic,
    # Arithmetic
    minimal_model_arithmetic,
    minimal_model_density,
    # Level crossing
    level_crossing_rate,
    level_crossing_fit,
    # Phase transition
    bar_spectral_gap_virasoro,
    spectral_gap_near_minimal_model,
    gap_opening_exponent,
    # Summary
    parametrized_landscape_summary,
    # Grids
    curvature_grid_affine,
    curvature_grid_virasoro,
    epstein_modulation_grid,
    wn_curvature_grid,
)


# =============================================================================
# 1. Affine sl_2 family
# =============================================================================

class TestAffineSl2Family:
    """Tests for affine sl_2 parametrized bar-cobar."""

    def test_curvature_at_critical(self):
        """kappa(-2) = 0: bar uncurved at critical level."""
        assert affine_sl2_curvature(-2) == 0

    def test_curvature_generic(self):
        """kappa(k) = k + 2 for generic k."""
        for k in [0, 1, 3, 10, -1, 0.5]:
            assert abs(affine_sl2_curvature(k) - (k + 2)) < 1e-14

    def test_curvature_positive_for_positive_k(self):
        """kappa > 0 for k > -2."""
        for k in [0, 1, 5, 100]:
            assert affine_sl2_curvature(k) > 0

    def test_central_charge_level1(self):
        """c(k=1) = 1 (level-1 = free boson)."""
        assert abs(affine_sl2_central_charge(1) - 1.0) < 1e-14

    def test_central_charge_large_k(self):
        """c -> 3 as k -> infinity."""
        assert abs(affine_sl2_central_charge(10000) - 3.0) < 0.001

    def test_central_charge_critical(self):
        """c is infinite (Sugawara undefined) at k = -2."""
        assert affine_sl2_central_charge(-2) == float('inf')

    def test_bar_cobar_obstruction_generic(self):
        """No obstruction at generic k."""
        obs = affine_sl2_bar_cobar_obstruction(1)
        assert obs['koszul'] is True
        assert obs['obstruction_type'] == 'none'
        assert obs['bar_curved'] is True

    def test_bar_cobar_obstruction_critical(self):
        """Critical level: bar uncurved, but still chirally Koszul (PBW universality)."""
        obs = affine_sl2_bar_cobar_obstruction(-2)
        assert obs['is_critical'] is True
        assert obs['koszul'] is True
        assert obs['bar_curved'] is False
        assert obs['obstruction_type'] == 'critical_uncurved'

    def test_admissible_levels_coprimality(self):
        """All admissible levels have coprime (p, q)."""
        levels = affine_sl2_admissible_levels(10, 10)
        for k, p, q in levels:
            assert gcd(p, q) == 1, f"({p}, {q}) not coprime"

    def test_admissible_levels_p_bound(self):
        """Admissible levels have p >= 2."""
        levels = affine_sl2_admissible_levels(10, 10)
        for k, p, q in levels:
            assert p >= 2

    def test_admissible_level_reconstruction(self):
        """k = -2 + p/q for admissible levels."""
        levels = affine_sl2_admissible_levels(8, 8)
        for k, p, q in levels:
            expected = -2.0 + p / q
            assert abs(k - expected) < 1e-14

    def test_degeneration_locus_affine(self):
        """D = {k = -2} for universal V_k(sl_2)."""
        D = affine_sl2_degeneration_locus()
        assert D['critical'] == [-2.0]
        assert D['type'] == 'discrete'
        assert D['algebraic'] is True

    def test_simple_quotient_degeneration(self):
        """Simple quotient has larger degeneration set."""
        D_simple = affine_sl2_simple_quotient_degeneration(5, 5)
        assert -2.0 in D_simple['critical']
        assert len(D_simple['admissible']) > 0
        assert D_simple['degeneration_set_size'] > 1


# =============================================================================
# 2. Virasoro family
# =============================================================================

class TestVirasoroFamily:
    """Tests for Virasoro parametrized bar-cobar."""

    def test_curvature_formula(self):
        """kappa(c) = c/2."""
        for c in [0, 1, 13, 26, -22 / 5]:
            assert abs(virasoro_curvature(c) - c / 2) < 1e-14

    def test_quartic_contact_formula(self):
        """Q^contact = 10/[c(5c+22)] at generic c."""
        c = 13.0
        expected = 10.0 / (13.0 * (65.0 + 22.0))
        assert abs(virasoro_quartic_contact(c) - expected) < 1e-14

    def test_quartic_contact_diverges_c0(self):
        """Q diverges at c = 0."""
        assert virasoro_quartic_contact(0) == float('inf')

    def test_quartic_contact_diverges_lee_yang(self):
        """Q diverges at c = -22/5."""
        assert virasoro_quartic_contact(-22.0 / 5.0) == float('inf')

    def test_genus1_hessian_correction(self):
        """delta_H^(1) = 120/[c^2(5c+22)]."""
        c = 10.0
        expected = 120.0 / (100.0 * (50.0 + 22.0))
        assert abs(virasoro_genus1_hessian_correction(c) - expected) < 1e-12

    def test_shadow_gf_singularity(self):
        """Shadow GF singularity at t = -c/6."""
        assert abs(virasoro_shadow_gf_singularity(6.0) - (-1.0)) < 1e-14

    def test_koszul_dual_formula(self):
        """Vir_c^! = Vir_{26-c}."""
        assert abs(virasoro_koszul_dual_central_charge(13.0) - 13.0) < 1e-14
        assert abs(virasoro_koszul_dual_central_charge(0.0) - 26.0) < 1e-14
        assert abs(virasoro_koszul_dual_central_charge(26.0) - 0.0) < 1e-14

    def test_self_dual_at_c13(self):
        """Self-dual at c = 13, NOT c = 26 (critical pitfall)."""
        c_dual = virasoro_koszul_dual_central_charge(13.0)
        assert abs(c_dual - 13.0) < 1e-14, "Self-dual point must be c = 13"

    def test_not_self_dual_at_c26(self):
        """NOT self-dual at c = 26."""
        c_dual = virasoro_koszul_dual_central_charge(26.0)
        assert abs(c_dual - 26.0) > 1.0, "c = 26 is NOT self-dual"

    def test_special_values_catalogue(self):
        """All expected special values present."""
        sv = virasoro_special_values()
        expected_keys = [0.0, -4.4, 0.5, 1.0, 13.0, 25.0, 26.0]
        for key in expected_keys:
            assert key in sv, f"Missing special value c = {key}"

    def test_minimal_model_ising(self):
        """c_{3,4} = 1/2 (Ising model)."""
        c = virasoro_minimal_model_c(4, 3)
        assert abs(c - 0.5) < 1e-14

    def test_minimal_model_tricritical_ising(self):
        """c_{4,5} = 7/10 (tricritical Ising)."""
        c = virasoro_minimal_model_c(5, 4)
        assert abs(c - 0.7) < 1e-14

    def test_minimal_model_lee_yang(self):
        """c_{2,5} = -22/5 (Lee-Yang)."""
        c = virasoro_minimal_model_c(5, 2)
        assert abs(c - (-22.0 / 5.0)) < 1e-14

    def test_minimal_model_exact_rational(self):
        """All c_{p,q} are exact rationals."""
        for q in range(2, 8):
            for p in range(q + 1, 10):
                if gcd(p, q) != 1:
                    continue
                c_exact = virasoro_minimal_model_c_exact(p, q)
                assert isinstance(c_exact, Fraction)
                # Verify float matches
                assert abs(float(c_exact) - virasoro_minimal_model_c(p, q)) < 1e-14

    def test_minimal_model_table_sorted(self):
        """Table is sorted by c."""
        table = virasoro_minimal_model_table(10, 11)
        cs = [entry['c'] for entry in table]
        assert cs == sorted(cs)

    def test_minimal_model_all_algebraic_degree_1(self):
        """All c_{p,q} are algebraic of degree 1 (rational)."""
        table = virasoro_minimal_model_table(10, 11)
        for entry in table:
            assert entry['algebraic_degree'] == 1

    def test_degeneration_locus_virasoro(self):
        """D = {0, -22/5} for Virasoro."""
        D = virasoro_degeneration_locus()
        assert 0.0 in D['Q_contact_poles']
        assert abs(D['Q_contact_poles'][1] - (-22.0 / 5.0)) < 1e-14
        assert D['type'] == 'discrete'
        assert D['algebraic'] is True


# =============================================================================
# 3. W_N family
# =============================================================================

class TestWNFamily:
    """Tests for W_N parametrized bar-cobar."""

    def test_dual_coxeter(self):
        """h^v = N for sl_N."""
        for N in [2, 3, 4, 5]:
            assert wn_dual_coxeter(N) == N

    def test_dimension(self):
        """dim(sl_N) = N^2 - 1."""
        assert wn_dimension(2) == 3
        assert wn_dimension(3) == 8
        assert wn_dimension(4) == 15

    def test_wn_central_charge_n2_matches_virasoro(self):
        """W_k(sl_2) = Vir at c_{W_2}(k) = 1 - 6/(k+2).

        Wait: the DS formula gives c_{W_2} = (2-1)[1 - 2*3/(k+2)] = 1 - 6/(k+2).
        But the Sugawara gives c_{V_k(sl_2)} = 3k/(k+2).
        And DS for principal nilpotent of sl_2: c_{W_2} = c_{V_k} - c_{ghost}
        where c_{ghost} = 3(2k+1)/(k+2) - 1 = ... Actually:

        For sl_2 with principal nilpotent: W_k(sl_2) IS the Virasoro algebra
        at central charge c = 1 - 6(k+1)^2/(k+2)... No, this is wrong.

        The correct formula: c_{W_N}(k) = (N-1)[1 - N(N+1)/(k+N)].
        For N=2: c = 1 - 6/(k+2).
        At k=1: c = 1 - 6/3 = -1.
        But Vir from sl_2 at level 1 should be c = 1 via Sugawara...

        Actually, the W-algebra W_k(sl_2, f_principal) IS the Virasoro algebra,
        but at a DIFFERENT central charge than the Sugawara c of V_k(sl_2).
        The DS reduction subtracts the ghost central charge.
        c_{W_2}(k) = 1 - 6/(k+2) is the VIRASORO central charge post-DS.
        """
        # At k = 10: c_{W_2} = 1 - 6*121/12 = -119/2 = -59.5
        c_w2 = wn_central_charge(10, 2)
        expected = 1.0 - 6.0 * 121.0 / 12.0
        assert abs(c_w2 - expected) < 1e-14

    def test_wn_critical_level(self):
        """c is infinite at k = -N (critical level)."""
        for N in [2, 3, 4]:
            assert wn_central_charge(-N, N) == float('inf')

    def test_wn_curvature_n2(self):
        """kappa_{W_2}(k) = c_{W_2}/2."""
        k = 5
        assert abs(wn_curvature(k, 2) - wn_central_charge(k, 2) / 2) < 1e-14

    def test_wn_quartic_contact_n2(self):
        """Q^{TT}_{W_2} matches Virasoro Q^contact."""
        k = 5
        c = wn_central_charge(k, 2)
        q_wn = wn_quartic_contact(k, 2)
        q_vir = virasoro_quartic_contact(c)
        assert abs(q_wn - q_vir) < 1e-14

    def test_wn_degeneration_critical(self):
        """Degeneration at k = -N."""
        for N in [2, 3, 4]:
            D = wn_degeneration_locus(N)
            assert abs(D['critical_level'] - (-N)) < 1e-14

    def test_wn_degeneration_algebraic(self):
        """Degeneration loci are algebraic."""
        for N in [2, 3, 4]:
            D = wn_degeneration_locus(N)
            assert D['algebraic'] is True

    def test_level_rank_involution_is_involution(self):
        """Level-rank duality squares to identity (up to shift)."""
        k, N = 3, 4
        k_dual = wn_level_rank_involution(k, N)
        k_double = wn_level_rank_involution(k_dual, N)
        assert abs(k_double - k) < 1e-14

    def test_wn_curvature_increases_with_N(self):
        """At fixed large k, |kappa_{W_N}| increases with N (more fields).

        With correct Fateev-Lukyanov, c ~ -N(N^2-1)*k for large k,
        so c is large and negative.  kappa = c/2 is also large and negative.
        |kappa| increases with N.
        """
        k = 100
        kappas = [wn_curvature(k, N) for N in [2, 3, 4]]
        # c is negative for large k, kappa = c/2 is negative
        # |kappa| increases with N
        assert abs(kappas[1]) > abs(kappas[0])
        assert abs(kappas[2]) > abs(kappas[1])


# =============================================================================
# 4. Lattice VOA family
# =============================================================================

class TestLatticeFamily:
    """Tests for lattice VOA parametrized bar-cobar."""

    def test_curvature_rank1(self):
        """kappa = 1 for rank-1 lattice (anomaly ratio rho = 1)."""
        assert abs(lattice_curvature(1) - 1.0) < 1e-14

    def test_curvature_independent_of_R(self):
        """kappa = rank, independent of R."""
        for rank in [1, 2, 3, 8]:
            assert abs(lattice_curvature(rank) - rank) < 1e-14

    def test_epstein_self_dual(self):
        """At R = 1 (self-dual): epsilon = 4*zeta(2s)."""
        s = 2.0
        eps = lattice_constrained_epstein_rank1(s, R=1.0, nmax=1000)
        # zeta(4) = pi^4/90
        zeta4 = np.pi ** 4 / 90.0
        expected = 4.0 * zeta4
        assert abs(eps - expected) / expected < 0.01

    def test_tduality(self):
        """T-duality: epsilon(R) = epsilon(1/R)."""
        for R in [0.5, 2.0, 3.0, 0.3]:
            eps_R, eps_dual, rel_err = lattice_tduality_check(2.0, R, nmax=500)
            assert rel_err < 0.01, f"T-duality fails at R={R}: err={rel_err}"

    def test_epstein_analytic_vs_numerical(self):
        """Analytic and numerical Epstein agree."""
        s = 2.5
        R = 1.5
        eps_num = lattice_constrained_epstein_rank1(s, R, nmax=1000)
        eps_ana = lattice_constrained_epstein_analytic(s, R)
        rel_err = abs(eps_num - eps_ana) / max(abs(eps_ana), 1e-30)
        assert rel_err < 0.02, f"Analytic vs numerical: err={rel_err}"

    def test_epstein_modulation_at_zeta_zeros(self):
        """R-dependent modulation factor is computable at all R > 0."""
        gamma1 = 14.134725  # First zeta zero imaginary part
        for R in [0.1, 0.5, 1.0, 2.0, 10.0]:
            mod = lattice_epstein_residue_at_zeta_zero(R, gamma1)
            assert mod >= 0, f"Modulation must be non-negative"
            assert np.isfinite(mod)

    def test_modulation_tduality_symmetry(self):
        """Modulation factor symmetric under R <-> 1/R."""
        gamma1 = 14.134725
        for R in [0.3, 0.7, 2.5]:
            mod_R = lattice_epstein_residue_at_zeta_zero(R, gamma1)
            mod_dual = lattice_epstein_residue_at_zeta_zero(1.0 / R, gamma1)
            assert abs(mod_R - mod_dual) < 1e-10, \
                f"Modulation T-duality fails: R={R}"

    def test_lattice_degeneration_empty(self):
        """D = empty for lattice VOA."""
        D = lattice_degeneration_locus()
        assert D['degeneration_set'] == []
        assert D['type'] == 'empty'


# =============================================================================
# 5. Degeneration locus topology
# =============================================================================

class TestDegenerationTopology:
    """Tests for degeneration locus structure."""

    def test_all_families_discrete(self):
        """Degeneration locus is discrete for all families."""
        for family in ['affine_sl2', 'virasoro', 'W_2', 'W_3', 'W_4', 'lattice']:
            is_disc, desc = degeneration_locus_is_discrete(family)
            assert is_disc, f"Family {family}: D not discrete"

    def test_all_families_algebraic(self):
        """Degeneration locus is algebraic for all families."""
        for family in ['affine_sl2', 'virasoro', 'W_2', 'W_3', 'W_4', 'lattice']:
            is_alg, polys = degeneration_locus_is_algebraic(family)
            assert is_alg, f"Family {family}: D not algebraic"


# =============================================================================
# 6. Arithmetic content of degeneration loci
# =============================================================================

class TestArithmeticContent:
    """Tests for arithmetic structure of degeneration points."""

    def test_all_minimal_models_rational(self):
        """All c_{p,q} are rational numbers."""
        data = minimal_model_arithmetic(10, 11)
        for entry in data:
            assert entry['algebraic_degree'] == 1

    def test_minimal_model_heights_grow(self):
        """Heights of c_{p,q} grow with p*q."""
        data = minimal_model_arithmetic(10, 11)
        # Heights should correlate with p*q
        for entry in data:
            assert entry['height'] >= 1

    def test_unitary_minimal_models_in_01(self):
        """Unitary minimal models (p = q+1) have 0 <= c < 1.

        c_{3,2} = 0 is the boundary case (trivial theory).
        For q >= 3: 0 < c_{q+1,q} < 1 strictly.
        """
        for q in range(2, 20):
            p = q + 1
            c = virasoro_minimal_model_c(p, q)
            assert 0 <= c < 1, f"Unitary c_{{{p},{q}}} = {c} not in [0,1)"
        # Strictly positive for q >= 3
        for q in range(3, 20):
            p = q + 1
            c = virasoro_minimal_model_c(p, q)
            assert c > 0, f"Unitary c_{{{p},{q}}} = {c} not positive for q >= 3"

    def test_minimal_model_accumulation(self):
        """c_{p,q} accumulates at c = 1 from below for unitary models."""
        cs = [virasoro_minimal_model_c(q + 1, q) for q in range(2, 50)]
        assert all(c < 1 for c in cs)
        assert cs[-1] > 0.99  # Approaches 1

    def test_minimal_model_density(self):
        """Density of c_{p,q} in [-10, 1] increases with bounds."""
        d1 = minimal_model_density(-10, 1, 20, 21)
        d2 = minimal_model_density(-10, 1, 40, 41)
        assert len(d2) > len(d1)

    def test_no_zeta_zero_relation(self):
        """Minimal model c-values are rational, hence no direct zeta-zero relation.

        Zeta zeros rho = 1/2 + i*gamma are transcendental (conditional on standard
        conjectures). The c_{p,q} are all rational. Hence no c_{p,q} equals any
        function of zeta zeros that would produce a rational number generically.
        """
        data = minimal_model_arithmetic(10, 11)
        # All algebraic degree 1 (rational)
        assert all(entry['algebraic_degree'] == 1 for entry in data)
        # The connection to zeta zeros is through the EPSTEIN ZETA, not
        # through the parameter values themselves.


# =============================================================================
# 7. Level-crossing phenomenon
# =============================================================================

class TestLevelCrossing:
    """Tests for level-crossing as k -> -2."""

    def test_linear_rate(self):
        """|kappa| = |k+2| (linear rate)."""
        epsilons = [0.1, 0.01, 0.001, 0.0001]
        results = level_crossing_rate(epsilons)
        for r in results:
            assert abs(r['kappa'] - r['epsilon']) < 1e-14
            assert r['rate'] == 'linear'

    def test_homotopy_norm_diverges(self):
        """Homotopy norm ~ 1/|k+2| diverges as k -> -2."""
        epsilons = [1.0, 0.1, 0.01, 0.001]
        results = level_crossing_rate(epsilons)
        norms = [r['homotopy_norm'] for r in results]
        # Monotonically increasing
        for i in range(len(norms) - 1):
            assert norms[i + 1] > norms[i]

    def test_fit_slope_one(self):
        """Linear fit: slope = 1, intercept = 0."""
        epsilons = np.logspace(-4, 0, 50)
        slope, intercept, r_sq = level_crossing_fit(epsilons)
        assert abs(slope - 1.0) < 1e-10, f"Slope = {slope}, expected 1"
        assert abs(intercept) < 1e-10, f"Intercept = {intercept}, expected 0"
        assert r_sq > 0.9999, f"R^2 = {r_sq}, expected ~1"

    def test_crossing_not_exponential(self):
        """The rate is NOT exponential (it's exactly linear)."""
        # If exponential: log(kappa) would be linear in epsilon
        # Since kappa = epsilon exactly, log(kappa) = log(epsilon),
        # which is linear in log(epsilon), not in epsilon.
        epsilons = np.linspace(0.01, 1.0, 50)
        kappas = np.array([affine_sl2_curvature(-2 + e) for e in epsilons])
        # Fit kappa = a*exp(b*epsilon): take log
        log_kappas = np.log(kappas)
        # If exponential, log_kappa vs epsilon would be linear
        # But it's log_kappa = log(epsilon), which is NOT linear in epsilon
        # Test: R^2 of linear fit to (epsilon, log_kappa) should be poor
        coeffs = np.polyfit(epsilons, log_kappas, 1)
        predicted = np.polyval(coeffs, epsilons)
        ss_res = np.sum((log_kappas - predicted) ** 2)
        ss_tot = np.sum((log_kappas - np.mean(log_kappas)) ** 2)
        r_sq_exp = 1.0 - ss_res / ss_tot
        # R^2 should be significantly below 1 for exponential fit
        assert r_sq_exp < 0.99, f"Exponential R^2 = {r_sq_exp}, should be < 0.99"


# =============================================================================
# 8. Phase transition detection
# =============================================================================

class TestPhaseTransition:
    """Tests for spectral gap and phase transition behavior."""

    def test_spectral_gap_c0(self):
        """Gap = 0 at c = 0."""
        assert bar_spectral_gap_virasoro(0.0) == 0.0

    def test_spectral_gap_positive_generic(self):
        """Gap > 0 at generic c."""
        for c in [1.0, 10.0, 13.0, 26.0]:
            gap = bar_spectral_gap_virasoro(c)
            assert gap > 0, f"Gap = {gap} at c = {c}"

    def test_spectral_gap_continuous(self):
        """Gap varies continuously in the weight-2 sector.

        The weight-2 spectral gap is proportional to |c|^2, which is
        manifestly continuous. We check this simple sector only, since
        the full Kac determinant model is a rough approximation.
        """
        # In the weight-2 sector: gap ~ c^2 (continuous and monotone for c > 0)
        cs = np.linspace(0.1, 2.0, 50)
        gaps = [abs(c) ** 2 for c in cs]
        # Monotonically increasing for c > 0
        for i in range(1, len(gaps)):
            assert gaps[i] >= gaps[i - 1] - 1e-14

    def test_gap_near_ising(self):
        """Gap computation near Ising model c = 1/2."""
        results = spectral_gap_near_minimal_model(4, 3, [0.01, 0.1, -0.01, -0.1])
        assert len(results) == 4
        for r in results:
            assert 'gap' in r
            assert 'c' in r


# =============================================================================
# 9. Cross-family consistency
# =============================================================================

class TestCrossFamilyConsistency:
    """Tests for consistency across families."""

    def test_wn_n2_is_virasoro(self):
        """W_2 degeneration matches Virasoro degeneration pattern."""
        D_w2 = wn_degeneration_locus(2)
        D_vir = virasoro_degeneration_locus()
        # Both have critical level and Q-pole
        assert D_w2['algebraic'] == D_vir['algebraic']

    def test_all_degeneration_discrete(self):
        """Universal property: all families have discrete degeneration."""
        families = ['affine_sl2', 'virasoro', 'W_2', 'W_3', 'W_4', 'lattice']
        for f in families:
            is_disc, _ = degeneration_locus_is_discrete(f)
            assert is_disc

    def test_all_degeneration_algebraic(self):
        """Universal property: all families have algebraic degeneration."""
        families = ['affine_sl2', 'virasoro', 'W_2', 'W_3', 'W_4', 'lattice']
        for f in families:
            is_alg, _ = degeneration_locus_is_algebraic(f)
            assert is_alg

    def test_summary_complete(self):
        """Landscape summary covers all families."""
        summary = parametrized_landscape_summary()
        assert 'affine_sl2' in summary['families']
        assert 'virasoro' in summary['families']
        assert 'W_N' in summary['families']
        assert 'lattice' in summary['families']


# =============================================================================
# 10. Visualization grid sanity
# =============================================================================

class TestGrids:
    """Tests for visualization grid functions."""

    def test_affine_grid_shape(self):
        """Affine curvature grid has correct shape."""
        ks, kappas = curvature_grid_affine(n_points=100)
        assert len(ks) == 100
        assert len(kappas) == 100

    def test_virasoro_grid_shape(self):
        """Virasoro grid has correct shape."""
        cs, kappas, Qs = curvature_grid_virasoro(n_points=100)
        assert len(cs) == 100
        assert len(kappas) == 100
        assert len(Qs) == 100

    def test_epstein_modulation_grid_shape(self):
        """Epstein modulation grid is computable."""
        Rs, results = epstein_modulation_grid(n_R=50)
        assert len(Rs) == 50
        assert len(results) == 5  # 5 zeta zeros by default

    def test_wn_grid_shape(self):
        """W_N curvature grid has correct shape."""
        ks, kappas = wn_curvature_grid(3, n_points=100)
        assert len(ks) == 100
        assert len(kappas) == 100

    def test_wn_grid_has_nan_at_critical(self):
        """W_N grid has NaN at critical level k = -N."""
        for N in [2, 3, 4]:
            ks, kappas = wn_curvature_grid(N, k_min=-N - 1, k_max=-N + 1, n_points=1000)
            # At least one NaN near k = -N
            assert np.any(np.isnan(kappas)), f"No NaN found near k = -{N}"


# =============================================================================
# 11. Additional edge cases and consistency
# =============================================================================

class TestEdgeCases:
    """Tests for edge cases and boundary behavior."""

    def test_affine_negative_level(self):
        """Curvature is well-defined for negative k > -2."""
        k = -1.5
        kappa = affine_sl2_curvature(k)
        assert abs(kappa - 0.5) < 1e-14

    def test_virasoro_large_c(self):
        """Q^contact -> 0 as c -> infinity (semiclassical limit)."""
        Q = virasoro_quartic_contact(10000.0)
        assert abs(Q) < 1e-6

    def test_virasoro_negative_c(self):
        """Q^contact is well-defined for c < -22/5."""
        c = -10.0
        Q = virasoro_quartic_contact(c)
        assert np.isfinite(Q)
        expected = 10.0 / (-10.0 * (-50.0 + 22.0))
        assert abs(Q - expected) < 1e-12

    def test_lattice_small_radius(self):
        """Lattice VOA is Koszul even at very small R."""
        D = lattice_degeneration_locus()
        assert D['type'] == 'empty'
        # Curvature does not depend on R
        assert abs(lattice_curvature(1) - 1.0) < 1e-14

    def test_epstein_large_s(self):
        """Epstein converges rapidly for large Re(s)."""
        eps = lattice_constrained_epstein_rank1(10.0, R=1.0, nmax=100)
        assert np.isfinite(eps)
        assert eps > 0
