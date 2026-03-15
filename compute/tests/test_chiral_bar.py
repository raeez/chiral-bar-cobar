"""Tests for the chiral_bar module.

Tests the Chevalley-Eilenberg complex, SDR construction, structure constants,
and associative bar differentials for sl_2.
"""

import pytest
from sympy import Rational, zeros, Matrix

from compute.lib.chiral_bar import (
    sl2_structure_constants,
    apply_bracket,
    bracket_vector,
    sl2_killing,
    CEComplex,
    SDR,
    sl2_assoc_bar_diff_2to1,
    sl2_assoc_bar_diff_3to2,
    chiral_bar_diff_3to2,
    os_residue,
)


# ===================================================================
# sl_2 structure constants
# ===================================================================

class TestSl2StructureConstants:
    def test_bracket_ef(self):
        """[e, f] = h."""
        sc = sl2_structure_constants()
        result = apply_bracket(sc, 0, 2)
        assert result == {1: Rational(1)}

    def test_bracket_fe(self):
        """[f, e] = -h."""
        sc = sl2_structure_constants()
        result = apply_bracket(sc, 2, 0)
        assert result == {1: Rational(-1)}

    def test_bracket_he(self):
        """[h, e] = 2e."""
        sc = sl2_structure_constants()
        result = apply_bracket(sc, 1, 0)
        assert result == {0: Rational(2)}

    def test_bracket_hf(self):
        """[h, f] = -2f."""
        sc = sl2_structure_constants()
        result = apply_bracket(sc, 1, 2)
        assert result == {2: Rational(-2)}

    def test_antisymmetry(self):
        """[a, b] = -[b, a] for all pairs."""
        sc = sl2_structure_constants()
        for a in range(3):
            for b in range(3):
                ab = bracket_vector(sc, a, b, 3)
                ba = bracket_vector(sc, b, a, 3)
                for i in range(3):
                    assert ab[i] == -ba[i], f"Antisymmetry fails at ({a},{b}), component {i}"

    def test_jacobi_identity(self):
        """[[a,b],c] + [[b,c],a] + [[c,a],b] = 0 for all triples."""
        sc = sl2_structure_constants()
        dim = 3
        for a in range(dim):
            for b in range(dim):
                for c in range(dim):
                    total = [Rational(0)] * dim
                    for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
                        xy = apply_bracket(sc, x, y)
                        for k, coeff in xy.items():
                            kz = apply_bracket(sc, k, z)
                            for m, c2 in kz.items():
                                total[m] += coeff * c2
                    for m in range(dim):
                        assert total[m] == 0, f"Jacobi fails at ({a},{b},{c}), component {m}"

    def test_bracket_zero(self):
        """Diagonal brackets [a, a] = 0."""
        sc = sl2_structure_constants()
        for a in range(3):
            result = apply_bracket(sc, a, a)
            assert result == {}


class TestSl2Killing:
    def test_ef_pairing(self):
        kf = sl2_killing()
        assert kf[(0, 2)] == Rational(1)
        assert kf[(2, 0)] == Rational(1)

    def test_hh_pairing(self):
        kf = sl2_killing()
        assert kf[(1, 1)] == Rational(2)

    def test_zero_entries(self):
        """Most off-diagonal Killing entries are zero."""
        kf = sl2_killing()
        assert (0, 0) not in kf
        assert (0, 1) not in kf


# ===================================================================
# Chevalley-Eilenberg complex
# ===================================================================

