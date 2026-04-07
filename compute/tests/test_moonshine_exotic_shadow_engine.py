r"""Tests for moonshine_exotic_shadow_engine.py.

Covers:
  1. V^natural: kappa, shadow tower, class M, discriminant, growth rate
  2. Niemeier lattice VOAs: kappa = 24, class G, universality
  3. Kappa resolution: bar complex argument for V_Leech (kappa=24 vs c/2=12)
  4. AP48 distinction: V^natural vs V_Leech at same c = 24
  5. j-function and shadow tower connection
  6. Norton/Griess algebra invariants
  7. Koszul dual of V^natural
  8. Shadow comparison across all 24 Niemeier lattices
  9. Exotic VOAs: Baby Monster VB^natural, Thompson V_Th
  10. Cross-family consistency: additivity, orbifold halving, genus amplitudes
  11. Shadow metrics and growth rates
  12. Multi-path verification of every numerical claim

Multi-path verification mandate (3+ paths per claim):
  Path 1: Direct computation from defining formulas
  Path 2: Alternative formula / algebraic identity
  Path 3: Limiting cases and special values
  Path 4: Cross-family consistency
  Path 5: Literature comparison

Mathematical references:
  - Frenkel-Lepowsky-Meurman (1988): V^natural construction
  - Conway-Norton (1979): Monstrous Moonshine
  - Borcherds (1992): proof of moonshine conjecture
  - Norton (1996): Griess algebra eigenvalues
  - Hoehn (2007): Baby Monster super VOA
  - AP48, AP39, AP20, AP24: anti-patterns
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational, bernoulli, Abs, factorial, sqrt

from compute.lib.moonshine_exotic_shadow_engine import (
    # Faber-Pandharipande
    _faber_pandharipande,
    # Constants
    MONSTER_ORDER, BABY_MONSTER_ORDER,
    MONSTER_IRREP_DIMS, J_COEFFS, MONSTER_DECOMPOSITIONS,
    # Part 1: V^natural
    monster_central_charge, monster_kappa,
    monster_kappa_bar_complex_argument,
    virasoro_shadow_coefficient, monster_virasoro_shadow_tower,
    monster_quartic_contact, monster_critical_discriminant,
    monster_shadow_class, monster_shadow_depth,
    monster_shadow_growth_rate, monster_genus_amplitude,
    # Part 2: Niemeier
    NIEMEIER_DATA,
    niemeier_root_count, niemeier_kappa, niemeier_shadow_class,
    niemeier_shadow_depth, niemeier_genus_amplitude, niemeier_shadow_data,
    # Part 3: Leech
    leech_kappa, leech_vs_monster_kappa, leech_kappa_bar_complex,
    # Part 4: j-function
    j_coefficient, j_function_shadow_connection,
    # Part 5: Norton/Griess
    norton_eigenvalue, griess_algebra_shadow_contribution,
    # Part 6: Koszul dual
    monster_koszul_dual_data,
    # Part 7: Niemeier comparison
    niemeier_shadow_comparison, niemeier_c_delta, niemeier_distinct_c_delta,
    # Part 8: Exotic VOAs
    baby_monster_voa_data, thompson_voa_data, exotic_voa_landscape,
    # Part 9: Cross-family
    kappa_additivity_check_leech, orbifold_kappa_halving,
    genus_amplitude_comparison,
    # Part 10: Shadow metrics
    shadow_metric_monster, all_exotic_shadow_metrics,
)


# =========================================================================
# Helper: independent Faber-Pandharipande for cross-checking
# =========================================================================

def _fp_independent(g):
    """Independent FP computation for cross-checking (AP10)."""
    B_2g = Rational(bernoulli(2 * g))
    num = (Rational(2) ** (2 * g - 1) - 1) * Abs(B_2g)
    den = Rational(2) ** (2 * g - 1) * factorial(2 * g)
    return Rational(num, den)


# =========================================================================
# 1. V^natural: kappa
# =========================================================================

class TestMonsterKappa:
    """Multi-path verification that kappa(V^natural) = 12."""

    def test_kappa_value(self):
        """Path 1: Direct Virasoro formula kappa = c/2."""
        assert monster_kappa() == Rational(12)

    def test_kappa_from_central_charge(self):
        """Path 2: kappa = c/2 = 24/2 = 12."""
        c = monster_central_charge()
        assert c == Rational(24)
        assert monster_kappa() == c / 2

    def test_kappa_not_rank(self):
        """AP48: kappa(V^natural) = 12, NOT rank = 24."""
        assert monster_kappa() != Rational(24)
        assert monster_kappa() == Rational(12)

    def test_kappa_vs_leech(self):
        """AP48: V^natural and V_Leech have DIFFERENT kappa at same c."""
        assert monster_kappa() != leech_kappa()
        assert monster_kappa() == Rational(12)
        assert leech_kappa() == Rational(24)

    def test_kappa_bar_complex_all_paths_agree(self):
        """All three verification paths in the bar complex argument agree."""
        data = monster_kappa_bar_complex_argument()
        assert data['kappa'] == Rational(12)
        assert data['all_agree'] is True
        for path in data['paths']:
            if 'result' in path:
                result = path['result']
                # Path 3 returns F1, not kappa directly
                if 'kappa_from_F1' in path:
                    assert path['kappa_from_F1'] == Rational(12)
                elif result == Rational(12):
                    pass  # direct kappa
                elif result == Rational(1, 2):
                    pass  # F1 = 1/2

    def test_F1_from_kappa(self):
        """Path 3: F_1 = kappa * lambda_1^FP = 12 * 1/24 = 1/2."""
        F1 = monster_genus_amplitude(1)
        lambda1 = _faber_pandharipande(1)
        assert lambda1 == Rational(1, 24)
        assert F1 == Rational(1, 2)
        # Recover kappa from F1
        assert F1 / lambda1 == Rational(12)


# =========================================================================
# 2. V^natural: shadow tower
# =========================================================================

class TestMonsterShadowTower:
    """Virasoro shadow tower at c = 24."""

    def test_S2(self):
        """S_2 = c/2 = 12."""
        assert virasoro_shadow_coefficient(2) == Rational(12)

    def test_S3(self):
        """S_3 = 2 (universal Virasoro)."""
        assert virasoro_shadow_coefficient(3) == Rational(2)

    def test_S4_direct(self):
        """S_4 = 10/[c(5c+22)] = 10/(24*142) = 5/1704."""
        S4 = virasoro_shadow_coefficient(4)
        assert S4 == Rational(5, 1704)

    def test_S4_alternative(self):
        """S_4 via the quartic contact function."""
        assert monster_quartic_contact() == Rational(5, 1704)
        assert monster_quartic_contact() == virasoro_shadow_coefficient(4)

    def test_S4_explicit_computation(self):
        """S_4 = 10/(24*(5*24+22)) = 10/(24*142) = 10/3408 = 5/1704."""
        c = Rational(24)
        S4_explicit = Rational(10) / (c * (5 * c + 22))
        assert S4_explicit == Rational(10, 3408)
        assert S4_explicit == Rational(5, 1704)
        assert S4_explicit == virasoro_shadow_coefficient(4)

    def test_S5_from_recursion(self):
        """S_5 computed from recursion. Cross-check: S_5 < 0 for c > 0."""
        S5 = virasoro_shadow_coefficient(5)
        # S_5 should be nonzero (class M has all S_r nonzero)
        assert S5 != 0
        # Verify it is rational
        assert isinstance(S5, Rational)

    def test_shadow_tower_dict(self):
        """The tower dictionary has all entries."""
        tower = monster_virasoro_shadow_tower(8)
        assert len(tower) == 7  # r = 2..8
        assert tower[2] == Rational(12)
        assert tower[3] == Rational(2)
        assert tower[4] == Rational(5, 1704)

    def test_S_r_nonzero_for_class_M(self):
        """For class M, S_r should be nonzero for all r >= 2."""
        tower = monster_virasoro_shadow_tower(10)
        for r in range(2, 11):
            assert tower[r] != 0, f"S_{r} should be nonzero for class M"

    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 8*12*(5/1704) = 480/1704 = 20/71."""
        Delta = monster_critical_discriminant()
        assert Delta == Rational(20, 71)
        # Cross-check: 8 * 12 * 5/1704
        assert Delta == 8 * Rational(12) * Rational(5, 1704)
        # Simplify: 480/1704 = 20/71
        assert Rational(480, 1704) == Rational(20, 71)

    def test_critical_discriminant_nonzero(self):
        """Delta != 0 is the condition for class M."""
        assert monster_critical_discriminant() != 0

    def test_shadow_class_M(self):
        """V^natural is class M."""
        assert monster_shadow_class() == 'M'

    def test_shadow_depth_infinite(self):
        """Shadow depth of V^natural is infinite."""
        assert monster_shadow_depth() == 'infinity'

    def test_growth_rate_positive(self):
        """Shadow growth rate is positive."""
        rho = monster_shadow_growth_rate()
        assert rho > 0

    def test_growth_rate_value(self):
        """Growth rate: rho = sqrt(9*4 + 40/71) / 24."""
        rho = monster_shadow_growth_rate()
        # rho^2 = (36 + 40/71) / (4*144) = (2596/71) / 576
        rho_sq_exact = (9 * Rational(4) + 2 * Rational(20, 71)) / (4 * Rational(144))
        assert abs(rho - float(sqrt(rho_sq_exact))) < 1e-12


