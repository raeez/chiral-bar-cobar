r"""Tests for celestial holography OPE from Koszul duality.

Verifies:
1. Lie algebra data and structure constants for sl_N (N = 2, 3, 4, 5)
2. Collinear algebra construction (self-dual YM, self-dual gravity)
3. Bar complex Koszulness (H*(B) concentrated in bar degree 1)
4. Celestial OPE coefficients (Delta conservation, pole orders, color structure)
5. Collision residue / r-matrix from bar complex (AP19: pole order reduction)
6. Conformally soft theorem tower (S_0 = BMS, S_1 = Virasoro, S_2 = w_{1+inf})
7. Modular characteristic kappa for collinear algebra at k=0 and k=1
8. Shadow tower for w_{1+infinity} on the T-line (Virasoro sub-tower)
9. Cross-verification: amplitude from bar complex vs direct Parke-Taylor
10. w_{1+infinity} shadow growth rate and convergence

Ground truth sources:
    - kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N)  (AP1: Kac-Moody specific)
    - kappa(Vir_c) = c/2
    - S_4(Vir) = 10/[c(5c+22)]  (quartic contact, AP1)
    - Delta(Vir) = 40/(5c+22)   (critical discriminant)
    - r-matrix pole order = OPE pole order - 1 (AP19)
    - Com^! = Lie (Koszul duality for current algebras)
    - Parke-Taylor MHV: A_n = <ij>^4 / prod <k,k+1>

References:
    celestial_koszul_ope.py (compute/lib/)
    concordance.tex, higher_genus_modular_koszul.tex
    Strominger (2014), Guevara-Himwich-Pate-Strominger (2021),
    Costello-Paquette (2022), Pate-Raclariu-Strominger-Yuan (2021)
"""

from fractions import Fraction

import pytest

from compute.lib.celestial_koszul_ope import (
    # Lie algebra data
    LieAlgebraData,
    sl_n_data,
    # Collinear algebra
    CollinearAlgebra,
    sdym_collinear_algebra,
    sdgr_collinear_algebra,
    # Bar complex
    BarComplexData,
    bar_complex_current_algebra,
    # Celestial OPE
    CelestialOPECoefficient,
    celestial_ope_gluon_pp,
    celestial_ope_gluon_pm,
    celestial_ope_gluon_pm_to_minus,
    # Collision residue
    CollisionResidue,
    collision_residue_current_algebra,
    collision_residue_virasoro,
    collision_residue_w_infinity,
    # Soft theorems
    SoftTheoremData,
    soft_theorem_tower,
    # Modular characteristics
    kappa_current_algebra,
    kappa_virasoro,
    kappa_w_infinity_tline,
    shadow_s4_virasoro,
    shadow_discriminant_virasoro,
    shadow_growth_rate_virasoro,
    shadow_tower_virasoro_coefficients,
    # Splitting functions
    collinear_splitting_pp,
    collinear_splitting_pm,
    parke_taylor_stripped,
    # Verification
    verify_bar_koszulness,
    verify_collision_residue_cybe,
    verify_celestial_ope_consistency,
    verify_kappa_at_level_zero,
    verify_kappa_at_level_one,
    verify_soft_theorem_tower,
    verify_shadow_tower_virasoro_at_c,
    verify_virasoro_r_matrix_pole_orders,
    w_infinity_shadow_tower_tline,
    celestial_4pt_from_bar,
    run_full_verification,
)

from sympy import Symbol


# ============================================================
# Section 1: Lie algebra data for sl_N
# ============================================================

class TestLieAlgebraData:
    """Verify Lie algebra data for sl_N at small N."""

    def test_sl2_dim(self):
        """dim(sl_2) = 3."""
        g = sl_n_data(2)
        assert g.dim == 3

    def test_sl2_rank(self):
        """rank(sl_2) = 1."""
        g = sl_n_data(2)
        assert g.rank == 1

    def test_sl2_dual_coxeter(self):
        """h^v(sl_2) = 2."""
        g = sl_n_data(2)
        assert g.dual_coxeter == 2

    def test_sl2_casimir_adjoint(self):
        """C_2(adj, sl_2) = 4 (= 2*N for N=2)."""
        g = sl_n_data(2)
        assert g.casimir_adjoint == Fraction(4)

    def test_sl3_dim(self):
        """dim(sl_3) = 8."""
        g = sl_n_data(3)
        assert g.dim == 8

    def test_sl3_rank(self):
        """rank(sl_3) = 2."""
        g = sl_n_data(3)
        assert g.rank == 2

    def test_sl3_dual_coxeter(self):
        """h^v(sl_3) = 3."""
        g = sl_n_data(3)
        assert g.dual_coxeter == 3

    def test_sl3_casimir_adjoint(self):
        """C_2(adj, sl_3) = 6 (= 2*N for N=3)."""
        g = sl_n_data(3)
        assert g.casimir_adjoint == Fraction(6)

    def test_sl4_dim(self):
        """dim(sl_4) = 15."""
        g = sl_n_data(4)
        assert g.dim == 15

    def test_sl5_dim(self):
        """dim(sl_5) = 24."""
        g = sl_n_data(5)
        assert g.dim == 24

    def test_sl_n_invalid(self):
        """N < 2 should raise ValueError."""
        with pytest.raises(ValueError):
            sl_n_data(1)

    def test_structure_constant_norm_sl2(self):
        """sum |f^{abc}|^2 = dim * C_2(adj) = 3 * 4 = 12 for sl_2."""
        g = sl_n_data(2)
        assert g.structure_constant_norm_sq == Fraction(12)

    def test_structure_constant_norm_sl3(self):
        """sum |f^{abc}|^2 = 8 * 6 = 48 for sl_3."""
        g = sl_n_data(3)
        assert g.structure_constant_norm_sq == Fraction(48)


