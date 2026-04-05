r"""Tests for the symplectic duality engine: Theorem C as Coulomb/Higgs correspondence.

MANDATE: 80+ tests across 6 verification paths.

VERIFICATION PATHS:
  Path 1: Direct complementarity computation (Theorem C)
  Path 2: Symplectic duality from 3D N=4 gauge theory data
  Path 3: Lagrangian condition verification
  Path 4: Coulomb branch / Yangian comparison
  Path 5: Known mirror pairs from the literature
  Path 6: Heisenberg limit as baseline

CRITICAL REGRESSION CHECKS:
  AP1:  kappa formulas recomputed per family, never copied
  AP8:  Virasoro self-dual at c=13, NOT c=26
  AP19: r-matrix pole order one below OPE
  AP24: kappa+kappa' = 13 for Virasoro (NOT 0)
  AP29: delta_kappa != kappa_eff
  AP33: H_k^! = Sym^ch(V*) != H_{-k} as algebras
  AP39: kappa != c/2 for affine at rank > 1

References:
  higher_genus_complementarity.tex: thm:quantum-complementarity-main
  higher_genus_complementarity.tex: thm:ambient-complementarity-fmp
  higher_genus_complementarity.tex: prop:ptvv-lagrangian
  Braden-Licata-Proudfoot-Webster, arXiv:1208.3863
  Braverman-Finkelberg-Nakajima, arXiv:1601.03586
"""

from __future__ import annotations

import pytest
from fractions import Fraction

from compute.lib.symplectic_duality_engine import (
    # Kappa functions
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine,
    kappa_wn,
    kappa_dual_heisenberg,
    kappa_dual_virasoro,
    kappa_dual_affine,
    # Complementarity sums
    complementarity_sum_heisenberg,
    complementarity_sum_virasoro,
    complementarity_sum_affine,
    # Central charges
    central_charge_affine_sl,
    central_charge_wn,
    # Feigin-Frenkel
    ff_dual_level,
    koszul_dual_central_charge_virasoro,
    # Shifted symplectic
    ptvv_shift,
    formal_moduli_shift,
    compute_shifted_symplectic_data,
    ShiftedSymplecticData,
    # Gauge theory data
    GaugeTheoryDatum,
    pure_su2_datum,
    sqcd_su2_nf4_datum,
    a1_hypertoric_datum,
    an_hypertoric_datum,
    jordan_quiver_datum,
    affine_sl_n_gauge_datum,
    argyres_douglas_h0_virasoro,
    # Shadow data
    ShadowGaugeData,
    virasoro_shadow_metric_coefficients,
    virasoro_critical_discriminant,
    heisenberg_shadow_data,
    virasoro_shadow_data,
    affine_sl2_shadow_data,
    # Lagrangian verification
    LagrangianVerification,
    verify_lagrangian_heisenberg,
    verify_lagrangian_virasoro,
    verify_lagrangian_affine,
    # Coulomb branch
    CoulombBranchData,
    coulomb_branch_a1,
    coulomb_branch_an,
    coulomb_branch_virasoro,
    # Mirror symmetry
    shadow_connection_data_virasoro,
    discriminant_complementarity_sum,
    # Hypertoric
    hypertoric_an_complementarity,
    # Nakajima
    nakajima_quiver_shadow,
    # Genus-g complementarity
    faber_pandharipande,
    genus_g_complementarity,
    # Full landscape
    full_landscape_symplectic_duality,
    # Shadow radius
    shadow_growth_rate_virasoro,
    mirror_shadow_radii,
    # Dimensional check
    symplectic_dim_check,
    # Cross-verification
    cross_verify_complementarity,
    # Argyres-Douglas
    ArgyresDouglasData,
    argyres_douglas_A1_A2n,
    # Master table
    master_verification_table,
)


# =========================================================================
# PATH 1: DIRECT COMPLEMENTARITY (Theorem C scalar level)
# =========================================================================

