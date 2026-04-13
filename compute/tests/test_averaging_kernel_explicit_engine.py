"""
Tests for averaging_kernel_explicit_engine.

Explicit basis verification for ker(av_n) in V^{tensor n} / Sym^n(V).

Verification sources for each expected value:
  [DC] direct computation   [LT] literature (Schur-Weyl duality)
  [LC] limiting case        [SY] symmetry (S_n action)
  [CF] cross-family         [DA] dimensional analysis

# VERIFIED: d=3,n=2: ker dim = 9-6 = 3 = C(3,2)  [DC] antisymmetric tensors [SY] Alt^2(C^3)
# VERIFIED: d=3,n=3: ker dim = 27-10 = 17 = 2*8+1 [DC] SVD [LT] Schur-Weyl: S^(2,1) dim = 3*8/3 = 8
# VERIFIED: d=3,n=4: ker dim = 81-15 = 66          [DC] SVD [LT] C(6,4)=15 symmetric
# VERIFIED: d=2,n=2: ker dim = 4-3 = 1             [DC] single antisymmetric [SY] Alt^2(C^2) = det
# VERIFIED: d=2,n=3: ker dim = 8-4 = 4             [DC] SVD [LT] C(4,2)=6 but wait, C(4,3)=4 symmetric
# VERIFIED: d=2,n=4: ker dim = 16-5 = 11           [DC] SVD [LT] C(5,4)=5 symmetric
# VERIFIED: Alt^3(C^3) = 1-dim (volume form)       [DC] explicit [SY] det representation
# VERIFIED: S^(2,1)(C^3) = 8-dim, multiplicity 2   [LT] hook-content formula [DC] Young symmetrizer rank
# VERIFIED: Schur-Weyl n=3,d=3: 10+16+1=27         [DC] [LT] partition dimensions sum to d^n
# VERIFIED: Schur-Weyl n=4,d=3: 15+45+12+9+0=81    [DC] [LT] hook-content formula
"""

from fractions import Fraction
from math import comb

import numpy as np
import pytest

from compute.lib.averaging_kernel_explicit_engine import (
    alternating_part_n3,
    antisymmetric_basis_n2,
    antisymmetric_basis_n2_labeled,
    basis_labels,
    enumerate_kernel_basis_labeled,
    kernel_basis_numerical,
    multi_index_to_label,
    schur_weyl_table_n2,
    schur_weyl_table_n4,
    sl2_ker_av2_basis,
    sl2_ker_av3_decomposition,
    standard_rep_part_n3,
    symmetrization_matrix,
    tensor_basis,
    verify_kernel_dim,
    verify_kernel_elements_in_kernel,
    verify_schur_weyl_n3,
)


# ── dimension verification: d=2 ────────────────────────────────────

class TestD2Dimensions:
    """d=2, n=2,3,4: verify ker(av_n) dimensions."""

    def test_d2_n2(self):
        # VERIFIED: [DC] 4-3=1; [SY] Alt^2(C^2)=det, 1-dim
        r = verify_kernel_dim(2, 2)
        assert r['expected_kernel_dim'] == 1
        assert r['computed_kernel_dim'] == 1
        assert r['match']

    def test_d2_n3(self):
        # VERIFIED: [DC] 8-4=4; [LT] C(4,2)=6 total sym, C(2+2,3)=4
        r = verify_kernel_dim(2, 3)
        assert r['expected_kernel_dim'] == 4
        assert r['computed_kernel_dim'] == 4
        assert r['match']

    def test_d2_n4(self):
        # VERIFIED: [DC] 16-5=11; [LT] C(5,4)=5 symmetric monomials
        r = verify_kernel_dim(2, 4)
        assert r['expected_kernel_dim'] == 11
        assert r['computed_kernel_dim'] == 11
        assert r['match']


# ── dimension verification: d=3 (sl_2 adjoint) ─────────────────────

class TestD3Dimensions:
    """d=3 (sl_2 adjoint), n=2,3,4: verify ker(av_n) dimensions."""

    def test_d3_n2(self):
        # VERIFIED: [DC] 9-6=3; [SY] Alt^2(C^3)=3-dim; [CF] matches averaging_kernel_engine
        r = verify_kernel_dim(3, 2)
        assert r['expected_kernel_dim'] == 3
        assert r['computed_kernel_dim'] == 3
        assert r['match']

    def test_d3_n3(self):
        # VERIFIED: [DC] 27-10=17; [LT] Schur-Weyl: 2*8+1=17; [CF] matches formula d^n-C(n+d-1,d-1)
        r = verify_kernel_dim(3, 3)
        assert r['expected_kernel_dim'] == 17
        assert r['computed_kernel_dim'] == 17
        assert r['match']

    def test_d3_n4(self):
        # VERIFIED: [DC] 81-15=66; [LT] C(6,4)=15 symmetric; [CF] matches averaging_kernel_engine
        r = verify_kernel_dim(3, 4)
        assert r['expected_kernel_dim'] == 66
        assert r['computed_kernel_dim'] == 66
        assert r['match']


