"""Tests for the modular tangent complex module.

Verifies:
  - CE complex C*(g, g) structure: dimensions, d^2 = 0
  - H*(sl_2, sl_2) = 0 (Whitehead rigidity)
  - H^2_cyc(sl_2, sl_2) = k (Killing 3-cocycle)
  - Nijenhuis-Richardson bracket properties
  - Killing cocycle: CE cocycle, nonzero 3-form
  - Killing bracket [eta, -] intertwining with d_CE
  - kappa-twisted differential: curvature proportional to kappa^2
  - d^2 = 0 at critical level k = -h^v
  - Obstruction o_4 = 0 for affine sl_2 (shadow terminates at r=3)
  - Shadow depth classification for standard families
  - Kappa formulas for standard families
  - Virasoro tangent H^1 = 1 (central charge deformation)
  - Heisenberg tangent: unobstructed, shadow depth 2
"""

import pytest
from fractions import Fraction
from math import comb

import numpy as np

from compute.lib.modular_tangent_complex import (
    CyclicDeformationComplex,
    KillingTwistedDifferential,
    _is_zero_matrix,
    _mat_multiply,
    _mat_add,
    _mat_scale,
    _np_zeros,
    _killing_bracket_matrix,
    killing_cocycle,
    killing_3form_value,
    kappa_affine_sl2,
    kappa_affine,
    kappa_heisenberg,
    kappa_virasoro,
    heisenberg_tangent,
    affine_sl2_tangent,
    virasoro_tangent,
    obstruction_class_affine_o4,
    shadow_depth_classification,
    sl2_deformation_complex,
    sl3_deformation_complex,
    verify_ce_d_squared_sl2,
    verify_sl2_rigidity,
    verify_sl2_killing_cocycle,
    verify_killing_bracket_d_intertwining_sl2,
    verify_kappa_twist_curvature_sl2,
    verify_affine_sl2_o4_vanishes,
)

from compute.lib.mc2_cyclic_ce import (
    sl2_structure_constants,
    sl2_killing_form,
    sl3_structure_constants,
    sl3_killing_form,
    ce_cohomology,
    cyclic_ce_cohomology,
    ce_differential_0,
    ce_differential_1,
    ce_differential_2,
    _exact_rank,
)


# ===================================================================
# sl_2 deformation complex: dimensions and structure
# ===================================================================

class TestSl2DeformationComplexDimensions:
    """Verify dimensions of C^n(sl_2, sl_2) = Hom(Lambda^n sl_2, sl_2)."""

    def setup_method(self):
        self.cx = sl2_deformation_complex()

    def test_c0_dim(self):
        """C^0 = sl_2 has dim 3."""
        assert self.cx.degree_dim(0) == 3

    def test_c1_dim(self):
        """C^1 = Hom(sl_2, sl_2) has dim 9."""
        assert self.cx.degree_dim(1) == 9

    def test_c2_dim(self):
        """C^2 = Hom(Lambda^2 sl_2, sl_2) has dim 9."""
        assert self.cx.degree_dim(2) == 9

    def test_c3_dim(self):
        """C^3 = Hom(Lambda^3 sl_2, sl_2) has dim 3."""
        assert self.cx.degree_dim(3) == 3

    def test_c4_dim_zero(self):
        """C^n = 0 for n >= 4 (since dim(sl_2) = 3)."""
        assert self.cx.degree_dim(4) == 0

    def test_negative_degree_zero(self):
        """C^n = 0 for n < 0."""
        assert self.cx.degree_dim(-1) == 0

    def test_euler_characteristic(self):
        """chi(C*(sl_2, sl_2)) = 3 - 9 + 9 - 3 = 0."""
        dims = [self.cx.degree_dim(n) for n in range(4)]
        assert dims == [3, 9, 9, 3]
        chi = sum((-1)**n * d for n, d in enumerate(dims))
        assert chi == 0

    def test_dimension_formula(self):
        """dim C^n(g,g) = dim(g) * C(dim(g), n)."""
        for n in range(5):
            expected = 3 * comb(3, n)
            assert self.cx.degree_dim(n) == expected


