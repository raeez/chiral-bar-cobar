r"""Cross-verification tests for shadow depth classification via 4 independent methods.

Tests the shadow depth classification G/L/C/M across ALL standard families
using four independent computational methods:

    METHOD 1: Direct shadow computation (convolution recursion)
    METHOD 2: Critical discriminant Delta = 8*kappa*S_4
    METHOD 3: Shadow metric factorization Q_L(t)
    METHOD 4: A-infinity / L-infinity formality level

Every family is verified by all four methods, which must agree.
Additionally tests: shadow radius for class M, DS depth increase,
complementarity of discriminants, admissible level depth.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    conj:operadic-complexity (higher_genus_modular_koszul.tex)
    thm:ds-koszul-obstruction (w_algebras.tex)
"""

import pytest
from fractions import Fraction

from compute.lib.shadow_depth_cross_verification import (
    # Family constructors
    heisenberg_family,
    lattice_family,
    free_fermion_family,
    affine_slN_family,
    non_simply_laced_family,
    betagamma_family,
    bc_ghost_family,
    virasoro_family,
    w_algebra_family,
    admissible_sl2_family,
    build_family_registry,
    # 4 methods
    method1_direct_shadow,
    method2_discriminant,
    method3_metric_factorization,
    method4_formality_level,
    # Cross-verification
    cross_verify,
    cross_verify_all,
    CrossVerificationResult,
    # Shadow radius
    shadow_radius,
    shadow_radius_float,
    virasoro_shadow_radius_at_c,
    # DS and complementarity
    ds_depth_increase_verification,
    complementarity_discriminant_check,
)


# ============================================================================
# SECTION 1: All 4 methods agree for each family (80+ tests)
# ============================================================================

class TestCrossVerificationAgreement:
    """All 4 methods must agree on class and depth for every family."""

    # --- CLASS G: Gaussian, depth 2 ---

    def test_heisenberg_k1(self):
        result = cross_verify(heisenberg_family(Fraction(1)))
        assert result.all_agree
        assert result.agreed_class == 'G'
        assert result.agreed_depth == 2

    def test_heisenberg_k5(self):
        result = cross_verify(heisenberg_family(Fraction(5)))
        assert result.all_agree
        assert result.agreed_class == 'G'
        assert result.agreed_depth == 2

    def test_heisenberg_k_half(self):
        result = cross_verify(heisenberg_family(Fraction(1, 2)))
        assert result.all_agree
        assert result.agreed_class == 'G'
        assert result.agreed_depth == 2

    def test_free_fermion(self):
        result = cross_verify(free_fermion_family())
        assert result.all_agree
        assert result.agreed_class == 'G'
        assert result.agreed_depth == 2

    @pytest.mark.parametrize("rank", [1, 2, 4, 8, 16, 24])
    def test_lattice_rank(self, rank):
        result = cross_verify(lattice_family(rank))
        assert result.all_agree
        assert result.agreed_class == 'G'
        assert result.agreed_depth == 2

    # --- CLASS L: Lie/tree, depth 3 ---

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_affine_slN(self, N):
        result = cross_verify(affine_slN_family(N, Fraction(1)))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_affine_sl2_k5(self):
        result = cross_verify(affine_slN_family(2, Fraction(5)))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_affine_sl3_k10(self):
        result = cross_verify(affine_slN_family(3, Fraction(10)))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_B2_non_simply_laced(self):
        """so_5, dim=10, h^vee=3."""
        result = cross_verify(non_simply_laced_family('B', 2, 10, 3))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_C2_non_simply_laced(self):
        """sp_4, dim=10, h^vee=3."""
        result = cross_verify(non_simply_laced_family('C', 2, 10, 3))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_G2_non_simply_laced(self):
        """G_2, dim=14, h^vee=4."""
        result = cross_verify(non_simply_laced_family('G', 2, 14, 4))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_F4_non_simply_laced(self):
        """F_4, dim=52, h^vee=9."""
        result = cross_verify(non_simply_laced_family('F', 4, 52, 9))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    # --- CLASS C: Contact/quartic, depth 4 ---

    def test_betagamma_standard(self):
        result = cross_verify(betagamma_family(Fraction(0)))
        assert result.all_agree
        assert result.agreed_class == 'C'
        assert result.agreed_depth == 4

    def test_betagamma_weight1(self):
        result = cross_verify(betagamma_family(Fraction(1)))
        assert result.all_agree
        assert result.agreed_class == 'C'
        assert result.agreed_depth == 4

    def test_betagamma_symplectic(self):
        result = cross_verify(betagamma_family(Fraction(1, 2)))
        assert result.all_agree
        assert result.agreed_class == 'C'
        assert result.agreed_depth == 4

    def test_bc_ghost_spin2(self):
        result = cross_verify(bc_ghost_family(Fraction(2)))
        assert result.all_agree
        assert result.agreed_class == 'C'
        assert result.agreed_depth == 4

    # --- CLASS M: Mixed, depth infinity ---

    @pytest.mark.parametrize("c_val", [
        Fraction(1, 2), Fraction(7, 10), Fraction(1), Fraction(2),
        Fraction(13), Fraction(25), Fraction(26),
    ])
    def test_virasoro(self, c_val):
        result = cross_verify(virasoro_family(c_val))
        assert result.all_agree
        assert result.agreed_class == 'M'
        assert result.agreed_depth is None  # infinity

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8])
    def test_w_algebra_tline(self, N):
        result = cross_verify(w_algebra_family(N, Fraction(5)))
        assert result.all_agree
        assert result.agreed_class == 'M'
        assert result.agreed_depth is None

    # --- Admissible levels ---

    def test_admissible_sl2_k_minus_half(self):
        """k = -1/2 (p=3, q=2)."""
        result = cross_verify(admissible_sl2_family(3, 2))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_admissible_sl2_k_minus_4_3(self):
        """k = -4/3 (p=2, q=3)."""
        result = cross_verify(admissible_sl2_family(2, 3))
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3


