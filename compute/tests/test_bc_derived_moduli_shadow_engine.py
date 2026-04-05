"""Tests for the derived moduli of shadow algebras engine.

Covers:
  1. Tangent complex dimensions (H^0, H^1, H^2) for all standard families
  2. Virtual dimension formula and Euler characteristic cross-check
  3. Kuranishi map vanishing by parity
  4. BV bracket structure and consistency
  5. BV Laplacian Delta^2 = 0
  6. Symplectic form from cyclic pairing
  7. Symplectic nondegeneracy
  8. (-1)-shifted symplectic structure
  9. Derived intersection degree (Theorem C)
  10. Cotangent complex amplitude
  11. Virtual count (vdim = 0 families)
  12. Shadow depth vs vdim correlation
  13. Koszul duality comparison (A vs A!)
  14. Complementarity sum kappa + kappa' (AP24)
  15. Cross-family consistency

CRITICAL PITFALLS TESTED:
  - AP1: kappa formula correctness per family
  - AP14: shadow depth != Koszulness
  - AP24: kappa + kappa' = 0 for KM/free; = 13 for Virasoro; = 250/3 for W_3
  - AP33: H_k^! = Sym^ch(V*) != H_{-k}
  - AP45: desuspension lowers degree
"""

import pytest
from fractions import Fraction

from compute.lib.bc_derived_moduli_shadow_engine import (
    # Family constructors
    FamilyParams,
    heisenberg_family,
    virasoro_family,
    affine_slN_family,
    betagamma_family,
    w3_family,
    lattice_family,
    STANDARD_FAMILIES,
    get_family,
    # Core functions
    mc_tangent_complex_dims,
    infinitesimal_automorphisms,
    deformation_space_dim,
    obstruction_space_dim,
    virtual_dimension,
    virtual_dimension_euler,
    kuranishi_map_vanishing,
    symplectic_form_on_mc,
    symplectic_nondegeneracy_check,
    bv_bracket,
    bv_laplacian_check,
    shifted_symplectic_form,
    derived_intersection_degree,
    cotangent_complex_amplitude,
    virtual_count,
    shadow_depth_vs_vdim,
    koszul_derived_comparison,
    # Auxiliary
    genus_g_free_energy,
    complementarity_genus_g,
    full_derived_moduli_package,
)


# ======================================================================
# Section 1: Family constructors and kappa values (AP1)
# ======================================================================

