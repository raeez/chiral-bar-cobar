r"""Tests for CY-6: Cech descent spectral sequence for dg categories over K3.

Multi-path verification mandate: every numerical result verified by 3+ paths.

The engine computes:
  1. Cech nerve of a K3 cover (2-set cover by complement + tubular nbhd)
  2. Descent spectral sequence E_1, E_2 pages
  3. Gluing data as Hochschild class (obstruction in H^2(K3, O))
  4. K-theory descent (Mukai lattice rank 24)
  5. Stacky descent for Kummer K3 (BKR equivalence, 16 exceptional objects)

Verification paths:
  (a) Spectral sequence computation (E_1 -> E_2 -> HH^*(K3))
  (b) K-theory rank checks (Mukai lattice, Kunneth, localization)
  (c) HKR decomposition comparison (Hodge diamond -> HH^*)
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.cy_cech_descent_engine import (
    # K3 topological data
    K3_HODGE,
    K3_DIM_COMPLEX,
    K3_DIM_REAL,
    K3_EULER_CHAR,
    K3_BETTI,
    K3_SIGNATURE,
    K3_MUKAI_RANK,
    k3_hodge_number,
    k3_betti_number,
    k3_euler_from_hodge,
    k3_signature_from_hodge,
    # HKR
    hkr_decomposition_smooth,
    hkr_k3,
    hkr_total_dim,
    hkr_euler_char,
    # Open subvarieties
    hodge_numbers_curve,
    divisor_genus_in_linear_system,
    hh_complement_divisor,
    hh_tubular_neighborhood,
    hh_punctured_normal_bundle,
    # Cech descent SS
    CechDescentSS,
    # K-theory
    k0_k3,
    k0_curve,
    k0_elliptic_curve,
    k0_product,
    k0_cstar,
    k1_cstar,
    k_theory_localization_sequence,
    k_theory_descent_verification,
    k0_k3_times_elliptic,
    # Kummer
    KummerDescent,
    # Gluing
    atiyah_class_contribution,
    trivial_gluing_class,
    brauer_obstruction_dim,
    # Verification
    verify_hh_k3_three_paths,
    verify_descent_ss_convergence,
    verify_kummer_descent,
    # General covers
    cech_ss_n_set_cover,
    euler_char_from_ss,
    # Divisor data
    divisor_self_intersection,
    divisor_genus_adjunction,
    normal_bundle_degree,
    # Summary
    full_descent_summary,
)


# =========================================================================
# Section 1: K3 topological invariants
# =========================================================================

class TestK3TopologicalData:
    """Verify K3 surface topological invariants by multiple paths."""

    def test_euler_characteristic_value(self):
        """chi(K3) = 24."""
        assert K3_EULER_CHAR == 24

    def test_euler_from_hodge(self):
        """chi = sum (-1)^{p+q} h^{p,q} = 24."""
        assert k3_euler_from_hodge() == 24

    def test_euler_from_betti(self):
        """chi = sum (-1)^k b_k = 1 - 0 + 22 - 0 + 1 = 24."""
        chi = sum((-1)**k * K3_BETTI[k] for k in range(5))
        assert chi == 24

    def test_euler_three_paths_agree(self):
        """All three Euler characteristic computations agree."""
        path1 = K3_EULER_CHAR
        path2 = k3_euler_from_hodge()
        path3 = sum((-1)**k * K3_BETTI[k] for k in range(5))
        assert path1 == path2 == path3 == 24

    def test_betti_numbers(self):
        """b_0=1, b_1=0, b_2=22, b_3=0, b_4=1."""
        assert K3_BETTI == [1, 0, 22, 0, 1]

    def test_betti_sum_equals_euler_unsigned(self):
        """sum b_k = 24 for K3 (all signs positive by accident)."""
        assert sum(K3_BETTI) == 24

    def test_signature(self):
        """sigma(K3) = -16."""
        assert K3_SIGNATURE == -16

    def test_signature_from_hodge(self):
        """sigma = b_2^+ - b_2^- = 3 - 19 = -16."""
        assert k3_signature_from_hodge() == -16

    def test_complex_dimension(self):
        """K3 is a complex surface (dim_C = 2)."""
        assert K3_DIM_COMPLEX == 2

    def test_real_dimension(self):
        """K3 has real dimension 4."""
        assert K3_DIM_REAL == 4

    def test_mukai_rank(self):
        """Mukai lattice rank = 1 + 22 + 1 = 24."""
        assert K3_MUKAI_RANK == 24

    def test_mukai_rank_from_betti(self):
        """Mukai rank = sum of even Betti numbers."""
        rk = sum(K3_BETTI[i] for i in range(0, 5, 2))
        assert rk == 24

    def test_hodge_diamond_symmetry(self):
        """h^{p,q} = h^{q,p} (complex conjugation)."""
        for (p, q), h in K3_HODGE.items():
            if (q, p) in K3_HODGE:
                assert K3_HODGE[(q, p)] == h, f"h^{{{q},{p}}} != h^{{{p},{q}}}"

    def test_hodge_diamond_serre_duality(self):
        """h^{p,q} = h^{d-p,d-q} for d=2 (Serre duality on K3)."""
        d = K3_DIM_COMPLEX
        for (p, q), h in K3_HODGE.items():
            dual = (d - p, d - q)
            if dual in K3_HODGE:
                assert K3_HODGE[dual] == h, f"Serre duality fails at ({p},{q})"

    def test_h20_equals_1(self):
        """h^{2,0}(K3) = 1 (holomorphic 2-form exists and is unique)."""
        assert K3_HODGE[(2, 0)] == 1

    def test_h11_equals_20(self):
        """h^{1,1}(K3) = 20."""
        assert K3_HODGE[(1, 1)] == 20

    def test_b1_vanishes(self):
        """b_1(K3) = 0 (K3 is simply connected)."""
        assert K3_BETTI[1] == 0

    def test_hodge_number_accessor(self):
        """k3_hodge_number(p,q) returns correct values."""
        assert k3_hodge_number(0, 0) == 1
        assert k3_hodge_number(2, 0) == 1
        assert k3_hodge_number(1, 1) == 20
        assert k3_hodge_number(1, 0) == 0
        assert k3_hodge_number(3, 0) == 0  # out of range

    def test_betti_number_accessor(self):
        """k3_betti_number(k) returns correct values."""
        assert k3_betti_number(0) == 1
        assert k3_betti_number(2) == 22
        assert k3_betti_number(5) == 0  # out of range

    def test_noether_formula(self):
        """Noether formula: chi(O_K3) = (c_1^2 + c_2)/12 = (0+24)/12 = 2.
        Also: chi(O) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2."""
        chi_O = K3_HODGE[(0, 0)] - K3_HODGE.get((0, 1), 0) + K3_HODGE[(0, 2)]
        assert chi_O == 2
        # Noether: (c_1^2 + chi)/12 = (0 + 24)/12 = 2
        assert (0 + K3_EULER_CHAR) // 12 == 2

    def test_hirzebruch_signature_formula(self):
        """Hirzebruch: sigma = (1/3)(c_1^2 - 2c_2) = (0 - 48)/3 = -16."""
        sigma = (0 - 2 * K3_EULER_CHAR) // 3
        assert sigma == K3_SIGNATURE


# =========================================================================
# Section 2: HKR decomposition
# =========================================================================

class TestHKR:
    """Verify Hochschild-Kostant-Rosenberg decomposition for K3."""

    def test_hkr_k3_dimensions(self):
        """HH^n(K3): n=-2: 1, n=-1: 0, n=0: 22, n=1: 0, n=2: 1."""
        hh = hkr_k3()
        assert hh.get(-2, 0) == 1
        assert hh.get(-1, 0) == 0
        assert hh.get(0, 0) == 22
        assert hh.get(1, 0) == 0
        assert hh.get(2, 0) == 1

    def test_hkr_total_equals_24(self):
        """sum dim HH^n(K3) = 24 = Mukai rank."""
        hh = hkr_k3()
        assert hkr_total_dim(hh) == 24

    def test_hkr_total_equals_mukai(self):
        """Total HH^* dimension = Mukai lattice rank (for CY)."""
        assert hkr_total_dim(hkr_k3()) == K3_MUKAI_RANK

    def test_hkr_euler_char(self):
        """chi(HH^*) = sum (-1)^n dim HH^n = 1 - 0 + 22 - 0 + 1 = 24."""
        hh = hkr_k3()
        chi = hkr_euler_char(hh)
        # Note: for K3 all HH contributions have even degree shifts,
        # so chi = 24 = total dim (no cancellation because odd HH vanish).
        assert chi == 24

    def test_hh0_is_deformation_space(self):
        """HH^0(K3) = 22 counts algebraic + complex deformations.

        HH^0 = H^0(O) + H^1(Omega^1) + H^2(Omega^2) = 1 + 20 + 1 = 22.
        The H^1(Omega^1) = H^1(T) part (20 dims) is the
        Kodaira-Spencer deformation space.
        """
        hh = hkr_k3()
        assert hh[0] == 22
        # Breakdown
        assert K3_HODGE[(0, 0)] + K3_HODGE[(1, 1)] + K3_HODGE[(2, 2)] == 22

    def test_hh2_is_h20(self):
        """HH^2(K3) = H^0(Omega^2) = h^{2,0} = 1 (the holomorphic 2-form)."""
        hh = hkr_k3()
        assert hh[2] == K3_HODGE[(2, 0)]

    def test_hh_minus2_is_h02(self):
        """HH^{-2}(K3) = H^2(O) = h^{0,2} = 1."""
        hh = hkr_k3()
        assert hh[-2] == K3_HODGE[(0, 2)]

    def test_hkr_odd_vanish(self):
        """HH^{odd}(K3) = 0 because b_1(K3) = b_3(K3) = 0."""
        hh = hkr_k3()
        assert hh.get(-1, 0) == 0
        assert hh.get(1, 0) == 0

    def test_hkr_serre_symmetry(self):
        """HH^n(K3) = HH^{-n}(K3) (Serre duality for CY surfaces)."""
        hh = hkr_k3()
        for n in range(-2, 3):
            assert hh.get(n, 0) == hh.get(-n, 0)

    def test_hkr_curve_genus_2(self):
        """HH^*(genus-2 curve): HH^{-1}=2, HH^0=2, HH^1=2."""
        hodge = hodge_numbers_curve(2)
        hh = hkr_decomposition_smooth(hodge, 1)
        assert hh.get(-1, 0) == 2
        assert hh.get(0, 0) == 2
        assert hh.get(1, 0) == 2

    def test_hkr_elliptic_curve(self):
        """HH^*(E): HH^{-1}=1, HH^0=2, HH^1=1."""
        hodge = hodge_numbers_curve(1)
        hh = hkr_decomposition_smooth(hodge, 1)
        assert hh.get(-1, 0) == 1
        assert hh.get(0, 0) == 2
        assert hh.get(1, 0) == 1

    def test_hkr_point(self):
        """HH^*(pt) = C in degree 0."""
        hodge = {(0, 0): 1}
        hh = hkr_decomposition_smooth(hodge, 0)
        assert hh == {0: 1}


# =========================================================================
# Section 3: Open subvarieties HH^*
# =========================================================================

class TestOpenSubvarieties:
    """Test HH^* computations for pieces of the cover."""

    def test_tubular_genus2(self):
        """HH^*(U_1) for D of genus 2: HH^{-1}=2, HH^0=2, HH^1=2."""
        hh = hh_tubular_neighborhood(2)
        assert hh[-1] == 2
        assert hh[0] == 2
        assert hh[1] == 2

    def test_tubular_genus1(self):
        """HH^*(tubular nbhd of E) = HH^*(E)."""
        hh = hh_tubular_neighborhood(1)
        assert hh[-1] == 1
        assert hh[0] == 2
        assert hh[1] == 1

    def test_punctured_genus2(self):
        """HH^*(D x C^*) for genus-2 D via Kunneth.

        HH^n(D x C^*) = HH^n(D) + HH^{n-1}(D):
          n=-2: HH^{-2}(D) + HH^{-3}(D) = 0 + 0 = 0
                (but HH^{-2}(D_genus2) needs checking: for dim 1, HKR gives
                 n range [-1, 1], so HH^{-2}(D) = 0.)
          n=-1: HH^{-1}(D) + HH^{-2}(D) = 2 + 0 = 2
          n=0: HH^0(D) + HH^{-1}(D) = 2 + 2 = 4
          n=1: HH^1(D) + HH^0(D) = 2 + 2 = 4
          n=2: HH^2(D) + HH^1(D) = 0 + 2 = 2
        """
        hh = hh_punctured_normal_bundle(2)
        assert hh.get(-2, 0) == 0
        assert hh.get(-1, 0) == 2
        assert hh.get(0, 0) == 4
        assert hh.get(1, 0) == 4
        assert hh.get(2, 0) == 2

    def test_punctured_total_dim(self):
        """Total dim HH^*(D x C^*) for genus-2 D."""
        hh = hh_punctured_normal_bundle(2)
        total = sum(hh.values())
        # 2 + 4 + 4 + 2 = 12
        assert total == 12

    def test_complement_divisor_k3(self):
        """HH^*(K3 \\ D) has contributions from localization."""
        hh = hh_complement_divisor(K3_HODGE, 2)
        # Should have entries at degrees -2, -1, 0, 1, 2
        assert isinstance(hh, dict)
        # Total should be finite
        assert sum(hh.values()) < 100

    def test_curve_hodge_numbers(self):
        """Hodge numbers of genus-g curve."""
        h = hodge_numbers_curve(3)
        assert h[(0, 0)] == 1
        assert h[(1, 0)] == 3
        assert h[(0, 1)] == 3
        assert h[(1, 1)] == 1

    def test_curve_euler(self):
        """chi(genus-g curve) = 2 - 2g."""
        for g in range(5):
            h = hodge_numbers_curve(g)
            chi = sum((-1)**(p+q) * v for (p, q), v in h.items())
            assert chi == 2 - 2*g


# =========================================================================
# Section 4: Cech descent spectral sequence
# =========================================================================

class TestCechDescentSS:
    """Test the descent spectral sequence for dg categories on K3."""

    def test_e1_page_exists(self):
        """E_1 page is nonempty."""
        ss = CechDescentSS(divisor_genus=2)
        e1 = ss.e1_page()
        assert len(e1) > 0

    def test_e1_only_p01(self):
        """For 2-set cover, E_1 has p in {0, 1} only."""
        ss = CechDescentSS(divisor_genus=2)
        e1 = ss.e1_page()
        for (p, q) in e1:
            assert p in (0, 1), f"Unexpected p={p} in E_1 page"

    def test_e2_page_exists(self):
        """E_2 page is computed."""
        ss = CechDescentSS(divisor_genus=2)
        e2 = ss.e2_page()
        assert len(e2) > 0

    def test_e2_equals_einfty(self):
        """For 2-set cover, E_2 = E_infty (no further differentials)."""
        ss = CechDescentSS(divisor_genus=2)
        e2 = ss.e2_page()
        # Verify by checking convergence to HH^*(K3)
        assert ss.verify_convergence()

    def test_convergence_genus2(self):
        """SS converges to HH^*(K3) for genus-2 divisor."""
        ss = CechDescentSS(divisor_genus=2)
        assert ss.verify_convergence()

    def test_convergence_genus5(self):
        """SS converges to HH^*(K3) for genus-5 divisor (d=2)."""
        ss = CechDescentSS(divisor_genus=5)
        assert ss.verify_convergence()

    def test_convergence_genus10(self):
        """SS converges to HH^*(K3) for genus-10 divisor (d=3)."""
        ss = CechDescentSS(divisor_genus=10)
        assert ss.verify_convergence()

    def test_e2_total_equals_24(self):
        """Total dim of E_2 page = dim HH^*(K3) = 24."""
        ss = CechDescentSS(divisor_genus=2)
        e2 = ss.e2_page()
        total = sum(e2.values())
        assert total == 24

    def test_e1_total_geq_24(self):
        """Total dim of E_1 >= dim HH^*(K3) (d_1 can only decrease)."""
        ss = CechDescentSS(divisor_genus=2)
        e1 = ss.e1_page()
        assert sum(e1.values()) >= 24

    def test_d1_ranks_nonneg(self):
        """All d_1 ranks are non-negative."""
        ss = CechDescentSS(divisor_genus=2)
        ranks = ss.d1_ranks()
        for q, r in ranks.items():
            assert r >= 0, f"Negative rank at q={q}"

    def test_d1_rank_bounded_by_source(self):
        """rank(d_1^q) <= dim E_1^{0,q}."""
        ss = CechDescentSS(divisor_genus=2)
        e1 = ss.e1_page()
        ranks = ss.d1_ranks()
        for q, r in ranks.items():
            src = e1.get((0, q), 0)
            assert r <= src, f"rank exceeds source at q={q}"

    def test_d1_rank_bounded_by_target(self):
        """rank(d_1^q) <= dim E_1^{1,q}."""
        ss = CechDescentSS(divisor_genus=2)
        e1 = ss.e1_page()
        ranks = ss.d1_ranks()
        for q, r in ranks.items():
            tgt = e1.get((1, q), 0)
            assert r <= tgt, f"rank exceeds target at q={q}"

    def test_obstruction_space_dim1(self):
        """Obstruction to descent lives in H^2(K3, O) = C (dim 1)."""
        ss = CechDescentSS(divisor_genus=2)
        assert ss.obstruction_space() == 1

    def test_euler_char_preserved(self):
        """Euler char of E_1 = Euler char of E_2 = chi(HH^*(K3))."""
        result = verify_descent_ss_convergence(divisor_genus=2)
        assert result['chi_match']

    def test_different_genera_all_converge(self):
        """Convergence holds for multiple divisor genera."""
        for g in [2, 3, 5, 10]:
            ss = CechDescentSS(divisor_genus=g)
            assert ss.verify_convergence(), f"Failed for genus {g}"


# =========================================================================
# Section 5: K-theory descent
# =========================================================================

class TestKTheoryDescent:
    """Test K-theory descent for K3."""

    def test_k0_k3_equals_24(self):
        """rk K_0(K3) = 24 (Mukai lattice)."""
        assert k0_k3() == 24

    def test_k0_k3_three_paths(self):
        """K_0(K3) rank verified by three paths."""
        result = k_theory_descent_verification()
        assert result['all_agree']
        assert result['rank'] == 24

    def test_k0_curve_rank_2(self):
        """rk K_0(C) = 2 for any smooth curve."""
        for g in range(5):
            assert k0_curve(g) == 2

    def test_k0_elliptic_rank_2(self):
        """rk K_0(E) = 2."""
        assert k0_elliptic_curve() == 2

    def test_k0_cstar_rank_1(self):
        """rk K_0(C^*) = 1."""
        assert k0_cstar() == 1

    def test_k1_cstar_rank_1(self):
        """rk K_1(C^*) = 1."""
        assert k1_cstar() == 1

    def test_k0_product_kunneth(self):
        """K_0(X x Y) = K_0(X) tensor K_0(Y): ranks multiply."""
        assert k0_product(24, 2) == 48
        assert k0_product(2, 2) == 4
        assert k0_product(1, 24) == 24

    def test_k0_k3_times_elliptic(self):
        """rk K_0(K3 x E) = 24 * 2 = 48."""
        result = k0_k3_times_elliptic()
        assert result['rk_K0_product'] == 48
        assert result['agree']

    def test_k0_k3xe_cross_check(self):
        """K_0(K3 x E) rank agrees with cohomological computation."""
        result = k0_k3_times_elliptic()
        assert result['rk_K0_product'] == result['cross_check_cohomology']

    def test_localization_sequence_ranks(self):
        """Localization sequence has correct ranks."""
        loc = k_theory_localization_sequence(divisor_genus=2)
        assert loc['K0_K3'] == 24
        assert loc['K0_D'] == 2
        assert loc['K0_U01'] == 2
        assert loc['K1_U01'] == 2

    def test_k0_product_associativity(self):
        """Kunneth is associative: K_0(X x Y x Z) computed two ways."""
        rk_a = k0_product(k0_product(24, 2), 2)   # (K3 x E) x E
        rk_b = k0_product(24, k0_product(2, 2))   # K3 x (E x E)
        assert rk_a == rk_b == 96


# =========================================================================
# Section 6: Kummer surface descent
# =========================================================================

class TestKummerDescent:
    """Test stacky descent for Kummer K3."""

    def test_fixed_point_count(self):
        """Z/2 on E x E has 16 fixed points."""
        kd = KummerDescent()
        assert kd.fixed_point_count() == 16

    def test_exceptional_curves_count(self):
        """16 exceptional (-2)-curves in the resolution."""
        kd = KummerDescent()
        assert kd.exceptional_curves_count() == 16

    def test_kummer_lattice_rank(self):
        """Kummer lattice has rank 16."""
        kd = KummerDescent()
        assert kd.kummer_lattice_rank() == 16

    def test_kummer_picard_number(self):
        """Picard number of generic Kummer surface is 19."""
        kd = KummerDescent()
        rho = kd.picard_number()
        assert rho == 19
        # Picard number of K3 must satisfy 1 <= rho <= 20
        assert 1 <= rho <= 20

    def test_kummer_hodge_numbers(self):
        """Kummer surface has standard K3 Hodge numbers."""
        kd = KummerDescent()
        h = kd.hodge_numbers_kummer()
        assert h[(0, 0)] == 1
        assert h[(2, 0)] == 1
        assert h[(1, 1)] == 20
        assert h[(0, 2)] == 1
        assert h[(2, 2)] == 1

    def test_equivariant_k0_rank(self):
        """K_0^{Z/2}(E x E) = K_0(Kum) has rank 24."""
        kd = KummerDescent()
        assert kd.equivariant_k0_rank() == 24

    def test_bkr_decomposition_total(self):
        """BKR decomposition: 4 + 4 + 16 = 24."""
        kd = KummerDescent()
        bkr = kd.bkr_decomposition()
        assert bkr['total_rank'] == 24
        assert bkr['matches_mukai']

    def test_bkr_free_invariant(self):
        """Free invariant sector has rank 4."""
        kd = KummerDescent()
        bkr = kd.bkr_decomposition()
        assert bkr['free_invariant_rank'] == 4

    def test_bkr_twisted_sector(self):
        """Twisted sector has rank 16 (from fixed points)."""
        kd = KummerDescent()
        bkr = kd.bkr_decomposition()
        assert bkr['twisted_sector_rank'] == 16

    def test_bkr_sign_sector(self):
        """Sign representation sector has rank 4."""
        kd = KummerDescent()
        bkr = kd.bkr_decomposition()
        assert bkr['free_sign_rank'] == 4

    def test_exceptional_objects_count(self):
        """16 exceptional objects in D^b(Kum)."""
        kd = KummerDescent()
        objs = kd.exceptional_object_classes()
        assert len(objs) == 16

    def test_exceptional_objects_rank_zero(self):
        """Exceptional objects have rank 0 (torsion sheaves)."""
        kd = KummerDescent()
        objs = kd.exceptional_object_classes()
        for obj in objs:
            assert obj['rank'] == 0

    def test_exceptional_objects_minus2(self):
        """Exceptional objects have Mukai vector squared = -2."""
        kd = KummerDescent()
        objs = kd.exceptional_object_classes()
        for obj in objs:
            assert obj['mukai_vector_squared'] == -2

    def test_verify_kummer_three_paths(self):
        """Kummer descent verified by three independent paths."""
        result = verify_kummer_descent()
        assert result['all_agree']


# =========================================================================
# Section 7: Gluing and obstruction
# =========================================================================

class TestGluingObstruction:
    """Test gluing data and Brauer obstruction."""

    def test_trivial_gluing(self):
        """Trivial gluing has alpha = 0."""
        assert trivial_gluing_class() == 0

    def test_brauer_obstruction_dim(self):
        """Brauer obstruction space has dim 1 for K3."""
        assert brauer_obstruction_dim() == 1

    def test_atiyah_class_dim(self):
        """Atiyah class space has dim 20 for K3."""
        dim = atiyah_class_contribution(K3_HODGE)
        assert dim == 20

    def test_obstruction_equals_h02(self):
        """Obstruction space = H^2(K3, O) = h^{0,2} = 1."""
        ss = CechDescentSS(divisor_genus=2)
        assert ss.obstruction_space() == K3_HODGE[(0, 2)]

    def test_gluing_moduli_is_finite(self):
        """Gluing moduli dimension is finite and non-negative."""
        ss = CechDescentSS(divisor_genus=2)
        dim = ss.gluing_moduli_dim()
        assert dim >= 0
        assert dim < 100


# =========================================================================
# Section 8: Divisor geometry
# =========================================================================

class TestDivisorGeometry:
    """Test divisor data on K3."""

    def test_divisor_genus_d1(self):
        """D in |H| on degree-2 K3: genus = 2."""
        assert divisor_genus_adjunction(1) == 2

    def test_divisor_genus_d2(self):
        """D in |2H| on degree-2 K3: genus = 5."""
        assert divisor_genus_adjunction(2) == 5

    def test_divisor_genus_d3(self):
        """D in |3H| on degree-2 K3: genus = 10."""
        assert divisor_genus_adjunction(3) == 10

    def test_self_intersection_d1(self):
        """D^2 = 2 for D in |H| with H^2 = 2."""
        assert divisor_self_intersection(1) == 2

    def test_self_intersection_d2(self):
        """D^2 = 8 for D in |2H| with H^2 = 2."""
        assert divisor_self_intersection(2) == 8

    def test_adjunction_formula(self):
        """2g - 2 = D^2 (adjunction on K3 with K = 0)."""
        for d in range(1, 6):
            g = divisor_genus_adjunction(d)
            d_sq = divisor_self_intersection(d)
            assert 2*g - 2 == d_sq

    def test_normal_bundle_equals_self_intersection(self):
        """deg(N_{D/K3}) = D^2."""
        for d in range(1, 6):
            assert normal_bundle_degree(d) == divisor_self_intersection(d)

    def test_genus_increases_with_degree(self):
        """Genus increases quadratically with degree."""
        genera = [divisor_genus_adjunction(d) for d in range(1, 6)]
        for i in range(len(genera) - 1):
            assert genera[i] < genera[i + 1]


# =========================================================================
# Section 9: Multi-path verifications
# =========================================================================

class TestMultiPathVerification:
    """Cross-verification using multiple independent paths."""

    def test_hh_k3_three_paths(self):
        """HH^*(K3) verified by three independent paths."""
        result = verify_hh_k3_three_paths()
        assert result['all_agree']
        assert result['path1_total'] == 24
        assert result['path2_total'] == 24
        assert result['path3_mukai'] == 24

    def test_descent_ss_three_paths(self):
        """Descent SS convergence verified by three paths."""
        result = verify_descent_ss_convergence(divisor_genus=2)
        assert result['converges']
        assert result['total_e2'] == 24
        assert result['chi_match']

    def test_k_theory_three_paths(self):
        """K-theory rank verified by three paths."""
        result = k_theory_descent_verification()
        assert result['mukai_lattice_rank'] == 24
        assert result['hodge_rank'] == 24
        assert result['chern_character_rank'] == 24
        assert result['all_agree']

    def test_kummer_three_paths(self):
        """Kummer descent verified by three paths."""
        result = verify_kummer_descent()
        assert result['all_agree']

    def test_total_dim_consistency(self):
        """All computations of total dimension agree: HH, K_0, Mukai."""
        dim_hh = hkr_total_dim(hkr_k3())
        dim_k0 = k0_k3()
        dim_mukai = K3_MUKAI_RANK
        assert dim_hh == dim_k0 == dim_mukai == 24

    def test_euler_char_multiple_paths(self):
        """chi(K3) computed by 4 independent paths."""
        # Path 1: Betti numbers
        p1 = sum((-1)**k * K3_BETTI[k] for k in range(5))
        # Path 2: Hodge numbers
        p2 = k3_euler_from_hodge()
        # Path 3: Constant
        p3 = K3_EULER_CHAR
        # Path 4: Noether + c_2
        p4 = 12 * (K3_HODGE[(0, 0)] - K3_HODGE.get((0, 1), 0) + K3_HODGE[(0, 2)])
        assert p1 == p2 == p3 == p4 == 24


# =========================================================================
# Section 10: General cover utilities
# =========================================================================

class TestGeneralCovers:
    """Test general Cech cover utilities."""

    def test_n_set_cover_single(self):
        """Single open set: E_1 = HH^*(U_0)."""
        hh = {0: 1, 1: 2}
        e1 = cech_ss_n_set_cover(1, [hh], {})
        assert e1[(0, 0)] == 1
        assert e1[(0, 1)] == 2

    def test_n_set_cover_two_sets(self):
        """Two open sets: p=0 gets both pieces, p=1 gets overlap."""
        hh0 = {0: 3}
        hh1 = {0: 2}
        hh01 = {0: 1}
        e1 = cech_ss_n_set_cover(2, [hh0, hh1], {(0, 1): hh01})
        assert e1[(0, 0)] == 5  # 3 + 2
        assert e1[(1, 0)] == 1

    def test_euler_char_from_ss_basic(self):
        """Euler char computation from E page."""
        e = {(0, 0): 2, (0, 1): 1, (1, 0): 1, (1, 1): 3}
        chi = euler_char_from_ss(e)
        # (0,0): +2, (0,1): -1, (1,0): -1, (1,1): +3 = 3
        assert chi == 3

    def test_euler_char_empty(self):
        """Empty page has chi = 0."""
        assert euler_char_from_ss({}) == 0


# =========================================================================
# Section 11: Full summary and integration
# =========================================================================

class TestFullSummary:
    """Integration tests for the full descent computation."""

    def test_summary_runs(self):
        """Full summary executes without error."""
        result = full_descent_summary(divisor_degree=1)
        assert 'K3_data' in result
        assert 'HKR' in result
        assert 'descent_SS' in result
        assert 'K_theory' in result
        assert 'Kummer' in result

    def test_summary_euler_char(self):
        """Summary reports correct Euler characteristic."""
        result = full_descent_summary(divisor_degree=1)
        assert result['K3_data']['euler_char'] == 24

    def test_summary_hkr_total(self):
        """Summary reports HH^* total = 24."""
        result = full_descent_summary(divisor_degree=1)
        assert result['HKR']['total_dim'] == 24

    def test_summary_ss_converges(self):
        """Summary reports convergence."""
        result = full_descent_summary(divisor_degree=1)
        assert result['descent_SS']['converges']

    def test_summary_k_theory(self):
        """Summary reports K_0 rank = 24."""
        result = full_descent_summary(divisor_degree=1)
        assert result['K_theory']['K0_K3'] == 24

    def test_summary_kummer(self):
        """Summary reports Kummer data correctly."""
        result = full_descent_summary(divisor_degree=1)
        assert result['Kummer']['fixed_points'] == 16
        assert result['Kummer']['exceptional_curves'] == 16
        assert result['Kummer']['equivariant_K0'] == 24

    def test_summary_cover_data(self):
        """Summary reports correct cover data for degree 1."""
        result = full_descent_summary(divisor_degree=1)
        cd = result['cover_data']
        assert cd['divisor_degree'] == 1
        assert cd['divisor_genus'] == 2
        assert cd['divisor_self_intersection'] == 2
        assert cd['normal_bundle_degree'] == 2

    def test_summary_degree_2(self):
        """Summary works for degree 2 polarization."""
        result = full_descent_summary(divisor_degree=2)
        cd = result['cover_data']
        assert cd['divisor_genus'] == 5
        assert cd['divisor_self_intersection'] == 8
        assert result['descent_SS']['converges']

    def test_summary_obstruction_dim(self):
        """Obstruction space has dim 1."""
        result = full_descent_summary(divisor_degree=1)
        assert result['descent_SS']['obstruction_dim'] == 1


# =========================================================================
# Section 12: Edge cases and consistency
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_genus0_curve_hodge(self):
        """Genus 0 curve (P^1): h^{0,0}=1, h^{1,0}=0, h^{0,1}=0, h^{1,1}=1."""
        h = hodge_numbers_curve(0)
        assert h[(0, 0)] == 1
        assert h[(1, 0)] == 0
        assert h[(0, 1)] == 0
        assert h[(1, 1)] == 1

    def test_genus0_tubular(self):
        """Tubular neighborhood of P^1: HH^{-1}=0, HH^0=2, HH^1=0."""
        hh = hh_tubular_neighborhood(0)
        assert hh[-1] == 0
        assert hh[0] == 2
        assert hh[1] == 0

    def test_large_genus_convergence(self):
        """SS converges even for large genus divisors."""
        ss = CechDescentSS(divisor_genus=50)
        assert ss.verify_convergence()

    def test_kummer_lattice_inside_picard(self):
        """Kummer lattice (rank 16) sits inside Picard lattice (rank 19)."""
        kd = KummerDescent()
        assert kd.kummer_lattice_rank() < kd.picard_number() + 1

    def test_picard_bounded(self):
        """Picard number of K3 satisfies 1 <= rho <= 20."""
        kd = KummerDescent()
        rho = kd.picard_number()
        assert 1 <= rho <= 20

    def test_k0_product_commutative(self):
        """K_0(X x Y) = K_0(Y x X) (Kunneth is commutative)."""
        assert k0_product(24, 2) == k0_product(2, 24)

    def test_hkr_respects_dimension(self):
        """HH^n = 0 for |n| > dim for smooth proper varieties."""
        hh = hkr_k3()
        for n, d in hh.items():
            assert abs(n) <= K3_DIM_COMPLEX, f"HH^{n} nonzero beyond dimension"

    def test_betti_poincare_duality(self):
        """b_k = b_{4-k} (Poincare duality for K3)."""
        for k in range(5):
            assert K3_BETTI[k] == K3_BETTI[4 - k]

    def test_b2_decomposition(self):
        """b_2 = h^{2,0} + h^{1,1} + h^{0,2} = 1 + 20 + 1 = 22."""
        b2 = K3_HODGE[(2, 0)] + K3_HODGE[(1, 1)] + K3_HODGE[(0, 2)]
        assert b2 == K3_BETTI[2]

    def test_transcendental_lattice_rank(self):
        """Transcendental lattice rank = 22 - rho."""
        kd = KummerDescent()
        rho = kd.picard_number()
        trans_rank = 22 - rho
        assert trans_rank == 3  # For Kummer with rho=19

    def test_k3_simply_connected(self):
        """K3 is simply connected: b_1 = 0, hence pi_1 = 0."""
        assert K3_BETTI[1] == 0

    def test_k3_spin(self):
        """K3 is spin: w_2 = 0 (since c_1 = 0 implies w_2 = c_1 mod 2 = 0).
        Consequence: signature divisible by 8 (Rokhlin theorem for spin 4-manifold
        actually requires sigma divisible by 16)."""
        assert K3_SIGNATURE % 16 == 0


# =========================================================================
# Section 13: Spectral sequence structural properties
# =========================================================================

class TestSSStructure:
    """Structural properties of the descent spectral sequence."""

    def test_e1_dimensions_nonneg(self):
        """All E_1 dimensions are non-negative."""
        ss = CechDescentSS(divisor_genus=2)
        for (p, q), d in ss.e1_page().items():
            assert d >= 0

    def test_e2_dimensions_nonneg(self):
        """All E_2 dimensions are non-negative."""
        ss = CechDescentSS(divisor_genus=2)
        for (p, q), d in ss.e2_page().items():
            assert d >= 0

    def test_e2_leq_e1(self):
        """dim E_2^{p,q} <= dim E_1^{p,q} (differentials can only kill)."""
        ss = CechDescentSS(divisor_genus=2)
        e1 = ss.e1_page()
        e2 = ss.e2_page()
        for (p, q), d2 in e2.items():
            d1 = e1.get((p, q), 0)
            assert d2 <= d1, f"E_2 > E_1 at ({p},{q})"

    def test_ss_functorial_in_genus(self):
        """E_2 page is independent of divisor genus (target is always K3).

        The E_2 = E_infty page converges to HH^*(K3) regardless of
        which cover we use. The E_1 page changes, but E_2 must give
        the same answer.
        """
        for g in [2, 5, 10]:
            ss = CechDescentSS(divisor_genus=g)
            e2 = ss.e2_page()
            total = sum(e2.values())
            assert total == 24, f"Failed for genus {g}"

    def test_chi_invariance_under_d1(self):
        """Euler char is preserved by d_1: chi(E_1) = chi(E_2)."""
        ss = CechDescentSS(divisor_genus=2)
        e1 = ss.e1_page()
        e2 = ss.e2_page()
        chi_e1 = sum((-1)**(p+q) * d for (p, q), d in e1.items())
        chi_e2 = sum((-1)**(p+q) * d for (p, q), d in e2.items())
        assert chi_e1 == chi_e2
