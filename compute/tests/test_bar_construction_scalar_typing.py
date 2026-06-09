import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/bar_construction.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_bar_construction_types_theorem_d_fp_term_as_scalar():
    body = compact(read())

    required_forms = (
        (
            r"F_g^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)",
        (
            r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
            r"+\deltaF_g^{\mathrm{cross}}(\cA)"
        ),
        r"\dfib^{\,2}=\kappa(\cA)\cdot\omega_g",
    )
    for required in required_forms:
        assert required in body


def test_bar_construction_has_no_bare_full_fp_coefficient():
    body = squashed(read())

    stale_regexes = (
        (
            r"F_g\(" + r"\\cA" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"genus expansion\s*\$F_g\(" + r"\\cA" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
        ),
        r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}",
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern


def test_bar_construction_retired_untyped_phrases_do_not_reappear():
    text = read()

    retired_phrases = (
        (
            "$F_g(\\cA) = \\kappa(\\cA)"
            "\\cdot\\lambda_g^{\\mathrm{FP}}$"
        ),
        "\\textup{(}UNIFORM-" + "WEIGHT\\textup{)}",
        "multi-weight extension at genus~$g \\geq 2$ receives",
    )
    for phrase in retired_phrases:
        assert phrase not in text