class TestFamilyConstructors:
    """Verify family parameter correctness (AP1)."""

    def test_heisenberg_kappa_k1(self):
        fam = heisenberg_family(Fraction(1))
        assert fam.kappa == Fraction(1)

    def test_heisenberg_kappa_k2(self):
        fam = heisenberg_family(Fraction(2))
        assert fam.kappa == Fraction(2)

    def test_heisenberg_kappa_dual(self):
        fam = heisenberg_family(Fraction(3))
        assert fam.kappa_dual == Fraction(-3)

    def test_heisenberg_complementarity_sum(self):
        """AP24: kappa + kappa' = 0 for Heisenberg."""
        fam = heisenberg_family(Fraction(5))
        assert fam.kappa + fam.kappa_dual == Fraction(0)

    def test_virasoro_kappa_c26(self):
        fam = virasoro_family(Fraction(26))
        assert fam.kappa == Fraction(13)

    def test_virasoro_kappa_c1(self):
        fam = virasoro_family(Fraction(1))
        assert fam.kappa == Fraction(1, 2)

    def test_virasoro_kappa_c13(self):
        """Self-dual point (AP8)."""
        fam = virasoro_family(Fraction(13))
        assert fam.kappa == Fraction(13, 2)
        assert fam.kappa_dual == Fraction(13, 2)

    def test_virasoro_complementarity_sum(self):
        """AP24: kappa + kappa' = 13 for Virasoro."""
        for c_val in [1, 2, 13, 26, 100]:
            fam = virasoro_family(Fraction(c_val))
            assert fam.kappa + fam.kappa_dual == Fraction(13), \
                f"Failed at c={c_val}: sum = {fam.kappa + fam.kappa_dual}"

    def test_affine_sl2_kappa_k1(self):
        """kappa = 3(k+2)/4 = 9/4 for sl_2 at k=1."""
        fam = affine_slN_family(2, Fraction(1))
        assert fam.kappa == Fraction(9, 4)

    def test_affine_sl2_kappa_k2(self):
        fam = affine_slN_family(2, Fraction(2))
        assert fam.kappa == Fraction(3)

    def test_affine_sl2_complementarity_sum(self):
        """AP24: kappa + kappa' = 0 for affine KM (FF antisymmetry)."""
        fam = affine_slN_family(2, Fraction(1))
        assert fam.kappa + fam.kappa_dual == Fraction(0)

    def test_affine_sl3_complementarity_sum(self):
        fam = affine_slN_family(3, Fraction(1))
        assert fam.kappa + fam.kappa_dual == Fraction(0)

    def test_w3_kappa_c2(self):
        """AP1: kappa(W_3) = 5c/6, NOT c/2."""
        fam = w3_family(Fraction(2))
        assert fam.kappa == Fraction(5, 3)

    def test_w3_complementarity_sum(self):
        """AP24: kappa + kappa' = 250/3 for W_3."""
        fam = w3_family(Fraction(2))
        assert fam.kappa + fam.kappa_dual == Fraction(250, 3)

    def test_betagamma_complementarity_sum(self):
        """AP24: kappa + kappa' = 0 for betagamma."""
        fam = betagamma_family(Fraction(-2))
        assert fam.kappa + fam.kappa_dual == Fraction(0)

    def test_lattice_kappa_rank24(self):
        """AP48: kappa = rank, NOT c/2 for lattice VOAs."""
        fam = lattice_family(24)
        assert fam.kappa == Fraction(24)

    def test_lattice_complementarity_sum(self):
        fam = lattice_family(24)
        assert fam.kappa + fam.kappa_dual == Fraction(0)

    def test_virasoro_S4(self):
        """Q^contact = 10/[c(5c+22)]."""
        fam = virasoro_family(Fraction(26))
        expected = Fraction(10) / (Fraction(26) * (Fraction(130) + Fraction(22)))
        assert fam.S4 == expected

    def test_shadow_classes(self):
        assert heisenberg_family().shadow_class == 'G'
        assert virasoro_family().shadow_class == 'M'
        assert affine_slN_family(2).shadow_class == 'L'
        assert betagamma_family().shadow_class == 'C'
        assert w3_family().shadow_class == 'M'


# ======================================================================
# Section 2: Tangent complex dimensions
# ======================================================================

class TestTangentComplex:
    """Test H^i of the MC tangent complex for standard families."""

    def test_virasoro_generic_h0(self):
        assert infinitesimal_automorphisms(Fraction(26)) == 0

    def test_virasoro_generic_h1(self):
        assert deformation_space_dim(Fraction(26)) == 1

    def test_virasoro_generic_h2(self):
        assert obstruction_space_dim(Fraction(26)) == 1

    def test_heisenberg_h0(self):
        assert infinitesimal_automorphisms(Fraction(1), "Heisenberg") == 0

    def test_heisenberg_h1(self):
        assert deformation_space_dim(Fraction(1), "Heisenberg") == 1

    def test_heisenberg_h2(self):
        assert obstruction_space_dim(Fraction(1), "Heisenberg") == 0

    def test_affine_sl2_h0(self):
        """dim H^0 = dim(sl_2) = 3 (adjoint action)."""
        assert infinitesimal_automorphisms(Fraction(1), "sl_2") == 3

    def test_affine_sl2_h1(self):
        assert deformation_space_dim(Fraction(1), "sl_2") == 1

    def test_affine_sl2_h2(self):
        assert obstruction_space_dim(Fraction(1), "sl_2") == 0

    def test_affine_sl3_h0(self):
        """dim H^0 = dim(sl_3) = 8."""
        assert infinitesimal_automorphisms(Fraction(1), "sl_3") == 8

    def test_betagamma_h0(self):
        """Ghost number symmetry: dim H^0 = 1."""
        assert infinitesimal_automorphisms(Fraction(-2), "betagamma") == 1

    def test_betagamma_h2(self):
        assert obstruction_space_dim(Fraction(-2), "betagamma") == 1

    def test_w3_h0(self):
        assert infinitesimal_automorphisms(Fraction(2), "W3") == 0

    def test_w3_h1(self):
        assert deformation_space_dim(Fraction(2), "W3") == 1

    def test_w3_h2(self):
        assert obstruction_space_dim(Fraction(2), "W3") == 1

    def test_negative_degrees_vanish(self):
        dims = mc_tangent_complex_dims(Fraction(26), degree_range=(-2, 3))
        assert dims[-2] == 0
        assert dims[-1] == 0
        assert dims[3] == 0

    def test_lattice_h0(self):
        """Lattice VOAs have rank-many translation symmetries."""
        dims = mc_tangent_complex_dims(Fraction(24), family_type="Lattice",
                                       degree_range=(0, 2))
        assert dims[0] == 24

    def test_lattice_h1_zero(self):
        """Lattice VOAs have discrete moduli (rigid)."""
        assert deformation_space_dim(Fraction(24), "Lattice") == 0


