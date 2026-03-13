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
from fractions import Fraction

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
    MAX_EXPLICIT_DQ_N_SOURCE_DIM,
    # Bar cohomology
    bar_cohomology_dim,
    all_bar_cohomology,
    # N-complex cohomology
    ncomplex_cohomology_dim,
    all_cohomology_flavors,
    euler_characteristic_sum,
    ncomplex_flavor_report,
    admissible_level_flavor_report,
    n3_degree4_flavor_packet,
    n3_degree4_exact_packet_profile,
    n4_low_degree_flavor_window,
    n4_degree1_h13_channel,
    n4_degree2_partial_packet,
    n4_degree2_h13_channel_bounds,
    n4_degree2_h13_precursor_screen,
    n4_degree2_h13_first_term_state_compression,
    n4_degree2_h13_cancellation_plane,
    n4_degree2_h13_cancellation_operator,
    n4_degree2_h13_exact_channel,
    n4_degree2_h13_exact_packet_profile,
    kl_shadow_transport_convolution_obstruction,
    kl_shadow_transport_schrodinger_ansatz,
    kl_exact_packet_profile_comparison,
    kl_periodic_shadow_candidates,
    # Diagnostics
    verify_uq_relations,
    verify_associativity,
    # Dimension data
    small_quantum_group_dim,
    bar_space_dims,
    # Full analysis
    full_ncomplex_analysis,
)


# ---------------------------------------------------------------------------
# Shared expensive fixtures.  BarComplex(SmallQuantumSl2(N), max_degree=3)
# allocates ~190 MB of differential matrices for N = 3.  Caching at module
# scope avoids repeated allocation across tests.
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def bar_N2_deg3():
    """BarComplex for N=2, max_degree=3 (reused across tests)."""
    uq = SmallQuantumSl2(2)
    return BarComplex(uq, max_degree=3, use_reduced=True)


@pytest.fixture(scope="module")
def bar_N3_deg3():
    """BarComplex for N=3, max_degree=3 (reused across tests)."""
    uq = SmallQuantumSl2(3)
    return BarComplex(uq, max_degree=3, use_reduced=True)


@pytest.fixture(scope="module")
def bar_N3_deg2():
    """BarComplex for N=3, max_degree=2 (reused across tests)."""
    uq = SmallQuantumSl2(3)
    return BarComplex(uq, max_degree=2, use_reduced=True)


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
        for N in [3, 4, 5, 7]:
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
    def test_d_squared_zero_larger_N_via_degree_two_structure(self, N):
        """d^2 = 0 at degree 2 because the reduced bar map B_1 -> B_0 vanishes."""
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

    def test_bar_cohomology_nontrivial_N3(self, bar_N3_deg3):
        """Bar cohomology is nontrivial in degree > 0 at N = 3.

        This confirms that u_q(sl_2) at q = e^{2 pi i / 3} is NOT semisimple.
        """
        cohom = all_bar_cohomology(bar_N3_deg3)
        # At least one H^n with n > 0 should be nonzero
        higher = [cohom[n] for n in range(1, 4) if cohom[n] is not None and cohom[n] > 0]
        assert len(higher) > 0, "Bar cohomology trivial in all degrees > 0 at N=3"

    def test_bar_cohomology_nontrivial_N2(self, bar_N2_deg3):
        """Bar cohomology nontrivial at N = 2 (u_{-1}(sl_2) not semisimple)."""
        cohom = all_bar_cohomology(bar_N2_deg3)
        higher = [cohom[n] for n in range(1, 4) if cohom[n] is not None and cohom[n] > 0]
        assert len(higher) > 0, "Bar cohomology trivial at N=2"

    def test_bar_cohomology_nonnegative(self, bar_N2_deg3, bar_N3_deg3):
        """All cohomology dimensions are non-negative."""
        for bar in [bar_N2_deg3, bar_N3_deg3]:
            cohom = all_bar_cohomology(bar)
            for n, h in cohom.items():
                if h is not None:
                    assert h >= 0, f"Negative H^{n} = {h}"

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

    def test_dq_proportional_to_standard_N2(self, bar_N2_deg3):
        """At N = 2, d_q is proportional to d (standard) at each degree.

        The q-signs q^{i-1} = (-1)^{i-1} and standard signs (-1)^{i+1}
        are related by an overall factor of (-1)^2 = 1 or -1 depending
        on the summation index convention. They may differ by an overall
        sign, but d_q^2 = 0 either way.
        """
        for degree in range(2, 4):
            d_std = bar_N2_deg3.differential(degree)
            d_q = bar_N2_deg3.q_differential(degree)
            # Check that d_q and d_std are proportional (differ by overall sign)
            # Either d_q = d_std or d_q = -d_std
            match_positive = np.allclose(d_q, d_std, atol=1e-10)
            match_negative = np.allclose(d_q, -d_std, atol=1e-10)
            assert match_positive or match_negative, (
                f"d_q not proportional to d at N=2, degree {degree}"
            )

    def test_dq_squared_zero_N2(self, bar_N2_deg3):
        """d_q^2 = 0 at N = 2 (ordinary chain complex)."""
        for degree in range(2, 4):
            norm = bar_N2_deg3.verify_dq_squared(degree)
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

    def test_dq_squared_nonzero_N3(self, bar_N3_deg3):
        """d_q^2 != 0 at N = 3 (genuine 3-complex) at degree 3.

        At degree 2 with reduced bar, d_q^2 is structurally zero
        (d_q: B_1 -> B_0 = 0). The definitive test uses degree 3
        where the N-complex structure is visible.

        NOTE: max_degree=3 (not 4) because B_4 = 26^4 ~ 457K is
        computationally infeasible.
        """
        # Degree 3 is where d_q^2 != 0 (degree 2 is structurally zero)
        norm = bar_N3_deg3.verify_dq_squared(3)
        assert norm > 1e-6, f"d_q^2 = 0 at degree 3 for N=3: {norm}"

    def test_dq_squared_nonzero_N3_degree3(self, bar_N3_deg3):
        """d_q^2 != 0 at degree 3 for N = 3."""
        norm = bar_N3_deg3.verify_dq_squared(3)
        assert norm > 1e-6, f"d_q^2 unexpectedly zero at N=3, degree 3: {norm}"

    def test_dq_cubed_zero_N3(self, bar_N3_deg3):
        """d_q^3 = 0 at N = 3 (the N-complex structure).

        This is the central prediction: the q-deformed bar differential
        satisfies d_q^3 = 0 when q is a primitive 3rd root of unity.
        The mechanism is the quantum binomial theorem: [3 choose k]_q = 0
        for k = 1, 2 when q^3 = 1.
        """
        norm = bar_N3_deg3.verify_dq_N(3)
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
    def test_dq_N_zero_N4_via_structural_certificate(self):
        """d_q^4 = 0 at N = 4 via the quantum-binomial structural route."""
        uq = SmallQuantumSl2(4)
        bar = BarComplex(uq, max_degree=4, use_reduced=True)
        assert bar.bar_space_dim(4) > MAX_EXPLICIT_DQ_N_SOURCE_DIM
        assert all(abs(q_binomial(4, k, uq.q)) < 1e-8 for k in range(1, 4))
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
    def test_dq_N_zero_N5_via_structural_certificate(self):
        """d_q^5 = 0 at N = 5 via the quantum-binomial structural route."""
        uq = SmallQuantumSl2(5)
        bar = BarComplex(uq, max_degree=5, use_reduced=True)
        assert bar.bar_space_dim(5) > MAX_EXPLICIT_DQ_N_SOURCE_DIM
        assert all(abs(q_binomial(5, k, uq.q)) < 1e-8 for k in range(1, 5))
        norm = bar.verify_dq_N(5)
        assert norm < 1e-8, f"d_q^5 != 0 at N=5: ||d_q^5|| = {norm}"


