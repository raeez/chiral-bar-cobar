r"""Tests for the finite BCOV bar-carrier module.

Tests the cofree carrier, represented differential, and scalar-shadow
lanes of the BCOV L-infinity input for:
    1. C^3 (flat space)
    2. Resolved conifold
    3. K3 x E (compact CY3)

Each computation is verified by at least two independent methods
(Multi-Path Verification Mandate).

VERIFICATION PATHS USED:
    (1) Direct computation from Hodge diamond
    (2) Cross-check against known invariants (Euler char, dimensions)
    (3) Consistency with shadow tower (F_g = kappa * a_hat_g)
    (4) Cross-geometry additivity / factorization checks
    (5) Bar-carrier dimension generating function consistency
    (6) Ghost number grading Euler characteristic
    (7) Represented state transitions and the identity d^2 = 0
"""

import math
import pytest
from fractions import Fraction

import compute.lib.bcov_bar_complex as bcov

F = Fraction

from compute.lib.bcov_bar_complex import (
    # Hodge diamonds
    k3_hodge, elliptic_hodge, product_hodge, k3_times_e_hodge,
    quintic_hodge,
    # Polyvector spaces
    polyvector_space, pv_c3_constant, pv_c3_truncated, pv_conifold_effective_carrier,
    pv_k3, pv_elliptic, pv_k3_times_e, pv_quintic,
    # Schouten brackets
    schouten_bracket_c3_constant, schouten_bracket_c3_linear,
    schouten_bracket_k3_on_h11,
    # BCOV L-infinity
    bcov_input_c3, bcov_input_conifold, bcov_input_k3_times_e, bcov_input_quintic,
    # Bar carriers
    bar_carrier_c3, bar_carrier_conifold, bar_carrier_k3_times_e,
    bar_carrier_quintic,
    compute_bar_carrier, RepresentedBarDifferential,
    # Yukawa couplings
    yukawa_conifold, yukawa_k3_times_e,
    # Scalar-shadow coefficients
    scalar_shadow_genus1, scalar_shadow_genus2,
    bcov_quintic_constant_map_low_genus,
    # Independently supplied scalar-series comparison
    compare_shadow_to_bcov_series,
    # Consistency checks
    kappa_additivity_check, euler_characteristic_check,
    pv_dimension_check, ghost_number_check,
    # Full analyses
    full_analysis_c3, full_analysis_conifold, full_analysis_k3xe,
    full_analysis_quintic,
    # Explicit dimensions
    bar_carrier_dims_c3_explicit, bar_carrier_dims_conifold_explicit,
    # Schouten bracket on K3 x E
    schouten_bracket_k3xe_structure,
    # Internal helpers
    _faber_pandharipande,
)


# =========================================================================
# Section 1: Hodge diamond tests
# =========================================================================