class TestFullRegistryCrossVerification:
    """Run cross-verification on the entire family registry."""

    def test_all_families_agree(self):
        """ALL families in the registry must have 4-method agreement."""
        results = cross_verify_all(max_arity=12)
        failures = [(name, r) for name, r in results.items() if not r.all_agree]
        assert len(failures) == 0, (
            f"{len(failures)} families disagreed: " +
            ", ".join(f"{n}: {r.discrepancies}" for n, r in failures))

    def test_registry_has_at_least_35_families(self):
        """Ensure comprehensive coverage."""
        registry = build_family_registry()
        assert len(registry) >= 35

    def test_all_four_classes_represented(self):
        """All four classes G, L, C, M must be represented."""
        results = cross_verify_all(max_arity=12)
        classes = {r.agreed_class for r in results.values()}
        assert 'G' in classes
        assert 'L' in classes
        assert 'C' in classes
        assert 'M' in classes


# ============================================================================
# SECTION 2: Method-specific verification
# ============================================================================

class TestMethod1DirectShadow:
    """Verify that method 1 produces correct shadow coefficients."""

    def test_heisenberg_all_zero_beyond_kappa(self):
        data = heisenberg_family(Fraction(3))
        m1 = method1_direct_shadow(data, max_arity=10)
        assert m1['coefficients'][2] == Fraction(3)
        for r in range(3, 11):
            assert m1['coefficients'][r] == Fraction(0)

    def test_affine_sl2_cubic_nonzero(self):
        data = affine_slN_family(2, Fraction(1))
        m1 = method1_direct_shadow(data, max_arity=10)
        assert m1['coefficients'][3] != Fraction(0)
        for r in range(4, 11):
            assert m1['coefficients'][r] == Fraction(0)

    def test_virasoro_quartic_matches_formula(self):
        """S_4(Vir_c) = 10/[c(5c+22)] from Q^contact_Vir."""
        c_val = Fraction(26)
        data = virasoro_family(c_val)
        m1 = method1_direct_shadow(data, max_arity=6)
        expected_S4 = Fraction(10) / (c_val * (5 * c_val + 22))
        assert m1['coefficients'][4] == expected_S4

    def test_virasoro_all_nonzero(self):
        """For class M, S_r != 0 for all r >= 2."""
        data = virasoro_family(Fraction(13))
        m1 = method1_direct_shadow(data, max_arity=15)
        for r in range(2, 16):
            assert m1['coefficients'][r] != Fraction(0), f"S_{r} = 0 for Virasoro at c=13"

    def test_betagamma_quartic_on_line(self):
        """On the bg single line (alpha=0): S_3 = 0, S_4 != 0, S_5 = 0, S_6 != 0."""
        data = betagamma_family(Fraction(0))
        m1 = method1_direct_shadow(data, max_arity=8)
        assert m1['coefficients'][3] == Fraction(0), "S_3 should be 0 (alpha=0)"
        assert m1['coefficients'][4] != Fraction(0), "S_4 should be nonzero (contact)"
        assert m1['coefficients'][5] == Fraction(0), "S_5 should be 0 (odd, alpha=0)"
        assert m1['coefficients'][6] != Fraction(0), "S_6 should be nonzero (even cascade)"

    def test_lattice_leech_kappa_24(self):
        """Leech lattice: rank=24, kappa=24."""
        data = lattice_family(24)
        m1 = method1_direct_shadow(data, max_arity=6)
        assert m1['coefficients'][2] == Fraction(24)

    def test_s2_equals_kappa(self):
        """S_2 = kappa for all families."""
        registry = build_family_registry()
        for name, data in registry.items():
            m1 = method1_direct_shadow(data, max_arity=4)
            assert (m1['coefficients'][2] == data.kappa or
                    m1['coefficients'][2] == -data.kappa), (
                f"{name}: S_2 = {m1['coefficients'][2]} != kappa = {data.kappa}")


