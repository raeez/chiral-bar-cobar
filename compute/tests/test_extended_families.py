"""Tests for non-simply-laced algebras, minimal models, E8 lattice, and toroidal bar.

Verifies ground truth for extended families beyond the simply-laced core:
B2, G2 (non-simply-laced with h != h^vee), Virasoro minimal models,
E8 lattice VOA, and elliptic/toroidal bar corrections.
"""

import pytest
from sympy import Rational, Symbol, simplify


# ============================================================================
# Non-simply-laced: B2 = so(5)
# ============================================================================


class TestB2Data:
    """B2 root system and Kac-Moody data."""

    def test_b2_dim(self):
        """dim(B2) = 10."""
        from compute.lib.nonsimplylaced_bar import b2_data
        assert b2_data()["dim"] == 10

    def test_b2_rank(self):
        """rank(B2) = 2."""
        from compute.lib.nonsimplylaced_bar import b2_data
        assert b2_data()["rank"] == 2

    def test_b2_coxeter(self):
        """Coxeter number h(B2) = 4."""
        from compute.lib.nonsimplylaced_bar import b2_data
        assert b2_data()["h"] == 4

    def test_b2_dual_coxeter(self):
        """Dual Coxeter number h^vee(B2) = 3."""
        from compute.lib.nonsimplylaced_bar import b2_data
        assert b2_data()["h_dual"] == 3

    def test_b2_h_neq_h_dual(self):
        """Non-simply-laced: h != h^vee for B2."""
        from compute.lib.nonsimplylaced_bar import b2_data
        d = b2_data()
        assert d["h"] != d["h_dual"]

    def test_b2_central_charge_k1(self):
        """c(B2, k=1) = 10/(1+3) = 5/2."""
        from compute.lib.nonsimplylaced_bar import b2_central_charge
        assert b2_central_charge(1) == Rational(5, 2)

    def test_b2_ff_dual_involution(self):
        """Feigin-Frenkel involution: (k')' = k for B2."""
        from compute.lib.nonsimplylaced_bar import b2_ff_dual
        k = Symbol('k')
        assert b2_ff_dual(b2_ff_dual(k)) == k

    def test_b2_kappa_k1(self):
        """kappa(B2, k=1) = 5*(1+3)/3 = 20/3."""
        from compute.lib.nonsimplylaced_bar import b2_kappa
        assert b2_kappa(1) == Rational(20, 3)

    def test_b2_complementarity_sum(self):
        """c + c' = 2*dim = 20 for B2."""
        from compute.lib.nonsimplylaced_bar import b2_complementarity_sum
        assert b2_complementarity_sum() == 20

    def test_b2_bar_generators_total(self):
        """Total bar generators = dim(B2) = 10."""
        from compute.lib.nonsimplylaced_bar import b2_bar_generators
        assert b2_bar_generators()["total"] == 10

    def test_b2_bar_deg2_count(self):
        """Degree-2 bar element count = 10^2 = 100."""
        from compute.lib.nonsimplylaced_bar import b2_bar_deg2_count
        assert b2_bar_deg2_count() == 100

    def test_b2_curvature_k1(self):
        """Curvature m_0(B2, k=1) = (1+3)/(2*3) = 2/3."""
        from compute.lib.nonsimplylaced_bar import b2_curvature
        assert simplify(b2_curvature(Rational(1)) - Rational(2, 3)) == 0

    def test_b2_kappa_formula_symbolic(self):
        """kappa(B2, k) = 5(k+3)/3 as a symbolic identity."""
        from compute.lib.nonsimplylaced_bar import b2_kappa
        k = Symbol('k')
        assert b2_kappa(k) == Rational(5) * (k + 3) / 3


# ============================================================================
# Non-simply-laced: G2
# ============================================================================