# ======================================================================
# Section 3: Virtual dimension
# ======================================================================

class TestVirtualDimension:
    """Test vdim = sum (-1)^i dim H^i."""

    def test_virasoro_vdim_zero(self):
        """Virasoro: vdim = 0 - 1 + 1 = 0."""
        assert virtual_dimension(Fraction(26)) == 0

    def test_virasoro_vdim_c1(self):
        assert virtual_dimension(Fraction(1)) == 0

    def test_heisenberg_vdim(self):
        """Heisenberg: vdim = 0 - 1 + 0 = -1."""
        assert virtual_dimension(Fraction(1), "Heisenberg") == -1

    def test_affine_sl2_vdim(self):
        """sl_2: vdim = 3 - 1 + 0 = 2."""
        assert virtual_dimension(Fraction(1), "sl_2") == 2

    def test_affine_sl3_vdim(self):
        """sl_3: vdim = 8 - 1 + 0 = 7."""
        assert virtual_dimension(Fraction(1), "sl_3") == 7

    def test_betagamma_vdim(self):
        """betagamma: vdim = 1 - 1 + 1 = 1."""
        assert virtual_dimension(Fraction(-2), "betagamma") == 1

    def test_w3_vdim(self):
        """W_3: vdim = 0 - 1 + 1 = 0."""
        assert virtual_dimension(Fraction(2), "W3") == 0

    def test_lattice_vdim(self):
        """Lattice rank 24: vdim = 24 - 0 + 0 = 24."""
        assert virtual_dimension(Fraction(24), "Lattice") == 24

    def test_vdim_euler_consistency(self):
        """Cross-check: vdim from Euler char matches direct computation."""
        for c_val, ftype in [(26, "Virasoro"), (1, "Heisenberg"),
                             (1, "sl_2"), (-2, "betagamma"),
                             (2, "W3")]:
            v1 = virtual_dimension(Fraction(c_val), ftype)
            v2 = virtual_dimension_euler(Fraction(c_val), ftype)
            assert v1 == v2, \
                f"Mismatch for {ftype} at c={c_val}: {v1} vs {v2}"


# ======================================================================
# Section 4: Kuranishi map vanishing
# ======================================================================

class TestKuranishi:
    """Test Kuranishi obstruction map vanishes by parity."""

    def test_virasoro_kuranishi_vanishes(self):
        result = kuranishi_map_vanishing(Fraction(26))
        assert result['vanishes'] is True

    def test_virasoro_kuranishi_mechanism(self):
        result = kuranishi_map_vanishing(Fraction(26))
        assert 'parity' in result['mechanism']

    def test_heisenberg_kuranishi_trivial(self):
        """H^2 = 0, so Kuranishi is trivially zero."""
        result = kuranishi_map_vanishing(Fraction(1), "Heisenberg")
        assert result['vanishes'] is True
        assert 'H^2 = 0' in result['mechanism']

    def test_affine_kuranishi_trivial(self):
        result = kuranishi_map_vanishing(Fraction(1), "sl_2")
        assert result['vanishes'] is True
        assert 'H^2 = 0' in result['mechanism']

    def test_w3_kuranishi_vanishes(self):
        result = kuranishi_map_vanishing(Fraction(2), "W3")
        assert result['vanishes'] is True

    def test_betagamma_kuranishi_vanishes(self):
        result = kuranishi_map_vanishing(Fraction(-2), "betagamma")
        assert result['vanishes'] is True

    def test_kuranishi_h1_h2_dims(self):
        result = kuranishi_map_vanishing(Fraction(26))
        assert result['h1_dim'] == 1
        assert result['h2_dim'] == 1


