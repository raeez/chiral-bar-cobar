import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/free_fields.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_free_fermion_fp_trace_equals_full_coefficient_on_class_g_lane():
    body = compact(read())

    required_forms = (
        (
            r"F_g(\mathcal{F})=F_g^{\mathrm{sc}}(\mathcal{F})"
            r"=\kappa(\mathcal{F})\cdot\lambda_g^{\mathrm{FP}}"
        ),
        r"\deltaF_g^{\mathrm{cross}}(\mathcalF)=0",
        (
            r"\sum_{g=1}^{\infty}F_g(\mathcal{F})\,x^{2g}"
            r"=\sum_{g=1}^{\infty}F_g^{\mathrm{sc}}(\mathcal{F})\,x^{2g}"
        ),
        (
            r"F_g(\cF)=F_g^{\mathrm{sc}}(\cF)"
            r"=\kappa(\cF)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g(\cF)=F_g^{\mathrm{sc}}(\cF)"
            r"=\frac{1}{4}\cdot"
        ),
        (
            r"\sum_{g=1}^\inftyF_g(\cF)\,\hbar^{2g}"
            r"=\sum_{g=1}^\inftyF_g^{\mathrm{sc}}(\cF)\,\hbar^{2g}"
        ),
        (
            r"F_1(\mathcalF)=F_1^{\mathrm{sc}}(\mathcalF)"
            r"=\kappa(\mathcalF)(1/24)=1/96"
        ),
    )
    for required in required_forms:
        assert required in body


def test_free_field_chapter_has_no_bare_fp_full_coefficient():
    body = squashed(read())

    stale_regexes = (
        (
            r"F_g\(" + r"\\mathcal\{F\}" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\mathcal\{F\}" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\cF" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cF" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\cA" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}",
        r"F_g\(" + r"\\cF" + r"\)\s*=\s*\\frac\{1\}\{4\}",
        r"F_g\(" + r"\\mathcal\{F\}" + r"\)\s*=\s*\\frac\{1\}\{4\}",
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern


def test_free_field_retired_untyped_phrases_do_not_reappear():
    text = read()

    retired_phrases = (
        "F_g = " + "\\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "F_g(" + "\\cF)=" + "\\kappa(\\cF)",
        "F_g(" + "\\mathcal{F}) = \\kappa(\\mathcal{F})",
        "free energy\n$F_g(" + "\\cF)=\\kappa(\\cF)",
        (
            "features of the partition function $Z_g$, not of the\n"
            "free energy\n$F_g(" + "\\cF)=\\kappa(\\cF)"
        ),
    )
    for phrase in retired_phrases:
        assert phrase not in text
