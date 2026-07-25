from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read_compact() -> str:
    path = ROOT / "chapters/connections/grand_unification_platonic.tex"
    return "".join(path.read_text().split())


def test_grand_unification_types_the_four_theorem_d_lanes():
    compact = read_compact()

    required_forms = (
        r"\operatorname{Obs}^{\mathrm{def}}_g(\cA)\inH^2(\Def_g(\cA))",
        r"\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_{1,1}="
        r"\kappa\lambda_1",
        r"\mathfrakO_g^K=\kappa\lambda_{-1}(\mathbbE_g)",
        r"\operatorname{ch}_g(\mathfrakO_g^K)=(-1)^g\kappa\lambda_g",
        r"F_g(\cA)=F_g^{\mathrm{sc}}(\cA)"
        r"+\deltaF_g^{\mathrm{cross}}(\cA)",
        r"F_g^{\mathrm{sc}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
    )
    for required in required_forms:
        assert required in compact

    for package in (
        r"H_D^1",
        r"H_D^K",
        r"H_D^{\mathrm{tr}}",
        r"H_D^{\mathrm{graph}}",
    ):
        assert package in compact


def test_grand_unification_retains_the_signed_hodge_character():
    compact = read_compact()

    assert (
        r"\mathfrakO_g^K(\cA)=\kappa(\cA)\lambda_{-1}(\mathbbE_g),"
        r"\qquad\operatorname{ch}_g\!\left(\mathfrakO_g^K(\cA)\right)="
        r"(-1)^g\kappa(\cA)\lambda_g"
    ) in compact


def test_grand_unification_retires_unsigned_obstruction_slogans():
    compact = read_compact()

    stale_forms = (
        r"\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g",
        r"\operatorname{Obs}^{\mathrm{def}}_g(\cA)="
        r"\kappa(\cA)\lambda_g",
        "obstruction-toweruniversality",
    )
    for stale in stale_forms:
        assert stale not in compact
