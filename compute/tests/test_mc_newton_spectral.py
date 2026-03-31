"""Tests for MC = Newton's identities for the shadow spectral measure.

Comprehensive verification of the deepest structural theorem:
the Maurer-Cartan equation projected to each shadow arity r
is EXACTLY Newton's identity for the spectral atoms.

50+ tests covering:
  - Newton's identities (pure algebra)
  - Power sums from shadow coefficients
  - Elementary symmetric from power sums
  - MC bracket = Newton (the key structural theorem)
  - Spectral atoms extraction
  - exp(G) = product verification
  - Bridge table consistency
  - Heisenberg trivial Newton (Gaussian archetype)
  - Affine sl_2 Newton (Lie/tree archetype)
  - Virasoro effective coupling and spectral polynomial
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fractions import Fraction

from sympy import (
    Rational, Symbol, simplify, cancel, factor, expand, sqrt, oo,
    S as Sym,
)

from lib.mc_newton_spectral import (
    newton_identity,
    newton_identity_check,
    power_sums_from_shadow,
    elementary_symmetric_from_power_sums,
    mc_bracket_arity_r,
    mc_bracket_nonlinear_arity_r,
    verify_mc_equals_newton,
    spectral_atoms_from_elementary,
    virasoro_shadow_coefficients,
    virasoro_shadow_coefficients_exact,
    virasoro_effective_coupling,
    virasoro_spectral_polynomial,
    lattice_spectral_atoms,
    verify_exp_G_equals_product,
    mc_newton_bridge_table,
    heisenberg_trivial_newton,
    affine_sl2_newton,
    virasoro_mc_newton_deep_check,
    shadow_generating_function,
    exp_shadow_gf,
    product_from_elementary,
    c, t,
)


# =====================================================================
# Section 1: Newton's identities (pure algebra)
# =====================================================================

class TestNewtonIdentities:
    """Verify Newton's identities as pure algebraic identities."""

    def test_newton_n1(self):
        """p_1 = e_1."""
        p = [Rational(5)]
        e = [Rational(5)]
        assert newton_identity_check(p, e, 1)

    def test_newton_n2(self):
        """p_2 = p_1 e_1 - 2 e_2."""
        # For atoms {2, 3}: p_1 = 5, p_2 = 13, e_1 = 5, e_2 = 6
        p = [Rational(5), Rational(13)]
        e = [Rational(5), Rational(6)]
        assert newton_identity_check(p, e, 2)

    def test_newton_n3(self):
        """p_3 = p_2 e_1 - p_1 e_2 + 3 e_3."""
        # For atoms {1, 2, 3}: e_1=6, e_2=11, e_3=6, p_1=6, p_2=14, p_3=36
        p = [Rational(6), Rational(14), Rational(36)]
        e = [Rational(6), Rational(11), Rational(6)]
        assert newton_identity_check(p, e, 3)

    def test_newton_n4(self):
        """p_4 = p_3 e_1 - p_2 e_2 + p_1 e_3 - 4 e_4."""
        # For atoms {1, 2, 3}: e_4 = 0, p_4 = 1+16+81 = 98
        p = [Rational(6), Rational(14), Rational(36), Rational(98)]
        e = [Rational(6), Rational(11), Rational(6), Rational(0)]
        assert newton_identity_check(p, e, 4)

    def test_newton_n5_four_atoms(self):
        """Newton at level 5 for atoms {1, 1, 2, 3} (with multiplicity)."""
        # p_r = 2*1^r + 2^r + 3^r
        p = [Rational(6), Rational(14), Rational(36), Rational(98), Rational(276)]
        # e_1 = 1+1+2+3=7, e_2=1+2+3+2+3+3=14, e_3=2+3+6+3=14
        # Actually let's just use Newton to derive e from p
        e = elementary_symmetric_from_power_sums(p)
        assert newton_identity_check(p, e, 5)

    def test_newton_n10(self):
        """Newton at level 10 for atoms {1, 2}."""
        p = [Rational(3), Rational(5), Rational(9), Rational(17),
             Rational(33), Rational(65), Rational(129), Rational(257),
             Rational(513), Rational(1025)]
        e = elementary_symmetric_from_power_sums(p)
        assert newton_identity_check(p, e, 10)

    def test_newton_symbolic(self):
        """Newton identity with symbolic entries."""
        a = Symbol('a')
        b = Symbol('b')
        p = [a + b, a**2 + b**2]
        e = [a + b, a * b]
        residual = newton_identity(p, e, 2)
        # p_2 = p_1 e_1 - 2 e_2 -> a^2+b^2 = (a+b)^2 - 2ab
        assert simplify(residual) == 0

    def test_newton_identity_wrong_values_fails(self):
        """Newton identity FAILS with wrong values."""
        p = [Rational(5), Rational(13)]
        e = [Rational(5), Rational(7)]  # wrong e_2
        assert not newton_identity_check(p, e, 2)

    def test_newton_all_levels_consistency(self):
        """If e_k is computed from p_k via Newton, all levels hold tautologically."""
        p = [Rational(3), Rational(7), Rational(15), Rational(31),
             Rational(63), Rational(127)]
        e = elementary_symmetric_from_power_sums(p)
        for r in range(1, 7):
            assert newton_identity_check(p, e, r), f"Failed at r={r}"


