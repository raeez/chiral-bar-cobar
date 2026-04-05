r"""Tests for the relative chiral algebra A_{K3 x E / E}.

Verifies the full chain:
  K3 sigma model -> relative chiral algebra -> shadow tower -> BKM -> Delta_5.

Multi-path verification mandate: every numerical result verified by 3+ paths.
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.k3_relative_chiral import (
    # Arithmetic helpers
    sigma_k,
    partition_count,
    bernoulli_number,
    faber_pandharipande,
    # K3 sigma model
    K3_CENTRAL_CHARGE,
    K3_EULER_CHAR,
    K3_COMPLEX_DIM,
    kappa_k3_sigma,
    kappa_k3_dual,
    k3_partition_function_coeffs,
    # phi_{0,1}
    phi01_discriminant_coeffs,
    phi01_coeff,
    verify_phi01_constancy,
    # Genus-g free energy
    F_g_k3,
    F_g_k3_ahat_check,
    # Shadow depth
    k3_shadow_depth_analysis,
    # DMVV
    dmvv_product_coeffs,
    hilb_k3_euler,
    # BKM
    bkm_root_multiplicity,
    verify_real_root_multiplicities,
    shadow_tower_to_product_formula,
    # Relative sewing
    relative_sewing_genus1,
    relative_sewing_higher_genus,
    # Complementarity
    k3_complementarity,
    # Igusa
    igusa_cusp_form_from_shadow,
    # A-hat
    ahat_generating_function,
    # Mathieu moonshine
    mathieu_moonshine_coefficients,
    # Multi-path verification
    kappa_k3_multi_path_verification,
    # Hilbert scheme
    hilb_k3_partition_detailed,
    # Full bridge
    full_bridge_summary,
)


# =========================================================================
# Section 1: K3 constants
# =========================================================================

class TestK3Constants:
    """Verify basic K3 surface data."""

    def test_central_charge(self):
        """K3 sigma model has c=6 (CY 2-fold: c = 3d = 3*2 = 6)."""
        assert K3_CENTRAL_CHARGE == 6

    def test_euler_characteristic(self):
        """chi(K3) = 24 (topological invariant)."""
        assert K3_EULER_CHAR == 24

    def test_complex_dimension(self):
        """K3 is a complex surface: d = 2."""
        assert K3_COMPLEX_DIM == 2

    def test_central_charge_from_dimension(self):
        """c = 3*d for a CY d-fold sigma model (holomorphic sector)."""
        # For CY: c = 3d because each complex dimension contributes
        # c = 3 (one beta-gamma pair contributes c = -1 + 2 = 2... no)
        # Actually c = 6d/d = 6 for K3... the formula is c_total = d_real/2 * 2 = d
        # For K3 (real dim 4): c = 3*2 = 6. Yes.
        # For CY_3 (real dim 6): c = 3*3 = 9.
        assert K3_CENTRAL_CHARGE == 3 * K3_COMPLEX_DIM


# =========================================================================
# Section 2: Modular characteristic kappa
# =========================================================================

class TestKappaK3:
    """Verify kappa(K3 sigma model) = 2 by multiple paths."""

    def test_kappa_value(self):
        """kappa(K3 sigma) = 2 (CY complex dimension)."""
        assert kappa_k3_sigma() == Fraction(2)

    def test_kappa_dual(self):
        """kappa(K3 sigma dual) = -2 (complementarity)."""
        assert kappa_k3_dual() == Fraction(-2)

    def test_kappa_complementarity_sum(self):
        """kappa + kappa' = 0 for K3 sigma model."""
        assert kappa_k3_sigma() + kappa_k3_dual() == 0

    def test_kappa_not_c_over_2(self):
        """kappa != c/2 for K3 sigma model (AP48).

        The Virasoro subalgebra at c=6 has kappa(Vir_6) = 3.
        The full K3 sigma model has kappa = 2 != 3.
        AP48: kappa depends on the FULL algebra, not the Virasoro subalgebra.
        """
        c = K3_CENTRAL_CHARGE
        kappa_virasoro = Fraction(c, 2)  # = 3
        assert kappa_k3_sigma() != kappa_virasoro
        assert kappa_virasoro == Fraction(3)

    def test_multi_path_verification(self):
        """Verify kappa = 2 by 5 independent paths."""
        result = kappa_k3_multi_path_verification()
        assert result['kappa'] == Fraction(2)
        assert result['num_paths'] >= 3  # multi-path mandate
        assert result['all_agree'] is True

    def test_kappa_additivity_with_torus(self):
        """kappa(K3 x T^2) = kappa(K3) + kappa(T^2) = 2 + 1 = 3 = dim(CY_3).

        Additivity of kappa (prop:independent-sum-factorization).
        """
        kappa_k3 = kappa_k3_sigma()
        kappa_t2 = Fraction(1)  # torus has rank 1 Heisenberg per complex dim
        kappa_total = kappa_k3 + kappa_t2
        assert kappa_total == Fraction(3)  # = complex dim of CY_3

    def test_kappa_orbifold_consistency(self):
        """kappa(T^4/Z_2) = kappa(T^4)/2 = 4/2 = 2 = kappa(K3).

        At the orbifold point in K3 moduli space, K3 = T^4/Z_2.
        """
        kappa_t4 = Fraction(4)  # rank 4 Heisenberg (4 complex coords)
        kappa_orbifold = kappa_t4 / 2  # Z_2 orbifold projects to half
        assert kappa_orbifold == kappa_k3_sigma()