# ── sl_2 explicit basis at n=2 ──────────────────────────────────────

class TestSl2KerAv2:
    """sl_2 (d=3): the 3 basis elements of ker(av_2) = Alt^2(sl_2)."""

    def test_basis_count(self):
        basis = sl2_ker_av2_basis()
        assert len(basis) == 3

    def test_basis_elements_are_antisymmetric(self):
        # VERIFIED: [DC] each is e_i tensor e_j - e_j tensor e_i with i < j
        basis = sl2_ker_av2_basis()
        assert 'e tensor h - h tensor e' in basis
        assert 'e tensor f - f tensor e' in basis
        assert 'h tensor f - f tensor h' in basis

    def test_antisymmetric_basis_count_formula(self):
        # Alt^2(V) has dim C(d,2)
        for d in [2, 3, 4, 5, 8]:
            basis = antisymmetric_basis_n2(d)
            assert len(basis) == comb(d, 2), (
                f"d={d}: got {len(basis)}, expected {comb(d,2)}"
            )

    def test_kernel_elements_genuinely_in_kernel_d3_n2(self):
        # VERIFIED: [DC] P*v = 0 for each basis vector
        assert verify_kernel_elements_in_kernel(3, 2)


# ── sl_2 decomposition at n=3 ───────────────────────────────────────

class TestSl2KerAv3:
    """sl_2 (d=3): 17-dim ker(av_3) = Alt^3 + 2*S^(2,1)."""

    def test_total_dim(self):
        decomp = sl2_ker_av3_decomposition()
        assert decomp['dim_ker'] == 17

    def test_alternating_dim(self):
        # VERIFIED: [DC] C(3,3)=1; [SY] unique volume form
        decomp = sl2_ker_av3_decomposition()
        assert decomp['alt3_dim'] == 1

    def test_hook_dim(self):
        # VERIFIED: [LT] hook-content: d(d^2-1)/3 = 3*8/3 = 8
        decomp = sl2_ker_av3_decomposition()
        assert decomp['hook21_dim'] == 8
        assert decomp['hook21_multiplicity'] == 2
        assert decomp['hook21_total'] == 16

    def test_decomposition_sums(self):
        decomp = sl2_ker_av3_decomposition()
        assert decomp['alt3_dim'] + decomp['hook21_total'] == decomp['dim_ker']

    def test_alternating_part_explicit(self):
        # VERIFIED: [DC] The volume form e^h^f has 6 terms with alternating signs
        alt = alternating_part_n3(3)
        assert alt is not None
        assert alt.shape == (1, 27)
        # Verify it is in the kernel
        P = symmetrization_matrix(3, 3)
        Pv = P @ alt[0]
        assert np.linalg.norm(Pv) < 1e-10

    def test_standard_rep_part_rank(self):
        # VERIFIED: [LT] 2 * dim S^(2,1)(C^3) = 2*8 = 16
        std = standard_rep_part_n3(3)
        assert std.shape[0] == 16

    def test_standard_rep_in_kernel(self):
        # Each standard-rep basis vector must be in ker(av_3)
        P = symmetrization_matrix(3, 3)
        std = standard_rep_part_n3(3)
        for i in range(std.shape[0]):
            Pv = P @ std[i]
            assert np.linalg.norm(Pv) < 1e-10, (
                f"Standard rep basis vector {i} NOT in kernel"
            )

    def test_kernel_elements_genuinely_in_kernel_d3_n3(self):
        assert verify_kernel_elements_in_kernel(3, 3)


# ── kernel membership: all (d,n) pairs ──────────────────────────────

class TestKernelMembership:
    """Every computed basis element satisfies P*v = 0."""

    @pytest.mark.parametrize("d,n", [
        (2, 2), (2, 3), (2, 4),
        (3, 2), (3, 3), (3, 4),
    ])
    def test_in_kernel(self, d, n):
        assert verify_kernel_elements_in_kernel(d, n)


# ── symmetrization projector properties ──────────────────────────────

