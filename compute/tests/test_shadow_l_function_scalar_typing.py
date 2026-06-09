import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/shadow_L_function_platonic.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_shadow_l_function_genus_slot_types_fp_term_as_scalar():
    body = compact(read())

    required_forms = (
        (
            r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
            r"+\deltaF_g^{\mathrm{cross}}(\cA)"
        ),
        r"\Coeff_{r=2g-2}",
        r"\Pi_g^{\mathrm{sh}}\Lsh(\cA)",
    )
    for required in required_forms:
        assert required in body


def test_shadow_l_function_has_no_bare_full_fp_coefficient():
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


def test_shadow_l_function_retired_untyped_phrases_do_not_reappear():
    text = read()

    retired_phrases = (
        "F_g(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}.",
        "the scalar " + "formula is replaced by",
        (
            "F_g(\\cA)\n =\n \\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}"
        ),
    )
    for phrase in retired_phrases:
        assert phrase not in text