class TestMethod2Discriminant:
    """Verify method 2 discriminant classification."""

    def test_delta_zero_for_G(self):
        data = heisenberg_family(Fraction(1))
        m2 = method2_discriminant(data)
        assert m2['Delta'] == 0
        assert m2['depth_class'] == 'G'

    def test_delta_zero_for_L(self):
        data = affine_slN_family(3, Fraction(1))
        m2 = method2_discriminant(data)
        assert m2['Delta'] == 0
        assert m2['depth_class'] == 'L'

    def test_delta_nonzero_for_C(self):
        data = betagamma_family(Fraction(0))
        m2 = method2_discriminant(data)
        assert m2['Delta'] != 0
        assert m2['depth_class'] == 'C'

    def test_delta_nonzero_for_M(self):
        data = virasoro_family(Fraction(26))
        m2 = method2_discriminant(data)
        assert m2['Delta'] != 0
        assert m2['depth_class'] == 'M'

    def test_delta_formula_virasoro(self):
        """Delta(Vir_c) = 40/(5c+22)."""
        c_val = Fraction(13)
        data = virasoro_family(c_val)
        m2 = method2_discriminant(data)
        expected = Fraction(40) / (5 * c_val + 22)
        assert m2['Delta'] == expected

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_delta_zero_all_slN(self, N):
        """All affine sl_N must have Delta = 0."""
        data = affine_slN_family(N)
        m2 = method2_discriminant(data)
        assert m2['Delta'] == 0