# ======================================================================
# Section 5: BV bracket
# ======================================================================

class TestBVBracket:
    """Test BV bracket structure on the MC moduli."""

    def test_bv_vacuum_central(self):
        """Vacuum is BV-central: {vac, anything} = 0."""
        for g in ["vac", "xi", "eta"]:
            result = bv_bracket(Fraction(26), "vac", g)
            assert result['vanishes'] is True

    def test_bv_xi_xi_parity(self):
        """{xi, xi} = 0 by graded antisymmetry."""
        result = bv_bracket(Fraction(26), "xi", "xi")
        assert result['vanishes'] is True

    def test_bv_xi_eta_nonzero(self):
        """{xi, eta} = kappa * vac, nonzero at generic c."""
        result = bv_bracket(Fraction(26), "xi", "eta")
        assert result['result'][0] == "vac"
        assert result['result'][1] == Fraction(13)

    def test_bv_xi_eta_c1(self):
        result = bv_bracket(Fraction(1), "xi", "eta")
        assert result['result'][1] == Fraction(1, 2)

    def test_bv_eta_eta_vanishes(self):
        """{eta, eta} = 0 (degree too high)."""
        result = bv_bracket(Fraction(26), "eta", "eta")
        assert result['vanishes'] is True

    def test_bv_xi_eta_at_c0_vanishes(self):
        """At c = 0: kappa = 0, so {xi, eta} = 0."""
        result = bv_bracket(Fraction(0), "xi", "eta")
        assert result['vanishes'] is True

    def test_bv_antisymmetry(self):
        """{xi, eta} = -{eta, xi} (graded antisymmetry)."""
        r1 = bv_bracket(Fraction(26), "xi", "eta")
        r2 = bv_bracket(Fraction(26), "eta", "xi")
        assert r1['result'][1] == -r2['result'][1]


# ======================================================================
# Section 6: BV Laplacian
# ======================================================================

class TestBVLaplacian:
    """Test Delta^2 = 0 for BV Laplacian."""

    def test_virasoro_delta_squared_zero(self):
        result = bv_laplacian_check(Fraction(26))
        assert result['delta_squared_zero'] is True

    def test_heisenberg_delta_squared_zero(self):
        result = bv_laplacian_check(Fraction(1), "Heisenberg")
        assert result['delta_squared_zero'] is True

    def test_affine_delta_squared_zero(self):
        result = bv_laplacian_check(Fraction(1), "sl_2")
        assert result['delta_squared_zero'] is True

    def test_w3_delta_squared_zero(self):
        result = bv_laplacian_check(Fraction(2), "W3")
        assert result['delta_squared_zero'] is True

    def test_betagamma_delta_squared_zero(self):
        result = bv_laplacian_check(Fraction(-2), "betagamma")
        assert result['delta_squared_zero'] is True

    def test_delta_squared_all_elements(self):
        """Every element satisfies Delta^2 = 0."""
        result = bv_laplacian_check(Fraction(26))
        for check in result['checks']:
            assert check['vanishes'] is True
            assert check['delta_squared'] == Fraction(0)


# ======================================================================
# Section 7: Symplectic form
# ======================================================================

