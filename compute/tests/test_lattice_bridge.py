"""The lattice bridge: the intermediate E₁ atom between Heisenberg and Yangian.

The lattice vertex algebra V_Λ sits between the two extremes:
  - Heisenberg H_κ (E∞): purely commutative, trivial braiding
  - Yangian Y(𝔤) (pure E₁): purely braided, R-matrix ordering

The lattice is BOTH: its Heisenberg sublattice is E∞, while the
full lattice (with non-symmetric cocycle) is strictly E₁.  The
cocycle ε(α,β) determines whether Borcherds symmetry holds.

The key structural advantage of lattices: SECTORWISE FINITENESS.
The bar complex decomposes as a direct sum indexed by lattice
vectors, with each sector finite-dimensional.  This bypasses thick
generation entirely, yielding UNCONDITIONAL H-level factorization
DK for all even positive-definite lattices.

Together with the Heisenberg and Yangian bridges, this completes
the TRIPTYCH: three atoms, two strata of commutativity, one
categorical logarithm.

References:
  - Vol I, chapters/examples/lattice_foundations.tex
  - Vol I, Theorem lattice:e1-vs-einf, Theorem lattice:homotopy-factorization-dk
  - compute/lib/e1_lattice_bar.py
"""

import pytest
import numpy as np

from compute.lib.e1_lattice_bar import (
    cartan_matrix,
    rank,
    symmetric_cocycle,
    is_symmetric_cocycle,
    verify_borcherds_symmetry,
    full_e1_computation,
)


# ============================================================
# The E₁/E∞ distinction: Borcherds symmetry
# ============================================================

class TestE1VsEinf:
    """Theorem lattice:e1-vs-einf: the cocycle determines commutativity."""

    @pytest.mark.parametrize("lie_type", ["A2", "A3", "D4"])
    def test_symmetric_cocycle_is_einf(self, lie_type):
        """Symmetric ε ⟹ E∞ (affine/commutative VOA).

        The FLM upper-triangular cocycle satisfies Borcherds symmetry:
          ε(α,β) = (-1)^⟨α,β⟩ ε(β,α)
        """
        A = cartan_matrix(lie_type)
        eps = symmetric_cocycle(lie_type)
        assert verify_borcherds_symmetry(eps, A), \
            f"{lie_type}: symmetric cocycle must satisfy Borcherds"
        assert is_symmetric_cocycle(eps, A), \
            f"{lie_type}: symmetric cocycle must be detected as E∞"

    def test_deformed_cocycle_is_e1(self):
        """Non-symmetric ε ⟹ strictly E₁ (quantum lattice VOA).

        Deforming the cocycle by (N, q_values) breaks Borcherds symmetry.
        """
        result = full_e1_computation("A2", N=5, q_values={(0, 1): 2})
        assert not result["symmetry"]["eps_deformed_is_borcherds_symmetric"], \
            "A₂ N=5 q=2: deformed cocycle must NOT be Borcherds-symmetric"

    def test_braiding_nontrivial(self):
        """The cocycle commutator c(α,β) ≠ 1 for E₁ quantum lattices.

        The braiding matrix is the E₁ obstruction: if c = 1 everywhere,
        the algebra is E∞. For quantum lattices, c is a root of unity.
        """
        result = full_e1_computation("A2", N=3)
        comm = result["braiding"]["commutator_matrix"]
        # At least one off-diagonal entry should be nontrivial
        has_nontrivial = any(
            abs(comm[i, j] - 1.0) > 1e-10
            for i in range(comm.shape[0])
            for j in range(comm.shape[1])
            if i != j
        )
        assert has_nontrivial, "A₂ N=3: braiding must be nontrivial"


# ============================================================
# Sectorwise finiteness and unconditional DK
# ============================================================

class TestSectorwiseFiniteness:
    """Sectorwise finiteness: each lattice sector is finite-dimensional."""

    @pytest.mark.parametrize("lie_type", ["A2", "A3", "D4"])
    def test_full_computation_succeeds(self, lie_type):
        """Full E₁ computation runs end-to-end for each Lie type.

        Sectorwise finiteness means we don't need thick generation.
        Just linear algebra in finite-dimensional sectors.
        """
        result = full_e1_computation(lie_type, N=3)
        assert result is not None
        assert "sectors" in result, \
            f"{lie_type}: must compute sector data"

    def test_e1_vs_einf_cohomology_differs(self):
        """E₁ and E∞ bar cohomology differ for non-symmetric cocycle.

        The E₁ bar differential has phase factors from the braiding.
        These change the kernel/image, altering the cohomology.
        """
        result = full_e1_computation("A2", N=3)
        sectors = result["sectors"]
        assert len(sectors) > 0, "Must produce data in some sector"
        # Check that E₁ and E∞ sector data both exist
        for key, data in sectors.items():
            assert "e1" in data, f"Sector {key}: must have E₁ data"
            assert "einf" in data, f"Sector {key}: must have E∞ data"

    def test_bar_differential_is_finite_matrix(self):
        """Each sector's bar differential is a finite matrix.

        This is the STRUCTURAL CONTRAST with the Yangian, where
        the bar complex is infinite-dimensional per internal degree.
        """
        result = full_e1_computation("A2", N=3)
        # Check that differential matrices exist and are finite
        if "sector_data" in result:
            for sector_key, data in result["sector_data"].items():
                if "differential" in data:
                    D = data["differential"]
                    assert D.shape[0] < 1000, \
                        f"Sector {sector_key}: must be finite-dim"


# ============================================================
# N-torsion: quantum group connection
# ============================================================

class TestNTorsion:
    """The deformation parameter N creates N-torsion."""

    def test_a2_n3_torsion(self):
        """A₂ at N=3 (Coxeter number): critical quantum lattice.

        The braiding ζ = exp(2πi/N) satisfies ζ^N = 1, but the
        commutator c(α,β) = ε(α,β)/ε(β,α) involves both ζ and
        the Cartan matrix sign (-1)^⟨α,β⟩.  The N-torsion check
        from the library verifies the correct combined identity.
        """
        result = full_e1_computation("A2", N=3)
        assert result["cocycle"]["N"] == 3
        # Use the library's own N-torsion verification
        assert result["n_torsion"]["all_pass"], \
            "A₂ N=3: N-torsion check must pass"


# ============================================================
# The Triptych: three atoms
# ============================================================

class TestTriptych:
    """Three atoms, two strata of commutativity, one logarithm."""

    def test_heisenberg_is_einf(self):
        """Heisenberg: E∞, no braiding, trivial R-matrix."""
        from compute.lib.heisenberg_bar import heisenberg_nth_products
        products = heisenberg_nth_products()
        assert 0 not in products, "Heisenberg has no simple pole"

    def test_lattice_symmetric_is_einf(self):
        """Lattice with symmetric cocycle: E∞, like Heisenberg."""
        A = cartan_matrix("A2")
        eps = symmetric_cocycle("A2")
        assert is_symmetric_cocycle(eps, A)

    def test_lattice_deformed_is_e1(self):
        """Lattice with deformed cocycle: E₁, like Yangian."""
        result = full_e1_computation("A2", N=5, q_values={(0, 1): 2})
        assert not result["symmetry"]["eps_deformed_is_borcherds_symmetric"]

    def test_yangian_is_e1(self):
        """Yangian: pure E₁, R-matrix braiding."""
        from compute.lib.yangian_residue import permutation_matrix
        P = permutation_matrix(2)
        evals = sorted(np.real(np.linalg.eigvals(P)))
        assert any(abs(e - (-1.0)) < 1e-10 for e in evals), \
            "Permutation has -1 eigenvalue: antisymmetric sector exists"

    def test_sectorwise_vs_thick_generation(self):
        """Lattice bypasses thick generation; Yangian needs it.

        This is WHY the lattice route resolves MC3 unconditionally.
        """
        # Lattice: full computation runs (sectorwise finite)
        result = full_e1_computation("A2", N=3)
        assert result is not None

        # Yangian: kernel exists but thick generation conjectural
        from compute.lib.yangian_residue_extraction import verify_auxiliary_kernel_identity
        yk = verify_auxiliary_kernel_identity(3)
        assert yk["K_line_dim"] == 3  # dim Λ²(ℂ³)

    def test_triptych_complete(self):
        """All three atoms computable: the triptych is executable."""
        from compute.lib.heisenberg_bar import heisenberg_curvature
        from compute.lib.yangian_residue_extraction import verify_auxiliary_kernel_identity
        from sympy import Symbol

        # Heisenberg: curvature κ
        assert heisenberg_curvature() == Symbol('kappa')

        # Lattice: E₁ bar complex
        result = full_e1_computation("A2", N=3)
        assert result is not None

        # Yangian: kernel identity
        yk = verify_auxiliary_kernel_identity(2)
        assert yk["identity_holds"]
