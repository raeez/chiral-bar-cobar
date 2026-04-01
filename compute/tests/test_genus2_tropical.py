r"""Tests for compute/lib/genus2_tropical.py.

Tropical geometry adversarial cross-check of the genus-2 free energy F_2.

Three independent verification axes:

AXIS 1 (COMBINATORIAL): Graph enumeration, automorphism orders, stability,
    genus, Betti numbers. These are COMBINATORIAL INVARIANTS that can be
    verified independently of any algebra.

AXIS 2 (TOPOLOGICAL): Orbifold Euler characteristics chi^orb(M_{g,n}),
    the graph-vertex-product formula, and chi^orb(M-bar_2). These are
    TOPOLOGICAL invariants with known values from Harer-Zagier.

AXIS 3 (ALGEBRAIC): Free energy F_2 = kappa * lambda_2^FP across families,
    complementarity, additivity, and the multi-channel W_3 graph sum.
    These test the ALGEBRAIC content of Theorem D.

Test count: 106 tests across 11 test classes.

AP1:  kappa formulas independently recomputed for each family.
AP5:  Cross-checked against existing engines (genus2_landscape, higher_genus_graph_sum_engine).
AP8:  Virasoro complementarity at c=13 (self-dual point, NOT c=26).
AP10: Cross-family structural checks (additivity, linearity, complementarity)
      are the real verification, not hardcoded expected values alone.
AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

import pytest
from fractions import Fraction

from compute.lib.genus2_tropical import (
    # Bernoulli / lambda_fp
    _bernoulli,
    lambda_fp,
    # Euler characteristics
    chi_orb_open,
    # Graph enumeration
    TropicalGraph,
    genus2_graphs,
    graph_euler_contribution,
    chi_orb_mbar2_tropical,
    chi_orb_mbar2_decomposition,
    # Kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_w3,
    kappa_w3_channels,
    kappa_betagamma,
    # F_2 computations
    F2,
    F2_heisenberg,
    F2_virasoro,
    F2_affine_sl2,
    F2_w3,
    scalar_graph_sum_F2,
    # W_3 multi-channel
    w3_propagator,
    w3_C3,
    w3_graph_amplitude,
    w3_graph_sum_all_channels,
    w3_F2_multichannel,
    w3_channel_enumeration,
    # Verification
    verify_graph_enumeration,
    verify_chi_orb,
    verify_chi_mbar2,
    verify_F2_cross_family,
    inverse_aut_sum,
    edge_count_spectrum,
    h1_spectrum,
    scalar_sum_polynomial,
    full_adversarial_comparison,
)


# ============================================================================
# AXIS 1: Combinatorial — graph enumeration
# ============================================================================

class TestGraphEnumeration:
    """Verify the 6 genus-2 stable graphs and their combinatorial data."""

    def test_exactly_6_graphs(self):
        """There are exactly 6 stable graphs at (g=2, n=0)."""
        assert len(genus2_graphs()) == 6

    def test_all_genus_2(self):
        """Every graph has arithmetic genus 2."""
        for g in genus2_graphs():
            assert g.arithmetic_genus == 2, f"{g.name} has genus {g.arithmetic_genus}"

    def test_all_stable(self):
        """Every graph satisfies the stability condition 2g_v - 2 + val_v > 0."""
        for g in genus2_graphs():
            assert g.is_stable, f"{g.name} is not stable"

    def test_names_unique(self):
        """All graph names are distinct."""
        names = [g.name for g in genus2_graphs()]
        assert len(names) == len(set(names))

    def test_smooth_g2(self):
        """Smooth genus-2 curve: 1 vertex g=2, no edges."""
        g = next(x for x in genus2_graphs() if x.name == 'smooth_g2')
        assert g.vertex_genera == (2,)
        assert g.num_edges == 0
        assert g.first_betti == 0
        assert g.aut_order == 1
        assert g.valences == (0,)

    def test_figure_eight(self):
        """Figure-eight: 1 vertex g=1, 1 self-loop."""
        g = next(x for x in genus2_graphs() if x.name == 'figure_eight')
        assert g.vertex_genera == (1,)
        assert g.num_edges == 1
        assert g.first_betti == 1
        assert g.aut_order == 2
        assert g.valences == (2,)

    def test_banana(self):
        """Banana (double self-loop): 1 vertex g=0, 2 self-loops."""
        g = next(x for x in genus2_graphs() if x.name == 'banana')
        assert g.vertex_genera == (0,)
        assert g.num_edges == 2
        assert g.first_betti == 2
        assert g.aut_order == 8
        assert g.valences == (4,)

    def test_dumbbell(self):
        """Dumbbell: 2 vertices g=1, 1 edge."""
        g = next(x for x in genus2_graphs() if x.name == 'dumbbell')
        assert g.vertex_genera == (1, 1)
        assert g.num_edges == 1
        assert g.first_betti == 0
        assert g.aut_order == 2
        assert g.valences == (1, 1)

    def test_theta(self):
        """Theta graph: 2 vertices g=0, 3 parallel edges."""
        g = next(x for x in genus2_graphs() if x.name == 'theta')
        assert g.vertex_genera == (0, 0)
        assert g.num_edges == 3
        assert g.first_betti == 2
        assert g.aut_order == 12
        assert g.valences == (3, 3)

    def test_mixed(self):
        """Mixed: vertex g=0 (self-loop + bridge) -- vertex g=1."""
        g = next(x for x in genus2_graphs() if x.name == 'mixed')
        assert g.vertex_genera == (0, 1)
        assert g.num_edges == 2
        assert g.first_betti == 1
        assert g.aut_order == 2
        assert g.valences == (3, 1)

    def test_edge_count_spectrum(self):
        """Edge count ranges from 0 (smooth) to 3 (theta)."""
        spec = edge_count_spectrum()
        assert spec == {
            0: ['smooth_g2'],
            1: ['figure_eight', 'dumbbell'],
            2: ['banana', 'mixed'],
            3: ['theta'],
        }

    def test_h1_spectrum(self):
        """Betti number h^1 ranges from 0 to 2."""
        spec = h1_spectrum()
        assert 0 in spec
        assert 1 in spec
        assert 2 in spec
        assert 'smooth_g2' in spec[0]
        assert 'dumbbell' in spec[0]
        assert 'theta' in spec[2]
        assert 'banana' in spec[2]

    def test_codimension_correct(self):
        """Codimension = number of edges = number of nodes on the curve."""
        for g in genus2_graphs():
            assert g.codimension == g.num_edges
            assert g.stratum_dimension == 3 - g.num_edges

    def test_verify_graph_enumeration(self):
        """Full verification function passes all checks."""
        result = verify_graph_enumeration()
        assert result['count_correct']
        assert result['all_genus_2']
        assert result['all_stable']
        for name, details in result['details'].items():
            assert details['genus_correct'], f"{name} genus wrong"
            assert details['h1_correct'], f"{name} h1 wrong"
            assert details['aut_correct'], f"{name} aut wrong"


# ============================================================================
# AXIS 2: Topological — orbifold Euler characteristics
# ============================================================================

class TestOrbifoldEuler:
    """Verify chi^orb(M_{g,n}) values from first principles."""

    def test_M03(self):
        """chi^orb(M_{0,3}) = 1. M-bar_{0,3} is a point."""
        assert chi_orb_open(0, 3) == Fraction(1)

    def test_M04(self):
        """chi^orb(M_{0,4}) = -1. M-bar_{0,4} = P^1, chi^top = 2, but open has chi = -1."""
        assert chi_orb_open(0, 4) == Fraction(-1)

    def test_M11(self):
        """chi^orb(M_{1,1}) = -1/12 (Harer-Zagier)."""
        assert chi_orb_open(1, 1) == Fraction(-1, 12)

    def test_M12(self):
        """chi^orb(M_{1,2}) = (2-2+1) * chi(M_{1,1}) = -1/12."""
        assert chi_orb_open(1, 2) == Fraction(-1, 12)

    def test_M20(self):
        """chi^orb(M_{2,0}) = B_4/(4*2*1) = (-1/30)/8 = -1/240."""
        assert chi_orb_open(2, 0) == Fraction(-1, 240)

    def test_M13(self):
        """chi^orb(M_{1,3}) = (2-2+2) * chi(M_{1,2}) = 2 * (-1/12) = -1/6."""
        assert chi_orb_open(1, 3) == Fraction(-1, 6)

    def test_M05(self):
        """chi^orb(M_{0,5}) = (-1)^4 * 2! = 2."""
        assert chi_orb_open(0, 5) == Fraction(2)

    def test_unstable_raises(self):
        """Unstable moduli (2g-2+n <= 0) raise ValueError."""
        with pytest.raises(ValueError):
            chi_orb_open(0, 2)
        with pytest.raises(ValueError):
            chi_orb_open(1, 0)
        with pytest.raises(ValueError):
            chi_orb_open(0, 1)

    def test_verify_chi_orb(self):
        """Full verification function passes."""
        result = verify_chi_orb()
        for key, data in result.items():
            assert data['match'], f"chi^orb mismatch at {key}"


class TestChiMbar2:
    """Verify chi^orb(M-bar_2) via the graph-vertex-product formula."""

    def test_chi_mbar2_computation(self):
        """chi^orb(M-bar_2) computed from graph sum is a definite Fraction."""
        chi = chi_orb_mbar2_tropical()
        assert isinstance(chi, Fraction)

    def test_chi_mbar2_known_value(self):
        r"""chi^orb(M-bar_2) = -181/1440.

        Known from Harer-Zagier / Bini-Harer. This is the definitive
        cross-check: the graph enumeration + automorphism orders +
        vertex Euler characteristics must combine to give exactly -181/1440.
        """
        chi = chi_orb_mbar2_tropical()
        assert chi == Fraction(-181, 1440), f"chi^orb(M-bar_2) = {chi}, expected -181/1440"

    def test_individual_contributions_sum(self):
        """Sum of individual graph contributions equals total."""
        decomp = chi_orb_mbar2_decomposition()
        total_from_parts = sum(data['contribution'] for data in decomp.values())
        total_direct = chi_orb_mbar2_tropical()
        assert total_from_parts == total_direct

    def test_smooth_contribution(self):
        """Smooth genus-2 contributes chi(M_2) = -1/240."""
        decomp = chi_orb_mbar2_decomposition()
        # smooth_g2: 1 vertex (g=2, val=0), |Aut|=1
        # Contribution = chi(M_{2,0}) / 1 = -1/240
        assert decomp['smooth_g2']['contribution'] == Fraction(-1, 240)

    def test_figure_eight_contribution(self):
        """Figure-eight: chi(M_{1,2})/2 = (-1/12)/2 = -1/24."""
        decomp = chi_orb_mbar2_decomposition()
        assert decomp['figure_eight']['contribution'] == Fraction(-1, 24)

    def test_banana_contribution(self):
        """Banana: chi(M_{0,4})/8 = (-1)/8 = -1/8."""
        decomp = chi_orb_mbar2_decomposition()
        assert decomp['banana']['contribution'] == Fraction(-1, 8)

    def test_dumbbell_contribution(self):
        """Dumbbell: chi(M_{1,1})^2 / 2 = (1/144) / 2 = 1/288."""
        decomp = chi_orb_mbar2_decomposition()
        # Two genus-1 vertices each with valence 1: chi(M_{1,1}) = -1/12 each
        # Product: (-1/12)^2 = 1/144. Divided by |Aut|=2: 1/288.
        assert decomp['dumbbell']['contribution'] == Fraction(1, 288)

    def test_theta_contribution(self):
        """Theta: chi(M_{0,3})^2 / 12 = 1/12."""
        decomp = chi_orb_mbar2_decomposition()
        # Two genus-0 vertices each with valence 3: chi(M_{0,3}) = 1 each
        # Product: 1. Divided by |Aut|=12: 1/12.
        assert decomp['theta']['contribution'] == Fraction(1, 12)

    def test_mixed_contribution(self):
        """Mixed: chi(M_{0,3}) * chi(M_{1,1}) / 2 = 1 * (-1/12) / 2 = -1/24."""
        decomp = chi_orb_mbar2_decomposition()
        # Vertex 0: g=0, val=3 -> chi(M_{0,3}) = 1
        # Vertex 1: g=1, val=1 -> chi(M_{1,1}) = -1/12
        # Product: -1/12. Divided by |Aut|=2: -1/24.
        assert decomp['mixed']['contribution'] == Fraction(-1, 24)

    def test_inverse_aut_sum(self):
        """Sum of 1/|Aut| over all genus-2 graphs."""
        # 1/1 + 1/2 + 1/8 + 1/2 + 1/12 + 1/2
        # = 1 + 1/2 + 1/8 + 1/2 + 1/12 + 1/2
        # = 1 + 3/2 + 1/8 + 1/12
        # = 1 + 1/2 + 1/2 + 1/2 + 1/8 + 1/12
        # LCD = 24: 24/24 + 12/24 + 12/24 + 12/24 + 3/24 + 2/24 = 65/24
        s = inverse_aut_sum()
        expected = Fraction(1) + Fraction(1, 2) + Fraction(1, 8) + Fraction(1, 2) + Fraction(1, 12) + Fraction(1, 2)
        assert s == expected


# ============================================================================
# Bernoulli numbers and lambda_fp
# ============================================================================

class TestBernoulliLambda:
    """Independent verification of Bernoulli numbers and Faber-Pandharipande."""

    def test_B0(self):
        assert _bernoulli(0) == Fraction(1)

    def test_B1(self):
        assert _bernoulli(1) == Fraction(-1, 2)

    def test_B2(self):
        assert _bernoulli(2) == Fraction(1, 6)

    def test_B4(self):
        assert _bernoulli(4) == Fraction(-1, 30)

    def test_B6(self):
        assert _bernoulli(6) == Fraction(1, 42)

    def test_odd_bernoulli_zero(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli(n) == Fraction(0)

    def test_lambda_fp_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_fp_2_from_bernoulli(self):
        """Independent derivation: (7/8) * (1/30) / 24 = 7/5760."""
        B4 = _bernoulli(4)
        assert B4 == Fraction(-1, 30)
        lam2 = Fraction(7, 8) * abs(B4) / Fraction(24)
        assert lam2 == Fraction(7, 5760)

    def test_lambda_fp_positive(self):
        """All lambda_g^FP are positive (critical: Bernoulli sign)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        for g in range(1, 7):
            assert lambda_fp(g + 1) < lambda_fp(g)


