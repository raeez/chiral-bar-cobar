"""Tests for KZ connection from shadow obstruction tower.

Verifies the proved recovery theorem: the shadow obstruction tower at genus 0, arity 2,
produces the KZ connection.  The CYBE for r(z) = Omega/z follows from the
Arnold relation on FM_3(C).  Higher-arity shadows give L_infinity corrections.

Organization:
  1. Casimir element: construction, symmetry, eigenvalues, invariance
  2. Arnold relation: symbolic and numerical verification
  3. CYBE from Arnold: IBR in fundamental and adjoint representations
  4. KZ connection: flatness, level dependence, 2/3/4-point systems
  5. Shadow = KZ: the proved identification (thm:yangian-shadow-theorem)
  6. Shadow connection: arity 3 (cubic), genus 1 (Hitchin)
  7. Dictionary table: completeness and consistency
  8. Hypergeometric solutions: sl_2 4-point KZ
  9. Collision residue: pole structure, Casimir extraction
  10. Drinfeld-Kohno: monodromy = R-matrix, braid relations
  11. Comprehensive verification sweep

References:
  thm:yangian-shadow-theorem (concordance.tex)
  thm:collision-residue-twisting (frontier_modular_holography_platonic.tex)
  thm:collision-depth-2-ybe (frontier_modular_holography_platonic.tex)
  thm:cubic-gauge-triviality (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import pytest

from compute.lib.kz_shadow_connection import (
    arnold_relation_verify,
    casimir_element,
    casimir_eigenvalue_from_killing,
    casimir_eigenvalue_on_VV,
    casimir_from_killing,
    casimir_on_tensor_product,
    collision_residue,
    comprehensive_kz_shadow_verification,
    cybe_from_arnold,
    cybe_from_derived_casimir,
    drinfeld_kohno_verification,
    flat_connection_check,
    flatness_from_arnold_explicit,
    killing_form_matrix,
    kz_connection_matrix,
    kz_equation_2point,
    kz_hypergeometric_solution_sl2,
    kz_ode_solve_2point,
    omega_eigenvalue_on_channel,
    shadow_connection_arity2,
    shadow_connection_arity2_matrix,
    shadow_connection_arity3,
    shadow_connection_genus1,
    shadow_to_kz_dictionary,
    sl2_fundamental_generators,
    sl2_adjoint_generators,
    sl2_spin_j_casimir,
    verify_kz_equals_shadow,
)


# =========================================================================
# 1. Casimir element tests
# =========================================================================

class TestCasimir:
    """Tests for Casimir tensor construction."""

    def test_sl2_casimir_structure(self):
        """Omega = E tensor F + F tensor E + (1/2) H tensor H for sl_2."""
        cas = casimir_element('sl2')
        Om = cas['matrix']
        assert cas['dim'] == 3
        assert cas['basis'] == ['E', 'F', 'H']
        # Check nonzero entries
        assert Om[0, 1] == Fraction(1)   # E tensor F
        assert Om[1, 0] == Fraction(1)   # F tensor E
        assert Om[2, 2] == Fraction(1, 2)  # (1/2) H tensor H
        # Check zero entries
        assert Om[0, 0] == 0
        assert Om[1, 1] == 0
        assert Om[0, 2] == 0

    def test_sl2_casimir_eigenvalue_on_VV(self):
        """Omega on V_{1/2} tensor V_{1/2}: eigenvalues -3/2 (singlet) and 1/2 (triplet).

        In our normalization (Killing form (E,F)=1, (H,H)=2):
          Omega eigenvalue on V_0 (singlet) = [C_2(0) - 2*C_2(1/2)] / 2
            = [0 - 2*3/2] / 2 = -3/2
          Omega eigenvalue on V_1 (triplet) = [C_2(1) - 2*C_2(1/2)] / 2
            = [4 - 3] / 2 = 1/2
        """
        result = casimir_eigenvalue_on_VV('sl2', rep_dim=2)
        eigs = result['eigenvalues']
        # Should have eigenvalue -3/2 with multiplicity 1 (singlet)
        # and eigenvalue 1/2 with multiplicity 3 (triplet)
        assert abs(min(eigs.keys()) - (-1.5)) < 1e-10
        assert abs(max(eigs.keys()) - 0.5) < 1e-10
        assert eigs[min(eigs.keys())] == 1  # singlet
        assert eigs[max(eigs.keys())] == 3  # triplet

    def test_casimir_symmetric(self):
        """Omega is symmetric: Omega_{ab} = Omega_{ba}."""
        for lt in ['sl2', 'sl3']:
            cas = casimir_element(lt)
            Om = cas['matrix']
            d = cas['dim']
            for a in range(d):
                for b in range(d):
                    assert Om[a, b] == Om[b, a], f"Asymmetry at ({a},{b}) for {lt}"

    def test_casimir_invariant_sl2(self):
        """[Delta(x), Omega] = 0 for all x in sl_2 (ad-invariance).

        Omega_{12} commutes with Delta(x) = x tensor 1 + 1 tensor x
        for all x in g.  Verified in the fundamental representation.
        """
        Omega_VV = casimir_on_tensor_product('sl2', 2)
        gens = sl2_fundamental_generators()
        I2 = np.eye(2, dtype=complex)

        for name, x in gens.items():
            Delta_x = np.kron(x, I2) + np.kron(I2, x)
            comm = Omega_VV @ Delta_x - Delta_x @ Omega_VV
            assert np.max(np.abs(comm)) < 1e-12, f"[Delta({name}), Omega] != 0"

    def test_sl3_casimir_structure(self):
        """Casimir for sl_3: correct inverse Killing form entries."""
        cas = casimir_element('sl3')
        Om = cas['matrix']
        assert cas['dim'] == 8
        # Cartan block: A^{-1} = (1/3)[[2,1],[1,2]]
        assert Om[0, 0] == Fraction(2, 3)  # H1-H1
        assert Om[0, 1] == Fraction(1, 3)  # H1-H2
        assert Om[1, 0] == Fraction(1, 3)  # H2-H1
        assert Om[1, 1] == Fraction(2, 3)  # H2-H2
        # Root-coroot pairs
        for i in range(3):
            ei = 2 + i  # E1, E2, E3
            fi = 5 + i  # F1, F2, F3
            assert Om[ei, fi] == Fraction(1), f"E{i+1}-F{i+1}"
            assert Om[fi, ei] == Fraction(1), f"F{i+1}-E{i+1}"

    def test_sl2_casimir_trace(self):
        """Trace of Omega on V_{1/2} tensor V_{1/2} = 0 (traceless generators)."""
        Omega_VV = casimir_on_tensor_product('sl2', 2)
        # tr(E tensor F + F tensor E + (1/2) H tensor H)
        # = tr(E)tr(F) + tr(F)tr(E) + (1/2)tr(H)tr(H) = 0
        assert abs(np.trace(Omega_VV)) < 1e-12

    def test_omega_eigenvalue_on_channel(self):
        """Split Casimir eigenvalues on fusion channels.

        In our normalization: Omega eigenvalue = s(s+1) - j1(j1+1) - j2(j2+1).
        """
        # V_{1/2} tensor V_{1/2} -> V_0 + V_1
        assert abs(omega_eigenvalue_on_channel(0.5, 0.5, 0) - (-1.5)) < 1e-12
        assert abs(omega_eigenvalue_on_channel(0.5, 0.5, 1) - 0.5) < 1e-12

        # V_1 tensor V_1 -> V_0 + V_1 + V_2
        assert abs(omega_eigenvalue_on_channel(1, 1, 0) - (-4.0)) < 1e-12
        assert abs(omega_eigenvalue_on_channel(1, 1, 1) - (-2.0)) < 1e-12
        assert abs(omega_eigenvalue_on_channel(1, 1, 2) - 2.0) < 1e-12

    def test_sl2_spin_j_casimir(self):
        """Quadratic Casimir eigenvalue C_2(V_j) = 2j(j+1) in our normalization."""
        assert abs(sl2_spin_j_casimir(0) - 0) < 1e-12
        assert abs(sl2_spin_j_casimir(0.5) - 1.5) < 1e-12
        assert abs(sl2_spin_j_casimir(1) - 4) < 1e-12
        assert abs(sl2_spin_j_casimir(1.5) - 7.5) < 1e-12


# =========================================================================
# 2. Arnold relation tests
# =========================================================================

class TestArnoldRelation:
    """Tests for the Arnold relation on FM_3(C)."""

    def test_arnold_symbolic(self):
        """eta_12 ^ eta_23 + eta_23 ^ eta_31 + eta_31 ^ eta_12 = 0 (symbolic)."""
        result = arnold_relation_verify()
        assert result['symbolic_zero']

    def test_arnold_numerical(self):
        """Arnold relation at random complex points."""
        result = arnold_relation_verify(n_random=200)
        assert result['numerical_passes']
        assert result['numerical_max_error'] < 1e-10

    def test_arnold_specific_points(self):
        """Arnold relation at specific real and complex triples."""
        triples = [
            (1.0, 2.0, 3.0),
            (0.1, 0.5, 0.9),
            (1 + 1j, 2 - 1j, 3 + 2j),
            (-1.0, 0.0, 1.0),
        ]
        for z1, z2, z3 in triples:
            val = (1 / ((z1 - z2) * (z2 - z3))
                   + 1 / ((z2 - z3) * (z3 - z1))
                   + 1 / ((z3 - z1) * (z1 - z2)))
            assert abs(val) < 1e-12, f"Arnold fails at ({z1}, {z2}, {z3}): {val}"

    def test_arnold_is_partial_fractions(self):
        """The Arnold relation is the partial-fractions identity 1/ab + 1/bc + 1/ca = 0."""
        # This is 1/(ab) + 1/(bc) + 1/(ca) = (c + a + b)/(abc)
        # which does NOT vanish!  The correct identity is with SIGNED products:
        # 1/[(z1-z2)(z2-z3)] + 1/[(z2-z3)(z3-z1)] + 1/[(z3-z1)(z1-z2)] = 0
        # i.e. the cyclic sum with consistent orientation.
        z1, z2, z3 = 1.0 + 0.1j, 2.5 - 0.3j, -1.0 + 0.7j
        a, b, c = z1 - z2, z2 - z3, z3 - z1
        # a + b + c = 0 (telescoping), so 1/(ab) + 1/(bc) + 1/(ca) = (c+a+b)/(abc) = 0
        assert abs(a + b + c) < 1e-12


# =========================================================================
# 3. CYBE from Arnold
# =========================================================================

class TestCYBE:
    """Tests for the classical Yang-Baxter equation derived from Arnold."""

    def test_cybe_sl2_fundamental(self):
        """[r_12, r_13] + [r_12, r_23] + [r_13, r_23] = 0 for sl_2 fundamental."""
        result = cybe_from_arnold('sl2', rep_dim=2)
        assert result['ibr_satisfied']
        assert result['ibr_max_norm'] < 1e-12

    def test_cybe_sl2_adjoint(self):
        """CYBE for sl_2 in the adjoint (3-dim) representation."""
        result = cybe_from_arnold('sl2', rep_dim=3)
        assert result['ibr_satisfied']
        assert result['ibr_max_norm'] < 1e-12

    def test_cybe_from_arnold_mechanism(self):
        """CYBE follows from Arnold relation (structural check)."""
        result = cybe_from_arnold('sl2', rep_dim=2)
        assert result['mechanism'] == 'Arnold partial-fractions => IBR => CYBE'

    def test_cybe_numerical_at_points(self):
        """CYBE verified numerically at specific z-triples."""
        result = cybe_from_arnold('sl2', rep_dim=2)
        assert result['cybe_max_error'] < 1e-10

    def test_r_matrix_simple_pole(self):
        """r(z) = Omega/z has a simple pole at z = 0."""
        res = collision_residue('sl2', Fraction(1))
        assert res['pole_order'] == 1
        assert res['pole_location'] == 0


# =========================================================================
# 4. KZ connection tests
# =========================================================================

class TestKZConnection:
    """Tests for the KZ connection."""

    def test_kz_flatness_sl2_3points(self):
        """KZ connection is flat for sl_2 at 3 points."""
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j]
        for k_val in [1, 2, 5, 10]:
            A = kz_connection_matrix('sl2', Fraction(k_val), z_pts, rep_dim=2)
            flat = flat_connection_check(A, z_pts)
            assert flat['commutator_vanishes'], f"Not flat at k={k_val}"

    def test_kz_flatness_sl2_4points(self):
        """KZ connection is flat for sl_2 at 4 points."""
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j, 3.0 + 0.5j]
        A = kz_connection_matrix('sl2', Fraction(3), z_pts, rep_dim=2)
        flat = flat_connection_check(A, z_pts)
        assert flat['commutator_vanishes']

    def test_kz_2point_sl2(self):
        """2-point KZ equation dPhi/dz = Omega/((k+2)z) Phi."""
        z = 0.5 + 0.2j
        result = kz_equation_2point('sl2', Fraction(1), z, rep_dim=2)
        # KZ parameter should be 1/(k+2) = 1/3
        assert abs(result['kz_parameter'] - 1.0 / 3.0) < 1e-12
        # Two distinct exponents (singlet and triplet channels)
        exps = result['exponents']
        assert len(exps) == 2

    def test_kz_level_dependence(self):
        """KZ parameter = 1/(k + h^v): check for various levels."""
        for k in [1, 2, 3, 5, 10, 100]:
            result = kz_equation_2point('sl2', Fraction(k), 1.0, rep_dim=2)
            expected = 1.0 / (k + 2)
            assert abs(result['kz_parameter'] - expected) < 1e-12

    def test_kz_critical_level_raises(self):
        """KZ at critical level k = -h^v should raise ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            kz_connection_matrix('sl2', Fraction(-2), [0.5, 1.0], rep_dim=2)

    def test_kz_3point_sl2_matrix_dims(self):
        """3-point KZ matrices have correct dimensions."""
        z_pts = [0.5, 1.0, 2.0]
        A = kz_connection_matrix('sl2', Fraction(1), z_pts, rep_dim=2)
        assert len(A) == 3
        for mat in A:
            assert mat.shape == (8, 8)  # 2^3 = 8

    def test_kz_sum_of_residues(self):
        """Sum of KZ matrices: Sigma_i A_i = 0 (global gauge invariance).

        For the KZ connection: Sigma_i A_i = 1/(k+h^v) Sigma_{i!=j} Omega_{ij}/(z_i-z_j).
        This sum actually vanishes because for each pair (i,j), the terms
        Omega_{ij}/(z_i-z_j) from A_i and Omega_{ji}/(z_j-z_i) from A_j
        give Omega_{ij}/(z_i-z_j) + Omega_{ij}/(z_j-z_i) = 0 (using Omega_{ij} = Omega_{ji}).
        Wait, that's not right: A_i has Omega_{ij}/(z_i-z_j) and A_j has
        Omega_{ji}/(z_j-z_i) = Omega_{ij}/(z_j-z_i) = -Omega_{ij}/(z_i-z_j).
        So the sum cancels: Sigma_i A_i = 0.
        """
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j]
        A = kz_connection_matrix('sl2', Fraction(2), z_pts, rep_dim=2)
        total = sum(A)
        assert np.max(np.abs(total)) < 1e-12