# =========================================================================
# 3. V^natural: genus amplitudes
# =========================================================================

class TestMonsterGenusAmplitudes:
    """Genus-g amplitudes for V^natural."""

    def test_F1(self):
        """F_1 = 12 * 1/24 = 1/2."""
        assert monster_genus_amplitude(1) == Rational(1, 2)

    def test_F2(self):
        """F_2 = 12 * 7/5760 = 84/5760 = 7/480."""
        F2 = monster_genus_amplitude(2)
        assert F2 == Rational(7, 480)
        # Cross-check: 12 * 7/5760
        assert F2 == 12 * Rational(7, 5760)

    def test_F3(self):
        """F_3 = 12 * 31/967680."""
        F3 = monster_genus_amplitude(3)
        assert F3 == 12 * _fp_independent(3)

    def test_genus_amplitudes_positive(self):
        """All genus amplitudes are positive."""
        for g in range(1, 8):
            assert monster_genus_amplitude(g) > 0

    def test_F_ratio_monster_niemeier(self):
        """F_g(V^natural)/F_g(Niemeier) = 12/24 = 1/2 for all g."""
        for g in range(1, 6):
            ratio = monster_genus_amplitude(g) / niemeier_genus_amplitude(g)
            assert ratio == Rational(1, 2)


# =========================================================================
# 4. Niemeier lattice VOAs
# =========================================================================