class TestDirectComplementarityHeisenberg:
    """Path 1: kappa + kappa^! = 0 for Heisenberg (all levels)."""

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10, -1, -3, Fraction(1, 2), Fraction(7, 3)])
    def test_sum_is_zero(self, k_val):
        """kappa(H_k) + kappa(H_k^!) = k + (-k) = 0."""
        s = complementarity_sum_heisenberg(k_val)
        assert s == Fraction(0), f"Heisenberg k={k_val}: sum={s}, expected 0"

    def test_kappa_values(self):
        assert kappa_heisenberg(1) == Fraction(1)
        assert kappa_heisenberg(Fraction(1, 2)) == Fraction(1, 2)
        assert kappa_dual_heisenberg(1) == Fraction(-1)
        assert kappa_dual_heisenberg(Fraction(7, 3)) == Fraction(-7, 3)


class TestDirectComplementarityVirasoro:
    """Path 1: kappa + kappa^! = 13 for Virasoro (AP24 regression).

    CRITICAL: the sum is 13, NOT 0.  The overclaim kappa+kappa'=0
    for all families was wrong (AP24: required 3-4 commits to fix).
    """

    @pytest.mark.parametrize("c_val", [
        Fraction(1, 2),  # Ising
        1,               # c=1 free boson boundary
        Fraction(-22, 5),  # Lee-Yang (H_0)
        13,              # self-dual point (AP8)
        25,
        26,              # bosonic string critical
        Fraction(152, 5),  # dual of Lee-Yang
        0,               # edge case
        -1,              # negative c
    ])
    def test_sum_is_13(self, c_val):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for ALL c."""
        s = complementarity_sum_virasoro(c_val)
        assert s == Fraction(13), f"Virasoro c={c_val}: sum={s}, expected 13"

    def test_kappa_values_specific(self):
        """Spot-check specific kappa values."""
        assert kappa_virasoro(Fraction(-22, 5)) == Fraction(-11, 5)
        assert kappa_virasoro(13) == Fraction(13, 2)
        assert kappa_virasoro(26) == Fraction(13)
        assert kappa_dual_virasoro(Fraction(-22, 5)) == Fraction(76, 5)

    def test_self_dual_point(self):
        """At c=13: kappa = kappa^! = 13/2. (AP8: NOT c=26)."""
        assert kappa_virasoro(13) == kappa_dual_virasoro(13) == Fraction(13, 2)

    def test_sum_not_zero_regression(self):
        """AP24 REGRESSION: the sum is NOT 0 for Virasoro."""
        s = complementarity_sum_virasoro(1)
        assert s != 0, "AP24 regression: sum should be 13, not 0"
        assert s == 13


class TestDirectComplementarityAffine:
    """Path 1: kappa + kappa^! = 0 for affine KM (FF involution)."""

    @pytest.mark.parametrize("N,k_val", [
        (2, 1), (2, 2), (2, 5), (2, Fraction(1, 2)),
        (3, 1), (3, 2), (3, 10),
        (4, 1), (4, 3),
        (5, 1),
    ])
    def test_sum_is_zero(self, N, k_val):
        dim_g = N * N - 1
        h_dual = N
        s = complementarity_sum_affine(dim_g, h_dual, k_val)
        assert s == Fraction(0), f"sl_{N} k={k_val}: sum={s}, expected 0"

    def test_kappa_not_c_over_2(self):
        """AP39: kappa(sl_N) != c/2 for N > 1 in general."""
        # sl_2, k=1: dim=3, h^v=2
        kap = kappa_affine(3, 2, 1)
        c_val = central_charge_affine_sl(2, 1)
        assert kap != c_val / 2 or True  # For sl_2 k=1: kappa = 3*3/4 = 9/4, c = 3/3=1
        # Actually: kappa = 3*(1+2)/(2*2) = 9/4. c = 3*1/3 = 1. c/2 = 1/2 != 9/4.
        assert kap == Fraction(9, 4)
        assert c_val == Fraction(1)
        assert kap != c_val / 2, "AP39: kappa != c/2 for affine sl_2"


# =========================================================================
# PATH 2: GAUGE THEORY / SYMPLECTIC DUALITY DATA
# =========================================================================

class TestPureSU2GaugeTheory:
    """Path 2: Pure SU(2) / Argyres-Douglas H_0."""

    def test_datum_basic(self):
        d = pure_su2_datum()
        assert d.central_charge == Fraction(-22, 5)
        assert d.dual_central_charge == Fraction(152, 5)
        assert d.kappa == Fraction(-11, 5)
        assert d.kappa_dual == Fraction(76, 5)

    def test_complementarity_sum(self):
        d = pure_su2_datum()
        assert d.complementarity_sum == Fraction(13)

    def test_coulomb_dim(self):
        d = pure_su2_datum()
        assert d.coulomb_dim == 2  # C^2/Z_2 is 2-dimensional
        assert d.higgs_dim == 0   # trivial Higgs branch

    def test_not_self_mirror(self):
        d = pure_su2_datum()
        assert not d.is_self_mirror


class TestSQCDSU2Nf4:
    """Path 2: SU(2) SQCD with N_f=4 (self-mirror)."""

    def test_datum_basic(self):
        d = sqcd_su2_nf4_datum()
        assert d.central_charge == Fraction(-9)
        assert d.kappa == Fraction(-9, 2)

    def test_self_mirror(self):
        d = sqcd_su2_nf4_datum()
        assert d.is_self_mirror

    def test_complementarity_sum(self):
        d = sqcd_su2_nf4_datum()
        assert d.complementarity_sum == Fraction(13)

    def test_equal_branch_dims(self):
        d = sqcd_su2_nf4_datum()
        assert d.coulomb_dim == d.higgs_dim  # self-mirror => equal dims


class TestHypertoricGaugeData:
    """Path 2: Hypertoric varieties."""

    def test_a1_hypertoric(self):
        d = a1_hypertoric_datum()
        assert d.kappa == Fraction(1)
        assert d.kappa_dual == Fraction(-1)
        assert d.complementarity_sum == Fraction(0)

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_an_hypertoric_sum_zero(self, n):
        d = an_hypertoric_datum(n)
        assert d.complementarity_sum == Fraction(0)
        assert d.kappa == Fraction(n + 1)
        assert d.kappa_dual == Fraction(-(n + 1))

    def test_jordan_quiver(self):
        d = jordan_quiver_datum()
        assert d.complementarity_sum == Fraction(0)
        assert d.is_self_mirror


class TestAffineCSGaugeData:
    """Path 2: Affine Chern-Simons gauge theories."""

    @pytest.mark.parametrize("N,k", [(2, 1), (3, 1), (4, 1), (2, 5)])
    def test_affine_sl_n_sum_zero(self, N, k):
        d = affine_sl_n_gauge_datum(N, k)
        assert d.complementarity_sum == Fraction(0)

    def test_affine_sl2_kappa(self):
        d = affine_sl_n_gauge_datum(2, 1)
        # kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4
        assert d.kappa == Fraction(9, 4)

    def test_affine_sl3_kappa(self):
        d = affine_sl_n_gauge_datum(3, 1)
        # kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3
        assert d.kappa == Fraction(16, 3)


# =========================================================================
# PATH 3: LAGRANGIAN CONDITION VERIFICATION
# =========================================================================

class TestLagrangianHeisenberg:
    """Path 3: Lagrangian condition for Heisenberg (class G)."""

    @pytest.mark.parametrize("k_val", [1, 2, 5, Fraction(1, 2)])
    def test_is_lagrangian(self, k_val):
        lag = verify_lagrangian_heisenberg(k_val)
        assert lag.is_lagrangian
        assert lag.is_isotropic
        assert lag.is_half_rank
        assert lag.is_verdier_dual

    def test_complementarity_sum_in_lagrangian(self):
        lag = verify_lagrangian_heisenberg(3)
        assert lag.complementarity_sum == Fraction(0)


class TestLagrangianVirasoro:
    """Path 3: Lagrangian condition for Virasoro (class M)."""

    @pytest.mark.parametrize("c_val", [
        Fraction(1, 2), 1, Fraction(-22, 5), 13, 25, 26,
    ])
    def test_is_lagrangian(self, c_val):
        lag = verify_lagrangian_virasoro(c_val)
        assert lag.is_lagrangian
        assert lag.complementarity_sum == Fraction(13)


class TestLagrangianAffine:
    """Path 3: Lagrangian condition for affine sl_N."""

    @pytest.mark.parametrize("N,k", [(2, 1), (3, 1), (4, 2)])
    def test_non_critical_is_lagrangian(self, N, k):
        lag = verify_lagrangian_affine(N, k)
        assert lag.is_lagrangian
        assert lag.complementarity_sum == Fraction(0)

    def test_critical_level_not_lagrangian(self):
        """At the critical level k = -h^v, Lagrangian condition fails."""
        lag = verify_lagrangian_affine(2, -2)  # k=-2 = -h^v for sl_2
        assert not lag.is_lagrangian


# =========================================================================
# PATH 4: COULOMB BRANCH / YANGIAN COMPARISON
# =========================================================================

class TestCoulombBranchA1:
    """Path 4: Coulomb branch of A_1 quiver (Heisenberg)."""

    def test_basic_data(self):
        cb = coulomb_branch_a1()
        assert cb.coulomb_dim == 2
        assert cb.is_yangian_type
        assert cb.lie_type == "A"
        assert cb.rank == 1

    def test_r_matrix_order(self):
        """AP19: r-matrix pole order = OPE pole order - 1.

        Heisenberg OPE: j(z)j(0) ~ k/z^2 (pole order 2).
        r-matrix: Omega/z (pole order 1).
        """
        cb = coulomb_branch_a1()
        assert cb.r_matrix_order == 1  # = OPE_order(2) - 1


class TestCoulombBranchAn:
    """Path 4: Coulomb branch of A_n quiver."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4])
    def test_yangian_type(self, n):
        cb = coulomb_branch_an(n)
        assert cb.is_yangian_type
        assert cb.coulomb_dim == 2 * n
        assert cb.r_matrix_order == 1

    def test_a1_matches(self):
        """A_1 quiver Coulomb branch should match standalone construction."""
        cb1 = coulomb_branch_a1()
        cb_an = coulomb_branch_an(1)
        assert cb1.coulomb_dim == cb_an.coulomb_dim
        assert cb1.r_matrix_order == cb_an.r_matrix_order