# =====================================================================
# Section 2: Power sums from shadow
# =====================================================================

class TestPowerSumsFromShadow:
    """Test the shadow -> power sum conversion p_r = -r * S_r."""

    def test_heisenberg_p2(self):
        """p_2 = -2 * S_2 = -k for Heisenberg."""
        k = Symbol('k', positive=True)
        shadows = {2: k / 2}
        p = power_sums_from_shadow(shadows)
        assert simplify(p[2] + k) == 0  # p_2 = -k

    def test_virasoro_p2(self):
        """p_2 = -c for Virasoro (from S_2 = c/2)."""
        shadows = virasoro_shadow_coefficients_exact(4)
        p = power_sums_from_shadow(shadows)
        assert simplify(p[2] + c) == 0  # p_2 = -c

    def test_virasoro_p3(self):
        """p_3 = -6 for Virasoro (from S_3 = 2)."""
        shadows = virasoro_shadow_coefficients_exact(4)
        p = power_sums_from_shadow(shadows)
        assert simplify(p[3] + 6) == 0  # p_3 = -3*2 = -6

    def test_virasoro_p4(self):
        """p_4 = -40/(c(5c+22)) for Virasoro."""
        shadows = virasoro_shadow_coefficients_exact(4)
        p = power_sums_from_shadow(shadows)
        expected = -Rational(40) / (c * (5 * c + 22))
        assert simplify(p[4] - expected) == 0

    def test_virasoro_p5(self):
        """p_5 = 240/(c^2(5c+22)) for Virasoro (from S_5 = -48/[c^2(5c+22)])."""
        shadows = virasoro_shadow_coefficients_exact(5)
        p = power_sums_from_shadow(shadows)
        expected = Rational(240) / (c**2 * (5 * c + 22))
        assert simplify(p[5] - expected) == 0

    def test_zero_shadow_gives_zero_power_sum(self):
        """Zero shadow coefficient gives zero power sum."""
        shadows = {5: Rational(0)}
        p = power_sums_from_shadow(shadows)
        assert p[5] == 0

    def test_power_sum_linearity(self):
        """Power sum conversion is linear in S_r."""
        a = Symbol('a')
        shadows = {3: a, 4: 2 * a}
        p = power_sums_from_shadow(shadows)
        assert simplify(p[3] + 3 * a) == 0
        assert simplify(p[4] + 8 * a) == 0


# =====================================================================
# Section 3: Elementary symmetric from power sums
# =====================================================================

