"""Tests for theorem_chiral_deformation_frontier_engine.py.

THEOREM: Chiral deformation complex arity-graded structure and rigidity.

Multi-path verification mandate (CLAUDE.md): every claim verified by >= 2
independent paths where possible.

Test organization:
    1. Deformation complex dimensions (H^1 universality, H^2 vanishing)
    2. Rigidity classification (G/L/C/M)
    3. Tangent complex at each arity
    4. Seven faces coordinate systems
    5. Cross-family consistency (additivity, complementarity, kappa)
    6. Full theorem verification
    7. AP compliance checks
"""

import pytest
from fractions import Fraction

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_chiral_deformation_frontier_engine import (
    # Data structures
    DeformationData,
    RigidityResult,
    TangentArityData,
    CoordinateSystemData,
    # Kappa formulas
    kappa_heisenberg,
    kappa_affine_km,
    kappa_virasoro,
    kappa_w_N,
    central_charge_w_N,
    central_charge_affine_km,
    # Quartic contact
    Q_contact_virasoro,
    S4_betagamma,
    # Koszul dual kappa
    kappa_koszul_dual_heisenberg,
    kappa_koszul_dual_affine_km,
    kappa_koszul_dual_virasoro,
    # Deformation data constructors
    deformation_data_heisenberg,
    deformation_data_affine_slN,
    deformation_data_virasoro,
    deformation_data_w_N,
    deformation_data_betagamma,
    deformation_data_lattice,
    # Registry
    build_deformation_registry,
    # Rigidity
    rigidity_data,
    classify_by_shadow_depth,
    # Tangent complex
    tangent_arity_data,
    # Seven faces
    coordinate_data,
    # Cross-family
    verify_H1_universality,
    verify_H2_vanishing,
    verify_H1_additivity,
    verify_complementarity_constraints,
    verify_kappa_consistency,
    verify_bar_residue_order,
    verify_depth_class_consistency,
    # Full theorem
    verify_full_deformation_theorem,
)


# ============================================================================
# 1. Deformation complex dimensions
# ============================================================================

class TestDeformationDimensions:
    """Verify H^1 = 1 (universality) and H^2 = 0 (unobstructed) for all families."""

    def test_heisenberg_H1(self):
        """Heisenberg: H^1 = 1 (the k-direction)."""
        d = deformation_data_heisenberg(Fraction(1))
        assert d.dim_H1 == 1

    def test_heisenberg_H2(self):
        """Heisenberg: H^2 = 0 (abelian, no obstruction)."""
        d = deformation_data_heisenberg(Fraction(1))
        assert d.dim_H2 == 0

    def test_affine_sl2_H1(self):
        """Affine sl_2: H^1 = 1 (the k-direction)."""
        d = deformation_data_affine_slN(2, Fraction(1))
        assert d.dim_H1 == 1

    def test_affine_sl2_H2(self):
        """Affine sl_2: H^2 = 0 (Whitehead lemma: H^2(sl_2, sl_2) = 0)."""
        d = deformation_data_affine_slN(2, Fraction(1))
        assert d.dim_H2 == 0

    def test_affine_sl3_H1(self):
        """Affine sl_3: H^1 = 1."""
        d = deformation_data_affine_slN(3, Fraction(1))
        assert d.dim_H1 == 1

    def test_virasoro_H1(self):
        """Virasoro: H^1 = 1 (the c-direction, Feigin-Fuks)."""
        d = deformation_data_virasoro(Fraction(26))
        assert d.dim_H1 == 1

    def test_virasoro_H2(self):
        """Virasoro: H^2 = 0 (central extension is unique deformation)."""
        d = deformation_data_virasoro(Fraction(26))
        assert d.dim_H2 == 0

    def test_w3_H1(self):
        """W_3: H^1 = 1 (Fateev-Lukyanov uniqueness)."""
        d = deformation_data_w_N(3)
        assert d.dim_H1 == 1

    def test_w3_H2(self):
        """W_3: H^2 = 0 at genus 0 (bootstrap forces c-deformation)."""
        d = deformation_data_w_N(3)
        assert d.dim_H2 == 0

    def test_betagamma_H1(self):
        """Betagamma: H^1 = 1 (the conformal weight direction)."""
        d = deformation_data_betagamma(Fraction(0))
        assert d.dim_H1 == 1

    def test_betagamma_H2(self):
        """Betagamma: H^2 = 0 (abelian on neutral stratum)."""
        d = deformation_data_betagamma(Fraction(0))
        assert d.dim_H2 == 0

    def test_lattice_H1(self):
        """Lattice VOA: H^1 = 1 (lattice scaling direction)."""
        d = deformation_data_lattice(8)
        assert d.dim_H1 == 1

    def test_H1_universality_all(self):
        """Full registry: dim H^1 = 1 for ALL standard families."""
        result = verify_H1_universality()
        assert result['all_pass'], f"H^1 universality failed: {result}"

    def test_H2_vanishing_all(self):
        """Full registry: dim H^2 = 0 for ALL standard families at generic level."""
        result = verify_H2_vanishing()
        assert result['all_pass'], f"H^2 vanishing failed: {result}"