# ============================================================================
# AXIS 3: Algebraic — kappa formulas and F_2
# ============================================================================

class TestKappaFormulas:
    """Verify kappa for each family from first principles (AP1)."""

    def test_heisenberg_k1(self):
        assert kappa_heisenberg(1) == Fraction(1)

    def test_heisenberg_k2(self):
        assert kappa_heisenberg(2) == Fraction(2)

    def test_virasoro_c1(self):
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_virasoro_c13(self):
        """Self-dual point: kappa(Vir_13) = 13/2."""
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_virasoro_c25(self):
        assert kappa_virasoro(25) == Fraction(25, 2)

    def test_virasoro_c26(self):
        """Critical dimension: kappa(Vir_26) = 13."""
        assert kappa_virasoro(26) == Fraction(13)

    def test_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4."""
        assert kappa_affine_sl2(1) == Fraction(9, 4)

    def test_sl2_k2(self):
        """kappa(sl_2, k=2) = 3*(2+2)/4 = 3."""
        assert kappa_affine_sl2(2) == Fraction(3)

    def test_w3_c2(self):
        """kappa(W_3, c=2) = 5*2/6 = 5/3."""
        assert kappa_w3(2) == Fraction(5, 3)

    def test_w3_c50(self):
        """kappa(W_3, c=50) = 5*50/6 = 125/3."""
        assert kappa_w3(50) == Fraction(125, 3)

    def test_w3_channel_decomposition(self):
        """kappa(W_3) = kappa_T + kappa_W for any c."""
        for c_val in [2, 10, 50, 100]:
            kT, kW = kappa_w3_channels(c_val)
            assert kT + kW == kappa_w3(c_val), f"Failed at c={c_val}"

    def test_betagamma(self):
        """kappa(betagamma, lambda=1) = 1."""
        assert kappa_betagamma() == Fraction(1)


class TestF2Values:
    """Verify F_2 = kappa * lambda_2^FP for each family."""

    def test_F2_heisenberg_k1(self):
        """F_2(H_1) = 7/5760."""
        assert F2_heisenberg(1) == Fraction(7, 5760)

    def test_F2_heisenberg_k2(self):
        """F_2(H_2) = 14/5760 = 7/2880."""
        assert F2_heisenberg(2) == Fraction(7, 2880)

    def test_F2_virasoro_c1(self):
        """F_2(Vir_1) = (1/2) * 7/5760 = 7/11520."""
        assert F2_virasoro(1) == Fraction(7, 11520)

    def test_F2_virasoro_c13(self):
        """F_2(Vir_13) = (13/2) * 7/5760 = 91/11520."""
        assert F2_virasoro(13) == Fraction(91, 11520)

    def test_F2_virasoro_c25(self):
        """F_2(Vir_25) = (25/2) * 7/5760 = 175/11520 = 35/2304."""
        assert F2_virasoro(25) == Fraction(35, 2304)

    def test_F2_sl2_k1(self):
        """F_2(sl_2, k=1) = (9/4) * 7/5760 = 63/23040 = 7/2560."""
        expected = Fraction(9, 4) * Fraction(7, 5760)
        assert F2_affine_sl2(1) == expected

    def test_F2_sl2_k2(self):
        """F_2(sl_2, k=2) = 3 * 7/5760 = 7/1920."""
        assert F2_affine_sl2(2) == Fraction(7, 1920)

    def test_F2_w3_c2(self):
        """F_2(W_3, c=2) = (5/3) * 7/5760 = 35/17280 = 7/3456."""
        expected = Fraction(5, 3) * Fraction(7, 5760)
        assert F2_w3(2) == expected

    def test_F2_w3_c50(self):
        """F_2(W_3, c=50) = (125/3) * 7/5760 = 875/17280."""
        expected = Fraction(125, 3) * Fraction(7, 5760)
        assert F2_w3(50) == expected


# ============================================================================
# Cross-family structural checks (AP10)
# ============================================================================

class TestStructuralChecks:
    """Cross-family structural verification (the real adversarial test)."""

    def test_linearity_in_kappa(self):
        """F_2 is linear in kappa: F_2(a*kappa) = a * F_2(kappa)."""
        for a in [2, 3, 5, 10]:
            assert F2(Fraction(a)) == Fraction(a) * F2(Fraction(1))

    def test_virasoro_complementarity_c1(self):
        """kappa(Vir_1) + kappa(Vir_25) = 1/2 + 25/2 = 13."""
        assert kappa_virasoro(1) + kappa_virasoro(25) == Fraction(13)
        F2_sum = F2_virasoro(1) + F2_virasoro(25)
        assert F2_sum == Fraction(13) * lambda_fp(2)

    def test_virasoro_complementarity_c13(self):
        """Self-dual point: kappa(Vir_13) + kappa(Vir_13) = 13."""
        assert kappa_virasoro(13) + kappa_virasoro(13) == Fraction(13)

    def test_virasoro_complementarity_c25(self):
        """kappa(Vir_25) + kappa(Vir_1) = 13."""
        assert kappa_virasoro(25) + kappa_virasoro(1) == Fraction(13)

    def test_virasoro_complementarity_F2(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 13 * lambda_2^FP for all c."""
        expected = Fraction(13) * lambda_fp(2)
        for c_val in [1, 5, 10, 13, 20, 25]:
            F2_sum = F2_virasoro(c_val) + F2_virasoro(26 - c_val)
            assert F2_sum == expected, f"Complementarity fails at c={c_val}"

    def test_E8_equals_8_heisenberg(self):
        """F_2(E_8) = 8 * F_2(H_1) (E_8 = 8 free bosons)."""
        F2_E8 = F2(Fraction(8))  # kappa(E_8) = 8
        F2_8H = Fraction(8) * F2_heisenberg(1)
        assert F2_E8 == F2_8H

    def test_sl2_kappa_antisymmetry(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0 (Feigin-Frenkel: k' = -k-2h^v)."""
        for k in [1, 2, 3, 5]:
            k_dual = -k - 4  # k' = -k - 2*h^v = -k - 4 for sl_2
            assert kappa_affine_sl2(k) + kappa_affine_sl2(k_dual) == Fraction(0)

    def test_heisenberg_additivity(self):
        """F_2(H_k) = k * F_2(H_1) (level additivity)."""
        F2_H1 = F2_heisenberg(1)
        for k in [2, 3, 5, 10]:
            assert F2_heisenberg(k) == Fraction(k) * F2_H1

    def test_scalar_graph_sum_returns_data(self):
        """scalar_graph_sum_F2 returns consistent data."""
        result = scalar_graph_sum_F2(Fraction(1))
        assert result['kappa'] == Fraction(1)
        assert result['lambda_2_FP'] == Fraction(7, 5760)
        assert result['F_2'] == Fraction(7, 5760)
        assert result['num_graphs'] == 6


class TestFullAdversarial:
    """Full adversarial comparison: tropical vs direct."""

    def test_heisenberg_k1(self):
        """Heisenberg at k=1: F_2 = 7/5760."""
        result = full_adversarial_comparison(Fraction(1))
        assert result['F2_direct'] == Fraction(7, 5760)
        assert result['chi_orb_mbar2'] == Fraction(-181, 1440)

    def test_virasoro_c1(self):
        """Virasoro at c=1: F_2 = 7/11520."""
        result = full_adversarial_comparison(Fraction(1, 2))
        assert result['F2_direct'] == Fraction(7, 11520)

    def test_virasoro_c13(self):
        """Virasoro at c=13 (self-dual): F_2 = 91/11520."""
        result = full_adversarial_comparison(Fraction(13, 2))
        assert result['F2_direct'] == Fraction(91, 11520)

    def test_virasoro_c25(self):
        """Virasoro at c=25: F_2 = 35/2304."""
        result = full_adversarial_comparison(Fraction(25, 2))
        assert result['F2_direct'] == Fraction(35, 2304)

    def test_sl2_k1(self):
        """sl_2 at k=1: F_2 = (9/4) * 7/5760."""
        result = full_adversarial_comparison(Fraction(9, 4))
        assert result['F2_direct'] == Fraction(9, 4) * Fraction(7, 5760)

    def test_sl2_k2(self):
        """sl_2 at k=2: F_2 = 3 * 7/5760 = 7/1920."""
        result = full_adversarial_comparison(Fraction(3))
        assert result['F2_direct'] == Fraction(7, 1920)

    def test_chi_orb_consistent_across_kappa(self):
        """chi^orb(M-bar_2) is independent of kappa (topological invariant)."""
        for k in [Fraction(1), Fraction(13, 2), Fraction(3), Fraction(100)]:
            result = full_adversarial_comparison(k)
            assert result['chi_orb_mbar2'] == Fraction(-181, 1440)


# ============================================================================
# W_3 multi-channel tests
# ============================================================================

class TestW3MultiChannel:
    """W_3 multi-channel graph sum verification."""

    def test_w3_propagator_T(self):
        """P_T = 2/c."""
        for c_val in [2, 10, 50]:
            assert w3_propagator('T', c_val) == Fraction(2, c_val)

    def test_w3_propagator_W(self):
        """P_W = 3/c."""
        for c_val in [2, 10, 50]:
            assert w3_propagator('W', c_val) == Fraction(3, c_val)

    def test_w3_C3_TTT(self):
        """C_{TTT} = c."""
        assert w3_C3('T', 'T', 'T', 10) == Fraction(10)

    def test_w3_C3_TWW(self):
        """C_{TWW} = c."""
        assert w3_C3('T', 'W', 'W', 10) == Fraction(10)

    def test_w3_C3_z2_vanishing(self):
        """Z_2 symmetry: odd W-count vanishes."""
        assert w3_C3('T', 'T', 'W', 10) == Fraction(0)
        assert w3_C3('W', 'W', 'W', 10) == Fraction(0)

    def test_w3_smooth_amplitude(self):
        """Smooth graph: no edges, contributes kappa_total * chi(M_2)."""
        for c_val in [2, 50]:
            amp = w3_graph_amplitude('smooth_g2', (), c_val)
            expected = kappa_w3(c_val) * chi_orb_open(2, 0)
            assert amp == expected

    def test_w3_dumbbell_T(self):
        """Dumbbell with T-channel edge."""
        c_val = 50
        amp = w3_graph_amplitude('dumbbell', ('T',), c_val)
        # (kappa_T/24)^2 * (2/c) / |Aut=2|
        kT = Fraction(c_val, 2)
        expected = (kT * lambda_fp(1))**2 * Fraction(2, c_val) / Fraction(2)
        assert amp == expected

    def test_w3_dumbbell_W(self):
        """Dumbbell with W-channel edge."""
        c_val = 50
        amp = w3_graph_amplitude('dumbbell', ('W',), c_val)
        kW = Fraction(c_val, 3)
        expected = (kW * lambda_fp(1))**2 * Fraction(3, c_val) / Fraction(2)
        assert amp == expected

    def test_w3_channel_enumeration_structure(self):
        """Channel enumeration returns data for all 6 graphs."""
        result = w3_channel_enumeration(50)
        assert len(result['graph_details']) == 6
        for name in ['smooth_g2', 'figure_eight', 'banana', 'dumbbell', 'theta', 'mixed']:
            assert name in result['graph_details']

    def test_w3_c2_multichannel(self):
        """W_3 at c=2: multi-channel F_2 computation."""
        result = w3_F2_multichannel(2)
        assert result['c'] == 2
        assert result['kappa_total'] == Fraction(5, 3)
        assert result['kappa_T'] == Fraction(1)
        assert result['kappa_W'] == Fraction(2, 3)

    def test_w3_c50_multichannel(self):
        """W_3 at c=50: multi-channel F_2 computation."""
        result = w3_F2_multichannel(50)
        assert result['c'] == 50
        assert result['kappa_total'] == Fraction(125, 3)


class TestVerifyFunctions:
    """Test the verification/cross-check functions."""

    def test_verify_chi_orb_all_pass(self):
        """All chi^orb values match known values."""
        result = verify_chi_orb()
        for key, data in result.items():
            assert data['match'], f"Failed at {key}"

    def test_verify_chi_mbar2_computes(self):
        """chi^orb(M-bar_2) computation runs and returns data."""
        result = verify_chi_mbar2()
        assert 'chi_total' in result
        assert 'decomposition' in result

    def test_verify_F2_cross_family(self):
        """Cross-family F_2 verification runs."""
        result = verify_F2_cross_family()
        assert 'families' in result
        assert 'complementarity' in result
        assert 'additivity' in result

    def test_verify_F2_complementarity_all_pass(self):
        """All complementarity checks pass."""
        result = verify_F2_cross_family()
        for key, data in result['complementarity'].items():
            assert data['match'], f"Complementarity failed at {key}"

    def test_verify_F2_additivity_all_pass(self):
        """All additivity checks pass."""
        result = verify_F2_cross_family()
        for key, data in result['additivity'].items():
            assert data['match'], f"Additivity failed at {key}"

    def test_scalar_polynomial_coefficients(self):
        """Scalar sum polynomial has correct structure."""
        poly = scalar_sum_polynomial()
        # Must have entries for edge counts 0, 1, 2, 3
        assert 0 in poly  # smooth: 1/1
        assert 1 in poly  # figure_eight (1/2) + dumbbell (1/2)
        assert 2 in poly  # banana (1/8) + mixed (1/2)
        assert 3 in poly  # theta (1/12)

        assert poly[0] == Fraction(1)     # 1/|Aut(smooth)| = 1
        assert poly[1] == Fraction(1)     # 1/2 + 1/2
        assert poly[2] == Fraction(5, 8)  # 1/8 + 1/2
        assert poly[3] == Fraction(1, 12) # 1/12


# ============================================================================
# Cross-engine consistency (AP5)
# ============================================================================

class TestCrossEngine:
    """Verify consistency with the existing genus-2 engines."""

    def test_lambda_fp_2_matches_existing(self):
        """lambda_2^FP matches the existing engine."""
        from compute.lib.genus2_landscape import lambda_fp_2 as existing_lambda
        from sympy import Rational
        existing = existing_lambda()
        tropical = lambda_fp(2)
        assert tropical == Fraction(existing.p, existing.q)

    def test_kappa_heisenberg_matches(self):
        """Heisenberg kappa matches existing engine."""
        from compute.lib.genus2_landscape import kappa_heisenberg as existing_kappa
        from sympy import Rational
        existing = existing_kappa(1)
        tropical = kappa_heisenberg(1)
        assert tropical == Fraction(existing.p, existing.q)

    def test_kappa_virasoro_matches(self):
        """Virasoro kappa matches existing engine."""
        from compute.lib.genus2_landscape import kappa_virasoro as existing_kappa
        from sympy import Rational
        for c_val in [1, 13, 25, 26]:
            existing = existing_kappa(c_val)
            tropical = kappa_virasoro(c_val)
            assert tropical == Fraction(existing.p, existing.q), f"Mismatch at c={c_val}"

    def test_kappa_sl2_matches(self):
        """sl_2 kappa matches existing engine."""
        from compute.lib.genus2_landscape import kappa_affine_sl2 as existing_kappa
        from sympy import Rational
        for k_val in [1, 2, 3]:
            existing = existing_kappa(k_val)
            tropical = kappa_affine_sl2(k_val)
            assert tropical == Fraction(existing.p, existing.q), f"Mismatch at k={k_val}"

    def test_F2_heisenberg_matches(self):
        """F_2(H_1) matches the existing landscape engine."""
        from compute.lib.genus2_landscape import F2_heisenberg as existing_F2
        from sympy import Rational
        existing = existing_F2(1)['F2']
        tropical = F2_heisenberg(1)
        assert tropical == Fraction(existing.p, existing.q)

    def test_graph_count_matches_stable_graph_engine(self):
        """Graph count at g=2, n=0 matches the stable_graph_enumeration engine."""
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        existing_graphs = enumerate_stable_graphs(2, 0)
        assert len(existing_graphs) == 6
        assert len(genus2_graphs()) == 6

    def test_chi_mbar2_matches_graph_sum_engine(self):
        """chi^orb(M-bar_2) matches the higher_genus_graph_sum_engine."""
        from compute.lib.higher_genus_graph_sum_engine import chi_orb_mbar
        existing = chi_orb_mbar(2, 0)
        tropical = chi_orb_mbar2_tropical()
        assert tropical == existing, f"Tropical: {tropical}, Engine: {existing}"
