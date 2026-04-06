"""Tests for compute/lib/dmod_purity_char_variety_engine.py.

Validates the D-module purity and characteristic variety engine
for factorization homology D-modules across the standard landscape.

Coverage:
  1. OPE pole orders and bar r-matrix pole orders (AP19 compliance)
  2. FM boundary strata enumeration
  3. Characteristic variety computation (Lagrangian, alignment)
  4. Heisenberg: free D-module, Ch = zero section
  5. Affine KM: Gaudin system, regular singular, Lagrangian
  6. Virasoro: BPZ system, holonomic, Lagrangian
  7. W_3: multi-weight case, holonomic, Lagrangian
  8. Non-Koszul Ising: purity/alignment failure evidence
  9. Symbol involutivity across families
  10. Purity landscape (all Koszul => Lagrangian + aligned)
  11. BB localization analogy (affine KM only)
  12. Weight filtration analysis (PBW = weight compatibility)
  13. Converse direction summary
  14. Cross-family consistency checks
  15. Multi-path verification: pole order consistency

References:
  thm:koszul-equivalences-meta item (xii) (chiral_koszul_pairs.tex)
  rem:d-module-purity-content (chiral_koszul_pairs.tex)
  AP19: bar r-matrix pole orders one below OPE
  AP37: spectral sequence page from full structure, not heuristics
  compute/audit/d_module_purity_converse_2026_04_05.md
"""

import pytest
from fractions import Fraction

from compute.lib.dmod_purity_char_variety_engine import (
    ope_pole_orders,
    bar_rmatrix_pole_orders,
    fm_boundary_strata,
    fm_stratum_codimension,
    char_variety_components,
    heisenberg_char_variety,
    gaudin_char_variety,
    bpz_char_variety,
    w3_char_variety,
    ising_char_variety,
    purity_landscape_check,
    symbol_involutivity_check,
    bb_localization_analogy,
    weight_filtration_analysis,
    converse_direction_summary,
)


# =====================================================================
# 1. OPE Pole Orders
# =====================================================================

class TestOPEPoleOrders:
    """Verify OPE pole structures for standard families."""

    def test_heisenberg_ope_poles(self):
        """Heisenberg: alpha(z) alpha(w) ~ k/(z-w)^2. Pole order 2."""
        poles = ope_pole_orders("heisenberg")
        assert poles["(alpha,alpha)"] == 2

    def test_affine_sl2_ope_poles(self):
        """Affine sl_2: J^a J^b ~ k delta/(z-w)^2 + f J/(z-w). Pole order 2."""
        poles = ope_pole_orders("affine_sl2")
        assert poles["(J,J)"] == 2

    def test_virasoro_ope_poles(self):
        """Virasoro: T T ~ (c/2)/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w). Pole order 4."""
        poles = ope_pole_orders("virasoro")
        assert poles["(T,T)"] == 4

    def test_betagamma_ope_poles(self):
        """betagamma: beta gamma ~ 1/(z-w). Pole order 1. Self-OPE trivial."""
        poles = ope_pole_orders("betagamma")
        assert poles["(beta,gamma)"] == 1
        assert poles["(gamma,beta)"] == 1
        assert poles["(beta,beta)"] == 0
        assert poles["(gamma,gamma)"] == 0

    def test_w3_ope_poles(self):
        """W_3: T-T pole 4, W-W pole 6, T-W pole 2."""
        poles = ope_pole_orders("w3")
        assert poles["(T,T)"] == 4
        assert poles["(W,W)"] == 6
        assert poles["(T,W)"] == 2
        assert poles["(W,T)"] == 2

    def test_free_fermion_ope_poles(self):
        """Free fermion: psi psi ~ 1/(z-w). Pole order 1."""
        poles = ope_pole_orders("free_fermion")
        assert poles["(psi,psi)"] == 1

    def test_ising_ope_poles(self):
        """Ising: same T-T OPE as Virasoro, plus null vector flag."""
        poles = ope_pole_orders("ising")
        assert poles["(T,T)"] == 4
        assert poles.get("null_vector") is True


# =====================================================================
# 2. Bar R-Matrix Pole Orders (AP19)
# =====================================================================

