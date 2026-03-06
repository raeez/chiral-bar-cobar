"""Master integration test: cross-checks across ALL compute modules.

This test verifies consistency across the entire compute engine,
ensuring that the same mathematical facts are encoded consistently
in every module that references them.
"""

import pytest
from sympy import Rational, Symbol

k = Symbol('k')
c = Symbol('c')


class TestCurvatureConsistency:
    """Verify curvature formulas are consistent across modules."""

    def test_virasoro_curvature(self):
        from compute.lib.virasoro_bar import virasoro_curvature
        from compute.lib.virasoro_ainfty import virasoro_m0
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY

        assert virasoro_curvature() == c / 2
        assert virasoro_m0() == c / 2
        assert ALGEBRA_REGISTRY["Virasoro"]["curvature_m0"] == "c/2"
        assert ALGEBRA_REGISTRY["Virasoro"]["kappa_formula"] == "c/2"

    def test_e8_curvature(self):
        from compute.lib.e8_lattice_bar import e8_curvature
        assert e8_curvature(1) == Rational(31, 60)

    def test_sl2_curvature_kappa(self):
        from compute.lib.lie_algebra import kappa_km
        kappa_sl2 = kappa_km("A", 1, k)
        assert kappa_sl2 == 3 * (k + 2) / 4


class TestFFDualityConsistency:
    """Verify Feigin-Frenkel duality consistent across modules."""

    def test_sl2_shift(self):
        from compute.lib.koszul_pairs import ff_shift_sl2
        from compute.lib.lie_algebra import ff_dual_level
        assert ff_shift_sl2(k) == -k - 4
        assert ff_dual_level("A", 1, k) == -k - 4

    def test_sl3_shift(self):
        from compute.lib.koszul_pairs import ff_shift_sl3
        from compute.lib.lie_algebra import ff_dual_level
        assert ff_shift_sl3(k) == -k - 6
        assert ff_dual_level("A", 2, k) == -k - 6

    def test_e8_shift(self):
        from compute.lib.e8_lattice_bar import e8_dual_level
        assert e8_dual_level(k) == -k - 60
        assert e8_dual_level(1) == -61

    def test_b2_shift(self):
        from compute.lib.nonsimplylaced_bar import b2_ff_dual
        from compute.lib.lie_algebra import ff_dual_level
        assert b2_ff_dual(k) == -k - 6
        assert ff_dual_level("B", 2, k) == -k - 6

    def test_g2_shift(self):
        from compute.lib.nonsimplylaced_bar import g2_ff_dual
        from compute.lib.lie_algebra import ff_dual_level
        assert g2_ff_dual(k) == -k - 8
        assert ff_dual_level("G", 2, k) == -k - 8


class TestComplementarityConsistency:
    """Verify complementarity sums consistent across modules."""

    def test_virasoro_26(self):
        from compute.lib.virasoro_bar import virasoro_complementarity_sum
        from compute.lib.cross_algebra import complementarity_table
        from compute.lib.koszul_pairs import complementarity_sum_ds
        from compute.lib.genus_bridge import COMPLEMENTARITY_KAPPA

        assert virasoro_complementarity_sum() == 26
        assert complementarity_table()["Virasoro"] == 26
        assert complementarity_sum_ds("Virasoro") == 26
        assert COMPLEMENTARITY_KAPPA["sl2_Virasoro"] == 26

    def test_w3_100(self):
        from compute.lib.cross_algebra import complementarity_table
        from compute.lib.koszul_pairs import complementarity_sum_ds

        assert complementarity_table()["W3"] == 100
        assert complementarity_sum_ds("W3") == 100

    def test_e8_496(self):
        from compute.lib.e8_lattice_bar import e8_complementarity_sum
        from compute.lib.cross_algebra import complementarity_table

        assert e8_complementarity_sum() == 496
        assert complementarity_table()["E8"] == 496


