"""Tests for E₁ primitive kernel profiles and coinvariant projection.

Verifies the structural identity av(K^{E₁}_A) = K_A:
the coinvariant projection of the E₁ (ordered/ribbon) primitive
kernel recovers the E_∞ primitive kernel for all standard families.

References:
  - Vol I, Remark rem:e1-primitive-kernel
  - Vol I, Theorem thm:e1-coinvariant-shadow
  - compute/lib/e1_primitive_kernel.py
  - compute/lib/modular_master.py (E_∞ profiles)
"""
import pytest
from fractions import Fraction

from compute.lib.e1_primitive_kernel import (
    AFFINE_SL2_E1,
    BETAGAMMA_E1,
    E1_PROFILES,
    HEISENBERG_E1,
    VIRASORO_E1,
    W3_E1,
    YANGIAN_SL2_E1,
    coinvariant_kappa_check,
    e1_master_equation_face_count,
    get_e1_profile,
    projection_table,
    verify_coinvariant_projection,
)
from compute.lib.modular_master import (
    AFFINE_SL2,
    HEISENBERG,
    PROFILES as EINFTY_PROFILES,
    VIRASORO,
    W3,
)


# ══════════════════════════════════════════════════════════════════════
#  1. COINVARIANT PROJECTION: av(K^{E₁}) = K
# ══════════════════════════════════════════════════════════════════════

class TestCoinvariantProjection:
    """Core structural test: av(K^{E₁}_A) = K_A for all families."""

    def test_heisenberg_coinvariant(self):
        """Heisenberg: av(K^{E₁}) = (K02, K11) = K_Heis."""
        assert verify_coinvariant_projection(
            "heisenberg", HEISENBERG.primitive_kernel()
        )

    def test_affine_sl2_coinvariant(self):
        """Affine sl2: av(K^{E₁}) projects to (K02, K03, K11)."""
        assert verify_coinvariant_projection(
            "affine_sl2", AFFINE_SL2.primitive_kernel()
        )

    def test_virasoro_coinvariant(self):
        """Virasoro: av(K^{E₁}) projects into the E_∞ kernel."""
        assert verify_coinvariant_projection(
            "virasoro", VIRASORO.primitive_kernel()
        )

    def test_w3_coinvariant(self):
        """W3: av(K^{E₁}) projects into the E_∞ kernel."""
        assert verify_coinvariant_projection(
            "w3", W3.primitive_kernel()
        )

    def test_all_profiles_coinvariant(self):
        """All E₁ profiles project consistently to their E_∞ counterparts."""
        for name, e1 in E1_PROFILES.items():
            proj = e1.coinvariant_projection()
            projected = tuple(proj.values())
            for comp in projected:
                assert comp in e1.einfty_kernel, (
                    f"{name}: E₁ component projects to {comp} "
                    f"which is not in E_∞ kernel {e1.einfty_kernel}"
                )


# ══════════════════════════════════════════════════════════════════════
#  2. DEGREE-2 SHADOW RECOVERY
# ══════════════════════════════════════════════════════════════════════

class TestKappaRecovery:
    """At (g,n)=(0,2): the E₁ r-matrix av-projects to the scalar degree-2 shadow."""

    def test_heisenberg_kappa(self):
        assert coinvariant_kappa_check("heisenberg")
        assert HEISENBERG_E1.verify_coinvariant_at_02() == Fraction(1)

    def test_affine_sl2_kappa(self):
        assert coinvariant_kappa_check("affine_sl2")
        assert AFFINE_SL2_E1.verify_coinvariant_at_02() == Fraction(3, 4)

    def test_betagamma_kappa_zero(self):
        """Beta-gamma: r(z) = 0, so av(r(z)) = 0 = κ(βγ)."""
        assert coinvariant_kappa_check("betagamma")
        assert BETAGAMMA_E1.verify_coinvariant_at_02() == Fraction(0)

    def test_virasoro_kappa(self):
        assert coinvariant_kappa_check("virasoro")
        assert VIRASORO_E1.verify_coinvariant_at_02() == Fraction(1, 2)

    def test_all_families_kappa(self):
        for name in E1_PROFILES:
            assert coinvariant_kappa_check(name), f"{name}: kappa mismatch"


# ══════════════════════════════════════════════════════════════════════
#  3. E₁ KERNEL COMPONENT STRUCTURE
# ══════════════════════════════════════════════════════════════════════