class TestSymmetrizationMatrix:
    """Structural properties of the symmetrization projector P = av_n."""

    def test_idempotent_d2_n2(self):
        # P^2 = P (projector)
        P = symmetrization_matrix(2, 2)
        P2 = P @ P
        assert np.allclose(P, P2, atol=1e-12)

    def test_idempotent_d3_n2(self):
        P = symmetrization_matrix(3, 2)
        P2 = P @ P
        assert np.allclose(P, P2, atol=1e-12)

    def test_idempotent_d3_n3(self):
        P = symmetrization_matrix(3, 3)
        P2 = P @ P
        assert np.allclose(P, P2, atol=1e-12)

    def test_rank_equals_sym_dim(self):
        # rank(P) = dim Sym^n(V) = C(n+d-1, d-1)
        for d, n in [(2, 2), (2, 3), (3, 2), (3, 3), (3, 4)]:
            P = symmetrization_matrix(d, n)
            rank = np.linalg.matrix_rank(P, tol=1e-10)
            expected_rank = comb(n + d - 1, d - 1)
            assert rank == expected_rank, (
                f"d={d},n={n}: rank={rank}, expected={expected_rank}"
            )

    def test_symmetric(self):
        # P is symmetric (self-adjoint projector)
        for d, n in [(2, 2), (3, 2), (3, 3)]:
            P = symmetrization_matrix(d, n)
            assert np.allclose(P, P.T, atol=1e-12)


# ── Schur-Weyl decomposition verification ───────────────────────────

class TestSchurWeylN2:
    """V^{tensor 2} = Sym^2(V) + Alt^2(V)."""

    @pytest.mark.parametrize("d", [2, 3, 4, 5, 8])
    def test_decomposition_sums(self, d):
        sw = schur_weyl_table_n2(d)
        assert sw['match']
        assert sw['ker(av_2)'] == comb(d, 2)

    def test_d3_values(self):
        # VERIFIED: [DC] Sym^2(C^3)=6, Alt^2(C^3)=3
        sw = schur_weyl_table_n2(3)
        assert sw['Sym^2'] == 6
        assert sw['Alt^2'] == 3
        assert sw['total'] == 9


class TestSchurWeylN3:
    """V^{tensor 3} = S^(3)(V) + S^(2,1)(V)^2 + S^(1,1,1)(V)."""

    @pytest.mark.parametrize("d", [2, 3, 4, 5])
    def test_decomposition_sums(self, d):
        sw = verify_schur_weyl_n3(d)
        assert sw['total_match'], f"d={d}: Schur-Weyl sum mismatch"
        assert sw['ker_match'], f"d={d}: kernel dim mismatch"

    def test_d3_values(self):
        # VERIFIED: [DC][LT] S^(3)=10, S^(2,1)*2=16, S^(1,1,1)=1
        sw = verify_schur_weyl_n3(3)
        assert sw['S^(3)'] == 10
        assert sw['S^(2,1) x 2'] == 16
        assert sw['S^(1,1,1)'] == 1
        assert sw['ker(av_3)'] == 17

    def test_d2_values(self):
        # VERIFIED: [DC] S^(3)(C^2)=4, S^(2,1)(C^2)=2 each copy, Alt^3(C^2)=0
        sw = verify_schur_weyl_n3(2)
        assert sw['S^(3)'] == 4     # C(4,3)=4
        assert sw['S^(2,1) x 2'] == 4  # 2*(2*3/3)=4
        assert sw['S^(1,1,1)'] == 0    # C(2,3)=0
        assert sw['total_match']


class TestSchurWeylN4:
    """V^{tensor 4} = sum over partitions of 4."""

    @pytest.mark.parametrize("d", [2, 3, 4])
    def test_decomposition_sums(self, d):
        sw = schur_weyl_table_n4(d)
        assert sw['match'], f"d={d}: Schur-Weyl sum mismatch at n=4"
        assert sw['ker_match'], f"d={d}: kernel dim mismatch at n=4"

    def test_d3_n4_values(self):
        # VERIFIED: [DC][LT] hook-content formula for each partition
        sw = schur_weyl_table_n4(3)
        decomp = sw['decomposition']
        assert decomp['(4,)']['schur_dim'] == 15       # C(6,4)=15
        assert decomp['(3, 1)']['schur_dim'] == 15     # hook-content: 15
        assert decomp['(3, 1)']['multiplicity'] == 3
        assert decomp['(2, 2)']['schur_dim'] == 6      # hook-content: 6
        assert decomp['(2, 2)']['multiplicity'] == 2
        assert decomp['(2, 1, 1)']['schur_dim'] == 3   # hook-content: 3
        assert decomp['(2, 1, 1)']['multiplicity'] == 3
        assert decomp['(1, 1, 1, 1)']['schur_dim'] == 0  # C(3,4)=0, d < n
        assert sw['ker(av_4)'] == 66