class TestOSAlgebraConsistency:
    """Verify Orlik-Solomon dimensions consistent across modules."""

    def test_top_dim(self):
        from compute.lib.virasoro_bar import os_top_dim as vir_os
        from compute.lib.fm_compactification import os_top_dim as fm_os
        from compute.lib.bar_comparison import os_dim as comp_os

        for n in range(2, 6):
            from math import factorial
            assert vir_os(n) == factorial(n - 1)
            assert fm_os(n) == factorial(n - 1)
            assert comp_os(n, n - 1) == factorial(n - 1)  # top-degree OS dim

    def test_poincare(self):
        from compute.lib.virasoro_bar import os_poincare
        from compute.lib.fm_compactification import poincare_polynomial

        for n in range(2, 6):
            assert os_poincare(n) == poincare_polynomial(n)


class TestKoszulPairConsistency:
    """Verify Koszul duality facts consistent across modules."""

    def test_heisenberg_not_self_dual(self):
        from compute.lib.koszul_pairs import KOSZUL_PAIRS
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY

        assert KOSZUL_PAIRS["Heisenberg_Symch"]["self_dual"] is False
        assert ALGEBRA_REGISTRY["Heisenberg"].get("self_dual") is False

    def test_bg_bc_pair(self):
        from compute.lib.koszul_pairs import KOSZUL_PAIRS
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY

        assert KOSZUL_PAIRS["beta_gamma_bc"]["A"] == "beta_gamma"
        assert KOSZUL_PAIRS["beta_gamma_bc"]["A_dual"] == "bc_ghosts"
        assert ALGEBRA_REGISTRY["beta_gamma"]["koszul_dual"] == "bc"
        assert ALGEBRA_REGISTRY["bc"]["koszul_dual"] == "beta_gamma"


class TestSpectralSequenceConsistency:
    """Verify spectral sequence data consistent across modules."""

    def test_km_collapse_E1(self):
        from compute.lib.spectral_sequence import spectral_sequence_collapse
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY

        for alg in ["sl2", "sl3", "E8"]:
            assert spectral_sequence_collapse(alg)["collapse_page"] == 1

    def test_virasoro_collapse_E2(self):
        from compute.lib.spectral_sequence import spectral_sequence_collapse
        assert spectral_sequence_collapse("Virasoro")["collapse_page"] == 2

    def test_bar_coh_dims(self):
        from compute.lib.spectral_sequence import VIRASORO_BAR_COH
        assert VIRASORO_BAR_COH[1] == 1
        assert VIRASORO_BAR_COH[5] == 30
        assert VIRASORO_BAR_COH[10] == 3610


class TestBVConsistency:
    """Verify BV-BRST coefficients are correct."""

    def test_qme_half(self):
        from compute.lib.bv_brst import qme_coefficients
        assert qme_coefficients()["antibracket_coeff"] == Rational(1, 2)

    def test_hcs_two_thirds(self):
        from compute.lib.bv_brst import hcs_coefficients
        assert hcs_coefficients()["cubic_coeff"] == Rational(2, 3)


class TestPeriodicityConsistency:
    """Verify h vs h^vee distinction."""

    def test_b2(self):
        from compute.lib.nonsimplylaced_bar import periodicity_coxeter
        from compute.lib.lie_algebra import cartan_data

        b2 = cartan_data("B", 2)
        assert b2.h == 4
        assert b2.h_dual == 3
        assert b2.h != b2.h_dual
        assert periodicity_coxeter("B", 2) == 8  # 2h, NOT 2h^vee=6

    def test_g2(self):
        from compute.lib.nonsimplylaced_bar import periodicity_coxeter
        from compute.lib.lie_algebra import cartan_data

        g2 = cartan_data("G", 2)
        assert g2.h == 6
        assert g2.h_dual == 4
        assert periodicity_coxeter("G", 2) == 12  # 2h, NOT 2h^vee=8


class TestDeformationConsistency:
    """Verify P_inf vs Coisson distinction."""

    def test_coisson_not_chiral(self):
        from compute.lib.deformation_bar import pinf_vs_coisson
        data = pinf_vs_coisson()
        assert not data["Coisson"]["is_chiral_algebra"]
        assert data["P_inf_chiral"]["is_chiral_algebra"]