class TestMethod3MetricFactorization:
    """Verify method 3 shadow metric factorization."""

    def test_perfect_square_heisenberg(self):
        data = heisenberg_family(Fraction(5))
        m3 = method3_metric_factorization(data)
        assert m3['is_perfect_square'] is True
        assert m3['depth_class'] == 'G'

    def test_perfect_square_affine(self):
        data = affine_slN_family(3, Fraction(1))
        m3 = method3_metric_factorization(data)
        assert m3['is_perfect_square'] is True
        assert m3['depth_class'] == 'L'

    def test_irreducible_virasoro(self):
        data = virasoro_family(Fraction(26))
        m3 = method3_metric_factorization(data)
        assert m3['is_perfect_square'] is False
        assert m3['depth_class'] == 'M'

    def test_pure_quadratic_betagamma(self):
        data = betagamma_family(Fraction(0))
        m3 = method3_metric_factorization(data)
        assert m3['is_perfect_square'] is False
        assert m3['depth_class'] == 'C'

    def test_discriminant_identity(self):
        """disc(Q_L) = -32*kappa^2*Delta for all families."""
        registry = build_family_registry()
        for name, data in registry.items():
            m3 = method3_metric_factorization(data)
            expected_disc = -32 * data.kappa**2 * (8 * data.kappa * data.S4)
            assert m3['disc_QL'] == expected_disc, (
                f"{name}: disc_QL mismatch")


class TestMethod4FormalityLevel:
    """Verify method 4 A-infinity formality classification."""

    def test_formal_heisenberg(self):
        data = heisenberg_family(Fraction(1))
        m4 = method4_formality_level(data)
        assert m4['depth_class'] == 'G'
        assert m4['first_nonzero_mn'] is None

    def test_quasi_formal_affine(self):
        data = affine_slN_family(2, Fraction(1))
        m4 = method4_formality_level(data)
        assert m4['depth_class'] == 'L'
        assert m4['first_nonzero_mn'] == 3

    def test_depth4_betagamma(self):
        data = betagamma_family(Fraction(0))
        m4 = method4_formality_level(data)
        assert m4['depth_class'] == 'C'
        assert m4['first_nonzero_mn'] == 4

    def test_nonformal_virasoro(self):
        data = virasoro_family(Fraction(26))
        m4 = method4_formality_level(data)
        assert m4['depth_class'] == 'M'
        assert m4['first_nonzero_mn'] == 3


# ============================================================================
# SECTION 3: Shadow radius for class M
# ============================================================================