# ── cross-checks with averaging_kernel_engine ────────────────────────

class TestCrossCheckWithDimEngine:
    """Verify explicit engine dimensions match the dimension engine."""

    @pytest.mark.parametrize("d,n", [
        (2, 2), (2, 3), (2, 4),
        (3, 2), (3, 3), (3, 4),
    ])
    def test_dimension_match(self, d, n):
        from compute.lib.averaging_kernel_engine import kernel_dim as dim_kernel_dim
        explicit_result = verify_kernel_dim(d, n)
        dim_result = dim_kernel_dim(d, n, "even")
        assert explicit_result['computed_kernel_dim'] == dim_result, (
            f"d={d},n={n}: explicit={explicit_result['computed_kernel_dim']}, "
            f"dim_engine={dim_result}"
        )


# ── alternating part vanishing ───────────────────────────────────────

class TestAlternatingPartVanishing:
    """Alt^n(V) = 0 when n > d."""

    def test_alt3_d2_vanishes(self):
        alt = alternating_part_n3(2)
        assert alt is None

    def test_alt3_d3_nonzero(self):
        alt = alternating_part_n3(3)
        assert alt is not None
        assert alt.shape[0] == 1  # C(3,3) = 1

    def test_alt3_d4_three_elements(self):
        alt = alternating_part_n3(4)
        assert alt is not None
        assert alt.shape[0] == comb(4, 3)  # 4


# ── basis labeling ──────────────────────────────────────────────────

class TestBasisLabeling:
    """Verify basis label conventions."""

    def test_d3_labels(self):
        assert basis_labels(3) == ['e', 'h', 'f']

    def test_d2_labels(self):
        assert basis_labels(2) == ['e_0', 'e_1']

    def test_tensor_basis_count(self):
        for d in [2, 3]:
            for n in [2, 3, 4]:
                tb = tensor_basis(d, n)
                assert len(tb) == d ** n


# ── structural: ker(av_1) = 0 always ────────────────────────────────

class TestArity1Trivial:
    """At n=1, av is the identity: ker(av_1) = 0."""

    @pytest.mark.parametrize("d", [1, 2, 3, 4, 8])
    def test_kernel_zero_at_n1(self, d):
        r = verify_kernel_dim(d, 1)
        assert r['expected_kernel_dim'] == 0
        assert r['computed_kernel_dim'] == 0


# ── d=1: ker(av_n) = 0 always ──────────────────────────────────────

class TestD1Trivial:
    """At d=1 (Heisenberg/Virasoro), ker(av_n) = 0 for all n."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_kernel_zero_d1(self, n):
        r = verify_kernel_dim(1, n)
        assert r['expected_kernel_dim'] == 0
        assert r['computed_kernel_dim'] == 0


# ── orthogonality of decomposition at n=3, d=3 ──────────────────────

class TestOrthogonalityN3D3:
    """Alt^3 and S^(2,1) parts span complementary subspaces of ker(av_3)."""

    def test_combined_rank(self):
        alt = alternating_part_n3(3)
        std = standard_rep_part_n3(3)
        # Stack both
        combined = np.vstack([alt, std])
        rank = np.linalg.matrix_rank(combined, tol=1e-10)
        assert rank == 17, f"Combined rank = {rank}, expected 17"

    def test_alt_not_in_standard_span(self):
        # The alternating element should not be in the span of standard-rep elements
        alt = alternating_part_n3(3)
        std = standard_rep_part_n3(3)
        # Project alt onto the span of std
        # If std has rank 16, the projection should not be all of alt
        # since alt is 1-dim and independent
        combined = np.vstack([std, alt])
        rank = np.linalg.matrix_rank(combined, tol=1e-10)
        assert rank == 17  # 16 + 1 = 17, confirming independence


# ── large dimension check (d=8, sl_3 adjoint) ───────────────────────

class TestSl3Adjoint:
    """d=8 (sl_3 adjoint): verify at n=2."""

    def test_d8_n2(self):
        # VERIFIED: [DC] 64-36=28; [SY] Alt^2(C^8) = C(8,2) = 28
        r = verify_kernel_dim(8, 2)
        assert r['expected_kernel_dim'] == 28
        assert r['computed_kernel_dim'] == 28
        assert r['match']

    def test_d8_n2_kernel_in_kernel(self):
        assert verify_kernel_elements_in_kernel(8, 2)
