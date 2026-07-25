"""Guards for the Delta_5 versus Saito--Kurokawa square distinction."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HOCHSCHILD = ROOT / "chapters/theory/hochschild_cohomology.tex"
APPENDIX_CACHE = ROOT / "appendices/first_principles_cache.md"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_delta5_is_borcherds_denominator_not_sk_source():
    text = _text(HOCHSCHILD)
    required = [
        "Borcherds denominator and Saito--Kurokawa square",
        r"$\Delta_5$ is the Borcherds--Gritsenko denominator with character",
        "it is not a standard Saito--Kurokawa lift with elliptic source",
        r"\Delta_{10}=\Delta_5^2=\mathrm{SK}(f_{18})",
        r"f_{18}=E_6\Delta\in S_{18}(\mathrm{SL}_2(\mathbb Z))",
        "not to $\\Delta_5$ itself",
        "not a third central-\\(L\\)-value evaluation of the $\\Delta_5$ period",
    ]
    for fragment in required:
        assert fragment in text


def test_retired_sk_delta5_period_route_is_absent():
    forbidden = [
        r"L(1/2,\mathrm{SK}(\Delta_5))",
        r"L(s,\mathrm{SK}(\Delta_5))",
        r"Saito--Kurokawa lift~$\mathrm{SK}(\Delta_5)$",
        "evaluates this central $L$-value",
    ]
    for path in (HOCHSCHILD, APPENDIX_CACHE):
        text = _text(path)
        for fragment in forbidden:
            assert fragment not in text, f"{fragment!r} remains in {path}"


def test_appendix_cache_uses_square_packet_language():
    text = _text(APPENDIX_CACHE)
    required = [
        r"squared Saito--Kurokawa packet $\Delta_{10}=\Delta_5^2=\mathrm{SK}(f_{18})$",
        r"$f_{18}=E_6\Delta$",
        r"not a central-$L$ evaluation for a Saito--Kurokawa lift of $\Delta_5$",
        "Klingen's orthogonal decomposition",
    ]
    for fragment in required:
        assert fragment in text


def test_harvest_matrix_records_arithmetic_local_pass():
    text = _text(MATRIX)
    assert "L Arithmetic and modular forms" in text
    assert "Pass 514" in text