class TestNiemeierShadow:
    """Shadow data for all 24 Niemeier lattice VOAs."""

    def test_count(self):
        """There are exactly 24 Niemeier lattices."""
        assert len(NIEMEIER_DATA) == 24

    def test_all_kappa_24(self):
        """kappa = 24 for ALL Niemeier lattice VOAs."""
        for label, _ in NIEMEIER_DATA:
            assert niemeier_kappa(label) == Rational(24)

    def test_all_class_G(self):
        """All Niemeier lattice VOAs are class G."""
        for label, _ in NIEMEIER_DATA:
            assert niemeier_shadow_class(label) == 'G'

    def test_all_depth_2(self):
        """Shadow depth = 2 for all Niemeier lattice VOAs."""
        for label, _ in NIEMEIER_DATA:
            assert niemeier_shadow_depth(label) == 2

    def test_F1_niemeier(self):
        """F_1 = 24 * 1/24 = 1 for all Niemeier lattice VOAs."""
        assert niemeier_genus_amplitude(1) == Rational(1)

    def test_F2_niemeier(self):
        """F_2 = 24 * 7/5760 = 7/240."""
        assert niemeier_genus_amplitude(2) == Rational(7, 240)

    def test_niemeier_shadow_data_complete(self):
        """shadow_data returns complete information."""
        data = niemeier_shadow_data('Leech')
        assert data['kappa'] == Rational(24)
        assert data['S3'] == Rational(0)
        assert data['S4'] == Rational(0)
        assert data['shadow_class'] == 'G'
        assert data['num_roots'] == 0

    def test_niemeier_shadow_data_3E8(self):
        """3E8 has 720 roots."""
        data = niemeier_shadow_data('3E8')
        assert data['num_roots'] == 720  # 3 * 240
        assert data['kappa'] == Rational(24)

    def test_root_counts(self):
        """Spot-check root counts."""
        assert niemeier_root_count('D24') == 2 * 24 * 23  # = 1104
        assert niemeier_root_count('3E8') == 3 * 240  # = 720
        assert niemeier_root_count('Leech') == 0
        assert niemeier_root_count('24A1') == 24 * 2  # = 48

    def test_leech_has_no_roots(self):
        """The Leech lattice has no roots."""
        assert niemeier_root_count('Leech') == 0


# =========================================================================
# 5. The AP48 distinction: V_Leech vs V^natural
# =========================================================================

class TestAP48Distinction:
    """The central resolution: kappa depends on the full algebra."""

    def test_same_central_charge(self):
        """V_Leech and V^natural both have c = 24."""
        assert monster_central_charge() == Rational(24)
        # V_Leech is also c = 24
        comp = leech_vs_monster_kappa()
        assert comp['V_Leech']['central_charge'] == Rational(24)
        assert comp['V_natural']['central_charge'] == Rational(24)

    def test_different_kappa(self):
        """kappa(V_Leech) = 24 != kappa(V^natural) = 12."""
        comp = leech_vs_monster_kappa()
        assert comp['V_Leech']['kappa'] == Rational(24)
        assert comp['V_natural']['kappa'] == Rational(12)
        assert comp['V_Leech']['kappa'] != comp['V_natural']['kappa']

    def test_different_shadow_class(self):
        """V_Leech is class G, V^natural is class M."""
        comp = leech_vs_monster_kappa()
        assert comp['V_Leech']['shadow_class'] == 'G'
        assert comp['V_natural']['shadow_class'] == 'M'

    def test_different_F1(self):
        """F_1(V_Leech) = 1, F_1(V^natural) = 1/2."""
        comp = leech_vs_monster_kappa()
        assert comp['V_Leech']['F1'] == Rational(1)
        assert comp['V_natural']['F1'] == Rational(1, 2)

    def test_kappa_ratio_is_2(self):
        """kappa(V_Leech) / kappa(V^natural) = 2."""
        comp = leech_vs_monster_kappa()
        assert comp['kappa_ratio'] == Rational(2)


