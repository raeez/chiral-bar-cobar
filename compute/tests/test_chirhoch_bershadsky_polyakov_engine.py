"""Tests for chiral Hochschild cohomology of the Bershadsky-Polyakov algebra.

First non-principal W-algebra ChirHoch computation.

Organized by:
  I.    ChirHoch^0 = Z(BP_k) (center)
  II.   ChirHoch^2 = Z((BP_k)!)^v (Koszul dual center)
  III.  ChirHoch^1 (derivation analysis)
  IV.   Hochschild polynomial P_BP(t)
  V.    Deformation-obstruction
  VI.   Koszul duality
  VII.  N=2 constraints
  VIII. Comparison with principal W-algebras
  IX.   Special levels
  X.    Master computation and verification

References:
  thm:hochschild-polynomial-growth (chiral_hochschild_koszul.tex)
  thm:bp-strict (subregular_hook_frontier.tex)
  thm:pbw-slodowy-collapse (subregular_hook_frontier.tex)
  sl3_subregular_bar.py (BP data)
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.chirhoch_bershadsky_polyakov_engine import (
    # Data
    BPChiralData,
    bp_data,
    # ChirHoch^0
    center_dimension_bp,
    # ChirHoch^2
    center_dimension_koszul_dual_bp,
    # ChirHoch^1
    BPDerivationAnalysis,
    derivation_analysis_bp,
    # Polynomial
    BPHochschildPolynomial,
    compute_bp_hochschild_polynomial,
    # Deformation-obstruction
    BPDeformationObstruction,
    deformation_obstruction_analysis_bp,
    all_deformations_unobstructed_bp,
    # Koszul duality
    koszul_duality_check_bp,
    # N=2
    n2_sca_constraints_on_chirhoch,
    # Comparison
    comparison_with_principal,
    # Special levels
    special_level_analysis,
    # Master
    BPChirHochResult,
    compute_chirhoch_bp,
    # Verification
    verify_chirhoch_bp,
    verify_theorem_h_for_bp,
)

from compute.lib.sl3_subregular_bar import (
    bp_anomaly_ratio,
    bp_central_charge,
    bp_dual_level,
    bp_koszul_conductor,
    kappa_path1_anomaly_ratio,
    kappa_all_paths_agree,
    GENERATORS,
)


k = Symbol('k')


# ===================================================================
# I. ChirHoch^0 = Z(BP_k) — center
# ===================================================================

class TestChirHoch0:
    """dim ChirHoch^0(BP_k) = 1 at generic level."""

    def test_center_dimension(self):
        """Z(BP_k) = C (vacuum) at generic k.
        # VERIFIED: [DC] J_{(0)} separates charge sectors, L_0 separates weights,
        #           G+_{(1/2)}/G-_{(1/2)} connect sectors; only vacuum survives
        # VERIFIED: [LT] Arakawa 2005 Thm 4.1: BP_k simple at generic k,
        #           hence center = C
        """
        assert center_dimension_bp() == 1

    def test_center_at_level_0(self):
        """Z(BP_0) = C (level 0 is generic)."""
        assert center_dimension_bp(0) == 1

    def test_center_at_level_1(self):
        """Z(BP_1) = C (level 1 is generic)."""
        assert center_dimension_bp(1) == 1


# ===================================================================
# II. ChirHoch^2 = Z((BP_k)!)^v — Koszul dual center
# ===================================================================

class TestChirHoch2:
    """dim ChirHoch^2(BP_k) = 1 at generic level."""

    def test_koszul_dual_center_dimension(self):
        """Z((BP_k)!) = Z(BP_{-k-6}) = C at generic dual level.
        # VERIFIED: [SY] Koszul duality: dim H^2(A) = dim Z(A!)
        # VERIFIED: [DC] (BP_k)! = BP_{-k-6}, self-dual family; center of
        #           dual is vacuum at generic -k-6
        """
        assert center_dimension_koszul_dual_bp() == 1

    def test_dual_level(self):
        """Dual level k' = -k - 6."""
        assert simplify(bp_dual_level() - (-k - 6)) == 0


