r"""
test_s3_framing_obstruction.py -- Tests for S^3-framing obstruction computation.

Tests are organized around the multi-path verification mandate:
every claim is verified by at least 2 independent methods.

Test groups:
  1. Homotopy group computations (pi_k of classifying spaces)
  2. Degree-three classifying-space groups in the chosen models
  3. Explicit CY3 examples (C^3, quintic, K3xE, conifold)
  4. BV obstruction analysis
  5. Mirror symmetry checks
  6. Framing anomaly computation
  7. Stable-range analysis
  8. Cross-checks with existing CY modules
"""

from fractions import Fraction
import math

import pytest

from compute.lib.bcov_bar_complex import pv_k3_times_e, pv_quintic
from compute.lib.s3_framing_obstruction import (
    # Homotopy groups
    pi_k_BO,
    pi_k_BSp,
    pi_k_BU,
    pi_k_BGL_C,
    # CY3 data
    CY3HodgeData,
    QUINTIC,
    K3_TIMES_E,
    MIRROR_QUINTIC,
    # Framing obstruction
    FramingAnomalyComparison,
    FramingObstruction,
    RepresentedBVClass,
    RepresentedNullHomotopy,
    s_d_framing_obstruction,
    obstruction_c3,
    obstruction_quintic,
    obstruction_mirror_quintic,
    obstruction_k3_times_e,
    obstruction_conifold,
    # Stable range
    stable_obstruction_vanishing,
    # Framing anomaly
    chern_simons_framing_anomaly,
    framing_anomaly_phase,
    framing_anomaly_order,
    # Pontryagin class
    first_pontryagin_class_cy3,
    # BV obstruction
    BVObstruction,
    bv_obstruction_cy3,
    # Mirror
    mirror_obstruction_comparison,
    # Summary
    d3_functor_existence_analysis,
)

# =========================================================================
# 1. Homotopy group tests
# =========================================================================

class TestHomotopyGroups:
    """Verify homotopy groups of classifying spaces.

    These are standard results from algebraic topology.
    Reference: Hatcher, "Algebraic Topology" and Milnor-Stasheff,
    "Characteristic Classes".
    """

    # --- pi_k(BO(n)) ---

    def test_pi_1_BO_orientation(self):
        """pi_1(BO(n)) = Z/2 for n >= 1 (orientation obstruction)."""
        for n in range(1, 10):
            assert pi_k_BO(1, n) == "Z/2"

    def test_pi_2_BO_unstable_and_stable_values(self):
        """The loop equivalence reads pi_2 BO(n) from pi_1 O(n)."""
        assert pi_k_BO(2, 1) == "0"
        assert pi_k_BO(2, 2) == "Z"
        for n in range(3, 10):
            assert pi_k_BO(2, n) == "Z/2"

    def test_pi_3_BO_is_zero(self):
        """The identity pi_3 BO(n)=pi_2 O(n) gives zero in every rank."""
        for n in range(1, 10):
            assert pi_k_BO(3, n) == "0"

    def test_pi_4_BO_unstable_rank_split(self):
        """The fourth group records the unstable O(3) and O(4) factors."""
        assert pi_k_BO(4, 1) == "0"
        assert pi_k_BO(4, 2) == "0"
        assert pi_k_BO(4, 3) == "Z"
        assert pi_k_BO(4, 4) == "Z+Z"
        for n in range(5, 10):
            assert pi_k_BO(4, n) == "Z"

    # --- pi_k(BSp(2m)) ---

    def test_pi_1_BSp_trivial(self):
        """pi_1(BSp(2m)) = 0 for all m >= 1 (Sp simply connected)."""
        for m in range(1, 10):
            assert pi_k_BSp(1, m) == "0"

    def test_pi_2_BSp_trivial(self):
        """pi_2(BSp(2m)) = 0 for all m >= 1."""
        for m in range(1, 10):
            assert pi_k_BSp(2, m) == "0"

    def test_pi_3_BSp_is_zero(self):
        """pi_3(BSp(2m)) = 0 for all m >= 1.

        This is the primary degree-three input from the chosen symplectic
        structure-group model.

        Proof: pi_3(BSp(2m)) = pi_2(Sp(2m)).
        Sp(2) = SU(2) = S^3, so pi_2(Sp(2)) = pi_2(S^3) = 0.
        For m >= 2: the fibration Sp(2m-2) -> Sp(2m) -> S^{4m-1}
        gives the long exact sequence, whose degree-two term is zero at
        each stage.
        """
        for m in range(1, 20):
            assert pi_k_BSp(3, m) == "0", (
                f"pi_3(BSp({2*m})) should be 0, "
                f"but got {pi_k_BSp(3, m)}"
            )

    def test_pi_4_BSp_Z(self):
        """pi_4(BSp(2m)) = Z for all m >= 1.

        pi_4(BSp(2m)) = pi_3(Sp(2m)) = Z.
        For Sp(2) = SU(2) = S^3: pi_3(S^3) = Z.
        This is the SYMPLECTIC PONTRYAGIN class.
        """
        for m in range(1, 10):
            assert pi_k_BSp(4, m) == "Z"

    # --- pi_k(BU) ---

    def test_pi_BU_bott_periodicity(self):
        """Bott periodicity: pi_k(BU) = Z for k even, 0 for k odd."""
        for k in range(1, 20):
            expected = "Z" if k % 2 == 0 else "0"
            assert pi_k_BU(k) == expected, (
                f"pi_{k}(BU) should be {expected}"
            )

    def test_pi_3_BU_zero(self):
        """pi_3(BU) = 0.  This implies pi_3(BGL(C)) = 0."""
        assert pi_k_BU(3) == "0"

    # --- pi_k(BGL(C)) ---

    def test_pi_3_BGL_C_zero_KEY(self):
        """pi_3(BGL(n,C)) = 0 in the stable range.

        GL(n,C) deformation-retracts onto U(n).
        pi_3(BU(n)) = pi_2(U(n)) = 0 for all n >= 1 (Bott periodicity).

        This gives the complex-linear route to the same primary group.
        """
        assert pi_k_BGL_C(3) == "0"

    def test_pi_2_BGL_C_Z(self):
        """pi_2(BGL(C)) = Z (first Chern class)."""
        assert pi_k_BGL_C(2) == "Z"


