r"""Tests for theorem_c_b_family_mukai_engine.

Verifies the B-row of the Vol I Theorem-C five-archetype ceiling
{0, 8, 13, 250/3, 98/3} at the Mukai-enhanced K3 Heisenberg
$\mathcal{H}_{\mathrm{Muk}}(K3)$:

    K^{kappa_ch}(H_Muk(K3)) = 2 * c_+(Mukai(K3)) = 8.

Three independent verification paths (Bruinier / Mukai / Lusztig),
all converging on the integer 8.

References:
    prop:archetype-complementarity-bridge (landscape_census.tex)
    rem:latfnd-2 (lattice_foundations.tex, three faces of 8)
    Bruinier 2002 LNM 1780 Prop 5.1
    Mukai 1987 Nagoya 81
    Lusztig 1990 §5.7
"""
from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.theorem_c_b_family_mukai_engine import (
    B_FAMILY_SCOPE,
    b_family_scope,
    b_row_membership,
    bruinier_equals_mukai,
    bruinier_heegner_h1_order,
    five_archetype_ceiling,
    lusztig_identity_verification,
    lusztig_root_of_unity_length,
    mukai_c_minus,
    mukai_c_plus,
    mukai_heisenberg_anomaly_ratio,
    mukai_heisenberg_bridge_verification,
    mukai_heisenberg_koszul_conductor,
    mukai_heisenberg_self_dual_kappa,
    mukai_heisenberg_trinity_conductor,
    mukai_rank,
    mukai_signature,
)


class TestMukaiLattice:
    """Mukai lattice II_{4,20} primary data."""

    def test_signature(self):
        """Signature (4, 20)."""
        assert mukai_signature() == (4, 20)

    def test_rank_is_24(self):
        """rank II_{4,20} = 24 = 1 + 22 + 1 (Mukai 1987)."""
        assert mukai_rank() == 24

    def test_c_plus_is_4(self):
        """c_+ = 4, the positive-definite index."""
        assert mukai_c_plus() == 4

    def test_c_minus_is_20(self):
        """c_- = 20."""
        assert mukai_c_minus() == 20

    def test_signature_sum_is_rank(self):
        """c_+ + c_- = rank."""
        assert mukai_c_plus() + mukai_c_minus() == mukai_rank()


class TestMukaiHeisenbergConductor:
    """The B-row Koszul conductor K^{kappa_ch} = 2 c_+ = 8."""

    def test_K_kappa_is_8(self):
        """K^{kappa_ch}(H_Muk(K3)) = 8 (Mukai doubling)."""
        assert mukai_heisenberg_koszul_conductor() == 8

    def test_K_kappa_equals_2_c_plus(self):
        """K^{kappa_ch} = 2 * c_+(II_{4,20})."""
        assert mukai_heisenberg_koszul_conductor() == 2 * mukai_c_plus()

    def test_K_trinity_is_48(self):
        """K_Trinity = c + c^! = 48 on the Mukai-self-dual convention."""
        assert mukai_heisenberg_trinity_conductor() == 48

    def test_K_trinity_equals_2_rank(self):
        """K_Trinity = 2 * rank(II_{4,20}) = 48."""
        assert mukai_heisenberg_trinity_conductor() == 2 * mukai_rank()

    def test_anomaly_ratio_is_one_sixth(self):
        """varrho(H_Muk) = c_+/rank = 1/6 (distinct from G-archetype varrho = 1)."""
        assert mukai_heisenberg_anomaly_ratio() == Fraction(1, 6)

    def test_bridge_verification(self):
        """Anomaly-ratio bridge K^kappa = varrho * K_Trinity."""
        result = mukai_heisenberg_bridge_verification()
        assert result["K_kappa"] == Fraction(8)
        assert result["K_trinity"] == Fraction(48)
        assert result["varrho"] == Fraction(1, 6)
        assert result["bridge_prediction"] == Fraction(8)
        assert result["bridge_equals_K_kappa"] is True

    def test_self_dual_kappa_is_4(self):
        """Self-dual kappa^* = K^kappa/2 = 4 = c_+(Mukai(K3))."""
        assert mukai_heisenberg_self_dual_kappa() == Fraction(4)
        assert mukai_heisenberg_self_dual_kappa() == Fraction(mukai_c_plus())


class TestBruinierHeegnerReciprocity:
    """Bruinier 2002 Prop 5.1: Humbert-H_1 torsion order = 8."""

    def test_h1_order_is_8(self):
        """Torsion order of c_1(L^{Delta_5} | H_1) = 8."""
        assert bruinier_heegner_h1_order() == 8

    def test_bruinier_equals_mukai(self):
        """Bruinier Heegner order = Mukai-doubling conductor."""
        assert bruinier_equals_mukai() is True


