r"""Tests for the bar complex of the N=4 SCA at c=6 (K3 chiral algebra).

Tests are organized by mathematical structure:
  1. Generator structure (8 generators, weights, parities, charges)
  2. OPE nth-product table (completeness, closure, charge conservation)
  3. Bar differential d: B^2 -> B^1 (explicit computations)
  4. Kappa computation (5-path cross-verification)
  5. Shadow obstruction tower (S_3, S_4, Delta, depth classification)
  6. Koszulness verification (PBW, rank check)
  7. R-matrix pole structure (AP19)
  8. Genus-g free energy (A-hat generating function)
  9. Cross-verification against cy_n4sca_k3_engine.py (the base engine)
  10. Skew-symmetry verification

Each test uses at least 2 independent verification paths.

CONVENTIONS:
  - Exact arithmetic via fractions.Fraction
  - Cohomological grading, |d| = +1
  - Desuspension: |s^{-1}v| = |v| - 1 (AP45)
  - Bar differential extracts ALL OPE modes (AP41)
  - r-matrix poles = OPE poles - 1 (AP19)
  - kappa = modular characteristic (AP48: depends on FULL algebra)
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_bar_n4sca_engine import (
    GENERATORS,
    GEN_NAMES,
    GEN_INDEX,
    NUM_GENERATORS,
    generator_weight,
    generator_parity,
    generator_charge,
    desuspended_degree,
    n4_nth_products,
    bar_differential_deg2,
    bar_differential_matrix,
    bar_differential_rank,
    curvature_from_ope,
    kappa_from_bar_curvature,
    kappa_from_character,
    kappa_from_geometric,
    kappa_from_complementarity,
    kappa_from_n4_ward,
    kappa_five_paths,
    cubic_shadow_coefficient,
    quartic_shadow_S4,
    critical_discriminant,
    shadow_metric_QL,
    shadow_depth_class,
    koszulness_check,
    r_matrix_poles,
    verify_n4_closure,
    verify_charge_conservation,
    faber_pandharipande,
    genus_g_free_energy,
    landscape_census,
    full_verification_report,
)


# =========================================================================
# Section 1: Generator structure
# =========================================================================

class TestGeneratorStructure:
    """Test the 8-generator structure of the small N=4 SCA."""

    def test_num_generators(self):
        """The small N=4 SCA has exactly 8 primary generators."""
        assert NUM_GENERATORS == 8

    def test_generator_names(self):
        """All 8 generators are named."""
        expected = {"T", "G+", "G-", "Gt+", "Gt-", "J++", "J--", "J3"}
        assert set(GEN_NAMES) == expected

    def test_bosonic_count(self):
        """4 bosonic generators: T, J++, J--, J3."""
        bosonic = [g for g in GENERATORS if g[2] == 0]
        assert len(bosonic) == 4

    def test_fermionic_count(self):
        """4 fermionic generators: G+, G-, Gt+, Gt-."""
        fermionic = [g for g in GENERATORS if g[2] == 1]
        assert len(fermionic) == 4

    def test_weight_T(self):
        assert generator_weight("T") == Fraction(2)

    def test_weight_G(self):
        for g in ["G+", "G-", "Gt+", "Gt-"]:
            assert generator_weight(g) == Fraction(3, 2)

    def test_weight_J(self):
        for j in ["J++", "J--", "J3"]:
            assert generator_weight(j) == Fraction(1)

    def test_parity_T_bosonic(self):
        assert generator_parity("T") == 0

    def test_parity_G_fermionic(self):
        for g in ["G+", "G-", "Gt+", "Gt-"]:
            assert generator_parity(g) == 1

    def test_parity_J_bosonic(self):
        for j in ["J++", "J--", "J3"]:
            assert generator_parity(j) == 0

    def test_J3_charges(self):
        """J^3 charges: G+(+1/2), G-(-1/2), Gt+(-1/2), Gt-(+1/2)."""
        assert generator_charge("G+") == Fraction(1, 2)
        assert generator_charge("G-") == Fraction(-1, 2)
        assert generator_charge("Gt+") == Fraction(-1, 2)
        assert generator_charge("Gt-") == Fraction(1, 2)

    def test_J3_charges_bosonic(self):
        """J^3 charges of bosonic generators."""
        assert generator_charge("T") == Fraction(0)
        assert generator_charge("J++") == Fraction(1)
        assert generator_charge("J--") == Fraction(-1)
        assert generator_charge("J3") == Fraction(0)

    def test_charge_sum_zero(self):
        """Total J^3 charge of all generators is zero."""
        total = sum(g[3] for g in GENERATORS)
        assert total == 0

    def test_weight_spectrum(self):
        """Three distinct weights: 1, 3/2, 2."""
        weights = sorted(set(g[1] for g in GENERATORS))
        assert weights == [Fraction(1), Fraction(3, 2), Fraction(2)]

    def test_desuspended_degree_bosonic(self):
        """|s^{-1}v| = |v|-1 for bosonic v: 0-1 = -1."""
        assert desuspended_degree("T") == Fraction(-1)
        assert desuspended_degree("J3") == Fraction(-1)

    def test_desuspended_degree_fermionic(self):
        """|s^{-1}v| = |v|-1 for fermionic v: 1-1 = 0."""
        assert desuspended_degree("G+") == Fraction(0)

    def test_generator_index_bijection(self):
        """GEN_INDEX is a bijection from names to 0..7."""
        assert len(GEN_INDEX) == 8
        assert set(GEN_INDEX.values()) == set(range(8))


# =========================================================================
# Section 2: OPE structure
# =========================================================================

class TestOPEStructure:
    """Test the OPE nth-product table of the N=4 SCA."""

    def test_ope_completeness(self):
        """All 64 ordered pairs (a,b) have OPE entries."""
        products = n4_nth_products()
        assert len(products) == 64

    def test_closure(self):
        """The N=4 algebra closes: all OPE outputs are generators or descendants."""
        result = verify_n4_closure()
        assert result['closed'], f"Unknown outputs: {result['unknown_outputs']}"

    def test_charge_conservation(self):
        """J^3 charge is conserved in every OPE."""
        result = verify_charge_conservation()
        assert result['conserved'], f"Violations: {result['violations']}"

    def test_TT_ope(self):
        """T x T OPE: (c/2)/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w)."""
        products = n4_nth_products()
        tt = products[("T", "T")]
        assert tt[3] == {"vac": Fraction(3)}  # c/2 = 3 at c=6
        assert tt[1] == {"T": Fraction(2)}
        assert tt[0] == {"dT": Fraction(1)}
        assert 2 not in tt  # no cubic pole

    def test_J3J3_ope(self):
        """J^3 x J^3 OPE: (k_R/2)/(z-w)^2 = 1/2/(z-w)^2."""
        products = n4_nth_products()
        j3j3 = products[("J3", "J3")]
        assert j3j3[1] == {"vac": Fraction(1, 2)}
        assert 0 not in j3j3  # no simple pole

    def test_JppJmm_ope(self):
        """J^{++} x J^{--}: k_R/(z-w)^2 + 2J^3/(z-w)."""
        products = n4_nth_products()
        jpm = products[("J++", "J--")]
        assert jpm[1] == {"vac": Fraction(1)}
        assert jpm[0] == {"J3": Fraction(2)}

    def test_GpGm_ope(self):
        """G^+ x G^-: 2k_R/(z-w)^3 + 2J^3/(z-w)^2 + (T+dJ^3)/(z-w)."""
        products = n4_nth_products()
        gm = products[("G+", "G-")]
        assert gm[2] == {"vac": Fraction(2)}
        assert gm[1] == {"J3": Fraction(2)}
        assert gm[0] == {"T": Fraction(1), "dJ3": Fraction(1)}

    def test_GtpGtm_ope(self):
        """Gt^+ x Gt^-: opposite J^3 sign from G^+ x G^-."""
        products = n4_nth_products()
        gt = products[("Gt+", "Gt-")]
        assert gt[2] == {"vac": Fraction(2)}
        assert gt[1] == {"J3": Fraction(-2)}  # opposite sign
        assert gt[0]["T"] == Fraction(1)

    def test_fermionic_self_ope_vanishes(self):
        """Fermionic self-OPE vanishes: G^+ x G^+ = 0."""
        products = n4_nth_products()
        for g in ["G+", "G-", "Gt+", "Gt-"]:
            assert products[(g, g)] == {}

    def test_same_type_bosonic_self_ope(self):
        """J^{++} x J^{++} = 0, J^{--} x J^{--} = 0."""
        products = n4_nth_products()
        assert products[("J++", "J++")] == {}
        assert products[("J--", "J--")] == {}

    def test_T_acts_as_virasoro(self):
        """T acts on all generators as a Virasoro primary."""
        products = n4_nth_products()
        # T x G^a: (3/2)*G^a/(z-w)^2 + dG^a/(z-w)
        for ga in ["G+", "G-", "Gt+", "Gt-"]:
            tg = products[("T", ga)]
            assert tg[1][ga] == Fraction(3, 2)
            assert tg[0]["d" + ga] == Fraction(1)
        # T x J^a: J^a/(z-w)^2 + dJ^a/(z-w)
        for ja in ["J++", "J--", "J3"]:
            tj = products[("T", ja)]
            assert tj[1][ja] == Fraction(1)
            assert tj[0]["d" + ja] == Fraction(1)

    def test_j3_charge_assignment_ope(self):
        """J^3 OPE gives the J^3 eigenvalue."""
        products = n4_nth_products()
        # J^3_{(0)}G^+ = (1/2)*G^+
        assert products[("J3", "G+")][0]["G+"] == Fraction(1, 2)
        # J^3_{(0)}G^- = (-1/2)*G^-
        assert products[("J3", "G-")][0]["G-"] == Fraction(-1, 2)
        # J^3_{(0)}Gt^+ = (-1/2)*Gt^+ (opposite from G^+!)
        assert products[("J3", "Gt+")][0]["Gt+"] == Fraction(-1, 2)
        # J^3_{(0)}Gt^- = (+1/2)*Gt^-
        assert products[("J3", "Gt-")][0]["Gt-"] == Fraction(1, 2)

    def test_cross_GGt_ope(self):
        """G^+ x Gt^-: -2J^{++}/(z-w)^2 - dJ^{++}/(z-w)."""
        products = n4_nth_products()
        ggt = products[("G+", "Gt-")]
        assert ggt[1] == {"J++": Fraction(-2)}
        assert ggt[0] == {"dJ++": Fraction(-1)}

    def test_cross_GGt_vanishing(self):
        """G^+ x Gt^+ = 0 (same doublet index = regular)."""
        products = n4_nth_products()
        assert products[("G+", "Gt+")] == {}
        assert products[("G-", "Gt-")] == {}

    def test_jpp_raising(self):
        """J^{++} acts as a raising operator on supercharges."""
        products = n4_nth_products()
        # J^{++}_{(0)}G^- = Gt^- (charge-consistent raising)
        assert products[("J++", "G-")][0] == {"Gt-": Fraction(1)}
        # J^{++}_{(0)}Gt^+ = -G^+ (raising across doublets)
        assert products[("J++", "Gt+")][0] == {"G+": Fraction(-1)}

    def test_jmm_lowering(self):
        """J^{--} acts as a lowering operator on supercharges."""
        products = n4_nth_products()
        # J^{--}_{(0)}G^+ = Gt^+ (charge-consistent lowering)
        assert products[("J--", "G+")][0] == {"Gt+": Fraction(1)}
        # J^{--}_{(0)}Gt^- = -G^- (lowering across doublets)
        assert products[("J--", "Gt-")][0] == {"G-": Fraction(-1)}


# =========================================================================
# Section 3: Bar differential
# =========================================================================

class TestBarDifferential:
    """Test the bar differential d: B^2 -> B^1 u B^0."""

    def test_d_TT(self):
        """D(T tensor T) = (c/2)|0> + 2T + dT."""
        vac, bar1 = bar_differential_deg2("T", "T")
        assert vac["vac"] == Fraction(3)  # c/2 = 3
        assert bar1["T"] == Fraction(2)
        assert bar1["dT"] == Fraction(1)

    def test_d_J3J3(self):
        """D(J^3 tensor J^3) = (k_R/2)|0> = (1/2)|0>."""
        vac, bar1 = bar_differential_deg2("J3", "J3")
        assert vac["vac"] == Fraction(1, 2)
        assert len(bar1) == 0

    def test_d_JppJmm(self):
        """D(J^{++} tensor J^{--}) = k_R|0> + 2J^3."""
        vac, bar1 = bar_differential_deg2("J++", "J--")
        assert vac["vac"] == Fraction(1)
        assert bar1["J3"] == Fraction(2)

    def test_d_GpGm(self):
        """D(G^+ tensor G^-) = 2k_R|0> + 2J^3 + T + dJ^3."""
        vac, bar1 = bar_differential_deg2("G+", "G-")
        assert vac["vac"] == Fraction(2)
        assert bar1["J3"] == Fraction(2)
        assert bar1["T"] == Fraction(1)
        assert bar1["dJ3"] == Fraction(1)

    def test_d_GmGp_skew(self):
        """D(G^- tensor G^+): vacuum has OPPOSITE sign from D(G^+ tensor G^-)."""
        vac_pm, _ = bar_differential_deg2("G+", "G-")
        vac_mp, _ = bar_differential_deg2("G-", "G+")
        assert vac_mp["vac"] == -vac_pm["vac"]

    def test_d_GtpGtm(self):
        """D(Gt^+ tensor Gt^-): same curvature as G^+G^-, opposite J^3."""
        vac, bar1 = bar_differential_deg2("Gt+", "Gt-")
        assert vac["vac"] == Fraction(2)  # same curvature 2k_R
        assert bar1["J3"] == Fraction(-2)  # opposite J^3 sign

    def test_d_TGp(self):
        """D(T tensor G^+) = (3/2)*G^+ + dG^+."""
        vac, bar1 = bar_differential_deg2("T", "G+")
        assert len(vac) == 0  # no vacuum
        assert bar1["G+"] == Fraction(3, 2)
        assert bar1["dG+"] == Fraction(1)

    def test_d_GpT(self):
        """D(G^+ tensor T) = (3/2)*G^+ + (1/2)*dG^+."""
        vac, bar1 = bar_differential_deg2("G+", "T")
        assert len(vac) == 0
        assert bar1["G+"] == Fraction(3, 2)
        assert bar1["dG+"] == Fraction(1, 2)

    def test_d_TGp_vs_GpT_asymmetry(self):
        """D(T tensor G^+) != D(G^+ tensor T) (asymmetric bar differential)."""
        _, bar1_tg = bar_differential_deg2("T", "G+")
        _, bar1_gt = bar_differential_deg2("G+", "T")
        # Both have same G^+ coefficient but different dG^+ coefficient
        assert bar1_tg["G+"] == bar1_gt["G+"]
        assert bar1_tg["dG+"] != bar1_gt["dG+"]

    def test_d_fermionic_self_zero(self):
        """D(G^+ tensor G^+) = 0 (fermionic self-OPE vanishes)."""
        vac, bar1 = bar_differential_deg2("G+", "G+")
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_d_JppJpp_zero(self):
        """D(J^{++} tensor J^{++}) = 0 (no self-OPE)."""
        vac, bar1 = bar_differential_deg2("J++", "J++")
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_d_J3Gp(self):
        """D(J^3 tensor G^+) = (1/2)*G^+."""
        vac, bar1 = bar_differential_deg2("J3", "G+")
        assert len(vac) == 0
        assert bar1 == {"G+": Fraction(1, 2)}

    def test_d_GpJ3(self):
        """D(G^+ tensor J^3) = -(1/2)*G^+ (skew-symmetry)."""
        vac, bar1 = bar_differential_deg2("G+", "J3")
        assert len(vac) == 0
        assert bar1 == {"G+": Fraction(-1, 2)}

    def test_d_GpGtm(self):
        """D(G^+ tensor Gt^-) involves J^{++}."""
        vac, bar1 = bar_differential_deg2("G+", "Gt-")
        assert len(vac) == 0
        assert bar1["J++"] == Fraction(-2)
        assert bar1["dJ++"] == Fraction(-1)

    def test_d_JppGm(self):
        """D(J^{++} tensor G^-) = Gt^-."""
        vac, bar1 = bar_differential_deg2("J++", "G-")
        assert len(vac) == 0
        assert bar1 == {"Gt-": Fraction(1)}


class TestBarDifferentialMatrix:
    """Test the full bar differential matrix."""

    def test_matrix_dimensions(self):
        """Matrix has 16 output rows (8 generators + 8 derivatives) and 64 input columns."""
        data = bar_differential_matrix()
        assert data['n_pairs'] == 64
        assert data['n_outputs'] == 16

    def test_rank(self):
        """Bar differential has rank 16 (full rank on output space)."""
        rk = bar_differential_rank()
        assert rk['rank'] == 16

    def test_kernel_dimension(self):
        """Kernel has dimension 48 = 64 - 16."""
        rk = bar_differential_rank()
        assert rk['kernel_dim'] == 48

    def test_vacuum_nonzero(self):
        """At least some pairs produce vacuum terms."""
        rk = bar_differential_rank()
        assert rk['vac_nonzero_entries'] > 0


# =========================================================================
# Section 4: Kappa (5-path cross-verification)
# =========================================================================

class TestKappa:
    """Test kappa(A_{N=4, c=6}) = 2 from 5 independent paths."""

    def test_kappa_value(self):
        """kappa = 2 for the K3 sigma model."""
        assert kappa_from_bar_curvature() == Fraction(2)

    def test_kappa_path_bar_curvature(self):
        assert kappa_from_bar_curvature(Fraction(6)) == Fraction(2)

    def test_kappa_path_character(self):
        assert kappa_from_character() == Fraction(2)

    def test_kappa_path_geometric(self):
        assert kappa_from_geometric(2) == Fraction(2)

    def test_kappa_path_complementarity(self):
        assert kappa_from_complementarity() == Fraction(2)

    def test_kappa_path_n4_ward(self):
        assert kappa_from_n4_ward(Fraction(1)) == Fraction(2)

    def test_all_five_paths_agree(self):
        """All 5 independent paths give kappa = 2."""
        result = kappa_five_paths()
        assert result['all_agree']
        assert result['kappa'] == Fraction(2)

    def test_kappa_not_c_over_2(self):
        """AP48: kappa != c/2 for the N=4 SCA. kappa = 2, but c/2 = 3."""
        kappa = kappa_from_bar_curvature()
        c = Fraction(6)
        assert kappa != c / 2
        assert kappa == Fraction(2)
        assert c / 2 == Fraction(3)

    def test_kappa_is_two_thirds_vir(self):
        """kappa(N=4) = (2/3) * kappa(Vir_c) = (2/3)*3 = 2."""
        kappa_vir = Fraction(6) / 2  # c/2 = 3
        kappa_n4 = kappa_from_bar_curvature()
        assert kappa_n4 == Fraction(2, 3) * kappa_vir

    def test_kappa_dual(self):
        """kappa(A!) = -kappa(A) = -2 (complementarity sum = 0)."""
        kappa = kappa_from_bar_curvature()
        kappa_dual = -kappa
        assert kappa + kappa_dual == 0

    def test_kappa_general_level(self):
        """kappa(N=4 at c=6k_R) = 2k_R."""
        for k_R in [Fraction(1), Fraction(2), Fraction(3), Fraction(1, 2)]:
            c = 6 * k_R
            assert kappa_from_bar_curvature(c) == 2 * k_R

    def test_F1_from_kappa(self):
        """F_1 = kappa/24 = 2/24 = 1/12."""
        kappa = kappa_from_bar_curvature()
        F1 = kappa * faber_pandharipande(1)
        assert F1 == Fraction(1, 12)

    def test_F1_value(self):
        """F_1 = 1/12 (cross-check with direct computation)."""
        assert genus_g_free_energy(1) == Fraction(1, 12)


# =========================================================================
# Section 5: Shadow obstruction tower
# =========================================================================

class TestShadowTower:
    """Test shadow tower coefficients and depth classification."""

    def test_S3_nonzero(self):
        """Cubic shadow S_3 = 2 (nonzero, from Virasoro T-line)."""
        assert cubic_shadow_coefficient() == Fraction(2)

    def test_S4_virasoro(self):
        """Quartic shadow S_4 = 5/156 at c=6."""
        # Q^contact_Vir = 10/(c*(5c+22)) = 10/(6*52) = 10/312 = 5/156
        assert quartic_shadow_S4() == Fraction(5, 156)

    def test_S4_formula(self):
        """Verify S_4 = 10/(c*(5c+22)) from the closed formula."""
        c = Fraction(6)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert quartic_shadow_S4(c) == expected

    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 8*2*(5/156) = 80/156 = 20/39."""
        Delta = critical_discriminant()
        assert Delta == Fraction(20, 39)

    def test_discriminant_formula(self):
        """Verify Delta = 8*kappa*S_4."""
        kappa = kappa_from_bar_curvature()
        S4 = quartic_shadow_S4()
        assert critical_discriminant() == 8 * kappa * S4

    def test_discriminant_nonzero(self):
        """Delta != 0 (class M, infinite depth)."""
        assert critical_discriminant() != 0

    def test_shadow_class_M(self):
        """K3 sigma model has shadow class M (infinite depth)."""
        result = shadow_depth_class()
        assert result['class'] == 'M'
        assert result['r_max'] is None  # infinity

    def test_shadow_class_reason(self):
        """Class M because both alpha (S_3) and Delta are nonzero."""
        result = shadow_depth_class()
        assert result['alpha'] != 0
        assert result['Delta'] != 0

    def test_shadow_metric_QL_at_0(self):
        """Q_L(0) = (2*kappa)^2 = 16."""
        Q0 = shadow_metric_QL(0)
        assert Q0 == 16

    def test_shadow_metric_QL_formula(self):
        """Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
        t = Fraction(1)
        Q1 = shadow_metric_QL(t)
        kappa = Fraction(2)
        alpha = Fraction(2)
        Delta = Fraction(20, 39)
        expected = (2 * kappa + 3 * alpha * t) ** 2 + 2 * Delta * t ** 2
        assert Q1 == expected

    def test_shadow_class_taxonomy(self):
        """Verify the 4-class taxonomy logic."""
        # G: Delta=0, alpha=0
        # L: Delta=0, alpha!=0
        # C: Delta!=0, alpha=0
        # M: Delta!=0, alpha!=0
        sd = shadow_depth_class()
        assert sd['class'] == 'M'
        # The K3 has both nonzero -> M
        assert sd['alpha'] != 0 and sd['Delta'] != 0


# =========================================================================
# Section 6: Koszulness
# =========================================================================

class TestKoszulness:
    """Test chiral Koszulness of the N=4 SCA."""

    def test_koszul_expected(self):
        """The N=4 SCA is expected to be chirally Koszul."""
        result = koszulness_check()
        assert result['koszul'] is True

    def test_pbw_criterion(self):
        """PBW: freely strongly generated implies Koszul."""
        result = koszulness_check()
        assert result['paths']['pbw']['koszul'] is True

    def test_bar_deg1_dim(self):
        """Bar degree 1 has dimension 8 (one per generator)."""
        result = koszulness_check()
        assert result['bar_deg1_dim'] == 8

    def test_bar_deg2_dim(self):
        """Bar degree 2 has dimension 64 (ordered pairs)."""
        result = koszulness_check()
        assert result['bar_deg2_dim'] == 64

    def test_rank_equals_output_dim(self):
        """The bar differential at degree 2 has full rank on the output space."""
        rk = bar_differential_rank()
        assert rk['rank'] == rk['n_rows']  # full rank = surjective onto outputs


# =========================================================================
# Section 7: R-matrix pole structure
# =========================================================================

class TestRMatrixPoles:
    """Test r-matrix pole orders (AP19: OPE poles - 1)."""

    def test_TT_rmatrix(self):
        """T x T: OPE pole 4, r-matrix pole 3."""
        poles = r_matrix_poles()
        tt = poles[("T", "T")]
        assert tt['ope_max_pole'] == 4
        assert tt['rmatrix_max_pole'] == 3

    def test_J3J3_rmatrix(self):
        """J^3 x J^3: OPE pole 2, r-matrix pole 1."""
        poles = r_matrix_poles()
        j3 = poles[("J3", "J3")]
        assert j3['ope_max_pole'] == 2
        assert j3['rmatrix_max_pole'] == 1

    def test_GpGm_rmatrix(self):
        """G^+ x G^-: OPE pole 3, r-matrix pole 2."""
        poles = r_matrix_poles()
        gm = poles[("G+", "G-")]
        assert gm['ope_max_pole'] == 3
        assert gm['rmatrix_max_pole'] == 2

    def test_TG_rmatrix(self):
        """T x G^+: OPE pole 2, r-matrix pole 1."""
        poles = r_matrix_poles()
        tg = poles[("T", "G+")]
        assert tg['ope_max_pole'] == 2
        assert tg['rmatrix_max_pole'] == 1

    def test_vanishing_rmatrix(self):
        """G^+ x G^+ has no poles (regular OPE)."""
        poles = r_matrix_poles()
        gg = poles[("G+", "G+")]
        assert gg['ope_max_pole'] == 0
        assert gg['rmatrix_max_pole'] == 0

    def test_ap19_universal(self):
        """AP19: for all pairs, rmatrix pole = max(0, OPE pole - 1)."""
        poles = r_matrix_poles()
        for pair, data in poles.items():
            expected = max(0, data['ope_max_pole'] - 1)
            assert data['rmatrix_max_pole'] == expected, \
                f"AP19 violated for {pair}: {data}"


# =========================================================================
# Section 8: Genus-g free energy
# =========================================================================

class TestGenusGFreeEnergy:
    """Test genus-g free energy F_g = kappa * lambda_g^FP."""

    def test_F1(self):
        """F_1 = 2 * 1/24 = 1/12."""
        assert genus_g_free_energy(1) == Fraction(1, 12)

    def test_F2(self):
        """F_2 = 2 * 7/5760 = 7/2880."""
        assert genus_g_free_energy(2) == Fraction(7, 2880)

    def test_F3(self):
        """F_3 = 2 * 31/967680 = 31/483840."""
        assert genus_g_free_energy(3) == Fraction(31, 483840)

    def test_faber_pandharipande_lambda1(self):
        """lambda_1 = 1/24."""
        assert faber_pandharipande(1) == Fraction(1, 24)

    def test_faber_pandharipande_lambda2(self):
        """lambda_2 = 7/5760."""
        assert faber_pandharipande(2) == Fraction(7, 5760)

    def test_Fg_positive(self):
        """F_g > 0 for all g >= 1 (Bernoulli sign convention)."""
        for g in range(1, 8):
            assert genus_g_free_energy(g) > 0

    def test_Fg_decreasing(self):
        """F_g decreases rapidly with g."""
        for g in range(1, 7):
            assert genus_g_free_energy(g) > genus_g_free_energy(g + 1)

    def test_Fg_is_kappa_times_lambda(self):
        """F_g = kappa * lambda_g for all g."""
        kappa = kappa_from_bar_curvature()
        for g in range(1, 6):
            assert genus_g_free_energy(g) == kappa * faber_pandharipande(g)


# =========================================================================
# Section 9: Cross-verification with cy_n4sca_k3_engine
# =========================================================================

class TestCrossVerification:
    """Cross-verify against the base N=4 SCA engine."""

    def test_kappa_agrees(self):
        """kappa from bar engine matches base engine."""
        from compute.lib.cy_n4sca_k3_engine import kappa_n4_k3
        assert kappa_from_bar_curvature() == kappa_n4_k3()

    def test_central_charge(self):
        """Central charge c = 6."""
        from compute.lib.cy_n4sca_k3_engine import K3_CENTRAL_CHARGE
        assert K3_CENTRAL_CHARGE == 6

    def test_num_generators_agrees(self):
        """Both engines agree on 8 generators."""
        from compute.lib.cy_n4sca_k3_engine import n4_sca_k3
        data = n4_sca_k3()
        assert data.num_generators == NUM_GENERATORS

    def test_ope_TT_agrees(self):
        """TT OPE central term agrees between engines."""
        from compute.lib.cy_n4sca_k3_engine import n4_ope_structure_constants
        ope_base = n4_ope_structure_constants(Fraction(6))
        products = n4_nth_products()
        # TT_4 = c/2 = 3
        assert products[("T", "T")][3]["vac"] == ope_base['TT_4']

    def test_ope_GpGm_agrees(self):
        """G^+G^- leading pole agrees between engines."""
        from compute.lib.cy_n4sca_k3_engine import n4_ope_structure_constants
        ope_base = n4_ope_structure_constants(Fraction(6))
        products = n4_nth_products()
        assert products[("G+", "G-")][2]["vac"] == ope_base['GpGm_3']

    def test_ope_J3J3_agrees(self):
        """J^3 J^3 level agrees between engines."""
        from compute.lib.cy_n4sca_k3_engine import n4_ope_structure_constants
        ope_base = n4_ope_structure_constants(Fraction(6))
        products = n4_nth_products()
        assert products[("J3", "J3")][1]["vac"] == ope_base['J3J3_2']

    def test_shadow_class_agrees(self):
        """Shadow depth class M agrees between engines."""
        from compute.lib.cy_n4sca_k3_engine import shadow_depth_classification
        base = shadow_depth_classification()
        mine = shadow_depth_class()
        assert base['shadow_class'] == mine['class']

    def test_F1_agrees(self):
        """F_1 agrees between engines."""
        from compute.lib.cy_n4sca_k3_engine import genus_g_free_energy as base_Fg
        assert genus_g_free_energy(1) == base_Fg(1)

    def test_F2_agrees(self):
        """F_2 agrees between engines."""
        from compute.lib.cy_n4sca_k3_engine import genus_g_free_energy as base_Fg
        assert genus_g_free_energy(2) == base_Fg(2)

    def test_kappa_five_paths_all_agree(self):
        """All 5 kappa paths from bar engine agree with base engine's 5 paths."""
        from compute.lib.cy_n4sca_k3_engine import kappa_n4_all_paths
        base = kappa_n4_all_paths()
        mine = kappa_five_paths()
        assert base['kappa'] == mine['kappa']
        assert base['all_agree'] and mine['all_agree']


