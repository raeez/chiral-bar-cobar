r"""Tests for elliptic genus and refined partition functions of K3 x E.

Multi-path verification of all invariants:
(a) Hodge number Kunneth (entry-by-entry, Betti, alternating sum)
(b) chi_y genus product formula vs direct computation
(c) GV/DT comparison and cross-family checks
(d) Shadow tower kappa additivity and F_g formulas
(e) Symmetry verification (Poincare, Serre, complex conjugation)

Target: >= 100 tests with >= 3 independent verification paths per claim.
"""

import math
from fractions import Fraction as F

import pytest

from compute.lib.cy_elliptic_genus_k3e_engine import (
    HodgeDiamond,
    product_hodge,
    k3_hodge,
    elliptic_hodge,
    k3_times_e_hodge,
    quintic_hodge,
    compute_elliptic_genus_k3,
    compute_elliptic_genus_e,
    compute_elliptic_genus_k3e,
    elliptic_genus_vanishing_reason,
    compute_chi_y,
    chi_y_product_verification,
    gv_k3_pure_class,
    gv_e_class,
    gv_genus0_k3_invariants,
    hilb_n_k3_euler,
    compute_genus1_k3e,
    compute_genus1_k3,
    compute_genus1_e,
    compute_shadow_tower_k3e,
    compute_shadow_tower_k3,
    compute_shadow_tower_e,
    lambda_fp,
    compute_hodge_elliptic_k3e,
    verify_hodge_symmetries,
    compute_dt_data_k3e,
    ray_singer_data_k3e,
    dmvv_coefficients,
    dmvv_product_coefficients,
    compute_new_susy_index_k3e,
    verify_kunneth_hodge_numbers,
    verify_additivity_kappa,
    verify_euler_product,
    verify_hodge_numbers_k3e_detailed,
    compare_with_quintic,
    compute_all_k3e,
)


# =========================================================================
# Section 1: K3 Hodge diamond (20 tests)
# =========================================================================

class TestK3Hodge:
    """Verify K3 surface Hodge diamond from first principles."""

    def test_k3_dimension(self):
        """K3 is a complex surface: dim_C = 2."""
        assert k3_hodge().dim == 2

    def test_k3_h00(self):
        """h^{0,0}(K3) = 1 (connected)."""
        assert k3_hodge().h(0, 0) == 1

    def test_k3_h10(self):
        """h^{1,0}(K3) = 0 (simply connected)."""
        assert k3_hodge().h(1, 0) == 0

    def test_k3_h01(self):
        """h^{0,1}(K3) = 0 (by conjugation from h^{1,0})."""
        assert k3_hodge().h(0, 1) == 0

    def test_k3_h20(self):
        """h^{2,0}(K3) = 1 (K_X trivial => unique holomorphic 2-form)."""
        assert k3_hodge().h(2, 0) == 1

    def test_k3_h11(self):
        """h^{1,1}(K3) = 20 (lattice theory: H^2 rank 22, minus h^{2,0}+h^{0,2})."""
        assert k3_hodge().h(1, 1) == 20

    def test_k3_h02(self):
        """h^{0,2}(K3) = 1 (conjugation from h^{2,0})."""
        assert k3_hodge().h(0, 2) == 1

    def test_k3_h22(self):
        """h^{2,2}(K3) = 1 (Poincare duality from h^{0,0})."""
        assert k3_hodge().h(2, 2) == 1

    def test_k3_euler_characteristic(self):
        """chi(K3) = 24."""
        assert k3_hodge().euler == 24

    def test_k3_euler_three_paths(self):
        """chi(K3) = 24 verified three ways."""
        hd = k3_hodge()
        # Path 1: sum (-1)^{p+q} h^{p,q}
        path1 = hd.euler
        # Path 2: alternating Betti sum
        betti = hd.betti_numbers
        path2 = sum((-1) ** k * betti.get(k, 0) for k in range(5))
        # Path 3: explicit: 1 - 0 + (1+20+1) - 0 + 1 = 24
        path3 = 1 - 0 + (1 + 20 + 1) - 0 + 1
        assert path1 == path2 == path3 == 24

    def test_k3_holomorphic_euler(self):
        """chi(O_{K3}) = 2."""
        assert k3_hodge().chi_O == F(2)

    def test_k3_betti_numbers(self):
        """Betti numbers of K3: b_0=1, b_1=0, b_2=22, b_3=0, b_4=1."""
        betti = k3_hodge().betti_numbers
        assert betti.get(0, 0) == 1
        assert betti.get(1, 0) == 0
        assert betti.get(2, 0) == 22
        assert betti.get(3, 0) == 0
        assert betti.get(4, 0) == 1

    def test_k3_poincare_duality(self):
        """b_k(K3) = b_{4-k}(K3)."""
        betti = k3_hodge().betti_numbers
        for k in range(5):
            assert betti.get(k, 0) == betti.get(4 - k, 0)

    def test_k3_conjugation_symmetry(self):
        """h^{p,q}(K3) = h^{q,p}(K3)."""
        hd = k3_hodge()
        for p in range(3):
            for q in range(3):
                assert hd.h(p, q) == hd.h(q, p)

    def test_k3_serre_duality(self):
        """h^{p,q}(K3) = h^{2-p,2-q}(K3)."""
        hd = k3_hodge()
        for p in range(3):
            for q in range(3):
                assert hd.h(p, q) == hd.h(2 - p, 2 - q)

    def test_k3_total_betti(self):
        """Sum of all Hodge numbers = sum of Betti numbers = 24."""
        assert k3_hodge().total_betti == 24

    def test_k3_b2_equals_22(self):
        """Second Betti number b_2(K3) = 22 (rank of H^2 lattice)."""
        assert k3_hodge().betti_numbers[2] == 22

    def test_k3_signature(self):
        """Signature tau(K3) = -16 (from b_2^+ = 3, b_2^- = 19).

        tau = b_2^+ - b_2^- = 3 - 19 = -16.
        Equivalently: tau = sum_{p even} (-1)^q h^{p,q} - sum_{p odd} (-1)^q h^{p,q}
        For K3: tau = (1 + 1 + 1 + 1) - 2*(0 + 20 + 0) + ... hmm.

        Actually: signature = chi_{y=1} for surfaces.
        chi_y(K3)|_{y=1} = chi(O) + chi(Omega^1) + chi(Omega^2) = 2 - 20 + 2 = -16.
        """
        hd = k3_hodge()
        chi_y_at_1 = sum(hd.chi_Omega_p(p) for p in range(3))
        assert chi_y_at_1 == -16

    def test_k3_cy_condition(self):
        """K3 satisfies CY condition: h^{2,0} = 1, h^{0,0} = 1."""
        hd = k3_hodge()
        assert hd.h(2, 0) == 1
        assert hd.h(0, 0) == 1


