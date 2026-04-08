r"""Tests for the deep twisted holography engine.

Organized by the five identification axes plus multi-path verification.

60+ tests covering:
  Axis 1: Zeng's boundary = universal defect via Koszul duality
  Axis 2: Garner-Paquette scattering with charged sources
  Axis 3: Omega-background -> bar-cobar identification
  Axis 4: Reproducible computations from shadow obstruction tower
  Axis 5: Extensions beyond twisted holography
  Multi-path: 3+ independent verification paths per claim
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_twisted_holography_deep_engine import (
    # Helpers
    _frac, _bernoulli_exact, _lambda_fp,
    # Lie data
    lie_dim, lie_h_dual, lie_name,
    # Boundary algebra
    BoundaryChiralAlgebra,
    make_boundary_sl_N, make_boundary_heisenberg,
    # Koszul dual
    compute_koszul_dual,
    # Collision residue
    compute_collision_residue, verify_cybe_from_mc,
    # Derived center
    compute_derived_center,
    # Triangle
    construct_triangle,
    # Holographic datum
    construct_holographic_datum,
    # Genus expansion
    genus_g_partition_function, genus_expansion_terms,
    # Celestial OPE
    compute_celestial_ope, collinear_splitting_from_shadow,
    # Boundary modular class
    compute_boundary_modular_class,
    # Comparison
    twisted_holography_comparison_table,
    # Omega-background
    omega_background_identification,
    # Anomaly
    anomaly_cancellation_check,
    # GZ differentials
    gz_commuting_differentials,
    # Multi-path
    verify_kappa_three_paths, verify_duality_constraint,
    # Full analysis
    full_twisted_holography_analysis, heisenberg_twisted_holography_analysis,
)


# ============================================================================
# Helpers
# ============================================================================

class TestHelpers:
    """Test exact arithmetic helpers."""

    def test_bernoulli_b0(self):
        assert _bernoulli_exact(0) == Fraction(1)

    def test_bernoulli_b1(self):
        assert _bernoulli_exact(1) == Fraction(-1, 2)

    def test_bernoulli_b2(self):
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_bernoulli_odd_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_exact(n) == 0

    def test_lambda_fp_genus1(self):
        """lambda_1 = 1/24."""
        assert _lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2 = 7/5760 (NOT 1/1152, AP38)."""
        assert _lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3 = 31/967680."""
        assert _lambda_fp(3) == Fraction(31, 967680)


# ============================================================================
# Axis 1: Zeng's boundary = universal defect via Koszul duality
# ============================================================================

class TestAxis1ZengBoundaryDefect:
    """Zeng [2302.06693]: boundary chiral algebra = universal defect
    chiral algebra via Koszul duality.

    In our framework:
      boundary = input A, universal defect = A^! = (H*(B(A)))^v.
    """

    def test_sl2_boundary_is_input(self):
        """Boundary algebra for SU(2) CS at level k is sl(2)_k."""
        A = make_boundary_sl_N(2, Fraction(1))
        assert A.name == "sl(2)_1"
        assert A.lie_type == "A"
        assert A.rank == 1

    def test_sl3_boundary(self):
        """Boundary for SU(3) CS at k=1."""
        A = make_boundary_sl_N(3, Fraction(1))
        assert A.dim_g == 8
        assert A.h_dual == 3

    def test_heisenberg_boundary(self):
        """Boundary for GL(1) CS at k."""
        A = make_boundary_heisenberg(Fraction(1))
        assert A.name == "H_1"
        assert A.kappa == Fraction(1)

    def test_universal_defect_is_koszul_dual(self):
        """The universal defect algebra IS A^!."""
        A = make_boundary_sl_N(2, Fraction(1))
        dual = compute_koszul_dual(A)
        # A^! has opposite kappa (FF involution)
        assert dual.kappa_dual == -A.kappa
        assert dual.is_anti_symmetric

    def test_heisenberg_defect_not_h_minus_k(self):
        """AP33: H_k^! = Sym^ch(V*), NOT H_{-k} as algebras.

        They have the same kappa but are different chiral algebras.
        """
        A = make_boundary_heisenberg(Fraction(3))
        dual = compute_koszul_dual(A)
        # Same kappa as H_{-k}
        assert dual.kappa_dual == -Fraction(3)
        # But the NAME is (H_3)^!, not H_{-3}
        assert "^!" in dual.name

    def test_boundary_bulk_distinction_ap34(self):
        """AP34: bar-cobar inversion != open-to-closed.

        The bulk is the derived center, NOT the bar complex.
        """
        A = make_boundary_sl_N(2, Fraction(1))
        triangle = construct_triangle(A)
        assert triangle.bar_is_not_bulk
        assert triangle.bulk_is_derived_center_of_boundary

    def test_koszul_duality_anti_symmetry_sl_N(self):
        """kappa(A) + kappa(A^!) = 0 for affine KM (AP24)."""
        for N in [2, 3, 4, 5]:
            A = make_boundary_sl_N(N, Fraction(1))
            dual = compute_koszul_dual(A)
            assert dual.kappa_sum == 0, f"Failed for sl({N})"

    def test_koszul_duality_anti_symmetry_heisenberg(self):
        """kappa(H_k) + kappa(H_k^!) = 0."""
        for k in [1, 2, 3, 5, 10]:
            A = make_boundary_heisenberg(Fraction(k))
            dual = compute_koszul_dual(A)
            assert dual.kappa_sum == 0

    def test_ff_involution_sl2(self):
        """Feigin-Frenkel involution for sl(2): k -> -k - 4."""
        A = make_boundary_sl_N(2, Fraction(1))
        dual = compute_koszul_dual(A)
        assert dual.ff_dual_level == Fraction(-5)  # -1 - 2*2 = -5

    def test_ff_involution_sl3(self):
        """FF involution for sl(3): k -> -k - 6."""
        A = make_boundary_sl_N(3, Fraction(2))
        dual = compute_koszul_dual(A)
        assert dual.ff_dual_level == Fraction(-8)  # -2 - 2*3 = -8


# ============================================================================
# Axis 2: Garner-Paquette scattering with charged sources
# ============================================================================

class TestAxis2GarnerPaquetteScattering:
    """Garner-Paquette [2408.11092]: scattering off twistorial line defects.

    Line defects are modules in C = A^!-mod.
    Scattering = correlators of the celestial chiral algebra.
    """

    def test_line_category_is_dual_modules(self):
        """C_line ~ A^!-mod on the Koszul locus."""
        A = make_boundary_sl_N(2, Fraction(1))
        triangle = construct_triangle(A)
        assert triangle.line_category_is_dual_modules
        assert "(sl(2)_1)^!" in triangle.line_category_description

    def test_celestial_ope_affine(self):
        """Celestial OPE for affine sl(N)_k has double pole."""
        A = make_boundary_sl_N(2, Fraction(1))
        ope = compute_celestial_ope(A)
        assert ope.max_ope_pole == 2
        assert 2 in ope.ope_coefficients

    def test_celestial_ope_heisenberg(self):
        """Celestial OPE for Heisenberg has double pole."""
        A = make_boundary_heisenberg(Fraction(1))
        ope = compute_celestial_ope(A)
        assert ope.max_ope_pole == 2

    def test_collinear_splitting_single_pole(self):
        """Collinear splitting from r(z) = Omega/z (single pole, AP19)."""
        A = make_boundary_sl_N(2, Fraction(1))
        split = collinear_splitting_from_shadow(A)
        assert split["collinear_pole_order"] == 1
        assert split["ap19_verified"]

    def test_collinear_splitting_heisenberg(self):
        """Heisenberg collinear splitting ~ k/z."""
        A = make_boundary_heisenberg(Fraction(5))
        split = collinear_splitting_from_shadow(A)
        assert split["collinear_pole_order"] == 1
        assert split["splitting_type"] == "scalar"

    def test_casimir_value_fundamental_sl2(self):
        """Quadratic Casimir in fundamental of sl(2) = 3/4."""
        A = make_boundary_sl_N(2, Fraction(1))
        split = collinear_splitting_from_shadow(A)
        assert split["casimir_value_fund"] == Fraction(3, 4)

    def test_casimir_value_fundamental_sl3(self):
        """Quadratic Casimir in fundamental of sl(3) = 4/3."""
        A = make_boundary_sl_N(3, Fraction(1))
        split = collinear_splitting_from_shadow(A)
        assert split["casimir_value_fund"] == Fraction(4, 3)


# ============================================================================
# Axis 3: Omega-background -> bar-cobar
# ============================================================================

class TestAxis3OmegaBarCobar:
    """Costello-Gaiotto: Omega-background produces VOA on boundary.

    In our framework: Omega = BV-BRST quantization producing A.
    The bar complex B(A) encodes full quantum content.
    """

    def test_omega_is_bv_brst(self):
        """Omega-background localization = BV-BRST quantization."""
        A = make_boundary_sl_N(2, Fraction(1))
        omega = omega_background_identification(A)
        assert omega.is_bv_brst

    def test_omega_is_not_nekrasov(self):
        """3d HT Omega != 4d Nekrasov Omega-background."""
        A = make_boundary_sl_N(2, Fraction(1))
        omega = omega_background_identification(A)
        assert omega.omega_is_not_nekrasov

    def test_genus_filtration_is_hbar(self):
        """The genus filtration parameter is hbar."""
        A = make_boundary_sl_N(2, Fraction(1))
        omega = omega_background_identification(A)
        assert "hbar" in omega.genus_filtration_parameter

    def test_bar_differential_uses_d_log(self):
        """Bar differential uses d log propagators on FM_k(C)."""
        A = make_boundary_sl_N(2, Fraction(1))
        omega = omega_background_identification(A)
        assert "d log" in omega.bar_differential_description


# ============================================================================
# Axis 4: Reproducible computations
# ============================================================================

class TestAxis4ReproducibleComputations:
    """Computations from the shadow obstruction tower that reproduce
    known twisted holography results."""

    # -- 4a: Collision residue for GL(N) CS --

    def test_collision_residue_sl2_casimir(self):
        """r(z) = Omega/z for sl(2) (Casimir r-matrix)."""
        A = make_boundary_sl_N(2, Fraction(1))
        r = compute_collision_residue(A)
        assert r.r_matrix_type == "Casimir/z"
        assert r.pole_order == 1

    def test_collision_residue_heisenberg_scalar(self):
        """r(z) = k/z for Heisenberg (scalar)."""
        A = make_boundary_heisenberg(Fraction(3))
        r = compute_collision_residue(A)
        assert r.r_matrix_type == "scalar/z"
        assert r.kappa_from_r == Fraction(3)

    def test_ap19_d_log_absorption_all_families(self):
        """AP19: residue pole = OPE pole - 1 for all standard families."""
        families = [
            make_boundary_sl_N(2, Fraction(1)),
            make_boundary_sl_N(3, Fraction(1)),
            make_boundary_sl_N(4, Fraction(2)),
            make_boundary_heisenberg(Fraction(1)),
            make_boundary_heisenberg(Fraction(5)),
        ]
        for A in families:
            r = compute_collision_residue(A)
            assert r.ap19_verified, f"AP19 failed for {A.name}"

    # -- 4b: CYBE from MC --

    def test_cybe_from_mc_sl2(self):
        """CYBE for sl(2) from genus-0 arity-3 MC equation."""
        A = make_boundary_sl_N(2, Fraction(1))
        result = verify_cybe_from_mc(A)
        assert result["satisfies_cybe"]
        assert result["is_strict_at_arity_3"]  # class L, depth 3

    def test_cybe_heisenberg_trivial(self):
        """CYBE for Heisenberg is trivially satisfied (abelian)."""
        A = make_boundary_heisenberg(Fraction(1))
        result = verify_cybe_from_mc(A)
        assert result["satisfies_cybe"]

    def test_cybe_mechanism_arnold(self):
        """CYBE mechanism is Arnold relations on FM_3(X)."""
        A = make_boundary_sl_N(3, Fraction(1))
        result = verify_cybe_from_mc(A)
        assert "Arnold" in result["mechanism"]

    # -- 4c: GZ commuting differentials --

    def test_gz_differentials_sl2(self):
        """GZ commuting differentials for sl(2)."""
        A = make_boundary_sl_N(2, Fraction(1))
        gz = gz_commuting_differentials(A)
        assert gz["d1_squared_zero"]
        assert gz["d2_squared_zero"]
        assert gz["anticommutator_zero"]

    def test_gz_from_mc_projection(self):
        """GZ differentials are arity-2 MC projection."""
        A = make_boundary_sl_N(2, Fraction(1))
        gz = gz_commuting_differentials(A)
        assert "arity=2" in gz["mc_source"]

    # -- 4d: Boundary modular class (Zeng's one-wheel) --

    def test_boundary_modular_class_sl2(self):
        """Boundary modular class for sl(2)_k."""
        A = make_boundary_sl_N(2, Fraction(1))
        mc = compute_boundary_modular_class(A)
        assert mc.lambda_1 == Fraction(1, 24)
        expected = A.kappa * Fraction(1, 24)
        assert mc.obstruction_value == expected

    def test_boundary_modular_class_heisenberg(self):
        """Boundary modular class for Heisenberg."""
        A = make_boundary_heisenberg(Fraction(2))
        mc = compute_boundary_modular_class(A)
        assert mc.obstruction_value == Fraction(2, 24)
        assert mc.is_zeng_compatible

    def test_modular_class_vanishes_uncurved(self):
        """Modular class vanishes iff kappa = 0 (uncurved)."""
        # kappa = 0 requires level to give kappa = 0
        # For sl(2): kappa = 3*(k+2)/4 = 0 => k = -2 (critical, disallowed)
        # For Heisenberg: kappa = k = 0
        A = make_boundary_heisenberg(Fraction(0))
        mc = compute_boundary_modular_class(A)
        assert mc.vanishes
        assert mc.obstruction_value == 0


# ============================================================================
# Axis 5: Extensions beyond twisted holography
# ============================================================================

class TestAxis5Extensions:
    """Our framework extends twisted holography in specific directions."""

    # -- 5a: Higher-genus data --

    def test_genus_1_sl2(self):
        """F_1(sl(2)_1) = kappa(sl(2)_1) / 24."""
        A = make_boundary_sl_N(2, Fraction(1))
        F1 = genus_g_partition_function(A, 1)
        assert F1 == A.kappa * Fraction(1, 24)

    def test_genus_2_sl2(self):
        """F_2(sl(2)_1) = kappa * 7/5760."""
        A = make_boundary_sl_N(2, Fraction(1))
        F2 = genus_g_partition_function(A, 2)
        assert F2 == A.kappa * Fraction(7, 5760)

    def test_genus_expansion_heisenberg(self):
        """Full genus expansion for Heisenberg at k=1."""
        A = make_boundary_heisenberg(Fraction(1))
        terms = genus_expansion_terms(A, max_g=4)
        assert terms[1] == Fraction(1, 24)
        assert terms[2] == Fraction(7, 5760)

    def test_genus_expansion_scales_with_kappa(self):
        """F_g scales linearly with kappa (uniform-weight lane)."""
        A1 = make_boundary_heisenberg(Fraction(1))
        A2 = make_boundary_heisenberg(Fraction(3))
        for g in range(1, 5):
            F1 = genus_g_partition_function(A1, g)
            F2 = genus_g_partition_function(A2, g)
            assert F2 == 3 * F1

    # -- 5b: Shadow depth classification --

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (Gaussian, depth 2)."""
        datum = construct_holographic_datum(make_boundary_heisenberg(Fraction(1)))
        assert datum.archetype_class == "G"
        assert datum.shadow_depth == 2

    def test_affine_class_L(self):
        """Affine sl(N) is class L (Lie/tree, depth 3)."""
        for N in [2, 3, 4]:
            datum = construct_holographic_datum(
                make_boundary_sl_N(N, Fraction(1)))
            assert datum.archetype_class == "L"
            assert datum.shadow_depth == 3

    # -- 5c: Complementarity --

    def test_complementarity_kappa_sum_zero_km(self):
        """kappa(A) + kappa(A!) = 0 for KM families (complementarity)."""
        for N in range(2, 7):
            A = make_boundary_sl_N(N, Fraction(1))
            dual = compute_koszul_dual(A)
            assert dual.kappa_sum == 0

    # -- 5d: Shadow connection flatness --

    def test_shadow_connection_flat(self):
        """Shadow connection nabla^hol is flat (from MC equation)."""
        A = make_boundary_sl_N(2, Fraction(1))
        datum = construct_holographic_datum(A)
        assert datum.shadow_connection_is_flat

    # -- 5e: Comparison table completeness --

    def test_comparison_table_has_all_axes(self):
        """Comparison table covers all identification axes."""
        table = twisted_holography_comparison_table()
        required_keys = [
            "boundary_chiral_algebra",
            "universal_defect_algebra",
            "bulk_algebra",
            "line_operators",
            "r_matrix",
            "cybe",
            "higher_operations",
            "modular_completion",
            "genus_tower",
            "shadow_depth",
            "complementarity",
        ]
        for key in required_keys:
            assert key in table, f"Missing key: {key}"

    def test_comparison_table_extensions_identified(self):
        """Our extensions are marked in the comparison table."""
        table = twisted_holography_comparison_table()
        for key in ["modular_completion", "genus_tower", "shadow_depth",
                     "complementarity", "entanglement", "shadow_arithmetic"]:
            assert "EXTENSION" in table[key]["identification"]


