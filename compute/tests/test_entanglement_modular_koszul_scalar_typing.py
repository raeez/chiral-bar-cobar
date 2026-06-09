import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/connections/entanglement_modular_koszul.tex"


def read() -> str:
    return TARGET.read_text()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def squashed(text: str) -> str:
    return " ".join(text.split())


def test_entanglement_btz_and_jt_type_fp_terms_as_scalar():
    body = compact(read())

    required_forms = (
        r"F_g^{\mathrm{sc}}=\kappa\cdot\lambda_g^{\mathrm{FP}}",
        r"F_g=F_g^{\mathrm{sc}}+\deltaF_g^{\mathrm{cross}}",
        r"scalarclosed-sectorinputs",
        r"uniform-weightscalarlane",
    )
    for required in required_forms:
        assert required in body


def test_entanglement_retains_class_m_cross_channel_warning():
    body = compact(read())

    required_forms = (
        r"ForVirasoro(class~M),theplanted-forestcorrections",
        r"contributeadditionaltermsbeyondthescalarlevel",
        r"ateverygenus$g\ge2$",
    )
    for required in required_forms:
        assert required in body


def test_entanglement_has_no_bare_full_fp_free_energy():
    body = squashed(read())

    stale_regexes = (
        r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}",
        (
            r"F_g\s*=\s*\\kappa\s*(?:\\cdot)?\s*"
            r"\\lambda_g\^\{\\mathrm\{FP\}\}\s*at\s+the\s+scalar\s+level"
        ),
        (
            r"shadow\s+free\s+energy\s+\$F_g\s*=\s*"
            r"\\kappa\s*(?:\\cdot)?\s*\\lambda_g\^\{\\mathrm\{FP\}\}"
        ),
        r"uniform-weight\s+lane",
    )
    for pattern in stale_regexes:
        assert re.search(pattern, body) is None, pattern