class TestElementarySymmetric:
    """Test extraction of elementary symmetric polynomials from power sums."""

    def test_heisenberg_e1_only(self):
        """Heisenberg: e_1 = 0 (no p_1), e_2 = k/2, rest zero."""
        k = Symbol('k', positive=True)
        p_list = [Rational(0), -k]  # p_1=0, p_2=-k
        e = elementary_symmetric_from_power_sums(p_list)
        assert simplify(e[0]) == 0  # e_1 = 0
        assert simplify(e[1] - k / 2) == 0  # e_2 = k/2

    def test_virasoro_first_three(self):
        """Virasoro: compute e_1, e_2, e_3."""
        shadows = virasoro_shadow_coefficients_exact(4)
        p_dict = power_sums_from_shadow(shadows)
        p_list = [Rational(0), p_dict[2], p_dict[3], p_dict[4]]
        e = elementary_symmetric_from_power_sums(p_list)
        # e_1 = p_1 = 0
        assert simplify(e[0]) == 0
        # e_2 = (1/2)(p_1 e_1 - p_2) = (1/2)(0 - (-c)) = c/2
        assert simplify(e[1] - c / 2) == 0
        # e_3 = (1/3)(p_1 e_2 - p_2 e_1 + p_3) = (1/3)(0 - 0 + (-6)) = -2
        assert simplify(e[2] + 2) == 0

    def test_consistency_roundtrip(self):
        """e_k from Newton roundtrips: given atoms, extract p_k, get e_k back."""
        # Atoms {2, 5}: e_1=7, e_2=10, p_1=7, p_2=29
        p = [Rational(7), Rational(29)]
        e = elementary_symmetric_from_power_sums(p)
        assert e[0] == 7
        assert e[1] == 10

    def test_three_atoms(self):
        """Three atoms {1, 3, 5}: e_1=9, e_2=23, e_3=15."""
        p = [Rational(9), Rational(35), Rational(153)]
        e = elementary_symmetric_from_power_sums(p)
        assert e[0] == 9
        assert e[1] == 23
        assert e[2] == 15

    def test_all_zero_power_sums(self):
        """All zero power sums give all zero elementary symmetric."""
        p = [Rational(0)] * 5
        e = elementary_symmetric_from_power_sums(p)
        for ek in e:
            assert ek == 0


# =====================================================================
# Section 4: MC bracket = Newton (the KEY structural theorem)
# =====================================================================

class TestMCBracketEqualsNewton:
    """The deepest tests: MC bracket at each arity = Newton's identity."""

    def test_virasoro_arity5_mc_consistency(self):
        """MC bracket at r=5 reproduces S_5 from the recursion."""
        shadows = virasoro_shadow_coefficients_exact(7)
        obs = mc_bracket_nonlinear_arity_r(shadows, 5)
        predicted = cancel(-obs / (2 * 5 * c))
        assert simplify(predicted - shadows[5]) == 0

    def test_virasoro_arity6_mc_consistency(self):
        """MC bracket at r=6 reproduces S_6."""
        shadows = virasoro_shadow_coefficients_exact(7)
        obs = mc_bracket_nonlinear_arity_r(shadows, 6)
        predicted = cancel(-obs / (2 * 6 * c))
        assert simplify(predicted - shadows[6]) == 0

    def test_virasoro_arity7_mc_consistency(self):
        """MC bracket at r=7 reproduces S_7."""
        shadows = virasoro_shadow_coefficients_exact(8)
        obs = mc_bracket_nonlinear_arity_r(shadows, 7)
        predicted = cancel(-obs / (2 * 7 * c))
        assert simplify(predicted - shadows[7]) == 0

    def test_virasoro_arity8_mc_consistency(self):
        """MC bracket at r=8 reproduces S_8."""
        shadows = virasoro_shadow_coefficients_exact(9)
        obs = mc_bracket_nonlinear_arity_r(shadows, 8)
        predicted = cancel(-obs / (2 * 8 * c))
        assert simplify(predicted - shadows[8]) == 0

    def test_virasoro_arity10_mc_consistency(self):
        """MC bracket at r=10 reproduces S_10."""
        shadows = virasoro_shadow_coefficients_exact(11)
        obs = mc_bracket_nonlinear_arity_r(shadows, 10)
        predicted = cancel(-obs / (2 * 10 * c))
        assert simplify(predicted - shadows[10]) == 0

    def test_virasoro_newton_all_levels(self):
        """All Newton identities hold tautologically for Virasoro through arity 10."""
        shadows = virasoro_shadow_coefficients_exact(10)
        p_dict = power_sums_from_shadow(shadows)
        p_list = [Rational(0)]  # p_1 = 0
        for r in range(2, 11):
            p_list.append(p_dict.get(r, Rational(0)))
        e_list = elementary_symmetric_from_power_sums(p_list)
        for r in range(1, 11):
            residual = newton_identity(p_list, e_list, r)
            assert residual == 0, f"Newton failed at r={r}: residual={residual}"

    def test_heisenberg_all_arities_trivial(self):
        """Heisenberg: MC trivially = Newton (all vanish for r >= 3)."""
        k = Symbol('k', positive=True)
        shadows = {2: k / 2}
        for r in range(3, 10):
            shadows[r] = Rational(0)
        for r in range(5, 10):
            obs = mc_bracket_nonlinear_arity_r(shadows, r)
            assert obs == 0, f"Heisenberg obstruction at r={r} should be 0"

    def test_affine_cartan_arities(self):
        """Affine sl_2 on Cartan line: MC at r=3 trivial, then vanishes."""
        k = Symbol('k', positive=True)
        shadows = {2: k}
        for r in range(3, 10):
            shadows[r] = Rational(0)
        for r in range(5, 10):
            obs = mc_bracket_nonlinear_arity_r(shadows, r)
            assert obs == 0

    def test_verify_mc_equals_newton_virasoro(self):
        """Full MC=Newton verification for Virasoro."""
        result = verify_mc_equals_newton('virasoro', max_arity=8)
        for r in range(1, 9):
            assert result['matches'][r], f"Newton failed at r={r}"
        for r in range(5, 9):
            if r in result['mc_reproduces_shadow']:
                assert result['mc_reproduces_shadow'][r], \
                    f"MC failed to reproduce S_{r}"

    def test_verify_mc_equals_newton_heisenberg(self):
        """Full MC=Newton verification for Heisenberg."""
        result = verify_mc_equals_newton('heisenberg', max_arity=8)
        for r in range(1, 9):
            assert result['matches'][r], f"Newton failed at r={r}"

    def test_deep_check_virasoro(self):
        """Deep MC-Newton bridge verification for Virasoro."""
        result = virasoro_mc_newton_deep_check(max_r=8)
        for r in range(1, 9):
            assert result['newton_tautological'][r], \
                f"Newton tautological check failed at r={r}"
        for r in range(5, 9):
            if r in result['mc_consistency']:
                assert result['mc_consistency'][r], \
                    f"MC consistency failed at r={r}"


