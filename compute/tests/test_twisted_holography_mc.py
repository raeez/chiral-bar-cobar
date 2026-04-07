r"""Tests for twisted_holography_mc: Costello-Gaiotto dictionary from Theta_A.

VERIFICATION STRUCTURE:

Three independent paths to the holographic dictionary:
  Path A: Direct MC projection (Theta_A^{(0,2)} -> r(z))
  Path B: Costello-Gaiotto boundary OPE (bar differential -> collision residue)
  Path C: Yangian from RTT (r(z) -> CYBE -> Y(g))

Each test class verifies one aspect across all standard families.
The master verification sweep checks everything simultaneously.

Test count: 35+ tests covering:
  1. Collision residue extraction (AP19 compliant)     [7 tests]
  2. CYBE from (0,3) MC equation                       [5 tests]
  3. Yangian structure from arity-3                     [4 tests]
  4. Quantum R-matrix and QYBE                          [5 tests]
  5. Shadow connection and KZ                           [4 tests]
  6. Koszul duality (AP24 compliant)                    [5 tests]
  7. Genus tower from Theta_A                           [3 tests]
  8. sl_2 explicit verification                         [4 tests]
  9. Master sweep                                       [2 tests]
"""

from __future__ import annotations

from fractions import Fraction

import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from twisted_holography_mc import (
    # Constructors
    make_heisenberg,
    make_affine_sl2,
    make_affine_slN,
    make_virasoro,
    make_betagamma,
    # Collision residue
    extract_collision_residue,
    collision_residue_leading_pole,
    collision_residue_matches_ope,
    # CYBE
    verify_cybe_from_mc,
    cybe_sl2_fundamental_numerical,
    cybe_slN_fundamental_numerical,
    # Yangian
    extract_yangian_data,
    yangian_coproduct_from_arity3,
    # Quantum R-matrix
    quantum_r_matrix,
    yang_r_matrix_numerical,
    verify_qybe_yang_numerical,
    # Shadow connection
    shadow_connection_genus0,
    kz_connection_matches_shadow,
    # Koszul duality
    koszul_dual_kappa,
    kappa_sum,
    # Genus tower
    genus_tower_from_theta,
    genus_expansion_three_paths,
    # sl_2 explicit
    sl2_explicit_verification,
    sl2_kappa_explicit,
    sl2_collision_residue_explicit,
    # Full dictionary
    extract_holographic_dictionary,
    # Master
    master_holographic_verification,
    # Internals
    _lambda_fp,
)


# =========================================================================
# 1. Collision residue extraction (AP19 compliant)
# =========================================================================

