"""Tests for the BV-BRST chain-level computation engine.

Verifies the central identification: bar-cobar adjunction = BV-BRST formalism.

Test structure:
  1. BV field algebra: ghost numbers, field types, bar degree identification
  2. QME verification: genus 0 (d^2=0), genus 1 (curvature = kappa*omega_1)
  3. Bar = BV identification: chain-level differential agreement
  4. Genus-1 curvature: E_2 defect, period correction, complementarity
  5. Ghost number filtration: bar degree = ghost number
  6. Anomaly cancellation: bosonic string (c=26), superstring (d=10)
  7. Cross-family kappa consistency (AP10 compliance)
  8. Faber-Pandharipande numbers and genus expansion

Ground truth: bv_brst.tex, bar_construction.tex, feynman_diagrams.tex,
  quantum_corrections.tex, genus_expansion.py, CLAUDE.md Critical Pitfalls.
"""

import pytest
from sympy import Rational, S, Symbol, simplify, symbols

from compute.lib.bv_brst_chain_level import (
    BVAlgebra,
    BVField,
    BarBVIdentification,
    ChainLevelDifferential,
    FieldType,
    QMEResult,
    affine_km_bv,
    anomaly_cancellation_check,
    arnold_relation_genus,
    bar_bv_identification,
    bc_system_bv,
    bosonic_string_anomaly_cancellation,
    compute_bar_differential_genus0,
    compute_bar_differential_genus1,
    cross_family_kappa_consistency,
    d_squared_genus1,
    genus1_complementarity,
    genus1_curvature,
    genus_expansion_from_bv,
    ghost_number_filtration,
    ghost_number_from_type,
    heisenberg_bv,
    kappa_formula,
    make_antifield,
    make_antighost,
    make_field,
    make_ghost,
    superstring_anomaly_cancellation,
    verify_bar_degree_equals_ghost_number,
    verify_bc_chain_level,
    verify_d_squared_zero_genus0,
    verify_faber_pandharipande,
    verify_heisenberg_chain_level,
    verify_kappa_anti_symmetry,
    verify_qme,
    verify_virasoro_chain_level,
    verify_w3_chain_level,
    virasoro_bv,
    w3_bv,
    w3_string_anomaly_cancellation,
)


# ═══════════════════════════════════════════════════════════════════════════
# Section 1: BV Field Algebra Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestBVFieldAlgebra:
    """Tests for BV field construction and ghost number assignments."""

    def test_field_ghost_number_zero(self):
        """Physical fields have ghost number 0."""
        phi = make_field("phi", Rational(1))
        assert phi.ghost_number == 0
        assert phi.field_type == FieldType.FIELD

    def test_antifield_ghost_number_plus_one(self):
        """Antifields have ghost number +1 (cohomological convention)."""
        phi_star = make_antifield("phi*", Rational(0))
        assert phi_star.ghost_number == 1
        assert phi_star.field_type == FieldType.ANTIFIELD

    def test_ghost_number_minus_one(self):
        """Ghosts have ghost number -1."""
        c = make_ghost("c", Rational(0))
        assert c.ghost_number == -1
        assert c.field_type == FieldType.GHOST

    def test_antighost_number_minus_two(self):
        """Antighosts have ghost number -2."""
        b = make_antighost("b", Rational(1))
        assert b.ghost_number == -2
        assert b.field_type == FieldType.ANTIGHOST

    def test_bar_degree_equals_negative_ghost_number(self):
        """Bar degree = -ghost_number (fundamental identification)."""
        phi = make_field("phi", Rational(1))
        assert phi.bar_degree == 0  # physical field: bar degree 0

        c = make_ghost("c", Rational(0))
        assert c.bar_degree == 1  # ghost: bar degree 1

        b = make_antighost("b", Rational(1))
        assert b.bar_degree == 2  # antighost: bar degree 2

    def test_ghost_number_from_type_mapping(self):
        """Ghost number canonical mapping is correct."""
        assert ghost_number_from_type(FieldType.FIELD) == 0
        assert ghost_number_from_type(FieldType.ANTIFIELD) == 1
        assert ghost_number_from_type(FieldType.GHOST) == -1
        assert ghost_number_from_type(FieldType.ANTIGHOST) == -2