# ===================================================================
# CE differential d^2 = 0
# ===================================================================

class TestCEDifferentialSquaredZero:
    """Verify d^2 = 0 for the CE complex of sl_2 with adjoint coefficients."""

    def setup_method(self):
        self.cx = sl2_deformation_complex()

    def test_d0_d1_zero(self):
        """d^1 o d^0 = 0."""
        assert self.cx.verify_d_squared(0)

    def test_d1_d2_zero(self):
        """d^2 o d^1 = 0."""
        assert self.cx.verify_d_squared(1)

    def test_verify_entry_point(self):
        """Verify via the entry point function."""
        result = verify_ce_d_squared_sl2()
        assert result["d0_d1_zero"]
        assert result["d1_d2_zero"]


# ===================================================================
# Whitehead's theorem: H*(sl_2, sl_2) = 0
# ===================================================================

class TestWhiteheadRigidity:
    """sl_2 is rigid: all CE cohomology with adjoint coefficients vanishes."""

    def setup_method(self):
        self.cx = sl2_deformation_complex()
        self.h = self.cx.cohomology_dims()

    def test_h0_zero(self):
        """H^0(sl_2, sl_2) = center(sl_2) = 0."""
        assert self.h[0] == 0

    def test_h1_zero(self):
        """H^1(sl_2, sl_2) = outer derivations = 0."""
        assert self.h[1] == 0

    def test_h2_zero(self):
        """H^2(sl_2, sl_2) = 0 (no Lie algebra deformations)."""
        assert self.h[2] == 0

    def test_h3_zero(self):
        """H^3(sl_2, sl_2) = 0."""
        assert self.h[3] == 0

    def test_verify_entry_point(self):
        """Verify via the entry point function."""
        result = verify_sl2_rigidity()
        for key, val in result.items():
            assert val, f"Failed: {key}"


# ===================================================================
# Cyclic cohomology H*_cyc(sl_2, sl_2)
# ===================================================================

class TestCyclicCohomologySl2:
    """H^n_cyc(sl_2, sl_2) = H^{n+1}(sl_2) via Killing form."""

    def setup_method(self):
        self.cx = sl2_deformation_complex()
        self.cyc = self.cx.cyclic_cohomology()

    def test_h0_cyc_zero(self):
        """H^0_cyc = H^1(sl_2) = 0."""
        assert self.cyc["dims"][0] == 0

    def test_h1_cyc_zero(self):
        """H^1_cyc = H^2(sl_2) = 0."""
        assert self.cyc["dims"][1] == 0

    def test_h2_cyc_one(self):
        """H^2_cyc = H^3(sl_2) = k (Killing 3-cocycle generates)."""
        assert self.cyc["dims"][2] == 1

    def test_killing_3form_nonzero(self):
        """The Killing 3-form kap([e,f], h) is nonzero."""
        assert self.cyc["killing_3form_value"] != 0


# ===================================================================
# Killing cocycle properties
# ===================================================================

class TestKillingCocycle:
    """Properties of the Killing cocycle eta = [-,-] in C^2(g,g)."""

    def setup_method(self):
        self.sc = sl2_structure_constants()
        self.kap = sl2_killing_form()
        self.dim = 3
        self.eta = killing_cocycle(self.sc, self.kap, self.dim)

    def test_eta_nonzero(self):
        """The Killing cocycle is nonzero."""
        assert any(self.eta[i] != 0 for i in range(len(self.eta)))

    def test_eta_is_ce_cocycle(self):
        """d_CE(eta) = 0: the Killing cocycle is closed."""
        d2 = ce_differential_2(self.sc, self.dim)
        d_eta = _mat_multiply(d2, self.eta.reshape(-1, 1))
        assert _is_zero_matrix(d_eta)

    def test_killing_3form_value(self):
        """kap([e_0, e_1], e_2) = kap([e, h], f) = kap(-2e, f) = -2."""
        val = killing_3form_value(self.sc, self.kap, self.dim)
        # Basis: e_0=e, e_1=h, e_2=f. [e,h] = -2e. kap(-2e, f) = -2*kap(e,f) = -2.
        assert val == Fraction(-2)

    def test_eta_represents_bracket(self):
        """eta(e_a, e_b) = [e_a, e_b] for all a, b."""
        pairs = [(i, j) for i in range(3) for j in range(i + 1, 3)]
        n_pairs = len(pairs)
        for p_idx, (a, b) in enumerate(pairs):
            for m in range(3):
                eta_val = self.eta[m * n_pairs + p_idx]
                sc_val = Fraction(self.sc[a, b, m])
                assert eta_val == sc_val, \
                    f"eta(e_{a}, e_{b})[{m}] = {eta_val} != {sc_val}"

    def test_verify_entry_point(self):
        """Verify via the entry point function."""
        result = verify_sl2_killing_cocycle()
        assert result["killing_3form_nonzero"]
        assert result["eta_is_ce_cocycle"]


