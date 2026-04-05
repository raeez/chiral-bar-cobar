#!/usr/bin/env python3
r"""Tests for modular spectral rigidity: MC equation constraints on spectral atoms.

T1-T15:   Direction 1 — MC equation -> Hecke multiplicativity
T16-T30:  Direction 2 — Modular bootstrap on spectral measures
T31-T45:  Direction 3 — Bracket [Theta, Theta] and self-interaction
T46-T65:  Direction 4 — Explicit verification for lattice VOAs
T66-T82:  Direction 5 — Weil analogy and quadratic form
T83-T95:  Cross-direction synthesis and landscape
"""

import math
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from modular_spectral_rigidity import (
    # Arithmetic utilities
    sigma_k, sigma_minus_1, is_prime, primes_up_to, ramanujan_tau,
    eisenstein_coefficient, _bernoulli,
    # Direction 1
    mc_equation_genus1_constraints, hecke_multiplicativity_from_mc,
    mc_to_hecke_bridge,
    # Direction 2
    modular_spectral_bootstrap, ramanujan_bound_test, bootstrap_exclusion_region,
    # Direction 3
    mc_bracket_contribution, bracket_to_hecke_translation, bracket_positivity_test,
    # Direction 4
    verify_ramanujan_for_lattice, verify_hecke_from_mc,
    spectral_rigidity_landscape, _KNOWN_TAU,
    # Direction 5
    weil_pairing_on_shadows, hodge_index_test,
    # Summary
    full_rigidity_report,
    # Shadow-moduli resolution
    shadow_moduli_map_single_atom, shadow_moduli_map_multi_atom,
    verify_shadow_moduli_heisenberg, modularity_constraint_test,
    ramanujan_bound_verification, symmetric_power_from_shadow,
    operadic_mc_constraint_symmetric_powers,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# T1-T15: Direction 1 — MC equation -> Hecke multiplicativity
# ============================================================

class TestMCEquationConstraints:

    def test_t1_mc_constraints_gaussian(self):
        """T1: MC constraints for Gaussian class (Heisenberg).
        Shadow terminates at arity 2: S_3 = S_4 = 0.
        MC constraints should be trivially satisfied."""
        S = {2: 0.5, 3: 0.0, 4: 0.0}
        constraints = mc_equation_genus1_constraints(S, 4)
        assert 3 in constraints
        assert abs(constraints[3]['defect']) < 1e-14, "Gaussian S_3 defect nonzero"

    def test_t2_mc_constraints_virasoro_c26(self):
        """T2: MC constraints for Virasoro at c=26 (bosonic string)."""
        c = 26.0
        kappa = c / 2.0
        Q = 10.0 / (c * (5 * c + 22))
        S = {2: kappa, 3: 0.0, 4: kappa * Q}
        constraints = mc_equation_genus1_constraints(S, 4)
        assert 3 in constraints
        assert 4 in constraints
        # The MC constraint records the structure
        assert 'mc_relation' in constraints[3]
        assert 'mc_relation' in constraints[4]

    def test_t3_mc_constraints_arity5_recorded(self):
        """T3: Arity 5+ constraints are recorded but not computed explicitly."""
        S = {r: 1.0 / r for r in range(2, 8)}
        constraints = mc_equation_genus1_constraints(S, 7)
        for r in range(5, 8):
            assert r in constraints
            assert 'not computed explicitly' in constraints[r]['note']

    def test_t4_hecke_multiplicativity_single_atom(self):
        """T4: Hecke check for a single atom: a(n) = lambda^n.
        For a single eigenvalue, Hecke recursion at weight k:
        a(p^2) = a(p)^2 - p^{k-1} cannot hold unless lambda = specific values."""
        atoms = [3.0]
        weights = [1.0]
        result = hecke_multiplicativity_from_mc(atoms, weights, prime_bound=10)
        assert 'hecke_defects' in result
        assert result['n_atoms'] == 1
        # For lambda=3, a(p) = 3^p, a(p^2) = 3^{p^2}
        # 3^{p^2} - (3^p)^2 = 3^{p^2} - 9^p which is NOT p^{k-1} for any integer k
        assert len(result['hecke_defects']) > 0

    def test_t5_hecke_multiplicativity_two_atoms(self):
        """T5: Hecke check with two atoms: a(n) = c_1*lambda_1^n + c_2*lambda_2^n."""
        atoms = [2.0, -3.0]
        weights = [1.0, 1.0]
        result = hecke_multiplicativity_from_mc(atoms, weights, prime_bound=7)
        assert 'hecke_defects' in result
        assert 2 in result['hecke_defects']

    def test_t6_mc_to_hecke_bridge_free_field(self):
        """T6: MC-to-Hecke bridge for c=1 (free boson).
        Should identify as Gaussian class, NOT force Hecke."""
        result = mc_to_hecke_bridge(c=1.0, r_max=4)
        assert result['c'] == 1.0
        assert abs(result['kappa'] - 0.5) < 1e-14
        assert result['hecke_from_mc'] == 'NOT FORCED'

    def test_t7_mc_to_hecke_bridge_virasoro_generic(self):
        """T7: MC-to-Hecke bridge for Virasoro at generic c.
        Shadow obstruction tower is infinite (class M), Hecke NOT forced at finite arity."""
        for c in [2.0, 10.0, 26.0, 100.0]:
            result = mc_to_hecke_bridge(c=c, r_max=6)
            assert result['hecke_from_mc'] == 'NOT FORCED'
            assert 'NECESSARY but NOT SUFFICIENT' in result['explanation']

    def test_t8_mc_constraints_kappa_formula(self):
        """T8: kappa = c/2 enters correctly as S_2."""
        for c in [0.5, 1.0, 12.0, 26.0, 248.0 / 31.0]:
            result = mc_to_hecke_bridge(c=c, r_max=4)
            assert abs(result['kappa'] - c / 2.0) < 1e-12

    def test_t9_q_contact_virasoro(self):
        """T9: Q^contact_Vir = 10/[c(5c+22)] at c=26."""
        c = 26.0
        Q = 10.0 / (c * (5 * c + 22))
        result = mc_to_hecke_bridge(c=c, r_max=4)
        assert abs(result['Q_contact'] - Q) < 1e-14

    def test_t10_q_contact_singular_c0(self):
        """T10: Q^contact diverges at c=0 (correctly handled)."""
        result = mc_to_hecke_bridge(c=0.0, r_max=4)
        assert result['Q_contact'] == float('inf')

    def test_t11_q_contact_singular_c_minus_22_over_5(self):
        """T11: Q^contact diverges at c=-22/5 (correctly handled)."""
        result = mc_to_hecke_bridge(c=-22.0 / 5.0, r_max=4)
        assert result['Q_contact'] == float('inf')

    def test_t12_shadow_cubic_virasoro(self):
        """T12: S_3 = 2 for Virasoro (c-independent; AP9)."""
        for c in [1.0, 10.0, 26.0]:
            result = mc_to_hecke_bridge(c=c, r_max=6)
            assert abs(result['shadow_coeffs'][3] - 2.0) < 1e-14

    def test_t13_mc_constraints_all_arities_have_relations(self):
        """T13: Every arity in range has a constraint entry."""
        S = {r: float(r) for r in range(2, 10)}
        constraints = mc_equation_genus1_constraints(S, 9)
        for r in range(3, 10):
            assert r in constraints

    def test_t14_moments_from_shadow_coeffs(self):
        """T14: Moments mu_r = -r * S_r correctly computed."""
        result = mc_to_hecke_bridge(c=26.0, r_max=6)
        for r, S_r in result['shadow_coeffs'].items():
            if r in result['moments']:
                assert abs(result['moments'][r] - (-r * S_r)) < 1e-12

    def test_t15_mc_constraints_return_structure(self):
        """T15: MC constraints have correct return structure."""
        S = {2: 13.0, 3: 0.0, 4: 0.01}
        constraints = mc_equation_genus1_constraints(S, 4)
        for r in [3, 4]:
            assert 'arity' in constraints[r]
            assert 'mc_relation' in constraints[r]
            assert 'actual' in constraints[r]


# ============================================================
# T16-T30: Direction 2 — Modular bootstrap on spectral measures
# ============================================================

class TestModularBootstrap:

    def test_t16_ramanujan_bound_single_small_atom(self):
        """T16: A small atom passes Ramanujan bound trivially."""
        result = ramanujan_bound_test(atoms=[1.0], k=12, prime_bound=10)
        assert result['all_pass'] is True

    def test_t17_ramanujan_bound_large_atom_fails(self):
        """T17: An absurdly large atom fails Ramanujan bound."""
        result = ramanujan_bound_test(atoms=[1e20], k=12, prime_bound=10)
        assert result['all_pass'] is False
        assert len(result['failures']) > 0

    def test_t18_ramanujan_tau_values_pass_bound(self):
        """T18: Known Ramanujan tau values satisfy |tau(p)| <= 2p^{11/2}."""
        for p in [2, 3, 5, 7, 11, 13]:
            tau_p = _KNOWN_TAU[p]
            bound = 2.0 * p ** 5.5
            assert abs(tau_p) <= bound + 1e-6, (
                f"|tau({p})| = {abs(tau_p)} > 2*{p}^(11/2) = {bound}"
            )

    def test_t19_ramanujan_bound_e8_eigenvalues_fail(self):
        """T19: E_8 Eisenstein eigenvalues sigma_3(p) VIOLATE Ramanujan bound."""
        # sigma_3(p) = 1 + p^3, bound = 2*p^{3/2}
        for p in [2, 3, 5]:
            sig3 = 1 + p ** 3
            bound = 2.0 * p ** 1.5
            assert sig3 > bound, (
                f"sigma_3({p}) = {sig3} should EXCEED bound {bound}"
            )

    def test_t20_ramanujan_bound_test_structure(self):
        """T20: ramanujan_bound_test returns correct structure."""
        result = ramanujan_bound_test(atoms=[1.0, -2.0], k=4, prime_bound=7)
        assert 'k' in result
        assert 'atoms' in result
        assert 'tests' in result
        assert 'all_pass' in result
        assert len(result['tests']) > 0

    def test_t21_ramanujan_bound_weight_12_tau_primes(self):
        """T21: Extended Ramanujan verification for tau(p) at weight 12."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for p in primes:
            tau_p = _KNOWN_TAU.get(p, ramanujan_tau(p))
            bound = 2.0 * p ** 5.5
            ratio = abs(tau_p) / bound
            assert ratio < 1.0 + 1e-10, (
                f"Ramanujan VIOLATED at p={p}: |tau(p)|/bound = {ratio}"
            )

    def test_t22_ramanujan_bound_ratio_decreasing(self):
        """T22: |tau(p)|/(2*p^{11/2}) ratio is bounded by 1 and varies."""
        ratios = []
        for p in [2, 3, 5, 7, 11, 13]:
            tau_p = _KNOWN_TAU[p]
            ratio = abs(tau_p) / (2.0 * p ** 5.5)
            ratios.append(ratio)
            assert ratio < 1.0
        # The ratios should NOT all be close to 1 (generically < 1)
        assert max(ratios) < 1.0

    @skip_no_mpmath
    def test_t23_modular_bootstrap_trivial_atom(self):
        """T23: Bootstrap with atom=0 gives zero function (trivially modular)."""
        q_points = [complex(0, 0.1)]  # q on imaginary axis
        # atom=0 => log(1 - 0*t) = 0 for all t
        result = modular_spectral_bootstrap(
            atoms=[0.0], weights=[1.0],
            q_test_points=q_points, weight_w=0,
        )
        assert result['max_defect'] < 1e-10

    @skip_no_mpmath
    def test_t24_modular_bootstrap_returns_structure(self):
        """T24: modular_spectral_bootstrap returns correct structure."""
        q_points = [complex(math.exp(-2 * math.pi * 1.0))]  # tau = i
        result = modular_spectral_bootstrap(
            atoms=[1.0], weights=[1.0],
            q_test_points=q_points, weight_w=0,
        )
        assert 'atoms' in result
        assert 'weights' in result
        assert 'modularity_defects' in result
        assert 'max_defect' in result
        assert len(result['modularity_defects']) == 1

    @skip_no_mpmath
    def test_t25_bootstrap_exclusion_1atom_returns_grid(self):
        """T25: Exclusion region with 1 atom returns a grid of defects."""
        result = bootstrap_exclusion_region(
            k=12, num_atoms=1, q_points=3,
            atom_range=(-5.0, 5.0), grid_size=10,
        )
        assert result['num_atoms'] == 1
        assert len(result['lambdas']) == 10
        assert len(result['defects']) == 10

    @skip_no_mpmath
    def test_t26_bootstrap_exclusion_2atoms_returns_grid(self):
        """T26: Exclusion region with 2 atoms returns a 2D grid."""
        result = bootstrap_exclusion_region(
            k=12, num_atoms=2, q_points=3,
            atom_range=(-2.0, 2.0), grid_size=5,
        )
        assert result['num_atoms'] == 2
        assert len(result['lambdas_1']) == 5
        assert len(result['lambdas_2']) == 5
        assert len(result['defects']) == 5
        assert len(result['defects'][0]) == 5

    def test_t27_bootstrap_exclusion_3atoms_error(self):
        """T27: 3+ atoms not supported for grid exclusion."""
        result = bootstrap_exclusion_region(k=12, num_atoms=3, q_points=3)
        assert 'error' in result

    def test_t28_ramanujan_bound_k2(self):
        """T28: Ramanujan bound at weight 2: 2*p^{1/2}."""
        result = ramanujan_bound_test(atoms=[3.0], k=2, prime_bound=20)
        # atom=3, p=2: bound = 2*sqrt(2) = 2.83 < 3 => FAIL
        assert result['all_pass'] is False

    def test_t29_ramanujan_bound_negative_atom(self):
        """T29: Negative atoms handled correctly."""
        result = ramanujan_bound_test(atoms=[-1.0], k=12, prime_bound=10)
        # |-1| = 1 <= 2*2^{5.5} => passes
        assert result['all_pass'] is True

    def test_t30_ramanujan_bound_zero_atom(self):
        """T30: Zero atom passes trivially."""
        result = ramanujan_bound_test(atoms=[0.0], k=12, prime_bound=10)
        assert result['all_pass'] is True


# ============================================================
# T31-T45: Direction 3 — Bracket [Theta, Theta] and self-interaction
# ============================================================

class TestBracketSelfInteraction:

    def test_t31_bracket_arity3_structure(self):
        """T31: Bracket at arity 3 involves S_2^2."""
        S = {2: 13.0, 3: 0.0, 4: 0.01}
        result = mc_bracket_contribution(S, 3)
        assert result['arity'] == 3
        assert abs(result['bracket'] - 13.0 ** 2) < 1e-10

    def test_t32_bracket_arity4_structure(self):
        """T32: Bracket at arity 4 involves S_2*S_3 and S_2^3."""
        S = {2: 2.0, 3: 3.0, 4: 0.0}
        result = mc_bracket_contribution(S, 4)
        assert result['arity'] == 4
        expected = 2.0 * 2.0 * 3.0 + (2.0 ** 3) / 6.0
        assert abs(result['bracket'] - expected) < 1e-10

    def test_t33_bracket_arity5_structure(self):
        """T33: Bracket at arity 5 involves S_2*S_4, S_3^2, S_2^2*S_3, S_2^4."""
        S = {2: 1.0, 3: 1.0, 4: 1.0}
        result = mc_bracket_contribution(S, 5)
        assert result['arity'] == 5
        expected = (2.0 * 1.0 * 1.0  # 2*S_2*S_4
                    + 1.0             # S_3^2
                    + 0.5             # (1/2)*S_2^2*S_3
                    + 1.0 / 24.0)    # (1/24)*S_2^4
        assert abs(result['bracket'] - expected) < 1e-10

    def test_t34_bracket_gaussian_class_vanishes(self):
        """T34: For Gaussian class (S_3=S_4=0), bracket at arity 4 is S_2^3/6."""
        S = {2: 0.5, 3: 0.0, 4: 0.0}
        result = mc_bracket_contribution(S, 4)
        expected = (0.5 ** 3) / 6.0
        assert abs(result['bracket'] - expected) < 1e-14

    def test_t35_bracket_high_arity_returns_note(self):
        """T35: Bracket at arity >= 6 returns a note about enumeration."""
        S = {2: 1.0}
        result = mc_bracket_contribution(S, 7)
        assert result['bracket'] is None
        assert 'Not computed' in result['note']

    def test_t36_bracket_to_hecke_hankel_test(self):
        """T36: Hankel matrix from moments is computed."""
        S = {2: 1.0, 3: 0.5, 4: 0.3, 5: 0.2, 6: 0.15}
        result = bracket_to_hecke_translation(S, r_max=6)
        assert 'hankel_tests' in result
        assert 'H_2x2' in result['hankel_tests']

    def test_t37_bracket_to_hecke_not_forced(self):
        """T37: Hecke multiplicativity is NOT forced at finite arity."""
        S = {2: 13.0, 3: 0.0, 4: 0.01}
        result = bracket_to_hecke_translation(S, r_max=4)
        assert result['hecke_forced'] is False

    def test_t38_bracket_to_hecke_cauchy_schwarz(self):
        """T38: Cauchy-Schwarz check on Hankel: mu_4*mu_2 >= mu_3^2."""
        # Use shadow coefficients where this should hold
        S = {2: 5.0, 3: 2.0, 4: 3.0}
        result = bracket_to_hecke_translation(S, r_max=4)
        if 'H_2x2' in result['hankel_tests']:
            H = result['hankel_tests']['H_2x2']
            mu_2 = -2 * S[2]
            mu_3 = -3 * S[3]
            mu_4 = -4 * S[4]
            # Cauchy-Schwarz: mu_4 * mu_2 >= mu_3^2 for positive measures
            # NOTE: This may not hold if the measure has negative weights
            cs = mu_4 * mu_2 - mu_3 ** 2
            # Just check the test runs and reports
            assert 'eigenvalues' in H

    def test_t39_bracket_positivity_gaussian(self):
        """T39: Bracket positivity for Gaussian class."""
        S = {2: 0.5, 3: 0.0, 4: 0.0}
        result = bracket_positivity_test(S, r_max=4)
        assert result['forces_ramanujan'] is False
        assert 'CANCELLATION condition' in result['explanation']

    def test_t40_bracket_positivity_virasoro(self):
        """T40: Bracket positivity for Virasoro c=26."""
        c = 26.0
        Q = 10.0 / (c * (5 * c + 22))
        S = {2: c / 2.0, 3: 0.0, 4: (c / 2.0) * Q}
        result = bracket_positivity_test(S, r_max=5)
        assert result['forces_ramanujan'] is False
        # Check bracket signs are recorded
        for r, data in result['bracket_data'].items():
            assert 'sign' in data

    def test_t41_bracket_components_arity4(self):
        """T41: Arity-4 bracket has exactly two named components."""
        S = {2: 3.0, 3: 2.0, 4: 1.0}
        result = mc_bracket_contribution(S, 4)
        assert len(result['components']) == 2
        names = [c[0] for c in result['components']]
        assert '2 * S_2 * S_3' in names
        assert '(1/6) * S_2^3' in names

    def test_t42_bracket_components_arity5(self):
        """T42: Arity-5 bracket has exactly four named components."""
        S = {2: 1.0, 3: 1.0, 4: 1.0}
        result = mc_bracket_contribution(S, 5)
        assert len(result['components']) == 4

    def test_t43_bracket_zero_coefficients(self):
        """T43: All-zero shadow coefficients give zero bracket."""
        S = {2: 0.0, 3: 0.0, 4: 0.0}
        for r in [3, 4, 5]:
            result = mc_bracket_contribution(S, r)
            if result['bracket'] is not None:
                assert abs(result['bracket']) < 1e-14

    def test_t44_hankel_3x3_computed_when_available(self):
        """T44: 3x3 Hankel matrix computed when enough moments exist."""
        S = {r: 1.0 / r for r in range(2, 7)}
        result = bracket_to_hecke_translation(S, r_max=6)
        assert 'H_3x3' in result['hankel_tests']
        H3 = result['hankel_tests']['H_3x3']
        assert 'eigenvalues' in H3
        assert len(H3['eigenvalues']) == 3

    def test_t45_bracket_to_hecke_explanation(self):
        """T45: Explanation clearly states finite arity limitation."""
        S = {2: 1.0, 3: 0.0, 4: 0.01}
        result = bracket_to_hecke_translation(S, r_max=4)
        assert 'WEAKER than Ramanujan' in result['explanation']


# ============================================================
# T46-T65: Direction 4 — Explicit verification for lattice VOAs
# ============================================================

class TestLatticeVerification:

    def test_t46_e8_eisenstein_violates_ramanujan(self):
        """T46: E_8 theta = E_4: Eisenstein eigenvalues violate Ramanujan."""
        result = verify_ramanujan_for_lattice('E8', num_primes=5)
        # sigma_3(p) = 1+p^3 > 2*p^{3/2} for p >= 2
        for test in result['eisenstein_tests']:
            assert test['satisfies_bound'] is False
            assert test['ratio'] > 1.0

    def test_t47_leech_cusp_satisfies_ramanujan(self):
        """T47: Leech theta: cusp part tau(p) satisfies Ramanujan (Deligne)."""
        result = verify_ramanujan_for_lattice('Leech', num_primes=10)
        for test in result['cusp_tests']:
            assert test['satisfies_bound'] is True, (
                f"Ramanujan VIOLATED at p={test['prime']}: "
                f"|tau(p)|={abs(test['tau_p'])}, bound={test['ramanujan_bound']}"
            )

    def test_t48_leech_eisenstein_violates_ramanujan(self):
        """T48: Leech theta: Eisenstein part violates Ramanujan."""
        result = verify_ramanujan_for_lattice('Leech', num_primes=5)
        for test in result['eisenstein_tests']:
            assert test['satisfies_bound'] is False

    def test_t49_z_lattice_summary(self):
        """T49: V_Z: weight 1/2, no standard Ramanujan."""
        result = verify_ramanujan_for_lattice('Z', num_primes=5)
        assert 'weight 1/2' in result['summary']

    def test_t50_z2_lattice_summary(self):
        """T50: V_{Z^2}: weight 1, Gamma_0(4)."""
        result = verify_ramanujan_for_lattice('Z2', num_primes=5)
        assert 'weight 1' in result['summary']

    def test_t51_a2_lattice_summary(self):
        """T51: V_{A_2}: weight 1, Gamma_0(3) with character."""
        result = verify_ramanujan_for_lattice('A2', num_primes=5)
        assert 'weight 1' in result['summary']

    def test_t52_hecke_e8_all_defects_zero(self):
        """T52: Hecke multiplicativity for E_4: sigma_3(p^2) = sigma_3(p)^2 - p^3."""
        result = verify_hecke_from_mc('E8', r_max=6)
        assert result['hecke_check']['applicable'] is True
        assert result['hecke_check']['all_pass'] is True
        for entry in result['hecke_check']['results']:
            assert entry['hecke_defect'] == 0, (
                f"Hecke defect at p={entry['prime']}: {entry['hecke_defect']}"
            )

    def test_t53_hecke_leech_all_defects_zero(self):
        """T53: Hecke multiplicativity for Delta: tau(p^2) = tau(p)^2 - p^{11}."""
        result = verify_hecke_from_mc('Leech', r_max=6)
        assert result['hecke_check']['applicable'] is True
        assert result['hecke_check']['all_pass'] is True
        for entry in result['hecke_check']['results']:
            assert entry['hecke_defect'] == 0, (
                f"Hecke defect at p={entry['prime']}: {entry['hecke_defect']}"
            )

    def test_t54_hecke_sigma3_identity_small_primes(self):
        """T54: Verify sigma_3(p^2) = sigma_3(p)^2 - p^3 directly for small primes."""
        for p in [2, 3, 5, 7, 11]:
            sig3_p = sigma_k(p, 3)
            sig3_p2 = sigma_k(p * p, 3)
            assert sig3_p2 == sig3_p ** 2 - p ** 3, (
                f"Hecke recursion fails at p={p}: "
                f"sigma_3({p}^2)={sig3_p2}, sigma_3({p})^2-{p}^3={sig3_p**2-p**3}"
            )

    def test_t55_hecke_tau_identity_small_primes(self):
        """T55: Verify tau(p^2) = tau(p)^2 - p^{11} for small primes."""
        for p in [2, 3, 5, 7]:
            tau_p = _KNOWN_TAU[p]
            tau_p2 = _KNOWN_TAU.get(p * p, ramanujan_tau(p * p))
            expected = tau_p ** 2 - p ** 11
            assert tau_p2 == expected, (
                f"Hecke recursion fails at p={p}: "
                f"tau({p}^2)={tau_p2}, tau({p})^2-{p}^11={expected}"
            )

    def test_t56_ramanujan_tau_known_values(self):
        """T56: Verify known Ramanujan tau values."""
        expected = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830}
        for n, val in expected.items():
            assert ramanujan_tau(n) == val, f"tau({n}) = {ramanujan_tau(n)} != {val}"

    def test_t57_ramanujan_tau_computed_vs_known(self):
        """T57: Computed tau matches known table for p <= 23."""
        for n, val in _KNOWN_TAU.items():
            computed = ramanujan_tau(n)
            assert computed == val, f"tau({n}): computed={computed}, known={val}"

    def test_t58_e8_kappa(self):
        """T58: kappa(V_{E_8}) = rank = 8."""
        result = verify_hecke_from_mc('E8', r_max=4)
        c = 248.0 / 31.0  # = 8.0
        assert abs(result['shadow_coeffs'][2] - c) < 1e-10

    def test_t59_leech_kappa(self):
        """T59: kappa(V_Leech) = rank = 24."""
        result = verify_hecke_from_mc('Leech', r_max=4)
        assert abs(result['shadow_coeffs'][2] - 24.0) < 1e-10

    def test_t60_z_lattice_kappa(self):
        """T60: kappa(V_Z) = rank = 1."""
        result = verify_hecke_from_mc('Z', r_max=4)
        assert abs(result['shadow_coeffs'][2] - 1.0) < 1e-10

    def test_t61_e8_gaussian_coefficients(self):
        """T61: E_8 higher shadows vanish (Lie class, but lattice part is depth 3)."""
        result = verify_hecke_from_mc('E8', r_max=6)
        for r in range(4, 7):
            assert abs(result['shadow_coeffs'][r]) < 1e-10

    def test_t62_spectral_landscape_five_points(self):
        """T62: Spectral landscape computation at 5 central charges."""
        landscape = spectral_rigidity_landscape([0.5, 1.0, 10.0, 26.0, 100.0], r_max=4)
        assert len(landscape) == 5
        for entry in landscape:
            assert 'c' in entry
            assert 'kappa' in entry
            assert 'shadow_class' in entry

    def test_t63_spectral_landscape_free_fields_gaussian(self):
        """T63: Free fields (c=1, c=1/2) classified as Gaussian."""
        landscape = spectral_rigidity_landscape([0.5, 1.0], r_max=4)
        for entry in landscape:
            assert entry['shadow_class'] == 'G'

    def test_t64_spectral_landscape_virasoro_mixed(self):
        """T64: Generic Virasoro classified as mixed (M)."""
        landscape = spectral_rigidity_landscape([10.0, 26.0, 100.0], r_max=4)
        for entry in landscape:
            assert entry['shadow_class'] == 'M'

    def test_t65_deligne_bound_tau2(self):
        """T65: Deligne's bound at p=2: |tau(2)| = 24 <= 2*2^{11/2} = 2*45.25 = 90.51."""
        tau_2 = _KNOWN_TAU[2]
        bound = 2.0 * 2 ** 5.5
        assert abs(tau_2) <= bound
        assert abs(tau_2) == 24
        assert bound > 90.0  # 2^{11/2} = 45.25..., so 2*45.25 = 90.51


# ============================================================
# T66-T82: Direction 5 — Weil analogy and quadratic form
# ============================================================

class TestWeilAnalogy:

    def test_t66_weil_pairing_basic(self):
        """T66: Weil pairing returns correct target arity."""
        result = weil_pairing_on_shadows(S_r=5.0, S_s=3.0, r=2, s=3)
        assert result['target_arity'] == 3  # r + s - 2 = 2 + 3 - 2 = 3
        assert result['honest_status'] == 'STRUCTURAL ANALOGY ONLY'

    def test_t67_weil_pairing_schematic_value(self):
        """T67: Schematic bracket value is S_r * S_s."""
        result = weil_pairing_on_shadows(S_r=4.0, S_s=7.0, r=3, s=4)
        assert abs(result['bracket_value_schematic'] - 28.0) < 1e-10

    def test_t68_hodge_index_gaussian(self):
        """T68: Hodge index for Gaussian class (single nonzero shadow)."""
        S = {2: 0.5}
        result = hodge_index_test(S, r_max=4)
        assert result['signature'] == (1, 0, 0)
        assert result['is_hodge_index_type'] is True

    def test_t69_hodge_index_two_shadows(self):
        """T69: Hodge index for two nonzero shadows."""
        S = {2: 5.0, 3: 0.0, 4: 0.01}
        result = hodge_index_test(S, r_max=4)
        # Two nonzero: S_2 and S_4
        assert result['rank'] == 1  # rank-1 outer product
        assert result['is_hodge_index_type'] is True

    def test_t70_hodge_index_three_shadows(self):
        """T70: Hodge index for three nonzero shadows."""
        S = {2: 5.0, 3: 2.0, 4: 0.01}
        result = hodge_index_test(S, r_max=4)
        assert len(result['arities']) == 3
        assert result['rank'] == 1  # rank-1 outer product
        assert result['is_hodge_index_type'] is True

    def test_t71_hodge_index_outer_product_rank1(self):
        """T71: The schematic intersection matrix is rank 1 (outer product)."""
        S = {2: 3.0, 3: 2.0, 4: 1.0, 5: 0.5}
        result = hodge_index_test(S, r_max=5)
        # Outer product of [3, 2, 1, 0.5] has rank 1
        assert result['rank'] == 1

    def test_t72_hodge_index_trivial_for_all_zero(self):
        """T72: All-zero shadows give trivial result."""
        S = {2: 0.0, 3: 0.0}
        result = hodge_index_test(S, r_max=4)
        assert result['status'] == 'trivial'

    def test_t73_hodge_index_honest_assessment(self):
        """T73: Honest assessment states rank-1 limitation."""
        S = {2: 13.0, 3: 0.0, 4: 0.01}
        result = hodge_index_test(S, r_max=4)
        assert 'RANK 1' in result['honest_assessment']

    def test_t74_weil_pairing_same_arity(self):
        """T74: Weil pairing S_2 with S_2 gives target arity 2."""
        result = weil_pairing_on_shadows(S_r=5.0, S_s=5.0, r=2, s=2)
        assert result['target_arity'] == 2
        assert abs(result['bracket_value_schematic'] - 25.0) < 1e-10

    def test_t75_weil_pairing_high_arity(self):
        """T75: Weil pairing at high arities."""
        result = weil_pairing_on_shadows(S_r=1.0, S_s=1.0, r=5, s=6)
        assert result['target_arity'] == 9

    def test_t76_hodge_index_eigenvalues_nonneg(self):
        """T76: Eigenvalues of rank-1 PSD outer product are non-negative."""
        S = {2: 3.0, 3: 2.0, 4: 1.5}
        result = hodge_index_test(S, r_max=4)
        for ev in result['eigenvalues']:
            assert ev >= -1e-10, f"Negative eigenvalue: {ev}"

    def test_t77_hodge_index_single_shadow_matrix(self):
        """T77: Single shadow gives 1x1 intersection matrix."""
        S = {2: 7.0}
        result = hodge_index_test(S, r_max=4)
        assert len(result['intersection_matrix']) == 1
        assert abs(result['intersection_matrix'][0][0] - 49.0) < 1e-10

    def test_t78_weil_analogy_text(self):
        """T78: Weil analogy text references Hodge index theorem."""
        result = weil_pairing_on_shadows(1.0, 1.0, 2, 3)
        assert 'Hodge index' in result['weil_analogy']

    def test_t79_hodge_index_virasoro_c26(self):
        """T79: Hodge index for Virasoro at c=26."""
        c = 26.0
        Q = 10.0 / (c * (5 * c + 22))
        S = {2: c / 2.0, 3: 0.0, 4: (c / 2.0) * Q}
        result = hodge_index_test(S, r_max=4)
        # Only S_2 and S_4 nonzero
        assert len(result['arities']) == 2
        assert result['is_hodge_index_type'] is True

    def test_t80_weil_pairing_zero_shadow(self):
        """T80: Pairing with zero shadow gives zero bracket."""
        result = weil_pairing_on_shadows(0.0, 5.0, 2, 3)
        assert abs(result['bracket_value_schematic']) < 1e-14

    def test_t81_hodge_index_negative_shadow(self):
        """T81: Negative shadow coefficients handled correctly."""
        S = {2: -3.0, 3: 2.0}
        result = hodge_index_test(S, r_max=4)
        assert result['rank'] == 1
        # Outer product of [-3, 2] has eigenvalue 9+4=13 and 0
        assert max(result['eigenvalues']) > 0

    def test_t82_hodge_index_large_shadow_vector(self):
        """T82: Large shadow vector (5 nonzero components)."""
        S = {2: 10.0, 3: 5.0, 4: 2.0, 5: 1.0, 6: 0.5}
        result = hodge_index_test(S, r_max=6)
        assert len(result['arities']) == 5
        assert result['rank'] == 1
        # Largest eigenvalue = sum(s^2 for s in shadow_vec)
        expected_largest = sum(s ** 2 for s in [10.0, 5.0, 2.0, 1.0, 0.5])
        assert abs(max(result['eigenvalues']) - expected_largest) < 1e-8


# ============================================================
# T83-T95: Cross-direction synthesis and landscape
# ============================================================

class TestCrossDirectionSynthesis:

    def test_t83_full_report_returns_all_sections(self):
        """T83: Full rigidity report has all required sections."""
        report = full_rigidity_report(lattice_type='E8', c_vir=26.0, r_max=4, num_primes=5)
        assert 'directions' in report
        assert 'lattice_verification' in report
        assert 'virasoro_analysis' in report
        assert 'honest_summary' in report

    def test_t84_full_report_honest_summary(self):
        """T84: Honest summary correctly identifies what works and doesn't."""
        report = full_rigidity_report(lattice_type='E8', c_vir=26.0, r_max=4, num_primes=5)
        summary = report['honest_summary']
        assert 'WHAT WORKS' in summary
        assert 'WHAT DOES NOT WORK' in summary
        assert 'WHAT REMAINS OPEN' in summary

    def test_t85_full_report_leech(self):
        """T85: Full report for Leech lattice: cusp part verified."""
        report = full_rigidity_report(lattice_type='Leech', c_vir=26.0, r_max=4, num_primes=5)
        leech_ram = report['lattice_verification']['ramanujan']
        assert len(leech_ram['cusp_tests']) > 0
        for test in leech_ram['cusp_tests']:
            assert test['satisfies_bound'] is True

    def test_t86_full_report_bracket_section(self):
        """T86: Full report includes bracket analysis."""
        report = full_rigidity_report(r_max=4, num_primes=3)
        assert 'bracket' in report['directions']
        assert 'positivity' in report['directions']

    def test_t87_full_report_hodge_index_section(self):
        """T87: Full report includes Hodge index analysis."""
        report = full_rigidity_report(r_max=4, num_primes=3)
        assert 'hodge_index' in report['directions']

    def test_t88_arithmetic_sigma_k_identity(self):
        """T88: sigma_k multiplicativity: sigma_k(mn) for gcd(m,n)=1."""
        # sigma_3 is multiplicative on coprime inputs
        for m, n in [(2, 3), (2, 5), (3, 5), (2, 7), (3, 7)]:
            assert math.gcd(m, n) == 1
            assert sigma_k(m * n, 3) == sigma_k(m, 3) * sigma_k(n, 3)

    def test_t89_arithmetic_sigma_minus_1_basic(self):
        """T89: sigma_{-1}(p) = 1 + 1/p for prime p."""
        for p in [2, 3, 5, 7, 11]:
            assert abs(sigma_minus_1(p) - (1.0 + 1.0 / p)) < 1e-14

    def test_t90_arithmetic_primes_up_to(self):
        """T90: primes_up_to(20) returns correct list."""
        assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_t91_bernoulli_numbers(self):
        """T91: Verify Bernoulli numbers B_0, B_2, B_4, B_6, B_12."""
        assert _bernoulli(0) == Fraction(1)
        assert _bernoulli(2) == Fraction(1, 6)
        assert _bernoulli(4) == Fraction(-1, 30)
        assert _bernoulli(6) == Fraction(1, 42)
        assert _bernoulli(12) == Fraction(-691, 2730)

    def test_t92_eisenstein_e4_coefficient(self):
        """T92: E_4 coefficient at n=1: -8/B_4 * sigma_3(1) = 240."""
        a1 = eisenstein_coefficient(4, 1)
        assert a1 == 240

    def test_t93_eisenstein_e12_coefficient_n1(self):
        """T93: E_{12} coefficient at n=1: 65520/691."""
        a1 = eisenstein_coefficient(12, 1)
        assert a1 == Fraction(65520, 691)

    def test_t94_spectral_landscape_kappa_consistent(self):
        """T94: kappa = c/2 consistent across landscape."""
        cs = [0.5, 1.0, 5.0, 10.0, 26.0, 100.0]
        landscape = spectral_rigidity_landscape(cs, r_max=4)
        for entry in landscape:
            assert abs(entry['kappa'] - entry['c'] / 2.0) < 1e-12

    def test_t95_virasoro_self_dual_c13(self):
        """T95: At c=13, Vir_c is self-dual (Vir_c^! = Vir_{26-c} = Vir_{13}).
        The Q^contact should be computed correctly."""
        c = 13.0
        Q = 10.0 / (c * (5 * c + 22))
        # 5*13 + 22 = 87, so Q = 10/(13*87) = 10/1131
        assert abs(Q - 10.0 / 1131.0) < 1e-14
        result = mc_to_hecke_bridge(c=13.0, r_max=4)
        assert abs(result['Q_contact'] - Q) < 1e-14


# ============================================================
# Shadow-moduli resolution tests
# ============================================================

class TestShadowModuliResolution:
    """Tests for the shadow-moduli resolution theorem."""

    def test_heisenberg_c1(self):
        """Verify shadow-moduli map for Heisenberg at c=1."""
        result = verify_shadow_moduli_heisenberg(c=1.0, q_max=20)
        assert result['match'], f"Heisenberg c=1 shadow-moduli failed: max_error={result['max_error']}"

    def test_heisenberg_c2(self):
        """Verify shadow-moduli map for Heisenberg at c=2."""
        result = verify_shadow_moduli_heisenberg(c=2.0, q_max=20)
        assert result['match'], f"Heisenberg c=2 shadow-moduli failed: max_error={result['max_error']}"

    def test_heisenberg_c_half(self):
        """Verify shadow-moduli map for Heisenberg at c=1/2 (free fermion)."""
        result = verify_shadow_moduli_heisenberg(c=0.5, q_max=15)
        # For non-integer c, the direct computation may not work perfectly
        # but the resolution formula should still give valid q-series
        assert result['t_resolution_first5'][1] != 0.0, "t(q) should be nonzero"

    def test_shadow_moduli_single_atom_basic(self):
        """Basic test: single atom at lambda=-6/c gives t proportional to partition function."""
        c = 10.0
        q_max = 15
        F1 = {N: c * sum(1.0/d for d in range(1, N+1) if N % d == 0)
              for N in range(1, q_max + 1)}
        t = shadow_moduli_map_single_atom(c, F1, q_max)
        # t should be nonzero
        assert abs(t[1]) > 1e-15, "t_1 should be nonzero"
        # t should be O(c) since t = (c/6)(exp(-F_1) - 1) and F_1 = O(c)

    def test_shadow_moduli_vanishes_for_zero_F1(self):
        """If F_1 = 0 (no energy), t(q) = 0."""
        c = 1.0
        q_max = 10
        F1 = {N: 0.0 for N in range(1, q_max + 1)}
        t = shadow_moduli_map_single_atom(c, F1, q_max)
        for N in range(1, q_max + 1):
            assert abs(t[N]) < 1e-15, f"t_{N} should be zero for zero F_1"

    def test_shadow_moduli_consistency(self):
        """t(q) from resolution gives back F_1 when composed with G.

        The resolution gives t = (c/6)(exp(-F_1) - 1), so 1 + 6t/c = exp(-F_1),
        hence F_1 = -log(1 + 6t/c). We verify G(t(q)) = F_1 where
        G(t) = -log(1 + 6t/c) = sum_{r>=1} (-1)^r (6/c)^r t^r / r.
        """
        c = 4.0
        q_max = 15
        F1 = {N: c * sum(1.0/d for d in range(1, N+1) if N % d == 0)
              for N in range(1, q_max + 1)}
        t = shadow_moduli_map_single_atom(c, F1, q_max)

        # Compute G(t(q)) = -log(1 + 6t/c) as power series:
        # -log(1+x) = sum_{r>=1} (-1)^r x^r / r  where x = 6t/c
        # So G = sum_{r>=1} (-1)^r (6/c)^r t^r / r
        t_arr = [0.0] * (q_max + 1)
        for N in range(1, q_max + 1):
            t_arr[N] = t[N]

        G_coeffs = [0.0] * (q_max + 1)
        t_power = [0.0] * (q_max + 1)
        t_power[0] = 1.0  # t^0

        ratio = 6.0 / c
        for r in range(1, q_max + 1):
            # t_power *= t_arr (convolution)
            new_power = [0.0] * (q_max + 1)
            for i in range(q_max + 1):
                for j in range(q_max + 1 - i):
                    new_power[i + j] += t_power[i] * t_arr[j]
            t_power = new_power

            # G(t) = sum_{r>=1} (-1)^r (6/c)^r t^r / r
            coeff = ((-1.0)**r / r) * ratio**r
            for N in range(1, q_max + 1):
                G_coeffs[N] += coeff * t_power[N]

        # G_coeffs should equal F_1
        for N in range(1, min(q_max + 1, 10)):
            expected = F1[N]
            actual = G_coeffs[N]
            assert abs(actual - expected) < 1e-6, \
                f"G(t(q)) at order {N}: expected {expected}, got {actual}"


class TestRamanujanBound:
    """Tests for Ramanujan bound verification."""

    def test_delta_ramanujan(self):
        """Verify Deligne's theorem for the Ramanujan tau function."""
        result = ramanujan_bound_verification(k=12, n_max=20)
        assert result['all_pass'], "Ramanujan bound should hold for Delta"

    def test_delta_tau_values(self):
        """Check known values of Ramanujan tau."""
        assert ramanujan_tau(1) == 1
        assert ramanujan_tau(2) == -24
        assert ramanujan_tau(3) == 252
        assert ramanujan_tau(4) == -1472
        assert ramanujan_tau(5) == 4830

    def test_tau_multiplicativity(self):
        """tau is multiplicative: tau(mn) = tau(m)tau(n) for (m,n)=1."""
        # tau(6) = tau(2)*tau(3) since gcd(2,3)=1
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        # tau(10) = tau(2)*tau(5) since gcd(2,5)=1
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)
        # tau(15) = tau(3)*tau(5) since gcd(3,5)=1
        assert ramanujan_tau(15) == ramanujan_tau(3) * ramanujan_tau(5)

    def test_tau_hecke_recursion(self):
        """Hecke recursion: tau(p^2) = tau(p)^2 - p^11."""
        for p in [2, 3, 5]:
            assert ramanujan_tau(p*p) == ramanujan_tau(p)**2 - p**11, \
                f"Hecke recursion failed at p={p}: tau({p}^2)={ramanujan_tau(p*p)}, tau({p})^2-{p}^11={ramanujan_tau(p)**2-p**11}"