# ═══════════════════════════════════════════════════════════════════════════
# Section 2: QME Verification Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestQME:
    """Tests for the quantum master equation: hbar*Delta*S + (1/2){S,S} = 0."""

    def test_qme_genus0_always_satisfied(self):
        """At genus 0, QME is satisfied for all chiral algebras (Arnold exact)."""
        for bv_factory in [heisenberg_bv, virasoro_bv, w3_bv]:
            bv = bv_factory()
            result = verify_qme(bv, genus=0)
            assert result.satisfied is True
            assert result.genus == 0
            assert result.anomaly == S.Zero

    def test_qme_genus0_d_squared_zero(self):
        """At genus 0, d^2 = 0 (from Arnold relation exactness)."""
        assert verify_d_squared_zero_genus0() is True

    def test_qme_genus1_heisenberg_anomaly(self):
        """Heisenberg at genus 1: anomaly = kappa * omega_1."""
        kappa = Symbol('kappa')
        bv = heisenberg_bv(kappa)
        result = verify_qme(bv, genus=1)
        assert result.anomaly == kappa
        assert result.genus == 1

    def test_qme_genus1_virasoro_anomaly(self):
        """Virasoro at genus 1: anomaly = c/2 * omega_1."""
        c = Symbol('c')
        bv = virasoro_bv(c)
        result = verify_qme(bv, genus=1)
        assert simplify(result.anomaly - c / 2) == 0

    def test_qme_genus1_zero_kappa_satisfied(self):
        """When kappa = 0, QME is satisfied even at genus 1."""
        bv = heisenberg_bv(S.Zero)
        result = verify_qme(bv, genus=1)
        assert result.satisfied is True

    def test_qme_genus1_nonzero_kappa_fails(self):
        """When kappa != 0, QME fails at genus 1 (anomaly)."""
        bv = heisenberg_bv(Rational(1, 2))
        result = verify_qme(bv, genus=1)
        assert result.satisfied is False


# ═══════════════════════════════════════════════════════════════════════════
# Section 3: Bar = BV Identification Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestBarBVIdentification:
    """Tests for the chain-level identification B(A) = BV complex."""

    def test_heisenberg_identification_valid(self):
        """Heisenberg bar=BV identification is valid at genus 0."""
        bv = heisenberg_bv()
        ident = bar_bv_identification(bv, genus=0)
        assert ident.identification_valid is True
        assert ident.genus == 0

    def test_virasoro_identification_valid(self):
        """Virasoro bar=BV identification is valid."""
        bv = virasoro_bv()
        ident = bar_bv_identification(bv, genus=0)
        assert ident.identification_valid is True

    def test_bar_degree_ghost_number_heisenberg(self):
        """Bar degree = -ghost_number for all Heisenberg fields."""
        bv = heisenberg_bv()
        checks = verify_bar_degree_equals_ghost_number(bv)
        assert all(checks.values())

    def test_bar_degree_ghost_number_virasoro(self):
        """Bar degree = -ghost_number for all Virasoro fields."""
        bv = virasoro_bv()
        checks = verify_bar_degree_equals_ghost_number(bv)
        assert all(checks.values())

    def test_bar_differential_genus0_heisenberg(self):
        """Bar differential at genus 0 has d^2 = 0 for Heisenberg."""
        bv = heisenberg_bv()
        chain = compute_bar_differential_genus0(bv)
        assert chain.d_squared == S.Zero
        assert chain.genus == 0

    def test_bar_differential_genus1_curvature(self):
        """Bar differential at genus 1 has d^2 = kappa for Heisenberg."""
        kappa = Symbol('kappa')
        bv = heisenberg_bv(kappa)
        chain = compute_bar_differential_genus1(bv)
        assert chain.d_squared == kappa
        assert chain.genus == 1