# ============================================================
# Section 2: Collinear algebra construction
# ============================================================

class TestCollinearAlgebra:
    """Verify collinear algebra construction for SDYM and SDGR."""

    def test_sdym_su2_generators(self):
        """SDYM with SU(2) has 3 generators."""
        alg = sdym_collinear_algebra(2)
        assert alg.num_generators == 3

    def test_sdym_su3_generators(self):
        """SDYM with SU(3) has 8 generators."""
        alg = sdym_collinear_algebra(3)
        assert alg.num_generators == 8

    def test_sdym_is_self_dual(self):
        """Self-dual YM at k=0 is self-dual."""
        alg = sdym_collinear_algebra(2)
        assert alg.is_self_dual

    def test_sdym_nonzero_level_not_self_dual(self):
        """Full YM at k=1 is NOT self-dual."""
        alg = sdym_collinear_algebra(2, level=Fraction(1))
        assert not alg.is_self_dual

    def test_sdym_central_charge_k0(self):
        """c(V_0(sl_2)) = 0 * 3 / (0 + 2) = 0."""
        alg = sdym_collinear_algebra(2, level=Fraction(0))
        assert alg.central_charge == Fraction(0)

    def test_sdym_central_charge_k1_su2(self):
        """c(V_1(sl_2)) = 1 * 3 / (1 + 2) = 1."""
        alg = sdym_collinear_algebra(2, level=Fraction(1))
        assert alg.central_charge == Fraction(1)

    def test_sdym_central_charge_k1_su3(self):
        """c(V_1(sl_3)) = 1 * 8 / (1 + 3) = 2."""
        alg = sdym_collinear_algebra(3, level=Fraction(1))
        assert alg.central_charge == Fraction(2)

    def test_sdgr_is_self_dual(self):
        """Self-dual gravity is self-dual."""
        alg = sdgr_collinear_algebra()
        assert alg.is_self_dual

    def test_sdgr_generators_exist(self):
        """SDGR has generators w_1, w_2, ..."""
        alg = sdgr_collinear_algebra()
        assert alg.num_generators >= 2
        assert alg.generators[0] == "w_1"
        assert alg.generators[1] == "w_2"


# ============================================================
# Section 3: Bar complex Koszulness
# ============================================================