class TestCoulombBranchVirasoro:
    """Path 4: Virasoro-type Coulomb branch."""

    def test_r_matrix_order(self):
        """AP19: Virasoro OPE has poles z^{-4}, z^{-2}, z^{-1}.
        r-matrix has poles z^{-3}, z^{-1}. Max order = 3.
        """
        cb = coulomb_branch_virasoro()
        assert cb.r_matrix_order == 3

    def test_not_yangian(self):
        cb = coulomb_branch_virasoro()
        assert not cb.is_yangian_type


# =========================================================================
# PATH 5: KNOWN MIRROR PAIRS
# =========================================================================

class TestShiftedSymplecticStructure:
    """Path 5: PTVV shifted-symplectic structure verification."""

    @pytest.mark.parametrize("g,expected_shift", [
        (1, 0),     # -(3*1-3) = 0
        (2, -3),    # -(3*2-3) = -3
        (3, -6),    # -(3*3-3) = -6
        (4, -9),
        (5, -12),
    ])
    def test_ptvv_shift(self, g, expected_shift):
        assert ptvv_shift(g) == expected_shift

    def test_formal_moduli_shift_is_minus_1(self):
        assert formal_moduli_shift() == -1

    def test_ptvv_shift_genus_0_raises(self):
        with pytest.raises(ValueError):
            ptvv_shift(0)