# ===================================================================
# III. ChirHoch^1 — derivation analysis
# ===================================================================

class TestChirHoch1:
    """dim ChirHoch^1(BP_k) = 2 (J-current + c-deformation)."""

    def test_total_outer_derivations(self):
        """Der(BP)/Inn(BP) = C^2 at generic level.
        # VERIFIED: [DC] derivation analysis: J weight-1 current gives 1 outer,
        #           c-deformation gives 1 outer, fermionic G+/G- give 0
        # VERIFIED: [CF] cross-family: matches betagamma pattern
        #           (1 weight-1 bosonic current => ChirHoch^1 = 2)
        """
        da = derivation_analysis_bp()
        assert da.dim_chirhoch1 == 2

    def test_j_current_contribution(self):
        """J (weight 1, bosonic) contributes 1 outer derivation.
        # VERIFIED: [DC] J is weight-1 bosonic current; parallels affine KM
        #           where each weight-1 current gives 1 outer derivation
        # VERIFIED: [CF] Heisenberg (1 weight-1 gen): H^1 = 1;
        #           affine sl_2 (3 weight-1 gens): H^1 = 3
        """
        da = derivation_analysis_bp()
        assert da.j_current_contribution == 1

    def test_c_deformation_contribution(self):
        """Level/c deformation contributes 1 outer derivation.
        # VERIFIED: [DC] BP_k is a 1-parameter family parametrized by k
        # VERIFIED: [CF] all W-algebras have 1 c-deformation direction
        """
        da = derivation_analysis_bp()
        assert da.c_deformation_contribution == 1

    def test_fermionic_contribution_zero(self):
        """G+, G- (fermionic, weight 3/2) contribute 0 to bosonic H^1.
        # VERIFIED: [DC] fermionic generators give odd (anticommuting) derivations,
        #           not in the bosonic part of ChirHoch^1
        # VERIFIED: [SY] N=2 SUSY locks G+/G- to J and T
        """
        da = derivation_analysis_bp()
        assert da.fermionic_contribution == 0

    def test_inner_derivations_listed(self):
        """Inner derivations: L_0 and J_{(0)}."""
        da = derivation_analysis_bp()
        assert len(da.inner_derivations) == 2

    def test_decomposition_adds_up(self):
        """j_current + c_deformation + fermionic = total_outer."""
        da = derivation_analysis_bp()
        assert (da.j_current_contribution
                + da.c_deformation_contribution
                + da.fermionic_contribution) == da.total_outer


# ===================================================================
# IV. Hochschild polynomial
# ===================================================================

class TestHochschildPolynomial:
    """P_BP(t) = 1 + 2t + t^2."""

    def test_polynomial_coefficients(self):
        """P_BP = [1, 2, 1].
        # VERIFIED: [DC] H^0=1, H^1=2, H^2=1 from sections above
        # VERIFIED: [CF] matches betagamma P(t) = 1 + 2t + t^2
        """
        poly = compute_bp_hochschild_polynomial()
        assert poly.coefficients == [1, 2, 1]

    def test_total_dimension(self):
        """Total dim = 4.
        # VERIFIED: [DC] 1 + 2 + 1 = 4
        # VERIFIED: [CF] matches betagamma/bc total = 4
        """
        poly = compute_bp_hochschild_polynomial()
        assert poly.total_dimension == 4

    def test_euler_characteristic(self):
        """chi = P(-1) = 1 - 2 + 1 = 0.
        # VERIFIED: [DC] direct computation
        # VERIFIED: [CF] betagamma chi = 1 - 2 + 1 = 0 (same)
        """
        poly = compute_bp_hochschild_polynomial()
        assert poly.euler_characteristic == 0

    def test_palindromic(self):
        """P_BP is palindromic: p0 = p2 = 1.
        # VERIFIED: [SY] Koszul duality: for self-dual family, p0 = p2
        # VERIFIED: [DC] both 1
        """
        poly = compute_bp_hochschild_polynomial()
        assert poly.is_palindromic

    def test_evaluate_at_1(self):
        """P_BP(1) = total dimension = 4."""
        poly = compute_bp_hochschild_polynomial()
        assert poly.evaluate(1) == 4

    def test_evaluate_at_minus_1(self):
        """P_BP(-1) = Euler characteristic = 0."""
        poly = compute_bp_hochschild_polynomial()
        assert poly.evaluate(-1) == 0


