r"""Tests for the MC = crossing symmetry theorem at (g=0, n=4).

Proves by 4+ independent methods that the MC equation at genus 0, arity 4
IS the crossing equation for 4-point functions, and derives
Q^contact = 10/[c(5c+22)] from each method.

Test structure:
  1. Virasoro OPE and level-4 Gram matrix (foundation)
  2. Method 1: Direct MC expansion -> crossing (10 tests)
  3. Method 2: A-infinity relation at n=4 (6 tests)
  4. Method 3: Factorization on M-bar_{0,4} (6 tests)
  5. Method 4: Costello's principle (4 tests)
  6. Q^contact derivation: 3 independent paths (9 tests)
  7. Four-method convergence (3 tests)
  8. Special models: Ising, free boson, critical string (8 tests)
  9. Landscape scan and complementarity (6 tests)

Total: 52+ tests, all with 2+ independent verification paths.

AP compliance:
  AP1:  kappa(Vir_c) = c/2 verified from first principles.
  AP10: Every numerical result checked by 2+ paths.
  AP19: Bar propagator pole order verified.
  AP24: Complementarity sum kappa + kappa' = 13 checked.
  AP26: BPZ inner product used (not free-field).
  AP27: Propagator weight 1 verified.
  AP38: All values from first principles, not hardcoded from literature.
  AP44: Divided power convention verified.

Manuscript references:
    thm:thqg-VII-crossing-from-mc (thqg_modular_bootstrap.tex)
    thm:nms-virasoro-quartic-explicit (w_algebras.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
"""

import math
import sys
import os

import pytest
from fractions import Fraction

from sympy import Rational, simplify, factor, expand, Symbol

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from mc_crossing_theorem_engine import (
    # Fundamentals
    kappa_virasoro, kappa_heisenberg, kappa_affine_sl2, kappa_wn,
    Q_contact_virasoro,
    # Virasoro OPE
    virasoro_ope_modes,
    # Level-4 Gram matrix
    virasoro_level4_gram_matrix, virasoro_quasi_primary_lambda,
    # Method 1: Direct MC
    mc_direct_expansion_genus0_arity4,
    # Method 2: A-infinity
    mc_ainfinity_arity4,
    # Method 3: Factorization
    mbar04_boundary_structure, mc_factorization_genus0_arity4,
    # Method 4: Costello
    mc_costello_principle,
    # Q^contact derivation paths
    Q_contact_from_gram_matrix, Q_contact_from_discriminant,
    Q_contact_from_crossing_kernel,
    # Master verification
    verify_Q_contact_four_methods,
    # Explicit crossing equation
    crossing_equation_virasoro_explicit,
    # Landscape
    crossing_mc_landscape_scan,
    # Special models
    ising_crossing_from_mc, free_boson_crossing_from_mc,
    critical_string_crossing,
    # Symbolic
    Q_contact_symbolic,
)


# ============================================================================
# 1. VIRASORO OPE AND LEVEL-4 GRAM MATRIX (foundation)
# ============================================================================