# ===================================================================
# Killing bracket [eta, -] on C*(g, g)
# ===================================================================

class TestKillingBracket:
    """[eta, -]_NR: C^n -> C^{n+1} for the Killing cocycle eta."""

    def setup_method(self):
        self.sc = sl2_structure_constants()
        self.kap = sl2_killing_form()
        self.dim = 3
        self.eta = killing_cocycle(self.sc, self.kap, self.dim)

    def test_bracket_c0_to_c1_shape(self):
        """[eta, -]: C^0 -> C^1 has shape (9, 3)."""
        mat = _killing_bracket_matrix(self.eta, self.sc, self.kap, self.dim, 0)
        assert mat.shape == (9, 3)

    def test_bracket_c1_to_c2_shape(self):
        """[eta, -]: C^1 -> C^2 has shape (9, 9)."""
        mat = _killing_bracket_matrix(self.eta, self.sc, self.kap, self.dim, 1)
        assert mat.shape == (9, 9)

    def test_bracket_c2_to_c3_shape(self):
        """[eta, -]: C^2 -> C^3 has shape (3, 9)."""
        mat = _killing_bracket_matrix(self.eta, self.sc, self.kap, self.dim, 2)
        assert mat.shape == (3, 9)

    def test_bracket_c0_nonzero(self):
        """[eta, -]: C^0 -> C^1 is nonzero."""
        mat = _killing_bracket_matrix(self.eta, self.sc, self.kap, self.dim, 0)
        assert not _is_zero_matrix(mat)

    def test_bracket_c0_is_bracket_map(self):
        """[eta, e_v](e_w) = eta(e_v, e_w) = [e_v, e_w].

        The NR bracket [eta, v](w) = eta(v, w) for eta in C^2, v in C^0.
        So the matrix of [eta, -]: C^0 -> C^1 should encode the Lie bracket.
        """
        mat = _killing_bracket_matrix(self.eta, self.sc, self.kap, self.dim, 0)
        # [eta, e_v](e_w) should be [e_v, e_w]
        for v in range(3):
            for w in range(3):
                for m in range(3):
                    # Position in C^1: m * dim + w (maps e_w to e_m)
                    actual = Fraction(mat[m * 3 + w, v])
                    expected = Fraction(self.sc[v, w, m])
                    assert actual == expected, \
                        f"[eta, e_{v}](e_{w})[{m}] = {actual} != {expected}"

    def test_bracket_intertwining(self):
        """d_CE o [eta,-] = [eta,-] o d_CE at C^0 (since d_CE(eta) = 0)."""
        result = verify_killing_bracket_d_intertwining_sl2()
        assert result["intertwining_holds"]


# ===================================================================
# Kappa-twisted differential
# ===================================================================

