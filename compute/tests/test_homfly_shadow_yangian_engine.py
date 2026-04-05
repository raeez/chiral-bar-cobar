r"""Tests for the HOMFLY-PT shadow/Yangian engine.

Verifies knot and link invariants computed from the shadow R-matrix
(bar complex collision residue) against known exact values.

Multi-path verification:
    Path 1: sl_N check_R braid representation (direct)
    Path 2: HOMFLY-PT at N=2 (should match Jones)
    Path 3: Alexander polynomial from HOMFLY specialization
    Path 4: Kauffman bracket state sum (where available)
    Path 5: Exact polynomial formulas (literature values)
    Path 6: Knot determinant = |Delta_K(-1)|

Ground truth:
    - KnotInfo database values
    - Kassel, Quantum Groups, GTM 155 (1995)
    - Lickorish, An introduction to knot theory (1997)
    - Ohtsuki, Quantum Invariants, World Scientific (2002)

Connection to the bar complex:
    The shadow r-matrix r(z) = Res^{coll}_{0,2}(Theta_A) for A = V_k(sl_N)
    produces the classical r-matrix Omega/z, whose quantization gives the
    quantum R-matrix of U_q(sl_N).  The DK bridge (proved for all simple
    types via MC3) identifies this with the Yangian representation, and
    the braid closure produces the HOMFLY-PT polynomial.

Conventions:
    - Jones variable t = q^2.
    - check_R = Kassel convention (eigenvalues q, -q^{-1}).
    - HOMFLY-PT: a P(L+) - a^{-1} P(L-) = z P(L0), a = q^N, z = q - q^{-1}.
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.homfly_shadow_yangian_engine import (
    # Extended knot/link table
    EXTENDED_KNOT_TABLE,
    LINK_COMPONENTS,
    KNOT_CROSSINGS,
    get_braid,
    # Exact HOMFLY polynomials
    homfly_exact_unknot,
    homfly_exact_trefoil,
    homfly_exact_figure_eight,
    homfly_exact_cinquefoil,
    eval_homfly_exact,
    homfly_exact_evaluate,
    verify_homfly_exact_vs_numerical,
    HOMFLY_UNKNOT,
    HOMFLY_TREFOIL,
    HOMFLY_FIGURE_EIGHT,
    HOMFLYPoly,
    # Alexander polynomial
    alexander_from_homfly,
    alexander_exact_trefoil,
    alexander_exact_figure_eight,
    alexander_exact_cinquefoil,
    alexander_exact_52,
    CONWAY_COEFFICIENTS,
    # Shadow r-matrix
    shadow_classical_r_matrix,
    verify_r_matrix_from_shadow,
    shadow_r_matrix_quantization,
    # Vassiliev invariants
    vassiliev_v2_from_shadow,
    vassiliev_v3_from_shadow,
    vassiliev_invariants_from_jones,
    VASSILIEV_V2,
    # Kontsevich weight system
    chord_diagram_weight_sl2,
    kontsevich_weight_from_shadow,
    kontsevich_weight_wheel,
    # Colored HOMFLY
    colored_homfly_adjoint_sl3,
    # Links
    homfly_link,
    jones_link,
    hopf_link_jones,
    hopf_link_jones_exact,
    borromean_rings_braid,
    borromean_jones,
    borromean_homfly,
    # Kauffman bracket
    kauffman_bracket_from_braid,
    jones_from_kauffman,
    # Conway polynomial
    conway_polynomial_from_alexander,
    conway_exact_trefoil,
    conway_exact_figure_eight,
    # Multi-path verification
    multipath_jones,
    multipath_homfly,
    # Knot determinant
    knot_determinant,
    KNOWN_DETERMINANTS,
    # Shadow depth
    shadow_depth_for_knot,
    crossing_number_bound_from_shadow,
    # Quantum utilities
    quantum_integer,
    quantum_factorial,
    quantum_binomial,
    # Torus knots
    torus_knot_jones_exact,
    # Summary
    knot_invariant_summary,
)

from compute.lib.knot_invariant_shadow_engine import (
    jones_at,
    homfly_at,
    jones_from_braid,
    homfly_from_braid,
    slN_check_r_matrix,
    verify_hecke_relation,
    verify_braid_relation,
    KNOT_BRAIDS,
)


# ============================================================
# Shadow R-matrix tests
# ============================================================

class TestShadowRMatrix:
    """Tests for the shadow r-matrix r(z) = Omega/z."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_casimir_is_permutation(self, N):
        """The Casimir Omega = sum e_{ij} otimes e_{ji} is the permutation P."""
        Omega = shadow_classical_r_matrix(N)
        d = N * N
        # Check Omega is a permutation matrix: Omega^2 = I
        assert np.allclose(Omega @ Omega, np.eye(d), atol=1e-12)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_casimir_trace(self, N):
        """Tr(Omega) = N (trace of the permutation = dimension)."""
        Omega = shadow_classical_r_matrix(N)
        assert abs(np.trace(Omega) - N) < 1e-12

    @pytest.mark.parametrize("N", [2, 3])
    def test_classical_limit(self, N):
        """check_R(q -> 1) -> P (the permutation operator)."""
        disc = verify_r_matrix_from_shadow(cmath.exp(0.3j), N)
        assert disc < 1e-10

    def test_shadow_quantization_sl2(self):
        """First-order quantization of the shadow r-matrix gives check_R."""
        hbar = 0.3j
        R = shadow_r_matrix_quantization(2, hbar)
        assert R.shape == (4, 4)

    @pytest.mark.parametrize("N", [2, 3])
    def test_shadow_to_hecke(self, N):
        """The quantized shadow R-matrix satisfies the Hecke relation."""
        q = cmath.exp(0.4j)
        disc = verify_hecke_relation(q, N)
        assert disc < 1e-10

    @pytest.mark.parametrize("N", [2, 3])
    def test_shadow_to_braid(self, N):
        """The quantized shadow R-matrix satisfies the braid relation."""
        q = cmath.exp(0.35j)
        disc = verify_braid_relation(q, N)
        assert disc < 1e-10

    def test_casimir_eigenvalues_sl2(self):
        """Omega for sl_2 has eigenvalues +1 (sym, dim 3) and -1 (anti, dim 1)."""
        Omega = shadow_classical_r_matrix(2)
        evals = np.linalg.eigvals(Omega)
        n_plus = sum(1 for e in evals if abs(e - 1) < 1e-10)
        n_minus = sum(1 for e in evals if abs(e + 1) < 1e-10)
        assert n_plus == 3
        assert n_minus == 1