# ============================================================================
# Multi-path verification
# ============================================================================

class TestMultiPathVerification:
    """Every claim verified by 3+ independent paths."""

    def test_kappa_three_paths_sl2(self):
        """kappa(sl(2)_1) verified via 3 paths."""
        A = make_boundary_sl_N(2, Fraction(1))
        result = verify_kappa_three_paths(A)
        assert result["all_agree"]
        assert result["path1_formula"] == Fraction(3 * 3, 2 * 2)  # 9/4

    def test_kappa_three_paths_sl3(self):
        """kappa(sl(3)_1) verified via 3 paths."""
        A = make_boundary_sl_N(3, Fraction(1))
        result = verify_kappa_three_paths(A)
        assert result["all_agree"]
        # dim(sl_3)=8, h^v=3, k=1: kappa = 8*(1+3)/(2*3) = 16/3
        assert result["path1_formula"] == Fraction(16, 3)

    def test_kappa_three_paths_heisenberg(self):
        """kappa(H_k) verified via 3 paths."""
        for k in [1, 2, 5, 10]:
            A = make_boundary_heisenberg(Fraction(k))
            result = verify_kappa_three_paths(A)
            assert result["all_agree"]
            assert result["path1_formula"] == Fraction(k)

    def test_duality_constraint_sl2(self):
        """Duality constraint for sl(2)."""
        A = make_boundary_sl_N(2, Fraction(1))
        result = verify_duality_constraint(A)
        assert result["is_anti_symmetric"]
        assert result["kappa_sum"] == Fraction(0)

    def test_duality_constraint_all_types(self):
        """Duality constraint for all standard sl(N) families."""
        for N in range(2, 8):
            A = make_boundary_sl_N(N, Fraction(1))
            result = verify_duality_constraint(A)
            assert result["is_anti_symmetric"], f"Failed for sl({N})"

    def test_kappa_formula_independent_computation_sl_N(self):
        """Independent kappa computation for sl(N) at level k.

        kappa = dim(g) * (k + h^v) / (2 * h^v)
        For sl(N): dim = N^2 - 1, h^v = N.
        kappa = (N^2 - 1)(k + N) / (2N).
        """
        for N in range(2, 7):
            for k_val in [1, 2, 3]:
                k = Fraction(k_val)
                A = make_boundary_sl_N(N, k)
                expected = Fraction(N * N - 1) * (k + N) / (2 * N)
                assert A.kappa == expected, \
                    f"kappa mismatch for sl({N}) at k={k}"


