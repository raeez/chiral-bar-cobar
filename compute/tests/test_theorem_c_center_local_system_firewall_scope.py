"""Semantic guards for the Theorem C / Theorem H object firewall."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "chapters/theory/higher_genus_complementarity.tex"
SCALAR = ROOT / "chapters/theory/chiral_center_theorem.tex"
HDM = ROOT / "chapters/connections/holographic_datum_master.tex"
OPEN_TOWER = ROOT / "chapters/frame/open_beilinson_tower_platonic.tex"

SURFACES = (
    ROOT / "main.tex",
    ROOT / "CLAUDE.md",
    ROOT / "chapters/frame/guide_to_main_results.tex",
    ROOT / "chapters/frame/open_beilinson_tower_platonic.tex",
    ROOT / "chapters/theory/introduction.tex",
    ROOT / "chapters/theory/chiral_climax_platonic.tex",
    ROOT / "chapters/theory/bar_cobar_adjunction_inversion.tex",
    ROOT / "chapters/theory/hochschild_cohomology.tex",
    ROOT / "chapters/connections/entanglement_modular_koszul.tex",
    ROOT / "chapters/connections/grand_unification_platonic.tex",
    ROOT / "chapters/connections/holographic_datum_master.tex",
    ROOT / "chapters/connections/master_concordance.tex",
    ROOT / "chapters/theory/poincare_duality_quantum.tex",
    ROOT / "chapters/theory/three_hochschild_unification_platonic.tex",
    ROOT / "chapters/theory/ftm_seven_fold_tfae_platonic.tex",
)


def _flat(path: Path) -> str:
    return re.sub(r"\s+", " ", path.read_text())


def _environment(path: Path, label: str, environment: str) -> str:
    source = path.read_text()
    label_at = source.index(rf"\label{{{label}}}")
    start = source.rindex(rf"\begin{{{environment}}}", 0, label_at)
    end = source.index(rf"\end{{{environment}}}", label_at)
    return re.sub(r"\s+", " ", source[start:end])


def test_canonical_surface_separates_theorem_c_from_theorem_h():
    text = _flat(CANONICAL)
    required = (
        r"\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))",
        r"Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) =\ChirHoch^\bullet(\cA,\cA)",
        r"\iota_Z^{\mathrm{der}}\colon Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal A)",
        r"\iota_Z := H^0(\iota_Z^{\mathrm{der}})",
        "ordinary flat fiber--center identification",
        r"K^\kappa(\cA) :=",
        r"= \kappa(\cA)+\kappa(\cA^!)",
    )
    for fragment in required:
        assert fragment in text


def test_propagated_surfaces_use_centre_local_system_language():
    retired = (
        "Theorem~C is derived-centre complementarity",
        "Theorem~C: derived-centre complementarity",
        "Theorem~C controls the chiral derived centre",
        "Theorem~C governs the chiral derived centre",
        "Theorem~C studies the derived centre",
        "Vol~I Theorem~C (derived-centre complementarity)",
    )
    for path in SURFACES:
        text = _flat(path)
        for phrase in retired:
            assert phrase not in text, f"{phrase!r} occurs in {path}"


def test_scalar_theorem_has_a_level_five_semantic_label():
    theorem = _environment(SCALAR, "thm:scalar-trace-complementarity", "theorem")
    assert "Computed and open scalar complementarity lanes" in theorem
    assert r"Beilinson level \(5\)" in theorem
    assert r"K^\kappa(A,A^!)" in theorem
    assert "sum of the two normalized Theorem~D trace outputs on the C1 eigensummands" in theorem
    assert r"\label{thm:derived-centre-complementarity-strengthened}" in theorem
    assert "Normalized scalar traces of Theorem~C eigensummands" in _flat(SCALAR)


def test_canonicity_is_relative_to_the_displayed_enhanced_data():
    text = _flat(CANONICAL)
    required = (
        "canonical relative to the displayed strict flat representative",
        r"centre comparison~$\iota_Z$",
        r"represented involution~$\sigma$",
        "Contractibility of the comparison space",
        "remains an open problem",
        "contractible comparison space for the enhanced triples",
        "is an open construction problem",
    )
    for fragment in required:
        assert fragment in text


def test_holographic_bucket_records_computed_and_candidate_statuses():
    remark = _environment(HDM, "rem:holo-master-theoremC-bucket", "remark")
    assert r"\{0,\;13,\;250/3\}" in remark
    assert r"K^c_{\mathrm{BP}}=50" in remark
    assert "$25/3$ awaits the genus-one curvature comparison" in remark
    assert r"2c_+(\mathrm{II}_{4,20})=8" in remark
    assert r"is conjectural under $H_{\mathsf B}$" in remark
    assert "98/3" not in remark


def test_open_tower_uses_the_scaled_deformation_retract_identity():
    text = _flat(OPEN_TOWER)
    required = (
        r"C_F=\Omega_X^{\mathrm{ch}}B_X^{\mathrm{ch}}(A_F)",
        r"p_F\colon C_F\to A_F",
        r"d_Fh_F+h_Fd_F =\nu_F(\mathrm{id}_{C_F}-\iota_Fp_F)",
        r"$\nu_F^{-1}h_F$ is a contracting homotopy",
        r"$\nu_F=K^\kappa(A_F)$ requires the additional chain map",
        "deformation retract to the scalar trace complex",
        r"Theorem~C acts on $R\Gamma(\overline{\mathcal M}_g,\mathcal Z(A_F))$",
        "Theorem~D supplies its normalized scalar trace",
    )
    for fragment in required:
        assert fragment in text
    assert r"K^2(\cA)\simeq\cA" not in text
    assert r"h_\cA = h_{\mathrm{LV}}/\mathcal N(\cA)" not in text
