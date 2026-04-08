r"""Tests for the BRST sl_5 (3,2) spectral sequence engine.

10 tests verifying structural data (root counts, n_+ dimension, grading,
ghost system, nilpotency, brackets).  All tests use data that is currently
implemented (no NotImplementedError functions).

Multi-path verification:
  Path 1: direct computation from the engine
  Path 2: cross-check with nonprincipal_ds_orbits canonical engine
  Path 3: independent combinatorial recomputation from first principles
  Path 4: consistency checks (dimensions sum correctly, symmetry, etc.)
  Path 5: cross-family comparison (abelian hook partitions vs non-abelian)
"""

import pytest
from sympy import Rational

from compute.lib.brst_sl5_subregular_engine import (
    # Root system
    positive_roots_sl5,
    simple_roots_sl5,
    root_height,
    # Grading
    sl2_triple_diagonal,
    half_grading_values,
    dynkin_grade_of_root,
    grading_decomposition,
    grade_dimensions,
    # n_+ structure
    n_plus_basis,
    n_plus_grade_decomposition,
    n_plus_dimension,
    n_plus_is_abelian,
    n_plus_nilpotency_step,
    n_plus_brackets,
    # Ghost system
    ghost_basis,
    ghost_number_range,
    num_ghost_sectors,
    # Kazhdan filtration (metadata only)
    kazhdan_filtration_data,
    # W-algebra character
    w_algebra_character_prediction,
    # Central charge
    central_charge,
    # Constants
    PARTITION,
    PARTITION_T,
    N,
    NUM_SIMPLE_ROOTS,
    NUM_POSITIVE_ROOTS,
    DIM_SL5,
    CARTAN_MATRIX,
    WEIGHTED_DYNKIN,
)

# Cross-check imports from canonical engines.
from compute.lib.nonprincipal_ds_orbits import (
    centralizer_dimension_sl_n,
    is_hook_partition,
    transpose_partition,
    type_a_partition_sl2_triple,
)
from compute.lib.hook_type_w_duality import (
    krw_central_charge,
)
from sympy import Symbol, simplify


# ============================================================================
# I. Root system of sl_5 (2 tests)
# ============================================================================

class TestRootSystemSl5:
    """Verify sl_5 root system data."""

    def test_positive_root_count(self):
        """sl_5 has C(5,2) = 10 positive roots.

        Path 1: count from engine.
        Path 2: combinatorial formula C(N,2) = N(N-1)/2.
        Path 3: cross-check constant NUM_POSITIVE_ROOTS.
        """
        roots = positive_roots_sl5()
        assert len(roots) == 10
        assert len(roots) == N * (N - 1) // 2  # Path 2
        assert len(roots) == NUM_POSITIVE_ROOTS  # Path 3

    def test_simple_roots_and_heights(self):
        """sl_5 has 4 simple roots; height distribution is (4, 3, 2, 1).

        Path 1: enumerate simple roots.
        Path 2: height distribution from root_height.
        Path 3: total roots = sum of height-k roots = N-1 + N-2 + ... + 1.
        """
        simples = simple_roots_sl5()
        assert len(simples) == NUM_SIMPLE_ROOTS
        assert simples == [(1, 2), (2, 3), (3, 4), (4, 5)]

        from collections import Counter
        roots = positive_roots_sl5()
        height_counts = Counter(root_height(r) for r in roots)
        # For sl_N: height k has N-k roots.
        for k in range(1, N):
            assert height_counts[k] == N - k
        # Path 3: sum = (N-1) + (N-2) + ... + 1 = C(N,2).
        assert sum(height_counts.values()) == NUM_POSITIVE_ROOTS


# ============================================================================
# II. Dynkin grading for (3,2) (2 tests)
# ============================================================================

