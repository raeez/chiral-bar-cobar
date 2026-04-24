"""
Guardrails for the MC5 class-M ambient separation.

The active manuscript proves the pro-object, J-adic, and
filtered-completed comparison on the strict Mittag-Leffler finite-window
surface, while keeping that surface distinct from the raw direct-sum bar
complex.  The corrected status is:

1. raw direct-sum class-M chain-level comparison in Ch(Vect) fails;
2. completed/pro/J-adic replacements are equivalent presentations of the
   strict finite-window surface;
3. no statement identifies that completed surface with the raw direct sum.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MC5_TEX = ROOT / "chapters/theory/mc5_class_m_chain_level_platonic.tex"
INTRO_TEX = ROOT / "chapters/theory/introduction.tex"


def _window_around(text: str, label: str, radius: int = 1400) -> str:
    idx = text.index(label)
    return text[max(0, idx - radius) : idx + radius]


def _env_block(text: str, label: str) -> str:
    idx = text.index(label)
    begin_candidates = [
        text.rfind("\\begin{theorem}", 0, idx),
        text.rfind("\\begin{proposition}", 0, idx),
        text.rfind("\\begin{corollary}", 0, idx),
    ]
    begin = max(begin_candidates)
    end_candidates = [
        text.find("\\end{theorem}", idx),
        text.find("\\end{proposition}", idx),
        text.find("\\end{corollary}", idx),
    ]
    end = min(candidate for candidate in end_candidates if candidate != -1)
    return text[begin:end]


def test_mc5_pro_and_j_adic_surfaces_are_proved_on_strict_ml_surface():
    tex = MC5_TEX.read_text()
    guarded_labels = (
        "thm:mc5-class-m-chain-level-pro-ambient",
        "cor:mc5-class-m-chain-level-on-inverse-limit",
        "thm:mc5-class-m-topological-chain-level-j-adic",
        "prop:ambient-equivalence",
    )
    for label in guarded_labels:
        window = _env_block(tex, "\\label{" + label + "}")
        assert "\\ClaimStatusProvedHere" in window
        assert "\\ClaimStatusConditional" not in window

    assert "strict Mittag--Leffler" in tex
    assert "not equal" in tex or "not an assertion" in tex


def test_raw_direct_sum_failure_remains_real():
    tex = MC5_TEX.read_text()
    assert "raw direct-sum failure" in tex
    assert "genuine obstruction on that raw surface" in tex
    assert "not identify" in tex


def test_frontier_summary_does_not_reclose_mc5():
    intro = INTRO_TEX.read_text()
    window = _window_around(intro, "\\label{sec:mc-frontier-intro}", 2400)
    assert "MC5 separates into several surfaces" in window
    assert "strict Mittag" in window
    assert "does not identify" in window

    stale_fragments = (
        "proved on the canonical " + "pro-object",
        "proved on three " + "equivalent ambients",
        "proved on those " + "equivalent ambients",
    )
    for fragment in stale_fragments:
        assert fragment not in window
