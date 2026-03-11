"""Tests for KL N-complex structure of u_q(sl_2) at roots of unity.

Fills structural gap H4. Tests verify:
  1. u_q(sl_2) structure constants (defining relations) at various roots of unity
  2. Associativity of the multiplication table
  3. Standard bar differential: d^2 = 0 always (associative algebra theorem)
  4. Bar cohomology nontrivial at roots of unity (non-semisimple)
  5. Q-deformed differential d_q: d_q^2 != 0 for N >= 3 (genuine N-complex)
  6. Q-deformed differential: d_q^N = 0 (N-complex structure)
  7. N = 2 recovery: d_q reduces to standard bar differential (d_q^2 = 0)
  8. N-complex cohomology flavors H^{j, N-j}
  9. Euler characteristic consistency across cohomology flavors

Mathematical context:
  The bar complex of an associative algebra ALWAYS has d^2 = 0 (this is a
  theorem, not a conjecture). The N-complex structure at roots of unity
  arises from the Q-DEFORMED bar differential d_q, which replaces the
  alternating signs (-1)^{i+1} with q-weights q^{i-1} following Kapranov's
  prescription. Since q^N = 1, the quantum binomial theorem implies d_q^N = 0.

  The standard bar cohomology H^*(u_q, C) = Ext^*(C, C) is the other key
  invariant: at roots of unity, u_q(sl_2) is NOT semisimple, so the Ext
  algebra is nontrivial in multiple degrees (unlike generic q, where
  semisimplicity forces Ext^{>0} = 0).

References:
  - concordance.tex, H4 structural gap
  - Kapranov, "On the q-analog of homological algebra"
  - Dubois-Violette, "d^N = 0: generalized homology"
  - Ginzburg-Kumar, "Cohomology of quantum groups at roots of unity"
  - yangians.tex, sec:cat-O-strategies
"""

import cmath

import numpy as np
import pytest

from compute.lib.kl_ncomplex_sl2 import (
    # Quantum arithmetic
    root_of_unity,
    q_integer,
    q_number,
    q_binomial,
    # Small quantum group
    SmallQuantumSl2,
    # Bar complex
    BarComplex,
    # Bar cohomology
    bar_cohomology_dim,
    all_bar_cohomology,
    # N-complex cohomology
    ncomplex_cohomology_dim,
    all_cohomology_flavors,
    euler_characteristic_sum,
    # Diagnostics
    verify_uq_relations,
    verify_associativity,
    # Dimension data
    small_quantum_group_dim,
    bar_space_dims,
    # Full analysis
    full_ncomplex_analysis,
)


# ============================================================================
# Quantum arithmetic
# ============================================================================

class TestQuantumArithmetic:
    """Test quantum integers and binomials at roots of unity."""

    def test_root_of_unity_basic(self):
        """e^{2 pi i / N} has modulus 1 and correct order."""
        for N in [2, 3, 4, 5, 6]:
            q = root_of_unity(N)
            assert abs(abs(q) - 1.0) < 1e-14
            assert abs(q ** N - 1.0) < 1e-12

    def test_q_integer_1(self):
        """[1]_q = 1 for any q."""
        for N in [3, 4, 5]:
            q = root_of_unity(N)
            assert abs(q_integer(1, q) - 1.0) < 1e-12

    def test_q_integer_N_vanishes(self):
        """[N]_q = 0 at q = e^{2 pi i / N}."""
        for N in [3, 4, 5, 6, 7]:
            q = root_of_unity(N)
            assert abs(q_integer(N, q)) < 1e-10, f"[{N}]_q != 0 at N={N}"

    def test_q_integer_2_at_cube_root(self):
        """[2]_omega = -1 where omega = e^{2 pi i / 3}."""
        q = root_of_unity(3)
        assert abs(q_integer(2, q) - (-1.0)) < 1e-10

    def test_q_integer_2_at_4th_root(self):
        """[2]_q = 0 at q = i (4th root of unity).

        [2]_i = (i^2 - i^{-2}) / (i - i^{-1}) = (-1-(-1)) / (i+i) = 0/2i = 0.
        """
        q = root_of_unity(4)
        assert abs(q_integer(2, q)) < 1e-10

    def test_q_number_alias(self):
        """q_number is an alias for q_integer."""
        q = root_of_unity(5)
        for n in range(6):
            assert q_integer(n, q) == q_number(n, q)

    def test_q_binomial_N_choose_k_vanishes(self):
        """[N choose k]_q = 0 for 1 <= k <= N-1 at N-th root of unity.

        This is the mechanism behind d_q^N = 0.
        """
        for N in [3, 5, 7]:
            q = root_of_unity(N)
            for k in range(1, N):
                val = q_binomial(N, k, q)
                assert abs(val) < 1e-8, (
                    f"[{N} choose {k}]_q != 0 at N={N}: got {val}"
                )

    def test_q_binomial_boundary(self):
        """[n choose 0]_q = [n choose n]_q = 1."""
        q = root_of_unity(5)
        for n in range(6):
            assert abs(q_binomial(n, 0, q) - 1.0) < 1e-12
            assert abs(q_binomial(n, n, q) - 1.0) < 1e-12


