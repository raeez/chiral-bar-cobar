from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_ising_scalar_free_energy_uses_typed_virasoro_characteristic():
    text = (ROOT / "chapters/examples/minimal_model_examples.tex").read_text()
    squashed = " ".join(text.split())

    required_forms = (
        "The scalar uniform-weight amplitudes",
        (
            "F_g^{\\mathrm{sc}}(\\mathrm{Ising}) "
            "=\\kappa^{\\mathrm{Vir}}(\\mathrm{Vir}_{1/2}) "
            "\\lambda_g^{\\mathrm{FP}}"
        ),
        "The scalar-level free energies are",
        (
            "F_g^{\\mathrm{sc}}(\\mathrm{Ising}) "
            "=\\kappa^{\\mathrm{Vir}}(\\mathrm{Vir}_{1/2}) "
            "\\lambda_g^{\\mathrm{FP}} =\\frac14\\,\\lambda_g^{\\mathrm{FP}}"
        ),
        "$g$ & $\\lambda_g^{\\mathrm{FP}}$ & $F_g^{\\mathrm{sc}}(\\mathrm{Ising})$",
        "the full amplitude receives corrections from higher degrees",
        (
            "The Virasoro minimal-model characteristic is "
            "\\(\\kappa^{\\mathrm{Vir}}(\\mathrm{Vir}_{1/2})=1/4\\). "
            "The scalar uniform-weight coefficient is therefore"
        ),
    )
    for required in required_forms:
        assert required in squashed

    stale_forms = (
        "F_g(\\mathrm{Ising}) = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "F_g = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "at $\\kappa = 1/4$ are",
        "F_g = (1/4) \\cdot \\lambda_g^{\\mathrm{FP}}",
        "$g$ & $\\lambda_g^{\\mathrm{FP}}$ & $F_g(\\mathrm{Ising})$",
        "The individual genus-$g$ amplitudes",
    )
    for stale in stale_forms:
        assert stale not in squashed