class TestCollisionResidue:
    """Test r(z) = Res^{coll}_{0,2}(Theta_A) with AP19 pole absorption."""

    def test_heisenberg_collision_residue(self):
        """Heisenberg: OPE k/z^2 -> collision residue k/z (AP19)."""
        A = make_heisenberg(Fraction(3))
        r = extract_collision_residue(A)
        # Single pole at z^{-1} with coefficient kappa = k = 3
        assert r.scalar_poles == {1: Fraction(3)}
        assert collision_residue_leading_pole(r) == 1

    def test_affine_sl2_collision_residue(self):
        """sl_2: OPE k/z^2 + f/z -> collision residue Omega/z (AP19).

        The double pole becomes a single pole (Casimir/z).
        The simple pole drops to regular (AP19).
        """
        A = make_affine_sl2(Fraction(1))
        r = extract_collision_residue(A)
        assert collision_residue_leading_pole(r) == 1
        assert r.is_matrix_valued is True
        assert r.casimir_order == 3  # dim(sl_2)

    def test_virasoro_collision_residue(self):
        """Virasoro: OPE (c/2)/z^4 + 2T/z^2 + T'/z
        -> collision residue (c/2)/z^3 + 2T/z (AP19).

        AP19: z^{-4} -> z^{-3}, z^{-2} -> z^{-1}, z^{-1} -> z^0 (drops out).
        The collision residue has ONLY odd-order poles (AP19 signature).
        """
        c = Fraction(25)
        A = make_virasoro(c)
        r = extract_collision_residue(A)
        # Leading pole: (c/2)/z^3
        assert 3 in r.scalar_poles
        assert r.scalar_poles[3] == c / 2
        assert collision_residue_leading_pole(r) == 3

    def test_virasoro_c26_collision_residue(self):
        """Virasoro at c=26: kappa = 13, leading collision pole = 13/z^3."""
        A = make_virasoro(Fraction(26))
        r = extract_collision_residue(A)
        assert r.scalar_poles[3] == Fraction(13)

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c=13: self-dual point, kappa = 13/2."""
        A = make_virasoro(Fraction(13))
        r = extract_collision_residue(A)
        assert r.scalar_poles[3] == Fraction(13, 2)

    def test_betagamma_collision_residue(self):
        """betagamma: OPE 1/z -> collision residue is regular (drops out).

        AP19: the simple pole in the beta-gamma OPE maps to z^0.
        The scalar projection of the collision residue is trivial.
        """
        A = make_betagamma()
        r = extract_collision_residue(A)
        # No scalar poles after AP19 absorption
        assert r.scalar_poles == {}
        assert collision_residue_leading_pole(r) == 0

    def test_collision_residue_pole_order_universal(self):
        """Universal: collision residue pole = OPE pole - 1 (AP19)."""
        # Heisenberg: OPE max pole 2 -> coll pole 1
        A_h = make_heisenberg()
        assert collision_residue_leading_pole(extract_collision_residue(A_h)) == 1

        # sl_2: OPE max pole 2 -> coll pole 1
        A_sl = make_affine_sl2(Fraction(1))
        assert collision_residue_leading_pole(extract_collision_residue(A_sl)) == 1

        # Virasoro: OPE max pole 4 -> coll pole 3
        A_v = make_virasoro(Fraction(25))
        assert collision_residue_leading_pole(extract_collision_residue(A_v)) == 3


# =========================================================================
# 2. CYBE from (0,3) MC equation
# =========================================================================

class TestCYBE:
    """Test CYBE satisfaction from the (0,3) MC projection."""

    def test_cybe_heisenberg(self):
        """Heisenberg: CYBE trivially satisfied (abelian)."""
        A = make_heisenberg()
        assert verify_cybe_from_mc(A) is True

    def test_cybe_sl2_algebraic(self):
        """sl_2: CYBE from ad-invariance of Casimir."""
        A = make_affine_sl2(Fraction(1))
        assert verify_cybe_from_mc(A) is True

    def test_cybe_sl2_numerical(self):
        """sl_2: CYBE for Yang r-matrix P/z in fundamental C^2, numerical."""
        assert cybe_sl2_fundamental_numerical() is True

    def test_cybe_sl3_numerical(self):
        """sl_3: CYBE for Yang r-matrix P/z in fundamental C^3, numerical."""
        assert cybe_slN_fundamental_numerical(3) is True

    def test_cybe_sl4_numerical(self):
        """sl_4: CYBE for Yang r-matrix P/z in fundamental C^4, numerical."""
        assert cybe_slN_fundamental_numerical(4) is True


# =========================================================================
# 3. Yangian structure from arity-3
# =========================================================================

class TestYangian:
    """Test Yangian extraction from (0,3) MC shadow."""

    def test_yangian_sl2(self):
        """sl_2: Yangian Y(sl_2) from arity-3 projection."""
        A = make_affine_sl2(Fraction(1))
        Y = extract_yangian_data(A)
        assert Y is not None
        assert Y.lie_algebra == "sl_2"
        assert Y.rank == 1
        assert Y.dim == 3
        assert Y.r_matrix_pole == 1
        assert Y.cybe_verified is True
        assert Y.rtt_consistent is True

    def test_yangian_heisenberg_abelian(self):
        """Heisenberg: trivial (abelian) quantum group."""
        A = make_heisenberg()
        Y = extract_yangian_data(A)
        assert Y is not None
        assert Y.lie_algebra == "u(1)"

    def test_yangian_virasoro_no_rtt(self):
        """Virasoro: no finite-dim RTT presentation (class M)."""
        A = make_virasoro(Fraction(25))
        Y = extract_yangian_data(A)
        assert Y is not None
        assert Y.rtt_consistent is False  # no finite-dim RTT

    def test_yangian_coproduct_sl2(self):
        """sl_2: Yangian coproduct from arity-3 shadow."""
        A = make_affine_sl2(Fraction(1))
        cop = yangian_coproduct_from_arity3(A)
        assert "Delta(J^a_0)" in cop
        assert "primitive" in cop["Delta(J^a_0)"]
        assert "Delta(J^a_1)" in cop
        assert "f^{abc}" in cop["Delta(J^a_1)"]  # structure constants appear


# =========================================================================
# 4. Quantum R-matrix and QYBE
# =========================================================================

class TestQuantumRMatrix:
    """Test R(z) = 1 + hbar*r(z) + O(hbar^2) and quantum YBE."""

    def test_quantum_r_sl2_genus1(self):
        """sl_2: genus-1 correction F_1 = kappa/24."""
        A = make_affine_sl2(Fraction(1))
        R = quantum_r_matrix(A)
        # kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4
        expected_kappa = Fraction(9, 4)
        assert R.genus1_correction == expected_kappa / 24

    def test_yang_r_matrix_sl2_shape(self):
        """Yang R-matrix for sl_2: R(z) = z*I - P, a 4x4 matrix.

        At large z: R(z)/z -> I (the classical r-matrix P/z emerges).
        """
        import numpy as np
        R = yang_r_matrix_numerical(2, 1.0)
        assert R.shape == (4, 4)
        # At z=infinity: R(z)/z -> I
        z_large = 1e10
        R_inf = yang_r_matrix_numerical(2, z_large) / z_large
        assert np.allclose(R_inf, np.eye(4), atol=1e-6)

    def test_qybe_yang_sl2(self):
        """Yang R-matrix for sl_2 satisfies QYBE numerically."""
        assert verify_qybe_yang_numerical(2) is True

    def test_qybe_yang_sl3(self):
        """Yang R-matrix for sl_3 satisfies QYBE numerically."""
        assert verify_qybe_yang_numerical(3) is True

    def test_quantum_r_from_mc(self):
        """R(z) is derived from Theta_A: the MC equation guarantees QYBE."""
        A = make_affine_sl2(Fraction(4))
        R = quantum_r_matrix(A)
        assert R.satisfies_qybe is True
        assert R.classical_r.satisfies_cybe is True


# =========================================================================
# 5. Shadow connection and KZ
# =========================================================================

class TestShadowConnection:
    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""

    def test_shadow_connection_flat(self):
        """Flatness from MC equation (thm:thqg-flatness)."""
        for A in [make_heisenberg(), make_affine_sl2(Fraction(1)),
                  make_virasoro(Fraction(25))]:
            conn = shadow_connection_genus0(A, 3)
            assert conn["is_flat"] is True

    def test_kz_match_sl2(self):
        """sl_2: shadow connection = KZ connection at genus 0."""
        A = make_affine_sl2(Fraction(1))
        assert kz_connection_matches_shadow(A) is True

    def test_kz_match_sl3(self):
        """sl_3: shadow connection = KZ connection at genus 0."""
        A = make_affine_slN(3, Fraction(1))
        assert kz_connection_matches_shadow(A) is True

    def test_heisenberg_not_kz(self):
        """Heisenberg is not KZ type (abelian, no Lie algebra)."""
        A = make_heisenberg()
        assert kz_connection_matches_shadow(A) is False


# =========================================================================
# 6. Koszul duality (AP24 compliant)
# =========================================================================

class TestKoszulDuality:
    """Test Koszul dual kappa and complementarity (AP24)."""

    def test_heisenberg_kappa_antisymmetric(self):
        """Heisenberg: kappa(H_k) + kappa(H_k^!) = 0."""
        for k in [Fraction(1), Fraction(3), Fraction(1, 2)]:
            A = make_heisenberg(k)
            assert kappa_sum(A) == 0

    def test_sl2_kappa_antisymmetric(self):
        """sl_2: kappa + kappa' = 0 (Feigin-Frenkel)."""
        for k in [Fraction(1), Fraction(4), Fraction(10)]:
            A = make_affine_sl2(k)
            assert kappa_sum(A) == 0

    def test_virasoro_kappa_sum_13(self):
        """Virasoro: kappa + kappa' = 13, NOT 0 (AP24)."""
        for c in [Fraction(1), Fraction(13), Fraction(25), Fraction(26)]:
            A = make_virasoro(c)
            assert kappa_sum(A) == Fraction(13), \
                f"AP24 violation: kappa_sum(Vir_{c}) = {kappa_sum(A)}, expected 13"

    def test_betagamma_kappa_antisymmetric(self):
        """betagamma: kappa + kappa' = 0 (free field)."""
        A = make_betagamma()
        assert kappa_sum(A) == 0

    def test_virasoro_c13_self_dual_kappa(self):
        """Virasoro c=13: kappa = kappa' = 13/2 (self-dual point).

        At the self-dual point, kappa(Vir_13) = 13/2 and
        kappa(Vir_{26-13}) = kappa(Vir_13) = 13/2.
        The sum is still 13 (AP24).
        """
        A = make_virasoro(Fraction(13))
        assert A.kappa == Fraction(13, 2)
        assert koszul_dual_kappa(A) == Fraction(13, 2)
        assert A.kappa == koszul_dual_kappa(A)  # self-dual!


