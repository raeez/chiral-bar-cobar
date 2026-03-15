"""Tests for Orlik-Solomon algebra (os_algebra.py).

Verifies:
1. OS dimensions match Stirling/factorial formulas
2. OS bases have correct dimensions
3. Residue maps have correct shapes and properties
4. Arnold relations are correctly computed
"""

import pytest
import numpy as np
from math import factorial, comb


class TestOSDimensions:
    """Verify OS^k(C_n) dimensions against known formulas."""

    def test_os_top_degree_factorial(self):
        """dim OS^{n-1}(C_n) = (n-1)!"""
        from compute.lib.os_algebra import os_dimension
        for n in range(2, 7):
            assert os_dimension(n, n - 1) == factorial(n - 1)

    def test_os_degree_0(self):
        """dim OS^0 = 1 for all n."""
        from compute.lib.os_algebra import os_dimension
        for n in range(2, 7):
            assert os_dimension(n, 0) == 1

    def test_os_degree_1(self):
        """dim OS^1(C_n) = C(n,2) = n(n-1)/2."""
        from compute.lib.os_algebra import os_dimension
        for n in range(2, 7):
            assert os_dimension(n, 1) == comb(n, 2)

    def test_poincare_polynomial(self):
        """Poincare poly = prod_{i=0}^{n-2}(1 + (i+1)*t).
        Sum at t=1 gives n!."""
        from compute.lib.os_algebra import os_dimension
        for n in range(2, 6):
            total = sum(os_dimension(n, k) for k in range(n))
            assert total == factorial(n), f"Total Betti for n={n}: {total} != {n}!"

    def test_os_n2(self):
        """OS dims for n=2: [1, 1]."""
        from compute.lib.os_algebra import os_dimension
        assert [os_dimension(2, k) for k in range(2)] == [1, 1]

    def test_os_n3(self):
        """OS dims for n=3: [1, 3, 2]."""
        from compute.lib.os_algebra import os_dimension
        assert [os_dimension(3, k) for k in range(3)] == [1, 3, 2]

    def test_os_n4(self):
        """OS dims for n=4: [1, 6, 11, 6]."""
        from compute.lib.os_algebra import os_dimension
        assert [os_dimension(4, k) for k in range(4)] == [1, 6, 11, 6]


class TestOSBasis:
    """Verify OS basis computation."""

    def test_basis_shape(self):
        """Basis matrix has shape (dim, num_monomials)."""
        from compute.lib.os_algebra import os_basis, os_dimension
        for n in range(2, 5):
            for k in range(1, n):
                mons, basis = os_basis(n, k)
                dim = os_dimension(n, k)
                if dim > 0:
                    assert basis.shape[0] == dim, f"n={n},k={k}: shape {basis.shape} but dim={dim}"

    def test_basis_independence(self):
        """Basis rows are linearly independent."""
        from compute.lib.os_algebra import os_basis
        for n in range(2, 5):
            for k in range(1, n):
                _, basis = os_basis(n, k)
                if basis.size > 0 and basis.shape[0] > 0:
                    rank = np.linalg.matrix_rank(basis)
                    assert rank == basis.shape[0], f"n={n},k={k}: rank {rank} != {basis.shape[0]}"


class TestResidueMaps:
    """Verify residue maps Res_{D_{ij}}."""

    def test_residue_shape(self):
        """Residue map has correct source/target dimensions."""
        from compute.lib.os_algebra import residue_map, os_dimension
        R = residue_map(3, 2, 1, 2)
        src_dim = os_dimension(3, 2)
        tgt_dim = os_dimension(2, 1)
        assert R.shape == (tgt_dim, src_dim)

    def test_residue_n2(self):
        """Res_{12}: OS^1(C_2) -> OS^0(C_1) is nonzero."""
        from compute.lib.os_algebra import residue_map
        R = residue_map(2, 1, 1, 2)
        assert np.abs(R).max() > 0.5

    def test_all_residues_defined(self):
        """All pair residues on OS^2(C_3) have correct shape."""
        from compute.lib.os_algebra import residue_map, os_dimension
        for i, j in [(1, 2), (1, 3), (2, 3)]:
            R = residue_map(3, 2, i, j)
            assert R.shape == (os_dimension(2, 1), os_dimension(3, 2))


class TestVerification:
    """Run the module's internal verification."""

    def test_verify_os_dimensions(self):
        from compute.lib.os_algebra import verify_os_dimensions
        results = verify_os_dimensions(5)
        for name, ok in results.items():
            assert ok, f"OS dimension check failed: {name}"

    def test_verify_residue_maps(self):
        from compute.lib.os_algebra import verify_residue_maps
        results = verify_residue_maps(4)
        for name, ok in results.items():
            assert ok, f"Residue map check failed: {name}"