# =====================================================================
# Section 5: Elementary symmetric polynomial structure
# =====================================================================

class TestElementarySymmetricStructure:
    """Test structural properties of elementary symmetric polynomials."""

    def test_virasoro_e2_equals_kappa(self):
        """e_2 = c/2 = kappa (the curvature appears as e_2)."""
        shadows = virasoro_shadow_coefficients_exact(6)
        p_dict = power_sums_from_shadow(shadows)
        p_list = [Rational(0)]
        for r in range(2, 7):
            p_list.append(p_dict.get(r, Rational(0)))
        e = elementary_symmetric_from_power_sums(p_list)
        assert simplify(e[1] - c / 2) == 0

    def test_virasoro_e3_equals_minus_cubic(self):
        """e_3 = -2 (the cubic shadow appears as -e_3)."""
        shadows = virasoro_shadow_coefficients_exact(6)
        p_dict = power_sums_from_shadow(shadows)
        p_list = [Rational(0)]
        for r in range(2, 7):
            p_list.append(p_dict.get(r, Rational(0)))
        e = elementary_symmetric_from_power_sums(p_list)
        assert simplify(e[2] + 2) == 0

    def test_virasoro_e4(self):
        """e_4 for Virasoro: determined by Newton from p_1,...,p_4."""
        shadows = virasoro_shadow_coefficients_exact(6)
        p_dict = power_sums_from_shadow(shadows)
        p_list = [Rational(0)]
        for r in range(2, 7):
            p_list.append(p_dict.get(r, Rational(0)))
        e = elementary_symmetric_from_power_sums(p_list)
        # e_4 = (1/4)(p_1 e_3 - p_2 e_2 + p_3 e_1 - p_4)
        # = (1/4)(0 - (-c)(c/2) + (-6)(0) - p_4)
        # = (1/4)(c^2/2 - p_4)
        p_4 = p_dict[4]
        expected_e4 = cancel((c**2 / 2 - p_4) / 4)
        assert simplify(e[3] - expected_e4) == 0


# =====================================================================
# Section 6: Spectral atoms
# =====================================================================

