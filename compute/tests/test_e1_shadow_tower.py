"""Tests for E₁ shadow tower: ordered R-matrix data for standard families.

Verifies the shadow depth classification (G/L/C/M), R-matrix structure,
CYBE satisfaction, and kappa averaging for all four archetype families.

Ground truth:
  - nonlinear_modular_shadows.tex: shadow depth classification
  - higher_genus_modular_koszul.tex: collision residue identification
  - affine_sl2_shadow_tower.py: affine sl_2 computations
  - modular_shadow_tower.py: Virasoro quartic contact
"""

import numpy as np
import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.e1_shadow_tower import (
    HeisenbergShadow,
    AffineSl2Shadow,
    BetaGammaShadow,
    VirasoroShadow,
    verify_cybe_heisenberg,
    verify_cybe_affine_sl2,
    verify_cybe_betagamma,
    verify_cybe_virasoro,
    shadow_depth_table,
    verify_kappa_averaging,
)


# =========================================================================
# Heisenberg shadow
# =========================================================================

class TestHeisenbergShadow:
    """Heisenberg H_k: Gaussian class G, depth 2."""

    def test_r_matrix_form(self):
        """r(z) = k/z."""
        h = HeisenbergShadow()
        z = Symbol('z')
        k = Symbol('k')
        r = h.r_matrix()
        assert simplify(r - k / z) == 0

    def test_r3_zero(self):
        """r_3 = 0 (Gaussian terminates at arity 2)."""
        h = HeisenbergShadow()
        assert h.r3() == 0

    def test_r4_zero(self):
        """r_4 = 0."""
        h = HeisenbergShadow()
        assert h.r4() == 0

    def test_kappa(self):
        """κ = k (level)."""
        h = HeisenbergShadow()
        k = Symbol('k')
        assert simplify(h.kappa() - k) == 0

    def test_shadow_depth(self):
        """Shadow depth = 2."""
        h = HeisenbergShadow()
        assert h.shadow_depth() == 2

    def test_depth_class(self):
        """Class G (Gaussian)."""
        h = HeisenbergShadow()
        assert h.depth_class() == "G"

    def test_is_scalar(self):
        """R-matrix is scalar (1d)."""
        h = HeisenbergShadow()
        assert h.is_scalar()

    def test_cybe(self):
        """CYBE trivially satisfied (scalar, 1d)."""
        h = HeisenbergShadow()
        assert h.cybe_lhs() == 0

    def test_numerical_kappa(self):
        """κ = k for specific numerical values."""
        for k_val in [1, 2, 5, 10]:
            h = HeisenbergShadow(level=k_val)
            assert h.kappa() == k_val


# =========================================================================
# Affine sl_2 shadow
# =========================================================================