# ===================================================================
# V. Deformation-obstruction
# ===================================================================

class TestDeformationObstruction:
    """All deformations of BP_k are unobstructed."""

    def test_all_unobstructed(self):
        """[xi, xi] = 0 for all xi in ChirHoch^1(BP_k).
        # VERIFIED: [DC] BP_k exists as smooth family for all generic k
        # VERIFIED: [LT] Feigin-Semikhatov 2004: BP_k defined for all k != -3
        """
        assert all_deformations_unobstructed_bp()

    def test_two_obstruction_classes(self):
        """Two obstruction classes, both vanishing."""
        obs = deformation_obstruction_analysis_bp()
        assert len(obs) == 2
        assert all(o.is_unobstructed for o in obs)

    def test_j_current_unobstructed(self):
        """J-current deformation is unobstructed."""
        obs = deformation_obstruction_analysis_bp()
        j_obs = [o for o in obs if "j_current" in o.derivation_name]
        assert len(j_obs) == 1
        assert j_obs[0].is_unobstructed

    def test_c_deformation_unobstructed(self):
        """c-deformation is unobstructed."""
        obs = deformation_obstruction_analysis_bp()
        c_obs = [o for o in obs if "c_deformation" in o.derivation_name]
        assert len(c_obs) == 1
        assert c_obs[0].is_unobstructed


# ===================================================================
# VI. Koszul duality
# ===================================================================

class TestKoszulDuality:
    """Koszul duality checks for BP_k."""

    def test_koszul_duality_satisfied(self):
        """dim H^n(BP_k) = dim H^{2-n}((BP_k)!) for n = 0, 1, 2.
        # VERIFIED: [SY] Koszul duality theorem (thm:main-koszul-hoch)
        # VERIFIED: [DC] betti = [1,2,1], dual betti = [1,2,1], checks pass
        """
        kd = koszul_duality_check_bp()
        assert kd["all_checks_pass"]

    def test_self_dual_family(self):
        """(2,1) is self-transpose: BP_k is in a self-dual family."""
        kd = koszul_duality_check_bp()
        assert kd["self_dual_family"]

    def test_koszul_conductor_196(self):
        """K_BP = c(k) + c(-k-6) = 196.
        # AP140: K_BP = 196, NOT 2
        # VERIFIED: [DC] symbolic: simplify(c(k) + c(-k-6)) = 196
        # VERIFIED: [NE] c(0) + c(-6) = -6 + 202 = 196
        """
        K = bp_koszul_conductor()
        assert simplify(K - 196) == 0

    def test_koszul_conductor_numerical(self):
        """K_BP at k=0: c(0) + c(-6) = -6 + 202 = 196.
        # VERIFIED: [NE] c(0) = 2 - 24*1/3 = -6; c(-6) = 2 - 24*25/(-3) = 202
        # VERIFIED: [DC] -6 + 202 = 196
        """
        c0 = bp_central_charge(0)
        c_dual_0 = bp_central_charge(-6)
        assert simplify(c0 + c_dual_0 - 196) == 0


# ===================================================================
# VII. N=2 constraints
# ===================================================================

