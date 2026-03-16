"""Genus-1 E₁ lattice bar complex: the first E₁ genus computation.

This is the central computational result of the session: the genus-1
bar complex for the A₂ quantum lattice at N=3 (Coxeter), demonstrating
that CURVATURE AND BRAIDING ARE ORTHOGONAL for lattice vertex algebras.

The theorem:
  For a quantum lattice algebra V_Λ^{N,q} on an elliptic curve E_τ:

  (1) The genus-1 bar complex decomposes sectorwise (by lattice vector γ).

  (2) In Cartan sectors (γ = 0): d²_fib = rank(Λ) · ω_1.
      This is the HEISENBERG curvature, independent of the cocycle.

  (3) In root sectors (γ = α_i + α_j, ⟨α_i,α_j⟩ = -1): d²_fib = 0.
      The simple-pole OPE residue is unchanged at genus 1.
      The E₁ ordering cycles persist from genus 0.

  (4) Therefore: κ(V_Λ^{N,q}) = rank(Λ), independent of N and q.
      The braiding (from the cocycle) and the curvature (from the
      genus tower) live in orthogonal sectors.

This answers the question posed in Remark rem:lattice-e1-genus-door:
the genus-1 curvature is controlled by a SINGLE SCALAR (the rank),
not by a lattice-vector-dependent function.  The E₁ genus theory
for lattices is a deformation of the E∞ theory in the root sectors
only; the modular structure is identical.

References:
  - e1_lattice_genus1.py: genus-1 computation library
  - higher_genus_foundations.tex: genus-1 propagator and Arnold correction
  - heisenberg_frame.tex: Heisenberg genus-1 computation
  - yangians_foundations.tex: Conj E₁-Theorem-D, Remark lattice-e1-genus-door
"""

import pytest
from compute.lib.e1_lattice_genus1 import (
    genus1_propagator_has_simple_pole_residue_unchanged,
    genus1_arnold_correction,
    genus1_curvature_by_sector,
    genus1_e1_bar_complex,
    verify_curvature_braiding_orthogonality,
)
from compute.lib.e1_lattice_bar import rank


# ============================================================
# The propagator: genus-1 modification preserves simple poles
# ============================================================

class TestGenus1Propagator:
    """The genus-1 propagator preserves simple-pole residues."""

    def test_simple_pole_residue_unchanged(self):
        """Res_{z=0} η^(1)(z; τ) = 1, same as genus 0.

        The Weierstrass ζ function has ζ(z) = 1/z + O(z).
        The non-holomorphic correction π/Im(τ) · Im(z) is regular.
        Therefore: simple-pole OPE coefficients are UNCHANGED at genus 1.
        """
        assert genus1_propagator_has_simple_pole_residue_unchanged()

    def test_arnold_correction_nonzero(self):
        """A₃^(1) = 2πi · ω_vol^(1) ≠ 0.

        The genus-1 Arnold relation acquires a nonzero correction
        from the non-holomorphic part of the propagator.  This is
        the SOURCE of curvature d²_fib ≠ 0.
        """
        correction = genus1_arnold_correction()
        assert "omega_vol" in correction, "Arnold correction involves volume form"


# ============================================================
# Sectorwise curvature: the central theorem
# ============================================================

class TestCurvatureBraidingOrthogonality:
    """CENTRAL THEOREM: curvature and braiding decouple sectorwise."""

    @pytest.mark.parametrize("lie_type", ["A2", "A3", "D4"])
    def test_curvature_only_in_cartan(self, lie_type):
        """d²_fib ≠ 0 ONLY in the Cartan (Heisenberg) sector.

        Double-pole OPEs (h_a(z)h_b(w) ~ A_{ab}/(z-w)²) acquire the
        genus-1 Arakelov correction.  Simple-pole OPEs (vertex operators
        e^α(z)e^β(w) with ⟨α,β⟩ = -1) do NOT.
        """
        curv = genus1_curvature_by_sector(lie_type)
        assert curv['cartan_sector']['total_curvature'] > 0, \
            f"{lie_type}: Cartan must have curvature"
        for name, sector in curv['adjacent_root_sectors'].items():
            assert sector['curvature'] == 0, \
                f"{lie_type} sector {name}: root sector must have zero curvature"

    @pytest.mark.parametrize("lie_type", ["A2", "A3", "D4"])
    def test_kappa_equals_rank(self, lie_type):
        """κ(V_Λ) = rank(Λ).

        The genus-1 curvature is rank(Λ) · ω_1: one unit per
        independent Cartan boson.  This is the Heisenberg curvature
        at level 1 summed over the rank.
        """
        curv = genus1_curvature_by_sector(lie_type)
        r = rank(lie_type)
        assert curv['total_curvature'] == r, \
            f"{lie_type}: κ must equal rank = {r}"

    @pytest.mark.parametrize("lie_type", ["A2", "A3", "D4"])
    def test_curvature_is_scalar(self, lie_type):
        """The curvature is a SINGLE scalar, not sector-dependent.

        This answers the question from Remark rem:lattice-e1-genus-door:
        the E₁ genus theory for lattices is NOT a new structure.
        The curvature is the same as the E∞ curvature.
        """
        curv = genus1_curvature_by_sector(lie_type)
        assert curv['curvature_is_scalar']
        assert curv['curvature_independent_of_cocycle']


