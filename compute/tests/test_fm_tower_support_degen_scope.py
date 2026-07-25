"""Guards for the Theorem-H FM-tower degeneration mechanism."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CHIRAL_HOCHSCHILD = ROOT / "chapters/theory/chiral_hochschild_koszul.tex"


def visible(path: Path) -> str:
    text = path.read_text()
    return "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("%")
    )


def proposition_block() -> str:
    text = visible(CHIRAL_HOCHSCHILD)
    label = text.index(r"\label{prop:fm-tower-collapse}")
    start = text.rindex(r"\begin{proposition}", 0, label)
    end = text.index(r"\begin{remark}[PBW, bar concentration", start)
    return text[start:end]


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


class TestFMTowerSupportDegenerationScope:
    def test_proposition_is_named_by_collision_depth_support(self):
        block = proposition_block()
        assert "Configuration-space collapse by collision-depth\nsupport" in block
        assert "Fulton--MacPherson!collision-depth spectral sequence" in block
        assert "FM-formality spectral sequence" not in block
        assert "Fulton--MacPherson!formality spectral sequence" not in block

    def test_formality_is_only_constant_fibre_input(self):
        block = proposition_block()
        flat = normalized(block)
        assert "Constant-fibre Arnold algebra" in block
        assert "This is only the constant-fibre input" in flat
        assert "not a degeneration argument for the coefficient-coupled" in flat
        assert "It does not control the OPE-coupled differentials" in flat
        assert "there are no higher chain-level corrections" not in flat
        assert "Formality" not in block

    def test_e2_degenerates_by_row_support_not_purity(self):
        block = proposition_block()
        flat = normalized(block)
        assert "Higher differentials vanish for support reasons" in block
        assert r"d_m \colon E_m^{r,s} \to E_m^{r+m,\,s-m+1}" in block
        assert "source or target vanishes" in flat
        assert "with no appeal to formality or weight purity" in flat
        assert "Deligne strictness" not in flat
        assert "pure mixed Hodge" not in flat