class TestBarRMatrixPoles:
    """Verify AP19: bar r-matrix poles are one order below OPE."""

    def test_heisenberg_bar_poles(self):
        """Heisenberg: OPE order 2 => bar r-matrix order 1 (Omega/z)."""
        bar_poles = bar_rmatrix_pole_orders("heisenberg")
        assert bar_poles["(alpha,alpha)"] == 1

    def test_virasoro_bar_poles(self):
        """Virasoro: OPE order 4 => bar r-matrix order 3.
        r(z) = (c/2)/z^3 + 2T/z (no even-order poles for bosonic)."""
        bar_poles = bar_rmatrix_pole_orders("virasoro")
        assert bar_poles["(T,T)"] == 3

    def test_w3_bar_poles(self):
        """W_3: W-W OPE order 6 => bar r-matrix order 5."""
        bar_poles = bar_rmatrix_pole_orders("w3")
        assert bar_poles["(T,T)"] == 3  # OPE 4 => bar 3
        assert bar_poles["(W,W)"] == 5  # OPE 6 => bar 5
        assert bar_poles["(T,W)"] == 1  # OPE 2 => bar 1

    def test_betagamma_bar_poles(self):
        """betagamma: OPE order 1 => bar r-matrix order 0 (no pole)."""
        bar_poles = bar_rmatrix_pole_orders("betagamma")
        assert bar_poles["(beta,gamma)"] == 0
        assert bar_poles["(gamma,beta)"] == 0

    def test_affine_sl2_bar_poles(self):
        """Affine sl_2: OPE order 2 => bar r-matrix order 1."""
        bar_poles = bar_rmatrix_pole_orders("affine_sl2")
        assert bar_poles["(J,J)"] == 1

    def test_ap19_universal(self):
        """AP19 holds universally: bar pole = OPE pole - 1 for all families."""
        families = ["heisenberg", "affine_sl2", "virasoro", "betagamma",
                     "w3", "free_fermion"]
        for family in families:
            ope = ope_pole_orders(family)
            bar = bar_rmatrix_pole_orders(family)
            for pair in ope:
                if pair == "null_vector":
                    continue
                assert bar[pair] == max(0, ope[pair] - 1), (
                    f"AP19 violation for {family}, pair {pair}: "
                    f"OPE order {ope[pair]}, bar order {bar[pair]}"
                )


# =====================================================================
# 3. FM Boundary Strata
# =====================================================================

class TestFMBoundaryStrata:
    """Verify FM boundary strata enumeration."""

    def test_n2_strata(self):
        """n=2: one pairwise collision Delta_{12}."""
        strata = fm_boundary_strata(2)
        # Only one codim-1 stratum: {1,2}
        codim1 = [s for s in strata if len(s) == 1 and len(list(s)[0]) == 2]
        assert len(codim1) == 1

    def test_n3_strata_count(self):
        """n=3: three pairwise + one triple collision."""
        strata = fm_boundary_strata(3)
        pairwise = [s for s in strata
                     if len(s) == 1 and len(list(s)[0]) == 2]
        triple = [s for s in strata
                   if len(s) == 1 and len(list(s)[0]) == 3]
        assert len(pairwise) == 3  # C(3,2) = 3
        assert len(triple) == 1    # C(3,3) = 1

    def test_n4_strata_count(self):
        """n=4: 6 pairwise + 4 triple + 3 double-pairwise collisions."""
        strata = fm_boundary_strata(4)
        pairwise = [s for s in strata
                     if len(s) == 1 and len(list(s)[0]) == 2]
        triple = [s for s in strata
                   if len(s) == 1 and len(list(s)[0]) == 3]
        double_pair = [s for s in strata if len(s) == 2]
        assert len(pairwise) == 6   # C(4,2) = 6
        assert len(triple) == 4     # C(4,3) = 4
        assert len(double_pair) == 3  # C(4,2)/2 disjoint pairs = 3

    def test_stratum_codimension(self):
        """Codimension of strata on a curve (dim_X = 1)."""
        # Pairwise collision: codim = 1
        s_pair = frozenset([frozenset([1, 2])])
        assert fm_stratum_codimension(s_pair) == 1

        # Triple collision: codim = 2
        s_triple = frozenset([frozenset([1, 2, 3])])
        assert fm_stratum_codimension(s_triple) == 2

        # Double pairwise: codim = 2
        s_double = frozenset([frozenset([1, 2]), frozenset([3, 4])])
        assert fm_stratum_codimension(s_double) == 2


# =====================================================================
# 4. Heisenberg Characteristic Variety
# =====================================================================