class TestDynkinGrading:
    """Verify the ad(h/2)-grading decomposition."""

    def test_h_diagonal_and_tracelessness(self):
        """sl_2-triple h for (3,2) has correct eigenvalues.

        Path 1: direct from engine.
        Path 2: cross-check with canonical engine type_a_partition_sl2_triple.
        Path 3: tracelessness (sl, not gl).
        """
        # Path 1: engine constant.
        h_diag = sl2_triple_diagonal()
        assert h_diag == (2, 0, -2, 1, -1)
        # Path 2: canonical engine.
        triple = type_a_partition_sl2_triple(PARTITION)
        h_canonical = tuple(int(triple.h[i, i]) for i in range(N))
        assert h_diag == h_canonical
        # Path 3: tracelessness.
        assert sum(h_diag) == 0

    def test_grading_dimensions_and_symmetry(self):
        """Root space dimensions sum to 20 and satisfy dim(g_j) = dim(g_{-j}).

        Path 1: sum of root space dims = dim(sl_5) - rank = 24 - 4 = 20.
        Path 2: symmetry from sl_2-triple structure.
        Path 3: explicit grade dimensions match (1, 2, 3, 4, 0, 4, 3, 2, 1).
        """
        dims = grade_dimensions()
        # Path 1: total root spaces.
        total_root_spaces = sum(dims.values())
        assert total_root_spaces == DIM_SL5 - NUM_SIMPLE_ROOTS  # 24 - 4 = 20

        # Path 2: symmetry.
        for g in dims:
            assert -g in dims, f"grade {g} has no partner at grade {-g}"
            assert dims[g] == dims[-g]

        # Path 3: explicit values for (3,2) with half-integer grades.
        # Positive grades: 1/2 -> 4, 1 -> 3, 3/2 -> 2, 2 -> 1.
        assert dims[Rational(1, 2)] == 4
        assert dims[Rational(1)] == 3
        assert dims[Rational(3, 2)] == 2
        assert dims[Rational(2)] == 1
        # Grade 0 root spaces: should be 0 for this partition.
        # (g_0 = Cartan only, no zero-grade root spaces.)
        assert dims.get(Rational(0), 0) == 0


# ============================================================================
# III. n_+ structure (3 tests)
# ============================================================================

class TestNPlusStructure:
    """Verify the nilradical n_+ for (3,2)."""

    def test_n_plus_dimension(self):
        """dim(n_+) = 10 for partition (3,2) in sl_5.

        Path 1: count from grading decomposition in engine.
        Path 2: from g_0 symmetry: dim(n_+) = (dim(g) - dim(g_0)) / 2.
        Path 3: cross-check with canonical engine nilradical computation.
        Path 4: sum of grade dimensions: 4 + 3 + 2 + 1 = 10.
        """
        # Path 1: direct.
        assert n_plus_dimension() == 10
        # Path 2: from g_0 dimension.
        dims = grade_dimensions()
        dim_g0_roots = dims.get(Rational(0), 0)
        dim_g0_total = dim_g0_roots + NUM_SIMPLE_ROOTS
        dim_n_plus_from_symmetry = (DIM_SL5 - dim_g0_total) // 2
        assert dim_n_plus_from_symmetry == 10
        assert n_plus_dimension() == dim_n_plus_from_symmetry
        # Path 3: canonical engine.
        from compute.lib.theorem_nonprincipal_sl5_32_engine import nilradical_data_32
        nrd = nilradical_data_32()
        assert nrd.dim_m_plus == 10
        # Path 4: sum of grade dimensions.
        grade_decomp = n_plus_grade_decomposition()
        assert sum(len(v) for v in grade_decomp.values()) == 10

    def test_n_plus_nonabelian_4step(self):
        """n_+ for (3,2) is non-abelian and 4-step nilpotent.

        Path 1: abelianness check from engine.
        Path 2: nilpotency step = number of distinct positive grades = 4.
        Path 3: cross-check with canonical engine.
        """
        # Path 1: non-abelian.
        assert not n_plus_is_abelian()
        # Path 2: 4-step nilpotent (grades 1/2, 1, 3/2, 2).
        assert n_plus_nilpotency_step() == 4
        grade_decomp = n_plus_grade_decomposition()
        assert len(grade_decomp) == 4
        # Path 3: cross-check with canonical engine.
        from compute.lib.theorem_nonprincipal_sl5_32_engine import nilradical_data_32
        nrd = nilradical_data_32()
        assert not nrd.is_abelian
        # Cross-check: (3,2) is NOT hook.
        assert not is_hook_partition(PARTITION)

    def test_n_plus_brackets_count_and_structure(self):
        """10 non-trivial brackets within n_+, all Lie brackets [E_{ij}, E_{kl}].

        Path 1: count brackets from engine.
        Path 2: verify each bracket obeys [E_{ij}, E_{jl}] = E_{il}.
        Path 3: verify grade additivity: grade(result) = grade(input1) + grade(input2).
        """
        brackets = n_plus_brackets()
        # Path 1: 10 brackets.
        assert len(brackets) == 10

        n_plus = set(n_plus_basis())
        grade_decomp = n_plus_grade_decomposition()
        # Build a root-to-grade map.
        root_grade = {}
        for g, roots in grade_decomp.items():
            for r in roots:
                root_grade[r] = g

        for (a, b, c) in brackets:
            # Path 2: structural validity.
            i_a, j_a = a
            i_b, j_b = b
            i_c, j_c = c
            assert j_a == i_b, f"bracket {a}, {b} -> {c}: j_a != i_b"
            assert i_c == i_a and j_c == j_b, f"result should be ({i_a},{j_b})"
            assert c in n_plus, f"result {c} not in n_+"
            # Path 3: grade additivity.
            assert root_grade[a] + root_grade[b] == root_grade[c], (
                f"grade({a})={root_grade[a]} + grade({b})={root_grade[b]} "
                f"!= grade({c})={root_grade[c]}"
            )


