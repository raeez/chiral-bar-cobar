"""Tests for the primitive kernel engine.

Verifies:
  1. Genus-2 shell calculator (all channels, Heisenberg reduction)
  2. Feynman transform expansion (tadpole, genus-1/2 graph sums)
  3. Stable graph census (counts, automorphisms, Euler characteristics)
  4. Branch operator spectral data (squaring identity, special cases)
  5. Operadic cumulant-moment transforms (inverse, low-genus identities)
  6. Cross-checks against manuscript claims (lambda_g^FP, kappa formulas)

Ground truth from:
  - stable_graph_enumeration.py (validated counts + Euler chars)
  - modular_shadow_tower.py (Virasoro quartic Q = 10/[c(5c+22)])
  - modular_master.py (profile structure)
  - Faber (1999): intersection numbers
  - Harer-Zagier (1986): orbifold Euler characteristics
"""
import pytest
from fractions import Fraction

from compute.lib.primitive_kernel_engine import (
    CorollaCoefficients,
    genus2_forcing_loop,
    genus2_forcing_bracket,
    genus2_forcing_planted_forest,
    genus2_forcing,
    genus2_scalar_level,
    tadpole_amplitude,
    genus1_n0_amplitudes,
    genus2_n0_amplitudes_scalar,
    genus2_scalar_polynomial,
    stable_graph_census,
    genus_graph_counts,
    spectral_determinant_series,
    metaplectic_half_density_series,
    verify_metaplectic_squaring,
    branch_spectral_data,
    cumulant_to_moment,
    moment_to_cumulant,
    verify_cumulant_moment_inverse,
    heisenberg_cumulant_moment_table,
    genus_spectral_sequence_page,
    scalar_amplitude_by_loop_level,
    heisenberg_genus2_check,
    partition_count,
    connected_partition_count,
    _integer_partitions,
    _partition_automorphism,
)


# =====================================================================
# 1. Genus-2 shell calculator
# =====================================================================

class TestGenus2Shell:
    """Genus-2 forcing computations for standard families."""

    def test_heisenberg_loop_channel(self):
        """Heisenberg loop contribution = kappa * (-1/12)."""
        result = genus2_forcing_loop(Fraction(1))
        assert result == Fraction(-1, 12)

    def test_heisenberg_loop_channel_kappa_half(self):
        """Heisenberg at kappa = 1/2: loop = -1/24."""
        result = genus2_forcing_loop(Fraction(1, 2))
        assert result == Fraction(-1, 24)

    def test_heisenberg_bracket_vanishes(self):
        """Heisenberg has no cubic, so bracket channel = 0."""
        result = genus2_forcing_bracket(Fraction(0), Fraction(0))
        assert result == Fraction(0)

    def test_heisenberg_planted_forest_vanishes(self):
        """Heisenberg has no quartic, so planted-forest = 0."""
        result = genus2_forcing_planted_forest(Fraction(0), Fraction(0), Fraction(1))
        assert result == Fraction(0)

    def test_heisenberg_full_forcing(self):
        """Full genus-2 forcing for Heisenberg is pure loop."""
        coeffs = CorollaCoefficients.heisenberg()
        forcing = genus2_forcing(coeffs)
        assert forcing["bracket"] == Fraction(0)
        assert forcing["planted_forest"] == Fraction(0)
        assert forcing["total"] == forcing["loop"]

    def test_virasoro_quartic_channel_nonzero(self):
        """Virasoro has nonzero quartic planted-forest contribution."""
        coeffs = CorollaCoefficients.virasoro(c=Fraction(1))
        forcing = genus2_forcing(coeffs)
        assert forcing["planted_forest"] != Fraction(0)

    def test_virasoro_all_channels_active(self):
        """For Virasoro, all three channels are nonzero."""
        coeffs = CorollaCoefficients.virasoro(c=Fraction(1))
        forcing = genus2_forcing(coeffs)
        assert forcing["loop"] != Fraction(0)
        assert forcing["bracket"] != Fraction(0)
        assert forcing["planted_forest"] != Fraction(0)

    def test_affine_sl2_no_quartic(self):
        """Affine sl_2 has no quartic contact, so planted-forest = 0."""
        coeffs = CorollaCoefficients.affine_sl2()
        forcing = genus2_forcing(coeffs)
        assert forcing["planted_forest"] == Fraction(0)

    def test_affine_sl2_bracket_nonzero(self):
        """Affine sl_2 has cubic coupling, so bracket channel is nonzero."""
        coeffs = CorollaCoefficients.affine_sl2()
        forcing = genus2_forcing(coeffs)
        assert forcing["bracket"] != Fraction(0)


