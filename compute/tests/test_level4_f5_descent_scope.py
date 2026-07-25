"""Type and status guards for the represented genus-one F5 class."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/connections/vertical_equivalence_level_4.tex"
FRONTIER = ROOT / "FRONTIER.md"
OPEN_TOWER = ROOT / "chapters/frame/open_beilinson_tower_platonic.tex"
GUIDE = ROOT / "chapters/frame/guide_to_main_results.tex"
INTRODUCTION = ROOT / "chapters/theory/introduction.tex"


def _compact() -> str:
    return "".join(SOURCE.read_text().split())


def _flat(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_f5_theorem_uses_a_represented_chain_map_and_deformation_target():
    text = _compact()
    for token in (
        r"H_{\mathrm{F5}}^{\mathrm{desc}}(\cA)",
        r"\rho_\cA",
        r"\gamma_\cA\colon",
        r"\Theta_{\mathrm{F5},\cA}",
        r"\Def_{\mathrm{KZB}}^\bullet(\rho_\cA)",
        r"\Def_{\mathrm{double}}^\bullet(\cA)",
        r"H^2(\Theta_{\mathrm{F5},\cA})",
        r"H^2(\gamma_\cA)",
    ):
        assert token in text


def test_level4_vertical_names_the_boundary_action_comparison():
    text = _compact()
    for token in (
        r"H_4^{\mathrm{vert}}=(\mathrm{H1})$--$(\mathrm{H7})",
        r"\Xi_4\colon",
        r"\Hbar^{\mathrm{line}}_\cC",
        r"\mathrm{LineMod}\!\left(D(\Yplus(X))\right)",
        r"Hypothesis~\textup{(H7)}",
    ):
        assert token in text


def test_primary_sources_supply_the_kzb_connection_and_associator_torsor():
    text = _compact()
    assert r"Calaque--Enriquez--Etingof~\cite{CEE09}" in text
    assert r"Enriquez~\cite{Enriquez14}" in text


def test_shadow_depth_statement_has_conjectural_status():
    text = _compact()
    start = text.index(r"\begin{conjecture}[Shadow-depthdetection")
    end = text.index(r"\end{conjecture}", start)
    block = text[start:end]
    assert r"\ClaimStatusConjectured" in block
    assert r"\rmax(\cA)=2" in block


def test_f5_source_uses_family_chain_data_for_the_proposed_comparison():
    text = _compact()
    assert r"dh_\cA+h_\cAd=\nu_\cA(\mathrm{id}-\iota_\cAp_\cA)" in text
    assert r"h_\cA=h_{\mathrm{LV}}/" not in text
    assert "uniquenon-trivialclass" not in text


def test_frontier_records_the_f5_statement_as_a_represented_conjecture():
    text = "".join(FRONTIER.read_text().split())
    assert r"\Theta_{\mathrm{F5},A}" in text
    assert "conj:level-4-F5-shadow-depth" in text
    assert r"**vanishesiff$r_{\max}(A)=2$**" not in text


def test_summary_surfaces_use_the_represented_f5_class():
    required = (
        r"H_{\mathrm{F5}}^{\mathrm{desc}}(\cA)",
        r"\Theta_{\mathrm{F5},\cA}",
        r"H^2(\Theta_{\mathrm{F5},\cA})",
        r"[\omega_{\mathrm{KZB}}(\rho_\cA)]",
        r"Conjecture~\ref{conj:level-4-F5-shadow-depth}",
    )
    for path in (OPEN_TOWER, GUIDE, INTRODUCTION):
        text = _flat(path)
        for fragment in required:
            assert fragment in text, f"{fragment!r} missing from {path}"


def test_summary_surfaces_assign_shadow_depth_to_the_conjecture():
    retired = (
        r"\mathrm{obs}^{(1)}_{\mathrm{double}}\in H^2",
        r"\emph{vanishes iff} $r_{\max}(\cA)=2$",
        r"vanishing iff $r_{\max}(\cA)=2$",
    )
    for path in (OPEN_TOWER, GUIDE, INTRODUCTION):
        text = _flat(path)
        for fragment in retired:
            assert fragment not in text, f"{fragment!r} occurs in {path}"