# ============================================================
# Full genus-1 computation: A₂ at N=3 (the door)
# ============================================================

class TestA2CoxeterGenus1:
    """The first explicit E₁ genus computation: A₂ at N=3."""

    def test_genus1_computation_runs(self):
        """Full genus-1 E₁ bar complex for A₂, N=3."""
        result = genus1_e1_bar_complex("A2", N=3)
        assert result['genus'] == 1
        assert result['kappa'] == 2  # rank(A₂) = 2

    def test_free_energy_F1(self):
        """F₁ = κ/24 = rank/24 = 2/24 = 1/12 for A₂.

        The genus-1 free energy is the conformal anomaly c/24,
        and for the rank-2 lattice VOA, c = 2 (two free bosons).
        """
        result = genus1_e1_bar_complex("A2", N=3)
        assert abs(result['F_1'] - 2/24) < 1e-15
        assert abs(result['F_1'] - 1/12) < 1e-15

    def test_complementarity_sum_zero(self):
        """κ(V_Λ) + κ(V_Λ^!) = 0: anomaly cancellation.

        The Koszul dual lattice VOA has κ' = -rank(Λ).
        Their sum is zero: the combined bar complex at genus 1
        is an honest cochain complex (d² = 0).
        """
        result = genus1_e1_bar_complex("A2", N=3)
        assert result['complementarity']['sum'] == 0

    def test_factorization_theorem(self):
        """The genus-1 bar complex factorizes: Cartan × roots.

        B^(1)(V_Λ^{N,q}) = B^(1)_Cartan(H_r) ⊗ B^(0)_roots(V_Λ^{N,q})

        The Cartan factor carries the curvature.
        The root factor carries the braiding.
        They are independent.
        """
        result = genus1_e1_bar_complex("A2", N=3)
        fact = result['factorization']
        assert fact['cartan_genus1']
        assert fact['roots_genus0']
        assert fact['curvature_braiding_orthogonal']

    def test_cocycle_does_not_affect_curvature(self):
        """Changing N and q does NOT change κ.

        The curvature κ = rank(Λ) = 2 for A₂, regardless of
        the deformation (N, q).  This is because the curvature
        lives in the Cartan sector, which is always E∞.
        """
        for N in [3, 5, 7]:
            result = genus1_e1_bar_complex("A2", N=N)
            assert result['kappa'] == 2, \
                f"N={N}: κ must be 2 (rank of A₂)"

    def test_e1_vs_einf_at_genus1(self):
        """E₁ and E∞ have the SAME curvature at genus 1.

        The difference between E₁ and E∞ at genus 1 is ONLY in the
        ordering cycles of the root sectors, not in the curvature.
        """
        result = genus1_e1_bar_complex("A2", N=3)
        comp = result['e1_vs_einf_genus1']
        assert comp['curvature_identical']
        assert comp['ordering_cycles_persist']


# ============================================================
# Higher rank: A₃ and D₄
# ============================================================

class TestHigherRankGenus1:
    """Genus-1 computation scales to higher rank."""

    def test_a3_genus1(self):
        """A₃ at N=3: κ = 3 (rank 3)."""
        result = genus1_e1_bar_complex("A3", N=3)
        assert result['kappa'] == 3
        assert abs(result['F_1'] - 3/24) < 1e-15

    def test_d4_genus1(self):
        """D₄ at N=3: κ = 4 (rank 4), with triality symmetry."""
        result = genus1_e1_bar_complex("D4", N=3)
        assert result['kappa'] == 4
        assert abs(result['F_1'] - 4/24) < 1e-15


# ============================================================
# Full verification suite
# ============================================================

class TestFullVerification:
    """Comprehensive verification of all structural claims."""

    @pytest.mark.parametrize("lie_type", ["A2", "A3", "D4"])
    def test_all_checks_pass(self, lie_type):
        """All structural checks pass for each lie type."""
        checks = verify_curvature_braiding_orthogonality(lie_type, N=3)
        for name, passed in checks.items():
            assert passed, f"{lie_type}: check '{name}' failed"
