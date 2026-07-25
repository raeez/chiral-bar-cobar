"""Claim-surface guards for Open obstruction and comparison nodes."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
BAR_CURVED = ROOT / "chapters/theory/bar_cobar_adjunction_curved.tex"
CHIRAL_CLIMAX = ROOT / "chapters/theory/chiral_climax_platonic.tex"
THEOREM_B_SCOPE = ROOT / "chapters/theory/theorem_B_scope_platonic.tex"
MC5 = ROOT / "chapters/theory/mc5_class_m_chain_level_platonic.tex"
E1_MODULAR = ROOT / "chapters/theory/e1_modular_koszul.tex"

H1 = "lem:cclimax-H1-failure"
H3 = "lem:cclimax-H3-failure"
H4 = "lem:cclimax-H4-failure"
LIM1 = "thm:tbsp-lim1-is-fourier-coefficient"
WALL = "thm:wall-of-walls-obstruction"


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def environment_block(path: Path, label: str, environment: str) -> str:
    text = visible(path)
    marker = rf"\label{{{label}}}"
    label_pos = text.index(marker)
    start = text.rfind(rf"\begin{{{environment}}}", 0, label_pos)
    end_marker = rf"\end{{{environment}}}"
    end = text.index(end_marker, label_pos) + len(end_marker)
    return text[start:end]


def reference_windows(path: Path, label: str, radius: int = 240) -> list[str]:
    text = visible(path)
    marker = rf"\ref{{{label}}}"
    windows = []
    start = 0
    while True:
        pos = text.find(marker, start)
        if pos < 0:
            break
        windows.append(normalized(text[max(0, pos - radius):pos + radius]))
        start = pos + len(marker)
    return windows


class TestOpenDependencyClaimSurface:
    def test_open_source_blocks_remain_obligational(self):
        for label in (H1, H3, H4):
            block = normalized(environment_block(CHIRAL_CLIMAX, label, "lemma"))
            assert r"\ClaimStatusOpen" in block
            assert "requires" in block

        wall = normalized(environment_block(THEOREM_B_SCOPE, WALL, "theorem"))
        assert r"\ClaimStatusOpen" in wall
        assert "Construction of this comparison remains an open obligation" in wall

        lim1 = normalized(environment_block(THEOREM_B_SCOPE, LIM1, "theorem"))
        assert r"\ClaimStatusOpen" in lim1
        assert "requires a filtered comparison" in lim1
        assert "becomes a theorem after that comparison is constructed" in lim1

    def test_humbert_consumers_make_the_open_data_antecedent_explicit(self):
        text = normalized(visible(BAR_CURVED))
        for phrase in (
            "conditional on the nearby-cycle, deformation-class, and descent data required by Open Lemmas",
            "requires the three comparison packages formulated in Open Lemmas",
            "constructions formulated in Open Lemmas",
        ):
            assert phrase in text

        for phrase in (
            rf"Lemma~\ref{{{H1}}} shows it fails only at",
            rf"Lemma~\ref{{{H3}}} is non-zero only at",
            "recovering the three obstruction classes of Lemmas",
            "direct computation at each leading wall",
        ):
            assert phrase not in text

        for label in (H1, H3, H4):
            windows = reference_windows(BAR_CURVED, label)
            assert windows
            for window in windows:
                assert "Open" in window
                assert "comparison" in window or "required" in window

    def test_fourier_to_milnor_identification_is_a_conditional_comparison(self):
        text = normalized(visible(BAR_CURVED))
        for phrase in (
            rf"Assume additionally the filtered automorphic-to-bar comparison required by Open Theorem~\ref{{{LIM1}}}",
            "The displayed identity is the conditional output of the comparison required by Open Theorem",
            "whose construction is the content of Open Theorem",
            "If the direct normalized Jacobi-coefficient calculation gives",
        ):
            assert phrase in text

        assert rf"By Theorem~\ref{{{LIM1}}}, this class equals" not in text
        for window in reference_windows(BAR_CURVED, LIM1):
            assert "Open" in window
            assert "comparison" in window

    def test_wall_of_walls_consumers_preserve_the_abstract_cech_target(self):
        mc5 = normalized(visible(MC5))
        e1 = normalized(visible(E1_MODULAR))

        for phrase in (
            rf"Open Theorem~\textup{{\ref{{{WALL}}}}} places its \v Cech class in the derived endomorphism complex",
            rf"Open Theorem~\textup{{\ref{{{WALL}}}}} defines an abstract \v Cech class",
        ):
            assert phrase in mc5
        assert "Under the monodromy-to-derived-endomorphism comparison required there" in mc5

        assert rf"Open Theorem~\textup{{\ref{{{WALL}}}}} defines the Vol~I \v Cech class" in e1
        assert "Conditional on the monodromy comparison required there" in e1

        for phrase in (
            rf"the commutator class of Theorem~\textup{{\ref{{{WALL}}}}} obstructs",
            rf"Theorem~\textup{{\ref{{{WALL}}}}} reads, in the coarser",
            "The wall-of-walls obstruction theorem of Vol~I",
        ):
            assert phrase not in mc5 + " " + e1

        for path in (MC5, E1_MODULAR):
            for window in reference_windows(path, WALL):
                assert "Open" in window
                assert "comparison" in window or "derived endomorphism" in window