class TestComputeShiftedSymplecticData:
    """Path 5: Full shifted-symplectic data computation."""

    def test_heisenberg_g1(self):
        data = compute_shifted_symplectic_data(
            genus=1,
            algebra_name="Heisenberg k=1",
            kappa=Fraction(1),
            kappa_dual=Fraction(-1),
        )
        assert data.ptvv_shift == 0
        assert data.formal_moduli_shift == -1
        assert data.complementarity_sum == Fraction(0)
        assert data.is_complementary_pair

    def test_virasoro_g1(self):
        data = compute_shifted_symplectic_data(
            genus=1,
            algebra_name="Virasoro c=1/2",
            kappa=Fraction(1, 4),
            kappa_dual=Fraction(51, 4),
        )
        assert data.ptvv_shift == 0
        assert data.complementarity_sum == Fraction(13)
        assert data.is_complementary_pair

    def test_virasoro_g2(self):
        data = compute_shifted_symplectic_data(
            genus=2,
            algebra_name="Virasoro c=1",
            kappa=Fraction(1, 2),
            kappa_dual=Fraction(25, 2),
        )
        assert data.ptvv_shift == -3
        assert data.complementarity_sum == Fraction(13)


class TestShadowConnectionMirror:
    """Path 5: Shadow connection data and mirror map."""

    def test_virasoro_c1(self):
        data = shadow_connection_data_virasoro(1)
        assert data["c"] == Fraction(1)
        assert data["c_dual"] == Fraction(25)
        assert data["kappa"] == Fraction(1, 2)
        assert data["kappa_dual"] == Fraction(25, 2)
        assert data["monodromy"] == -1
        assert data["self_dual_c"] == Fraction(13)

    def test_discriminant_complementarity(self):
        """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)]."""
        for c_val in [Fraction(1), Fraction(1, 2), Fraction(13), Fraction(25)]:
            data = shadow_connection_data_virasoro(c_val)
            assert data["delta_sum"] == data["delta_sum_expected"]

    @pytest.mark.parametrize("c_val", [1, Fraction(1, 2), 5, 13, 20, 25])
    def test_discriminant_formula_matches(self, c_val):
        c = Fraction(c_val)
        delta_sum = discriminant_complementarity_sum(c)
        delta = virasoro_critical_discriminant(c)
        delta_d = virasoro_critical_discriminant(Fraction(26) - c)
        assert delta + delta_d == delta_sum

    def test_self_dual_discriminant(self):
        """At c=13: Delta(13) = Delta(13) (self-dual)."""
        d13 = virasoro_critical_discriminant(13)
        d13_dual = virasoro_critical_discriminant(13)
        assert d13 == d13_dual
        # Delta(13) = 40/(5*13+22) = 40/87
        assert d13 == Fraction(40, 87)


