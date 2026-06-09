import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/connections/arithmetic_shadows.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_arithmetic_shadows_types_lattice_and_bernoulli_fp_terms_as_scalar():
    body = compact(read())

    required_forms = (
        (
            r"F_g^{\mathrm{sc}}(V_\Lambda)"
            r"=r\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"F_g^{\mathrm{sc}}(\cA)"
            r"=\kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}"
        ),
        (
            r"\lambda_g^{\mathrm{FP}}="
            r"\tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot"
            r"\lvertB_{2g}\rvert/(2g)!"
        ),
    )
    for required in required_forms:
        assert required in body


def test_arithmetic_shadows_distinguishes_genus_scalar_projection_from_shadow_degree():
    text = read()

    assert (
        "Note: $F_g^{\\mathrm{sc}}$ is the \\emph{genus}-$g$ scalar\n"
        "projection of the shadow obstruction tower, not the\n"
        "\\emph{degree}-$r$ shadow coefficient~$S_r$."
    ) in text


def test_arithmetic_shadows_has_no_bare_full_fp_coefficient_or_old_marker():
    body = squashed(read())

    stale_regexes = (
        (
            r"F_g\(" + r"\\cA" + r"\)\s*=\s*"
            r"\\kappa\(" + r"\\cA" + r"\)"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        (
            r"F_g\(V_" + r"\\Lambda" + r"\)\s*=\s*r"
            r"(?:\s*\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}",
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern

    retired_phrases = (
        "UNIFORM-WEIGHT",
        "F_g^{\\mathrm{scal}}",
        "Note: $F_g$ is the \\emph{genus}",
    )
    text = read()
    for phrase in retired_phrases:
        assert phrase not in text