# ============================================================================
# 2. Rigidity classification
# ============================================================================

class TestRigidityClassification:
    """Verify the G/L/C/M rigidity data for each family."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G: kappa alone determines Theta_A."""
        r = rigidity_data('heisenberg')
        assert r.shadow_class == 'G'
        assert r.r_max == 2
        assert r.terminates is True
        assert r.determining_data == ['kappa']

    def test_affine_class_L(self):
        """Affine KM is class L: kappa + S_3 determine Theta_A."""
        r = rigidity_data('affine_km')
        assert r.shadow_class == 'L'
        assert r.r_max == 3
        assert r.terminates is True
        assert r.determining_data == ['kappa', 'S_3']

    def test_betagamma_class_C(self):
        """Betagamma is class C: kappa + S_3 + Q^contact determine Theta_A."""
        r = rigidity_data('betagamma')
        assert r.shadow_class == 'C'
        assert r.r_max == 4
        assert r.terminates is True
        assert r.determining_data == ['kappa', 'S_3', 'Q_contact']

    def test_virasoro_class_M(self):
        """Virasoro is class M: full infinite tower needed."""
        r = rigidity_data('virasoro')
        assert r.shadow_class == 'M'
        assert r.r_max == float('inf')
        assert r.terminates is False
        assert len(r.determining_data) > 3  # all arities needed

    def test_w_algebra_class_M(self):
        """W-algebras are class M."""
        r = rigidity_data('w_n')
        assert r.shadow_class == 'M'
        assert r.r_max == float('inf')
        assert r.terminates is False

    def test_lattice_class_G(self):
        """Lattice VOA is class G."""
        r = rigidity_data('lattice')
        assert r.shadow_class == 'G'
        assert r.r_max == 2
        assert r.terminates is True

    def test_free_fermion_class_G(self):
        """Free fermion is class G."""
        r = rigidity_data('free_fermion')
        assert r.shadow_class == 'G'

    def test_depth_ordering(self):
        """Shadow depth obeys G < L < C < M ordering."""
        depths = {
            'G': rigidity_data('heisenberg').r_max,
            'L': rigidity_data('affine_km').r_max,
            'C': rigidity_data('betagamma').r_max,
            'M': rigidity_data('virasoro').r_max,
        }
        assert depths['G'] < depths['L'] < depths['C'] < depths['M']

    def test_classification_covers_all_classes(self):
        """All four classes G/L/C/M are represented in the registry."""
        classification = classify_by_shadow_depth()
        for cls in ['G', 'L', 'C', 'M']:
            assert len(classification[cls]) >= 1, f"Class {cls} empty"


# ============================================================================
# 3. Tangent complex at each arity
# ============================================================================