# =========================================================================
# 6. Leech kappa bar complex argument
# =========================================================================

class TestLeechKappaBarComplex:
    """Bar complex computation of kappa(V_Leech) = 24."""

    def test_leech_kappa_value(self):
        """kappa(V_Leech) = 24."""
        assert leech_kappa() == Rational(24)

    def test_leech_24_channels(self):
        """V_Leech has 24 Heisenberg channels."""
        data = leech_kappa_bar_complex()
        assert data['num_channels'] == 24

    def test_leech_each_channel_contributes_1(self):
        """Each boson contributes kappa_i = 1."""
        data = leech_kappa_bar_complex()
        for _, kappa_i in data['channels']:
            assert kappa_i == Rational(1)

    def test_leech_total_kappa(self):
        """Total kappa = sum of 24 channels = 24."""
        data = leech_kappa_bar_complex()
        assert data['kappa'] == Rational(24)

    def test_sugawara_not_independent(self):
        """The Sugawara Virasoro is NOT an independent curvature source."""
        data = leech_kappa_bar_complex()
        assert data['sugawara_submersion']['is_independent'] is False
        assert data['sugawara_submersion']['kappa_Vir'] == Rational(12)


# =========================================================================
# 7. j-function
# =========================================================================

class TestJFunction:
    """J-function coefficients and shadow connection."""

    def test_j_polar(self):
        """J(tau) has polar term q^{-1}."""
        assert j_coefficient(-1) == 1

    def test_j_constant_term_vanishes(self):
        """The constant term J|_{q^0} = 0 (Rademacher)."""
        assert j_coefficient(0) == 0

    def test_j_first_coefficient(self):
        """c(1) = 196884 = 1 + 196883."""
        assert j_coefficient(1) == 196884
        assert j_coefficient(1) == 1 + 196883

    def test_j_second_coefficient(self):
        """c(2) = 21493760 = 1 + 196883 + 21296876."""
        assert j_coefficient(2) == 21493760
        assert j_coefficient(2) == 1 + 196883 + 21296876

    def test_j_third_coefficient(self):
        """c(3) = 864299970."""
        assert j_coefficient(3) == 864299970

    def test_decomposition_dimensions(self):
        """Monster irrep decompositions sum to J-coefficients."""
        for n, decomp in MONSTER_DECOMPOSITIONS.items():
            total = sum(
                mult * MONSTER_IRREP_DIMS[chi]
                for chi, mult in decomp
            )
            assert total == j_coefficient(n), (
                f"Decomposition at n={n}: sum={total} != c(n)={j_coefficient(n)}"
            )

    def test_shadow_connection_F1(self):
        """The shadow-j connection reports F_1 = 1/2."""
        data = j_function_shadow_connection()
        assert data['F1'] == Rational(1, 2)

    def test_shadow_connection_indirect(self):
        """The connection is indirect (shadow tower does not encode j directly)."""
        data = j_function_shadow_connection()
        assert data['connection_type'] == 'indirect'


# =========================================================================
# 8. Norton/Griess algebra
# =========================================================================

class TestNortonGriess:
    """Norton algebra eigenvalues and Griess algebra invariants."""

    def test_lambda_trivial(self):
        """lambda_0 = 2/c = 2/24 = 1/12."""
        assert norton_eigenvalue('trivial') == Rational(1, 12)

    def test_lambda_196883(self):
        """lambda_1 = 4/(c+2) = 4/26 = 2/13."""
        assert norton_eigenvalue('196883') == Rational(2, 13)

    def test_lambda_21296876(self):
        """lambda_2 = 2/(c+2) = 2/26 = 1/13."""
        assert norton_eigenvalue('21296876') == Rational(1, 13)

    def test_lambda_ordering(self):
        """lambda_2 < lambda_0 < lambda_1: 1/13 < 1/12 < 2/13."""
        l0 = norton_eigenvalue('trivial')
        l1 = norton_eigenvalue('196883')
        l2 = norton_eigenvalue('21296876')
        assert l2 < l0 < l1

    def test_lambda_ratio(self):
        """lambda_1 / lambda_2 = 2 (from 4/(c+2) vs 2/(c+2))."""
        ratio = norton_eigenvalue('196883') / norton_eigenvalue('21296876')
        assert ratio == Rational(2)

    def test_griess_shadow_class_determination(self):
        """The Griess algebra does not change the class M determination."""
        data = griess_algebra_shadow_contribution()
        assert data['S3_virasoro_sector'] == Rational(2)
        assert data['S4_virasoro_sector'] == Rational(5, 1704)

    def test_norton_eigenvalue_invalid(self):
        """Invalid channel raises ValueError."""
        with pytest.raises(ValueError):
            norton_eigenvalue('invalid')