class TestCEComplex:
    @pytest.fixture
    def ce(self):
        return CEComplex(3, sl2_structure_constants())

    def test_basis_dimensions(self, ce):
        """C^n = Lambda^n(g*) dimensions: 1, 3, 3, 1."""
        assert ce.dim(0) == 1
        assert ce.dim(1) == 3
        assert ce.dim(2) == 3
        assert ce.dim(3) == 1

    def test_basis_out_of_range(self, ce):
        assert ce.dim(-1) == 0
        assert ce.dim(4) == 0

    def test_d_squared_01(self, ce):
        """d^1 circ d^0 = 0."""
        assert ce.verify_d_squared(0) is True

    def test_d_squared_12(self, ce):
        """d^2 circ d^1 = 0."""
        assert ce.verify_d_squared(1) is True

    def test_d0_is_zero(self, ce):
        """d^0: C^0 -> C^1 is zero (trivial coefficients)."""
        d0 = ce.differential(0)
        assert d0.equals(zeros(3, 1))

    def test_d1_rank(self, ce):
        """d^1: C^1 -> C^2 is 3x3 with full rank (H^1 = 0 requires ker(d1) = 0)."""
        d1 = ce.differential(1)
        # H^1 = ker(d1)/im(d0) = ker(d1)/0. H^1=0 requires ker(d1)=0, i.e. rank=3.
        assert d1.rank() == 3

    def test_cohomology_dims(self, ce):
        """H*(sl_2) = (1, 0, 0, 1) — exterior algebra on degree-3 generator."""
        cohom = ce.cohomology_dims()
        assert cohom[0] == 1
        assert cohom[1] == 0
        assert cohom[2] == 0
        assert cohom[3] == 1


# ===================================================================
# SDR (Strong Deformation Retract)
# ===================================================================

class TestSDR:
    @pytest.fixture
    def sdr(self):
        ce = CEComplex(3, sl2_structure_constants())
        dims = [ce.dim(k) for k in range(4)]
        diffs = [ce.differential(k) for k in range(3)]
        return SDR(dims, diffs)

    def test_cohomology_dims(self, sdr):
        """SDR should recover H*(sl_2) = (1, 0, 0, 1)."""
        assert sdr.cohom_dims == [1, 0, 0, 1]

    def test_p_iota_identity(self, sdr):
        """p circ iota = id_H at degrees with nonzero cohomology."""
        results = sdr.verify_sdr()
        for key, val in results.items():
            if "p∘ι=id" in key:
                assert val is True, f"SDR check failed: {key}"


# ===================================================================
# Associative bar differentials
# ===================================================================

class TestAssocBarDiff:
    def test_d21_shape(self):
        """D21 is 3 x 9 (g -> g tensor g)."""
        D = sl2_assoc_bar_diff_2to1()
        assert D.shape == (3, 9)

    def test_d21_rank(self):
        """D21 should have rank 3 for sl_2 (surjective)."""
        D = sl2_assoc_bar_diff_2to1()
        assert D.rank() == 3

    def test_d32_shape(self):
        """D32 is 9 x 27."""
        D = sl2_assoc_bar_diff_3to2()
        assert D.shape == (9, 27)

    def test_d_squared_nonzero(self):
        """d^2 != 0 for associative bar (Lie bracket is not associative)."""
        D21 = sl2_assoc_bar_diff_2to1()
        D32 = sl2_assoc_bar_diff_3to2()
        product = D21 * D32
        assert not product.equals(zeros(*product.shape)), \
            "d^2 should NOT be zero for associative bar"

    def test_d21_ef_bracket(self):
        """d([e|f]) = [e,f] = h, so D[1, 0*3+2] = 1."""
        D = sl2_assoc_bar_diff_2to1()
        # [e,f] = h: generator 0 bracket 2 -> generator 1
        # col = 0*3 + 2 = 2, row = 1
        assert D[1, 2] == Rational(1)


# ===================================================================
# OS residue (Orlik-Solomon)
# ===================================================================

class TestOSResidue:
    def test_residue_12_on_omega1(self):
        """Res_{(1,2)} of omega_1 = eta_{12}^eta_{13}."""
        # omega_1 = eta_{12} ^ eta_{13}: residue along D_{12} extracts eta_{12},
        # leaving eta_{13} which relabels to eta_{12} on the 2-point config.
        res = os_residue(0, (1, 2))
        assert res is not None

    def test_residue_type(self):
        """All residues should return Rational."""
        for omega_idx in [0, 1]:
            for collision in [(1, 2), (1, 3), (2, 3)]:
                res = os_residue(omega_idx, collision)
                assert isinstance(res, Rational)


# ===================================================================
# Chiral bar differential
# ===================================================================

class TestChiralBarDiff:
    def test_d32_shape(self):
        """Chiral bar D: B^3 -> B^2 should be 9 x 54."""
        D = chiral_bar_diff_3to2()
        assert D.shape == (9, 54)

    def test_d32_not_identically_zero(self):
        """The chiral differential should have nonzero entries."""
        D = chiral_bar_diff_3to2()
        assert not D.equals(zeros(*D.shape))