# =========================================================================
# PATH 6: HEISENBERG BASELINE
# =========================================================================

class TestHeisenbergBaseline:
    """Path 6: Heisenberg as the simplest verification baseline."""

    def test_shadow_data_class_G(self):
        sd = heisenberg_shadow_data(1)
        assert sd.shadow_class == "G"
        assert sd.shadow_depth == 2
        assert sd.delta == Fraction(0)

    def test_shadow_data_q0(self):
        """Q_L(0) = 4 * kappa^2 for Heisenberg k=1: Q_L(0) = 4."""
        sd = heisenberg_shadow_data(1)
        assert sd.q0 == Fraction(4)

    @pytest.mark.parametrize("k_val", [1, 2, 3, Fraction(1, 2)])
    def test_q0_formula(self, k_val):
        sd = heisenberg_shadow_data(k_val)
        expected = 4 * Fraction(k_val) ** 2
        assert sd.q0 == expected

    def test_gauge_datum_for_k1(self):
        sd = heisenberg_shadow_data(1)
        assert sd.gauge_datum.complementarity_sum == Fraction(0)

    def test_genus_1_complementarity(self):
        """F_1(H_k) + F_1(H_k^!) = 0 for all k."""
        for k in [1, 2, 5]:
            kap = kappa_heisenberg(k)
            kap_d = kappa_dual_heisenberg(k)
            fg = genus_g_complementarity(1, kap, kap_d)
            assert fg["match"]
            assert fg["sum"] == Fraction(0)


# =========================================================================
# SHADOW METRIC TESTS
# =========================================================================

class TestVirasoroShadowMetric:
    """Shadow metric Q_Vir(t) and critical discriminant."""

    def test_metric_coefficients_c1(self):
        """Q_Vir(t) at c=1: q0=1, q1=12, q2=(180+872)/27 = 1052/27."""
        q0, q1, q2 = virasoro_shadow_metric_coefficients(1)
        assert q0 == Fraction(1)
        assert q1 == Fraction(12)
        assert q2 == Fraction(1052, 27)

    def test_metric_gaussian_decomposition(self):
        """Q_Vir(t) = (c + 6t)^2 + [80/(5c+22)] t^2.

        At c=1, t=0: Q = 1.
        At c=1, t=1: (1+6)^2 + 80/27 = 49 + 80/27 = (1323+80)/27 = 1403/27.
        Also from expanded: 1 + 12 + 1052/27 = 13 + 1052/27 = (351+1052)/27 = 1403/27.
        """
        q0, q1, q2 = virasoro_shadow_metric_coefficients(1)
        # Evaluate at t=1
        q_val = q0 + q1 + q2
        # From Gaussian
        gaussian_val = Fraction(7) ** 2 + Fraction(80, 27)
        assert q_val == gaussian_val

    def test_critical_discriminant_c1(self):
        """Delta(c=1) = 40/(5+22) = 40/27."""
        d = virasoro_critical_discriminant(1)
        assert d == Fraction(40, 27)

    def test_critical_discriminant_c13(self):
        """Delta(c=13) = 40/(65+22) = 40/87."""
        d = virasoro_critical_discriminant(13)
        assert d == Fraction(40, 87)


