"""Scope guard for the simple-quotient sl2 bar diagnostic.

The simple-quotient helper is useful finite evidence, but it substitutes
the universal V_k(sl2) cohomology model for the quotient cohomology table
and uses Verma dimensions above the Shapovalov budget.  It must not be
treated as a proof of all admissible sl2 Koszulness.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

ENGINE = ROOT / "compute/lib/bar_cohomology_simple_quotient_engine.py"
TESTS = ROOT / "compute/tests/test_bar_cohomology_simple_quotient_engine.py"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"

LIVE_TEX_SURFACES = (
    ROOT / "chapters/theory/chiral_koszul_pairs.tex",
    ROOT / "chapters/examples/kac_moody.tex",
    ROOT / "chapters/connections/concordance.tex",
    ROOT / "chapters/theory/theorem_h_off_koszul_platonic.tex",
    ROOT / "chapters/frame/preface.tex",
    ROOT / "chapters/frame/preface_sections5_9_draft.tex",
    ROOT / "standalone/koszulness_fourteen_characterizations.tex",
    ROOT / "standalone/survey_track_a_compressed.tex",
    ROOT / "standalone/survey_modular_koszul_duality.tex",
    ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
    ROOT / "standalone/programme_summary.tex",
    ROOT / "standalone/programme_summary_sections9_14.tex",
)

COMPUTE_SCOPE_SURFACES = (
    ROOT / "compute/lib/theorem_admissible_koszul_sl3_engine.py",
    ROOT / "compute/tests/test_theorem_admissible_koszul_sl3_engine.py",
    ROOT / "compute/lib/vertex_algebra_extensions_engine.py",
    ROOT / "compute/tests/test_vertex_algebra_extensions.py",
    ROOT / "compute/lib/theorem_universal_chiral_genus_extension_engine.py",
    ROOT / "compute/tests/test_theorem_universal_chiral_genus_extension_engine.py",
    ROOT / "compute/lib/admissible_sl3_d1_rank_engine.py",
    ROOT / "compute/tests/test_admissible_sl3_d1_rank_engine.py",
    ROOT / "compute/lib/admissible_sl3_d1_poisson_engine.py",
    ROOT / "compute/tests/test_admissible_sl3_d1_poisson_engine.py",
    ROOT / "compute/lib/theorem_linshaw_rigidity_engine.py",
)


def text(path: Path) -> str:
    return path.read_text()


def compact(source: str) -> str:
    return " ".join(source.split())


def test_simple_quotient_helper_declares_finite_diagnostic_scope():
    combined = compact(text(ENGINE) + "\n" + text(TESTS))
    required = (
        "finite Shapovalov/character diagnostic",
        "not a proof that all admissible L_k(sl_2) are chirally Koszul",
        "legacy universal V_k(sl_2) bar-cohomology model",
        "returns the Verma dimension as an upper-bound placeholder",
        "PBW/Shapovalov detection, finite-window exactness, and strong convergence",
        "model-level Koszul verdict",
        "not proof of all admissible",
    )
    for fragment in required:
        if compact(fragment) not in combined:
            raise AssertionError(f"required fragment missing: {fragment}")


def test_simple_quotient_helper_retired_theorem_phrases():
    combined = text(ENGINE) + "\n" + text(TESTS)
    retired = (
        "STRUCTURAL ANSWER",
        "STRUCTURAL THEOREM",
        "The MAIN RESULT",
        "The key theorem: sl_2 Koszulness is unconditional",
        "L_k(sl_2) is Koszul at ALL admissible levels",
        "L_k(sl_2) is Koszul at ALL levels",
        "Since V_k is Koszul, so is L_k. This covers all admissible levels",
        "H^n(B(L_k(sl_2))) = H^n(B(V_k(sl_2))) for all n",
        "spectral sequence collapses for dimensional reasons",
        "Computes H*(B(L_k(sl_2)))",
    )
    for fragment in retired:
        if compact(fragment) in combined:
            raise AssertionError(f"retired fragment still present: {fragment}")


def test_simple_quotient_runtime_metadata_exposes_nonproof_status():
    from compute.lib.bar_cohomology_simple_quotient_engine import (
        MODEL_SCOPE,
        SimpleQuotientBarEngine,
    )

    assert MODEL_SCOPE["not_proof_all_admissible"] is True
    assert MODEL_SCOPE["uses_universal_cohomology_model"] is True
    assert MODEL_SCOPE["uses_verma_upper_bound_above_shapovalov_budget"] is True

    engine = SimpleQuotientBarEngine(5, 2, max_weight=8)
    result = engine.compute_bar_cohomology()
    assert result.is_koszul is True
    assert result.not_proof_all_admissible is True
    assert result.uses_universal_cohomology_model is True
    assert result.uses_verma_upper_bound_above_shapovalov_budget is True
    assert "PBW/Shapovalov detection" in result.missing_proof_obligation

    analysis = engine.koszulness_structural_analysis()
    assert analysis["is_koszul"] is True
    assert analysis["not_proof_all_admissible"] is True
    assert "diagnostic" in analysis["verdict_scope"]


def test_live_tex_surfaces_keep_admissible_simple_quotients_conditional():
    combined = compact("\n".join(text(path) for path in LIVE_TEX_SURFACES))
    required = (
        "finite Shapovalov and character computations",
        "quotient bar spectral sequence",
        "PBW/Shapovalov detection",
        "finite-window exactness",
        "strong convergence",
        "not a settled input to Theorem~H or bar--cobar inversion",
        "rationality is not a Koszulness criterion",
        "conditional on the quotient-bar package",
        "non-critical PBW/Koszul lane",
        "critical Feigin--Frenkel centre boundary",
        "separate Sugawara/KZ degeneration surface",
        "admissible",
        "simple quotient levels",
    )
    for fragment in required:
        if compact(fragment) not in combined:
            raise AssertionError(f"required fragment missing: {fragment}")

    retired = (
        "admissible Koszulness is settled",
        "rank-$1$ case is completely settled",
        "Koszul at all admissible levels",
        "bar functor preserves surjections",
        "inherits concentration from the universal algebra",
        "including critical and admissible",
        "Koszul at every level including critical",
        "critical and admissible)",
    )
    for fragment in retired:
        if compact(fragment) in combined:
            raise AssertionError(f"retired fragment still present: {fragment}")


def test_compute_surfaces_do_not_promote_admissible_quotients_to_theorems():
    combined = compact("\n".join(text(path) for path in COMPUTE_SCOPE_SURFACES))
    required = (
        "FINITE EVIDENCE / CONDITIONAL",
        '"koszul": None',
        "not promoted into the proved",
        "conditional-model",
        "MODEL DIAGNOSTIC",
        "MODEL-LEVEL TESTS",
        "quotient-bar spectral sequence",
        "finite-window exactness",
        "strong convergence",
        "CONDITIONAL_QUOTIENT_BAR",
    )
    for fragment in required:
        if compact(fragment) not in combined:
            raise AssertionError(f"required fragment missing: {fragment}")

    retired = (
        "PROVED at all admissible levels",
        "For sl_2: L_k(sl_2) IS Koszul at all admissible levels",
        "THEOREM-LEVEL ENGINE",
        "THEOREM-LEVEL TESTS",
        "UNCONDITIONALLY Koszul",
        "confidence='unconditional'",
        "should be unconditional",
        "simple quotient L_k equals the universal algebra V_k",
    )
    for fragment in retired:
        if compact(fragment) in combined:
            raise AssertionError(f"retired fragment still present: {fragment}")


def test_pass_552_and_553_are_recorded_in_ledger_and_matrix():
    ledger = text(LEDGER)
    matrix = text(MATRIX)
    assert "Pass 552: Simple-quotient sl2 bar diagnostic scope" in ledger
    assert "Pass 552 fences the simple-quotient sl2 bar diagnostic" in matrix
    assert "universal-cohomology model" in matrix
    assert "Pass 553: Admissible simple-quotient theorem-surface sync" in ledger
    assert "Pass 553 propagates that correction" in matrix
    assert "admissible simple quotients are finite-evidence/conditional" in matrix
