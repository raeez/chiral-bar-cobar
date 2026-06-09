import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/landscape_census.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_landscape_census_types_fp_trace_as_scalar_or_exact_lane():
    body = compact(read())

    required_forms = (
        r"F_1(\cA)=\kappa(\cA)/24",
        r"F_2^{\mathrm{scalar}}(\cA)=7\kappa(\cA)/5760",
        (
            r"F_g^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)",
        (
            r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
            r"+\deltaF_g^{\mathrm{cross}}(\cA)"
        ),
        (
            r"F_1(\cA)=F_1^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)/24"
        ),
        r"F_2^{\mathrm{sc}}/F_1^{\mathrm{sc}}=7/240",
        r"\operatorname{obs}_g(\cA)=\kappa(\cA)\cdot\lambda_g",
        r"\theta_1(\cA)=\kappa(\cA)\cdot\mu",
        (
            r"F_1(\mathcalW^k(\mathfrak{g}))"
            r"=\kappa(\mathcalW^k(\mathfrak{g}))/24"
        ),
        (
            r"\kappa(\mathcalW^k(\mathfrak{g}))"
            r"=c(\mathcalW^k(\mathfrak{g}))\cdot\varrho"
        ),
    )
    for required in required_forms:
        assert required in body


def test_landscape_census_has_no_bare_full_fp_coefficient():
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
        (
            r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"free energy\s*\$F_g\(" + r"\\cA" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
        ),
        r"scalar " + r"formula .*fails",
        r"F_2/F_1\s*=\s*7/240",
        (
            r"Scalar genus-\$g\$ coefficients \$F_g\("
            r"\\cA" + r"\)=\\kappa"
        ),
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern


def test_landscape_census_retired_untyped_phrases_do_not_reappear():
    text = read()

    retired_phrases = (
        "free energy\n$F_g(\\cA)=\\kappa(\\cA)",
        "free energy $F_g = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "F_g(\\cA)=\\kappa(\\cA) \\cdot \\lambda_g^{\\mathrm{FP}}$ is proved",
        (
            "F_g(\\cA)=\\kappa(\\cA) \\cdot \\lambda_g^{\\mathrm{FP}}\n"
            " + \\delta F_g^{\\mathrm{cross}}(\\cA)"
        ),
        "Theorem~\\ref{thm:multi-weight-genus-expansion}: the scalar formula",
        "fails at $g \\ge 2$",
        (
            "Scalar genus-$g$ coefficients $F_g(\\cA)=\\kappa(\\cA) "
            "\\cdot \\lambda_g^{\\mathrm{FP}}$"
        ),
        "For any uniform-weight algebra $\\cA$ with curvature parameter~$\\kappa$",
    )
    for phrase in retired_phrases:
        assert phrase not in text