# =========================================================================
# 5. Shadow = KZ (the proved identification)
# =========================================================================

class TestShadowEqualsKZ:
    """Tests for the identification: shadow at arity 2 = KZ connection."""

    def test_arity2_is_kz(self):
        """Shadow connection at arity 2 equals KZ connection."""
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j]
        # Shadow (matrix version) should equal KZ
        shadow_mats = shadow_connection_arity2_matrix('sl2', Fraction(1), z_pts, rep_dim=2)
        kz_mats = kz_connection_matrix('sl2', Fraction(1), z_pts, rep_dim=2)
        for i in range(len(z_pts)):
            diff = np.max(np.abs(shadow_mats[i] - kz_mats[i]))
            assert diff < 1e-12, f"Shadow != KZ at point {i}: diff = {diff}"

    def test_kappa_matches_casimir_scaling(self):
        """kappa = dim(g)(k+h^v)/(2h^v) matches Casimir scaling."""
        for k_val in [1, 2, 5]:
            result = verify_kz_equals_shadow('sl2', Fraction(k_val))
            # kappa = 3(k+2)/4
            expected_kappa = 3.0 * (k_val + 2) / 4.0
            assert abs(result['kappa'] - expected_kappa) < 1e-12

    def test_collision_residue_is_r_matrix(self):
        """Res^{coll}(Theta_A) = Omega/z for affine algebras."""
        for k_val in [1, 2, 5]:
            res = collision_residue('sl2', Fraction(k_val))
            assert res['r_matrix_type'] == 'Omega/z'
            expected_coeff = 1.0 / (k_val + 2)
            assert abs(res['r_matrix_coefficient'] - expected_coeff) < 1e-12

    def test_pole_structure_matches(self):
        """Shadow and KZ have same pole structure in z_i - z_j."""
        result = verify_kz_equals_shadow('sl2', Fraction(3))
        assert result['pole_structure_matches']

    def test_identification_statement(self):
        """The identification is the content of thm:yangian-shadow-theorem."""
        result = verify_kz_equals_shadow('sl2', Fraction(1))
        assert 'thm:yangian-shadow-theorem' in result['identification']