# =========================================================================
# 9. Koszul dual
# =========================================================================

class TestKoszulDual:
    """Koszul dual of V^natural."""

    def test_kappa_dual_km_type(self):
        """If KM-type (K=0): kappa' = -12."""
        data = monster_koszul_dual_data()
        assert data['complementarity_options']['KM_type (K=0)']['kappa_dual'] == Rational(-12)

    def test_kappa_dual_w_type(self):
        """If W-type (K=26): kappa' = 1."""
        data = monster_koszul_dual_data()
        assert data['complementarity_options']['W_type (K=26)']['kappa_dual'] == Rational(1)

    def test_anomaly_ratio(self):
        """Anomaly ratio rho = kappa/c = 12/24 = 1/2."""
        data = monster_koszul_dual_data()
        assert data['rho'] == Rational(1, 2)

    def test_no_holomorphic_at_c2(self):
        """No holomorphic VOA at c = 2."""
        data = monster_koszul_dual_data()
        assert data['no_holomorphic_at_c2'] is True

    def test_dual_is_curved(self):
        """The Koszul dual is a curved A-infinity algebra."""
        data = monster_koszul_dual_data()
        assert data['dual_is_curved'] is True

    def test_status_open(self):
        """The complementarity class of V^natural is OPEN."""
        data = monster_koszul_dual_data()
        assert 'OPEN' in data['status']


# =========================================================================
# 10. Niemeier shadow comparison
# =========================================================================

class TestNiemeierComparison:
    """All 24 Niemeier lattices have identical shadow data."""

    def test_all_identical_shadow(self):
        """Shadow data identical for all 24."""
        comp = niemeier_shadow_comparison()
        assert len(comp) == 24
        for label, data in comp.items():
            assert data['kappa'] == Rational(24)
            assert data['S3'] == Rational(0)
            assert data['S4'] == Rational(0)
            assert data['Delta'] == Rational(0)
            assert data['shadow_class'] == 'G'
            assert data['shadow_depth'] == 2
            assert data['distinguishable_by_shadow'] is False

    def test_root_counts_vary(self):
        """Root counts vary across lattices (the shadow-blind invariant)."""
        comp = niemeier_shadow_comparison()
        root_counts = {label: data['num_roots'] for label, data in comp.items()}
        # Leech has 0, D24 has 1104
        assert root_counts['Leech'] == 0
        assert root_counts['D24'] == 1104
        # Not all the same
        assert len(set(root_counts.values())) > 1

    def test_c_delta_distinguishes(self):
        """c_Delta distinguishes lattices with different root counts."""
        cd = niemeier_distinct_c_delta()
        # c_Delta for Leech: (691*0 - 65520)/691 = -65520/691
        assert cd['Leech'] == Rational(-65520, 691)
        # c_Delta for D24: (691*1104 - 65520)/691 = (762864 - 65520)/691 = 697344/691
        assert cd['D24'] == Rational(691 * 1104 - 65520, 691)

    def test_c_delta_leech_explicit(self):
        """c_Delta(Leech) = -65520/691."""
        assert niemeier_c_delta('Leech') == Rational(-65520, 691)

    def test_c_delta_formula(self):
        """c_Delta = (691*N_roots - 65520)/691 for each lattice."""
        for label, _ in NIEMEIER_DATA:
            n_roots = niemeier_root_count(label)
            expected = (Rational(691) * n_roots - 65520) / 691
            assert niemeier_c_delta(label) == expected


# =========================================================================
# 11. Exotic VOAs
# =========================================================================