class TestGenus2ScalarLevel:
    """Scalar-level genus-2 free energy F_2 = kappa * lambda_2^FP."""

    def test_lambda2_fp_value(self):
        """lambda_2^FP = 7/5760."""
        result = genus2_scalar_level(Fraction(1))
        assert result == Fraction(7, 5760)

    def test_kappa_linearity(self):
        """F_2 is linear in kappa at the scalar level."""
        f2_1 = genus2_scalar_level(Fraction(1))
        f2_2 = genus2_scalar_level(Fraction(2))
        assert f2_2 == 2 * f2_1

    def test_heisenberg_genus2_exact(self):
        """F_2(H_1) = 7/5760."""
        result = genus2_scalar_level(Fraction(1))
        assert result == Fraction(7, 5760)


# =====================================================================
# 2. Feynman transform expansion
# =====================================================================

class TestFeynmanExpansion:
    """Graph-by-graph amplitude decomposition."""

    def test_tadpole_at_kappa_1(self):
        """Tadpole amplitude = kappa/2 = 1/2 at kappa = 1."""
        result = tadpole_amplitude(Fraction(1))
        assert result == Fraction(1, 2)

    def test_tadpole_kappa_scaling(self):
        """Tadpole is linear in kappa."""
        assert tadpole_amplitude(Fraction(3)) == Fraction(3, 2)

    def test_genus1_n0_two_graphs(self):
        """Genus 1, n = 0: exactly 2 graphs contribute."""
        amps = genus1_n0_amplitudes(Fraction(1))
        # The result dict has individual entries plus 'total'
        non_total = {k: v for k, v in amps.items() if k != "total"}
        assert len(non_total) == 2

    def test_genus2_n0_six_graphs(self):
        """Genus 2, n = 0: exactly 6 graphs contribute."""
        amps = genus2_n0_amplitudes_scalar(Fraction(1))
        non_total = {k: v for k, v in amps.items() if k != "total"}
        assert len(non_total) == 6

    def test_genus2_smooth_amplitude(self):
        """Smooth genus-2 curve: 0 edges, |Aut|=1, amplitude = 1."""
        amps = genus2_n0_amplitudes_scalar(Fraction(1))
        assert amps["smooth_g2"] == Fraction(1)

    def test_genus2_banana_amplitude(self):
        """Banana graph (2 self-loops): kappa^2 / 8."""
        amps = genus2_n0_amplitudes_scalar(Fraction(1))
        assert amps["banana_g0"] == Fraction(1, 8)

    def test_genus2_theta_amplitude(self):
        """Theta graph (3 parallel edges): kappa^3 / 12."""
        amps = genus2_n0_amplitudes_scalar(Fraction(1))
        assert amps["theta_00"] == Fraction(1, 12)

    def test_genus2_polynomial_degree0(self):
        """Scalar polynomial: c_0 = 1 (smooth graph only)."""
        poly = genus2_scalar_polynomial()
        assert poly.get(0, Fraction(0)) == Fraction(1)

    def test_genus2_polynomial_degree1(self):
        """Scalar polynomial: c_1 = 1/2 + 1/2 = 1 (irr_node + separating)."""
        poly = genus2_scalar_polynomial()
        assert poly.get(1, Fraction(0)) == Fraction(1)

    def test_genus2_polynomial_degree3(self):
        """Scalar polynomial: c_3 = 1/12 (theta graph only)."""
        poly = genus2_scalar_polynomial()
        assert poly.get(3, Fraction(0)) == Fraction(1, 12)


# =====================================================================
# 3. Stable graph census
# =====================================================================

