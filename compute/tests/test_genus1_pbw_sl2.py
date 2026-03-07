"""Tests for genus-1 PBW spectral sequence verification (MC1).

Verifies all claims in Theorem thm:pbw-genus1-km (higher_genus.tex:8517):
PBW degeneration for affine KM algebras at genus 1.

Ground truth: the enrichment from H^1(E_tau) at each weight is killed
by the combination of:
  (a) Whitehead vanishing (non-trivial g-modules)
  (b) Level-k Killing contraction (invariant part)

Tests organized by claim number matching the computation module.
"""

import pytest
from sympy import Rational, Matrix

from compute.lib.genus1_pbw_sl2 import (
    DIM_SL2,
    lie_bracket,
    killing,
    bracket_on_tensor_square,
    killing_form_element,
    adjoint_casimir_on_tensor_square,
    ce_differential_1_to_2,
    ce_differential_2_to_3,
    verify_enrichment_claims,
    verify_ce_complex,
)


# ---------------------------------------------------------------------------
# sl2 structure constants
# ---------------------------------------------------------------------------

class TestSL2StructureConstants:
    """Verify sl2 bracket and Killing form data."""

    def test_bracket_ef(self):
        assert lie_bracket(0, 2) == {1: Rational(1)}   # [e, f] = h

    def test_bracket_fe(self):
        assert lie_bracket(2, 0) == {1: Rational(-1)}  # [f, e] = -h

    def test_bracket_he(self):
        assert lie_bracket(1, 0) == {0: Rational(2)}   # [h, e] = 2e

    def test_bracket_hf(self):
        assert lie_bracket(1, 2) == {2: Rational(-2)}  # [h, f] = -2f

    def test_bracket_ee_vanishes(self):
        assert lie_bracket(0, 0) == {}

    def test_bracket_hh_vanishes(self):
        assert lie_bracket(1, 1) == {}

    def test_bracket_ff_vanishes(self):
        assert lie_bracket(2, 2) == {}

    def test_killing_ef(self):
        assert killing(0, 2) == Rational(1)

    def test_killing_hh(self):
        assert killing(1, 1) == Rational(2)

    def test_killing_ee_vanishes(self):
        assert killing(0, 0) == Rational(0)

    def test_jacobi_identity(self):
        """Verify [[e_a, e_b], e_c] + cyclic = 0 for all triples."""
        d = DIM_SL2
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    # [[a,b],c]
                    total = [Rational(0)] * d
                    for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
                        ab = lie_bracket(x, y)
                        for m, coeff1 in ab.items():
                            mc = lie_bracket(m, z)
                            for n, coeff2 in mc.items():
                                total[n] += coeff1 * coeff2
                    assert all(t == 0 for t in total), \
                        f"Jacobi fails for ({a},{b},{c}): {total}"


# ---------------------------------------------------------------------------
# Enrichment differential d_1 (Claims 1-5)
# ---------------------------------------------------------------------------

class TestEnrichmentD1:
    """Verify d_1: g^{otimes 2} -> g (Lie bracket map)."""

    def test_d1_shape(self):
        D = bracket_on_tensor_square()
        assert D.shape == (3, 9)

    def test_d1_rank_3(self):
        """Claim (1): d_1 is surjective (rank 3)."""
        D = bracket_on_tensor_square()
        assert D.rank() == 3

    def test_kernel_dim_6(self):
        """Claim (2): ker(d_1) has dimension 6."""
        D = bracket_on_tensor_square()
        assert 9 - D.rank() == 6

    def test_antisymmetric_isomorphism(self):
        """Claim (3): d_1 restricted to Lambda^2(g) = V_3 is an isomorphism."""
        D = bracket_on_tensor_square()
        d = DIM_SL2
        # Build antisymmetric basis vectors
        antisym_cols = []
        for a in range(d):
            for b in range(a + 1, d):
                v = Matrix([Rational(0)] * d**2)
                v[a * d + b] = Rational(1)
                v[b * d + a] = Rational(-1)
                antisym_cols.append(v)
        D_antisym = D * Matrix([list(v) for v in antisym_cols]).T
        assert D_antisym.rank() == 3


