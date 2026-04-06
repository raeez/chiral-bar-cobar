r"""Tests for the K3 x E Koszul dual engine.

Multi-path verification of the Koszul dual computation for the K3 sigma
model and K3 x E chiral algebras.  Tests are organized by verification
path following the Multi-Path Verification Mandate.

Verification paths:
  (a) Direct computation — kappa from definition
  (b) Alternative formula — kappa from Feigin-Frenkel level / N=4 Ward / geometry
  (c) Complementarity sum check — Theorem C consistency
  (d) Genus expansion — F_g + F_g' = 0 at multiple genera
  (e) Cross-family consistency — additivity, subalgebra decomposition
  (f) Anti-pattern cross-checks — AP19, AP24, AP33, AP48, AP50

Total: 86 tests.
"""

import pytest
from fractions import Fraction

F = Fraction

from compute.lib.cy_koszul_dual_k3e_engine import (
    # Constants
    K3_CENTRAL_CHARGE,
    K3_COMPLEX_DIM,
    K3_EULER_CHAR,
    K3_SU2_LEVEL,
    E_CENTRAL_CHARGE,
    E_COMPLEX_DIM,
    K3E_CENTRAL_CHARGE,
    K3E_COMPLEX_DIM,
    # Arithmetic
    bernoulli_number,
    faber_pandharipande,
    # Kappa (multi-path)
    kappa_k3,
    kappa_k3_path_geometric,
    kappa_k3_path_character,
    kappa_k3_path_n4_ward,
    kappa_k3_path_hodge,
    kappa_k3_path_euler,
    kappa_k3_all_paths,
    kappa_elliptic_curve,
    kappa_k3e,
    # Dual kappa
    kappa_dual_cy,
    kappa_dual_k3,
    kappa_dual_k3_path_complementarity,
    kappa_dual_k3_path_geometric,
    kappa_dual_k3_path_n4_level_inversion,
    kappa_dual_k3_all_paths,
    kappa_dual_e,
    kappa_dual_k3e,
    # Complementarity
    complementarity_sum_k3,
    complementarity_sum_k3e,
    complementarity_sum_virasoro_component,
    complementarity_sum_su2_component,
    # Central charge
    dual_central_charge_k3,
    dual_central_charge_e,
    dual_central_charge_k3e,
    # Dual OPE
    n4_dual_ope_leading_poles,
    verify_dual_ope_sign_reversal,
    # Genus expansion
    genus_g_free_energy_k3,
    genus_g_free_energy_dual_k3,
    genus_g_free_energy_k3e,
    genus_g_free_energy_dual_k3e,
    verify_genus_complementarity_k3,
    verify_genus_complementarity_k3e,
    # Bar complex
    bar_dim_1_k3,
    bar_dim_1_k3_by_sector,
    bar_dim_1_dual_k3,
    bar_dim_2_k3_estimate,
    bar_dim_1_k3e,
    bar_dim_1_dual_k3e,
    # Hochschild (bulk)
    hochschild_dim_0_k3,
    hochschild_dim_1_k3,
    hochschild_dim_2_k3,
    hochschild_polynomial_check_k3,
    # Shadow
    shadow_depth_class_k3,
    shadow_depth_class_e,
    shadow_depth_class_k3e,
    shadow_kappa_k3,
    shadow_kappa_dual_k3,
    quartic_contact_k3,
    critical_discriminant_k3,
    # FF vs Koszul (AP33)
    ff_dual_level_su2,
    ff_dual_level_su2_of_n4,
    # Homotopy vs strict (AP50)
    homotopy_vs_strict_koszul_dual_k3,
    # Boundary-to-bulk (AP25/AP34)
    boundary_bulk_passage_k3,
    # Generators
    n4_dual_generators,
    n4_dual_generator_weights,
    # Assembly
    assemble_koszul_dual_k3,
    assemble_koszul_dual_k3e,
    KoszulDualData,
    # Cross-checks
    cross_check_kappa_vs_virasoro,
    cross_check_complementarity_components,
    cross_check_ff_vs_koszul,
    full_consistency_check,
)


# =========================================================================
# PATH (a): Direct computation of kappa
# =========================================================================