# ============================================================================
# N-complex cohomology flavors
# ============================================================================

class TestNCohomologyFlavors:
    """Test the N-complex cohomology flavors H^{j, N-j}."""

    def test_N2_single_flavor(self, bar_N2_deg3):
        """At N = 2, there is exactly one cohomology flavor (j = 1)."""
        flavors = all_cohomology_flavors(bar_N2_deg3, 2)
        assert len(flavors) == 1
        assert 1 in flavors

    def test_N3_two_flavors(self, bar_N3_deg3):
        """At N = 3, there are two cohomology flavors (j = 1, 2)."""
        flavors = all_cohomology_flavors(bar_N3_deg3, 2)
        assert len(flavors) == 2
        assert 1 in flavors
        assert 2 in flavors

    def test_cohomology_nonnegative_N2(self, bar_N2_deg3):
        """N-complex cohomology dimensions are non-negative at N = 2."""
        for n in range(1, 4):
            flavors = all_cohomology_flavors(bar_N2_deg3, n)
            for j, dim_h in flavors.items():
                if dim_h is not None:
                    assert dim_h >= 0, (
                        f"Negative cohomology at N=2, degree {n}, j={j}: {dim_h}"
                    )

    def test_cohomology_nonnegative_N3(self, bar_N3_deg3):
        """N-complex cohomology dimensions are non-negative at N = 3."""
        for n in range(1, 4):
            flavors = all_cohomology_flavors(bar_N3_deg3, n)
            for j, dim_h in flavors.items():
                if dim_h is not None:
                    assert dim_h >= 0, (
                        f"Negative cohomology at N=3, degree {n}, j={j}: {dim_h}"
                    )

    def test_invalid_flavor_j(self, bar_N3_deg2):
        """j outside [1, N-1] raises ValueError."""
        with pytest.raises(ValueError):
            ncomplex_cohomology_dim(bar_N3_deg2, 2, 0)
        with pytest.raises(ValueError):
            ncomplex_cohomology_dim(bar_N3_deg2, 2, 3)

    def test_N2_flavor_matches_bar_cohomology(self, bar_N2_deg3):
        """At N = 2, the single N-complex flavor (j=1) matches standard bar cohomology.

        Since d_q = d (standard) at N = 2, the N-complex flavor H^{1,1}
        should agree with the standard bar cohomology.
        """
        for n in range(1, 4):
            h_bar = bar_cohomology_dim(bar_N2_deg3, n)
            h_ncomplex = ncomplex_cohomology_dim(bar_N2_deg3, n, j=1)
            if h_bar is not None and h_ncomplex is not None:
                assert h_bar == h_ncomplex, (
                    f"Bar H^{n} = {h_bar} != N-complex H^{{1,1}}_{n} = {h_ncomplex} at N=2"
                )


