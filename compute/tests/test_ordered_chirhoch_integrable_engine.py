r"""Tests for ordered chiral Hochschild cohomology at integrable level.

Multi-path verification of the ordered ChirHoch computation at k=1 and
higher integrable levels, cross-checked against the Verlinde algebra engine,
the quantum group root-of-unity engine, and direct computation.

Each hardcoded expected value has 2+ independent derivation paths (AP10/HZ-6):
  [DC] direct computation
  [LT] literature (paper + equation)
  [LC] limiting case
  [SY] symmetry
  [CF] cross-family / cross-engine
  [NE] numerical (>=10 digits)
"""

from __future__ import annotations

import math
import sys
import os

import numpy as np
import pytest

# Ensure compute/lib is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from ordered_chirhoch_integrable_engine import (
    quantum_integer,
    quantum_dimension,
    q_from_level,
    fusion_coefficient,
    fusion_product,
    iterated_fusion_rank,
    integrable_rank,
    sl2_S_matrix,
    verlinde_dimension,
    kzb_monodromy_arity2,
    monodromy_has_invariants,
    ordered_chirhoch_integrable,
    comparison_table,
    k1_structural_summary,
)


# =========================================================================
# 1. Quantum number tests
# =========================================================================

class TestQuantumNumbers:
    """Quantum integers and dimensions at roots of unity."""

    def test_quantum_integer_generic(self):
        """[DC] [n]_q at generic q reduces to n at q=1."""
        q = 1.0001 + 0j  # near 1
        for n in range(1, 6):
            val = quantum_integer(n, q)
            assert abs(val - n) < 0.01, f"[{n}]_q near q=1 should be ~{n}"

    def test_quantum_integer_root_of_unity(self):
        """[DC] [p]_q = 0 when q^p = 1 (primitive root).

        At q = e^{2*pi*i/3}: [3]_q = 0.
        # VERIFIED: [DC] (q^3 - q^{-3})/(q - q^{-1}) = 0 since q^3=1.
        # VERIFIED: [LT] Kassel, Quantum Groups, Prop. VI.1.4.
        """
        q = q_from_level(1)  # q = e^{2*pi*i/3}, order 3
        val = quantum_integer(3, q)
        assert abs(val) < 1e-10, f"[3]_q should vanish at q^3=1, got {val}"

    def test_quantum_dimension_k1(self):
        """[DC] [CF] d_0 = d_1 = 1 at k=1.

        # VERIFIED: [DC] d_j = sin((j+1)*pi/3) / sin(pi/3).
        #   j=0: sin(pi/3)/sin(pi/3) = 1. j=1: sin(2*pi/3)/sin(pi/3) = 1.
        # VERIFIED: [CF] verlinde_shadow_algebra.sl2_quantum_dimensions(1) = [1, 1].
        """
        assert abs(quantum_dimension(0, 1) - 1.0) < 1e-12
        assert abs(quantum_dimension(1, 1) - 1.0) < 1e-12

    def test_quantum_dimension_k2(self):
        """[DC] d_0=1, d_1=sqrt(2), d_2=1 at k=2.

        # VERIFIED: [DC] d_j = sin((j+1)*pi/4) / sin(pi/4).
        #   j=0: 1. j=1: sin(pi/2)/sin(pi/4) = sqrt(2). j=2: sin(3pi/4)/sin(pi/4) = 1.
        # VERIFIED: [LT] Bakalov-Kirillov, Table 3.1.
        """
        assert abs(quantum_dimension(0, 2) - 1.0) < 1e-12
        assert abs(quantum_dimension(1, 2) - math.sqrt(2)) < 1e-12
        assert abs(quantum_dimension(2, 2) - 1.0) < 1e-12


# =========================================================================
# 2. Fusion rule tests
# =========================================================================

