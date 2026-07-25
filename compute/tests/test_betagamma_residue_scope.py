"""Guardrails for the beta-gamma residue convention.

The raw beta-gamma OPE contraction is nonzero.  In the manuscript's
pole-valued collision r-matrix convention, the dlog bar kernel absorbs
the simple pole, so r_coll vanishes.  The regular ordered contact
operator remains nonzero and carries the class-C contact datum.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

SURFACES = [
    ROOT / "chapters/examples/beta_gamma.tex",
    ROOT / "chapters/examples/free_fields.tex",
    ROOT / "chapters/connections/genus1_seven_faces.tex",
    ROOT / "appendices/ordered_associative_chiral_kd.tex",
    ROOT / "standalone/seven_faces.tex",
]


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def assert_anchor(text: str, anchor: str) -> None:
    assert compact(anchor) in compact(text), anchor


def test_retired_unqualified_binary_residue_zero_phrases_are_absent():
    combined = "\n".join(visible(path) for path in SURFACES)
    retired = (
        "The binary collision residue of the $\\beta\\gamma$ system is zero",
        "collision residue $r(z)$ of $\\Theta_{\\beta\\gamma}$ is\nzero",
        "$r$-matrix} & $r(z) = 0$ (simple pole absorbed by $d\\log$ extraction)",
        "the ordered binary residue is zero",
        "the raw OPE contraction vanishes",
    )
    for fragment in retired:
        assert compact(fragment) not in compact(combined), fragment


def test_canonical_beta_gamma_surface_separates_ope_r_coll_and_contact():
    text = visible(ROOT / "chapters/examples/beta_gamma.tex")
    for anchor in (
        "\\beta(z)\\gamma(w) \\;\\sim\\; \\frac{1}{z-w}",
        "the $d\\log$\nbar kernel lowers the pole-valued collision residue to\n$k_{\\max}=0$",
        "regular contact\noperator $\\Theta^{\\mathrm{ord}}_{\\beta\\gamma}",
        "this is not a pole-valued collision residue",
        "still has $r^{\\mathrm{coll}}_{\\beta\\gamma}(z)=0$ after the $d\\log$\nabsorption convention",
        "All mixed types have nontrivial bar differential",
    ):
        assert_anchor(text, anchor)


def test_summary_surfaces_name_nonzero_ope_and_zero_pole_valued_r_coll():
    free_fields = visible(ROOT / "chapters/examples/free_fields.tex")
    for anchor in (
        "Its raw ordered OPE contraction is nonzero",
        "\\beta(z)\\gamma(w)\\sim (z-w)^{-1}",
        "the \\(d\\log\\)-bar\nkernel absorbs this simple pole",
        "\\(r^{\\mathrm{coll}}_{\\beta\\gamma}(z)=0\\)",
        "the separate regular contact operator",
    ):
        assert_anchor(free_fields, anchor)

    genus1 = visible(ROOT / "chapters/connections/genus1_seven_faces.tex")
    for anchor in (
        "genus-$0$ \\emph{pole-valued} collision \\(r\\)-matrix vanishes",
        "This does not say that the\nordered binary OPE contraction vanishes",
        "\\beta(z)\\gamma(w)\\sim (z-w)^{-1}",
        "simple pole is absorbed by the \\(d\\log\\)-bar kernel",
        "regular\ncontact transport",
        "remains the nonzero class-\\(C\\) contact datum",
    ):
        assert_anchor(genus1, anchor)

    seven = visible(ROOT / "standalone/seven_faces.tex")
    for anchor in (
        "pole-valued collision \\(r_{\\mathrm{coll}}\\)",
        "zero after \\(d\\log\\)-absorption",
        "raw\nordered contraction \\(\\beta(z)\\gamma(w)\\sim(z-w)^{-1}\\) is nonzero",
        "regular contact transport",
        "is the surviving ordered datum",
    ):
        assert_anchor(seven, anchor)


def test_ordered_associative_surface_keeps_augmented_residue_and_contact_separate():
    text = visible(ROOT / "appendices/ordered_associative_chiral_kd.tex")
    for anchor in (
        "every collision residue $\\pm 1$ lies in $\\bC\\cdot 1$,\nwhich the augmentation kills",
        "pole-valued residue is zero\nbecause the simple pole is absorbed by the $d\\log$ kernel",
        "Contact\ntransport terminates at linear order because $\\Theta^2=0$",
        "\\Theta_{\\beta\\gamma}",
    ):
        assert_anchor(text, anchor)