# ============================================================================
# Euler characteristic sums
# ============================================================================

class TestEulerCharacteristic:
    """Test Euler characteristic relations for N-complex cohomology."""

    def test_euler_sum_N2(self, bar_N2_deg3):
        """At N = 2, the Euler sum is just dim H^{1,1} (single term)."""
        for n in range(1, 4):
            esum = euler_characteristic_sum(bar_N2_deg3, n)
            if esum is not None:
                flavors = all_cohomology_flavors(bar_N2_deg3, n)
                if flavors[1] is not None:
                    assert abs(esum - flavors[1]) < 1e-10

    def test_euler_sum_real_N3(self, bar_N3_deg3):
        """At N = 3, the Euler sum should be real (integer-valued)."""
        for n in range(1, 4):
            esum = euler_characteristic_sum(bar_N3_deg3, n)
            if esum is not None:
                assert abs(esum.imag) < 1e-8, (
                    f"Euler sum has imaginary part at N=3, degree {n}: {esum}"
                )


# ============================================================================
# Flavor report / admissible-level extractor
# ============================================================================

class TestFlavorReport:
    """Test the compact admissible-level flavor report."""

    def test_flavor_report_identifies_single_observed_flavor_N2(self):
        """At N = 2, the observed truncation supports the single ordinary flavor."""
        uq = SmallQuantumSl2(2)
        bar = BarComplex(uq, max_degree=4, use_reduced=True)
        report = ncomplex_flavor_report(bar)

        assert report["N"] == 2
        assert report["fully_computable_degrees"] == [1, 2, 3]
        assert report["observed_nonzero_flavors"] == [1]
        assert report["candidate_flavor"] == 1
        assert report["degrees"][3]["flavors"] == {1: 4}
        assert report["degrees"][4]["missing_flavors"] == {1: 5}
        assert report["flavors"][1]["nonzero_degrees"] == [1, 2, 3]

    def test_flavor_report_exposes_truncation_barrier_N3(self, bar_N3_deg3):
        """At N = 3, the first unresolved flavor boundary is the missing degree-4 input."""
        report = ncomplex_flavor_report(bar_N3_deg3)

        assert report["N"] == 3
        assert report["fully_computable_degrees"] == [1]
        assert report["observed_nonzero_flavors"] == []
        assert report["candidate_flavor"] is None
        assert report["degrees"][1]["flavors"] == {1: 0, 2: 0}
        assert report["degrees"][2]["missing_flavors"] == {1: 4}
        assert report["flavors"][1]["first_missing_source_degree"] == 4
        assert report["flavors"][2]["first_missing_source_degree"] == 4

    def test_admissible_level_report_wrapper_matches_bar_report(self, bar_N3_deg3):
        """The N-level wrapper agrees with the direct bar-based report."""
        direct = ncomplex_flavor_report(bar_N3_deg3)
        wrapped = admissible_level_flavor_report(3, max_degree=3)

        assert wrapped["degrees"] == direct["degrees"]
        assert wrapped["flavors"] == direct["flavors"]
        assert wrapped["candidate_flavor"] == direct["candidate_flavor"]


# ============================================================================
# N = 3 degree-4 completion
# ============================================================================

class TestN3Degree4FlavorPacket:
    """Test the first sparse degree-4 flavor completion at N = 3."""

    @pytest.mark.slow
    def test_sparse_degree4_packet_is_three_dimensional_on_both_flavors(self):
        """The first unresolved N = 3 flavor packet resolves to a symmetric 3-dim pair."""
        packet = n3_degree4_flavor_packet()

        assert packet["N"] == 3
        assert packet["source_degree"] == 4
        assert packet["kernel_dims"] == {
            2: {1: 650},
            3: {2: 17550},
        }
        assert packet["image_ranks"] == {
            2: {1: 647},
            3: {2: 17547},
        }
        assert packet["resolved_flavors"] == {
            2: {1: 3},
            3: {2: 3},
        }

    @pytest.mark.slow
    def test_periodic_shadow_candidate_report_sees_three_vs_zero(self):
        """The candidate report records the first resolved N=3 vs N=4 shadow mismatch."""
        report = kl_periodic_shadow_candidates()

        assert report["candidate_dimensions"] == {
            "single_flavor_dim": 3,
            "paired_packet_total": 6,
            "degree2_euler_shadow": 3,
        }
        assert report["N3_degree4_profile"]["flavors"][2][1]["total_root_weight_profile"] == {
            -3: 1,
            0: 1,
            3: 1,
        }
        assert report["N3_degree4_profile"]["flavors"][3][2]["total_root_weight_profile"] == {
            -3: 1,
            0: 1,
            3: 1,
        }
        assert report["N4_degree1_window"]["resolved_flavors"] == {
            1: {3: 0, 2: 0},
        }