class TestStableGraphCensus:
    """Stable graph enumeration cross-checks."""

    def test_genus0_n3_count(self):
        """Genus 0, n = 3: exactly 1 stable graph (the point)."""
        census = stable_graph_census(0, 3)
        assert census["count"] == 1

    def test_genus0_n4_count(self):
        """Genus 0, n = 4: exactly 4 stable graphs."""
        census = stable_graph_census(0, 4)
        assert census["count"] == 4

    def test_genus1_n0_unstable(self):
        """Genus 1, n = 0: M_{1,0} is unstable (2g-2+n = 0).

        The stable_graph_census requires 2g-2+n > 0.  The genus-1 n=0
        graphs (smooth torus + self-loop) exist in the explicit
        enumeration as a book-keeping convention for the Feynman
        transform boundary, but M_{1,0} is the unstable stratum.
        """
        census = stable_graph_census(1, 0)
        assert census["count"] == 0

    def test_genus1_n1_count(self):
        """Genus 1, n = 1: exactly 2 stable graphs."""
        census = stable_graph_census(1, 1)
        assert census["count"] == 2

    def test_genus1_n2_count(self):
        """Genus 1, n = 2: exactly 5 stable graphs."""
        census = stable_graph_census(1, 2)
        assert census["count"] == 5

    def test_genus2_n0_count(self):
        """Genus 2, n = 0: exactly 6 stable graphs."""
        census = stable_graph_census(2, 0)
        assert census["count"] == 6

    def test_genus2_aut_spectrum(self):
        """Genus 2, n = 0: automorphism spectrum [1, 2, 2, 2, 8, 12]."""
        census = stable_graph_census(2, 0)
        assert census["aut_spectrum"] == [1, 2, 2, 2, 8, 12]

    def test_unstable_returns_empty(self):
        """M_{0,2} is unstable: no stable graphs."""
        census = stable_graph_census(0, 2)
        assert census["count"] == 0

    def test_genus2_by_edges(self):
        """Genus 2, n = 0: edge distribution {0:1, 1:2, 2:2, 3:1}."""
        census = stable_graph_census(2, 0)
        assert census["by_edges"] == {0: 1, 1: 2, 2: 2, 3: 1}

    def test_genus2_by_h1(self):
        """Genus 2, n = 0: h^1 distribution {0:2, 1:2, 2:2}.

        h^1 = 0: smooth (g=2) + separating (g=(1,1), 1 edge, h^1=0)
        h^1 = 1: irr_node (g=1, 1 self-loop) + mixed (g=(0,1), 2 edges)
        h^1 = 2: banana (g=0, 2 self-loops) + theta (g=(0,0), 3 edges)
        """
        census = stable_graph_census(2, 0)
        assert census["by_h1"] == {0: 2, 1: 2, 2: 2}
        assert sum(census["by_h1"].values()) == 6


# =====================================================================
# 4. Branch operator spectral data
# =====================================================================