class TestKappaTwistedDifferential:
    """d_kappa = d_CE + kappa * [eta, -] on C*(sl_2, sl_2).

    KEY FACT: Since eta = mu (the Lie bracket), [mu,mu]_NR = 0 (Jacobi).
    Therefore (d_CE + kappa*[eta,-])^2 = 0 for ALL kappa.
    The genus-1 curvature is a chiral phenomenon, not CE-level.
    """

    def setup_method(self):
        self.cx = sl2_deformation_complex()

    def test_kappa_zero_is_ce(self):
        """At kappa = 0 (critical level), d_kappa = d_CE, and d^2 = 0."""
        tw = KillingTwistedDifferential(complex=self.cx, kappa=Fraction(0))
        # d_kappa = d_CE at kappa=0
        d_ce_0 = self.cx.differential(0)
        d_tw_0 = tw.d_twisted_matrix(0)
        diff = _mat_add(d_tw_0, _mat_scale(Fraction(-1), d_ce_0))
        assert _is_zero_matrix(diff)

    def test_d_squared_zero_at_critical_level(self):
        """At k = -h^v = -2 (critical), kappa = 0, d^2 = 0."""
        tw = KillingTwistedDifferential(complex=self.cx, kappa=Fraction(0))
        d2 = tw.d_squared_matrix(0)
        assert _is_zero_matrix(d2)

    def test_d_squared_zero_at_generic_level_deg0(self):
        """At generic k, (d_kappa)^2 = 0 at C^0 (Jacobi holds for rescaled mu)."""
        kap = kappa_affine_sl2(Fraction(1))  # k=1, kappa=9/4
        tw = KillingTwistedDifferential(complex=self.cx, kappa=kap)
        d2 = tw.d_squared_matrix(0)
        assert _is_zero_matrix(d2)

    def test_d_squared_zero_at_generic_level_deg1(self):
        """At generic k, (d_kappa)^2 = 0 at C^1."""
        kap = kappa_affine_sl2(Fraction(1))
        tw = KillingTwistedDifferential(complex=self.cx, kappa=kap)
        d2 = tw.d_squared_matrix(1)
        assert _is_zero_matrix(d2)

    def test_jacobi_implies_d_squared_zero(self):
        """d^2 = 0 for all kappa: [eta,eta]_NR = [mu,mu]_NR = 0 (Jacobi)."""
        kap = kappa_affine_sl2(Fraction(1))
        tw = KillingTwistedDifferential(complex=self.cx, kappa=kap)
        assert tw.verify_jacobi_implies_d_squared_zero(0)
        assert tw.verify_jacobi_implies_d_squared_zero(1)

    def test_d_squared_zero_multiple_kappa(self):
        """d^2 = 0 at C^0 for several different kappa values."""
        for kap in [Fraction(0), Fraction(1), Fraction(-1),
                    Fraction(3, 4), Fraction(100)]:
            tw = KillingTwistedDifferential(complex=self.cx, kappa=kap)
            d2 = tw.d_squared_matrix(0)
            assert _is_zero_matrix(d2), f"d^2 != 0 at kappa={kap}"

    def test_twisted_differential_changes_with_kappa(self):
        """The twisted differential d_kappa changes as kappa varies."""
        tw1 = KillingTwistedDifferential(complex=self.cx, kappa=Fraction(0))
        tw2 = KillingTwistedDifferential(complex=self.cx, kappa=Fraction(1))
        d1 = tw1.d_twisted_matrix(0)
        d2 = tw2.d_twisted_matrix(0)
        diff = _mat_add(d1, _mat_scale(Fraction(-1), d2))
        # d_kappa should change with kappa (the bracket term contributes)
        assert not _is_zero_matrix(diff)

    def test_verify_entry_point_critical(self):
        """Verify the entry point at critical level k = -2."""
        result = verify_kappa_twist_curvature_sl2(Fraction(-2))
        assert result["kappa_value"] == Fraction(0)
        assert result["d_squared_zero_at_deg0"]
        assert result["jacobi_consistent"]

    def test_verify_entry_point_generic(self):
        """Verify the entry point at generic level k = 1."""
        result = verify_kappa_twist_curvature_sl2(Fraction(1))
        assert result["kappa_value"] == Fraction(9, 4)
        assert result["d_squared_zero_at_deg0"]
        assert result["d_squared_zero_at_deg1"]


# ===================================================================
# Kappa formulas for standard families
# ===================================================================