# =========================================================================
# 7. Genus tower from Theta_A
# =========================================================================

class TestGenusTower:
    """Test F_g = kappa * lambda_g^FP from the MC element."""

    def test_lambda_1_value(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp(1) == Fraction(1, 24)

    def test_genus_tower_sl2(self):
        """sl_2 at k=1: F_g = (9/4) * lambda_g."""
        A = make_affine_sl2(Fraction(1))
        tower = genus_tower_from_theta(A, max_g=3)
        kappa = Fraction(9, 4)
        assert tower[1] == kappa * Fraction(1, 24)
        assert tower[2] == kappa * _lambda_fp(2)

    def test_genus_expansion_three_paths(self):
        """Three-path verification of F_1 = kappa/24."""
        A = make_affine_sl2(Fraction(1))
        result = genus_expansion_three_paths(A)
        assert result["three_paths_agree"] is True
        assert result["F_1_shadow"] == result["F_1_annulus"]
        assert result["F_1_shadow"] == result["F_1_hochschild"]


# =========================================================================
# 8. sl_2 explicit verification
# =========================================================================

class TestSl2Explicit:
    """Explicit sl_2 Chern-Simons: the prototypical example."""

    def test_sl2_kappa_formula(self):
        """kappa(sl_2, k) = 3*(k+2)/4."""
        assert sl2_kappa_explicit(Fraction(1)) == Fraction(9, 4)
        assert sl2_kappa_explicit(Fraction(4)) == Fraction(9, 2)
        assert sl2_kappa_explicit(Fraction(0)) == Fraction(3, 2)

    def test_sl2_collision_residue_explicit(self):
        """sl_2: OPE double pole -> collision single pole (AP19)."""
        result = sl2_collision_residue_explicit(Fraction(1))
        assert result["AP19_applied"] is True
        assert result["OPE_double_pole"] == Fraction(1)
        assert result["collision_residue_single_pole"] == Fraction(1)

    def test_sl2_full_verification_k1(self):
        """Full holographic dictionary for sl_2 at k=1."""
        result = sl2_explicit_verification(Fraction(1))
        assert result["r_matrix_leading_pole"] == 1
        assert result["r_matrix_is_casimir_type"] is True
        assert result["cybe_from_mc"] is True
        assert result["cybe_numerical_sl2"] is True
        assert result["qybe_yang_sl2"] is True
        assert result["kz_matches_shadow"] is True
        assert result["F_1_equals_kappa_over_24"] is True
        assert result["kappa_anti_symmetric"] is True
        assert result["three_paths_agree"] is True

    def test_sl2_full_verification_k4(self):
        """Full holographic dictionary for sl_2 at k=4."""
        result = sl2_explicit_verification(Fraction(4))
        assert result["kappa"] == Fraction(9, 2)
        assert result["kappa_sum"] == Fraction(0)
        assert result["three_paths_agree"] is True


# =========================================================================
# 9. Master verification sweep
# =========================================================================

class TestMasterSweep:
    """Master verification across all standard families."""

    def test_master_sweep_all_families(self):
        """All families pass the holographic dictionary verification."""
        results = master_holographic_verification()
        for name, data in results.items():
            assert data["cybe"] is True, f"CYBE failed for {name}"
            assert data["connection_flat"] is True, f"Connection not flat for {name}"

    def test_master_sweep_kappa_consistency(self):
        """Kappa values are consistent across the sweep."""
        results = master_holographic_verification()

        # Heisenberg: kappa = level = 1
        assert results["Heisenberg(k=1)"]["kappa"] == Fraction(1)

        # sl_2 at k=1: kappa = 9/4
        assert results["sl_2(k=1)"]["kappa"] == Fraction(9, 4)

        # sl_2 at k=4: kappa = 9/2
        assert results["sl_2(k=4)"]["kappa"] == Fraction(9, 2)

        # sl_3 at k=1: kappa = 8*(1+3)/(2*3) = 16/3
        assert results["sl_3(k=1)"]["kappa"] == Fraction(16, 3)

        # Virasoro c=25: kappa = 25/2
        assert results["Vir(c=25)"]["kappa"] == Fraction(25, 2)

        # Virasoro c=26: kappa = 13
        assert results["Vir(c=26)"]["kappa"] == Fraction(13)

        # Virasoro c=13: kappa = 13/2
        assert results["Vir(c=13)"]["kappa"] == Fraction(13, 2)

    def test_full_dictionary_extraction(self):
        """Extract complete holographic dictionary for each family."""
        families = [
            make_heisenberg(Fraction(1)),
            make_affine_sl2(Fraction(1)),
            make_virasoro(Fraction(25)),
            make_betagamma(),
        ]
        for A in families:
            H = extract_holographic_dictionary(A)
            assert H.shadow_connection_flat is True
            assert H.path_a_mc_projection is True
            assert H.path_b_boundary_ope is True
            assert H.collision_residue.satisfies_cybe is True

    def test_ap24_virasoro_all_c(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c_num in range(0, 30):
            c = Fraction(c_num)
            A = make_virasoro(c)
            s = kappa_sum(A)
            assert s == Fraction(13), \
                f"AP24 violation at c={c}: kappa_sum={s}"

    def test_ap19_pole_orders_all_families(self):
        """AP19: collision residue pole = OPE max pole - 1."""
        # Heisenberg: OPE max 2 -> coll 1
        assert collision_residue_leading_pole(
            extract_collision_residue(make_heisenberg())) == 1

        # sl_2: OPE max 2 -> coll 1
        assert collision_residue_leading_pole(
            extract_collision_residue(make_affine_sl2(Fraction(1)))) == 1

        # Virasoro: OPE max 4 -> coll 3
        assert collision_residue_leading_pole(
            extract_collision_residue(make_virasoro(Fraction(25)))) == 3

        # betagamma: OPE max 1 -> coll 0 (drops to regular)
        assert collision_residue_leading_pole(
            extract_collision_residue(make_betagamma())) == 0
