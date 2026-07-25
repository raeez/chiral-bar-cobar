"""Guards for conformal-block / pointed-bar comparison scope."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CHIRAL_MODULES = ROOT / "chapters" / "theory" / "chiral_modules.tex"
CONFIG_SPACES = ROOT / "chapters" / "theory" / "configuration_spaces.tex"
KAC_MOODY = ROOT / "chapters" / "examples" / "kac_moody.tex"
THEOREM_C = ROOT / "chapters" / "theory" / "theorem_C_refinements_platonic.tex"
ENGINE = ROOT / "compute" / "lib" / "conformal_blocks_bar_identification_engine.py"
ENGINE_TEST = ROOT / "compute" / "tests" / "test_conformal_blocks_bar_identification_engine.py"
THEOREM_INDEX = ROOT / "standalone" / "theorem_index.tex"
THEOREM_REGISTRY = ROOT / "metadata" / "theorem_registry.md"
CLAIMS = ROOT / "metadata" / "claims.jsonl"
LABEL_INDEX = ROOT / "metadata" / "label_index.json"
DEPENDENCY_GRAPH = ROOT / "metadata" / "dependency_graph.dot"
ANTIPATTERNS = ROOT / "notes" / "antipatterns_catalogue.md"
FIRST_PRINCIPLES_CACHE = ROOT / "notes" / "first_principles_cache_comprehensive.md"


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def window_after_label(path: Path, label: str, lines: int) -> str:
    text = visible(path)
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    return "\n".join(text.split(anchor, 1)[1].splitlines()[:lines])


def window_around_label(path: Path, label: str, before: int, after: int) -> str:
    text = visible(path)
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    prefix, suffix = text.split(anchor, 1)
    return "\n".join(prefix.splitlines()[-before:] + [anchor] + suffix.splitlines()[:after])


class TestConformalBlockBarComparisonScope:
    def test_pointed_bar_proposition_is_conditional_derived_coinvariants(self):
        window = normalized(
            window_around_label(CHIRAL_MODULES, "prop:conformal-blocks-bar", 4, 75)
        )
        for fragment in (
            "\\ClaimStatusConditional",
            "Type signature:",
            "derived coinvariant complex",
            "finite-rank conformal-block comparison",
            "classical conformal blocks requires an additional comparison theorem",
            "higher derived coinvariants need not vanish",
        ):
            assert fragment in window

        for fragment in (
            "ClaimStatusProvedHere",
            "the space of conformal blocks is computed by the bar complex",
            "complex computes the derived conformal blocks",
        ):
            assert fragment not in window

    def test_kzb_and_verlinde_surfaces_are_comparison_gated(self):
        kzb = normalized(
            window_around_label(CHIRAL_MODULES, "prop:kzb-bar-complex", 4, 85)
        )
        for fragment in (
            "\\ClaimStatusConditional",
            "derived coinvariant complex",
            "determinant-anomaly matching",
            "projectivised or anomaly-cancelled",
            "ordinary conformal-block bundle inherits only projectively flat transport",
        ):
            assert fragment in kzb

        verlinde = normalized(
            window_around_label(CHIRAL_MODULES, "thm:verlinde-bar", 4, 95)
        )
        for fragment in (
            "\\ClaimStatusConditional",
            "TUY/Hitchin conformal-block target with pointed-bar comparison",
            "pointed-bar comparison package",
            "Koszul property is not by itself a proof",
            "finite-rank comparison, sewing, and anomaly hypotheses",
        ):
            assert fragment in verlinde

        for fragment in (
            "Verlinde formula via the bar complex",
            "The Koszul property ensures that the bar spectral sequence degenerates",
        ):
            assert fragment not in verlinde

    def test_punctured_and_kac_moody_duplicates_are_synced(self):
        punctured = normalized(
            window_around_label(CONFIG_SPACES, "cor:conformal-blocks-punctured-bar", 4, 55)
        )
        for fragment in (
            "Punctured bar coinvariants and conformal-block comparison",
            "\\ClaimStatusConditional",
            "derived coinvariant complex",
            "conformal-block comparison for the inserted modules",
        ):
            assert fragment in punctured
        assert "recovers the space of conformal blocks" not in punctured

        kac = normalized(
            window_around_label(KAC_MOODY, "thm:bar-verlinde-recovery", 4, 95)
        )
        for fragment in (
            "\\ClaimStatusConditional",
            "Kac--Moody TUY target with pointed-bar comparison",
            "S_{0,\\lambda}^{\\,2-2g}",
            "Z_0(\\mathfrak g,k)=1",
            "unitarity of the first row",
        ):
            assert fragment in kac
        assert "\\frac{S_{0,\\lambda}}{S_{0,0}}" not in kac

        example = normalized(window_after_label(KAC_MOODY, "ex:conformal-blocks-sl2", 80))
        assert "no second non-negative integrable-level Verlinde category" in example
        assert "when both levels are non-negative integers" not in example

    def test_theorem_c_and_compute_docs_keep_comparison_language(self):
        theorem_c = normalized(visible(THEOREM_C))
        for fragment in (
            "Under the comparison package of Proposition~\\ref{prop:conformal-blocks-bar}",
            "degreewise-finiteness, exactness, and conformal-block comparison hypotheses",
        ):
            assert fragment in theorem_c

        compute_text = normalized(ENGINE.read_text() + "\n" + ENGINE_TEST.read_text())
        for fragment in (
            "pointed-bar exactness, TUY/Hitchin comparison, sewing, and anomaly matching",
            "derived coinvariant H^0",
            "Expected pointed-bar H^0 dimension on the comparison lane",
            "Verlinde dimensions and pointed-bar comparison targets",
        ):
            assert fragment in compute_text

        for fragment in (
            "Conformal blocks as bar cohomology",
            "conformal blocks = bar cohomology identification",
            "bar H^0 = conformal blocks",
        ):
            assert fragment not in compute_text

    def test_index_metadata_and_active_notes_are_synced_to_comparison_gate(self):
        index = normalized(THEOREM_INDEX.read_text())
        for fragment in (
            "prop:conformal-blocks-bar & Pointed bar resolution and conformal-block comparison",
            "prop:kzb-bar-complex & KZB comparison from the pointed bar family",
            "thm:verlinde-bar & Verlinde formula on the TUY target and pointed-bar comparison",
            "cor:conformal-blocks-punctured-bar & Punctured bar coinvariants and conformal-block comparison",
            "thm:bar-verlinde-recovery & Verlinde recovery through the Kac--Moody pointed-bar comparison",
        ):
            assert fragment in index

        registry = normalized(THEOREM_REGISTRY.read_text())
        for fragment in (
            "This registry now tracks every `\\ClaimStatusProvedHere` and `\\ClaimStatusProvedElsewhere`",
            "| `Conditional` | 1785 |",
        ):
            assert fragment in registry
        for fragment in (
            "prop:conformal-blocks-bar",
            "prop:kzb-bar-complex",
            "thm:verlinde-bar",
            "cor:conformal-blocks-punctured-bar",
            "thm:bar-verlinde-recovery",
            "Pointed bar resolution and conformal-block comparison",
            "KZB comparison from the pointed bar family",
            "Verlinde formula on the TUY target and pointed-bar comparison",
            "Punctured bar coinvariants and conformal-block comparison",
            "Verlinde recovery through the Kac--Moody pointed-bar comparison",
        ):
            assert fragment not in registry

        claims = normalized(CLAIMS.read_text())
        for fragment in (
            '"label": "prop:conformal-blocks-bar", "env_type": "proposition", "status": "Conditional"',
            '"line": 704, "title": "Pointed bar resolution and conformal-block comparison"',
            '"label": "prop:kzb-bar-complex", "env_type": "proposition", "status": "Conditional"',
            '"line": 1036, "title": "KZB comparison from the pointed bar family"',
            '"label": "thm:verlinde-bar", "env_type": "theorem", "status": "Conditional"',
            '"line": 1110, "title": "Verlinde formula on the TUY target and pointed-bar\\ncomparison',
            '"label": "cor:conformal-blocks-punctured-bar", "env_type": "corollary", "status": "Conditional"',
            '"line": 2030, "title": "Punctured bar coinvariants and conformal-block comparison"',
            '"label": "thm:bar-verlinde-recovery", "env_type": "theorem", "status": "Conditional"',
            '"line": 4027, "title": "Verlinde recovery through the Kac--Moody pointed-bar\\ncomparison"',
        ):
            assert fragment in claims

        label_index = LABEL_INDEX.read_text()
        for fragment in (
            '"line": 704',
            '"line": 1036',
            '"line": 1110',
            '"line": 2030',
            '"line": 4027',
            '"chapters/theory/chiral_modules.tex#proposition:1034:10"',
            '"chapters/theory/chiral_modules.tex#theorem:1108:11"',
            '"chapters/examples/kac_moody.tex#theorem:4025:39"',
        ):
            assert fragment in label_index

        graph = DEPENDENCY_GRAPH.read_text()
        for fragment in (
            "prop:conformal-blocks-bar\\\\nproposition [Co]",
            "chapters/theory/chiral_modules.tex:704",
            "chapters/theory/chiral_modules.tex#proposition:1034:10",
            "chapters/theory/chiral_modules.tex#theorem:1108:11",
            "chapters/examples/kac_moody.tex#theorem:4025:39",
            "chapters/theory/configuration_spaces.tex:2030",
            "Punctured bar coinvariants and conformal",
        ):
            assert fragment in graph

        active_notes = normalized(
            ANTIPATTERNS.read_text() + "\n" + FIRST_PRINCIPLES_CACHE.read_text()
        )
        for fragment in (
            "pointed-bar/conformal-block comparison package",
            "Pointed bar complexes compute derived coinvariants",
            "classical conformal blocks require degreewise finite holonomic pointed bar terms",
            "identifying its \\(H^0\\) with classical conformal blocks is conditional",
        ):
            assert fragment in active_notes

        synced_surfaces = "\n".join(
            path.read_text()
            for path in (
                THEOREM_INDEX,
                THEOREM_REGISTRY,
                CLAIMS,
                LABEL_INDEX,
                DEPENDENCY_GRAPH,
                ANTIPATTERNS,
                FIRST_PRINCIPLES_CACHE,
            )
        )
        for fragment in (
            "Conformal blocks via the bar complex",
            "KZB connection from the bar complex",
            "Verlinde formula via the bar complex",
            "Conformal blocks from punctured bar complex",
            "Verlinde recovery from the bar complex",
            "Vol-I bar-complex identification of conformal blocks",
            "to identify $H^0$ with finite-rank TUY conformal blocks",
            "chiral_modules.tex:540",
            "chiral_modules.tex:541-554",
            "4007:39",
            "1000:10",
            "1064:11",
        ):
            assert fragment not in synced_surfaces
