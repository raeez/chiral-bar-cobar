"""Tests for compute/lib/deformation_bar.py — Deformation quantization chain-level structure.

Verifies:
  - Quantization hierarchy (3 levels: classical, singly quantum, doubly quantum)
  - P_inf vs Coisson distinction (critical: Coisson is NOT a chiral algebra)
  - Star product expansion structure
  - Deformation obstruction theory (HH^2 for deformations, HH^3 for obstructions)
  - Known deformation examples
  - Quantization maps between levels
  - Built-in verification suite

References:
  deformation_quantization.tex, deformation_quantization_examples.tex
  CLAUDE.md: P_inf vs Coisson distinction
"""

import pytest

from compute.lib.deformation_bar import (
    QUANTIZATION_LEVELS,
    QUANTIZATION_MAPS,
    pinf_vs_coisson,
    star_product_expansion,
    deformation_obstructions,
    deformation_examples,
    verify_deformation,
)


# ═══════════════════════════════════════════════════════════════
# Import test
# ═══════════════════════════════════════════════════════════════

class TestImport:
    def test_module_loads(self):
        """Module imports without error."""
        import compute.lib.deformation_bar
        assert hasattr(compute.lib.deformation_bar, 'QUANTIZATION_LEVELS')


# ═══════════════════════════════════════════════════════════════
# Quantization hierarchy
# ═══════════════════════════════════════════════════════════════

class TestQuantizationLevels:
    """Test the three-level quantization hierarchy."""

    def test_three_levels(self):
        """There should be exactly 3 quantization levels."""
        assert len(QUANTIZATION_LEVELS) == 3

    def test_level_names(self):
        """The three levels are classical, singly_quantum, doubly_quantum."""
        expected = {"classical", "singly_quantum", "doubly_quantum"}
        assert set(QUANTIZATION_LEVELS.keys()) == expected

    def test_classical_not_chiral(self):
        """Classical (Coisson/PVA) is NOT a chiral algebra.

        This is a critical distinction: Coisson = commutative D_X-algebra
        + Lie* bracket, NOT a chiral algebra.
        """
        assert QUANTIZATION_LEVELS["classical"]["is_chiral"] is False

    def test_classical_no_ope(self):
        """Classical level has no OPE."""
        assert QUANTIZATION_LEVELS["classical"]["has_ope"] is False

    def test_classical_commutative(self):
        """Classical level is commutative."""
        assert QUANTIZATION_LEVELS["classical"]["commutative"] is True

    def test_singly_quantum_is_chiral(self):
        """Singly quantum (vertex algebra) IS a chiral algebra."""
        assert QUANTIZATION_LEVELS["singly_quantum"]["is_chiral"] is True

    def test_singly_quantum_has_ope(self):
        """Singly quantum level has OPE."""
        assert QUANTIZATION_LEVELS["singly_quantum"]["has_ope"] is True

    def test_doubly_quantum_is_chiral(self):
        """Doubly quantum (E_1-chiral) IS a chiral algebra."""
        assert QUANTIZATION_LEVELS["doubly_quantum"]["is_chiral"] is True

    def test_doubly_quantum_not_commutative(self):
        """Doubly quantum level is NOT commutative (nonlocal VA)."""
        assert QUANTIZATION_LEVELS["doubly_quantum"]["commutative"] is False

    def test_doubly_quantum_has_ope(self):
        """Doubly quantum level has OPE."""
        assert QUANTIZATION_LEVELS["doubly_quantum"]["has_ope"] is True


# ═══════════════════════════════════════════════════════════════
# Quantization maps
# ═══════════════════════════════════════════════════════════════