class TestTangentArity:
    """Verify tangent complex structure at arities 2, 3, 4."""

    def test_heisenberg_arity2_nonzero(self):
        """Heisenberg arity 2: kappa/z is nonzero."""
        t = tangent_arity_data('heisenberg', 2, k=Fraction(3))
        assert not t.is_zero
        assert t.scalar_value == Fraction(3)  # kappa(H_3) = 3

    def test_heisenberg_arity3_zero(self):
        """Heisenberg arity 3: cubic shadow vanishes (abelian)."""
        t = tangent_arity_data('heisenberg', 3)
        assert t.is_zero
        assert t.scalar_value == Fraction(0)

    def test_heisenberg_arity4_zero(self):
        """Heisenberg arity 4: quartic shadow vanishes (class G)."""
        t = tangent_arity_data('heisenberg', 4)
        assert t.is_zero
        assert t.scalar_value == Fraction(0)

    def test_affine_arity2_nonzero(self):
        """Affine sl_2 arity 2: Casimir r-matrix is nonzero."""
        t = tangent_arity_data('affine_km', 2, N=2, k=Fraction(1))
        assert not t.is_zero
        # kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4
        assert t.scalar_value == Fraction(9, 4)

    def test_affine_arity3_nonzero(self):
        """Affine sl_N arity 3: cubic shadow from Lie bracket is nonzero."""
        t = tangent_arity_data('affine_km', 3)
        assert not t.is_zero

    def test_affine_arity4_zero(self):
        """Affine KM arity 4: Jacobi kills quartic (class L)."""
        t = tangent_arity_data('affine_km', 4)
        assert t.is_zero
        assert t.scalar_value == Fraction(0)

    def test_betagamma_arity3_zero(self):
        """Betagamma arity 3: zero on neutral stratum."""
        t = tangent_arity_data('betagamma', 3)
        assert t.is_zero

    def test_betagamma_arity4_nonzero(self):
        """Betagamma arity 4: quartic contact on charged stratum."""
        t = tangent_arity_data('betagamma', 4)
        assert not t.is_zero
        assert t.scalar_value == Fraction(-5, 12)

    def test_virasoro_arity2_nonzero(self):
        """Virasoro arity 2: r-matrix is nonzero."""
        t = tangent_arity_data('virasoro', 2, c=Fraction(26))
        assert not t.is_zero
        assert t.scalar_value == Fraction(13)  # kappa(Vir_26) = 13

    def test_virasoro_arity3_nonzero(self):
        """Virasoro arity 3: cubic shadow from singular vectors."""
        t = tangent_arity_data('virasoro', 3)
        assert not t.is_zero

    def test_virasoro_arity4_nonzero(self):
        """Virasoro arity 4: quartic contact Q^contact != 0."""
        t = tangent_arity_data('virasoro', 4, c=Fraction(26))
        assert not t.is_zero
        expected_q = Fraction(10) / (Fraction(26) * (5 * Fraction(26) + 22))
        assert t.scalar_value == expected_q


# ============================================================================
# 4. Seven faces coordinate systems
# ============================================================================

class TestSevenFaces:
    """Verify the seven coordinate system descriptions."""

    def test_sl2_seven_faces_count(self):
        """sl_2 has exactly seven coordinate systems."""
        coords = coordinate_data('affine_km', N=2)
        assert len(coords) == 7

    def test_virasoro_seven_faces_count(self):
        """Virasoro has exactly seven coordinate systems."""
        coords = coordinate_data('virasoro')
        assert len(coords) == 7

    def test_heisenberg_seven_faces_count(self):
        """Heisenberg has exactly seven coordinate systems."""
        coords = coordinate_data('heisenberg')
        assert len(coords) == 7

    def test_sl2_pole_order(self):
        """sl_2 r-matrix has pole order 1 (AP19: OPE pole 2 -> residue 1)."""
        coords = coordinate_data('affine_km', N=2)
        for c in coords:
            assert c.pole_order == 1

    def test_virasoro_pole_order(self):
        """Virasoro r-matrix has pole order 3 (AP19: OPE pole 4 -> residue 3)."""
        coords = coordinate_data('virasoro')
        for c in coords:
            assert c.pole_order == 3

    def test_heisenberg_pole_order(self):
        """Heisenberg r-matrix has pole order 1."""
        coords = coordinate_data('heisenberg')
        for c in coords:
            assert c.pole_order == 1

    def test_coordinate_types_complete(self):
        """All seven coordinate types are represented for sl_2."""
        coords = coordinate_data('affine_km', N=2)
        types = {c.coordinate_type for c in coords}
        expected = {'twisting', 'yangian', 'sklyanin', 'drinfeld', 'current',
                    'collision', 'bar'}
        assert types == expected