# ============================================================================
# Derived center tests (AP34 compliance)
# ============================================================================

class TestDerivedCenter:
    """Verify derived center properties (AP34, AP-OC)."""

    def test_derived_center_is_not_bar(self):
        """The bulk is the derived center, NOT the bar complex."""
        A = make_boundary_sl_N(2, Fraction(1))
        center = compute_derived_center(A)
        assert center.is_not_bar_complex
        assert center.is_derived_center

    def test_derived_center_has_shifted_poisson(self):
        """Bulk has (-1)-shifted Poisson bracket (CDG20)."""
        A = make_boundary_sl_N(2, Fraction(1))
        center = compute_derived_center(A)
        assert center.is_commutative_with_poisson
        assert center.poisson_bracket_shift == -1

    def test_heisenberg_bulk_is_fock(self):
        """Heisenberg bulk = Fock space (jet algebra)."""
        A = make_boundary_heisenberg(Fraction(1))
        center = compute_derived_center(A)
        assert "Fock" in center.bulk_description


# ============================================================================
# Critical level exclusion
# ============================================================================

class TestCriticalLevel:
    """Sugawara is undefined at k = -h^v (AP: critical level)."""

    def test_sl2_critical_raises(self):
        """sl(2) at k = -2 (critical) raises ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            make_boundary_sl_N(2, Fraction(-2))

    def test_sl3_critical_raises(self):
        """sl(3) at k = -3 (critical) raises ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            make_boundary_sl_N(3, Fraction(-3))

    def test_non_critical_works(self):
        """Non-critical levels work fine."""
        A = make_boundary_sl_N(2, Fraction(-1))  # k = -1 != -2
        assert A.level == Fraction(-1)