class TestQuantizationMaps:
    def test_two_maps(self):
        """There should be exactly 2 quantization maps."""
        assert len(QUANTIZATION_MAPS) == 2

    def test_first_quantization_exists(self):
        """Classical -> singly_quantum map exists."""
        assert ("classical", "singly_quantum") in QUANTIZATION_MAPS

    def test_second_quantization_exists(self):
        """Singly_quantum -> doubly_quantum map exists."""
        assert ("singly_quantum", "doubly_quantum") in QUANTIZATION_MAPS

    def test_first_quantization_obstruction(self):
        """First quantization obstruction lives in HH^2."""
        m = QUANTIZATION_MAPS[("classical", "singly_quantum")]
        assert "HH^2" in m["obstruction"]

    def test_second_quantization_obstruction(self):
        """Second quantization obstruction lives in chiral HH^2."""
        m = QUANTIZATION_MAPS[("singly_quantum", "doubly_quantum")]
        assert "HH^2" in m["obstruction"]


# ═══════════════════════════════════════════════════════════════
# P_inf vs Coisson distinction
# ═══════════════════════════════════════════════════════════════

class TestPinfVsCoisson:
    """Critical distinction: Coisson is NOT a chiral algebra, P_inf IS.

    Ground truth: CLAUDE.md P_inf vs Coisson section.
    """

    def setup_method(self):
        self.pvc = pinf_vs_coisson()

    def test_coisson_not_chiral(self):
        """Coisson (PVA) is NOT a chiral algebra."""
        assert self.pvc["Coisson"]["is_chiral_algebra"] is False

    def test_pinf_is_chiral(self):
        """P_inf-chiral IS a chiral algebra."""
        assert self.pvc["P_inf_chiral"]["is_chiral_algebra"] is True

    def test_coisson_no_ope(self):
        """Coisson has no OPE."""
        assert self.pvc["Coisson"]["has_ope"] is False

    def test_pinf_has_ope(self):
        """P_inf-chiral has OPE."""
        assert self.pvc["P_inf_chiral"]["has_ope"] is True

    def test_coisson_aliases(self):
        """Coisson has PVA as an alternative name."""
        names = self.pvc["Coisson"]["alternative_names"]
        assert "PVA" in names or "Poisson vertex algebra" in names

    def test_coisson_quantizes_to_va(self):
        """Coisson quantizes to a vertex algebra (E_inf-chiral)."""
        assert "vertex algebra" in self.pvc["Coisson"]["quantizes_to"]

    def test_pinf_quantizes_to_e1(self):
        """P_inf-chiral quantizes to E_1-chiral."""
        assert "E_1" in self.pvc["P_inf_chiral"]["quantizes_to"]

    def test_pinf_koszul_duality_property(self):
        """P_inf has the Koszul duality property: chirCom^! = chirLie."""
        assert "chirCom" in self.pvc["P_inf_chiral"]["key_property"]
        assert "chirLie" in self.pvc["P_inf_chiral"]["key_property"]


# ═══════════════════════════════════════════════════════════════
# Star product expansion
# ═══════════════════════════════════════════════════════════════

class TestStarProduct:
    def test_order_0_commutative(self):
        """Order 0 term is the commutative product m_2."""
        sp = star_product_expansion(3)
        assert "commutative" in sp[0]

    def test_order_1_poisson(self):
        """Order 1 term is the Poisson bracket."""
        sp = star_product_expansion(3)
        assert "Poisson" in sp[1]

    def test_order_2_obstruction(self):
        """Order 2 references HH^3 obstruction."""
        sp = star_product_expansion(3)
        assert "obstruction" in sp[2] or "order" in sp[2]

    def test_expansion_length(self):
        """Expansion through order n has n+1 terms."""
        for order in [0, 1, 2, 5, 10]:
            sp = star_product_expansion(order)
            assert len(sp) == order + 1


# ═══════════════════════════════════════════════════════════════
# Deformation obstructions
# ═══════════════════════════════════════════════════════════════

