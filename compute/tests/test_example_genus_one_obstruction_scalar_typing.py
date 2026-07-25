from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

TARGET_FILES = (
    "chapters/examples/w_algebras_deep.tex",
    "chapters/examples/y_algebras.tex",
    "chapters/examples/w3_holographic_datum.tex",
    "chapters/examples/n2_superconformal.tex",
)


def read_squashed(relative_path: str) -> str:
    return " ".join((ROOT / relative_path).read_text().split())


def test_active_examples_type_genus_one_obstruction_source():
    required_by_file = {
        "chapters/examples/w_algebras_deep.tex": (
            "\\operatorname{tr}_1 "
            "\\operatorname{Obs}^{\\mathrm{def}}_{1,1}(\\mathcal W_N^k) "
            "=\\kappa(\\mathcal W_N^k)\\lambda_1",
        ),
        "chapters/examples/y_algebras.tex": (
            "\\operatorname{tr}_1\\operatorname{Obs}^{\\mathrm{def}}_{1,1}"
            "(Y_{1,1,1}[\\Psi]) "
            "=\\kappa(Y_{1,1,1}[\\Psi])\\lambda_1 =\\Psi\\lambda_1",
        ),
        "chapters/examples/w3_holographic_datum.tex": (
            "\\operatorname{tr}_1 "
            "\\operatorname{Obs}^{\\mathrm{def}}_{1,1}(\\mathcal W_3^k) "
            "=\\kappa_{\\mathrm{ch}}(\\mathcal W_3^k)\\lambda_1",
        ),
        "chapters/examples/n2_superconformal.tex": (
            "\\operatorname{tr}_1 "
            "\\operatorname{Obs}^{\\mathrm{def}}_{1,1} "
            "\\bigl(V_c^{\\mathcal N=2}\\bigr) "
            "=\\kappa\\bigl(V_c^{\\mathcal N=2}\\bigr)\\lambda_1",
        ),
    }

    for relative_path, required_forms in required_by_file.items():
        squashed = read_squashed(relative_path)
        for required in required_forms:
            assert required in squashed


def test_active_examples_have_no_bare_genus_one_obstruction_slogan():
    combined = "\n".join((ROOT / path).read_text() for path in TARGET_FILES)

    stale_forms = (
        "\\operatorname{Obs}^{\\mathrm{def}}_1",
        "\\mathrm{obs}_1 = \\kappa \\cdot \\lambda_1",
        "\\mathrm{obs}_1 = \\kappa\\cdot\\lambda_1",
        "\\mathrm{obs}_1 = \\kappa\n\\cdot \\lambda_1",
        "\\mathrm{obs}_1=\\kappa\\lambda_1",
        "\\mathrm{obs}_1 = \\kappa",
    )
    for stale in stale_forms:
        assert stale not in combined
