from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_grand_unification_types_obstruction_and_cross_channel_scalar_lane():
    text = (ROOT / "chapters/connections/grand_unification_platonic.tex").read_text()
    squashed = " ".join(text.split())

    required_forms = (
        "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
        (
            "F_g(\\cA) =F_g^{\\mathrm{sc}}(\\cA)"
            "+\\delta F_g^{\\mathrm{cross}}(\\cA), \\qquad "
            "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)"
            "\\lambda_g^{\\mathrm{FP}}"
        ),
        (
            "Theorem~D (obstruction-tower universality "
            "$\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g$)"
        ),
        (
            "F_g(\\cA)=F_g^{\\mathrm{sc}}(\\cA) "
            "+\\delta F_g^{\\mathrm{cross}}(\\cA), \\qquad "
            "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)"
            "\\lambda_g^{\\mathrm{FP}}"
        ),
        (
            "Theorem~D ($\\mathrm{obs}_g(\\cA)="
            "\\kappa(\\cA)\\lambda_g$)"
        ),
    )
    for required in required_forms:
        assert required in squashed

    stale_forms = (
        "$\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g$",
        "$\\mathrm{obs}_g = \\kappa \\lambda_g$",
        "F_g = \\kappa\\lambda_g^{\\mathrm{FP}}",
        "F_g = \\kappa\\lambda_g^{\\mathrm{FP}} + \\delta F_g^{\\mathrm{cross}}",
        "Theorem~D ($\\mathrm{obs}_g = \\kappa \\lambda_g$)",
    )
    for stale in stale_forms:
        assert stale not in squashed