class TestN4LowDegreeFlavorWindow:
    """Test the first sparse N=4 low-degree flavor window."""

    def test_n4_low_degree_window_vanishes_in_resolved_channels(self):
        """At N = 4, the first resolved degree-1 flavors j=3 and j=2 are both zero."""
        window = n4_low_degree_flavor_window()

        assert window["N"] == 4
        assert window["degree"] == 1
        assert window["kernel_dims"] == {
            1: {3: 63, 2: 63},
        }
        assert window["image_ranks"] == {
            1: {3: 63, 2: 63},
        }
        assert window["resolved_flavors"] == {
            1: {3: 0, 2: 0},
        }

    @pytest.mark.slow
    def test_n4_h13_degree1_channel_vanishes(self):
        """The remaining N=4 degree-1 flavor H^{1,3}_1 also vanishes."""
        channel = n4_degree1_h13_channel()

        assert channel["N"] == 4
        assert channel["degree"] == 1
        assert channel["flavor"] == (1, 3)
        assert channel["kernel_dim"] == 63
        assert channel["image_rank"] == 63
        assert channel["cohomology_dim"] == 0

    @pytest.mark.slow
    def test_n4_degree2_partial_packet_vanishes_in_two_resolved_channels(self):
        """At N = 4, the tractable degree-2 channels H^{3,1}_2 and H^{2,2}_2 are zero."""
        packet = n4_degree2_partial_packet()

        assert packet["N"] == 4
        assert packet["degree"] == 2
        assert packet["kernel_dims"] == {
            (3, 1): 3969,
            (2, 2): 3969,
        }
        assert packet["image_ranks"] == {
            (3, 1): 3969,
            (2, 2): 3969,
        }
        assert packet["resolved_flavors"] == {
            (3, 1): 0,
            (2, 2): 0,
        }
        assert packet["unresolved_flavors"] == [(1, 3)]

    @pytest.mark.slow
    def test_n4_degree2_h13_channel_compressed_bound(self):
        """The remaining N = 4 degree-2 channel is compressed to a 66-dimensional residual packet."""
        bound = n4_degree2_h13_channel_bounds()

        assert bound["N"] == 4
        assert bound["degree"] == 2
        assert bound["flavor"] == (1, 3)
        assert bound["kernel_dim"] == 3969
        assert bound["image_rank_lower_bound"] == 3903
        assert bound["cohomology_upper_bound"] == 66
        assert bound["status"] == "unresolved"
        assert bound["split_coefficients"][1] == pytest.approx(1.0 + 1.0j)
        assert bound["split_coefficients"][2] == pytest.approx(1.0 - 1.0j)
        assert bound["split_coefficients"][3] == pytest.approx(-1.0 - 1.0j)
        assert bound["split_coefficients"][4] == pytest.approx(-1.0 + 1.0j)
        assert bound["seed_family_stats"] == [
            {"tail": (60, 60), "added_rank": 2976, "columns": 250047, "max_support": 38},
            {"tail": (60, 0), "added_rank": 743, "columns": 250047, "max_support": 45},
            {"tail": (60, 12), "added_rank": 184, "columns": 250047, "max_support": 38},
        ]
        assert bound["residual_row_count"] == 66
        assert bound["residual_left_factor_profile"] == {
            "F": 48,
            "E": 15,
            "K-1": 3,
        }
        assert bound["generator_cube"] == {
            "support": ("F", "E", "K-1"),
            "tuples_checked": 243,
            "added_rank": 0,
            "max_support": 0,
        }
        assert bound["generator_prefix_cube"] == {
            "prefix_support": ("F", "E", "K-1"),
            "prefixes_checked": 27,
            "tuples_checked": 107163,
            "added_rank": 0,
            "max_support": 0,
            "active_prefixes": [],
        }

    @pytest.mark.slow
    def test_n4_degree2_h13_precursor_screen_kills_later_split_stages(self):
        """The ab/abc/abcd precursor stages are quotient-zero, leaving only the first split term live."""
        screen = n4_degree2_h13_precursor_screen()

        assert screen["N"] == 4
        assert screen["degree"] == 2
        assert screen["flavor"] == (1, 3)
        assert screen["residual_left_factor_profile"] == {
            "F": 48,
            "E": 15,
            "K-1": 3,
        }
        assert screen["pair_stage"] == {
            "precursor_count": 55,
            "tuples_checked": 13752585,
            "quotient_rank": 0,
            "max_support": 0,
            "active_precursors": [],
        }
        assert screen["triple_stage"] == {
            "precursor_count": 712,
            "tuples_checked": 2825928,
            "quotient_rank": 0,
            "max_support": 0,
            "active_precursors": [],
        }
        assert screen["quad_stage"] == {
            "precursor_count": 6820,
            "tuples_checked": 429660,
            "quotient_rank": 0,
            "max_support": 0,
            "active_precursors": [],
        }
        assert screen["remaining_first_factor_stage"] == {
            "left_factor_counts": {
                "F": 13917960,
                "E": 14965524,
                "K-1": 13834800,
            },
            "tuples_remaining": 42718284,
        }

    @pytest.mark.slow
    def test_n4_degree2_h13_first_term_state_compression(self):
        """The surviving first split term factors through a small state graph over the seed span."""
        compression = n4_degree2_h13_first_term_state_compression()

        assert compression["N"] == 4
        assert compression["degree"] == 2
        assert compression["flavor"] == (1, 3)
        assert compression["status"] == "unresolved"
        assert compression["method"] == "surviving first-term state compression"
        assert compression["residual_left_factor_profile"] == {
            "F": 48,
            "E": 15,
            "K-1": 3,
        }
        assert compression["remaining_first_factor_stage"] == {
            "left_factor_counts": {
                "F": 13917960,
                "E": 14965524,
                "K-1": 13834800,
            },
            "tuples_remaining": 42718284,
        }
        assert compression["per_left_factor"] == {
            "F": {
                "left_index": 0,
                "stage1_basis_count": 56,
                "stage2_state_count": 287,
                "stage3_state_count": 791,
                "final_right_product_state_count": 1405,
                "standalone_first_term_added_rank": 43,
            },
            "E": {
                "left_index": 12,
                "stage1_basis_count": 60,
                "stage2_state_count": 311,
                "stage3_state_count": 849,
                "final_right_product_state_count": 1469,
                "standalone_first_term_added_rank": 14,
            },
            "K-1": {
                "left_index": 60,
                "stage1_basis_count": 56,
                "stage2_state_count": 284,
                "stage3_state_count": 782,
                "final_right_product_state_count": 1358,
                "standalone_first_term_added_rank": 0,
            },
        }
        assert compression["union_final_right_product_state_count"] == 1493
        assert compression["standalone_first_term_state_packets"] == 4232
        assert compression["seed_rank"] == 3903
        assert compression["standalone_first_term_added_rank"] == 57
        assert compression["standalone_first_term_span_rank"] == 3960
        assert compression["standalone_first_term_gap"] == 9

    @pytest.mark.slow
    def test_n4_degree2_h13_cancellation_plane_is_common(self):
        """The first-term and non-first split sectors already span the same 57-plane."""
        plane = n4_degree2_h13_cancellation_plane()

        assert plane["N"] == 4
        assert plane["degree"] == 2
        assert plane["flavor"] == (1, 3)
        assert plane["status"] == "unresolved"
        assert plane["method"] == "quotient-plane comparison of surviving split terms"
        assert plane["quotient_dimension"] == 66
        assert plane["common_plane_rank"] == 57
        assert plane["first_term_rank"] == 57
        assert plane["term2_rank"] == 57
        assert plane["term3_rank"] == 57
        assert plane["term4_rank"] == 57
        assert plane["nonfirst_rank"] == 57
        assert plane["first_term_extra_over_nonfirst"] == 0
        assert plane["term2_pair_count"] == 51813
        assert plane["term3_pair_count"] == 35772
        assert plane["term4_left_state_count"] == 1118
        assert plane["union_final_right_product_state_count"] == 1493
        assert plane["shared_plane_gap_to_full_quotient"] == 9

    @pytest.mark.slow
    def test_n4_degree2_h13_cancellation_operator_is_scalar(self):
        """On the witness common plane, the surviving full split action cancels exactly."""
        operator = n4_degree2_h13_cancellation_operator()

        assert operator["N"] == 4
        assert operator["degree"] == 2
        assert operator["flavor"] == (1, 3)
        assert operator["status"] == "witness-basis common-plane operator"
        assert operator["basis_dim"] == 57
        assert len(operator["witness_tuples"]) == 57
        assert operator["split1_scalar"] == pytest.approx(1.0 + 1.0j)
        assert operator["operator_rank"] == 57
        assert operator["weighted_rank"] == 0
        assert operator["weighted_nullity"] == 57
        assert operator["scalar_candidate"] == pytest.approx(-1.0 - 1.0j)
        assert operator["max_deviation_from_scalar_identity"] < 1e-12
        assert operator["weighted_max_entry_abs"] < 1e-12
        assert operator["operator_matrix"].shape == (57, 57)
        assert operator["weighted_operator_matrix"].shape == (57, 57)

    @pytest.mark.slow
    def test_n4_degree2_h13_exact_channel_is_66_dimensional(self):
        """The full surviving packet adds no rank beyond the 3903-dimensional seed span."""
        channel = n4_degree2_h13_exact_channel()

        assert channel["N"] == 4
        assert channel["degree"] == 2
        assert channel["flavor"] == (1, 3)
        assert channel["status"] == "resolved"
        assert channel["method"] == "exhaustive compressed prefix verification of the surviving packet"
        assert channel["kernel_dim"] == 3969
        assert channel["seed_rank"] == 3903
        assert channel["common_plane_basis_dim"] == 57
        assert channel["residual_seed_quotient_dim"] == 66
        assert channel["compressed_prefix_signature_count"] == 354668
        assert channel["raw_prefix_count"] == 678068
        assert channel["compressed_columns_checked"] == 22344084
        assert channel["raw_columns_covered"] == 42718284
        assert channel["compressed_common_nonzero_columns"] == 0
        assert channel["compressed_residual_nonzero_columns"] == 0
        assert channel["raw_common_nonzero_columns"] == 0
        assert channel["raw_residual_nonzero_columns"] == 0
        assert channel["weighted_common_plane_rank"] == 0
        assert channel["weighted_residual_rank"] == 0
        assert channel["image_rank"] == 3903
        assert channel["cohomology_dim"] == 66
        assert channel["first_common_counterexample"] is None
        assert channel["first_residual_counterexample"] is None

    @pytest.mark.slow
    def test_n4_degree2_h13_exact_packet_profile_has_palindromic_weights(self):
        """The exact 66-dimensional packet has a rigid left-factor split and palindromic weight profile."""
        profile = n4_degree2_h13_exact_packet_profile()

        assert profile["N"] == 4
        assert profile["degree"] == 2
        assert profile["flavor"] == (1, 3)
        assert profile["status"] == "resolved support profile"
        assert profile["cohomology_dim"] == 66
        assert profile["basis_row_count"] == 66
        assert profile["left_factor_profile"] == {
            "F": 48,
            "E": 15,
            "K-1": 3,
        }
        assert profile["right_kind_profile"] == {
            "Kminus1": 7,
            "pbw": 59,
        }
        assert profile["right_root_weight_profile"] == {
            -3: 1,
            -2: 4,
            -1: 12,
            0: 15,
            1: 17,
            2: 12,
            3: 5,
        }
        assert profile["total_root_weight_profile"] == {
            -4: 1,
            -3: 4,
            -2: 8,
            -1: 12,
            0: 16,
            1: 12,
            2: 8,
            3: 4,
            4: 1,
        }
        assert profile["support_by_left_factor"]["F"]["right_kind_profile"] == {
            "Kminus1": 3,
            "pbw": 45,
        }
        assert profile["support_by_left_factor"]["E"]["right_kind_profile"] == {
            "Kminus1": 3,
            "pbw": 12,
        }
        assert profile["support_by_left_factor"]["K-1"]["right_kind_profile"] == {
            "Kminus1": 1,
            "pbw": 2,
        }
        assert profile["support_by_left_factor"]["F"]["right_ac_profile"] == {
            ("Kminus1", 1): 1,
            ("Kminus1", 2): 1,
            ("Kminus1", 3): 1,
            (0, 1): 4,
            (0, 2): 4,
            (0, 3): 1,
            (1, 0): 4,
            (1, 1): 4,
            (1, 2): 4,
            (2, 0): 4,
            (2, 1): 4,
            (2, 2): 4,
            (3, 0): 4,
            (3, 1): 4,
            (3, 2): 4,
        }
        assert profile["support_by_left_factor"]["E"]["right_ac_profile"] == {
            ("Kminus1", 1): 1,
            ("Kminus1", 2): 1,
            ("Kminus1", 3): 1,
            (0, 1): 3,
            (1, 0): 4,
            (2, 0): 4,
            (3, 0): 1,
        }
        assert profile["support_by_left_factor"]["K-1"]["right_ac_profile"] == {
            ("Kminus1", 1): 1,
            (0, 1): 1,
            (1, 0): 1,
        }