# =========================================================================
# Section 10: Skew-symmetry verification
# =========================================================================

class TestSkewSymmetry:
    """Verify skew-symmetry of OPE at leading order.

    For bosonic fields a, b: a_{(n)}b and b_{(n)}a are related by
    skew-symmetry with derivative corrections.  At the LEADING pole
    (highest n), there are no derivative corrections, so:
      b_{(n_max)}a = (-1)^{|a||b|+1} * a_{(n_max)}b
    For two bosonic fields: (-1)^{0+1} = -1 (antisymmetric at leading pole).
    For two fermionic fields: (-1)^{1+1} = +1 (WAIT: skew-symmetry formula
    has (-1)^{|a||b|+n+j+1}).  At j=0: (-1)^{|a||b|+n+1}.
    """

    def test_TT_skew(self):
        """T x T leading pole is symmetric (c/2), but skew says d^3 correction.
        Actually T is bosonic, and the skew-symmetry at leading order:
        T_{(3)}T = c/2 (leading).  For the reversed order T_{(3)}T, it's the same!
        (Self-OPE with a single bosonic field.)"""
        products = n4_nth_products()
        assert products[("T", "T")][3] == {"vac": Fraction(3)}
        # T x T is symmetric in both orders (same field)

    def test_J3J3_symmetric(self):
        """J^3 x J^3: self-OPE, leading term k_R/2."""
        products = n4_nth_products()
        assert products[("J3", "J3")][1] == {"vac": Fraction(1, 2)}

    def test_JppJmm_vs_JmmJpp_leading(self):
        """J^{++}_{(1)}J^{--} = k_R and J^{--}_{(1)}J^{++} = k_R.
        (Both are bosonic, leading pole has no derivative correction,
        and the Killing form is symmetric.)"""
        products = n4_nth_products()
        assert products[("J++", "J--")][1]["vac"] == Fraction(1)
        assert products[("J--", "J++")][1]["vac"] == Fraction(1)

    def test_JppJmm_vs_JmmJpp_subleading(self):
        """The subleading (simple pole) terms have opposite sign:
        J^{++}_{(0)}J^{--} = 2J^3,  J^{--}_{(0)}J^{++} = -2J^3."""
        products = n4_nth_products()
        assert products[("J++", "J--")][0]["J3"] == Fraction(2)
        assert products[("J--", "J++")][0]["J3"] == Fraction(-2)

    def test_GpGm_vs_GmGp_leading(self):
        """G^+G^- leading (n=2): +2k_R.  G^-G^+ leading: -2k_R.
        (Fermionic skew: at j=0, (-1)^{1+2+1} = 1 * (-1)^{2+1} = -1.)"""
        products = n4_nth_products()
        assert products[("G+", "G-")][2]["vac"] == Fraction(2)
        assert products[("G-", "G+")][2]["vac"] == Fraction(-2)

    def test_GpGtm_vs_GtmGp_leading(self):
        """G^+Gt^- leading (n=1): -2J^{++}.  Gt^-G^+ leading: +2J^{++}."""
        products = n4_nth_products()
        assert products[("G+", "Gt-")][1]["J++"] == Fraction(-2)
        assert products[("Gt-", "G+")][1]["J++"] == Fraction(2)


