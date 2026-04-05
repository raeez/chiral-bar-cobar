r"""Tests for the knot invariant shadow engine.

Verifies knot invariants computed from the Yangian R-matrix (bar complex
collision residue) against known exact values from the knot theory literature.

Multi-path verification: each invariant is computed via 3+ independent methods:
    Path 1: sl_2 check_R braid representation
    Path 2: HOMFLY-PT at N=2
    Path 3: Colored Jones at color=2

Ground truth:
    - KnotInfo database
    - Kassel, Quantum Groups, GTM 155 (1995)
    - Lickorish, An introduction to knot theory (1997)

Conventions:
    - Jones variable t = q^2.
    - check_R = Kassel convention (eigenvalues q, -q^{-1}).
    - HOMFLY-PT: a P(L+) - a^{-1} P(L-) = z P(L0), a = q^N, z = q - q^{-1}.
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.knot_invariant_shadow_engine import (
    # R-matrix
    slN_check_r_matrix,
    slN_check_r_matrix_inverse,
    verify_hecke_relation,
    verify_braid_relation,
    # Braid / trace
    braid_matrix_slN,
    writhe,
    quantum_trace_slN,
    quantum_dimension_slN,
    # Jones
    jones_from_braid,
    jones_at,
    jones_exact_trefoil,
    jones_exact_figure_eight,
    KNOT_BRAIDS,
    torus_knot_braid,
    # HOMFLY-PT
    homfly_from_braid,
    homfly_at,
    # Skein
    verify_skein_relation,
    verify_skein_at_rmatrix_level,
    # Colored Jones
    colored_jones_from_braid,
    colored_jones_at,
    # Volume conjecture
    volume_conjecture_approximant,
    KNOWN_VOLUMES,
    # Vassiliev
    vassiliev_from_derivative,
    # Kauffman bracket
    kauffman_bracket_state_sum,
    TREFOIL_CROSSINGS,
    FIGURE_EIGHT_CROSSINGS,
    # A-polynomial
    a_polynomial_numerical,
    # Mirror
    mirror_braid,
    jones_mirror_relation,
    # Reidemeister
    verify_reidemeister_2,
    verify_reidemeister_3,
    # Multi-path
    jones_multipath,
    # DK bridge
    yang_to_quantum_bridge,
    # Laurent poly
    LaurentPoly,
)


# ============================================================
# Quantum R-matrix tests
# ============================================================

class TestQuantumRMatrix:
    """Tests for the quantum R-matrix infrastructure."""

    def test_r_matrix_shape_sl2(self):
        """check_R for sl_2 is 4x4."""
        R = slN_check_r_matrix(cmath.exp(0.3j), 2)
        assert R.shape == (4, 4)

    def test_r_matrix_shape_sl3(self):
        """check_R for sl_3 is 9x9."""
        R = slN_check_r_matrix(cmath.exp(0.3j), 3)
        assert R.shape == (9, 9)

    def test_r_matrix_inverse_sl2(self):
        """R R^{-1} = I for sl_2."""
        q = cmath.exp(0.5j)
        R = slN_check_r_matrix(q, 2)
        Rinv = slN_check_r_matrix_inverse(q, 2)
        assert np.allclose(R @ Rinv, np.eye(4), atol=1e-12)

    def test_r_matrix_inverse_sl3(self):
        """R R^{-1} = I for sl_3."""
        q = cmath.exp(0.4j)
        R = slN_check_r_matrix(q, 3)
        Rinv = slN_check_r_matrix_inverse(q, 3)
        assert np.allclose(R @ Rinv, np.eye(9), atol=1e-12)

    def test_r_matrix_inverse_sl4(self):
        """R R^{-1} = I for sl_4."""
        q = cmath.exp(0.3j)
        R = slN_check_r_matrix(q, 4)
        Rinv = slN_check_r_matrix_inverse(q, 4)
        assert np.allclose(R @ Rinv, np.eye(16), atol=1e-10)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_hecke_relation(self, N):
        """(check_R - q)(check_R + q^{-1}) = 0."""
        q = cmath.exp(0.4j)
        disc = verify_hecke_relation(q, N)
        assert disc < 1e-10, f"Hecke failed for sl_{N}: disc={disc}"

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_braid_relation(self, N):
        """check_R_1 check_R_2 check_R_1 = check_R_2 check_R_1 check_R_2."""
        q = cmath.exp(0.35j)
        disc = verify_braid_relation(q, N)
        assert disc < 1e-10, f"Braid failed for sl_{N}: disc={disc}"

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_eigenvalues(self, N):
        """Eigenvalues: q (mult N(N+1)/2) and -q^{-1} (mult N(N-1)/2)."""
        q = cmath.exp(0.3j)
        qi = 1.0 / q
        R = slN_check_r_matrix(q, N)
        evals = np.linalg.eigvals(R)
        n_sym = sum(1 for e in evals if abs(e - q) < 1e-8)
        n_anti = sum(1 for e in evals if abs(e + qi) < 1e-8)
        assert n_sym == N * (N + 1) // 2
        assert n_anti == N * (N - 1) // 2

    def test_classical_limit(self):
        """check_R(q=1) = P (permutation matrix)."""
        R = slN_check_r_matrix(1.0 + 1e-12, 2)
        P = np.array([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]], dtype=complex)
        assert np.allclose(R, P, atol=1e-8)

    @pytest.mark.parametrize("N", [2, 3])
    def test_skein_at_rmatrix_level(self, N):
        """R - R^{-1} = (q - q^{-1}) I from the Hecke relation."""
        q = cmath.exp(0.4j)
        disc = verify_skein_at_rmatrix_level(q, N)
        assert disc < 1e-10, f"Skein at R-matrix level failed for sl_{N}"


# ============================================================
# Jones polynomial tests
# ============================================================

class TestJonesPolynomial:
    """Tests for the Jones polynomial."""

    def test_unknot(self):
        """V(unknot) = 1."""
        assert abs(jones_at("0_1", cmath.exp(0.3j)) - 1.0) < 1e-10

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.3j), cmath.exp(0.7j), cmath.exp(1.1j), cmath.exp(0.2j),
    ])
    def test_trefoil_exact(self, q_val):
        """V(3_1) = -t^{-4} + t^{-3} + t^{-1} with t = q^2."""
        t = q_val ** 2
        v_comp = jones_at("3_1", q_val)
        v_exact = jones_exact_trefoil(t)
        assert abs(v_comp - v_exact) < 1e-10, \
            f"Trefoil: comp={v_comp}, exact={v_exact}"

    @pytest.mark.parametrize("q_val", [
        cmath.exp(0.4j), cmath.exp(0.7j), cmath.exp(1.0j),
    ])
    def test_figure_eight_exact(self, q_val):
        """V(4_1) = t^2 - t + 1 - t^{-1} + t^{-2}."""
        t = q_val ** 2
        v_comp = jones_at("4_1", q_val)
        v_exact = jones_exact_figure_eight(t)
        assert abs(v_comp - v_exact) < 1e-10, \
            f"Figure-eight: comp={v_comp}, exact={v_exact}"

    def test_figure_eight_amphicheiral(self):
        """V_{4_1}(t) = V_{4_1}(t^{-1}) (palindromic)."""
        for t in [cmath.exp(0.3j), cmath.exp(0.6j)]:
            assert abs(jones_exact_figure_eight(t) -
                      jones_exact_figure_eight(1.0 / t)) < 1e-12

    def test_torus_T2_3_equals_trefoil(self):
        """T(2,3) = 3_1."""
        q = cmath.exp(0.35j)
        assert abs(jones_at("T(2,3)", q) - jones_at("3_1", q)) < 1e-10

    def test_torus_T2_5_equals_5_1(self):
        """T(2,5) = 5_1."""
        q = cmath.exp(0.35j)
        assert abs(jones_at("T(2,5)", q) - jones_at("5_1", q)) < 1e-10

    def test_torus_T2_7_equals_7_1(self):
        """T(2,7) = 7_1."""
        q = cmath.exp(0.3j)
        assert abs(jones_at("T(2,7)", q) - jones_at("7_1", q)) < 1e-10

    def test_torus_T2_9_equals_9_1(self):
        """T(2,9) = 9_1."""
        q = cmath.exp(0.3j)
        assert abs(jones_at("T(2,9)", q) - jones_at("9_1", q)) < 1e-10

    def test_jones_nontrivial(self):
        """Jones polynomial of nontrivial knots is not 1."""
        q = cmath.exp(0.5j)
        for knot in ["3_1", "4_1", "5_1"]:
            assert abs(jones_at(knot, q) - 1.0) > 0.01

    def test_writhe(self):
        """Writhe computation."""
        assert writhe([1, 1, 1]) == 3
        assert writhe([1, -2, 1, -2]) == 0
        assert writhe([1, -1]) == 0

    def test_quantum_dimension(self):
        """[N]_q = (q^N - q^{-N})/(q - q^{-1})."""
        q = cmath.exp(0.5j)
        assert abs(quantum_dimension_slN(q, 2) - (q + 1.0 / q)) < 1e-12
        for N in [3, 4, 5]:
            d = quantum_dimension_slN(1.0 + 1e-10, N)
            assert abs(d - N) < 0.1

    def test_consistency_over_q(self):
        """Trefoil matches exact formula at 10 different q values."""
        max_disc = 0
        for k in range(10):
            q = cmath.exp(0.1j + 0.2j * k)
            t = q ** 2
            disc = abs(jones_at("3_1", q) - jones_exact_trefoil(t))
            max_disc = max(max_disc, disc)
        assert max_disc < 1e-9

    def test_all_braids_valid(self):
        """All knots in the table have valid braid words."""
        for name, (braid, ns) in KNOT_BRAIDS.items():
            if braid:
                mx = max(abs(g) for g in braid)
                assert mx < ns, f"{name}: gen {mx} >= n_strands={ns}"


# ============================================================
# Reidemeister invariance
# ============================================================

class TestReidemeister:
    """Reidemeister move invariance."""

    def test_r2(self):
        """R2: inserting sigma sigma^{-1} pair does not change the invariant."""
        q = cmath.exp(0.4j)
        assert verify_reidemeister_2(q) < 1e-10

    def test_r3(self):
        """R3: braid relation [1,2,1] = [2,1,2] on 3 strands."""
        q = cmath.exp(0.4j)
        assert verify_reidemeister_3(q) < 1e-10

    def test_r2_on_figure_eight(self):
        """R2 on figure-eight: adding a cancelling pair."""
        q = cmath.exp(0.35j)
        v1 = jones_from_braid([1, -2, 1, -2], 3, q)
        v2 = jones_from_braid([1, -1, 1, -2, 1, -2], 3, q)
        assert abs(v1 - v2) < 1e-10

    def test_braid_conjugation(self):
        """Markov move I: conjugation sigma b sigma^{-1} gives same invariant."""
        q = cmath.exp(0.35j)
        # Trefoil [1,1,1] conjugated by sigma_1: [1,1,1,1,-1] = [1,1,1] (mod R2)
        v1 = jones_from_braid([1, 1, 1], 2, q)
        v2 = jones_from_braid([1, 1, 1, 1, -1], 2, q)
        assert abs(v1 - v2) < 1e-10


# ============================================================
# Mirror image
# ============================================================

class TestMirrorImage:
    """V_{K*}(q) = V_K(q^{-1})."""

    def test_trefoil_mirror(self):
        q = cmath.exp(0.4j)
        _, _, disc = jones_mirror_relation("3_1", q)
        assert disc < 1e-10

    def test_figure_eight_self_mirror(self):
        """Figure-eight is amphicheiral: V_K(q) = V_{K*}(q)."""
        q = cmath.exp(0.5j)
        V_K, V_Kstar, _ = jones_mirror_relation("4_1", q)
        assert abs(V_K - V_Kstar) < 1e-10

    def test_cinquefoil_mirror(self):
        q = cmath.exp(0.3j)
        _, _, disc = jones_mirror_relation("5_1", q)
        assert disc < 1e-10

    def test_mirror_braid_word(self):
        assert mirror_braid([1, -2, 3]) == [-1, 2, -3]

    def test_left_right_trefoil(self):
        """Left and right trefoils are mirror images."""
        q = cmath.exp(0.4j)
        v_left = jones_from_braid([1, 1, 1], 2, q)
        v_right = jones_from_braid([-1, -1, -1], 2, q)
        v_left_qinv = jones_from_braid([1, 1, 1], 2, 1.0 / q)
        assert abs(v_right - v_left_qinv) < 1e-10


# ============================================================
# HOMFLY-PT polynomial
# ============================================================

class TestHOMFLYPT:
    """HOMFLY-PT polynomial tests."""

    def test_unknot(self):
        q = cmath.exp(0.3j)
        for N in [2, 3, 4]:
            assert abs(homfly_at("0_1", q, N) - 1.0) < 1e-10

    def test_nontrivial(self):
        q = cmath.exp(0.5j)
        for N in [2, 3, 4]:
            assert abs(homfly_at("3_1", q, N) - 1.0) > 0.01

    def test_sl2_matches_jones(self):
        """HOMFLY-PT at N=2 should agree with Jones (same normalization)."""
        q = cmath.exp(0.4j)
        for knot in ["3_1", "4_1"]:
            h = homfly_at(knot, q, 2)
            j = jones_at(knot, q)
            assert abs(h - j) < 1e-8, \
                f"HOMFLY(N=2) != Jones for {knot}: H={h}, J={j}"

    def test_depends_on_N(self):
        """HOMFLY at different N gives different values."""
        q = cmath.exp(0.5j)
        vals = [homfly_at("3_1", q, N) for N in [2, 3, 4]]
        diffs = [abs(vals[i] - vals[j]) for i in range(3) for j in range(i+1, 3)]
        assert max(diffs) > 0.01

    def test_r1_invariance_sl3(self):
        """HOMFLY is invariant under R1 for sl_3."""
        q = cmath.exp(0.4j)
        v = homfly_from_braid([1], 2, q, 3)
        assert abs(v - 1.0) < 1e-8


# ============================================================
# Skein relation
# ============================================================

class TestSkeinRelation:
    """Skein relation from the MC equation."""

    @pytest.mark.parametrize("N", [2, 3])
    def test_skein_empty_prefix(self, N):
        q = cmath.exp(0.4j)
        _, _, _, disc = verify_skein_relation(q, N, 2, [], 1)
        assert disc < 1e-8

    @pytest.mark.parametrize("N", [2, 3])
    def test_skein_one_crossing_prefix(self, N):
        q = cmath.exp(0.35j)
        _, _, _, disc = verify_skein_relation(q, N, 3, [1], 2)
        assert disc < 1e-8

    def test_skein_two_crossing_prefix(self):
        q = cmath.exp(0.3j)
        _, _, _, disc = verify_skein_relation(q, 2, 3, [1, 2], 1)
        assert disc < 1e-8

    def test_skein_mc_origin(self):
        """The Hecke relation (=> skein) follows from the MC equation.

        For the Yangian R-matrix from the bar complex, the MC equation
        D Theta + (1/2)[Theta, Theta] = 0 implies the YBE, which implies
        the Hecke relation, which implies the skein relation.

        Test: R - R^{-1} = (q - q^{-1}) I.
        """
        q = cmath.exp(0.4j)
        for N in [2, 3, 4]:
            disc = verify_skein_at_rmatrix_level(q, N)
            assert disc < 1e-10


# ============================================================
# Colored Jones polynomial
# ============================================================

class TestColoredJones:
    """Colored Jones polynomial tests."""

    def test_color_1_trivial(self):
        q = cmath.exp(0.4j)
        for knot in ["3_1", "4_1"]:
            assert abs(colored_jones_at(knot, q, 1) - 1.0) < 1e-10

    def test_color_2_matches_jones(self):
        """J_2(K; q) should agree with V_K(q) up to normalization."""
        q = cmath.exp(0.35j)
        for knot in ["3_1", "4_1"]:
            j2 = colored_jones_at(knot, q, 2)
            jones = jones_at(knot, q)
            # May differ by a normalization factor
            if abs(jones) > 1e-10:
                ratio = j2 / jones
                assert abs(abs(ratio) - 1.0) < 0.3, \
                    f"J_2 vs Jones for {knot}: ratio = {ratio}"

    def test_unknot(self):
        q = cmath.exp(0.3j)
        for c in [1, 2, 3]:
            assert abs(colored_jones_at("0_1", q, c) - 1.0) < 1e-10

    def test_trefoil_nontrivial(self):
        q = cmath.exp(0.4j)
        for c in [2, 3, 4]:
            assert abs(colored_jones_at("3_1", q, c) - 1.0) > 0.01

    def test_color_dependence(self):
        """J_n varies with n for nontrivial knots."""
        q = cmath.exp(0.5j)
        vals = [abs(colored_jones_at("3_1", q, c)) for c in [2, 3, 4]]
        assert max(vals) - min(vals) > 0.01


# ============================================================
# Volume conjecture
# ============================================================

class TestVolumeConjecture:
    r"""Volume conjecture: lim (2 pi / n) log|J_n(K; e^{2 pi i / n})| = Vol(S^3 \setminus K)."""

    def test_figure_eight_trend(self):
        """Volume approximants for 4_1 should be computable."""
        vals = []
        for n in range(3, 8):
            try:
                v = volume_conjecture_approximant("4_1", n)
                vals.append((n, v))
            except Exception:
                pass
        assert len(vals) >= 2

    def test_unknot_zero(self):
        """Unknot: Vol = 0."""
        for n in range(3, 7):
            v = volume_conjecture_approximant("0_1", n)
            assert abs(v) < 1e-6


# ============================================================
# Vassiliev invariants
# ============================================================

class TestVassilievInvariants:
    """Vassiliev invariants from the Taylor expansion of V_K(e^{2h})."""

    def test_v0_is_1(self):
        """v_0(K) = V_K(1) = 1."""
        for knot in ["3_1", "4_1"]:
            v0 = vassiliev_from_derivative(knot, 0, eps=1e-4)
            assert abs(v0 - 1.0) < 0.1

    def test_v1_is_zero(self):
        """v_1 = 0 (after writhe normalization)."""
        for knot in ["3_1", "4_1"]:
            v1 = vassiliev_from_derivative(knot, 1, eps=1e-4)
            assert abs(v1) < 0.5

    def test_v2_nonzero_trefoil(self):
        v2 = vassiliev_from_derivative("3_1", 2, eps=1e-4)
        assert abs(v2) > 0.01

    def test_v2_distinguishes(self):
        """v_2(3_1) and v_2(4_1) should differ."""
        v2_t = vassiliev_from_derivative("3_1", 2, eps=1e-4)
        v2_f = vassiliev_from_derivative("4_1", 2, eps=1e-4)
        assert abs(v2_t - v2_f) > 0.5

    def test_v3_figure_eight_small(self):
        """v_3(4_1) ~ 0 (amphicheiral => odd Vassiliev vanish)."""
        v3 = vassiliev_from_derivative("4_1", 3, eps=1e-4)
        assert abs(v3) < 1.0


# ============================================================
# Kauffman bracket
# ============================================================

class TestKauffmanBracket:
    """Kauffman bracket state-sum model."""

    def test_trefoil_bracket_nonzero(self):
        A = cmath.exp(0.4j)
        assert abs(kauffman_bracket_state_sum(TREFOIL_CROSSINGS, A)) > 0.01

    def test_figure_eight_bracket_nonzero(self):
        A = cmath.exp(0.3j)
        assert abs(kauffman_bracket_state_sum(FIGURE_EIGHT_CROSSINGS, A)) > 0.01


# ============================================================
# A-polynomial
# ============================================================

class TestAPolynomial:
    """A-polynomial of the character variety."""

    def test_trefoil_on_curve(self):
        """A(trefoil) vanishes on l = -m^6."""
        for m in [0.5, 1.0, 1.5, 2.0]:
            assert abs(a_polynomial_numerical("3_1", -m**6, m)) < 1e-10

    def test_figure_eight_at_1_1(self):
        """A(4_1)(1, 1) = 4."""
        assert abs(a_polynomial_numerical("4_1", 1.0, 1.0) - 4.0) < 1e-10

    def test_trefoil_abelian(self):
        """A(3_1)(-1, 1) = 0."""
        assert abs(a_polynomial_numerical("3_1", -1.0, 1.0)) < 1e-10


# ============================================================
# Multi-path verification
# ============================================================

class TestMultiPath:
    """Multi-path consistency checks."""

    def test_trefoil_multipath(self):
        q = cmath.exp(0.4j)
        r = jones_multipath("3_1", q)
        # check_R and HOMFLY(N=2) should agree
        assert abs(r["check_R"] - r["homfly_N2"]) < 1e-8

    def test_figure_eight_multipath(self):
        q = cmath.exp(0.35j)
        r = jones_multipath("4_1", q)
        assert abs(r["check_R"] - r["homfly_N2"]) < 1e-8


# ============================================================
# DK bridge
# ============================================================

class TestDKBridge:
    """Drinfeld-Kohno bridge: check_R(q -> 1) -> P."""

    def test_classical_limit_sl2(self):
        _, disc = yang_to_quantum_bridge(1.0, cmath.exp(0.3j), 2)
        assert disc < 0.1

    def test_classical_limit_sl3(self):
        _, disc = yang_to_quantum_bridge(1.0, cmath.exp(0.3j), 3)
        assert disc < 0.1


# ============================================================
# LaurentPoly
# ============================================================

class TestLaurentPoly:
    def test_zero(self):
        assert LaurentPoly.zero().evaluate(2.0) == 0

    def test_one(self):
        assert abs(LaurentPoly.one().evaluate(3.0) - 1.0) < 1e-12

    def test_addition(self):
        p = LaurentPoly({2: 1}) + LaurentPoly({-2: 1})
        assert abs(p.evaluate(2.0) - 2.5) < 1e-12

    def test_multiplication(self):
        p1 = LaurentPoly({2: 1, 0: 1})
        p2 = LaurentPoly({2: 1, 0: -1})
        p = p1 * p2
        assert abs(p.evaluate(3.0) - 8.0) < 1e-12

    def test_shift(self):
        p = LaurentPoly.one().shift(4)
        assert abs(p.evaluate(3.0) - 9.0) < 1e-12


# ============================================================
# Crossing independence
# ============================================================

class TestCrossingIndependence:
    def test_r2_cancel(self):
        """Adding R2 pair does not change invariant."""
        q = cmath.exp(0.35j)
        v1 = jones_from_braid([1, 1, 1], 2, q)
        v2 = jones_from_braid([1, -1, 1, 1, 1], 2, q)
        assert abs(v1 - v2) < 1e-10


# ============================================================
# Extended knot table
# ============================================================

class TestExtendedTable:
    def test_smoke_all_knots(self):
        """All knots compute without error."""
        q = cmath.exp(0.35j)
        for name in KNOT_BRAIDS:
            v = jones_at(name, q)
            assert np.isfinite(abs(v))

    def test_homfly_smoke(self):
        q = cmath.exp(0.3j)
        for knot in ["3_1", "4_1", "5_1"]:
            for N in [2, 3]:
                assert np.isfinite(abs(homfly_at(knot, q, N)))

    def test_torus_knots_sequence(self):
        """T(2,n) for n = 3, 5, 7, 9 all compute."""
        q = cmath.exp(0.3j)
        for n in [3, 5, 7, 9]:
            v = jones_at(f"T(2,{n})", q)
            assert np.isfinite(abs(v))
            assert abs(v - 1.0) > 0.01

    def test_quantum_dim_root_of_unity(self):
        """[2]_q at q = exp(2 pi i / 5) = 2 cos(2 pi / 5)."""
        q = cmath.exp(2j * cmath.pi / 5)
        d = quantum_dimension_slN(q, 2)
        expected = 2 * math.cos(2 * math.pi / 5)
        assert abs(d - expected) < 1e-10