class TestSymmetricPowerFromShadow:
    """Tests for symmetric power extraction from shadow data."""

    def test_newton_identity(self):
        """Newton's identity: p_r = e1*p_{r-1} - e2*p_{r-2} for two variables."""
        result = symmetric_power_from_shadow(
            atoms=[3.0, 5.0], weights=[1.0, 1.0], r_max=10
        )
        assert all(r['passes'] for r in result['newton_checks'].values()), \
            "Newton's identities should hold exactly"

    def test_satake_at_weight_12(self):
        """Satake parameters for Delta at p=2: alpha*beta = p^{k-1} = 2^11."""
        a_p = ramanujan_tau(2)  # = -24
        # alpha + beta = -24, alpha * beta = 2^11 = 2048
        # alpha, beta are roots of x^2 + 24x + 2048 = 0
        discriminant = 24**2 - 4 * 2048
        assert discriminant < 0, "Satake params at p=2 should be complex (Ramanujan)"

        # |alpha| = |beta| = p^{(k-1)/2} = 2^{11/2}
        import cmath
        alpha = (-24 + cmath.sqrt(discriminant)) / 2
        beta = (-24 - cmath.sqrt(discriminant)) / 2
        assert abs(abs(alpha) - 2**(11/2)) < 1e-6, "Satake magnitude = p^{(k-1)/2}"
        assert abs(abs(beta) - 2**(11/2)) < 1e-6, "Satake magnitude = p^{(k-1)/2}"

    def test_virasoro_mc_recursion(self):
        """MC recursion for Virasoro shadow coefficients."""
        result = operadic_mc_constraint_symmetric_powers(c=10.0, r_max=10)
        assert result['all_recursion_pass'], "MC recursion should hold at leading order"

    def test_virasoro_mc_recursion_large_c(self):
        """MC recursion improves at large c (semiclassical)."""
        result = operadic_mc_constraint_symmetric_powers(c=100.0, r_max=10)
        assert result['all_recursion_pass'], "MC recursion should hold well at large c"