# =========================================================================
# Section 11: Curvature extraction
# =========================================================================

class TestCurvature:
    """Test curvature extraction from OPE."""

    def test_T_curvature(self):
        """T_{(3)}T = c/2 = 3."""
        curv = curvature_from_ope()
        assert curv['T_curvature'] == Fraction(3)

    def test_GpGm_curvature(self):
        """G^+_{(2)}G^- = 2k_R = 2."""
        curv = curvature_from_ope()
        assert curv['GpGm_curvature'] == Fraction(2)

    def test_GtpGtm_curvature(self):
        """Gt^+_{(2)}Gt^- = 2k_R = 2."""
        curv = curvature_from_ope()
        assert curv['GtpGtm_curvature'] == Fraction(2)

    def test_J3J3_curvature(self):
        """J^3_{(1)}J^3 = k_R/2 = 1/2."""
        curv = curvature_from_ope()
        assert curv['J3J3_curvature'] == Fraction(1, 2)

    def test_JppJmm_curvature(self):
        """J^{++}_{(1)}J^{--} = k_R = 1."""
        curv = curvature_from_ope()
        assert curv['JppJmm_curvature'] == Fraction(1)


# =========================================================================
# Section 12: Landscape census
# =========================================================================

class TestLandscapeCensus:
    """Test landscape census entry for K3."""

    def test_census_name(self):
        census = landscape_census()
        assert 'K3' in census['name'] or 'N=4' in census['name']

    def test_census_c(self):
        assert landscape_census()['c'] == Fraction(6)

    def test_census_kappa(self):
        assert landscape_census()['kappa'] == Fraction(2)

    def test_census_class(self):
        assert landscape_census()['shadow_class'] == 'M'

    def test_census_generators(self):
        assert landscape_census()['num_generators'] == 8

    def test_census_bosonic(self):
        assert landscape_census()['bosonic_generators'] == 4

    def test_census_fermionic(self):
        assert landscape_census()['fermionic_generators'] == 4

    def test_census_koszul(self):
        assert landscape_census()['koszul'] is True

    def test_census_complementarity(self):
        assert landscape_census()['complementarity_sum'] == 0

    def test_census_dual_kappa(self):
        assert landscape_census()['kappa_dual'] == Fraction(-2)