class TestG2Data:
    """G2 root system and Kac-Moody data."""

    def test_g2_dim(self):
        """dim(G2) = 14."""
        from compute.lib.nonsimplylaced_bar import g2_data
        assert g2_data()["dim"] == 14

    def test_g2_rank(self):
        """rank(G2) = 2."""
        from compute.lib.nonsimplylaced_bar import g2_data
        assert g2_data()["rank"] == 2

    def test_g2_coxeter(self):
        """Coxeter number h(G2) = 6."""
        from compute.lib.nonsimplylaced_bar import g2_data
        assert g2_data()["h"] == 6

    def test_g2_dual_coxeter(self):
        """Dual Coxeter number h^vee(G2) = 4."""
        from compute.lib.nonsimplylaced_bar import g2_data
        assert g2_data()["h_dual"] == 4

    def test_g2_central_charge_k1(self):
        """c(G2, k=1) = 14/(1+4) = 14/5."""
        from compute.lib.nonsimplylaced_bar import g2_central_charge
        assert g2_central_charge(1) == Rational(14, 5)

    def test_g2_ff_dual_involution(self):
        """Feigin-Frenkel involution: (k')' = k for G2."""
        from compute.lib.nonsimplylaced_bar import g2_ff_dual
        k = Symbol('k')
        assert g2_ff_dual(g2_ff_dual(k)) == k

    def test_g2_kappa_k1(self):
        """kappa(G2, k=1) = 7*(1+4)/4 = 35/4."""
        from compute.lib.nonsimplylaced_bar import g2_kappa
        assert g2_kappa(1) == Rational(35, 4)

    def test_g2_complementarity_sum(self):
        """c + c' = 2*dim = 28 for G2."""
        from compute.lib.nonsimplylaced_bar import g2_complementarity_sum
        assert g2_complementarity_sum() == 28

    def test_g2_bar_generators_total(self):
        """Total bar generators = dim(G2) = 14."""
        from compute.lib.nonsimplylaced_bar import g2_bar_generators
        assert g2_bar_generators()["total"] == 14

    def test_g2_bar_deg2_count(self):
        """Degree-2 bar element count = 14^2 = 196."""
        from compute.lib.nonsimplylaced_bar import g2_bar_deg2_count
        assert g2_bar_deg2_count() == 196


# ============================================================================
# Periodicity distinction: h vs h^vee
# ============================================================================


class TestPeriodicity:
    """KM bar cohomology period uses h (Coxeter), not h^vee."""

    def test_b2_period(self):
        """B2 period = 2h = 8, NOT 2*h^vee = 6."""
        from compute.lib.nonsimplylaced_bar import periodicity_coxeter
        assert periodicity_coxeter("B", 2) == 8

    def test_g2_period(self):
        """G2 period = 2h = 12, NOT 2*h^vee = 8."""
        from compute.lib.nonsimplylaced_bar import periodicity_coxeter
        assert periodicity_coxeter("G", 2) == 12

    def test_a2_simply_laced(self):
        """A2 is simply-laced: h = h^vee = 3."""
        from compute.lib.nonsimplylaced_bar import periodicity_vs_dual_coxeter
        a2 = periodicity_vs_dual_coxeter("A", 2)
        assert a2["simply_laced"] is True
        assert a2["h"] == a2["h_dual"]


# ============================================================================
# Minimal models
# ============================================================================


class TestMinimalModelCentralCharges:
    """Central charge formula c = 1 - 6(p-q)^2/(pq)."""

    def test_trivial_m32(self):
        """M(3,2): c = 0 (trivial model)."""
        from compute.lib.minimal_model_bar import minimal_model_c
        assert minimal_model_c(3, 2) == 0

    def test_ising_m43(self):
        """M(4,3): c = 1/2 (Ising model)."""
        from compute.lib.minimal_model_bar import minimal_model_c
        assert minimal_model_c(4, 3) == Rational(1, 2)

    def test_lee_yang_m52(self):
        """M(5,2): c = -22/5 (Lee-Yang, non-unitary)."""
        from compute.lib.minimal_model_bar import minimal_model_c
        assert minimal_model_c(5, 2) == Rational(-22, 5)

    def test_tricritical_ising_m54(self):
        """M(5,4): c = 7/10 (tricritical Ising)."""
        from compute.lib.minimal_model_bar import minimal_model_c
        assert minimal_model_c(5, 4) == Rational(7, 10)

    def test_three_state_potts_m65(self):
        """M(6,5): c = 4/5 (three-state Potts)."""
        from compute.lib.minimal_model_bar import minimal_model_c
        assert minimal_model_c(6, 5) == Rational(4, 5)


