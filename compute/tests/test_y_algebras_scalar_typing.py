from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_y111_genus_tower_types_kappa_source_and_fp_coefficient():
    text = (ROOT / "chapters/examples/y_algebras.tex").read_text()
    squashed = " ".join(text.split())

    required_forms = (
        "F_1(Y_{1,1,1}[\\Psi]) = \\kappa(Y_{1,1,1}[\\Psi])/24",
        "\\kappa(Y_{1,1,1}[\\Psi]) = \\Psi",
        "\\kappa(Y_{1,1,1}[\\Psi]) \\cdot \\lambda_g^{\\mathrm{FP}}",
        "\\delta F_g^{\\mathrm{cross}}(Y_{1,1,1}[\\Psi])",
        (
            "\\lambda_g^{\\mathrm{FP}} "
            "=\\int_{\\overline{\\cM}_{g,1}}\\psi_1^{2g-2}\\lambda_g"
        ),
        "\\kappa(Y_{1,1,1}[\\Psi])=\\Psi",
        "controlling the genus tower in the trivalent case",
        "\\kappa(A) \\cdot \\omega_g",
    )
    for required in required_forms:
        assert required in squashed

    stale_forms = (
        "F_g(Y_{1,1,1}) = \\Psi \\cdot \\lambda_g^{\\mathrm{FP}}",
        "$F_1 = \\kappa/24$ unconditionally",
        "F_g = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}} + \\delta",
        "F_g = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}} = \\Psi",
        "intersection numbers on~$\\overline{\\cM}_g$",
        "with $\\kappa = \\Psi$ (for $Y_{1,1,1}$) controlling",
    )
    for stale in stale_forms:
        assert stale not in squashed