class TestKappaDirectComputation:
    """Direct computation of kappa from defining formula."""

    def test_kappa_k3_equals_2(self):
        """kappa(A_{K3}) = 2."""
        assert kappa_k3() == F(2)

    def test_kappa_elliptic_curve_equals_1(self):
        """kappa(A_E) = 1."""
        assert kappa_elliptic_curve() == F(1)

    def test_kappa_k3e_equals_3(self):
        """kappa(A_{K3xE}) = 3 by additivity."""
        assert kappa_k3e() == F(3)

    def test_kappa_k3e_is_sum(self):
        """kappa(K3xE) = kappa(K3) + kappa(E)."""
        assert kappa_k3e() == kappa_k3() + kappa_elliptic_curve()

    def test_kappa_dual_k3_equals_minus_2(self):
        """kappa(A_{K3}^!) = -2."""
        assert kappa_dual_k3() == F(-2)

    def test_kappa_dual_e_equals_minus_1(self):
        """kappa(A_E^!) = -1."""
        assert kappa_dual_e() == F(-1)

    def test_kappa_dual_k3e_equals_minus_3(self):
        """kappa(A_{K3xE}^!) = -3."""
        assert kappa_dual_k3e() == F(-3)

    def test_kappa_dual_k3e_is_sum(self):
        """kappa'(K3xE) = kappa'(K3) + kappa'(E)."""
        assert kappa_dual_k3e() == kappa_dual_k3() + kappa_dual_e()

    def test_kappa_dual_cy_formula(self):
        """kappa'(CY_d) = -d for d = 1, 2, 3, 4."""
        for d in range(1, 5):
            assert kappa_dual_cy(d) == F(-d)


# =========================================================================
# PATH (b): Alternative formula verification
# =========================================================================

class TestKappaAlternativeFormulas:
    """Verify kappa from structurally different expressions."""

    def test_kappa_path_geometric(self):
        """Path 1: kappa = d = complex dimension."""
        assert kappa_k3_path_geometric() == F(2)

    def test_kappa_path_character(self):
        """Path 2: kappa = 24 * F_1 where F_1 = 1/12."""
        assert kappa_k3_path_character() == F(2)

    def test_kappa_path_n4_ward(self):
        """Path 3: kappa = 2 * k_R = 2."""
        assert kappa_k3_path_n4_ward() == F(2)

    def test_kappa_path_hodge(self):
        """Path 4: kappa = obs_1 / lambda_1 = (1/12)/(1/24) = 2."""
        assert kappa_k3_path_hodge() == F(2)

    def test_kappa_path_euler(self):
        """Path 5: kappa = chi(O_{K3}) = 2."""
        assert kappa_k3_path_euler() == F(2)

    def test_all_5_paths_agree(self):
        """All 5 independent paths give kappa = 2."""
        paths = kappa_k3_all_paths()
        assert paths['all_agree'] is True
        assert paths['kappa'] == F(2)

    def test_dual_path_complementarity(self):
        """Dual path 1: kappa' = -kappa = -2."""
        assert kappa_dual_k3_path_complementarity() == F(-2)

    def test_dual_path_geometric(self):
        """Dual path 2: kappa' = -d = -2."""
        assert kappa_dual_k3_path_geometric() == F(-2)

    def test_dual_path_n4_inversion(self):
        """Dual path 3: k_R' = -1 -> kappa' = -2."""
        assert kappa_dual_k3_path_n4_level_inversion() == F(-2)

    def test_all_3_dual_paths_agree(self):
        """All 3 dual paths give kappa' = -2."""
        paths = kappa_dual_k3_all_paths()
        assert paths['all_agree'] is True
        assert paths['kappa_dual'] == F(-2)


# =========================================================================
# PATH (c): Complementarity sum check (Theorem C)
# =========================================================================

class TestComplementaritySum:
    """Verify kappa + kappa' = 0 for CY sigma models."""

    def test_k3_complementarity_zero(self):
        """kappa(K3) + kappa(K3^!) = 0."""
        assert complementarity_sum_k3() == F(0)

    def test_k3e_complementarity_zero(self):
        """kappa(K3xE) + kappa(K3xE^!) = 0."""
        assert complementarity_sum_k3e() == F(0)

    def test_virasoro_complementarity_is_13(self):
        """AP24: kappa(Vir_6) + kappa(Vir_20) = 13."""
        assert complementarity_sum_virasoro_component() == F(13)

    def test_su2_complementarity_is_zero(self):
        """AP24: kappa(su(2)_1) + kappa(su(2)_{-5}) = 0."""
        assert complementarity_sum_su2_component() == F(0)

    def test_full_ne_virasoro_plus_su2(self):
        """Full N=4 complementarity != Virasoro + su(2) sum."""
        cc = cross_check_complementarity_components()
        assert cc['full_ne_sum_of_parts'] is True

    def test_central_charge_complementarity_k3(self):
        """c + c' = 0 for the K3 sigma model."""
        assert K3_CENTRAL_CHARGE + dual_central_charge_k3() == F(0)

    def test_central_charge_complementarity_k3e(self):
        """c + c' = 0 for K3 x E."""
        assert K3E_CENTRAL_CHARGE + dual_central_charge_k3e() == F(0)