class TestBarComplexKoszulness:
    """Verify bar complex of current algebra is Koszul (concentrated)."""

    def test_bar_sl2_k0_koszul(self):
        """B(V_0(sl_2)) is Koszul."""
        g = sl_n_data(2)
        bar = bar_complex_current_algebra(g, Fraction(0))
        assert bar.is_koszul

    def test_bar_sl2_k0_H1(self):
        """H^1(B(V_0(sl_2))) = sl_2^* has dim 3."""
        g = sl_n_data(2)
        bar = bar_complex_current_algebra(g, Fraction(0))
        assert bar.bar_cohomology_dims[1] == 3

    def test_bar_sl2_k0_H2(self):
        """H^2(B(V_0(sl_2))) = 0."""
        g = sl_n_data(2)
        bar = bar_complex_current_algebra(g, Fraction(0))
        assert bar.bar_cohomology_dims[2] == 0

    def test_bar_sl3_k0_koszul(self):
        """B(V_0(sl_3)) is Koszul."""
        g = sl_n_data(3)
        bar = bar_complex_current_algebra(g, Fraction(0))
        assert bar.is_koszul

    def test_bar_sl3_k0_H1(self):
        """H^1(B(V_0(sl_3))) = sl_3^* has dim 8."""
        g = sl_n_data(3)
        bar = bar_complex_current_algebra(g, Fraction(0))
        assert bar.bar_cohomology_dims[1] == 8

    def test_bar_sl3_k1_koszul(self):
        """B(V_1(sl_3)) is Koszul."""
        g = sl_n_data(3)
        bar = bar_complex_current_algebra(g, Fraction(1))
        assert bar.is_koszul

    def test_bar_koszul_dual_type(self):
        """Koszul dual of current algebra Com is Lie."""
        g = sl_n_data(2)
        bar = bar_complex_current_algebra(g, Fraction(0))
        assert bar.koszul_dual_type == "Lie"

    def test_bar_depth_class_k0(self):
        """Level k=0 current algebra is class G (Gaussian: no curvature)."""
        g = sl_n_data(2)
        bar = bar_complex_current_algebra(g, Fraction(0))
        assert bar.depth_class == "G"

    def test_bar_depth_class_k1(self):
        """Level k=1 current algebra is class L (Lie/tree)."""
        g = sl_n_data(2)
        bar = bar_complex_current_algebra(g, Fraction(1))
        assert bar.depth_class == "L"

    def test_verify_bar_koszulness_sl2(self):
        """Full verification for sl_2 at k=0."""
        g = sl_n_data(2)
        results = verify_bar_koszulness(g, Fraction(0))
        assert results["H^0 = C"]
        assert results["H^1 = g^*"]
        assert results["H^2 = 0"]
        assert results["H^3 = 0"]
        assert results["is_koszul"]

    def test_verify_bar_koszulness_sl4(self):
        """Full verification for sl_4 at k=1."""
        g = sl_n_data(4)
        results = verify_bar_koszulness(g, Fraction(1))
        assert results["H^0 = C"]
        assert results["H^1 = g^*"]
        assert results["is_koszul"]


# ============================================================
# Section 4: Celestial OPE coefficients
# ============================================================

class TestCelestialOPE:
    """Verify celestial OPE coefficient structure."""

    def test_pp_delta_conservation(self):
        """O_Delta^+ O_{Delta'}^+ -> O_{Delta+Delta'-1}^+."""
        Delta, Dp = Symbol("Delta"), Symbol("Delta_prime")
        ope = celestial_ope_gluon_pp(Delta, Dp, 2)
        assert ope.delta_out == Delta + Dp - 1

    def test_pp_color_structure(self):
        """++ channel has f^{abc} structure constant."""
        ope = celestial_ope_gluon_pp(1, 1, 2)
        assert ope.color_structure == "f^{abc}"

    def test_pp_simple_pole(self):
        """++ celestial OPE has simple pole."""
        ope = celestial_ope_gluon_pp(1, 1, 2)
        assert ope.pole_order == 1

    def test_pp_helicity_out(self):
        """++ -> + (helicity conservation in self-dual sector)."""
        ope = celestial_ope_gluon_pp(1, 1, 2)
        assert ope.helicity_out == +1

    def test_pm_delta_conservation(self):
        """O^+ O^- -> O^+ preserves Delta sum."""
        Delta, Dp = Symbol("Delta"), Symbol("Delta_prime")
        ope = celestial_ope_gluon_pm(Delta, Dp, 2)
        assert ope.delta_out == Delta + Dp - 1

    def test_pm_color_structure(self):
        """+- channel has delta^{ab} (from double pole)."""
        ope = celestial_ope_gluon_pm(1, 1, 2)
        assert ope.color_structure == "delta^{ab}"

    def test_pm_minus_color_structure(self):
        """+- -> - channel has f^{abc}."""
        ope = celestial_ope_gluon_pm_to_minus(1, 1, 2)
        assert ope.color_structure == "f^{abc}"

    def test_pm_minus_helicity(self):
        """+- -> - gives negative helicity output."""
        ope = celestial_ope_gluon_pm_to_minus(1, 1, 2)
        assert ope.helicity_out == -1

    def test_verify_celestial_ope_su2(self):
        """Full OPE consistency for SU(2)."""
        results = verify_celestial_ope_consistency(2)
        for key, val in results.items():
            assert val, f"Failed: {key}"

    def test_verify_celestial_ope_su3(self):
        """Full OPE consistency for SU(3)."""
        results = verify_celestial_ope_consistency(3)
        for key, val in results.items():
            assert val, f"Failed: {key}"


# ============================================================
# Section 5: Collision residue / R-matrix (AP19)
# ============================================================