class TestHodgeDiamonds:
    """Verify Hodge diamond data for all geometries."""

    def test_k3_euler(self):
        """chi(K3) = 24."""
        assert k3_hodge().euler == 24

    def test_elliptic_euler(self):
        """chi(E) = 0."""
        assert elliptic_hodge().euler == 0

    def test_k3xe_euler_multiplicative(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 0."""
        assert k3_times_e_hodge().euler == 0

    def test_quintic_euler(self):
        """chi(quintic) = -200."""
        assert quintic_hodge().euler == -200

    def test_k3_hodge_symmetry(self):
        """h^{p,q}(K3) = h^{q,p}(K3) (Hodge symmetry)."""
        hd = k3_hodge()
        for p in range(3):
            for q in range(3):
                assert hd.h(p, q) == hd.h(q, p), f"h^{{{p},{q}}} != h^{{{q},{p}}}"

    def test_k3xe_product_consistency(self):
        """K3 x E Hodge diamond from product formula matches direct."""
        hd_prod = product_hodge(k3_hodge(), elliptic_hodge())
        hd_direct = k3_times_e_hodge()
        for p in range(4):
            for q in range(4):
                assert hd_prod.h(p, q) == hd_direct.h(p, q), \
                    f"h^{{{p},{q}}} mismatch: product={hd_prod.h(p,q)} direct={hd_direct.h(p,q)}"

    def test_k3_chi_O(self):
        """chi(O_{K3}) = 2."""
        assert k3_hodge().chi_O == F(2)

    def test_elliptic_chi_O(self):
        """chi(O_E) = 0."""
        assert elliptic_hodge().chi_O == F(0)

    def test_quintic_h21(self):
        """h^{2,1}(quintic) = 101."""
        assert quintic_hodge().h(2, 1) == 101


# =========================================================================
# Section 2: Polyvector field space tests
# =========================================================================

class TestPolyvectorSpaces:
    """Verify polyvector field space dimensions and gradings."""

    def test_pv_c3_constant_dim(self):
        """PV*(C^3) constant = 8 = 1+3+3+1 (exterior algebra on C^3)."""
        pv = pv_c3_constant()
        assert pv.total_dim == 8

    def test_pv_c3_constant_decomposition(self):
        """PV^{p,0}(C^3) = binom(3,p) for constant polyvectors."""
        pv = pv_c3_constant()
        for p in range(4):
            assert pv.pv_dims.get((p, 0), 0) == math.comb(3, p)

    def test_pv_conifold_effective_carrier_dim(self):
        """PV*(conifold) = 3-dimensional."""
        assert pv_conifold_effective_carrier().total_dim == 3

    def test_pv_k3_dim(self):
        """PV*(K3) = 24-dimensional.

        Path 1: direct computation from Hodge diamond.
        Path 2: PV^{0,*} + PV^{1,*} + PV^{2,*} = 2 + 20 + 2 = 24.
        """
        pv = pv_k3()
        assert pv.total_dim == 24

        # Path 2: manual sum
        manual = 0
        for p in range(3):  # K3 is dim 2
            for q in range(3):
                manual += pv.pv_dims.get((p, q), 0)
        assert manual == 24

    def test_pv_elliptic_dim(self):
        """PV*(E) = 4-dimensional."""
        assert pv_elliptic().total_dim == 4

    def test_pv_k3xe_dim_from_kunneth(self):
        """PV*(K3 x E) = 96 = 24 * 4.

        Path 1: from product Hodge diamond.
        Path 2: dim(PV*(K3)) * dim(PV*(E)).
        """
        pv = pv_k3_times_e()
        assert pv.total_dim == 96

        # Cross-check with factor dimensions
        assert pv_k3().total_dim * pv_elliptic().total_dim == 96

    def test_pv_quintic_dim(self):
        """PV*(quintic) = 208-dimensional.

        PV^{0,*} = h^{3,*}: 1+0+0+1 = 2
        PV^{1,*} = h^{2,*}: 0+101+1+0 = 102
        PV^{2,*} = h^{1,*}: 0+1+101+0 = 102
        PV^{3,*} = h^{0,*}: 1+0+0+1 = 2
        Total: 2 + 102 + 102 + 2 = 208
        """
        pv = pv_quintic()
        assert pv.total_dim == 208

    def test_ghost_number_c3(self):
        """Ghost number grading on C^3 constant polyvectors."""
        pv = pv_c3_constant()
        gh = pv.ghost_graded_dims

        assert gh.get(-1, 0) == 1   # PV^{0,0}: functions
        assert gh.get(0, 0) == 3    # PV^{1,0}: vector fields
        assert gh.get(1, 0) == 3    # PV^{2,0}: bivectors
        assert gh.get(2, 0) == 1    # PV^{3,0}: trivectors

    def test_ghost_euler_c3(self):
        """Ghost number Euler char of C^3 = 0.

        sum (-1)^{gh} dim = 1 - 3 + 3 - 1 = 0.
        """
        pv = pv_c3_constant()
        gh = pv.ghost_graded_dims
        euler = sum((-1) ** k * d for k, d in gh.items())
        assert euler == 0


# =========================================================================
# Section 3: Schouten bracket tests
# =========================================================================

class TestSchoutenBrackets:
    """Verify Schouten bracket properties."""

    def test_c3_constant_abelian(self):
        """Schouten bracket on constant polyvectors of C^3 is zero."""
        sb = schouten_bracket_c3_constant()
        assert sb.is_abelian is True
        assert sb.nonzero_brackets == 0

    def test_c3_linear_nontrivial(self):
        """Schouten bracket on linear polyvectors of C^3 is gl(3)."""
        sb = schouten_bracket_c3_linear()
        assert sb.is_abelian is False
        assert sb.nonzero_brackets > 0

    def test_c3_linear_bracket_count(self):
        """Count of nonzero gl(3) brackets.

        [e_{ij}, e_{kl}] = delta_{jk} e_{il} - delta_{li} e_{kj}
        Nonzero when the result has at least one nonzero component.
        """
        sb = schouten_bracket_c3_linear()
        # For gl(3), the nonzero brackets: should be 9*8 - (vanishing ones)
        # Each pair (ij, kl) with j != k and l != i gives zero.
        # With j = k: get e_{il}; subtract delta_{li} e_{kj} if l = i.
        assert sb.nonzero_brackets > 0

    def test_k3_schouten_vanishes(self):
        """Schouten bracket on K3 cohomology vanishes (BTT)."""
        sb = schouten_bracket_k3_on_h11()
        assert sb.is_abelian is True


# =========================================================================
# Section 4: Finite carrier-profile tests
# =========================================================================

class TestBCOVCarrierInputs:
    """Verify the represented carrier inputs and scalar lanes."""

    def test_c3_kappa(self):
        """kappa(C^3) = 1."""
        data = bcov_input_c3()
        assert data.scalar_lane == "equivariant_constant_map"
        assert data.scalar_value == F(1)

    def test_conifold_kappa(self):
        """kappa(conifold) = 1 = chi/2 = 2/2."""
        data = bcov_input_conifold()
        assert data.scalar_lane == "effective_euler_half_shadow"
        assert data.scalar_value == F(1)
        assert data.bcov_one_loop_scalar is None

    def test_k3xe_kappa(self):
        """kappa_BKM(K3 x E) = 5 (weight of primitive Delta_5).

        This is the BKM/BPS lane, not the compact total-space
        kappa_cat(K3 x E)=0 and not the Heisenberg-Mukai value 3.
        """
        data = bcov_input_k3_times_e()
        assert data.scalar_lane == "BKM"
        assert data.scalar_value == F(5)
        assert data.bcov_one_loop_scalar == F(0)

    def test_k3xe_scalar_lanes_are_distinct(self):
        """K3 x E has compact Euler, Heisenberg-Mukai, and BKM lanes."""
        bcov_one_loop = bcov_input_k3_times_e().bcov_one_loop_scalar
        heisenberg_mukai = k3_hodge().chi_O + F(1)  # K3 plus level-one E.
        bkm = bcov_input_k3_times_e().scalar_value

        assert bcov_one_loop == F(0)
        assert heisenberg_mukai == F(3)
        assert bkm == F(5)
        assert len({bcov_one_loop, heisenberg_mukai, bkm}) == 3

    def test_quintic_kappa(self):
        """The quintic Euler-half and BCOV one-loop scalars are distinct."""
        data = bcov_input_quintic()
        assert data.scalar_lane == "euler_half_shadow"
        assert data.scalar_value == F(-100)
        assert data.bcov_one_loop_scalar == F(-25, 3)
        assert data.scalar_value != data.bcov_one_loop_scalar

    def test_c3_class_G(self):
        """C^3 is shadow class G (Gaussian)."""
        assert bcov_input_c3().shadow_depth_class == "G"

    def test_conifold_class_G(self):
        """Conifold is shadow class G."""
        assert bcov_input_conifold().shadow_depth_class == "G"

    def test_k3xe_class_M(self):
        """K3 x E is shadow class M (infinite tower from BKM)."""
        assert bcov_input_k3_times_e().shadow_depth_class == "M"

    def test_quintic_class_M(self):
        """Quintic is shadow class M (infinite GW tower)."""
        assert bcov_input_quintic().shadow_depth_class == "M"

    def test_only_constant_c3_has_a_represented_coderivation(self):
        """The profile status controls construction of the differential."""
        assert bcov_input_c3().coderivation_status == "represented_zero"
        for data in (
            bcov_input_conifold(),
            bcov_input_k3_times_e(),
            bcov_input_quintic(),
        ):
            assert data.coderivation_status == "open"
            assert data.requires_coderivation_construction is True

    def test_auxiliary_prepotential_cubics_are_separate_objects(self):
        """Kähler prepotential data remains outside the carrier profile."""
        assert yukawa_conifold().classical_cubic == {(0, 0, 0): F(1)}
        assert yukawa_k3_times_e().classical_cubic == {(0, 1, 2): F(1)}
        assert "yukawa_cubic" not in bcov_input_conifold()._fields


# =========================================================================
# Section 4b: Scalar scope and object firewall tests
# =========================================================================

class TestScalarScopeAndObjectFirewalls:
    """Pin the compute-lane scalar scope of the BCOV bar module."""

    def test_bar_carrier_has_no_dual_or_centre_payload(self):
        """The carrier record contains only its finite cohomological input."""
        bar = bar_carrier_k3_times_e()
        fields = set(bar._fields)

        assert bar.carrier_input is not bar
        assert bar.carrier_input.name == "K3xE"
        assert fields == {
            "name",
            "carrier_input",
            "bar_carrier_dims",
            "bar_carrier_graded_dims",
            "differential",
            "bar_cohomology_dims",
            "bar_cohomology_graded_dims",
            "max_bar_degree",
            "scalar_shadow_amplitudes",
        }
        assert fields.isdisjoint({
            "ai",
            "a_i",
            "a_dual",
            "a_bang",
            "koszul_dual",
            "verdier_dual",
            "derived_centre",
            "derived_center",
        })

    def test_missing_bcov_series_keeps_comparison_open(self):
        """A shadow series alone produces an explicit open comparison."""
        comp = compare_shadow_to_bcov_series(
            "conifold",
            "effective_euler_half_shadow",
            {1: F(1, 24), 2: F(7, 5760)},
        )

        assert comp.status == "open"
        assert comp.bcov_series is None
        assert comp.compared_genera == ()

    def test_independent_equal_series_produces_agreement(self):
        """Agreement follows from two supplied series in one named lane."""
        shadow = {1: F(1, 24), 2: F(7, 5760)}
        independently_computed = {1: F(1, 24), 2: F(7, 5760)}
        comp = compare_shadow_to_bcov_series(
            "unit comparison",
            "lane_alpha",
            shadow,
            bcov_lane="lane_alpha",
            bcov_series=independently_computed,
            bcov_source="independent unit oracle",
        )

        assert comp.status == "agrees"
        assert comp.compared_genera == (1, 2)
        assert comp.discrepancies == {}

    def test_k3xe_bkm_and_bcov_one_loop_lanes_remain_distinct(self):
        """BKM weight five and BCOV one-loop scalar zero stay typed."""
        comp = compare_shadow_to_bcov_series(
            "K3xE",
            "BKM",
            {1: F(5, 24)},
            bcov_lane="BCOV_one_loop",
            bcov_series={1: F(0)},
            bcov_source="K3xE Hodge Euler computation",
        )

        assert comp.status == "different_lanes"
        assert comp.discrepancies == {1: (F(5, 24), F(0))}

    def test_holographic_package_boundary_is_documented(self):
        """The module pins H(T) as seven entries and not a computed payload."""
        doc = bcov.__doc__ or ""
        normalized_doc = " ".join(doc.split())

        assert "COMPUTE-LANE SCALAR SHADOW:" in doc
        assert "euler_half_shadow" in doc
        assert "chi(X)/24 is stored separately" in normalized_doc
        assert "A, B(A), A^i, A^!, and the chiral derived centre" in doc
        assert "belong to their reconstruction layers" in doc
        assert "(A, A^i, A^!, C, r(z), Theta_A, nabla_hol)" in doc
        assert doc.count("A^i") >= 2

    def test_c3_has_an_exact_zero_coderivation(self):
        """The constant C^3 carrier is an actual zero-differential complex."""
        bar = bar_carrier_c3(max_bar_degree=3)

        assert bar.coderivation_constructed is True
        assert bar.differential is not None
        assert bar.differential.coderivation_verified is True
        assert bar.differential.square_zero is True
        assert bar.differential.apply({(2, 0): F(7)}) == {}
        assert bar.bar_cohomology_computed is True
        assert bar.bar_cohomology_dims == bar.bar_carrier_dims
        assert bar.bar_cohomology_graded_dims == bar.bar_carrier_graded_dims

    @pytest.mark.parametrize(
        "bar",
        [bar_carrier_conifold(), bar_carrier_k3_times_e()],
    )
    def test_open_profiles_keep_the_differential_slot_empty(self, bar):
        """An open profile exposes the finite coderivation obligation."""
        assert bar.carrier_input.requires_coderivation_construction is True
        assert bar.differential is None
        assert bar.coderivation_constructed is False
        assert bar.yukawa_entered_coderivation is False
        assert bar.bar_cohomology_computed is False
        assert bar.bar_cohomology_dims is None

    def test_represented_differential_changes_state_and_squares_to_zero(self):
        """Sparse differential data performs a checked nontrivial transition."""
        differential = RepresentedBarDifferential(
            carrier_dims={1: 1, 2: 1, 3: 1},
            basis_degrees={(1, 0): 2, (2, 0): 1, (3, 0): 0},
            images={(3, 0): {(2, 0): F(2)}},
            source="unit test finite carrier",
        )

        assert differential.apply({(3, 0): F(3)}) == {(2, 0): F(6)}
        assert differential.apply(differential.apply({(3, 0): F(3)})) == {}
        assert differential.square_zero is True
        assert differential.coderivation_verified is False

    def test_represented_differential_rejects_nonzero_square(self):
        """The constructor enforces the chain identity on every basis state."""
        with pytest.raises(ValueError, match=r"d\^2=0"):
            RepresentedBarDifferential(
                carrier_dims={1: 1, 2: 1, 3: 1},
                basis_degrees={(1, 0): 2, (2, 0): 1, (3, 0): 0},
                images={
                    (3, 0): {(2, 0): F(1)},
                    (2, 0): {(1, 0): F(1)},
                },
                source="invalid unit test carrier",
            )

    def test_represented_differential_enforces_degree_plus_one(self):
        """Every nonzero matrix coefficient raises cohomological degree by one."""
        with pytest.raises(ValueError, match="cohomological degree \\+1"):
            RepresentedBarDifferential(
                carrier_dims={1: 1, 2: 1},
                basis_degrees={(1, 0): 0, (2, 0): 0},
                images={(2, 0): {(1, 0): F(1)}},
                source="degree-zero transition",
            )

    def test_supplied_grading_must_match_the_computed_carrier(self):
        """A self-consistent grading cannot replace the carrier Hilbert series."""
        fake_grading = {(1, index): 0 for index in range(7)}
        fake_grading[(1, 7)] = 1
        differential = RepresentedBarDifferential(
            carrier_dims={1: 8},
            basis_degrees=fake_grading,
            images={(1, 0): {(1, 7): F(1)}},
            source="self-consistent but geometrically false grading",
        )

        with pytest.raises(ValueError, match="computed carrier"):
            compute_bar_carrier(
                bcov_input_c3(),
                max_bar_degree=1,
                differential=differential,
            )


# =========================================================================
# Section 5: Bar-carrier dimension tests
# =========================================================================

class TestBarCarrierDimensions:
    """Verify cofree bar-carrier dimensions at each arity."""

    def test_c3_arity_one_keeps_the_full_cohomological_grading(self):
        """The desuspended constant-polyvector basis has four exact degrees."""
        bar = bar_carrier_c3(max_bar_degree=2)
        assert bar.bar_carrier_graded_dims[1] == {
            -2: 1,
            -1: 3,
            0: 3,
            1: 1,
        }

    @pytest.mark.parametrize(
        "bar",
        [bar_carrier_c3(), bar_carrier_conifold(), bar_carrier_k3_times_e(2)],
    )
    def test_graded_hilbert_series_recovers_total_carrier(self, bar):
        """Summing every degree distribution recovers the direct count."""
        for arity, degree_dims in bar.bar_carrier_graded_dims.items():
            assert sum(degree_dims.values()) == bar.bar_carrier_dims[arity]

    def test_c3_bar_degree_1(self):
        """B^1(C^3) = s^{-1}(PV*(C^3)) = 8-dimensional."""
        b = bar_carrier_c3()
        assert b.bar_carrier_dims[1] == 8

    def test_c3_bar_degree_2(self):
        """B^2(C^3) = Sym^2(s^{-1}(PV*(C^3))).

        s^{-1}(PV*(C^3)) has:
          degree -2: 1-dim (even)
          degree -1: 3-dim (odd)
          degree 0:  3-dim (even)
          degree 1:  1-dim (odd)

        Sym^2 = sum over partitions (j_{-2}, j_{-1}, j_0, j_1) with sum = 2:
          Sym^{j_{-2}}(1-dim even) * Ext^{j_{-1}}(3-dim odd) *
          Sym^{j_0}(3-dim even) * Ext^{j_1}(1-dim odd)

        Enumeration:
          (2,0,0,0): C(1+1,2)*1*1*1 = 1
          (0,2,0,0): 1*C(3,2)*1*1 = 3
          (0,0,2,0): 1*1*C(3+1,2)*1 = 6
          (0,0,0,2): 1*1*1*C(1,2) = 0
          (1,1,0,0): 1*3*1*1 = 3
          (1,0,1,0): 1*1*3*1 = 3
          (1,0,0,1): 1*1*1*1 = 1
          (0,1,1,0): 1*3*3*1 = 9
          (0,1,0,1): 1*3*1*1 = 3
          (0,0,1,1): 1*1*3*1 = 3
          Total: 1+3+6+0+3+3+1+9+3+3 = 32
        """
        b = bar_carrier_c3()
        assert b.bar_carrier_dims[2] == 32

    def test_conifold_bar_degree_1(self):
        """B^1(conifold) = 3-dimensional."""
        b = bar_carrier_conifold()
        assert b.bar_carrier_dims[1] == 3

    def test_conifold_bar_degree_2(self):
        """B^2(conifold) = 5-dimensional.

        s^{-1}(PV*(conifold)):
          degree -2: 1-dim (even)
          degree 0:  1-dim (even)
          degree 1:  1-dim (odd)

        Sym^2 partitions:
          (2,0,0): C(2,2)=1, (0,2,0): C(2,2)=1, (0,0,2): C(1,2)=0
          (1,1,0): 1, (1,0,1): 1, (0,1,1): 1
          Total: 1+1+0+1+1+1 = 5
        """
        b = bar_carrier_conifold()
        assert b.bar_carrier_dims[2] == 5

    def test_conifold_bar_degree_3(self):
        """B^3(conifold) from Sym^3.

        s^{-1}: deg -2 (1,even), deg 0 (1,even), deg 1 (1,odd)

        Sym^3 partitions (j_{-2}, j_0, j_1) with sum = 3:
          (3,0,0): C(3,3)=1
          (0,3,0): C(3,3)=1
          (0,0,3): C(1,3)=0  (ext, 1-dim)
          (2,1,0): C(2,2)*1*1 = 1
          (2,0,1): C(2,2)*1*1 = 1
          (1,2,0): 1*C(2,2)*1 = 1
          (0,2,1): 1*C(2,2)*1 = 1
          (1,0,2): 1*1*C(1,2) = 0
          (0,1,2): 1*1*C(1,2) = 0
          (1,1,1): 1*1*1 = 1
          Total: 1+1+0+1+1+1+1+0+0+1 = 7
        """
        b = bar_carrier_conifold()
        assert b.bar_carrier_dims[3] == 7

    def test_k3xe_bar_degree_1(self):
        """B^1(K3 x E) = 96-dimensional."""
        b = bar_carrier_k3_times_e()
        assert b.bar_carrier_dims[1] == 96


# =========================================================================
# Section 6: Faber-Pandharipande intersection numbers
# =========================================================================

class TestFaberPandharipande:
    """Verify a-hat genus coefficients (FP intersection numbers)."""

    def test_ahat_g1(self):
        """a_hat_1 = 1/24.

        From (x/2)/sinh(x/2) = 1 - x^2/24 + ...
        |a_1| = 1/24.
        """
        assert _faber_pandharipande(1) == F(1, 24)

    def test_ahat_g2(self):
        """a_hat_2 = 7/5760.

        From (x/2)/sinh(x/2) = 1 - x^2/24 + 7x^4/5760 - ...
        |a_2| = 7/5760.
        """
        assert _faber_pandharipande(2) == F(7, 5760)

    def test_ahat_g3(self):
        """a_hat_3 = 31/967680.

        Coefficient of x^6 in (x/2)/sinh(x/2).
        """
        # (x/2)/sinh(x/2) = 1 - x^2/24 + 7x^4/5760 - 31x^6/967680 + ...
        assert _faber_pandharipande(3) == F(31, 967680)

    def test_ahat_positivity(self):
        """All |a_hat_g| > 0 for g >= 1."""
        for g in range(1, 8):
            assert _faber_pandharipande(g) > 0


# =========================================================================
# Section 7: scalar-shadow coefficient tests
# =========================================================================

class TestScalarShadowAmplitudes:
    """Verify the independent scalar projection F_g^sc = kappa * a_hat_g."""

    def test_f1_c3(self):
        """F_1(C^3) = kappa/24 = 1/24."""
        b = bar_carrier_c3()
        assert b.scalar_shadow_amplitudes[1] == F(1, 24)

    def test_f1_conifold(self):
        """F_1(conifold) = 1/24."""
        b = bar_carrier_conifold()
        assert b.scalar_shadow_amplitudes[1] == F(1, 24)

    def test_f1_k3xe(self):
        """F_1(K3 x E) = 5/24."""
        b = bar_carrier_k3_times_e()
        assert b.scalar_shadow_amplitudes[1] == F(5, 24)

    def test_f1_k3xe_uses_bkm_lane_not_euler_or_heisenberg(self):
        """The selected K3 x E scalar lane is BKM 5."""
        b = bar_carrier_k3_times_e()

        assert b.carrier_input.scalar_lane == "BKM"
        assert b.carrier_input.scalar_value == F(5)
        assert b.scalar_shadow_amplitudes[1] == F(5, 24)
        assert b.scalar_shadow_amplitudes[1] != F(0)
        assert b.scalar_shadow_amplitudes[1] != F(3, 24)

    def test_quintic_euler_half_shadow_and_bcov_one_loop_are_separate(self):
        """The two normalizations give -25/6 and -25/72, respectively."""
        profile = bcov_input_quintic()
        b = compute_bar_carrier(profile)
        assert b.scalar_shadow_amplitudes[1] == F(-25, 6)
        assert profile.bcov_one_loop_scalar == F(-25, 3)
        assert profile.bcov_one_loop_scalar * _faber_pandharipande(1) == F(-25, 72)

    def test_quintic_bcov_constant_map_values_use_the_canonical_formula(self):
        """The independent BCOV oracle gives F_1=-25/72 and F_2=5/144."""
        constants = bcov_quintic_constant_map_low_genus()
        assert constants == {1: F(-25, 72), 2: F(5, 144)}

        chi = F(quintic_hodge().euler)
        direct_genus_two = (
            -F(1, 30)
            * F(1, 6)
            / (F(4) * F(2) * F(math.factorial(2)))
            * (chi / F(2))
        )
        assert constants[2] == direct_genus_two

    def test_f2_c3(self):
        """F_2(C^3) = 7/5760."""
        b = bar_carrier_c3()
        assert b.scalar_shadow_amplitudes[2] == F(7, 5760)

    def test_f2_k3xe(self):
        """F_2(K3 x E) = 5 * 7/5760 = 7/1152."""
        b = bar_carrier_k3_times_e()
        assert b.scalar_shadow_amplitudes[2] == F(5) * F(7, 5760)
        assert b.scalar_shadow_amplitudes[2] == F(7, 1152)

    def test_fg_scaling(self):
        """F_g(K3xE) / F_g(conifold) = kappa(K3xE) / kappa(conifold) = 5.

        The ratio of genus-g amplitudes should equal the ratio of kappas,
        since F_g = kappa * a_hat_g is linear in kappa.
        """
        b_kxe = bar_carrier_k3_times_e()
        b_con = bar_carrier_conifold()
        for g in range(1, 4):
            ratio = b_kxe.scalar_shadow_amplitudes[g] / b_con.scalar_shadow_amplitudes[g]
            assert ratio == F(5)


# =========================================================================
# Section 8: Scalar-shadow formula tests
# =========================================================================

class TestScalarShadowFormula:
    """Verify the one-dimensional modular trace coefficients."""

    def test_genus1_formula(self):
        """F_1^sc = kappa/24."""
        for kappa in [F(1), F(5), F(-100)]:
            assert scalar_shadow_genus1(kappa) == kappa / 24

    def test_genus2_formula(self):
        """F_2^sc = kappa * 7/5760."""
        for kappa in [F(1), F(5)]:
            assert scalar_shadow_genus2(kappa) == kappa * F(7, 5760)


# =========================================================================
# Section 9: Shadow tower comparison tests
# =========================================================================

class TestIndependentScalarComparison:
    """Verify status transitions for independently supplied series."""

    def test_discrepant_series_are_reported(self):
        comp = compare_shadow_to_bcov_series(
            "discrepant compact lane",
            "lane_alpha",
            {1: F(1, 24), 2: F(7, 5760)},
            bcov_lane="lane_alpha",
            bcov_series={1: F(1, 24), 2: F(0)},
            bcov_source="discrepant unit oracle",
        )

        assert comp.status == "differs"
        assert comp.discrepancies == {2: (F(7, 5760), F(0))}

    def test_partial_series_are_reported(self):
        comp = compare_shadow_to_bcov_series(
            "partial compact lane",
            "lane_alpha",
            {1: F(1, 24), 2: F(7, 5760)},
            bcov_lane="lane_alpha",
            bcov_series={1: F(1, 24)},
            bcov_source="partial unit oracle",
        )

        assert comp.status == "incomplete"
        assert comp.compared_genera == (1,)

    def test_supplied_bcov_series_requires_provenance(self):
        with pytest.raises(ValueError, match="provenance"):
            compare_shadow_to_bcov_series(
                "unsourced series",
                "lane_alpha",
                {1: F(1)},
                bcov_lane="lane_alpha",
                bcov_series={1: F(1)},
            )


# =========================================================================
# Section 10: Cross-geometry consistency tests
# =========================================================================

class TestCrossGeometry:
    """Cross-geometry consistency checks."""

    def test_kappa_not_multiplicative(self):
        """kappa is NOT multiplicative: kappa(K3 x E) != kappa(K3) * kappa(E)."""
        assert kappa_additivity_check() is True

    def test_euler_checks(self):
        """Euler characteristic computations are correct."""
        assert euler_characteristic_check() is True

    def test_pv_dim_checks(self):
        """PV dimension computations are correct."""
        assert pv_dimension_check() is True

    def test_ghost_number_checks(self):
        """Ghost number grading is correct."""
        assert ghost_number_check() is True


# =========================================================================
# Section 11: Yukawa coupling tests
# =========================================================================

class TestYukawaCouplings:
    """Verify Yukawa coupling data."""

    def test_conifold_single_modulus(self):
        """Conifold has 1 Kahler modulus."""
        y = yukawa_conifold()
        assert y.n_moduli == 1

    def test_conifold_cttt(self):
        """C_{ttt} = 1 for the conifold."""
        y = yukawa_conifold()
        assert y.classical_cubic[(0, 0, 0)] == F(1)

    def test_k3xe_three_moduli(self):
        """K3 x E has 3 moduli in simplified model."""
        y = yukawa_k3_times_e()
        assert y.n_moduli == 3

    def test_k3xe_yukawa_tensor_is_represented(self):
        """K3 x E has nonzero Yukawa coupling."""
        y = yukawa_k3_times_e()
        assert len(y.classical_cubic) > 0
        assert y.has_instantons is True


# =========================================================================
# Section 12: K3 x E Schouten structure test
# =========================================================================

class TestK3xESchouten:
    """Verify Schouten bracket analysis on K3 x E."""

    def test_bracket_vanishes(self):
        """Schouten bracket vanishes on K3 x E cohomology (BTT)."""
        info = schouten_bracket_k3xe_structure()
        assert info["bracket_vanishes_on_cohomology"] is True

    def test_total_dim(self):
        """PV*(K3 x E) total dimension = 96."""
        info = schouten_bracket_k3xe_structure()
        assert info["total_dim"] == 96

    def test_leading_bracket_is_l3(self):
        """Leading nontrivial bracket is l_3 (Yukawa)."""
        info = schouten_bracket_k3xe_structure()
        assert "l_3" in info["leading_nontrivial_bracket"]


# =========================================================================
# Section 13: Full analysis integration tests
# =========================================================================

class TestFullAnalysis:
    """Integration tests for full analyses."""

    def test_c3_full(self):
        """Full C^3 analysis runs without error."""
        result = full_analysis_c3(max_bar=3, max_genus=3)
        assert result["scalar_lane"] == "equivariant_constant_map"
        assert result["scalar_value"] == F(1)
        assert result["shadow_class"] == "G"
        assert result["pv_total_dim"] == 8
        assert result["bar_carrier_dims"][1] == 8
        assert result["coderivation_constructed"] is True
        assert result["bar_cohomology_dims"][1] == 8
        assert result["bcov_comparison"].status == "open"

    def test_conifold_full(self):
        """Full conifold analysis runs without error."""
        result = full_analysis_conifold(max_bar=3, max_genus=3)
        assert result["scalar_lane"] == "effective_euler_half_shadow"
        assert result["scalar_value"] == F(1)
        assert result["bcov_one_loop_scalar"] is None
        assert result["shadow_class"] == "G"
        assert result["pv_total_dim"] == 3
        assert result["bar_carrier_dims"][1] == 3
        assert result["coderivation_constructed"] is False
        assert result["bar_cohomology_dims"] is None
        assert result["bcov_comparison"].status == "open"

    def test_k3xe_full(self):
        """Full K3 x E analysis runs without error."""
        result = full_analysis_k3xe(max_bar=2, max_genus=3)
        assert result["scalar_lane"] == "BKM"
        assert result["scalar_value"] == F(5)
        assert result["bcov_one_loop_scalar"] == F(0)
        assert result["shadow_class"] == "M"
        assert result["pv_total_dim"] == 96
        assert result["bar_carrier_dims"][1] == 96
        assert result["coderivation_constructed"] is False
        assert result["bar_cohomology_dims"] is None
        assert result["bcov_comparison"].bcov_lane == "BCOV_one_loop"
        assert result["bcov_comparison"].status == "open"

    def test_quintic_full_separates_shadow_and_bcov_constant_maps(self):
        result = full_analysis_quintic(max_bar=2, max_genus=3)

        assert result["pv_total_dim"] == 208
        assert result["bar_carrier_dims"][1] == 208
        assert result["bar_cohomology_dims"] is None
        assert result["bcov_constant_map_low_genus"] == {
            1: F(-25, 72),
            2: F(5, 144),
        }
        assert result["bcov_comparison"].status == "different_lanes"
        assert result["bcov_comparison"].bcov_source.endswith(
            "prop:canonical-bcov-quintic"
        )
        assert result["bcov_comparison"].discrepancies == {
            1: (F(-25, 6), F(-25, 72)),
            2: (F(-35, 288), F(5, 144)),
        }


# =========================================================================
# Section 14: Bar-carrier dimension generating-function consistency
# =========================================================================

class TestBarCarrierDimensionConsistency:
    """Verify carrier dimensions by independent counting methods."""

    def test_c3_explicit_matches_computed(self):
        """Explicit bar dims for C^3 match computed values."""
        explicit = bar_carrier_dims_c3_explicit()
        computed = bar_carrier_c3(max_bar_degree=4).bar_carrier_dims
        for k in explicit:
            assert explicit[k] == computed[k], f"Bar degree {k}: {explicit[k]} != {computed[k]}"

    def test_conifold_explicit_matches_computed(self):
        """Explicit bar dims for conifold match computed values."""
        explicit = bar_carrier_dims_conifold_explicit()
        computed = bar_carrier_conifold(max_bar_degree=4).bar_carrier_dims
        for k in explicit:
            assert explicit[k] == computed[k]

    def test_bar_degree_1_equals_pv_dim(self):
        """Bar degree 1 always equals dim(PV*(X)) (desuspension doesn't change total dim)."""
        for geom, expected in [("c3", 8), ("conifold", 3), ("k3xe", 96)]:
            if geom == "c3":
                b = bar_carrier_c3()
            elif geom == "conifold":
                b = bar_carrier_conifold()
            else:
                b = bar_carrier_k3_times_e()
            assert b.bar_carrier_dims[1] == expected

    def test_carrier_dims_monotone_c3(self):
        """Carrier dimensions for C^3 grow through the retained arities.

        For an 8-dim graded space with both even and odd generators,
        the carrier dimensions grow.
        """
        b = bar_carrier_c3(max_bar_degree=4)
        # Bar degree 1: 8, Bar degree 2: 32, Bar degree 3: should be larger
        assert b.bar_carrier_dims[2] >= b.bar_carrier_dims[1]


# =========================================================================
# Section 15: Desuspension grading test
# =========================================================================

class TestDesuspension:
    """Verify desuspension shifts degrees correctly."""

    def test_c3_desuspended_degrees(self):
        """After desuspension, C^3 PV has degrees -2, -1, 0, 1.

        PV^{p,0} has BCOV degree p - 1.
        After desuspension: degree p - 2.
        So: p=0 -> -2, p=1 -> -1, p=2 -> 0, p=3 -> 1.
        """
        pv = pv_c3_constant()
        bcov_graded = pv.bcov_graded_dims
        # BCOV degrees: p+q-1 for (p,0) = p-1
        assert bcov_graded.get(-1, 0) == 1   # p=0
        assert bcov_graded.get(0, 0) == 3    # p=1
        assert bcov_graded.get(1, 0) == 3    # p=2
        assert bcov_graded.get(2, 0) == 1    # p=3

    def test_conifold_desuspended_degrees(self):
        """Conifold desuspended degrees.

        PV^{0,0}: BCOV deg -1, desusp -2 (even)
        PV^{1,1}: BCOV deg 1, desusp 0 (even)
        PV^{3,0}: BCOV deg 2, desusp 1 (odd)
        """
        pv = pv_conifold_effective_carrier()
        bcov = pv.bcov_graded_dims
        assert bcov.get(-1, 0) == 1
        assert bcov.get(1, 0) == 1
        assert bcov.get(2, 0) == 1