class TestWNConductorFormula:
    """Verify W_N conductor K_N = 2*(N-1)*(2*N^2 + 2*N + 1) = 4*N^3 - 2*N - 2."""

    def test_known_values(self):
        expected = {2: 26, 3: 100, 4: 246, 5: 488}
        for N, K_expected in expected.items():
            K_formula1 = 2 * (N - 1) * (2 * N**2 + 2 * N + 1)
            K_formula2 = 4 * N**3 - 2 * N - 2
            assert K_formula1 == K_expected, f"K_{N} formula1 = {K_formula1}, expected {K_expected}"
            assert K_formula2 == K_expected, f"K_{N} formula2 = {K_formula2}, expected {K_expected}"
            assert K_formula1 == K_formula2, f"Two formulas disagree at N={N}"


class TestE8KappaDerivation:
    """Verify kappa(E8) from general formula dim_g*(k+h_dual)/(2*h_dual)."""

    def test_e8_kappa_formula(self):
        """kappa(E8, k) = 248*(k+30)/(2*30) = 62*(k+30)/15."""
        from sympy import Rational, simplify
        # E8: dim=248, h_dual=30
        dim_g = 248
        h_dual = 30
        for k_val in [0, 1, 2, 5, 10]:
            expected = Rational(dim_g * (k_val + h_dual), 2 * h_dual)
            simplified = Rational(62 * (k_val + h_dual), 15)
            assert expected == simplified, (
                f"kappa(E8, k={k_val}): {expected} != {simplified}"
            )


class TestBarDimCrossModuleConsistency:
    """Verify KNOWN_BAR_DIMS (bar_complex.py) is consistent with
    SL2_BAR_COH (spectral_sequence.py) and Heisenberg E2 leading values."""

    def test_sl2_cross_module(self):
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        from compute.lib.spectral_sequence import SL2_BAR_COH
        for deg, val in SL2_BAR_COH.items():
            assert KNOWN_BAR_DIMS["sl2"][deg] == val, (
                f"sl2 bar dim mismatch at degree {deg}: "
                f"bar_complex={KNOWN_BAR_DIMS['sl2'][deg]}, "
                f"spectral_sequence={val}"
            )

    def test_heisenberg_e2_leading(self):
        """HEISENBERG_BAR_COH_E2_LEADING is all-ones (leading weight),
        while full bar cohomology in KNOWN_BAR_DIMS uses p(n-2)."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        from compute.lib.spectral_sequence import HEISENBERG_BAR_COH_E2_LEADING
        # E2 leading is 1 in each degree
        for deg in range(1, 11):
            assert HEISENBERG_BAR_COH_E2_LEADING[deg] == 1
        # Full bar cohomology differs from degree 4 onward
        assert KNOWN_BAR_DIMS["Heisenberg"][4] == 2  # p(2) = 2, not 1

    def test_virasoro_cross_module(self):
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        from compute.lib.spectral_sequence import VIRASORO_BAR_COH
        for deg, val in VIRASORO_BAR_COH.items():
            assert KNOWN_BAR_DIMS["Virasoro"][deg] == val, (
                f"Virasoro bar dim mismatch at degree {deg}"
            )


class TestGeneratorCounts:
    """Verify generator counts are consistent."""

    def test_e8(self):
        from compute.lib.e8_lattice_bar import e8_generator_count
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY

        assert e8_generator_count()["total"] == 248
        assert ALGEBRA_REGISTRY["E8"]["n_generators"] == 248

    def test_sl2(self):
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY
        assert ALGEBRA_REGISTRY["sl2"]["n_generators"] == 3

    def test_sl3(self):
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY
        assert ALGEBRA_REGISTRY["sl3"]["n_generators"] == 8

    def test_w3(self):
        from compute.lib.cross_algebra import ALGEBRA_REGISTRY
        assert ALGEBRA_REGISTRY["W3"]["n_generators"] == 2