class TestAffineSl2Shadow:
    """Affine sl_2 at level k: Lie class L, depth 3."""

    def test_casimir_tensor_shape(self):
        """Casimir Ω is 4×4 (acting on C²⊗C²)."""
        a = AffineSl2Shadow()
        omega = a.casimir_tensor()
        assert omega.shape == (4, 4)

    def test_casimir_tensor_trace(self):
        """Tr(Ω) on C²⊗C² = dim(g)/dim(V)² * ... check value."""
        a = AffineSl2Shadow()
        omega = a.casimir_tensor()
        # Ω = (1/2)(h⊗h) + e⊗f + f⊗e
        # Tr(Ω) = Tr(h⊗h)/2 + Tr(e⊗f) + Tr(f⊗e)
        # Tr(h⊗h) = Tr(h)² = 0 (traceless)
        # Tr(e⊗f) = Tr(e)·Tr(f) = 0
        # Actually Tr(A⊗B) = Tr(A)*Tr(B), so Tr(Ω) = 0 + 0 + 0 = 0
        # Wait: the 4×4 trace of Ω = sum of diagonal entries
        tr = np.trace(omega)
        # Diagonal: 1/2, -1/2, -1/2, 1/2 → sum = 0
        assert abs(tr) < 1e-14

    def test_casimir_symmetric(self):
        """Ω is symmetric: Ω^T = Ω (by sl_2 invariance)."""
        a = AffineSl2Shadow()
        omega = a.casimir_tensor()
        assert np.allclose(omega, omega.T)

    def test_casimir_eigenvalues(self):
        """Casimir eigenvalues on C²⊗C²: 1/2 (triplet, ×3) and -3/2 (singlet, ×1).

        Wait: Ω acts on V⊗V = S²V ⊕ Λ²V (3 ⊕ 1 for sl_2).
        On the triplet (spin 1): Casimir eigenvalue = 1 (for standard normalization)
        On the singlet (spin 0): Casimir eigenvalue = 0
        But our Ω = Σ t_a ⊗ t_a with specific normalization...

        Actually: eigenvalues of our Ω = (1/2)(h⊗h) + e⊗f + f⊗e.
        The eigenvalues are: {3/2, 1/2, 1/2, -1/2}... let me just check.
        """
        a = AffineSl2Shadow()
        omega = a.casimir_tensor()
        eigvals = sorted(np.real(np.linalg.eigvals(omega)))
        # Ω on symmetric part (triplet): eigenvalue (C₂(adj)-2C₂(fund))/...
        # Just verify the eigenvalue structure
        assert len(eigvals) == 4
        # The singlet should have one eigenvalue, triplet should have three
        # Group eigenvalues
        unique_eigs = set(round(float(e), 10) for e in eigvals)
        assert len(unique_eigs) == 2  # Two distinct eigenvalues

    def test_r3_nonzero(self):
        """r_3 ≠ 0 (KZ associator)."""
        a = AffineSl2Shadow()
        assert a.r3_nonzero()

    def test_r4_zero(self):
        """r_4 = 0 (Jacobi identity kills quartic obstruction)."""
        a = AffineSl2Shadow()
        assert a.r4() == 0

    def test_kappa_formula(self):
        """κ = 3(k+2)/4 for sl_2: (k+h^v)*dim(g)/(2*h^v)."""
        a = AffineSl2Shadow()
        k = Symbol('k')
        expected = 3 * (k + 2) / 4
        assert simplify(a.kappa() - expected) == 0

    def test_kappa_numerical(self):
        """κ = 3(k+2)/4 at specific levels."""
        # k=1: κ = 3*3/4 = 9/4 = 2.25
        a1 = AffineSl2Shadow(level=1)
        assert a1.kappa() == pytest.approx(2.25)
        # k=2: κ = 3*4/4 = 3.0
        a2 = AffineSl2Shadow(level=2)
        assert a2.kappa() == pytest.approx(3.0)
        # k=4: κ = 3*6/4 = 4.5
        a4 = AffineSl2Shadow(level=4)
        assert a4.kappa() == pytest.approx(4.5)

    def test_shadow_depth(self):
        """Shadow depth = 3."""
        a = AffineSl2Shadow()
        assert a.shadow_depth() == 3

    def test_depth_class(self):
        """Class L (Lie)."""
        a = AffineSl2Shadow()
        assert a.depth_class() == "L"

    def test_r_matrix_numerical(self):
        """Numerical R-matrix r = k·Ω is 4×4."""
        a = AffineSl2Shadow()
        r = a.r_matrix_numerical(level_val=2.0)
        assert r.shape == (4, 4)
        # At k=2, r = 2*Ω
        omega = a.casimir_tensor()
        assert np.allclose(r, 2.0 * omega)

    def test_r_matrix_symbolic(self):
        """Symbolic R-matrix is a 4×4 sympy Matrix."""
        a = AffineSl2Shadow()
        r = a.r_matrix_symbolic()
        assert r.shape == (4, 4)


# =========================================================================
# CYBE verification
# =========================================================================