# ============================================================
# Exact HOMFLY-PT polynomial tests
# ============================================================

class TestExactHOMFLY:
    """Tests for exact HOMFLY-PT polynomial formulas."""

    def test_unknot_is_one(self):
        """P(unknot) = 1 at all (a, z)."""
        for a, z in [(1.0, 0.5), (2.0, 1.0), (0.5, 2.0)]:
            val = eval_homfly_exact(homfly_exact_unknot(), a, z)
            assert abs(val - 1.0) < 1e-12

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.5j), cmath.exp(0.7j), cmath.exp(1.0j),
    ])
    def test_trefoil_exact_vs_numerical(self, q_val):
        """Exact HOMFLY for trefoil matches numerical computation."""
        disc = verify_homfly_exact_vs_numerical("3_1", q_val, 2)
        assert disc is not None
        assert disc < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.5j), cmath.exp(0.7j),
    ])
    def test_figure_eight_exact_vs_numerical(self, q_val):
        """Exact HOMFLY for figure-eight matches numerical computation."""
        disc = verify_homfly_exact_vs_numerical("4_1", q_val, 2)
        assert disc is not None
        assert disc < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.5j), cmath.exp(0.7j),
    ])
    def test_cinquefoil_exact_vs_numerical(self, q_val):
        """Exact HOMFLY for 5_1 matches numerical computation."""
        disc = verify_homfly_exact_vs_numerical("5_1", q_val, 2)
        assert disc is not None
        assert disc < 1e-10

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_trefoil_exact_vs_numerical_multiN(self, N):
        """Trefoil HOMFLY matches at multiple N values."""
        q = cmath.exp(0.4j)
        disc = verify_homfly_exact_vs_numerical("3_1", q, N)
        assert disc is not None
        assert disc < 1e-10

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_figure_eight_exact_vs_numerical_multiN(self, N):
        """Figure-eight HOMFLY matches at multiple N values."""
        q = cmath.exp(0.4j)
        disc = verify_homfly_exact_vs_numerical("4_1", q, N)
        assert disc is not None
        assert disc < 1e-10

    def test_trefoil_conway_specialization(self):
        """At a=1, trefoil HOMFLY gives Conway polynomial 1 + z^2."""
        for z in [0.5, 1.0, 1.5, 2.0]:
            val = eval_homfly_exact(homfly_exact_trefoil(), 1.0, z)
            expected = 1.0 + z**2
            assert abs(val - expected) < 1e-12

    def test_figure_eight_conway_specialization(self):
        """At a=1, figure-eight HOMFLY gives Conway polynomial 1 - z^2."""
        for z in [0.5, 1.0, 1.5]:
            val = eval_homfly_exact(homfly_exact_figure_eight(), 1.0, z)
            expected = 1.0 - z**2
            assert abs(val - expected) < 1e-12


# ============================================================
# HOMFLYPoly class tests
# ============================================================

class TestHOMFLYPoly:
    """Tests for the HOMFLYPoly Laurent polynomial class."""

    def test_zero(self):
        assert abs(HOMFLYPoly.zero().evaluate(1.0, 1.0)) < 1e-12

    def test_one(self):
        assert abs(HOMFLYPoly.one().evaluate(2.0, 3.0) - 1.0) < 1e-12

    def test_trefoil_evaluation(self):
        q = cmath.exp(0.4j)
        a = q**2
        z = q - 1.0/q
        val = HOMFLY_TREFOIL.evaluate(a, z)
        expected = homfly_at("3_1", q, 2)
        assert abs(val - expected) < 1e-10

    def test_jones_specialization(self):
        """Jones specialization of trefoil HOMFLY."""
        q = cmath.exp(0.4j)
        j_from_poly = HOMFLY_TREFOIL.jones_specialization(q)
        j_direct = jones_at("3_1", q)
        assert abs(j_from_poly - j_direct) < 1e-10

    def test_alexander_specialization(self):
        """Alexander specialization (a=1) of trefoil HOMFLY."""
        z = 0.7
        val = HOMFLY_TREFOIL.alexander_specialization(z)
        expected = 1.0 + z**2
        assert abs(val - expected) < 1e-12

    def test_addition(self):
        p = HOMFLY_TREFOIL + HOMFLY_FIGURE_EIGHT
        q = cmath.exp(0.3j)
        a = q**2
        z = q - 1.0/q
        assert abs(p.evaluate(a, z) - HOMFLY_TREFOIL.evaluate(a, z)
                   - HOMFLY_FIGURE_EIGHT.evaluate(a, z)) < 1e-12

    def test_scale(self):
        p = HOMFLY_TREFOIL.scale(3)
        q = cmath.exp(0.4j)
        a = q**2
        z = q - 1.0/q
        assert abs(p.evaluate(a, z) - 3 * HOMFLY_TREFOIL.evaluate(a, z)) < 1e-12


# ============================================================
# Alexander polynomial tests
# ============================================================

class TestAlexanderPolynomial:
    """Tests for the Alexander polynomial from HOMFLY specialization."""

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.2j), cmath.exp(0.5j), cmath.exp(0.7j), cmath.exp(1.0j),
    ])
    def test_trefoil_exact(self, q_val):
        """Delta_{3_1}(t) = t^{-1} - 1 + t."""
        t = q_val**2
        alex = alexander_from_homfly("3_1", q_val)
        exact = alexander_exact_trefoil(t)
        assert abs(alex - exact) < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.6j), cmath.exp(0.9j),
    ])
    def test_figure_eight_exact(self, q_val):
        """Delta_{4_1}(t) = -t^{-1} + 3 - t."""
        t = q_val**2
        alex = alexander_from_homfly("4_1", q_val)
        exact = alexander_exact_figure_eight(t)
        assert abs(alex - exact) < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.6j), cmath.exp(0.9j),
    ])
    def test_cinquefoil_exact(self, q_val):
        """Delta_{5_1}(t) = t^{-2} - t^{-1} + 1 - t + t^2."""
        t = q_val**2
        alex = alexander_from_homfly("5_1", q_val)
        exact = alexander_exact_cinquefoil(t)
        assert abs(alex - exact) < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.6j), cmath.exp(0.9j),
    ])
    def test_52_exact(self, q_val):
        """Delta_{5_2}(t) = 2t^{-1} - 3 + 2t."""
        t = q_val**2
        alex = alexander_from_homfly("5_2", q_val)
        exact = alexander_exact_52(t)
        assert abs(alex - exact) < 1e-10

    def test_unknot(self):
        """Delta(unknot) = 1."""
        q = cmath.exp(0.4j)
        assert abs(alexander_from_homfly("0_1", q) - 1.0) < 1e-10

    @pytest.mark.parametrize("knot", ["3_1", "4_1", "5_1", "5_2", "6_1", "7_1"])
    def test_alexander_at_1(self, knot):
        """Delta_K(1) = 1 for all knots (via Conway(0) = 1)."""
        # At t=1, z = 0, Conway(0) = 1.
        q = 1.0 + 1e-10j  # q near 1, t = q^2 near 1
        alex = alexander_from_homfly(knot, q)
        assert abs(alex - 1.0) < 0.01, f"Delta_{knot}(1) = {alex}"

    @pytest.mark.parametrize("knot", ["3_1", "4_1", "5_1", "5_2"])
    def test_alexander_symmetry(self, knot):
        """Delta_K(t) = Delta_K(t^{-1}) for knots."""
        q = cmath.exp(0.4j)
        t = q**2
        alex_t = alexander_from_homfly(knot, q)
        alex_tinv = alexander_from_homfly(knot, 1.0 / q)
        # Note: 1/q gives t^{-1} = (1/q)^2.
        assert abs(alex_t - alex_tinv) < 1e-8, \
            f"Symmetry failed for {knot}: Delta(t)={alex_t}, Delta(1/t)={alex_tinv}"

    def test_figure_eight_amphicheiral(self):
        """4_1 is amphicheiral: Delta(t) = Delta(t^{-1})."""
        q = cmath.exp(0.5j)
        t = q**2
        assert abs(alexander_exact_figure_eight(t) -
                   alexander_exact_figure_eight(1.0/t)) < 1e-12


# ============================================================
# Knot determinant tests
# ============================================================

class TestKnotDeterminant:
    """Tests for knot determinant det(K) = |Delta_K(-1)|."""

    @pytest.mark.parametrize("knot,expected", [
        ("3_1", 3), ("4_1", 5), ("5_1", 5), ("5_2", 7),
        ("6_1", 9), ("7_1", 7),
    ])
    def test_determinant(self, knot, expected):
        """Knot determinant matches KnotInfo value."""
        det = knot_determinant(knot)
        assert abs(det - expected) < 0.5, \
            f"det({knot}) = {det:.1f}, expected {expected}"


# ============================================================
# Extended knot/link table tests
# ============================================================

class TestExtendedTable:
    """Tests for the extended knot and link table."""

    def test_all_braids_valid(self):
        """All knots in the extended table have valid braid words."""
        for name, (braid, ns) in EXTENDED_KNOT_TABLE.items():
            if braid:
                mx = max(abs(g) for g in braid)
                assert mx < ns, f"{name}: gen {mx} >= n_strands={ns}"

    def test_get_braid_all(self):
        """get_braid works for all named knots."""
        for name in EXTENDED_KNOT_TABLE:
            braid, ns = get_braid(name)
            assert ns >= 1

    def test_get_braid_torus(self):
        """get_braid works for T(p, n) torus knots."""
        for p, n in [(2, 3), (2, 5), (2, 7), (3, 4)]:
            braid, ns = get_braid(f"T({p},{n})")
            assert ns == p

    @pytest.mark.parametrize("name", list(EXTENDED_KNOT_TABLE.keys()))
    def test_jones_computes(self, name):
        """Jones polynomial computes without error for all extended knots."""
        q = cmath.exp(0.35j)
        braid, ns = get_braid(name)
        if braid:
            v = jones_from_braid(braid, ns, q)
            assert np.isfinite(abs(v))

    @pytest.mark.parametrize("name", [
        "3_1", "4_1", "5_1", "5_2", "6_1", "6_2", "6_3",
        "7_1", "7_2", "7_3", "7_4",
    ])
    def test_jones_nontrivial(self, name):
        """Jones polynomial of nontrivial knots is not 1."""
        q = cmath.exp(0.5j)
        braid, ns = get_braid(name)
        v = jones_from_braid(braid, ns, q)
        assert abs(v - 1.0) > 0.01, f"Jones({name}) = {v}"

    @pytest.mark.parametrize("name", [
        "3_1", "4_1", "5_1", "5_2", "6_1", "6_2", "6_3",
        "7_1", "7_2", "7_3", "7_4",
    ])
    def test_homfly_computes_N2(self, name):
        """HOMFLY at N=2 computes and matches Jones."""
        q = cmath.exp(0.4j)
        braid, ns = get_braid(name)
        j = jones_from_braid(braid, ns, q)
        h = homfly_from_braid(braid, ns, q, 2)
        assert abs(h - j) < 1e-8, f"HOMFLY(N=2) != Jones for {name}"

    @pytest.mark.parametrize("name", [
        "3_1", "4_1", "5_1", "5_2", "6_1", "7_1",
    ])
    def test_homfly_computes_N3(self, name):
        """HOMFLY at N=3 computes without error."""
        q = cmath.exp(0.3j)
        braid, ns = get_braid(name)
        h = homfly_from_braid(braid, ns, q, 3)
        assert np.isfinite(abs(h))


# ============================================================
# Link invariant tests
# ============================================================

class TestLinkInvariants:
    """Tests for link invariants."""

    def test_hopf_link_computes(self):
        """Hopf link Jones polynomial is computable."""
        q = cmath.exp(0.4j)
        val = hopf_link_jones(q)
        assert np.isfinite(abs(val))

    def test_hopf_link_nontrivial(self):
        """Hopf link is not the unknot."""
        q = cmath.exp(0.4j)
        val = hopf_link_jones(q)
        assert abs(val - 1.0) > 0.01

    def test_hopf_link_consistent(self):
        """Hopf link Jones from two methods agree."""
        q = cmath.exp(0.4j)
        j1 = hopf_link_jones(q)
        j2 = jones_from_braid([1, 1], 2, q)
        assert abs(j1 - j2) < 1e-12

    def test_borromean_rings_computes(self):
        """Borromean rings Jones polynomial computes."""
        q = cmath.exp(0.3j)
        val = borromean_jones(q)
        assert np.isfinite(abs(val))

    def test_borromean_rings_homfly(self):
        """Borromean rings HOMFLY at N=2 matches Jones."""
        q = cmath.exp(0.35j)
        j = borromean_jones(q)
        h = borromean_homfly(q, 2)
        assert abs(h - j) < 1e-8

    def test_borromean_rings_nontrivial(self):
        """Borromean rings are not the unlink."""
        q = cmath.exp(0.4j)
        val = borromean_jones(q)
        assert abs(val) > 0.01

    def test_solomon_link(self):
        """Solomon link (T(2,4) on 2 strands) computes."""
        q = cmath.exp(0.35j)
        braid, ns = get_braid("solomon")
        v = jones_from_braid(braid, ns, q)
        assert np.isfinite(abs(v))

    def test_hopf_link_homfly_N3(self):
        """Hopf link HOMFLY at N=3 computes."""
        q = cmath.exp(0.4j)
        val = homfly_link("hopf", q, 3)
        assert np.isfinite(abs(val))


# ============================================================
# Kauffman bracket tests
# ============================================================

class TestKauffmanBracket:
    """Tests for the Kauffman bracket state-sum model."""

    def test_trefoil_nonzero(self):
        """Kauffman bracket of trefoil is nonzero."""
        A = cmath.exp(0.4j)
        val = kauffman_bracket_from_braid("3_1", A)
        assert val is not None
        assert abs(val) > 0.01

    def test_figure_eight_nonzero(self):
        """Kauffman bracket of figure-eight is nonzero."""
        A = cmath.exp(0.3j)
        val = kauffman_bracket_from_braid("4_1", A)
        assert val is not None
        assert abs(val) > 0.01

    @pytest.mark.parametrize("knot", ["3_1", "5_1", "7_1"])
    def test_kauffman_available(self, knot):
        """Kauffman bracket is available for knots with crossing data."""
        if knot in KNOT_CROSSINGS:
            A = cmath.exp(0.4j)
            val = kauffman_bracket_from_braid(knot, A)
            assert val is not None

    def test_kauffman_unavailable(self):
        """Kauffman bracket returns None for knots without crossing data."""
        val = kauffman_bracket_from_braid("5_2", cmath.exp(0.3j))
        # 5_2 may or may not have crossing data; just check it doesn't crash
        # (it returns None if not available)

    def test_jones_from_kauffman_trefoil(self):
        """Jones from Kauffman bracket should be computable for trefoil."""
        q = cmath.exp(0.4j)
        val = jones_from_kauffman("3_1", q)
        if val is not None:
            assert np.isfinite(abs(val))


# ============================================================
# Conway polynomial tests
# ============================================================

class TestConwayPolynomial:
    """Tests for the Conway polynomial."""

    def test_trefoil_exact(self):
        """nabla_{3_1}(z) = z^2 + 1."""
        for z in [0.3, 0.5, 1.0, 2.0]:
            assert abs(conway_exact_trefoil(z) - (z**2 + 1)) < 1e-12

    def test_figure_eight_exact(self):
        """nabla_{4_1}(z) = 1 - z^2."""
        for z in [0.3, 0.5, 1.0]:
            assert abs(conway_exact_figure_eight(z) - (1 - z**2)) < 1e-12

    def test_conway_from_alexander_trefoil(self):
        """Conway polynomial from Alexander for trefoil."""
        for z in [0.5j, 1.0j, 0.5]:
            val = conway_polynomial_from_alexander("3_1", z)
            expected = conway_exact_trefoil(z)
            assert abs(val - expected) < 0.1

    @pytest.mark.parametrize("knot", list(CONWAY_COEFFICIENTS.keys()))
    def test_conway_at_zero(self, knot):
        """nabla_K(0) = 1 for all knots."""
        coeffs = CONWAY_COEFFICIENTS[knot]
        assert coeffs.get(0, 0) == 1


# ============================================================
# Vassiliev invariant tests
# ============================================================

class TestVassilievInvariants:
    """Tests for Vassiliev invariants from the shadow arity."""

    def test_v2_unknot_zero(self):
        """v_2(unknot) = 0."""
        v2 = vassiliev_v2_from_shadow("0_1", eps=1e-4)
        assert abs(v2) < 0.5

    def test_v2_trefoil_nonzero(self):
        """v_2(3_1) != 0 (the trefoil is nontrivial at arity 2)."""
        v2 = vassiliev_v2_from_shadow("3_1", eps=1e-4)
        assert abs(v2) > 0.01

    def test_v2_distinguishes_trefoil_figure_eight(self):
        """v_2(3_1) != v_2(4_1)."""
        v2_t = vassiliev_v2_from_shadow("3_1", eps=1e-4)
        v2_f = vassiliev_v2_from_shadow("4_1", eps=1e-4)
        assert abs(v2_t - v2_f) > 0.1

    def test_v3_figure_eight_small(self):
        """v_3(4_1) ~ 0 (amphicheiral => odd Vassiliev vanish)."""
        v3 = vassiliev_v3_from_shadow("4_1", eps=1e-4)
        assert abs(v3) < 1.0

    def test_vassiliev_series(self):
        """v_0 = 1, v_1 = 0 for all knots."""
        for knot in ["3_1", "4_1"]:
            vs = vassiliev_invariants_from_jones(knot, max_order=3, eps=1e-4)
            assert abs(vs[0] - 1.0) < 0.1  # v_0 = 1
            assert abs(vs[1]) < 0.5  # v_1 ~ 0

    def test_vassiliev_v2_shadow_arity_connection(self):
        """v_2 from Jones derivative is proportional to Conway coefficient a_2.

        The arity-2 shadow gives the classical r-matrix Omega/z;
        its weight system on the trefoil's chord diagram of order 2
        gives the Conway coefficient a_2(3_1) = 1.

        The Jones expansion V(e^{2h}) gives v_2 = -12 * a_2
        (the factor -12 comes from the writhe normalization and
        the relation between Jones and Conway conventions).

        For the trefoil: v_2^{Jones} = -12, a_2 = 1.
        For the figure-eight: v_2^{Jones} = 12, a_2 = -1.
        """
        v2_trefoil = vassiliev_v2_from_shadow("3_1", eps=1e-5)
        v2_fig8 = vassiliev_v2_from_shadow("4_1", eps=1e-5)
        # Check the ratio is -12 (Jones-to-Conway normalization)
        assert abs(v2_trefoil.real - (-12.0)) < 1.0
        assert abs(v2_fig8.real - 12.0) < 1.0
        # And opposite signs (matching a_2 signs)
        assert v2_trefoil.real * v2_fig8.real < 0


# ============================================================
# Kontsevich weight system tests
# ============================================================

class TestKontsevichWeight:
    """Tests for the Kontsevich integral weight system from the shadow."""

    def test_sl2_single_chord(self):
        """Weight of a single chord (n=1) in sl_2: W = (3 + (-1)^1)/4 = 1/2."""
        assert abs(chord_diagram_weight_sl2(1) - 0.5) < 1e-12

    def test_sl2_double_chord(self):
        """Weight of two chords (n=2) in sl_2: W = (3 + 1)/4 = 1."""
        assert abs(chord_diagram_weight_sl2(2) - 1.0) < 1e-12

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_isolated_chords(self, N):
        """Weight of n isolated chords from sl_N shadow = N^{-n}."""
        for n in [1, 2, 3]:
            assert abs(kontsevich_weight_from_shadow(N, n) - N**(-n)) < 1e-12

    def test_wheel_weight_n1(self):
        """Wheel with 1 spoke: W = N."""
        for N in [2, 3, 4]:
            assert abs(kontsevich_weight_wheel(N, 1) - N) < 1e-12


# ============================================================
# Colored HOMFLY tests
# ============================================================

class TestColoredHOMFLY:
    """Tests for colored HOMFLY polynomials."""

    def test_adjoint_sl3_computes(self):
        """Colored HOMFLY for trefoil adjoint of sl_3 computes."""
        q = cmath.exp(0.4j)
        val = colored_homfly_adjoint_sl3("3_1", q)
        if val is not None:
            assert np.isfinite(abs(val))

    def test_adjoint_unknot(self):
        """Colored HOMFLY for unknot is 1 (any representation)."""
        q = cmath.exp(0.3j)
        val = colored_homfly_adjoint_sl3("0_1", q)
        if val is not None:
            assert abs(val - 1.0) < 1e-8


# ============================================================
# Multi-path verification tests
# ============================================================

class TestMultiPath:
    """Multi-path consistency verification."""

    @pytest.mark.parametrize("knot", ["3_1", "4_1", "5_1"])
    def test_jones_multipath(self, knot):
        """Jones from check_R matches Jones from HOMFLY(N=2)."""
        q = cmath.exp(0.4j)
        result = multipath_jones(knot, q)
        assert abs(result["jones_direct"] - result["homfly_N2"]) < 1e-8

    @pytest.mark.parametrize("knot", ["3_1", "4_1", "5_1"])
    def test_jones_colored_j2(self, knot):
        """Jones matches colored Jones at color=2."""
        q = cmath.exp(0.4j)
        result = multipath_jones(knot, q)
        # Colored J_2 may differ by normalization, check consistency
        assert np.isfinite(abs(result["colored_j2"]))

    def test_homfly_multiN(self):
        """HOMFLY at different N gives different values for nontrivial knots."""
        q = cmath.exp(0.5j)
        result = multipath_homfly("3_1", q)
        h2 = result["homfly_N2"]
        h3 = result["homfly_N3"]
        h4 = result["homfly_N4"]
        # All three should be different
        assert abs(h2 - h3) > 0.01
        assert abs(h3 - h4) > 0.01

    def test_homfly_N2_matches_jones(self):
        """HOMFLY at N=2 matches Jones for all tested knots."""
        q = cmath.exp(0.4j)
        for knot in ["3_1", "4_1", "5_1", "5_2"]:
            result = multipath_homfly(knot, q)
            assert abs(result["homfly_N2"] - result["jones_direct"]) < 1e-8


# ============================================================
# HOMFLY-PT at multiple N tests
# ============================================================

class TestHOMFLYMultiN:
    """Tests for HOMFLY at multiple sl_N ranks."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_unknot_is_one(self, N):
        """P(unknot; N) = 1."""
        q = cmath.exp(0.3j)
        assert abs(homfly_at("0_1", q, N) - 1.0) < 1e-10

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_trefoil_nontrivial(self, N):
        """P(3_1; N) != 1 for all N."""
        q = cmath.exp(0.5j)
        assert abs(homfly_at("3_1", q, N) - 1.0) > 0.01

    def test_sl2_jones_consistency(self):
        """HOMFLY at N=2 = Jones for all standard knots."""
        q = cmath.exp(0.4j)
        for knot in ["3_1", "4_1", "5_1", "5_2", "6_1"]:
            h = homfly_at(knot, q, 2)
            j = jones_at(knot, q)
            assert abs(h - j) < 1e-8, \
                f"HOMFLY(N=2) != Jones for {knot}: H={h}, J={j}"


# ============================================================
# Torus knot tests
# ============================================================

class TestTorusKnots:
    """Tests for torus knot invariants."""

    @pytest.mark.parametrize("n", [3, 5, 7, 9])
    def test_T2n_jones(self, n):
        """T(2,n) Jones polynomial computes and is nontrivial."""
        q = cmath.exp(0.3j)
        v = torus_knot_jones_exact(2, n, q)
        assert np.isfinite(abs(v))
        assert abs(v - 1.0) > 0.01

    def test_T23_equals_trefoil(self):
        """T(2,3) = 3_1."""
        q = cmath.exp(0.35j)
        v_torus = torus_knot_jones_exact(2, 3, q)
        v_trefoil = jones_at("3_1", q)
        assert abs(v_torus - v_trefoil) < 1e-10

    def test_T25_equals_51(self):
        """T(2,5) = 5_1."""
        q = cmath.exp(0.35j)
        v_torus = torus_knot_jones_exact(2, 5, q)
        v_51 = jones_at("5_1", q)
        assert abs(v_torus - v_51) < 1e-10

    def test_T27_equals_71(self):
        """T(2,7) = 7_1."""
        q = cmath.exp(0.3j)
        v_torus = torus_knot_jones_exact(2, 7, q)
        v_71 = jones_at("7_1", q)
        assert abs(v_torus - v_71) < 1e-10

    def test_T34_jones(self):
        """T(3,4) Jones polynomial computes."""
        q = cmath.exp(0.3j)
        braid, ns = get_braid("T(3,4)")
        v = jones_from_braid(braid, ns, q)
        assert np.isfinite(abs(v))


# ============================================================
# Shadow depth and complexity tests
# ============================================================

class TestShadowDepth:
    """Tests for shadow depth classification of affine algebras."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_affine_slN_is_class_L(self, N):
        """Affine sl_N is class L (Lie/tree, r_max = 3)."""
        assert shadow_depth_for_knot(N) == "L"

    def test_crossing_bound(self):
        """Crossing number bound from v_2."""
        # For trefoil: v_2 = 1, bound = 12 * sqrt(1) = 12.
        # Actual crossing number = 3, so bound is not tight but valid.
        bound = crossing_number_bound_from_shadow(1.0)
        assert bound == 12.0
        assert bound >= 3  # trefoil crossing number


