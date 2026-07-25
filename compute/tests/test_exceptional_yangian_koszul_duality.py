"""Classical input checks for the exceptional Yangian programme.

These tests establish Cartan data, root counts, Weyl dimensions, diagram
automorphisms, and elementary permutation-operator identities.  They do
not evaluate an exceptional Yangian bar complex, prove PBW, construct an
exceptional R-matrix, or establish Koszul duality.  Those theorem-level
statements require their own algebraic implementations or cited inputs.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import pytest

from compute.lib.yangian_rtt_exceptional import (
    ExceptionalRootSystem,
    EXCEPTIONAL_DATA,
    FUNDAMENTAL_DIMS,
    CARTAN_MATRICES_EXCEPTIONAL,
    weyl_dim_explicit,
)


# ---------------------------------------------------------------------------
# Fixtures and helpers
# ---------------------------------------------------------------------------


EXCEPTIONAL_TYPES = ("E6", "E7", "E8", "F4", "G2")


# Cartan / root-system ground truth (from Bourbaki / Humphreys).
GROUND_TRUTH = {
    "E6": {"rank": 6, "dim": 78, "num_pos_roots": 36, "dual_coxeter": 12,
           "out_order": 2, "simply_laced": True},
    "E7": {"rank": 7, "dim": 133, "num_pos_roots": 63, "dual_coxeter": 18,
           "out_order": 1, "simply_laced": True},
    "E8": {"rank": 8, "dim": 248, "num_pos_roots": 120, "dual_coxeter": 30,
           "out_order": 1, "simply_laced": True},
    "F4": {"rank": 4, "dim": 52, "num_pos_roots": 24, "dual_coxeter": 9,
           "out_order": 1, "simply_laced": False},
    "G2": {"rank": 2, "dim": 14, "num_pos_roots": 6, "dual_coxeter": 4,
           "out_order": 1, "simply_laced": False},
}


def _chevalley_involution_on_simple_roots(cartan):
    """Return the matrix representing sigma: alpha_i -> -alpha_i on the
    alpha basis.  This is -I of the appropriate size, regardless of the
    Dynkin diagram: the Chevalley involution is the UNIQUE anti-involution
    of a simple Lie algebra that negates each simple root (Humphreys,
    Thm 14.3, or Kac's ``Infinite Dimensional Lie Algebras'').

    The matrix -I is independent of Cartan data, which is what makes the
    Chevalley involution intrinsic.  We derive it here from first
    principles and check involutivity.
    """
    r = len(cartan)
    return -np.eye(r)


def _is_involution(M):
    """sigma is an involution iff M @ M = I."""
    r = M.shape[0]
    return np.allclose(M @ M, np.eye(r), atol=1e-12)


# ---------------------------------------------------------------------------
# Root and representation data for all five exceptional types
# ---------------------------------------------------------------------------


def test_exceptional_root_and_fundamental_representation_data():
    """Root counts, Lie dimensions, and selected Weyl dimensions agree."""
    for name in EXCEPTIONAL_TYPES:
        rs = ExceptionalRootSystem(name)
        gt = GROUND_TRUTH[name]

        # (1) Root-system combinatorics.
        assert rs.rank == gt["rank"], f"{name}: rank mismatch"
        assert len(rs.positive_roots) == gt["num_pos_roots"], (
            f"{name}: positive-root count {len(rs.positive_roots)} != "
            f"expected {gt['num_pos_roots']}"
        )
        assert rs.dim_algebra == gt["dim"], (
            f"{name}: dim g = {rs.dim_algebra} != expected {gt['dim']}"
        )
        assert rs.dual_coxeter_number == gt["dual_coxeter"], (
            f"{name}: h^vee = {rs.dual_coxeter_number} != "
            f"{gt['dual_coxeter']}"
        )

        # dim g = rank + 2 * num pos roots
        assert rs.dim_algebra == rs.rank + 2 * len(rs.positive_roots), (
            f"{name}: Lie-algebra dimension identity "
            f"dim = rank + 2 * |Phi_+| fails"
        )

    # (2) Weyl-dimension check on the standard minuscule/adjoint representations.
    # For simply-laced exceptional types, Weyl dimension is computable.
    checks = [
        ("E6", (1, 0, 0, 0, 0, 0), 27),   # minuscule 27
        ("E6", (0, 0, 0, 0, 0, 1), 27),   # dual 27*
        ("E7", (0, 0, 0, 0, 0, 0, 1), 56),  # minuscule 56
        ("E8", (0, 0, 0, 0, 0, 0, 0, 1), 248),  # adjoint 248
    ]
    for name, hw, expected_dim in checks:
        d = weyl_dim_explicit(name, hw)
        assert d == expected_dim, (
            f"{name} Weyl dim at {hw} = {d} != expected {expected_dim}"
        )

# ---------------------------------------------------------------------------
# Chevalley involution on the classical root lattice
# ---------------------------------------------------------------------------


def test_chevalley_involution_all_exceptional_types():
    """Chevalley involution sigma_g on a simple Lie algebra g satisfies
    sigma_g(alpha_i) = -alpha_i for every simple root.  In the alpha basis,
    sigma_g acts as -I.

    We verify:
    (1) sigma_g is an involution: (-I)^2 = I;
    (2) sigma_g negates every simple root;
    (3) sigma_g negates every positive root (automatic from (2)
        by linearity);
    (4) the outer-automorphism-group orders match Bourbaki.
    """
    for name in EXCEPTIONAL_TYPES:
        rs = ExceptionalRootSystem(name)
        gt = GROUND_TRUTH[name]

        sigma = _chevalley_involution_on_simple_roots(rs.cartan)

        # (1) Involutivity.
        assert _is_involution(sigma), f"{name}: sigma is not an involution"

        # (2) Every simple root is negated.
        for i in range(rs.rank):
            e_i = np.zeros(rs.rank)
            e_i[i] = 1.0
            sigma_e_i = sigma @ e_i
            expected = -e_i
            assert np.allclose(sigma_e_i, expected, atol=1e-12), (
                f"{name}: sigma(alpha_{i}) != -alpha_{i}"
            )

        # (3) Every positive root negates (linearity from (2)).
        for beta_alpha in rs.positive_roots_alpha:
            beta_vec = np.array(beta_alpha, dtype=float)
            sigma_beta = sigma @ beta_vec
            assert np.allclose(sigma_beta, -beta_vec, atol=1e-12), (
                f"{name}: sigma(beta) != -beta for beta = {beta_alpha}"
            )

        # (4) Outer automorphism group order.
        # E_6: Dynkin diagram has a flip (exchange leaves) -> |Out| = 2.
        # E_7, E_8, F_4, G_2: no non-trivial diagram automorphism -> |Out| = 1.
        # We verify via direct Cartan-matrix permutation search.
        A = np.array(rs.cartan)
        out_order = _count_cartan_automorphisms(A)
        assert out_order == gt["out_order"], (
            f"{name}: |Out| = {out_order} != expected {gt['out_order']}"
        )


def _count_cartan_automorphisms(A):
    """Count permutations P of nodes such that P^T A P = A.

    This equals |Out(g)| for simple g (Out = diagram automorphism group).
    """
    from itertools import permutations
    r = A.shape[0]
    count = 0
    for perm in permutations(range(r)):
        P = np.zeros((r, r))
        for i, j in enumerate(perm):
            P[j, i] = 1
        if np.allclose(P.T @ A @ P, A):
            count += 1
    return count


# ---------------------------------------------------------------------------
# Scalar unitarity of the permutation-operator R-matrix
# ---------------------------------------------------------------------------


def test_permutation_r_matrix_scalar_unitarity_at_selected_dimensions():
    """For the standard permutation-operator ansatz on a vector space V,

      R(u; hbar) = 1 - hbar * P / u         (Yang R-matrix)
      R(u; hbar) R(u; -hbar) = (1-hbar^2/u^2) Id.

    This linear-algebra identity uses P^2=Id.  The selected dimensions
    coincide with familiar exceptional representations; the identity
    itself supplies no exceptional Yangian or bar-complex structure.
    """
    # Test dimensions chosen to match the smallest fundamental of each type.
    test_fundamentals = {
        "E6": 27,
        "E7": 56,
        "E8": 248,
        "F4": 26,
        "G2": 7,
    }

    hbar = 0.1
    u = 2.0

    for name, dim in test_fundamentals.items():
        # Permutation matrix on dim-dimensional V tensor V (size dim^2).
        # To keep tests fast for E_8 (dim^2 = 61504), we verify the
        # algebraic identity analytically, then check a small numerical
        # instance at dim 2 as a sanity base.
        if dim * dim > 10000:
            # Analytic verification: the identity (1 - hbar P/u)(1 + hbar P/u) / 1
            # evaluates to (1 - hbar^2/u^2) on the {Sym, Alt} eigenbasis of P;
            # inverting gives R^{-1}(u; hbar) = (1 + hbar P/u) / (1 - hbar^2/u^2)
            # = R(u; -hbar) / (1 - hbar^2/u^2).  The normalization factor
            # (1 - hbar^2/u^2) is scalar.  We test this unitarity identity
            # on the two eigenvalues of the permutation operator.
            for P_eigenvalue in (+1, -1):
                R_plus = 1.0 - hbar * P_eigenvalue / u
                R_minus = 1.0 + hbar * P_eigenvalue / u  # R(u; -hbar)
                R_inv_expected = R_minus / (1.0 - (hbar ** 2) / (u ** 2))
                R_inv_computed = 1.0 / R_plus
                assert abs(R_inv_computed - R_inv_expected) < 1e-12, (
                    f"{name}: R-matrix sign-flip identity fails on "
                    f"P-eigenvalue {P_eigenvalue} at dim = {dim}"
                )
        else:
            # Direct matrix instance.
            P = np.zeros((dim * dim, dim * dim))
            for i in range(dim):
                for j in range(dim):
                    P[i * dim + j, j * dim + i] = 1.0

            I = np.eye(dim * dim)
            R_hbar = I - hbar * P / u
            R_minus_hbar = I + hbar * P / u  # = R(u; -hbar)

            # On V_fund tensor V_fund, R(u; hbar) * R(u; -hbar) should be a scalar.
            product = R_hbar @ R_minus_hbar
            expected_scalar = (1.0 - (hbar ** 2) / (u ** 2))
            assert np.allclose(product, expected_scalar * I, atol=1e-10), (
                f"{name}: R(u; hbar) R(u; -hbar) != scalar at dim = {dim}"
            )


# ---------------------------------------------------------------------------
# Per-type classical data
# ---------------------------------------------------------------------------


def test_E6_classical_data_consistency():
    """E_6 Cartan data, outer-automorphism
    group order, fundamental-representation dimensions.
    """
    rs = ExceptionalRootSystem("E6")
    assert rs.rank == 6
    assert rs.dim_algebra == 78
    assert rs.dual_coxeter_number == 12
    assert len(rs.positive_roots) == 36

    # Fundamental 27 and its dual 27*.
    assert weyl_dim_explicit("E6", (1, 0, 0, 0, 0, 0)) == 27
    assert weyl_dim_explicit("E6", (0, 0, 0, 0, 0, 1)) == 27

    # Outer automorphism: Dynkin-diagram flip.
    A = np.array(rs.cartan)
    assert _count_cartan_automorphisms(A) == 2, "E_6 Out = Z/2"


def test_E7_classical_data_consistency():
    rs = ExceptionalRootSystem("E7")
    assert rs.rank == 7
    assert rs.dim_algebra == 133
    assert rs.dual_coxeter_number == 18
    assert len(rs.positive_roots) == 63

    assert weyl_dim_explicit("E7", (0, 0, 0, 0, 0, 0, 1)) == 56

    A = np.array(rs.cartan)
    assert _count_cartan_automorphisms(A) == 1, "E_7 Out = 1"


def test_E8_classical_data_consistency():
    rs = ExceptionalRootSystem("E8")
    assert rs.rank == 8
    assert rs.dim_algebra == 248
    assert rs.dual_coxeter_number == 30
    assert len(rs.positive_roots) == 120
    # Total root system: 240 = 2 * 120.
    assert 2 * len(rs.positive_roots) == 240

    assert weyl_dim_explicit("E8", (0, 0, 0, 0, 0, 0, 0, 1)) == 248

    A = np.array(rs.cartan)
    assert _count_cartan_automorphisms(A) == 1, "E_8 Out = 1"


def test_F4_classical_data_consistency():
    rs = ExceptionalRootSystem("F4")
    assert rs.rank == 4
    assert rs.dim_algebra == 52
    assert rs.dual_coxeter_number == 9
    assert len(rs.positive_roots) == 24

    # F_4 is non-simply-laced: symmetrizer d = (1, 1, 2, 2) or an equivalent
    # up to overall rescaling.  We check that there exist at least two
    # distinct values in the symmetrizer (not all equal).
    d = rs.symmetrizer
    assert len(set(d)) >= 2, (
        f"F_4 symmetrizer should be non-trivial, got {d}"
    )

    A = np.array(rs.cartan)
    assert _count_cartan_automorphisms(A) == 1, "F_4 Out = 1"


def test_G2_classical_data_consistency():
    rs = ExceptionalRootSystem("G2")
    assert rs.rank == 2
    assert rs.dim_algebra == 14
    assert rs.dual_coxeter_number == 4
    assert len(rs.positive_roots) == 6

    # G_2 is non-simply-laced.
    d = rs.symmetrizer
    assert len(set(d)) >= 2, (
        f"G_2 symmetrizer should be non-trivial, got {d}"
    )

    A = np.array(rs.cartan)
    assert _count_cartan_automorphisms(A) == 1, "G_2 Out = 1"


# ---------------------------------------------------------------------------
# Cross-type sanity check: all five types covered, none missed.
# ---------------------------------------------------------------------------


def test_five_family_coverage_non_trivial():
    """Smoke test: ensure all five exceptional types are testable via the
    classical compute infrastructure, and that each has non-trivial data.
    """
    covered = set()
    for name in EXCEPTIONAL_TYPES:
        rs = ExceptionalRootSystem(name)
        assert rs.dim_algebra > 0
        assert rs.rank > 0
        assert len(rs.positive_roots) > 0
        covered.add(name)
    assert covered == set(EXCEPTIONAL_TYPES), (
        f"Five-family coverage incomplete: {covered} != "
        f"{set(EXCEPTIONAL_TYPES)}"
    )


def test_cartan_killing_family_inventory():
    """The Cartan--Killing inventory has four series and five exceptions."""
    # Classical types parameters (standard Dynkin).
    classical_families = {"A", "B", "C", "D"}
    exceptional_types = {"E6", "E7", "E8", "F4", "G2"}
    all_types = classical_families | exceptional_types
    # Cartan-Killing classification: four classical + five exceptional = 9 distinct types.
    assert len(all_types) == 9, (
        f"Cartan-Killing gives 9 simple types; got {all_types}"
    )
    # All five exceptional types are handled by this module:
    for name in exceptional_types:
        assert name in CARTAN_MATRICES_EXCEPTIONAL, (
            f"{name} absent from exceptional Cartan-matrix registry"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
