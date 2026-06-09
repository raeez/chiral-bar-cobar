from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_genus_complete_heisenberg_chern_weil_types_scalar_projection():
    text = (ROOT / "chapters/connections/genus_complete.tex").read_text()
    squashed = " ".join(text.split())

    required_forms = (
        (
            "\\operatorname{tr}(\\Theta_{\\mathcal{H}}) "
            "= \\sum_{g \\geq 1} "
            "\\kappa(\\mathcal{H}_\\kappa)\\lambda_g^{\\mathrm{FP}}"
        ),
        "The genus tower is determined by the scalar characteristic",
        (
            "\\(\\kappa(\\mathcal{H}_\\kappa)\\), which evaluates "
            "to the level \\(\\kappa\\)"
        ),
        (
            "Chern--Weil projection is a function of the single level "
            "parameter \\(\\kappa\\) alone"
        ),
        "while the scalar projection itself factors through the typed characteristic",
        (
            "F_g^{\\mathrm{sc}}(\\mathcal H_\\kappa) "
            "= \\kappa(\\mathcal H_\\kappa)\\lambda_g^{\\mathrm{FP}}"
        ),
        "$\\delta F_g^{\\mathrm{cross}}=0$",
        "$\\Delta(x) = 1 - \\kappa x$",
        "$r_{\\mathcal{H}}(z)=\\kappa/z$",
    )
    for required in required_forms:
        assert required in squashed

    stale_forms = (
        "\\sum_{g \\geq 1} \\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "The genus tower is determined by \\kappa alone",
        "F_g = \\kappa\\lambda_g^{\\mathrm{FP}}",
        "Chern--Weil projection is a function of the single scalar $\\kappa$ alone",
    )
    for stale in stale_forms:
        assert stale not in squashed