class TestHeisenbergCharVariety:
    """Heisenberg: the simplest case. Free D-module, Ch = zero section."""

    def test_ch_is_zero_section(self):
        """Ch(FH_n(H_k)) = zero section for all n."""
        for n in range(2, 6):
            result = heisenberg_char_variety(n)
            assert result["char_variety"] == "zero_section"

    def test_lagrangian(self):
        """Zero section is Lagrangian in T*Conf_n."""
        for n in range(2, 6):
            result = heisenberg_char_variety(n)
            assert result["is_lagrangian"] is True
            assert result["char_variety_dim"] == n  # dim = n in T*(Conf_n) of dim 2n

    def test_pure(self):
        """Heisenberg bar D-module is pure (flat connection)."""
        result = heisenberg_char_variety(3)
        assert result["is_pure"] is True
        assert result["dmod_type"] == "flat_connection"

    def test_aligned(self):
        """Zero section is trivially aligned to FM strata."""
        result = heisenberg_char_variety(3)
        assert result["is_aligned"] is True

    def test_kappa_matches(self):
        """kappa(H_k) = k. Verify for several k values."""
        for k in [1, 2, Fraction(1, 2), -1]:
            result = heisenberg_char_variety(3, k=k)
            expected_kappa = Fraction(k) if not isinstance(k, Fraction) else k
            assert result["kappa"] == expected_kappa

    def test_shadow_depth(self):
        """Heisenberg is class G: shadow depth = 2."""
        result = heisenberg_char_variety(3)
        assert result["shadow_depth"] == 2

    def test_genus0_curvature_zero(self):
        """At genus 0, the flat connection has zero curvature."""
        result = heisenberg_char_variety(3)
        assert result["curvature_genus0"] == 0


# =====================================================================
# 5. Affine KM: Gaudin System
# =====================================================================

class TestGaudinCharVariety:
    """Affine KM factorization homology via the Gaudin system."""

    def test_sl2_regular_singular(self):
        """Gaudin system for sl_2 is regular singular."""
        result = gaudin_char_variety("sl2", n=3)
        assert result["regular_singular"] is True

    def test_sl2_lagrangian(self):
        """Gaudin characteristic variety is Lagrangian."""
        result = gaudin_char_variety("sl2", n=4)
        assert result["is_lagrangian"] is True

    def test_sl2_aligned(self):
        """Gaudin singularities are at collision diagonals only."""
        result = gaudin_char_variety("sl2", n=3)
        assert result["is_aligned"] is True

    def test_sl2_involutive(self):
        """Gaudin Hamiltonians are in involution."""
        result = gaudin_char_variety("sl2", n=4)
        assert result["involutive"] is True

    def test_sl2_singular_locus_count(self):
        """Number of collision strata = C(n,2)."""
        for n in range(2, 6):
            result = gaudin_char_variety("sl2", n=n)
            expected = n * (n - 1) // 2
            assert result["num_singular_strata"] == expected

    def test_sl3_lagrangian(self):
        """Gaudin for sl_3 is also Lagrangian."""
        result = gaudin_char_variety("sl3", n=4)
        assert result["is_lagrangian"] is True
        assert result["dim_g"] == 8

    def test_integrability_reference(self):
        """Gaudin integrability is from Feigin-Frenkel-Reshetikhin."""
        result = gaudin_char_variety("sl2", n=3)
        assert "Feigin-Frenkel-Reshetikhin" in result["integrability"]

    def test_dim_data(self):
        """Dimension data: dim_conf = n, dim_cotangent = 2n."""
        result = gaudin_char_variety("sl2", n=5)
        assert result["dim_conf"] == 5
        assert result["dim_cotangent"] == 10


# =====================================================================
# 6. Virasoro: BPZ System
# =====================================================================

