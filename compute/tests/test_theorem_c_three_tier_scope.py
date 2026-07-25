"""Guards for Theorem C C0/C1/C2 theorem-surface discipline."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CLAUDE = ROOT / "CLAUDE.md"
PROGRAMME = ROOT / "standalone/programme_summary.tex"
PROGRAMME_2_4 = ROOT / "standalone/programme_summary_sections2_4.tex"
FIVE_THEOREMS = ROOT / "standalone/five_theorems_modular_koszul.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"
THEOREM_C = ROOT / "chapters/theory/theorem_C_refinements_platonic.tex"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_claude_theorem_c_row_names_c0_c1_c2_and_scalar_shadow():
    text = _text(CLAUDE)
    required = [
        r"**C**",
        "C0 identifies the degree-zero strict-flat fibre with the ordinary centre local system",
        r"$\mathbf C_g(A_b)=R\Gamma(\overline{\mathcal M}_g,\mathcal Z(A_b))$",
        r"a supplied brace comparison $\iota_Z^{\mathrm{der}}$ connects the Theorem H derived centre",
        r"scalar ceiling $K^\kappa(A_b)=\kappa(A_b)+\kappa^!_{\mathrm{alg}}(A_b)$ is the normalized trace shadow",
        "normalized trace shadow of C1 together with Theorem D",
        "C2 is the separate shifted-symplectic upgrade",
        "strict-flat centre-local-system cohomology, then modular trace per stratum",
        "C2 shifted-symplectic/BV package when explicitly supplied",
        r"algebra-level Verdier sum distinct from $\mathcal N(A_b)$",
    ]
    for fragment in required:
        assert fragment in text

    assert r"**C** | $K^\kappa(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{alg}}(A_b)$ in family-stratum ceiling" not in text


def test_programme_summaries_state_theorem_c_three_tiers():
    for path in (PROGRAMME, PROGRAMME_2_4):
        text = _text(path)
        required = [
            "Theorem~C has three typed tiers",
            r"\textsc{C0}",
            r"\textsc{C1}",
            r"\textsc{C2}",
            "cohomological degree $-(3g-3)$",
            "uniform-weight scalar trace shadow of C1 together with Theorem~D",
            "not the C2 shifted-symplectic upgrade",
            "BV/QME anomaly-killing inputs",
        ]
        for fragment in required:
            assert fragment in text, f"{fragment!r} missing from {path}"


def test_five_theorems_statement_names_c0_c1_c2_hypotheses():
    text = _text(FIVE_THEOREMS)
    required = [
        "Theorem~C has three typed tiers",
        "strict flat fibre--centre comparison",
        "A represented Verdier involution, perfectness, and a nondegenerate anti-invariant pairing",
        "A shifted-symplectic/BV package upgrades the represented eigenspaces",
        "The scalar relation belongs to the trace realization of \\textsc{C1} together with Theorem~D",
        "The shifted-symplectic assertion belongs to \\textsc{C2}",
        "the BV Laplacian, the QME anomaly class, and a chosen null-homotopy",
    ]
    for fragment in required:
        assert fragment in text


def test_old_theorem_c_overstatements_do_not_return():
    forbidden = [
        "The eigenspace decomposition (C1) is unconditional",
        r"are Lagrangian for the $(-1)$-shifted symplectic pairing",
        r"on each summand (C2) requires the uniform-weight hypothesis",
        r"the ambient complex carries a $(2 - d)$-shifted symplectic",
        r"class~$\mathsf{M}$ boundary-stratum perfectness is the open conjecture",
    ]

    for path in (PROGRAMME, PROGRAMME_2_4, FIVE_THEOREMS):
        text = _text(path)
        for fragment in forbidden:
            assert fragment not in text, f"retired fragment {fragment!r} still in {path}"


def test_harvest_matrix_records_theorem_c_local_pass():
    text = _text(MATRIX)
    assert "F Theorem C / derived centre" in text
    assert "Pass 507" in text
    assert "Pass 512" in text
    assert "applied for local theorem-surface harvest" in text


def test_theorem_c_scalar_and_mukai_surfaces_are_typed():
    text = _text(THEOREM_C)
    required = [
        r"\{0,13,250/3\}",
        "Fehily--Kawasetsu--Ridout's bosonic conformal presentation",
        r"c_{\mathrm{BP}}(k)+ c_{\mathrm{BP}}(-k-6)=50",
        r"\kappa_{\mathrm{BP}}=c_{\mathrm{BP}}/6\Rightarrow K^\kappa_{\mathrm{BP}}=25/3",
        "open genus-one obligation",
        r"H_{\mathsf B}:=(H_{\mathrm{chart}},H_{\mathrm{KD}}, H_{\mathrm{scalar}},H_{\mathrm{mod}},H_{\mathrm{quant}})",
        r"2c_+(\mathrm{Mukai}(K3))=8",
        r"\ClaimStatusConjectured{} arithmetic candidate",
        r"\cite[Lemma~5.1]{Bruinier2002}",
        r"N'=\operatorname{lcm}(N,8)",
        "root-of-unity construction takes the root order as input",
    ]
    for fragment in required:
        assert fragment in text

    assert "98/3" not in text
    assert r"\frac16\cdot 196" not in text
    assert r"\{0,13,25/3,250/3\}" not in text


def test_theorem_c_active_prose_uses_positive_type_signatures():
    text = _text(THEOREM_C)
    for word in (
        " must not ",
        " does not ",
        " do not ",
        " cannot ",
        " without ",
        " lacks ",
        " no finite-type ",
    ):
        assert word not in f" {text} "