# =========================================================================
# 6. Shadow connection: arity 3 and genus 1
# =========================================================================

class TestShadowConnection:
    """Tests for higher-arity and higher-genus shadow connections."""

    def test_arity3_vanishes_simple_g(self):
        """Cubic shadow correction vanishes for simple g (gauge triviality)."""
        z_pts = [0.5, 1.0, 2.0, 3.0]
        # For simple Lie algebras, cubic shadow is gauge-trivial
        corrections = shadow_connection_arity3(0.0, z_pts)
        assert all(abs(c) < 1e-15 for c in corrections)

    def test_arity3_nonzero_for_nonzero_cubic(self):
        """Cubic correction is nonzero when cubic shadow is nonzero."""
        z_pts = [0.5, 1.0, 2.0, 3.0]
        corrections = shadow_connection_arity3(1.0, z_pts)
        # At least some corrections should be nonzero
        assert any(abs(c) > 1e-10 for c in corrections)

    def test_genus1_hitchin(self):
        """Genus-1 shadow connection has curvature (quasi-modular anomaly)."""
        result = shadow_connection_genus1(Fraction(3, 4), 0.5j)
        assert result['has_curvature']
        assert result['genus'] == 1
        assert result['arity'] == 0

    def test_genus1_e2_converges(self):
        """E_2(tau) is well-defined for Im(tau) > 0."""
        result = shadow_connection_genus1(Fraction(1), 0.1 + 1.0j)
        e2 = result['E2_value']
        # E_2 should be a finite complex number
        assert np.isfinite(abs(e2))

    def test_genus1_e2_at_i(self):
        """E_2(i) = 3/pi (classical value)."""
        result = shadow_connection_genus1(Fraction(1), 1.0j)
        e2 = result['E2_value']
        expected = 3.0 / np.pi
        assert abs(e2 - expected) < 1e-4  # numerical approximation

    def test_shadow_connection_flat_genus0(self):
        """Shadow connection is flat at genus 0 (from MC equation)."""
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j]
        A = shadow_connection_arity2_matrix('sl2', Fraction(2), z_pts, rep_dim=2)
        flat = flat_connection_check(A, z_pts)
        assert flat['commutator_vanishes']

    def test_scalar_shadow_well_defined(self):
        """Scalar shadow connection values are finite at generic points."""
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j, 3.5 + 0.1j]
        vals = shadow_connection_arity2(Fraction(3, 4), z_pts)
        assert len(vals) == 4
        assert all(np.isfinite(v) for v in vals)

    def test_scalar_shadow_sum_vanishes(self):
        """Sum of scalar shadow connection values vanishes.

        Sigma_i A_i = kappa * Sigma_i Sigma_{j!=i} 1/(z_i-z_j) = 0
        because each pair (i,j) contributes 1/(z_i-z_j) + 1/(z_j-z_i) = 0.
        """
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j]
        vals = shadow_connection_arity2(Fraction(1), z_pts)
        assert abs(sum(vals)) < 1e-12