# ============================================================================
# 5. Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Verify cross-family structural constraints."""

    def test_H1_additivity(self):
        """H^1 is additive under direct sums."""
        result = verify_H1_additivity()
        assert result['all_pass'], f"H^1 additivity failed: {result}"

    def test_complementarity_km(self):
        """Affine KM: kappa + kappa_dual = 0 (AP24)."""
        d = deformation_data_affine_slN(2, Fraction(1))
        assert d.complementarity_sum == Fraction(0)

    def test_complementarity_heisenberg(self):
        """Heisenberg: kappa + kappa_dual = 0."""
        d = deformation_data_heisenberg(Fraction(3))
        assert d.complementarity_sum == Fraction(0)

    def test_complementarity_virasoro(self):
        """Virasoro: kappa + kappa_dual = 13 (AP24: NOT zero)."""
        d = deformation_data_virasoro(Fraction(1))
        assert d.complementarity_sum == Fraction(13)

    def test_complementarity_virasoro_c26(self):
        """Virasoro at c=26: kappa(26) + kappa(0) = 13 + 0 = 13."""
        d = deformation_data_virasoro(Fraction(26))
        assert d.kappa == Fraction(13)
        assert d.kappa_dual == Fraction(0)
        assert d.complementarity_sum == Fraction(13)

    def test_complementarity_virasoro_c13(self):
        """Virasoro at c=13: self-dual. kappa = kappa_dual = 13/2."""
        d = deformation_data_virasoro(Fraction(13))
        assert d.kappa == Fraction(13, 2)
        assert d.kappa_dual == Fraction(13, 2)
        assert d.complementarity_sum == Fraction(13)

    def test_complementarity_betagamma(self):
        """Betagamma: kappa + kappa_dual = 0 (free field)."""
        d = deformation_data_betagamma(Fraction(0))
        assert d.complementarity_sum == Fraction(0)

    def test_complementarity_full(self):
        """Full complementarity check across all families."""
        result = verify_complementarity_constraints()
        assert result['all_pass'], f"Complementarity failed: {result}"

    def test_kappa_consistency(self):
        """Kappa values computed by two independent paths must agree."""
        result = verify_kappa_consistency()
        assert result['all_pass'], f"Kappa consistency failed: {result}"


# ============================================================================
# 6. Kappa formula cross-checks (AP1, AP39)
# ============================================================================