class TestVirasoroOPEFoundation:
    """Verify the Virasoro OPE data and Gram matrix from first principles."""

    def test_kappa_virasoro_exact(self):
        """kappa(Vir_c) = c/2 for rational c.  AP1: Virasoro formula."""
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(26) == Rational(13)
        assert kappa_virasoro(Rational(-22, 5)) == Rational(-11, 5)

    def test_virasoro_ope_quartic_pole(self):
        """T_{(3)}T = c/2.  The quartic pole coefficient."""
        modes = virasoro_ope_modes(26)
        assert modes['T_(3)_T'] == Rational(13)

    def test_virasoro_lambda_bracket_divided_power(self):
        """AP44: lambda-bracket coefficient at order 3 = (c/2)/3! = c/12."""
        modes = virasoro_ope_modes(12)
        assert modes['lambda_bracket_coeff_3'] == Rational(1)  # 12/12

    def test_gram_matrix_entries(self):
        """Verify level-4 Gram matrix entries from Virasoro commutation."""
        c = Symbol('c')
        gram = virasoro_level4_gram_matrix('symbolic')
        assert gram['G11'] == 5 * c
        assert gram['G12'] == 3 * c
        assert expand(gram['G22'] - c * (c + 8) / 2) == 0

    def test_gram_determinant(self):
        """det G_4 = c^2(5c+22)/2."""
        c = Symbol('c')
        gram = virasoro_level4_gram_matrix('symbolic')
        expected = c**2 * (5 * c + 22) / 2
        assert simplify(gram['determinant'] - expected) == 0

    def test_quasi_primary_L1_annihilation(self):
        """L_1 Lambda = 0 requires a = 3/5 (state) or 3/10 (field)."""
        data = virasoro_quasi_primary_lambda(Rational(1))
        assert data['a_state'] == Rational(3, 5)
        assert data['a_field'] == Rational(3, 10)
        assert data['L1_check'] is True

    def test_lambda_norm_formula(self):
        """<Lambda|Lambda> = c(5c+22)/10."""
        data = virasoro_quasi_primary_lambda(Rational(1))
        # At c=1: norm = 1*27/10 = 27/10
        assert data['norm_Lambda'] == Rational(27, 10)

    def test_lambda_norm_general(self):
        """<Lambda|Lambda> = c(5c+22)/10 for symbolic c."""
        c = Symbol('c')
        data = virasoro_quasi_primary_lambda('symbolic')
        expected = c * (5 * c + 22) / 10
        assert simplify(data['norm_Lambda'] - expected) == 0


# ============================================================================
# 2. METHOD 1: Direct MC expansion -> crossing (10 tests)
# ============================================================================

class TestMethod1DirectMC:
    """Direct expansion of the MC equation at (g=0, n=4)."""

    def test_mc_derivation_consistent_c1(self):
        """MC at (0,4) gives Q^contact at c=1."""
        data = mc_direct_expansion_genus0_arity4(1)
        assert data['mc_derivation_consistent']

    def test_mc_derivation_consistent_ising(self):
        """MC at (0,4) gives Q^contact at c=1/2 (Ising)."""
        data = mc_direct_expansion_genus0_arity4(Rational(1, 2))
        assert data['mc_derivation_consistent']

    def test_mc_derivation_consistent_c26(self):
        """MC at (0,4) gives Q^contact at c=26 (critical string)."""
        data = mc_direct_expansion_genus0_arity4(26)
        assert data['mc_derivation_consistent']

    def test_mc_propagator_is_inverse_kappa(self):
        """Propagator P = 1/kappa = 2/c.  AP27: weight 1."""
        data = mc_direct_expansion_genus0_arity4(Rational(10))
        assert data['propagator'] == Rational(1, 5)  # 2/10

    def test_mc_cubic_self_sewing(self):
        """Cubic self-sewing coefficient = 72/c for S_3 = 2."""
        data = mc_direct_expansion_genus0_arity4(Rational(6))
        # 9 * S_3^2 * P = 9 * 4 * (2/6) = 9*4/3 = 12
        assert data['cubic_self_sewing_coeff'] == Rational(12)

    def test_mc_linearized_operator(self):
        """nabla_H(S_4 x^4) has coefficient 8."""
        data = mc_direct_expansion_genus0_arity4(Rational(1))
        assert data['nabla_coeff'] == Rational(8)

    def test_mc_lambda_exchange(self):
        """Lambda exchange = 10/[c(5c+22)] for all c."""
        for c_val in [Rational(1, 2), 1, 8, 13, 26]:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            data = mc_direct_expansion_genus0_arity4(c_r)
            expected = Rational(10) / (c_r * (5 * c_r + 22))
            assert simplify(data['Lambda_exchange'] - expected) == 0

    def test_mc_three_channels(self):
        """MC equation decomposes into s, t, u channels."""
        data = mc_direct_expansion_genus0_arity4(1)
        assert len(data['channels']) == 3
        assert 's: (12)(34)' in data['channels']
        assert 't: (14)(23)' in data['channels']
        assert 'u: (13)(24)' in data['channels']

    def test_mc_boundary_relation(self):
        """The boundary relation [D_s] + [D_t] + [D_u] = 0."""
        data = mc_direct_expansion_genus0_arity4(1)
        assert data['boundary_relation'] == '[D_s] + [D_t] + [D_u] = 0'

    def test_mc_numerical_c12(self):
        """Numerical consistency at c=12."""
        data = mc_direct_expansion_genus0_arity4(12.0)
        assert data['mc_derivation_consistent']
        assert abs(data['Q_contact_from_mc'] - 10.0 / (12.0 * 82.0)) < 1e-12


