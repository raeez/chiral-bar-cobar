"""Surface guards for non-principal DS and AGT comparison scope.

These tests protect the status split harvested from the external review:
AGT is comparison evidence, DS is a filtered functor on primitive triples,
and Bershadsky--Polyakov same-family duality requires the subregular
DS--bar transport package.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GENUS_TEX = ROOT / "chapters" / "examples" / "genus_expansions.tex"
W_ALGEBRAS_TEX = ROOT / "chapters" / "examples" / "w_algebras.tex"
SURVEY_TEX = ROOT / "standalone" / "survey_track_a_compressed.tex"
FOURTEEN_TEX = ROOT / "standalone" / "koszulness_fourteen_characterizations.tex"
SUBREGULAR_TEX = ROOT / "chapters" / "connections" / "subregular_hook_frontier.tex"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _normalized(path: Path) -> str:
    return " ".join(_text(path).split())


def test_genus_expansion_does_not_make_ds_preservation_unconditional():
    genus = _text(GENUS_TEX)
    normalized = _normalized(GENUS_TEX)

    assert "On the principal generic lane" in genus
    assert "only after the DS--bar exchange and scalar-normalization hypotheses" in genus
    assert "subregular DS--bar transport package" in genus
    assert (
        "DS reduction is a filtered functor on primitive triples, "
        "not an equality of all structures"
    ) in normalized
    assert "DS reduction preserves both the discriminant" not in genus


def test_agt_surface_is_external_comparison_not_koszul_proof():
    w_alg = _text(W_ALGEBRAS_TEX)
    normalized = _normalized(W_ALGEBRAS_TEX)

    assert "The AGT comparison is external evidence" in w_alg
    assert "it is not a proof of chiral Koszul duality" in w_alg
    assert "H_{\\mathrm{AGT\\text{-}shadow}}" in w_alg
    assert "not a proof of Koszul duality" in normalized
    assert (
        "does not identify a Drinfeld--Sokolov reduction with a bar "
        "construction outside the stated DS--bar exchange hypotheses"
    ) in normalized
    assert "non\\text{-}principal\\ same\\text{-}family\\ duality" in w_alg
    assert "subregular\\ DS\\text{-}bar\\ transport" in w_alg

    forbidden = [
        "W-algebra Koszul duality corresponds to S-duality in the gauge theory",
        "Part of the MC2 theorem package",
        "The entire Koszul pair",
        "The non-scalar all-weight contribution is exactly the cross-channel term",
        "AGT proves Koszul duality",
    ]
    for phrase in forbidden:
        assert phrase not in normalized


def test_bp_standalone_surfaces_keep_same_family_duality_conditional():
    survey = _text(SURVEY_TEX)
    survey_norm = _normalized(SURVEY_TEX)
    fourteen = _text(FOURTEEN_TEX)
    fourteen_norm = _normalized(FOURTEEN_TEX)

    assert "proved canonical strictness and computed" in survey_norm
    assert "conditional output of the subregular DS--bar transport package" in survey_norm
    assert "not a consequence of DS reduction alone" in survey_norm
    assert "all-orbit Koszul-duality transport remains conditional" in survey_norm

    assert "The stronger assertion that this diagonal Ext condition is transported" in fourteen
    assert "conditional on the subregular DS--bar transport package" in fourteen_norm
    assert "DS reduction is a filtered functor on primitive triples" in fourteen_norm
    assert "level-shifted same-family duality remains conditional" in fourteen_norm

    forbidden = [
        "Bershadsky--Polyakov algebra $\\mathrm{BP}_k$ is chirally Koszul "
        "at generic level",
        "Koszulness is established through Ext diagonal vanishing",
        "nonvanishing at generic level gives diagonal concentration",
    ]
    for phrase in forbidden:
        assert phrase not in survey_norm
        assert phrase not in fourteen_norm


def test_rectangular_sl4_keeps_scalar_and_categorical_questions_separate():
    subregular = _text(SUBREGULAR_TEX)
    normalized = _normalized(SUBREGULAR_TEX)

    assert "The Kazhdan--Li theorem supplies the Slodowy associated graded" in normalized
    assert "H_{\\mathrm{PBW}}^{\\mathrm{bar}}" in subregular
    assert "modular characteristic requires a separate genus-$1$" in normalized
    assert "rectangular DS--bar/Verdier exchange package" in normalized
    assert "companion is open" in normalized
    assert "KSDual membership is a further fixed-point statement" in normalized

    forbidden = [
        "c(k) + c(k^\\vee) = 14",
        "\\kappa(k) + \\kappa(k^\\vee) = 70",
        "c(k) + c(k^\\vee) = 110",
        "\\kappa(k) + \\kappa(k^\\vee) = 550",
        "\\kappa(k) = 5c(k)",
        "DS--KD commutation is \\textsc{proved} for $(2,2)$ by self-duality",
        "self-transpose structure forces the intertwining diagram to commute",
    ]
    for phrase in forbidden:
        assert phrase not in subregular