class TestN2Constraints:
    """N=2 SCA structure constrains ChirHoch^1."""

    def test_j_level_locked(self):
        """J-level kJ = c/3 is locked to c by N=2 structure."""
        n2 = n2_sca_constraints_on_chirhoch()
        assert n2["j_level_locked"]

    def test_fermionic_locked(self):
        """G+, G- are locked by SUSY."""
        n2 = n2_sca_constraints_on_chirhoch()
        assert n2["fermionic_locked_by_susy"]

    def test_naive_vs_actual(self):
        """Naive 4 derivations reduced to 2 by N=2 constraints."""
        n2 = n2_sca_constraints_on_chirhoch()
        assert n2["naive_derivation_count"] == 4
        assert n2["actual_outer_derivations"] == 2


# ===================================================================
# VIII. Comparison with principal W-algebras
# ===================================================================

class TestComparisonWithPrincipal:
    """BP vs principal W-algebras."""

    def test_bp_has_extra_derivation(self):
        """BP has 1 extra outer derivation vs principal W_N.
        # VERIFIED: [CF] principal W_N: H^1 = 1; BP: H^1 = 2
        # VERIFIED: [DC] extra derivation from weight-1 current J (absent in principal)
        """
        comp = comparison_with_principal()
        assert comp["bp_polynomial"] == [1, 2, 1]
        assert comp["principal_w2_polynomial"] == [1, 1, 1]

    def test_general_formula_n1(self):
        """General formula: dim H^1 = n_1 + 1 where n_1 = # weight-1 bosonic currents."""
        comp = comparison_with_principal()
        assert comp["bp_n1"] == 1
        assert comp["principal_n1"] == 0

    def test_bp_matches_betagamma(self):
        """BP polynomial matches betagamma (both have 1 weight-1 current).
        # VERIFIED: [CF] betagamma: P(t) = 1 + 2t + t^2; BP: P(t) = 1 + 2t + t^2
        """
        comp = comparison_with_principal()
        assert comp["bp_polynomial"] == [1, 2, 1]
        assert comp["bp_total"] == 4


# ===================================================================
# IX. Special levels
# ===================================================================

class TestSpecialLevels:
    """ChirHoch at special levels of BP_k."""

    def test_generic_result(self):
        """Generic result: [1, 2, 1]."""
        sl = special_level_analysis()
        assert sl["generic_result"] == {"H0": 1, "H1": 2, "H2": 1, "total": 4}

    def test_critical_level(self):
        """Critical level is k = -3."""
        sl = special_level_analysis()
        assert sl["critical_level"] == -3

    def test_level_0_central_charge(self):
        """c(0) = -6.
        # VERIFIED: [DC] 2 - 24*1/3 = 2 - 8 = -6
        # VERIFIED: [NE] numerical evaluation
        """
        sl = special_level_analysis()
        assert sl["level_0"]["c"] == -6

    def test_level_1_central_charge(self):
        """c(1) = -22.
        # VERIFIED: [DC] 2 - 24*4/4 = 2 - 24 = -22
        # VERIFIED: [NE] numerical evaluation
        """
        sl = special_level_analysis()
        assert sl["level_1"]["c"] == -22


# ===================================================================
# X. Master computation and verification
# ===================================================================