class TestSymplecticForm:
    """Test the symplectic form from cyclic pairing."""

    def test_virasoro_symplectic_rank(self):
        result = symplectic_form_on_mc(Fraction(26))
        assert result['rank'] == 1

    def test_virasoro_symplectic_nondegenerate(self):
        result = symplectic_form_on_mc(Fraction(26))
        assert result['is_nondegenerate'] is True

    def test_virasoro_symplectic_kappa(self):
        result = symplectic_form_on_mc(Fraction(26))
        assert result['kappa_coefficient'] == Fraction(13)

    def test_heisenberg_symplectic(self):
        result = symplectic_form_on_mc(Fraction(1), "Heisenberg")
        assert result['is_nondegenerate'] is True
        assert result['kappa_coefficient'] == Fraction(1)

    def test_c0_symplectic_degenerate(self):
        """At c = 0: kappa = 0, symplectic form degenerates."""
        result = symplectic_form_on_mc(Fraction(0))
        assert result['is_nondegenerate'] is False
        assert result['rank'] == 0

    def test_self_dual_point_symplectic(self):
        """At c = 13 (self-dual): kappa = 13/2."""
        result = symplectic_form_on_mc(Fraction(13))
        assert result['kappa_coefficient'] == Fraction(13, 2)
        assert result['is_nondegenerate'] is True


# ======================================================================
# Section 8: Symplectic nondegeneracy
# ======================================================================

class TestSymplecticNondegeneracy:

    def test_virasoro_generic_nondegenerate(self):
        result = symplectic_nondegeneracy_check(Fraction(26))
        assert result['is_nondegenerate'] is True

    def test_virasoro_c0_degenerate(self):
        result = symplectic_nondegeneracy_check(Fraction(0))
        assert result['is_nondegenerate'] is False
        assert result['degeneration_locus'] == 'kappa = 0'

    def test_heisenberg_k0_degenerate(self):
        result = symplectic_nondegeneracy_check(Fraction(0), "Heisenberg")
        assert result['is_nondegenerate'] is False

    def test_affine_sl2_nondegenerate(self):
        result = symplectic_nondegeneracy_check(Fraction(1), "sl_2")
        assert result['is_nondegenerate'] is True


# ======================================================================
# Section 9: Shifted symplectic form
# ======================================================================

class TestShiftedSymplectic:
    """Test (-1)-shifted symplectic structure."""

    def test_shift_value(self):
        result = shifted_symplectic_form(Fraction(26))
        assert result['shift'] == -1

    def test_form_degree(self):
        """Total form degree = 2 + shift = 1."""
        result = shifted_symplectic_form(Fraction(26))
        assert result['form_degree'] == 1

    def test_virasoro_nondegenerate(self):
        result = shifted_symplectic_form(Fraction(26))
        assert result['is_nondegenerate'] is True

    def test_pairing_matrix_antisymmetry(self):
        """The shifted symplectic pairing is antisymmetric."""
        result = shifted_symplectic_form(Fraction(1), family_type="sl_2")
        M = result['pairing_matrix']
        n = len(M)
        for i in range(n):
            for j in range(n):
                assert M[i][j] == -M[j][i], \
                    f"Antisymmetry fails at ({i},{j}): {M[i][j]} vs {-M[j][i]}"

    def test_lagrangian_existence(self):
        """Lagrangians exist when total dim is even and form is nondegenerate."""
        result = shifted_symplectic_form(Fraction(26))
        # Virasoro: total dim = h0 + h1 + h2 = 0 + 1 + 1 = 2 (even)
        assert result['total_tangent_dim'] == 2
        assert result['lagrangian_exists'] is True

    def test_custom_shift(self):
        result = shifted_symplectic_form(Fraction(26), shift=-2)
        assert result['shift'] == -2
        assert result['form_degree'] == 0


# ======================================================================
# Section 10: Derived intersection degree
# ======================================================================