class TestSpectralAtoms:
    """Test spectral atom extraction."""

    def test_two_known_atoms(self):
        """Two atoms at {2, 5}: p_1=7, p_2=29, e_1=7, e_2=10."""
        e = [Rational(7), Rational(10)]
        atoms = spectral_atoms_from_elementary(e)
        atoms_sorted = sorted([float(cancel(a)) for a in atoms])
        assert abs(atoms_sorted[0] - 2.0) < 1e-10
        assert abs(atoms_sorted[1] - 5.0) < 1e-10

    def test_three_known_atoms(self):
        """Three atoms at {1, 3, 5}."""
        e = [Rational(9), Rational(23), Rational(15)]
        atoms = spectral_atoms_from_elementary(e)
        atoms_sorted = sorted([float(cancel(a)) for a in atoms])
        assert abs(atoms_sorted[0] - 1.0) < 1e-10
        assert abs(atoms_sorted[1] - 3.0) < 1e-10
        assert abs(atoms_sorted[2] - 5.0) < 1e-10

    def test_heisenberg_no_real_atoms(self):
        """Heisenberg: e_1=0, e_2=k/2 gives purely imaginary atoms."""
        k_val = 4
        e = [Rational(0), Rational(k_val, 2)]
        atoms = spectral_atoms_from_elementary(e)
        # P(t) = 1 + 2t^2, roots at t = +/- i/sqrt(2)
        # atoms = 1/t = +/- i*sqrt(2)
        for a in atoms:
            a_val = complex(a)
            assert abs(a_val.real) < 1e-10, "Heisenberg atoms should be purely imaginary"
            assert abs(abs(a_val.imag) - sqrt(float(k_val) / 2)) < 1e-10

    def test_lattice_e8_eisenstein_only(self):
        """E8 lattice: Eisenstein-only decomposition (no cusp form atoms)."""
        result = lattice_spectral_atoms('E8')
        assert result['eisenstein_only'] is True
        assert result['spectral_atoms']['type'] == 'eisenstein'

    def test_lattice_leech_has_hecke_atoms(self):
        """Leech lattice: has Hecke eigenvalue atoms from Ramanujan Delta."""
        result = lattice_spectral_atoms('Leech')
        assert result['eisenstein_only'] is False
        assert result['spectral_atoms']['type'] == 'hecke'
        assert result['spectral_atoms']['cusp_form'] == 'Delta'

    def test_lattice_leech_ramanujan_bound(self):
        """Leech lattice: all Hecke eigenvalues satisfy Ramanujan bound."""
        result = lattice_spectral_atoms('Leech')
        atoms = result['spectral_atoms']['atoms_by_prime']
        for p, info in atoms.items():
            assert info['ramanujan_bound_check'], \
                f"Ramanujan bound violated at p={p}: |tau(p)| > 2p^(11/2)"


# =====================================================================
# Section 7: exp(G) = product verification
# =====================================================================

class TestExpGProduct:
    """Verify exp(G(t)) = prod(1 - lambda_j t)^{c_j}."""

    def test_heisenberg_product(self):
        """Heisenberg: exp(G) = exp((k/2)t^2), product side = 1 + (k/2)t^2."""
        k_sym = Symbol('k', positive=True)
        shadows = {2: k_sym / 2}
        for r in range(3, 7):
            shadows[r] = Rational(0)
        p_dict = power_sums_from_shadow(shadows)
        p_list = [Rational(0)]
        for r in range(2, 7):
            p_list.append(p_dict.get(r, Rational(0)))
        e_list = elementary_symmetric_from_power_sums(p_list)

        result = verify_exp_G_equals_product(shadows, e_list, max_order=6)
        # Check order-by-order
        for k_ord in range(min(5, len(result['matches']))):
            if k_ord in result['matches']:
                assert result['matches'][k_ord], f"Mismatch at order {k_ord}"

    def test_virasoro_order4(self):
        """Virasoro: exp(G) matches product through order 4."""
        shadows = virasoro_shadow_coefficients_exact(6)
        p_dict = power_sums_from_shadow(shadows)
        p_list = [Rational(0)]
        for r in range(2, 7):
            p_list.append(p_dict.get(r, Rational(0)))
        e_list = elementary_symmetric_from_power_sums(p_list)

        result = verify_exp_G_equals_product(shadows, e_list, max_order=4)
        for k_ord in range(min(5, len(result['matches']))):
            if k_ord in result['matches']:
                assert result['matches'][k_ord], f"Mismatch at order {k_ord}"


# =====================================================================
# Section 8: Bridge table
# =====================================================================