class TestShadowRadius:
    """Test shadow growth rate rho for class M families."""

    def test_virasoro_selfdual_c13(self):
        """rho(Vir_13) approx 0.4674 (self-dual point)."""
        rho = virasoro_shadow_radius_at_c(Fraction(13))
        assert abs(rho - 0.4674) < 0.001

    def test_virasoro_c26_convergent(self):
        """rho(Vir_26) approx 0.232 < 1 (convergent)."""
        rho = virasoro_shadow_radius_at_c(Fraction(26))
        assert rho < 1.0
        assert abs(rho - 0.2325) < 0.001

    def test_virasoro_c1_divergent(self):
        """rho(Vir_1) >> 1 (divergent, small c)."""
        rho = virasoro_shadow_radius_at_c(Fraction(1))
        assert rho > 1.0

    def test_virasoro_ising_divergent(self):
        """rho(Vir_{1/2}) >> 1 (Ising model, divergent)."""
        rho = virasoro_shadow_radius_at_c(Fraction(1, 2))
        assert rho > 1.0

    def test_selfdual_symmetry(self):
        """rho(Vir_c) = rho(Vir_{26-c}) at c=13 (self-dual point)."""
        rho_13 = virasoro_shadow_radius_at_c(Fraction(13))
        rho_13_dual = virasoro_shadow_radius_at_c(Fraction(26 - 13))
        assert abs(rho_13 - rho_13_dual) < 1e-12

    def test_koszul_dual_radius_asymmetry(self):
        """rho(Vir_c) != rho(Vir_{26-c}) for c != 13."""
        rho_1 = virasoro_shadow_radius_at_c(Fraction(1))
        rho_25 = virasoro_shadow_radius_at_c(Fraction(25))
        # rho(1) and rho(25) are the Koszul dual pair
        # They are NOT equal (unlike at self-dual c=13)
        assert abs(rho_1 - rho_25) > 0.1

    def test_shadow_radius_zero_for_class_G(self):
        """Class G has rho = 0."""
        rho = shadow_radius_float(heisenberg_family(Fraction(1)))
        assert rho == 0.0

    def test_shadow_radius_zero_for_class_L(self):
        """Class L has rho = 0 (tower terminates)."""
        rho = shadow_radius_float(affine_slN_family(3, Fraction(1)))
        assert rho == 0.0

    def test_shadow_radius_none_for_class_C(self):
        """Class C has no single-line radius (stratum separation)."""
        rho = shadow_radius_float(betagamma_family(Fraction(0)))
        assert rho is None

    def test_shadow_radius_positive_for_class_M(self):
        """Class M has rho > 0."""
        rho = shadow_radius_float(virasoro_family(Fraction(26)))
        assert rho is not None
        assert rho > 0

    def test_virasoro_radius_monotone_large_c(self):
        """rho(Vir_c) is decreasing for large c (convergence improves)."""
        rho_10 = virasoro_shadow_radius_at_c(Fraction(10))
        rho_20 = virasoro_shadow_radius_at_c(Fraction(20))
        rho_50 = virasoro_shadow_radius_at_c(Fraction(50))
        assert rho_10 > rho_20 > rho_50

    def test_critical_cubic_root(self):
        """The critical c* where rho = 1 satisfies 5c^3 + 22c^2 - 180c - 872 = 0.

        c* is approximately 6.1243.
        """
        # Evaluate rho at c slightly above and below c*
        rho_6 = virasoro_shadow_radius_at_c(Fraction(6))
        rho_7 = virasoro_shadow_radius_at_c(Fraction(7))
        # rho(6) > 1 and rho(7) < 1, confirming c* is between 6 and 7
        assert rho_6 > 1.0
        assert rho_7 < 1.0


# ============================================================================
# SECTION 4: DS depth increase
# ============================================================================