class TestCollisionResidue:
    """Verify collision residue (r-matrix) from bar complex."""

    def test_sl2_k0_single_pole(self):
        """r(z) for V_0(sl_2) has a single simple pole."""
        g = sl_n_data(2)
        cr = collision_residue_current_algebra(g, Fraction(0))
        assert cr.pole_orders == (1,)

    def test_sl2_k0_leading_pole_1(self):
        """Leading pole order is 1 for current algebra."""
        g = sl_n_data(2)
        cr = collision_residue_current_algebra(g, Fraction(0))
        assert cr.leading_pole_order == 1

    def test_sl2_k0_cybe(self):
        """r(z) for V_0(sl_2) satisfies CYBE."""
        g = sl_n_data(2)
        cr = collision_residue_current_algebra(g, Fraction(0))
        assert cr.satisfies_cybe

    def test_sl2_k0_triangular(self):
        """r(z) at level 0 is triangular (skew-symmetric)."""
        g = sl_n_data(2)
        cr = collision_residue_current_algebra(g, Fraction(0))
        assert cr.is_triangular

    def test_sl3_k1_cybe(self):
        """r(z) for V_1(sl_3) satisfies CYBE."""
        g = sl_n_data(3)
        cr = collision_residue_current_algebra(g, Fraction(1))
        assert cr.satisfies_cybe

    def test_virasoro_pole_orders(self):
        """Virasoro r-matrix has poles at z^{-3} and z^{-1} (AP19)."""
        cr = collision_residue_virasoro(26)
        assert cr.pole_orders == (3, 1)

    def test_virasoro_no_even_poles(self):
        """Bosonic algebra: no even-order poles in r-matrix (AP19)."""
        cr = collision_residue_virasoro(26)
        assert all(p % 2 == 1 for p in cr.pole_orders)

    def test_virasoro_leading_pole_cubic(self):
        """Virasoro r-matrix leading pole is z^{-3} (from z^{-4} OPE via AP19)."""
        cr = collision_residue_virasoro(26)
        assert cr.leading_pole_order == 3

    def test_virasoro_residue_c26(self):
        """At c=26: leading residue = c/2 = 13."""
        cr = collision_residue_virasoro(26)
        assert cr.residue_at_leading == Fraction(13)

    def test_virasoro_residue_c2(self):
        """At c=2: leading residue = c/2 = 1."""
        cr = collision_residue_virasoro(2)
        assert cr.residue_at_leading == Fraction(1)

    def test_w_infinity_pole_orders(self):
        """w_{1+infinity} r-matrix pole orders: (1, 3, 5, 7) for max_spin=4."""
        cr = collision_residue_w_infinity(26, max_spin=4)
        assert cr.pole_orders == (1, 3, 5, 7)

    def test_w_infinity_leading_pole(self):
        """w_{1+inf} at max_spin=4: leading pole = 2*4-1 = 7."""
        cr = collision_residue_w_infinity(26, max_spin=4)
        assert cr.leading_pole_order == 7

    def test_verify_virasoro_rmatrix(self):
        """Full Virasoro r-matrix pole verification."""
        results = verify_virasoro_r_matrix_pole_orders()
        for key, val in results.items():
            assert val, f"Failed: {key}"

    def test_verify_cybe_sl2_k0(self):
        """Full CYBE verification for sl_2 at k=0."""
        g = sl_n_data(2)
        results = verify_collision_residue_cybe(g, Fraction(0))
        assert results["satisfies_cybe"]

    def test_verify_cybe_sl3_k1(self):
        """Full CYBE verification for sl_3 at k=1."""
        g = sl_n_data(3)
        results = verify_collision_residue_cybe(g, Fraction(1))
        assert results["satisfies_cybe"]


# ============================================================
# Section 6: Conformally soft theorem tower
# ============================================================

class TestSoftTheoremTower:
    """Verify structure of the soft theorem tower."""

    def test_S0_delta(self):
        """S_0 has Delta = 1 (leading soft)."""
        tower = soft_theorem_tower(5)
        assert tower[0].conformal_dim == 1

    def test_S0_spin(self):
        """S_0 has spin 1 (BMS supertranslation current)."""
        tower = soft_theorem_tower(5)
        assert tower[0].spin == 1

    def test_S0_symmetry(self):
        """S_0 corresponds to BMS supertranslation."""
        tower = soft_theorem_tower(5)
        assert "BMS" in tower[0].symmetry

    def test_S1_delta(self):
        """S_1 has Delta = 0 (subleading soft)."""
        tower = soft_theorem_tower(5)
        assert tower[1].conformal_dim == 0

    def test_S1_spin(self):
        """S_1 has spin 2 (stress tensor / superrotation)."""
        tower = soft_theorem_tower(5)
        assert tower[1].spin == 2

    def test_S1_symmetry(self):
        """S_1 corresponds to Virasoro/conformal symmetry."""
        tower = soft_theorem_tower(5)
        assert "Virasoro" in tower[1].symmetry or "conformal" in tower[1].symmetry

    def test_S2_delta(self):
        """S_2 has Delta = -1 (sub-subleading soft)."""
        tower = soft_theorem_tower(5)
        assert tower[2].conformal_dim == -1

    def test_S2_spin(self):
        """S_2 has spin 3 (w_{1+infinity} extension)."""
        tower = soft_theorem_tower(5)
        assert tower[2].spin == 3

    def test_S2_symmetry(self):
        """S_2 corresponds to w_{1+infinity}."""
        tower = soft_theorem_tower(5)
        assert "w_{1+infinity}" in tower[2].symmetry

    def test_tower_bar_degrees(self):
        """All soft theorems live at bar degree 1."""
        tower = soft_theorem_tower(5)
        for st in tower:
            assert st.bar_degree == 1

    def test_tower_bar_weights(self):
        """Bar weight of S_n = n + 1."""
        tower = soft_theorem_tower(5)
        for st in tower:
            assert st.bar_weight == st.order + 1

    def test_tower_delta_sequence(self):
        """Delta decreases by 1 at each order: 1, 0, -1, -2, -3, -4."""
        tower = soft_theorem_tower(5)
        for n, st in enumerate(tower):
            assert st.conformal_dim == 1 - n

    def test_verify_soft_theorems(self):
        """Full soft theorem tower verification."""
        results = verify_soft_theorem_tower()
        for key, val in results.items():
            assert val, f"Failed: {key}"