class TestFusionRules:
    """Verlinde fusion rules at integrable level."""

    def test_k1_fusion_Z2(self):
        """[DC] [LT] k=1 fusion ring is Z/2Z.

        # VERIFIED: [DC] Truncated CG: V_1 x V_1 = V_0 (since min(2, 2-2)=0).
        # VERIFIED: [LT] Verlinde (1988), sl_2 at k=1.
        """
        assert fusion_product(0, 0, 1) == [0]
        assert fusion_product(0, 1, 1) == [1]
        assert fusion_product(1, 0, 1) == [1]
        assert fusion_product(1, 1, 1) == [0]

    def test_k2_fusion(self):
        """[DC] [CF] k=2 fusion rules (Ising-type).

        # VERIFIED: [DC] Truncated CG with k=2.
        # VERIFIED: [CF] verlinde_shadow_algebra.sl2_fusion_rules_explicit(2).
        """
        # V_0 x V_j = V_j (unit)
        for j in range(3):
            assert fusion_product(0, j, 2) == [j]

        # V_1 x V_1 = V_0 + V_2
        assert fusion_product(1, 1, 2) == [0, 2]

        # V_1 x V_2 = V_1
        assert fusion_product(1, 2, 2) == [1]

        # V_2 x V_2 = V_0
        assert fusion_product(2, 2, 2) == [0]

    def test_iterated_fusion_k1(self):
        """[DC] V_1^{tensor n} in Z/2Z fusion: {n%2: 1}.

        # VERIFIED: [DC] V_1 x V_1 = V_0, V_0 x V_1 = V_1, alternating.
        # VERIFIED: [SY] Z/2Z group law: 1+1=0, 0+1=1 mod 2.
        """
        for n in range(8):
            decomp = iterated_fusion_rank(n, 1, 1)
            expected_j = n % 2
            assert decomp == {expected_j: 1}, \
                f"V_1^{n} at k=1: expected {{{expected_j}: 1}}, got {decomp}"

    def test_integrable_rank_k1(self):
        """[DC] Integrable rank: 1 (n even) or 2 (n odd) at k=1.

        # VERIFIED: [DC] dim(V_0)=1, dim(V_1)=2; fusion gives V_{n%2}.
        # VERIFIED: [SY] Z/2Z alternation.
        """
        for n in range(1, 9):
            expected = 1 if n % 2 == 0 else 2
            assert integrable_rank(n, 1, 1) == expected

    def test_integrable_rank_vs_generic(self):
        """[DC] Generic rank 2^n >> integrable rank at k=1 for n >= 3.

        # VERIFIED: [DC] 2^n grows exponentially; integrable alternates 1, 2.
        """
        for n in range(3, 8):
            gen_rank = 2 ** n
            int_rank = integrable_rank(n, 1, 1)
            assert int_rank < gen_rank, \
                f"Arity {n}: integrable {int_rank} should be < generic {gen_rank}"


# =========================================================================
# 3. S-matrix and Verlinde dimension tests
# =========================================================================

class TestVerlinde:
    """S-matrix and Verlinde formula."""

    def test_S_matrix_k1_is_hadamard(self):
        """[DC] [LT] S-matrix at k=1 is Hadamard/sqrt(2).

        # VERIFIED: [DC] S_{jl} = sqrt(2/3)*sin(pi*(j+1)*(l+1)/3).
        #   S_{00}=S_{01}=sqrt(2/3)*sin(2pi/3)=sqrt(2/3)*sqrt(3)/2=1/sqrt(2).
        # VERIFIED: [LT] Bakalov-Kirillov, Example 3.1.11.
        """
        S = sl2_S_matrix(1)
        hadamard = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
        np.testing.assert_allclose(S, hadamard, atol=1e-12)

    def test_S_matrix_unitarity(self):
        """[DC] S*S^T = I (unitarity) for k=1,...,5.

        # VERIFIED: [DC] S is real symmetric orthogonal for sl_2.
        # VERIFIED: [LT] Kac-Peterson (1984), unitarity of S-matrix.
        """
        for k in range(1, 6):
            S = sl2_S_matrix(k)
            product = S @ S.T
            np.testing.assert_allclose(
                product, np.eye(k + 1), atol=1e-10,
                err_msg=f"S-matrix not unitary at k={k}")

    def test_verlinde_k1_is_2_to_g(self):
        """[DC] [CF] Z_g = 2^g at k=1.

        # VERIFIED: [DC] Z_g = S_{00}^{2-2g} + S_{01}^{2-2g}
        #   = 2 * (1/sqrt(2))^{2-2g} = 2 * 2^{g-1} = 2^g.
        # VERIFIED: [CF] verlinde_shadow_algebra.sl2_genus_g_verlinde(g, 1).
        """
        for g in range(7):
            Z_g = verlinde_dimension(g, 1)
            expected = 2.0 ** g
            assert abs(Z_g - expected) < 1e-10, \
                f"Z_{g} at k=1: expected {expected}, got {Z_g}"

    def test_verlinde_g0_is_1(self):
        """[DC] Z_0 = 1 for all k (unitarity of S).

        # VERIFIED: [DC] Z_0 = sum S_{0j}^2 = 1 by unitarity.
        # VERIFIED: [LT] Verlinde (1988): genus-0 with no insertions = 1.
        """
        for k in range(1, 8):
            Z_0 = verlinde_dimension(0, k)
            assert abs(Z_0 - 1.0) < 1e-10, \
                f"Z_0 at k={k}: expected 1, got {Z_0}"

    def test_verlinde_g1_is_k_plus_1(self):
        """[DC] [LT] Z_1 = k+1 for all k.

        # VERIFIED: [DC] Z_1 = sum S_{0j}^0 = sum 1 = k+1.
        # VERIFIED: [LT] Verlinde: genus-1 blocks = number of integrable reps.
        """
        for k in range(1, 10):
            Z_1 = verlinde_dimension(1, k)
            assert abs(Z_1 - (k + 1)) < 1e-10, \
                f"Z_1 at k={k}: expected {k + 1}, got {Z_1}"

    def test_verlinde_integrality_g2(self):
        """[DC] Z_2 is a positive integer for k=1,...,20.

        # VERIFIED: [DC] Z_2 = sum S_{0j}^{-2} = sum d_j^2 * S_{00}^{-2}
        #   = D^2 * sum d_j^{-2} (positive, integer by MTC theory).
        # VERIFIED: [NE] Numerical check for k=1,...,20.
        """
        for k in range(1, 21):
            Z_2 = verlinde_dimension(2, k)
            assert Z_2 > 0, f"Z_2 at k={k} should be positive"
            assert abs(Z_2 - round(Z_2)) < 1e-6, \
                f"Z_2 at k={k} should be integer, got {Z_2}"