class TestDSDepthIncrease:
    """Verify DS reduction increases shadow depth: sl_N (L) -> W_N (M)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_ds_increases_depth(self, N):
        """sl_N is class L (depth 3), W_N is class M (depth infinity)."""
        result = ds_depth_increase_verification(N)
        assert result['sl_N_class'] == 'L'
        assert result['sl_N_depth'] == 3
        assert result['W_N_class'] == 'M'
        assert result['W_N_depth'] is None  # infinity
        assert result['depth_increased'] is True

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_ds_rho_positive(self, N):
        """W_N must have positive shadow radius (class M)."""
        result = ds_depth_increase_verification(N)
        assert result['rho_W_N'] is not None
        assert result['rho_W_N'] > 0

    def test_ghost_sector_creates_quartic(self):
        """The quartic S_4 of W_N is nonzero (from BRST coupling).

        For W_2 = Virasoro: S_4 = 10/[c(5c+22)] != 0.
        """
        k_val = Fraction(5)
        wn_data = w_algebra_family(2, k_val)
        m1 = method1_direct_shadow(wn_data, max_arity=6)
        assert m1['coefficients'][4] != Fraction(0)


# ============================================================================
# SECTION 5: Complementarity of discriminants
# ============================================================================

class TestComplementarity:
    """Verify complementarity formulas for Koszul dual pairs."""

    @pytest.mark.parametrize("c_val", [
        Fraction(1), Fraction(5), Fraction(13), Fraction(25),
    ])
    def test_complementarity_formula(self, c_val):
        """Delta(Vir_c) + Delta(Vir_{26-c}) = 6960/((5c+22)(152-5c))."""
        result = complementarity_discriminant_check(c_val)
        assert result['match'] is True

    def test_selfdual_complementarity(self):
        """At c=13 (self-dual): Delta(A) = Delta(A!)."""
        result = complementarity_discriminant_check(Fraction(13))
        assert abs(result['Delta_A'] - result['Delta_A_dual']) < 1e-15

    def test_selfdual_rho_equality(self):
        """At c=13: rho(Vir_13) = rho(Vir_13) (self-dual)."""
        result = complementarity_discriminant_check(Fraction(13))
        assert result['rho_A'] is not None
        assert result['rho_A_dual'] is not None
        assert abs(result['rho_A'] - result['rho_A_dual']) < 1e-12

    def test_duality_exchange_symmetry(self):
        """Delta(Vir_c) at c and Delta(Vir_{26-c}) at c should exchange under c->26-c."""
        r1 = complementarity_discriminant_check(Fraction(1))
        r25 = complementarity_discriminant_check(Fraction(25))
        assert abs(r1['Delta_A'] - r25['Delta_A_dual']) < 1e-15
        assert abs(r1['Delta_A_dual'] - r25['Delta_A']) < 1e-15


# ============================================================================
# SECTION 6: Admissible level depth (new computation)
# ============================================================================

class TestAdmissibleLevelDepth:
    """Admissible levels of sl_2 remain class L (same as generic level).

    This is a genuinely new verification: at fractional levels, the module
    category changes (becomes non-semisimple), but the SHADOW DEPTH
    classification does not change because it depends on the OPE structure
    of the UNIVERSAL algebra, not on the module category.
    """

    def test_k_minus_half(self):
        """k = -1/2: admissible, still class L."""
        data = admissible_sl2_family(3, 2)  # k = 3/2 - 2 = -1/2
        result = cross_verify(data)
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_k_minus_4_3(self):
        """k = -4/3: admissible, still class L."""
        data = admissible_sl2_family(2, 3)  # k = 2/3 - 2 = -4/3
        result = cross_verify(data)
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3

    def test_admissible_kappa_positive(self):
        """At k = -1/2: kappa = 3*(-1/2+2)/4 = 3*(3/2)/4 = 9/8 > 0."""
        data = admissible_sl2_family(3, 2)
        assert data.kappa == Fraction(9, 8)
        assert data.kappa > 0

    def test_admissible_kappa_formula(self):
        """At k = -4/3: kappa = 3*(-4/3+2)/4 = 3*(2/3)/4 = 1/2."""
        data = admissible_sl2_family(2, 3)
        assert data.kappa == Fraction(1, 2)

    @pytest.mark.parametrize("p,q", [
        (3, 2),  # k = -1/2
        (2, 3),  # k = -4/3
        (4, 1),  # k = 2 (integrable)
        (5, 2),  # k = 1/2
        (3, 4),  # k = -5/4
    ])
    def test_admissible_all_class_L(self, p, q):
        """All admissible levels give class L."""
        data = admissible_sl2_family(p, q)
        result = cross_verify(data)
        assert result.all_agree
        assert result.agreed_class == 'L'
        assert result.agreed_depth == 3


# ============================================================================
# SECTION 7: Non-simply-laced families
# ============================================================================

class TestNonSimplyLaced:
    """All non-simply-laced affine KM are class L (AP3 prevention)."""

    def test_B2_class_L(self):
        """B_2 = so_5: dim=10, h^vee=3."""
        result = cross_verify(non_simply_laced_family('B', 2, 10, 3))
        assert result.all_agree and result.agreed_class == 'L'

    def test_C2_class_L(self):
        """C_2 = sp_4: dim=10, h^vee=3."""
        result = cross_verify(non_simply_laced_family('C', 2, 10, 3))
        assert result.all_agree and result.agreed_class == 'L'

    def test_G2_class_L(self):
        """G_2: dim=14, h^vee=4."""
        result = cross_verify(non_simply_laced_family('G', 2, 14, 4))
        assert result.all_agree and result.agreed_class == 'L'

    def test_F4_class_L(self):
        """F_4: dim=52, h^vee=9."""
        result = cross_verify(non_simply_laced_family('F', 4, 52, 9))
        assert result.all_agree and result.agreed_class == 'L'

    def test_G2_no_cubic_casimir_but_S3_nonzero(self):
        """G_2 has no degree-3 Casimir (exponents [1,5]) but S_3 != 0.

        S_3 comes from the ANTISYMMETRIC structure constants f^{abc},
        not from symmetric d_{abc} (which doesn't exist for G_2).
        """
        data = non_simply_laced_family('G', 2, 14, 4)
        m1 = method1_direct_shadow(data, max_arity=6)
        assert m1['coefficients'][3] != Fraction(0)

    def test_kappa_B2_formula(self):
        """kappa(B_2, k=1) = 10*(1+3)/(2*3) = 20/3."""
        data = non_simply_laced_family('B', 2, 10, 3, Fraction(1))
        assert data.kappa == Fraction(20, 3)


# ============================================================================
# SECTION 8: Shadow coefficient structure
# ============================================================================

class TestShadowCoefficientStructure:
    """Structural tests on shadow coefficients across classes."""

    def test_class_G_only_kappa_nonzero(self):
        """Class G: S_r = 0 for all r >= 3."""
        for data in [heisenberg_family(Fraction(1)),
                     lattice_family(8),
                     free_fermion_family()]:
            m1 = method1_direct_shadow(data, max_arity=10)
            for r in range(3, 11):
                assert m1['coefficients'][r] == 0, f"S_{r} != 0 for {data.name}"

    def test_class_L_only_kappa_and_cubic(self):
        """Class L: S_3 != 0, S_r = 0 for r >= 4."""
        for data in [affine_slN_family(2), affine_slN_family(5),
                     non_simply_laced_family('G', 2, 14, 4)]:
            m1 = method1_direct_shadow(data, max_arity=10)
            assert m1['coefficients'][3] != 0, f"S_3 = 0 for {data.name}"
            for r in range(4, 11):
                assert m1['coefficients'][r] == 0, f"S_{r} != 0 for {data.name}"

    def test_class_C_odd_arities_vanish_on_line(self):
        """Class C on single line (alpha=0): odd arities vanish."""
        data = betagamma_family(Fraction(0))
        m1 = method1_direct_shadow(data, max_arity=10)
        for r in [3, 5, 7, 9]:
            assert m1['coefficients'][r] == 0, f"S_{r} != 0 for bg (should be 0, alpha=0)"

    def test_class_C_even_arities_nonzero_on_line(self):
        """Class C on single line: even arities >= 4 are nonzero."""
        data = betagamma_family(Fraction(0))
        m1 = method1_direct_shadow(data, max_arity=10)
        for r in [4, 6, 8, 10]:
            assert m1['coefficients'][r] != 0, f"S_{r} = 0 for bg (even cascade)"

    def test_class_M_all_nonzero_from_3(self):
        """Class M: S_r != 0 for all r >= 3 (both odd and even)."""
        data = virasoro_family(Fraction(26))
        m1 = method1_direct_shadow(data, max_arity=15)
        for r in range(3, 16):
            assert m1['coefficients'][r] != 0, f"S_{r} = 0 for Vir_26 (class M)"


# ============================================================================
# SECTION 9: Consistency with existing shadow_radius.py module
# ============================================================================

class TestConsistencyWithExistingModule:
    """Cross-check against existing shadow_radius.py computations."""

    def test_virasoro_rho_formula_match(self):
        """Our rho matches the formula rho^2 = (180c+872)/((5c+22)*c^2)."""
        c_val = Fraction(13)
        rho = virasoro_shadow_radius_at_c(c_val)
        expected_sq = float(Fraction(180 * 13 + 872) / (Fraction(5 * 13 + 22) * 13**2))
        assert abs(rho**2 - expected_sq) < 1e-12

    def test_virasoro_selfdual_rho_approximately_0_467(self):
        """rho(Vir_13) ~ 0.467 from shadow_radius.py."""
        rho = virasoro_shadow_radius_at_c(Fraction(13))
        assert abs(rho - 0.467396) < 0.001

    def test_delta_formula_virasoro_40_over_5c22(self):
        """Delta(Vir_c) = 40/(5c+22) matches shadow_radius.py."""
        c_val = Fraction(26)
        data = virasoro_family(c_val)
        m2 = method2_discriminant(data)
        expected = Fraction(40) / (5 * c_val + 22)
        assert m2['Delta'] == expected


# ============================================================================
# SECTION 10: Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary behavior."""

    def test_large_rank_lattice(self):
        """Lattice at rank 24 (Leech): still class G."""
        result = cross_verify(lattice_family(24))
        assert result.all_agree and result.agreed_class == 'G'

    def test_small_c_virasoro(self):
        """Virasoro at c = 1/2 (Ising): class M with large rho."""
        data = virasoro_family(Fraction(1, 2))
        result = cross_verify(data)
        assert result.all_agree and result.agreed_class == 'M'
        rho = virasoro_shadow_radius_at_c(Fraction(1, 2))
        assert rho > 10  # very divergent

    def test_large_N_affine(self):
        """sl_8 at k=1: still class L."""
        result = cross_verify(affine_slN_family(8, Fraction(1)))
        assert result.all_agree and result.agreed_class == 'L'

    def test_w8_tline(self):
        """W_8 on T-line: class M."""
        result = cross_verify(w_algebra_family(8, Fraction(5)))
        assert result.all_agree and result.agreed_class == 'M'

    def test_betagamma_negative_kappa(self):
        """bg at lambda=1/2: kappa = -1/2 < 0.  Still class C."""
        data = betagamma_family(Fraction(1, 2))
        assert data.kappa == Fraction(-1, 2)
        result = cross_verify(data)
        assert result.all_agree and result.agreed_class == 'C'

    def test_bc_large_negative_kappa(self):
        """bc at j=2: kappa = -13.  Still class C."""
        data = bc_ghost_family(Fraction(2))
        assert data.kappa == Fraction(-13)
        result = cross_verify(data)
        assert result.all_agree and result.agreed_class == 'C'


# ============================================================================
# SECTION 11: Kappa values (AP1 cross-check)
# ============================================================================

class TestKappaValues:
    """Cross-check kappa values against known formulas (AP1 mitigation)."""

    def test_heisenberg_kappa_equals_k(self):
        data = heisenberg_family(Fraction(7))
        assert data.kappa == Fraction(7)

    def test_virasoro_kappa_c_over_2(self):
        data = virasoro_family(Fraction(26))
        assert data.kappa == Fraction(13)

    def test_sl2_kappa_3k2_over_4(self):
        data = affine_slN_family(2, Fraction(1))
        assert data.kappa == Fraction(3) * (1 + 2) / 4  # 9/4

    def test_sl3_kappa(self):
        data = affine_slN_family(3, Fraction(1))
        # (9-1)*(1+3)/(2*3) = 8*4/6 = 32/6 = 16/3
        assert data.kappa == Fraction(16, 3)

    def test_betagamma_kappa_6lam2_6lam_1(self):
        data = betagamma_family(Fraction(0))
        assert data.kappa == Fraction(1)  # 6*0 - 6*0 + 1

    def test_bc_kappa_negative(self):
        data = bc_ghost_family(Fraction(2))
        # -(6*4 - 6*2 + 1) = -(24-12+1) = -13
        assert data.kappa == Fraction(-13)

    def test_lattice_kappa_equals_rank(self):
        data = lattice_family(8)
        assert data.kappa == Fraction(8)

    def test_free_fermion_kappa_quarter(self):
        data = free_fermion_family()
        assert data.kappa == Fraction(1, 4)