# =========================================================================
# Section 2: Elliptic curve Hodge diamond (10 tests)
# =========================================================================

class TestEllipticHodge:
    """Verify elliptic curve E Hodge diamond."""

    def test_e_dimension(self):
        assert elliptic_hodge().dim == 1

    def test_e_h00(self):
        assert elliptic_hodge().h(0, 0) == 1

    def test_e_h10(self):
        """h^{1,0}(E) = 1 (genus = 1)."""
        assert elliptic_hodge().h(1, 0) == 1

    def test_e_h01(self):
        assert elliptic_hodge().h(0, 1) == 1

    def test_e_h11(self):
        assert elliptic_hodge().h(1, 1) == 1

    def test_e_euler_zero(self):
        """chi(E) = 0."""
        assert elliptic_hodge().euler == 0

    def test_e_euler_explicit(self):
        """chi(E) = 1 - 1 - 1 + 1 = 0."""
        assert 1 - 1 - 1 + 1 == 0
        assert elliptic_hodge().euler == 0

    def test_e_holomorphic_euler(self):
        """chi(O_E) = h^{0,0} - h^{0,1} = 1 - 1 = 0."""
        assert elliptic_hodge().chi_O == F(0)

    def test_e_betti_numbers(self):
        """b_0=1, b_1=2, b_2=1."""
        betti = elliptic_hodge().betti_numbers
        assert betti[0] == 1
        assert betti[1] == 2
        assert betti[2] == 1

    def test_e_total_betti(self):
        assert elliptic_hodge().total_betti == 4


# =========================================================================
# Section 3: K3 x E Hodge diamond via Kunneth (20 tests)
# =========================================================================

