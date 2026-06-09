import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

TARGET_FILES = (
    "chapters/examples/n2_superconformal.tex",
    "chapters/connections/concordance.tex",
    "chapters/frame/preface.tex",
    "chapters/theory/e1_modular_koszul.tex",
    "chapters/theory/higher_genus_complementarity.tex",
    "chapters/theory/higher_genus_foundations.tex",
    "chapters/theory/higher_genus_modular_koszul.tex",
    "compute/lib/csft_from_bar.py",
)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text()


def squashed(relative_path: str) -> str:
    return " ".join(read(relative_path).split())


def test_scalar_trace_and_full_coefficient_are_distinguished():
    required_by_file = {
        "chapters/examples/n2_superconformal.tex": (
            "F_g^{\\mathrm{sc}}(\\mathrm{SCA}_c) "
            "=\\kappa(\\mathrm{SCA}_c)\\lambda_g^{\\mathrm{FP}}",
            (
                "F_g(\\mathrm{SCA}_c) "
                "=F_g^{\\mathrm{sc}}(\\mathrm{SCA}_c) "
                "+\\delta F_g^{\\mathrm{cross}}(\\mathrm{SCA}_c)"
            ),
        ),
        "chapters/connections/concordance.tex": (
            "F_g=F_g^{\\mathrm{sc}}+\\delta F_g^{\\mathrm{cross}}",
            (
                "F_g(\\cA)=F_g^{\\mathrm{sc}}(\\cA) "
                "+ \\delta F_g^{\\mathrm{cross}}(\\cA)"
            ),
            "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
            (
                "F_g^{\\mathrm{BV}}(\\cH_\\kappa) "
                "= F_g^{\\mathrm{bar}}(\\cH_\\kappa) "
                "= F_g^{\\mathrm{sc}}(\\cH_\\kappa) "
                "= \\kappa(\\cH_\\kappa)\\lambda_g^{\\mathrm{FP}}"
            ),
        ),
        "chapters/frame/preface.tex": (
            (
                "F_g(\\cA)=F_g^{\\mathrm{sc}}(\\cA) "
                "+\\delta F_g^{\\mathrm{cross}}(\\cA)"
            ),
            "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
            (
                "F_g(\\beta\\gamma_\\lambda) "
                "=F_g^{\\mathrm{sc}}(\\beta\\gamma_\\lambda) "
                "=\\kappa(\\beta\\gamma_\\lambda)\\lambda_g^{\\mathrm{FP}}"
            ),
        ),
        "chapters/theory/e1_modular_koszul.tex": (
            "the scalar genus-$g$ free energies $F_g^{\\mathrm{sc}}(\\cA)$",
            "F_g=F_g^{\\mathrm{sc}}+\\delta F_g^{\\mathrm{cross}}",
        ),
        "chapters/theory/higher_genus_complementarity.tex": (
            "the full coefficient is the scalar trace plus the cross-channel summand",
        ),
        "chapters/theory/higher_genus_foundations.tex": (
            (
                "F_g(\\cA) \\;=\\; F_g^{\\mathrm{sc}}(\\cA) "
                "\\;+\\; \\delta F_g^{\\mathrm{cross}}(\\cA),"
            ),
            "F_g^{\\mathrm{sc}}(\\cA)= \\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
            (
                "F_g^{\\mathrm{sc}}(\\cA) \\;=\\; \\kappa(\\cA) \\cdot "
                "\\int_{\\overline{\\mathcal{M}}_{g,1}}"
            ),
            (
                "F_g(\\cA) = F_g^{\\mathrm{sc}}(\\cA) "
                "+ \\delta F_g^{\\mathrm{cross}}(\\cA)"
            ),
        ),
        "chapters/theory/higher_genus_modular_koszul.tex": (
            "F_g(\\cA)=F_g^{\\mathrm{sc}}(\\cA) +\\delta F_g^{\\mathrm{cross}}(\\cA)",
            "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
            "full coefficient has no cross-channel summand",
        ),
        "compute/lib/csft_from_bar.py": (
            "Genus-g scalar free-energy trace F_g^sc = kappa * lambda_g^FP.",
            "F_g = F_g^sc + delta_F_g^cross",
        ),
    }

    for relative_path, required_forms in required_by_file.items():
        body = squashed(relative_path)
        for required in required_forms:
            assert required in body


def test_retired_scalar_full_phrases_do_not_reappear():
    combined = "\n".join(read(path) for path in TARGET_FILES)

    retired_phrases = (
        "scalar formula " + "receives",
        "scalar formula " + "acquires",
        "scalar formula " + "fails and requires",
        "all-weight, with cross-channel " + "correction",
        "ALL-WEIGHT " + "+",
        "ALL-WEIGHT" + ";",
        "free energy " + "receives a cross-channel",
    )
    for phrase in retired_phrases:
        assert phrase not in combined


def test_bare_fp_formula_is_not_used_for_full_coefficient():
    combined = "\n".join(squashed(path) for path in TARGET_FILES)

    stale_forms = (
        "F_g(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
        "F_g = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "F_g(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}} +\\delta",
    )
    for stale in stale_forms:
        assert stale not in combined

    stale_regexes = (
        (
            r"F_g\(" + r"\\cA" + r"\)\s*(?:\\;)?=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(" + r"\\cA" + r"\)\s*=\s*\\kappa\s*\\cdot\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
    )
    for pattern in stale_regexes:
        assert re.search(pattern, combined) is None, pattern