# ============================================================================
# IV. Ghost system (1 test)
# ============================================================================

class TestGhostSystem:
    """Verify the ghost basis and ghost number range."""

    def test_ghost_system_structure(self):
        """10 ghost pairs, ghost number range [-10, +10], 21 sectors.

        Path 1: count and range from engine.
        Path 2: verify conformal weights b_weight = 1 - grade, c_weight = grade.
        Path 3: verify grade distribution matches n_+ grade decomposition.
        """
        ghosts = ghost_basis()
        # Path 1: counts.
        assert len(ghosts) == 10
        assert ghost_number_range() == (-10, 10)
        assert num_ghost_sectors() == 21

        # Path 2: conformal weight formula.
        for g in ghosts:
            assert g.c_weight == g.grade
            assert g.b_weight == 1 - g.grade

        # Path 3: grade distribution matches n_+.
        from collections import Counter
        ghost_grade_counts = Counter(g.grade for g in ghosts)
        n_plus_grade_counts = {g: len(rs) for g, rs in n_plus_grade_decomposition().items()}
        for grade, count in ghost_grade_counts.items():
            assert n_plus_grade_counts[grade] == count

        # Explicit per-grade checks.
        assert ghost_grade_counts[Rational(1, 2)] == 4
        assert ghost_grade_counts[Rational(1)] == 3
        assert ghost_grade_counts[Rational(3, 2)] == 2
        assert ghost_grade_counts[Rational(2)] == 1


# ============================================================================
# V. Kazhdan filtration metadata (1 test)
# ============================================================================

class TestKazhdanFiltration:
    """Verify Kazhdan filtration structural data."""

    def test_kazhdan_metadata(self):
        """Both Q_st and Q_gh have Kazhdan degree 0 for (3,2).

        Path 1: metadata from engine.
        Path 2: structural argument (max grade of n_+ is 2, so the
                 Kazhdan filtration has 5 layers: grades 0, 1/2, 1, 3/2, 2).
        """
        data = kazhdan_filtration_data()
        assert data['partition'] == PARTITION
        assert data['max_grade'] == 2
        assert data['num_filtration_layers'] == 5  # grades 0, 1/2, 1, 3/2, 2
        assert data['q_st_filtration_degree'] == 0
        assert data['q_gh_filtration_degree'] == 0
        assert data['d_0_is_full_brst'] is True


# ============================================================================
# VI. Central charge cross-check (1 test)
# ============================================================================

class TestCentralCharge:
    """Cross-check central charge with canonical engine."""

    def test_central_charge_cross_check(self):
        """c(3,2; k) = 2 - 108/(k+5) = 2(k-49)/(k+5).

        Path 1: from brst engine.
        Path 2: from canonical krw_central_charge.
        Path 3: numerical evaluation at k=1.
        """
        kk = Symbol('k')
        # Path 1: brst engine.
        c_brst = central_charge()
        # Path 2: canonical.
        c_canonical = krw_central_charge(PARTITION, kk)
        assert simplify(c_brst - c_canonical) == 0
        # Path 3: numerical at k=1.
        c_at_1 = central_charge(level=1)
        assert c_at_1 == Rational(2 * (1 - 49), (1 + 5))  # = -96/6 = -16
        assert c_at_1 == Rational(-16)