class TestBPZCharVariety:
    """Virasoro factorization homology via the BPZ system."""

    def test_holonomic(self):
        """BPZ D-module is holonomic."""
        result = bpz_char_variety(n=3)
        assert result["is_holonomic"] is True

    def test_lagrangian(self):
        """Holonomic => Lagrangian characteristic variety."""
        result = bpz_char_variety(n=4)
        assert result["is_lagrangian"] is True

    def test_aligned(self):
        """BPZ singularities are at collision diagonals only."""
        result = bpz_char_variety(n=3)
        assert result["is_aligned"] is True

    def test_regular_singular(self):
        """BPZ system has regular singularities."""
        result = bpz_char_variety(n=3)
        assert result["regular_singular"] is True

    def test_symbol_order_2(self):
        """BPZ is second-order (weight-2 generator T)."""
        result = bpz_char_variety(n=3)
        assert result["symbol_order"] == 2

    def test_singular_locus(self):
        """Singular locus = collision diagonals."""
        result = bpz_char_variety(n=4)
        assert result["num_singular_strata"] == 6  # C(4,2)

    def test_c_parameter(self):
        """Central charge is recorded correctly."""
        result = bpz_char_variety(n=3, c=Fraction(1, 2))
        assert result["c"] == Fraction(1, 2)


# =====================================================================
# 7. W_3 Characteristic Variety
# =====================================================================

class TestW3CharVariety:
    """W_3: the first nontrivial multi-weight case."""

    def test_holonomic(self):
        """W_3 FH is holonomic."""
        result = w3_char_variety(n=3)
        assert result["is_holonomic"] is True

    def test_lagrangian(self):
        """Holonomic => Lagrangian."""
        result = w3_char_variety(n=3)
        assert result["is_lagrangian"] is True

    def test_aligned(self):
        """Ch aligned to FM strata."""
        result = w3_char_variety(n=3)
        assert result["is_aligned"] is True

    def test_max_symbol_order(self):
        """Max symbol order = 3 (from weight-3 generator W)."""
        result = w3_char_variety(n=3)
        assert result["max_symbol_order"] == 3

    def test_symbol_data(self):
        """Symbol has quadratic (T) and cubic (W) components."""
        result = w3_char_variety(n=3)
        sd = result["symbol_data"]
        assert sd["T_self"]["order"] == 2
        assert sd["W_self"]["order"] == 3
        assert sd["T_W_mixed"]["order"] == 1

    def test_shadow_depth_infinite(self):
        """W_3 is class M: shadow depth = infinity."""
        result = w3_char_variety(n=3)
        assert result["shadow_depth"] == "infinity"


# =====================================================================
# 8. Non-Koszul: Ising Minimal Model
# =====================================================================

class TestIsingCharVariety:
    """Ising L(c_{3,4}, 0): NOT Koszul. Evidence for the contrapositive."""

    def test_not_koszul(self):
        """Ising is not chirally Koszul."""
        result = ising_char_variety(n=2)
        assert result["is_koszul"] is False

    def test_central_charge(self):
        """c = 1/2 for the Ising model."""
        result = ising_char_variety(n=2)
        assert result["c"] == Fraction(1, 2)

    def test_null_level(self):
        """Null vector at level 6."""
        result = ising_char_variety(n=2)
        assert result["null_level"] == 6

    def test_low_arity_agrees_with_vir(self):
        """At n < 6, bar complex agrees with universal Virasoro."""
        for n in range(2, 6):
            result = ising_char_variety(n=n)
            assert result["bar_agrees_with_virasoro"] is True

    def test_high_arity_differs(self):
        """At n >= 6, null vector quotient modifies the bar complex."""
        result = ising_char_variety(n=6)
        assert result["bar_agrees_with_virasoro"] is False
        assert len(result["extra_components"]) > 0

    def test_alignment_fails_at_high_arity(self):
        """At n >= 6, alignment to FM strata fails."""
        result = ising_char_variety(n=6)
        assert result["is_aligned"] is False

    def test_alignment_holds_at_low_arity(self):
        """At n < 6, alignment holds (agrees with Virasoro)."""
        for n in range(2, 6):
            result = ising_char_variety(n=n)
            assert result["is_aligned"] is True

    def test_kac_shapovalov_failure(self):
        """Kac-Shapovalov criterion fails at h = 6."""
        result = ising_char_variety(n=2)
        assert result["kac_shapovalov_fails_at"] == 6

    def test_converse_evidence(self):
        """Non-Koszul => alignment failure is evidence for the contrapositive."""
        result = ising_char_variety(n=7)
        assert "NOT Koszul" in result["converse_evidence"]


# =====================================================================
# 9. Characteristic Variety Components
# =====================================================================