class TestKappaFormulas:
    """Independent verification of kappa formulas per family.

    AP1: Never copy kappa between families. Compute from first principles.
    AP39: kappa != c/2 for non-Virasoro families in general.
    """

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1."""
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)

    def test_kappa_heisenberg_k5(self):
        """kappa(H_5) = 5."""
        assert kappa_heisenberg(Fraction(5)) == Fraction(5)

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        # dim(sl_2) = 3, h^vee = 2
        assert kappa_affine_km(3, Fraction(1), 2) == Fraction(9, 4)

    def test_kappa_sl2_k1_not_c_over_2(self):
        """AP39: kappa(sl_2, k=1) = 9/4 != c/2 = 1/2.

        c(sl_2, k=1) = 1*3/(1+2) = 1. So c/2 = 1/2 != 9/4.
        """
        kap = kappa_affine_km(3, Fraction(1), 2)
        c = central_charge_affine_km(3, Fraction(1), 2)
        assert kap != c / 2

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        # dim(sl_3) = 8, h^vee = 3
        assert kappa_affine_km(8, Fraction(1), 3) == Fraction(16, 3)

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)

    def test_kappa_w3(self):
        """kappa(W_3) = c * (H_3 - 1) = c * (1/2 + 1/3) = 5c/6."""
        c = Fraction(100)  # arbitrary
        H3_minus_1 = Fraction(1, 2) + Fraction(1, 3)
        assert H3_minus_1 == Fraction(5, 6)
        assert kappa_w_N(3, c) == c * Fraction(5, 6)

    def test_kappa_koszul_dual_heisenberg(self):
        """kappa(H_k^!) = -k. AP33: H_k^! != H_{-k} as algebras."""
        assert kappa_koszul_dual_heisenberg(Fraction(3)) == Fraction(-3)

    def test_kappa_koszul_dual_sl2_anti_symmetric(self):
        """kappa(sl_2, k) + kappa(sl_2, k^!) = 0. FF involution: k -> -k - 4."""
        k = Fraction(1)
        kap = kappa_affine_km(3, k, 2)
        kap_dual = kappa_koszul_dual_affine_km(3, k, 2)
        assert kap + kap_dual == Fraction(0)

    def test_kappa_koszul_dual_virasoro_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c (AP24)."""
        for c_val in [1, 2, 5, 13, 25, 26]:
            c = Fraction(c_val)
            assert kappa_virasoro(c) + kappa_koszul_dual_virasoro(c) == Fraction(13)


# ============================================================================
# 7. AP compliance and structural checks
# ============================================================================

class TestAPCompliance:
    """Verify anti-pattern compliance across all deformation data."""

    def test_ap19_bar_residue_all(self):
        """AP19: bar_residue_order = ope_pole_order - 1 for ALL families."""
        result = verify_bar_residue_order()
        assert result['all_pass'], f"AP19 violated: {result}"

    def test_ap14_all_koszul(self):
        """AP14: ALL standard families are chirally Koszul."""
        reg = build_deformation_registry()
        for name, d in reg.items():
            assert d.is_koszul, f"{name} should be Koszul (AP14)"

    def test_depth_class_consistency(self):
        """Shadow class matches r_max for all families."""
        result = verify_depth_class_consistency()
        assert result['all_pass'], f"Depth/class mismatch: {result}"

    def test_q_contact_virasoro_c1(self):
        """Q^contact_Vir(c=1) = 10/(1*27) = 10/27."""
        assert Q_contact_virasoro(Fraction(1)) == Fraction(10, 27)

    def test_q_contact_virasoro_c26(self):
        """Q^contact_Vir(c=26) = 10/(26*152) = 10/3952 = 5/1976."""
        expected = Fraction(10) / (Fraction(26) * Fraction(152))
        assert Q_contact_virasoro(Fraction(26)) == expected

    def test_s4_betagamma(self):
        """S_4(betagamma) = -5/12."""
        assert S4_betagamma() == Fraction(-5, 12)

    def test_registry_size(self):
        """Registry has substantial coverage."""
        reg = build_deformation_registry()
        assert len(reg) >= 25, f"Registry too small: {len(reg)}"

    def test_all_four_classes_present(self):
        """All four shadow classes G/L/C/M are represented."""
        reg = build_deformation_registry()
        classes = {d.shadow_class for d in reg.values()}
        assert classes == {'G', 'L', 'C', 'M'}


# ============================================================================
# 8. Full theorem verification
# ============================================================================

class TestFullTheorem:
    """End-to-end verification of the deformation complex theorem."""

    def test_full_theorem(self):
        """All checks pass in the full theorem verification."""
        result = verify_full_deformation_theorem()
        assert result['all_pass'], f"Full theorem failed: {result}"

    def test_full_theorem_registry_size(self):
        """Full theorem covers enough algebras."""
        result = verify_full_deformation_theorem()
        assert result['registry_size'] >= 25
