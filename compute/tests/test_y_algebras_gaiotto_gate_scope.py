"""Guards for the Gaiotto gate on Y-algebra surfaces."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
Y_CHAPTER = ROOT / "chapters/examples/y_algebras.tex"
W_DEEP = ROOT / "chapters/examples/w_algebras_deep.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"


def visible(path: Path) -> str:
    return "\n".join(
        line for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def assert_anchor(text: str, anchor: str) -> None:
    assert compact(anchor) in compact(text), anchor


def window(text: str, start: str, end: str | None = None) -> str:
    start_index = text.index(start)
    if end is None:
        return text[start_index:]
    return text[start_index:text.index(end, start_index)]


class TestYAlgebrasGaiottoGateScope:
    def test_y_chapter_names_junction_data_before_theorem_table(self):
        text = visible(Y_CHAPTER)
        for anchor in (
            "Gaiotto--Rap\\v{c}\\'ak junction datum",
            "\\(\\Omega\\)-background parameters",
            "\\eqref{eq:y-omega-params}",
            "boundary labels\n\\(\\mathrm{GL}(N_1),\\mathrm{GL}(N_2),\\mathrm{GL}(N_3)\\)",
            "Algebraic\nBRST/truncation statements, chiral Koszul statements, and physical\nbulk",
            "a named comparison package is supplied",
        ):
            assert_anchor(text, anchor)

    def test_y_dual_surface_is_conditional_verdier_branched(self):
        text = visible(Y_CHAPTER)
        dual = window(
            text,
            "\\begin{proposition}[{Verdier/BRST comparison",
            "\\end{proof}",
        )
        for anchor in (
            "\\ClaimStatusConditional",
            "assume the package \\(H_Y^\\vee\\)",
            "Gaiotto--Rap\\v{c}\\'ak junction datum",
            "\\(\\Omega\\)-background",
            "\\mathrm{GL}(N_i)\\) boundary labels",
            "PBW chiral\nKoszulness",
            "convergence of the\nVerdier-dual completed bar construction",
            "BRST/DS comparison",
            "K_X\\!\\left(Y_{N_1,N_2,N_3}[\\Psi]\\right)",
            "\\mathbb D_{\\Ran}\\Bbarch_X\\!\\left(Y_{N_1,N_2,N_3}[\\Psi]\\right)",
            "formality/minimal-model\ncomparison",
            "not, by itself, the Feigin--Frenkel centre\ntheorem",
            "not bar--cobar inversion",
            "bar--cobar counit itself reconstructs",
            "it does not construct the dual",
        ):
            assert_anchor(dual, anchor)

        retired = (
            "\\ClaimStatusProvedHere",
            "The Feigin--Frenkel involution $\\Psi \\mapsto -\\Psi$",
            "is Verdier duality on the bar coalgebra",
            "Feigin--Frenkel involution of the parent superalgebra",
            "bar of the Feigin--Frenkel\ndual",
        )
        for fragment in retired:
            assert fragment not in dual

    def test_y_central_charge_surface_is_truncation_lane_not_physical_voa(self):
        text = visible(Y_CHAPTER)
        theorem = window(
            text,
            "\\begin{theorem}[{Truncation-lane central-charge scalar",
            "\\end{proof}",
        )
        for anchor in (
            "\\ClaimStatusConditional",
            "scalar attached here to the \\(\\cW_{1+\\infty}\\)-truncation lane",
            "not asserted to be the physical VOA central charge after BRST\nreduction",
            "decoupled \\(U(1)\\)-normalisation",
            "normalisation-comparison package",
            "typed as a truncation-lane scalar",
        ):
            assert_anchor(theorem, anchor)
        assert "\\ClaimStatusProvedHere" not in theorem
        assert "central charge of $Y_{N_1,N_2,N_3}[\\Psi]$ is" not in theorem

    def test_y_summary_tables_and_junction_remark_keep_conditional_lane(self):
        text = visible(Y_CHAPTER)
        for anchor in (
            "Five-theorem status table for $Y_{N_1,N_2,N_3}[\\Psi]$",
            "A (Verdier branch)",
            "\\(K_X(Y_{N_1,N_2,N_3}[\\Psi])\\simeq\n Y_{N_1,N_2,N_3}[-\\Psi]\\) only under \\(H_Y^\\vee\\)",
            "Conditional & Thm~\\ref{thm:bar-cobar-verdier}",
            "$\\Omega(\\barB(Y[\\Psi])) \\xrightarrow{\\sim}\n Y[\\Psi]$\n & Conditional",
            "For \\(Y_{1,1,1}\\),\n \\(\\kappa(\\Psi)+\\kappa(-\\Psi)=0\\); general \\(Y\\)-channel\n complementarity requires \\(H_Y^\\vee\\)",
            "$\\kappa = \\sum_i \\kappa_i$ (channel-by-channel) under the\n channel-decomposition package\n & Conditional",
            "Conditional Verdier/BRST companion",
            "\\(K_X(Y[\\Psi])\\simeq Y[-\\Psi]\\), not a bare\n parameter reflection",
            "conditional parameter-reflected dual-companion lane",
            "and, under \\(H_Y^\\vee\\)",
            "\\(K_X(A)\\simeq Y_{N_1,N_2,N_3}[-\\Psi]\\)",
            "conditional homotopy Koszul-dual companion",
        ):
            assert_anchor(text, anchor)

        for fragment in (
            "Feigin--Frenkel involution on~$\\Psi$",
            "The Koszul duality $\\Psi \\mapsto -\\Psi$ has no real",
            "$A^! = Y_{N_1,N_2,N_3}[-\\Psi]$: the boundary and its\n Koszul dual",
        ):
            assert fragment not in text

    def test_w_algebras_deep_y_section_uses_parameter_reflected_companion(self):
        text = visible(W_DEEP)
        section = window(
            text,
            "\\section{Gaiotto--Rap\\v{c}\\'ak corner VOAs and chiral Koszulness}",
            "\\begin{remark}[Shadow depth classification]",
        )
        for anchor in (
            "Parameter-reflected BRST companion",
            "Gaiotto--Rap\\v{c}\\'ak \\(\\Omega\\)-background and boundary labels",
            "\\item \\emph{Koszul duality} \\textup{(}conditional\\textup{)}",
            "the Verdier/BRST comparison\npackage identifying the homotopy Koszul dual",
            "reflected BRST lane",
        ):
            assert_anchor(section, anchor)
        for fragment in (
            "Feigin--Frenkel duality",
            "the Koszul dual is the FF-dual",
        ):
            assert fragment not in section

    def test_review_harvest_records_y_algebra_gaiotto_gate_pass(self):
        for text in (MATRIX.read_text(), LEDGER.read_text()):
            normalized = compact(text)
            assert "Pass 548" in text
            assert "Y-algebra Gaiotto gate" in normalized
