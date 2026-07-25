"""Semantic guards for the four outputs in the Koszul-existence appendix."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXISTENCE = ROOT / "chapters/theory/existence_criteria.tex"


def environment_block(label: str, environment: str) -> str:
    source = EXISTENCE.read_text(encoding="utf-8")
    anchor = source.index(rf"\label{{{label}}}")
    start = source.rfind(rf"\begin{{{environment}}}", 0, anchor)
    assert start >= 0, f"opening {environment!r} missing before {label!r}"
    closing = rf"\end{{{environment}}}"
    end = source.index(closing, anchor) + len(closing)
    return " ".join(source[start:end].split())


def require(block: str, *fragments: str) -> None:
    for fragment in fragments:
        assert fragment in block, f"{fragment!r} missing from scoped block"


def test_koszul_property_is_the_quadratic_comparison():
    block = environment_block("def:koszul-property-existence", "definition")
    require(
        block,
        r"\ClaimStatusDefinitional",
        r"q_{\mathcal A}\colon \mathcal A^i\longrightarrow\bar B(\mathcal A)",
        r"\Omega(\mathcal A^i)\longrightarrow\mathcal A",
        "Theorem~3.4.6",
        r"\epsilon_{\mathcal A}\colon \Omega\bar B(\mathcal A)\longrightarrow\mathcal A",
        "Corollary~2.3.4",
        "separate Ran/factorization comparison package",
    )
    assert r"\bar{B}(\mathcal{A}) \xrightarrow{\;\sim\;} \mathcal{A}^i" not in block


def test_pbw_theorem_separates_quadratic_resolution_and_duality():
    block = environment_block("thm:regular-implies-koszul", "theorem")
    require(
        block,
        r"\ClaimStatusConditional",
        r"\mathcal A^i_{\mathrm{quad}}=C(s^{-1}V,s^{-2}R)",
        r"\mathcal A^i_{\mathrm{quad}}\longrightarrow\bar B(\mathcal A)",
        r"\Omega(\mathcal A^i_{\mathrm{quad}})\to\mathcal A",
        r"\Omega\bar B(\mathcal A)\longrightarrow\mathcal A",
        r"(\mathcal A^i_{\mathrm{quad}})^\vee_{\mathrm{cont}}",
    )


def test_completed_theorem_runs_two_milnor_arguments():
    block = environment_block("thm:completed-koszul-dual", "theorem")
    require(
        block,
        r"\ClaimStatusConditional",
        r"q_n\colon\mathcal A_n^i\longrightarrow\bar B(\mathcal A_n)",
        r"\epsilon_n\colon\Omega\bar B(\mathcal A_n)\longrightarrow\mathcal A_n",
        r"\{H^j(\operatorname{Cone}(q_n))\}_n",
        r"\{H^j(\operatorname{Cone}(\epsilon_n))\}_n",
        r"\widehat q_{\mathcal A}\colon",
        r"\widehat\epsilon_{\mathcal A}\colon",
        r"\mathbb D_{\Ran}(\widehat{\mathcal A^i})",
    )
    assert r"\ClaimStatusProvedElsewhere" not in block


def test_classifier_and_correctness_proposition_have_four_independent_outputs():
    construction = environment_block(
        "con:koszul-dual-existence", "construction"
    )
    require(
        construction,
        "Type signature: Open quadrant",
        "E1: universal bar--cobar resolution",
        "E2: quadratic coalgebra and Koszul comparison",
        "E3: completed convergence",
        "E4: Verdier and chosen-pair comparison",
        r"q_{\mathcal A}\colon \mathcal A^i_{\mathrm{quad}}\longrightarrow\bar B(\mathcal A)",
        r"K_X(\mathcal A)=\mathbb D_{\Ran}\bar B_X(\mathcal A)",
        r"\mathbb D(q_{\mathcal A})\colon K_X(\mathcal A)\to",
        r"\nu_{\mathcal A}\colon K_X(\mathcal A)\to\mathcal A^!",
    )

    proposition = environment_block(
        "prop:existence-test-correctness", "proposition"
    )
    require(
        proposition,
        r"\ClaimStatusConditional",
        "Type signature: Open quadrant",
        "Corollary~2.3.4",
        r"\mathcal A^i_{\mathrm{quad}}=C(s^{-1}V,s^{-2}R)",
        r"\mathcal A^i_{\mathrm{quad}}\longrightarrow\bar B(\mathcal A)",
        r"conditions~\textup{(C1)--(C5)}",
        r"K_X(\mathcal A)",
        r"\mathbb D(q_{\mathcal A})",
        r"\nu_{\mathcal A}",
    )


def test_lv_coalgebra_convention_is_uniform_in_the_appendix():
    source = EXISTENCE.read_text(encoding="utf-8")
    assert r"C_{\mathcal D}(s^{-1}V,s^{-2}R)" in source
    assert r"C(s^{-1}V,s^{-2}R)" in source
    assert r"C_{\mathcal D}(sV,s^2R)" not in source
    assert r"C(sV,s^2R)" not in source
    assert r"T^c_{\mathcal D}(sV)" not in source
    assert r"\Lambda^c(sV)" not in source
    assert r"\text{Cofree}(sV^*)" not in source
    assert r"q_{\mathcal A}\colon\bar B(\mathcal A)" not in source
    assert "\t" + "o" not in source
