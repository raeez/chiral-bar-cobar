import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/genus_expansions.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_genus_expansions_types_fp_trace_as_scalar_or_diagonal():
    body = compact(read())

    required_forms = (
        (
            r"F_g^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
            r"+\deltaF_g^{\mathrm{cross}}(\cA)"
        ),
        (
            r"F_g^{\mathrm{sc}}(\mathcal{A})"
            r"=\kappa(\mathcal{A})\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"\sum_{g=1}^{\infty}F_g^{\mathrm{sc}}(\mathcal{A})\,x^{2g}"
            r"\;=\;\kappa\left(\frac{x/2}{\sin(x/2)}-1\right)"
        ),
        (
            r"F_g^{\mathrm{sc}}(\hat{\fg}_k)"
            r"=\kappa(\hat{\fg}_k)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_1(\hat{\fg}_k)=F_1^{\mathrm{sc}}(\hat{\fg}_k)"
            r"=\kappa(\hat{\fg}_k)/24"
        ),
        (
            r"F_g^{\mathrm{diag}}(\mathcal{W}_3^k)"
            r"=\kappa(\mathcal{W}_3^k)\lambda_g^{\mathrm{FP}}"
        ),
    )
    for required in required_forms:
        assert required in body


def test_genus_expansions_has_no_bare_full_fp_coefficient():
    text = read()
    body = squashed(text)

    stale_regexes = (
        (
            r"F_g\(" + r"\\cA" + r"\)\s*(?:\\;)?=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\mathcal\{A\}" + r"\)\s*(?:\\;)?=\s*"
            r"\\kappa\(" + r"\\mathcal\{A\}" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\hat\{\\fg\}_k" + r"\)\s*(?:\\;)?=\s*"
            r"\\kappa\(" + r"\\hat\{\\fg\}_k" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\s*=\s*\(c_\{p,q\}/2\)\s*\\cdot\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern


def test_genus_expansions_retired_scalar_full_phrases_do_not_reappear():
    text = read()

    retired_phrases = (
        "scalar formula " + "receives a cross-channel",
        "scalar formula " + "fails at",
        "free energy " + "receives a cross-channel",
        "F_g = " + "\\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
    )
    for phrase in retired_phrases:
        assert phrase not in text
