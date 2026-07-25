"""Guards for Theorem D curved-chain versus scalar-shadow discipline."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIVE_THEOREMS = ROOT / "standalone/five_theorems_modular_koszul.tex"
PROGRAMME = ROOT / "standalone/programme_summary.tex"
PROGRAMME_2_4 = ROOT / "standalone/programme_summary_sections2_4.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def _compact(path: Path) -> str:
    return "".join(path.read_text().split())


def test_five_theorems_d_names_four_typed_realizations():
    text = _text(FIVE_THEOREMS)
    required = [
        r"m_1^2=[m_0,-]",
        r"\operatorname{Obs}^{\mathrm{def}}_g(\cA) \in H^2(\mathrm{Def}_g(\cA))",
        r"\mathrm{Def}_{1,1}(\cA)",
        r"\operatorname{Obs}^{\mathrm{def}}_{1,1}(\cA) \in H^2(\mathrm{Def}_{1,1}(\cA))",
        r"\operatorname{tr}_1 \operatorname{Obs}^{\mathrm{def}}_{1,1}(\cA) =\kappa(\cA)\lambda_1",
        r"\mathfrak O_g^K(\cA) =\kappa(\cA)\lambda_{-1}(\mathbb E_g)",
        r"\operatorname{obs}^{\mathrm{Hdg}}_g(\cA) =(-1)^g\kappa(\cA)\lambda_g",
        r"F_g(\cA) =\kappa(\cA)\lambda_g^{\mathrm{FP}} +\delta F_g^{\mathrm{cross}}(\cA)",
        r"H_D=(H_D^1,H_D^K,H_D^{\mathrm{tr}},H_D^{\mathrm{graph}})",
    ]
    for fragment in required:
        assert fragment in text


def test_programme_summaries_separate_deformation_k_hodge_and_graph_stages():
    for path in (PROGRAMME, PROGRAMME_2_4):
        text = _compact(path)
        required = [
            r"\operatorname{Obs}^{\mathrm{def}}_g(\cA)\in"
            r"H^2(\operatorname{Def}_g(\cA))",
            r"H_D^1",
            r"\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_{1,1}(\cA)="
            r"\kappa(\cA)\lambda_1",
            r"H_D^K",
            r"\mathfrakO_g^K(\cA)=\kappa(\cA)\lambda_{-1}(\mathbbE_g)",
            r"\operatorname{ch}_g(\mathfrakO_g^K(\cA))="
            r"(-1)^g\kappa(\cA)\lambda_g",
            r"H_D^{\mathrm{tr}}",
            r"H_D^{\mathrm{graph}}",
            r"F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}"
            r"+\deltaF_g^{\mathrm{cross}}(\cA)",
        ]
        for fragment in required:
            assert fragment in text, f"{fragment!r} missing from {path}"


def test_old_theorem_d_global_single_number_language_does_not_return():
    forbidden = [
        r"Theorem D: genus universality $\mathrm{obs}_g = \kappa \cdot \lambda_g$",
        "The universality is the point: no matter how complicated the OPE structure, the genus tower is controlled by a single number",
    ]
    for path in (FIVE_THEOREMS, PROGRAMME, PROGRAMME_2_4):
        text = _text(path)
        for fragment in forbidden:
            assert fragment not in text, f"retired fragment {fragment!r} still in {path}"


def test_harvest_matrix_records_theorem_d_local_pass():
    text = _text(MATRIX)
    assert "G Theorem D / modular tower" in text
    assert "Pass 508" in text
    assert "applied for local theorem-surface harvest" in text