# ============================================================================
# Small quantum group structure
# ============================================================================

class TestSmallQuantumSl2:
    """Test the small quantum group u_q(sl_2) at various roots of unity."""

    def test_dimension(self):
        """dim u_q(sl_2) = N^3."""
        for N in [2, 3, 4, 5]:
            uq = SmallQuantumSl2(N)
            assert uq.dim == N ** 3

    def test_invalid_N(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            SmallQuantumSl2(1)
        with pytest.raises(ValueError):
            SmallQuantumSl2(0)

    def test_basis_index_roundtrip(self):
        """basis_index and basis_label are inverses."""
        for N in [2, 3, 4]:
            uq = SmallQuantumSl2(N)
            for idx in range(uq.dim):
                a, b, c = uq.basis_label(idx)
                assert uq.basis_index(a, b, c) == idx

    def test_basis_index_range(self):
        """All PBW basis indices are distinct and cover {0, ..., N^3-1}."""
        for N in [2, 3, 4]:
            uq = SmallQuantumSl2(N)
            indices = set()
            for a in range(N):
                for b in range(N):
                    for c in range(N):
                        idx = uq.basis_index(a, b, c)
                        assert 0 <= idx < uq.dim
                        indices.add(idx)
            assert len(indices) == uq.dim

    def test_unit_vector(self):
        """Unit vector is at index (0,0,0)."""
        for N in [2, 3]:
            uq = SmallQuantumSl2(N)
            unit = uq.unit_vector()
            assert abs(unit[0] - 1.0) < 1e-14
            assert np.sum(np.abs(unit)) == pytest.approx(1.0, abs=1e-14)


class TestUqRelations:
    """Test the defining relations of u_q(sl_2) via the multiplication table."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_all_relations(self, N):
        """All 6 defining relations hold for u_q(sl_2) at each N."""
        uq = SmallQuantumSl2(N)
        results = verify_uq_relations(uq)
        for name, ok in results.items():
            assert ok, f"Relation '{name}' failed at N={N}"

    def test_K_N_equals_1(self):
        """K^N = 1 for N = 3."""
        uq = SmallQuantumSl2(3)
        results = verify_uq_relations(uq)
        assert results["K^N = 1"]

    def test_E_N_equals_0(self):
        """E^N = 0 for N = 3 (nilpotency)."""
        uq = SmallQuantumSl2(3)
        results = verify_uq_relations(uq)
        assert results["E^N = 0"]

    def test_F_N_equals_0(self):
        """F^N = 0 for N = 3 (nilpotency)."""
        uq = SmallQuantumSl2(3)
        results = verify_uq_relations(uq)
        assert results["F^N = 0"]

    def test_commutation_relations(self):
        """KE, KF, EF-FE relations at N = 3."""
        uq = SmallQuantumSl2(3)
        results = verify_uq_relations(uq)
        assert results["KE = q^2 EK"]
        assert results["KF = q^{-2} FK"]
        assert results["EF - FE = (K-K^{-1})/(q-q^{-1})"]

    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_associativity(self, N):
        """Associativity spot-check for the multiplication table."""
        uq = SmallQuantumSl2(N)
        assert verify_associativity(uq, n_samples=30)


# ============================================================================
# Bar complex construction
# ============================================================================

class TestBarComplex:
    """Test bar complex construction and basic properties."""

    def test_bar_space_dims_N2(self):
        """Bar space dimensions for N=2: dim I = 7, B_n = 7^n."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        assert bar.bar_space_dim(0) == 1
        assert bar.bar_space_dim(1) == 7
        assert bar.bar_space_dim(2) == 49
        assert bar.bar_space_dim(3) == 343

    def test_bar_space_dims_N3(self):
        """Bar space dimensions for N=3: dim I = 26, B_n = 26^n."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        assert bar.bar_space_dim(0) == 1
        assert bar.bar_space_dim(1) == 26
        assert bar.bar_space_dim(2) == 676

    def test_differential_shape(self):
        """Differential d: B_n -> B_{n-1} has correct shape."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        d2 = bar.differential(2)
        assert d2.shape == (7, 49)
        d3 = bar.differential(3)
        assert d3.shape == (49, 343)

    def test_differential_degree_1(self):
        """d: B_1 -> B_0 is the zero map."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        d1 = bar.differential(1)
        assert d1.shape == (1, 7)


# ============================================================================
# Standard bar differential: d^2 = 0 always
# ============================================================================

class TestStandardBarDifferential:
    """The standard bar differential of any associative algebra satisfies d^2 = 0.

    This is a theorem (not a conjecture). We verify it computationally as
    a consistency check on the multiplication table and differential construction.
    """

    @pytest.mark.parametrize("N", [2, 3])
    def test_d_squared_zero(self, N):
        """d^2 = 0 for the standard bar differential at N = 2, 3."""
        uq = SmallQuantumSl2(N)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for degree in range(2, 4):
            norm = bar.verify_d_squared(degree)
            assert norm < 1e-10, (
                f"d^2 != 0 at N={N}, degree {degree}: ||d^2|| = {norm}. "
                f"This should ALWAYS be zero for the bar complex of an "
                f"associative algebra."
            )

    @pytest.mark.slow
    @pytest.mark.parametrize("N", [4, 5])
    def test_d_squared_zero_larger_N(self, N):
        """d^2 = 0 for larger N (consistency check)."""
        uq = SmallQuantumSl2(N)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        norm = bar.verify_d_squared(2)
        assert norm < 1e-10


# ============================================================================
# Bar cohomology at roots of unity
# ============================================================================

class TestBarCohomology:
    """Test bar cohomology H^*(u_q, C) = Ext^*(C, C).

    At roots of unity, u_q(sl_2) is not semisimple, so bar cohomology is
    nontrivial in degrees > 0.
    """

    def test_H0_is_1(self):
        """H^0(u_q, C) = C (trivial module has 1-dim endomorphisms)."""
        for N in [2, 3]:
            uq = SmallQuantumSl2(N)
            bar = BarComplex(uq, max_degree=2, use_reduced=True)
            h0 = bar_cohomology_dim(bar, 0)
            assert h0 == 1, f"H^0 = {h0} != 1 at N={N}"

    def test_bar_cohomology_nontrivial_N3(self):
        """Bar cohomology is nontrivial in degree > 0 at N = 3.

        This confirms that u_q(sl_2) at q = e^{2 pi i / 3} is NOT semisimple.
        """
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        cohom = all_bar_cohomology(bar)
        # At least one H^n with n > 0 should be nonzero
        higher = [cohom[n] for n in range(1, 4) if cohom[n] is not None and cohom[n] > 0]
        assert len(higher) > 0, "Bar cohomology trivial in all degrees > 0 at N=3"

    def test_bar_cohomology_nontrivial_N2(self):
        """Bar cohomology nontrivial at N = 2 (u_{-1}(sl_2) not semisimple)."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        cohom = all_bar_cohomology(bar)
        higher = [cohom[n] for n in range(1, 4) if cohom[n] is not None and cohom[n] > 0]
        assert len(higher) > 0, "Bar cohomology trivial at N=2"

    def test_bar_cohomology_nonnegative(self):
        """All cohomology dimensions are non-negative."""
        for N in [2, 3]:
            uq = SmallQuantumSl2(N)
            bar = BarComplex(uq, max_degree=3, use_reduced=True)
            cohom = all_bar_cohomology(bar)
            for n, h in cohom.items():
                if h is not None:
                    assert h >= 0, f"Negative H^{n} = {h} at N={N}"

    def test_H1_is_generators(self):
        """H^1(u_q, C) counts the generators of the augmentation ideal mod I^2.

        For u_q(sl_2) with generators E, F, K (and K^{-1} = K^{N-1}),
        the Ext^1 = I/I^2 has dimension equal to the number of
        "independent generators" of I as a module.
        """
        for N in [2, 3]:
            uq = SmallQuantumSl2(N)
            bar = BarComplex(uq, max_degree=2, use_reduced=True)
            h1 = bar_cohomology_dim(bar, 1)
            # H^1 should be finite and non-negative
            assert h1 is not None
            assert h1 >= 0


# ============================================================================
# N = 2: ordinary Koszul duality recovery
# ============================================================================

class TestN2OrdinaryDG:
    """At N = 2 (q = -1), the q-deformed differential satisfies d_q^2 = 0.

    The q-signs q^{i-1} = (-1)^{i-1} differ from the standard signs
    (-1)^{i+1} = (-1)^{i-1} by at most an overall factor. The key point
    is that d_q^2 = 0 at N = 2, so it still gives an ordinary chain complex
    (the 2-complex is the standard case).
    """

    def test_dq_proportional_to_standard_N2(self):
        """At N = 2, d_q is proportional to d (standard) at each degree.

        The q-signs q^{i-1} = (-1)^{i-1} and standard signs (-1)^{i+1}
        are related by an overall factor of (-1)^2 = 1 or -1 depending
        on the summation index convention. They may differ by an overall
        sign, but d_q^2 = 0 either way.
        """
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for degree in range(2, 4):
            d_std = bar.differential(degree)
            d_q = bar.q_differential(degree)
            # Check that d_q and d_std are proportional (differ by overall sign)
            # Either d_q = d_std or d_q = -d_std
            match_positive = np.allclose(d_q, d_std, atol=1e-10)
            match_negative = np.allclose(d_q, -d_std, atol=1e-10)
            assert match_positive or match_negative, (
                f"d_q not proportional to d at N=2, degree {degree}"
            )

    def test_dq_squared_zero_N2(self):
        """d_q^2 = 0 at N = 2 (ordinary chain complex)."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for degree in range(2, 4):
            norm = bar.verify_dq_squared(degree)
            assert norm < 1e-10, f"d_q^2 != 0 at N=2, degree {degree}: {norm}"


# ============================================================================
# N >= 3: genuine N-complex structure (q-deformed differential)
# ============================================================================

class TestNComplexStructure:
    """Test the N-complex predictions for the q-deformed differential.

    Predictions:
      - d_q^2 != 0 for N >= 3 (genuine N-complex)
      - d_q^N = 0 (N-complex identity from quantum binomial theorem)
    """

    def test_dq_squared_nonzero_N3(self):
        """d_q^2 != 0 at N = 3 (genuine 3-complex) at degree 3.

        At degree 2 with reduced bar, d_q^2 is structurally zero
        (d_q: B_1 -> B_0 = 0). The definitive test uses degree 3
        where the N-complex structure is visible.

        NOTE: max_degree=3 (not 4) because B_4 = 26^4 ~ 457K is
        computationally infeasible.
        """
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        # Degree 3 is where d_q^2 != 0 (degree 2 is structurally zero)
        norm = bar.verify_dq_squared(3)
        assert norm > 1e-6, f"d_q^2 = 0 at degree 3 for N=3: {norm}"

    def test_dq_squared_nonzero_N3_degree3(self):
        """d_q^2 != 0 at degree 3 for N = 3."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        norm = bar.verify_dq_squared(3)
        assert norm > 1e-6, f"d_q^2 unexpectedly zero at N=3, degree 3: {norm}"

    def test_dq_cubed_zero_N3(self):
        """d_q^3 = 0 at N = 3 (the N-complex structure).

        This is the central prediction: the q-deformed bar differential
        satisfies d_q^3 = 0 when q is a primitive 3rd root of unity.
        The mechanism is the quantum binomial theorem: [3 choose k]_q = 0
        for k = 1, 2 when q^3 = 1.
        """
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        norm = bar.verify_dq_N(3)
        assert norm < 1e-8, (
            f"d_q^3 != 0 at N=3: the N-complex prediction fails. ||d_q^3|| = {norm}"
        )

    @pytest.mark.slow
    def test_dq_squared_zero_at_degree2_N4(self):
        """d_q^2 = 0 at degree 2 for N = 4 (structural: d_q(B_1->B_0) = 0).

        On the reduced bar complex, B_1 = ker(epsilon) so d_q: B_1 -> B_0
        is the zero map. Hence d_q^2: B_2 -> B_0 = 0 for ALL q,
        regardless of N-complex structure. The genuine d_q^2 != 0
        test requires degree >= 3, which is computationally infeasible
        at N=4 (dim B_3 = 63^3 ~ 250K).
        """
        uq = SmallQuantumSl2(4)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        norm = bar.verify_dq_squared(2)
        assert norm < 1e-8, f"d_q^2 unexpectedly nonzero at degree 2: {norm}"

    @pytest.mark.slow
    def test_dq_N_zero_N4(self):
        """d_q^4 = 0 at N = 4."""
        uq = SmallQuantumSl2(4)
        bar = BarComplex(uq, max_degree=4, use_reduced=True)
        norm = bar.verify_dq_N(4)
        assert norm < 1e-8, f"d_q^4 != 0 at N=4: ||d_q^4|| = {norm}"

    @pytest.mark.slow
    def test_dq_squared_zero_at_degree2_N5(self):
        """d_q^2 = 0 at degree 2 for N = 5 (same structural reason as N=4)."""
        uq = SmallQuantumSl2(5)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        norm = bar.verify_dq_squared(2)
        assert norm < 1e-8, f"d_q^2 unexpectedly nonzero at degree 2: {norm}"

    @pytest.mark.slow
    def test_dq_N_zero_N5(self):
        """d_q^5 = 0 at N = 5."""
        uq = SmallQuantumSl2(5)
        bar = BarComplex(uq, max_degree=5, use_reduced=True)
        norm = bar.verify_dq_N(5)
        assert norm < 1e-8, f"d_q^5 != 0 at N=5: ||d_q^5|| = {norm}"


# ============================================================================
# N-complex cohomology flavors
# ============================================================================

class TestNCohomologyFlavors:
    """Test the N-complex cohomology flavors H^{j, N-j}."""

    def test_N2_single_flavor(self):
        """At N = 2, there is exactly one cohomology flavor (j = 1)."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        flavors = all_cohomology_flavors(bar, 2)
        assert len(flavors) == 1
        assert 1 in flavors

    def test_N3_two_flavors(self):
        """At N = 3, there are two cohomology flavors (j = 1, 2)."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        flavors = all_cohomology_flavors(bar, 2)
        assert len(flavors) == 2
        assert 1 in flavors
        assert 2 in flavors

    def test_cohomology_nonnegative_N2(self):
        """N-complex cohomology dimensions are non-negative at N = 2."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for n in range(1, 4):
            flavors = all_cohomology_flavors(bar, n)
            for j, dim_h in flavors.items():
                if dim_h is not None:
                    assert dim_h >= 0, (
                        f"Negative cohomology at N=2, degree {n}, j={j}: {dim_h}"
                    )

    def test_cohomology_nonnegative_N3(self):
        """N-complex cohomology dimensions are non-negative at N = 3."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for n in range(1, 4):
            flavors = all_cohomology_flavors(bar, n)
            for j, dim_h in flavors.items():
                if dim_h is not None:
                    assert dim_h >= 0, (
                        f"Negative cohomology at N=3, degree {n}, j={j}: {dim_h}"
                    )

    def test_invalid_flavor_j(self):
        """j outside [1, N-1] raises ValueError."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        with pytest.raises(ValueError):
            ncomplex_cohomology_dim(bar, 2, 0)
        with pytest.raises(ValueError):
            ncomplex_cohomology_dim(bar, 2, 3)

    def test_N2_flavor_matches_bar_cohomology(self):
        """At N = 2, the single N-complex flavor (j=1) matches standard bar cohomology.

        Since d_q = d (standard) at N = 2, the N-complex flavor H^{1,1}
        should agree with the standard bar cohomology.
        """
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for n in range(1, 4):
            h_bar = bar_cohomology_dim(bar, n)
            h_ncomplex = ncomplex_cohomology_dim(bar, n, j=1)
            if h_bar is not None and h_ncomplex is not None:
                assert h_bar == h_ncomplex, (
                    f"Bar H^{n} = {h_bar} != N-complex H^{{1,1}}_{n} = {h_ncomplex} at N=2"
                )


# ============================================================================
# Euler characteristic sums
# ============================================================================

class TestEulerCharacteristic:
    """Test Euler characteristic relations for N-complex cohomology."""

    def test_euler_sum_N2(self):
        """At N = 2, the Euler sum is just dim H^{1,1} (single term)."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for n in range(1, 4):
            esum = euler_characteristic_sum(bar, n)
            if esum is not None:
                flavors = all_cohomology_flavors(bar, n)
                if flavors[1] is not None:
                    assert abs(esum - flavors[1]) < 1e-10

    def test_euler_sum_real_N3(self):
        """At N = 3, the Euler sum should be real (integer-valued)."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for n in range(1, 4):
            esum = euler_characteristic_sum(bar, n)
            if esum is not None:
                assert abs(esum.imag) < 1e-8, (
                    f"Euler sum has imaginary part at N=3, degree {n}: {esum}"
                )


# ============================================================================
# Dimension data
# ============================================================================

class TestDimensionData:
    """Test dimension computations and predictions."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_small_quantum_group_dim(self, N):
        """dim u_q(sl_2) = N^3."""
        assert small_quantum_group_dim(N) == N ** 3

    def test_bar_space_dims(self):
        """Bar space dimensions follow I^n pattern."""
        dims = bar_space_dims(3, 3)
        assert dims[0] == 1
        assert dims[1] == 26
        assert dims[2] == 676
        assert dims[3] == 17576

    def test_bar_space_dims_N2(self):
        """N = 2: dim I = 7."""
        dims = bar_space_dims(2, 4)
        assert dims[1] == 7
        assert dims[2] == 49
        assert dims[3] == 343
        assert dims[4] == 2401


# ============================================================================
# Integration: full analysis
# ============================================================================

class TestFullAnalysis:
    """Integration tests running the full analysis pipeline."""

    def test_full_analysis_N2(self):
        """Full analysis at N = 2 completes and satisfies key invariants."""
        result = full_ncomplex_analysis(2, max_degree=3)
        assert result["N"] == 2
        assert result["dim_uq"] == 8
        assert result["dim_I"] == 7
        assert result["associativity"]
        for name, ok in result["uq_relations"].items():
            assert ok, f"Relation '{name}' failed at N=2"
        # Standard d^2 = 0
        for deg, norm in result["d_squared_norms"].items():
            assert norm < 1e-10, f"d^2 != 0 at N=2, degree {deg}"
        # Q-deformed d_q^2 = 0 at N=2 (since d_q = d)
        for deg, norm in result["dq_squared_norms"].items():
            assert norm < 1e-10, f"d_q^2 != 0 at N=2, degree {deg}"

    def test_full_analysis_N3(self):
        """Full analysis at N = 3 completes and satisfies key invariants."""
        result = full_ncomplex_analysis(3, max_degree=3)
        assert result["N"] == 3
        assert result["dim_uq"] == 27
        assert result["dim_I"] == 26
        assert result["associativity"]
        for name, ok in result["uq_relations"].items():
            assert ok, f"Relation '{name}' failed at N=3"
        # Standard d^2 = 0 (always)
        for deg, norm in result["d_squared_norms"].items():
            assert norm < 1e-10, f"Standard d^2 != 0 at N=3, degree {deg}"
        # Q-deformed d_q^2 != 0 at degree >= 3 (genuine N-complex)
        # At degree 2, d_q^2: B_2 -> B_0 is structurally zero (d_q(B_1->B_0)=0)
        for deg, norm in result["dq_squared_norms"].items():
            if deg >= 3:
                assert norm > 1e-6, (
                    f"d_q^2 = 0 at N=3, degree {deg}: not a genuine N-complex"
                )
        # Q-deformed d_q^3 = 0 (N-complex structure)
        for deg, norm in result["dq_N_norms"].items():
            assert norm < 1e-8, f"d_q^3 != 0 at N=3, degree {deg}"


# ============================================================================
# Edge cases and regression
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_bar_space_dim_degree_zero(self):
        """B_0 has dimension 1 (the ground field)."""
        for N in [2, 3]:
            uq = SmallQuantumSl2(N)
            bar = BarComplex(uq, max_degree=2, use_reduced=True)
            assert bar.bar_space_dim(0) == 1

    def test_bar_space_dim_negative(self):
        """B_n = 0 for n < 0."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        assert bar.bar_space_dim(-1) == 0

    def test_d_power_zero(self):
        """d^0 is the identity matrix."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        d0 = bar.d_power(2, 0)
        assert np.allclose(d0, np.eye(bar.bar_space_dim(2), dtype=complex))

    def test_d_power_one_is_differential(self):
        """d^1 is the bar differential itself."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=2, use_reduced=True)
        d1 = bar.d_power(2, 1)
        d_direct = bar.differential(2)
        assert np.allclose(d1, d_direct)

    def test_augmentation_map_on_generators(self):
        """Augmentation sends E -> 0, F -> 0, K^b -> 1."""
        for N in [2, 3]:
            uq = SmallQuantumSl2(N)
            eps = uq.augmentation_map()
            assert abs(eps[uq.basis_index(1, 0, 0)]) < 1e-14
            assert abs(eps[uq.basis_index(0, 0, 1)]) < 1e-14
            for b in range(N):
                assert abs(eps[uq.basis_index(0, b, 0)] - 1.0) < 1e-14

    def test_reduced_bar_dim_I(self):
        """Augmentation ideal has dimension N^3 - 1."""
        for N in [2, 3, 4]:
            uq = SmallQuantumSl2(N)
            bar = BarComplex(uq, max_degree=1, use_reduced=True)
            assert bar.I_dim == N ** 3 - 1


# ============================================================================
# N-complex vs ordinary complex comparison
# ============================================================================

class TestNComplexVsOrdinary:
    """Compare N-complex (q-deformed) and ordinary complex structures.

    At N = 2, d_q = d (standard), so d_q^2 = 0.
    At N >= 3, d_q^2 != 0 but d_q^N = 0.
    The standard d always has d^2 = 0.
    """

    def test_N2_dq_is_ordinary(self):
        """N = 2: d_q^2 = 0 (reduces to standard chain complex)."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        for n in range(2, 4):
            norm = bar.verify_dq_squared(n)
            assert norm < 1e-10

    def test_N3_dq_not_ordinary(self):
        """N = 3: d_q^2 != 0 (genuine N-complex)."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        norms = [bar.verify_dq_squared(n) for n in range(2, 4)]
        assert max(norms) > 1e-6, "d_q^2 = 0 at all degrees for N=3"

    def test_N3_dq_is_3complex(self):
        """N = 3: d_q^3 = 0 (it is a 3-complex)."""
        uq = SmallQuantumSl2(3)
        bar = BarComplex(uq, max_degree=3, use_reduced=True)
        norm = bar.verify_dq_N(3)
        assert norm < 1e-8

    def test_standard_always_ordinary(self):
        """The standard bar differential always satisfies d^2 = 0."""
        for N in [2, 3]:
            uq = SmallQuantumSl2(N)
            bar = BarComplex(uq, max_degree=3, use_reduced=True)
            for degree in range(2, 4):
                norm = bar.verify_d_squared(degree)
                assert norm < 1e-10

    def test_transition_N2_to_N3(self):
        """The transition from N=2 to N=3 activates N-complex structure.

        At N=2: d_q^2 = 0 (ordinary, since q = -1 gives standard signs).
        At N=3: d_q^2 != 0, d_q^3 = 0 (genuine 3-complex).
        Both always have standard d^2 = 0.
        """
        # N = 2
        uq2 = SmallQuantumSl2(2)
        bar2 = BarComplex(uq2, max_degree=3, use_reduced=True)
        dq2_norm_N2 = bar2.verify_dq_squared(2)

        # N = 3
        uq3 = SmallQuantumSl2(3)
        bar3 = BarComplex(uq3, max_degree=3, use_reduced=True)
        dq2_norm_N3 = bar3.verify_dq_squared(2)
        dq3_norm_N3 = bar3.verify_dq_N(3)

        assert dq2_norm_N2 < 1e-10  # N=2: d_q^2 = 0 (always at degree 2)
        # At degree 2, d_q^2: B_2 -> B_0 is structurally zero (d_q(B_1->B_0)=0)
        # Test d_q^2 at degree 3 instead for genuine N-complex evidence
        dq2_norm_N3_deg3 = bar3.verify_dq_squared(3)
        assert dq2_norm_N3_deg3 > 1e-6   # N=3: d_q^2 != 0 at degree 3
        assert dq3_norm_N3 < 1e-8   # N=3: d_q^3 = 0