class TestCharVarietyComponents:
    """Generic characteristic variety computation across families."""

    def test_heisenberg_n2(self):
        """Heisenberg at n=2: zero section + one conormal."""
        cv = char_variety_components("heisenberg", 2)
        assert cv["is_lagrangian"] is True
        assert cv["is_aligned"] is True
        # Has zero section + conormal to Delta_12
        types = [c["type"] for c in cv["components"]]
        assert "zero_section" in types
        assert "conormal_pairwise" in types

    def test_virasoro_n3(self):
        """Virasoro at n=3: zero section + 3 pairwise + 1 triple."""
        cv = char_variety_components("virasoro", 3)
        assert cv["is_lagrangian"] is True
        assert cv["is_aligned"] is True
        pairwise = [c for c in cv["components"]
                     if c["type"] == "conormal_pairwise"]
        triple = [c for c in cv["components"]
                   if c["type"] == "conormal_triple"]
        assert len(pairwise) == 3  # C(3,2)
        assert len(triple) == 1    # C(3,3)

    def test_all_components_lagrangian(self):
        """Every component of Ch has dimension = dim(Conf_n)."""
        for family in ["heisenberg", "affine_sl2", "virasoro", "w3"]:
            for n in range(2, 5):
                cv = char_variety_components(family, n)
                for comp in cv["components"]:
                    assert comp["dimension"] == n, (
                        f"Component {comp['type']} of {family} at n={n} "
                        f"has dimension {comp['dimension']}, expected {n}"
                    )

    def test_pure_dimensional(self):
        """Ch is pure-dimensional for all Koszul families."""
        for family in ["heisenberg", "affine_sl2", "virasoro",
                        "betagamma", "w3"]:
            cv = char_variety_components(family, 3)
            assert cv["is_pure_dimensional"] is True

    def test_betagamma_no_triple(self):
        """betagamma at n=3: pole order 1 => no triple conormals.
        (max OPE pole = 1, so higher collision strata not generated.)"""
        cv = char_variety_components("betagamma", 3)
        triple = [c for c in cv["components"]
                   if c["type"] == "conormal_triple"]
        assert len(triple) == 0  # pole order 1 < 2 threshold

    def test_ising_has_null_vector_component(self):
        """Ising: extra component from null vector quotient."""
        cv = char_variety_components("ising", 3)
        null_comps = [c for c in cv["components"]
                       if c["type"] == "null_vector_component"]
        assert len(null_comps) == 1
        assert cv["is_aligned"] is False  # null vector breaks alignment


# =====================================================================
# 10. Symbol Involutivity
# =====================================================================

class TestSymbolInvolutivity:
    """Verify involutivity of the symbol ideal."""

    def test_all_families_involutive(self):
        """All chiral algebras have involutive symbol ideals."""
        families = ["heisenberg", "affine_sl2", "virasoro",
                     "betagamma", "w3", "free_fermion"]
        for family in families:
            result = symbol_involutivity_check(family)
            assert result["involutive"] is True

    def test_heisenberg_linear_symbol(self):
        """Heisenberg: weight-1 generator => linear symbol."""
        result = symbol_involutivity_check("heisenberg")
        assert result["symbol_type"] == "linear"
        assert result["max_conformal_weight"] == 1

    def test_virasoro_quadratic_symbol(self):
        """Virasoro: weight-2 generator => quadratic symbol."""
        result = symbol_involutivity_check("virasoro")
        assert result["symbol_type"] == "quadratic"
        assert result["max_conformal_weight"] == 2

    def test_w3_cubic_symbol(self):
        """W_3: weight-3 generator => cubic symbol."""
        result = symbol_involutivity_check("w3")
        assert result["symbol_type"] == "cubic"
        assert result["max_conformal_weight"] == 3

    def test_factorization_mechanism(self):
        """Involutivity follows from factorization coalgebra structure."""
        result = symbol_involutivity_check("virasoro")
        assert "Factorization" in result["mechanism"]


# =====================================================================
# 11. Purity Landscape Check
# =====================================================================