class TestKappaFormulas:
    """Modular characteristic kappa for standard families."""

    def test_heisenberg_kappa(self):
        """kappa(Heis) = 1 (rank 1, anomaly ratio rho = 1)."""
        assert kappa_heisenberg() == Fraction(1)

    def test_sl2_kappa_at_k1(self):
        """kappa(V_1(sl_2)) = 3(1+2)/4 = 9/4."""
        assert kappa_affine_sl2(Fraction(1)) == Fraction(9, 4)

    def test_sl2_kappa_at_critical(self):
        """kappa(V_{-2}(sl_2)) = 0 (critical level)."""
        assert kappa_affine_sl2(Fraction(-2)) == Fraction(0)

    def test_sl2_kappa_formula(self):
        """kappa = dim(g)(k+h^v)/(2h^v) = 3(k+2)/4 for sl_2."""
        for k in [Fraction(-1), Fraction(0), Fraction(1), Fraction(2), Fraction(10)]:
            expected = Fraction(3) * (k + Fraction(2)) / Fraction(4)
            assert kappa_affine_sl2(k) == expected

    def test_general_kappa_formula(self):
        """kappa = dim(g)(k+h^v)/(2h^v) for general g."""
        # sl_2: dim=3, h^v=2
        assert kappa_affine(3, Fraction(1), 2) == Fraction(9, 4)
        # sl_3: dim=8, h^v=3
        assert kappa_affine(8, Fraction(1), 3) == Fraction(8) * Fraction(4) / Fraction(6)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)
        assert kappa_virasoro(Fraction(1, 2)) == Fraction(1, 4)

    def test_kappa_additivity(self):
        """kappa(A tensor B) = kappa(A) + kappa(B) (Theorem D)."""
        k1 = kappa_heisenberg()          # 1
        k2 = kappa_affine_sl2(Fraction(1))  # 9/4
        # V_1(sl_2) tensor Heis: kappa = 9/4 + 1 = 13/4
        assert k1 + k2 == Fraction(13, 4)


# ===================================================================
# Obstruction classes
# ===================================================================

class TestObstructionClasses:
    """Obstruction o_{r+1} to extending the shadow obstruction tower."""

    def test_affine_sl2_o4_vanishes(self):
        """Quartic obstruction vanishes for affine sl_2 (shadow depth 3)."""
        result = verify_affine_sl2_o4_vanishes()
        assert result["o4_vanishes"]

    def test_affine_sl2_o4_via_function(self):
        """Direct check: o_4 = 0 for sl_2."""
        sc = sl2_structure_constants()
        kap = sl2_killing_form()
        assert obstruction_class_affine_o4(sc, kap, 3)

    def test_affine_sl3_o4_vanishes(self):
        """Quartic obstruction vanishes for affine sl_3."""
        sc = sl3_structure_constants()
        kap = sl3_killing_form()
        assert obstruction_class_affine_o4(sc, kap, 8)


# ===================================================================
# Shadow depth classification
# ===================================================================

class TestShadowDepthClassification:
    """Shadow archetype classification (G/L/C/M)."""

    def test_heisenberg_gaussian(self):
        """Heisenberg: Gaussian class G, r_max = 2."""
        info = shadow_depth_classification("heisenberg")
        assert info["class"] == "G"
        assert info["r_max"] == 2

    def test_affine_lie(self):
        """Affine V_k(g): Lie/tree class L, r_max = 3."""
        info = shadow_depth_classification("affine")
        assert info["class"] == "L"
        assert info["r_max"] == 3

    def test_betagamma_contact(self):
        """Beta-gamma: contact/quartic class C, r_max = 4."""
        info = shadow_depth_classification("betagamma")
        assert info["class"] == "C"
        assert info["r_max"] == 4

    def test_virasoro_mixed(self):
        """Virasoro: mixed class M, r_max = infinity."""
        info = shadow_depth_classification("virasoro")
        assert info["class"] == "M"
        assert info["r_max"] is None

    def test_wn_mixed(self):
        """W_N: mixed class M, r_max = infinity."""
        info = shadow_depth_classification("w_n")
        assert info["class"] == "M"
        assert info["r_max"] is None

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError):
            shadow_depth_classification("nonexistent")


# ===================================================================
# Heisenberg tangent complex
# ===================================================================