# =========================================================================
# Section 3: Phi_{0,1} Fourier coefficients
# =========================================================================

class TestPhi01:
    """Verify phi_{0,1} Fourier coefficients (K3 elliptic genus)."""

    def test_discriminant_minus_1(self):
        """c(-1) = 1 (the y^{+/-1} terms at q^0)."""
        table = phi01_discriminant_coeffs()
        assert table[-1] == 1

    def test_discriminant_0(self):
        """c(0) = 10 (the constant term at q^0)."""
        table = phi01_discriminant_coeffs()
        assert table[0] == 10

    def test_phi01_at_z0(self):
        """phi_{0,1}(tau, 0) = c(0) + 2*c(-1) = 10 + 2 = 12."""
        table = phi01_discriminant_coeffs()
        # At n=0: c(0,0) = c(0) = 10, c(0,+/-1) = c(-1) = 1 each
        total = table[0] + 2 * table[-1]
        assert total == 12

    def test_constancy_at_z0(self):
        """sum_l c(n, l) = 0 for n >= 1 (phi is constant at z=0)."""
        result = verify_phi01_constancy(nmax=5)
        for n in range(5):
            assert result[n]['correct'], f"phi constancy fails at n={n}"

    def test_constancy_at_n0(self):
        """At n=0: sum_l c(0, l) = 12."""
        result = verify_phi01_constancy(nmax=1)
        assert result[0]['sum_l_c(n,l)'] == 12

    def test_constancy_at_n1(self):
        """At n=1: c(4) + 2*c(3) + 2*c(0) = 108 + 2*(-64) + 2*10 = 0."""
        table = phi01_discriminant_coeffs()
        total = table[4] + 2 * table[3] + 2 * table[0]
        assert total == 0

    def test_constancy_at_n2(self):
        """At n=2: c(8) + 2*c(7) + 2*c(4) + 2*c(-1) = 808 - 1026 + 216 + 2 = 0."""
        table = phi01_discriminant_coeffs()
        total = table[8] + 2 * table[7] + 2 * table[4] + 2 * table[-1]
        assert total == 0

    def test_constancy_at_n3(self):
        """At n=3: c(12) + 2*c(11) + 2*c(8) + 2*c(3) + 2*c(0) = 0.

        4016 + 2*(-2752) + 2*808 + 2*(-64) + 2*10
        = 4016 - 5504 + 1616 - 128 + 20 = 20 ... let me recheck.
        """
        table = phi01_discriminant_coeffs()
        # D = 12 - l^2: l=0 -> D=12, l=+-1 -> D=11, l=+-2 -> D=8, l=+-3 -> D=3
        # But also: l=+-4 -> D=12-16=-4 (skip). l=+-3 -> D=12-9=3. l=+-2 -> D=8.
        # Wait: D = 4*3 - l^2 = 12 - l^2.
        # l=0: D=12, l=+-1: D=11, l=+-2: D=8, l=+-3: D=3
        # But l can also be +-4: D=12-16 = -4 < -1 => c=0.
        # So: total = c(12) + 2*c(11) + 2*c(8) + 2*c(3)
        total = table[12] + 2*table[11] + 2*table[8] + 2*table[3]
        assert total == 0, f"n=3 constancy: got {total}"

    def test_constancy_at_n4(self):
        """At n=4: c(16) + 2*c(15) + 2*c(12) + 2*c(7) + 2*c(0) = 0."""
        table = phi01_discriminant_coeffs()
        total = table[16] + 2*table[15] + 2*table[12] + 2*table[7] + 2*table[0]
        assert total == 0, f"n=4 constancy: got {total}"

    def test_phi01_coeff_function(self):
        """phi01_coeff(n, l) correctly looks up c(4n - l^2)."""
        assert phi01_coeff(0, 0) == 10
        assert phi01_coeff(0, 1) == 1
        assert phi01_coeff(0, -1) == 1
        assert phi01_coeff(1, 0) == 108
        assert phi01_coeff(1, 1) == -64
        assert phi01_coeff(1, 2) == 10