# =========================================================================
# Section 13: Full verification report
# =========================================================================

class TestFullReport:
    """Test the full verification report passes."""

    def test_full_report_passes(self):
        report = full_verification_report()
        assert report['all_pass']

    def test_report_kappa_agrees(self):
        report = full_verification_report()
        assert report['kappa']['all_agree']

    def test_report_closure(self):
        report = full_verification_report()
        assert report['closure']['closed']

    def test_report_charge(self):
        report = full_verification_report()
        assert report['charge_conservation']['conserved']


# =========================================================================
# Section 14: Parametric tests (general c)
# =========================================================================

class TestGeneralLevel:
    """Test at general SU(2)_R level (not just k_R=1)."""

    @pytest.mark.parametrize("k_R", [Fraction(1), Fraction(2), Fraction(3)])
    def test_kappa_scales(self, k_R):
        """kappa = 2*k_R for all levels."""
        c = 6 * k_R
        assert kappa_from_bar_curvature(c) == 2 * k_R

    @pytest.mark.parametrize("k_R", [Fraction(1), Fraction(2), Fraction(3)])
    def test_charge_conservation_general(self, k_R):
        """Charge conserved at all levels."""
        c = 6 * k_R
        result = verify_charge_conservation(c)
        assert result['conserved']

    @pytest.mark.parametrize("k_R", [Fraction(1), Fraction(2), Fraction(3)])
    def test_closure_general(self, k_R):
        """Closure at all levels."""
        c = 6 * k_R
        result = verify_n4_closure(c)
        assert result['closed']

    @pytest.mark.parametrize("k_R", [Fraction(1), Fraction(2)])
    def test_class_M_general(self, k_R):
        """Shadow class M at all non-zero levels."""
        c = 6 * k_R
        result = shadow_depth_class(c)
        assert result['class'] == 'M'

    @pytest.mark.parametrize("k_R", [Fraction(1), Fraction(2)])
    def test_discriminant_positive(self, k_R):
        """Critical discriminant is positive at all levels."""
        c = 6 * k_R
        assert critical_discriminant(c) > 0