class TestVirasoroShadowData:
    """Virasoro shadow gauge data."""

    def test_shadow_class_M(self):
        sd = virasoro_shadow_data(1)
        assert sd.shadow_class == "M"
        assert sd.shadow_depth == float('inf')

    def test_self_dual_flag(self):
        sd = virasoro_shadow_data(13)
        assert sd.gauge_datum.is_self_mirror  # self-dual at c=13


class TestAffineSl2ShadowData:
    """Affine sl_2 shadow gauge data."""

    def test_shadow_class_L(self):
        sd = affine_sl2_shadow_data(1)
        assert sd.shadow_class == "L"
        assert sd.shadow_depth == 3

    def test_kappa(self):
        sd = affine_sl2_shadow_data(1)
        assert sd.gauge_datum.kappa == Fraction(9, 4)


# =========================================================================
# FABER-PANDHARIPANDE AND GENUS-g COMPLEMENTARITY
# =========================================================================

class TestFaberPandharipande:
    """Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        assert faber_pandharipande(1) == Fraction(1, 24)

    def test_lambda_2(self):
        assert faber_pandharipande(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        assert faber_pandharipande(3) == Fraction(31, 967680)

    def test_genus_0_raises(self):
        with pytest.raises(ValueError):
            faber_pandharipande(0)


class TestGenusGComplementarity:
    """F_g(A) + F_g(A!) = (kappa+kappa') * lambda_g."""

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_heisenberg_genus_g(self, g):
        """F_g(H_k) + F_g(H_k^!) = 0 for all g."""
        kap, kap_d = Fraction(1), Fraction(-1)
        result = genus_g_complementarity(g, kap, kap_d)
        assert result["match"]
        assert result["sum"] == Fraction(0)

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_virasoro_genus_g(self, g):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g."""
        c = Fraction(1, 2)
        kap = kappa_virasoro(c)
        kap_d = kappa_dual_virasoro(c)
        result = genus_g_complementarity(g, kap, kap_d)
        assert result["match"]
        assert result["sum"] == Fraction(13) * faber_pandharipande(g)


# =========================================================================
# FEIGIN-FRENKEL AND KOSZUL DUALITY
# =========================================================================

class TestFeiginFrenkelInvolution:
    """Feigin-Frenkel dual level k^! = -k - 2h^v."""

    @pytest.mark.parametrize("k,h_dual,expected", [
        (1, 2, -5),     # sl_2: 1 -> -5
        (1, 3, -7),     # sl_3: 1 -> -7
        (0, 2, -4),     # sl_2 at critical: 0 -> -4
        (5, 2, -9),     # sl_2: 5 -> -9
    ])
    def test_dual_level(self, k, h_dual, expected):
        assert ff_dual_level(k, h_dual) == Fraction(expected)

    def test_virasoro_koszul_dual(self):
        assert koszul_dual_central_charge_virasoro(Fraction(-22, 5)) == Fraction(152, 5)
        assert koszul_dual_central_charge_virasoro(13) == Fraction(13)
        assert koszul_dual_central_charge_virasoro(26) == Fraction(0)


# =========================================================================
# ARGYRES-DOUGLAS THEORIES
# =========================================================================

class TestArgyresDouglas:
    """Argyres-Douglas (A_1, A_{2n}) theories."""

    def test_h0_is_lee_yang(self):
        ad = argyres_douglas_A1_A2n(0)
        assert ad.central_charge_2d == Fraction(-22, 5)
        assert ad.kappa == Fraction(-11, 5)
        assert ad.complementarity_sum == Fraction(13)

    def test_h1(self):
        ad = argyres_douglas_A1_A2n(1)
        # c = -(22+10)/(5+2) = -32/7
        assert ad.central_charge_2d == Fraction(-32, 7)
        assert ad.complementarity_sum == Fraction(13)

    @pytest.mark.parametrize("n", range(5))
    def test_complementarity_sum_always_13(self, n):
        """All AD theories have complementarity sum = 13 (Virasoro type)."""
        ad = argyres_douglas_A1_A2n(n)
        assert ad.complementarity_sum == Fraction(13)

    def test_h0_matches_pure_su2(self):
        """H_0 AD theory = pure SU(2) gauge theory."""
        ad = argyres_douglas_A1_A2n(0)
        gt = pure_su2_datum()
        assert ad.central_charge_2d == gt.central_charge
        assert ad.kappa == gt.kappa


# =========================================================================
# HYPERTORIC VARIETIES
# =========================================================================

class TestHypertoricComplementarity:
    """Hypertoric A_n complementarity data."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 10])
    def test_sum_zero(self, n):
        data = hypertoric_an_complementarity(n)
        assert data["sum"] == Fraction(0)
        assert data["shadow_class"] == "G"
        assert data["shadow_depth"] == 2

    def test_kappa_values(self):
        data = hypertoric_an_complementarity(3)
        assert data["kappa"] == Fraction(4)
        assert data["kappa_dual"] == Fraction(-4)


# =========================================================================
# NAKAJIMA QUIVER VARIETIES
# =========================================================================

class TestNakajimaQuiver:
    """Nakajima quiver variety shadow data."""

    def test_jordan_quiver(self):
        data = nakajima_quiver_shadow("Jordan", (1,), (1,))
        assert data["complementarity_sum"] == Fraction(0)
        assert data["shadow_class"] == "G"
        assert data["kappa"] == Fraction(1)

    def test_a1_quiver(self):
        data = nakajima_quiver_shadow("A1", (1,), (1, 1))
        assert data["complementarity_sum"] == Fraction(0)
        assert data["shadow_class"] == "L"

    @pytest.mark.parametrize("n", [2, 3, 4])
    def test_cyclic_quiver(self, n):
        dim_vec = tuple([1] * n)
        framing = tuple([1] + [0] * (n - 1))
        data = nakajima_quiver_shadow(f"cyclic_A{n-1}", dim_vec, framing)
        assert data["complementarity_sum"] == Fraction(0)
        assert data["kappa"] == Fraction(n)

    def test_unknown_quiver_raises(self):
        with pytest.raises(ValueError):
            nakajima_quiver_shadow("unknown", (1,), (1,))


# =========================================================================
# DIMENSIONAL CONSISTENCY
# =========================================================================

class TestDimensionalConsistency:
    """Dimensional checks on gauge theory data."""

    def test_self_mirror_equal_dims(self):
        """Self-mirror theories must have equal Coulomb and Higgs dims."""
        for datum_fn in [sqcd_su2_nf4_datum, jordan_quiver_datum]:
            d = datum_fn()
            if d.is_self_mirror:
                check = symplectic_dim_check(d)
                assert check["dims_equal_if_self_mirror"]

    def test_pure_su2_dims(self):
        d = pure_su2_datum()
        check = symplectic_dim_check(d)
        assert check["coulomb_dim_C"] == 2
        assert check["higgs_dim_C"] == 0


# =========================================================================
# SHADOW RADIUS AND MIRROR SYMMETRY
# =========================================================================

class TestShadowRadiusMirror:
    """Shadow radius comparison for mirror pairs."""

    def test_self_dual_equal_radii(self):
        """At c=13: rho(A) = rho(A!) (self-dual)."""
        data = mirror_shadow_radii(13)
        assert data["self_dual"]
        assert data["rho"] is not None
        assert data["rho_dual"] is not None
        assert abs(data["rho"] - data["rho_dual"]) < 1e-12

    def test_positive_radii(self):
        for c_val in [1, Fraction(1, 2), 13, 25]:
            data = mirror_shadow_radii(c_val)
            if data["rho"] is not None:
                assert data["rho"] > 0
            if data["rho_dual"] is not None:
                assert data["rho_dual"] > 0


# =========================================================================
# CROSS-VERIFICATION (MULTI-PATH)
# =========================================================================

class TestCrossVerification:
    """Multi-path cross-verification for each family."""

    def test_heisenberg_k1(self):
        r = cross_verify_complementarity("heisenberg", {"k": 1})
        assert r["all_agree"]
        assert r["path1_direct_sum"] == Fraction(0)
        assert r["path3_lagrangian"]
        assert r["path4_F1_match"]

    def test_heisenberg_k5(self):
        r = cross_verify_complementarity("heisenberg", {"k": 5})
        assert r["all_agree"]

    def test_virasoro_c_half(self):
        r = cross_verify_complementarity("virasoro", {"c": Fraction(1, 2)})
        assert r["all_agree"]
        assert r["path1_direct_sum"] == Fraction(13)

    def test_virasoro_c_lee_yang(self):
        r = cross_verify_complementarity("virasoro", {"c": Fraction(-22, 5)})
        assert r["all_agree"]

    def test_virasoro_c13_self_dual(self):
        r = cross_verify_complementarity("virasoro", {"c": 13})
        assert r["all_agree"]

    def test_affine_sl2_k1(self):
        r = cross_verify_complementarity("affine_sl", {"N": 2, "k": 1})
        assert r["all_agree"]
        assert r["path1_direct_sum"] == Fraction(0)
        assert r["path2_gauge_sum"] == Fraction(0)

    def test_affine_sl3_k2(self):
        r = cross_verify_complementarity("affine_sl", {"N": 3, "k": 2})
        assert r["all_agree"]


# =========================================================================
# FULL LANDSCAPE VERIFICATION
# =========================================================================

class TestFullLandscape:
    """Full landscape cross-verification."""

    def test_all_entries_match(self):
        results = full_landscape_symplectic_duality()
        for entry in results:
            assert entry["match"], (
                f"Family {entry['family']}: sum={entry['sum']}, "
                f"expected={entry['expected_sum']}"
            )

    def test_heisenberg_entries_sum_zero(self):
        results = full_landscape_symplectic_duality()
        heis = [r for r in results if "Heisenberg" in r["family"]]
        assert len(heis) >= 5
        for r in heis:
            assert r["sum"] == Fraction(0)

    def test_virasoro_entries_sum_13(self):
        results = full_landscape_symplectic_duality()
        vir = [r for r in results if "Virasoro" in r["family"]]
        assert len(vir) >= 6
        for r in vir:
            assert r["sum"] == Fraction(13)

    def test_affine_entries_sum_zero(self):
        results = full_landscape_symplectic_duality()
        aff = [r for r in results if "affine" in r["family"]]
        assert len(aff) >= 9
        for r in aff:
            assert r["sum"] == Fraction(0)

    def test_landscape_count(self):
        results = full_landscape_symplectic_duality()
        assert len(results) >= 20, f"Expected 20+ entries, got {len(results)}"


# =========================================================================
# MASTER VERIFICATION TABLE
# =========================================================================

class TestMasterTable:
    """Master verification table combining all gauge theory data."""

    def test_all_entries_match(self):
        table = master_verification_table()
        for entry in table:
            assert entry["match"], (
                f"Entry {entry['name']}: sum={entry['sum']}, "
                f"expected={entry['expected']}"
            )

    def test_ptvv_shifts(self):
        table = master_verification_table()
        for entry in table:
            assert entry["ptvv_shift_g1"] == 0    # -(3-3) = 0
            assert entry["ptvv_shift_g2"] == -3   # -(6-3) = -3

    def test_table_count(self):
        table = master_verification_table()
        assert len(table) >= 15


# =========================================================================
# CENTRAL CHARGE FORMULAS (independent verification)
# =========================================================================

class TestCentralChargeFormulas:
    """Independent verification of central charge formulas."""

    def test_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert central_charge_affine_sl(2, 1) == Fraction(1)

    def test_sl3_k1(self):
        """c(sl_3, k=1) = 8*1/(1+3) = 2."""
        assert central_charge_affine_sl(3, 1) == Fraction(2)

    def test_sl2_k2(self):
        """c(sl_2, k=2) = 3*2/(2+2) = 3/2."""
        assert central_charge_affine_sl(2, 2) == Fraction(3, 2)

    def test_wn_n2_is_virasoro(self):
        """W_2 = Virasoro: c(W_2, k) should match c_Vir from DS of sl_2."""
        # c(W_2, k) = 1 - 6*(k+1)^2/(k+2) (Virasoro from sl_2)
        c_w2 = central_charge_wn(2, 1)
        # N=2, k=1: c = 1 - 6/3 = -1
        assert c_w2 == Fraction(-1)

    def test_critical_level_raises(self):
        with pytest.raises(ValueError):
            central_charge_affine_sl(2, -2)
        with pytest.raises(ValueError):
            central_charge_wn(3, -3)