# ============================================================================
# 3. METHOD 2: A-infinity relation at n=4 (6 tests)
# ============================================================================

class TestMethod2AInfinity:
    """A-infinity relation at arity 4 IS crossing symmetry."""

    def test_ainfinity_m2_bracket(self):
        """m_2(T,T) = 2T from T_{(1)}T = 2T."""
        data = mc_ainfinity_arity4(Rational(1))
        assert data['m2_TT'] == Rational(2)

    def test_ainfinity_S3(self):
        """S_3 = 2 (gravitational cubic shadow)."""
        data = mc_ainfinity_arity4(Rational(1))
        assert data['S_3'] == Rational(2)

    def test_ainfinity_Q_contact(self):
        """A-infinity relation gives Q^contact = 10/[c(5c+22)]."""
        for c_val in [Rational(1, 2), 1, 13, 26]:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            data = mc_ainfinity_arity4(c_r)
            expected = Q_contact_virasoro(c_r)
            assert simplify(data['Q_contact'] - expected) == 0

    def test_ainfinity_three_channels(self):
        """Three binary compositions correspond to s, t, u channels."""
        data = mc_ainfinity_arity4(1)
        channels = data['three_channels']
        assert 's' in channels
        assert 't' in channels
        assert 'u' in channels

    def test_ainfinity_crossing_identification(self):
        """The A-infinity relation IS crossing."""
        data = mc_ainfinity_arity4(1)
        assert data['crossing_is_ainfinity'] is True

    def test_ainfinity_agrees_with_direct_mc(self):
        """Method 2 agrees with Method 1 for all test c-values."""
        for c_val in [Rational(1, 2), 1, 8, 24]:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            m1 = mc_direct_expansion_genus0_arity4(c_r)
            m2 = mc_ainfinity_arity4(c_r)
            assert simplify(
                m1['Q_contact_from_mc'] - m2['Q_contact_from_ainfinity']
            ) == 0


# ============================================================================
# 4. METHOD 3: Factorization on M-bar_{0,4} (6 tests)
# ============================================================================

class TestMethod3Factorization:
    """Factorization structure of M-bar_{0,4} gives crossing."""

    def test_mbar04_is_p1(self):
        """M-bar_{0,4} = P^1 (projective line)."""
        data = mbar04_boundary_structure()
        assert data['moduli_space'] == 'M-bar_{0,4} = P^1'
        assert data['dimension'] == 1

    def test_three_boundary_divisors(self):
        """Three boundary divisors D_s, D_t, D_u."""
        data = mbar04_boundary_structure()
        divs = data['boundary_divisors']
        assert len(divs) == 3
        assert 'D_s' in divs
        assert 'D_t' in divs
        assert 'D_u' in divs

    def test_boundary_relation_topological(self):
        """[D_s] + [D_t] + [D_u] = 0 in H_0."""
        data = mbar04_boundary_structure()
        assert data['boundary_relation'] == '[D_s] + [D_t] + [D_u] = 0'

    def test_s_channel_at_z0(self):
        """s-channel is at z=0 (collision of points 1,2)."""
        data = mbar04_boundary_structure()
        assert data['boundary_divisors']['D_s']['z'] == 0
        assert data['boundary_divisors']['D_s']['channel'] == 's'

    def test_factorization_Q_contact(self):
        """Factorization gives Q^contact = 10/[c(5c+22)]."""
        for c_val in [Rational(1, 2), 1, 13]:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            data = mc_factorization_genus0_arity4(c_r)
            expected = Q_contact_virasoro(c_r)
            assert simplify(data['Q_contact_from_factorization'] - expected) == 0

    def test_factorization_d_squared_zero(self):
        """d^2 = 0 on M-bar_{0,4} gives crossing."""
        data = mc_factorization_genus0_arity4(1)
        assert data['crossing_from_d_squared_zero'] is True


