from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

THEOREM_D_SUMMARY_FILES = (
    "chapters/connections/master_reconstruction.tex",
    "chapters/theory/chiral_climax_platonic.tex",
)


def read_compact(relative_path: str) -> str:
    return "".join((ROOT / relative_path).read_text().split())


def test_active_theorem_d_summaries_separate_the_four_typed_lanes():
    required_by_file = {
        "chapters/connections/master_reconstruction.tex": (
            r"\operatorname{Obs}^{\mathrm{def}}_g(A_b)\in"
            r"H^2\!\left(\Def_g(A_b)\right)",
            r"\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_{1,1}(A)"
            r"=\kappa(A)\lambda_1",
            r"\mathfrakO^K_{g,n}(A)=\kappa(A)\lambda_{-1}(\mathbbE_g)",
            r"\operatorname{obs}^{\mathrm{Hdg}}_{g,n}(A)="
            r"\operatorname{ch}_g\!\left(\mathfrakO^K_{g,n}(A)\right)="
            r"(-1)^g\kappa(A)\lambda_g",
            r"F_{g,n}=F^{\mathrm{sc}}_{g,n}+\deltaF^{\mathrm{cross}}_{g,n}",
        ),
        "chapters/theory/chiral_climax_platonic.tex": (
            r"\operatorname{Obs}^{\mathrm{def}}_g(\cA)\in"
            r"H^2\!\left(\Def_g(\cA)\right)",
            r"\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_{1,1}(\cA)="
            r"\kappa(\cA)\lambda_1",
            r"\mathfrakO_g^K(\cA)=\kappa(\cA)\lambda_{-1}(\mathbbE_g)",
            r"\operatorname{ch}_g\!\left(\mathfrakO_g^K(\cA)\right)="
            r"(-1)^g\kappa(\cA)\lambda_g",
            r"F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}"
            r"+\deltaF_g^{\mathrm{cross}}(\cA)",
        ),
    }

    for relative_path, required_forms in required_by_file.items():
        compact = read_compact(relative_path)
        for required in required_forms:
            assert required in compact


def test_active_theorem_d_summaries_name_each_comparison_package():
    for path in THEOREM_D_SUMMARY_FILES:
        compact = read_compact(path)
        for package in (
            r"H_D^1",
            r"H_D^K",
            r"H_D^{\mathrm{tr}}",
            r"H_D^{\mathrm{graph}}",
        ):
            assert package in compact


def test_active_theorem_d_summaries_retire_the_unsigned_identification():
    combined = "".join(read_compact(path) for path in THEOREM_D_SUMMARY_FILES)

    stale_forms = (
        r"\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g",
        r"\mathrm{obs}_g(A_b)=\kappa(A_b)\lambda_g",
        r"\operatorname{Obs}^{\mathrm{def}}_g(\cA)="
        r"\kappa(\cA)\lambda_g",
        r"\operatorname{Obs}^{\mathrm{def}}_g(A_b)="
        r"\kappa(A_b)\lambda_g",
    )
    for stale in stale_forms:
        assert stale not in combined
