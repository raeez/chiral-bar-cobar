"""Tests for the bipartite (polarized) shadow graph algebra.

Verifies conj:nms-quartic-lift from nonlinear_modular_shadows.tex:
  The shadow package (H_A, C_A, Q_A) is precisely the zero-internal-edge
  truncation of the polarized universal class Theta^pm_A through arity 4.

Test organization:
  1. Bipartite vanishing theorem (same-colour propagators vanish)
  2. Shadow data for all four standard families
  3. Zero-internal-edge truncation = shadow package (the conjecture)
  4. Finite-depth truncation exactness
  5. Exchange diagrams and total quartic
  6. Genus-1 loop corrections
  7. Cross-family consistency

Ground truth:
  - nonlinear_modular_shadows.tex: conj:nms-quartic-lift,
    conj:nms-bipartite-vanishing, thm:nms-bipartite-complementarity,
    rem:nms-implementation-path
  - modular_shadow_tower.py: Virasoro shadow data
  - virasoro_quartic_contact.py: Q^contact_Vir = 10/[c(5c+22)]
  - genus_expansion.py: kappa formulas
  - betagamma_quartic_contact.py: mu_{bg} = 0
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, expand, factor

from compute.lib.bipartite_shadow import (
    # Data structures
    BipartiteVertex, BipartiteEdge, BipartiteGraph,
    PolarizedPropagator,
    COLOUR_PLUS, COLOUR_MINUS,
    # Shadow data constructors
    ShadowData,
    heisenberg_shadow,
    affine_sl2_shadow,
    affine_shadow_general,
    betagamma_shadow,
    virasoro_shadow,
    # Polarized MC element
    theta_pm_zero_edge,
    theta_pm_one_edge,
    theta_pm_through_arity,
    # Truncation and comparison
    shadow_package_from_theta,
    theta_truncation_matches_shadow,
    finite_depth_truncation_exact,
    # Exchange diagrams
    cubic_exchange_quartic,
    total_quartic_from_theta,
    # Graph weight
    graph_weight,
    # Bipartite vanishing
    verify_bipartite_vanishing,
    # Genus-1
    genus1_loop_correction,
    genus1_loop_ratio,
    # Kappa
    kappa_from_hessian_trace,
)


c = Symbol('c')
k = Symbol('k')


# ====================================================================
# 1. Bipartite vanishing theorem
# ====================================================================

class TestBipartiteVanishing:
    """Verify conj:nms-bipartite-vanishing / thm:nms-bipartite-complementarity:
    same-colour propagators vanish identically."""

    def test_same_colour_vanishes_scalar(self):
        """P^{++} = P^{--} = 0 for scalar B."""
        result = verify_bipartite_vanishing(Rational(3))
        assert result['bipartite_vanishing'] is True

    def test_mixed_propagator_nonzero_scalar(self):
        """P^{+-} != 0 for nonzero B."""
        result = verify_bipartite_vanishing(Rational(3))
        assert result['mixed_nonzero'] is True

    def test_mixed_propagator_value(self):
        """P^{+-} = 1/B for scalar B."""
        result = verify_bipartite_vanishing(Rational(5))
        assert result['P_mixed'] == Rational(1, 5)

    def test_same_colour_vanishes_symbolic(self):
        """Bipartite vanishing holds for symbolic B."""
        result = verify_bipartite_vanishing(c / 2)
        assert result['bipartite_vanishing'] is True
        assert simplify(result['P_mixed'] - 2 / c) == 0

    def test_same_colour_edge_graph_zero_weight(self):
        """A graph with same-colour edge has zero weight."""
        v1 = BipartiteVertex(COLOUR_PLUS, 3, 0)
        v2 = BipartiteVertex(COLOUR_PLUS, 3, 0)  # SAME colour
        e = BipartiteEdge(0, 1)
        g = BipartiteGraph([v1, v2], [e])
        assert not g.is_bipartite()

    def test_opposite_colour_edge_valid(self):
        """A graph with opposite-colour edge is bipartite."""
        v1 = BipartiteVertex(COLOUR_PLUS, 3, 0)
        v2 = BipartiteVertex(COLOUR_MINUS, 3, 0)
        e = BipartiteEdge(0, 1)
        g = BipartiteGraph([v1, v2], [e])
        assert g.is_bipartite()


# ====================================================================
# 2. Shadow data for four standard families
# ====================================================================

class TestHeisenbergShadow:
    """Heisenberg: Gaussian archetype, depth 2."""

    def test_depth(self):
        assert heisenberg_shadow().depth == 2

    def test_archetype(self):
        assert heisenberg_shadow().archetype == 'G'

    def test_hessian(self):
        s = heisenberg_shadow()
        assert simplify(s.H - c / 2) == 0

    def test_cubic_vanishes(self):
        """No cubic shadow: abelian algebra, no Lie bracket."""
        assert heisenberg_shadow().C == 0

    def test_quartic_vanishes(self):
        """No quartic shadow: tower terminates at arity 2."""
        assert heisenberg_shadow().Q == 0

    def test_kappa(self):
        """kappa(Heis_c) = c/2."""
        s = heisenberg_shadow()
        assert simplify(s.kappa - c / 2) == 0

    def test_kappa_numeric(self):
        """kappa(Heis_1) = 1/2."""
        s = heisenberg_shadow(c=1)
        assert s.kappa == Rational(1, 2)


class TestAffineSl2Shadow:
    """Affine sl_2: Lie/tree archetype, depth 3."""

    def test_depth(self):
        assert affine_sl2_shadow().depth == 3

    def test_archetype(self):
        assert affine_sl2_shadow().archetype == 'L'

    def test_hessian(self):
        s = affine_sl2_shadow()
        assert simplify(s.H - k) == 0

    def test_cubic_nonzero(self):
        """Cubic shadow nonzero: Lie bracket gives structure constants."""
        s = affine_sl2_shadow()
        assert s.C != 0

    def test_quartic_vanishes(self):
        """Quartic contact = 0: Jacobi identity kills the obstruction."""
        assert affine_sl2_shadow().Q == 0

    def test_kappa_formula(self):
        """kappa(sl_2_k) = 3(k+2)/4."""
        s = affine_sl2_shadow()
        expected = 3 * (k + 2) / 4
        assert simplify(s.kappa - expected) == 0

    def test_kappa_numeric_k1(self):
        """kappa(sl_2_1) = 3*3/4 = 9/4."""
        s = affine_sl2_shadow(k=1)
        assert s.kappa == Rational(9, 4)

    def test_kappa_numeric_k2(self):
        """kappa(sl_2_2) = 3*4/4 = 3."""
        s = affine_sl2_shadow(k=2)
        assert s.kappa == Rational(3)


class TestBetagammaShadow:
    """Beta-gamma: contact archetype, depth 4."""

    def test_depth(self):
        assert betagamma_shadow().depth == 4

    def test_archetype(self):
        assert betagamma_shadow().archetype == 'C'

    def test_cubic_vanishes_on_weight_line(self):
        """On the weight-changing line, cubic vanishes (rank-one abelian)."""
        assert betagamma_shadow().C == 0

    def test_quartic_vanishes_on_weight_line(self):
        """mu_bg = 0 on the weight-changing line (rank-one rigidity).
        Ground truth: betagamma_quartic_contact.py, cor:nms-betagamma-mu-vanishing."""
        assert betagamma_shadow().Q == 0

    def test_kappa(self):
        """kappa(bg_c) = c/2 (same as Heisenberg for c=2)."""
        s = betagamma_shadow()
        assert simplify(s.kappa - c / 2) == 0


class TestVirasoroShadow:
    """Virasoro: mixed archetype, depth infinity."""

    def test_depth_infinite(self):
        assert virasoro_shadow().depth == float('inf')

    def test_archetype(self):
        assert virasoro_shadow().archetype == 'M'

    def test_hessian(self):
        s = virasoro_shadow()
        assert simplify(s.H - c / 2) == 0

    def test_cubic(self):
        """C_Vir = 2 (from T_(1)T = 2T)."""
        assert virasoro_shadow().C == 2

    def test_quartic_contact(self):
        """Q^contact_Vir = 10/[c(5c+22)].
        Ground truth: virasoro_quartic_contact.py."""
        s = virasoro_shadow()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(s.Q - expected) == 0

    def test_kappa(self):
        """kappa(Vir_c) = c/2."""
        s = virasoro_shadow()
        assert simplify(s.kappa - c / 2) == 0

    def test_quartic_numeric_c1(self):
        """Q^contact_Vir(c=1) = 10/(1*27) = 10/27."""
        s = virasoro_shadow(c=1)
        assert s.Q == Rational(10, 27)

    def test_quartic_numeric_c26(self):
        """Q^contact_Vir(c=26) = 10/(26*152) = 10/3952 = 5/1976."""
        s = virasoro_shadow(c=26)
        assert s.Q == Rational(10, 3952)


# ====================================================================
# 3. conj:nms-quartic-lift: zero-edge truncation = shadow package
# ====================================================================

class TestQuarticLiftConjecture:
    """The core conjecture: zero-internal-edge truncation of Theta^pm
    through arity 4 equals the shadow package (H, C, Q)."""

    def test_heisenberg_truncation_matches(self):
        """Heisenberg: zero-edge truncation = (c/2, 0, 0)."""
        result = theta_truncation_matches_shadow(heisenberg_shadow())
        assert all(result.values())

    def test_affine_truncation_matches(self):
        """Affine sl_2: zero-edge truncation = (k, 2/k, 0)."""
        result = theta_truncation_matches_shadow(affine_sl2_shadow())
        assert all(result.values())

    def test_betagamma_truncation_matches(self):
        """Beta-gamma: zero-edge truncation = (c/2, 0, 0)."""
        result = theta_truncation_matches_shadow(betagamma_shadow())
        assert all(result.values())

    def test_virasoro_truncation_matches(self):
        """Virasoro: zero-edge truncation = (c/2, 2, 10/[c(5c+22)])."""
        result = theta_truncation_matches_shadow(virasoro_shadow())
        assert all(result.values())

    def test_truncation_matches_per_arity(self):
        """Check each arity separately for all families."""
        for family_fn in [heisenberg_shadow, affine_sl2_shadow,
                          betagamma_shadow, virasoro_shadow]:
            shadow = family_fn()
            theta = theta_pm_zero_edge(shadow, max_arity=4)
            assert simplify(theta[2] - shadow.H) == 0, \
                f"{shadow.name}: arity-2 mismatch"
            assert simplify(theta[3] - shadow.C) == 0, \
                f"{shadow.name}: arity-3 mismatch"
            assert simplify(theta[4] - shadow.Q) == 0, \
                f"{shadow.name}: arity-4 mismatch"

    def test_affine_general_sl3(self):
        """Affine sl_3: kappa = 8(k+3)/6 = 4(k+3)/3."""
        shadow = affine_shadow_general(dim_g=8, h_dual=3)
        expected_kappa = Rational(8) * (k + 3) / (2 * 3)
        assert simplify(shadow.kappa - expected_kappa) == 0
        result = theta_truncation_matches_shadow(shadow)
        assert all(result.values())


# ====================================================================
# 4. Finite-depth truncation exactness
# ====================================================================

class TestFiniteDepthExactness:
    """For algebras of depth <= r, Theta^pm_{<=r} = Theta^pm exactly."""

    def test_heisenberg_depth2_exact(self):
        """Heisenberg: depth 2, truncation at arity 2 is exact."""
        assert finite_depth_truncation_exact(heisenberg_shadow())

    def test_affine_depth3_exact(self):
        """Affine: depth 3, truncation at arity 3 is exact."""
        assert finite_depth_truncation_exact(affine_sl2_shadow())

    def test_betagamma_depth4_exact(self):
        """Beta-gamma: depth 4, truncation at arity 4 is exact.
        (On the weight-changing line, C=Q=0.)"""
        assert finite_depth_truncation_exact(betagamma_shadow())

    def test_virasoro_infinite_not_exact(self):
        """Virasoro: depth infinity, truncation is NOT exact."""
        assert not finite_depth_truncation_exact(virasoro_shadow())

    def test_depth2_implies_no_cubic_or_quartic(self):
        """Depth 2 means C = 0 and Q = 0."""
        s = heisenberg_shadow()
        assert s.C == 0 and s.Q == 0

    def test_depth3_implies_no_quartic(self):
        """Depth 3 means Q = 0 (but C can be nonzero)."""
        s = affine_sl2_shadow()
        assert s.Q == 0 and s.C != 0


# ====================================================================
# 5. Exchange diagrams
# ====================================================================

class TestExchangeDiagrams:
    """One-edge bipartite graphs: the cubic exchange quartic C *_P C."""

    def test_heisenberg_exchange_zero(self):
        """Heisenberg: no cubic => no exchange quartic."""
        assert cubic_exchange_quartic(heisenberg_shadow()) == 0

    def test_affine_exchange_nonzero(self):
        """Affine: C *_P C = (2/k)^2 * (1/k) = 4/k^3.
        Cubic coefficient = 2/k, propagator = 1/H = 1/k."""
        s = affine_sl2_shadow()
        expected = Rational(4) / k**3
        assert simplify(cubic_exchange_quartic(s) - expected) == 0

    def test_virasoro_exchange(self):
        """Virasoro: C *_P C = 2 * 2 * (2/c) = 8/c."""
        s = virasoro_shadow()
        expected = Rational(8) / c
        assert simplify(cubic_exchange_quartic(s) - expected) == 0

    def test_virasoro_total_quartic(self):
        """Total quartic = Q + C*_P*C for Virasoro."""
        s = virasoro_shadow()
        total = total_quartic_from_theta(s)
        expected_contact = Rational(10) / (c * (5 * c + 22))
        expected_exchange = Rational(8) / c
        expected = expected_contact + expected_exchange
        assert simplify(total - expected) == 0

    def test_affine_total_quartic_equals_exchange(self):
        """Affine: Q = 0, so total quartic = exchange only."""
        s = affine_sl2_shadow()
        total = total_quartic_from_theta(s)
        exchange = cubic_exchange_quartic(s)
        assert simplify(total - exchange) == 0

    def test_exchange_bipartite_structure(self):
        """The exchange diagram is a bipartite graph: + vertex -> - vertex."""
        v_plus = BipartiteVertex(COLOUR_PLUS, 3, 0, label="cubic+")
        v_minus = BipartiteVertex(COLOUR_MINUS, 3, 0, label="cubic-")
        edge = BipartiteEdge(0, 1)
        g = BipartiteGraph([v_plus, v_minus], [edge])
        assert g.is_bipartite()
        assert g.total_arity == 4  # 3 + 3 - 2 = 4
        assert g.loop_genus == 0   # tree-level
        assert g.is_connected


# ====================================================================
# 6. Genus-1 loop corrections
# ====================================================================

class TestGenus1Loop:
    """Genus-1 Hessian corrections from the bipartite genus loop."""

    def test_virasoro_genus1_correction(self):
        """delta_H^(1)_Vir = 120/[c^2(5c+22)].
        Ground truth: modular_shadow_tower.py."""
        s = virasoro_shadow()
        corr = genus1_loop_correction(s)
        expected = Rational(120) / (c**2 * (5 * c + 22))
        assert simplify(corr - expected) == 0

    def test_virasoro_genus1_ratio(self):
        """rho^(1)_Vir = 240/[c^3(5c+22)]."""
        s = virasoro_shadow()
        ratio = genus1_loop_ratio(s)
        expected = Rational(240) / (c**3 * (5 * c + 22))
        assert simplify(ratio - expected) == 0

    def test_heisenberg_no_genus1_correction(self):
        """Heisenberg: Q = 0, so no genus-1 loop correction."""
        assert genus1_loop_correction(heisenberg_shadow()) == 0

    def test_affine_no_genus1_correction(self):
        """Affine: Q = 0, so no genus-1 loop correction from quartic."""
        assert genus1_loop_correction(affine_sl2_shadow()) == 0


# ====================================================================
# 7. Cross-family consistency
# ====================================================================

class TestCrossFamilyConsistency:
    """Consistency checks across families."""

    def test_kappa_agrees_with_genus_expansion(self):
        """kappa values agree with genus_expansion.py formulas.

        kappa(Heis_c) = c/2
        kappa(Vir_c) = c/2
        kappa(sl_2_k) = 3(k+2)/4
        """
        assert simplify(heisenberg_shadow().kappa - c / 2) == 0
        assert simplify(virasoro_shadow().kappa - c / 2) == 0
        assert simplify(affine_sl2_shadow().kappa - 3 * (k + 2) / 4) == 0

    def test_shadow_depth_ordering(self):
        """G < L < C < M in shadow depth."""
        depths = [
            heisenberg_shadow().depth,   # 2
            affine_sl2_shadow().depth,    # 3
            betagamma_shadow().depth,     # 4
        ]
        assert depths == sorted(depths)
        assert virasoro_shadow().depth == float('inf')

    def test_archetype_classification(self):
        """Archetype labels: G, L, C, M."""
        assert heisenberg_shadow().archetype == 'G'
        assert affine_sl2_shadow().archetype == 'L'
        assert betagamma_shadow().archetype == 'C'
        assert virasoro_shadow().archetype == 'M'

    def test_heisenberg_betagamma_kappa_agreement(self):
        """Heisenberg and beta-gamma have the same kappa = c/2.
        (Standard beta-gamma has c = 2.)"""
        h = heisenberg_shadow()
        bg = betagamma_shadow()
        assert simplify(h.kappa - bg.kappa) == 0

    def test_all_families_pass_quartic_lift(self):
        """All four families satisfy conj:nms-quartic-lift."""
        for fn in [heisenberg_shadow, affine_sl2_shadow,
                   betagamma_shadow, virasoro_shadow]:
            result = theta_truncation_matches_shadow(fn())
            assert all(result.values()), f"Quartic lift failed for {fn().name}"


# ====================================================================
# 8. Graph data structure tests
# ====================================================================

class TestGraphStructure:
    """Structural properties of bipartite graphs."""

    def test_single_vertex_connected(self):
        v = BipartiteVertex(COLOUR_PLUS, 3, 0)
        g = BipartiteGraph([v], [])
        assert g.is_connected
        assert g.total_arity == 3
        assert g.loop_genus == 0

    def test_two_vertex_one_edge(self):
        v1 = BipartiteVertex(COLOUR_PLUS, 3, 0)
        v2 = BipartiteVertex(COLOUR_MINUS, 3, 0)
        e = BipartiteEdge(0, 1)
        g = BipartiteGraph([v1, v2], [e])
        assert g.is_connected
        assert g.total_arity == 4
        assert g.loop_genus == 0

    def test_loop_graph(self):
        """Two vertices connected by two edges: loop genus 1."""
        v1 = BipartiteVertex(COLOUR_PLUS, 2, 0)
        v2 = BipartiteVertex(COLOUR_MINUS, 2, 0)
        e1 = BipartiteEdge(0, 1)
        e2 = BipartiteEdge(0, 1)
        g = BipartiteGraph([v1, v2], [e1, e2])
        assert g.is_connected
        assert g.loop_genus == 1  # 2 - 2 + 1 = 1
        assert g.total_arity == 0  # 2 + 2 - 4 = 0

    def test_invalid_same_colour(self):
        """Same-colour edge detected by is_bipartite."""
        v1 = BipartiteVertex(COLOUR_MINUS, 2, 0)
        v2 = BipartiteVertex(COLOUR_MINUS, 2, 0)
        e = BipartiteEdge(0, 1)
        g = BipartiteGraph([v1, v2], [e])
        assert not g.is_bipartite()

    def test_vertex_colour_validation(self):
        """Invalid colour raises ValueError."""
        with pytest.raises(ValueError):
            BipartiteVertex('red', 2, 0)

    def test_self_loop_rejected(self):
        """Self-loop raises ValueError."""
        with pytest.raises(ValueError):
            BipartiteEdge(0, 0)

    def test_graph_weight_bipartite_check(self):
        """Graph weight returns 0 for non-bipartite graph."""
        v1 = BipartiteVertex(COLOUR_PLUS, 3, 0)
        v2 = BipartiteVertex(COLOUR_PLUS, 3, 0)
        e = BipartiteEdge(0, 1)
        g = BipartiteGraph([v1, v2], [e])
        prop = PolarizedPropagator(Rational(1))
        w = graph_weight(g, {0: Rational(2), 1: Rational(3)}, prop)
        assert w == 0


# ====================================================================
# 9. Numeric spot checks
# ====================================================================

class TestNumericSpotChecks:
    """Numeric evaluations at specific parameter values."""

    def test_virasoro_quartic_c1(self):
        """Q^contact_Vir(c=1) = 10/27."""
        s = virasoro_shadow(c=1)
        assert s.Q == Rational(10, 27)

    def test_virasoro_quartic_c13_self_dual(self):
        """At c=13 (self-dual point): Q = 10/(13*87) = 10/1131."""
        s = virasoro_shadow(c=13)
        assert s.Q == Rational(10, 1131)

    def test_affine_kappa_k1(self):
        """kappa(sl_2, k=1) = 9/4."""
        s = affine_sl2_shadow(k=1)
        assert s.kappa == Rational(9, 4)

    def test_virasoro_genus1_correction_c1(self):
        """delta_H^(1)(c=1) = 120/(1*27) = 40/9."""
        s = virasoro_shadow(c=1)
        corr = genus1_loop_correction(s)
        assert corr == Rational(40, 9)

    def test_virasoro_exchange_c1(self):
        """C*_P*C at c=1: 8/1 = 8."""
        s = virasoro_shadow(c=1)
        assert cubic_exchange_quartic(s) == Rational(8)

    def test_virasoro_total_quartic_c26(self):
        """Total quartic at c=26 = 10/(26*152) + 8/26."""
        s = virasoro_shadow(c=26)
        total = total_quartic_from_theta(s)
        expected = Rational(10, 3952) + Rational(8, 26)
        assert total == expected