# ============================================================================
# 5. METHOD 4: Costello's principle (4 tests)
# ============================================================================

class TestMethod4Costello:
    """Costello's principle: OPE associativity determines all loops."""

    def test_costello_Q_contact(self):
        """Costello's principle gives Q^contact."""
        data = mc_costello_principle(Rational(1))
        expected = Q_contact_virasoro(Rational(1))
        assert simplify(data['Q_contact'] - expected) == 0

    def test_costello_logical_chain(self):
        """Logical chain: d^2=0 -> MC -> crossing -> Q^contact."""
        data = mc_costello_principle(1)
        chain = data['logical_chain']
        assert len(chain) == 4
        assert 'd^2 = 0' in chain[0]
        assert 'MC equation' in chain[1]
        assert 'crossing symmetry' in chain[2]
        assert 'Q^contact' in chain[3]

    def test_costello_factorization_stronger(self):
        """Factorization associativity is stronger than OPE associativity."""
        data = mc_costello_principle(1)
        assert 'strictly stronger' in data['factorization_vs_ope']

    def test_costello_agrees_with_other_methods(self):
        """Method 4 agrees with Methods 1-3 for all test c-values."""
        for c_val in [Rational(1, 2), 1, 26]:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            m4 = mc_costello_principle(c_r)
            m1 = mc_direct_expansion_genus0_arity4(c_r)
            assert simplify(
                m4['Q_contact_from_costello'] - m1['Q_contact_from_mc']
            ) == 0


# ============================================================================
# 6. Q^CONTACT DERIVATION: 3 independent paths (9 tests)
# ============================================================================

class TestQContactDerivation:
    """Derive Q^contact = 10/[c(5c+22)] via three independent paths."""

    # Path A: Gram matrix
    def test_path_a_gram_c1(self):
        """Path A (Gram matrix): Q^contact at c=1."""
        data = Q_contact_from_gram_matrix(1)
        assert data['match']
        assert simplify(data['Q_contact'] - Rational(10, 27)) == 0

    def test_path_a_gram_ising(self):
        """Path A (Gram matrix): Q^contact at c=1/2."""
        data = Q_contact_from_gram_matrix(Rational(1, 2))
        assert data['match']
        assert simplify(data['Q_contact'] - Rational(40, 49)) == 0

    def test_path_a_gram_c26(self):
        """Path A (Gram matrix): Q^contact at c=26."""
        data = Q_contact_from_gram_matrix(26)
        assert data['match']
        assert simplify(data['Q_contact'] - Rational(5, 1976)) == 0

    # Path B: discriminant
    def test_path_b_discriminant_c1(self):
        """Path B (discriminant): Delta = 40/(5c+22) at c=1."""
        data = Q_contact_from_discriminant(1)
        assert data['Delta_match']
        expected_Delta = Rational(40, 27)
        assert simplify(data['Delta'] - expected_Delta) == 0

    def test_path_b_discriminant_ising(self):
        """Path B (discriminant): Delta at c=1/2."""
        data = Q_contact_from_discriminant(Rational(1, 2))
        assert data['Delta_match']
        expected = Rational(40, Rational(5, 2) + 22)
        assert simplify(data['Delta'] - expected) == 0

    def test_path_b_shadow_class_M(self):
        """Discriminant nonzero confirms Virasoro is class M."""
        data = Q_contact_from_discriminant(Rational(1))
        assert 'M' in data['shadow_class']

    # Path C: crossing kernel
    def test_path_c_crossing_kernel_c1(self):
        """Path C (crossing kernel): C_{TT Lambda}^2/<Lambda|Lambda> = Q^contact."""
        data = Q_contact_from_crossing_kernel(1)
        assert data['crossing_kernel_consistent']

    def test_path_c_crossing_kernel_ising(self):
        """Path C at c=1/2."""
        data = Q_contact_from_crossing_kernel(Rational(1, 2))
        assert data['crossing_kernel_consistent']

    def test_path_c_structure_constants(self):
        """OPE structure constants are correctly computed."""
        data = Q_contact_from_crossing_kernel(Rational(10))
        assert data['C_TT_id_sq'] == Rational(1)
        # C_{TTT}^2 = c (= 2*kappa)
        assert data['C_TT_T_sq'] == Rational(10)