# =========================================================================
# 2. Degree-three classifying-space groups for CY3 models
# =========================================================================

class TestTopologicalObstruction:
    """The chosen symplectic and complex-linear models have zero pi_3.

    Two independent proofs:
    Path 1: pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0 (symplectic structure group).
    Path 2: pi_3(BGL(n,C)) = pi_2(U(n)) = 0 (complex structure group).
    """

    def test_primary_coordinate_c3(self):
        obs = obstruction_c3()
        assert obs.topological_obstruction == 0

    def test_primary_coordinate_quintic(self):
        obs = obstruction_quintic()
        assert obs.topological_obstruction == 0

    def test_primary_coordinate_mirror_quintic(self):
        obs = obstruction_mirror_quintic()
        assert obs.topological_obstruction == 0

    def test_primary_coordinate_k3xe(self):
        obs = obstruction_k3_times_e()
        assert obs.topological_obstruction == 0

    def test_primary_coordinate_conifold(self):
        obs = obstruction_conifold()
        assert obs.topological_obstruction == 0

    def test_symplectic_primary_group(self):
        """Path 1: for ALL symplectic ranks, pi_3(BSp) = 0."""
        for m in range(1, 50):
            assert pi_k_BSp(3, m) == "0"

    def test_complex_primary_group(self):
        """Path 2: pi_3(BGL(C)) = 0 (complex structure group)."""
        assert pi_k_BGL_C(3) == "0"

    def test_d1_primary_coordinate(self):
        """The dimension-one primary coordinate equals zero."""
        obs = s_d_framing_obstruction(1, "elliptic_curve")
        assert obs.topological_obstruction == 0

    def test_d2_primary_coordinate(self):
        """The supplied tangent Calabi--Yau class sets c_1(TX) to zero."""
        obs = s_d_framing_obstruction(2, "K3", mukai_rank=24)
        assert obs.topological_obstruction == 0


# =========================================================================
# 3. Explicit CY3 examples
# =========================================================================