class TestHeisenbergTangent:
    """Tangent complex for the Heisenberg VOA."""

    def setup_method(self):
        self.data = heisenberg_tangent()

    def test_kappa(self):
        """kappa = 1 (rank 1 Heisenberg, anomaly ratio rho = 1)."""
        assert self.data["kappa"] == Fraction(1)

    def test_shadow_depth(self):
        """Shadow depth = 2 (Gaussian)."""
        assert self.data["shadow_depth"] == 2

    def test_shadow_class(self):
        """Shadow class = G."""
        assert self.data["shadow_class"] == "G"

    def test_h1_one(self):
        """H^1 = 1 (level/scaling deformation)."""
        assert self.data["h1"] == 1

    def test_h2_zero(self):
        """H^2 = 0 (unobstructed)."""
        assert self.data["h2"] == 0

    def test_d_theta_squared_zero(self):
        """d_{Theta}^2 = 0 (terminates at arity 2)."""
        assert self.data["d_theta_squared_zero"]


# ===================================================================
# Affine sl_2 tangent complex
# ===================================================================

class TestAffineSl2Tangent:
    """Tangent complex for V_k(sl_2)."""

    def test_shadow_depth_3(self):
        """Shadow depth = 3 for affine sl_2."""
        data = affine_sl2_tangent(Fraction(1))
        assert data["shadow_depth"] == 3

    def test_shadow_class_L(self):
        """Shadow class = L (Lie/tree)."""
        data = affine_sl2_tangent(Fraction(1))
        assert data["shadow_class"] == "L"

    def test_h0_ce_zero(self):
        """H^0_CE = center(sl_2) = 0."""
        data = affine_sl2_tangent(Fraction(1))
        assert data["h0_ce"] == 0

    def test_h1_ce_zero(self):
        """H^1_CE = 0 (sl_2 is rigid)."""
        data = affine_sl2_tangent(Fraction(1))
        assert data["h1_ce"] == 0

    def test_h2_cyc_one(self):
        """H^2_cyc = 1 (level deformation via Killing 3-cocycle)."""
        data = affine_sl2_tangent(Fraction(1))
        assert data["h2_cyc"] == 1

    def test_critical_level(self):
        """At k = -2, kappa = 0 and is_critical = True."""
        data = affine_sl2_tangent(Fraction(-2))
        assert data["is_critical"]
        assert data["kappa"] == Fraction(0)

    def test_obstruction_o4_zero(self):
        """o_4 = 0 (quartic obstruction vanishes)."""
        data = affine_sl2_tangent(Fraction(1))
        assert data["obstruction_o4"] == Fraction(0)


# ===================================================================
# Virasoro tangent complex
# ===================================================================

class TestVirasoroTangent:
    """Tangent complex for the Virasoro algebra."""

    def test_h1_deformation_one(self):
        """H^1 = 1 (central charge deformation)."""
        data = virasoro_tangent(Fraction(26))
        assert data["h1_deformation"] == 1

    def test_shadow_class_M(self):
        """Shadow class = M (mixed, infinite tower)."""
        data = virasoro_tangent(Fraction(1))
        assert data["shadow_class"] == "M"

    def test_shadow_depth_infinite(self):
        """Shadow depth = None (infinite)."""
        data = virasoro_tangent(Fraction(1))
        assert data["shadow_depth"] is None

    def test_kappa_c_over_2(self):
        """kappa = c/2."""
        data = virasoro_tangent(Fraction(26))
        assert data["kappa"] == Fraction(13)

    def test_q_contact_formula(self):
        """Q^contact_Vir = 10 / (c(5c+22)) at generic c."""
        c = Fraction(1)
        data = virasoro_tangent(c)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert data["q_contact"] == expected

    def test_q_contact_c26(self):
        """Q^contact at c = 26: 10 / (26 * 152) = 10/3952 = 5/1976."""
        data = virasoro_tangent(Fraction(26))
        expected = Fraction(10, 26 * 152)
        assert data["q_contact"] == expected

    def test_quintic_forced(self):
        """The quintic obstruction o_5 is nonzero (infinite tower)."""
        data = virasoro_tangent(Fraction(1))
        assert data["obstruction_o5_nonzero"]


# ===================================================================
# sl_3 deformation complex
# ===================================================================

