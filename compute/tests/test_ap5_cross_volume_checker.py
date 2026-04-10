"""Tests for the AP5 cross-volume consistency checker.

Each test cites the anti-pattern (AP) it verifies.  The cases use a small
fixture tree of synthetic .tex files so the tests are deterministic and do
not depend on the live state of the three volumes.  A final integration
test exercises the real sweep against the actual volume roots and only
asserts structural invariants (shape of the return value, report string)
so it stays green even as the manuscript evolves.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from compute.lib.ap5_cross_volume_checker import (
    AP5Checker,
    CANONICAL_FORMULAS,
    CanonicalFormula,
    CheckResult,
    run_default_sweep,
)


# ---------------------------------------------------------------------------
# Synthetic fixture: a miniature three-volume tree we can mutate per test.
# ---------------------------------------------------------------------------

def _write(root: Path, rel: str, content: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content), encoding="utf-8")


@pytest.fixture
def fake_volumes(tmp_path: Path):
    """Create a minimal three-volume tree for isolated AP5 tests."""
    vol1 = tmp_path / "vol1"
    vol2 = tmp_path / "vol2"
    vol3 = tmp_path / "vol3"
    for v in (vol1, vol2, vol3):
        (v / "chapters").mkdir(parents=True)
        (v / "appendices").mkdir(parents=True)

    # Canonical, clean content in all three volumes.
    _write(
        vol1,
        "chapters/bar.tex",
        r"""
        The bar complex $T^c(s^{-1}\bar{A})$ is the primitive object.
        The affine KM r-matrix is $k\cdot\Omega/z$, which vanishes at $k=0$.
        We write $\kappa(H_k) = k$ and $\kappa(V_k(\fg))$.
        """,
    )
    _write(
        vol2,
        "chapters/e1.tex",
        r"""
        The E_1 primitive uses $T^c(s^{-1}\bar{A})$.
        The level-k r-matrix $k\cdot\Omega/z$ respects AP126.
        """,
    )
    _write(
        vol3,
        "chapters/cy.tex",
        r"""
        In the CY setting we use subscripted $\kappa_{\ch}$ and
        $\kappa_{\BKM}$ throughout; bare kappa is forbidden.
        """,
    )
    return {"vol1": vol1, "vol2": vol2, "vol3": vol3}


def _checker(fake_volumes) -> AP5Checker:
    return AP5Checker(
        vol1_path=fake_volumes["vol1"],
        vol2_path=fake_volumes["vol2"],
        vol3_path=fake_volumes["vol3"],
    )


# ---------------------------------------------------------------------------
# Test 1 -- AP126: bare \Omega/z must not appear in any volume.
# ---------------------------------------------------------------------------

def test_ap126_bare_omega_over_z_clean(fake_volumes):
    """AP126: every r-matrix must carry an explicit level factor."""
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=r"(?<![*k0-9])\\Omega/z",
        description="AP126 bare Omega/z",
        expected_per_volume={"vol1": 0, "vol2": 0, "vol3": 0},
        ap_tag="AP126",
    )
    assert result.ok, result.drift
    assert result.observed == {"vol1": 0, "vol2": 0, "vol3": 0}


def test_ap126_violation_detected(fake_volumes):
    """Planting a bare \\Omega/z must be caught."""
    _write(
        fake_volumes["vol1"],
        "chapters/violation.tex",
        r"The naive r-matrix \Omega/z is wrong (AP126).",
    )
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=r"(?<![*k0-9])\\Omega/z",
        description="AP126 bare Omega/z",
        expected_per_volume={"vol1": 0, "vol2": 0, "vol3": 0},
        ap_tag="AP126",
    )
    assert not result.ok
    assert result.observed["vol1"] >= 1


# ---------------------------------------------------------------------------
# Test 2 -- AP113: bare \kappa in Vol III forbidden.
# ---------------------------------------------------------------------------

def test_ap113_bare_kappa_vol3_clean(fake_volumes):
    """AP113: Vol III kappa must always be subscripted."""
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=r"\\kappa(?![_^a-zA-Z(])",
        description="AP113 bare kappa in Vol III",
        expected_per_volume={"vol3": 0},
        ap_tag="AP113",
        scope=("vol3",),
    )
    assert result.ok
    assert result.observed == {"vol3": 0}


def test_ap113_bare_kappa_vol3_violation(fake_volumes):
    """Planting a bare \\kappa in Vol III must be flagged."""
    _write(
        fake_volumes["vol3"],
        "chapters/bad.tex",
        r"Here is bare \kappa = 1 without subscript.",
    )
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=r"\\kappa(?![_^a-zA-Z(])",
        description="AP113 bare kappa in Vol III",
        expected_per_volume={"vol3": 0},
        ap_tag="AP113",
        scope=("vol3",),
    )
    assert not result.ok
    assert result.observed["vol3"] >= 1


# ---------------------------------------------------------------------------
# Test 3 -- git rule: no AI attribution anywhere.
# ---------------------------------------------------------------------------

def test_git_no_ai_attribution(fake_volumes):
    """All commits are authored by Raeez Lorgat; no AI attribution in .tex."""
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=(
            r"(?i)co-authored-by|anthropic|claude\.ai|generated by claude"
        ),
        description="AI attribution keywords",
        expected_per_volume={"vol1": 0, "vol2": 0, "vol3": 0},
        ap_tag="git",
    )
    assert result.ok
    assert sum(result.observed.values()) == 0


# ---------------------------------------------------------------------------
# Test 4 -- prose law 3: no em dashes.
# ---------------------------------------------------------------------------

def test_em_dash_absence(fake_volumes):
    """Prose law 3: em dash U+2014 forbidden."""
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern="\u2014",
        description="Em dash",
        expected_per_volume={"vol1": 0, "vol2": 0, "vol3": 0},
        ap_tag="prose",
    )
    assert result.ok


def test_em_dash_violation_flagged(fake_volumes):
    """Planting an em dash in Vol II must be flagged."""
    _write(
        fake_volumes["vol2"],
        "chapters/dash.tex",
        "An em dash \u2014 appears here.",
    )
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern="\u2014",
        description="Em dash",
        expected_per_volume={"vol1": 0, "vol2": 0, "vol3": 0},
        ap_tag="prose",
    )
    assert not result.ok
    assert result.observed["vol2"] >= 1


# ---------------------------------------------------------------------------
# Test 5 -- compile-breaker typo \end{xxx>
# ---------------------------------------------------------------------------

def test_end_environment_typo_absent(fake_volumes):
    """No \\end{env> typos; these are compile-breakers."""
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=r"\\end\{[a-zA-Z*]+>",
        description="\\end{env> compile-breaker typo",
        expected_per_volume={"vol1": 0, "vol2": 0, "vol3": 0},
        ap_tag="build",
    )
    assert result.ok


# ---------------------------------------------------------------------------
# Test 6 -- V2-AP26: hardcoded Part~[IVX] occurrences bounded.
# ---------------------------------------------------------------------------

def test_hardcoded_part_bounded(fake_volumes):
    """Hardcoded Part~[IVX] occurrences tolerated within an envelope."""
    _write(
        fake_volumes["vol1"],
        "chapters/xref.tex",
        "See Part~I for the overture and Part~IV for the bridges.",
    )
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=r"Part~[IVX]+\b",
        description="Hardcoded Part~[IVX]",
        expected_per_volume={
            "vol1": (0, 10),
            "vol2": (0, 10),
            "vol3": (0, 10),
        },
        ap_tag="V2-AP26",
    )
    assert result.ok
    assert result.observed["vol1"] == 2


# ---------------------------------------------------------------------------
# Test 7 -- run_all returns a list of CheckResult.
# ---------------------------------------------------------------------------

def test_run_all_returns_list(fake_volumes):
    """run_all must return a list of CheckResult, one per canonical formula."""
    checker = _checker(fake_volumes)
    results = checker.run_all()
    assert isinstance(results, list)
    assert len(results) == len(CANONICAL_FORMULAS)
    assert all(isinstance(r, CheckResult) for r in results)
    # Every result must have observed counts for its in-scope volumes.
    for r in results:
        for vol in r.scope:
            assert vol in r.observed


# ---------------------------------------------------------------------------
# Test 8 -- report generation produces a non-empty string with headers.
# ---------------------------------------------------------------------------

def test_generate_report_structure(fake_volumes):
    """generate_report returns a formatted ASCII report."""
    checker = _checker(fake_volumes)
    checker.run_all()
    report = checker.generate_report()
    assert isinstance(report, str)
    assert "AP5 CROSS-VOLUME CONSISTENCY REPORT" in report
    assert "checks run:" in report
    assert "CLEAN CHECKS" in report


# ---------------------------------------------------------------------------
# Test 9 -- AP124: cross-volume duplicate \label detection.
# ---------------------------------------------------------------------------

def test_ap124_duplicate_label_detection(fake_volumes):
    """AP124: a label that occurs in two volumes must be flagged."""
    _write(
        fake_volumes["vol1"],
        "chapters/lbl1.tex",
        r"A theorem: \label{thm:shared-label} done.",
    )
    _write(
        fake_volumes["vol2"],
        "chapters/lbl2.tex",
        r"Another theorem: \label{thm:shared-label} done.",
    )
    checker = _checker(fake_volumes)
    dup_formula = next(f for f in CANONICAL_FORMULAS if f.duplicate_label)
    result = checker.check_duplicate_labels(dup_formula)
    assert not result.ok
    joined = " ".join(result.drift)
    assert "thm:shared-label" in joined


def test_ap124_no_cross_volume_duplicates(fake_volumes):
    """Distinct labels per volume: no duplicates flagged."""
    _write(
        fake_volumes["vol1"],
        "chapters/lbl1.tex",
        r"\label{thm:vol1-only}",
    )
    _write(
        fake_volumes["vol2"],
        "chapters/lbl2.tex",
        r"\label{thm:vol2-only}",
    )
    checker = _checker(fake_volumes)
    dup_formula = next(f for f in CANONICAL_FORMULAS if f.duplicate_label)
    result = checker.check_duplicate_labels(dup_formula)
    assert result.ok


# ---------------------------------------------------------------------------
# Test 10 -- AP1: canonical kappa(H_k)=k present in Vol I.
# ---------------------------------------------------------------------------

def test_ap1_canonical_heisenberg_kappa_present(fake_volumes):
    """AP1: kappa(H_k)=k canonical form must be writable in Vol I fixture."""
    checker = _checker(fake_volumes)
    result = checker.check_formula(
        pattern=r"\\kappa\s*\(\s*H_k\s*\)\s*=\s*k",
        description="Canonical Heisenberg kappa",
        expected_per_volume={"vol1": (1, 10), "vol2": "any", "vol3": "any"},
        ap_tag="AP1",
    )
    assert result.ok, (
        f"expected at least one occurrence in Vol I, got {result.observed}"
    )
    assert result.observed["vol1"] >= 1


# ---------------------------------------------------------------------------
# Test 11 -- AP132: augmentation-ideal bar complex present, unbarred absent.
# ---------------------------------------------------------------------------

def test_ap132_augmentation_ideal_discipline(fake_volumes):
    """AP132: T^c(s^{-1} bar A) present, T^c(s^{-1} A) absent."""
    checker = _checker(fake_volumes)
    good = checker.check_formula(
        pattern=r"T\^c\(\s*s\^\{-1\}\s*\\bar\s*\{?A\}?\s*\)",
        description="augmentation-ideal present",
        expected_per_volume={"vol1": (1, 100)},
        ap_tag="AP132",
        scope=("vol1",),
    )
    bad = checker.check_formula(
        pattern=r"T\^c\(\s*s\^\{-1\}\s*A\s*\)",
        description="augmentation missing",
        expected_per_volume={"vol1": 0, "vol2": 0, "vol3": 0},
        ap_tag="AP132",
    )
    assert good.ok
    assert bad.ok


# ---------------------------------------------------------------------------
# Test 12 -- Envelope semantics: int, tuple, "any".
# ---------------------------------------------------------------------------

def test_envelope_semantics(fake_volumes):
    """Exercise the three envelope kinds accepted by check_formula."""
    checker = _checker(fake_volumes)
    for envelope, should_pass in [
        (0, True),        # exact count
        ((0, 5), True),   # bound
        ("any", True),    # unconstrained
        (99, False),      # exact count mismatch
    ]:
        result = checker.check_formula(
            pattern=r"this-string-never-appears-anywhere-xyz123",
            description=f"envelope test {envelope}",
            expected_per_volume={
                "vol1": envelope,
                "vol2": envelope,
                "vol3": envelope,
            },
            ap_tag="test",
        )
        assert result.ok is should_pass, (envelope, result.drift)


# ---------------------------------------------------------------------------
# Test 13 -- Live volume sweep (structural only).
# ---------------------------------------------------------------------------

@pytest.mark.filterwarnings("ignore")
def test_live_sweep_runs():
    """The real sweep across the three volume roots must complete cleanly.

    We only assert structural invariants (length of the result list, the
    presence of the report header) so this stays green as the manuscript
    evolves and new anti-patterns are caught and cleared.
    """
    checker = AP5Checker()
    results = checker.run_all()
    assert len(results) == len(CANONICAL_FORMULAS)
    for r in results:
        assert isinstance(r.observed, dict)
        for v in r.scope:
            assert v in r.observed
            assert isinstance(r.observed[v], int)
    report = checker.generate_report(results)
    assert "AP5 CROSS-VOLUME CONSISTENCY REPORT" in report


# ---------------------------------------------------------------------------
# Test 14 -- run_default_sweep returns a non-empty report string.
# ---------------------------------------------------------------------------

def test_run_default_sweep_returns_string():
    """The module-level convenience function returns a formatted report."""
    report = run_default_sweep()
    assert isinstance(report, str)
    assert "AP5 CROSS-VOLUME CONSISTENCY REPORT" in report
    assert "checks run:" in report


# ---------------------------------------------------------------------------
# Test 15 -- CANONICAL_FORMULAS catalog integrity.
# ---------------------------------------------------------------------------

def test_canonical_library_has_fifteen_entries():
    """The canonical library must carry at least the 15 promised checks."""
    assert len(CANONICAL_FORMULAS) >= 15
    # Every entry must carry an AP tag and a non-empty description.
    for f in CANONICAL_FORMULAS:
        assert isinstance(f, CanonicalFormula)
        assert f.ap_tag, f.key
        assert f.description, f.key
        assert f.pattern, f.key
    keys = {f.key for f in CANONICAL_FORMULAS}
    # Spot-check the flagship entries.
    for required in (
        "ap126_bare_omega_over_z",
        "ap113_bare_kappa_vol3",
        "git_ai_attribution",
        "prose_em_dash",
        "ap124_duplicate_labels",
        "ap132_bar_no_augmentation",
        "ap136_wn_harmonic_wrong",
        "ap39_kappa_equals_s2",
    ):
        assert required in keys, f"missing canonical entry: {required}"