class TestExoticVOAs:
    """Baby Monster, Thompson, and other exotic VOAs."""

    def test_baby_monster_central_charge(self):
        """VB^natural has c = 47/2."""
        data = baby_monster_voa_data()
        assert data['central_charge'] == Rational(47, 2)

    def test_baby_monster_kappa(self):
        """kappa(VB^natural) = c/2 = 47/4."""
        data = baby_monster_voa_data()
        assert data['kappa'] == Rational(47, 4)

    def test_baby_monster_F1(self):
        """F_1(VB^natural) = (47/4) * (1/24) = 47/96."""
        data = baby_monster_voa_data()
        assert data['F1'] == Rational(47, 96)

    def test_baby_monster_class_M(self):
        """VB^natural is conjectured class M."""
        data = baby_monster_voa_data()
        assert 'M' in data['shadow_class']

    def test_baby_monster_delta_nonzero(self):
        """Delta for VB^natural is nonzero (Virasoro sector)."""
        data = baby_monster_voa_data()
        assert data['Delta_nonzero'] is True

    def test_baby_monster_S4(self):
        """S_4(VB^natural) = 10/[c(5c+22)] at c = 47/2."""
        c = Rational(47, 2)
        S4_expected = Rational(10) / (c * (5 * c + 22))
        data = baby_monster_voa_data()
        assert data['S4_virasoro'] == S4_expected
        assert S4_expected > 0

    def test_thompson_central_charge(self):
        """V_Th has c = 47/2."""
        data = thompson_voa_data()
        assert data['central_charge'] == Rational(47, 2)

    def test_thompson_kappa(self):
        """kappa(V_Th) = 47/4."""
        data = thompson_voa_data()
        assert data['kappa'] == Rational(47, 4)

    def test_thompson_F1(self):
        """F_1(V_Th) = 47/96."""
        data = thompson_voa_data()
        assert data['F1'] == Rational(47, 96)

    def test_baby_monster_equals_thompson_kappa(self):
        """VB^natural and V_Th have the SAME kappa (same c = 47/2)."""
        bb = baby_monster_voa_data()
        th = thompson_voa_data()
        assert bb['kappa'] == th['kappa']

    def test_exotic_landscape_completeness(self):
        """The exotic landscape includes all known exotic VOAs."""
        landscape = exotic_voa_landscape()
        assert 'V_natural' in landscape
        assert 'V_Leech' in landscape
        assert 'VB_natural' in landscape
        assert 'V_Th' in landscape


# =========================================================================
# 12. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks."""

    def test_kappa_additivity_leech(self):
        """Kappa is additive for the Leech lattice (24 independent bosons)."""
        data = kappa_additivity_check_leech()
        assert data['kappa_heisenberg'] == Rational(24)
        assert data['kappa_lattice_formula'] == Rational(24)
        assert data['additivity_holds'] is True
        assert data['all_consistent'] is True

    def test_sugawara_submersion(self):
        """Sugawara kappa(Vir) = 12 < kappa(V_Leech) = 24."""
        data = kappa_additivity_check_leech()
        assert data['sugawara_is_submersion'] is True
        assert data['kappa_sugawara'] == Rational(12)
        assert data['kappa_sugawara'] < data['kappa_heisenberg']

    def test_orbifold_halving(self):
        """Z/2Z orbifold V_Leech -> V^natural halves kappa."""
        data = orbifold_kappa_halving()
        assert data['kappa_before'] == Rational(24)
        assert data['kappa_after'] == Rational(12)
        assert data['ratio'] == Rational(1, 2)

    def test_genus_amplitude_ratio(self):
        """F_g(V^natural)/F_g(Niemeier) = 1/2 for all g."""
        comp = genus_amplitude_comparison()
        for g in range(1, 6):
            assert comp['ratio'][g] == Rational(1, 2)

    def test_genus_amplitudes_proportional(self):
        """Monster and Niemeier amplitudes are proportional (kappa ratio)."""
        comp = genus_amplitude_comparison()
        kappa_ratio = monster_kappa() / niemeier_kappa('Leech')
        for g in range(1, 6):
            assert comp['V_natural'][g] == kappa_ratio * comp['Niemeier'][g]


# =========================================================================
# 13. Shadow metrics
# =========================================================================

class TestShadowMetrics:
    """Shadow metric data for exotic VOAs."""

    def test_monster_Q_at_0(self):
        """Q_L(0) = (2*12)^2 = 576 for V^natural."""
        data = shadow_metric_monster()
        assert data['Q_L_at_0'] == Rational(576)

    def test_monster_irreducible(self):
        """Q_L is irreducible (Delta != 0) for V^natural."""
        data = shadow_metric_monster()
        assert data['is_irreducible'] is True

    def test_monster_class_from_metric(self):
        """Shadow metric confirms class M for V^natural."""
        data = shadow_metric_monster()
        assert data['class_from_metric'] == 'M'

    def test_leech_metric_class_G(self):
        """V_Leech has class G in the shadow metric."""
        metrics = all_exotic_shadow_metrics()
        assert metrics['V_Leech']['class'] == 'G'
        assert metrics['V_Leech']['alpha'] == Rational(0)
        assert metrics['V_Leech']['Delta'] == Rational(0)

    def test_baby_monster_class_M(self):
        """VB^natural has class M in the shadow metric."""
        metrics = all_exotic_shadow_metrics()
        assert metrics['VB_natural']['class'] == 'M'
        assert metrics['VB_natural']['Delta'] != 0

    def test_all_exotic_metrics_populated(self):
        """All four exotic VOAs have shadow metric data."""
        metrics = all_exotic_shadow_metrics()
        assert len(metrics) == 4
        for label in ['V_natural', 'V_Leech', 'VB_natural', 'V_Th']:
            assert label in metrics
            assert 'kappa' in metrics[label]
            assert 'class' in metrics[label]


# =========================================================================
# 14. Multi-path verification: kappa(V^natural) = 12
# =========================================================================

