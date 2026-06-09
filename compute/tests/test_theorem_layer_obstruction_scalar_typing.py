from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


TARGET_FILES = (
    "chapters/theory/introduction.tex",
    "chapters/frame/part_ii_platonic_introduction.tex",
    "chapters/theory/higher_genus_foundations.tex",
    "chapters/theory/higher_genus_modular_koszul.tex",
    "chapters/theory/higher_genus_complementarity.tex",
    "chapters/connections/thqg_introduction_supplement_body.tex",
)


def read_squashed(relative_path: str) -> str:
    return " ".join((ROOT / relative_path).read_text().split())


def test_theorem_layer_obstruction_formulas_use_typed_characteristic():
    required_by_file = {
        "chapters/theory/introduction.tex": (
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
            "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
            "\\kappa(\\cA)+\\kappa(\\cA^!)=0",
        ),
        "chapters/frame/part_ii_platonic_introduction.tex": (
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
        ),
        "chapters/theory/higher_genus_foundations.tex": (
            "\\mathrm{obs}_1(\\mathcal H_\\kappa) =\\kappa(\\mathcal H_\\kappa)\\lambda_1",
            "\\mathrm{obs}_g(V_k(\\fg)) =\\kappa(V_k(\\fg))\\lambda_g",
            "\\mathrm{obs}_1(\\mathcal W_3^k) =\\kappa(\\mathcal W_3^k)\\lambda_1",
            "\\mathrm{obs}_1(\\cA)=\\kappa(\\cA)\\lambda_1",
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
        ),
        "chapters/theory/higher_genus_modular_koszul.tex": (
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
            "\\mathrm{obs}_1(\\cA)=\\kappa(\\cA)\\lambda_1",
        ),
        "chapters/theory/higher_genus_complementarity.tex": (
            "\\mathrm{obs}_g(V_k(\\mathfrak g)) =\\kappa(V_k(\\mathfrak g))\\lambda_g",
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
        ),
        "chapters/connections/thqg_introduction_supplement_body.tex": (
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
        ),
    }

    for relative_path, required_forms in required_by_file.items():
        squashed = read_squashed(relative_path)
        for required in required_forms:
            assert required in squashed


def test_theorem_layer_obstruction_formulas_have_no_bare_kappa_slogans():
    combined = "\n".join((ROOT / path).read_text() for path in TARGET_FILES)

    stale_forms = (
        "\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g",
        "\\mathrm{obs}_g=\\kappa\\cdot\\lambda_g",
        "\\mathrm{obs}_g=\\kappa\\lambda_g",
        "\\mathrm{obs}_1 = \\kappa \\cdot \\lambda_1",
        "\\mathrm{obs}_1=\\kappa\\lambda_1",
        "$\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g$",
        "$\\mathrm{obs}_g=\\kappa\\lambda_g$",
    )
    for stale in stale_forms:
        assert stale not in combined