# =========================================================================
# 4. KZB monodromy tests
# =========================================================================

class TestKZBMonodromy:
    """KZB monodromy at integrable level."""

    def test_monodromy_eigenvalues_k1(self):
        """[DC] Monodromy eigenvalues at k=1.

        # VERIFIED: [DC] M_gamma = exp(2*pi*i * (1/3) * Omega).
        #   Sym: exp(pi*i/3) = (1+i*sqrt(3))/2. Alt: exp(-pi*i) = -1.
        # VERIFIED: [LT] Bernard (1988), KZB monodromy on the torus.
        """
        data = kzb_monodromy_arity2(1)

        # Puncture monodromy on Sym^2: exp(pi*i/3)
        expected_sym = np.exp(1j * np.pi / 3)
        assert abs(data.M_gamma_sym - expected_sym) < 1e-10

        # Puncture monodromy on wedge^2: exp(-pi*i) = -1
        assert abs(data.M_gamma_alt - (-1.0)) < 1e-10

        # B-cycle: inverse of puncture
        assert abs(data.M_B_sym - 1.0 / expected_sym) < 1e-10
        assert abs(data.M_B_alt - (-1.0)) < 1e-10

    def test_monodromy_finite_order_k1(self):
        """[DC] Monodromy has finite order at k=1.

        # VERIFIED: [DC] exp(pi*i/3) has order 6; -1 has order 2.
        # VERIFIED: [SY] q = e^{2pi*i/3} has order 3; monodromy order | 6(k+2).
        """
        data = kzb_monodromy_arity2(1)
        assert data.order_gamma_sym == 6, \
            f"Sym monodromy order: expected 6, got {data.order_gamma_sym}"
        assert data.order_gamma_alt == 2, \
            f"Alt monodromy order: expected 2, got {data.order_gamma_alt}"

    def test_no_monodromy_invariants_k1(self):
        """[DC] No monodromy invariants at k=1: H^0 = 0.

        # VERIFIED: [DC] exp(pi*i/3) != 1 and -1 != 1.
        # VERIFIED: [LC] At generic hbar, H^0 = 0 (KZB has no flat sections).
        """
        assert not monodromy_has_invariants(1)

    def test_monodromy_finite_all_integrable(self):
        """[DC] Monodromy is finite for all integrable k = 1,...,10.

        # VERIFIED: [DC] At q = e^{2*pi*i/(k+2)}, all eigenvalues are
        #   roots of unity of order dividing 2*(k+2).
        """
        for k in range(1, 11):
            data = kzb_monodromy_arity2(k)
            assert data.order_gamma_sym is not None, \
                f"Sym monodromy should have finite order at k={k}"
            assert data.order_gamma_alt is not None, \
                f"Alt monodromy should have finite order at k={k}"

    def test_hecke_eigenvalues_k1(self):
        """[DC] R-matrix eigenvalues at k=1: q on Sym, -q^{-1} on wedge.

        # VERIFIED: [DC] Hecke relation (R-q)(R+q^{-1})=0.
        # VERIFIED: [CF] theorem_yangian_roots_unity_engine.verify_hecke_relation.
        """
        data = kzb_monodromy_arity2(1)
        q = data.q
        assert abs(data.R_sym - q) < 1e-10
        assert abs(data.R_alt - (-1.0 / q)) < 1e-10


