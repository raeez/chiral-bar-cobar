"""Structural guards for the public five-theorem tables."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PUBLIC_TABLES = (ROOT / "README.md", ROOT / "FRONTIER.md")
CHAIN_SURFACES = PUBLIC_TABLES + (ROOT / "CLAUDE.md", ROOT / "AGENTS.md")


def _row(path: Path, theorem: str) -> str:
    text = path.read_text()
    match = re.search(
        rf"^\|\s*\*\*{theorem}\*\*\s*\|.*$",
        text,
        flags=re.MULTILINE,
    )
    assert match is not None, f"missing theorem-{theorem} row in {path.name}"
    return "".join(match.group(0).split())


def test_public_tables_type_theorem_a_as_reconstruction_and_verdier_algebra():
    for path in PUBLIC_TABLES:
        row = _row(path, "A")
        assert r"\Omega_XB_X(A_b)" in row
        assert r"\mathbbD_{\operatorname{Ran}}B_X(A_b)" in row


def test_public_tables_type_theorem_b_through_the_presentation_map():
    for path in PUBLIC_TABLES:
        row = _row(path, "B")
        assert "q_" in row
        assert r"C_X(s^{-1}V,s^{-2}R)" in row
        assert r"H_{\mathrm{CL}}" in row


def test_public_tables_keep_theorem_c_on_the_ordinary_centre_lane():
    for path in PUBLIC_TABLES:
        row = _row(path, "C")
        assert r"\mathbfC_g" in row
        assert r"\mathcalZ" in row
        assert r"K^\kappa" in row


def test_public_tables_keep_theorem_d_four_typed_outputs():
    for path in PUBLIC_TABLES:
        row = _row(path, "D")
        for token in (
            r"\operatorname{Obs}^{\mathrm{def}}_g",
            r"\mathfrakO_g^K",
            "F_g",
            r"H_D^1",
            r"H_D^K",
            r"H_D^{\mathrm{tr}}",
            r"H_D^{\mathrm{graph}}",
        ):
            assert token in row


def test_public_tables_state_theorem_h_as_family_support_transport():
    for path in PUBLIC_TABLES:
        row = _row(path, "H")
        assert "H_H(A" in row
        assert "supportedin$S$" in row


def test_public_surfaces_use_the_chain_rescaling_identity():
    for path in CHAIN_SURFACES:
        compact = "".join(path.read_text().split())
        assert "d_Ah_A+h_Ad_A" in compact
        assert r"=\nu_A(" in compact
        assert r"\iota_Ap_A" in compact
        assert r"h_{A_b}=h_{\mathrm{LV}}" not in compact