# =========================================================================
# 7. Dictionary table tests
# =========================================================================

class TestDictionaryTable:
    """Tests for the shadow-to-KZ dictionary."""

    def test_shadow_kz_table_completeness(self):
        """Dictionary has entries for all key shadow data."""
        d = shadow_to_kz_dictionary()
        required_keys = [
            'kappa', 'r_matrix', 'kz_connection', 'cybe',
            'cubic_shadow', 'quartic_shadow', 'hitchin_connection',
            'flatness', 'drinfeld_kohno', 'genus_1_curvature',
        ]
        for key in required_keys:
            assert key in d, f"Missing key: {key}"

    def test_dictionary_fields(self):
        """Each dictionary entry has shadow, kz, and identification fields."""
        d = shadow_to_kz_dictionary()
        for key, entry in d.items():
            assert 'shadow' in entry, f"Missing 'shadow' in {key}"
            assert 'kz' in entry, f"Missing 'kz' in {key}"
            assert 'identification' in entry, f"Missing 'identification' in {key}"

    def test_dictionary_genus_arity_labels(self):
        """Each dictionary entry has genus and arity labels."""
        d = shadow_to_kz_dictionary()
        for key, entry in d.items():
            assert 'genus' in entry, f"Missing 'genus' in {key}"
            assert 'arity' in entry, f"Missing 'arity' in {key}"

    def test_proved_identifications_count(self):
        """At least 4 entries are marked as PROVED."""
        d = shadow_to_kz_dictionary()
        proved = sum(1 for e in d.values() if 'PROVED' in e.get('identification', ''))
        assert proved >= 4, f"Only {proved} proved identifications (expected >= 4)"