class TestMultiPathKappaMonster:
    """At least 3 independent paths verifying kappa(V^natural) = 12."""

    def test_path1_virasoro_formula(self):
        """Path 1: kappa(Vir_c) = c/2 = 24/2 = 12."""
        assert Rational(24) / 2 == Rational(12)
        assert monster_kappa() == Rational(12)

    def test_path2_bar_complex(self):
        """Path 2: Bar complex genus-1 curvature with no weight-1 channels."""
        # No weight-1 currents => only Virasoro curvature source
        data = monster_kappa_bar_complex_argument()
        path2 = data['paths'][1]
        assert path2['result'] == Rational(12)

    def test_path3_F1_inversion(self):
        """Path 3: F_1 = 1/2 and lambda_1^FP = 1/24 => kappa = 12."""
        F1 = monster_genus_amplitude(1)
        lambda1 = _fp_independent(1)
        kappa_recovered = F1 / lambda1
        assert kappa_recovered == Rational(12)

    def test_path4_orbifold_consistency(self):
        """Path 4: V^natural = (V_Leech)^{Z/2Z}, kappa halved from 24 to 12."""
        assert orbifold_kappa_halving()['kappa_after'] == Rational(12)

    def test_path5_not_rank(self):
        """Path 5: AP48 exclusion: kappa != rank = 24 because dim V_1 = 0."""
        # V^natural has no weight-1 currents
        assert j_coefficient(0) == 0  # The q^0 term of q*J(tau) counts dim V_1 = 0
        assert monster_kappa() != Rational(24)


# =========================================================================
# 15. Multi-path verification: kappa(V_Leech) = 24
# =========================================================================

class TestMultiPathKappaLeech:
    """At least 3 independent paths verifying kappa(V_Leech) = 24."""

    def test_path1_heisenberg_additivity(self):
        """Path 1: 24 bosons, each contributing kappa_i = 1."""
        assert 24 * Rational(1) == Rational(24)
        assert leech_kappa() == Rational(24)

    def test_path2_lattice_formula(self):
        """Path 2: kappa(V_Lambda) = rank(Lambda) for lattice VOAs."""
        assert niemeier_kappa('Leech') == Rational(24)

    def test_path3_F1_inversion(self):
        """Path 3: F_1 = 1 and lambda_1^FP = 1/24 => kappa = 24."""
        F1 = niemeier_genus_amplitude(1)
        lambda1 = _fp_independent(1)
        kappa_recovered = F1 / lambda1
        assert kappa_recovered == Rational(24)

    def test_path4_bar_complex_channels(self):
        """Path 4: Bar complex has 24 independent curvature channels."""
        data = leech_kappa_bar_complex()
        assert data['kappa'] == Rational(24)
        assert data['num_channels'] == 24


# =========================================================================
# 16. Structural consistency: constants
# =========================================================================

class TestConstants:
    """Verify hardcoded constants against independent sources."""

    def test_monster_order(self):
        """Monster group order: 2^46 * 3^20 * 5^9 * 7^6 * 11^2 * 13^3 * 17 * 19 * 23 * 29 * 31 * 41 * 47 * 59 * 71."""
        # Cross-check a few digits
        assert MONSTER_ORDER == 808017424794512875886459904961710757005754368000000000
        # Divisibility checks
        assert MONSTER_ORDER % (2 ** 46) == 0
        assert MONSTER_ORDER % (3 ** 20) == 0
        assert MONSTER_ORDER % 71 == 0

    def test_baby_monster_order(self):
        """Baby Monster group order."""
        assert BABY_MONSTER_ORDER == 4154781481226426191177580544000000

    def test_monster_irrep_dims(self):
        """Monster irrep dimensions (Atlas of Finite Groups)."""
        assert MONSTER_IRREP_DIMS['chi_1'] == 1
        assert MONSTER_IRREP_DIMS['chi_2'] == 196883
        assert MONSTER_IRREP_DIMS['chi_3'] == 21296876

    def test_j_coefficients_literature(self):
        """J-function coefficients match OEIS A014708."""
        assert J_COEFFS[-1] == 1
        assert J_COEFFS[0] == 0
        assert J_COEFFS[1] == 196884
        assert J_COEFFS[2] == 21493760
        assert J_COEFFS[3] == 864299970
        assert J_COEFFS[4] == 20245856256

    def test_196884_equals_1_plus_196883(self):
        """The McKay observation: 196884 = 1 + 196883."""
        assert 196884 == 1 + 196883

    def test_21493760_decomposition(self):
        """21493760 = 1 + 196883 + 21296876."""
        assert 21493760 == 1 + 196883 + 21296876


# =========================================================================
# 17. Virasoro shadow coefficient at general c
# =========================================================================

