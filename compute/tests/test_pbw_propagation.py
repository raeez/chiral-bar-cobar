"""Tests for PBW propagation theorem (thm:pbw-propagation).

Verifies: for any CFT-type chiral algebra A satisfying MK1 (genus-0 Koszulity)
with positive conformal grading and unique weight-2 stress tensor, axiom MK3
(PBW concentration at all genera) follows automatically.

Proof outline:
  Step 1: d_coll is curve-independent (regular part has zero residue)
  Step 2: B-bar(A|X) = core + enrichment (d_coll preserves both)
  Step 3: d_2^{PBW} = h * id on enrichment (kills it for h >= 1)
  Conclusion: E_infty(g) = E_infty(0) for all g

Ground truth sources:
  - bar_complex.py: bar dims at genus 0 (partition formulas, Riordan, Motzkin)
  - shadow_metric_census.py: kappa values for cross-check
  - thm:pbw-propagation in higher_genus_modular_koszul.tex
  - rem:bar-dims-partitions in free_fields.tex

~90 tests total.
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.pbw_propagation_engine import (
    PropagatorDecomposition,
    CoreEnrichmentDecomposition,
    PBWSpectralSequence,
    HeisenbergGenusgVerification,
    AffineSl2GenusgVerification,
    VirasoroGenusgVerification,
    PBWPropagationTheorem,
    verify_collision_differential_independence,
    verify_enrichment_factorization,
    genus1_szego_expansion_orders,
    heisenberg_weight_space_dims,
    sl2_weight_space_dims,
    virasoro_weight_space_dims,
    _bar_dim_heisenberg_g0,
    _bar_dim_sl2_g0,
    _bar_dim_virasoro_g0,
    _colored_partition,
    _partitions_min_part,
)
from compute.lib.bar_complex import (
    bar_dim_heisenberg,
    bar_dim_sl2,
    bar_dim_virasoro,
    KNOWN_BAR_DIMS,
)
from compute.lib.shadow_metric_census import (
    kappa_heisenberg,
    kappa_affine_sl2,
    kappa_virasoro,
)
from compute.lib.utils import partition_number


# =========================================================================
# 1. Propagator tests (~15 tests)
# =========================================================================

class TestPropagatorDecomposition:
    """Tests for Szego kernel decomposition at various genera."""

    def test_genus0_no_regular_part(self):
        """Genus 0: no regular part (no holomorphic 1-forms on P^1)."""
        prop = PropagatorDecomposition(0)
        assert prop.dim_h10 == 0
        assert prop.regular_part_matrix() is None

    def test_genus0_singular_part_residue(self):
        """Genus 0: singular part 1/(z-w) has residue 1."""
        prop = PropagatorDecomposition(0)
        assert prop.singular_part_residue() == 1

    def test_genus0_regular_part_residue(self):
        """Genus 0: regular part residue is 0 (vacuously, no regular part)."""
        prop = PropagatorDecomposition(0)
        assert prop.regular_part_residue() == 0

    def test_genus1_dim_h10(self):
        """Genus 1: dim H^{1,0}(E_tau) = 1."""
        prop = PropagatorDecomposition(1)
        assert prop.dim_h10 == 1

    def test_genus1_regular_part_residue_zero(self):
        """Genus 1: Res_{z->w}[R_1(z,w)] = 0."""
        prop = PropagatorDecomposition(1)
        assert prop.regular_part_residue() == 0

    def test_genus1_szego_with_explicit_tau(self):
        """Genus 1 with explicit period matrix tau = i."""
        tau = np.array([[1j]])
        prop = PropagatorDecomposition(1, period_matrix=tau)
        assert prop.dim_h10 == 1
        assert prop.regular_part_residue() == 0
        # (Im tau)^{-1} = [[1]]
        np.testing.assert_allclose(prop.im_tau_inv, [[1.0]])

    def test_genus1_szego_with_modular_tau(self):
        """Genus 1 with tau = (1+i*sqrt(3))/2 (hexagonal lattice)."""
        tau = np.array([[0.5 + 0.5j * np.sqrt(3)]])
        prop = PropagatorDecomposition(1, period_matrix=tau)
        assert prop.regular_part_residue() == 0
        expected_im_inv = 1.0 / (0.5 * np.sqrt(3))
        np.testing.assert_allclose(prop.im_tau_inv, [[expected_im_inv]], rtol=1e-10)

    def test_genus2_dim_h10(self):
        """Genus 2: dim H^{1,0}(Sigma_2) = 2."""
        prop = PropagatorDecomposition(2)
        assert prop.dim_h10 == 2

    def test_genus2_regular_part_residue_zero(self):
        """Genus 2: Res_{z->w}[R_2(z,w)] = 0."""
        prop = PropagatorDecomposition(2)
        assert prop.regular_part_residue() == 0

    def test_genus2_with_symmetric_period_matrix(self):
        """Genus 2 with symmetric period matrix."""
        tau = np.array([[2j, 0.5j], [0.5j, 2j]])
        prop = PropagatorDecomposition(2, period_matrix=tau)
        assert prop.regular_part_residue() == 0
        im_tau = tau.imag
        expected_inv = np.linalg.inv(im_tau)
        np.testing.assert_allclose(prop.im_tau_inv, expected_inv, atol=1e-12)

    def test_genus3_regular_part_residue_zero(self):
        """Genus 3: regular part still has zero residue."""
        prop = PropagatorDecomposition(3)
        assert prop.regular_part_residue() == 0

    def test_genus5_dim_h10(self):
        """Genus 5: dim H^{1,0} = 5."""
        prop = PropagatorDecomposition(5)
        assert prop.dim_h10 == 5

    def test_singular_part_universal(self):
        """Singular part residue = 1, independent of genus."""
        for g in range(6):
            prop = PropagatorDecomposition(g)
            assert prop.singular_part_residue() == 1, f"Failed at genus {g}"

    def test_regular_part_residue_universal_zero(self):
        """Regular part residue = 0, independent of genus."""
        for g in range(6):
            prop = PropagatorDecomposition(g)
            assert prop.regular_part_residue() == 0, f"Failed at genus {g}"

    def test_genus1_szego_expansion_orders(self):
        """Genus-1 Szego regular part has only positive-odd powers of (z-w)."""
        orders = genus1_szego_expansion_orders()
        assert all(n >= 1 for n in orders), "All powers should be >= 1 (no pole)"
        assert all(n % 2 == 1 for n in orders), "All powers should be odd"

    def test_invalid_genus_raises(self):
        """Negative genus should raise ValueError."""
        with pytest.raises(ValueError):
            PropagatorDecomposition(-1)

    def test_period_matrix_shape_mismatch_raises(self):
        """Wrong-shaped period matrix should raise ValueError."""
        with pytest.raises(ValueError):
            PropagatorDecomposition(2, period_matrix=np.array([[1j]]))


# =========================================================================
# 2. Core-enrichment decomposition tests (~15 tests)
# =========================================================================

class TestCoreEnrichmentDecomposition:
    """Tests for B-bar = core + enrichment decomposition."""

    def test_genus0_no_enrichment_heisenberg(self):
        """Genus 0: enrichment = 0 (no holomorphic 1-forms)."""
        decomp = CoreEnrichmentDecomposition(0, "Heisenberg")
        for h in range(1, 8):
            assert decomp.enrichment_dim_at_weight(h) == 0

    def test_genus1_heisenberg_core_matches_g0(self):
        """Genus 1, Heisenberg: core dim = genus-0 bar dim at each degree."""
        decomp = CoreEnrichmentDecomposition(1, "Heisenberg")
        for n in range(1, 8):
            assert decomp.core_dim(n) == bar_dim_heisenberg(n), f"Mismatch at degree {n}"

    def test_genus1_heisenberg_enrichment_dims(self):
        """Genus 1, Heisenberg: enrichment dim at weight h = p(h) * 1."""
        decomp = CoreEnrichmentDecomposition(1, "Heisenberg")
        for h in range(1, 8):
            expected = partition_number(h)  # p(h) * genus(=1)
            assert decomp.enrichment_dim_at_weight(h) == expected, f"Mismatch at weight {h}"

    def test_genus2_heisenberg_enrichment_dims(self):
        """Genus 2, Heisenberg: enrichment dim at weight h = p(h) * 2."""
        decomp = CoreEnrichmentDecomposition(2, "Heisenberg")
        for h in range(1, 8):
            expected = partition_number(h) * 2
            assert decomp.enrichment_dim_at_weight(h) == expected, f"Mismatch at weight {h}"

    def test_genus1_sl2_core_matches_g0(self):
        """Genus 1, sl_2: core dim = genus-0 bar cohomology dim."""
        decomp = CoreEnrichmentDecomposition(1, "sl2")
        for n in range(1, 6):
            assert decomp.core_dim(n) == bar_dim_sl2(n), f"Mismatch at degree {n}"

    def test_genus1_sl2_enrichment_dims(self):
        """Genus 1, sl_2: enrichment dim at weight h = (3-col partitions of h) * 1."""
        decomp = CoreEnrichmentDecomposition(1, "sl2")
        # Weight 1: 3 generators => dim M_1 = 3
        assert decomp.enrichment_dim_at_weight(1) == 3
        # Weight 2: 3-colored partitions of 2 = 9
        assert decomp.enrichment_dim_at_weight(2) == 9

    def test_genus1_virasoro_core_matches_g0(self):
        """Genus 1, Virasoro: core dim = genus-0 bar cohomology dim."""
        decomp = CoreEnrichmentDecomposition(1, "Virasoro")
        for n in range(1, 6):
            assert decomp.core_dim(n) == bar_dim_virasoro(n), f"Mismatch at degree {n}"

    def test_genus1_virasoro_enrichment_weight1_zero(self):
        """Genus 1, Virasoro: no enrichment at weight 1 (T has weight 2)."""
        decomp = CoreEnrichmentDecomposition(1, "Virasoro")
        assert decomp.enrichment_dim_at_weight(1) == 0

    def test_genus1_virasoro_enrichment_weight2(self):
        """Genus 1, Virasoro: enrichment at weight 2 = 1 (one state L_{-2}|0>)."""
        decomp = CoreEnrichmentDecomposition(1, "Virasoro")
        assert decomp.enrichment_dim_at_weight(2) == 1

    def test_d_coll_preserves_core(self):
        """d_coll preserves core summand."""
        for alg in ["Heisenberg", "sl2", "Virasoro"]:
            decomp = CoreEnrichmentDecomposition(1, alg)
            assert decomp.d_coll_preserves_core(), f"Failed for {alg}"

    def test_d_coll_preserves_enrichment(self):
        """d_coll preserves enrichment summand."""
        for alg in ["Heisenberg", "sl2", "Virasoro"]:
            decomp = CoreEnrichmentDecomposition(1, alg)
            assert decomp.d_coll_preserves_enrichment(), f"Failed for {alg}"

    def test_no_mixed_terms(self):
        """No mixed core-enrichment terms in d_coll."""
        for alg in ["Heisenberg", "sl2", "Virasoro"]:
            decomp = CoreEnrichmentDecomposition(1, alg)
            assert decomp.no_mixed_terms(), f"Failed for {alg}"

    def test_genus3_heisenberg_enrichment(self):
        """Genus 3, Heisenberg: enrichment = p(h) * 3."""
        decomp = CoreEnrichmentDecomposition(3, "Heisenberg")
        for h in range(1, 6):
            expected = partition_number(h) * 3
            assert decomp.enrichment_dim_at_weight(h) == expected

    def test_total_enrichment_dim(self):
        """Total enrichment dim up to weight W is sum of p(h)*g for h=1..W."""
        decomp = CoreEnrichmentDecomposition(2, "Heisenberg")
        expected = sum(partition_number(h) * 2 for h in range(1, 6))
        assert decomp.total_enrichment_dim(5) == expected

    def test_invalid_genus_raises(self):
        """Negative genus should raise ValueError."""
        with pytest.raises(ValueError):
            CoreEnrichmentDecomposition(-1, "Heisenberg")


# =========================================================================
# 3. Enrichment killing tests (~20 tests)
# =========================================================================

class TestEnrichmentKilling:
    """Tests for d_2 = h * id on enrichment (Step 3 of proof)."""

    # --- Heisenberg at genus 1 ---

    @pytest.mark.parametrize("weight", [1, 2, 3, 4, 5])
    def test_heisenberg_g1_d2_eigenvalue(self, weight):
        """Heisenberg genus 1: d_2 on M_h tensor dz = h * id."""
        ss = PBWSpectralSequence(1, "Heisenberg")
        assert ss.d2_eigenvalue_on_enrichment(weight) == weight

    @pytest.mark.parametrize("weight", [1, 2, 3, 4, 5])
    def test_heisenberg_g1_d2_is_isomorphism(self, weight):
        """Heisenberg genus 1: d_2 is isomorphism on weight-h enrichment."""
        ss = PBWSpectralSequence(1, "Heisenberg")
        assert ss.d2_is_isomorphism_on_enrichment(weight)

    @pytest.mark.parametrize("weight", [1, 2, 3, 4, 5])
    def test_heisenberg_g1_kernel_trivial(self, weight):
        """Heisenberg genus 1: ker(d_2) on enrichment = 0."""
        ss = PBWSpectralSequence(1, "Heisenberg")
        assert ss.enrichment_kernel_dim(weight) == 0

    @pytest.mark.parametrize("weight", [1, 2, 3, 4, 5])
    def test_heisenberg_g1_e3_enrichment_zero(self, weight):
        """Heisenberg genus 1: E_3(enrichment, weight h) = 0."""
        ss = PBWSpectralSequence(1, "Heisenberg")
        assert ss.e3_enrichment_dim(weight) == 0

    # --- Affine sl_2 at genus 1 ---

    @pytest.mark.parametrize("weight", [1, 2, 3])
    def test_sl2_g1_d2_kills_enrichment(self, weight):
        """Affine sl_2 genus 1: d_2 = h * id kills enrichment."""
        ss = PBWSpectralSequence(1, "sl2")
        assert ss.d2_is_isomorphism_on_enrichment(weight)
        assert ss.e3_enrichment_dim(weight) == 0

    # --- Virasoro at genus 1 ---

    @pytest.mark.parametrize("weight", [2, 3, 4, 5])
    def test_virasoro_g1_d2_kills_enrichment(self, weight):
        """Virasoro genus 1: d_2 = h * id kills enrichment at weight h >= 2."""
        ss = PBWSpectralSequence(1, "Virasoro")
        assert ss.d2_is_isomorphism_on_enrichment(weight)
        assert ss.e3_enrichment_dim(weight) == 0

    def test_virasoro_g1_no_enrichment_weight1(self):
        """Virasoro genus 1: no enrichment at weight 1 (T has weight 2)."""
        decomp = CoreEnrichmentDecomposition(1, "Virasoro")
        assert decomp.enrichment_dim_at_weight(1) == 0

    # --- Weight-0 edge case ---

    def test_weight0_no_enrichment(self):
        """Weight 0: no enrichment (vacuum removed)."""
        for alg in ["Heisenberg", "sl2", "Virasoro"]:
            decomp = CoreEnrichmentDecomposition(1, alg)
            assert decomp.enrichment_dim_at_weight(0) == 0

    # --- Higher genus ---

    @pytest.mark.parametrize("weight", [1, 2, 3, 4])
    def test_heisenberg_g2_d2_kills_enrichment(self, weight):
        """Heisenberg genus 2: d_2 kills enrichment on each tensor factor."""
        ss = PBWSpectralSequence(2, "Heisenberg")
        assert ss.d2_is_isomorphism_on_enrichment(weight)
        assert ss.e3_enrichment_dim(weight) == 0


# =========================================================================
# 4. Spectral sequence convergence tests (~20 tests)
# =========================================================================

class TestSpectralSequenceConvergence:
    """E_infty(g) = E_infty(0) for all families and genera."""

    # --- Heisenberg at genus 1 ---

    @pytest.mark.parametrize("degree", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_heisenberg_g1_einfty_vs_g0(self, degree):
        """Heisenberg: E_infty(genus 1) dim = E_infty(genus 0) dim at each degree."""
        ss_g1 = PBWSpectralSequence(1, "Heisenberg")
        core_dim_g1 = ss_g1.core_dim_at_degree(degree)
        g0_dim = _bar_dim_heisenberg_g0(degree)
        # Core at genus 1 = genus 0 bar complex
        assert core_dim_g1 == g0_dim
        # All enrichment killed on E_3
        assert ss_g1.e_infinity_enrichment_is_zero(degree)

    # --- Affine sl_2 at genus 1 ---

    @pytest.mark.parametrize("degree", [1, 2, 3, 4, 5, 6])
    def test_sl2_g1_einfty_vs_g0(self, degree):
        """Affine sl_2: E_infty(genus 1) = E_infty(genus 0) at each degree."""
        ss_g1 = PBWSpectralSequence(1, "sl2")
        core_dim_g1 = ss_g1.core_dim_at_degree(degree)
        g0_dim = _bar_dim_sl2_g0(degree)
        assert core_dim_g1 == g0_dim

    # --- Heisenberg at genus 2 ---

    @pytest.mark.parametrize("degree", [1, 2, 3, 4, 5, 6])
    def test_heisenberg_g2_einfty_vs_g0(self, degree):
        """Heisenberg: E_infty(genus 2) = E_infty(genus 0) at each degree."""
        ss_g2 = PBWSpectralSequence(2, "Heisenberg")
        core_dim_g2 = ss_g2.core_dim_at_degree(degree)
        g0_dim = _bar_dim_heisenberg_g0(degree)
        assert core_dim_g2 == g0_dim
        assert ss_g2.e_infinity_enrichment_is_zero(degree)

    # --- Virasoro at genus 1 ---

    @pytest.mark.parametrize("degree", [1, 2, 3, 4, 5])
    def test_virasoro_g1_einfty_vs_g0(self, degree):
        """Virasoro: E_infty(genus 1) = E_infty(genus 0) at each degree."""
        ss_g1 = PBWSpectralSequence(1, "Virasoro")
        core_dim_g1 = ss_g1.core_dim_at_degree(degree)
        g0_dim = _bar_dim_virasoro_g0(degree)
        assert core_dim_g1 == g0_dim

    # --- Full theorem at each genus ---

    def test_heisenberg_theorem_genus1(self):
        """Heisenberg: full PBW propagation holds at genus 1."""
        ss = PBWSpectralSequence(1, "Heisenberg")
        assert ss.e_infinity_genus_g_equals_genus_0(10)

    def test_heisenberg_theorem_genus2(self):
        """Heisenberg: full PBW propagation holds at genus 2."""
        ss = PBWSpectralSequence(2, "Heisenberg")
        assert ss.e_infinity_genus_g_equals_genus_0(10)

    def test_sl2_theorem_genus1(self):
        """Affine sl_2: full PBW propagation holds at genus 1."""
        ss = PBWSpectralSequence(1, "sl2")
        assert ss.e_infinity_genus_g_equals_genus_0(8)

    def test_virasoro_theorem_genus1(self):
        """Virasoro: full PBW propagation holds at genus 1."""
        ss = PBWSpectralSequence(1, "Virasoro")
        assert ss.e_infinity_genus_g_equals_genus_0(8)

    def test_virasoro_theorem_genus2(self):
        """Virasoro: full PBW propagation holds at genus 2."""
        ss = PBWSpectralSequence(2, "Virasoro")
        assert ss.e_infinity_genus_g_equals_genus_0(8)

    def test_sl2_theorem_genus2(self):
        """Affine sl_2: full PBW propagation holds at genus 2."""
        ss = PBWSpectralSequence(2, "sl2")
        assert ss.e_infinity_genus_g_equals_genus_0(6)


# =========================================================================
# 5. Integration tests (~10 tests)
# =========================================================================

class TestIntegration:
    """Cross-checks with existing bar_complex.py and shadow_metric_census.py."""

    @pytest.mark.parametrize("degree", range(1, 9))
    def test_heisenberg_bar_dim_crosscheck(self, degree):
        """Bar dims from pbw_propagation_engine match bar_complex.py."""
        assert _bar_dim_heisenberg_g0(degree) == bar_dim_heisenberg(degree)

    @pytest.mark.parametrize("degree", range(1, 6))
    def test_sl2_bar_dim_crosscheck(self, degree):
        """Bar cohomology dims from pbw_propagation_engine match bar_complex.py."""
        assert _bar_dim_sl2_g0(degree) == bar_dim_sl2(degree)

    @pytest.mark.parametrize("degree", range(1, 6))
    def test_virasoro_bar_dim_crosscheck(self, degree):
        """Bar cohomology dims from pbw_propagation_engine match bar_complex.py."""
        assert _bar_dim_virasoro_g0(degree) == bar_dim_virasoro(degree)

    def test_heisenberg_bar_dims_known_table(self):
        """Cross-check against KNOWN_BAR_DIMS table in bar_complex.py."""
        known = KNOWN_BAR_DIMS["Heisenberg"]
        for n, expected in known.items():
            assert _bar_dim_heisenberg_g0(n) == expected, f"Mismatch at degree {n}"

    def test_mk1_implies_mk3_heisenberg(self):
        """Full MK1 => MK3 theorem for Heisenberg."""
        thm = PBWPropagationTheorem("Heisenberg", max_genus=2)
        assert thm.verify_mk1_implies_mk3(max_weight=10)

    def test_mk1_implies_mk3_sl2(self):
        """Full MK1 => MK3 theorem for affine sl_2."""
        thm = PBWPropagationTheorem("sl2", max_genus=2)
        assert thm.verify_mk1_implies_mk3(max_weight=8)

    def test_mk1_implies_mk3_virasoro(self):
        """Full MK1 => MK3 theorem for Virasoro."""
        thm = PBWPropagationTheorem("Virasoro", max_genus=2)
        assert thm.verify_mk1_implies_mk3(max_weight=8)

    def test_kappa_values_crosscheck(self):
        """Cross-check kappa values with shadow_metric_census.py.

        The PBW propagation theorem works with kappa > 0 (positive curvature).
        Verify that the standard families have positive kappa at generic levels.
        """
        from sympy import Rational, Symbol
        k = Symbol('k')

        # Heisenberg: kappa = k (positive for k > 0)
        assert kappa_heisenberg(1) == 1
        assert kappa_heisenberg(Rational(1, 2)) == Rational(1, 2)

        # sl_2: kappa = 3(k+2)/4 (positive for k > -2)
        assert kappa_affine_sl2(1) == Rational(9, 4)

        # Virasoro: kappa = c/2 (positive for c > 0)
        assert kappa_virasoro(26) == 13


# =========================================================================
# 6. Independence tests (~10 tests)
# =========================================================================

class TestCurveIndependence:
    """d_coll is the SAME operator at all genera."""

    def test_d_coll_independent_genus_0_to_5(self):
        """d_coll is genus-independent: verified at genera 0 through 5."""
        results = verify_collision_differential_independence(5)
        for g, passes in results.items():
            assert passes, f"d_coll independence failed at genus {g}"

    def test_enrichment_factorization_heisenberg_g1(self):
        """Enrichment factorization for Heisenberg at genus 1."""
        results = verify_enrichment_factorization(1, "Heisenberg", max_weight=8)
        for h, (matches, actual, expected) in results.items():
            assert matches, f"Weight {h}: got {actual}, expected {expected}"

    def test_enrichment_factorization_heisenberg_g2(self):
        """Enrichment factorization for Heisenberg at genus 2."""
        results = verify_enrichment_factorization(2, "Heisenberg", max_weight=8)
        for h, (matches, actual, expected) in results.items():
            assert matches, f"Weight {h}: got {actual}, expected {expected}"

    def test_enrichment_factorization_sl2_g1(self):
        """Enrichment factorization for affine sl_2 at genus 1."""
        results = verify_enrichment_factorization(1, "sl2", max_weight=6)
        for h, (matches, actual, expected) in results.items():
            assert matches, f"Weight {h}: got {actual}, expected {expected}"

    def test_enrichment_factorization_virasoro_g1(self):
        """Enrichment factorization for Virasoro at genus 1."""
        results = verify_enrichment_factorization(1, "Virasoro", max_weight=8)
        for h, (matches, actual, expected) in results.items():
            assert matches, f"Weight {h}: got {actual}, expected {expected}"


# =========================================================================
# 7. Weight space dimension tests
# =========================================================================

class TestWeightSpaceDimensions:
    """Verify weight space dimensions for all families."""

    def test_heisenberg_weight_spaces(self):
        """Heisenberg: dim M_h = p(h) for h >= 1."""
        ws = heisenberg_weight_space_dims(10)
        assert ws[0] == 0, "M_0 = 0 (vacuum removed)"
        for h in range(1, 11):
            assert ws[h] == partition_number(h), f"Mismatch at weight {h}"

    def test_sl2_weight_spaces_weight1(self):
        """Affine sl_2: dim M_1 = 3 (= dim sl_2)."""
        ws = sl2_weight_space_dims(1)
        assert ws[1] == 3

    def test_sl2_weight_spaces_weight2(self):
        """Affine sl_2: dim M_2 = 9 (3-colored partitions of 2).

        Partitions of 2 with 3 colors:
          (2) in 3 colors = 3 ways
          (1,1) in 3 colors: C(3+1,2) = 6 ways? No.
          (1,1) with 3 colors for each 1: 3*3 = 9 ordered, but since
          parts of same size are unordered, it's C(3,2) + 3 = 3 + 3 = 6.
          Total: 3 + 6 = 9.
        """
        ws = sl2_weight_space_dims(2)
        assert ws[2] == 9

    def test_virasoro_weight_spaces(self):
        """Virasoro: dim M_h = partitions of h with parts >= 2."""
        ws = virasoro_weight_space_dims(8)
        assert ws[0] == 0
        assert ws[1] == 0, "No states at weight 1 (T has weight 2)"
        assert ws[2] == 1, "L_{-2}|0>"
        assert ws[3] == 1, "L_{-3}|0>"
        assert ws[4] == 2, "L_{-4}|0>, L_{-2}^2|0>"
        assert ws[5] == 2, "L_{-5}|0>, L_{-3}L_{-2}|0>"
        assert ws[6] == 4, "L_{-6}, L_{-4}L_{-2}, L_{-3}^2, L_{-2}^3"
        assert ws[7] == 4, "L_{-7}, L_{-5}L_{-2}, L_{-4}L_{-3}, L_{-3}L_{-2}^2"
        assert ws[8] == 7

    def test_colored_partitions_match_oeis(self):
        """3-colored partitions match OEIS A000716.

        A000716: 1, 3, 9, 22, 51, 108, 221, 429, 810, 1479, ...
        """
        expected = [1, 3, 9, 22, 51, 108, 221, 429, 810, 1479]
        for n, exp in enumerate(expected):
            assert _colored_partition(n, 3) == exp, f"Mismatch at n={n}"

    def test_partitions_min2_values(self):
        """Partitions with min part 2: known values."""
        expected = {0: 1, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 7, 9: 8}
        for n, exp in expected.items():
            assert _partitions_min_part(n, 2) == exp, f"Mismatch at n={n}"

    def test_colored_partition_single_color_is_partition(self):
        """1-colored partitions = ordinary partitions."""
        for n in range(15):
            assert _colored_partition(n, 1) == partition_number(n), f"Mismatch at n={n}"


# =========================================================================
# 8. Explicit genus-g verification classes
# =========================================================================

class TestHeisenbergGenusgVerification:
    """Explicit tests for HeisenbergGenusgVerification."""

    def test_core_dimension_g1(self):
        """Core dimension matches genus-0 at genus 1."""
        v = HeisenbergGenusgVerification(1)
        for n in range(1, 8):
            matches, core, g0 = v.verify_core_dimension(n)
            assert matches, f"Degree {n}: core={core}, g0={g0}"

    def test_enrichment_dimension_g1(self):
        """Enrichment dimension = p(h) * 1 at genus 1."""
        v = HeisenbergGenusgVerification(1)
        for h in range(1, 8):
            matches, actual, m_h, expected = v.verify_enrichment_dimension(h)
            assert matches, f"Weight {h}: actual={actual}, m_h={m_h}, expected={expected}"

    @pytest.mark.parametrize("weight", [1, 2, 3, 4, 5])
    def test_d2_kills_enrichment_g1(self, weight):
        """d_2 = h * id kills all enrichment at genus 1."""
        v = HeisenbergGenusgVerification(1)
        matches, eigenval, ker_dim = v.verify_d2_kills_enrichment(weight)
        assert matches, f"Weight {weight}: eigenval={eigenval}, ker={ker_dim}"

    def test_e_infinity_equality_g1(self):
        """E_infty(1) = E_infty(0) for Heisenberg."""
        v = HeisenbergGenusgVerification(1)
        assert v.verify_e_infinity_equality(10)

    def test_e_infinity_equality_g2(self):
        """E_infty(2) = E_infty(0) for Heisenberg."""
        v = HeisenbergGenusgVerification(2)
        assert v.verify_e_infinity_equality(8)


class TestAffineSl2GenusgVerification:
    """Explicit tests for AffineSl2GenusgVerification."""

    def test_enrichment_dimension_g1(self):
        """Enrichment dimension at genus 1 for sl_2."""
        v = AffineSl2GenusgVerification(1)
        # Weight 1: dim M_1 = 3, enrichment = 3 * 1 = 3
        matches, actual, expected = v.verify_enrichment_dimension(1)
        assert matches and actual == 3

    @pytest.mark.parametrize("weight", [1, 2, 3])
    def test_d2_kills_enrichment_g1(self, weight):
        """d_2 kills enrichment at genus 1 for sl_2."""
        v = AffineSl2GenusgVerification(1)
        assert v.verify_d2_kills_enrichment(weight)


class TestVirasoroGenusgVerification:
    """Explicit tests for VirasoroGenusgVerification."""

    def test_enrichment_dimension_g1(self):
        """Enrichment dimensions at genus 1 for Virasoro."""
        v = VirasoroGenusgVerification(1)
        # Weight 1: 0 (T has weight 2)
        matches, actual, expected = v.verify_enrichment_dimension(1)
        assert matches and actual == 0
        # Weight 2: 1 (L_{-2}|0>)
        matches, actual, expected = v.verify_enrichment_dimension(2)
        assert matches and actual == 1

    @pytest.mark.parametrize("weight", [2, 3, 4, 5])
    def test_d2_kills_enrichment_g1(self, weight):
        """d_2 kills enrichment at genus 1 for Virasoro."""
        v = VirasoroGenusgVerification(1)
        assert v.verify_d2_kills_enrichment(weight)


# =========================================================================
# 9. PBW propagation theorem full verification
# =========================================================================

class TestPBWPropagationTheorem:
    """Full three-step verification of thm:pbw-propagation."""

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro"])
    def test_step1_all_algebras(self, algebra):
        """Step 1 (curve independence) holds for all algebras."""
        thm = PBWPropagationTheorem(algebra, max_genus=3)
        results = thm.verify_step1()
        for g, passes in results.items():
            assert passes, f"{algebra} genus {g}: Step 1 failed"

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro"])
    def test_step2_all_algebras(self, algebra):
        """Step 2 (core-enrichment decomposition) holds for all algebras."""
        thm = PBWPropagationTheorem(algebra, max_genus=2)
        results = thm.verify_step2()
        for g, props in results.items():
            for prop, passes in props.items():
                assert passes, f"{algebra} genus {g}: Step 2 {prop} failed"

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro"])
    def test_step3_all_algebras(self, algebra):
        """Step 3 (enrichment killing) holds for all algebras."""
        thm = PBWPropagationTheorem(algebra, max_genus=2)
        results = thm.verify_step3()
        for g, passes in results.items():
            assert passes, f"{algebra} genus {g}: Step 3 failed"

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro"])
    def test_conclusion_all_algebras(self, algebra):
        """Conclusion (E_infty(g) = E_infty(0)) holds for all algebras."""
        thm = PBWPropagationTheorem(algebra, max_genus=2)
        results = thm.verify_conclusion()
        for g, passes in results.items():
            assert passes, f"{algebra} genus {g}: Conclusion failed"

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro"])
    def test_full_theorem(self, algebra):
        """Full MK1 => MK3 theorem holds for all standard families."""
        thm = PBWPropagationTheorem(algebra, max_genus=2)
        assert thm.verify_mk1_implies_mk3(max_weight=8)

    def test_heisenberg_up_to_genus5(self):
        """Heisenberg: theorem verified up to genus 5."""
        thm = PBWPropagationTheorem("Heisenberg", max_genus=5)
        assert thm.verify_mk1_implies_mk3(max_weight=6)