# ============================================================================
# Anomaly cancellation (AP29)
# ============================================================================

class TestAnomalyCancellation:
    """Anomaly cancellation kappa_eff = kappa(matter) + kappa(ghost) = 0."""

    def test_heisenberg_anomaly_cancels(self):
        """Heisenberg: kappa(H_k) + kappa(ghost) = 0."""
        A = make_boundary_heisenberg(Fraction(1))
        result = anomaly_cancellation_check(A)
        assert result["cancels"]

    def test_sl2_anomaly(self):
        """sl(2) at k=1: kappa_eff = kappa - dim/2."""
        A = make_boundary_sl_N(2, Fraction(1))
        result = anomaly_cancellation_check(A)
        # kappa(sl(2)_1) = 9/4, ghost = -3/2
        # kappa_eff = 9/4 - 3/2 = 3/4
        assert result["kappa_eff"] == Fraction(3, 4)
        assert not result["cancels"]

    def test_ap29_note_present(self):
        """AP29: kappa_eff != delta_kappa is documented."""
        A = make_boundary_sl_N(2, Fraction(1))
        result = anomaly_cancellation_check(A)
        assert "kappa_eff" in result["ap29_note"]
        assert "delta_kappa" in result["ap29_note"]


# ============================================================================
# Full analysis integration tests
# ============================================================================