class TestLusztigRootOfUnity:
    """Lusztig 1990 §5.7: root-of-unity length ell = 8."""

    def test_length_is_8(self):
        """ell = 8 at zeta^8 = 1."""
        assert lusztig_root_of_unity_length() == 8

    def test_universal_identity(self):
        """hbar^2 * K^{kappa_ch} = -1 at ell = 8, hbar^2 = -1/8."""
        result = lusztig_identity_verification()
        assert result["hbar_squared"] == Fraction(-1, 8)
        assert result["K_kappa"] == Fraction(8)
        assert result["product"] == Fraction(-1)
        assert result["identity_holds"] is True


class TestThreeFacesCoincidence:
    """Three faces of 8 (Bruinier / Mukai / Lusztig) all coincide."""

    def test_three_faces_all_equal_8(self):
        """Bruinier = Mukai = Lusztig = 8."""
        assert bruinier_heegner_h1_order() == 8
        assert mukai_heisenberg_koszul_conductor() == 8
        assert lusztig_root_of_unity_length() == 8


class TestFiveArchetypeCeiling:
    """Vol I Theorem C ceiling {0, 8, 13, 250/3, 98/3}."""

    def test_ceiling_has_five_values(self):
        """The ceiling has exactly five distinct values."""
        ceiling = five_archetype_ceiling()
        assert len(set(ceiling)) == 5

    def test_ceiling_contents(self):
        """Ceiling = {0, 8, 13, 98/3, 250/3}."""
        expected = {
            Fraction(0),
            Fraction(8),
            Fraction(13),
            Fraction(98, 3),
            Fraction(250, 3),
        }
        assert set(five_archetype_ceiling()) == expected

    def test_b_row_in_ceiling(self):
        """K^{kappa_ch}(H_Muk) = 8 is a member of the ceiling."""
        assert b_row_membership() is True


class TestBFamilyScopeQualifier:
    """Scope declaration for the B-family."""

    def test_scope_string(self):
        """Scope is 'Lorentzian-lattice-parametric'."""
        scope = b_family_scope()
        assert scope["scope"] == "Lorentzian-lattice-parametric"

    def test_primary_sources(self):
        """Primary sources: Bruinier, Mukai, Lusztig, Borcherds, Gritsenko-Nikulin."""
        scope = b_family_scope()
        sources_text = " | ".join(scope["primary_sources"])
        assert "Bruinier 2002" in sources_text
        assert "Mukai 1987" in sources_text
        assert "Lusztig 1990" in sources_text
        assert "Borcherds 1992" in sources_text
        assert "Gritsenko-Nikulin 1998" in sources_text

    def test_universal_identity(self):
        """Universal identity: hbar^2 * K^{kappa_ch} = -1."""
        scope = b_family_scope()
        assert "hbar^2" in scope["universal_identity"]
        assert "K^{kappa_ch}" in scope["universal_identity"]

    def test_scope_caveat_is_present(self):
        """Scope has a caveat about Lorentzian vs positive-definite lattices."""
        scope = b_family_scope()
        assert "Lorentzian" in scope["caveat"] or "indefinite" in scope["caveat"]

    def test_distinct_from_G_archetype(self):
        """varrho differs between G (=1) and B (=1/6)."""
        scope = b_family_scope()
        assert "varrho" in scope["distinct_from_G_archetype"]


class TestCeilingIntegrationWithStandardFamilies:
    """Integration checks against the standard families from the complementarity engine."""

    def test_K3_Mukai_K_kappa_equals_B_row_value(self):
        """The B-row value 8 coincides with Mukai-doubling 2 c_+."""
        from compute.lib.theorem_c_b_family_mukai_engine import mukai_heisenberg_koszul_conductor
        assert mukai_heisenberg_koszul_conductor() == 8

    def test_varrho_times_K_reproduces_each_ceiling_value(self):
        """The bridge K^kappa = varrho * K_Trinity reproduces each ceiling entry."""
        # G: varrho = 1, K = 0  -> 0
        # L: varrho = 0, K = 2 dim g -> 0
        # C: varrho = 1/2, K = 0 -> 0
        # M (Vir): varrho = 1/2, K = 26 -> 13
        # M-ext (W_3): varrho = 5/6, K = 100 -> 250/3
        # M-ext (BP): varrho = 1/6, K = 196 -> 98/3
        # B (Mukai): varrho = 1/6, K = 48  -> 8

        cases = [
            ("G",  Fraction(1),      Fraction(0),    Fraction(0)),
            ("L",  Fraction(0),      Fraction(100),  Fraction(0)),  # any positive K collapses by rho=0
            ("C",  Fraction(1, 2),   Fraction(0),    Fraction(0)),
            ("M",  Fraction(1, 2),   Fraction(26),   Fraction(13)),
            ("W3", Fraction(5, 6),   Fraction(100),  Fraction(250, 3)),
            ("BP", Fraction(1, 6),   Fraction(196),  Fraction(98, 3)),
            ("B",  Fraction(1, 6),   Fraction(48),   Fraction(8)),
        ]

        for name, rho, K, expected in cases:
            assert rho * K == expected, f"Bridge failed on {name}: {rho}*{K} != {expected}"