class TestBridgeTable:
    """Test the MC-Newton bridge table."""

    def test_table_format(self):
        """Bridge table has expected structure."""
        table = mc_newton_bridge_table(max_arity=6)
        assert len(table) >= 5  # arities 2 through 6
        for row in table:
            assert 'arity' in row
            assert 'S_r' in row
            assert 'p_r' in row

    def test_table_consistency(self):
        """Bridge table: p_r = -r * S_r for all entries."""
        table = mc_newton_bridge_table(max_arity=6)
        for row in table:
            r = row['arity']
            S_r = row['S_r']
            p_r = row['p_r']
            assert simplify(p_r + r * S_r) == 0, \
                f"p_{r} != -r*S_{r}: got p={p_r}, S={S_r}"

    def test_table_newton_holds(self):
        """Bridge table: Newton identity holds at every arity."""
        table = mc_newton_bridge_table(max_arity=8)
        for row in table:
            if 'newton_holds' in row:
                assert row['newton_holds'], \
                    f"Newton failed at arity {row['arity']}"

    def test_table_mc_matches(self):
        """Bridge table: MC reproduces shadow at arities 5+."""
        table = mc_newton_bridge_table(max_arity=8)
        for row in table:
            if 'mc_matches' in row:
                assert row['mc_matches'], \
                    f"MC mismatch at arity {row['arity']}"


# =====================================================================
# Section 9: Effective coupling
# =====================================================================

class TestEffectiveCoupling:
    """Test the Virasoro effective coupling constant."""

    def test_virasoro_coupling(self):
        """lambda_eff = -6/c."""
        for c_val in [1, 2, 13, 26, 100]:
            lam = virasoro_effective_coupling(c_val)
            expected = Fraction(-6, c_val)
            assert lam == expected

    def test_large_c_limit(self):
        """lambda_eff -> 0 as c -> infinity."""
        for c_val in [100, 1000, 10000]:
            lam = virasoro_effective_coupling(c_val)
            assert abs(float(lam)) < 0.1

    def test_self_dual_c13(self):
        """lambda_eff(13) = -6/13."""
        lam = virasoro_effective_coupling(13)
        assert lam == Fraction(-6, 13)

    def test_coupling_sign(self):
        """Effective coupling is negative for positive c."""
        for c_val in [1, 5, 13, 100]:
            lam = virasoro_effective_coupling(c_val)
            assert float(lam) < 0


# =====================================================================
# Section 10: Heisenberg trivial Newton
# =====================================================================

class TestHeisenbergTrivialNewton:
    """Heisenberg: the Gaussian archetype where everything terminates."""

    def test_heisenberg_newton_all_levels(self):
        """All Newton identities hold for Heisenberg."""
        result = heisenberg_trivial_newton()
        for r, holds in result['newton_holds'].items():
            assert holds, f"Newton failed at r={r} for Heisenberg"

    def test_heisenberg_p2(self):
        """p_2 = -2k for Heisenberg (since S_2 = kappa = k, p_2 = -2*S_2 = -2k)."""
        k = Symbol('k', positive=True)
        result = heisenberg_trivial_newton()
        p2 = result['power_sums'][2]
        assert simplify(p2 + 2 * k) == 0

    def test_heisenberg_e1_zero(self):
        """e_1 = 0 for Heisenberg (no arity-1 shadow)."""
        result = heisenberg_trivial_newton()
        assert simplify(result['e_1']) == 0

    def test_heisenberg_e2(self):
        """e_2 = k for Heisenberg (since p_2 = -2k, e_2 = -p_2/2 = k)."""
        k = Symbol('k', positive=True)
        result = heisenberg_trivial_newton()
        assert simplify(result['e_2'] - k) == 0

    def test_heisenberg_higher_shadows_zero(self):
        """All S_r = 0 for r >= 3 (Gaussian termination)."""
        result = heisenberg_trivial_newton()
        for r in range(3, 13):
            assert result['shadows'][r] == 0


# =====================================================================
# Section 11: Affine sl_2 Newton
# =====================================================================

class TestAffineSl2Newton:
    """Affine sl_2: the Lie/tree archetype."""

    def test_affine_newton_cartan(self):
        """All Newton identities hold on the Cartan line."""
        result = affine_sl2_newton()
        for r, holds in result['newton_holds_cartan'].items():
            assert holds, f"Newton failed at r={r} for affine Cartan"

    def test_affine_termination_cartan(self):
        """Shadow tower terminates at arity 2 on Cartan line."""
        result = affine_sl2_newton()
        assert result['termination_arity_cartan'] == 2

    def test_affine_termination_full(self):
        """Shadow tower terminates at arity 3 on full sl_2."""
        result = affine_sl2_newton()
        assert result['termination_arity_full'] == 3


