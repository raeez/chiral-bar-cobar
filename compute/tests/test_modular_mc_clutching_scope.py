"""Scope guards for the modular MC clutching proof."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CONFIGURATION_SPACES = ROOT / "chapters/theory/configuration_spaces.tex"


def visible_configuration_spaces() -> str:
    text = CONFIGURATION_SPACES.read_text()
    return "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("%")
    )


def window_after(label: str, chars: int) -> str:
    text = visible_configuration_spaces()
    start = text.find(label)
    assert start >= 0, f"missing label {label}"
    return text[start:start + chars]


def assert_anchor(window: str, anchor: str) -> None:
    normalized_window = re.sub(r"\s+", " ", window)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in window or normalized_anchor in normalized_window, anchor


class TestModularMCClutchingScope:
    def test_fixed_fiber_bordered_fm_result_excludes_nodal_blowups(self):
        text = visible_configuration_spaces()
        label = r"\label{eq:bordered-fm-result}"
        start = text.find(label)
        assert start >= 0, "missing fixed bordered FM result"
        end = text.find(r"\end{equation}", start)
        assert end >= 0, "fixed bordered FM result display is not closed"
        display = text[start:end]
        assert r"\Delta_B^{\mathrm{bdy}}" in display
        assert r"\Delta_{S,B,j}^{\mathrm{mix}}" in display
        assert r"D_\Gamma^{\mathrm{nod}}" not in display

        following = text[end:end + 900]
        assert_anchor(following, "In the relative modular family")
        assert_anchor(following, r"$D_\Gamma^{\mathrm{nod}}$")
        assert_anchor(following, "not boundary faces of the fixed-fiber space")

    def test_boundary_decomposition_separates_fixed_three_from_relative_four(self):
        window = window_after(r"\label{prop:four-type-boundary}", 15000)
        for anchor in (
            "fixed-fiber bordered FM",
            "three collision types",
            r"\label{eq:boundary-three-types-fixed}",
            "relative bordered FM compactification",
            "add a fourth type",
            r"\label{eq:boundary-four-types}",
            "there is no $t_e$ coordinate, hence no Type~IV face",
        ):
            assert_anchor(window, anchor)
        for forbidden in (
            "decomposes into four types of smooth faces",
            "Only Type~I and Type~IV faces are present",
        ):
            assert forbidden not in window

    def test_modular_mc_proof_is_two_source_not_fixed_curve_type_iv_stokes(self):
        window = window_after(r"\label{thm:modular-mc-clutching}", 15000)
        for anchor in (
            "Source 1: fixed-fiber Stokes",
            "Source 2: modular-operad square-zero",
            "not a boundary face of the\nfixed-fiber Stokes chain",
            "fixed-fiber Stokes calculation for collision faces",
            "relative modular-operad square-zero identity",
            r"\label{eq:modular-two-source-assembly}",
            "not a single fixed-curve Stokes formula",
        ):
            assert_anchor(window, anchor)
        for forbidden in (
            "Stokes' theorem on the four-type boundary",
            "Summing the contributions from all four boundary types",
            r"\label{eq:stokes-assembly}",
            r"0 &= \int_{\partial\sigma} \omega^{(g)}",
        ):
            assert forbidden not in window