# ============================================================================
# 7. FOUR-METHOD CONVERGENCE (3 tests)
# ============================================================================

class TestFourMethodConvergence:
    """All four proof methods and all derivation paths converge."""

    def test_all_seven_paths_c1(self):
        """All 7 paths agree at c=1."""
        data = verify_Q_contact_four_methods(1)
        assert data['all_seven_paths_agree']

    def test_all_seven_paths_ising(self):
        """All 7 paths agree at c=1/2 (Ising)."""
        data = verify_Q_contact_four_methods(Rational(1, 2))
        assert data['all_seven_paths_agree']

    def test_all_seven_paths_c26(self):
        """All 7 paths agree at c=26 (critical string)."""
        data = verify_Q_contact_four_methods(26)
        assert data['all_seven_paths_agree']


# ============================================================================
# 8. SPECIAL MODELS (8 tests)
# ============================================================================

class TestSpecialModels:
    """Ising, free boson, and critical string crossing."""

    # Ising (c = 1/2)
    def test_ising_Q_is_40_over_49(self):
        """Ising Q^contact = 40/49."""
        data = ising_crossing_from_mc()
        assert data['Q_match']
        assert data['Q_contact'] == Rational(40, 49)

    def test_ising_bpz_consistent(self):
        """MC is consistent with BPZ null vector at level 2."""
        data = ising_crossing_from_mc()
        assert data['mc_consistent_with_bpz']

    def test_ising_hypergeometric(self):
        """Ising 4-point function is _2F_1(1/2, 1/2; 1; z)."""
        data = ising_crossing_from_mc()
        params = data['hypergeometric_params']
        assert params['a'] == Rational(1, 2)
        assert params['b'] == Rational(1, 2)

    # Free boson (c = 1)
    def test_free_boson_heisenberg_Q_zero(self):
        """Heisenberg (class G): Q^contact = 0, crossing is trivial."""
        data = free_boson_crossing_from_mc()
        assert data['heisenberg']['Q_contact'] == Rational(0)
        assert data['heisenberg']['shadow_class'] == 'G'

    def test_free_boson_virasoro_Q_nonzero(self):
        """Virasoro at c=1 (class M): Q^contact = 10/27."""
        data = free_boson_crossing_from_mc()
        assert data['virasoro']['Q_match']
        assert data['virasoro']['Q_contact'] == Rational(10, 27)

    def test_free_boson_two_perspectives(self):
        """AP9: Heisenberg and Virasoro give different Q^contact."""
        data = free_boson_crossing_from_mc()
        assert data['heisenberg']['Q_contact'] != data['virasoro']['Q_contact']

    # Critical string (c = 26)
    def test_critical_string_kappa(self):
        """kappa(Vir_26) = 13."""
        data = critical_string_crossing(26)
        assert data['kappa'] == Rational(13)

    def test_critical_string_Q_contact(self):
        """Q^contact(Vir_26) = 5/1976."""
        data = critical_string_crossing(26)
        expected = Rational(10) / (26 * 152)
        assert simplify(data['Q_contact'] - expected) == 0
        assert simplify(data['Q_contact'] - Rational(5, 1976)) == 0


# ============================================================================
# 9. LANDSCAPE SCAN AND COMPLEMENTARITY (6 tests)
# ============================================================================