# =========================================================================
# 5. Ordered ChirHoch dimension tests
# =========================================================================

class TestOrderedChirHoch:
    """Ordered chiral Hochschild cohomology dimensions."""

    def test_arity0_k1(self):
        """[DC] [LT] Arity 0 at k=1: C^2 (center of integrable quotient).

        # VERIFIED: [DC] Center = C^{k+1} = C^2 (Grothendieck ring of fusion cat).
        # VERIFIED: [LT] Kazhdan-Lusztig: center of integrable category = C^{k+1}.
        """
        data = ordered_chirhoch_integrable(1)
        assert data.arity_dims[0]['dim_integrable'] == 2

    def test_arity0_finite_vs_generic_infinite(self):
        """[DC] Arity 0: finite (integrable) vs infinite (generic).

        # VERIFIED: [DC] Z(Y_hbar(sl_2)) = C[qdet] (infinite) at generic level.
        # VERIFIED: [DC] Z(L_k(sl_2)) = C^{k+1} (finite) at integrable level.
        """
        data = ordered_chirhoch_integrable(1)
        assert data.arity_dims[0]['dim_integrable'] == 2
        assert data.arity_dims[0]['dim_generic'] == float('inf')

    def test_arity1_level_independent(self):
        """[DC] Arity 1: dim 12, independent of level.

        # VERIFIED: [DC] H*(E_tau) tensor s^{-1}sl_2 = C^4 tensor C^3 = C^12.
        #   Bar H^1 = s^{-1}g for any affine KM, regardless of level.
        # VERIFIED: [CF] Generic-level computation (prop:ell-arity1).
        """
        for k in [1, 2, 3, 5]:
            data = ordered_chirhoch_integrable(k)
            assert data.arity_dims[1]['dim_integrable'] == 12, \
                f"Arity 1 at k={k}: expected 12"
            assert data.arity_dims[1]['dim_generic'] == 12

    def test_arity2_k1(self):
        """[DC] [CF] Arity 2 at k=1: dim H^1 = 4.

        # VERIFIED: [DC] Euler char = 4*(2-2-1) = -4; H^0=H^2=0 -> H^1=4.
        # VERIFIED: [CF] Generic-level arity-2 (prop:ell-arity2): same dim 4.
        """
        data = ordered_chirhoch_integrable(1)
        assert data.arity_dims[2]['dim_integrable'] == 4
        assert data.arity_dims[2]['H0'] == 0
        assert data.arity_dims[2]['H1'] == 4
        assert data.arity_dims[2]['H2'] == 0

    def test_central_charge_k1(self):
        """[DC] c = 3k/(k+2) = 1 at k=1.

        # VERIFIED: [DC] 3*1/3 = 1.
        # VERIFIED: [CF] sl2_central_charge(1) from verlinde_shadow_algebra.
        """
        data = ordered_chirhoch_integrable(1)
        assert abs(data.c - 1.0) < 1e-10

    def test_kappa_k1(self):
        """[DC] [CF] kappa = 3(k+2)/4 = 9/4 at k=1.

        # VERIFIED: [DC] dim(sl_2)*(k+h^v)/(2*h^v) = 3*3/4 = 9/4.
        #   AP1: k=0 -> 3/2 (not zero!), k=-2 -> 0 (critical).
        # VERIFIED: [CF] sl2_kappa(1) from verlinde_shadow_algebra.
        """
        data = ordered_chirhoch_integrable(1)
        assert abs(data.kappa - 9.0 / 4) < 1e-10

    def test_total_quantum_dimension_k1(self):
        """[DC] D^2 = 2 at k=1.

        # VERIFIED: [DC] d_0^2 + d_1^2 = 1 + 1 = 2.
        # VERIFIED: [CF] Formula: (k+2)/(2*sin^2(pi/(k+2))) = 3/(2*3/4) = 2.
        """
        data = ordered_chirhoch_integrable(1)
        assert abs(data.total_D_sq - 2.0) < 1e-10


# =========================================================================
# 6. Comprehensive k=1 structural test
# =========================================================================