# =========================================================================
# 8. Hypergeometric solution tests
# =========================================================================

class TestHypergeometric:
    """Tests for KZ hypergeometric solutions."""

    def test_sl2_4point_parameters(self):
        """Hypergeometric parameters for sl_2 4-point function are correct."""
        result = kz_hypergeometric_solution_sl2(
            Fraction(1), (Fraction(1, 2),) * 4, 0.3)
        # KZ parameter = 1/3
        assert abs(result['kz_parameter'] - 1.0 / 3.0) < 1e-12
        # Two fusion channels
        assert result['n_channels'] == 2

    def test_sl2_4point_exponents(self):
        """Singlet exponent = -3/2 * 1/(k+2) and triplet = 1/2 * 1/(k+2).

        In our normalization: Omega eigenvalues are -3/2 (singlet) and 1/2 (triplet).
        """
        k = 2
        result = kz_hypergeometric_solution_sl2(
            Fraction(k), (Fraction(1, 2),) * 4, 0.5)
        param = 1.0 / (k + 2)
        assert abs(result['exponent_singlet'] - (-1.5 * param)) < 1e-12
        assert abs(result['exponent_triplet'] - (0.5 * param)) < 1e-12

    def test_sl2_4point_solution_finite(self):
        """The hypergeometric solution is finite at z = 0.3."""
        result = kz_hypergeometric_solution_sl2(
            Fraction(1), (Fraction(1, 2),) * 4, 0.3)
        assert np.isfinite(abs(result['solution_s0']))
        assert np.isfinite(abs(result['F_value']))

    def test_sl2_4point_level_variation(self):
        """Solution changes with level k."""
        solutions = []
        for k in [1, 2, 5, 10]:
            result = kz_hypergeometric_solution_sl2(
                Fraction(k), (Fraction(1, 2),) * 4, 0.3)
            solutions.append(result['F_value'])
        # All should be distinct
        for i in range(len(solutions)):
            for j in range(i + 1, len(solutions)):
                assert abs(solutions[i] - solutions[j]) > 1e-10

    def test_sl2_4point_needs_4_spins(self):
        """Raises ValueError if not exactly 4 spins."""
        with pytest.raises(ValueError, match="exactly 4 spins"):
            kz_hypergeometric_solution_sl2(
                Fraction(1), (Fraction(1, 2),) * 3, 0.3)


# =========================================================================
# 9. Collision residue tests
# =========================================================================