# =========================================================================
# PATH (d): Genus expansion (F_g + F_g' = 0)
# =========================================================================

class TestGenusExpansion:
    """Verify genus-g free energies and their complementarity."""

    def test_F1_k3(self):
        """F_1(K3) = 2 * lambda_1 = 2/24 = 1/12."""
        assert genus_g_free_energy_k3(1) == F(1, 12)

    def test_F2_k3(self):
        """F_2(K3) = 2 * lambda_2 = 2 * 7/5760 = 7/2880."""
        assert genus_g_free_energy_k3(2) == F(7, 2880)

    def test_F1_dual_k3(self):
        """F_1(K3^!) = -2 * lambda_1 = -1/12."""
        assert genus_g_free_energy_dual_k3(1) == F(-1, 12)

    def test_F2_dual_k3(self):
        """F_2(K3^!) = -2 * lambda_2 = -7/2880."""
        assert genus_g_free_energy_dual_k3(2) == F(-7, 2880)

    def test_F1_k3e(self):
        """F_1(K3xE) = 3/24 = 1/8."""
        assert genus_g_free_energy_k3e(1) == F(1, 8)

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_genus_complementarity_k3(self, g):
        """F_g(K3) + F_g(K3^!) = 0 for g=1..5."""
        gc = verify_genus_complementarity_k3(g)
        assert gc['sum_is_zero'] is True

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_genus_complementarity_k3e(self, g):
        """F_g(K3xE) + F_g(K3xE^!) = 0 for g=1..5."""
        gc = verify_genus_complementarity_k3e(g)
        assert gc['sum_is_zero'] is True

    @pytest.mark.parametrize("g", [1, 2, 3, 4])
    def test_F_g_equals_kappa_times_lambda(self, g):
        """F_g = kappa * lambda_g^FP for all g."""
        Fg = genus_g_free_energy_k3(g)
        expected = F(2) * faber_pandharipande(g)
        assert Fg == expected

    def test_F_g_positive_for_k3(self):
        """F_g(K3) > 0 for all g >= 1 (kappa = 2 > 0)."""
        for g in range(1, 6):
            assert genus_g_free_energy_k3(g) > 0

    def test_F_g_negative_for_dual(self):
        """F_g(K3^!) < 0 for all g >= 1 (kappa' = -2 < 0)."""
        for g in range(1, 6):
            assert genus_g_free_energy_dual_k3(g) < 0


# =========================================================================
# PATH (e): Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Additivity, subalgebra decomposition, cross-checks."""

    def test_kappa_additivity(self):
        """kappa(A tensor B) = kappa(A) + kappa(B)."""
        assert kappa_k3e() == kappa_k3() + kappa_elliptic_curve()

    def test_kappa_dual_additivity(self):
        """kappa'(A tensor B) = kappa'(A) + kappa'(B)."""
        assert kappa_dual_k3e() == kappa_dual_k3() + kappa_dual_e()

    def test_central_charge_additivity(self):
        """c(A tensor B) = c(A) + c(B)."""
        assert K3E_CENTRAL_CHARGE == K3_CENTRAL_CHARGE + E_CENTRAL_CHARGE

    def test_dual_central_charge_additivity(self):
        """c'(A tensor B) = c'(A) + c'(B)."""
        assert (dual_central_charge_k3e() ==
                dual_central_charge_k3() + dual_central_charge_e())

    def test_bar_dim_additivity(self):
        """bar dim 1(A tensor B) = bar dim 1(A) + bar dim 1(B)."""
        assert bar_dim_1_k3e() == bar_dim_1_k3() + 1  # +1 for Heisenberg

    def test_generator_count_k3(self):
        """K3 has 8 generators: 1 Virasoro + 4 super + 3 su(2)."""
        sectors = bar_dim_1_k3_by_sector()
        assert sectors['virasoro'] == 1
        assert sectors['supercharges'] == 4
        assert sectors['su2_R'] == 3
        assert sectors['total'] == 8

    def test_koszul_dual_same_bar_dim_1(self):
        """For Koszul algebras: dim B^1(A^!) = dim B^1(A)."""
        assert bar_dim_1_dual_k3() == bar_dim_1_k3()
        assert bar_dim_1_dual_k3e() == bar_dim_1_k3e()

    def test_complementarity_different_from_virasoro(self):
        """Full N=4 complementarity (0) != Virasoro complementarity (13)."""
        assert complementarity_sum_k3() != complementarity_sum_virasoro_component()

    def test_kappa_ne_c_over_2(self):
        """AP48: kappa(A_{K3}) != c/2 = 3."""
        cc = cross_check_kappa_vs_virasoro()
        assert cc['different'] is True
        assert cc['kappa_full_n4'] == F(2)
        assert cc['kappa_vir_subalgebra'] == F(3)

    def test_kappa_ratio_two_thirds(self):
        """kappa(N=4 at c=6) / kappa(Vir_6) = 2/3."""
        cc = cross_check_kappa_vs_virasoro()
        assert cc['ratio'] == F(2, 3)