class TestDerivedIntersection:
    """Test L_A cap^L L_{A!} from Theorem C."""

    def test_virasoro_transverse(self):
        """Virasoro: kappa + kappa' = 13 != 0, transverse."""
        result = derived_intersection_degree(Fraction(26))
        assert result['is_transverse'] is True
        assert result['complementarity_sum'] == Fraction(13)

    def test_heisenberg_tangential(self):
        """Heisenberg: kappa + kappa' = 0, tangential."""
        result = derived_intersection_degree(Fraction(1), "Heisenberg")
        assert result['is_transverse'] is False
        assert result['complementarity_sum'] == Fraction(0)

    def test_affine_tangential(self):
        result = derived_intersection_degree(Fraction(1), "sl_2")
        assert result['is_transverse'] is False

    def test_genus_1_intersection_virasoro(self):
        """F_1(A) + F_1(A!) = 13/24 for Virasoro."""
        result = derived_intersection_degree(Fraction(26))
        assert result['genus_1_intersection'] == Fraction(13, 24)

    def test_genus_1_intersection_heisenberg(self):
        """F_1(A) + F_1(A!) = 0 for Heisenberg."""
        result = derived_intersection_degree(Fraction(1), "Heisenberg")
        assert result['genus_1_intersection'] == Fraction(0)

    def test_self_dual_transverse(self):
        """At c = 13 (self-dual): still transverse (sum = 13)."""
        result = derived_intersection_degree(Fraction(13))
        assert result['is_transverse'] is True


# ======================================================================
# Section 11: Cotangent complex amplitude
# ======================================================================

class TestCotangentComplex:

    def test_heisenberg_smooth(self):
        """Heisenberg at generic k: smooth scheme [0,0]."""
        result = cotangent_complex_amplitude(Fraction(1), "Heisenberg")
        assert result['is_smooth'] is True
        assert result['amplitude'] == (0, 0)

    def test_virasoro_derived(self):
        """Virasoro: has H^2 obstruction, so is derived."""
        result = cotangent_complex_amplitude(Fraction(26))
        assert result['is_derived'] is True
        assert result['amplitude'][0] == -1

    def test_affine_artin(self):
        """Affine sl_2: has automorphisms, is an Artin stack."""
        result = cotangent_complex_amplitude(Fraction(1), "sl_2")
        assert result['is_artin'] is True
        assert result['h_1'] == 3  # L^1 = T^{0*} = aut dual

    def test_cotangent_dual_tangent(self):
        """L^i = T^{1-i*}: verify the duality."""
        result = cotangent_complex_amplitude(Fraction(26))
        assert result['h_minus1'] == 1  # = dim H^2(T)
        assert result['h_0'] == 1       # = dim H^1(T)
        assert result['h_1'] == 0       # = dim H^0(T)


# ======================================================================
# Section 12: Virtual count
# ======================================================================

class TestVirtualCount:
    """Test [MC]^{vir} for vdim = 0 families."""

    def test_virasoro_vdim_zero(self):
        result = virtual_count(Fraction(26))
        assert result['is_zero_dimensional'] is True

    def test_virasoro_genus1_count(self):
        """F_1 = kappa * lambda_1 = 13 * 1/24 = 13/24."""
        result = virtual_count(Fraction(26))
        assert result['virtual_counts'][1] == Fraction(13, 24)

    def test_virasoro_genus2_count(self):
        """F_2 = kappa * lambda_2 = 13 * 7/5760."""
        result = virtual_count(Fraction(26))
        expected = Fraction(13) * Fraction(7, 5760)
        assert result['virtual_counts'][2] == expected

    def test_heisenberg_not_zero_dim(self):
        """Heisenberg: vdim = -1, no virtual count."""
        result = virtual_count(Fraction(1), "Heisenberg")
        assert result['is_zero_dimensional'] is False
        assert result['virtual_counts'] is None

    def test_w3_vdim_zero(self):
        result = virtual_count(Fraction(2), "W3")
        assert result['is_zero_dimensional'] is True

    def test_w3_genus1_count(self):
        """F_1(W_3) = kappa * lambda_1 = 5c/6 * 1/24 = 5*2/(6*24) = 5/72."""
        result = virtual_count(Fraction(2), "W3")
        expected = Fraction(5, 3) * Fraction(1, 24)
        assert result['virtual_counts'][1] == expected


# ======================================================================
# Section 13: Shadow depth vs vdim
# ======================================================================