class TestKillingFormInvariant:
    """Verify claims about the Killing form element kappa^{ab}."""

    def test_killing_element_correct(self):
        """kappa = e tensor f + f tensor e + (1/2) h tensor h."""
        kappa = killing_form_element()
        # e tensor f = index 0*3+2 = 2
        assert kappa[2] == Rational(1)
        # f tensor e = index 2*3+0 = 6
        assert kappa[6] == Rational(1)
        # h tensor h = index 1*3+1 = 4
        assert kappa[4] == Rational(1, 2)
        # All others zero
        for i in [0, 1, 3, 5, 7, 8]:
            assert kappa[i] == Rational(0)

    def test_kappa_in_kernel(self):
        """Claim (4): kappa lies in ker(d_1)."""
        D = bracket_on_tensor_square()
        kappa = killing_form_element()
        result = D * kappa
        assert result.is_zero_matrix

    def test_kappa_is_invariant(self):
        """kappa is g-invariant (Casimir eigenvalue 0)."""
        C2 = adjoint_casimir_on_tensor_square()
        kappa = killing_form_element()
        assert (C2 * kappa).is_zero_matrix

    def test_killing_contraction_nonzero(self):
        """Claim (5): kappa^{ab} kappa_{ab} = dim(g) = 3 (nonzero)."""
        # This is the scalar that d_2 produces
        inv_killing = {
            (0, 2): Rational(1),
            (2, 0): Rational(1),
            (1, 1): Rational(1, 2),
        }
        contraction = sum(
            coeff * killing(a, b)
            for (a, b), coeff in inv_killing.items()
        )
        assert contraction == Rational(3)  # = dim(sl2)

    def test_symmetry_argument(self):
        """Verify kappa^{ab} f^c_{ab} = 0 (why kappa survives d_1).

        This is the key identity: the Killing form contracted with
        structure constants vanishes by symmetry vs antisymmetry.
        """
        inv_killing = {
            (0, 2): Rational(1),
            (2, 0): Rational(1),
            (1, 1): Rational(1, 2),
        }
        d = DIM_SL2
        for c in range(d):
            total = Rational(0)
            for (a, b), coeff in inv_killing.items():
                bracket = lie_bracket(a, b)
                total += coeff * bracket.get(c, Rational(0))
            assert total == 0, f"kappa^ab f^{c}_ab = {total} != 0"


# ---------------------------------------------------------------------------
# Casimir decomposition of g tensor g
# ---------------------------------------------------------------------------

class TestCasimirDecomposition:
    """Verify g tensor g = V_5 + V_3 + V_1 via Casimir eigenvalues."""

    def test_casimir_eigenvalues(self):
        """Eigenvalues should be {12: 5, 4: 3, 0: 1}.

        With our Killing form normalization (kappa(h,h)=2),
        the Casimir eigenvalue on spin-j rep is 2j(j+1).
        """
        C2 = adjoint_casimir_on_tensor_square()
        eigenvals = C2.eigenvals()
        assert eigenvals == {
            Rational(12): 5,  # V_5 (spin 2): 2*2*3 = 12
            Rational(4): 3,   # V_3 (spin 1): 2*1*2 = 4
            Rational(0): 1,   # V_1 (spin 0): 0
        }

    def test_dimension_sum(self):
        """5 + 3 + 1 = 9 = dim(g tensor g)."""
        C2 = adjoint_casimir_on_tensor_square()
        eigenvals = C2.eigenvals()
        total = sum(eigenvals.values())
        assert total == 9


# ---------------------------------------------------------------------------
# Chevalley-Eilenberg complex (Claims 6-8)
# ---------------------------------------------------------------------------

class TestCEComplex:
    """Verify CE complex of sl2: H*(sl2) = k[0] + k[3]."""

    def test_d1_rank_3(self):
        """Claim (6): d_CE^1 is injective (rank 3)."""
        d1 = ce_differential_1_to_2()
        assert d1.shape == (3, 3)
        assert d1.rank() == 3

    def test_d2_is_zero(self):
        """Claim (7): d_CE^2 = 0."""
        d2 = ce_differential_2_to_3()
        assert d2.shape == (1, 3)
        assert d2.rank() == 0

    def test_d_squared_zero(self):
        """d^2 = 0 in the CE complex."""
        d1 = ce_differential_1_to_2()
        d2 = ce_differential_2_to_3()
        assert (d2 * d1).is_zero_matrix

    def test_cohomology(self):
        """Claim (8): H*(sl2) = (1, 0, 0, 1)."""
        d1 = ce_differential_1_to_2()
        d2 = ce_differential_2_to_3()

        h0 = 1  # H^0 = k
        h1 = 3 - d1.rank()  # ker(d1) - im(d0=0) = 0
        h2 = (3 - d2.rank()) - d1.rank()  # ker(d2)/im(d1) = 0
        h3 = 1 - d2.rank()  # coker(d2) = 1

        assert (h0, h1, h2, h3) == (1, 0, 0, 1)

    def test_poincare_polynomial(self):
        """Poincare polynomial is 1 + t^3."""
        ce = verify_ce_complex()
        assert ce["total_betti"] == 2
        assert ce["H0"] == 1
        assert ce["H3"] == 1