# =========================================================================
# PATH (f): Anti-pattern cross-checks
# =========================================================================

class TestAntiPatternCrossChecks:
    """Verify adherence to all relevant anti-patterns."""

    # AP19: r-matrix poles one less than OPE
    def test_ap19_rmatrix_poles(self):
        """r-matrix poles = OPE poles - 1 for all sectors."""
        poles = n4_dual_ope_leading_poles()
        for sector, data in poles.items():
            assert data['rmatrix_max_pole'] == data['ope_max_pole'] - 1, (
                f"AP19 violated in {sector}: "
                f"rmatrix={data['rmatrix_max_pole']} != "
                f"OPE-1={data['ope_max_pole']-1}"
            )

    # AP24: complementarity sums
    def test_ap24_cy_complementarity_zero(self):
        """AP24: kappa + kappa' = 0 for CY sigma models."""
        assert complementarity_sum_k3() == F(0)
        assert complementarity_sum_k3e() == F(0)

    def test_ap24_virasoro_complementarity_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        assert complementarity_sum_virasoro_component() == F(13)

    def test_ap24_km_complementarity_zero(self):
        """AP24: kappa + kappa' = 0 for affine KM."""
        assert complementarity_sum_su2_component() == F(0)

    # AP33: FF != Koszul
    def test_ap33_ff_ne_koszul(self):
        """AP33: FF dual level != Koszul dual level."""
        cc = cross_check_ff_vs_koszul()
        assert cc['are_different'] is True

    def test_ap33_ff_dual_level(self):
        """su(2) FF dual: k=1 -> k'=-5."""
        assert ff_dual_level_su2(F(1)) == F(-5)

    def test_ap33_koszul_dual_level(self):
        """N=4 Koszul dual: k_R=1 -> k_R'=-1."""
        ff_data = ff_dual_level_su2_of_n4()
        assert ff_data['koszul_dual_k_R'] == F(-1)

    def test_ap33_ff_kappa_ne_koszul_kappa(self):
        """kappa of FF dual su(2) != kappa of Koszul dual N=4."""
        cc = cross_check_ff_vs_koszul()
        assert cc['ff_kappa_ne_koszul_kappa'] is True

    # AP48: kappa depends on full algebra
    def test_ap48_kappa_not_c_over_2(self):
        """AP48: kappa(A_{K3}) = 2 != c/2 = 3."""
        assert kappa_k3() != K3_CENTRAL_CHARGE / 2
        assert kappa_k3() == F(2)

    # AP50: homotopy vs strict Koszul dual
    def test_ap50_homotopy_agrees_on_koszul_locus(self):
        """AP50: A^!_infty = A^! on the Koszul locus."""
        hvs = homotopy_vs_strict_koszul_dual_k3()
        assert hvs['is_koszul'] is True
        assert hvs['homotopy_dual_agrees_with_strict'] is True

    def test_ap50_a_infinity_formal(self):
        """AP50: on Koszul locus, m_k = 0 for k >= 3."""
        hvs = homotopy_vs_strict_koszul_dual_k3()
        assert hvs['higher_operations_vanish'] is True
        assert hvs['a_infinity_formal'] is True

    # AP25/AP34: three distinct functors
    def test_ap25_three_functors_distinct(self):
        """AP25: bar-cobar, Verdier, derived center are DIFFERENT."""
        bbp = boundary_bulk_passage_k3()
        assert bbp['bar_cobar_inversion']['result'] != bbp['koszul_duality']['result']
        assert bbp['koszul_duality']['result'] != bbp['derived_center']['result']
        assert bbp['bar_cobar_inversion']['result'] != bbp['derived_center']['result']