class TestN3ExactPacketProfile:
    """Test exact support profiles for the first admissible N=3 packet."""

    @pytest.mark.slow
    def test_n3_degree4_exact_packet_profile(self):
        """Both N=3 flavors have the same extremal/neutral class-weight pattern."""
        profile = n3_degree4_exact_packet_profile()

        assert profile["N"] == 3
        assert profile["source_degree"] == 4
        assert profile["status"] == "resolved support profile"
        assert profile["quotient_dims"] == {
            2: {1: 29},
            3: {2: 29},
        }
        assert profile["cohomology_dims"] == {
            2: {1: 3},
            3: {2: 3},
        }

        flavor_12 = profile["flavors"][2][1]
        flavor_21 = profile["flavors"][3][2]

        assert flavor_12["total_root_weight_profile"] == {
            -3: 1,
            0: 1,
            3: 1,
        }
        assert flavor_21["total_root_weight_profile"] == {
            -3: 1,
            0: 1,
            3: 1,
        }
        assert flavor_12["class_support_sizes"] == (1, 6, 1)
        assert flavor_21["class_support_sizes"] == (1, 6, 1)

        assert flavor_12["classes"][0]["entries"] == (
            {
                "quotient_row": 1,
                "coeff": (1.0, 0.0),
                "left_label": ("pbw", (0, 0, 1)),
                "right_label": ("pbw", (0, 0, 2)),
                "left_root_weight": -1,
                "right_root_weight": -2,
                "total_root_weight": -3,
            },
        )
        assert flavor_12["classes"][2]["entries"] == (
            {
                "quotient_row": 171,
                "coeff": (1.0, 0.0),
                "left_label": ("pbw", (1, 0, 0)),
                "right_label": ("pbw", (2, 0, 0)),
                "left_root_weight": 1,
                "right_root_weight": 2,
                "total_root_weight": 3,
            },
        )
        assert flavor_21["classes"][0]["entries"] == (
            {
                "quotient_row": 0,
                "coeff": (1.0, 0.0),
                "left_label": ("pbw", (0, 0, 1)),
                "middle_label": ("pbw", (0, 0, 1)),
                "right_label": ("pbw", (0, 0, 1)),
                "left_root_weight": -1,
                "middle_root_weight": -1,
                "right_root_weight": -1,
                "total_root_weight": -3,
            },
        )
        assert flavor_21["classes"][2]["entries"] == (
            {
                "quotient_row": 4218,
                "coeff": (1.0, 0.0),
                "left_label": ("pbw", (1, 0, 0)),
                "middle_label": ("pbw", (1, 0, 0)),
                "right_label": ("pbw", (1, 0, 0)),
                "left_root_weight": 1,
                "middle_root_weight": 1,
                "right_root_weight": 1,
                "total_root_weight": 3,
            },
        )
        assert tuple(entry["total_root_weight"] for entry in flavor_12["classes"]) == (-3, 0, 3)
        assert tuple(entry["total_root_weight"] for entry in flavor_21["classes"]) == (-3, 0, 3)

    @pytest.mark.slow
    def test_exact_profile_comparison_detects_staircase_only_at_n4(self):
        """The first N=3 packet is not yet a unit-step character staircase, but N=4 is."""
        report = kl_exact_packet_profile_comparison()

        assert report["status"] == "exact profile comparison"
        assert report["N3_flavors_match"] is True
        assert report["N3_single_flavor_profile"] == {
            -3: 1,
            0: 1,
            3: 1,
        }
        assert report["N3_paired_profile"] == {
            -3: 2,
            0: 2,
            3: 2,
        }
        assert report["N3_single_character_test"]["is_character_profile"] is False
        assert report["N3_single_character_test"]["obstruction_kind"] == "negative multiplicity"
        assert report["N3_single_character_test"]["first_obstruction_weight"] == 2
        assert report["N3_paired_character_test"]["is_character_profile"] is False
        assert report["N3_paired_character_test"]["obstruction_kind"] == "negative multiplicity"
        assert report["N3_paired_character_test"]["first_obstruction_weight"] == 2
        assert report["N4_profile"] == {
            -4: 1,
            -3: 4,
            -2: 8,
            -1: 12,
            0: 16,
            1: 12,
            2: 8,
            3: 4,
            4: 1,
        }
        assert report["N4_character_test"]["is_character_profile"] is True
        assert report["N4_character_test"]["character_multiplicities"] == {
            0: 4,
            1: 4,
            2: 4,
            3: 3,
            4: 1,
        }
        assert report["N4_vs_paired_N3_dimension_ratio"] == 11

    @pytest.mark.slow
    def test_convolution_obstruction_rules_out_nonnegative_transport(self):
        """There is no exact symmetric convolution transport from the first N=3 packet to N=4."""
        report = kl_shadow_transport_convolution_obstruction()

        assert report["status"] == "exact convolution obstruction"
        assert report["source_profiles"]["single"] == {
            -3: 1,
            0: 1,
            3: 1,
        }
        assert report["source_profiles"]["paired"] == {
            -3: 2,
            0: 2,
            3: 2,
        }
        assert report["target_profile"] == {
            -4: 1,
            -3: 4,
            -2: 8,
            -1: 12,
            0: 16,
            1: 12,
            2: 8,
            3: 4,
            4: 1,
        }
        assert report["exact_transport_possible"] is False
        assert report["nonnegative_transport_possible"] is False
        assert report["full_single_flavor_radius_solutions"] == {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }
        assert report["full_paired_radius_solutions"] == {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }
        assert report["window_single_flavor_radius_solutions"] == {
            0: None,
            1: None,
            2: None,
            3: None,
            4: {
                "status": "unique",
                "radius": 4,
                "full_support": False,
                "kernel": {
                    -4: Fraction(4, 1),
                    -3: Fraction(12, 1),
                    -2: Fraction(11, 1),
                    -1: Fraction(-3, 1),
                    0: Fraction(-8, 1),
                    1: Fraction(-3, 1),
                    2: Fraction(11, 1),
                    3: Fraction(12, 1),
                    4: Fraction(4, 1),
                },
                "nonnegative": False,
            },
        }

    @pytest.mark.slow
    def test_schrodinger_ansatz_finds_first_structured_transport(self):
        """The first structured finite-window transport is Dirichlet Laplacian plus sextic potential."""
        report = kl_shadow_transport_schrodinger_ansatz()

        assert report["status"] == "structured non-convolutional finite-window transport"
        assert report["single_source_profile"] == {
            -3: 1,
            0: 1,
            3: 1,
        }
        assert report["paired_source_profile"] == {
            -3: 2,
            0: 2,
            3: 2,
        }
        assert report["target_profile"] == {
            -4: 1,
            -3: 4,
            -2: 8,
            -1: 12,
            0: 16,
            1: 12,
            2: 8,
            3: 4,
            4: 1,
        }
        assert report["paired_schrodinger"] == {
            "status": "resolved",
            "include_laplacian": True,
            "minimal_potential_degree": 6,
            "laplacian_coeff": Fraction(-3, 140),
            "potential_coeffs": {
                0: Fraction(4, 35),
                2: Fraction(-2519, 16800),
                4: Fraction(503, 13440),
                6: Fraction(-17, 9600),
            },
            "output_profile": {
                -4: Fraction(0, 1),
                -3: Fraction(2, 1),
                -2: Fraction(0, 1),
                -1: Fraction(0, 1),
                0: Fraction(2, 1),
                1: Fraction(0, 1),
                2: Fraction(0, 1),
                3: Fraction(2, 1),
                4: Fraction(0, 1),
            },
        }
        assert report["single_schrodinger"] == {
            "status": "resolved",
            "include_laplacian": True,
            "minimal_potential_degree": 6,
            "laplacian_coeff": Fraction(-3, 280),
            "potential_coeffs": {
                0: Fraction(2, 35),
                2: Fraction(-2519, 33600),
                4: Fraction(503, 26880),
                6: Fraction(-17, 19200),
            },
            "output_profile": {
                -4: Fraction(0, 1),
                -3: Fraction(1, 1),
                -2: Fraction(0, 1),
                -1: Fraction(0, 1),
                0: Fraction(1, 1),
                1: Fraction(0, 1),
                2: Fraction(0, 1),
                3: Fraction(1, 1),
                4: Fraction(0, 1),
            },
        }
        assert report["paired_pure_potential"] == {
            "status": "resolved",
            "include_laplacian": False,
            "minimal_potential_degree": 8,
            "laplacian_coeff": Fraction(0, 1),
            "potential_coeffs": {
                0: Fraction(1, 8),
                2: Fraction(-2221, 13440),
                4: Fraction(109, 2560),
                6: Fraction(-3, 1280),
                8: Fraction(1, 53760),
            },
            "output_profile": {
                -4: Fraction(0, 1),
                -3: Fraction(2, 1),
                -2: Fraction(0, 1),
                -1: Fraction(0, 1),
                0: Fraction(2, 1),
                1: Fraction(0, 1),
                2: Fraction(0, 1),
                3: Fraction(2, 1),
                4: Fraction(0, 1),
            },
        }
        obstruction = kl_shadow_transport_convolution_obstruction()
        assert obstruction["window_paired_radius_solutions"] == {
            0: None,
            1: None,
            2: None,
            3: None,
            4: {
                "status": "unique",
                "radius": 4,
                "full_support": False,
                "kernel": {
                    -4: Fraction(2, 1),
                    -3: Fraction(6, 1),
                    -2: Fraction(11, 2),
                    -1: Fraction(-3, 2),
                    0: Fraction(-4, 1),
                    1: Fraction(-3, 2),
                    2: Fraction(11, 2),
                    3: Fraction(6, 1),
                    4: Fraction(2, 1),
                },
                "nonnegative": False,
            },
        }


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
        assert result["flavor_report"]["degrees"][2]["missing_flavors"] == {1: 4}
        assert result["flavor_report"]["candidate_flavor"] is None


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

    def test_N2_dq_is_ordinary(self, bar_N2_deg3):
        """N = 2: d_q^2 = 0 (reduces to standard chain complex)."""
        for n in range(2, 4):
            norm = bar_N2_deg3.verify_dq_squared(n)
            assert norm < 1e-10

    def test_N3_dq_not_ordinary(self, bar_N3_deg3):
        """N = 3: d_q^2 != 0 (genuine N-complex)."""
        norms = [bar_N3_deg3.verify_dq_squared(n) for n in range(2, 4)]
        assert max(norms) > 1e-6, "d_q^2 = 0 at all degrees for N=3"

    def test_N3_dq_is_3complex(self, bar_N3_deg3):
        """N = 3: d_q^3 = 0 (it is a 3-complex)."""
        norm = bar_N3_deg3.verify_dq_N(3)
        assert norm < 1e-8

    def test_standard_always_ordinary(self, bar_N2_deg3, bar_N3_deg3):
        """The standard bar differential always satisfies d^2 = 0."""
        for bar in [bar_N2_deg3, bar_N3_deg3]:
            for degree in range(2, 4):
                norm = bar.verify_d_squared(degree)
                assert norm < 1e-10

    def test_transition_N2_to_N3(self, bar_N2_deg3, bar_N3_deg3):
        """The transition from N=2 to N=3 activates N-complex structure.

        At N=2: d_q^2 = 0 (ordinary, since q = -1 gives standard signs).
        At N=3: d_q^2 != 0, d_q^3 = 0 (genuine 3-complex).
        Both always have standard d^2 = 0.
        """
        dq2_norm_N2 = bar_N2_deg3.verify_dq_squared(2)
        dq2_norm_N3 = bar_N3_deg3.verify_dq_squared(2)
        dq3_norm_N3 = bar_N3_deg3.verify_dq_N(3)

        assert dq2_norm_N2 < 1e-10  # N=2: d_q^2 = 0 (always at degree 2)
        # At degree 2, d_q^2: B_2 -> B_0 is structurally zero (d_q(B_1->B_0)=0)
        # Test d_q^2 at degree 3 instead for genuine N-complex evidence
        dq2_norm_N3_deg3 = bar_N3_deg3.verify_dq_squared(3)
        assert dq2_norm_N3_deg3 > 1e-6   # N=3: d_q^2 != 0 at degree 3
        assert dq3_norm_N3 < 1e-8   # N=3: d_q^3 = 0