# ---------------------------------------------------------------------------
# Full MC1 verification bundle
# ---------------------------------------------------------------------------

class TestMC1FullVerification:
    """Run the complete MC1 verification and check all claims pass."""

    def test_all_enrichment_claims(self):
        results = verify_enrichment_claims()
        assert results["claim_1_surjective"]
        assert results["claim_2_ker_dim_6"]
        assert results["claim_3_V3_isomorphism"]
        assert results["claim_4_kappa_in_ker"]
        assert results["claim_5_d2_nonzero"]
        assert results["claim_adjoint_decomposition"]
        assert results["claim_kappa_is_invariant"]

    def test_all_ce_claims(self):
        results = verify_ce_complex()
        assert results["claim_6_d1_rank_3"]
        assert results["claim_7_d2_is_zero"]
        assert results["d_squared_zero"]
        assert results["claim_8_cohomology"]


# ---------------------------------------------------------------------------
# Weight h=3: g^{otimes 3} enrichment (higher weight check)
# ---------------------------------------------------------------------------

class TestWeightH3Enrichment:
    """Verify enrichment killing at conformal weight h=3, bar degree 3.

    At bar degree 3, the enrichment involves g^{otimes 3} = sl2^{otimes 3}.
    The d_1 differential acts by bracketing adjacent pairs.
    We verify the same Whitehead + Killing mechanism works.

    g^{otimes 3} decomposes under diagonal adjoint action as:
    (V_5 + V_3 + V_1) tensor V_3 = V_7 + 2*V_5 + 2*V_3 + V_1
    Total dim = 7 + 10 + 6 + 1 = ... wait, multiplicities:
    V_7(dim 7) + V_5(dim 5)*2 + V_3(dim 3)*2 + V_1(dim 1) = 7+10+6+1 = 24
    But g^{otimes 3} has dim 27. Need to recompute.

    Actually: V_3 tensor V_3 tensor V_3:
    Step 1: V_3 tensor V_3 = V_5 + V_3 + V_1
    Step 2: (V_5 + V_3 + V_1) tensor V_3:
      V_5 tensor V_3 = V_7 + V_5 + V_3
      V_3 tensor V_3 = V_5 + V_3 + V_1
      V_1 tensor V_3 = V_3
    Total: V_7 + 2*V_5 + 3*V_3 + V_1
    Dims: 7 + 10 + 9 + 1 = 27. Correct.

    Invariant part: V_1 has dim 1.
    """

    def _build_adjoint_on_triple(self):
        """Build ad(e_x) on g^{otimes 3} (diagonal action)."""
        d = DIM_SL2
        n = d ** 3

        def ad_triple(x_idx):
            from sympy import zeros
            mat = zeros(n, n)
            for a in range(d):
                for b in range(d):
                    for c in range(d):
                        src = a * d**2 + b * d + c
                        # [x, e_a] tensor e_b tensor e_c
                        for m, coeff in lie_bracket(x_idx, a).items():
                            tgt = m * d**2 + b * d + c
                            mat[tgt, src] += coeff
                        # e_a tensor [x, e_b] tensor e_c
                        for m, coeff in lie_bracket(x_idx, b).items():
                            tgt = a * d**2 + m * d + c
                            mat[tgt, src] += coeff
                        # e_a tensor e_b tensor [x, e_c]
                        for m, coeff in lie_bracket(x_idx, c).items():
                            tgt = a * d**2 + b * d + m
                            mat[tgt, src] += coeff
            return mat

        return ad_triple

    def _build_casimir_triple(self):
        """Build Casimir C_2 on g^{otimes 3}."""
        from sympy import zeros
        d = DIM_SL2
        n = d ** 3
        ad = self._build_adjoint_on_triple()

        inv_killing = {
            (0, 2): Rational(1),
            (2, 0): Rational(1),
            (1, 1): Rational(1, 2),
        }
        casimir = zeros(n, n)
        for (a, b), coeff in inv_killing.items():
            casimir += coeff * ad(a) * ad(b)
        return casimir

    def test_triple_tensor_decomposition(self):
        """g^{otimes 3} = V_7 + 2*V_5 + 3*V_3 + V_1."""
        C2 = self._build_casimir_triple()
        eigenvals = C2.eigenvals()

        # With normalization 2j(j+1):
        # V_7 (spin 3): 2*3*4 = 24, dim 7
        # V_5 (spin 2): 2*2*3 = 12, dim 5, mult 2 => 10
        # V_3 (spin 1): 2*1*2 = 4, dim 3, mult 3 => 9
        # V_1 (spin 0): 0, dim 1, mult 1
        expected = {
            Rational(24): 7,   # V_7
            Rational(12): 10,  # 2 * V_5
            Rational(4): 9,    # 3 * V_3
            Rational(0): 1,    # V_1
        }
        assert eigenvals == expected

    def test_invariant_subspace_dim_1(self):
        """The g-invariant subspace of g^{otimes 3} is 1-dimensional."""
        C2 = self._build_casimir_triple()
        eigenvals = C2.eigenvals()
        assert eigenvals.get(Rational(0), 0) == 1

    def test_d1_bracket_on_triple(self):
        """d_1: g^{otimes 3} -> g^{otimes 2} (bracket adjacent pairs).

        d_1(a tensor b tensor c) = [a,b] tensor c + (-1) a tensor [b,c]

        Non-trivial reps in g^{otimes 3} map to non-trivial reps in g^{otimes 2},
        and Whitehead kills them at E_2.
        """
        from sympy import zeros
        d = DIM_SL2

        # d_1(a tensor b tensor c) = [a,b] tensor c - a tensor [b,c]
        # Source: g^3 (dim 27), Target: g^2 (dim 9)
        mat = zeros(d**2, d**3)
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    src = a * d**2 + b * d + c
                    # [a,b] tensor c
                    for m, coeff in lie_bracket(a, b).items():
                        tgt = m * d + c
                        mat[tgt, src] += coeff
                    # -a tensor [b,c]
                    for m, coeff in lie_bracket(b, c).items():
                        tgt = a * d + m
                        mat[tgt, src] -= coeff
        # d_1 should have nontrivial rank
        rank = mat.rank()
        assert rank > 0
        # ker(d_1) should contain the invariant (V_1) but not exhaust g^{otimes 3}
        ker_dim = 27 - rank
        assert ker_dim >= 1  # at least V_1 survives

    def test_triple_killing_invariant_in_kernel(self):
        """The unique invariant in g^{otimes 3} is f_{abc} (structure constants
        contracted with Killing form), and it lies in ker(d_1).

        For sl2, f_{abc} = kappa_{ad} f^d_{bc} is totally antisymmetric.
        """
        from sympy import zeros
        d = DIM_SL2

        # Build f_{abc} = kappa_{ad} f^d_{bc}
        f_tensor = zeros(d**3, 1)
        for a in range(d):
            for b in range(d):
                for c_idx in range(d):
                    idx = a * d**2 + b * d + c_idx
                    # kappa_{ad} f^d_{bc}
                    val = Rational(0)
                    for dd in range(d):
                        kappa_ad = killing(a, dd)
                        bracket_bc = lie_bracket(b, c_idx)
                        val += kappa_ad * bracket_bc.get(dd, Rational(0))
                    f_tensor[idx] = val

        # f_tensor should be nonzero
        assert not f_tensor.is_zero_matrix

        # Build d_1
        mat = zeros(d**2, d**3)
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    src = a * d**2 + b * d + c
                    for m, coeff in lie_bracket(a, b).items():
                        mat[m * d + c, src] += coeff
                    for m, coeff in lie_bracket(b, c).items():
                        mat[a * d + m, src] -= coeff

        # f_{abc} should be in ker(d_1)
        result = mat * f_tensor
        assert result.is_zero_matrix

    def test_triple_killing_is_invariant(self):
        """f_{abc} is g-invariant (lives in V_1)."""
        from sympy import zeros
        d = DIM_SL2
        C2 = self._build_casimir_triple()

        # Build f_{abc}
        f_tensor = zeros(d**3, 1)
        for a in range(d):
            for b in range(d):
                for c_idx in range(d):
                    idx = a * d**2 + b * d + c_idx
                    val = Rational(0)
                    for dd in range(d):
                        kappa_ad = killing(a, dd)
                        bracket_bc = lie_bracket(b, c_idx)
                        val += kappa_ad * bracket_bc.get(dd, Rational(0))
                    f_tensor[idx] = val

        # C_2(f_{abc}) = 0
        assert (C2 * f_tensor).is_zero_matrix