class TestIsingBarData:
    """Ising model M(4,3) bar complex data."""

    def test_ising_c(self):
        """Ising central charge c = 1/2."""
        from compute.lib.minimal_model_bar import ising_bar_data
        assert ising_bar_data()["c"] == Rational(1, 2)

    def test_ising_kappa(self):
        """Ising kappa = c/2 = 1/4."""
        from compute.lib.minimal_model_bar import ising_bar_data
        assert ising_bar_data()["kappa"] == Rational(1, 4)

    def test_ising_obs_1(self):
        """Ising genus-1 obstruction = kappa/24 = 1/96."""
        from compute.lib.minimal_model_bar import ising_bar_data
        assert ising_bar_data()["obs_1"] == Rational(1, 96)

    def test_ising_n_modules(self):
        """Ising model has 3 modules."""
        from compute.lib.minimal_model_bar import ising_bar_data
        assert ising_bar_data()["n_modules"] == 3

    def test_ising_genus1_bar_dim(self):
        """Genus-1 bar: B(sigma,sigma) has dim 2."""
        from compute.lib.minimal_model_bar import ising_genus1_bar
        assert ising_genus1_bar()["B_{g=1}(sigma, sigma)"]["dim"] == 2


class TestMinimalModelComplementarity:
    """All Virasoro minimal models satisfy c + c' = 26."""

    @pytest.mark.parametrize("p,q", [
        (3, 2), (4, 3), (5, 4), (6, 5), (7, 2), (7, 4), (7, 6),
    ])
    def test_complementarity_sum_26(self, p, q):
        """c + c' = 26 for M(p,q) (all Virasoro quotients)."""
        from compute.lib.minimal_model_bar import minimal_model_complementarity
        assert minimal_model_complementarity(p, q) == 26

    @pytest.mark.parametrize("p,q", [
        (4, 3), (5, 4), (6, 5), (7, 6),
    ])
    def test_complementarity_explicit(self, p, q):
        """Explicit check: c(p,q) + (26 - c(p,q)) = 26."""
        from compute.lib.minimal_model_bar import minimal_model_c
        c = minimal_model_c(p, q)
        assert c + (26 - c) == 26


class TestTricriticalAndPotts:
    """Tricritical Ising and three-state Potts data."""

    def test_tricritical_c(self):
        """Tricritical Ising: c = 7/10."""
        from compute.lib.minimal_model_bar import tricritical_ising_data
        assert tricritical_ising_data()["c"] == Rational(7, 10)

    def test_tricritical_n_modules(self):
        """Tricritical Ising has 6 modules."""
        from compute.lib.minimal_model_bar import tricritical_ising_data
        assert tricritical_ising_data()["n_modules"] == 6

    def test_potts_c(self):
        """Three-state Potts: c = 4/5."""
        from compute.lib.minimal_model_bar import three_state_potts_data
        assert three_state_potts_data()["c"] == Rational(4, 5)

    def test_potts_n_modules(self):
        """Three-state Potts has 10 modules."""
        from compute.lib.minimal_model_bar import three_state_potts_data
        assert three_state_potts_data()["n_modules"] == 10


# ============================================================================
# E8 lattice VOA
# ============================================================================


class TestE8CentralCharge:
    """E8 lattice VOA central charge and duality."""

    def test_e8_central_charge_k1(self):
        """c(E8, k=1) = 248/31."""
        from compute.lib.e8_lattice_bar import e8_central_charge
        assert e8_central_charge(1) == Rational(248, 31)

    def test_e8_generator_total(self):
        """Total generators = 248 = 8 Cartan + 240 roots."""
        from compute.lib.e8_lattice_bar import e8_generator_count
        gens = e8_generator_count()
        assert gens["total"] == 248
        assert gens["cartan"] == 8
        assert gens["vertex_operators"] == 240
        assert gens["cartan"] + gens["vertex_operators"] == 248

    def test_e8_complementarity_sum(self):
        """c + c' = 2 * dim(E8) = 496."""
        from compute.lib.e8_lattice_bar import e8_complementarity_sum
        assert e8_complementarity_sum() == 496

    def test_e8_complementarity_explicit_k1(self):
        """Explicit: c(1) + c(-61) = 496."""
        from compute.lib.e8_lattice_bar import e8_central_charge, e8_dual_central_charge
        assert e8_central_charge(1) + e8_dual_central_charge(1) == 496

    def test_e8_dual_level_k1(self):
        """k' = -1 - 60 = -61 at k=1."""
        from compute.lib.e8_lattice_bar import e8_dual_level
        assert e8_dual_level(1) == -61