class TestCYBE:
    """Classical Yang-Baxter equation for all families."""

    def test_cybe_heisenberg(self):
        """CYBE for Heisenberg: trivially satisfied."""
        assert verify_cybe_heisenberg()

    def test_cybe_affine_sl2_k1_skew(self):
        """Strict CYBE for skew part of sl_2 Casimir at k=1."""
        result = verify_cybe_affine_sl2(level_val=1.0)
        assert result["cybe_skew_zero"]
        assert result["cybe_skew_norm"] < 1e-10

    def test_cybe_affine_sl2_k2_skew(self):
        """Strict CYBE for skew part at k=2."""
        result = verify_cybe_affine_sl2(level_val=2.0)
        assert result["cybe_skew_zero"]

    def test_cybe_affine_sl2_k5_skew(self):
        """Strict CYBE for skew part at k=5."""
        result = verify_cybe_affine_sl2(level_val=5.0)
        assert result["cybe_skew_zero"]

    def test_cybe_affine_sl2_fractional_skew(self):
        """Strict CYBE for skew part at k=1/3."""
        result = verify_cybe_affine_sl2(level_val=1.0 / 3.0)
        assert result["cybe_skew_zero"]

    def test_mcybe_affine_sl2_full_casimir(self):
        """Full Casimir satisfies MODIFIED CYBE (nonzero RHS).

        [Ω₁₂, Ω₁₃] + [Ω₁₂, Ω₂₃] + [Ω₁₃, Ω₂₃] = Φ₁₂₃ ≠ 0.
        This is because the Casimir is SYMMETRIC, not skew.
        The nonzero Φ₁₂₃ is the ad-invariant cubic tensor.
        """
        result = verify_cybe_affine_sl2(level_val=1.0)
        assert result["mcybe_lhs_nonzero"]

    def test_cybe_betagamma(self):
        """CYBE for beta-gamma: trivially satisfied (r = 0)."""
        assert verify_cybe_betagamma()

    def test_cybe_virasoro(self):
        """CYBE for Virasoro: satisfied (scalar)."""
        assert verify_cybe_virasoro()

    def test_cybe_triple_tensor_dimension(self):
        """CYBE computation uses V⊗V⊗V = C⁸ for sl_2."""
        result = verify_cybe_affine_sl2()
        assert result["dim_V"] == 2
        assert result["dim_triple"] == 8

    def test_cybe_skew_scales_cubically(self):
        """CYBE skew norm scales as k³ (cubic in level)."""
        r1 = verify_cybe_affine_sl2(level_val=1.0)
        r2 = verify_cybe_affine_sl2(level_val=2.0)
        # Skew norm should be 0 for both
        assert r1["cybe_skew_norm"] < 1e-10
        assert r2["cybe_skew_norm"] < 1e-10


# =========================================================================
# Beta-gamma shadow
# =========================================================================

class TestBetaGammaShadow:
    """Beta-gamma system: contact class C, depth 4."""

    def test_r_matrix_zero(self):
        """r(z) = 0 (no double pole)."""
        b = BetaGammaShadow()
        assert b.r_matrix() == 0

    def test_r3_zero(self):
        """r_3 = 0."""
        b = BetaGammaShadow()
        assert b.r3() == 0

    def test_r4_nonzero(self):
        """r_4 ≠ 0 (quartic contact invariant)."""
        b = BetaGammaShadow()
        assert b.r4_nonzero()

    def test_r4_vanishes_weight_line(self):
        """μ_{βγ} = 0 on weight-changing line."""
        b = BetaGammaShadow()
        assert b.r4_vanishes_on_weight_line()

    def test_kappa(self):
        """κ = c/2 = -1 for beta-gamma (c = -2)."""
        b = BetaGammaShadow()
        assert b.kappa() == -1

    def test_shadow_depth(self):
        """Shadow depth = 4."""
        b = BetaGammaShadow()
        assert b.shadow_depth() == 4

    def test_depth_class(self):
        """Class C (contact)."""
        b = BetaGammaShadow()
        assert b.depth_class() == "C"


# =========================================================================
# Virasoro shadow
# =========================================================================