# ═══════════════════════════════════════════════════════════════════════════
# Section 4: Genus-1 Curvature Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestGenus1Curvature:
    """Tests for d_fib^2 = kappa(A) * E_2(tau) * omega_1."""

    def test_heisenberg_curvature(self):
        """Heisenberg curvature at genus 1: kappa = symbol."""
        kappa = Symbol('kappa')
        bv = heisenberg_bv(kappa)
        curv = genus1_curvature(bv)
        assert curv["kappa"] == kappa
        assert curv["D1_squared_zero"] is True

    def test_heisenberg_free_energy_F1(self):
        """Heisenberg F_1 = kappa/24."""
        kappa = Symbol('kappa')
        bv = heisenberg_bv(kappa)
        curv = genus1_curvature(bv)
        assert simplify(curv["free_energy_F1"] - kappa / 24) == 0

    def test_virasoro_curvature(self):
        """Virasoro curvature at genus 1: kappa = c/2."""
        c = Symbol('c')
        bv = virasoro_bv(c)
        curv = genus1_curvature(bv)
        assert simplify(curv["kappa"] - c / 2) == 0
        assert simplify(curv["free_energy_F1"] - c / 48) == 0

    def test_sl2_free_energy_F1(self):
        """sl_2 F_1 = 3(k+2)/4 * 1/24 = (k+2)/32."""
        k = Symbol('k')
        bv = affine_km_bv("sl2", k)
        curv = genus1_curvature(bv)
        expected = Rational(3) * (k + 2) / 4 / 24
        assert simplify(curv["free_energy_F1"] - expected) == 0

    def test_lambda_1_FP_equals_one_over_24(self):
        """lambda_1^FP = 1/24."""
        kappa = Symbol('kappa')
        bv = heisenberg_bv(kappa)
        curv = genus1_curvature(bv)
        assert curv["lambda_1_FP"] == Rational(1, 24)

    def test_flat_when_kappa_zero(self):
        """When kappa = 0, the genus-1 bar complex is flat."""
        bv = heisenberg_bv(S.Zero)
        curv = genus1_curvature(bv)
        assert curv["is_flat"] is True


# ═══════════════════════════════════════════════════════════════════════════
# Section 5: Complementarity Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestComplementarity:
    """Tests for kappa(A) + kappa(A!) = constant (Theorem C at genus 1)."""

    def test_heisenberg_anti_symmetry(self):
        """Heisenberg: kappa + kappa' = 0."""
        kappa = Symbol('kappa')
        result = genus1_complementarity(kappa, -kappa, S.Zero)
        assert result["complementarity_holds"] is True

    def test_virasoro_complementarity_13(self):
        """Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        c = Symbol('c')
        result = genus1_complementarity(c / 2, (26 - c) / 2, Rational(13))
        assert result["complementarity_holds"] is True

    def test_sl2_anti_symmetry(self):
        """sl_2: kappa(sl_2_k) + kappa(sl_2_{-k-4}) = 0."""
        k = Symbol('k')
        kA = Rational(3) * (k + 2) / 4
        kA_dual = Rational(3) * (-k - 4 + 2) / 4
        result = genus1_complementarity(kA, kA_dual, S.Zero)
        assert result["complementarity_holds"] is True

    def test_w3_complementarity(self):
        """W_3: kappa(W_3_c) + kappa(W_3_{100-c}) = 250/3."""
        c = Symbol('c')
        result = genus1_complementarity(
            5 * c / 6, 5 * (100 - c) / 6, Rational(250, 3)
        )
        assert result["complementarity_holds"] is True

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is Koszul self-dual at c=13, NOT c=26."""
        kappa_13 = Rational(13, 2)
        kappa_dual_13 = (26 - Rational(13)) / 2
        assert simplify(kappa_13 - kappa_dual_13) == 0

    def test_virasoro_NOT_self_dual_at_c26(self):
        """Virasoro is NOT self-dual at c=26 (Critical Pitfall)."""
        kappa_26 = Rational(26, 2)
        kappa_dual_26 = (26 - Rational(26)) / 2
        assert simplify(kappa_26 - kappa_dual_26) != 0


# ═══════════════════════════════════════════════════════════════════════════
# Section 6: Anomaly Cancellation Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestAnomalyCancellation:
    """Tests for anomaly cancellation in string theories."""

    def test_bosonic_string_c26(self):
        """Bosonic string at d=26: anomaly cancels."""
        result = bosonic_string_anomaly_cancellation(26)
        assert result["anomaly_cancelled"] is True
        assert result["kappa_total"] == 0
        assert result["critical_dimension"] == 26

    def test_bosonic_string_c25_fails(self):
        """Bosonic string at d=25: anomaly does NOT cancel."""
        result = bosonic_string_anomaly_cancellation(25)
        assert result["anomaly_cancelled"] is False

    def test_bosonic_string_kappa_matter(self):
        """26 free bosons: kappa = 26/2 = 13."""
        result = bosonic_string_anomaly_cancellation(26)
        assert result["kappa_matter"] == 13

    def test_bosonic_string_kappa_ghost(self):
        """bc ghost system: kappa = -13."""
        result = bosonic_string_anomaly_cancellation(26)
        assert result["kappa_ghost"] == -13

    def test_superstring_d10(self):
        """N=1 superstring at d=10: anomaly cancels."""
        result = superstring_anomaly_cancellation()
        assert result["anomaly_cancelled"] is True
        assert result["critical_dimension"] == 10

    def test_anomaly_cancellation_collection(self):
        """Test anomaly cancellation for a collection of BV algebras."""
        bv1 = heisenberg_bv(Rational(3))
        bv2 = heisenberg_bv(Rational(-3))
        result = anomaly_cancellation_check([bv1, bv2], target_kappa=S.Zero)
        assert result["anomaly_cancelled"] is True