class TestDeformationObstructions:
    """Verify the obstruction theory structure."""

    def setup_method(self):
        self.obs = deformation_obstructions()

    def test_three_levels(self):
        """Three levels of obstruction: first_order, obstruction, curved."""
        assert "first_order" in self.obs
        assert "obstruction" in self.obs
        assert "curved" in self.obs

    def test_first_order_in_hh2(self):
        """First-order deformations live in HH^2(A, A)."""
        assert "HH^2" in self.obs["first_order"]["lives_in"]

    def test_obstruction_in_hh3(self):
        """Obstructions to extending deformations live in HH^3(A, A)."""
        assert "HH^3" in self.obs["obstruction"]["lives_in"]

    def test_curved_in_hh0(self):
        """Curved deformations (curvature) live in HH^0 = center."""
        assert "HH^0" in self.obs["curved"]["lives_in"]

    def test_massey_product(self):
        """Obstruction is a Massey product [f, f] in HH^3."""
        assert "Massey" in self.obs["obstruction"]["massey_product"] or \
               "[f, f]" in self.obs["obstruction"]["massey_product"]

    def test_curved_bar_relation(self):
        """Curvature relates to m_0 in bar degree 0."""
        assert "m_0" in self.obs["curved"]["relation_to_bar"]


# ═══════════════════════════════════════════════════════════════
# Deformation examples
# ═══════════════════════════════════════════════════════════════

class TestDeformationExamples:
    """Known deformation quantization examples."""

    def setup_method(self):
        self.examples = deformation_examples()

    def test_heisenberg_dq(self):
        """Heisenberg DQ: Sym^ch -> H_k, unobstructed."""
        heis = self.examples["Heisenberg_DQ"]
        assert heis["obstruction_vanishes"] is True
        assert "k" in heis["parameter"]

    def test_lattice_dq(self):
        """Lattice DQ: C[L] -> V_L, unobstructed for even lattice."""
        lat = self.examples["lattice_DQ"]
        assert lat["obstruction_vanishes"] is True

    def test_symplectic_fermion_dq(self):
        """Symplectic fermion DQ: Lambda^ch -> SF, unobstructed."""
        sf = self.examples["symplectic_fermion_DQ"]
        assert sf["obstruction_vanishes"] is True

    def test_all_examples_unobstructed(self):
        """All standard examples in the module are unobstructed.

        This is a structural check: the examples were chosen because
        they are unobstructed (quadratic OPEs).
        """
        for name, ex in self.examples.items():
            assert ex["obstruction_vanishes"] is True, f"{name} should be unobstructed"


# ═══════════════════════════════════════════════════════════════
# Structural consistency checks
# ═══════════════════════════════════════════════════════════════

class TestStructuralConsistency:
    """Cross-consistency checks (AP10 prevention)."""

    def test_chiral_hierarchy_monotone(self):
        """The chirality property is monotone: classical < singly < doubly.

        Once chiral, always chiral in the hierarchy.
        """
        assert not QUANTIZATION_LEVELS["classical"]["is_chiral"]
        assert QUANTIZATION_LEVELS["singly_quantum"]["is_chiral"]
        assert QUANTIZATION_LEVELS["doubly_quantum"]["is_chiral"]

    def test_ope_hierarchy_monotone(self):
        """The OPE property is monotone: classical (no) -> quantum (yes)."""
        assert not QUANTIZATION_LEVELS["classical"]["has_ope"]
        assert QUANTIZATION_LEVELS["singly_quantum"]["has_ope"]
        assert QUANTIZATION_LEVELS["doubly_quantum"]["has_ope"]

    def test_commutativity_decreasing(self):
        """Commutativity decreases along the hierarchy.

        Classical: commutative. Singly: commutative (up to homotopy).
        Doubly: NOT commutative.
        """
        assert QUANTIZATION_LEVELS["classical"]["commutative"] is True
        assert QUANTIZATION_LEVELS["doubly_quantum"]["commutative"] is False


# ═══════════════════════════════════════════════════════════════
# Full verification suite
# ═══════════════════════════════════════════════════════════════

class TestVerifyDeformation:
    def test_all_verifications_pass(self):
        """The module's built-in verify_deformation() should all pass."""
        results = verify_deformation()
        for name, ok in results.items():
            assert ok, f"FAIL: {name}"
