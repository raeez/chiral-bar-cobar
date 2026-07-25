from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

BAR_COBAR_CURVED = ROOT / "chapters/theory/bar_cobar_adjunction_curved.tex"
CHIRAL_KOSZUL_PAIRS = ROOT / "chapters/theory/chiral_koszul_pairs.tex"
THEOREM_A_INFINITY = ROOT / "chapters/theory/theorem_A_infinity_2.tex"
REFERENCES = ROOT / "standalone" / "references.bib"
FIRST_PRINCIPLES_CACHE = ROOT / "notes" / "first_principles_cache_comprehensive.md"


def read(path: Path) -> str:
    return path.read_text()


def squashed(path: Path) -> str:
    return " ".join(read(path).split())


def environment_block(path: Path, label: str, environment: str) -> str:
    text = read(path)
    anchor = text.index(rf"\label{{{label}}}")
    start = text.rfind(rf"\begin{{{environment}}}", 0, anchor)
    assert start >= 0, f"opening {environment!r} missing before {label!r}"
    closing = rf"\end{{{environment}}}"
    end = text.index(closing, anchor) + len(closing)
    return " ".join(text[start:end].split())


def assert_required(path: Path, fragments: tuple[str, ...]) -> None:
    text = squashed(path)
    for fragment in fragments:
        assert fragment in text, f"{fragment!r} missing from {path}"


def assert_forbidden(path: Path, fragments: tuple[str, ...]) -> None:
    text = squashed(path)
    for fragment in fragments:
        assert fragment not in text, f"retired fragment {fragment!r} still in {path}"


def test_theorem_a_ambient_is_conditional_not_gr17_iv5_model_theorem():
    assert_required(
        THEOREM_A_INFINITY,
        (
            "Conditional factorization ambient package",
            r"$H_{\Fact}(X)$ consists",
            r"Francis--Gaitsgory construct the chiral monoidal operation on $D(\Ran X)$",
            "Clauses (b)--(d) specify the model presentation used in this volume",
            r"properadic transfer adds the separate package $H_{\mathrm{prop}}$",
            "Conditional factorization-enriched properad transfer",
            r"Under $H_{\mathrm{prop}}$, factorization-enriched properads carry the transferred cofibrantly generated model structure",
        ),
    )
    assert_forbidden(
        THEOREM_A_INFINITY,
        (
            "Vallette's bar--cobar Quillen equivalence (\\cite[Theorem~2.1]{Val16}) applies to the Koszul-resolved chiral operad in the symmetric-monoidal ambient",
            "promotion to a symmetric-monoidal Quillen equivalence uses Hinich",
            r"\cite[Chapter~IV.5",
            "Theorem~3.1.2",
            "GR17 transfer",
            "GR17 model-categorical localisation",
        ),
    )


def test_bibliography_and_cache_do_not_reintroduce_gr17_iv5_model_route():
    assert_required(
        REFERENCES,
        (
            "not for a category-valued factorization Morita theorem",
            "not for a GR17 IV.5 factorization-sheaf model structure",
            "a numbered \\((\\infty,2)\\)-enhancement theorem",
        ),
    )
    assert_forbidden(
        REFERENCES,
        (
            "Chapter~IV.5 treats factorization sheaves",
            "\\((\\infty,2)\\)-enhancement of the Francis star-product",
        ),
    )

    assert_required(
        FIRST_PRINCIPLES_CACHE,
        (
            "Do not cite GR17 IV.5 for this unit",
            "Do not replace Val16 by a phantom GR17 IV.5 model theorem",
            "Use Val16 only on the \\(k\\)-linear pole-free operadic model",
            "conditional \\(H_{\\Fact}(X)\\) package plus Hackney--Robertson/Hinich machinery",
        ),
    )
    assert_forbidden(
        FIRST_PRINCIPLES_CACHE,
        (
            "GR17 IV.5 S2.2",
            "Cite GR17 Chapter IV.5 Theorem 3.1.2",
            "Francis-Gaitsgory-Rozenblyum model structure on factorization coalgebras",
        ),
    )


def test_bar_cobar_curved_uses_conditional_factorization_ambient_package():
    assert_required(
        BAR_COBAR_CURVED,
        (
            r"conditional factorization ambient package $H_{\Fact}(X)$",
            r"Proposition~\ref{prop:fg-ambient-properties}",
            "no published GR17 model theorem is used for this lift",
            "without that package this is only the chain-operadic rectification statement",
        ),
    )
    assert_forbidden(
        BAR_COBAR_CURVED,
        (
            r"\cite[Chapter~IV.5",
            "Theorem~3.1.2",
            "Francis--Gaitsgory--Rozenblyum model structure",
            "Francis--Gaitsgory--Rozenblyum factorization model structure",
        ),
    )


def test_curved_chapter_states_the_exact_francis_gaitsgory_scope():
    block = environment_block(
        BAR_COBAR_CURVED,
        "thm:fg-factorization-bar-cobar",
        "theorem",
    )
    required = (
        r"\ClaimStatusConditional",
        "Type signature: Open quadrant",
        "pro-nilpotent Francis--Gaitsgory ambient",
        r"$H_{\Fact}(X)$",
        r"$H_{\mathrm{fact}}$",
        r"H_{\mathrm{conv}}",
        r"$H_{\mathrm{fact}}^{R}$",
        r"$H_{\mathrm{VD}}$",
        "Proposition~4.1.2",
        "Theorem~5.1.1",
        "Theorem~5.2.1",
        r"\operatorname{Bar}^{\mathrm{enh}}_{\mathsf{Ass}}",
        r"\operatorname{CoAlg}^{\mathrm{dp}}_{\operatorname{Bar}(\mathsf{Ass})}",
        r"\varepsilon_{\mathcal F}\colon \Omegach_X\barBch_X(\mathcal F)",
        r"K_X(\mathcal F):=\mathbb D_{\Ran}\barBch_X(\mathcal F)",
    )
    for fragment in required:
        assert fragment in block, f"{fragment!r} missing from repaired FG theorem"

    retired = (
        "FG, Theorem 7.2.1",
        r"\textup{Fact}(X, \Omega(B(\mathcal{F})))",
        r"\ClaimStatusProvedElsewhere]\label{thm:fg-factorization-bar-cobar}",
    )
    for fragment in retired:
        assert fragment not in block, f"retired FG claim {fragment!r} survived"


def test_chiral_koszul_pairs_does_not_apply_lv_transfer_to_dmod_chiral_tensor():
    assert_required(
        CHIRAL_KOSZUL_PAIRS,
        (
            r"chosen factorization/Ran enhancement satisfying $H_{\Fact}(X)$",
            "not by itself an ordinary symmetric monoidal chiral tensor bifunctor",
            "Beilinson--Drinfeld chiral operations form a pseudo-tensor structure",
            r"Proposition~\ref{prop:fg-ambient-properties}",
            "Francis star-product isolated as the conditional package",
        ),
    )
    assert_forbidden(
        CHIRAL_KOSZUL_PAIRS,
        (
            r"\cite[Chapter~IV.5",
            r"$\mathcal{V} = \mathcal{D}\text{-mod}(X)$ equipped with the chiral tensor product",
            "as established in \\cite[Chapter~IV.5]{GR17}",
        ),
    )