class TestSl3DeformationComplex:
    """Deformation complex for sl_3."""

    def setup_method(self):
        self.cx = sl3_deformation_complex()

    def test_sl3_dim(self):
        """dim(sl_3) = 8."""
        assert self.cx.dim == 8

    def test_sl3_c0_dim(self):
        """C^0(sl_3, sl_3) = sl_3 has dim 8."""
        assert self.cx.degree_dim(0) == 8

    def test_sl3_c1_dim(self):
        """C^1(sl_3, sl_3) has dim 64."""
        assert self.cx.degree_dim(1) == 64

    def test_sl3_c2_dim(self):
        """C^2(sl_3, sl_3) has dim 8 * C(8,2) = 224."""
        assert self.cx.degree_dim(2) == 224

    def test_sl3_rigidity(self):
        """sl_3 is rigid: H^0 = H^1 = H^2 = 0."""
        h = self.cx.cohomology_dims()
        assert h[0] == 0
        assert h[1] == 0
        assert h[2] == 0

    def test_sl3_cyclic_h2_one(self):
        """H^2_cyc(sl_3, sl_3) = 1 (universal: Killing 3-cocycle)."""
        cyc = self.cx.cyclic_cohomology()
        assert cyc["dims"][2] == 1


# ===================================================================
# Differential matrix shapes
# ===================================================================

class TestDifferentialShapes:
    """Verify differential matrices have correct shapes."""

    def setup_method(self):
        self.cx = sl2_deformation_complex()

    def test_d0_shape(self):
        """d^0: C^0 (dim 3) -> C^1 (dim 9)."""
        d0 = self.cx.differential(0)
        assert d0.shape == (9, 3)

    def test_d1_shape(self):
        """d^1: C^1 (dim 9) -> C^2 (dim 9)."""
        d1 = self.cx.differential(1)
        assert d1.shape == (9, 9)

    def test_d2_shape(self):
        """d^2: C^2 (dim 9) -> C^3 (dim 3)."""
        d2 = self.cx.differential(2)
        assert d2.shape == (3, 9)


# ===================================================================
# Matrix utility tests
# ===================================================================

class TestMatrixUtilities:
    """Verify exact arithmetic helpers."""

    def test_zero_matrix_detection(self):
        """_is_zero_matrix detects zero matrices."""
        assert _is_zero_matrix(_np_zeros(3, 3))

    def test_nonzero_matrix_detection(self):
        """_is_zero_matrix rejects nonzero matrices."""
        M = _np_zeros(2, 2)
        M[0, 0] = Fraction(1)
        assert not _is_zero_matrix(M)

    def test_mat_multiply_identity(self):
        """Matrix multiplication with identity."""
        I = _np_zeros(3, 3)
        for i in range(3):
            I[i, i] = Fraction(1)
        A = _np_zeros(3, 3)
        A[0, 1] = Fraction(2)
        A[1, 2] = Fraction(3)
        result = _mat_multiply(I, A)
        assert result[0, 1] == Fraction(2)
        assert result[1, 2] == Fraction(3)

    def test_mat_scale(self):
        """Scalar multiplication."""
        A = _np_zeros(2, 2)
        A[0, 0] = Fraction(3)
        A[1, 1] = Fraction(5)
        B = _mat_scale(Fraction(2), A)
        assert B[0, 0] == Fraction(6)
        assert B[1, 1] == Fraction(10)


# ===================================================================
# Cross-checks with mc2_cyclic_ce
# ===================================================================

class TestCrossChecks:
    """Cross-check with mc2_cyclic_ce module results."""

    def test_ce_cohomology_matches(self):
        """CyclicDeformationComplex.cohomology_dims matches ce_cohomology."""
        cx = sl2_deformation_complex()
        h_new = cx.cohomology_dims()
        h_old = ce_cohomology(sl2_structure_constants(), 3)
        for n in range(4):
            assert h_new[n] == h_old[n], f"H^{n} mismatch: {h_new[n]} != {h_old[n]}"

    def test_differential_0_matches(self):
        """CyclicDeformationComplex.differential(0) matches ce_differential_0."""
        cx = sl2_deformation_complex()
        d_new = cx.differential(0)
        d_old = ce_differential_0(sl2_structure_constants(), 3)
        for i in range(d_new.shape[0]):
            for j in range(d_new.shape[1]):
                assert Fraction(d_new[i, j]) == Fraction(d_old[i, j])

    def test_differential_1_matches(self):
        """CyclicDeformationComplex.differential(1) matches ce_differential_1."""
        cx = sl2_deformation_complex()
        d_new = cx.differential(1)
        d_old = ce_differential_1(sl2_structure_constants(), 3)
        for i in range(d_new.shape[0]):
            for j in range(d_new.shape[1]):
                assert Fraction(d_new[i, j]) == Fraction(d_old[i, j])


