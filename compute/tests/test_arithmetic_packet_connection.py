"""Tests for arithmetic packet connection (thm:packet-connection-flatness et al.).

Verifies:
  1. Flatness is automatic in 1D (thm:packet-connection-flatness(i))
  2. Divisor independence from nilpotent parts (thm:packet-connection-flatness(ii))
  3. Lattice transparency: all N_chi = 0 (cor:lattice-packet-diagonal)
  4. Depth decomposition consistency (thm:depth-decomposition)
  5. Heisenberg packet is rank-1 diagonal
  6. E8 packet has no cusp forms
  7. Leech packet has exactly 1 cusp form (Delta_12)
  8. Miura splitting for W_N (prop:miura-packet-splitting)
  9. Frontier defect form is generically nonzero (rem:packet-reformulation)
  10. Horizontal section commutativity (thm:packet-connection-flatness(iii))
  11. Cusp dimension formula for standard weights
  12. Scattering matrix functional equation
"""

import cmath
import math
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest

from lib.arithmetic_packet_connection import (
    LatticePacket,
    HeisenbergPacket,
    E8Packet,
    LeechPacket,
    WNPacketSplitting,
    verify_flatness_rank1,
    verify_flatness_block_diagonal,
    verify_depth_decomposition,
    verify_horizontal_section_commutativity,
    frontier_defect_nonzero,
    scattering_matrix,
    completed_zeta,
)


# ---------------------------------------------------------------------------
# Packet module structure tests
# ---------------------------------------------------------------------------

class TestPacketModuleStructure:
    """Tests for def:arithmetic-packet-module."""

    def test_heisenberg_rank(self):
        """Heisenberg packet module is rank 1 (Eisenstein only, no cusp forms)."""
        p = HeisenbergPacket()
        assert p.module_rank == 1
        assert p.cusp_dim == 0

    def test_e8_rank(self):
        """E8 lattice: weight 4, S_4(SL(2,Z)) = {0}, so rank = 1."""
        p = E8Packet()
        assert p.module_rank == 1
        assert p.cusp_dim == 0

    def test_leech_rank(self):
        """Leech lattice: weight 12, dim S_12 = 1 (Ramanujan Delta), rank = 2."""
        p = LeechPacket()
        assert p.module_rank == 2
        assert p.cusp_dim == 1

    def test_rank_16_lattice(self):
        """Rank 16 lattice: weight 8, dim S_8 = 0, rank = 1."""
        p = LatticePacket(rank=16)
        assert p.cusp_dim == 0
        assert p.module_rank == 1

    def test_rank_32_lattice(self):
        """Rank 32 lattice: weight 16, dim S_16 = 1, rank = 2."""
        p = LatticePacket(rank=32)
        assert p.cusp_dim == 1
        assert p.module_rank == 2

    def test_rank_48_lattice(self):
        """Rank 48 lattice: weight 24, dim S_24 = 2, rank = 3."""
        p = LatticePacket(rank=48)
        assert p.cusp_dim == 2
        assert p.module_rank == 3


class TestCuspDimension:
    """Verify cusp dimension formula dim S_k(SL(2,Z))."""

    @pytest.mark.parametrize("k,expected", [
        (2, 0), (4, 0), (6, 0), (8, 0), (10, 0),
        (12, 1), (14, 0), (16, 1), (18, 1), (20, 1),
        (22, 1), (24, 2), (26, 1), (28, 2), (30, 2),
        (32, 2), (34, 2), (36, 3),
    ])
    def test_cusp_dim(self, k, expected):
        """Standard cusp dimension for weight k."""
        assert LatticePacket._cusp_dimension(k) == expected


# ---------------------------------------------------------------------------
# Lattice transparency tests (cor:lattice-packet-diagonal)
# ---------------------------------------------------------------------------

class TestLatticeTransparency:
    """Tests for cor:lattice-packet-diagonal: all N_chi = 0 for lattice VOAs."""

    def test_heisenberg_diagonal(self):
        p = HeisenbergPacket()
        assert p.is_diagonal

    def test_e8_diagonal(self):
        p = E8Packet()
        assert p.is_diagonal

    def test_leech_diagonal(self):
        p = LeechPacket()
        assert p.is_diagonal

    @pytest.mark.parametrize("rank", [8, 16, 24, 32, 40, 48])
    def test_lattice_always_diagonal(self, rank):
        """All lattice VOAs have diagonal packet connection."""
        p = LatticePacket(rank=rank)
        assert p.is_diagonal
        assert p.d_alg == 0


# ---------------------------------------------------------------------------
# Depth decomposition tests (thm:depth-decomposition)
# ---------------------------------------------------------------------------

class TestDepthDecomposition:
    """Tests for thm:depth-decomposition: d = 1 + d_arith + d_alg."""

    def test_heisenberg_depth(self):
        p = HeisenbergPacket()
        assert verify_depth_decomposition(p)
        assert p.d_alg == 0

    def test_e8_depth(self):
        p = E8Packet()
        assert verify_depth_decomposition(p)

    def test_leech_depth(self):
        p = LeechPacket()
        assert verify_depth_decomposition(p)

    @pytest.mark.parametrize("rank", [8, 16, 24, 32, 40, 48])
    def test_lattice_depth_formula(self, rank):
        """d = 3 + dim S_{r/2} for lattice VOAs."""
        p = LatticePacket(rank=rank)
        assert verify_depth_decomposition(p)


# ---------------------------------------------------------------------------
# Flatness tests (thm:packet-connection-flatness)
# ---------------------------------------------------------------------------