# ═══════════════════════════════════════════════════════════════════════════
# Section 7: Ghost Number Filtration Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestGhostNumberFiltration:
    """Tests for ghost number filtration = bar degree filtration."""

    def test_heisenberg_ghost_content(self):
        """Heisenberg has fields at ghost number 0 and 1."""
        bv = heisenberg_bv()
        filt = ghost_number_filtration(bv)
        assert 0 in filt["content_by_ghost_number"]
        assert 1 in filt["content_by_ghost_number"]

    def test_virasoro_ghost_range(self):
        """Virasoro BV has ghost numbers from -2 to +1."""
        bv = virasoro_bv()
        filt = ghost_number_filtration(bv)
        gh_min, gh_max = filt["ghost_number_range"]
        assert gh_min == -2
        assert gh_max == 1

    def test_total_field_count(self):
        """Total field count matches field list length."""
        bv = virasoro_bv()
        filt = ghost_number_filtration(bv)
        assert filt["total_fields"] == len(bv.fields)


# ═══════════════════════════════════════════════════════════════════════════
# Section 8: Arnold Relations Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestArnoldRelations:
    """Tests for Arnold relation behavior at different genera."""

    def test_arnold_genus0_exact(self):
        """Arnold relation is exact at genus 0."""
        result = arnold_relation_genus(0)
        assert result["defect"] == S.Zero
        assert result["d_squared"] == S.Zero

    def test_arnold_genus1_defect(self):
        """Arnold relation has E_2 defect at genus 1."""
        result = arnold_relation_genus(1)
        assert result["defect"] == "E_2(tau)"
        assert "kappa" in str(result["d_squared"])

    def test_arnold_genus2_exists(self):
        """Arnold defect exists at genus 2."""
        result = arnold_relation_genus(2)
        assert "omega_2" in str(result["defect"])


# ═══════════════════════════════════════════════════════════════════════════
# Section 9: Kappa Formula Tests (AP1 Compliance)
# ═══════════════════════════════════════════════════════════════════════════

class TestKappaFormulas:
    """Tests for kappa formulas, computed from first principles (AP1)."""

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        k = Symbol('k')
        assert simplify(kappa_formula("heisenberg", k=k) - k) == 0

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        c = Symbol('c')
        assert simplify(kappa_formula("virasoro", c=c) - c / 2) == 0

    def test_kappa_sl2(self):
        """kappa(sl_2_k) = 3(k+2)/4."""
        k = Symbol('k')
        expected = Rational(3) * (k + 2) / 4
        assert simplify(kappa_formula("sl2", k=k) - expected) == 0

    def test_kappa_sl3(self):
        """kappa(sl_3_k) = 4(k+3)/3."""
        k = Symbol('k')
        expected = Rational(4) * (k + 3) / 3
        assert simplify(kappa_formula("sl3", k=k) - expected) == 0

    def test_kappa_w3(self):
        """kappa(W_3_c) = 5c/6."""
        c = Symbol('c')
        assert simplify(kappa_formula("w3", c=c) - 5 * c / 6) == 0

    def test_kappa_bc_at_lambda_2(self):
        """kappa(bc at lambda=2) = -13."""
        result = kappa_formula("bc", **{"lambda": Rational(2)})
        assert simplify(result + 13) == 0

    def test_kappa_bc_at_lambda_half(self):
        """kappa(bc at lambda=1/2) = 1/2."""
        result = kappa_formula("bc", **{"lambda": Rational(1, 2)})
        assert simplify(result - Rational(1, 2)) == 0

    def test_kappa_anti_symmetry_sl2(self):
        """sl_2: kappa + kappa' = 0 under Feigin-Frenkel."""
        result = verify_kappa_anti_symmetry("sl2")
        assert result["anti_symmetry_holds"] is True

    def test_kappa_anti_symmetry_sl3(self):
        """sl_3: kappa + kappa' = 0 under Feigin-Frenkel."""
        result = verify_kappa_anti_symmetry("sl3")
        assert result["anti_symmetry_holds"] is True

    def test_kappa_complementarity_virasoro(self):
        """Virasoro: kappa + kappa' = 13."""
        result = verify_kappa_anti_symmetry("virasoro")
        assert result["anti_symmetry_holds"] is True

    def test_kappa_complementarity_w3(self):
        """W_3: kappa + kappa' = 250/3."""
        result = verify_kappa_anti_symmetry("w3")
        assert result["anti_symmetry_holds"] is True


