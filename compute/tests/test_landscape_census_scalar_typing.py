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


def between(text: str, start: str, end: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index)
    return text[start_index:end_index]


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
        (
            r"\operatorname{obs}^{\mathrm{sc}}_1(\cA)"
            r"=\kappa_{\mathrm{mod}}(\cA)\lambda_1"
        ),
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


def test_principal_wn_modular_conductor_carries_both_hypotheses():
    text = read()
    wn_package = (
        r"H_{\mathrm{diag}}^{g=1}+H_{W_N}^{\mathrm{DS/bar}}"
    )
    w3_package = (
        r"H_{\mathrm{diag}}^{g=1}+H_{W_3}^{\mathrm{DS/bar}}"
    )

    blocks = (
        (
            between(
                text,
                r"For the principal family, write",
                r"{\scriptsize",
            ),
            wn_package,
        ),
        (
            between(
                text,
                r"Principal \(\mathcal W_N\) &",
                r"Critical affine \(V_{-h^\vee}(\fg)\) &",
            ),
            wn_package,
        ),
        (
            between(
                text,
                r"\begin{remark}[Standard-family constants",
                r"\begin{table}[ht]",
            ),
            wn_package,
        ),
        (
            between(
                text,
                r"\label{cor:anomaly-ratio-ds}",
                r"\begin{corollary}[Genus-",
            ),
            wn_package,
        ),
        (
            between(
                text,
                r"\label{thm:census-witness-complementarity}",
                r"\begin{proposition}[Archetype-by-archetype",
            ),
            w3_package,
        ),
        (
            between(
                text,
                r"\label{prop:archetype-complementarity-bridge}",
                r"\begin{proposition}[Mukai lattice arithmetic",
            ),
            w3_package,
        ),
        (
            between(
                text,
                r"\label{thm:census-self-dual-locus}",
                r"\begin{remark}[Three-path computation of",
            ),
            w3_package,
        ),
        (
            between(
                text,
                r"\label{rem:koszul-conductor-explicit}",
                r"\begin{proposition}[Fateev--Lukyanov",
            ),
            wn_package,
        ),
    )

    for block, package in blocks:
        assert package in block


def test_principal_w3_separates_exact_central_and_conditional_modular_data():
    text = read()
    compact_text = compact(text)

    assert r"K_3^c=100" in compact_text
    assert "exact central conductor is $K_3^c=100$" in text
    assert "conditional modular conductor is" in text
    assert r"K_3^{\kappa_{\mathrm{mod}}}=250/3" in compact_text
    assert r"\{0,\,13\}" in text
    assert "unconditional scalar Verdier values" in text
    assert r"\{0,\,13,\,250/3\}" in text
    assert "conditional value $250/3$" in text