class TestMasterComputation:
    """End-to-end computation and verification."""

    def test_compute_chirhoch_bp(self):
        """Master computation returns correct result."""
        r = compute_chirhoch_bp()
        assert r.dim_H0 == 1
        assert r.dim_H1 == 2
        assert r.dim_H2 == 1
        assert r.total_dimension == 4

    def test_betti_numbers(self):
        """Betti numbers [1, 2, 1]."""
        r = compute_chirhoch_bp()
        assert r.betti_numbers == [1, 2, 1]

    def test_concentrated_in_0_1_2(self):
        """Theorem H: concentration in {0, 1, 2}."""
        r = compute_chirhoch_bp()
        assert r.concentrated_in_0_1_2

    def test_all_unobstructed(self):
        """All deformations unobstructed."""
        r = compute_chirhoch_bp()
        assert r.all_unobstructed

    def test_koszul_duality_in_result(self):
        """Koszul duality check passes in master result."""
        r = compute_chirhoch_bp()
        assert r.koszul_duality["all_checks_pass"]

    def test_verify_chirhoch_bp_all_pass(self):
        """Full verification suite: all checks pass."""
        results = verify_chirhoch_bp()
        for check_name, passed in results.items():
            assert passed, f"Verification check '{check_name}' failed"

    def test_theorem_h_satisfied(self):
        """Theorem H is satisfied for BP."""
        th = verify_theorem_h_for_bp()
        assert th["theorem_h_satisfied"]
        assert th["concentrated_in_0_1_2"]
        assert th["is_chirally_koszul"]
        assert th["palindromic"]

    def test_anomaly_ratio(self):
        """rho(BP) = 1/6.
        # VERIFIED: [DC] 1/1 - 2/3 - 2/3 + 1/2 = 1/6 (sum over generators)
        # VERIFIED: [NE] 1.0 - 0.6667 - 0.6667 + 0.5 = 0.1667 = 1/6
        """
        assert bp_anomaly_ratio() == Rational(1, 6)

    def test_kappa_paths_agree(self):
        """Three kappa computation paths agree.
        # VERIFIED: [DC] path 1 (rho*c), path 2 (DS from affine), path 3 (complementarity)
        # VERIFIED: [SY] complementarity: kappa(k) + kappa(-k-6) = 98/3
        """
        paths = kappa_all_paths_agree()
        assert paths["all_agree"]


# ===================================================================
# XI. Cross-checks with existing engines
# ===================================================================

class TestCrossChecks:
    """Cross-check with existing ChirHoch engine for standard families."""

    def test_bp_generators_data(self):
        """BP generator data matches sl3_subregular_bar.py."""
        data = bp_data()
        assert data.n_generators == 4
        assert set(data.generators.keys()) == {"J", "G+", "G-", "T"}

    def test_weight_one_bosonic(self):
        """Only J is weight-1 bosonic."""
        data = bp_data()
        assert data.weight_one_bosonic == ["J"]

    def test_fermionic_generators(self):
        """G+ and G- are fermionic."""
        data = bp_data()
        assert set(data.fermionic_generators) == {"G+", "G-"}

    def test_bosonic_generators(self):
        """J and T are bosonic."""
        data = bp_data()
        assert set(data.bosonic_generators) == {"J", "T"}

    def test_central_charge_at_0(self):
        """c(0) = -6."""
        data = bp_data(0)
        assert simplify(data.central_charge - (-6)) == 0

    def test_central_charge_at_1(self):
        """c(1) = -22."""
        data = bp_data(1)
        assert simplify(data.central_charge - (-22)) == 0

    def test_anomaly_ratio_from_data(self):
        """Anomaly ratio from BPChiralData."""
        data = bp_data()
        assert data.anomaly_ratio == Rational(1, 6)


# ===================================================================
# XII. Regression guards
# ===================================================================

class TestRegressionGuards:
    """Guard against known anti-patterns."""

    def test_koszul_conductor_not_2(self):
        """AP140: K_BP = 196, NOT 2."""
        K = bp_koszul_conductor()
        assert simplify(K - 2) != 0
        assert simplify(K - 196) == 0

    def test_chirhoch_not_polynomial_ring(self):
        """AP94: ChirHoch*(BP) is NOT C[Theta] (polynomial ring).
        It is finite-dimensional: [1, 2, 1], total = 4.
        """
        r = compute_chirhoch_bp()
        assert r.total_dimension == 4  # finite, not infinite

    def test_chirhoch_not_gelfand_fuchs(self):
        """AP95: ChirHoch != Gelfand-Fuchs cohomology.
        GF cohomology is infinite-dimensional; ChirHoch is bounded.
        """
        r = compute_chirhoch_bp()
        assert r.concentrated_in_0_1_2  # bounded amplitude

    def test_amplitude_not_virtual_dimension(self):
        """AP134: cohomological amplitude [0, 2] != virtual dimension 2.
        Total dim = 4, not 2.
        """
        r = compute_chirhoch_bp()
        assert r.total_dimension == 4
        # Amplitude is [0, 2] but total dim is 4, not 2