# ═══════════════════════════════════════════════════════════════════════════
# Section 10: Cross-Family Consistency (AP10)
# ═══════════════════════════════════════════════════════════════════════════

class TestCrossFamilyConsistency:
    """Cross-family kappa checks — the REAL verification (AP10)."""

    def test_all_cross_family_checks(self):
        """All cross-family kappa consistency checks pass."""
        results = cross_family_kappa_consistency()
        for name, ok in results.items():
            assert ok, f"Cross-family check failed: {name}"

    def test_additivity_26_bosons(self):
        """26 free bosons: kappa = 26 * 1/2 = 13."""
        results = cross_family_kappa_consistency()
        assert results["additivity_26_bosons"]

    def test_bosonic_string_cancellation(self):
        """26 bosons + bc ghosts: total kappa = 0."""
        results = cross_family_kappa_consistency()
        assert results["bosonic_string_cancellation"]

    def test_virasoro_self_dual_c13(self):
        """Virasoro self-dual at c=13."""
        results = cross_family_kappa_consistency()
        assert results["virasoro_self_dual_c13"]

    def test_virasoro_not_self_dual_c26(self):
        """Virasoro NOT self-dual at c=26."""
        results = cross_family_kappa_consistency()
        assert results["virasoro_NOT_self_dual_c26"]


# ═══════════════════════════════════════════════════════════════════════════
# Section 11: Faber-Pandharipande Numbers
# ═══════════════════════════════════════════════════════════════════════════

class TestFaberPandharipande:
    """Tests for Faber-Pandharipande numbers lambda_g^FP."""

    def test_lambda_1_equals_1_over_24(self):
        """lambda_1^FP = 1/24."""
        fp = verify_faber_pandharipande()
        assert fp["values"][1]["computed"] == Rational(1, 24)

    def test_lambda_2_equals_7_over_5760(self):
        """lambda_2^FP = 7/5760."""
        fp = verify_faber_pandharipande()
        assert fp["values"][2]["computed"] == Rational(7, 5760)

    def test_lambda_3_equals_31_over_967680(self):
        """lambda_3^FP = 31/967680."""
        fp = verify_faber_pandharipande()
        assert fp["values"][3]["computed"] == Rational(31, 967680)

    def test_all_lambda_positive(self):
        """All Faber-Pandharipande numbers are positive."""
        fp = verify_faber_pandharipande()
        assert fp["all_positive"] is True

    def test_known_values_match(self):
        """Known lambda_g values match computation."""
        fp = verify_faber_pandharipande()
        assert fp["known_matches"] is True


# ═══════════════════════════════════════════════════════════════════════════
# Section 12: Genus Expansion Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestGenusExpansion:
    """Tests for F_g(A) = kappa(A) * lambda_g^FP from BV perspective."""

    def test_heisenberg_F1(self):
        """Heisenberg F_1 = kappa/24."""
        kappa = Symbol('kappa')
        bv = heisenberg_bv(kappa)
        expansion = genus_expansion_from_bv(bv, 3)
        assert simplify(expansion[1] - kappa / 24) == 0

    def test_virasoro_F1(self):
        """Virasoro F_1 = c/48."""
        c = Symbol('c')
        bv = virasoro_bv(c)
        expansion = genus_expansion_from_bv(bv, 3)
        assert simplify(expansion[1] - c / 48) == 0

    def test_sl2_F1(self):
        """sl_2 F_1 = (k+2)/32."""
        k = Symbol('k')
        bv = affine_km_bv("sl2", k)
        expansion = genus_expansion_from_bv(bv, 3)
        expected = Rational(3) * (k + 2) / 4 / 24
        assert simplify(expansion[1] - expected) == 0


