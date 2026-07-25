"""Scope certificate for Theorem B and its neighbouring derived lanes.

The canonical theorem is quadratic Koszul recognition for
``q_A: A^i -> B_X(A)``.  Universal bar--cobar reconstruction belongs to
Theorem A.  Positselski's Correspondence Theorem 5.2 concerns a fixed CDG
coalgebra, while his Theorem 6.5 concerns modules attached to an acyclic
twisting cochain.  These tests keep the four type signatures distinct.
"""

from __future__ import annotations

from pathlib import Path

from compute.lib.independent_verification import independent_verification


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/theorem_B_scope_platonic.tex"


def _environment(text: str, label: str) -> str:
    """Return the theorem-like environment containing ``label``."""
    index = text.index(label)
    starts = [
        text.rfind(r"\begin{theorem}", 0, index),
        text.rfind(r"\begin{proposition}", 0, index),
        text.rfind(r"\begin{corollary}", 0, index),
    ]
    start = max(starts)
    ends = [
        text.find(r"\end{theorem}", index),
        text.find(r"\end{proposition}", index),
        text.find(r"\end{corollary}", index),
    ]
    end = min(candidate for candidate in ends if candidate >= 0)
    return text[start:end]


@independent_verification(
    claim="thm:theorem-B-scope-quadratic-recognition",
    derived_from=[
        "quadratic chiral comparison q_A and hypothesis package H_CL",
        "PBW/bar filtration comparison in the chiral de Rham model",
    ],
    verified_against=[
        "Loday--Vallette 2012 Theorem 2.3.2 fundamental theorem of "
        "twisting morphisms",
        "Loday--Vallette 2012 Theorem 3.4.6 Koszul criterion",
    ],
    disjoint_rationale=(
        "The manuscript derives the chiral transport from its explicit "
        "comparison package, while Loday--Vallette supplies the independent "
        "ordinary quadratic criterion over a point."
    ),
)
def test_theorem_b_is_quadratic_recognition():
    tex = TARGET.read_text()
    theorem = _environment(
        tex, r"\label{thm:theorem-B-scope-quadratic-recognition}"
    )
    flat = " ".join(theorem.split())

    for token in (
        r"A^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)",
        r"q_A\colon A^{\mathrm i}\to B_X(A)",
        r"\Omega_X(A^{\mathrm i})\to A",
        r"K^L_{\tau_{\mathrm i}}",
        r"K^R_{\tau_{\mathrm i}}",
        r"H_{\mathrm{CL}}(A,A^{\mathrm i},\tau_{\mathrm i})",
        "Theorem~2.3.2",
        "Theorem~3.4.6",
    ):
        assert token in flat

    assert r"D^{\mathrm{co}}" not in flat
    assert r"D^{\mathrm{ctr}}" not in flat


def test_fixed_coalgebra_correspondence_has_its_own_hypotheses():
    tex = TARGET.read_text()
    finite = _environment(
        tex, r"\label{thm:chiral-positselski-at-each-weight}"
    )
    completed = _environment(
        tex, r"\label{thm:chiral-positselski-weight-completed}"
    )
    lane = " ".join((finite + completed).split())

    for token in (
        "fixed-coalgebra",
        r"D^{\mathrm{co}}",
        r"D^{\mathrm{ctr}}",
        "(CP1)",
        "(CP2)",
        "(CP3)",
        "strict Mittag",
    ):
        assert token in lane

    assert "q_A" not in lane
    assert r"A^{\mathrm i}" not in lane


def test_opening_types_the_four_lanes_and_retires_the_conflation():
    tex = TARGET.read_text()
    opening = tex[:9000]

    for token in (
        "belongs to Theorem~A",
        "Theorem~5.2",
        "Theorem~6.5",
        r"q_A\colon A^{\mathrm i}\longrightarrow B_X(A)",
        r"\mathsf{Tw}^{\mathrm{ch}}_{\mathrm{acyc}}",
    ):
        assert token in opening

    retired_phrases = (
        "Theorem~B (chiral Positselski)",
        "chiral Positselski (Theorem~B)",
        "Module-level Theorem B",
        "Theorem B as $\\eta_C$",
    )
    for phrase in retired_phrases:
        assert phrase not in tex
