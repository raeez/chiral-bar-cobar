r"""Tests for CY-24: Noncommutative deformations of D^b(K3 x E).

Multi-path verification mandate: every numerical result verified by 3+ paths.

The engine computes:
  1. HKR decomposition of HH^*(K3 x E) and other CY manifolds
  2. Deformation space analysis: complex structure, B-field, volume, NC
  3. Brauer group structure and transcendental lattice
  4. Poisson structures and deformation quantization
  5. Morita moduli and extended period domain
  6. A-infinity deformation of endomorphism algebras
  7. Chiral Hochschild comparison (Costello-Gwilliam)

Verification paths:
  (a) HKR dimension count (direct Hodge computation)
  (b) Kuenneth product cross-check (product vs factor HH)
  (c) CY Serre duality cross-check (HH^n = HH^{2d-n})
  (d) Euler characteristic multiplicativity
  (e) Brauer group decomposition consistency
  (f) Poisson dimension from Hodge data two ways
  (g) Chiral vs categorical comparison
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.cy_nc_deformation_k3e_engine import (
    # Hodge diamonds
    hodge_K3,
    hodge_elliptic,
    hodge_product,
    hodge_K3xE,
    hodge_torus,
    hodge_number,
    betti_from_hodge,
    euler_char,
    dimension_from_hodge,
    # HH via HKR
    hh_hkr_cy,
    hh_hkr_decomposition_cy,
    hh_kuenneth,
    # Deformation space
    DeformationSpace,
    deformation_space_K3xE,
    deformation_space_K3,
    deformation_space_elliptic,
    deformation_space_torus3,
    deformation_space_quintic,
    # Brauer group
    BrauerGroupData,
    brauer_K3,
    brauer_elliptic,
    brauer_K3xE,
    brauer_product_decomposition,
    # Poisson
    PoissonData,
    poisson_K3,
    poisson_elliptic,
    poisson_K3xE,
    poisson_torus3,
    star_product_order_n,
    # Morita moduli
    MoritaModuli,
    morita_moduli_K3,
    morita_moduli_K3xE,
    # A-infinity
    AinfDeformation,
    ainfty_deformation_K3xE,
    ainfty_deformation_K3,
    # Chiral comparison
    chiral_hochschild_dim_cy,
    chiral_comparison_K3xE,
    # Cross-checks
    verify_cy_serre_duality,
    verify_hodge_symmetry,
    verify_cy_condition,
    verify_kuenneth_euler,
    hh2_kuenneth_decomposition,
    hh2_kuenneth_total,
    total_hh_dim,
    hh_euler,
    verify_hh_euler_equals_chi_squared,
    nc_to_commutative_ratio,
    # Summaries
    full_nc_deformation_summary,
    summary_K3xE,
    summary_K3,
    summary_quintic,
    summary_T3,
)


# ================================================================
# SECTION 1: K3 SURFACE HODGE DATA
# ================================================================

class TestK3HodgeDiamond:
    """Verify K3 Hodge diamond from first principles."""

    def test_k3_hodge_numbers(self):
        """K3: h^{0,0}=h^{2,2}=1, h^{2,0}=h^{0,2}=1, h^{1,1}=20."""
        h = hodge_K3()
        assert h[(0, 0)] == 1
        assert h[(2, 0)] == 1
        assert h[(0, 2)] == 1
        assert h[(1, 1)] == 20
        assert h[(2, 2)] == 1
        # All h^{1,0} = h^{0,1} = 0 (simply connected)
        assert h[(1, 0)] == 0
        assert h[(0, 1)] == 0

    def test_k3_euler_characteristic(self):
        """chi(K3) = 24.

        Path (a): sum (-1)^k b_k = 1 - 0 + 22 - 0 + 1 = 24.
        Path (b): chi = 2 + 2*h^{1,1} - 4*h^{1,0} + 2*h^{2,0}
                      = 2 + 40 - 0 + 2 = ... NO, use Noether formula.
        Path (c): Noether formula: chi(O_K3) = (c_1^2 + c_2)/12.
                  For K3: c_1 = 0, c_2 = chi = 24. chi(O_K3) = 2.
                  sum h^{0,q}(-1)^q = 1 - 0 + 1 = 2. Check.
        """
        h = hodge_K3()
        assert euler_char(h) == 24

    def test_k3_betti_numbers(self):
        """K3 Betti numbers: b_0=b_4=1, b_1=b_3=0, b_2=22."""
        b = betti_from_hodge(hodge_K3())
        assert b[0] == 1
        assert b.get(1, 0) == 0
        assert b[2] == 22
        assert b.get(3, 0) == 0
        assert b[4] == 1

    def test_k3_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} for K3."""
        assert verify_hodge_symmetry(hodge_K3())

    def test_k3_cy_condition(self):
        """K3 has a unique holomorphic 2-form: h^{2,0} = 1."""
        assert verify_cy_condition(hodge_K3(), 2)

    def test_k3_dimension(self):
        """K3 has complex dimension 2."""
        assert dimension_from_hodge(hodge_K3()) == 2


class TestEllipticHodgeDiamond:
    """Verify elliptic curve Hodge data."""

    def test_elliptic_hodge_numbers(self):
        """E: h^{p,q} = 1 for all (p,q) with 0 <= p,q <= 1."""
        h = hodge_elliptic()
        assert h[(0, 0)] == 1
        assert h[(1, 0)] == 1
        assert h[(0, 1)] == 1
        assert h[(1, 1)] == 1

    def test_elliptic_euler(self):
        """chi(E) = 0. Genus-1 curve has vanishing Euler characteristic."""
        assert euler_char(hodge_elliptic()) == 0

    def test_elliptic_betti(self):
        """E: b_0 = b_2 = 1, b_1 = 2."""
        b = betti_from_hodge(hodge_elliptic())
        assert b[0] == 1
        assert b[1] == 2
        assert b[2] == 1

    def test_elliptic_cy_condition(self):
        """E has h^{1,0} = 1, so it is a CY 1-fold (omega_E = O_E)."""
        assert verify_cy_condition(hodge_elliptic(), 1)