class TestPurityLandscape:
    """Cross-family purity verification."""

    def test_all_koszul_lagrangian(self):
        """All Koszul families have Lagrangian Ch at all arities."""
        results = purity_landscape_check(max_n=4)
        for family in ["heisenberg", "affine_sl2", "virasoro",
                        "betagamma", "w3", "free_fermion"]:
            assert results[family]["all_lagrangian"] is True, (
                f"{family}: not all Lagrangian"
            )

    def test_all_koszul_aligned(self):
        """All Koszul families have aligned Ch at all arities."""
        results = purity_landscape_check(max_n=4)
        for family in ["heisenberg", "affine_sl2", "virasoro",
                        "betagamma", "w3", "free_fermion"]:
            assert results[family]["all_aligned"] is True, (
                f"{family}: not all aligned"
            )

    def test_ising_not_koszul(self):
        """Ising is flagged as not Koszul."""
        results = purity_landscape_check(max_n=4)
        assert results["ising"]["koszul"] is False

    def test_ising_alignment_at_low_arity(self):
        """At n <= 4 (< null_level = 6), Ising alignment holds."""
        results = purity_landscape_check(max_n=4)
        # All arities 2-4 are below null level 6
        for n, data in results["ising"]["by_arity"].items():
            assert data["bar_agrees_with_vir"] is True


# =====================================================================
# 12. BB Localization Analogy
# =====================================================================

class TestBBLocalizationAnalogy:
    """Beilinson-Bernstein localization for the converse."""

    def test_sl2_localization_available(self):
        """Chiral localization exists for sl_2."""
        result = bb_localization_analogy("sl2")
        assert result["localization_available"] is True

    def test_sl2_converse_expected(self):
        """For affine KM, purity => Koszul is expected via localization.

        The chiral localization argument (Frenkel-Gaitsgory + BGS) provides
        a strategy but the full argument in the chiral setting has not been
        formally written.  Status: EXPECTED, not PROVED.
        """
        result = bb_localization_analogy("sl2")
        assert "EXPECTED" in result["converse_status_for_km"]

    def test_general_converse_open(self):
        """For general chiral algebras, the converse is still open."""
        result = bb_localization_analogy("sl2")
        assert "OPEN" in result["converse_status_general"]

    def test_limitation(self):
        """Localization does NOT extend to Virasoro/W-algebras."""
        result = bb_localization_analogy("sl2")
        assert "Virasoro" in result["limitation"]
        assert "W-algebras" in result["limitation"]


# =====================================================================
# 13. Weight Filtration Analysis
# =====================================================================

class TestWeightFiltrationAnalysis:
    """PBW = weight compatibility analysis."""

    def test_heisenberg_trivial(self):
        """Heisenberg: both filtrations trivial, compatibility obvious."""
        result = weight_filtration_analysis("heisenberg")
        assert result["pbw_filtration_trivial"] is True
        assert result["weight_filtration_trivial"] is True
        assert result["pbw_weight_compatibility"] == "TRIVIAL"

    def test_affine_km_expected(self):
        """Affine KM: compatibility expected via localization."""
        result = weight_filtration_analysis("affine_sl2")
        assert "localization" in result["pbw_weight_compatibility"].lower()

    def test_virasoro_open(self):
        """Virasoro: compatibility is open."""
        result = weight_filtration_analysis("virasoro")
        assert "OPEN" in result["pbw_weight_compatibility"]

    def test_w3_open(self):
        """W_3: compatibility open (multi-weight complicates)."""
        result = weight_filtration_analysis("w3")
        assert "OPEN" in result["pbw_weight_compatibility"]

    def test_ising_fails(self):
        """Ising: compatibility fails (null vector quotient)."""
        result = weight_filtration_analysis("ising")
        assert "FAILS" in result["pbw_weight_compatibility"]
        assert result["koszul"] is False


# =====================================================================
# 14. Converse Direction Summary
# =====================================================================

class TestConverseSummary:
    """Verify the summary of the D-module purity converse status."""

    def test_proved_direction(self):
        """(xii) => (x) is proved."""
        summary = converse_direction_summary()
        assert "(xii) => (x)" in summary["proved_direction"]["statement"]

    def test_open_direction(self):
        """(x) => (xii) is open."""
        summary = converse_direction_summary()
        assert "(x) => (xii)" in summary["open_direction"]["statement"]
        assert summary["open_direction"]["status"] == "OPEN"

    def test_approach_d_most_promising(self):
        """Approach D (contrapositive) is most promising."""
        summary = converse_direction_summary()
        assert "MOST PROMISING" in summary["approaches"]["D_contrapositive"]

    def test_approach_b_not_viable(self):
        """Approach B (Saito on Ran) is not viable."""
        summary = converse_direction_summary()
        assert "NOT VIABLE" in summary["approaches"]["B_saito_on_ran"]

    def test_central_obstruction(self):
        """Central obstruction is PBW-weight compatibility."""
        summary = converse_direction_summary()
        assert "PBW" in summary["central_obstruction"]["name"]

    def test_computational_evidence(self):
        """All Koszul families have Lagrangian + aligned Ch."""
        summary = converse_direction_summary()
        ce = summary["computational_evidence"]
        assert "Lagrangian" in ce["all_koszul_families"]
        assert "zero section" in ce["heisenberg"]
        assert "Gaudin" in ce["affine_km"]