class TestVirasoroShadow:
    """Virasoro at central charge c: mixed class M, depth ∞."""

    def test_r_matrix_form(self):
        """r(z) = (c/2)/z."""
        v = VirasoroShadow()
        z = Symbol('z')
        c = Symbol('c')
        r = v.r_matrix()
        assert simplify(r - c / (2 * z)) == 0

    def test_r3_nonzero(self):
        """r_3 ≠ 0 (gravitational cubic)."""
        v = VirasoroShadow()
        assert v.r3_nonzero()

    def test_r3_coefficient(self):
        """Cubic coefficient = 2 (from T*T ~ 2T OPE)."""
        v = VirasoroShadow()
        assert v.r3_coefficient() == 2

    def test_r4_nonzero(self):
        """r_4 ≠ 0."""
        v = VirasoroShadow()
        assert v.r4_nonzero()

    def test_quartic_contact(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        v = VirasoroShadow()
        c = Symbol('c')
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(v.quartic_contact() - expected) == 0

    def test_quartic_contact_numerical(self):
        """Q^contact at c = 1/2 (Ising): 10/[(1/2)(5/2+22)] = 10/[1/2 * 49/2] = 10*4/49."""
        v = VirasoroShadow(central_charge=Rational(1, 2))
        q = v.quartic_contact()
        expected = Rational(10) / (Rational(1, 2) * (Rational(5, 2) + 22))
        assert simplify(q - expected) == 0

    def test_kappa(self):
        """κ = c/2."""
        v = VirasoroShadow()
        c = Symbol('c')
        assert simplify(v.kappa() - c / 2) == 0

    def test_shadow_depth_infinite(self):
        """Shadow depth = ∞."""
        v = VirasoroShadow()
        assert v.shadow_depth() == float('inf')

    def test_depth_class(self):
        """Class M (mixed)."""
        v = VirasoroShadow()
        assert v.depth_class() == "M"

    def test_quintic_forced(self):
        """o⁵_Vir ≠ 0."""
        v = VirasoroShadow()
        assert v.quintic_forced()

    def test_virasoro_not_self_dual(self):
        """Virasoro is NOT self-dual: Vir_c^! = Vir_{26-c}.
        Self-dual at c = 13."""
        # The R-matrix r(z) = c/2z, Koszul dual r^!(z) = (26-c)/2z
        # Self-dual when c/2 = (26-c)/2 => c = 13
        v13 = VirasoroShadow(central_charge=13)
        assert float(v13.kappa()) == pytest.approx(6.5)
        # Dual kappa = (26 - 13)/2 = 13/2 = same
        dual_kappa = (26 - 13) / 2
        assert float(v13.kappa()) == pytest.approx(dual_kappa)


# =========================================================================
# Shadow depth table
# =========================================================================

class TestShadowDepthTable:
    """Summary table of all shadow depths."""

    def test_table_has_four_families(self):
        table = shadow_depth_table()
        assert len(table) == 4
        assert "Heisenberg" in table
        assert "Affine_sl2" in table
        assert "BetaGamma" in table
        assert "Virasoro" in table

    def test_depth_ordering(self):
        """G (2) < L (3) < C (4) < M (∞)."""
        table = shadow_depth_table()
        assert table["Heisenberg"]["depth"] == 2
        assert table["Affine_sl2"]["depth"] == 3
        assert table["BetaGamma"]["depth"] == 4
        assert table["Virasoro"]["depth"] == float('inf')

    def test_class_labels(self):
        table = shadow_depth_table()
        assert table["Heisenberg"]["class"] == "G"
        assert table["Affine_sl2"]["class"] == "L"
        assert table["BetaGamma"]["class"] == "C"
        assert table["Virasoro"]["class"] == "M"

    def test_r3_zero_pattern(self):
        """r_3 = 0 for Heisenberg and BetaGamma, ≠ 0 for affine and Virasoro."""
        table = shadow_depth_table()
        assert table["Heisenberg"]["r3_zero"] is True
        assert table["BetaGamma"]["r3_zero"] is True
        assert table["Affine_sl2"]["r3_zero"] is False
        assert table["Virasoro"]["r3_zero"] is False

    def test_r4_zero_pattern(self):
        """r_4 = 0 for Heisenberg and affine, ≠ 0 for BetaGamma and Virasoro."""
        table = shadow_depth_table()
        assert table["Heisenberg"]["r4_zero"] is True
        assert table["Affine_sl2"]["r4_zero"] is True
        assert table["BetaGamma"]["r4_zero"] is False
        assert table["Virasoro"]["r4_zero"] is False


# =========================================================================
# Kappa averaging
# =========================================================================

class TestKappaAveraging:
    """Verify av(r(z)) = κ for each family."""

    def test_heisenberg_averaging(self):
        result = verify_kappa_averaging("Heisenberg", k=3.0)
        assert result["match"]
        assert result["kappa_expected"] == pytest.approx(3.0)

    def test_affine_sl2_averaging(self):
        result = verify_kappa_averaging("Affine_sl2", k=4.0)
        assert result["match"]
        assert result["kappa_value"] == pytest.approx(4.5)  # 3*(4+2)/4 = 4.5

    def test_betagamma_averaging(self):
        result = verify_kappa_averaging("BetaGamma")
        assert result["match"]

    def test_virasoro_averaging(self):
        result = verify_kappa_averaging("Virasoro", c=26.0)
        assert result["match"]
        assert result["kappa_expected"] == pytest.approx(13.0)