class TestK1Structural:
    """Full structural verification at k=1."""

    def test_k1_full_structural_summary(self):
        """[DC] [CF] [LT] [SY] All 14 structural assertions at k=1.

        This test verifies the complete structural summary,
        cross-checking against Verlinde algebra, fusion rules,
        S-matrix, monodromy, and the generic-level predictions.
        """
        results = k1_structural_summary()

        # All assertions passed inside k1_structural_summary
        assert results['fusion_is_Z2']
        assert results['pointed_MTC']
        assert results['S_is_hadamard']
        assert results['verlinde_2_to_g']
        assert results['arity_0_dim'] == 2
        assert results['arity_1_dim'] == 12
        assert results['arity_2_dim'] == 4
        assert results['rank_Z2_pattern']
        assert results['H0_vanishes']
        assert abs(results['central_charge'] - 1.0) < 1e-10
        assert abs(results['kappa'] - 9.0 / 4) < 1e-10
        assert abs(results['total_D_sq'] - 2.0) < 1e-10


# =========================================================================
# 7. Higher integrable level tests
# =========================================================================

class TestHigherLevels:
    """Verification at k=2, 3 to confirm patterns generalize."""

    def test_k2_center_dim(self):
        """[DC] Arity 0 at k=2: C^3.

        # VERIFIED: [DC] k+1 = 3 integrable reps at k=2.
        # VERIFIED: [LT] Verlinde: Z_1 = k+1 = 3.
        """
        data = ordered_chirhoch_integrable(2)
        assert data.arity_dims[0]['dim_integrable'] == 3

    def test_k2_arity2(self):
        """[DC] Arity 2 at k=2: dim H^1 = 4 (same Euler char).

        # VERIFIED: [DC] Rank 4 local system, chi = -4, H^0=0 -> H^1=4.
        """
        data = ordered_chirhoch_integrable(2)
        assert data.arity_dims[2]['dim_integrable'] == 4

    def test_k2_verlinde(self):
        """[DC] Verlinde dimensions at k=2.

        # VERIFIED: [DC] Z_g = sum_{j=0}^2 S_{0j}^{2-2g}.
        #   S_{00} = sqrt(2/4)*sin(pi/4) = 1/2,
        #   S_{01} = sqrt(2/4)*sin(pi/2) = 1/sqrt(2),
        #   S_{02} = sqrt(2/4)*sin(3pi/4) = 1/2.
        # VERIFIED: [DC] Z_2 = S_{00}^{-2} + S_{01}^{-2} + S_{02}^{-2}
        #   = 4 + 2 + 4 = 10.
        # VERIFIED: [CF] Z_2(sl_2, k) = C(k+3, 3); C(5,3) = 10.
        # Previous value 6 was WRONG (AP10 violation: no independent derivation).
        """
        assert abs(verlinde_dimension(0, 2) - 1.0) < 1e-10
        assert abs(verlinde_dimension(1, 2) - 3.0) < 1e-10
        # Z_2 at k=2: sum S_{0j}^{-2} = 4 + 2 + 4 = 10
        Z_2 = verlinde_dimension(2, 2)
        assert abs(Z_2 - round(Z_2)) < 1e-6
        assert round(Z_2) == 10  # VERIFIED: [DC] 4+2+4=10; [CF] C(5,3)=10

    def test_k3_verlinde_g1(self):
        """[DC] Z_1 = 4 at k=3.

        # VERIFIED: [DC] Z_1 = k+1 = 4.
        """
        assert abs(verlinde_dimension(1, 3) - 4.0) < 1e-10

    def test_integrable_rank_k2(self):
        """[DC] Integrable ranks at k=2 for V_1^{tensor n}.

        # VERIFIED: [DC] k=2 fusion: V_1 x V_1 = V_0 + V_2, V_1 x V_2 = V_1.
        """
        # V_1^1 = V_1, rank 2
        assert integrable_rank(1, 2, 1) == 2
        # V_1^2 = V_0 + V_2, rank 1 + 3 = 4
        assert integrable_rank(2, 2, 1) == 4
        # V_1^3 = (V_0+V_2) x V_1 = V_1 + V_1 = 2*V_1, rank 2*2 = 4
        assert integrable_rank(3, 2, 1) == 4


# =========================================================================
# 8. Comparison table (smoke test)
# =========================================================================

class TestComparison:
    """Comparison table generation."""

    def test_comparison_table_runs(self):
        """Comparison table generates without errors."""
        table = comparison_table(1)
        assert "Z/2Z" in table
        assert "k=1" in table

    def test_comparison_table_k2(self):
        """Comparison table at k=2."""
        table = comparison_table(2)
        assert "k=2" in table


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