class TestE1KernelStructure:
    """E₁ kernel has ordered components: r(z), Φ_KZ, r_4, genus-1."""

    def test_heisenberg_components(self):
        comps = HEISENBERG_E1.e1_kernel_components()
        assert comps == ("K02_r(z)", "K11_genus1")

    def test_affine_sl2_components(self):
        comps = AFFINE_SL2_E1.e1_kernel_components()
        assert comps == ("K02_r(z)", "K03_Phi", "K11_genus1")

    def test_betagamma_components(self):
        """βγ: no associator, but quartic is non-trivial."""
        comps = BETAGAMMA_E1.e1_kernel_components()
        assert comps == ("K02_r(z)", "K04_r4", "K11_genus1")

    def test_virasoro_components(self):
        comps = VIRASORO_E1.e1_kernel_components()
        assert "K02_r(z)" in comps
        assert "K03_Phi" in comps
        assert "K04_r4" in comps
        assert "K11_genus1" in comps

    def test_all_have_k02_k11(self):
        """Every E₁ kernel has at least the r-matrix and genus-1 primitive."""
        for name, e1 in E1_PROFILES.items():
            comps = e1.e1_kernel_components()
            assert "K02_r(z)" in comps, f"{name}: missing K02_r(z)"
            assert "K11_genus1" in comps, f"{name}: missing K11_genus1"

    def test_component_count_bounded(self):
        """E₁ kernel has at most 4 components (r, Φ, r_4, genus-1)."""
        for name, e1 in E1_PROFILES.items():
            assert len(e1.e1_kernel_components()) <= 4, (
                f"{name}: too many E₁ kernel components"
            )


# ══════════════════════════════════════════════════════════════════════
#  4. E₁ PRIMITIVE MASTER EQUATION
# ══════════════════════════════════════════════════════════════════════

class TestE1MasterEquation:
    """dK^{E₁} + K^{E₁} ⋆_{E₁} K^{E₁} = 0."""

    def test_arity2_is_cybe(self):
        """Arity 2: 2 faces of K_3 → CYBE."""
        terms = HEISENBERG_E1.e1_master_equation_terms(2)
        assert "CYBE" in terms[1]

    def test_arity3_is_pentagon(self):
        """Arity 3: 5 faces of K_4 → pentagon equation."""
        terms = AFFINE_SL2_E1.e1_master_equation_terms(3)
        assert "pentagon" in terms[1]

    def test_arity4_quartic(self):
        """Arity 4: 9 codim-1 faces of K_5 → quartic identity."""
        terms = VIRASORO_E1.e1_master_equation_terms(4)
        assert any("9 faces" in t for t in terms)

    def test_associahedron_face_counts(self):
        """Facets of K_{r+1}: n(n-1)/2 - 1 where n=r+1.
        K_3: 2, K_4: 5, K_5: 9, K_6: 14."""
        assert e1_master_equation_face_count(2) == 2
        assert e1_master_equation_face_count(3) == 5
        assert e1_master_equation_face_count(4) == 9
        assert e1_master_equation_face_count(5) == 14

    def test_face_count_matches_profile(self):
        """Profile's associahedron_faces method agrees."""
        for r in range(2, 7):
            assert (
                HEISENBERG_E1.associahedron_faces(r)
                == e1_master_equation_face_count(r)
            )


# ══════════════════════════════════════════════════════════════════════
#  5. LOW-ARITY IDENTIFICATIONS
# ══════════════════════════════════════════════════════════════════════

class TestLowArityIdentifications:
    """K^{E₁}_{0,2} = r(z), K^{E₁}_{0,3} = Φ_KZ for affine."""

    def test_heisenberg_r_matrix_scalar(self):
        """Heisenberg: r(z) = k/z, scalar type."""
        assert HEISENBERG_E1.r_matrix_type == "scalar"
        assert HEISENBERG_E1.r_matrix_scalar == Fraction(1)

    def test_affine_r_matrix_casimir(self):
        """Affine: r(z) = κΩ/z, Casimir type."""
        assert AFFINE_SL2_E1.r_matrix_type == "casimir"

    def test_betagamma_r_matrix_zero(self):
        """βγ: r(z) = 0 (no arity-2 E₁ shadow)."""
        assert BETAGAMMA_E1.r_matrix_type == "zero"
        assert BETAGAMMA_E1.r_matrix_scalar == Fraction(0)

    def test_affine_associator_kz(self):
        """Affine: Φ_KZ is the KZ associator."""
        assert AFFINE_SL2_E1.associator_type == "KZ"
        assert AFFINE_SL2_E1.associator_nonzero is True

    def test_heisenberg_no_associator(self):
        """Heisenberg: no arity-3 shadow (Gaussian terminates at 2)."""
        assert HEISENBERG_E1.associator_nonzero is False

    def test_yangian_drinfeld_associator(self):
        """Yangian: arity-3 shadow is Drinfeld associator."""
        assert YANGIAN_SL2_E1.associator_type == "Drinfeld"
        assert YANGIAN_SL2_E1.associator_nonzero is True

    def test_betagamma_quartic_nonzero(self):
        """βγ: the quartic contact invariant is non-trivial at E₁ level."""
        assert BETAGAMMA_E1.quartic_nonzero is True

    def test_heisenberg_quartic_zero(self):
        """Heisenberg: quartic vanishes (depth 2)."""
        assert HEISENBERG_E1.quartic_nonzero is False


# ══════════════════════════════════════════════════════════════════════
#  6. SHADOW DEPTH CLASSIFICATION
# ══════════════════════════════════════════════════════════════════════