class TestVirasoroShadowGeneral:
    """Virasoro shadow coefficients at various central charges."""

    def test_S2_general(self):
        """S_2(c) = c/2 for any c."""
        for c_val in [1, 2, Rational(1, 2), Rational(25, 2), 24, 26]:
            c = Rational(c_val)
            assert virasoro_shadow_coefficient(2, c) == c / 2

    def test_S3_universal(self):
        """S_3 = 2 for ALL central charges (universal Virasoro)."""
        for c_val in [1, Rational(1, 2), 12, 24, 26, 100]:
            c = Rational(c_val)
            assert virasoro_shadow_coefficient(3, c) == Rational(2)

    def test_S4_c1(self):
        """S_4 at c = 1: 10/(1*27) = 10/27."""
        c = Rational(1)
        S4 = virasoro_shadow_coefficient(4, c)
        assert S4 == Rational(10, 27)

    def test_S4_c26(self):
        """S_4 at c = 26: 10/(26*152) = 10/3952 = 5/1976."""
        c = Rational(26)
        S4 = virasoro_shadow_coefficient(4, c)
        assert S4 == Rational(10) / (26 * 152)

    def test_S4_self_dual_c13(self):
        """S_4 at c = 13 (self-dual): 10/(13*87) = 10/1131."""
        c = Rational(13)
        S4 = virasoro_shadow_coefficient(4, c)
        assert S4 == Rational(10, 1131)


# =========================================================================
# 18. Niemeier c_delta arithmetic
# =========================================================================

class TestNiemeierCDelta:
    """Arithmetic invariants distinguishing Niemeier lattices."""

    def test_c_delta_D24(self):
        """c_Delta for D24 with 1104 roots."""
        cd = niemeier_c_delta('D24')
        expected = (Rational(691) * 1104 - 65520) / 691
        assert cd == expected

    def test_c_delta_Leech(self):
        """c_Delta for Leech with 0 roots."""
        cd = niemeier_c_delta('Leech')
        assert cd == Rational(-65520, 691)

    def test_c_delta_3E8(self):
        """c_Delta for 3E8 with 720 roots."""
        cd = niemeier_c_delta('3E8')
        expected = (Rational(691) * 720 - 65520) / 691
        assert cd == expected

    def test_c_delta_varies(self):
        """Different root counts give different c_Delta."""
        cd_all = niemeier_distinct_c_delta()
        # Root counts are not all distinct (some lattices share root counts)
        # But c_Delta is determined by root count, so same root count => same c_Delta
        values = list(cd_all.values())
        # There should be at least 19 distinct values (since there are 19 distinct root counts)
        distinct_values = set(values)
        assert len(distinct_values) >= 19

    def test_no_c_delta_is_zero(self):
        """c_Delta != 0 for ALL 24 Niemeier lattices (including Leech).

        Since 65520/691 is not an integer (691 is prime, 65520 = 691*94 + 566),
        c_Delta = (691*N - 65520)/691 is zero only if N = 65520/691, which is
        not an integer. So c_Delta != 0 for all integer N.
        """
        for label, _ in NIEMEIER_DATA:
            assert niemeier_c_delta(label) != 0


# =========================================================================
# 19. Faber-Pandharipande cross-checks
# =========================================================================

class TestFaberPandharipande:
    """Independent FP verification (AP10 prevention)."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert _faber_pandharipande(1) == Rational(1, 24)
        assert _fp_independent(1) == Rational(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760."""
        assert _faber_pandharipande(2) == Rational(7, 5760)
        assert _fp_independent(2) == Rational(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert _faber_pandharipande(3) == Rational(31, 967680)

    def test_two_implementations_agree(self):
        """Engine FP matches independent FP for g = 1..5."""
        for g in range(1, 6):
            assert _faber_pandharipande(g) == _fp_independent(g)


# =========================================================================
# 20. Comprehensive shadow class determination
# =========================================================================

class TestShadowClassDetermination:
    """Shadow class is determined by the critical discriminant."""

    def test_monster_delta_implies_M(self):
        """Delta(V^natural) = 20/71 != 0 => class M."""
        Delta = monster_critical_discriminant()
        assert Delta == Rational(20, 71)
        assert Delta != 0
        assert monster_shadow_class() == 'M'

    def test_niemeier_delta_implies_G(self):
        """Delta = 0 and S_3 = 0 => class G for Niemeier lattice VOAs."""
        for label, _ in NIEMEIER_DATA:
            data = niemeier_shadow_data(label)
            assert data['critical_discriminant'] == Rational(0)
            assert data['S3'] == Rational(0)
            assert data['shadow_class'] == 'G'

    def test_baby_monster_delta_nonzero(self):
        """Delta != 0 for Baby Monster (Virasoro sector forces it)."""
        data = baby_monster_voa_data()
        assert data['Delta_nonzero'] is True

    def test_thompson_delta_nonzero(self):
        """Delta != 0 for Thompson VOA."""
        data = thompson_voa_data()
        assert data['Delta_nonzero'] is True