# ===================================================================
# Killing bracket [eta, eta] and curvature
# ===================================================================

class TestKillingBracketSquared:
    """[eta, eta]_NR = [mu, mu]_NR = 0 (Jacobi identity).

    The Killing cocycle eta = mu is the Lie bracket itself.
    The NR bracket [mu, mu]_NR = 0 is equivalent to the Jacobi identity.
    Genus-1 curvature is a chiral phenomenon beyond the CE complex.
    """

    def setup_method(self):
        self.sc = sl2_structure_constants()
        self.kap = sl2_killing_form()
        self.dim = 3
        self.eta = killing_cocycle(self.sc, self.kap, self.dim)

    def test_eta_bracket_eta_is_zero(self):
        """[eta, eta]_NR = [mu, mu]_NR = 0 (Jacobi identity for sl_2).

        This is the key structural fact: the Killing cocycle IS the Lie bracket,
        and [mu, mu]_NR = 0 is exactly the Jacobi identity.
        """
        bracket_2 = _killing_bracket_matrix(self.eta, self.sc, self.kap, self.dim, 2)
        result = _mat_multiply(bracket_2, self.eta.reshape(-1, 1))
        assert _is_zero_matrix(result)

    def test_d_squared_always_zero(self):
        """(d_CE + kappa*[eta,-])^2 = 0 for all kappa (consequence of Jacobi).

        Since [mu, mu]_NR = 0 and d_CE(mu) = 0 (mu is a CE cocycle, being the
        Lie bracket), the full expansion of (d + kappa*[mu,-])^2 vanishes:
        d^2 + kappa*(d[mu,-] + [mu,-]d) + kappa^2*[mu,[mu,-]] = 0.
        """
        cx = sl2_deformation_complex()
        for kap in [Fraction(0), Fraction(1), Fraction(-3, 7), Fraction(100)]:
            tw = KillingTwistedDifferential(complex=cx, kappa=kap)
            d2 = tw.d_squared_matrix(0)
            assert _is_zero_matrix(d2), f"d^2 != 0 at kappa={kap}"

    def test_bracket_c0_equals_neg_d_ce(self):
        """[eta, -]: C^0 -> C^1 equals -d_CE: C^0 -> C^1.

        [eta, v](w) = eta(v, w) = [v, w], while d_CE(v)(w) = [w, v] = -[v, w].
        """
        cx = sl2_deformation_complex()
        bracket_0 = _killing_bracket_matrix(self.eta, self.sc, self.kap, self.dim, 0)
        d0 = cx.differential(0)
        # bracket_0 + d0 should be zero
        sum_mat = _mat_add(bracket_0, d0)
        assert _is_zero_matrix(sum_mat)


# ===================================================================
# Kappa at various levels
# ===================================================================

class TestKappaAtVariousLevels:
    """kappa = 3(k+2)/4 for sl_2 at various levels."""

    @pytest.mark.parametrize("k,expected", [
        (Fraction(-2), Fraction(0)),      # critical
        (Fraction(-1), Fraction(3, 4)),   # k = -1
        (Fraction(0), Fraction(3, 2)),    # k = 0
        (Fraction(1), Fraction(9, 4)),    # k = 1
        (Fraction(2), Fraction(3)),       # k = 2
        (Fraction(10), Fraction(9)),      # k = 10
        (Fraction(-3, 2), Fraction(3, 8)),  # admissible k = -3/2
    ])
    def test_kappa_value(self, k, expected):
        assert kappa_affine_sl2(k) == expected