# =====================================================================
# 15. Multi-Path Verification: Pole Orders
# =====================================================================

class TestMultiPathVerification:
    """Cross-check pole orders via multiple independent methods."""

    def test_virasoro_pole_via_ope_vs_bar(self):
        """Virasoro: verify OPE pole 4, bar pole 3 by two paths.
        Path 1: direct from OPE (T_{(3)}T = c/2).
        Path 2: bar r-matrix = OPE - 1 (AP19)."""
        ope = ope_pole_orders("virasoro")
        bar = bar_rmatrix_pole_orders("virasoro")
        # Path 1: OPE pole order 4 (from T(z)T(w) ~ (c/2)/(z-w)^4 + ...)
        assert ope["(T,T)"] == 4
        # Path 2: bar r-matrix pole = 4 - 1 = 3
        assert bar["(T,T)"] == 3
        # Consistency
        assert bar["(T,T)"] == ope["(T,T)"] - 1

    def test_heisenberg_pole_via_three_paths(self):
        """Heisenberg: 3-path verification of pole orders.
        Path 1: OPE alpha(z) alpha(w) ~ k/(z-w)^2, order 2.
        Path 2: bar r-matrix Omega/z, order 1 = OPE - 1.
        Path 3: char variety = zero section (flat connection, no poles)."""
        ope = ope_pole_orders("heisenberg")
        bar = bar_rmatrix_pole_orders("heisenberg")
        cv = heisenberg_char_variety(2)

        assert ope["(alpha,alpha)"] == 2          # Path 1
        assert bar["(alpha,alpha)"] == 1           # Path 2
        assert cv["char_variety"] == "zero_section"  # Path 3

    def test_w3_pole_consistency(self):
        """W_3: pole orders consistent between OPE, bar, and symbol.
        The W-W OPE has pole order 6.
        The bar r-matrix has pole order 5.
        The max symbol order is 3 (from weight-3 generator W)."""
        ope = ope_pole_orders("w3")
        bar = bar_rmatrix_pole_orders("w3")
        w3cv = w3_char_variety(3)

        assert ope["(W,W)"] == 6
        assert bar["(W,W)"] == 5
        assert w3cv["max_symbol_order"] == 3

    def test_lagrangian_via_holonomicity_and_components(self):
        """Two independent paths to Lagrangian for Virasoro.
        Path 1: holonomic D-module => Ch is Lagrangian (by definition).
        Path 2: all components of Ch are conormal bundles to strata
                 (conormal bundles are Lagrangian)."""
        bpz = bpz_char_variety(3)
        cv = char_variety_components("virasoro", 3)

        # Path 1: holonomic => Lagrangian
        assert bpz["is_holonomic"] is True
        assert bpz["is_lagrangian"] is True

        # Path 2: all components are conormal bundles
        assert cv["is_aligned"] is True
        for comp in cv["components"]:
            assert comp["lagrangian"] is True

    def test_koszul_implies_lagrangian_all_families(self):
        """For all Koszul families: Koszul => FH concentrated => holonomic.
        Holonomic => Ch is Lagrangian. This is a chain of proved implications."""
        families = ["heisenberg", "affine_sl2", "virasoro",
                     "betagamma", "w3", "free_fermion"]
        for family in families:
            cv = char_variety_components(family, 3)
            assert cv["is_lagrangian"] is True, (
                f"{family}: Koszul but Ch not Lagrangian"
            )

    def test_non_koszul_alignment_failure_at_null_level(self):
        """Ising: null vector at level 6 breaks alignment at n >= 6.
        Two independent paths:
        Path 1: ising_char_variety reports alignment failure.
        Path 2: char_variety_components reports alignment failure."""
        # Path 1
        ising = ising_char_variety(7)
        assert ising["is_aligned"] is False

        # Path 2
        cv = char_variety_components("ising", 3)
        assert cv["has_null_vector"] is True
        assert cv["is_aligned"] is False