class TestShadowDepthVsVdim:
    """Shadow depth is INDEPENDENT of virtual dimension (AP14)."""

    def test_all_families_present(self):
        result = shadow_depth_vs_vdim()
        assert len(result) == len(STANDARD_FAMILIES)

    def test_class_g_various_vdim(self):
        """Class G families can have different vdim."""
        result = shadow_depth_vs_vdim()
        # Heisenberg: vdim = -1
        assert result['Heisenberg']['vdim'] == -1
        assert result['Heisenberg']['shadow_class'] == 'G'
        # Lattice: vdim = 24
        assert result['Lattice_24']['vdim'] == 24
        assert result['Lattice_24']['shadow_class'] == 'G'

    def test_class_m_vdim_zero(self):
        """Class M (Virasoro, W_3): vdim = 0."""
        result = shadow_depth_vs_vdim()
        assert result['Virasoro_c26']['vdim'] == 0
        assert result['W3_c2']['vdim'] == 0

    def test_depth_does_not_determine_vdim(self):
        """AP14: shadow depth and vdim are independent invariants."""
        result = shadow_depth_vs_vdim()
        # Depth 2 (G): vdim varies (-1, 24, ...)
        # Depth inf (M): vdim = 0
        # These are different, confirming independence.
        g_vdims = {v['vdim'] for k, v in result.items()
                   if v['shadow_class'] == 'G'}
        assert len(g_vdims) >= 2, "Class G should have varying vdims"


# ======================================================================
# Section 14: Koszul derived comparison
# ======================================================================

class TestKoszulComparison:
    """Compare derived moduli of A vs A!."""

    def test_virasoro_dual_central_charge(self):
        result = koszul_derived_comparison(Fraction(26))
        assert result['c_A'] == Fraction(26)
        assert result['c_A_dual'] == Fraction(0)

    def test_virasoro_kappa_sum(self):
        result = koszul_derived_comparison(Fraction(26))
        assert result['complementarity_sum'] == Fraction(13)

    def test_heisenberg_kappa_sum(self):
        result = koszul_derived_comparison(Fraction(1), "Heisenberg")
        assert result['complementarity_sum'] == Fraction(0)

    def test_f1_additivity(self):
        """F_1(A) + F_1(A!) = (kappa + kappa') * lambda_1."""
        result = koszul_derived_comparison(Fraction(26))
        assert result['F1_sum'] == result['F1_sum_expected']

    def test_f1_additivity_heisenberg(self):
        result = koszul_derived_comparison(Fraction(1), "Heisenberg")
        assert result['F1_sum'] == result['F1_sum_expected']

    def test_virasoro_same_vdim(self):
        """Vir_c and Vir_{26-c} have the same vdim."""
        result = koszul_derived_comparison(Fraction(1))
        assert result['vdim_A'] == result['vdim_A_dual']

    def test_self_dual_comparison(self):
        """At c = 13: A = A!, kappa = kappa' = 13/2."""
        result = koszul_derived_comparison(Fraction(13))
        assert result['kappa_A'] == result['kappa_A_dual']
        assert result['vdim_difference'] == 0


# ======================================================================
# Section 15: Cross-family consistency
# ======================================================================