# =========================================================================
# Central charge tests
# =========================================================================

class TestCentralCharge:
    """Central charge of the Koszul dual."""

    def test_dual_c_k3(self):
        """c(A_{K3}^!) = -6."""
        assert dual_central_charge_k3() == F(-6)

    def test_dual_c_e(self):
        """c(A_E^!) = -1."""
        assert dual_central_charge_e() == F(-1)

    def test_dual_c_k3e(self):
        """c(A_{K3xE}^!) = -7."""
        assert dual_central_charge_k3e() == F(-7)

    def test_c_sum_zero_k3(self):
        """c + c' = 0 for K3."""
        assert K3_CENTRAL_CHARGE + dual_central_charge_k3() == F(0)

    def test_c_sum_zero_k3e(self):
        """c + c' = 0 for K3xE."""
        assert K3E_CENTRAL_CHARGE + dual_central_charge_k3e() == F(0)


# =========================================================================
# Dual OPE structure
# =========================================================================

class TestDualOPE:
    """OPE structure of the Koszul dual."""

    def test_dual_virasoro_pole(self):
        """TT OPE in dual: max pole = 4, coefficient = c'/2 = -3."""
        poles = n4_dual_ope_leading_poles()
        assert poles['TT']['ope_max_pole'] == 4
        assert poles['TT']['coefficient'] == F(-3)

    def test_dual_su2_pole(self):
        """J3J3 OPE in dual: coefficient = k_R'/2 = -1/2."""
        poles = n4_dual_ope_leading_poles()
        assert poles['J3J3']['coefficient'] == F(-1, 2)

    def test_dual_fermionic_pole(self):
        """G+G- OPE in dual: coefficient = 2k_R' = -2."""
        poles = n4_dual_ope_leading_poles()
        assert poles['GpGm']['coefficient'] == F(-2)

    def test_sign_reversal(self):
        """All dual OPE coefficients have reversed sign."""
        sr = verify_dual_ope_sign_reversal()
        assert sr['virasoro_reversed'] is True
        assert sr['su2_reversed'] is True
        assert sr['fermionic_reversed'] is True
        assert sr['c_sum_zero'] is True


# =========================================================================
# Bar complex dimensions
# =========================================================================

class TestBarComplex:
    """Bar complex structure."""

    def test_bar_dim_1_k3(self):
        assert bar_dim_1_k3() == 8

    def test_bar_dim_1_sectors(self):
        s = bar_dim_1_k3_by_sector()
        assert s['virasoro'] + s['supercharges'] + s['su2_R'] == s['total']

    def test_bar_dim_1_dual_k3(self):
        assert bar_dim_1_dual_k3() == 8

    def test_bar_dim_2_positive(self):
        assert bar_dim_2_k3_estimate() > 0

    def test_bar_dim_1_k3e(self):
        assert bar_dim_1_k3e() == 9


# =========================================================================
# Hochschild cohomology (boundary-to-bulk)
# =========================================================================

class TestHochschildCohomology:
    """Derived center / bulk algebra tests."""

    def test_hh0_is_1(self):
        """Center is 1-dimensional."""
        assert hochschild_dim_0_k3() == 1

    def test_hh1_is_1(self):
        """One outer derivation (k_R direction)."""
        assert hochschild_dim_1_k3() == 1

    def test_hh2_is_1(self):
        """One obstruction class."""
        assert hochschild_dim_2_k3() == 1

    def test_polynomial_check(self):
        """HH* is polynomial in {0,1,2}."""
        pc = hochschild_polynomial_check_k3()
        assert pc['polynomial'] is True
        assert pc['hh_geq_3_vanishes'] is True

    def test_total_hh_dim(self):
        """Total HH dim = 3."""
        pc = hochschild_polynomial_check_k3()
        assert pc['total_hh_dim'] == 3


# =========================================================================
# Shadow obstruction tower
# =========================================================================