class TestFullAnalysis:
    """Integration tests for full_twisted_holography_analysis."""

    def test_full_sl2_analysis(self):
        """Complete analysis for SU(2) CS at k=1."""
        result = full_twisted_holography_analysis(2, Fraction(1))
        assert result["input"]["N"] == 2
        assert result["kappa_verification"]["all_agree"]
        assert result["cybe_verification"]["satisfies_cybe"]
        assert result["duality_constraint"]["is_anti_symmetric"]

    def test_full_sl3_analysis(self):
        """Complete analysis for SU(3) CS at k=2."""
        result = full_twisted_holography_analysis(3, Fraction(2))
        assert result["input"]["N"] == 3
        assert result["kappa_verification"]["all_agree"]

    def test_full_heisenberg_analysis(self):
        """Complete analysis for GL(1) CS at k=1."""
        result = heisenberg_twisted_holography_analysis(Fraction(1))
        assert result["kappa_verification"]["all_agree"]
        assert result["duality_constraint"]["is_anti_symmetric"]

    def test_full_analysis_has_all_components(self):
        """Full analysis has all expected components."""
        result = full_twisted_holography_analysis(2, Fraction(1))
        required = [
            "holographic_datum", "triangle", "modular_class",
            "celestial_ope", "collinear_splitting", "cybe_verification",
            "kappa_verification", "duality_constraint",
            "anomaly_cancellation", "gz_differentials",
            "omega_background", "genus_expansion",
        ]
        for key in required:
            assert key in result, f"Missing: {key}"

    def test_genus_expansion_in_full_analysis(self):
        """Genus expansion is present and correct."""
        result = full_twisted_holography_analysis(2, Fraction(1))
        ge = result["genus_expansion"]
        assert 1 in ge
        assert 2 in ge
        A = make_boundary_sl_N(2, Fraction(1))
        assert ge[1] == A.kappa * Fraction(1, 24)


