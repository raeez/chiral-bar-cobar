"""Regression guards for the KL/DK q-convention bridge.

The canonical convention is recorded in
appendices/q_convention_bridge_appendix.tex:

    q_KL = exp(pi i hbar_ref),  q_DK = exp(2 pi i hbar_ref),
    q_DK = q_KL^2,  hbar_ref = 1/(k + h^vee).

These tests guard theorem-facing and standalone summary surfaces against
the common error of naming the half-monodromy parameter q_DK.
"""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def _read(relpath: str) -> str:
    return (REPO_ROOT / relpath).read_text()


def test_canonical_q_bridge_has_half_and_full_keys():
    """The appendix must expose the KL half-key, DK full-key, and r-matrix
    normalization distinction in one place.
    """
    text = _read("appendices/q_convention_bridge_appendix.tex")

    assert r"q_{\KL} \;:=\; \exp(\pi i \hbar)" in text
    assert r"q_{\DK} \;:=\; \exp(2 \pi i \hbar)" in text
    assert r"$q_{\KL}^{2} = q_{\DK}$" in text
    assert "trace-form current-algebra residue" in text
    assert r"r_{\KZ}(z):=\Omega/((k+\hv)z)=\hbar\,\Omega/z" in text
    assert "KZ coupling" in text
    assert r"\hbar := 1/(k + \hv)" in text


def test_genus1_standalone_uses_kl_for_half_monodromy():
    """The genus-1 seven-face standalone may discuss DK, but it must not
    call exp(pi i/(k+h^vee)) the DK parameter.
    """
    text = _read("standalone/genus1_seven_faces.tex")

    forbidden = [
        r"q_{\mathrm{DK}}=\exp(\pi i\hbar)",
        r"q_{\mathrm{DK}}=\exp(\pi i/(k+h^\vee))",
        r"q_{\mathrm{DK}}=e^{\pi i/(k+2)}",
    ]
    for fragment in forbidden:
        assert fragment not in text

    assert r"q_{\mathrm{KL}}=\exp(\pi i\hbar_{\mathrm{ref}})" in text
    assert r"q_{\mathrm{DK}}=q_{\mathrm{KL}}^2" in text
    assert r"q_{\mathrm{KL}}=\exp(\pi i/(k+h^\vee))" in text
    assert r"q_{\mathrm{KL}}=e^{\pi i/(k+2)}" in text


def test_drinfeld_kohno_bridge_uses_reference_hbar_for_kl_parameter():
    """The Drinfeld--Kohno standalone must not reuse hbar for both the
    additive Yangian/KZ parameter and the KL exponent.
    """
    text = _read("standalone/drinfeld_kohno_bridge.tex")

    assert r"q_{\mathrm{KL}} = e^{\hbar}" not in text
    assert r"q_{\mathrm{KL}}=\exp(\pi i\hbar_{\mathrm{ref}})" in text
    assert r"\hbar_{\mathrm{ref}}=\kp^{-1}" in text
    assert r"q_{\mathrm{DK}}=q_{\mathrm{KL}}^2" in text


def test_yangian_overlap_zones_name_additive_hbar_parameter():
    """Where Yangian categories meet exponentiated quantum-loop
    parameters, the additive parameter is named hbar_Y.
    """
    checked = [
        "standalone/drinfeld_kohno_bridge.tex",
        "chapters/examples/yangians_drinfeld_kohno.tex",
    ]
    forbidden = [
        r"\hbar = \pi i/(\kp)",
        r"\hbar = \frac{\pi i}{\kp}",
        r"q_Y = e^\hbar",
        r"q_Y = e^{\hbar}",
    ]
    for relpath in checked:
        text = _read(relpath)
        for fragment in forbidden:
            assert fragment not in text, f"{fragment!r} still in {relpath}"

        assert r"\hbar_Y" in text
        assert r"q_Y = \exp(\hbar_Y)" in text
