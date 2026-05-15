r"""Tests for the deep twisted holography engine.

Organized by the five identification axes plus multi-path verification.

60+ tests covering:
  Axis 1: Zeng boundary/defect comparison via Koszul-Verdier lanes
  Axis 2: Garner-Paquette scattering with charged sources
  Axis 3: Omega-background -> bar-cobar identification
  Axis 4: Reproducible computations from shadow obstruction tower
  Axis 5: Extensions beyond twisted holography
  Multi-path: 3+ independent verification paths per claim
"""

import pytest
from dataclasses import fields, is_dataclass
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
    # Finite analysis
    full_twisted_holography_analysis, heisenberg_twisted_holography_analysis,
)


def _available_component_names(datum):
    if isinstance(datum, dict):
        return sorted(datum)
    if is_dataclass(datum):
        return sorted(field.name for field in fields(datum))
    return sorted(name for name in dir(datum) if not name.startswith("_"))


def _get_component(datum, *names):
    if isinstance(datum, dict):
        for name in names:
            if name in datum:
                return datum[name]
    for name in names:
        if hasattr(datum, name):
            return getattr(datum, name)
    raise AssertionError(
        f"Missing component {names}; available={_available_component_names(datum)}"
    )


def _get_component_or_package_label(datum, label, *names):
    try:
        return _get_component(datum, *names)
    except AssertionError:
        entries = getattr(datum, "package_entries", ())
        if label in entries:
            return label
        raise


def _holographic_components(datum):
    return {
        "A": _get_component(datum, "A", "boundary"),
        "A_i": _get_component(
            datum, "A_i", "bar_dual", "bar_dual_coalgebra",
            "bar_dual_cohomology",
        ),
        "A_dual": _get_component(
            datum, "A_dual", "koszul_dual", "verdier_koszul_branch",
        ),
        "C": _get_component(datum, "C", "derived_center", "bulk"),
        "r": _get_component(datum, "r", "collision_residue", "r_matrix"),
        "Theta": _get_component_or_package_label(
            datum, "Theta_A", "Theta", "theta", "theta_A", "mc_element",
        ),
        "nabla": _get_component_or_package_label(
            datum, "nabla^hol", "nabla", "nabla_hol",
            "shadow_connection", "holomorphic_connection",
        ),
    }


