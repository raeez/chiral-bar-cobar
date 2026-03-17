"""Tests for holographic shadow connection constructions.

Verifies:
  1. Heisenberg shadow connection flatness (cor:shadow-connection-heisenberg)
  2. Heisenberg flat sections: f = prod (z_i-z_j)^{kappa q_i q_j}
  3. KZ connection for sl_2 (thm:shadow-connection-kz): parameter = 1/(k+2)
  4. Arnold relation (thm:arnold-relations): eta_12^eta_23+eta_23^eta_31+eta_31^eta_12=0
  5. Shadow depth classification: G(2), L(3), C(4), M(inf)
  6. Genus-1 free energy: F_1 = kappa/12 (Bernoulli B_2=1/6)
  7. Collision residue = r-matrix (thm:collision-residue-twisting)
  8. Five shadow extraction for Heisenberg
  9. IBR from Arnold (thm:collision-depth-2-ybe): [O_ij, O_ik+O_jk]=0

Mathematical references in frontier_modular_holography_platonic.tex
and configuration_spaces.tex.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from holographic_shadow_connection import (
    HeisenbergShadowConnection,
    verify_arnold_relation_symbolic,
    arnold_relation_numerical,
    kz_parameter_sl2,
    kappa_sl2,
    sl2_casimir_tensor,
    kz_flatness_sl2_n3,
    kz_flatness_sl2_n4,
    shadow_depth_data,
    quartic_contact_virasoro,
    genus1_free_energy,
    bernoulli_lambda1,
    collision_residue_heisenberg,
    collision_residue_sl2,
    heisenberg_five_shadows,
    verify_cybe_casimir_sl2,
    master_holographic_shadow_verification,
    SHADOW_DEPTH_CLASSIFICATION,
)


# ========================================================================
# 1. Heisenberg shadow connection flatness (cor:shadow-connection-heisenberg)
# ========================================================================

class TestHeisenbergFlatness:
    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""

    def test_flatness_n3_unit_charges(self):
        """Flatness for n=3 with charges (1,1,1)."""
        conn = HeisenbergShadowConnection(Fraction(1), 3,
                                           [Fraction(1)] * 3)
        result = conn.verify_flatness()
        assert result['is_flat']
        assert result['n_pairs_checked'] == 3

    def test_flatness_n4_unit_charges(self):
        """Flatness for n=4 with charges (1,1,1,1)."""
        conn = HeisenbergShadowConnection(Fraction(1), 4,
                                           [Fraction(1)] * 4)
        result = conn.verify_flatness()
        assert result['is_flat']

    def test_flatness_n3_mixed_charges(self):
        """Flatness for n=3 with charges (1, -1, 2)."""
        conn = HeisenbergShadowConnection(Fraction(1), 3,
                                           [Fraction(1), Fraction(-1), Fraction(2)])
        result = conn.verify_flatness()
        assert result['is_flat']

    def test_flatness_n4_mixed_charges(self):
        """Flatness for n=4 with charges (1, -1, 2, -2)."""
        conn = HeisenbergShadowConnection(Fraction(2), 4,
                                           [Fraction(1), Fraction(-1),
                                            Fraction(2), Fraction(-2)])
        result = conn.verify_flatness()
        assert result['is_flat']

    @pytest.mark.parametrize("kappa", [Fraction(1, 2), Fraction(1), Fraction(3), Fraction(7, 3)])
    def test_flatness_various_kappa(self, kappa):
        """Flatness holds at all levels kappa."""
        conn = HeisenbergShadowConnection(kappa, 3,
                                           [Fraction(1), Fraction(-1), Fraction(0)])
        result = conn.verify_flatness()
        assert result['is_flat']


# ========================================================================
# 2. Heisenberg flat sections
# ========================================================================

class TestHeisenbergFlatSections:
    """f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j} satisfies nabla f = 0."""

    def test_flat_section_n3(self):
        """Verify nabla(f) = 0 for n=3 at generic points."""
        conn = HeisenbergShadowConnection(Fraction(1), 3,
                                           [Fraction(1), Fraction(-1), Fraction(0)])
        z = [1.0 + 0.1j, 2.0 - 0.3j, 4.0 + 0.5j]
        result = conn.flat_section_check(z)
        assert result['valid']
        assert result['nabla_f_is_zero']
        assert result['max_residual'] < 1e-14

    def test_flat_section_n4(self):
        """Verify nabla(f) = 0 for n=4."""
        conn = HeisenbergShadowConnection(Fraction(2), 4,
                                           [Fraction(1), Fraction(-1),
                                            Fraction(2), Fraction(-2)])
        z = [0.5 + 0.1j, 1.5 - 0.2j, 3.0 + 0.4j, 5.0 - 0.1j]
        result = conn.flat_section_check(z)
        assert result['valid']
        assert result['nabla_f_is_zero']

    def test_flat_section_coincident_points_rejected(self):
        """Coincident points should be flagged."""
        conn = HeisenbergShadowConnection(Fraction(1), 3,
                                           [Fraction(1)] * 3)
        z = [1.0, 1.0, 2.0]
        result = conn.flat_section_check(z)
        assert not result['valid']


# ========================================================================
# 3. KZ connection for sl_2 (thm:shadow-connection-kz)
# ========================================================================

class TestKZConnection:
    """KZ parameter is 1/(k+2); kappa(sl_2_k) = 3(k+2)/4."""

    def test_kz_parameter_k1(self):
        """k = 1: KZ parameter = 1/3."""
        assert kz_parameter_sl2(Fraction(1)) == Fraction(1, 3)

    def test_kz_parameter_k2(self):
        """k = 2: KZ parameter = 1/4."""
        assert kz_parameter_sl2(Fraction(2)) == Fraction(1, 4)

    def test_kz_parameter_critical_level_raises(self):
        """k = -2 (critical level): KZ parameter undefined."""
        with pytest.raises(ValueError, match="Critical level"):
            kz_parameter_sl2(Fraction(-2))

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3 * 3 / 4 = 9/4."""
        assert kappa_sl2(Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl2_k2(self):
        """kappa(sl_2, k=2) = 3 * 4 / 4 = 3."""
        assert kappa_sl2(Fraction(2)) == Fraction(3)

    def test_kz_flatness_n3_k1(self):
        """KZ flatness for sl_2 k=1, n=3 (CYBE in spin-1/2 rep)."""
        result = kz_flatness_sl2_n3(Fraction(1))
        assert result['cybe_satisfied']
        assert result['cybe_max_entry'] < 1e-12

    def test_kz_flatness_n3_k10(self):
        """KZ flatness for sl_2 k=10, n=3."""
        result = kz_flatness_sl2_n3(Fraction(10))
        assert result['cybe_satisfied']

    def test_kz_flatness_n4_k1(self):
        """KZ flatness for sl_2 k=1, n=4 (all 4 triples checked)."""
        result = kz_flatness_sl2_n4(Fraction(1))
        assert result['cybe_satisfied']
        assert result['n_triples_checked'] == 4

    def test_kz_flatness_n4_k3(self):
        """KZ flatness for sl_2 k=3, n=4."""
        result = kz_flatness_sl2_n4(Fraction(3))
        assert result['cybe_satisfied']

    def test_casimir_tensor_structure(self):
        """Casimir tensor Omega = E*F + F*E + H*H/2."""
        Omega = sl2_casimir_tensor()
        assert Omega[0, 1] == 1  # E tensor F
        assert Omega[1, 0] == 1  # F tensor E
        assert Omega[2, 2] == Fraction(1, 2)  # H tensor H / 2


# ========================================================================
# 4. Arnold relation (thm:arnold-relations)
# ========================================================================

class TestArnoldRelation:
    """eta_12^eta_23 + eta_23^eta_31 + eta_31^eta_12 = 0."""

    def test_symbolic_verification(self):
        """Sympy verifies the partial fractions identity."""
        result = verify_arnold_relation_symbolic()
        assert result['symbolic_zero']

    def test_numerical_100_random(self):
        """Arnold relation holds for 100 random triples."""
        result = arnold_relation_numerical(100)
        assert result['passes']
        assert result['max_error'] < 1e-10

    def test_numerical_real_points(self):
        """Arnold relation at specific real points."""
        z1, z2, z3 = 1.0, 3.0, 7.0
        val = (1 / ((z1 - z2) * (z2 - z3))
               + 1 / ((z2 - z3) * (z3 - z1))
               + 1 / ((z3 - z1) * (z1 - z2)))
        assert abs(val) < 1e-15


# ========================================================================
# 5. Shadow depth classification
# ========================================================================

class TestShadowDepthClassification:
    """Shadow depth: Heisenberg(G,2), affine(L,3), betaGamma(C,4), Vir(M,inf)."""

    def test_heisenberg_class_G(self):
        data = shadow_depth_data('Heisenberg')
        assert data['class'] == 'G'
        assert data['r_max'] == 2

    def test_affine_class_L(self):
        data = shadow_depth_data('affine')
        assert data['class'] == 'L'
        assert data['r_max'] == 3

    def test_betagamma_class_C(self):
        data = shadow_depth_data('beta_gamma')
        assert data['class'] == 'C'
        assert data['r_max'] == 4

    def test_virasoro_class_M(self):
        data = shadow_depth_data('Virasoro')
        assert data['class'] == 'M'
        assert data['r_max'] == float('inf')

    def test_all_four_classes_present(self):
        classes = {v['class'] for v in SHADOW_DEPTH_CLASSIFICATION.values()}
        assert classes == {'G', 'L', 'C', 'M'}

    def test_quartic_contact_virasoro(self):
        """Q^contact_Vir = 10 / (c(5c+22))."""
        # c = 1: 10 / (1 * 27) = 10/27
        assert quartic_contact_virasoro(Fraction(1)) == Fraction(10, 27)
        # c = 25: 10 / (25 * 147) = 10/3675 = 2/735
        assert quartic_contact_virasoro(Fraction(25)) == Fraction(10, 3675)

    def test_quartic_contact_virasoro_c_half(self):
        """Q^contact_Vir at c = 1/2 (Ising)."""
        # 10 / ((1/2)(5/2 + 22)) = 10 / ((1/2)(49/2)) = 10 / (49/4) = 40/49
        assert quartic_contact_virasoro(Fraction(1, 2)) == Fraction(40, 49)


# ========================================================================
# 6. Genus-1 free energy
# ========================================================================

class TestGenus1:
    """F_1 = kappa/12 from B_2 = 1/6, lambda_1 = 1/12."""

    def test_bernoulli_lambda1(self):
        """lambda_1^FP = |B_2|/(2*0!) = (1/6)/2 = 1/12."""
        assert bernoulli_lambda1() == Fraction(1, 12)

    def test_genus1_heisenberg(self):
        """Heisenberg kappa = 1: F_1 = 1/12."""
        assert genus1_free_energy(Fraction(1)) == Fraction(1, 12)

    def test_genus1_sl2_k1(self):
        """sl_2 k=1: kappa = 9/4, F_1 = 9/48 = 3/16."""
        kappa = kappa_sl2(Fraction(1))
        assert kappa == Fraction(9, 4)
        assert genus1_free_energy(kappa) == Fraction(9, 48)
        assert genus1_free_energy(kappa) == Fraction(3, 16)


# ========================================================================
# 7. Collision residue = r-matrix (thm:collision-residue-twisting)
# ========================================================================

class TestCollisionResidue:
    """Collision residue recovers the r-matrix."""

    def test_heisenberg_r_matrix(self):
        """Heisenberg: r(z) = 1/(kappa*z), abelian."""
        result = collision_residue_heisenberg(Fraction(1))
        assert result['abelian']
        assert result['cybe_trivially_satisfied']
        assert result['order_of_pole'] == 1

    def test_sl2_r_matrix(self):
        """sl_2 k=1: r(z) = Omega/(3z), not abelian."""
        result = collision_residue_sl2(Fraction(1))
        assert not result['abelian']
        assert result['cybe_from_arnold']
        assert result['kz_parameter'] == Fraction(1, 3)

    def test_sl2_kappa_from_residue(self):
        """sl_2 k=2: kappa = 3, KZ param = 1/4."""
        result = collision_residue_sl2(Fraction(2))
        assert result['kappa'] == Fraction(3)
        assert result['kz_parameter'] == Fraction(1, 4)


# ========================================================================
# 8. Five shadow extraction for Heisenberg
# ========================================================================

class TestFiveShadows:
    """All 5 shadows consistent for Heisenberg (class G)."""

    def test_five_shadows_kappa1(self):
        result = heisenberg_five_shadows(Fraction(1))
        shadows = result['shadows']
        checks = result['checks']

        assert shadows['kappa'] == Fraction(1)
        assert shadows['Delta'] == Fraction(1, 12)
        assert shadows['cubic_C'] == 0
        assert shadows['quartic_Q'] == 0
        assert shadows['quintic_o5'] == 0

        assert checks['tower_terminates']
        assert checks['termination_arity'] == 2
        assert checks['class'] == 'G'
        assert checks['all_higher_vanish']
        assert checks['genus1_consistent']

    def test_five_shadows_kappa3(self):
        result = heisenberg_five_shadows(Fraction(3))
        assert result['shadows']['kappa'] == Fraction(3)
        assert result['shadows']['Delta'] == Fraction(1, 4)
        assert result['checks']['genus1_consistent']

    @pytest.mark.parametrize("kappa", [Fraction(1, 2), Fraction(1),
                                        Fraction(5), Fraction(10)])
    def test_five_shadows_various_kappa(self, kappa):
        result = heisenberg_five_shadows(kappa)
        assert result['checks']['all_higher_vanish']
        assert result['checks']['tower_terminates']


# ========================================================================
# 9. CYBE from Arnold (thm:collision-depth-2-ybe)
# ========================================================================

class TestCYBE:
    """IBR [O_ij, O_ik+O_jk]=0 for sl_2 Casimir (thm:collision-depth-2-ybe).

    The Arnold relation implies the infinitesimal braid relation (IBR)
    via partial fractions. The IBR is the flatness condition for KZ and
    the spectral-parameter CYBE for r(z) = Omega/z.
    """

    def test_ibr_fundamental_rep(self):
        """IBR in 2-dim (spin-1/2) representation."""
        result = verify_cybe_casimir_sl2()
        assert result['fundamental']['satisfied']
        assert result['fundamental']['cybe_norm'] < 1e-12

    def test_ibr_adjoint_rep(self):
        """IBR in 3-dim (adjoint) representation."""
        result = verify_cybe_casimir_sl2()
        assert result['adjoint']['satisfied']
        assert result['adjoint']['cybe_norm'] < 1e-12

    def test_ibr_dimensions(self):
        """Check representation dimensions: 2^3=8, 3^3=27."""
        result = verify_cybe_casimir_sl2()
        assert result['fundamental']['dim'] == 8
        assert result['adjoint']['dim'] == 27


# ========================================================================
# Master verification
# ========================================================================

class TestMaster:
    """Run all holographic shadow connection verifications."""

    def test_master_all_pass(self):
        results = master_holographic_shadow_verification()
        for r in results:
            assert r['passed'], f"FAILED: {r['test']}"

    def test_master_count(self):
        results = master_holographic_shadow_verification()
        assert len(results) >= 14