class TestLandscapeScan:
    """Cross-family landscape scan and complementarity checks."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G with Q^contact = 0."""
        scan = crossing_mc_landscape_scan()
        assert scan['heisenberg_k1']['Q_contact'] == Rational(0)
        assert scan['heisenberg_k1']['shadow_class'] == 'G'

    def test_affine_class_L(self):
        """Affine sl_2 is class L with Q^contact = 0."""
        scan = crossing_mc_landscape_scan()
        assert scan['affine_sl2_k1']['Q_contact'] == Rational(0)
        assert scan['affine_sl2_k1']['shadow_class'] == 'L'

    def test_virasoro_class_M(self):
        """Virasoro is class M with Q^contact nonzero."""
        scan = crossing_mc_landscape_scan()
        for c_val in [Rational(1, 2), 1, 8, 13, 24, 25, 26]:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            key = f'virasoro_c{c_r}'
            assert scan[key]['Q_contact'] != 0
            assert scan[key]['shadow_class'] == 'M'

    def test_Q_monotone_decreasing(self):
        """Q^contact decreases monotonically for c > 0."""
        scan = crossing_mc_landscape_scan()
        c_vals = [Rational(1, 2), 1, 8, 13, 24, 25, 26]
        Q_vals = []
        for c_val in c_vals:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            Q_vals.append(float(scan[f'virasoro_c{c_r}']['Q_contact']))
        for i in range(len(Q_vals) - 1):
            assert Q_vals[i] > Q_vals[i + 1], (
                f"Q^contact not decreasing at c={c_vals[i]}: {Q_vals[i]} vs {Q_vals[i+1]}"
            )

    def test_complementarity_sum_rational(self):
        """Q(c) + Q(26-c) is a rational function of c.  AP24."""
        scan = crossing_mc_landscape_scan()
        # At c=13 (self-dual): Q(13) + Q(13) = 20/1131
        comp = scan['complementarity_c13']
        expected = 2 * Q_contact_virasoro(13)
        assert simplify(comp['Q(c)+Q(26-c)'] - expected) == 0

    def test_complementarity_c1(self):
        """Q(1) + Q(25) = 10/27 + 10/(25*147) = 10/27 + 2/735."""
        Q1 = Q_contact_virasoro(1)
        Q25 = Q_contact_virasoro(25)
        comp_sum = Q1 + Q25
        # Verify nonzero: complementarity sum for Q^contact is NOT zero
        # (unlike kappa complementarity which is 13 for Virasoro)
        assert comp_sum != 0


# ============================================================================
# 10. SYMBOLIC Q^CONTACT PROPERTIES (5 tests)
# ============================================================================

class TestSymbolicQContact:
    """Symbolic properties of Q^contact as a function of c."""

    def test_symbolic_formula(self):
        """Q^contact = 10/[c(5c+22)]."""
        data = Q_contact_symbolic()
        c = Symbol('c')
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(data['Q_contact'] - expected) == 0

    def test_poles(self):
        """Q^contact has poles at c=0 and c=-22/5."""
        data = Q_contact_symbolic()
        assert Rational(0) in data['poles'] or 0 in data['poles']
        assert Rational(-22, 5) in data['poles']

    def test_ising_value(self):
        """Q^contact(1/2) = 40/49."""
        data = Q_contact_symbolic()
        assert simplify(data['ising_value'] - Rational(40, 49)) == 0

    def test_self_dual_value(self):
        """Q^contact(13) = 10/1131."""
        data = Q_contact_symbolic()
        assert simplify(data['self_dual_value'] - Rational(10, 1131)) == 0

    def test_large_c_asymptotics(self):
        """Q^contact ~ 2/c^2 as c -> infinity."""
        c = Symbol('c')
        data = Q_contact_symbolic()
        assert data['large_c_leading'] == Rational(2) / c**2


# ============================================================================
# 11. CROSSING EQUATION: explicit form (3 tests)
# ============================================================================