# ============================================================================
# Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10: not just hardcoded)."""

    def test_kappa_additivity(self):
        """kappa is additive for direct sums (AP1, AP10).

        For H_k1 + H_k2: kappa = k1 + k2.
        Verify this is consistent with the formula.
        """
        k1, k2 = Fraction(3), Fraction(7)
        A1 = make_boundary_heisenberg(k1)
        A2 = make_boundary_heisenberg(k2)
        assert A1.kappa + A2.kappa == k1 + k2

    def test_kappa_scales_with_level(self):
        """For sl(N): kappa is affine-linear in k."""
        N = 3
        k1, k2 = Fraction(1), Fraction(2)
        A1 = make_boundary_sl_N(N, k1)
        A2 = make_boundary_sl_N(N, k2)
        # kappa = dim*(k+h^v)/(2h^v) is affine-linear in k
        diff = A2.kappa - A1.kappa
        expected_slope = Fraction(lie_dim("A", N - 1), 2 * lie_h_dual("A", N - 1))
        assert diff == expected_slope * (k2 - k1)

    def test_f1_kappa_ratio_universal(self):
        """F_1 / kappa = 1/24 for ALL families (lambda_1 universal)."""
        algebras = [
            make_boundary_heisenberg(Fraction(1)),
            make_boundary_heisenberg(Fraction(5)),
            make_boundary_sl_N(2, Fraction(1)),
            make_boundary_sl_N(3, Fraction(2)),
            make_boundary_sl_N(4, Fraction(1)),
        ]
        for A in algebras:
            F1 = genus_g_partition_function(A, 1)
            ratio = F1 / A.kappa
            assert ratio == Fraction(1, 24), f"Failed for {A.name}"

    def test_collision_residue_consistent_with_kappa(self):
        """kappa from collision residue = kappa from formula."""
        algebras = [
            make_boundary_heisenberg(Fraction(k)) for k in [1, 2, 3, 5]
        ] + [
            make_boundary_sl_N(N, Fraction(1)) for N in [2, 3, 4]
        ]
        for A in algebras:
            r = compute_collision_residue(A)
            assert r.kappa_from_r == A.kappa, \
                f"Residue kappa mismatch for {A.name}"
