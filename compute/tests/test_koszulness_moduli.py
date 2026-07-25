"""Narrow guards for the quadratic Koszulness moduli carrier."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEX_PATH = ROOT / "chapters/theory/koszulness_moduli_scheme.tex"
TEX = TEX_PATH.read_text(encoding="utf-8")
COMPACT = re.sub(r"\s+", "", TEX)


def _window(label: str, size: int = 5000) -> str:
    marker = rf"\label{{{label}}}"
    start = TEX.index(marker)
    return TEX[start : start + size]


def _status(label: str) -> str:
    marker = rf"\label{{{label}}}"
    start = TEX.index(marker)
    neighbourhood = TEX[max(0, start - 300) : start + 800]
    match = re.search(r"\\ClaimStatus([A-Za-z]+)", neighbourhood)
    assert match is not None, f"missing claim status near {label}"
    return match.group(1)


def test_carrier_deforms_the_quadratic_twisting_datum() -> None:
    finite = _window("v1-def:kms-finite-window-test")
    moduli = _window("v1-def:kms-moduli-scheme")

    assert _status("v1-def:kms-finite-window-test") == "Definitional"
    assert _status("v1-def:kms-moduli-scheme") == "Definitional"
    assert r"\cA^{\mathrm i}=C(sV,s^2R)" in TEX
    assert r"\kappa_{\Phi,N,m}\colon F_{\le N}\cA^{\mathrm i}" in finite
    assert r"q_{\Phi,N,m}\colon F_{\le N}\cA^{\mathrm i}" in finite
    assert r"C^q_{\Phi,N,m}:=" in finite
    assert r"\operatorname{Cone}\bigl(\mathsf U(q_{\Phi,N,m})\bigr)" in finite

    expected_conv = re.sub(
        r"\s+",
        "",
        r"\mathrm{Conv}_\Phi\bigl(F_{\le N}\cA^{\mathrm i},"
        r"F_{\le N}\cA\bigr)",
    )
    assert expected_conv in re.sub(r"\s+", "", moduli)
    assert r"\xi\mapstoC^q_{\kappa_\cA+\xi}" in re.sub(r"\s+", "", moduli)


def test_universal_bar_cobar_counit_is_not_the_koszul_detector() -> None:
    a1 = _window("v1-item:kms-A1", 2600)

    assert r"\operatorname{Cone}(\varepsilon" not in TEX
    assert r"\operatorname{Cone}\bigl(\varepsilon" not in TEX
    assert r"\xi\mapsto\operatorname{Cone}(\varepsilon_\xi)" not in TEX
    assert r"\cA^{\mathrm{i}}=H^\bullet(\barBch(\cA))" not in TEX
    assert (
        r"\mathrm{Conv}_\Phi\bigl(F_{\leN}\barBch(\cA),"
        r"F_{\leN}\cA\bigr)"
    ) not in COMPACT

    assert r"q_{\cA,\Phi}\colon\widehat{\cA^{\mathrm i}}" in a1
    assert r"p_{\cA,\Phi}\colon\Omega^{\mathrm{ch}}_\Phi" in a1
    assert "universal reconstruction map" in a1


def test_representability_and_chart_equivalence_are_conditional() -> None:
    conditional_labels = {
        "v1-thm:kms-moduli",
        "v1-cor:kms-grt-invariant",
        "v1-thm:kms-fourteen-home-chart",
        "v1-prop:kms-at-chart",
        "v1-prop:kms-hodge-betti-chart",
        "v1-prop:kms-elliptic-chart",
        "v1-prop:kms-kontsevich-chart",
        "v1-thm:kms-koszulness-is-grt-invariant",
        "v1-thm:kms-virasoro-noncircular",
        "v1-thm:kms-yangian-embedding",
        "rem:kms-K3-placement",
        "rem:kms-grt-transport-312",
        "rem:kms-humbert-cocycle",
    }
    for label in conditional_labels:
        assert _status(label) == "Conditional", label

    assert r"\ClaimStatusProvedHere" not in TEX
    assert r"H_{\mathrm{mod}}" in _window("v1-thm:kms-moduli")
    assert r"H_{\mathrm{chart}}" in _window("v1-thm:kms-fourteen-home-chart")


def test_home_chart_theorem_compares_to_quadratic_cones() -> None:
    theorem = _window("v1-thm:kms-fourteen-home-chart", 9000)

    assert r"C^q_{\Phi_j,N,m}" in theorem
    assert r"\alpha_{j,N,m}" in theorem
    assert r"q_\cA\colon\widehat{\cA^{\mathrm i}}" in theorem
    assert r"p_\cA\colon\Omega^{\mathrm{ch}}" in theorem
    assert r"\Omega^{\mathrm{ch}}(\widehat{\barBch}(\cA))" not in theorem


def test_supplementary_charts_name_their_missing_comparison_maps() -> None:
    expected = {
        "v1-prop:kms-at-chart": r"\alpha^{\mathrm{AT}}_{N,m}",
        "v1-prop:kms-hodge-betti-chart": r"\alpha^{\mathrm{HB}}_N",
        "v1-prop:kms-elliptic-chart": r"\alpha^{\mathrm{ell}}_{N,m}",
        "v1-prop:kms-kontsevich-chart": r"\alpha^{\mathrm{Kon}}_{N,m}",
    }
    for label, comparison in expected.items():
        block = _window(label, 6500)
        assert comparison in block, label
        assert r"C^q_{\Phi" in block, label


def test_grt_transport_requires_an_equivariant_comparison_package() -> None:
    a3 = _window("v1-item:kms-A3", 2200)
    corollary = _window("v1-cor:kms-grt-invariant", 2600)
    theorem = _window("v1-thm:kms-koszulness-is-grt-invariant", 2400)

    for block in (a3, corollary, theorem):
        assert r"H_{\mathrm{GRT}}" in block
        assert r"C^q_" in block

    assert r"\gamma_{g,\Phi,N,m}" in a3
    assert "principal" in a3 and "precisely when" in a3


def test_acyclicity_open_has_the_ambient_mc_tangent_complex() -> None:
    a2 = _window("v1-item:kms-A2", 1800)

    assert r"\mathfrak g_{\Phi,N,m}" in a2
    assert r"^{\kappa_\cA+\xi}[1]" in a2
    assert "acyclicity condition is open" in a2
    assert r"\mathrm{RHom}(C_\xi,C_\xi)" not in TEX


def test_meta_koszulness_is_the_precise_open_operadic_problem() -> None:
    meta = _window("v1-thm:kms-meta-koszulness", 3800)

    assert _status("v1-thm:kms-meta-koszulness") == "Open"
    assert r"\begin{problem}[Meta-Koszulness]" in TEX
    assert r"C_*(E_2)\longrightarrow" in meta
    assert r"\operatorname{End}" in meta
    assert "remaining chain-level obligation" in meta
    assert "carries a natural\n$\\Etwo$-structure" not in TEX


def test_manuscript_surface_contains_no_control_character_corruption() -> None:
    forbidden = {
        character
        for character in TEX
        if ord(character) < 32 and character not in {"\n", "\r"}
    }
    assert forbidden == set()