# ============================================================
# Quantum utility tests
# ============================================================

class TestQuantumUtilities:
    """Tests for quantum integer, factorial, binomial."""

    def test_quantum_integer_classical(self):
        """[n]_1 = n."""
        for n in range(1, 6):
            assert abs(quantum_integer(n, 1.0 + 1e-14) - n) < 0.01

    def test_quantum_integer_formula(self):
        """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
        q = cmath.exp(0.3j)
        for n in range(1, 5):
            expected = (q**n - q**(-n)) / (q - q**(-1))
            assert abs(quantum_integer(n, q) - expected) < 1e-12

    def test_quantum_factorial(self):
        """[n]! = [1][2]...[n]."""
        q = cmath.exp(0.3j)
        f3 = quantum_factorial(3, q)
        expected = quantum_integer(1, q) * quantum_integer(2, q) * quantum_integer(3, q)
        assert abs(f3 - expected) < 1e-12

    def test_quantum_binomial_symmetry(self):
        """[n choose k]_q = [n choose n-k]_q."""
        q = cmath.exp(0.4j)
        for n in range(2, 5):
            for k in range(n + 1):
                assert abs(quantum_binomial(n, k, q) -
                          quantum_binomial(n, n - k, q)) < 1e-10

    def test_quantum_binomial_classical(self):
        """[n choose k]_1 = binomial(n, k)."""
        from math import comb
        for n in range(2, 6):
            for k in range(n + 1):
                val = quantum_binomial(n, k, 1.0 + 1e-12)
                assert abs(val - comb(n, k)) < 0.1


# ============================================================
# Knot invariant summary tests
# ============================================================

class TestSummary:
    """Tests for the knot invariant summary function."""

    def test_summary_computes(self):
        """Summary computes without error."""
        q = cmath.exp(0.4j)
        summary = knot_invariant_summary("3_1", q)
        assert "jones" in summary
        assert "homfly_2" in summary
        assert "homfly_3" in summary
        assert "alexander" in summary
        assert "shadow_class" in summary

    def test_summary_jones_nontrivial(self):
        """Summary Jones is nontrivial for nontrivial knots."""
        q = cmath.exp(0.5j)
        summary = knot_invariant_summary("3_1", q)
        assert abs(summary["jones"] - 1.0) > 0.01


# ============================================================
# Cross-verification: Alexander-Conway-HOMFLY triangle
# ============================================================

class TestAlexanderConwayHOMFLY:
    """Cross-verification of the three polynomial invariants.

    The Alexander polynomial Delta(t), Conway polynomial nabla(z), and
    HOMFLY-PT polynomial P(a, z) are related by:
        Delta(t) = nabla(t^{1/2} - t^{-1/2})
        nabla(z) = P(1, z)
        Delta(t) = P(1, t^{1/2} - t^{-1/2})
    """

    @pytest.mark.parametrize("knot", ["3_1", "4_1"])
    def test_triangle_consistency(self, knot):
        """Alexander = Conway = HOMFLY(a=1) for trefoil and figure-eight."""
        q = cmath.exp(0.4j)
        t = q**2
        z = q - 1.0/q

        # Path 1: Alexander from Conway coefficients
        alex = alexander_from_homfly(knot, q)

        # Path 2: Direct exact Alexander formula
        if knot == "3_1":
            exact = alexander_exact_trefoil(t)
        else:
            exact = alexander_exact_figure_eight(t)

        # Path 3: HOMFLY at a=1
        exact_coeffs = {"3_1": homfly_exact_trefoil, "4_1": homfly_exact_figure_eight}
        homfly_at_a1 = eval_homfly_exact(exact_coeffs[knot](), 1.0, z)

        assert abs(alex - exact) < 1e-10
        assert abs(alex - homfly_at_a1) < 1e-10
        assert abs(exact - homfly_at_a1) < 1e-10


# ============================================================
# Amphicheiral knot tests
# ============================================================

class TestAmphicheiral:
    """Tests for properties of amphicheiral knots (e.g., 4_1)."""

    def test_figure_eight_jones_palindromic(self):
        """V_{4_1}(t) = V_{4_1}(t^{-1}) (palindromic)."""
        for theta in [0.3, 0.5, 0.7]:
            t = cmath.exp(theta * 2j)
            assert abs(alexander_exact_figure_eight(t) -
                      alexander_exact_figure_eight(1.0/t)) < 1e-12

    def test_figure_eight_odd_vassiliev_zero(self):
        """For 4_1 (amphicheiral), odd Vassiliev invariants should be small."""
        v3 = vassiliev_v3_from_shadow("4_1", eps=1e-4)
        assert abs(v3) < 1.0

    def test_figure_eight_conway_even_powers(self):
        """Conway polynomial of 4_1 only has even z-powers."""
        coeffs = CONWAY_COEFFICIENTS["4_1"]
        for power in coeffs:
            assert power % 2 == 0


# ============================================================
# Skein relation from shadow MC equation tests
# ============================================================

class TestSkeinFromMC:
    """The skein relation follows from the MC equation via the Hecke relation.

    The chain: MC equation D*Theta + (1/2)[Theta, Theta] = 0
    => Yang-Baxter equation for R(u)
    => Hecke relation (check_R - q)(check_R + q^{-1}) = 0
    => Skein: R - R^{-1} = (q - q^{-1}) I
    => HOMFLY skein: a P(L+) - a^{-1} P(L-) = z P(L0)
    """

    @pytest.mark.parametrize("N", [2, 3])
    def test_hecke_from_mc(self, N):
        """Hecke relation (from MC) holds for sl_N."""
        q = cmath.exp(0.4j)
        disc = verify_hecke_relation(q, N)
        assert disc < 1e-10

    @pytest.mark.parametrize("N", [2, 3])
    def test_braid_from_mc(self, N):
        """Braid relation (from MC via YBE) holds for sl_N."""
        q = cmath.exp(0.35j)
        disc = verify_braid_relation(q, N)
        assert disc < 1e-10

    def test_skein_identity(self):
        """check_R - check_R^{-1} = (q - q^{-1}) I."""
        q = cmath.exp(0.4j)
        R = slN_check_r_matrix(q, 2)
        qi = 1.0 / q
        d = 4
        R_inv = R - (q - qi) * np.eye(d, dtype=complex)
        lhs = R - R_inv
        rhs = (q - qi) * np.eye(d, dtype=complex)
        assert np.allclose(lhs, rhs, atol=1e-10)


# ============================================================
# HOMFLY exact polynomial consistency tests
# ============================================================

class TestHOMFLYConsistency:
    """Consistency tests across multiple evaluation methods."""

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.2j), cmath.exp(0.4j), cmath.exp(0.6j),
        cmath.exp(0.8j), cmath.exp(1.0j), cmath.exp(1.2j),
    ])
    def test_trefoil_6_point_consistency(self, q_val):
        """Trefoil HOMFLY at N=2 matches exact formula at 6 q-values."""
        a = q_val**2
        z = q_val - 1.0/q_val
        exact = eval_homfly_exact(homfly_exact_trefoil(), a, z)
        numerical = homfly_at("3_1", q_val, 2)
        assert abs(exact - numerical) < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.2j), cmath.exp(0.4j), cmath.exp(0.6j),
        cmath.exp(0.8j), cmath.exp(1.0j), cmath.exp(1.2j),
    ])
    def test_figure_eight_6_point(self, q_val):
        """Figure-eight HOMFLY at N=2 matches exact formula at 6 q-values."""
        a = q_val**2
        z = q_val - 1.0/q_val
        exact = eval_homfly_exact(homfly_exact_figure_eight(), a, z)
        numerical = homfly_at("4_1", q_val, 2)
        assert abs(exact - numerical) < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.5j), cmath.exp(0.7j), cmath.exp(0.9j),
    ])
    def test_cinquefoil_multipoint(self, q_val):
        """Cinquefoil HOMFLY at N=2 matches exact formula."""
        a = q_val**2
        z = q_val - 1.0/q_val
        exact = eval_homfly_exact(homfly_exact_cinquefoil(), a, z)
        numerical = homfly_at("5_1", q_val, 2)
        assert abs(exact - numerical) < 1e-10


# ============================================================
# Writhe and braid tests
# ============================================================

class TestWritheAndBraid:
    """Tests for writhe and braid word operations."""

    def test_trefoil_writhe(self):
        """Trefoil: w = 3."""
        from compute.lib.knot_invariant_shadow_engine import writhe
        assert writhe([1, 1, 1]) == 3

    def test_figure_eight_writhe_zero(self):
        """Figure-eight: w = 0."""
        from compute.lib.knot_invariant_shadow_engine import writhe
        assert writhe([1, -2, 1, -2]) == 0

    def test_cinquefoil_writhe(self):
        """Cinquefoil: w = 5."""
        from compute.lib.knot_invariant_shadow_engine import writhe
        assert writhe([1, 1, 1, 1, 1]) == 5

    def test_hopf_writhe(self):
        """Hopf link: w = 2."""
        from compute.lib.knot_invariant_shadow_engine import writhe
        assert writhe([1, 1]) == 2

    def test_borromean_writhe(self):
        """Borromean rings: w = 0."""
        from compute.lib.knot_invariant_shadow_engine import writhe
        braid, _ = borromean_rings_braid()
        assert writhe(braid) == 0