# ═══════════════════════════════════════════════════════════════════════════
# Section 13: Full Family Verification Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestFullFamilyVerification:
    """Full chain-level verification for each family."""

    def test_heisenberg_full(self):
        """Full Heisenberg chain-level verification passes."""
        result = verify_heisenberg_chain_level()
        assert result["qme_genus0"].satisfied is True
        assert result["complementarity"]["complementarity_holds"] is True

    def test_virasoro_full(self):
        """Full Virasoro chain-level verification passes."""
        result = verify_virasoro_chain_level()
        assert result["qme_genus0"].satisfied is True
        assert result["complementarity"]["complementarity_holds"] is True
        assert result["self_duality_verified"] is True
        assert result["bosonic_string"]["anomaly_cancelled"] is True

    def test_w3_full(self):
        """Full W_3 chain-level verification passes."""
        result = verify_w3_chain_level()
        assert result["qme_genus0"].satisfied is True
        assert result["complementarity"]["complementarity_holds"] is True

    def test_bc_full(self):
        """Full bc system chain-level verification passes."""
        result = verify_bc_chain_level()
        assert result["qme_genus0"].satisfied is True
        assert result["ghost_system_c"] == -26
        assert result["ghost_system_kappa"] == -13
        assert result["bosonic_c"] == 1
        assert result["bosonic_kappa"] == Rational(1, 2)


# ═══════════════════════════════════════════════════════════════════════════
# Section 14: BV Algebra Factory Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestBVAlgebraFactories:
    """Tests for BV algebra construction factories."""

    def test_heisenberg_bv_kappa(self):
        """Heisenberg BV algebra has correct kappa."""
        bv = heisenberg_bv(Rational(1, 2))
        assert bv.kappa == Rational(1, 2)

    def test_virasoro_bv_kappa(self):
        """Virasoro BV algebra at c=26 has kappa=13."""
        bv = virasoro_bv(Rational(26))
        assert simplify(bv.kappa - 13) == 0

    def test_affine_sl2_bv_kappa(self):
        """sl_2 BV algebra at k=1 has kappa = 3*3/4 = 9/4."""
        bv = affine_km_bv("sl2", Rational(1))
        assert simplify(bv.kappa - Rational(9, 4)) == 0

    def test_w3_bv_kappa(self):
        """W_3 BV algebra at c=2 has kappa = 5*2/6 = 5/3."""
        bv = w3_bv(Rational(2))
        assert simplify(bv.kappa - Rational(5, 3)) == 0

    def test_bc_system_lambda_2(self):
        """bc system at lambda=2 has c=-26, kappa=-13."""
        bv = bc_system_bv(Rational(2))
        assert simplify(bv.central_charge + 26) == 0
        assert simplify(bv.kappa + 13) == 0

    def test_affine_sl3_kappa(self):
        """sl_3 at k=0 has kappa = 4*3/3 = 4."""
        bv = affine_km_bv("sl3", Rational(0))
        assert simplify(bv.kappa - 4) == 0


# ═══════════════════════════════════════════════════════════════════════════
# Section 15: d^2 and Period Correction Tests
# ═══════════════════════════════════════════════════════════════════════════

class TestDSquaredAndPeriodCorrection:
    """Tests for d_fib^2 and the period correction D_1^2 = 0."""

    def test_d_squared_genus1_coefficient(self):
        """d^2 coefficient at genus 1 is kappa."""
        kappa = Symbol('kappa')
        result = d_squared_genus1(kappa)
        assert result["d_squared_coefficient"] == kappa

    def test_period_correction_absorbs_curvature(self):
        """F_1 = kappa/24 absorbs the genus-1 curvature."""
        kappa = Symbol('kappa')
        result = d_squared_genus1(kappa)
        assert simplify(result["period_correction_F1"] - kappa / 24) == 0

    def test_total_differential_nilpotent(self):
        """After period correction, D_1^2 = 0."""
        kappa = Symbol('kappa')
        result = d_squared_genus1(kappa)
        assert result["total_differential_nilpotent"] is True


# ═══════════════════════════════════════════════════════════════════════════
# Section 16: W_3 String Anomaly (Speculative)
# ═══════════════════════════════════════════════════════════════════════════

class TestW3String:
    """Tests for hypothetical W_3 string anomaly cancellation."""

    def test_w3_string_anomaly_cancels(self):
        """W_3 string at c=100: anomaly cancels."""
        result = w3_string_anomaly_cancellation()
        assert result["anomaly_cancelled"] is True
        assert result["status"] == "speculative"