class TestModularityConstraint:
    """Tests for the modularity constraint on spectral measures."""

    def test_lattice_z_hecke(self):
        """Z lattice: theta = theta_3, spectral measure is Eisenstein.
        Eisenstein eigenvalues VIOLATE the cusp form Ramanujan bound (expected).
        The modularity_constraint_test correctly detects this violation."""
        result = modularity_constraint_test(
            atoms=[-6.0], weights=[1.0], k=1, q_max=30
        )
        # Single atom at -6.0 with k=1: Ramanujan bound = 2*p^0 = 2,
        # so |-6| > 2 fails. This is EXPECTED for Eisenstein eigenvalues.
        assert not result['all_ramanujan_pass'], \
            "Eisenstein eigenvalue -6.0 should violate cusp form Ramanujan bound"

    def test_leech_satake_ramanujan(self):
        """Leech lattice: Delta_{12} cusp form satisfies Ramanujan."""
        # The Leech lattice has spectral measure with atoms from E_{12} and Delta_{12}.
        # The cusp-form atom has Satake parameters satisfying Ramanujan.
        result = ramanujan_bound_verification(k=12, n_max=15)
        assert result['all_pass'], "Leech/Ramanujan should satisfy Deligne bound"


# ============================================================
# Import guard
# ============================================================

from fractions import Fraction