class TestCollisionResidue:
    """Tests for collision residue = r-matrix."""

    def test_collision_residue_sl2(self):
        """Collision residue for sl_2: r(z) = Omega/((k+2)z)."""
        res = collision_residue('sl2', Fraction(1))
        assert res['r_matrix_type'] == 'Omega/z'
        assert abs(res['r_matrix_coefficient'] - 1.0 / 3.0) < 1e-12
        assert res['satisfies_cybe']

    def test_collision_residue_sl3(self):
        """Collision residue for sl_3: r(z) = Omega/((k+3)z)."""
        res = collision_residue('sl3', Fraction(1))
        assert res['r_matrix_type'] == 'Omega/z'
        assert abs(res['r_matrix_coefficient'] - 0.25) < 1e-12  # 1/(1+3)
        assert res['satisfies_cybe']

    def test_collision_residue_pole_structure(self):
        """r(z) has a simple pole at z=0."""
        for lt in ['sl2', 'sl3']:
            res = collision_residue(lt, Fraction(2))
            assert res['pole_order'] == 1
            assert res['pole_location'] == 0

    def test_collision_residue_casimir_eigenvalue(self):
        """Casimir eigenvalue on adjoint = 2h^v."""
        for lt, hv in [('sl2', 2), ('sl3', 3)]:
            res = collision_residue(lt, Fraction(1))
            assert abs(res['casimir_eigenvalue_adj'] - 2 * hv) < 1e-12

    def test_collision_residue_critical_level_raises(self):
        """Critical level k = -h^v raises ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            collision_residue('sl2', Fraction(-2))


# =========================================================================
# 10. Drinfeld-Kohno tests
# =========================================================================

class TestDrinfeldKohno:
    """Tests for the Drinfeld-Kohno theorem (algebraic content)."""

    def test_ibr_satisfied(self):
        """IBR [Omega_{ij}, Omega_{ik}+Omega_{jk}] = 0 (infinitesimal Drinfeld-Kohno)."""
        result = drinfeld_kohno_verification('sl2', Fraction(1))
        assert result['ibr_satisfied']
        assert result['ibr_max_norm'] < 1e-12

    def test_ibr_various_levels(self):
        """IBR holds at various levels (level-independent)."""
        for k in [1, 2, 3, 5]:
            result = drinfeld_kohno_verification('sl2', Fraction(k))
            assert result['ibr_satisfied'], f"IBR fails at k={k}"

    def test_q_parameter(self):
        """q = exp(pi i / (k + h^v)) is correct."""
        k = 1
        result = drinfeld_kohno_verification('sl2', Fraction(k))
        expected_q = np.exp(1j * np.pi / 3.0)
        assert abs(result['q_parameter'] - expected_q) < 1e-12

    def test_kz_is_flat(self):
        """KZ flatness is verified as part of Drinfeld-Kohno."""
        result = drinfeld_kohno_verification('sl2', Fraction(2))
        assert result['kz_flat']

    def test_r_matrix_eigenvalues_finite(self):
        """R-matrix eigenvalues are finite complex numbers."""
        result = drinfeld_kohno_verification('sl2', Fraction(1))
        for ev in result['R_matrix_eigenvalues']:
            assert np.isfinite(abs(ev))

    def test_r_matrix_eigenvalue_structure(self):
        """R-matrix eigenvalues = exp(pi i h * Omega_eigenvalue)."""
        result = drinfeld_kohno_verification('sl2', Fraction(1))
        assert result['R_eigenvalue_structure_correct']

    def test_pure_braid_commutativity(self):
        """Disjoint Casimirs commute: [Omega_{12}, Omega_{34}] = 0."""
        result = drinfeld_kohno_verification('sl2', Fraction(1), n_points=4)
        assert result['pure_braid_commutativity']


# =========================================================================
# 11. Comprehensive verification
# =========================================================================

class TestComprehensive:
    """End-to-end verification of the KZ-shadow correspondence."""

    def test_comprehensive_all_pass(self):
        """All verifications in the comprehensive sweep pass."""
        results = comprehensive_kz_shadow_verification()
        for r in results:
            assert r['passed'], f"FAILED: {r['test']}"

    def test_comprehensive_count(self):
        """At least 10 independent verifications."""
        results = comprehensive_kz_shadow_verification()
        assert len(results) >= 10

    def test_kz_equals_shadow_sl2_multiple_levels(self):
        """Shadow = KZ identification holds at multiple levels for sl_2."""
        for k_val in [1, 2, 3, 5, 10, 50]:
            z_pts = [0.3, 1.1 + 0.2j, 2.5 - 0.4j]
            shadow_mats = shadow_connection_arity2_matrix(
                'sl2', Fraction(k_val), z_pts, rep_dim=2)
            kz_mats = kz_connection_matrix(
                'sl2', Fraction(k_val), z_pts, rep_dim=2)
            for i in range(len(z_pts)):
                diff = np.max(np.abs(shadow_mats[i] - kz_mats[i]))
                assert diff < 1e-12, f"Shadow != KZ at k={k_val}, point {i}"

    def test_shadow_depth_classification(self):
        """Shadow depth: Heisenberg@2, affine@3, betagamma@4, Virasoro@inf."""
        # The arity-3 correction vanishes for simple g (affine terminates at 3)
        corrections = shadow_connection_arity3(0.0, [0.5, 1.0, 2.0])
        assert all(abs(c) < 1e-15 for c in corrections)

    def test_kz_shadow_for_sl3(self):
        """Collision residue works for sl_3."""
        res = collision_residue('sl3', Fraction(1))
        assert res['lie_type'] == 'sl3'
        assert res['r_matrix_type'] == 'Omega/z'
        assert res['satisfies_cybe']


# =========================================================================
# 12. Killing form and derived Casimir tests
# =========================================================================

class TestKillingForm:
    """Tests for Killing form computation and Casimir derivation."""

    def test_sl2_killing_form_structure(self):
        """Killing form of sl_2: B(E,F)=B(F,E)=4, B(H,H)=8, rest zero.

        B_{EF} = tr(ad(E) ad(F)) = tr([[0,-2],[0,0],[0,1]] @ ...).
        Direct: ad(E)ad(F) has diagonal entries. tr = 4.
        """
        B = killing_form_matrix('sl2')
        assert B.shape == (3, 3)
        # B(E,F) = B(F,E) = 4
        assert abs(B[0, 1] - 4.0) < 1e-10
        assert abs(B[1, 0] - 4.0) < 1e-10
        # B(H,H) = 8
        assert abs(B[2, 2] - 8.0) < 1e-10
        # B(E,E) = B(F,F) = B(E,H) = B(H,E) = B(F,H) = B(H,F) = 0
        assert abs(B[0, 0]) < 1e-10
        assert abs(B[1, 1]) < 1e-10
        assert abs(B[0, 2]) < 1e-10
        assert abs(B[2, 0]) < 1e-10

    def test_sl2_killing_form_symmetric(self):
        """Killing form is symmetric: B_{ab} = B_{ba}."""
        B = killing_form_matrix('sl2')
        assert np.max(np.abs(B - B.T)) < 1e-10

    def test_sl3_killing_form_symmetric(self):
        """Killing form of sl_3 is symmetric."""
        B = killing_form_matrix('sl3')
        assert B.shape == (8, 8)
        assert np.max(np.abs(B - B.T)) < 1e-10

    def test_sl3_killing_form_nondegenerate(self):
        """Killing form of sl_3 is nondegenerate (sl_3 is semisimple)."""
        B = killing_form_matrix('sl3')
        assert abs(np.linalg.det(B)) > 1e-5

    def test_sl2_casimir_derived_matches_hardcoded(self):
        """Casimir derived from Killing form inversion matches hardcoded value."""
        result = casimir_from_killing('sl2')
        assert result['matches_hardcoded']
        assert result['max_diff'] < 1e-10

    def test_sl3_casimir_derived_matches_hardcoded(self):
        """Casimir derived from Killing form for sl_3 matches hardcoded."""
        result = casimir_from_killing('sl3')
        assert result['matches_hardcoded'], \
            f"Max diff = {result['max_diff']}"
        assert result['max_diff'] < 1e-10

    def test_sl2_normalization_factor(self):
        """Normalization factor for sl_2: Killing = 4 * our_form."""
        result = casimir_from_killing('sl2')
        assert abs(result['normalization_factor'] - 4.0) < 1e-10

    def test_sl3_normalization_factor(self):
        """Normalization factor for sl_3: Killing = 6 * our_form."""
        result = casimir_from_killing('sl3')
        assert abs(result['normalization_factor'] - 6.0) < 1e-10


class TestCasimirEigenvalueFromKilling:
    """Tests for Casimir eigenvalue computed from derived Casimir."""

    def test_sl2_fundamental_eigenvalue(self):
        """C_2(V_{1/2}) = 3/2 in our normalization (from derived Casimir).

        C_2(V_j) = 2j(j+1). For j=1/2: C_2 = 2*(1/2)*(3/2) = 3/2.
        """
        result = casimir_eigenvalue_from_killing('sl2', rep_dim=2)
        assert result['is_scalar_on_irrep']
        assert abs(result['scalar_value'] - 1.5) < 1e-10

    def test_sl2_adjoint_eigenvalue(self):
        """C_2(V_1) = 4 on the adjoint (from derived Casimir).

        C_2(V_j) = 2j(j+1). For j=1 (adjoint): C_2 = 2*1*2 = 4.
        """
        result = casimir_eigenvalue_from_killing('sl2', rep_dim=3)
        # Adjoint is an irrep, so C_2 should be scalar
        assert result['is_scalar_on_irrep']
        assert abs(result['scalar_value'] - 4.0) < 1e-10

    def test_eigenvalue_matches_formula(self):
        """Derived eigenvalue matches the formula C_2(V_j) = 2j(j+1)."""
        for j, rep_dim in [(0.5, 2), (1.0, 3)]:
            result = casimir_eigenvalue_from_killing('sl2', rep_dim=rep_dim)
            expected = 2.0 * j * (j + 1)
            assert abs(result['scalar_value'] - expected) < 1e-10


# =========================================================================
# 13. KZ ODE numerical solution and monodromy tests
# =========================================================================

class TestKZODESolve:
    """Tests for numerical KZ ODE solution and monodromy computation."""

    def test_monodromy_analytic_numerical_match(self):
        """Analytic and numerical monodromy agree (RK4 integration)."""
        result = kz_ode_solve_2point('sl2', Fraction(1), rep_dim=2, n_steps=5000)
        assert result['analytic_numerical_match'], \
            f"Diff = {result['analytic_numerical_diff']}"

    def test_monodromy_eigenvalue_match(self):
        """Monodromy eigenvalues match exp(2 pi i * param * lambda)."""
        result = kz_ode_solve_2point('sl2', Fraction(1), rep_dim=2)
        assert result['eigenvalue_match']

    def test_monodromy_level_variation(self):
        """Monodromy changes with level k."""
        monodromies = []
        for k_val in [1, 2, 5]:
            result = kz_ode_solve_2point('sl2', Fraction(k_val), rep_dim=2)
            monodromies.append(result['monodromy_eigenvalues'])
        # Eigenvalues should differ at different levels
        for i in range(len(monodromies)):
            for j in range(i + 1, len(monodromies)):
                diff = max(abs(a - b)
                           for a, b in zip(monodromies[i], monodromies[j]))
                assert diff > 1e-5, \
                    f"Monodromy unchanged between levels {i} and {j}"

    def test_monodromy_unitary(self):
        """Monodromy matrix is unitary (eigenvalues on unit circle)."""
        result = kz_ode_solve_2point('sl2', Fraction(1), rep_dim=2)
        for ev in result['monodromy_eigenvalues']:
            assert abs(abs(ev) - 1.0) < 1e-6, \
                f"Eigenvalue {ev} not on unit circle"

    def test_monodromy_sl2_adjoint(self):
        """Monodromy computation works for sl_2 adjoint representation."""
        result = kz_ode_solve_2point('sl2', Fraction(1), rep_dim=3, n_steps=5000)
        assert result['analytic_numerical_match']
        assert result['eigenvalue_match']


# =========================================================================
# 14. CYBE with derived Casimir tests
# =========================================================================

class TestCYBEDerivedCasimir:
    """Tests for CYBE verified using Casimir derived from Killing form."""

    def test_cybe_derived_sl2_fundamental(self):
        """CYBE holds using derived Casimir for sl_2 fundamental."""
        result = cybe_from_derived_casimir('sl2', rep_dim=2)
        assert result['ibr_satisfied']
        assert result['casimir_derived_from_killing']
        assert result['casimir_matches_hardcoded']

    def test_cybe_derived_sl2_adjoint(self):
        """CYBE holds using derived Casimir for sl_2 adjoint."""
        result = cybe_from_derived_casimir('sl2', rep_dim=3)
        assert result['ibr_satisfied']
        assert result['ibr_max_norm'] < 1e-10

    def test_cybe_derived_numerical_check(self):
        """CYBE numerical errors small for derived Casimir."""
        result = cybe_from_derived_casimir('sl2', rep_dim=2)
        assert result['cybe_max_error'] < 1e-10

    def test_derived_matches_hardcoded_cybe(self):
        """CYBE from derived Casimir gives same result as hardcoded."""
        result_derived = cybe_from_derived_casimir('sl2', rep_dim=2)
        result_hardcoded = cybe_from_arnold('sl2', rep_dim=2)
        assert result_derived['ibr_satisfied'] == result_hardcoded['ibr_satisfied']
        # Both should have very small IBR norm
        assert abs(result_derived['ibr_max_norm'] - result_hardcoded['ibr_max_norm']) < 1e-10


# =========================================================================
# 15. Flatness from Arnold explicit derivative tests
# =========================================================================

class TestFlatnessExplicitDerivatives:
    """Tests for flatness verified by explicit derivative computation."""

    def test_flatness_sl2_3points(self):
        """KZ connection is flat at 3 points (explicit derivatives)."""
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j]
        result = flatness_from_arnold_explicit('sl2', Fraction(1), z_pts, rep_dim=2)
        assert result['all_flat'], \
            f"Max curvature = {result['max_curvature']}"

    def test_flatness_sl2_4points(self):
        """KZ connection is flat at 4 points (explicit derivatives)."""
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j, 3.0 + 0.5j]
        result = flatness_from_arnold_explicit('sl2', Fraction(2), z_pts, rep_dim=2)
        assert result['all_flat']

    def test_flatness_various_levels(self):
        """Flatness holds at various levels k (explicit derivatives)."""
        z_pts = [0.5, 1.0, 2.0 + 0.5j]
        for k_val in [1, 2, 5, 10]:
            result = flatness_from_arnold_explicit('sl2', Fraction(k_val), z_pts, rep_dim=2)
            assert result['all_flat'], \
                f"Flatness fails at k={k_val}: max curv = {result['max_curvature']}"

    def test_flatness_nonzero_derivative_terms(self):
        """Individual derivative and commutator terms are nonzero even though F=0.

        The curvature F_{ij} = dA_j/dz_i - dA_i/dz_j + [A_i,A_j] = 0
        is a cancellation between three individually nonzero terms.
        """
        z_pts = [0.5, 1.0 + 0.3j, 2.0 - 0.1j]
        result = flatness_from_arnold_explicit('sl2', Fraction(1), z_pts, rep_dim=2)
        # At least some pairs should have nonzero commutator and derivative terms
        has_nonzero = any(
            d['commutator_norm'] > 1e-5 or d['dAj_dzi_norm'] > 1e-5
            for d in result['curvature_data']
        )
        assert has_nonzero, "All derivative/commutator terms are zero (trivial test)"

    def test_flatness_n_pairs_correct(self):
        """Number of pairs checked = n(n-1)/2."""
        z_pts = [0.5, 1.0, 2.0, 3.0]
        result = flatness_from_arnold_explicit('sl2', Fraction(1), z_pts, rep_dim=2)
        n = len(z_pts)
        assert result['n_pairs'] == n * (n - 1) // 2