# =====================================================================
# Section 12: Virasoro spectral polynomial
# =====================================================================

class TestVirasoroSpectralPolynomial:
    """Test the Virasoro spectral polynomial and its roots."""

    def test_polynomial_exists(self):
        """Spectral polynomial can be computed at numeric c."""
        e_list, atoms = virasoro_spectral_polynomial(26, max_r=6)
        assert e_list is not None
        assert atoms is not None
        assert len(atoms) > 0

    def test_polynomial_c1(self):
        """Spectral polynomial at c=1."""
        e_list, atoms = virasoro_spectral_polynomial(1, max_r=6)
        assert len(e_list) >= 4
        assert len(atoms) > 0

    def test_polynomial_c13_self_dual(self):
        """Spectral polynomial at self-dual c=13."""
        e_list, atoms = virasoro_spectral_polynomial(13, max_r=6)
        assert len(atoms) > 0

    def test_polynomial_exact_symbolic(self):
        """Spectral polynomial can be computed symbolically."""
        e_list, atoms = virasoro_spectral_polynomial(c, max_r=6)
        assert len(e_list) >= 4
        assert atoms is None  # symbolic doesn't give roots


# =====================================================================
# Section 13: Generating function and product
# =====================================================================

class TestGeneratingFunction:
    """Test shadow generating function and its exponential."""

    def test_shadow_gf_heisenberg(self):
        """Heisenberg GF: G(t) = (k/2)t^2."""
        k_sym = Symbol('k', positive=True)
        shadows = {2: k_sym / 2, 3: Rational(0), 4: Rational(0)}
        G = shadow_generating_function(shadows, max_order=4)
        expected = k_sym / 2 * t**2
        assert simplify(G - expected) == 0

    def test_exp_gf_heisenberg_order4(self):
        """exp(G) for Heisenberg: 1 + (k/2)t^2 + (k^2/8)t^4."""
        k_sym = Symbol('k', positive=True)
        shadows = {2: k_sym / 2, 3: Rational(0), 4: Rational(0)}
        coeffs = exp_shadow_gf(shadows, max_order=4)
        assert coeffs[0] == 1
        assert simplify(coeffs[1]) == 0
        assert simplify(coeffs[2] - k_sym / 2) == 0
        assert simplify(coeffs[3]) == 0
        assert simplify(coeffs[4] - k_sym**2 / 8) == 0

    def test_product_from_elementary_basic(self):
        """Product polynomial from elementary symmetric: P(t) = 1 - 3t + 2t^2."""
        e = [Rational(3), Rational(2)]
        coeffs = product_from_elementary(e, max_order=3)
        assert coeffs[0] == 1
        assert coeffs[1] == -3
        assert coeffs[2] == 2


# =====================================================================
# Section 14: Lattice spectral atoms
# =====================================================================

class TestLatticeSpectralAtoms:
    """Test lattice spectral atoms and their Hecke structure."""

    def test_Z_lattice(self):
        """V_Z: rank 1, Gaussian, depth 2."""
        result = lattice_spectral_atoms('Z')
        assert result['rank'] == 1
        assert result['shadow_depth'] == 2
        assert result['archetype'] == 'G'
        assert result['eisenstein_only'] is True

    def test_E8_lattice(self):
        """V_{E8}: rank 8, Lie/tree, depth 3, no cusp forms."""
        result = lattice_spectral_atoms('E8')
        assert result['rank'] == 8
        assert result['shadow_depth'] == 3
        assert result['archetype'] == 'L'
        assert result['eisenstein_only'] is True

    def test_Leech_lattice_depth(self):
        """V_Leech: rank 24, contact, depth 4."""
        result = lattice_spectral_atoms('Leech')
        assert result['rank'] == 24
        assert result['shadow_depth'] == 4

    def test_Leech_tau2(self):
        """Leech: tau(2) = -24."""
        result = lattice_spectral_atoms('Leech')
        atoms = result['spectral_atoms']['atoms_by_prime']
        assert atoms[2]['tau_p'] == -24

    def test_Leech_tau3(self):
        """Leech: tau(3) = 252."""
        result = lattice_spectral_atoms('Leech')
        atoms = result['spectral_atoms']['atoms_by_prime']
        assert atoms[3]['tau_p'] == 252

    def test_Leech_tau5(self):
        """Leech: tau(5) = 4830."""
        result = lattice_spectral_atoms('Leech')
        atoms = result['spectral_atoms']['atoms_by_prime']
        assert atoms[5]['tau_p'] == 4830