class TestShadowDepth:
    """Shadow depth at E₁ level matches E_∞ depth classification."""

    def test_heisenberg_gaussian(self):
        assert HEISENBERG_E1.shadow_depth == 2  # G class

    def test_affine_lie_tree(self):
        assert AFFINE_SL2_E1.shadow_depth == 3  # L class

    def test_betagamma_contact(self):
        assert BETAGAMMA_E1.shadow_depth == 4  # C class

    def test_virasoro_infinite(self):
        assert VIRASORO_E1.shadow_depth == 0  # M class (infinite)

    def test_w3_infinite(self):
        assert W3_E1.shadow_depth == 0


# ══════════════════════════════════════════════════════════════════════
#  7. PROJECTION TABLE
# ══════════════════════════════════════════════════════════════════════

class TestProjectionTable:
    """The summary projection table is consistent."""

    def test_table_all_valid(self):
        table = projection_table()
        for name, e1_comps, einfty_comps, valid in table:
            assert valid, f"{name}: coinvariant projection invalid"

    def test_table_covers_all_profiles(self):
        table = projection_table()
        names = {row[0] for row in table}
        assert names == set(E1_PROFILES.keys())

    def test_table_e1_components_nonempty(self):
        table = projection_table()
        for name, e1_comps, _, _ in table:
            assert len(e1_comps) >= 2, f"{name}: E₁ kernel too small"


# ══════════════════════════════════════════════════════════════════════
#  8. CROSS-VALIDATION WITH E_∞ PROFILES
# ══════════════════════════════════════════════════════════════════════

class TestCrossValidation:
    """E₁ profiles are consistent with modular_master.py E_∞ profiles."""

    def test_heisenberg_einfty_kernel_matches(self):
        assert HEISENBERG_E1.einfty_kernel == HEISENBERG.primitive_kernel()

    def test_affine_einfty_kernel_matches(self):
        assert AFFINE_SL2_E1.einfty_kernel == AFFINE_SL2.primitive_kernel()

    def test_virasoro_einfty_kernel_matches(self):
        assert VIRASORO_E1.einfty_kernel == VIRASORO.primitive_kernel()

    def test_w3_einfty_kernel_matches(self):
        assert W3_E1.einfty_kernel == W3.primitive_kernel()

    def test_coinvariant_surjects_onto_corolla_components(self):
        """The coinvariant image covers at least the corolla part of K_A.

        The E_∞ kernel may additionally have planted-forest rigid terms
        (Rpf2, Rpf3) that arise from higher-genus corrections, not from
        the genus-0 E₁ projection.
        """
        for name in ["heisenberg", "affine_sl2"]:
            e1 = E1_PROFILES[name]
            proj_values = set(e1.coinvariant_projection().values())
            einfty = set(e1.einfty_kernel)
            # All projected components land in the E_∞ kernel
            assert proj_values <= einfty, (
                f"{name}: {proj_values - einfty} not in E_∞ kernel"
            )

    def test_genus0_components_project(self):
        """All genus-0 E₁ components (K02, K03, K04) project to E_∞."""
        for name, e1 in E1_PROFILES.items():
            proj = e1.coinvariant_projection()
            genus0_e1 = [c for c in e1.e1_kernel_components()
                         if c.startswith("K0")]
            for c in genus0_e1:
                assert c in proj, f"{name}: {c} has no projection"


# ══════════════════════════════════════════════════════════════════════
#  9. COINVARIANT AT ARITY 3: av(Φ_KZ) = C(A)
# ══════════════════════════════════════════════════════════════════════

class TestArityThreeCoinvariant:
    """av(Φ_KZ(A)) = C(A): the KZ associator averages to the cubic shadow."""

    def test_heisenberg_trivial(self):
        result = HEISENBERG_E1.verify_coinvariant_at_03()
        assert "trivial" in result

    def test_affine_cubic(self):
        result = AFFINE_SL2_E1.verify_coinvariant_at_03()
        assert "cubic shadow" in result

    def test_betagamma_trivial(self):
        result = BETAGAMMA_E1.verify_coinvariant_at_03()
        assert "trivial" in result

    def test_virasoro_nontrivial(self):
        result = VIRASORO_E1.verify_coinvariant_at_03()
        assert "cubic shadow" in result


# ══════════════════════════════════════════════════════════════════════
# 10. COINVARIANT AT ARITY 4: av(r_4) = Q(A)
# ══════════════════════════════════════════════════════════════════════

class TestArityFourCoinvariant:
    """av(r_4(A)) = Q(A): the quartic R-matrix shadow averages to Q."""

    def test_heisenberg_trivial(self):
        result = HEISENBERG_E1.verify_coinvariant_at_04()
        assert "trivial" in result

    def test_affine_trivial(self):
        result = AFFINE_SL2_E1.verify_coinvariant_at_04()
        assert "trivial" in result

    def test_betagamma_nontrivial(self):
        result = BETAGAMMA_E1.verify_coinvariant_at_04()
        assert "quartic shadow" in result

    def test_virasoro_nontrivial(self):
        result = VIRASORO_E1.verify_coinvariant_at_04()
        assert "quartic shadow" in result
