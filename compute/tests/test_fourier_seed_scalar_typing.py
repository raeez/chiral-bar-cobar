import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/fourier_seed.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_fourier_seed_characteristic_function_types_scalar_and_full_coefficients():
    body = compact(read())

    required_forms = (
        r"\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g",
        (
            r"F_g^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
            r"+\deltaF_g^{\mathrm{cross}}(\cA)"
        ),
        r"\deltaF_1^{\mathrm{cross}}=0",
        r"scalar-lanegeneratingfunction",
    )
    for required in required_forms:
        assert required in body


def test_fourier_seed_has_no_bare_full_fp_coefficient():
    body = squashed(read())

    stale_regexes = (
        (
            r"F_g\(" + r"\\cA" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\cA" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
            r"\s*\+\s*\\delta\s*F_g\^\{\\mathrm\{cross\}\}\("
            r"\\cA" + r"\)"
        ),
        r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}",
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern


def test_fourier_seed_retired_untyped_phrases_do_not_reappear():
    text = read()

    retired_phrases = (
        "At the all-weight numerical level,\n$F_g(\\cA)=\\kappa(\\cA)",
        "F_g(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
        "F_g(\\cA)=\\kappa(\\cA)\\cdot\\lambda_g^{\\mathrm{FP}}",
    )
    for phrase in retired_phrases:
        assert phrase not in text
