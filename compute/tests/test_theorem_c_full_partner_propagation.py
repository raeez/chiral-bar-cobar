"""Structural guards for full genuine-partner propagation in Theorem C."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_complementarity.tex"


def source() -> str:
    return SOURCE.read_text()


def environment(label: str, kind: str) -> str:
    text = source()
    label_at = text.index(rf"\label{{{label}}}")
    start = text.rindex(rf"\begin{{{kind}}}", 0, label_at)
    end = text.index(rf"\end{{{kind}}}", label_at)
    return text[start:end]


def test_legacy_one_index_theorem_c_symbols_are_absent() -> None:
    text = source()
    for legacy in (r"Q_g(", r"\mathbf{Q}_g", r"\mathbf Q_g", r"Q_1("):
        assert legacy not in text

    assert text.count("d_g") == 1
    assert r"d_g:=d_{g,n_g}" in text


def test_self_dual_halving_uses_stable_partner_transport() -> None:
    block = environment("thm:self-dual-halving", "theorem")
    for required in (
        "Type signature: Open quadrant",
        r"stable pair",
        r"\mathbf C_{g,n}(\cA)",
        r"\dim Q_{g,n}(\cA) \;=\; \dim Q_{g,n}(\cA^!)",
        r"H^*(\mathbf C_{g,n}(\cA))",
    ):
        assert required in block

    proof_start = source().index(r"\begin{proof}", source().index(block))
    proof_end = source().index(r"\end{proof}", proof_start)
    proof = source()[proof_start:proof_end]
    assert r"(H^*\chi^-_{\cA;g,n})^{-1}Q_{g,n}(\cA^!)" in proof


def test_quotient_reconstructs_partner_before_verdier_dualizing() -> None:
    block = environment("cor:uniqueness-quantum", "corollary")
    assert (
        r"(H^*\chi^-_{\mathcal A;g,n_g})^{-1}Q_{g,n_g}(\mathcal A^!)"
        in block
    )
    assert r"/Q_{g,n_g}(\mathcal A)" in block
    assert r"Q_{g,n_g}(\mathcal A^!)^\vee[-d_{g,n_g}]" in block
    assert r"/Q_{g,n_g}(\mathcal A)\right)^\vee" not in block


def test_protected_cofiber_is_the_transported_partner() -> None:
    block = environment("thm:holo-comp-bulk-reconstruction", "theorem")
    for required in (
        "Type signature: Open quadrant",
        r"stable pair \((g,n)\)",
        r"\mathbf{H}^{\mathrm{hol}}_{g,n}(\cA)",
        r"(\chi^-_{\cA;g,n})^{-1}\mathbf{Q}_{g,n}(\cA^!)",
    ):
        assert required in block


def test_cotangent_and_spectral_lanes_use_unpointed_stable_shift() -> None:
    cotangent = environment("thm:holo-comp-cotangent-realization", "theorem")
    spectral = environment("cor:holo-comp-spectral-reciprocity", "corollary")

    assert r"-d_{g,0}" in cotangent
    assert r"\mathbf{C}_{g,0}(\cA)" in cotangent
    assert "balanced protected" in cotangent

    assert r"\ClaimStatusConditional" in spectral
    assert r"u^{d_{g,0}}" in spectral
    assert r"\mathbf Q_{g,0}(\cA^!)" in spectral
    assert "balanced protected" in spectral


def test_ptvv_lane_places_only_the_transport_in_the_primal_ambient() -> None:
    block = environment("prop:ptvv-lagrangian", "proposition")
    for required in (
        "Type signature: Open quadrant",
        r"C_{g,0}",
        r"-d_{g,0}",
        r"(\chi^-_{\cA;g,0})^{-1}\mathbf{Q}_{g,0}(\cA^!)",
    ):
        assert required in block