class TestE8BarDeg2:
    """E8 degree-2 bar complex type decomposition."""

    def test_type_I_count(self):
        """Type I (Cartan-Cartan): 8^2 = 64."""
        from compute.lib.e8_lattice_bar import e8_bar_deg2_type_counts
        assert e8_bar_deg2_type_counts()["type_I_cartan_cartan"] == 64

    def test_type_II_count(self):
        """Type II (Cartan-root): 2 * 8 * 240 = 3840."""
        from compute.lib.e8_lattice_bar import e8_bar_deg2_type_counts
        assert e8_bar_deg2_type_counts()["type_II_cartan_root"] == 3840

    def test_type_III_count(self):
        """Type III (root-root): 240^2 = 57600."""
        from compute.lib.e8_lattice_bar import e8_bar_deg2_type_counts
        assert e8_bar_deg2_type_counts()["type_III_root_root"] == 57600

    def test_total_deg2(self):
        """Total degree-2: (8+240)^2 = 248^2 = 61504."""
        from compute.lib.e8_lattice_bar import e8_bar_deg2_type_counts
        counts = e8_bar_deg2_type_counts()
        assert counts["total"] == 248 ** 2
        assert counts["total"] == 61504

    def test_type_sum_equals_total(self):
        """Type I + II + III = total."""
        from compute.lib.e8_lattice_bar import e8_bar_deg2_type_counts
        c = e8_bar_deg2_type_counts()
        assert (c["type_I_cartan_cartan"] + c["type_II_cartan_root"]
                + c["type_III_root_root"]) == c["total"]

    def test_e8_bar_diff_type_I_diagonal(self):
        """Type I diagonal: D([J^i|J^i]) = k*|0> (vacuum component)."""
        from compute.lib.e8_lattice_bar import e8_bar_diff_type_I
        vac, _ = e8_bar_diff_type_I(1, 1)
        k = Symbol('k')
        assert vac["vac"] == k

    def test_e8_bar_diff_type_I_offdiag(self):
        """Type I off-diagonal: D([J^i|J^j]) = 0 for i != j."""
        from compute.lib.e8_lattice_bar import e8_bar_diff_type_I
        vac, bar1 = e8_bar_diff_type_I(1, 2)
        assert vac == {}
        assert bar1 == {}

    def test_e8_bar_diff_type_III_minus2(self):
        """Opposite roots <a,b>=-2: gives J_alpha + k*|0>."""
        from compute.lib.e8_lattice_bar import e8_bar_diff_type_III
        vac, bar1 = e8_bar_diff_type_III(-2)
        assert vac["vac"] == Symbol('k')
        assert bar1["J_alpha"] == Rational(1)

    def test_e8_bar_diff_type_III_minus1(self):
        """Neighbor roots <a,b>=-1: gives epsilon*e^{a+b}."""
        from compute.lib.e8_lattice_bar import e8_bar_diff_type_III
        vac, bar1 = e8_bar_diff_type_III(-1)
        assert vac == {}
        assert "e_alpha_plus_beta" in bar1

    def test_e8_bar_diff_type_III_zero(self):
        """Orthogonal roots <a,b>=0: differential vanishes."""
        from compute.lib.e8_lattice_bar import e8_bar_diff_type_III
        vac, bar1 = e8_bar_diff_type_III(0)
        assert vac == {}
        assert bar1 == {}

    def test_e8_curvature_k1(self):
        """m_0(k=1) = 31/60."""
        from compute.lib.e8_lattice_bar import e8_curvature
        assert e8_curvature(1) == Rational(31, 60)


# ============================================================================
# Toroidal bar complex
# ============================================================================