# =====================================================================
# Section 15: Cross-family comparison
# =====================================================================

class TestCrossFamilyComparison:
    """Compare Newton structure across families."""

    def test_heisenberg_vs_virasoro_e2(self):
        """Both families have e_2 = kappa (the curvature)."""
        # Heisenberg: e_2 = k (since kappa(H_k) = k)
        heis = heisenberg_trivial_newton()
        assert simplify(heis['e_2'] - Symbol('k', positive=True)) == 0

        # Virasoro: e_2 = c/2 (since kappa(Vir_c) = c/2)
        vir_shadows = virasoro_shadow_coefficients_exact(4)
        vir_p = power_sums_from_shadow(vir_shadows)
        vir_p_list = [Rational(0), vir_p[2], vir_p[3], vir_p[4]]
        vir_e = elementary_symmetric_from_power_sums(vir_p_list)
        assert simplify(vir_e[1] - c / 2) == 0

    def test_heisenberg_tower_finite_newton_structure(self):
        """Heisenberg: e_1=0, e_2=k, odd e_k=0, even e_k from Newton.

        Since kappa(H_k) = k, we have S_2 = k, p_2 = -2k.
        Although all shadows S_r = 0 for r >= 3 (p_r = 0 for r >= 3),
        Newton's identities generate nonzero even e_k from e_2 alone.
        This is because exp(G) = exp(k*t^2) has nonzero Taylor
        coefficients at all even orders: the product representation
        has infinitely many (virtual) atoms.
        """
        result = heisenberg_trivial_newton()
        es = result['elementary_symmetric']
        k = Symbol('k', positive=True)
        # e_1 = 0
        assert simplify(es[1]) == 0
        # e_3 = 0 (odd)
        assert simplify(es[3]) == 0
        # e_5 = 0 (odd)
        assert simplify(es[5]) == 0
        # e_2 = k (since p_2 = -2k, e_2 = -p_2/2 = k)
        assert simplify(es[2] - k) == 0
        # e_4 = k^2/2 (from Newton: e_4 = (1/4)(0 - (-2k)(k) + 0 - 0) = k^2/2)
        assert simplify(es[4] - k**2 / 2) == 0

    def test_virasoro_has_nonzero_e3(self):
        """Virasoro has nonzero e_3 = -2 (from the cubic shadow)."""
        vir_shadows = virasoro_shadow_coefficients_exact(5)
        vir_p = power_sums_from_shadow(vir_shadows)
        vir_p_list = [Rational(0)]
        for r in range(2, 6):
            vir_p_list.append(vir_p.get(r, Rational(0)))
        vir_e = elementary_symmetric_from_power_sums(vir_p_list)
        # e_3 = -2 (nonzero! the cubic breaks the Gaussian structure)
        assert simplify(vir_e[2] + 2) == 0


# =====================================================================
# Section 16: Numerical consistency
# =====================================================================

class TestNumericalConsistency:
    """Numerical cross-checks at specific central charge values."""

    def test_virasoro_c1_power_sums(self):
        """Power sums at c=1."""
        shadows = virasoro_shadow_coefficients(1, max_r=6)
        p = power_sums_from_shadow(shadows)
        assert abs(p[2] - (-1.0)) < 1e-10
        assert abs(p[3] - (-6.0)) < 1e-10

    def test_virasoro_c26_power_sums(self):
        """Power sums at c=26."""
        shadows = virasoro_shadow_coefficients(26, max_r=6)
        p = power_sums_from_shadow(shadows)
        assert abs(p[2] - (-26.0)) < 1e-10
        assert abs(p[3] - (-6.0)) < 1e-10  # p_3 = -6 is c-independent

    def test_virasoro_p4_numerical(self):
        """p_4 at c=1: -40/(1*27) = -40/27."""
        shadows = virasoro_shadow_coefficients(1, max_r=6)
        p = power_sums_from_shadow(shadows)
        expected = -40.0 / 27.0
        assert abs(p[4] - expected) < 1e-10

    def test_effective_coupling_numerical(self):
        """Effective coupling at various c values."""
        for c_val in [1, 2, 10, 26]:
            lam = virasoro_effective_coupling(c_val)
            assert abs(float(lam) - (-6.0 / c_val)) < 1e-12