class TestShadowTower:
    """Shadow obstruction tower data."""

    def test_k3_depth_class(self):
        assert shadow_depth_class_k3() == 'M'

    def test_e_depth_class(self):
        assert shadow_depth_class_e() == 'G'

    def test_k3e_depth_class(self):
        assert shadow_depth_class_k3e() == 'M'

    def test_shadow_kappa_k3(self):
        assert shadow_kappa_k3() == F(2)

    def test_shadow_kappa_dual_k3(self):
        assert shadow_kappa_dual_k3() == F(-2)

    def test_quartic_contact_positive(self):
        """Q^contact > 0 for c=6."""
        assert quartic_contact_k3() > 0

    def test_quartic_contact_value(self):
        """Q^contact = 10/(6*52) = 5/156."""
        assert quartic_contact_k3() == F(5, 156)

    def test_critical_discriminant_nonzero(self):
        """Delta != 0 confirms class M."""
        assert critical_discriminant_k3() != F(0)

    def test_critical_discriminant_positive(self):
        """Delta > 0 for kappa > 0 and S_4 > 0."""
        assert critical_discriminant_k3() > 0


# =========================================================================
# Dual generator data
# =========================================================================

class TestDualGenerators:
    """Generator structure of the Koszul dual."""

    def test_dual_has_8_generators(self):
        gens = n4_dual_generators()
        assert len(gens) == 8

    def test_dual_weights_preserved(self):
        """Conformal weights are preserved by Koszul duality."""
        weights = n4_dual_generator_weights()
        assert F(1) in weights
        assert F(3, 2) in weights
        assert F(2) in weights

    def test_dual_generator_parities(self):
        gens = n4_dual_generators()
        bosonic = sum(1 for g in gens if g['parity'] == 0)
        fermionic = sum(1 for g in gens if g['parity'] == 1)
        assert bosonic == 4  # T, J++, J--, J3
        assert fermionic == 4  # G+, G-, Gt+, Gt-


# =========================================================================
# Assembly and full consistency
# =========================================================================

class TestAssembly:
    """Full datum assembly and internal consistency."""

    def test_assemble_k3(self):
        kd = assemble_koszul_dual_k3()
        assert isinstance(kd, KoszulDualData)
        assert kd.kappa == F(2)
        assert kd.dual_kappa == F(-2)
        assert kd.complementarity_sum == F(0)

    def test_assemble_k3e(self):
        kd = assemble_koszul_dual_k3e()
        assert isinstance(kd, KoszulDualData)
        assert kd.kappa == F(3)
        assert kd.dual_kappa == F(-3)
        assert kd.complementarity_sum == F(0)

    def test_k3_internal_checks(self):
        kd = assemble_koszul_dual_k3()
        checks = kd.verify_internal()
        for name, val in checks.items():
            assert val is True, f"Internal check {name} failed"

    def test_k3e_internal_checks(self):
        kd = assemble_koszul_dual_k3e()
        checks = kd.verify_internal()
        for name, val in checks.items():
            assert val is True, f"Internal check {name} failed"

    def test_k3_summary_nonempty(self):
        kd = assemble_koszul_dual_k3()
        s = kd.summary()
        assert len(s) > 100
        assert 'kappa' in s

    def test_full_consistency_check(self):
        """Run ALL consistency checks."""
        checks = full_consistency_check()
        for name, val in checks.items():
            assert val is True, f"Consistency check {name} failed"

    def test_full_consistency_count(self):
        """Verify we have a substantial number of checks."""
        checks = full_consistency_check()
        assert len(checks) >= 20


# =========================================================================
# Arithmetic helpers
# =========================================================================

class TestArithmetic:
    """Basic arithmetic helper verification."""

    def test_bernoulli_0(self):
        assert bernoulli_number(0) == F(1)

    def test_bernoulli_1(self):
        assert bernoulli_number(1) == F(-1, 2)

    def test_bernoulli_2(self):
        assert bernoulli_number(2) == F(1, 6)

    def test_faber_pandharipande_1(self):
        """lambda_1 = 1/24."""
        assert faber_pandharipande(1) == F(1, 24)

    def test_faber_pandharipande_2(self):
        """lambda_2 = 7/5760."""
        assert faber_pandharipande(2) == F(7, 5760)

    def test_faber_pandharipande_positive(self):
        """lambda_g > 0 for all g >= 1."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0
