"""Structural guards for the stable genuine-partner Theorem C refinements."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/theorem_C_refinements_platonic.tex"


def source() -> str:
    return TARGET.read_text()


def environment_block(label: str, environment: str) -> str:
    text = source()
    label_at = text.index(rf"\label{{{label}}}")
    start = text.rindex(rf"\begin{{{environment}}}", 0, label_at)
    end = text.index(rf"\end{{{environment}}}", label_at)
    return re.sub(r"\s+", " ", text[start:end])


def section_block(label: str) -> str:
    text = source()
    label_at = text.index(rf"\label{{{label}}}")
    start = text.rfind(r"\section{", 0, label_at)
    next_section = text.find(r"\section{", label_at)
    return text[start : next_section if next_section >= 0 else len(text)]


def test_chapter_spine_uses_stable_genuine_partner_decomposition():
    text = source()
    opening = text[: text.index(r"\section{Scalar, Hochschild")]
    required = (
        r"2g-2+n>0",
        r"d_{g,n}=3g-3+n",
        r"\chi^-_{\cA;g,n}\colon",
        r"\mathbf Q^-_{g,n}(\cA)\xrightarrow{\;\simeq\;}",
        r"(\chi^-_{\cA;g,n})^{-1}\mathbf Q_{g,n}(\cA^!)",
        r"degree \(-d_{g,n}\)",
        r"\overline{\mathcal M}_{1,1}",
    )
    for fragment in required:
        assert fragment in opening

    assert r"Q_g(" not in text
    assert r"\mathbf{Q}_g" not in text


def test_five_surface_proposition_has_permanent_type_and_transport():
    block = environment_block("prop:theorem-C-surface-separation", "proposition")
    required = (
        "Type signature: Open quadrant",
        r"Beilinson levels~\(3\) and~\(5\)",
        r"\mathbf C_{g,n}(\cA)\simeq",
        r"(\chi^-_{\cA;g,n})^{-1}\mathbf Q_{g,n}(\cA^!)",
        r"cross-pairing of degree \(-d_{g,n}\)",
        r"\dim Q_{g,n}(\cA)=\dim Q_{g,n}(\cA^!)",
        r"\overline{\mathcal{M}}_{g,n}",
        r"\mathbf{C}_{g,n}(\cA)",
        r"Theorem~D bases \((1,1)\) and \((g,0)\)",
    )
    for fragment in required:
        assert fragment in block


def test_stable_genus_zero_keeps_coefficient_action_visible():
    block = section_block("sec:theorem-C-g0")
    required = (
        r"\ClaimStatusProvedHere",
        r"\label{prop:theorem-C-stable-genus-zero}",
        r"\overline{\mathcal M}_{0,3}\simeq\mathrm{pt}",
        r"d_{0,3}=0",
        r"(\chi^-_{\cA;0,3})^{-1}\mathbf Q_{0,3}(\cA^!)",
        "additional coefficient-involution hypothesis",
        r"\sigma_{\cA}=\mathrm{id}_{\mathbf C_{0,3}(\cA)}",
        r"\sigma_{\cA^!}=-\mathrm{id}_{\mathbf C_{0,3}(\cA^!)}",
        r"Q_{0,3}(\cA^!)=0",
        r"-d_{1,1}=-1",
    )
    for fragment in required:
        assert fragment in block

    hypothesis_at = block.index("additional coefficient-involution hypothesis")
    vanishing_at = block.index(r"Q_{0,3}(\cA^!)=0")
    assert hypothesis_at < vanishing_at


def test_ptvv_criterion_uses_stable_base_and_transported_partner():
    block = environment_block("thm:C-PTVV-alternative", "theorem")
    required = (
        "Type signature: Open quadrant",
        r"stable pair \((g,n)\)",
        r"Y_{g,n} \to \overline{\mathcal{M}}_{g,n}",
        r"\mathbb{C}[-d_{g,n}]",
        r"\mathbf{C}_{g,n}(\cA)^\vee[-d_{g,n}]",
        r"R\operatorname{Map}(Y_{g,n},S_\cA)",
        r"(\chi^-_{\cA;g,n})^{-1}\mathbf Q_{g,n}(\cA^!)",
        r"(-d_{g,n})\)-shifted Lagrangian",
    )
    for fragment in required:
        assert fragment in block

    assert r"Y_g" not in block
    assert r"\mathbf{C}_g" not in block


def test_every_load_bearing_environment_has_a_type_signature():
    claims = (
        ("prop:theorem-C-surface-separation", "proposition"),
        ("lem:naive-center-koszul-identification", "lemma"),
        ("conj:derived-center-koszul-equivalence", "conjecture"),
        ("prop:derived-center-morita-criterion", "proposition"),
        ("prop:perfectness-standard-landscape", "proposition"),
        ("conj:perfectness-boundary-km-generic", "conjecture"),
        ("conj:perfectness-boundary-class-M", "conjecture"),
        ("cor:c0-ordinary-class-G-L-locus", "corollary"),
        ("prop:theorem-C-stable-genus-zero", "proposition"),
        ("thm:C-PTVV-alternative", "theorem"),
    )
    for label, environment in claims:
        block = environment_block(label, environment)
        assert "Type signature:" in block, label
        assert "hypothesis package" in block, label


def test_active_prose_uses_affirmative_scope_language():
    text = re.sub(r"\s+", " ", source()).lower()
    retired = (
        " must not ",
        " does not ",
        " do not ",
        " cannot ",
        " without ",
        " lacks ",
        " missing ",
    )
    for phrase in retired:
        assert phrase not in f" {text} "