# =========================================================================
# Section 4: Genus-g free energy
# =========================================================================

class TestGenusGFreeEnergy:
    """Verify F_g(K3) = 2 * lambda_g^FP."""

    def test_F1(self):
        """F_1 = 2/24 = 1/12."""
        assert F_g_k3(1) == Fraction(1, 12)

    def test_F2(self):
        """F_2 = 2 * 7/5760 = 7/2880."""
        assert F_g_k3(2) == Fraction(7, 2880)

    def test_F3(self):
        """F_3 = 2 * 31/967680 = 31/483840."""
        assert F_g_k3(3) == Fraction(31, 483840)

    def test_F1_explicit(self):
        """F_1 = kappa * |B_2|/(4*2!) = 2 * (1/6)/(4*2) = 2 * 1/48 ... no.

        lambda_1^FP = (2^1 - 1)/2^1 * |B_2|/2! = 1/2 * (1/6)/2 = 1/24.
        F_1 = 2 * 1/24 = 1/12.
        """
        lam1 = Fraction(1, 2) * Fraction(1, 6) / 2
        assert lam1 == Fraction(1, 24)
        assert F_g_k3(1) == 2 * lam1

    def test_Fg_positivity(self):
        """All F_g are positive (Bernoulli alternation absorbed by |B|)."""
        for g in range(1, 8):
            assert F_g_k3(g) > 0

    def test_ahat_consistency(self):
        """F_g from A-hat formula matches F_g from lambda_g^FP formula."""
        for g in range(1, 6):
            assert F_g_k3(g) == F_g_k3_ahat_check(g)


# =========================================================================
# Section 5: Shadow depth classification
# =========================================================================

class TestShadowDepth:
    """Verify K3 sigma model is class M (infinite shadow depth)."""

    def test_shadow_class(self):
        """K3 sigma model is class M."""
        result = k3_shadow_depth_analysis()
        assert result['shadow_class'] == 'M'

    def test_shadow_depth_infinite(self):
        """Shadow depth is infinite."""
        result = k3_shadow_depth_analysis()
        assert result['shadow_depth'] == 'infinite'

    def test_kappa_in_analysis(self):
        """Shadow analysis returns kappa = 2."""
        result = k3_shadow_depth_analysis()
        assert result['kappa'] == Fraction(2)

    def test_Q_contact_nonzero(self):
        """Virasoro Q^contact at c=6 is nonzero."""
        result = k3_shadow_depth_analysis()
        assert result['Q_contact_virasoro'] != 0
        # Q^contact = 10/(6*52) = 5/156
        assert result['Q_contact_virasoro'] == Fraction(5, 156)

    def test_has_weight1_currents(self):
        """K3 sigma model has SU(2)_R weight-1 currents (N=4 structure)."""
        result = k3_shadow_depth_analysis()
        assert result['has_weight_1_currents'] is True


# =========================================================================
# Section 6: Hilbert scheme of K3
# =========================================================================

