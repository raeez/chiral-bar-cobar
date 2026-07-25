"""Guards for based and unbased comparison of bar models."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/bar_construction.tex"


def test_based_comparison_lives_in_the_slice_over_the_fixed_bar_object():
    compact = "".join(SOURCE.read_text().split())
    start = compact.index(r"\begin{proposition}[Basedcomparisonofbarmodels;")
    end = compact.index(r"\end{proposition}", start)
    block = compact[start:end]
    for token in (
        r"\ClaimStatusProvedHere",
        r"u_i\colonB_i\xrightarrow{\;\sim\;}\mathcalB_X(\cA)",
        r"\mathsf{dgCoalg}_{X,/\mathcalB_X(\cA)}",
        "contractible",
    ):
        assert token in block


def test_unbased_comparison_records_the_automorphism_torsor():
    compact = "".join(SOURCE.read_text().split())
    assert r"\operatorname{Aut}(\mathcalB_X(\cA))" in compact
    assert "unbasedcomparisonisachoiceinthecorrespondingautomorphismtorsor" in compact
    assert "connectedbyacontractiblespaceofquasi-isomorphisms" not in compact