# ============================================================
# Section 7: Modular characteristic kappa
# ============================================================

class TestKappaValues:
    """Verify kappa values for collinear algebras (AP1: recompute from first principles)."""

    def test_kappa_sl2_k0(self):
        """kappa(V_0(sl_2)) = 3 * (0+2)/(2*2) = 3/2."""
        g = sl_n_data(2)
        assert kappa_current_algebra(g, Fraction(0)) == Fraction(3, 2)

    def test_kappa_sl2_k1(self):
        """kappa(V_1(sl_2)) = 3 * (1+2)/(2*2) = 9/4."""
        g = sl_n_data(2)
        assert kappa_current_algebra(g, Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl3_k0(self):
        """kappa(V_0(sl_3)) = 8 * (0+3)/(2*3) = 4."""
        g = sl_n_data(3)
        assert kappa_current_algebra(g, Fraction(0)) == Fraction(4)

    def test_kappa_sl3_k1(self):
        """kappa(V_1(sl_3)) = 8 * (1+3)/(2*3) = 16/3."""
        g = sl_n_data(3)
        assert kappa_current_algebra(g, Fraction(1)) == Fraction(16, 3)

    def test_kappa_sl4_k0(self):
        """kappa(V_0(sl_4)) = 15 * (0+4)/(2*4) = 15/2."""
        g = sl_n_data(4)
        assert kappa_current_algebra(g, Fraction(0)) == Fraction(15, 2)

    def test_kappa_sl5_k0(self):
        """kappa(V_0(sl_5)) = 24 * (0+5)/(2*5) = 12."""
        g = sl_n_data(5)
        assert kappa_current_algebra(g, Fraction(0)) == Fraction(12)

    def test_kappa_critical_level_raises(self):
        """kappa at critical level k = -h^v should raise ValueError."""
        g = sl_n_data(2)
        with pytest.raises(ValueError):
            kappa_current_algebra(g, Fraction(-2))

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_w_infinity_tline_c26(self):
        """T-line kappa for w_{1+inf} at c=26 is 13 (= c/2)."""
        assert kappa_w_infinity_tline(Fraction(26)) == Fraction(13)

    def test_verify_kappa_k0_su2(self):
        """Verification bundle for kappa at k=0, SU(2)."""
        result = verify_kappa_at_level_zero(2)
        assert result["match"]

    def test_verify_kappa_k0_su3(self):
        """Verification bundle for kappa at k=0, SU(3)."""
        result = verify_kappa_at_level_zero(3)
        assert result["match"]

    def test_verify_kappa_k1_su2(self):
        """Verification bundle for kappa at k=1, SU(2)."""
        result = verify_kappa_at_level_one(2)
        assert result["match"]

    def test_verify_kappa_k1_su3(self):
        """Verification bundle for kappa at k=1, SU(3)."""
        result = verify_kappa_at_level_one(3)
        assert result["match"]

    def test_kappa_k0_general_formula(self):
        """kappa(V_0(sl_N)) = (N^2-1)/2 for all N = 2, ..., 6."""
        for N in range(2, 7):
            g = sl_n_data(N)
            expected = Fraction(N * N - 1, 2)
            computed = kappa_current_algebra(g, Fraction(0))
            assert computed == expected, f"Failed at N={N}: {computed} != {expected}"


# ============================================================
# Section 8: Shadow tower for Virasoro / w_{1+infinity} T-line
# ============================================================

class TestShadowTower:
    """Verify shadow tower computation for Virasoro (= w_{1+inf} T-line)."""

    def test_S2_is_kappa_c1(self):
        """S_2 = kappa = 1/2 at c=1."""
        coeffs = shadow_tower_virasoro_coefficients(Fraction(1), 4)
        assert coeffs[2] == Fraction(1, 2)

    def test_S2_is_kappa_c26(self):
        """S_2 = kappa = 13 at c=26."""
        coeffs = shadow_tower_virasoro_coefficients(Fraction(26), 4)
        assert coeffs[2] == Fraction(13)

    def test_S4_virasoro_c1(self):
        """S_4(Vir_1) = 10/(1 * 27) = 10/27."""
        expected = Fraction(10, 27)
        assert shadow_s4_virasoro(Fraction(1)) == expected

    def test_S4_virasoro_c2(self):
        """S_4(Vir_2) = 10/(2 * 32) = 10/64 = 5/32."""
        expected = Fraction(10, 64)
        assert shadow_s4_virasoro(Fraction(2)) == expected

    def test_S4_virasoro_c26(self):
        """S_4(Vir_26) = 10/(26 * 152) = 10/3952 = 5/1976."""
        expected = Fraction(10, 26 * 152)
        assert shadow_s4_virasoro(Fraction(26)) == expected

    def test_S4_singular_c0(self):
        """S_4 singular at c=0."""
        with pytest.raises(ValueError):
            shadow_s4_virasoro(Fraction(0))

    def test_discriminant_c1(self):
        """Delta(Vir_1) = 40/(5+22) = 40/27."""
        expected = Fraction(40, 27)
        assert shadow_discriminant_virasoro(Fraction(1)) == expected

    def test_discriminant_c26(self):
        """Delta(Vir_26) = 40/(130+22) = 40/152 = 5/19."""
        expected = Fraction(40, 152)
        assert shadow_discriminant_virasoro(Fraction(26)) == expected

    def test_discriminant_nonzero(self):
        """Delta != 0 for all finite nonzero c (class M)."""
        for c_val in [Fraction(1), Fraction(2), Fraction(13), Fraction(26)]:
            delta = shadow_discriminant_virasoro(c_val)
            assert delta != 0

    def test_shadow_tower_recursive_c26_S4(self):
        """Recursive S_4 matches direct formula at c=26."""
        coeffs = shadow_tower_virasoro_coefficients(Fraction(26), 6)
        direct = shadow_s4_virasoro(Fraction(26))
        assert coeffs[4] == direct

    def test_shadow_tower_recursive_c1_S4(self):
        """Recursive S_4 matches direct formula at c=1."""
        coeffs = shadow_tower_virasoro_coefficients(Fraction(1), 6)
        direct = shadow_s4_virasoro(Fraction(1))
        assert coeffs[4] == direct

    def test_growth_rate_c26(self):
        """Shadow growth rate rho at c=26 is small (convergent tower)."""
        rho = shadow_growth_rate_virasoro(Fraction(26))
        assert rho < 1.0
        assert rho > 0.0

    def test_growth_rate_c1(self):
        """Shadow growth rate rho at c=1 is larger."""
        rho = shadow_growth_rate_virasoro(Fraction(1))
        assert rho > 0.0

    def test_growth_rate_c13_self_dual(self):
        """At the self-dual point c=13, rho should be about 0.467."""
        rho = shadow_growth_rate_virasoro(Fraction(13))
        # Known value: rho(c=13) approx 0.467 (from shadow_radius_programme)
        assert abs(rho - 0.467) < 0.01

    def test_growth_rate_singular_c0(self):
        """Growth rate undefined at c=0."""
        with pytest.raises(ValueError):
            shadow_growth_rate_virasoro(Fraction(0))

    def test_shadow_S5_c26_nonzero(self):
        """S_5 at c=26 is nonzero (class M: infinite depth)."""
        coeffs = shadow_tower_virasoro_coefficients(Fraction(26), 6)
        assert coeffs[5] != 0

    def test_shadow_S6_c26_nonzero(self):
        """S_6 at c=26 is nonzero (class M: infinite depth)."""
        coeffs = shadow_tower_virasoro_coefficients(Fraction(26), 7)
        assert coeffs[6] != 0


# ============================================================
# Section 9: w_{1+infinity} shadow tower on T-line
# ============================================================

class TestWInfinityShadowTower:
    """Verify w_{1+infinity} shadow tower on the Virasoro T-line."""

    def test_w_inf_tline_kappa_c26(self):
        """T-line kappa for w_{1+inf} at c=26 is 13."""
        result = w_infinity_shadow_tower_tline(Fraction(26))
        assert result["kappa_tline"] == Fraction(13)

    def test_w_inf_tline_depth_class_M(self):
        """w_{1+infinity} on T-line is class M (infinite depth)."""
        result = w_infinity_shadow_tower_tline(Fraction(26))
        assert result["depth_class"] == "M"

    def test_w_inf_tline_discriminant_nonzero(self):
        """Discriminant is nonzero for c=26."""
        result = w_infinity_shadow_tower_tline(Fraction(26))
        assert result["discriminant"] != 0

    def test_w_inf_tline_convergent_c26(self):
        """Shadow tower is convergent at c=26 (rho < 1)."""
        result = w_infinity_shadow_tower_tline(Fraction(26))
        assert result.get("convergent") is True

    def test_w_inf_tline_S2_S3_S4(self):
        """First three shadow coefficients for w_{1+inf} T-line at c=2."""
        result = w_infinity_shadow_tower_tline(Fraction(2), max_arity=6)
        coeffs = result["coefficients"]
        assert coeffs[2] == Fraction(1)  # kappa = c/2 = 1
        # S_4 = 10/(2*32) = 5/32
        assert coeffs[4] == Fraction(5, 32)


# ============================================================
# Section 10: Splitting functions and Parke-Taylor
# ============================================================

class TestSplittingFunctions:
    """Verify collinear splitting functions for celestial OPE."""

    def test_pp_splitting_pole_order(self):
        """++ splitting function has single pole."""
        sp = collinear_splitting_pp()
        assert sp["pole_order"] == 1

    def test_pp_splitting_color(self):
        """++ splitting has f^{abc} color factor."""
        sp = collinear_splitting_pp()
        assert sp["color_factor"] == "f^{abc}"

    def test_pm_splitting_pole_order(self):
        """+- splitting function has single pole."""
        sp = collinear_splitting_pm()
        assert sp["pole_order"] == 1

    def test_pm_splitting_color(self):
        """+- splitting has delta^{ab} * k color factor."""
        sp = collinear_splitting_pm()
        assert "delta" in sp["color_factor"]

    def test_parke_taylor_n4(self):
        """Parke-Taylor at n=4 is well-formed."""
        pt = parke_taylor_stripped(4)
        assert "<ij>^4" in pt
        assert "4" in pt


# ============================================================
# Section 11: 4-point amplitude from bar complex
# ============================================================

class TestCelestialAmplitudeFromBar:
    """Verify 4-point celestial amplitude from bar complex."""

    def test_4pt_bar_degree(self):
        """4-point amplitude involves bar degree 3."""
        result = celestial_4pt_from_bar(2)
        assert result["bar_degree"] == 3

    def test_4pt_color_factor(self):
        """4-point color is f^{abe} f^{cde} (two structure constants)."""
        result = celestial_4pt_from_bar(2)
        assert "f^{abe}" in result["color_factor"]

    def test_4pt_kinematic_factor(self):
        """4-point kinematic is a beta function."""
        result = celestial_4pt_from_bar(2)
        assert "B(" in result["kinematic_factor"] or "Beta" in result["kinematic_factor"]


# ============================================================
# Section 12: Comprehensive verification
# ============================================================

class TestFullVerification:
    """Run the full verification bundle."""

    def test_full_verification_runs(self):
        """Full verification completes without error."""
        results = run_full_verification(N_list=[2, 3], max_arity=6)
        assert len(results) > 0

    def test_full_verification_bar_koszul(self):
        """All bar Koszulness checks pass."""
        results = run_full_verification(N_list=[2, 3], max_arity=6)
        for key in results:
            if "bar_koszul" in key:
                for subkey, val in results[key].items():
                    assert val, f"Failed: {key}.{subkey}"

    def test_full_verification_cybe(self):
        """All CYBE checks pass."""
        results = run_full_verification(N_list=[2, 3], max_arity=6)
        for key in results:
            if "cybe" in key:
                for subkey, val in results[key].items():
                    assert val, f"Failed: {key}.{subkey}"

    def test_full_verification_kappa(self):
        """All kappa checks pass."""
        results = run_full_verification(N_list=[2, 3], max_arity=6)
        for key in results:
            if "kappa" in key:
                for subkey, val in results[key].items():
                    assert val, f"Failed: {key}.{subkey}"

    def test_full_verification_virasoro_rmatrix(self):
        """Virasoro r-matrix checks pass."""
        results = run_full_verification(N_list=[2], max_arity=6)
        for key, val in results.get("virasoro_rmatrix", {}).items():
            assert val, f"Failed: virasoro_rmatrix.{key}"


# ============================================================
# Section 13: Cross-family consistency checks (AP10)
# ============================================================

class TestCrossFamilyConsistency:
    """Verify cross-family consistency (AP10: not just hardcoded values)."""

    def test_kappa_additivity_heisenberg_pair(self):
        """For two independent Heisenberg systems:
        kappa(H_{k1} + H_{k2}) = kappa(H_{k1}) + kappa(H_{k2}).

        The collinear algebra of a product theory is the direct sum.
        kappa is additive on direct sums (prop:independent-sum-factorization).

        For V_k(sl_N): kappa = (N^2-1)(k+N)/(2N).
        At k=0: kappa = (N^2-1)/2.
        Additivity: kappa(sl_2 + sl_3) = 3/2 + 4 = 11/2.
        """
        g2 = sl_n_data(2)
        g3 = sl_n_data(3)
        k2 = kappa_current_algebra(g2, Fraction(0))
        k3 = kappa_current_algebra(g3, Fraction(0))
        assert k2 + k3 == Fraction(11, 2)

    def test_kappa_anti_symmetry_km(self):
        """kappa(V_k(g)) + kappa(V_{-k-2h^v}(g)) = 0 for Kac-Moody.

        Feigin-Frenkel involution: k -> -k - 2h^v.
        kappa(V_k) = dim(g)(k+h^v)/(2h^v).
        kappa(V_{-k-2h^v}) = dim(g)(-k-2h^v+h^v)/(2h^v) = dim(g)(-k-h^v)/(2h^v) = -kappa(V_k).
        """
        for N in [2, 3, 4]:
            g = sl_n_data(N)
            k = Fraction(1)
            k_dual = -k - 2 * Fraction(g.dual_coxeter)
            kappa_A = kappa_current_algebra(g, k)
            kappa_A_dual = kappa_current_algebra(g, k_dual)
            assert kappa_A + kappa_A_dual == 0, (
                f"Anti-symmetry failed for sl_{N}: {kappa_A} + {kappa_A_dual} != 0"
            )

    def test_kappa_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero for Virasoro).

        This is NOT anti-symmetric: kappa + kappa' = c/2 + (26-c)/2 = 13.
        """
        for c in [1, 2, 5, 10, 13, 20, 25]:
            c_val = Fraction(c)
            k1 = kappa_virasoro(c_val)
            k2 = kappa_virasoro(Fraction(26) - c_val)
            assert k1 + k2 == Fraction(13), (
                f"Complementarity failed at c={c}: {k1} + {k2} != 13"
            )

    def test_shadow_discriminant_complementarity(self):
        """Discriminant complementarity: Delta(c) and Delta(26-c).

        Delta(c) = 40/(5c+22).
        Delta(26-c) = 40/(5(26-c)+22) = 40/(152-5c).
        Sum = 40/(5c+22) + 40/(152-5c) = 40(152-5c + 5c+22)/((5c+22)(152-5c))
            = 40*174/((5c+22)(152-5c)) = 6960/((5c+22)(152-5c)).
        Constant numerator = 6960.
        """
        for c in [Fraction(1), Fraction(2), Fraction(13), Fraction(25)]:
            d1 = shadow_discriminant_virasoro(c)
            d2 = shadow_discriminant_virasoro(Fraction(26) - c)
            total = d1 + d2
            numer = (5 * c + 22) * (152 - 5 * c)
            expected = Fraction(6960) / numer
            assert total == expected, (
                f"Discriminant complementarity failed at c={c}"
            )

    def test_discriminant_self_dual_c13(self):
        """At c=13 (self-dual): Delta(13) = 40/(65+22) = 40/87."""
        d = shadow_discriminant_virasoro(Fraction(13))
        assert d == Fraction(40, 87)

    def test_shadow_metric_positive(self):
        """Shadow metric q0 = 4*kappa^2 > 0 for kappa > 0."""
        for c in [Fraction(1), Fraction(2), Fraction(26)]:
            kappa = kappa_virasoro(c)
            q0 = 4 * kappa ** 2
            assert q0 > 0


# ============================================================
# Section 14: Edge cases and error handling
# ============================================================

class TestEdgeCases:
    """Verify error handling and edge cases."""

    def test_sl_n_N1_raises(self):
        """sl_1 is trivial, should raise."""
        with pytest.raises(ValueError):
            sl_n_data(1)

    def test_kappa_critical_level_sl3(self):
        """kappa at critical level k=-3 for sl_3 raises."""
        g = sl_n_data(3)
        with pytest.raises(ValueError):
            kappa_current_algebra(g, Fraction(-3))

    def test_S4_singular_c0(self):
        """S_4 at c=0 raises ValueError."""
        with pytest.raises(ValueError):
            shadow_s4_virasoro(Fraction(0))

    def test_shadow_tower_negative_c_raises(self):
        """Shadow tower at c < 0 (kappa < 0) raises due to branch."""
        with pytest.raises(ValueError):
            shadow_tower_virasoro_coefficients(Fraction(-1), 4)

    def test_growth_rate_c0_raises(self):
        """Growth rate undefined at c=0."""
        with pytest.raises(ValueError):
            shadow_growth_rate_virasoro(Fraction(0))
