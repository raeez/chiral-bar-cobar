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


def test_entanglement_jt_comparison_is_contour_scoped():
    source = read()
    block_start = source.index(r"\section{JT gravity as a conditional Schwarzian comparison}")
    block_end = source.index(r"\section{Entanglement and Koszul conductor", block_start)
    block = source[block_start:block_end]
    flat = squashed(block)

    required = (
        "Conditional JT comparison from the shadow obstruction tower",
        r"x=z^2",
        r"y_{\mathrm{WP}}(z)=\frac{\sin(2\pi z)}{4\pi}",
        r"\rho_0(E)=\frac{1}{i\pi}y_{\mathrm{WP}}(i\sqrt E)",
        r"\frac{\sinh(2\pi\sqrt E)}{4\pi^2}",
    )
    for needle in required:
        assert needle in block

    required_flat = (
        "not a theorem of the scalar shadow tower",
        "not obtained from the scalar shadow obstruction tower alone",
        "does not reconstruct the full JT",
        "non-perturbative completion",
        "requires the external topological recursion",
    )
    for needle in required_flat:
        assert needle in flat

    stale = (
        "degenerates to the JT gravity genus expansion",
        "whose topological recursion reproduces the JT amplitudes",
        "obtained from the shadow obstruction tower in the",
        "density of states in the Schwarzian quantum mechanics",
    )
    for needle in stale:
        assert needle not in flat