class TestFlatness:
    """Tests for thm:packet-connection-flatness(i): (nabla^arith)^2 = 0."""

    def test_flatness_automatic_1d(self):
        """Flatness is automatic for meromorphic connections on the s-line."""
        s_vals = [complex(2.0, 0.5), complex(3.0, 1.0), complex(1.5, 2.0)]
        assert verify_flatness_rank1(s_vals, lambda s: sum(n ** (-s) for n in range(1, 100)))

    def test_flatness_block_diagonal(self):
        """Block-diagonal connection is flat iff each block is flat."""
        blocks = [
            {'omega': lambda s: 1 / s, 'E': [[1]]},
            {'omega': lambda s: 1 / (s - 1), 'E': [[1, 1], [0, 1]]},
        ]
        assert verify_flatness_block_diagonal(blocks)


# ---------------------------------------------------------------------------
# Horizontal section commutativity (thm:packet-connection-flatness(iii))
# ---------------------------------------------------------------------------

class TestHorizontalSections:
    """Tests for the commutativity in horizontal section formula."""

    def test_scalar_nilpotent_commute(self):
        """exp(c*(id + N)) = exp(c*id) * exp(c*N) when N is nilpotent."""
        assert verify_horizontal_section_commutativity()


# ---------------------------------------------------------------------------
# Miura splitting tests (prop:miura-packet-splitting)
# ---------------------------------------------------------------------------

class TestMiuraSplitting:
    """Tests for prop:miura-packet-splitting: W_N packet = (N-1)*H + defect."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_heisenberg_copies(self, N):
        """W_N has exactly N-1 Heisenberg copies."""
        w = WNPacketSplitting(N)
        assert w.heisenberg_copies == N - 1

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_euler_koszul_rank(self, N):
        """Defect dimension is N-2 (the Euler-Koszul rank)."""
        w = WNPacketSplitting(N)
        assert w.euler_koszul_rank == N - 2

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: 1 Heisenberg copy, 0 defect dimension."""
        w = WNPacketSplitting(2)
        assert w.heisenberg_copies == 1
        assert w.euler_koszul_rank == 0

    def test_w3_defect(self):
        """W_3: 2 Heisenberg copies, 1 defect mode."""
        w = WNPacketSplitting(3)
        assert w.heisenberg_copies == 2
        assert w.euler_koszul_rank == 1

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_sewing_lift_structural(self, N):
        """Sewing lift decomposes into Heisenberg + defect parts."""
        w = WNPacketSplitting(N)
        u_vals = [complex(2.0, 0.0), complex(3.0, 0.5), complex(2.5, 1.0)]
        assert w.verify_additive_decomposition(u_vals)

    def test_defect_polynomial_finite(self):
        """Defect Dirichlet polynomial is a finite sum for each N."""
        for N in [2, 3, 4, 5, 10]:
            w = WNPacketSplitting(N)
            u = complex(3.0, 0.0)
            val = w.defect_dirichlet_polynomial(u)
            assert isinstance(val, (complex, float))
            assert not math.isinf(abs(val))


# ---------------------------------------------------------------------------
# Frontier defect form tests (def:frontier-defect-form)
# ---------------------------------------------------------------------------

class TestFrontierDefectForm:
    """Tests for def:frontier-defect-form: Omega_A = d log Lambda_Eis - d log phi."""

    def test_frontier_defect_generically_nonzero(self):
        """Omega_{V_Lambda} != 0 in general (rem:packet-reformulation)."""
        p = LeechPacket()
        s_values = [complex(2.0, t) for t in [0.5, 1.0, 1.5, 2.0, 3.0]]
        assert frontier_defect_nonzero(p, s_values)

    def test_scattering_matrix_computed(self):
        """Scattering matrix phi(s) is computable at generic s."""
        s = complex(2.0, 1.0)
        phi = scattering_matrix(s, terms=100)
        assert phi != float('inf')
        assert abs(phi) > 0

    def test_scattering_functional_equation(self):
        """phi(s) * phi(1-s) should be close to 1 (involution property)."""
        for t in [0.5, 1.0, 2.0, 3.0]:
            s = complex(0.5, t)
            phi_s = scattering_matrix(s, terms=150)
            phi_1ms = scattering_matrix(1 - s, terms=150)
            if phi_s != float('inf') and phi_1ms != float('inf'):
                product = phi_s * phi_1ms
                # phi(s)*phi(1-s) = 1 is the involution property
                assert abs(product - 1.0) < 0.5, f"phi({s})*phi({1-s}) = {product}"


# ---------------------------------------------------------------------------
# Arithmetic skeleton vs algebraic defect (rem:arithmetic-homotopy-dictionary)
# ---------------------------------------------------------------------------

class TestArithmeticHomotopyDictionary:
    """Tests for the principle: arithmetic is semisimple, defect is unipotent."""

    @pytest.mark.parametrize("rank", [8, 16, 24, 32, 48])
    def test_lattice_pure_arithmetic(self, rank):
        """Lattice VOAs have d_alg = 0: pure arithmetic, no defect."""
        p = LatticePacket(rank=rank)
        assert p.d_alg == 0
        assert p.is_diagonal

    def test_skeleton_controls_divisor(self):
        """Number of divisor components = d_arith + 1 (including Eisenstein)."""
        for rank in [8, 16, 24, 32, 48]:
            p = LatticePacket(rank=rank)
            # For lattice: d_arith = 2 + cusp_dim
            # Divisor components: 1 (Eisenstein) + cusp_dim (each L(s,f_j))
            # = module_rank
            assert p.module_rank == 1 + p.cusp_dim
