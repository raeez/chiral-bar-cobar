"""Guards for conductor, cross-channel, and critical-reflection scope."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"


def visible_text() -> str:
    return "\n".join(
        line
        for line in SOURCE.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def window_after_label(text: str, label: str, lines: int) -> str:
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    return "\n".join(text.split(anchor, 1)[1].splitlines()[:lines])


class TestConductorCrossChannelScope:
    def test_tau_identity_uses_delta_cross_channel_not_delta_capital(self):
        text = visible_text()
        window = normalized(window_after_label(text, "thm:shadow-tau-kw", 55))

        assert "\\delta F_g^{\\mathrm{cross}}(\\cA)" in window
        assert "\\Delta F_g^{\\mathrm{cross}}(\\cA)" not in window

    def test_conductor_is_scalar_diagnostic_not_cross_channel_vanishing(self):
        text = visible_text()
        window = normalized(
            window_after_label(text, "prop:koszul-conductor-anomaly-vanishing", 95)
        )

        required = (
            "scalar anomaly diagnostic",
            "not, by itself, a theorem",
            "mixed stable-graph contribution",
            "\\delta F_g^{\\mathrm{cross}}(\\cA)",
            "strict channel-decoupling package \\(H_{\\mathrm{SCD}}\\)",
            "must be computed or separately proved zero",
        )
        for fragment in required:
            assert fragment in window

        forbidden = (
            "controlled by $\\kappa + \\kappa'$",
            "vanishes identically when",
            "Feigin--Frenkel involution",
        )
        for fragment in forbidden:
            assert fragment not in window

    def test_ds_level_reflections_are_not_named_feigin_frenkel_involutions_here(self):
        text = visible_text()
        windows = [
            normalized(window_after_label(text, "rem:ds-tower-non-a", 45)),
            normalized(window_after_label(text, "prop:koszul-conductor-wn", 35)),
            normalized(
                window_after_label(text, "prop:koszul-conductor-anomaly-vanishing", 95)
            ),
        ]

        for window in windows:
            assert "critical-level reflection" in window
            assert "Feigin--Frenkel involution" not in window
