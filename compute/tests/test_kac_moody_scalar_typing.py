from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_kac_moody_higher_genus_obstruction_uses_typed_characteristic():
    text = (ROOT / "chapters/examples/kac_moody.tex").read_text()
    squashed = " ".join(text.split())

    required_forms = (
        (
            "\\kappa(\\widehat{\\fg}_k) = "
            "\\dim(\\fg)(k + h^\\vee)/(2h^\\vee)"
        ),
        (
            "\\(\\mathrm{obs}_g(\\widehat{\\fg}_k) "
            "=\\kappa(\\widehat{\\fg}_k)\\lambda_g\\) "
            "for every $g \\geq 1$"
        ),
        (
            "\\(\\kappa(\\widehat{\\fg}_k) "
            "+\\kappa(\\widehat{\\fg}_{-k-2h^\\vee})=0\\)"
        ),
    )
    for required in required_forms:
        assert required in squashed

    stale_forms = (
        "\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g",
        "$\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g$",
        "\\kappa + \\kappa' = 0 for affine Kac--Moody",
    )
    for stale in stale_forms:
        assert stale not in squashed