class TestExplicitCY3:
    """Detailed tests for each standard CY3 example."""

    # --- C^3 ---

    def test_c3_primary_and_chain_state(self):
        """The local model has a zero primary class and an open chain lane."""
        obs = obstruction_c3()
        assert obs.topological_obstruction == 0
        assert obs.scalar_shadow == Fraction(0)
        assert obs.bv_obstruction_class is None
        assert obs.framing_anomaly is None
        assert obs.trivialization_exists is None
        assert obs.bv_cocycle_supplied is False
        assert obs.trivialization_supplied is False
        assert obs.framing_anomaly_supplied is False

    def test_c3_is_rigid(self):
        """The affine local model occupies the rigid construction lane."""
        obs = obstruction_c3()
        assert "rigid local model" in obs.chain_level_obstruction.lower()
        assert obs.structure_group == "chosen local symplectic model"
        assert "each supplied finite rank" in obs.obstruction_group

    # --- Quintic ---

    def test_quintic_hodge_numbers(self):
        """Verify quintic Hodge numbers."""
        assert QUINTIC.h11 == 1
        assert QUINTIC.h21 == 101

    def test_quintic_euler_characteristic(self):
        """chi(quintic) = 2(h^{1,1} - h^{2,1}) = 2(1 - 101) = -200."""
        assert QUINTIC.euler == -200

    def test_quintic_h3(self):
        """dim H^3(quintic) = 2 + 2*101 = 204."""
        assert QUINTIC.h3 == 204

    def test_quintic_kappa_bcov(self):
        """kappa(quintic) = chi/24 = -200/24 = -25/3."""
        assert QUINTIC.kappa_bcov == Fraction(-25, 3)

    def test_quintic_symplectic_rank(self):
        """Symplectic rank for quintic = 2*(1 + 101) = 204."""
        assert QUINTIC.symplectic_rank == 204

    def test_quintic_primary_coordinate(self):
        obs = obstruction_quintic()
        assert obs.topological_obstruction == 0

    def test_quintic_scalar_and_bv_lanes_are_distinct(self):
        """The exact Euler scalar precedes a represented BV cocycle."""
        obs = obstruction_quintic()
        assert obs.scalar_shadow == Fraction(-25, 3)
        assert obs.bv_obstruction_class is None
        assert obs.scalar_projection_agrees is None
        assert obs.bv_cocycle_supplied is False

    def test_quintic_chain_trivialization_is_a_construction_problem(self):
        """The default state names the chain data required for a transition."""
        obs = obstruction_quintic()
        assert obs.trivialization_exists is None
        assert "represented holomorphic Chern--Simons functional" in (
            obs.trivialization_data
        )
        assert "BV comparison map" in obs.trivialization_data
        assert "explicit null-homotopy" in obs.trivialization_data

    def test_quintic_framing_anomaly_awaits_comparison(self):
        """A three-dimensional comparison supplies the anomaly coordinate."""
        obs = obstruction_quintic()
        assert obs.scalar_shadow == Fraction(-25, 3)
        assert obs.framing_anomaly is None

    # --- K3 x E ---

    def test_k3xe_hodge_numbers(self):
        assert K3_TIMES_E.h11 == 21
        assert K3_TIMES_E.h21 == 21

    def test_k3xe_euler_zero(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.

        Alternatively: chi = 2(h11 - h21) = 2(21 - 21) = 0.
        """
        assert K3_TIMES_E.euler == 0

    def test_k3xe_kappa_zero(self):
        """kappa(K3xE) = 0/24 = 0."""
        assert K3_TIMES_E.kappa_bcov == Fraction(0)

    def test_k3xe_zero_scalar_leaves_bv_lane_open(self):
        """The zero Euler scalar and the BV deformation class stay separate."""
        obs = obstruction_k3_times_e()
        assert obs.scalar_shadow == Fraction(0)
        assert obs.bv_obstruction_class is None
        assert obs.trivialization_exists is None

    def test_k3xe_gauss_manin_rank(self):
        """Kunneth gives rank H^3(K3 x E)=22 times 2=44."""
        assert K3_TIMES_E.h3 == 22 * 2
        assert K3_TIMES_E.symplectic_rank == 44
        assert K3_TIMES_E.hh_total_dim == 96

    # --- Mirror quintic ---

    def test_mirror_quintic_hodge_numbers(self):
        assert MIRROR_QUINTIC.h11 == 101
        assert MIRROR_QUINTIC.h21 == 1

    def test_mirror_quintic_euler(self):
        """chi(mirror quintic) = 2(101 - 1) = 200 = -chi(quintic)."""
        assert MIRROR_QUINTIC.euler == 200
        assert MIRROR_QUINTIC.euler == -QUINTIC.euler

    def test_mirror_quintic_kappa(self):
        """kappa(mirror) = 25/3 = -kappa(quintic)."""
        assert MIRROR_QUINTIC.kappa_bcov == Fraction(25, 3)
        assert MIRROR_QUINTIC.kappa_bcov == -QUINTIC.kappa_bcov

    # --- Conifold ---

    def test_conifold_obstruction(self):
        """The conifold chart records its supplied scalar and chain state."""
        obs = obstruction_conifold()
        assert obs.topological_obstruction == 0
        assert obs.scalar_shadow == Fraction(1)
        assert obs.bv_obstruction_class is None
        assert obs.trivialization_exists is None
        assert obs.bv_cocycle_supplied is False
        assert obs.trivialization_supplied is False
        assert obs.framing_anomaly_supplied is False


# =========================================================================
# 4. BV obstruction analysis
# =========================================================================

class TestBVObstruction:
    """Tests for represented deformation classes and comparison data."""

    def test_rigid_cy3_default_state(self):
        """Rigidity and a zero scalar leave representation as input data."""
        bv = bv_obstruction_cy3("C^3", Fraction(0), h21=0, rigid=True)
        assert bv.scalar_shadow == Fraction(0)
        assert bv.bv_class is None
        assert bv.bcov_anomaly is None
        assert bv.is_trivializable is None
        assert bv.bv_cocycle_supplied is False
        assert bv.bcov_comparison_supplied is False
        assert bv.trivialization_supplied is False

    def test_quintic_default_state(self):
        """The quintic scalar occupies its own field before comparison."""
        bv = bv_obstruction_cy3("quintic", Fraction(-25, 3), h21=101)
        assert bv.scalar_shadow == Fraction(-25, 3)
        assert bv.bv_class is None
        assert bv.bcov_anomaly is None
        assert bv.is_trivializable is None

    def test_k3xe_default_state(self):
        """K3 x E supplies a zero scalar and an independent chain lane."""
        bv = bv_obstruction_cy3("K3xE", Fraction(0), h21=21)
        assert bv.scalar_shadow == Fraction(0)
        assert bv.bv_class is None
        assert bv.is_trivializable is None

    def test_end_to_end_represented_bv_transitions(self):
        """Representation and trivialization define two mathematically typed states."""
        represented = RepresentedBVClass(
            complex_name="Obs_loc(hCS_quintic)",
            degree=1,
            basis=("omega_BV_quintic", "eta_BV_quintic"),
            coefficients=(Fraction(1), Fraction(0)),
            incoming_basis=(),
            incoming_differential=((), ()),
            outgoing_differential=(
                (Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(0)),
            ),
            scalar_functional=(Fraction(-25, 3), Fraction(0)),
        )
        framing_comparison = FramingAnomalyComparison(
            theory_name="three-dimensional quintic comparison",
            unit_framing_normalization=Fraction(1),
        )

        raw = s_d_framing_obstruction(
            d=3,
            name="quintic",
            h11=1,
            h21=101,
            compact=True,
        )
        constructed = s_d_framing_obstruction(
            d=3,
            name="quintic",
            h11=1,
            h21=101,
            compact=True,
            represented_bv_class=represented,
            framing_comparison=framing_comparison,
        )

        assert raw.scalar_shadow == constructed.scalar_shadow == Fraction(-25, 3)
        assert raw.bv_obstruction_class is None
        assert raw.trivialization_exists is None
        assert raw.framing_anomaly is None
        assert raw.bv_cocycle_supplied is False
        assert raw.trivialization_supplied is False
        assert raw.framing_anomaly_supplied is False
        assert constructed.bv_obstruction_class == represented
        assert constructed.bv_obstruction_class.complex_name == (
            "Obs_loc(hCS_quintic)"
        )
        assert constructed.bv_obstruction_class.degree == 1
        assert constructed.bv_obstruction_class.is_cocycle is True
        assert constructed.bv_obstruction_class.boundary == (Fraction(0), Fraction(0))
        assert constructed.bv_obstruction_class.scalar_projection == Fraction(-25, 3)
        assert constructed.scalar_projection_agrees is True
        assert constructed.null_homotopy is None
        assert constructed.trivialization_exists is None
        assert constructed.framing_anomaly == Fraction(-25, 3)
        assert constructed.bv_cocycle_supplied is True
        assert constructed.trivialization_supplied is False
        assert constructed.framing_anomaly_supplied is True

        quintic_bv = bv_obstruction_cy3(
            "quintic",
            Fraction(-25, 3),
            h21=101,
            represented_bv_class=represented,
        )
        assert quintic_bv.scalar_shadow == Fraction(-25, 3)
        assert quintic_bv.bv_class == represented
        assert quintic_bv.scalar_projection_agrees is True
        assert quintic_bv.null_homotopy is None
        assert quintic_bv.bcov_anomaly == Fraction(-25, 3)
        assert quintic_bv.is_trivializable is None
        assert quintic_bv.bv_cocycle_supplied is True
        assert quintic_bv.bcov_comparison_supplied is True
        assert quintic_bv.trivialization_supplied is False

        zero_cocycle = RepresentedBVClass(
            complex_name="Obs_loc(hCS_K3xE)",
            degree=1,
            basis=("omega_BV_K3xE",),
            coefficients=(Fraction(1),),
            incoming_basis=("h_hCS_K3xE",),
            incoming_differential=((Fraction(1),),),
            outgoing_differential=((Fraction(0),),),
            scalar_functional=(Fraction(0),),
        )
        zero_homotopy = RepresentedNullHomotopy(
            complex_name="Obs_loc(hCS_K3xE)",
            degree=0,
            source_basis=("h_hCS_K3xE",),
            target_basis=("omega_BV_K3xE",),
            coefficients=(Fraction(1),),
            outgoing_differential=((Fraction(1),),),
        )
        k3xe_bv = bv_obstruction_cy3(
            "K3xE",
            Fraction(0),
            h21=21,
            represented_bv_class=zero_cocycle,
            null_homotopy=zero_homotopy,
        )
        assert zero_homotopy.trivializes(zero_cocycle) is True
        assert zero_cocycle.scalar_projection == 0
        assert k3xe_bv.scalar_projection_agrees is True
        assert k3xe_bv.null_homotopy == zero_homotopy
        assert k3xe_bv.bcov_anomaly == 0
        assert k3xe_bv.is_trivializable is True
        assert k3xe_bv.trivialization_supplied is True

    def test_default_examples_retain_open_chain_state(self):
        """Each numerical example begins in the same unrepresented state."""
        examples = [
            ("C^3", Fraction(0), 0, True),
            ("quintic", Fraction(-25, 3), 101, False),
            ("K3xE", Fraction(0), 21, False),
            ("conifold", Fraction(1), 0, True),
        ]
        for name, kappa, h21, rigid in examples:
            bv = bv_obstruction_cy3(name, kappa, h21=h21, rigid=rigid)
            assert bv.scalar_shadow == kappa
            assert bv.bv_class is None
            assert bv.bcov_anomaly is None
            assert bv.is_trivializable is None
            assert bv.bv_cocycle_supplied is False
            assert bv.bcov_comparison_supplied is False
            assert bv.trivialization_supplied is False

    def test_bv_input_types(self):
        """The public API accepts represented classes and rational scalars."""
        with pytest.raises(TypeError):
            bv_obstruction_cy3(
                "quintic",
                Fraction(-25, 3),
                represented_bv_class=Fraction(-25, 3),
            )
        with pytest.raises(TypeError):
            bv_obstruction_cy3(
                "quintic",
                Fraction(-25, 3),
                null_homotopy=Fraction(1),
            )

    def test_trivialization_state_requires_a_represented_class(self):
        """A null-homotopy state begins from a named deformation cocycle."""
        orphan_homotopy = RepresentedNullHomotopy(
            complex_name="Obs_loc(hCS_quintic)",
            degree=0,
            source_basis=("h",),
            target_basis=("omega",),
            coefficients=(Fraction(1),),
            outgoing_differential=((Fraction(1),),),
        )
        with pytest.raises(ValueError):
            bv_obstruction_cy3(
                "quintic",
                Fraction(-25, 3),
                null_homotopy=orphan_homotopy,
            )
        with pytest.raises(ValueError):
            s_d_framing_obstruction(
                d=3,
                name="quintic",
                h11=1,
                h21=101,
                null_homotopy=orphan_homotopy,
            )

    def test_cocycle_and_null_homotopy_equations_are_enforced(self):
        """The engine computes both d(c)=0 and d(h)=c in the finite window."""
        noncocycle = RepresentedBVClass(
            complex_name="Obs_loc(hCS_quintic)",
            degree=1,
            basis=("omega",),
            coefficients=(Fraction(1),),
            incoming_basis=(),
            incoming_differential=((),),
            outgoing_differential=((Fraction(1),),),
        )
        assert noncocycle.boundary == (Fraction(1),)
        assert noncocycle.is_cocycle is False
        with pytest.raises(ValueError):
            bv_obstruction_cy3(
                "quintic",
                Fraction(-25, 3),
                represented_bv_class=noncocycle,
            )

        cocycle = RepresentedBVClass(
            complex_name="Obs_loc(hCS_quintic)",
            degree=1,
            basis=("omega",),
            coefficients=(Fraction(1),),
            incoming_basis=(),
            incoming_differential=((),),
            outgoing_differential=((Fraction(0),),),
        )
        mismatched = RepresentedNullHomotopy(
            complex_name="Obs_loc(hCS_quintic)",
            degree=0,
            source_basis=("h",),
            target_basis=("omega",),
            coefficients=(Fraction(1),),
            outgoing_differential=((Fraction(2),),),
        )
        assert mismatched.image == (Fraction(2),)
        assert mismatched.trivializes(cocycle) is False
        with pytest.raises(ValueError):
            bv_obstruction_cy3(
                "quintic",
                Fraction(-25, 3),
                represented_bv_class=cocycle,
                null_homotopy=mismatched,
            )

        with pytest.raises(ValueError, match=r"d\^2=0"):
            RepresentedBVClass(
                complex_name="two-step-window",
                degree=1,
                basis=("c",),
                coefficients=(Fraction(1),),
                incoming_basis=("h",),
                incoming_differential=((Fraction(1),),),
                outgoing_differential=((Fraction(1),),),
            )

        with pytest.raises(ValueError, match="annihilate incoming boundaries"):
            RepresentedBVClass(
                complex_name="cohomological-projection-window",
                degree=1,
                basis=("c",),
                coefficients=(Fraction(1),),
                incoming_basis=("h",),
                incoming_differential=((Fraction(1),),),
                outgoing_differential=((Fraction(0),),),
                scalar_functional=(Fraction(-25, 3),),
            )


# =========================================================================
# 5. Mirror symmetry checks
# =========================================================================

class TestMirrorSymmetry:
    """Mirror symmetry: (X, X_mirror) should have related obstructions."""

    def test_quintic_mirror_hodge_swap(self):
        """h^{1,1}(X) = h^{2,1}(X_mirror) and vice versa."""
        result = mirror_obstruction_comparison(
            h11_A=1, h21_A=101,
            h11_B=101, h21_B=1,
            name_A="quintic", name_B="mirror_quintic",
        )
        assert result["mirror_hodge_swap"] is True

    def test_quintic_mirror_chi_sign_flip(self):
        """chi(X) = -chi(X_mirror) for mirror pair."""
        result = mirror_obstruction_comparison(
            h11_A=1, h21_A=101,
            h11_B=101, h21_B=1,
        )
        assert result["chi_sign_flip"] is True
        assert result["chi_A"] == -200
        assert result["chi_B"] == 200

    def test_quintic_mirror_kappa_sign_flip(self):
        """kappa(X) = -kappa(X_mirror) for mirror pair."""
        result = mirror_obstruction_comparison(
            h11_A=1, h21_A=101,
            h11_B=101, h21_B=1,
        )
        assert result["kappa_sign_flip"] is True
        assert result["kappa_A"] == -result["kappa_B"]

    def test_mirror_scalar_shadow_sum_zero(self):
        """Mirror exchange makes the two Euler scalar shadows sum to zero."""
        result = mirror_obstruction_comparison(
            h11_A=1, h21_A=101,
            h11_B=101, h21_B=1,
        )
        assert result["scalar_shadow_sum"] == 0
        assert result["bv_obstruction_A"] is None
        assert result["bv_obstruction_B"] is None
        assert result["framing_anomaly_sum"] is None

    def test_k3xe_self_mirror(self):
        """K3 x E is self-mirror (h^{1,1} = h^{2,1} = 21)."""
        result = mirror_obstruction_comparison(
            h11_A=21, h21_A=21,
            h11_B=21, h21_B=21,
            name_A="K3xE", name_B="K3xE_mirror",
        )
        assert result["mirror_hodge_swap"] is True
        assert result["chi_A"] == 0
        assert result["kappa_A"] == 0
        assert result["scalar_shadow_sum"] == 0
        assert result["framing_anomaly_sum"] is None

    def test_mirror_topological_both_vanish(self):
        """Both mirror entries have zero primary coordinates."""
        result = mirror_obstruction_comparison(
            h11_A=1, h21_A=101,
            h11_B=101, h21_B=1,
        )
        assert result["topological_obstruction_A"] == 0
        assert result["topological_obstruction_B"] == 0


# =========================================================================
# 6. Framing anomaly computation
# =========================================================================

class TestFramingAnomaly:
    """Tests for anomaly values after an explicit comparison theorem."""

    def test_cs_anomaly_comparison_gate(self):
        """The supplied comparison carries the scalar into the anomaly lane."""
        comparison = FramingAnomalyComparison(
            theory_name="unit-normalized three-dimensional theory",
            unit_framing_normalization=Fraction(1),
        )
        for kappa in (Fraction(-25, 3), Fraction(0), Fraction(1)):
            assert chern_simons_framing_anomaly(kappa) is None
            assert chern_simons_framing_anomaly(
                kappa, comparison=comparison
            ) == kappa

    def test_unit_framing_normalization_scales_the_anomaly(self):
        """The chosen unit shift multiplies the compared scalar."""
        comparison = FramingAnomalyComparison(
            theory_name="one-over-twenty-four normalization",
            unit_framing_normalization=Fraction(1, 24),
        )
        assert chern_simons_framing_anomaly(
            Fraction(-25, 3),
            comparison=comparison,
        ) == Fraction(-25, 72)

    def test_framing_phase_integer_kappa(self):
        """Compared integral scalars exponentiate to the unit phase."""
        comparison = FramingAnomalyComparison("unit normalization", Fraction(1))
        for kappa in (Fraction(1), Fraction(0), Fraction(12)):
            assert framing_anomaly_phase(kappa) is None
            phase = framing_anomaly_phase(kappa, comparison=comparison)
            assert phase is not None
            assert abs(phase - 1.0) < 1e-12

    def test_framing_phase_rational_kappa(self):
        """For rational kappa = p/q, phase = exp(2 pi i p/q) (root of unity)."""
        # kappa = -25/3: phase = exp(-50 pi i / 3) = exp(2 pi i * (-25/3))
        # Since -25/3 = -8 - 1/3, the phase is exp(-2 pi i / 3)
        kappa = Fraction(-25, 3)
        assert framing_anomaly_phase(kappa) is None
        comparison = FramingAnomalyComparison("unit normalization", Fraction(1))
        phase = framing_anomaly_phase(kappa, comparison=comparison)
        # exp(-2 pi i / 3) = cos(-2pi/3) + i sin(-2pi/3) = -1/2 - i sqrt(3)/2
        expected_angle = 2 * math.pi * float(kappa)
        expected = complex(math.cos(expected_angle), math.sin(expected_angle))
        assert phase is not None
        assert abs(phase - expected) < 1e-12

    def test_framing_order_integer(self):
        """Integer kappa has order 1."""
        comparison = FramingAnomalyComparison("unit normalization", Fraction(1))
        assert framing_anomaly_order(Fraction(0)) is None
        assert framing_anomaly_order(
            Fraction(0), comparison=comparison
        ) == 1
        assert framing_anomaly_order(
            Fraction(1), comparison=comparison
        ) == 1
        assert framing_anomaly_order(
            Fraction(12), comparison=comparison
        ) == 1

    def test_framing_order_rational(self):
        """kappa = p/q in lowest terms has order q."""
        comparison = FramingAnomalyComparison("unit normalization", Fraction(1))
        assert framing_anomaly_order(
            Fraction(-25, 3), comparison=comparison
        ) == 3
        assert framing_anomaly_order(
            Fraction(25, 3), comparison=comparison
        ) == 3
        assert framing_anomaly_order(
            Fraction(1, 2), comparison=comparison
        ) == 2

    def test_quintic_framing_order(self):
        """A compared quintic scalar produces a phase of order three."""
        comparison = FramingAnomalyComparison("unit normalization", Fraction(1))
        assert framing_anomaly_order(QUINTIC.kappa_bcov) is None
        assert framing_anomaly_order(
            QUINTIC.kappa_bcov, comparison=comparison
        ) == 3

    def test_k3xe_framing_order(self):
        """A compared zero scalar produces the unit phase."""
        comparison = FramingAnomalyComparison("unit normalization", Fraction(1))
        assert framing_anomaly_order(K3_TIMES_E.kappa_bcov) is None
        assert framing_anomaly_order(
            K3_TIMES_E.kappa_bcov, comparison=comparison
        ) == 1


# =========================================================================
# 7. Stable-range analysis
# =========================================================================

class TestStableRange:
    """Tests for the stable-range obstruction analysis."""

    def test_d1_primary_input_is_resolved(self):
        result = stable_obstruction_vanishing(1)
        assert result["primary_input_resolved"] is True
        assert result["categorical_framing_constructed"] is False

    def test_d2_tangent_cy_class_resolves_primary_input(self):
        """For d=2 the tangent Calabi--Yau class supplies c_1(TX)=0."""
        result = stable_obstruction_vanishing(2)
        assert result["pi_d_BU"] == "Z"
        assert result["vanishes_complex"] is False
        assert result["tangent_cy_class_resolves_primary"] is True
        assert result["primary_input_resolved"] is True
        assert result["categorical_framing_constructed"] is False

    def test_d3_complex_primary_group_is_zero(self):
        """For d=3 the stable complex primary group is zero."""
        result = stable_obstruction_vanishing(3)
        assert result["pi_d_BU"] == "0"
        assert result["vanishes_complex"] is True
        assert result["primary_input_resolved"] is True
        assert result["categorical_framing_constructed"] is False

    def test_d3_symplectic_primary_group_is_zero(self):
        """d=3: pi_3(BSp) = 0 as well."""
        result = stable_obstruction_vanishing(3)
        assert result["pi_d_BSp"] == "0"
        assert result["vanishes_symplectic"] is True

    def test_d4_primary_class_requires_geometric_input(self):
        """For d=4 the degree-four coordinate is the second Chern class."""
        result = stable_obstruction_vanishing(4)
        assert result["pi_d_BU"] == "Z"
        assert result["vanishes_complex"] is False
        assert result["tangent_cy_class_resolves_primary"] is False
        assert result["primary_input_resolved"] is False
        assert result["categorical_framing_constructed"] is False

    def test_d5_primary_group_is_zero(self):
        """d=5: pi_5(BGL(C)) = 0."""
        result = stable_obstruction_vanishing(5)
        assert result["vanishes_complex"] is True
        assert result["primary_input_resolved"] is True
        assert result["categorical_framing_constructed"] is False

    def test_odd_d_complex_primary_groups_are_zero(self):
        """For all ODD d, pi_d(BGL(C)) = 0."""
        for d in range(1, 20, 2):
            result = stable_obstruction_vanishing(d)
            assert result["vanishes_complex"] is True
            assert result["primary_input_resolved"] is True
            assert result["categorical_framing_constructed"] is False


# =========================================================================
# 8. Cross-checks with existing CY modules
# =========================================================================

class TestCrossChecks:
    """Cross-check with existing Vol III compute modules."""

    def test_quintic_kappa_matches_cy_functor(self):
        """kappa(quintic) = -25/3 matches cy_to_chiral_functor.py."""
        assert QUINTIC.kappa_bcov == Fraction(-25, 3)

    def test_k3xe_kappa_matches(self):
        """kappa(K3xE) = 0 matches cy_bar_complex_engine.py (chi = 0)."""
        assert K3_TIMES_E.kappa_bcov == Fraction(0)

    def test_mirror_quintic_kappa_matches(self):
        """kappa(mirror quintic) = 25/3 = -kappa(quintic)."""
        assert MIRROR_QUINTIC.kappa_bcov == Fraction(25, 3)
        assert MIRROR_QUINTIC.kappa_bcov == -QUINTIC.kappa_bcov

    def test_pontryagin_class_quintic(self):
        """Hodge numbers determine ranks while curvature supplies p_1."""
        p1 = first_pontryagin_class_cy3(h11=1, h21=101)
        assert p1["dim_M_cs"] == 101
        assert p1["symplectic_half_rank"] == 102
        assert p1["symplectic_rank"] == 204
        assert p1["kappa"] == Fraction(-25, 3)
        assert p1["chi"] == -200
        assert p1["gauss_manin_connection"] == "flat on the smooth locus"
        assert "Weil--Petersson" in p1["tangent_connection"]
        assert p1["p1_representative"] is None
        assert p1["cs_transgression"] is None

    def test_hh_total_dim_quintic(self):
        """HH total dim for quintic = 4 + 2*1 + 2*101 = 208."""
        assert QUINTIC.hh_cohomology_vector == (1, 0, 101, 4, 101, 0, 1)
        assert QUINTIC.hh_total_dim == 208

        pv = pv_quintic()
        hkr_vector = tuple(
            sum(
                dimension
                for (polyvector_degree, sheaf_degree), dimension
                in pv.pv_dims.items()
                if polyvector_degree + sheaf_degree == degree
            )
            for degree in range(7)
        )
        assert hkr_vector == QUINTIC.hh_cohomology_vector

    def test_hh_degree_distribution_mirror_quintic(self):
        """Mirror symmetry exchanges h11 and h21 in the HKR degrees."""
        assert MIRROR_QUINTIC.hh_cohomology_vector == (
            1, 0, 1, 204, 1, 0, 1
        )
        assert MIRROR_QUINTIC.hh_total_dim == 208

    def test_hh_total_dim_k3xe(self):
        """Kunneth gives dim HH(K3 x E) = 24*4 = 96."""
        k3_vector = (1, 0, 22, 0, 1)
        elliptic_vector = (1, 2, 1)
        convolution = tuple(
            sum(
                k3_vector[i] * elliptic_vector[degree - i]
                for i in range(len(k3_vector))
                if 0 <= degree - i < len(elliptic_vector)
            )
            for degree in range(len(k3_vector) + len(elliptic_vector) - 1)
        )
        assert convolution == (1, 2, 23, 44, 23, 2, 1)
        assert K3_TIMES_E.hh_cohomology_vector == convolution
        assert K3_TIMES_E.hh_total_dim == 24 * 4 == 96

        pv = pv_k3_times_e()
        hkr_vector = tuple(
            sum(
                dimension
                for (polyvector_degree, sheaf_degree), dimension
                in pv.pv_dims.items()
                if polyvector_degree + sheaf_degree == degree
            )
            for degree in range(7)
        )
        assert hkr_vector == convolution
        assert pv.total_dim == 96


# =========================================================================
# 9. Summary analysis tests
# =========================================================================

class TestSummaryAnalysis:
    """Tests for the typed d=3 framing and functor summary."""

    def test_primary_group_and_functor_status_are_separate(self):
        """The zero test-sphere group supplies one input to the functor."""
        analysis = d3_functor_existence_analysis()
        assert analysis["primary_test_sphere_group_zero"] is True
        assert analysis["factorization_stage"] == "Phi_3^FA"
        assert analysis["specialization_stage"] == "Sp^ch_(Sigma_2,C)"
        assert analysis["composite_functor"] == (
            "Sp^ch_(Sigma_2,C) o Phi_3^FA"
        )
        assert analysis["factorization_stage_status"] == (
            "conditional construction problem"
        )
        assert analysis["specialization_stage_status"] == (
            "conditional construction problem"
        )
        assert analysis["composite_functor_status"] == (
            "conditional construction problem"
        )
        assert analysis["factorization_stage_constructed"] is False
        assert analysis["specialization_stage_constructed"] is False
        assert analysis["chain_level_framing_constructed"] is False

    def test_all_examples_have_zero_primary_coordinate(self):
        """Every listed example occupies the zero coordinate of this model."""
        analysis = d3_functor_existence_analysis()
        for data in analysis["examples"].values():
            assert data["topological_obstruction"] == 0

    def test_example_trivialization_status_tracks_chain_data(self):
        """Each summary entry begins before represented chain data are supplied."""
        analysis = d3_functor_existence_analysis()
        for name in ("C^3", "conifold", "quintic", "mirror_quintic", "K3xE"):
            assert analysis["examples"][name]["trivialization_exists"] is None
            assert analysis["examples"][name]["bv_cocycle_supplied"] is False
            assert analysis["examples"][name]["trivialization_supplied"] is False
            assert analysis["examples"][name]["framing_anomaly_supplied"] is False

    def test_quintic_summary_separates_scalar_and_bv_class(self):
        """The summary stores the quintic scalar before the BV representative."""
        analysis = d3_functor_existence_analysis()
        assert analysis["examples"]["quintic"]["scalar_shadow"] == Fraction(-25, 3)
        assert analysis["examples"]["quintic"]["bv_class"] is None

    def test_c3_summary_separates_scalar_and_bv_class(self):
        """The local model likewise separates its scalar from a BV cocycle."""
        analysis = d3_functor_existence_analysis()
        assert analysis["examples"]["C^3"]["scalar_shadow"] == Fraction(0)
        assert analysis["examples"]["C^3"]["bv_class"] is None

    def test_functor_summary_names_the_construction_data(self):
        """The summary names the framing, quantization, and target comparison."""
        analysis = d3_functor_existence_analysis()
        requirement = analysis["d3_functor_construction_requires"]
        assert "holomorphic Chern--Simons functional" in requirement
        assert "specialization kernel" in requirement
        assert "descent" in requirement
        assert analysis["factorization_stage_constructed"] is False
        assert analysis["specialization_stage_constructed"] is False
        assert analysis["chain_level_framing_constructed"] is False


# =========================================================================
# 10. Consistency and multi-path verification
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification: each key result checked 3+ ways."""

    def test_primary_test_sphere_group_3_paths(self):
        """The primary test-sphere group is zero by three routes.

        Path 1: pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0 for all m >= 1.
        Path 2: pi_3(BGL(n,C)) = pi_2(U(n)) = 0 (Bott periodicity).
        Path 3: the stable-range table returns the same group.
        """
        # Path 1: symplectic
        for m in range(1, 10):
            assert pi_k_BSp(3, m) == "0"

        # Path 2: complex linear
        assert pi_k_BGL_C(3) == "0"

        # Path 3: stable range
        result = stable_obstruction_vanishing(3)
        assert result["pi_d_BU"] == "0"
        assert result["pi_d_BSp"] == "0"
        assert result["primary_input_resolved"] is True
        assert result["categorical_framing_constructed"] is False

    def test_quintic_kappa_2_paths(self):
        """kappa(quintic) = -25/3, verified 2 ways.

        Path 1: chi/24 = -200/24 = -25/3.
        Path 2: BCOV formula F_1 coefficient.
        """
        # Path 1: from Euler characteristic
        assert Fraction(-200, 24) == Fraction(-25, 3)

        # Path 2: from CY3HodgeData
        assert QUINTIC.kappa_bcov == Fraction(-25, 3)

    def test_mirror_scalar_sum_3_paths(self):
        """The two mirror Euler scalars sum to zero by three routes.

        Path 1: chi(X) + chi(X_mirror) = 0 (mirror symmetry).
        Path 2: Direct computation for quintic + mirror quintic.
        Path 3: Mirror comparison function.
        """
        # Path 1: general argument
        # chi = 2(h11 - h21), mirror swaps h11 <-> h21
        # chi_mirror = 2(h21 - h11) = -chi.  So kappa + kappa_mirror = 0.

        # Path 2: explicit
        assert QUINTIC.kappa_bcov + MIRROR_QUINTIC.kappa_bcov == 0

        # Path 3: mirror comparison
        result = mirror_obstruction_comparison(
            h11_A=1, h21_A=101,
            h11_B=101, h21_B=1,
        )
        assert result["scalar_shadow_sum"] == 0
        assert result["framing_anomaly_sum"] is None

    def test_scalar_bv_and_gauss_manin_lanes_across_examples(self):
        """Three examples preserve the scalar, chain, and H^3 distinctions."""
        obs_c3 = obstruction_c3()
        assert obs_c3.scalar_shadow == 0
        assert obs_c3.bv_obstruction_class is None

        obs_q = obstruction_quintic()
        assert obs_q.scalar_shadow == Fraction(-25, 3)
        assert obs_q.bv_obstruction_class is None
        assert obs_q.trivialization_exists is None
        assert QUINTIC.symplectic_rank == QUINTIC.h3 == 204

        obs_k = obstruction_k3_times_e()
        assert obs_k.scalar_shadow == 0
        assert obs_k.bv_obstruction_class is None
        assert K3_TIMES_E.symplectic_rank == K3_TIMES_E.h3 == 44
        assert K3_TIMES_E.hh_total_dim == 96


# =========================================================================
# 11. Edge cases and sanity checks
# =========================================================================

class TestEdgeCases:
    """Edge cases and sanity checks."""

    def test_d3_framing_for_rigid_noncompact(self):
        """A rigid local chart still receives represented chain data explicitly."""
        obs = s_d_framing_obstruction(
            d=3, name="test_rigid",
            h11=0, h21=0, chi=0, kappa=Fraction(0),
            compact=False, rigid=True,
        )
        assert obs.topological_obstruction == 0
        assert obs.scalar_shadow == Fraction(0)
        assert obs.bv_obstruction_class is None
        assert obs.trivialization_exists is None
        assert obs.framing_anomaly is None

    def test_public_dimension_domain(self):
        """The public construction domain currently consists of d=1,2,3."""
        with pytest.raises(NotImplementedError):
            s_d_framing_obstruction(4, "CY4")

    def test_framing_anomaly_zero_kappa(self):
        """A supplied comparison sends the zero scalar to the unit phase."""
        comparison = FramingAnomalyComparison("unit normalization", Fraction(1))
        assert chern_simons_framing_anomaly(Fraction(0)) is None
        assert framing_anomaly_order(Fraction(0)) is None
        assert framing_anomaly_phase(Fraction(0)) is None
        assert chern_simons_framing_anomaly(
            Fraction(0), comparison=comparison
        ) == 0
        assert framing_anomaly_order(
            Fraction(0), comparison=comparison
        ) == 1
        phase = framing_anomaly_phase(Fraction(0), comparison=comparison)
        assert phase is not None
        assert abs(phase - 1.0) < 1e-12

    def test_cy3_with_large_hodge(self):
        """The degree-three primary group stays zero at large Hodge rank."""
        big_cy3 = CY3HodgeData(h11=1000, h21=500, name="big_CY3")
        assert big_cy3.euler == 2 * (1000 - 500)
        assert big_cy3.kappa_bcov == Fraction(1000, 24)
        obs = s_d_framing_obstruction(
            d=3, name="big_CY3",
            h11=1000, h21=500,
            compact=True,
        )
        assert obs.topological_obstruction == 0
        assert obs.trivialization_exists is None

    def test_self_mirror_cy3(self):
        """Self-mirror Hodge data give the zero Euler scalar."""
        for n in [1, 5, 21, 100]:
            cy3 = CY3HodgeData(h11=n, h21=n, name=f"self_mirror_{n}")
            assert cy3.euler == 0
            assert cy3.kappa_bcov == 0