# =====================================================================
# 16. Dimensional Consistency
# =====================================================================

class TestDimensionalConsistency:
    """Verify dimensional consistency of all computations."""

    def test_cotangent_dimension(self):
        """T*(Conf_n) has dimension 2n for curves."""
        for n in range(2, 6):
            cv = char_variety_components("virasoro", n)
            assert cv["dim_cotangent"] == 2 * n
            assert cv["dim_conf"] == n

    def test_lagrangian_dimension(self):
        """Lagrangian subvariety has dimension = n = dim(Conf_n)."""
        for n in range(2, 5):
            for family in ["heisenberg", "virasoro", "w3"]:
                cv = char_variety_components(family, n)
                for comp in cv["components"]:
                    assert comp["dimension"] == n

    def test_gaudin_dimensions(self):
        """Gaudin system dimensions are consistent."""
        result = gaudin_char_variety("sl2", n=4)
        assert result["dim_conf"] == 4
        assert result["dim_cotangent"] == 8

    def test_bpz_dimensions(self):
        """BPZ system dimensions are consistent."""
        result = bpz_char_variety(n=5)
        assert result["dim_conf"] == 5
        assert result["dim_cotangent"] == 10


# =====================================================================
# 17. Converse Direction Evidence
# =====================================================================

class TestConverseEvidence:
    """Computational evidence for and against the converse."""

    def test_all_koszul_satisfy_purity(self):
        """Every Koszul family satisfies both conditions of (xii):
        Lagrangian + aligned. This is consistent with (x) => (xii)."""
        families = ["heisenberg", "affine_sl2", "virasoro",
                     "betagamma", "w3", "free_fermion"]
        for family in families:
            for n in range(2, 5):
                cv = char_variety_components(family, n)
                assert cv["is_lagrangian"] is True
                assert cv["is_aligned"] is True

    def test_non_koszul_violates_alignment(self):
        """The non-Koszul Ising model violates alignment.
        This supports the contrapositive: NOT Koszul => NOT aligned."""
        cv = char_variety_components("ising", 3)
        assert cv["is_aligned"] is False

    def test_contrapositive_supported(self):
        """The contrapositive NOT Koszul => NOT pure is supported by:
        1. Ising violates alignment.
        2. Weight filtration analysis shows compatibility fails for Ising.
        Both are consistent with the converse direction."""
        ising_cv = char_variety_components("ising", 3)
        ising_wf = weight_filtration_analysis("ising")

        assert ising_cv["is_aligned"] is False
        assert "FAILS" in ising_wf["pbw_weight_compatibility"]

    def test_no_counterexample_to_converse(self):
        """No Koszul algebra is found where purity/alignment fails.
        This is necessary (but not sufficient) for the converse."""
        results = purity_landscape_check(max_n=4)
        for family in ["heisenberg", "affine_sl2", "virasoro",
                        "betagamma", "w3", "free_fermion"]:
            assert results[family]["all_lagrangian"] is True
            assert results[family]["all_aligned"] is True


# =====================================================================
# 18. Edge Cases and Robustness
# =====================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_n1_trivial(self):
        """At n = 1, Conf_1(X) = X, and bar_B_1 = A (the algebra itself).
        Ch(A) = zero section (A is an O_X-module, not a D-module)."""
        # At n=1, the bar complex is just the desuspended generating space
        cv = char_variety_components("heisenberg", 1)
        # Only the zero section (no collision strata for a single point)
        types = [c["type"] for c in cv["components"]]
        assert "zero_section" in types
        assert "conormal_pairwise" not in types

    def test_large_n(self):
        """At n = 6, still computes correctly."""
        cv = char_variety_components("virasoro", 6)
        assert cv["is_lagrangian"] is True
        pairwise = [c for c in cv["components"]
                     if c["type"] == "conormal_pairwise"]
        assert len(pairwise) == 15  # C(6,2)

    def test_w_infinity(self):
        """W_infinity has unbounded OPE pole orders."""
        poles = ope_pole_orders("w_infinity", N=5)
        # W_s W_t has pole order s + t
        assert poles["(W_2,W_2)"] == 4
        assert poles["(W_3,W_3)"] == 6
        assert poles["(W_2,W_5)"] == 7
        assert poles["(W_5,W_5)"] == 10

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError):
            ope_pole_orders("nonexistent_algebra")
