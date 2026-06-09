from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

TARGET_FILES = (
    "appendices/type_system.tex",
    "chapters/connections/master_reconstruction.tex",
    "chapters/theory/theorem_A_infinity_2.tex",
    "chapters/theory/chiral_climax_platonic.tex",
    "chapters/theory/mc5_class_m_chain_level_platonic.tex",
)


def read_squashed(relative_path: str) -> str:
    return " ".join((ROOT / relative_path).read_text().split())


def test_active_theory_summaries_type_obstruction_characteristic():
    required_by_file = {
        "appendices/type_system.tex": (
            "\\mathrm{obs}_g(\\Ab)=\\kappa(\\Ab)\\lambda_g",
        ),
        "chapters/connections/master_reconstruction.tex": (
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
        ),
        "chapters/theory/theorem_A_infinity_2.tex": (
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
        ),
        "chapters/theory/chiral_climax_platonic.tex": (
            "\\mathrm{obs}_g(\\cA)=\\kappa(\\cA)\\lambda_g",
            (
                "F_g(\\cA)=F_g^{\\mathrm{sc}}(\\cA)"
                " +\\delta F_g^{\\mathrm{cross}}(\\cA)"
            ),
            "F_g^{\\mathrm{sc}}(\\cA)=\\kappa(\\cA)\\lambda_g^{\\mathrm{FP}}",
        ),
        "chapters/theory/mc5_class_m_chain_level_platonic.tex": (
            (
                "\\mathrm{obs}_2(\\mathbf H_{\\Delta_5}) "
                "=\\kappa_{\\mathrm{ch}}(\\mathbf H_{\\Delta_5})\\lambda_2"
            ),
            (
                "\\mathrm{ob}_{\\mathrm{form}}|_{H_n} =c_n="
                "\\kappa_{\\mathrm{ch}}(\\mathbf H_{\\Delta_5})"
                "\\lambda_2|_{H_n}"
            ),
        ),
    }

    for relative_path, required_forms in required_by_file.items():
        squashed = read_squashed(relative_path)
        for required in required_forms:
            assert required in squashed


def test_active_theory_summaries_have_no_bare_obstruction_slogans():
    combined = "\n".join((ROOT / path).read_text() for path in TARGET_FILES)

    stale_forms = (
        "\\mathrm{obs}_g=\\kappa\\cdot\\lambda_g",
        "\\mathrm{obs}_g=\\kappa\\lambda_g",
        "\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g",
        "\\mathrm{obs}_g = \\kappa\\lambda_g",
        "F_g=\\kappa\\lambda_g^{\\mathrm{FP}}",
        "F_g=\\kappa\\cdot\\lambda_g^{\\mathrm{FP}}",
        "F_g = \\kappa\\lambda_g^{\\mathrm{FP}}",
        "F_g = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
    )
    for stale in stale_forms:
        assert stale not in combined
