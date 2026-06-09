import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/connections/frontier_modular_holography_platonic.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_frontier_types_additivity_and_origami_fp_terms_as_scalar():
    body = compact(read())

    required_forms = (
        r"F_g^{\mathrm{sc}}=\kappa\cdot\lambda_g^{\mathrm{FP}}",
        r"additivityof~$F_g^{\mathrm{sc}}$",
        r"Thescalarshadowgenusexpansion$F_g^{\mathrm{sc}}",
        r"reproducesthescalarvacuumsectoroftheNekrasovgenusexpansion",
    )
    for required in required_forms:
        assert required in body


def test_frontier_types_twisted_and_burns_fp_terms_as_scalar():
    body = compact(read())

    required_forms = (
        r"F_g^{\mathrm{sc}}=\kappa\cdot\lambda_g^{\mathrm{FP}}$ontheuniform-weightscalarlane",
        r"protectedscalartwisted$\mathcal{N}=4$amplitude",
        r"F_1^{\mathrm{sc}}(\cA_{\mathrm{Burns}})",
        r"F_2^{\mathrm{sc}}(\cA_{\mathrm{Burns}})",
        r"F_3^{\mathrm{sc}}(\cA_{\mathrm{Burns}})",
        r"doesnotaffectthescalargenusexpansion$F_g^{\mathrm{sc}}",
        r"controls$F_g^{\mathrm{sc}}$ontheuniform-weightscalarlane",
    )
    for required in required_forms:
        assert required in body


def test_frontier_has_no_bare_full_fp_free_energy_slogans():
    body = squashed(read())

    stale_regexes = (
        r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}",
        (
            r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}\s*at\s+the\s+scalar\s+level"
        ),
        r"F_g\s+on\s+the\s+uniform-weight\s+lane",
        r"shadow\s+genus\s+expansion\s+\$F_g\s*=",
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern
