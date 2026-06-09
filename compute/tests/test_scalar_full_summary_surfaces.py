import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

TARGET_FILES = (
    "chapters/frame/guide_to_main_results.tex",
    "chapters/connections/outlook.tex",
    "chapters/connections/master_concordance.tex",
    "chapters/connections/feynman_diagrams.tex",
    "chapters/connections/genus_complete.tex",
)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text()


def squashed(relative_path: str) -> str:
    return " ".join(read(relative_path).split())


def compact(relative_path: str) -> str:
    return re.sub(r"\s+", "", read(relative_path))


def test_summary_surfaces_distinguish_scalar_trace_from_full_coefficient():
    required_compact_forms = {
        "chapters/frame/guide_to_main_results.tex": (
            (
                r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
                r"+\deltaF_g^{\mathrm{cross}}(\cA)"
            ),
            r"F_g^{\mathrm{sc}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
        ),
        "chapters/connections/outlook.tex": (
            (
                r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
                r"+\deltaF_g^{\mathrm{cross}}(\cA)"
            ),
            r"F_g^{\mathrm{sc}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
            r"F_g^{\mathrm{diag}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
        ),
        "chapters/connections/master_concordance.tex": (
            (
                r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
                r"+\deltaF_g^{\mathrm{cross}}(\cA)"
            ),
            r"F_g^{\mathrm{sc}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
        ),
        "chapters/connections/feynman_diagrams.tex": (
            (
                r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
                r"+\deltaF_g^{\mathrm{cross}}(\cA)"
            ),
            r"F_g^{\mathrm{sc}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
        ),
        "chapters/connections/genus_complete.tex": (
            (
                r"F_g(\cA)=F_g^{\mathrm{diag}}(\cA)"
                r"+\deltaF_g^{\mathrm{cross}}(\cA)"
            ),
            r"F_g^{\mathrm{diag}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
        ),
    }

    for relative_path, required_forms in required_compact_forms.items():
        body = compact(relative_path)
        for required in required_forms:
            assert required in body


def test_summary_surfaces_have_no_retired_scalar_full_phrasing():
    combined = "\n".join(read(path) for path in TARGET_FILES)

    retired_phrases = (
        "ALL-WEIGHT " + "+",
        "ALL-WEIGHT" + ";",
        "free energy " + "receives a cross-channel",
        "scalar formula " + "receives",
        "all-weight, with cross-channel " + "correction",
    )
    for phrase in retired_phrases:
        assert phrase not in combined


def test_summary_surfaces_do_not_identify_full_coefficient_with_scalar_trace():
    combined_squashed = "\n".join(squashed(path) for path in TARGET_FILES)

    stale_literal_forms = (
        (
            "F_g(" + "\\cA" + ")=" + "\\kappa("
            + "\\cA" + ")" + "\\lambda_g^{\\mathrm{FP}}"
        ),
        (
            "F_g(" + "\\cA" + ")=" + "\\kappa("
            + "\\cA" + ")" + "\\cdot" + "\\lambda_g^{\\mathrm{FP}}"
        ),
        "F_g=" + "\\kappa" + "\\cdot" + "\\lambda_g^{\\mathrm{FP}}",
    )
    combined_compact = re.sub(r"\s+", "", combined_squashed)
    for stale in stale_literal_forms:
        assert stale not in combined_compact

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
    )
    for pattern in stale_regexes:
        assert re.search(pattern, combined_squashed) is None, pattern