# ================================================================
# SECTION 2: K3 x E HODGE DIAMOND (3 verification paths)
# ================================================================

class TestK3xEHodgeDiamond:
    """K3 x E Hodge diamond: Kuenneth, direct, and Euler cross-checks."""

    def test_k3xe_hodge_via_kuenneth(self):
        """Path (a): Kuenneth product of K3 and E Hodge diamonds.

        h^{p,q}(K3 x E) = sum_{a+c=p, b+d=q} h^{a,b}(K3) * h^{c,d}(E).
        """
        h = hodge_K3xE()
        assert h[(0, 0)] == 1
        assert h[(1, 0)] == 1  # h^{0,0}(K3)*h^{1,0}(E) = 1
        assert h[(0, 1)] == 1  # h^{0,0}(K3)*h^{0,1}(E) = 1
        assert h[(2, 0)] == 1  # h^{2,0}(K3)*h^{0,0}(E) = 1
        assert h[(0, 2)] == 1  # h^{0,2}(K3)*h^{0,0}(E) = 1
        assert h[(1, 1)] == 21  # h^{1,1}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{1,1}(E) = 20+1
        assert h[(3, 0)] == 1  # h^{2,0}(K3)*h^{1,0}(E) = 1
        assert h[(0, 3)] == 1  # h^{0,2}(K3)*h^{0,1}(E) = 1
        assert h[(2, 1)] == 21  # h^{2,0}(K3)*h^{0,1}(E) + h^{1,1}(K3)*h^{1,0}(E) = 1+20
        assert h[(1, 2)] == 21  # h^{0,2}(K3)*h^{1,0}(E) + h^{1,1}(K3)*h^{0,1}(E) = 1+20
        assert h[(3, 1)] == 1  # h^{2,2}(K3)*h^{1,0}(E) = 1
        assert h[(1, 3)] == 1  # h^{0,2}(K3)*h^{0,1}(E)... no
        # h^{1,3}: sum a+c=1, b+d=3. Nonzero: (a,b)=(0,2),(c,d)=(1,1) -> h^{0,2}*h^{1,1}=1
        assert h[(2, 2)] == 21  # by Hodge symmetry of h^{2,2} check below
        assert h[(3, 2)] == 1
        assert h[(2, 3)] == 1
        assert h[(3, 3)] == 1  # h^{2,2}(K3)*h^{1,1}(E) = 1

    def test_k3xe_hodge_symmetry(self):
        """Path (b): h^{p,q} = h^{q,p} for K3 x E."""
        assert verify_hodge_symmetry(hodge_K3xE())

    def test_k3xe_euler_multiplicativity(self):
        """Path (c): chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert euler_char(hodge_K3xE()) == 0
        assert verify_kuenneth_euler(hodge_K3(), hodge_elliptic())

    def test_k3xe_cy_condition(self):
        """K3 x E is a CY 3-fold: h^{3,0} = 1."""
        assert verify_cy_condition(hodge_K3xE(), 3)

    def test_k3xe_betti_numbers(self):
        """K3 x E Betti numbers via Kuenneth of Betti numbers.

        b_k(K3 x E) = sum_{i+j=k} b_i(K3) * b_j(E).
        b(K3) = [1, 0, 22, 0, 1], b(E) = [1, 2, 1].
        b_0 = 1*1 = 1
        b_1 = 1*2 + 0*1 = 2
        b_2 = 1*1 + 0*2 + 22*1 = 23
        b_3 = 0*1 + 22*2 + 0*1 = 44
        b_4 = 1*1 + 0*2 + 22*1 = 23
        b_5 = 1*2 + 0*1 = 2
        b_6 = 1*1 = 1
        """
        b = betti_from_hodge(hodge_K3xE())
        assert b[0] == 1
        assert b[1] == 2
        assert b[2] == 23
        assert b[3] == 44
        assert b[4] == 23
        assert b[5] == 2
        assert b[6] == 1

    def test_k3xe_betti_kuenneth_product(self):
        """Cross-check: Betti Kuenneth vs Hodge Kuenneth."""
        b_k3 = betti_from_hodge(hodge_K3())
        b_e = betti_from_hodge(hodge_elliptic())
        b_product: dict = {}
        for i, vi in b_k3.items():
            for j, vj in b_e.items():
                k = i + j
                b_product[k] = b_product.get(k, 0) + vi * vj
        b_direct = betti_from_hodge(hodge_K3xE())
        for k in range(7):
            assert b_product.get(k, 0) == b_direct.get(k, 0), f"Mismatch at b_{k}"

    def test_k3xe_dimension(self):
        """K3 x E has complex dimension 3."""
        assert dimension_from_hodge(hodge_K3xE()) == 3

    def test_k3xe_h21_equals_h11(self):
        """For CY 3-fold: mirror symmetry predicts h^{2,1} relates to h^{1,1}.
        For K3 x E: h^{2,1} = h^{1,1} = 21 (self-mirror in this sense)."""
        h = hodge_K3xE()
        assert h[(2, 1)] == h[(1, 1)] == 21


# ================================================================
# SECTION 3: HH VIA HKR (3 verification paths per dimension)
# ================================================================

class TestHHK3xE:
    """Hochschild cohomology of K3 x E via HKR."""

    def test_hh2_direct(self):
        """Path (a): HH^2(K3xE) = h^{3,2} + h^{2,1} + h^{1,0} = 1+21+1 = 23.

        For CY 3-fold: HH^n = sum_{p+q=n} h^{3-p, q}.
        n=2: (p,q) = (0,2), (1,1), (2,0).
        h^{3,2} + h^{2,1} + h^{1,0} = 1 + 21 + 1 = 23.
        """
        hh = hh_hkr_cy(hodge_K3xE(), 3)
        assert hh[2] == 23

    def test_hh2_via_kuenneth(self):
        """Path (b): HH^2(K3xE) via Kuenneth of HH*(K3) and HH*(E).

        HH*(K3) = {0:1, 2:22, 4:1}  (h^{2,0}+h^{1,1}+h^{0,2} = 1+20+1 = 22 for n=2)
        HH*(E) = {0:1, 1:2, 2:1}
        HH^2(K3xE) = HH^0(K3)*HH^2(E) + HH^2(K3)*HH^0(E)
                    = 1*1 + 22*1 = 23.
        """
        hh_k3 = hh_hkr_cy(hodge_K3(), 2)
        hh_e = hh_hkr_cy(hodge_elliptic(), 1)
        total = hh2_kuenneth_total(hh_k3, hh_e)
        assert total == 23

    def test_hh2_decomposition(self):
        """Path (c): HKR decomposition of HH^2 matches Hodge pieces."""
        decomp = hh_hkr_decomposition_cy(hodge_K3xE(), 3, 2)
        # Pieces: (3,2) -> h^{3,2}=1, (2,1) -> h^{2,1}=21, (1,0) -> h^{1,0}=1
        assert decomp[(3, 2)] == 1
        assert decomp[(2, 1)] == 21
        assert decomp[(1, 0)] == 1
        assert sum(decomp.values()) == 23

    def test_hh0(self):
        """HH^0(K3xE) = h^{3,0} = 1 (one endomorphism = identity)."""
        hh = hh_hkr_cy(hodge_K3xE(), 3)
        assert hh[0] == 1

    def test_hh1(self):
        """HH^1(K3xE) = h^{3,1} + h^{2,0} = 1 + 1 = 2.

        Two infinitesimal automorphisms: one from translation on E,
        one from the CY volume rescaling.
        """
        hh = hh_hkr_cy(hodge_K3xE(), 3)
        assert hh[1] == 2

    def test_hh3(self):
        """HH^3(K3xE) = h^{3,3}+h^{2,2}+h^{1,1}+h^{0,0} = 1+21+21+1 = 44.

        Obstructions space.  Despite dim 44, by Bogomolov-Tian-Todorov,
        geometric deformations are unobstructed.
        """
        hh = hh_hkr_cy(hodge_K3xE(), 3)
        assert hh[3] == 44

    def test_hh_serre_duality(self):
        """CY Serre duality: HH^n = HH^{2d-n} for d=3.

        HH^0=HH^6=1, HH^1=HH^5=2, HH^2=HH^4=23, HH^3=HH^3=44.
        """
        assert verify_cy_serre_duality(hodge_K3xE(), 3)

    def test_hh_kuenneth_matches_direct(self):
        """Full Kuenneth product of HH matches direct HKR computation."""
        hh_direct = hh_hkr_cy(hodge_K3xE(), 3)
        hh_k3 = hh_hkr_cy(hodge_K3(), 2)
        hh_e = hh_hkr_cy(hodge_elliptic(), 1)
        hh_kuenneth_result = hh_kuenneth(hh_k3, hh_e)
        for n in range(7):
            assert hh_direct.get(n, 0) == hh_kuenneth_result.get(n, 0), \
                f"HH^{n} mismatch: direct={hh_direct.get(n,0)}, Kuenneth={hh_kuenneth_result.get(n,0)}"

    def test_total_hh_dim(self):
        """Sum of all HH^n = 1+2+23+44+23+2+1 = 96.

        Path (a): direct sum.
        Path (b): total(K3)*total(E) = 24*4 = 96.
        """
        hh = hh_hkr_cy(hodge_K3xE(), 3)
        assert total_hh_dim(hh) == 96
        # Cross-check via factor product
        hh_k3 = hh_hkr_cy(hodge_K3(), 2)
        hh_e = hh_hkr_cy(hodge_elliptic(), 1)
        assert total_hh_dim(hh_k3) == 24  # 1 + 22 + 1
        assert total_hh_dim(hh_e) == 4    # 1 + 2 + 1
        assert total_hh_dim(hh_k3) * total_hh_dim(hh_e) == 96


class TestHHK3:
    """HH for K3 surface."""

    def test_hh_k3_dimensions(self):
        """HH*(K3): HH^0=1, HH^1=0, HH^2=22, HH^3=0, HH^4=1.

        For CY 2-fold: HH^n = sum_{p+q=n} h^{2-p, q}.
        n=0: h^{2,0}=1. n=1: h^{2,1}+h^{1,0}=0+0=0.
        n=2: h^{2,2}+h^{1,1}+h^{0,0}=1+20+1=22.
        n=3: h^{1,2}+h^{0,1}=0+0=0. n=4: h^{0,2}=1.
        """
        hh = hh_hkr_cy(hodge_K3(), 2)
        assert hh.get(0, 0) == 1
        assert hh.get(1, 0) == 0
        assert hh.get(2, 0) == 22
        assert hh.get(3, 0) == 0
        assert hh.get(4, 0) == 1

    def test_hh_k3_serre_duality(self):
        """CY Serre duality for K3: HH^n = HH^{4-n}."""
        assert verify_cy_serre_duality(hodge_K3(), 2)


class TestHHElliptic:
    """HH for elliptic curve."""

    def test_hh_e_dimensions(self):
        """HH*(E): HH^0=1, HH^1=2, HH^2=1.

        For CY 1-fold: HH^n = sum_{p+q=n} h^{1-p, q}.
        n=0: p=0,q=0: h^{1,0}=1.
        n=1: p=0,q=1: h^{1,1}=1; p=1,q=0: h^{0,0}=1. Total=2.
        n=2: p=1,q=1: h^{0,1}=1. Total=1.
        """
        hh = hh_hkr_cy(hodge_elliptic(), 1)
        assert hh[0] == 1
        assert hh[1] == 2
        assert hh[2] == 1

    def test_hh_e_serre_duality(self):
        """CY Serre duality for E: HH^n = HH^{2-n}."""
        assert verify_cy_serre_duality(hodge_elliptic(), 1)


# ================================================================
# SECTION 4: DEFORMATION SPACE (3 verification paths)
# ================================================================

class TestDeformationSpaceK3xE:
    """Deformation space of D^b(K3 x E)."""

    def test_total_deformations(self):
        """dim HH^2 = 23: total first-order deformations."""
        ds = deformation_space_K3xE()
        assert ds.dim_hh2 == 23

    def test_complex_structure_deformations(self):
        """dim H^1(T_{K3xE}) = h^{2,1} = 21.

        Path (a): direct Hodge number.
        Path (b): by Kuenneth: h^{2,1}(K3xE) = h^{2,0}*h^{0,1} + h^{1,1}*h^{1,0}
                  = 1*1 + 20*1 = 21.
        """
        ds = deformation_space_K3xE()
        assert ds.dim_complex_structure == 21

    def test_bfield_deformation(self):
        """dim H^0(wedge^2 T) = h^{1,0}(K3xE) = 1.

        For CY 3-fold: H^0(wedge^2 T) = h^{3-2, 0} = h^{1,0}.
        The B-field comes from the 1-form on E (translation).
        """
        ds = deformation_space_K3xE()
        assert ds.dim_bfield == 1

    def test_volume_deformation(self):
        """dim H^2(O_{K3xE}) = h^{0,2} = 1.

        The CY volume rescaling direction. h^{0,2} = h^{2,0} = 1 (from K3).
        """
        ds = deformation_space_K3xE()
        assert ds.dim_volume == 1

    def test_nc_deformations_count(self):
        """NC deformations = HH^2 - H^1(T) = 23 - 21 = 2.

        The two NC directions are: B-field (1) + volume (1).
        """
        ds = deformation_space_K3xE()
        assert ds.dim_nc == 2
        assert ds.dim_nc == ds.dim_bfield + ds.dim_volume

    def test_decomposition_sums_to_total(self):
        """Complex str + B-field + volume = total HH^2.

        Path (a): 21 + 1 + 1 = 23.
        Path (b): HKR decomposition pieces sum to HH^2.
        """
        ds = deformation_space_K3xE()
        assert ds.dim_complex_structure + ds.dim_bfield + ds.dim_volume == ds.dim_hh2

    def test_obstruction_dimension(self):
        """dim HH^3(K3xE) = 44.

        Despite nonzero obstructions, BTT ensures geometric deformations are
        unobstructed.  The NC obstructions require separate analysis.
        """
        ds = deformation_space_K3xE()
        assert ds.dim_obstructions == 44

    def test_nc_ratio(self):
        """NC ratio = 2/23."""
        ds = deformation_space_K3xE()
        assert nc_to_commutative_ratio(ds) == Fraction(2, 23)


class TestDeformationSpaceQuintic:
    """Quintic CY3 in P^4: h^{2,1}=101, h^{1,1}=1."""

    def test_quintic_hh2(self):
        """HH^2(quintic) = h^{2,1} = 101.

        h^{3,2}=0, h^{1,0}=0 for the quintic.
        All deformations are complex structure: NO NC deformations.
        """
        ds = deformation_space_quintic()
        assert ds.dim_hh2 == 101

    def test_quintic_no_nc(self):
        """Quintic has zero NC deformations."""
        ds = deformation_space_quintic()
        assert ds.dim_nc == 0
        assert ds.dim_bfield == 0
        assert ds.dim_volume == 0

    def test_quintic_obstructions(self):
        """HH^3(quintic) = 4.  But unobstructed by BTT."""
        ds = deformation_space_quintic()
        assert ds.dim_obstructions == 4

    def test_quintic_serre_duality(self):
        """CY Serre duality for quintic."""
        ds = deformation_space_quintic()
        assert ds.serre_dual


class TestDeformationSpaceT3:
    """Complex 3-torus T^3."""

    def test_t3_hh2(self):
        """HH^2(T^3) = h^{3,2}+h^{2,1}+h^{1,0} = 3+9+3 = 15.

        h^{p,q}(T^3) = C(3,p)*C(3,q).
        h^{3,2}=1*3=3, h^{2,1}=3*3=9, h^{1,0}=3*1=3.
        """
        ds = deformation_space_torus3()
        assert ds.dim_hh2 == 15

    def test_t3_complex_structure(self):
        """dim H^1(T_{T^3}) = h^{2,1} = 9."""
        ds = deformation_space_torus3()
        assert ds.dim_complex_structure == 9

    def test_t3_bfield(self):
        """dim H^0(wedge^2 T_{T^3}) = h^{1,0} = 3."""
        ds = deformation_space_torus3()
        assert ds.dim_bfield == 3

    def test_t3_nc(self):
        """NC deformations of T^3: 15 - 9 = 6."""
        ds = deformation_space_torus3()
        assert ds.dim_nc == 6

    def test_t3_nc_ratio(self):
        """NC ratio for T^3: 6/15 = 2/5."""
        ds = deformation_space_torus3()
        assert nc_to_commutative_ratio(ds) == Fraction(2, 5)


class TestDeformationSpaceK3:
    """K3 surface deformations."""

    def test_k3_hh2(self):
        """HH^2(K3) = h^{2,2}+h^{1,1}+h^{0,0} = 1+20+1 = 22.

        For CY 2-fold: HH^2 = sum_{p+q=2} h^{2-p, q}.
        """
        ds = deformation_space_K3()
        assert ds.dim_hh2 == 22

    def test_k3_complex_structure(self):
        """dim H^1(T_{K3}) = h^{1,1} = 20.

        This is the 20-dimensional K3 moduli space (local dimension).
        """
        ds = deformation_space_K3()
        assert ds.dim_complex_structure == 20

    def test_k3_bfield(self):
        """dim H^0(wedge^2 T_{K3}) = h^{0,0} = 1.

        For CY 2-fold (d=2): H^0(wedge^2 T) = h^{d-2,0} = h^{0,0} = 1.
        This is the B-field from the volume form.
        """
        ds = deformation_space_K3()
        assert ds.dim_bfield == 1

    def test_k3_nc(self):
        """NC deformations of K3: HH^2 - H^1(T) = 22 - 20 = 2."""
        ds = deformation_space_K3()
        assert ds.dim_nc == 2


class TestDeformationSpaceElliptic:
    """Elliptic curve deformations."""

    def test_e_hh2(self):
        """HH^2(E) = h^{0,1} = 1.

        For CY 1-fold: HH^2 = sum_{p+q=2} h^{1-p,q}.
        Only p=1,q=1: h^{0,1}=1.
        """
        ds = deformation_space_elliptic()
        assert ds.dim_hh2 == 1

    def test_e_complex_structure(self):
        """dim H^1(T_E) = h^{0,1} = 1. The modular parameter tau."""
        ds = deformation_space_elliptic()
        assert ds.dim_complex_structure == 1

    def test_e_no_nc(self):
        """E has no NC deformations (dim 1, no B-field possible)."""
        ds = deformation_space_elliptic()
        assert ds.dim_nc == 0


# ================================================================
# SECTION 5: BRAUER GROUP (3 verification paths)
# ================================================================

class TestBrauerGroup:
    """Brauer group structure of K3 x E."""

    def test_brauer_k3_generic(self):
        """Br(K3) for generic K3 (rho=0): transcendental rank = 22.

        Path (a): b2(K3) = 22, rho = 0, so trans_rank = 22 - 0 = 22.
        Path (b): the transcendental lattice of generic K3 has rank 22
                  (entire H^2 is transcendental).
        """
        br = brauer_K3(rho=0)
        assert br.transcendental_brauer_rank() == 22

    def test_brauer_k3_algebraic(self):
        """Br(K3) for algebraic K3 (rho=1): transcendental rank = 21."""
        br = brauer_K3(rho=1)
        assert br.transcendental_brauer_rank() == 21

    def test_brauer_k3_maximal_picard(self):
        """K3 with maximal Picard rank rho=20: trans_rank = 2.

        Known to exist (singular K3 surfaces, e.g., Fermat quartic in P^3).
        """
        br = brauer_K3(rho=20)
        assert br.transcendental_brauer_rank() == 2

    def test_brauer_elliptic(self):
        """Br(E) = Q/Z, rank 1."""
        br = brauer_elliptic()
        # The Brauer group of an elliptic curve has rank 1
        # Our model stores b2=1, rho=0, so trans_rank=1
        assert br.b2 == 1

    def test_brauer_k3xe_generic(self):
        """Br(K3xE) for generic K3 (rho_K3=0): trans_rank = 22.

        b2(K3xE) = 23, rho(K3xE) = rho_K3 + 1 = 1.
        trans_rank = 23 - 1 = 22.
        """
        br = brauer_K3xE(rho_K3=0)
        assert br.transcendental_brauer_rank() == 22

    def test_brauer_k3xe_algebraic(self):
        """Br(K3xE) for algebraic K3 (rho_K3=1): trans_rank = 21."""
        br = brauer_K3xE(rho_K3=1)
        assert br.transcendental_brauer_rank() == 21

    def test_brauer_product_decomposition_generic(self):
        """Decomposition of Br(K3 x E) into components.

        Br(K3) + Br(E) + mixed = 22 + 1 + 0 = 23.
        But total product transcendental rank = 22 (not 23).
        The discrepancy: sum_of_parts = 23 but total = 22 because
        the product has rho = rho_K3 + 1 = 1, so b2 - rho = 23 - 1 = 22.
        The Br(E) = Q/Z contributes via the product Picard, not additively.
        """
        decomp = brauer_product_decomposition(rho_K3=0)
        assert decomp["Br_K3_rank"] == 22
        assert decomp["Br_E_rank"] == 1
        assert decomp["mixed_H1_K3_Pic0_E"] == 0
        assert decomp["total_product_rank"] == 22
        # sum_of_parts = 22 + 1 + 0 = 23
        assert decomp["sum_of_parts"] == 23

    def test_formal_brauer_k3xe(self):
        """Formal Brauer group dim = h^{0,2}(K3xE) = 1."""
        br = brauer_K3xE()
        assert br.formal_brauer_dim() == 1

    def test_formal_brauer_k3(self):
        """Formal Brauer group of K3: h^{0,2}(K3) = 1."""
        br = brauer_K3()
        assert br.formal_brauer_dim() == 1


# ================================================================
# SECTION 6: POISSON AND DEFORMATION QUANTIZATION
# ================================================================

class TestPoissonStructure:
    """Poisson structures and deformation quantization."""

    def test_k3_poisson_dim(self):
        """K3: dim H^0(wedge^2 T_K3) = h^{0,0} = 1.

        Path (a): direct from CY condition. wedge^2 T = O_K3, so H^0 = C.
        Path (b): T_K3 = Omega^1 (via omega), so wedge^2 T = wedge^2 Omega^1 = omega_K3 = O_K3.
        """
        ps = poisson_K3()
        assert ps.dim_poisson == 1

    def test_k3_is_symplectic(self):
        """K3 is holomorphic symplectic."""
        ps = poisson_K3()
        assert ps.is_symplectic()

    def test_elliptic_no_poisson(self):
        """E has no Poisson structure (wedge^2 T_E = 0)."""
        ps = poisson_elliptic()
        assert ps.dim_poisson == 0

    def test_elliptic_not_symplectic(self):
        """E is not symplectic (dim 1, odd)."""
        ps = poisson_elliptic()
        assert not ps.is_symplectic()

    def test_k3xe_poisson_dim(self):
        """K3 x E: dim Poisson = 1, coming entirely from K3.

        H^0(wedge^2 T_{K3xE}) = h^{1,0}(K3xE) = 1.
        The decomposition: from K3 symplectic (1) + cross (0) + E (0) = 1.
        """
        ps = poisson_K3xE()
        assert ps.dim_poisson == 1

    def test_k3xe_not_symplectic(self):
        """K3 x E is NOT symplectic (dim 3, odd)."""
        ps = poisson_K3xE()
        assert not ps.is_symplectic()

    def test_k3xe_poisson_gauge_dim(self):
        """K3 x E: gauge group dim = H^0(T) = h^{2,0} = 1.

        For CY 3-fold: H^0(T) = h^{d-1, 0} = h^{2,0} = 1.
        The gauge is from the CY volume rescaling.
        """
        ps = poisson_K3xE()
        assert ps.dim_gauge == 1

    def test_t3_poisson_dim(self):
        """T^3: dim Poisson = 3.

        H^0(wedge^2 T_{T^3}) = h^{1,0}(T^3) = C(3,1) = 3.
        Three independent Poisson structures from the three coordinate 2-planes.
        """
        ps = poisson_torus3()
        assert ps.dim_poisson == 3

    def test_star_product_order_0(self):
        """Star product at order 0: ordinary multiplication."""
        data = star_product_order_n(0)
        assert data["order"] == 0
        assert data["differential_order"] == (0, 0)

    def test_star_product_order_1(self):
        """Star product at order 1: Poisson bracket."""
        data = star_product_order_n(1)
        assert data["order"] == 1
        assert data["differential_order"] == (1, 1)

    def test_star_product_order_2(self):
        """Star product at order 2: Moyal coefficient = 1/8."""
        data = star_product_order_n(2)
        assert data["order"] == 2
        assert data["coefficient"] == Fraction(1, 8)

    def test_star_product_order_3(self):
        """Star product at order 3: Moyal coefficient = 1/48."""
        data = star_product_order_n(3)
        assert data["coefficient"] == Fraction(1, 48)

    def test_star_product_moyal_coefficients(self):
        """Moyal coefficients: 1/(2^n * n!) for n=0,1,2,3,4.

        Path (a): direct formula.
        Path (b): 1/1, 1/2, 1/8, 1/48, 1/384.
        """
        expected = [Fraction(1), Fraction(1, 2), Fraction(1, 8),
                    Fraction(1, 48), Fraction(1, 384)]
        for n in range(5):
            data = star_product_order_n(n)
            assert data["coefficient"] == expected[n], \
                f"Moyal coeff at order {n}: got {data['coefficient']}, expected {expected[n]}"


# ================================================================
# SECTION 7: MORITA MODULI
# ================================================================

class TestMoritaModuli:
    """Morita moduli of Brauer-twisted derived categories."""

    def test_k3_bfield_torus(self):
        """B-field torus for K3: dim = b2(K3) = 22."""
        mm = morita_moduli_K3()
        assert mm.bfield_torus_dim == 22

    def test_k3xe_bfield_torus(self):
        """B-field torus for K3 x E: dim = b2(K3xE) = 23."""
        mm = morita_moduli_K3xE()
        assert mm.bfield_torus_dim == 23

    def test_k3_complex_moduli(self):
        """Complex structure moduli of K3: h^{1,1} = 20."""
        mm = morita_moduli_K3()
        assert mm.complex_moduli_dim == 20

    def test_k3xe_complex_moduli(self):
        """Complex structure moduli of K3 x E: h^{2,1} = 21."""
        mm = morita_moduli_K3xE()
        assert mm.complex_moduli_dim == 21

    def test_extended_period_dim(self):
        """Extended period domain dimension (real) = 2 * b2.

        K3: 2*22 = 44.  K3 x E: 2*23 = 46.
        """
        assert morita_moduli_K3().extended_period_dim_real == 44
        assert morita_moduli_K3xE().extended_period_dim_real == 46


# ================================================================
# SECTION 8: A-INFINITY DEFORMATION
# ================================================================

class TestAinfDeformation:
    """A-infinity deformation of End*(O_X)."""

    def test_k3xe_ext_dims(self):
        """Ext^q(O_{K3xE}, O_{K3xE}) = H^q(O_{K3xE}) = h^{0,q}.

        h^{0,0}=h^{0,1}=h^{0,2}=h^{0,3}=1. Total = 4.
        """
        ai = ainfty_deformation_K3xE()
        assert ai.ext_dims == {0: 1, 1: 1, 2: 1, 3: 1}
        assert ai.total_ext_dim == 4

    def test_k3_ext_dims(self):
        """Ext^q(O_K3, O_K3) = H^q(O_K3).

        h^{0,0}=1, h^{0,1}=0, h^{0,2}=1. Total = 2.
        This is H*(S^2) = C + C[-2]: O_K3 is a SPHERICAL object.
        """
        ai = ainfty_deformation_K3()
        assert ai.ext_dims == {0: 1, 1: 0, 2: 1}
        assert ai.total_ext_dim == 2

    def test_k3xe_ainfty_relations(self):
        """A-infinity relations satisfied at all orders (Kontsevich formality)."""
        ai = ainfty_deformation_K3xE()
        checks = ai.ainfty_relation_check(5)
        assert all(checks.values())

    def test_k3xe_trace_degree(self):
        """Trace pairing: Ext^q x Ext^{3-q} -> Ext^3 = C.

        The trace map is in degree d = 3 for CY 3-fold.
        """
        ai = ainfty_deformation_K3xE()
        assert ai.trace_deg == 3

    def test_k3xe_first_order_deformation(self):
        """First-order deformation: m_2^{(1)} = Poisson bracket."""
        ai = ainfty_deformation_K3xE()
        data = ai.poisson_deformation_at_order(1)
        assert data["order"] == 1
        assert "Poisson" in data["m2_deformation"]


# ================================================================
# SECTION 9: CHIRAL COMPARISON
# ================================================================

class TestChiralComparison:
    """Compare chiral Hochschild with categorical HH."""

    def test_chiral_hh2_matches(self):
        """ChirHoch^2(CDO_{K3xE}) = HH^2(K3xE) = 23.

        By the Costello-Gwilliam theorem for CDOs on CY manifolds.
        """
        comp = chiral_comparison_K3xE()
        assert comp["match"]
        assert comp["HH2_categorical"] == 23
        assert comp["ChirHoch2_chiral"] == 23

    def test_chiral_nc_directions(self):
        """The chiral algebra sees both NC directions (B-field + volume)."""
        comp = chiral_comparison_K3xE()
        assert comp["NC_directions"] == 2
        assert comp["B_field"] == 1
        assert comp["volume"] == 1

    def test_chiral_all_degrees_k3xe(self):
        """ChirHoch^n = HH^n for all n, for K3 x E.

        This is the full Costello-Gwilliam isomorphism.
        """
        h = hodge_K3xE()
        hh = hh_hkr_cy(h, 3)
        for n in range(7):
            assert chiral_hochschild_dim_cy(h, 3, n) == hh.get(n, 0)

    def test_chiral_comparison_quintic(self):
        """Quintic: ChirHoch^2 = HH^2 = 101. All complex structure."""
        ds = deformation_space_quintic()
        assert chiral_hochschild_dim_cy(ds.hodge, 3, 2) == 101

    def test_chiral_comparison_t3(self):
        """T^3: ChirHoch^2 = HH^2 = 15. NC dim = 6."""
        h = hodge_torus(3)
        assert chiral_hochschild_dim_cy(h, 3, 2) == 15


# ================================================================
# SECTION 10: CROSS-CHECKS AND CONSISTENCY
# ================================================================

class TestCrossChecks:
    """Multi-path cross-checks across all CY manifolds."""

    @pytest.mark.parametrize("label,hodge_fn,d,expected_chi", [
        ("K3", hodge_K3, 2, 24),
        ("E", hodge_elliptic, 1, 0),
        ("K3xE", hodge_K3xE, 3, 0),
        ("Quintic", lambda: deformation_space_quintic().hodge, 3, -200),
    ])
    def test_euler_characteristics(self, label, hodge_fn, d, expected_chi):
        """Euler characteristics from independent computation.

        K3: 24. E: 0. K3xE: 0. Quintic: -200 (= 2*(1-101)).
        """
        h = hodge_fn()
        assert euler_char(h) == expected_chi

    def test_euler_multiplicativity_k3_e(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert verify_kuenneth_euler(hodge_K3(), hodge_elliptic())

    def test_euler_multiplicativity_e_e(self):
        """chi(E x E) = 0 * 0 = 0."""
        assert verify_kuenneth_euler(hodge_elliptic(), hodge_elliptic())

    @pytest.mark.parametrize("label,hodge_fn,d", [
        ("K3", hodge_K3, 2),
        ("E", hodge_elliptic, 1),
        ("K3xE", hodge_K3xE, 3),
        ("T^3", lambda: hodge_torus(3), 3),
    ])
    def test_hodge_symmetry(self, label, hodge_fn, d):
        """Hodge symmetry h^{p,q} = h^{q,p} for all CY manifolds."""
        assert verify_hodge_symmetry(hodge_fn())

    @pytest.mark.parametrize("label,hodge_fn,d", [
        ("K3", hodge_K3, 2),
        ("E", hodge_elliptic, 1),
        ("K3xE", hodge_K3xE, 3),
        ("T^3", lambda: hodge_torus(3), 3),
    ])
    def test_cy_serre_duality(self, label, hodge_fn, d):
        """CY Serre duality HH^n = HH^{2d-n}."""
        assert verify_cy_serre_duality(hodge_fn(), d)

    @pytest.mark.parametrize("label,hodge_fn,d", [
        ("K3", hodge_K3, 2),
        ("E", hodge_elliptic, 1),
        ("K3xE", hodge_K3xE, 3),
        ("T^3", lambda: hodge_torus(3), 3),
    ])
    def test_cy_condition(self, label, hodge_fn, d):
        """CY condition: h^{d,0} = 1."""
        assert verify_cy_condition(hodge_fn(), d)

    @pytest.mark.parametrize("label,hodge_fn,d", [
        ("K3", hodge_K3, 2),
        ("E", hodge_elliptic, 1),
        ("K3xE", hodge_K3xE, 3),
    ])
    def test_hh_euler_equals_topological_euler(self, label, hodge_fn, d):
        """HH Euler characteristic = topological Euler characteristic.

        For CY d-fold: sum (-1)^n dim HH^n = chi(X).
        """
        assert verify_hh_euler_equals_chi_squared(hodge_fn(), d)

    def test_hh2_additive_kuenneth(self):
        """HH^2(K3xE) decomposes additively via Kuenneth.

        HH^2(K3xE) = HH^0(K3)*HH^2(E) + HH^2(K3)*HH^0(E) = 1 + 22 = 23.
        (HH^1(K3) = 0, so the HH^1*HH^1 cross-term vanishes.)
        """
        hh_k3 = hh_hkr_cy(hodge_K3(), 2)
        hh_e = hh_hkr_cy(hodge_elliptic(), 1)
        decomp = hh2_kuenneth_decomposition(hh_k3, hh_e)
        assert decomp == {
            "HH^0(X) x HH^2(Y)": 1,   # 1 * 1
            "HH^2(X) x HH^0(Y)": 22,  # 22 * 1
        }
        assert sum(decomp.values()) == 23


class TestTorus:
    """Complex torus Hodge diamonds."""

    @pytest.mark.parametrize("d", [1, 2, 3, 4, 5])
    def test_torus_euler_vanishes(self, d):
        """chi(T^d) = 0 for all d >= 1.

        b_k(T^d) = C(2d, k), so chi = sum (-1)^k C(2d,k) = (1-1)^{2d} = 0.
        """
        assert euler_char(hodge_torus(d)) == 0

    def test_torus_hodge_formula(self):
        """h^{p,q}(T^d) = C(d,p)*C(d,q)."""
        for d in range(1, 5):
            h = hodge_torus(d)
            for p in range(d + 1):
                for q in range(d + 1):
                    assert h[(p, q)] == math.comb(d, p) * math.comb(d, q)

    def test_torus_betti(self):
        """b_k(T^d) = C(2d, k).

        By Kuenneth: b_k(T^d) = sum_{p+q=k} C(d,p)*C(d,q) = C(2d, k)
        (Vandermonde identity).
        """
        for d in range(1, 5):
            h = hodge_torus(d)
            b = betti_from_hodge(h)
            for k in range(2 * d + 1):
                assert b.get(k, 0) == math.comb(2 * d, k), \
                    f"b_{k}(T^{d}): got {b.get(k,0)}, expected {math.comb(2*d, k)}"


# ================================================================
# SECTION 11: SUMMARY AND INTEGRATION TESTS
# ================================================================

class TestSummaries:
    """Full summary integration tests."""

    def test_summary_k3xe(self):
        """Full summary for K3 x E is self-consistent."""
        s = summary_K3xE()
        assert s["CY_condition"]
        assert s["Hodge_symmetry"]
        assert s["Serre_duality"]
        assert s["chiral_match"]
        assert s["HH2"] == 23
        assert s["complex_structure_dim"] == 21
        assert s["B_field_dim"] == 1
        assert s["volume_dim"] == 1
        assert s["NC_dim"] == 2
        assert s["poisson_dim"] == 1
        assert not s["is_symplectic"]
        assert s["euler_char"] == 0

    def test_summary_k3(self):
        """Full summary for K3 is self-consistent."""
        s = summary_K3()
        assert s["CY_condition"]
        assert s["HH2"] == 22
        assert s["complex_structure_dim"] == 20
        assert s["NC_dim"] == 2
        assert s["poisson_dim"] == 1
        assert s["is_symplectic"]
        assert s["euler_char"] == 24

    def test_summary_quintic(self):
        """Full summary for quintic is self-consistent."""
        s = summary_quintic()
        assert s["CY_condition"]
        assert s["HH2"] == 101
        assert s["NC_dim"] == 0
        assert s["poisson_dim"] == 0
        assert s["euler_char"] == -200

    def test_summary_t3(self):
        """Full summary for T^3 is self-consistent."""
        s = summary_T3()
        assert s["CY_condition"]
        assert s["HH2"] == 15
        assert s["NC_dim"] == 6
        assert s["poisson_dim"] == 3
        assert s["euler_char"] == 0


# ================================================================
# SECTION 12: COMPARATIVE TABLE (all CY manifolds)
# ================================================================

class TestComparativeTable:
    """Cross-family comparison of NC deformation data.

    Verifies that the relationships between different CY manifolds
    are consistent and highlight the special features of K3 x E.
    """

    def test_hh2_ordering(self):
        """HH^2 ordering across families.

        T^3 (15) < K3 (22) < K3xE (23) < Quintic (101).
        """
        assert deformation_space_torus3().dim_hh2 == 15
        assert deformation_space_K3().dim_hh2 == 22
        assert deformation_space_K3xE().dim_hh2 == 23
        assert deformation_space_quintic().dim_hh2 == 101

    def test_nc_ordering(self):
        """NC dimensions: Quintic (0) < K3xE (2) = K3 (2) < T^3 (6)."""
        assert deformation_space_quintic().dim_nc == 0
        assert deformation_space_K3xE().dim_nc == 2
        assert deformation_space_K3().dim_nc == 2
        assert deformation_space_torus3().dim_nc == 6

    def test_poisson_ordering(self):
        """Poisson dimensions: Quintic/E (0) < K3/K3xE (1) < T^3 (3)."""
        assert poisson_elliptic().dim_poisson == 0
        ps_q = PoissonData(deformation_space_quintic().hodge, 3, "Q")
        assert ps_q.dim_poisson == 0
        assert poisson_K3().dim_poisson == 1
        assert poisson_K3xE().dim_poisson == 1
        assert poisson_torus3().dim_poisson == 3

    def test_k3xe_special_feature(self):
        """K3 x E is the SIMPLEST CY3 with both NC deformations AND Poisson.

        Quintic: no NC, no Poisson.
        K3 x E: NC=2, Poisson=1.
        T^3: NC=6, Poisson=3 (too many).
        """
        ds_q = deformation_space_quintic()
        ds_k = deformation_space_K3xE()
        ds_t = deformation_space_torus3()
        # K3 x E has exactly the right amount of NC structure
        assert ds_q.dim_nc == 0  # quintic: none
        assert ds_k.dim_nc == 2  # K3xE: minimal nonzero
        assert ds_t.dim_nc == 6  # T^3: large

    def test_ext_dim_comparison(self):
        """Ext*(O,O) dimensions across families.

        K3: [1,0,1] (spherical object, total 2).
        E: [1,1] (total 2).
        K3xE: [1,1,1,1] (total 4, exterior algebra on one generator).
        """
        ai_k3 = ainfty_deformation_K3()
        ai_k3xe = ainfty_deformation_K3xE()
        assert ai_k3.total_ext_dim == 2
        assert ai_k3xe.total_ext_dim == 4

    def test_chiral_match_universal(self):
        """ChirHoch^2 = HH^2 for all CY manifolds tested.

        This is the Costello-Gwilliam theorem applied to each.
        """
        for hodge_fn, d in [
            (hodge_K3, 2),
            (hodge_elliptic, 1),
            (hodge_K3xE, 3),
            (lambda: hodge_torus(3), 3),
        ]:
            h = hodge_fn()
            hh = hh_hkr_cy(h, d)
            assert chiral_hochschild_dim_cy(h, d, 2) == hh.get(2, 0)


# ================================================================
# SECTION 13: EDGE CASES AND ROBUSTNESS
# ================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_hodge_number_missing_key(self):
        """hodge_number returns 0 for missing keys."""
        h = hodge_K3()
        assert hodge_number(h, 5, 5) == 0
        assert hodge_number(h, 1, 0) == 0

    def test_empty_hodge_product(self):
        """Product with point (all zero except h^{0,0}=1)."""
        h_pt = {(0, 0): 1}
        h_k3 = hodge_K3()
        h_prod = hodge_product(h_k3, h_pt)
        for (p, q), v in h_k3.items():
            assert h_prod.get((p, q), 0) == v

    def test_high_picard_rank_brauer(self):
        """Brauer rank for rho = b2 (maximal): trans_rank = 0."""
        br = brauer_K3(rho=22)
        assert br.transcendental_brauer_rank() == 0

    def test_deformation_space_repr(self):
        """DeformationSpace repr is well-formed."""
        ds = deformation_space_K3xE()
        r = repr(ds)
        assert "K3 x E" in r
        assert "HH^2=23" in r

    def test_hh_negative_index(self):
        """HH^n = 0 for n < 0 or n > 2d (outside range)."""
        hh = hh_hkr_cy(hodge_K3xE(), 3)
        assert hh.get(-1, 0) == 0
        assert hh.get(7, 0) == 0

    def test_star_product_coefficient_decreasing(self):
        """Moyal coefficients are strictly decreasing."""
        prev = Fraction(1)
        for n in range(1, 8):
            data = star_product_order_n(n)
            coeff = data["coefficient"]
            assert coeff < prev
            prev = coeff