class TestHilbK3:
    """Verify Hilbert scheme Euler characteristics."""

    def test_hilb0(self):
        """chi(Hilb^0(K3)) = 1 (point)."""
        assert hilb_k3_euler(0) == 1

    def test_hilb1(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        assert hilb_k3_euler(1) == 24

    def test_hilb2(self):
        """chi(Hilb^2(K3)) = 324."""
        assert hilb_k3_euler(2) == 324

    def test_hilb3(self):
        """chi(Hilb^3(K3)) = 3200."""
        assert hilb_k3_euler(3) == 3200

    def test_hilb4(self):
        """chi(Hilb^4(K3)) = 25650."""
        assert hilb_k3_euler(4) == 25650

    def test_hilb5(self):
        """chi(Hilb^5(K3)) = 176256."""
        assert hilb_k3_euler(5) == 176256

    def test_hilb_detailed_checks(self):
        """Cross-check via hilb_k3_partition_detailed."""
        result = hilb_k3_partition_detailed(nmax=10)
        for n, data in result['checks'].items():
            assert data['correct'], f"Hilb^{n}(K3) mismatch: {data}"

    def test_hilb2_formula(self):
        """chi(Hilb^2(K3)) = C(25,2) + 24 = 300 + 24 = 324.

        Decomposition: 2 = 1+1 (24*25/2 = 300 ways with 24 colors)
        plus 2 (24 ways with 24 colors).
        C(25,1) for part size 2 = 24 (one part of size 2 in any of 24 colors).
        Wait: 24 colors of part size 1, so 2 = 1+1 gives C(24+1, 2) = 300.
        Plus 2 itself gives 24 (one part of size 2 in 24 colors). Total 324.
        """
        # C(25,2) = 300 (two indistinguishable parts of size 1 from 24 colors)
        # 24 (one part of size 2 from 24 colors)
        assert math.comb(25, 2) + 24 == 324
        assert hilb_k3_euler(2) == 324


# =========================================================================
# Section 7: BKM root multiplicities
# =========================================================================

class TestBKMRoots:
    """Verify BKM root multiplicities from phi_{0,1}."""

    def test_odd_simple_root(self):
        """delta_2 = (0,-1,0): D=-1, mult=c(-1)=1 (odd/fermionic root)."""
        assert bkm_root_multiplicity(0, 0, -1) == 1

    def test_even_simple_root_delta1(self):
        """delta_1 = (1,0,0): D=0, mult=c(0)=10."""
        assert bkm_root_multiplicity(1, 0, 0) == 10

    def test_even_simple_root_delta3(self):
        """delta_3 = (0,1,0): D=0, mult=c(0)=10."""
        assert bkm_root_multiplicity(0, 1, 0) == 10

    def test_imaginary_root_level2(self):
        """Root (1,l=0,1): D=4*1*1-0=4, mult=c(4)=108."""
        assert bkm_root_multiplicity(1, 1, 0) == 108

    def test_imaginary_root_with_l(self):
        """Root (1,l=1,1): D=4*1*1-1=3, mult=c(3)=-64 (negative: fermionic)."""
        assert bkm_root_multiplicity(1, 1, 1) == -64

    def test_imaginary_root_nm_product(self):
        """Root (2,l=0,1): D=4*2*1-0=8, mult=c(8)=808."""
        assert bkm_root_multiplicity(2, 1, 0) == 808

    def test_verify_real_root_structure(self):
        """Verify the real root multiplicity table."""
        result = verify_real_root_multiplicities()
        # delta_2: odd root, mult = 1
        assert result['delta_2']['mult'] == 1
        assert result['delta_2']['D'] == -1
        # delta_1: even root, mult = 10
        assert result['delta_1']['mult'] == 10
        assert result['delta_1']['D'] == 0
        # delta_3: even root, mult = 10
        assert result['delta_3']['mult'] == 10
        assert result['delta_3']['D'] == 0

    def test_root_multiplicity_symmetry(self):
        """mult(n, l, m) = mult(n, -l, m) (phi_{0,1} symmetry in l)."""
        for n in range(3):
            for m in range(3):
                for l in range(4):
                    assert bkm_root_multiplicity(n, m, l) == bkm_root_multiplicity(n, m, -l)


# =========================================================================
# Section 8: DMVV formula
# =========================================================================

class TestDMVV:
    """Verify the DMVV product formula at low orders."""

    def test_dmvv_hilb0(self):
        """DMVV at p^0: chi(Sym^0(K3)) = chi(point) = 1."""
        result = dmvv_product_coeffs(p_max=5)
        assert result[(0, 0)] == 1

    def test_dmvv_hilb1(self):
        """DMVV at p^1: chi(Hilb^1(K3)) = chi(K3) = 24."""
        result = dmvv_product_coeffs(p_max=5)
        assert result[(1, 0)] == 24

    def test_dmvv_hilb2(self):
        """DMVV at p^2: chi(Hilb^2(K3)) = 324."""
        result = dmvv_product_coeffs(p_max=5)
        assert result[(2, 0)] == 324


# =========================================================================
# Section 9: Complementarity
# =========================================================================

class TestComplementarity:
    """Verify complementarity data for K3 sigma model."""

    def test_complementarity_sum_zero(self):
        """kappa(K3) + kappa(K3!) = 0."""
        result = k3_complementarity()
        assert result['complementarity_sum'] == 0

    def test_genus_by_genus_cancellation(self):
        """F_g(K3) + F_g(K3!) = 0 for each g."""
        result = k3_complementarity()
        for g in range(1, 6):
            assert result[f'genus_{g}']['sum'] == 0

    def test_not_virasoro_complementarity(self):
        """K3 sigma is NOT Virasoro: kappa+kappa'=0, not 13.

        For Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24).
        For K3 sigma: kappa + kappa' = 0 (like lattice VOAs).
        """
        result = k3_complementarity()
        assert result['complementarity_sum'] == 0
        assert result['complementarity_sum'] != 13


# =========================================================================
# Section 10: A-hat generating function
# =========================================================================

class TestAhatGF:
    """Verify the A-hat generating function F_g = kappa * (Ahat(ihbar) - 1)."""

    def test_ahat_kappa2(self):
        """A-hat GF with kappa = 2 gives correct F_g values."""
        result = ahat_generating_function(Fraction(2), gmax=5)
        assert result[1]['F_g'] == Fraction(1, 12)
        assert result[2]['F_g'] == Fraction(7, 2880)

    def test_ahat_is_positive(self):
        """All F_g > 0 for kappa > 0."""
        result = ahat_generating_function(Fraction(2), gmax=8)
        for g in range(1, 9):
            assert result[g]['F_g'] > 0


# =========================================================================
# Section 11: Mathieu moonshine
# =========================================================================

class TestMathieuMoonshine:
    """Verify Mathieu moonshine coefficients."""

    def test_A1_is_90(self):
        """A_1 = 90 = 45 + 45 (two M24 45-dim irreps)."""
        result = mathieu_moonshine_coefficients()
        assert result['A_n'][1] == 90

    def test_A2_is_462(self):
        """A_2 = 462 = 231 + 231."""
        result = mathieu_moonshine_coefficients()
        assert result['A_n'][2] == 462

    def test_A3_is_1540(self):
        """A_3 = 1540 = 770 + 770."""
        result = mathieu_moonshine_coefficients()
        assert result['A_n'][3] == 1540

    def test_A1_decomposition(self):
        """Verify A_1 = 45 + 45 (M24 irrep decomposition)."""
        result = mathieu_moonshine_coefficients()
        assert result['decomposition_checks']['A_1']['verified'] is True


# =========================================================================
# Section 12: Shadow tower -> BKM bridge
# =========================================================================

class TestShadowBKMBridge:
    """Verify the shadow tower -> BKM product formula connection."""

    def test_bridge_kappa(self):
        """Shadow tower arity 2 gives kappa = 2."""
        result = shadow_tower_to_product_formula(Fraction(2))
        assert result['arity_2']['kappa'] == Fraction(2)

    def test_bridge_F1(self):
        """F_1 = kappa/24 = 1/12 from arity-2 projection."""
        result = shadow_tower_to_product_formula(Fraction(2))
        assert result['arity_2']['F_1'] == Fraction(1, 12)

    def test_level_1_roots_exist(self):
        """Level 1 has roots with nonzero multiplicity."""
        result = shadow_tower_to_product_formula(Fraction(2), nmax=3)
        assert result['level_1']['num_distinct_roots'] > 0

    def test_level_1_multiplicities_from_phi01(self):
        """Root multiplicities at level 1 are phi_{0,1} coefficients."""
        result = shadow_tower_to_product_formula(Fraction(2), nmax=3)
        # Level 1 roots: (1,l,0), (0,l,1), and (0,-l,0) with l<0
        # These should have multiplicities c(D) from phi_{0,1}
        for root_data in result['level_1']['roots']:
            n, l, m = root_data['root']
            D = root_data['D']
            mult = root_data['mult']
            expected = phi01_discriminant_coeffs().get(D, 0)
            assert mult == expected, f"Root ({n},{l},{m}): D={D}, mult={mult}, expected={expected}"


# =========================================================================
# Section 13: Igusa cusp form
# =========================================================================

class TestIgusaConnection:
    """Verify Igusa cusp form Delta_5 connection."""

    def test_igusa_weight(self):
        """Delta_5 is weight 5 on H_2."""
        result = igusa_cusp_form_from_shadow()
        assert result['igusa_weight'] == 5

    def test_igusa_kappa(self):
        """kappa = 2 in the Igusa computation."""
        result = igusa_cusp_form_from_shadow()
        assert result['kappa_k3'] == Fraction(2)


# =========================================================================
# Section 14: Relative sewing amplitudes
# =========================================================================

class TestRelativeSewing:
    """Verify sewing amplitudes of the relative chiral algebra."""

    def test_genus1_F1(self):
        """Genus-1 sewing gives F_1 = 1/12."""
        result = relative_sewing_genus1()
        assert result['F_1_scalar'] == Fraction(1, 12)

    def test_genus1_kappa(self):
        """Genus-1 sewing uses kappa = 2."""
        result = relative_sewing_genus1()
        assert result['kappa'] == Fraction(2)

    def test_higher_genus_values(self):
        """Higher-genus F_g values match kappa * lambda_g^FP."""
        result = relative_sewing_higher_genus(gmax=5)
        for g in range(1, 6):
            expected = Fraction(2) * faber_pandharipande(g)
            assert result[g]['F_g_scalar'] == expected


# =========================================================================
# Section 15: Full bridge summary
# =========================================================================

class TestFullBridge:
    """Verify the full bridge A_{K3 x E / E} -> BKM -> Delta_5."""

    def test_bridge_exists(self):
        """The full bridge summary is self-consistent."""
        result = full_bridge_summary()
        assert result['kappa'] == 2
        assert result['shadow_class'] == 'M (infinite depth)'
        assert result['bypasses_d3_functor'] is True

    def test_bridge_chain_length(self):
        """The identification chain has 5 steps."""
        result = full_bridge_summary()
        assert len(result['chain']) == 5

    def test_bridge_bkm(self):
        """The BKM algebra is g_{Delta_5}."""
        result = full_bridge_summary()
        assert result['bkm_algebra'] == 'g_{Delta_5}'


# =========================================================================
# Section 16: Cross-checks and consistency
# =========================================================================

class TestCrossChecks:
    """Cross-family and cross-method consistency checks."""

    def test_kappa_k3_vs_lattice_rank24(self):
        """kappa(K3) = 2 != kappa(V_Leech) = 24.

        K3 sigma model (c=6, kappa=2) is NOT the same as the Leech
        lattice VOA (c=24, kappa=24).  They are unrelated algebras.
        AP48: kappa depends on the full algebra.
        """
        assert kappa_k3_sigma() == 2
        # Leech lattice VOA has kappa = 24
        assert kappa_k3_sigma() != 24

    def test_F_g_scaling(self):
        """F_g(K3) = (2/r) * F_g(V_{D_4}) for scalar level.

        V_{D_4} has rank 4, kappa = 4. K3 has kappa = 2.
        F_g is linear in kappa, so F_g(K3) / F_g(D_4) = 2/4 = 1/2.
        """
        kappa_k3 = Fraction(2)
        kappa_d4 = Fraction(4)
        for g in range(1, 6):
            Fg_k3 = kappa_k3 * faber_pandharipande(g)
            Fg_d4 = kappa_d4 * faber_pandharipande(g)
            assert Fg_k3 * 2 == Fg_d4

    def test_phi01_n0_is_k3_chi_over_2(self):
        """phi_{0,1}(tau, 0) = 12 = chi(K3)/2.

        The K3 elliptic genus is 2 * phi_{0,1}, so at z=0:
        phi(K3; tau, 0) = 2 * 12 = 24 = chi(K3).
        """
        table = phi01_discriminant_coeffs()
        phi01_at_0 = table[0] + 2 * table[-1]  # c(0) + 2*c(-1) = 10 + 2 = 12
        assert phi01_at_0 == 12
        assert 2 * phi01_at_0 == K3_EULER_CHAR

    def test_hilb_growth_rate(self):
        """chi(Hilb^n(K3)) grows like exp(4*pi*sqrt(n)) / n^{27/4}.

        From the Hardy-Ramanujan-Rademacher formula for p_{-24}(n).
        Verify the growth is superexponential (consistent with asymptotic).
        """
        h3 = hilb_k3_euler(3)
        h4 = hilb_k3_euler(4)
        h5 = hilb_k3_euler(5)
        # Check monotonic growth
        assert h5 > h4 > h3 > 0
        # Check growth rate: ratio h5/h4 should be around 6-7
        ratio = h5 / h4
        assert 5 < ratio < 10

    def test_bernoulli_B2(self):
        """B_2 = 1/6 (used in lambda_1^FP)."""
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_bernoulli_B4(self):
        """B_4 = -1/30."""
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_lambda1_FP(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Fraction(1, 24)

    def test_lambda2_FP(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Fraction(7, 5760)

    def test_lambda3_FP(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Fraction(31, 967680)
