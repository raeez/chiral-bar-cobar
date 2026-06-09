import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/heisenberg_eisenstein.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_heisenberg_fp_trace_equals_full_coefficient_on_gaussian_lane():
    body = compact(read())

    required_forms = (
        (
            r"F_g(\cH_\kappa)=F_g^{\mathrm{sc}}(\cH_\kappa)"
            r"=\kappa(\cH_\kappa)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        r"\deltaF_g^{\mathrm{cross}}(\cH_\kappa)=0",
        (
            r"F_g(\cH_\kappa^!)=F_g^{\mathrm{sc}}(\cH_\kappa^!)"
            r"=\kappa(\cH_\kappa^!)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g(\mathcal{H}_\kappa)=F_g^{\mathrm{sc}}(\mathcal{H}_\kappa)"
            r"=\kappa(\mathcal{H}_\kappa)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g^{\mathrm{sc}}(\mathcalH_\kappa)"
            r"=\kappa(\mathcalH_\kappa)"
            r"\int_{\overline{\mathcalM}_{g,1}}\psi_1^{2g-2}\lambda_g"
        ),
        (
            r"\sum_{g\ge1}F_g(\mathcal{H}_\kappa)\,\hbar^{2g-2}"
            r"\;=\;\sum_{g\ge1}F_g^{\mathrm{sc}}(\mathcal{H}_\kappa)"
            r"\,\hbar^{2g-2}"
        ),
        (
            r"\pi_{\mathrm{cl}}(\delta_\Gamma(Z_g))"
            r"=F_g^{\mathrm{sc}}(\cH_\kappa)=F_g(\cH_\kappa)"
        ),
    )
    for required in required_forms:
        assert required in body


def test_heisenberg_chapter_has_no_bare_fp_full_coefficient():
    body = squashed(read())

    stale_regexes = (
        (
            r"F_g\(" + r"\\cH_\\kappa" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cH_\\kappa" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\mathcal\{H\}_\\kappa" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\mathcal\{H\}_\\kappa" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\mathcal H_\\kappa" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\mathcal H_\\kappa" + r"\)"
        ),
        (
            r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_2\(" + r"\\mathcal\{H\}_\\kappa" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\mathcal H_\\kappa" + r"\)"
        ),
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern


def test_heisenberg_retired_untyped_phrases_do_not_reappear():
    text = read()

    retired_phrases = (
        "GF $= (\\kappa/" + "\\hbar^2)",
        "F_g=" + "\\kappa\\lambda_g^{\\mathrm{FP}}",
        "F_g = " + "\\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "F_g(\\cH_\\kappa)=" + "\\kappa(\\cH_\\kappa)",
    )
    for phrase in retired_phrases:
        assert phrase not in text