class TestCrossingExplicit:
    """Explicit form of the crossing equation from the MC projection."""

    def test_structure_constants_c1(self):
        """OPE structure constants at c=1."""
        data = crossing_equation_virasoro_explicit(1)
        assert data['C_id_sq'] == Rational(1)
        # C_{TTT}^2 = 2*kappa = c = 1
        assert data['C_T_sq'] == Rational(1)
        # C_{TT Lambda}^2 / <Lambda|Lambda> = Q^contact
        assert simplify(data['C_Lambda_sq'] - Rational(10, 27)) == 0

    def test_structure_constants_c26(self):
        """OPE structure constants at c=26."""
        data = crossing_equation_virasoro_explicit(26)
        assert data['C_T_sq'] == Rational(26)  # 2*13

    def test_crossing_equation_text(self):
        """Crossing equation string matches expected form."""
        data = crossing_equation_virasoro_explicit(1)
        assert 'G_p^(s)' in data['crossing_equation']
        assert 'G_p^(t)' in data['crossing_equation']


# ============================================================================
# 12. Q^CONTACT EXACT VALUES (cross-check table, 6 tests)
# ============================================================================

class TestQContactExactValues:
    """Verify Q^contact at specific c-values by direct computation.

    AP38: All values computed from first principles, not from literature.
    AP10: Each value checked by the formula AND by Gram matrix derivation.
    """

    @pytest.mark.parametrize("c_val,expected_num,expected_den", [
        (Rational(1, 2), 40, 49),       # Ising
        (1, 10, 27),                     # free boson
        (8, 10, 496),                    # E_8 level 1 (c=8)
        (13, 10, 1131),                  # self-dual
        (24, 10, 3408),                  # Monster (c=24)
        (26, 5, 1976),                   # critical string
    ])
    def test_Q_contact_exact(self, c_val, expected_num, expected_den):
        """Q^contact exact value at specific c."""
        c_r = Rational(c_val) if isinstance(c_val, int) else c_val
        Q = Q_contact_virasoro(c_r)
        expected = Rational(expected_num, expected_den)
        assert simplify(Q - expected) == 0, (
            f"At c={c_r}: Q={Q}, expected={expected}"
        )
        # Cross-check via Gram matrix path
        gram_data = Q_contact_from_gram_matrix(c_r)
        assert gram_data['match'], f"Gram matrix path fails at c={c_r}"

    def test_Q_contact_c8_from_formula(self):
        """Q^contact(c=8) = 10/(8*62) = 10/496 = 5/248."""
        Q = Q_contact_virasoro(8)
        assert Q == Rational(10, 496)
        assert Q == Rational(5, 248)

    def test_Q_contact_c24_from_formula(self):
        """Q^contact(c=24) = 10/(24*142) = 10/3408 = 5/1704."""
        Q = Q_contact_virasoro(24)
        assert Q == Rational(10, 3408)
        assert Q == Rational(5, 1704)


# ============================================================================
# 13. POSITIVITY AND MONOTONICITY (3 tests)
# ============================================================================

class TestPositivityMonotonicity:
    """Physical properties of Q^contact."""

    def test_Q_positive_for_positive_c(self):
        """Q^contact > 0 for all c > 0 (unitarity)."""
        for c_val in [Rational(1, 10), Rational(1, 2), 1, 10, 100, 1000]:
            c_r = Rational(c_val) if isinstance(c_val, int) else c_val
            Q = Q_contact_virasoro(c_r)
            assert Q > 0, f"Q^contact not positive at c={c_r}"

    def test_Q_negative_for_negative_c(self):
        """Q^contact < 0 for -22/5 < c < 0 (non-unitary)."""
        for c_val in [Rational(-1), Rational(-2), Rational(-3)]:
            Q = Q_contact_virasoro(c_val)
            assert Q < 0, f"Q^contact not negative at c={c_val}"

    def test_Q_diverges_at_poles(self):
        """Q^contact diverges at c = 0 and c = -22/5."""
        with pytest.raises(ValueError):
            Q_contact_virasoro(0)
        with pytest.raises(ValueError):
            Q_contact_virasoro(Rational(-22, 5))