class TestEisensteinCoefficients:
    """Eisenstein series q-expansion coefficients."""

    def test_e2_constant_term(self):
        """E_2: constant term = 1."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(2, 5)[0] == 1

    def test_e2_q1(self):
        """E_2: coefficient of q = -24*sigma_1(1) = -24."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(2, 5)[1] == -24

    def test_e2_q2(self):
        """E_2: coefficient of q^2 = -24*sigma_1(2) = -24*3 = -72."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(2, 5)[2] == -72

    def test_e2_q3(self):
        """E_2: coefficient of q^3 = -24*sigma_1(3) = -24*4 = -96."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(2, 5)[3] == -96

    def test_e2_q4(self):
        """E_2: coefficient of q^4 = -24*sigma_1(4) = -24*7 = -168."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(2, 5)[4] == -168

    def test_e4_constant_term(self):
        """E_4: constant term = 1."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(4, 5)[0] == 1

    def test_e4_q1(self):
        """E_4: coefficient of q = 240*sigma_3(1) = 240."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(4, 5)[1] == 240

    def test_e4_q2(self):
        """E_4: coefficient of q^2 = 240*sigma_3(2) = 240*9 = 2160."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(4, 5)[2] == 2160

    def test_e4_q3(self):
        """E_4: coefficient of q^3 = 240*sigma_3(3) = 240*28 = 6720."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(4, 5)[3] == 6720

    def test_e4_q4(self):
        """E_4: coefficient of q^4 = 240*sigma_3(4) = 240*73 = 17520."""
        from compute.lib.toroidal_bar import eisenstein_q_expansion
        assert eisenstein_q_expansion(4, 5)[4] == 17520


class TestZetaLaurent:
    """Weierstrass zeta function Laurent expansion."""

    def test_pole_coefficient(self):
        """Leading pole: zeta(eps) ~ 1/eps, coefficient = 1."""
        from compute.lib.toroidal_bar import zeta_laurent_coefficients
        coeffs = zeta_laurent_coefficients()
        assert coeffs[-1]["coeff"] == 1

    def test_e2_correction_present(self):
        """E_2 correction appears at eps^1."""
        from compute.lib.toroidal_bar import zeta_laurent_coefficients
        coeffs = zeta_laurent_coefficients()
        assert coeffs[1]["eisenstein"] == "E_2"

    def test_e4_correction_present(self):
        """E_4 correction appears at eps^3."""
        from compute.lib.toroidal_bar import zeta_laurent_coefficients
        coeffs = zeta_laurent_coefficients()
        assert coeffs[3]["eisenstein"] == "E_4"


class TestEllipticBarDifferential:
    """Elliptic bar differential modular weight structure."""

    def test_deg1_vanishes(self):
        """Degree-1 elliptic bar differential vanishes."""
        from compute.lib.toroidal_bar import elliptic_bar_diff_deg
        d1 = elliptic_bar_diff_deg(1)
        assert d1["rational"] == 0
        assert d1["elliptic"] == 0

    def test_deg2_modular_weight(self):
        """Degree-2 correction has modular weight 2 (E_2)."""
        from compute.lib.toroidal_bar import elliptic_bar_diff_deg
        d2 = elliptic_bar_diff_deg(2)
        assert d2["modular_weight"] == 2

    def test_deg2_quasi_modular(self):
        """Degree-2 correction is quasi-modular (E_2 is quasi-modular)."""
        from compute.lib.toroidal_bar import elliptic_bar_diff_deg
        d2 = elliptic_bar_diff_deg(2)
        assert d2["quasi_modular"] is True

    def test_deg3_modular_weight(self):
        """Degree-3 correction has modular weight 4 (E_4)."""
        from compute.lib.toroidal_bar import elliptic_bar_diff_deg
        d3 = elliptic_bar_diff_deg(3)
        assert d3["modular_weight"] == 4

    def test_deg3_not_quasi_modular(self):
        """Degree-3 correction is genuinely modular (E_4 is holomorphic)."""
        from compute.lib.toroidal_bar import elliptic_bar_diff_deg
        d3 = elliptic_bar_diff_deg(3)
        assert d3["quasi_modular"] is False

    def test_deg4_modular_weight(self):
        """Degree-4 correction has modular weight 6 (E_6)."""
        from compute.lib.toroidal_bar import elliptic_bar_diff_deg
        d4 = elliptic_bar_diff_deg(4)
        assert d4["modular_weight"] == 6
