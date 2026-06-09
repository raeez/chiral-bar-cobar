import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = "chapters/theory/higher_genus_modular_koszul.tex"


def read_squashed() -> str:
    return " ".join((ROOT / TARGET).read_text().split())


def test_higher_genus_modular_koszul_types_fp_scalar_source():
    squashed = read_squashed()

    required_forms = (
        "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
        (
            "F_g(\\cA)=F_g^{\\mathrm{sc}}(\\cA) "
            "+\\delta F_g^{\\mathrm{cross}}(\\cA)"
        ),
        "F_2(\\cW_3) = \\kappa(\\cW_3)\\lambda_2^{\\mathrm{FP}}",
        "F_g^{\\mathrm{UW}}(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
        (
            "F_g^{\\mathrm{sh}}(\\mathcal{A}) "
            "=\\kappa(\\mathcal{A})\\lambda_g^{\\mathrm{FP}}"
        ),
        "F^{\\mathrm{trop}}_g(\\cA)=F_g^{\\mathrm{sc}}(\\cA)",
    )
    for required in required_forms:
        assert required in squashed


def test_higher_genus_modular_koszul_has_no_bare_fp_free_energy_slogans():
    squashed = read_squashed()

    stale_patterns = (
        r"F_g\s*=\s*\\kappa\s*(?:\\cdot\s*)?\\lambda_g\^\{\\mathrm\{FP\}\}",
        r"F_g=\\kappa\\lambda_g\^\{\\mathrm\{FP\}\}",
        r"F_g\^\{\\mathrm\{UW\}\}\s*=\s*\\kappa\s*\\cdot\s*\\lambda_g",
        r"F_g\^\{\\mathrm\{sh\}\}\s*=\s*\\kappa\s*\\cdot\s*\\lambda_g",
        r"F\^\{\\mathrm\{trop\}\}_g\s*=\s*\\kappa\\cdot\\lambda_g",
        r"\\delta F_g / \\\(\\kappa \\cdot \\lambda_g\^\{\\mathrm\{FP\}\}\\\)",
        r"\\sum_g \\kappa\\,\\lambda_g\^\{\\mathrm\{FP\}\}",
        r"F_2\s*=\s*\\kappa\s*\\cdot\s*\\lambda_2\^\{\\mathrm\{FP\}\}",
        r"F_2\s*=\s*\\kappa\s*\\cdot\s*7/5760",
        r"F_3\s*=\s*\\kappa\\cdot\s*31/967680",
        r"\\sum_\{g \\geq 1\} F_g \\, x\^\{2g\} = \\kappa",
    )
    for pattern in stale_patterns:
        assert re.search(pattern, squashed) is None, pattern