def _component_text(component):
    parts = [type(component).__name__, str(component)]
    doc = getattr(type(component), "__doc__", None)
    if doc:
        parts.append(doc)
    if isinstance(component, dict):
        parts.extend(str(value) for value in component.values())
    elif is_dataclass(component):
        parts.extend(str(getattr(component, field.name))
                     for field in fields(component))
    for attr in (
        "name", "description", "bulk_description", "bar_cobar_scope", "kind",
    ):
        if hasattr(component, attr):
            parts.append(str(getattr(component, attr)))
    return "\n".join(parts)


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
        """lambda_2 = 7/5760; AP38 excludes 1/1152."""
        assert _lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3 = 31/967680."""
        assert _lambda_fp(3) == Fraction(31, 967680)


# ============================================================================
# Axis 1: Zeng boundary/defect comparison via Koszul-Verdier lanes
# ============================================================================

class TestAxis1ZengBoundaryDefect:
    """Zeng [2302.06693]: boundary chiral algebra = universal defect
    chiral algebra through the Koszul/Verdier comparison.

    In our framework:
      boundary = input A;
      A^i = H^*(B(A)) is the bar-dual cohomology;
      A^! is the Verdier/Koszul branch under the finite-type or completed
      hypotheses;
      Omega(B(A)) = A is inversion, not construction of A^!.
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

    def test_universal_defect_is_verdier_koszul_branch(self):
        """The universal defect algebra is the A^! Verdier/Koszul branch."""
        A = make_boundary_sl_N(2, Fraction(1))
        dual = compute_koszul_dual(A)
        # The A^! branch has opposite kappa (FF involution).
        assert dual.kappa_dual == -A.kappa
        assert dual.is_anti_symmetric
        assert dual.bar_dual_source == "A^i(sl(2)_1) = H^*(B(sl(2)_1))"
        assert "finite-type or completed Verdier" in dual.branch_scope
        assert not dual.full_dual_constructed

    def test_heisenberg_defect_is_sym_ch_dual(self):
        """AP33: H_k^! = Sym^ch(V*) with the H_{-k} kappa value.

        They have the same kappa but are different chiral algebras.
        """
        A = make_boundary_heisenberg(Fraction(3))
        dual = compute_koszul_dual(A)
        # Same kappa as H_{-k}.
        assert dual.kappa_dual == -Fraction(3)
        # The object name records the Verdier/Koszul branch.
        assert "^!" in dual.name

    def test_boundary_bulk_derived_center_distinction_ap34(self):
        """AP34: bar-cobar inversion != open-to-closed.

        The bulk is the derived center, distinct from the bar complex.
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

    Line defects are modules in C_line = A^!-mod.
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
        """Collinear splitting from r^coll(z) = k Omega_tr/z."""
        A = make_boundary_sl_N(2, Fraction(1))
        split = collinear_splitting_from_shadow(A)
        assert split["collinear_pole_order"] == 1
        assert split["ap19_verified"]
        assert split["kernel_formula"] == "k*Omega_tr/z"
        assert split["leading_coefficient"] == "1*Omega_tr(sl_2)"

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
    The bar complex B(A) records the OPE data in the bar lane.
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

    def test_omega_background_does_not_assert_full_bv_bar(self):
        """Boundary BV-BRST production is not genus>=1 BV/BRST=bar."""
        A = make_boundary_sl_N(2, Fraction(1))
        omega = omega_background_identification(A)
        assert not omega.full_bv_brst_bar_identification
        assert "coderived" in omega.bv_brst_bar_scope
        assert "BV functor bridge" in omega.bv_brst_bar_scope
        assert "no chain-level class-M" in " ".join(omega.factorization_hypotheses)


# ============================================================================
# Axis 4: Reproducible computations
# ============================================================================

class TestAxis4ReproducibleComputations:
    """Computations from the shadow obstruction tower that reproduce
    known twisted holography results."""

    # -- 4a: Collision residue for GL(N) CS --

    def test_collision_residue_sl2_casimir(self):
        """r^coll(z) = k Omega_tr/z for sl(2) in trace form."""
        A = make_boundary_sl_N(2, Fraction(1))
        r = compute_collision_residue(A)
        assert r.r_matrix_type == "trace-form k*Omega_tr/z"
        assert r.kernel_formula == "k*Omega_tr/z"
        assert r.raw_level_coefficient == Fraction(1)
        assert r.kz_kernel_formula == "Omega_KZ/((k+h^vee)z)"
        assert r.kz_denominator == Fraction(3)
        assert r.pole_order == 1

    def test_affine_trace_form_k_zero_does_not_equal_kappa(self):
        """At k=0, trace-form r^coll vanishes but kappa does not."""
        A = make_boundary_sl_N(2, Fraction(0))
        r = compute_collision_residue(A)
        assert r.raw_kernel_vanishes_at_level_zero
        assert r.raw_level_coefficient == 0
        assert r.kappa_from_r == Fraction(3, 2)
        assert r.raw_level_coefficient != r.kappa_from_r
        assert not r.raw_kernel_equals_kappa_projection
        assert r.kz_denominator == Fraction(2)

    def test_collision_residue_heisenberg_scalar(self):
        """r(z) = k/z for Heisenberg (scalar)."""
        A = make_boundary_heisenberg(Fraction(3))
        r = compute_collision_residue(A)
        assert r.r_matrix_type == "scalar/z"
        assert r.kappa_from_r == Fraction(3)
        assert r.raw_kernel_equals_kappa_projection

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
        assert not result["full_mc_reconstructed"]
        assert "genus-0" in result["projection_scope"]

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
        assert not gz["full_mc_reconstructed"]

    # -- 4d: Boundary modular class (Zeng's one-wheel) --

    def test_boundary_modular_class_sl2(self):
        """Boundary modular class for sl(2)_k."""
        A = make_boundary_sl_N(2, Fraction(1))
        mc = compute_boundary_modular_class(A)
        assert mc.lambda_1 == Fraction(1, 24)
        expected = A.kappa * Fraction(1, 24)
        assert mc.obstruction_value == expected
        assert mc.genus_1_lift_exists
        assert "genus-1 scalar" in mc.lift_scope
        assert not mc.full_genus_lift_asserted

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
        """Finite scalar genus expansion for Heisenberg at k=1."""
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
        """Extensions are scoped instead of promoted to package theorems."""
        table = twisted_holography_comparison_table()
        for key in ["modular_completion", "genus_tower", "shadow_depth",
                     "complementarity", "entanglement", "shadow_arithmetic"]:
            assert table[key]["status"]
            assert table[key]["scope"]

        assert table["modular_completion"]["status"] == (
            "conditional outside finite projections"
        )
        assert table["genus_tower"]["status"] == "uniform-weight scalar lane"
        assert table["entanglement"]["status"] == "out of compute scope"


# ============================================================================
# Holographic package firewall
# ============================================================================

class TestHolographicPackageFirewall:
    """Enforce A, A^i, A^!, C, r(z), Theta_A, nabla^hol separation."""

    def test_holographic_datum_has_seven_firewall_components(self):
        """H(A) exposes exactly the seven mathematical package entries."""
        datum = construct_holographic_datum(make_boundary_sl_N(2, Fraction(1)))
        components = _holographic_components(datum)
        expected_entries = (
            "A", "A^i", "A^!", "C", "r(z)", "Theta_A", "nabla^hol",
        )

        assert tuple(components) == (
            "A", "A_i", "A_dual", "C", "r", "Theta", "nabla",
        )
        assert getattr(datum, "package_entries") == expected_entries
        assert len(datum.package_entries) == 7
        assert components["Theta"] == "Theta_A"
        assert components["nabla"] == "nabla^hol"

        datum_doc = type(datum).__doc__ or ""
        assert "(A, A^i, A^!, C, r(z), Theta_A, nabla^hol)" in datum_doc
        assert "sextuple" not in datum_doc.lower()
        assert not datum.full_mc_data_reconstructed
        assert not datum.full_holographic_package_theorem
        assert "finite genus-0" in datum.connection_flatness_scope

    def test_bar_dual_cohomology_is_not_A_dual_branch(self):
        """A^i is bar-dual cohomology; A^! is the Verdier/Koszul branch."""
        datum = construct_holographic_datum(make_boundary_sl_N(2, Fraction(1)))
        components = _holographic_components(datum)

        assert components["A_i"] != components["A_dual"]
        assert components["A_i"] != components["A"]

        bar_text = _component_text(components["A_i"]).lower()
        assert "a^i" in bar_text
        assert (
            "cohomolog" in bar_text
            or "h^*(b(a))" in bar_text
            or "h^*(b(" in bar_text
            or "h*(b(" in bar_text
        )

        firewall = datum.object_firewall
        assert "bar-dual" in firewall["A^i"]
        assert "H^*(B(A))" in firewall["A^i"]

        dual_text = _component_text(components["A_dual"]).lower()
        assert "verdier" in dual_text or "koszul branch" in dual_text
        assert "omega(b(a)) constructs" not in dual_text

    def test_C_component_is_derived_center_bulk_not_bar_or_dual(self):
        """C is the derived centre/bulk channel, not A, A^i, or A^!."""
        datum = construct_holographic_datum(make_boundary_heisenberg(Fraction(1)))
        components = _holographic_components(datum)

        assert components["C"] != components["A"]
        assert components["C"] != components["A_i"]
        assert components["C"] != components["A_dual"]

        center_text = _component_text(components["C"]).lower()
        assert "derived" in center_text
        assert "center" in center_text or "centre" in center_text
        assert "bulk" in center_text
        if hasattr(components["C"], "is_derived_center"):
            assert components["C"].is_derived_center

    def test_comparison_table_removes_linear_dual_shortcut(self):
        """The table states the A^i -> A^! branch, not a six-slot shortcut."""
        table = twisted_holography_comparison_table()
        serialized = repr(table)

        forbidden_shortcuts = [
            "A^!" + " = " + "(H*(B(A)))" + "^v",
            "A^!" + " = " + "(H^*(B(A)))" + "^v",
            "(H*(B(A)))" + "^v",
            "(H^*(B(A)))" + "^v",
        ]
        for phrase in forbidden_shortcuts:
            assert phrase not in serialized

        defect = table["universal_defect_algebra"]["our_framework"]
        assert "A^i" in defect
        assert "Verdier" in defect or "Koszul branch" in defect
        assert "Omega(B(A))" not in defect

        bulk = table["bulk_algebra"]["our_framework"]
        assert "Derived center" in bulk or "derived centre" in bulk

    def test_omega_background_records_inversion_not_duality(self):
        """Omega(B(A)) = A is bar-cobar inversion, not construction of A^!."""
        omega = omega_background_identification(make_boundary_sl_N(2, Fraction(1)))
        omega_text = _component_text(omega)

        assert "Omega(B(A))" in omega_text
        assert "recovers A" in omega_text or "inversion" in omega_text
        assert "Omega(B(A)) constructs A^!" not in omega_text

    def test_holographic_datum_records_bv_and_factorization_hypotheses(self):
        """The finite datum names BV/BRST and factorization hypotheses."""
        datum = construct_holographic_datum(make_boundary_sl_N(2, Fraction(1)))
        bv_text = " ".join(datum.bv_brst_hypotheses)
        fact_text = " ".join(datum.factorization_hypotheses)

        assert "genus>=1 BV/BRST=bar requires" in bv_text
        assert "class-M identification is not asserted" in bv_text
        assert "Koszul locus" in fact_text
        assert "descent/excision not computed" in fact_text

    def test_comparison_table_has_no_full_package_overclaim(self):
        """The table must not promote finite projections to full theorems."""
        table = twisted_holography_comparison_table()
        serialized = repr(table)

        forbidden = [
            "SAME " + "(proved)",
            "OUR " + "EXTENSION",
            "all genera, proved",
            "full holographic package theorem",
        ]
        for phrase in forbidden:
            assert phrase not in serialized

        assert table["r_matrix"]["status"] == "computed projection"
        assert "not the full open/closed MC package" in table["cybe"]["scope"]


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
        assert result["raw_trace_form_level"] == Fraction(1)
        assert result["raw_trace_form_level"] != result["path1_formula"]
        assert result["kz_kernel_formula"] == "Omega_KZ/((k+h^vee)z)"

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
            assert result["raw_trace_form_level"] == Fraction(k)
            assert result["kz_kernel_formula"] is None

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

    def test_derived_center_is_bulk(self):
        """The bulk is the derived center, distinct from the bar complex."""
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
# Finite analysis integration tests
# ============================================================================

class TestFullAnalysis:
    """Integration tests for full_twisted_holography_analysis."""

    def test_full_sl2_analysis(self):
        """Finite analysis for SU(2) CS at k=1."""
        result = full_twisted_holography_analysis(2, Fraction(1))
        assert result["input"]["N"] == 2
        assert result["kappa_verification"]["all_agree"]
        assert result["cybe_verification"]["satisfies_cybe"]
        assert result["duality_constraint"]["is_anti_symmetric"]
        assert result["scope"]["finite_diagnostics_only"]
        assert not result["scope"]["full_mc_reconstructed"]
        assert not result["scope"]["full_holographic_package_theorem"]

    def test_full_sl3_analysis(self):
        """Finite analysis for SU(3) CS at k=2."""
        result = full_twisted_holography_analysis(3, Fraction(2))
        assert result["input"]["N"] == 3
        assert result["kappa_verification"]["all_agree"]

    def test_full_heisenberg_analysis(self):
        """Finite analysis for GL(1) CS at k=1."""
        result = heisenberg_twisted_holography_analysis(Fraction(1))
        assert result["kappa_verification"]["all_agree"]
        assert result["duality_constraint"]["is_anti_symmetric"]
        assert result["scope"]["finite_diagnostics_only"]

    def test_full_analysis_has_all_components(self):
        """Finite analysis has all expected components."""
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
    """Cross-family consistency checks proving AP10 structural dependence."""

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
        expected_derivative = Fraction(lie_dim("A", N - 1), 2 * lie_h_dual("A", N - 1))
        assert diff == expected_derivative * (k2 - k1)

    def test_f1_kappa_ratio_universal(self):
        """F_1 / kappa = 1/24 for implemented families."""
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