class TestCrossFamily:
    """Cross-family consistency checks (AP10: not just hardcoded values)."""

    def test_complementarity_sum_ap24_virasoro_parametric(self):
        """AP24: kappa + kappa' = 13 for ALL values of c."""
        for c_val in range(1, 50):
            fam = virasoro_family(Fraction(c_val))
            s = fam.kappa + fam.kappa_dual
            assert s == Fraction(13), f"c={c_val}: sum={s}"

    def test_complementarity_sum_ap24_affine_parametric(self):
        """AP24: kappa + kappa' = 0 for affine KM at all levels."""
        for N in [2, 3, 4]:
            for k_val in [1, 2, 3, 5]:
                fam = affine_slN_family(N, Fraction(k_val))
                s = fam.kappa + fam.kappa_dual
                assert s == Fraction(0), f"sl_{N} k={k_val}: sum={s}"

    def test_vdim_euler_all_families(self):
        """vdim from direct formula matches Euler characteristic for all families."""
        cases = [
            (Fraction(1), "Virasoro"),
            (Fraction(13), "Virasoro"),
            (Fraction(26), "Virasoro"),
            (Fraction(1), "Heisenberg"),
            (Fraction(2), "Heisenberg"),
            (Fraction(1), "sl_2"),
            (Fraction(1), "sl_3"),
            (Fraction(-2), "betagamma"),
            (Fraction(2), "W3"),
        ]
        for c_val, ftype in cases:
            v1 = virtual_dimension(c_val, ftype)
            v2 = virtual_dimension_euler(c_val, ftype)
            assert v1 == v2, f"{ftype}(c={c_val}): {v1} vs {v2}"

    def test_genus_g_additivity(self):
        """F_g(A) + F_g(A!) = (kappa + kappa') * lambda_g."""
        fam = virasoro_family(Fraction(10))
        for g in range(1, 5):
            total = complementarity_genus_g(fam, g)
            expected = Fraction(13) * Fraction(
                int(Fraction(2**(2*g-1)-1, 2**(2*g-1)).numerator),
                int(Fraction(2**(2*g-1)-1, 2**(2*g-1)).denominator)
            )
            # Simpler: just check directly
            from compute.lib.bc_derived_moduli_shadow_engine import _lambda_fp
            assert total == Fraction(13) * _lambda_fp(g)

    def test_kuranishi_vanishes_all_families(self):
        """Kuranishi map vanishes for ALL standard families."""
        cases = [
            (Fraction(26), "Virasoro"),
            (Fraction(1), "Heisenberg"),
            (Fraction(1), "sl_2"),
            (Fraction(-2), "betagamma"),
            (Fraction(2), "W3"),
        ]
        for c_val, ftype in cases:
            result = kuranishi_map_vanishing(c_val, ftype)
            assert result['vanishes'] is True, f"{ftype}(c={c_val})"

    def test_bv_delta_squared_all_families(self):
        """Delta^2 = 0 for ALL standard families."""
        cases = [
            (Fraction(26), "Virasoro"),
            (Fraction(1), "Heisenberg"),
            (Fraction(1), "sl_2"),
            (Fraction(-2), "betagamma"),
            (Fraction(2), "W3"),
        ]
        for c_val, ftype in cases:
            result = bv_laplacian_check(c_val, ftype)
            assert result['delta_squared_zero'] is True, f"{ftype}(c={c_val})"


# ======================================================================
# Section 16: Full package integration
# ======================================================================

class TestFullPackage:
    """Test the full_derived_moduli_package master function."""

    def test_virasoro_package_keys(self):
        pkg = full_derived_moduli_package(Fraction(26))
        expected_keys = {
            'tangent_complex', 'automorphisms', 'deformations',
            'obstructions', 'virtual_dimension', 'virtual_dimension_euler',
            'kuranishi', 'symplectic', 'symplectic_nondeg',
            'bv_laplacian', 'shifted_symplectic', 'intersection',
            'cotangent', 'virtual_count', 'koszul_comparison',
        }
        assert set(pkg.keys()) == expected_keys

    def test_virasoro_package_consistency(self):
        """All components of the package are mutually consistent."""
        pkg = full_derived_moduli_package(Fraction(26))
        assert pkg['automorphisms'] == 0
        assert pkg['deformations'] == 1
        assert pkg['obstructions'] == 1
        assert pkg['virtual_dimension'] == 0
        assert pkg['virtual_dimension'] == pkg['virtual_dimension_euler']
        assert pkg['kuranishi']['vanishes'] is True
        assert pkg['symplectic']['is_nondegenerate'] is True
        assert pkg['bv_laplacian']['delta_squared_zero'] is True
        assert pkg['intersection']['complementarity_sum'] == Fraction(13)
        assert pkg['cotangent']['is_derived'] is True
        assert pkg['virtual_count']['is_zero_dimensional'] is True

    def test_heisenberg_package_consistency(self):
        pkg = full_derived_moduli_package(Fraction(1), "Heisenberg")
        assert pkg['automorphisms'] == 0
        assert pkg['deformations'] == 1
        assert pkg['obstructions'] == 0
        assert pkg['virtual_dimension'] == -1
        assert pkg['kuranishi']['vanishes'] is True
        assert pkg['intersection']['complementarity_sum'] == Fraction(0)
        assert pkg['cotangent']['is_smooth'] is True