class TestBranchSpectralData:
    """Metaplectic half-density and spectral determinant."""

    def test_rank1_determinant(self):
        """det(1 - lambda*x) = 1 - lambda*x for rank 1."""
        eigenvalues = (Fraction(3),)
        coeffs = spectral_determinant_series(eigenvalues, 3)
        assert coeffs[0] == Fraction(1)
        assert coeffs[1] == Fraction(-3)
        assert coeffs[2] == Fraction(0)
        assert coeffs[3] == Fraction(0)

    def test_rank2_determinant(self):
        """det(1 - xT) = 1 - (a+b)x + ab*x^2 for diagonal T with eigenvalues a, b."""
        a, b = Fraction(2), Fraction(5)
        coeffs = spectral_determinant_series((a, b), 4)
        assert coeffs[0] == Fraction(1)
        assert coeffs[1] == -(a + b)
        assert coeffs[2] == a * b
        assert coeffs[3] == Fraction(0)

    def test_rank1_squaring(self):
        """Metaplectic half-density squares to determinant, rank 1."""
        assert verify_metaplectic_squaring((Fraction(1, 3),), 8)

    def test_rank2_squaring(self):
        """Metaplectic half-density squares to determinant, rank 2."""
        assert verify_metaplectic_squaring((Fraction(1, 2), Fraction(1, 3)), 6)

    def test_rank3_squaring(self):
        """Metaplectic half-density squares to determinant, rank 3."""
        assert verify_metaplectic_squaring(
            (Fraction(1, 4), Fraction(1, 5), Fraction(1, 7)), 5
        )

    def test_zero_eigenvalues(self):
        """All-zero eigenvalues: det = 1, half-density = 1."""
        coeffs = spectral_determinant_series((Fraction(0), Fraction(0)), 4)
        assert coeffs == [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
        half = metaplectic_half_density_series((Fraction(0), Fraction(0)), 4)
        assert half[0] == Fraction(1)
        for k in range(1, 5):
            assert half[k] == Fraction(0)

    def test_branch_data_structure(self):
        """Branch spectral data returns correct structure."""
        data = branch_spectral_data((Fraction(1, 2), Fraction(1, 3)))
        assert data["rank"] == 2
        assert data["squaring_verified"] is True
        assert data["trace"] == Fraction(5, 6)

    def test_identity_eigenvalue_squaring(self):
        """Eigenvalue = 1: det(1-x) = 1-x, half = (1-x)^{1/2}."""
        assert verify_metaplectic_squaring((Fraction(1),), 10)


# =====================================================================
# 5. Operadic cumulant-moment transforms
# =====================================================================

class TestCumulantMoment:
    """Cumulant-moment (exp/log) on genus expansion."""

    def test_inverse_property(self):
        """cumulant -> moment -> cumulant is the identity."""
        assert verify_cumulant_moment_inverse(max_genus=5)

    def test_F1_equals_Z1(self):
        """At genus 1, F_1 = Z_1 (no disconnected contributions)."""
        cumulants = {1: Fraction(7, 13)}
        moments = cumulant_to_moment(cumulants, 1)
        assert moments[1] == cumulants[1]

    def test_Z2_F2_relation(self):
        """Z_2 = F_2 + (1/2) F_1^2."""
        F1, F2 = Fraction(1, 24), Fraction(7, 5760)
        cumulants = {1: F1, 2: F2}
        moments = cumulant_to_moment(cumulants, 2)
        expected = F2 + Fraction(1, 2) * F1 ** 2
        assert moments[2] == expected

    def test_Z3_F3_relation(self):
        """Z_3 = F_3 + F_1 * F_2 + (1/6) F_1^3."""
        F1 = Fraction(1, 24)
        F2 = Fraction(7, 5760)
        F3 = Fraction(31, 967680)
        cumulants = {1: F1, 2: F2, 3: F3}
        moments = cumulant_to_moment(cumulants, 3)
        expected = F3 + F1 * F2 + Fraction(1, 6) * F1 ** 3
        assert moments[3] == expected

    def test_moment_to_cumulant_genus2(self):
        """F_2 = Z_2 - (1/2) Z_1^2."""
        Z1, Z2 = Fraction(3, 7), Fraction(5, 11)
        moments = {1: Z1, 2: Z2}
        cumulants = moment_to_cumulant(moments, 2)
        expected_F2 = Z2 - Fraction(1, 2) * Z1 ** 2
        assert cumulants[2] == expected_F2

    def test_moment_to_cumulant_genus3(self):
        """F_3 = Z_3 - Z_1 Z_2 + (1/3) Z_1^3."""
        Z1 = Fraction(1, 5)
        Z2 = Fraction(1, 7)
        Z3 = Fraction(1, 11)
        moments = {1: Z1, 2: Z2, 3: Z3}
        cumulants = moment_to_cumulant(moments, 3)
        expected_F3 = Z3 - Z1 * Z2 + Fraction(1, 3) * Z1 ** 3
        assert cumulants[3] == expected_F3

    def test_heisenberg_table_genus1(self):
        """Heisenberg F_1 = kappa/24 at kappa = 1."""
        table = heisenberg_cumulant_moment_table(Fraction(1), max_genus=1)
        assert table["cumulants"][1] == Fraction(1, 24)

    def test_heisenberg_Z2_includes_disconnected(self):
        """Heisenberg Z_2 = F_2 + (1/2) F_1^2 (disconnected part nonzero)."""
        table = heisenberg_cumulant_moment_table(Fraction(1), max_genus=2)
        F1 = table["cumulants"][1]
        F2 = table["cumulants"][2]
        Z2 = table["moments"][2]
        assert Z2 == F2 + Fraction(1, 2) * F1 ** 2

    def test_inverse_with_random_data(self):
        """Round-trip with non-trivial data at genus 4."""
        cumulants = {
            1: Fraction(3, 7),
            2: Fraction(-5, 13),
            3: Fraction(11, 17),
            4: Fraction(-2, 19),
        }
        moments = cumulant_to_moment(cumulants, 4)
        recovered = moment_to_cumulant(moments, 4)
        for g in range(1, 5):
            assert recovered[g] == cumulants[g], f"Mismatch at genus {g}"


# =====================================================================
# 6. Integer partition data
# =====================================================================

class TestPartitions:
    """Integer partition helpers."""

    def test_partition_counts(self):
        """p(n) for small n: 1, 1, 2, 3, 5, 7, 11."""
        expected = [1, 1, 2, 3, 5, 7, 11]
        for n, p in enumerate(expected):
            assert partition_count(n) == p, f"p({n}) = {partition_count(n)}, expected {p}"

    def test_connected_partition_count(self):
        """Trivial partition (g) has exactly 1 element for g >= 1."""
        for g in range(1, 8):
            assert connected_partition_count(g) == 1

    def test_partition_automorphism_trivial(self):
        """Partition (n) has |Aut| = 1."""
        for n in range(1, 8):
            assert _partition_automorphism((n,)) == 1

    def test_partition_automorphism_repeated(self):
        """Partition (1, 1) has |Aut| = 2!, (1, 1, 1) has |Aut| = 3!."""
        assert _partition_automorphism((1, 1)) == 2
        assert _partition_automorphism((1, 1, 1)) == 6
        assert _partition_automorphism((2, 2)) == 2
        assert _partition_automorphism((2, 1, 1)) == 2
        assert _partition_automorphism((1, 1, 1, 1)) == 24


# =====================================================================
# 7. Cross-checks against manuscript
# =====================================================================

class TestManuscriptCrossChecks:
    """Verify computations against explicit manuscript values."""

    def test_lambda1_fp(self):
        """lambda_1^FP = 1/24 (Faber-Pandharipande)."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda2_fp(self):
        """lambda_2^FP = 7/5760."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda3_fp(self):
        """lambda_3^FP = 31/967680."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        assert _lambda_fp_exact(3) == Fraction(31, 967680)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        coeffs = CorollaCoefficients.virasoro(c=Fraction(26))
        assert coeffs.kappa == Fraction(13)

    def test_affine_sl2_kappa(self):
        """kappa(V_k(sl_2)) = 3(k+2)/2."""
        coeffs = CorollaCoefficients.affine_sl2(k=Fraction(1))
        assert coeffs.kappa == Fraction(9, 2)

    def test_virasoro_quartic_c1(self):
        """Q^contact_Vir(c=1) = 10/27."""
        coeffs = CorollaCoefficients.virasoro(c=Fraction(1))
        assert coeffs.quartic == Fraction(10, 27)

    def test_virasoro_quartic_c25(self):
        """Q^contact_Vir(c=25) = 10/(25*147) = 2/735."""
        coeffs = CorollaCoefficients.virasoro(c=Fraction(25))
        assert coeffs.quartic == Fraction(2, 735)

    def test_heisenberg_genus2_reduces_to_scalar(self):
        """For Heisenberg, genus-2 forcing is pure loop (no bracket, no pf)."""
        check = heisenberg_genus2_check()
        assert check["bracket_is_zero"]
        assert check["pf_is_zero"]

    def test_genus2_orbifold_euler(self):
        """chi^orb(M-bar_{2,0}) = -181/1440 (from orbifold vertex-product formula)."""
        from compute.lib.stable_graph_enumeration import (
            genus2_stable_graphs_n0, orbifold_euler_characteristic
        )
        graphs = genus2_stable_graphs_n0()
        chi = orbifold_euler_characteristic(graphs)
        assert chi == Fraction(-181, 1440)


# =====================================================================
# 8. Genus spectral sequence
# =====================================================================

class TestGenusSpectralSequence:
    """E_1 page decomposition by loop number."""

    def test_genus1_n0_spectral(self):
        """Genus 1, n = 0: M_{1,0} unstable, empty spectral sequence."""
        page = genus_spectral_sequence_page(1, 0)
        assert page == {}

    def test_genus1_n1_spectral(self):
        """Genus 1, n = 1: 2 stable graphs, h^1 in {0, 1}."""
        page = genus_spectral_sequence_page(1, 1)
        assert sum(page.values()) == 2

    def test_genus2_n0_spectral_total(self):
        """Genus 2, n = 0: 6 total graphs across all loop levels."""
        page = genus_spectral_sequence_page(2, 0)
        assert sum(page.values()) == 6

    def test_scalar_amplitude_sums_correctly(self):
        """Sum over loop levels equals total graph sum at genus 2."""
        kappa = Fraction(3)
        by_h1 = scalar_amplitude_by_loop_level(2, 0, kappa)
        total = sum(by_h1.values())
        from compute.lib.stable_graph_enumeration import genus2_stable_graphs_n0, graph_sum_scalar
        expected = graph_sum_scalar(genus2_stable_graphs_n0(), kappa)
        assert total == expected

    def test_unstable_spectral_sequence(self):
        """Unstable moduli gives empty spectral sequence."""
        page = genus_spectral_sequence_page(0, 1)
        assert page == {}