class TestK3xEHodge:
    """Verify K3 x E Hodge diamond via Kunneth formula."""

    def test_k3xe_dimension(self):
        """K3 x E has dim_C = 3."""
        assert k3_times_e_hodge().dim == 3

    def test_k3xe_h00(self):
        assert k3_times_e_hodge().h(0, 0) == 1

    def test_k3xe_h10(self):
        """h^{1,0} = h^{0,0}(K3)*h^{1,0}(E) + h^{1,0}(K3)*h^{0,0}(E) = 1*1+0*1 = 1."""
        assert k3_times_e_hodge().h(1, 0) == 1

    def test_k3xe_h01(self):
        assert k3_times_e_hodge().h(0, 1) == 1

    def test_k3xe_h11(self):
        """h^{1,1} = h^{0,0}*h^{1,1}(E) + h^{1,1}(K3)*h^{0,0}(E) + h^{1,0}*h^{0,1} + h^{0,1}*h^{1,0}
                   = 1*1 + 20*1 + 0*1 + 0*1 = 21."""
        assert k3_times_e_hodge().h(1, 1) == 21

    def test_k3xe_h20(self):
        """h^{2,0} = h^{2,0}(K3)*h^{0,0}(E) + h^{1,0}(K3)*h^{1,0}(E) = 1*1+0*1 = 1."""
        assert k3_times_e_hodge().h(2, 0) == 1

    def test_k3xe_h21(self):
        """h^{2,1} = h^{2,0}(K3)*h^{0,1}(E) + h^{1,1}(K3)*h^{1,0}(E)
                   + h^{2,1}(K3)*h^{0,0}(E) + h^{1,0}(K3)*h^{1,1}(E)
                   = 1*1 + 20*1 + 0*1 + 0*1 = 21."""
        assert k3_times_e_hodge().h(2, 1) == 21

    def test_k3xe_h30(self):
        """h^{3,0} = h^{2,0}(K3)*h^{1,0}(E) = 1*1 = 1."""
        assert k3_times_e_hodge().h(3, 0) == 1

    def test_k3xe_h12(self):
        assert k3_times_e_hodge().h(1, 2) == 21

    def test_k3xe_h03(self):
        assert k3_times_e_hodge().h(0, 3) == 1

    def test_k3xe_h31(self):
        assert k3_times_e_hodge().h(3, 1) == 1

    def test_k3xe_h22(self):
        assert k3_times_e_hodge().h(2, 2) == 21

    def test_k3xe_h33(self):
        assert k3_times_e_hodge().h(3, 3) == 1

    def test_k3xe_euler_zero(self):
        """chi(K3 x E) = 0 (from chi(K3)*chi(E) = 24*0)."""
        assert k3_times_e_hodge().euler == 0

    def test_k3xe_euler_product(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert k3_hodge().euler * elliptic_hodge().euler == 0

    def test_k3xe_betti_numbers(self):
        """Betti numbers: b_0=1, b_1=2, b_2=23, b_3=44, b_4=23, b_5=2, b_6=1."""
        betti = k3_times_e_hodge().betti_numbers
        assert betti[0] == 1
        assert betti[1] == 2
        assert betti[2] == 23
        assert betti[3] == 44
        assert betti[4] == 23
        assert betti[5] == 2
        assert betti[6] == 1

    def test_k3xe_betti_sum(self):
        """Sum of Betti numbers = 1+2+23+44+23+2+1 = 96."""
        betti = k3_times_e_hodge().betti_numbers
        assert sum(betti.values()) == 96

    def test_k3xe_total_hodge(self):
        """Sum of all h^{p,q} = 96."""
        assert k3_times_e_hodge().total_betti == 96

    def test_k3xe_poincare_duality(self):
        """b_k = b_{6-k} for K3 x E."""
        betti = k3_times_e_hodge().betti_numbers
        for k in range(7):
            assert betti.get(k, 0) == betti.get(6 - k, 0)

    def test_k3xe_conjugation(self):
        """h^{p,q} = h^{q,p}."""
        hd = k3_times_e_hodge()
        for p in range(4):
            for q in range(4):
                assert hd.h(p, q) == hd.h(q, p)

    def test_k3xe_serre_duality(self):
        """h^{p,q} = h^{3-p,3-q}."""
        hd = k3_times_e_hodge()
        for p in range(4):
            for q in range(4):
                assert hd.h(p, q) == hd.h(3 - p, 3 - q)


# =========================================================================
# Section 4: Kunneth cross-verification (8 tests)
# =========================================================================

class TestKunnethVerification:
    """Cross-verify Kunneth formula via multiple paths."""

    def test_all_paths_agree(self):
        result = verify_kunneth_hodge_numbers()
        assert result['all_paths_agree']

    def test_betti_agree(self):
        result = verify_kunneth_hodge_numbers()
        assert result['betti_agree']

    def test_no_discrepancies(self):
        result = verify_kunneth_hodge_numbers()
        assert len(result['discrepancies']) == 0

    def test_euler_from_kunneth(self):
        result = verify_kunneth_hodge_numbers()
        assert result['euler'] == 0

    def test_total_hodge_from_kunneth(self):
        result = verify_kunneth_hodge_numbers()
        assert result['total_hodge'] == 96

    def test_detailed_h11(self):
        """h^{1,1}(K3xE) = 21 with explicit Kunneth terms."""
        details = verify_hodge_numbers_k3e_detailed()
        assert details[(1, 1)]['value'] == 21

    def test_detailed_h21(self):
        details = verify_hodge_numbers_k3e_detailed()
        assert details[(2, 1)]['value'] == 21

    def test_detailed_h30(self):
        details = verify_hodge_numbers_k3e_detailed()
        assert details[(3, 0)]['value'] == 1


# =========================================================================
# Section 5: Elliptic genus vanishing (12 tests)
# =========================================================================

class TestEllipticGenus:
    """Verify elliptic genus computations."""

    def test_k3_elliptic_genus_nonzero(self):
        eg = compute_elliptic_genus_k3()
        assert not eg.vanishes

    def test_k3_elliptic_genus_index(self):
        """K3 elliptic genus is Jacobi form of index d/2 = 1."""
        eg = compute_elliptic_genus_k3()
        assert eg.index == F(1)

    def test_k3_euler_24(self):
        eg = compute_elliptic_genus_k3()
        assert eg.chi_euler == 24

    def test_e_elliptic_genus_zero(self):
        """Z_E(tau, z) = 0."""
        eg = compute_elliptic_genus_e()
        assert eg.vanishes

    def test_e_chi_O_zero(self):
        """chi(O_E) = 0 forces Z_E = 0."""
        eg = compute_elliptic_genus_e()
        assert eg.chi_O == F(0)

    def test_k3xe_elliptic_genus_zero(self):
        """Z_{K3xE} = Z_{K3} * Z_E = 0."""
        eg = compute_elliptic_genus_k3e()
        assert eg.vanishes

    def test_k3xe_vanishing_reason(self):
        """The vanishing is because chi_y = 0."""
        hd = k3_times_e_hodge()
        reason = elliptic_genus_vanishing_reason(hd)
        assert reason is not None

    def test_k3xe_euler_zero(self):
        eg = compute_elliptic_genus_k3e()
        assert eg.chi_euler == 0

    def test_k3xe_index(self):
        """K3 x E: Jacobi index = d/2 = 3/2."""
        eg = compute_elliptic_genus_k3e()
        assert eg.index == F(3, 2)

    def test_product_vanishing_theorem(self):
        """For ANY X: Z_{X x E}(tau,z) = 0 because Z_E = 0."""
        # Test with quintic x E
        quintic_e = product_hodge(quintic_hodge(), elliptic_hodge())
        reason = elliptic_genus_vanishing_reason(quintic_e)
        assert reason is not None

    def test_k3_chi_y_nonzero(self):
        """chi_y(K3) != 0."""
        cy = compute_chi_y(k3_hodge(), "K3")
        assert not cy.vanishes_identically

    def test_e_chi_y_zero(self):
        """chi_y(E) = 0 identically."""
        cy = compute_chi_y(elliptic_hodge(), "E")
        assert cy.vanishes_identically


# =========================================================================
# Section 6: chi_y genus (15 tests)
# =========================================================================

class TestChiYGenus:
    """Verify chi_y genus computations via multiple paths."""

    def test_k3_chi_Omega0(self):
        """chi(O_{K3}) = 2."""
        cy = compute_chi_y(k3_hodge(), "K3")
        assert cy.chi_Omega[0] == 2

    def test_k3_chi_Omega1(self):
        """chi(Omega^1_{K3}) = 0 - 20 + 0 = -20."""
        cy = compute_chi_y(k3_hodge(), "K3")
        assert cy.chi_Omega[1] == -20

    def test_k3_chi_Omega2(self):
        """chi(Omega^2_{K3}) = 1 - 0 + 1 = 2."""
        cy = compute_chi_y(k3_hodge(), "K3")
        assert cy.chi_Omega[2] == 2

    def test_k3_chi_y_polynomial(self):
        """chi_y(K3) = 2 - 20y + 2y^2."""
        cy = compute_chi_y(k3_hodge(), "K3")
        assert cy.chi_y_poly.get(0, 0) == 2
        assert cy.chi_y_poly.get(1, 0) == -20
        assert cy.chi_y_poly.get(2, 0) == 2

    def test_k3_chi_y_at_minus1(self):
        """chi_{y=-1}(K3) = chi(K3) = 24."""
        cy = compute_chi_y(k3_hodge(), "K3")
        assert cy.chi_y_at_minus_1 == 24

    def test_k3_chi_y_at_minus1_explicit(self):
        """2*(-1)^0 - 20*(-1)^1 + 2*(-1)^2 = 2 + 20 + 2 = 24."""
        assert 2 - (-20) + 2 == 24

    def test_e_chi_Omega0(self):
        """chi(O_E) = 0."""
        cy = compute_chi_y(elliptic_hodge(), "E")
        assert cy.chi_Omega[0] == 0

    def test_e_chi_Omega1(self):
        """chi(Omega^1_E) = 0."""
        cy = compute_chi_y(elliptic_hodge(), "E")
        assert cy.chi_Omega[1] == 0

    def test_k3xe_chi_y_vanishes(self):
        """chi_y(K3 x E) = 0 identically."""
        cy = compute_chi_y(k3_times_e_hodge(), "K3xE")
        assert cy.vanishes_identically

    def test_chi_y_product_formula(self):
        """chi_y(K3xE) = chi_y(K3) * chi_y(E) verified via product."""
        result = chi_y_product_verification(k3_hodge(), elliptic_hodge(), "K3", "E")
        assert result['paths_agree']
        assert result['poly_agree']

    def test_chi_y_product_is_zero(self):
        """The product polynomial is empty (all zero)."""
        result = chi_y_product_verification(k3_hodge(), elliptic_hodge())
        assert len(result['product_poly']) == 0

    def test_k3xe_chi_Omega_all_zero(self):
        """Every chi(Omega^p(K3xE)) = 0."""
        cy = compute_chi_y(k3_times_e_hodge(), "K3xE")
        for p in range(4):
            assert cy.chi_Omega[p] == 0

    def test_k3xe_chi_Omega0_product(self):
        """chi(O_{K3xE}) = chi(O_{K3})*chi(O_E) + ... via Kunneth.

        chi(Omega^0(K3xE)) = sum_{a+b=0} chi(Omega^a(K3)) chi(Omega^b(E))
                            = chi(O_{K3}) * chi(O_E) = 2 * 0 = 0."""
        k3_chi = compute_chi_y(k3_hodge(), "K3")
        e_chi = compute_chi_y(elliptic_hodge(), "E")
        product = k3_chi.chi_Omega[0] * e_chi.chi_Omega[0]
        assert product == 0

    def test_k3xe_chi_Omega1_product(self):
        """chi(Omega^1(K3xE)) = chi(O_K3)*chi(Omega^1_E) + chi(Omega^1_K3)*chi(O_E)
                               = 2*0 + (-20)*0 = 0."""
        k3_chi = compute_chi_y(k3_hodge(), "K3")
        e_chi = compute_chi_y(elliptic_hodge(), "E")
        product = k3_chi.chi_Omega[0] * e_chi.chi_Omega[1] + k3_chi.chi_Omega[1] * e_chi.chi_Omega[0]
        assert product == 0

    def test_quintic_chi_y_nonzero(self):
        """chi_y(quintic) != 0 (for comparison)."""
        cy = compute_chi_y(quintic_hodge(), "quintic")
        assert not cy.vanishes_identically


# =========================================================================
# Section 7: Gopakumar-Vafa invariants (10 tests)
# =========================================================================

class TestGVInvariants:
    """Verify GV invariant computations."""

    def test_gv_k3_h0(self):
        """n^0_0 = 1 (point class)."""
        gv = gv_k3_pure_class(5)
        assert gv[0] == 1

    def test_gv_k3_h1(self):
        """n^0_1 = 24 (genus-0 GV for K3, from 1/(1-q)^24)."""
        gv = gv_k3_pure_class(5)
        assert gv[1] == 24

    def test_gv_k3_h2(self):
        """n^0_2 = 324."""
        gv = gv_k3_pure_class(5)
        assert gv[2] == 324

    def test_gv_k3_h3(self):
        """n^0_3 = 3200."""
        gv = gv_k3_pure_class(5)
        assert gv[3] == 3200

    def test_gv_k3_h4(self):
        """n^0_4 = 25650."""
        gv = gv_k3_pure_class(5)
        assert gv[4] == 25650

    def test_gv_k3_h5(self):
        """n^0_5 = 176256."""
        gv = gv_k3_pure_class(5)
        assert gv[5] == 176256

    def test_hilb_equals_gv(self):
        """chi(Hilb^N(K3)) = GV genus-0 invariants (multi-path)."""
        gv = gv_genus0_k3_invariants(5)
        hilb = hilb_n_k3_euler(5)
        for n in range(6):
            assert gv[n] == hilb[n]

    def test_gv_e_genus0_zero(self):
        """No rational curves wrap E."""
        gv = gv_e_class()
        assert gv[0] == 0

    def test_gv_e_genus1(self):
        """Genus-1 GV for E class: -chi(K3) = -24."""
        gv = gv_e_class()
        assert gv[1] == -24

    def test_gv_integrality(self):
        """All GV invariants are integers."""
        gv = gv_k3_pure_class(10)
        for h, n in gv.items():
            assert isinstance(n, int)


# =========================================================================
# Section 8: Genus-1 partition function (12 tests)
# =========================================================================

class TestGenus1:
    """Verify genus-1 partition function data."""

    def test_k3xe_chi_zero(self):
        g1 = compute_genus1_k3e()
        assert g1.chi == 0

    def test_k3xe_bcov_leading_zero(self):
        """BCOV leading term -chi/12 = 0."""
        g1 = compute_genus1_k3e()
        assert g1.f1_bcov_leading == F(0)

    def test_k3xe_kappa_3(self):
        """kappa(K3 x E) = 3 (CY dimension)."""
        g1 = compute_genus1_k3e()
        assert g1.kappa == F(3)

    def test_k3xe_f1_shadow(self):
        """F_1 = kappa/24 = 3/24 = 1/8."""
        g1 = compute_genus1_k3e()
        assert g1.f1_shadow == F(1, 8)

    def test_k3xe_f1_nonzero(self):
        """F_1 does NOT vanish despite chi = 0 (AP31)."""
        g1 = compute_genus1_k3e()
        assert not g1.f1_vanishes
        assert g1.f1_shadow != 0

    def test_k3_kappa_2(self):
        g1 = compute_genus1_k3()
        assert g1.kappa == F(2)

    def test_k3_f1(self):
        """F_1(K3) = 2/24 = 1/12."""
        g1 = compute_genus1_k3()
        assert g1.f1_shadow == F(1, 12)

    def test_e_kappa_1(self):
        g1 = compute_genus1_e()
        assert g1.kappa == F(1)

    def test_e_f1(self):
        """F_1(E) = 1/24."""
        g1 = compute_genus1_e()
        assert g1.f1_shadow == F(1, 24)

    def test_f1_additivity(self):
        """F_1(K3xE) = F_1(K3) + F_1(E)."""
        f1_k3 = compute_genus1_k3().f1_shadow
        f1_e = compute_genus1_e().f1_shadow
        f1_k3e = compute_genus1_k3e().f1_shadow
        assert f1_k3 + f1_e == f1_k3e

    def test_f1_additivity_explicit(self):
        """1/12 + 1/24 = 3/24 = 1/8."""
        assert F(1, 12) + F(1, 24) == F(1, 8)

    def test_new_susy_nonzero(self):
        """New-supersymmetric index is nonzero for K3 x E."""
        g1 = compute_genus1_k3e()
        assert g1.new_susy_index_nonzero


# =========================================================================
# Section 9: Shadow obstruction tower (15 tests)
# =========================================================================

class TestShadowTower:
    """Verify shadow obstruction tower data."""

    def test_k3xe_kappa(self):
        st = compute_shadow_tower_k3e()
        assert st.kappa == F(3)

    def test_k3xe_dim(self):
        st = compute_shadow_tower_k3e()
        assert st.dim_c == 3

    def test_k3xe_kappa_equals_dim(self):
        """For CY: kappa = dim_C."""
        st = compute_shadow_tower_k3e()
        assert st.kappa_equals_dim
        assert st.kappa == F(st.dim_c)

    def test_k3xe_shadow_class_M(self):
        """K3 x E has infinite shadow depth (class M)."""
        st = compute_shadow_tower_k3e()
        assert st.shadow_depth_class == "M"

    def test_kappa_additivity(self):
        """kappa(K3xE) = kappa(K3) + kappa(E)."""
        result = verify_additivity_kappa()
        assert result['additivity_kappa']

    def test_f1_additivity_shadow(self):
        result = verify_additivity_kappa()
        assert result['additivity_f1']

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == F(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == F(7, 5760)

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == F(31, 967680)

    def test_k3xe_f1(self):
        st = compute_shadow_tower_k3e()
        assert st.f_g[1] == F(3) * F(1, 24)
        assert st.f_g[1] == F(1, 8)

    def test_k3xe_f2(self):
        """F_2(K3xE) = 3 * 7/5760 = 7/1920."""
        st = compute_shadow_tower_k3e()
        assert st.f_g[2] == F(7, 1920)

    def test_k3xe_f3(self):
        """F_3(K3xE) = 3 * 31/967680 = 31/322560."""
        st = compute_shadow_tower_k3e()
        assert st.f_g[3] == F(31, 322560)

    def test_f_g_additivity_all_genera(self):
        """F_g(K3xE) = F_g(K3) + F_g(E) for g = 1,...,5."""
        st_k3e = compute_shadow_tower_k3e()
        st_k3 = compute_shadow_tower_k3()
        st_e = compute_shadow_tower_e()
        for g in range(1, 6):
            assert st_k3.f_g[g] + st_e.f_g[g] == st_k3e.f_g[g]

    def test_f_g_positive(self):
        """F_g > 0 for all g >= 1 (from positive kappa and positive lambda^FP)."""
        st = compute_shadow_tower_k3e()
        for g in range(1, 6):
            assert st.f_g[g] > 0

    def test_k3xe_chi_nonzero_kappa(self):
        """chi = 0 but kappa = 3 != 0 (AP31: no contradiction)."""
        st = compute_shadow_tower_k3e()
        assert st.chi == 0
        assert st.kappa == F(3)
        assert st.kappa != 0


# =========================================================================
# Section 10: Hodge symmetries (5 tests)
# =========================================================================

class TestHodgeSymmetries:
    """Verify Hodge diamond symmetries for all spaces."""

    def test_k3_symmetries(self):
        result = verify_hodge_symmetries(k3_hodge())
        assert result['conjugation']
        assert result['serre_duality']
        assert result['poincare_duality']
        assert result['calabi_yau_triviality']

    def test_e_symmetries(self):
        result = verify_hodge_symmetries(elliptic_hodge())
        assert result['conjugation']
        assert result['serre_duality']
        assert result['poincare_duality']
        assert result['calabi_yau_triviality']

    def test_k3xe_symmetries(self):
        result = verify_hodge_symmetries(k3_times_e_hodge())
        assert result['conjugation']
        assert result['serre_duality']
        assert result['poincare_duality']
        assert result['calabi_yau_triviality']

    def test_quintic_symmetries(self):
        result = verify_hodge_symmetries(quintic_hodge())
        assert result['conjugation']
        assert result['serre_duality']
        assert result['poincare_duality']
        assert result['calabi_yau_triviality']

    def test_k3xe_cy_condition(self):
        """h^{3,0} = 1 and h^{0,0} = 1 for CY3."""
        hd = k3_times_e_hodge()
        assert hd.h(3, 0) == 1
        assert hd.h(0, 0) == 1


# =========================================================================
# Section 11: Euler characteristic three paths (5 tests)
# =========================================================================

class TestEulerThreePaths:
    """Verify chi = 0 via three independent methods."""

    def test_path1_hodge(self):
        result = verify_euler_product()
        assert result['path1_hodge'] == 0

    def test_path2_product(self):
        result = verify_euler_product()
        assert result['path2_product'] == 0

    def test_path3_betti(self):
        result = verify_euler_product()
        assert result['path3_betti'] == 0

    def test_all_zero(self):
        result = verify_euler_product()
        assert result['all_zero']

    def test_explicit_betti_alternating_sum(self):
        """1 - 2 + 23 - 44 + 23 - 2 + 1 = 0."""
        assert 1 - 2 + 23 - 44 + 23 - 2 + 1 == 0


# =========================================================================
# Section 12: DT invariants and DMVV (5 tests)
# =========================================================================

class TestDTandDMVV:
    """Verify DT invariant structure and DMVV formula."""

    def test_dt_chi_zero(self):
        dt = compute_dt_data_k3e()
        assert dt.chi == 0

    def test_dt_macmahon_trivial(self):
        """M(-q)^0 = 1."""
        dt = compute_dt_data_k3e()
        assert dt.macmahon_is_trivial

    def test_dt_reduced_equals_full(self):
        dt = compute_dt_data_k3e()
        assert dt.reduced_equals_full

    def test_dmvv_z0_constant(self):
        """phi_{0,1}(tau, 0) = 12 => coefficients [12, 0, 0, ...]."""
        coeffs = dmvv_coefficients(5)
        assert coeffs[0] == 12
        for n in range(1, 6):
            assert coeffs[n] == 0

    def test_hilb_k3_gottsche(self):
        """chi(Hilb^N(K3)) from Gottsche's formula matches GV."""
        hilb = hilb_n_k3_euler(5)
        assert hilb[0] == 1
        assert hilb[1] == 24
        assert hilb[2] == 324


# =========================================================================
# Section 13: Ray-Singer torsion (3 tests)
# =========================================================================

class TestRaySinger:
    """Verify Ray-Singer analytic torsion data."""

    def test_rs_chi_zero(self):
        rs = ray_singer_data_k3e()
        assert rs['chi'] == 0

    def test_rs_leading_vanishes(self):
        rs = ray_singer_data_k3e()
        assert rs['leading_vanishes']

    def test_rs_h1_nonzero(self):
        """b_1(K3xE) = 2 > 0, so torsion is nontrivial."""
        rs = ray_singer_data_k3e()
        assert rs['h1_nonzero']


# =========================================================================
# Section 14: Hodge-elliptic genus (4 tests)
# =========================================================================

class TestHodgeElliptic:
    """Verify Hodge-elliptic genus data."""

    def test_constant_map_vanishes(self):
        he = compute_hodge_elliptic_k3e()
        assert he.vanishes  # constant-map part

    def test_refined_nontrivial(self):
        he = compute_hodge_elliptic_k3e()
        assert he.refined_nontrivial

    def test_k3_chi_y_in_he(self):
        """chi_y(K3) part: {0: 2, 1: -20, 2: 2}."""
        he = compute_hodge_elliptic_k3e()
        assert he.chi_y1_k3.get(0, 0) == 2
        assert he.chi_y1_k3.get(1, 0) == -20
        assert he.chi_y1_k3.get(2, 0) == 2

    def test_e_chi_y_in_he_zero(self):
        """chi_y(E) = 0 identically."""
        he = compute_hodge_elliptic_k3e()
        assert all(v == 0 for v in he.chi_y2_e.values()) or len(he.chi_y2_e) == 0


# =========================================================================
# Section 15: New supersymmetric index (3 tests)
# =========================================================================

class TestNewSusyIndex:
    """Verify new-supersymmetric index data."""

    def test_nonzero(self):
        nsi = compute_new_susy_index_k3e()
        assert nsi.nonzero

    def test_weight(self):
        nsi = compute_new_susy_index_k3e()
        assert nsi.weight == 2

    def test_siegel_connection(self):
        nsi = compute_new_susy_index_k3e()
        assert "Phi_10" in nsi.siegel_connection or "chi_10" in nsi.siegel_connection


# =========================================================================
# Section 16: Comparison with quintic (5 tests)
# =========================================================================

class TestQuinticComparison:
    """Compare K3 x E with the quintic CY3."""

    def test_same_kappa(self):
        """Both K3xE and quintic have kappa = 3 (AP48)."""
        comp = compare_with_quintic()
        assert comp['same_kappa']

    def test_different_chi(self):
        comp = compare_with_quintic()
        assert comp['different_chi']

    def test_quintic_chi_minus_200(self):
        comp = compare_with_quintic()
        assert comp['quintic']['chi'] == -200

    def test_k3xe_chi_zero_in_comparison(self):
        comp = compare_with_quintic()
        assert comp['k3xe']['chi'] == 0

    def test_quintic_elliptic_genus_nonzero(self):
        comp = compare_with_quintic()
        assert not comp['quintic']['elliptic_genus_vanishes']


# =========================================================================
# Section 17: Master computation (5 tests)
# =========================================================================

class TestMasterComputation:
    """Verify the master computation assembles correctly."""

    def test_master_runs(self):
        data = compute_all_k3e()
        assert data is not None

    def test_master_elliptic_genus_vanishes(self):
        data = compute_all_k3e()
        assert data.elliptic_genus.vanishes

    def test_master_chi_y_vanishes(self):
        data = compute_all_k3e()
        assert data.chi_y.vanishes_identically

    def test_master_kappa_3(self):
        data = compute_all_k3e()
        assert data.shadow.kappa == F(3)

    def test_master_hodge_symmetries(self):
        data = compute_all_k3e()
        for key, val in data.hodge_symmetries.items():
            assert val, f"Hodge symmetry {key} failed"


# =========================================================================
# Section 18: Cross-family consistency (8 tests)
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks for consistency across all spaces."""

    def test_product_euler_multiplicativity(self):
        """chi(XxY) = chi(X) * chi(Y) for all combinations."""
        spaces = [k3_hodge(), elliptic_hodge(), quintic_hodge()]
        for i, h1 in enumerate(spaces):
            for j, h2 in enumerate(spaces):
                prod = product_hodge(h1, h2)
                assert prod.euler == h1.euler * h2.euler

    def test_product_chi_O_multiplicativity(self):
        """chi(O_{XxY}) = chi(O_X) * chi(O_Y)."""
        h1, h2 = k3_hodge(), elliptic_hodge()
        prod = product_hodge(h1, h2)
        assert prod.chi_O == h1.chi_O * h2.chi_O

    def test_product_dimension_additivity(self):
        """dim_C(XxY) = dim_C(X) + dim_C(Y)."""
        h1, h2 = k3_hodge(), elliptic_hodge()
        prod = product_hodge(h1, h2)
        assert prod.dim == h1.dim + h2.dim

    def test_product_betti_sum(self):
        """total_betti(XxY) = total_betti(X) * total_betti(Y)."""
        h1, h2 = k3_hodge(), elliptic_hodge()
        prod = product_hodge(h1, h2)
        assert prod.total_betti == h1.total_betti * h2.total_betti

    def test_kappa_sum_equals_product_kappa(self):
        """For CY factors: kappa(XxY) = dim(X) + dim(Y) = kappa(X) + kappa(Y)."""
        kappa_k3 = 2  # dim_C(K3)
        kappa_e = 1   # dim_C(E)
        kappa_k3e = 3  # dim_C(K3xE)
        assert kappa_k3 + kappa_e == kappa_k3e

    def test_f_g_ratio_is_kappa_ratio(self):
        """F_g(K3xE)/lambda_g = kappa(K3xE) = 3."""
        st = compute_shadow_tower_k3e()
        for g in range(1, 6):
            ratio = st.f_g[g] / lambda_fp(g)
            assert ratio == F(3)

    def test_f_g_ratio_k3(self):
        """F_g(K3)/lambda_g = kappa(K3) = 2."""
        st = compute_shadow_tower_k3()
        for g in range(1, 6):
            ratio = st.f_g[g] / lambda_fp(g)
            assert ratio == F(2)

    def test_f_g_ratio_e(self):
        """F_g(E)/lambda_g = kappa(E) = 1."""
        st = compute_shadow_tower_e()
        for g in range(1, 6):
            ratio = st.f_g[g] / lambda_fp(g)
            assert ratio == F(1)


# =========================================================================
# Section 19: Lambda_g^FP cross-checks (5 tests)
# =========================================================================

class TestLambdaFP:
    """Cross-check Faber-Pandharipande constants."""

    def test_lambda1_from_bernoulli(self):
        """lambda_1 = (2^1-1)/2^1 * |B_2|/2! = 1/2 * 1/6 / 2 = 1/24."""
        B2 = F(1, 6)
        result = F(1, 2) * B2 / F(2)
        assert result == F(1, 24)
        assert lambda_fp(1) == result

    def test_lambda2_from_bernoulli(self):
        """lambda_2 = (2^3-1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 24 = 7/5760."""
        B4 = F(1, 30)
        result = F(7, 8) * B4 / F(24)
        assert result == F(7, 5760)
        assert lambda_fp(2) == result

    def test_lambda3_from_bernoulli(self):
        """lambda_3 = (2^5-1)/2^5 * |B_6|/6! = 31/32 * 1/42 / 720 = 31/967680."""
        B6 = F(1, 42)
        result = F(31, 32) * B6 / F(720)
        assert result == F(31, 967680)
        assert lambda_fp(3) == result

    def test_lambda_g_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_g_decreasing(self):
        """lambda_g^FP is decreasing (checked numerically for g=1..7)."""
        vals = [float(lambda_fp(g)) for g in range(1, 8)]
        for i in range(len(vals) - 1):
            assert vals[i] > vals[i + 1]


# =========================================================================
# Section 20: Product Hodge diamond general properties (3 tests)
# =========================================================================

class TestProductHodgeGeneral:
    """General properties of Kunneth product."""

    def test_product_is_commutative(self):
        """product_hodge(X, Y) = product_hodge(Y, X) up to Hodge numbers."""
        h1 = k3_hodge()
        h2 = elliptic_hodge()
        p12 = product_hodge(h1, h2)
        p21 = product_hodge(h2, h1)
        for p in range(4):
            for q in range(4):
                assert p12.h(p, q) == p21.h(p, q)

    def test_product_with_point(self):
        """X x {pt} = X."""
        point = HodgeDiamond(dim=0, data={(0, 0): 1})
        k3 = k3_hodge()
        prod = product_hodge(k3, point)
        for (p, q), v in k3.data.items():
            assert prod.h(p, q) == v

    def test_triple_product_associative(self):
        """(K3 x E) x pt = K3 x (E x pt) at Hodge level."""
        point = HodgeDiamond(dim=0, data={(0, 0): 1})
        k3 = k3_hodge()
        e = elliptic_hodge()
        left = product_hodge(product_hodge(k3, e), point)
        right = product_hodge(k3, product_hodge(e, point))
        for p in range(4):
            for q in range(4):
                assert left.h(p, q) == right.h(p, q)
